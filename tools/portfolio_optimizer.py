#!/usr/bin/env python3
"""
Portfolio Optimizer - Portfolio-level E[CAGR] calculator + deployment/rotation simulator.

Converts abstract cash drag into concrete deployment decisions with numbers.
All output is RAW DATA. No buy/sell recommendations.

Modes:
  python3 tools/portfolio_optimizer.py                # Portfolio E[CAGR] breakdown
  python3 tools/portfolio_optimizer.py --deploy       # Simulate deploying cash into pipeline candidates
  python3 tools/portfolio_optimizer.py --rotate       # Simulate rotation (sell weak + buy strong)
  python3 tools/portfolio_optimizer.py --cash-drag    # Cash drag analysis at different levels
  python3 tools/portfolio_optimizer.py --all          # All modes combined

E[CAGR] = (FV/Price)^(1/3) - 1 + Sustainable_Growth + Dividend_Yield
Cash E[CAGR] = 0% (actual cost = benchmark opportunity cost ~8%/yr)
"""

import sys
import os
import re
import argparse
import yaml
import yfinance as yf
import warnings
warnings.filterwarnings('ignore')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORTFOLIO_FILE = os.path.join(BASE_DIR, 'portfolio', 'current.yaml')
UNIVERSE_FILE = os.path.join(BASE_DIR, 'state', 'quality_universe.yaml')
THESIS_ACTIVE_DIR = os.path.join(BASE_DIR, 'thesis', 'active')
THESIS_RESEARCH_DIR = os.path.join(BASE_DIR, 'thesis', 'research')

# Default deployment amount for simulation
DEFAULT_DEPLOY_EUR = 500
# Assumed benchmark annual return for cash drag calculation
BENCHMARK_ANNUAL_RETURN = 0.08


def load_yaml(path):
    """Load a YAML file. Returns None on error."""
    try:
        with open(path, 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"ERROR loading {path}: {e}")
        return None


def get_fx_rates():
    """Get EUR/USD, GBP/EUR, and DKK/EUR exchange rates with fallbacks."""
    defaults = {'EURUSD': 1.04, 'GBPEUR': 1.19, 'DKKEUR': 0.134}
    fallbacks_used = []
    rates = {}

    for pair, yf_ticker, default in [
        ('EURUSD', 'EURUSD=X', defaults['EURUSD']),
        ('GBPEUR', 'GBPEUR=X', defaults['GBPEUR']),
        ('DKKEUR', 'DKKEUR=X', defaults['DKKEUR']),
    ]:
        try:
            val = yf.Ticker(yf_ticker).info.get('previousClose')
            if not val:
                val = default
                fallbacks_used.append(f"{pair}={val}")
        except Exception:
            val = default
            fallbacks_used.append(f"{pair}={val}")
        rates[pair] = val

    if fallbacks_used:
        print(f"FX WARNING: Using static fallback rates ({', '.join(fallbacks_used)}). Values may be inaccurate.")

    return rates['EURUSD'], rates['GBPEUR'], rates['DKKEUR']


def to_eur(amount_usd, eurusd):
    """Convert USD amount to EUR."""
    if eurusd and eurusd > 0:
        return amount_usd / eurusd
    return amount_usd


def normalize_gbp_currency(ticker, currency):
    """
    Normalize GBP -> GBp for LSE tickers (.L suffix).
    LSE stocks trade in pence (GBp). The quality_universe.yaml sometimes stores
    currency as 'GBP' when fair values are actually in pence. yfinance always
    reports .L tickers as GBp. This normalizer ensures consistency.
    """
    if ticker.endswith('.L') and currency == 'GBP':
        return 'GBp'
    return currency


def price_to_eur(price, currency, eurusd, gbpeur, dkkeur):
    """Convert a price in any supported currency to EUR."""
    if currency == 'EUR':
        return price
    elif currency == 'USD':
        return price / eurusd if eurusd else price
    elif currency in ('GBp', 'GBX'):
        return (price / 100) * gbpeur
    elif currency == 'GBP':
        return price * gbpeur
    elif currency == 'DKK':
        return price * dkkeur
    elif currency == 'SEK':
        return price * 0.088  # Static fallback
    return price


def parse_fv_from_portfolio(fv_string):
    """
    Parse fair_value string from portfolio/current.yaml.
    Formats: "EUR 35.00 (...)", "$191 (...)", "190 GBp (...)", "580 GBp (...)",
             "$390 (...)", "$66 (...)", "$196 (...)", "$195 (...)", "345 GBp (...)"

    Returns (value, currency) or (None, None).
    """
    if not fv_string or not isinstance(fv_string, str):
        return None, None

    # Try EUR format: "EUR 35.00" or "EUR 29.0"
    m = re.search(r'EUR\s+([0-9,]+(?:\.\d+)?)', fv_string)
    if m:
        return float(m.group(1).replace(',', '')), 'EUR'

    # Try USD format: "$191" or "$390" or "$66"
    m = re.search(r'\$\s*([0-9,]+(?:\.\d+)?)', fv_string)
    if m:
        return float(m.group(1).replace(',', '')), 'USD'

    # Try GBp format: "190 GBp" or "580 GBp" or "345 GBp"
    m = re.search(r'([0-9,]+(?:\.\d+)?)\s*GBp', fv_string)
    if m:
        return float(m.group(1).replace(',', '')), 'GBp'

    # Try DKK format: "DKK 850"
    m = re.search(r'DKK\s+([0-9,]+(?:\.\d+)?)', fv_string)
    if m:
        return float(m.group(1).replace(',', '')), 'DKK'

    # Try plain number (assume same currency as stock)
    m = re.match(r'^([0-9,]+(?:\.\d+)?)', fv_string.strip())
    if m:
        val = float(m.group(1).replace(',', ''))
        # Check suffix for pence
        if fv_string.strip().endswith('p'):
            return val, 'GBp'
        return val, None  # Currency unknown

    return None, None


def convert_fv_to_eur(fv, fv_currency, eurusd, gbpeur, dkkeur):
    """Convert a fair value to EUR."""
    return price_to_eur(fv, fv_currency or 'USD', eurusd, gbpeur, dkkeur)


def get_yf_data_batch(tickers):
    """
    Fetch yfinance data for multiple tickers.
    Returns dict of {ticker: info_dict}.
    """
    results = {}
    TICKER_MAP = {'LIGHT.NV': 'LIGHT.AS'}

    for ticker in tickers:
        yf_ticker = TICKER_MAP.get(ticker, ticker)
        try:
            info = yf.Ticker(yf_ticker).info
            if info and ('symbol' in info or 'currentPrice' in info or 'previousClose' in info):
                results[ticker] = info
        except Exception:
            pass

    return results


def get_price_from_info(info):
    """Extract current price from yfinance info dict."""
    return info.get('currentPrice') or info.get('regularMarketPrice') or info.get('previousClose')


def get_dividend_yield_pct(info):
    """
    Get dividend yield percentage from yfinance info.
    dividendYield is already in percentage form (e.g., 2.97 = 2.97%).
    """
    dy = info.get('dividendYield')
    if dy is None or not isinstance(dy, (int, float)):
        return 0.0
    return dy if dy >= 0 else 0.0


def extract_growth_from_thesis(ticker):
    """
    Extract expected growth rate from thesis file.
    Returns growth as percentage (e.g., 8.0 for 8%) or None.
    """
    for subdir in ['active', 'research']:
        thesis_path = os.path.join(BASE_DIR, 'thesis', subdir, ticker, 'thesis.md')
        if not os.path.exists(thesis_path):
            continue
        try:
            with open(thesis_path, 'r') as f:
                content = f.read()
        except Exception:
            continue

        patterns = [
            (r'Expected Growth[^:]*:\s*(?:~)?(\d+(?:\.\d+)?)\s*%', 'single'),
            (r'Revenue Growth Base:\s*(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)\s*%', 'range'),
            (r'GP Growth[^:]*:\s*(?:~)?(\d+(?:\.\d+)?)\s*%\s*\(base', 'single'),
            (r'GP CAGR[):\s]+(?:~)?(\d+(?:\.\d+)?)\s*%\s*\(base', 'single'),
            (r'Expected Growth \(GP CAGR\):\s*(\d+(?:\.\d+)?)\s*%', 'single'),
            (r'(?:Expected )?Growth:\s*(\d+(?:\.\d+)?)\s*%', 'single'),
            (r'Revenue Growth:\s*(?:~)?(\d+(?:\.\d+)?)\s*%', 'single'),
            (r'growth of\s*(?:~)?(\d+(?:\.\d+)?)\s*%', 'single'),
            (r'~?(\d+(?:\.\d+)?)\s*%\s*CAGR\s*\((?:normalized|base)', 'single'),
        ]

        for pat, pat_type in patterns:
            m = re.search(pat, content, re.IGNORECASE)
            if m:
                groups = m.groups()
                if pat_type == 'range' and len(groups) >= 2:
                    try:
                        g1 = float(groups[0])
                        g2 = float(groups[1])
                        growth = (g1 + g2) / 2
                        if -50 <= growth <= 50:
                            return growth
                    except (ValueError, TypeError):
                        continue
                else:
                    try:
                        growth = float(groups[0])
                        if -50 <= growth <= 50:
                            return growth
                    except (ValueError, TypeError):
                        continue
    return None


def compute_ecagr(fv_eur, price_eur, growth_pct, yield_pct):
    """
    Compute E[CAGR] = (FV/Price)^(1/3) - 1 + growth + div_yield

    All values in EUR for comparability.
    growth_pct and yield_pct are percentages (e.g., 8.0 for 8%).
    Returns E[CAGR] as percentage, or None.
    """
    if not fv_eur or not price_eur or price_eur <= 0 or fv_eur <= 0:
        return None

    ratio = fv_eur / price_eur
    mos_cagr = (ratio ** (1.0 / 3.0)) - 1.0
    growth_decimal = (growth_pct or 0.0) / 100.0
    div_decimal = (yield_pct or 0.0) / 100.0
    ecagr = (mos_cagr + growth_decimal + div_decimal) * 100.0
    return round(ecagr, 1)


def process_portfolio_positions(portfolio, eurusd, gbpeur, dkkeur):
    """
    Process all portfolio positions. Returns list of dicts with:
    ticker, invested_eur, value_eur, weight, fv_eur, price_eur, ecagr, growth_pct, yield_pct, contribution
    """
    positions = portfolio.get('positions', [])
    cash_eur = portfolio.get('cash', {}).get('amount', 0)

    # Collect all tickers for batch fetch
    tickers = [p['ticker'] for p in positions]
    print(f"Fetching prices for {len(tickers)} positions...")
    yf_data = get_yf_data_batch(tickers)

    results = []
    total_value_eur = 0

    for p in positions:
        ticker = p['ticker']
        shares = p.get('shares', 0)

        # Invested amount in EUR
        if 'invested_usd' in p:
            invested_eur = to_eur(p['invested_usd'], eurusd)
        elif 'invested_eur' in p:
            invested_eur = p['invested_eur']
        else:
            invested_eur = 0

        info = yf_data.get(ticker)
        if not info:
            results.append({
                'ticker': ticker, 'invested_eur': invested_eur,
                'value_eur': invested_eur, 'price_eur': None, 'fv_eur': None,
                'ecagr': None, 'growth_pct': None, 'yield_pct': None,
                'currency': '?', 'error': 'No yfinance data'
            })
            continue

        price = get_price_from_info(info)
        if price is None:
            results.append({
                'ticker': ticker, 'invested_eur': invested_eur,
                'value_eur': invested_eur, 'price_eur': None, 'fv_eur': None,
                'ecagr': None, 'growth_pct': None, 'yield_pct': None,
                'currency': '?', 'error': 'No price'
            })
            continue

        currency = info.get('currency', 'USD')
        price_eur = price_to_eur(price, currency, eurusd, gbpeur, dkkeur)
        value_eur = price_eur * shares if currency not in ('GBp', 'GBX') else price_to_eur(price * shares, currency, eurusd, gbpeur, dkkeur)

        # For GBp stocks, value = (price_in_pence * shares / 100) * gbpeur
        if currency in ('GBp', 'GBX'):
            value_eur = (price * shares / 100) * gbpeur
        else:
            value_eur = price_eur * shares

        total_value_eur += value_eur

        # Parse fair value
        fv_raw, fv_currency = parse_fv_from_portfolio(p.get('fair_value', ''))
        fv_eur = None
        if fv_raw is not None:
            # If currency unknown, assume same as stock
            if fv_currency is None:
                fv_currency = currency
            fv_eur = convert_fv_to_eur(fv_raw, fv_currency, eurusd, gbpeur, dkkeur)

        # Growth from thesis
        growth_pct = extract_growth_from_thesis(ticker)

        # Fallback to yfinance growth estimates
        if growth_pct is None:
            yf_eg = info.get('earningsGrowth')
            yf_rg = info.get('revenueGrowth')
            if yf_eg and isinstance(yf_eg, (int, float)):
                growth_pct = yf_eg * 100
            elif yf_rg and isinstance(yf_rg, (int, float)):
                growth_pct = yf_rg * 100
            else:
                growth_pct = 0.0

        # Dividend yield
        yield_pct = get_dividend_yield_pct(info)

        # E[CAGR]
        ecagr = compute_ecagr(fv_eur, price_eur, growth_pct, yield_pct)

        results.append({
            'ticker': ticker, 'invested_eur': invested_eur,
            'value_eur': value_eur, 'price_eur': price_eur,
            'fv_eur': fv_eur, 'ecagr': ecagr,
            'growth_pct': growth_pct, 'yield_pct': yield_pct,
            'currency': currency, 'error': None
        })

    # Calculate NAV and weights
    nav = total_value_eur + cash_eur
    for r in results:
        r['weight'] = (r['value_eur'] / nav * 100) if nav > 0 else 0
        r['contribution'] = (r['weight'] / 100 * (r['ecagr'] or 0))

    return results, cash_eur, nav, total_value_eur


def load_universe_candidates(eurusd, gbpeur, dkkeur):
    """
    Load pipeline candidates from quality_universe.yaml.
    Returns list of dicts with: ticker, name, qs, tier, fair_value, currency,
    entry_price, pipeline_status, direction, fv_eur, growth_pct (from thesis)
    """
    data = load_yaml(UNIVERSE_FILE)
    if not data:
        return []

    companies = data.get('quality_universe', {}).get('companies', [])
    candidates = []

    for c in companies:
        if c.get('direction', 'long') != 'long':
            continue

        # Only include candidates with fair_value and sufficient pipeline status
        fv = c.get('fair_value')
        if not fv:
            continue

        pipeline = c.get('pipeline_status', '')
        # Include R1_COMPLETE and above
        valid_statuses = {'R1_COMPLETE', 'R3_COMPLETE', 'R4_APPROVED', 'APPROVED', 'STANDING_ORDER'}
        if pipeline not in valid_statuses:
            continue

        currency = c.get('currency', 'USD')
        ticker = c['ticker']
        # Normalize GBP -> GBp for LSE tickers: FVs in universe are in pence
        currency = normalize_gbp_currency(ticker, currency)
        fv_eur = price_to_eur(fv, currency, eurusd, gbpeur, dkkeur)

        candidates.append({
            'ticker': ticker,
            'name': c.get('name', ''),
            'qs': c.get('qs_adj') or c.get('qs_tool') or 0,
            'tier': c.get('tier', '?'),
            'fair_value': fv,
            'currency': currency,
            'entry_price': c.get('entry_price'),
            'pipeline_status': pipeline,
            'fv_eur': fv_eur,
            'current_price': c.get('current_price'),
            'notes': c.get('notes', ''),
        })

    return candidates


def fetch_candidate_prices(candidates, eurusd, gbpeur, dkkeur):
    """Fetch current prices for pipeline candidates and compute E[CAGR]."""
    tickers = [c['ticker'] for c in candidates]
    print(f"Fetching prices for {len(tickers)} pipeline candidates...")
    yf_data = get_yf_data_batch(tickers)

    for c in candidates:
        info = yf_data.get(c['ticker'])
        if not info:
            c['price_eur'] = None
            c['ecagr'] = None
            c['yield_pct'] = 0.0
            c['growth_pct'] = 0.0
            continue

        price = get_price_from_info(info)
        if price is None:
            c['price_eur'] = None
            c['ecagr'] = None
            c['yield_pct'] = 0.0
            c['growth_pct'] = 0.0
            continue

        currency = info.get('currency', c['currency'])
        c['price_eur'] = price_to_eur(price, currency, eurusd, gbpeur, dkkeur)
        c['price_native'] = price
        c['yield_pct'] = get_dividend_yield_pct(info)

        # Growth from thesis
        growth = extract_growth_from_thesis(c['ticker'])
        if growth is None:
            yf_eg = info.get('earningsGrowth')
            yf_rg = info.get('revenueGrowth')
            if yf_eg and isinstance(yf_eg, (int, float)):
                growth = yf_eg * 100
            elif yf_rg and isinstance(yf_rg, (int, float)):
                growth = yf_rg * 100
            else:
                growth = 0.0
        c['growth_pct'] = growth

        c['ecagr'] = compute_ecagr(c['fv_eur'], c['price_eur'], c['growth_pct'], c['yield_pct'])


def print_portfolio_ecagr(results, cash_eur, nav, total_value_eur):
    """Print the portfolio E[CAGR] breakdown."""
    cash_weight = (cash_eur / nav * 100) if nav > 0 else 0

    print()
    print("=" * 100)
    print("PORTFOLIO E[CAGR] ANALYSIS")
    print("=" * 100)
    print(f"NAV: EUR {nav:,.0f} | Invested: EUR {total_value_eur:,.0f} ({100-cash_weight:.1f}%) | Cash: EUR {cash_eur:,.0f} ({cash_weight:.1f}%)")
    print()
    print(f"{'Ticker':<10} {'Weight':>7} {'E[CAGR]':>8} {'Contrib':>8} {'MoS%':>7} {'Grw%':>6} {'Yld%':>6} {'FV(EUR)':>10} {'Price(EUR)':>11}")
    print("-" * 100)

    # Sort by contribution descending
    sorted_results = sorted(results, key=lambda x: x.get('contribution', 0), reverse=True)

    total_contribution = 0
    for r in sorted_results:
        if r.get('error'):
            print(f"{r['ticker']:<10} {r.get('weight', 0):>6.1f}% {'ERR':>8} {'':>8} {'':>7} {'':>6} {'':>6} {'':>10} {'':>11}  {r['error']}")
            continue

        weight = r.get('weight', 0)
        ecagr = r.get('ecagr')
        contrib = r.get('contribution', 0)
        total_contribution += contrib

        fv_eur = r.get('fv_eur')
        price_eur = r.get('price_eur')

        # MoS = (FV - Price) / Price
        if fv_eur and price_eur and price_eur > 0:
            mos = ((fv_eur - price_eur) / price_eur) * 100
            mos_str = f"{mos:+.1f}"
        else:
            mos_str = 'N/A'

        ecagr_str = f"{ecagr:.1f}%" if ecagr is not None else 'N/A'
        contrib_str = f"{contrib:+.2f}%" if ecagr is not None else '-'
        grw_str = f"{r['growth_pct']:.1f}" if r.get('growth_pct') is not None else '-'
        yld_str = f"{r['yield_pct']:.1f}" if r.get('yield_pct') is not None else '-'
        fv_str = f"{fv_eur:,.1f}" if fv_eur else 'N/A'
        price_str = f"{price_eur:,.2f}" if price_eur else 'N/A'

        print(f"{r['ticker']:<10} {weight:>6.1f}% {ecagr_str:>8} {contrib_str:>8} {mos_str:>7} {grw_str:>6} {yld_str:>6} {fv_str:>10} {price_str:>11}")

    # Cash line
    cash_drag = 0  # Cash contributes 0% E[CAGR]
    print(f"{'CASH':<10} {cash_weight:>6.1f}% {'0.0%':>8} {'0.00%':>8} {'':>7} {'':>6} {'':>6} {'':>10} {'':>11}")
    print("-" * 100)

    portfolio_ecagr = total_contribution
    print(f"{'PORTFOLIO':<10} {'100.0':>6}% {portfolio_ecagr:>+7.1f}%")
    print()

    # Cash drag impact
    if cash_weight > 5:
        # What would portfolio E[CAGR] be if cash were invested at avg position E[CAGR]?
        invested_weight = 100 - cash_weight
        if invested_weight > 0:
            avg_position_ecagr = total_contribution / (invested_weight / 100)
            full_invest_ecagr = avg_position_ecagr
            drag = full_invest_ecagr - portfolio_ecagr
            print(f"CASH DRAG IMPACT:")
            print(f"  Portfolio E[CAGR]:          {portfolio_ecagr:+.1f}%")
            print(f"  Avg position E[CAGR]:       {avg_position_ecagr:+.1f}%")
            print(f"  If fully invested (same Q):  {full_invest_ecagr:+.1f}%")
            print(f"  Cash drag:                   {drag:+.1f}pp (EUR {cash_eur * drag / 100:,.0f}/yr opportunity cost)")
            print()


def print_deployment_simulation(results, cash_eur, nav, candidates, eurusd, gbpeur, dkkeur, deploy_amount=DEFAULT_DEPLOY_EUR):
    """Simulate deploying cash into pipeline candidates."""
    # Current portfolio E[CAGR]
    current_ecagr = sum(r.get('contribution', 0) for r in results)
    cash_weight = (cash_eur / nav * 100) if nav > 0 else 0

    # Filter candidates with valid E[CAGR] and positive upside
    viable = [c for c in candidates if c.get('ecagr') is not None and c['ecagr'] > 0]
    viable.sort(key=lambda x: x['ecagr'], reverse=True)

    print()
    print("=" * 115)
    print(f"DEPLOYMENT SIMULATION -- Deploy EUR {deploy_amount} from cash (EUR {cash_eur:,.0f})")
    print("=" * 115)

    if not viable:
        print("  No viable pipeline candidates with positive E[CAGR] found.")
        return

    if cash_eur < deploy_amount:
        print(f"  WARNING: Cash EUR {cash_eur:,.0f} < deployment amount EUR {deploy_amount}. Showing hypothetical results.")
        print()

    print(f"  Current Portfolio E[CAGR]: {current_ecagr:+.1f}% | Cash: EUR {cash_eur:,.0f} ({cash_weight:.1f}%)")
    print()
    print(f"{'Ticker':<10} {'QS':>3} {'Tier':>4} {'Pipeline':>15} {'E[CAGR]':>8} {'NewPfE[CAGR]':>13} {'Delta':>7} {'NewCash%':>9} {'MoS%':>7}")
    print("-" * 115)

    for c in viable[:15]:
        # Simulate: add EUR deploy_amount at current price
        new_cash = cash_eur - deploy_amount
        new_nav = nav  # NAV doesn't change, just reallocation
        new_cash_weight = (new_cash / new_nav * 100) if new_nav > 0 else 0
        deploy_weight = (deploy_amount / new_nav * 100) if new_nav > 0 else 0

        # New portfolio E[CAGR] = old contributions + new position contribution
        new_contribution = deploy_weight / 100 * c['ecagr']
        # Reduce cash contribution (was 0, still 0 but weight changed)
        new_portfolio_ecagr = current_ecagr + new_contribution
        delta = new_portfolio_ecagr - current_ecagr

        # MoS
        if c.get('fv_eur') and c.get('price_eur') and c['price_eur'] > 0:
            mos = ((c['fv_eur'] - c['price_eur']) / c['price_eur']) * 100
            mos_str = f"{mos:+.1f}"
        else:
            mos_str = 'N/A'

        ecagr_str = f"{c['ecagr']:.1f}%"
        new_ecagr_str = f"{new_portfolio_ecagr:+.1f}%"
        delta_str = f"+{delta:.2f}pp"
        new_cash_str = f"{new_cash_weight:.1f}%"
        pipeline_short = c['pipeline_status'][:15]

        print(f"{c['ticker']:<10} {c['qs']:>3} {c['tier']:>4} {pipeline_short:>15} {ecagr_str:>8} {new_ecagr_str:>13} {delta_str:>7} {new_cash_str:>9} {mos_str:>7}")

    print("-" * 115)
    deployments_possible = int(cash_eur / deploy_amount) if deploy_amount > 0 else 0
    print(f"  {len(viable)} viable candidates | {deployments_possible} x EUR {deploy_amount} deployments possible from cash")

    # Best combined deployment
    if len(viable) >= 2 and deployments_possible >= 2:
        print()
        print(f"  TOP {min(deployments_possible, 5)} SEQUENTIAL DEPLOYMENTS (cumulative):")
        cumulative_ecagr = current_ecagr
        remaining_cash = cash_eur
        for i, c in enumerate(viable[:min(deployments_possible, 5)]):
            if remaining_cash < deploy_amount:
                break
            remaining_cash -= deploy_amount
            deploy_w = (deploy_amount / nav * 100) if nav > 0 else 0
            cumulative_ecagr += deploy_w / 100 * c['ecagr']
            remaining_pct = (remaining_cash / nav * 100) if nav > 0 else 0
            print(f"    {i+1}. +{c['ticker']:<10} E[CAGR] {c['ecagr']:>5.1f}% -> Portfolio {cumulative_ecagr:+.1f}% | Cash: EUR {remaining_cash:,.0f} ({remaining_pct:.1f}%)")
    print()


def print_rotation_simulation(results, cash_eur, nav, candidates):
    """Simulate rotation: sell weak position, buy strong candidate."""
    current_ecagr = sum(r.get('contribution', 0) for r in results)

    # Weakest positions (lowest E[CAGR], excluding errors)
    valid_positions = [r for r in results if r.get('ecagr') is not None]
    if not valid_positions:
        print("\n  No positions with valid E[CAGR] for rotation analysis.")
        return

    weakest = sorted(valid_positions, key=lambda x: x['ecagr'])

    # Strongest candidates
    viable = [c for c in candidates if c.get('ecagr') is not None and c['ecagr'] > 0]
    viable.sort(key=lambda x: x['ecagr'], reverse=True)

    if not viable:
        print("\n  No viable pipeline candidates for rotation.")
        return

    print()
    print("=" * 120)
    print("ROTATION SIMULATION -- Sell weak position, buy strong candidate")
    print("=" * 120)
    print(f"  Current Portfolio E[CAGR]: {current_ecagr:+.1f}%")
    print()
    print(f"{'SELL':<10} {'E[CAGR]':>8} {'Weight':>7}  -->  {'BUY':<10} {'E[CAGR]':>8} {'QS':>3}  {'NewPfE[CAGR]':>13} {'Delta':>8} {'Tier':>4}")
    print("-" * 120)

    rotations = []
    for weak in weakest[:5]:
        for strong in viable[:3]:
            # Simulate: remove weak position contribution, add strong at same weight
            w = weak['weight']
            weak_contrib = w / 100 * weak['ecagr']
            new_contrib = w / 100 * strong['ecagr']
            new_portfolio_ecagr = current_ecagr - weak_contrib + new_contrib
            delta = new_portfolio_ecagr - current_ecagr
            rotations.append({
                'sell': weak['ticker'],
                'sell_ecagr': weak['ecagr'],
                'sell_weight': w,
                'buy': strong['ticker'],
                'buy_ecagr': strong['ecagr'],
                'buy_qs': strong['qs'],
                'buy_tier': strong['tier'],
                'new_ecagr': new_portfolio_ecagr,
                'delta': delta,
            })

    # Sort by delta descending (most impactful rotations first)
    rotations.sort(key=lambda x: x['delta'], reverse=True)

    # Show top 10, dedup sell-buy pairs
    seen = set()
    shown = 0
    for rot in rotations:
        key = (rot['sell'], rot['buy'])
        if key in seen:
            continue
        seen.add(key)
        if shown >= 10:
            break

        print(f"{rot['sell']:<10} {rot['sell_ecagr']:>+7.1f}% {rot['sell_weight']:>6.1f}%  -->  {rot['buy']:<10} {rot['buy_ecagr']:>+7.1f}% {rot['buy_qs']:>3}  {rot['new_ecagr']:>+12.1f}% {rot['delta']:>+7.2f}pp {rot['buy_tier']:>4}")
        shown += 1

    print("-" * 120)
    print(f"  Positive delta = portfolio improves. Same weight assumed (sell proceeds = buy amount).")
    print()


def print_cash_drag_analysis(results, cash_eur, nav, total_value_eur):
    """Analyze cash drag at different allocation levels."""
    current_ecagr = sum(r.get('contribution', 0) for r in results)
    cash_weight = (cash_eur / nav * 100) if nav > 0 else 0
    invested_weight = 100 - cash_weight

    # Average position E[CAGR]
    valid = [r for r in results if r.get('ecagr') is not None]
    if not valid:
        print("\n  No positions with valid E[CAGR] for cash drag analysis.")
        return

    avg_ecagr = sum(r['ecagr'] * r['weight'] for r in valid) / invested_weight if invested_weight > 0 else 0

    print()
    print("=" * 100)
    print("CASH DRAG ANALYSIS")
    print("=" * 100)
    print(f"  Current cash: EUR {cash_eur:,.0f} ({cash_weight:.1f}% of NAV EUR {nav:,.0f})")
    print(f"  Current portfolio E[CAGR]: {current_ecagr:+.1f}%")
    print(f"  Avg invested position E[CAGR]: {avg_ecagr:.1f}%")
    print(f"  Benchmark return (assumed): {BENCHMARK_ANNUAL_RETURN*100:.0f}%/yr")
    print()

    # Annual cash drag in EUR
    annual_drag_eur = cash_eur * BENCHMARK_ANNUAL_RETURN
    print(f"  Annual cash drag (vs {BENCHMARK_ANNUAL_RETURN*100:.0f}% benchmark): EUR {annual_drag_eur:,.0f}/yr")
    print(f"  3-year cumulative cash drag: EUR {annual_drag_eur * 3:,.0f}")
    print()

    # Scenario table
    print(f"{'Cash Level':>12} {'Cash EUR':>10} {'Deploy EUR':>11} {'Pf E[CAGR]':>11} {'Delta vs Now':>13} {'Deployments':>12}")
    print("-" * 80)

    target_levels = [50, 40, 30, 20, 10, 5]
    for target_pct in target_levels:
        target_cash = nav * target_pct / 100
        deploy_needed = cash_eur - target_cash
        if deploy_needed < 0:
            continue  # Cash already below this level

        # If we deploy at avg position E[CAGR]
        deploy_weight = deploy_needed / nav * 100
        new_ecagr = current_ecagr + (deploy_weight / 100 * avg_ecagr)
        delta = new_ecagr - current_ecagr
        n_deployments = int(deploy_needed / DEFAULT_DEPLOY_EUR) if DEFAULT_DEPLOY_EUR > 0 else 0

        marker = " <-- current" if abs(target_pct - cash_weight) < 2 else ""
        print(f"{target_pct:>10.0f}% {target_cash:>10,.0f} {deploy_needed:>10,.0f} {new_ecagr:>+10.1f}% {delta:>+12.1f}pp {n_deployments:>8} x EUR {DEFAULT_DEPLOY_EUR}{marker}")

    # Full investment scenario
    full_ecagr = avg_ecagr  # 100% invested at avg E[CAGR]
    delta_full = full_ecagr - current_ecagr
    n_full = int(cash_eur / DEFAULT_DEPLOY_EUR) if DEFAULT_DEPLOY_EUR > 0 else 0
    print(f"{'0':>10}% {'0':>10} {cash_eur:>10,.0f} {full_ecagr:>+10.1f}% {delta_full:>+12.1f}pp {n_full:>8} x EUR {DEFAULT_DEPLOY_EUR}")

    print("-" * 80)
    print(f"  Assumes new deployments achieve avg position E[CAGR] of {avg_ecagr:.1f}%.")
    print(f"  Actual E[CAGR] depends on specific opportunities. Use --deploy for candidate-level detail.")
    print()


def main():
    parser = argparse.ArgumentParser(
        description='Portfolio E[CAGR] optimizer: deployment and rotation simulator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 tools/portfolio_optimizer.py                # Portfolio E[CAGR] breakdown
  python3 tools/portfolio_optimizer.py --deploy       # Deploy cash simulation
  python3 tools/portfolio_optimizer.py --deploy 400   # Deploy EUR 400 per candidate
  python3 tools/portfolio_optimizer.py --rotate       # Rotation simulation
  python3 tools/portfolio_optimizer.py --cash-drag    # Cash drag at different levels
  python3 tools/portfolio_optimizer.py --all          # All modes
        """
    )
    parser.add_argument('--deploy', nargs='?', const=DEFAULT_DEPLOY_EUR, type=float,
                        metavar='EUR', help=f'Deploy simulation (default EUR {DEFAULT_DEPLOY_EUR})')
    parser.add_argument('--rotate', action='store_true', help='Rotation simulation')
    parser.add_argument('--cash-drag', action='store_true', help='Cash drag analysis')
    parser.add_argument('--all', action='store_true', help='Run all modes')

    args = parser.parse_args()

    # Default: show portfolio E[CAGR] if no flags
    show_portfolio = True
    show_deploy = args.deploy is not None or args.all
    show_rotate = args.rotate or args.all
    show_cash_drag = args.cash_drag or args.all
    deploy_amount = args.deploy if args.deploy is not None else DEFAULT_DEPLOY_EUR

    # Load portfolio
    portfolio = load_yaml(PORTFOLIO_FILE)
    if not portfolio:
        print("ERROR: Cannot load portfolio/current.yaml")
        sys.exit(1)

    # FX rates
    print("Loading FX rates...")
    eurusd, gbpeur, dkkeur = get_fx_rates()
    print(f"FX: EUR/USD={eurusd:.4f} | GBP/EUR={gbpeur:.4f} | DKK/EUR={dkkeur:.4f}")

    # Process portfolio
    results, cash_eur, nav, total_value_eur = process_portfolio_positions(
        portfolio, eurusd, gbpeur, dkkeur
    )

    # Always show portfolio E[CAGR]
    if show_portfolio:
        print_portfolio_ecagr(results, cash_eur, nav, total_value_eur)

    # Load pipeline candidates if needed for deploy/rotate
    candidates = []
    if show_deploy or show_rotate:
        candidates = load_universe_candidates(eurusd, gbpeur, dkkeur)
        # Exclude tickers already in portfolio
        portfolio_tickers = {r['ticker'] for r in results}
        candidates = [c for c in candidates if c['ticker'] not in portfolio_tickers]
        if candidates:
            fetch_candidate_prices(candidates, eurusd, gbpeur, dkkeur)

    if show_deploy:
        print_deployment_simulation(results, cash_eur, nav, candidates, eurusd, gbpeur, dkkeur, deploy_amount)

    if show_rotate:
        print_rotation_simulation(results, cash_eur, nav, candidates)

    if show_cash_drag:
        print_cash_drag_analysis(results, cash_eur, nav, total_value_eur)

    print("[Raw data. Portfolio optimization context.]")
    print()


if __name__ == '__main__':
    main()
