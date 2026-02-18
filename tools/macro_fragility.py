#!/usr/bin/env python3
"""
Macro Fragility - 3-layer macro data tool. Raw data only, no judgments.
Provides macro conditions at world, country, and sector levels via yfinance.

Usage:
  python3 tools/macro_fragility.py world                  # Global indicators
  python3 tools/macro_fragility.py country US              # Country-specific
  python3 tools/macro_fragility.py country DE              # Country-specific (Germany)
  python3 tools/macro_fragility.py sector "Technology"     # Sector-specific
  python3 tools/macro_fragility.py sector "Healthcare"     # Sector-specific
  python3 tools/macro_fragility.py full                    # All three layers combined
"""

import sys
import argparse
import yfinance as yf
import warnings
from datetime import datetime, timedelta

warnings.filterwarnings('ignore')


# ==============================================================================
# Configuration
# ==============================================================================

WORLD_TICKERS = {
    'VIX':       {'ticker': '^VIX',      'label': 'VIX (Volatility)',       'type': 'level'},
    'US10Y':     {'ticker': '^TNX',      'label': 'US 10Y Yield',          'type': 'yield'},
    'US2Y':      {'ticker': '2YY=F',     'label': 'US 2Y Yield',           'type': 'yield'},
    'GOLD':      {'ticker': 'GC=F',      'label': 'Gold',                  'type': 'commodity'},
    'OIL':       {'ticker': 'CL=F',      'label': 'Oil (WTI)',             'type': 'commodity'},
    'DXY':       {'ticker': 'DX-Y.NYB',  'label': 'US Dollar Index',       'type': 'level'},
    'SP500':     {'ticker': '^GSPC',     'label': 'S&P 500',              'type': 'index'},
    'HYG':       {'ticker': 'HYG',       'label': 'HY Corp Bond ETF',     'type': 'etf'},
    'LQD':       {'ticker': 'LQD',       'label': 'IG Corp Bond ETF',     'type': 'etf'},
}

COUNTRY_CONFIG = {
    'US': {
        'name': 'United States',
        'index': '^GSPC',
        'index_name': 'S&P 500',
        'bond_10y': '^TNX',
        'currency': None,  # USD is base
        'etf': 'SPY',
        'sector_etfs': {
            'Technology':      'XLK',
            'Healthcare':      'XLV',
            'Financials':      'XLF',
            'Energy':          'XLE',
            'Industrials':     'XLI',
            'Consumer Disc.':  'XLY',
            'Consumer Stap.':  'XLP',
            'Utilities':       'XLU',
            'Real Estate':     'XLRE',
            'Materials':       'XLB',
            'Communication':   'XLC',
        },
    },
    'UK': {
        'name': 'United Kingdom',
        'index': '^FTSE',
        'index_name': 'FTSE 100',
        'bond_10y': None,
        'currency': 'GBPUSD=X',
        'etf': 'EWU',
        'sector_etfs': {},
    },
    'DE': {
        'name': 'Germany',
        'index': '^GDAXI',
        'index_name': 'DAX 40',
        'bond_10y': None,
        'currency': 'EURUSD=X',
        'etf': 'EWG',
        'sector_etfs': {},
    },
    'FR': {
        'name': 'France',
        'index': '^FCHI',
        'index_name': 'CAC 40',
        'bond_10y': None,
        'currency': 'EURUSD=X',
        'etf': 'EWQ',
        'sector_etfs': {},
    },
    'JP': {
        'name': 'Japan',
        'index': '^N225',
        'index_name': 'Nikkei 225',
        'bond_10y': None,
        'currency': 'JPYUSD=X',
        'etf': 'EWJ',
        'sector_etfs': {},
    },
    'IT': {
        'name': 'Italy',
        'index': 'FTSEMIB.MI',
        'index_name': 'FTSE MIB',
        'bond_10y': None,
        'currency': 'EURUSD=X',
        'etf': 'EWI',
        'sector_etfs': {},
    },
    'ES': {
        'name': 'Spain',
        'index': '^IBEX',
        'index_name': 'IBEX 35',
        'bond_10y': None,
        'currency': 'EURUSD=X',
        'etf': 'EWP',
        'sector_etfs': {},
    },
    'DK': {
        'name': 'Denmark',
        'index': '^OMXC25',
        'index_name': 'OMX Copenhagen 25',
        'bond_10y': None,
        'currency': 'DKKUSD=X',
        'etf': 'EDEN',
        'sector_etfs': {},
    },
    'EU': {
        'name': 'Eurozone (aggregate)',
        'index': '^STOXX50E',
        'index_name': 'Euro Stoxx 50',
        'bond_10y': None,
        'currency': 'EURUSD=X',
        'etf': 'FEZ',
        'sector_etfs': {},
    },
}

SECTOR_CONFIG = {
    'technology':         {'etfs': ['XLK', 'VGT', 'QQQ'],   'primary': 'XLK'},
    'healthcare':         {'etfs': ['XLV', 'VHT', 'IBB'],    'primary': 'XLV'},
    'financials':         {'etfs': ['XLF', 'VFH', 'KBE'],    'primary': 'XLF'},
    'energy':             {'etfs': ['XLE', 'VDE', 'OIH'],    'primary': 'XLE'},
    'industrials':        {'etfs': ['XLI', 'VIS'],            'primary': 'XLI'},
    'consumer discretionary': {'etfs': ['XLY', 'VCR'],       'primary': 'XLY'},
    'consumer staples':   {'etfs': ['XLP', 'VDC'],            'primary': 'XLP'},
    'utilities':          {'etfs': ['XLU', 'VPU'],            'primary': 'XLU'},
    'real estate':        {'etfs': ['XLRE', 'VNQ', 'IYR'],   'primary': 'XLRE'},
    'materials':          {'etfs': ['XLB', 'VAW'],            'primary': 'XLB'},
    'communication':      {'etfs': ['XLC', 'VOX'],            'primary': 'XLC'},
    'semiconductors':     {'etfs': ['SMH', 'SOXX'],           'primary': 'SMH'},
    'defense':            {'etfs': ['ITA', 'PPA'],            'primary': 'ITA'},
    'insurance':          {'etfs': ['KIE', 'IAK'],            'primary': 'KIE'},
    'payments':           {'etfs': ['IPAY'],                  'primary': 'IPAY'},
    'biotech':            {'etfs': ['IBB', 'XBI'],            'primary': 'IBB'},
    'pharma':             {'etfs': ['XLV', 'IHE'],            'primary': 'IHE'},
    'luxury':             {'etfs': ['LUXE'],                  'primary': 'LUXE'},
    'telecom':            {'etfs': ['IYZ', 'VOX'],            'primary': 'IYZ'},
}


# ==============================================================================
# Data fetching helpers
# ==============================================================================

def safe_float(val):
    """Convert to float, return None if impossible."""
    if val is None:
        return None
    try:
        f = float(val)
        if f != f:  # NaN
            return None
        return f
    except (ValueError, TypeError):
        return None


def fetch_ticker_data(ticker_str):
    """Fetch basic price data for a ticker. Returns dict or None on failure."""
    try:
        t = yf.Ticker(ticker_str)
        info = t.info
        if not info:
            return None

        price = safe_float(info.get('currentPrice')) or \
                safe_float(info.get('regularMarketPrice')) or \
                safe_float(info.get('regularMarketPreviousClose')) or \
                safe_float(info.get('previousClose'))

        high_52w = safe_float(info.get('fiftyTwoWeekHigh'))
        low_52w = safe_float(info.get('fiftyTwoWeekLow'))
        name = info.get('shortName', ticker_str)

        # Distance from 52-week high
        dist_high = None
        if price is not None and high_52w is not None and high_52w > 0:
            dist_high = ((price - high_52w) / high_52w) * 100

        # Distance from 52-week low
        dist_low = None
        if price is not None and low_52w is not None and low_52w > 0:
            dist_low = ((price - low_52w) / low_52w) * 100

        # Dividend yield: prefer trailingAnnualDividendYield (reliable for ETFs)
        # yfinance dividendYield is sometimes wrong for ETFs (returns fund yield instead)
        div_yield = safe_float(info.get('trailingAnnualDividendYield'))
        if div_yield is None:
            div_yield = safe_float(info.get('dividendYield'))
            # Sanity check: if yield > 20%, it's likely a data error
            if div_yield is not None and div_yield > 0.20:
                div_yield = None

        return {
            'ticker': ticker_str,
            'name': name,
            'price': price,
            'high_52w': high_52w,
            'low_52w': low_52w,
            'dist_high_pct': dist_high,
            'dist_low_pct': dist_low,
            'pe': safe_float(info.get('trailingPE')),
            'forward_pe': safe_float(info.get('forwardPE')),
            'div_yield': div_yield,  # as decimal (0.01 = 1%)
        }
    except Exception:
        return None


def fetch_historical_changes(ticker_str, periods_months=(3, 12)):
    """Fetch price changes over specified periods (in months). Returns dict of period->pct_change."""
    changes = {}
    try:
        t = yf.Ticker(ticker_str)
        hist = t.history(period='1y')
        if hist.empty:
            return changes

        current_price = hist['Close'].iloc[-1]

        for months in periods_months:
            target_date = datetime.now() - timedelta(days=months * 30)
            # Handle timezone-aware vs naive index
            if hasattr(hist.index, 'tz') and hist.index.tz:
                target_aware = target_date.replace(tzinfo=hist.index.tz)
                past_data = hist[hist.index <= target_aware]
            else:
                past_data = hist[hist.index <= str(target_date)]

            if not past_data.empty:
                past_price = past_data['Close'].iloc[-1]
                if past_price > 0:
                    changes[f'{months}m'] = ((current_price - past_price) / past_price) * 100
    except Exception:
        pass
    return changes


def fetch_top_holdings(etf_ticker, max_holdings=10):
    """Fetch top holdings of an ETF via funds_data. Returns list of dicts or empty list."""
    try:
        t = yf.Ticker(etf_ticker)
        fd = t.funds_data
        if fd is None:
            return []
        holdings = fd.top_holdings
        if holdings is None or holdings.empty:
            return []
        result = []
        for symbol, row in holdings.head(max_holdings).iterrows():
            name = row.get('Name', symbol) if 'Name' in row.index else symbol
            weight = safe_float(row.get('Holding Percent'))
            result.append({
                'symbol': symbol,
                'name': name,
                'weight': weight,
            })
        return result
    except Exception:
        return []


def fmt_pct(val, decimals=1, with_sign=True):
    """Format percentage for display."""
    if val is None:
        return 'N/A'
    if with_sign:
        return f"{val:+.{decimals}f}%"
    return f"{val:.{decimals}f}%"


def fmt_price(val, decimals=2):
    """Format price for display."""
    if val is None:
        return 'N/A'
    if val >= 10000:
        return f"{val:,.0f}"
    elif val >= 100:
        return f"{val:,.{decimals}f}"
    else:
        return f"{val:.{decimals}f}"


# ==============================================================================
# Layer 1: World
# ==============================================================================

def layer_world():
    """Fetch and display global macro indicators."""
    print("=" * 90)
    print("LAYER 1: WORLD MACRO INDICATORS")
    print("=" * 90)
    print()

    results = {}
    yf_calls = 0

    for key, cfg in WORLD_TICKERS.items():
        ticker_str = cfg['ticker']
        data = fetch_ticker_data(ticker_str)
        yf_calls += 1
        changes = fetch_historical_changes(ticker_str)
        yf_calls += 1
        results[key] = {'data': data, 'changes': changes, 'config': cfg}

    # Calculate spread if both US10Y and US2Y are available
    us10y_data = results.get('US10Y', {}).get('data')
    us2y_data = results.get('US2Y', {}).get('data')
    spread_2_10 = None
    if us10y_data and us2y_data:
        p10 = us10y_data.get('price')
        p2 = us2y_data.get('price')
        if p10 is not None and p2 is not None:
            spread_2_10 = p10 - p2

    # Calculate credit spread proxy: HYG/LQD ratio
    hyg_data = results.get('HYG', {}).get('data')
    lqd_data = results.get('LQD', {}).get('data')
    credit_ratio = None
    if hyg_data and lqd_data:
        hyg_p = hyg_data.get('price')
        lqd_p = lqd_data.get('price')
        if hyg_p and lqd_p and lqd_p > 0:
            credit_ratio = hyg_p / lqd_p

    # Print main table
    print(f"{'Indicator':<22} {'Value':>10} {'52w High':>10} {'52w Low':>10} {'Dist High':>10} {'3m Chg':>10} {'12m Chg':>10}")
    print("-" * 90)

    for key in ['VIX', 'US10Y', 'US2Y', 'GOLD', 'OIL', 'DXY', 'SP500']:
        r = results.get(key, {})
        d = r.get('data')
        c = r.get('changes', {})
        cfg = r.get('config', {})
        label = cfg.get('label', key)

        if d is None:
            print(f"{label:<22} {'ERROR':>10}")
            continue

        price_str = fmt_price(d.get('price'))
        high_str = fmt_price(d.get('high_52w'))
        low_str = fmt_price(d.get('low_52w'))
        dist_str = fmt_pct(d.get('dist_high_pct'))
        chg_3m = fmt_pct(c.get('3m'))
        chg_12m = fmt_pct(c.get('12m'))

        print(f"{label:<22} {price_str:>10} {high_str:>10} {low_str:>10} {dist_str:>10} {chg_3m:>10} {chg_12m:>10}")

    print()

    # Derived metrics
    print("DERIVED METRICS:")
    print(f"  2Y-10Y Spread:      {spread_2_10:+.2f}%" if spread_2_10 is not None else "  2Y-10Y Spread:      N/A")
    print(f"  HYG/LQD Ratio:      {credit_ratio:.4f}" if credit_ratio is not None else "  HYG/LQD Ratio:      N/A")
    print()

    return yf_calls


# ==============================================================================
# Layer 2: Country
# ==============================================================================

def layer_country(country_code):
    """Fetch and display country-specific macro indicators."""
    code = country_code.upper()
    if code not in COUNTRY_CONFIG:
        print(f"ERROR: Country '{code}' not supported.")
        print(f"Supported: {', '.join(sorted(COUNTRY_CONFIG.keys()))}")
        return 0

    cfg = COUNTRY_CONFIG[code]
    yf_calls = 0

    print("=" * 90)
    print(f"LAYER 2: COUNTRY - {cfg['name']} ({code})")
    print("=" * 90)
    print()

    # Main index
    idx_data = fetch_ticker_data(cfg['index'])
    idx_changes = fetch_historical_changes(cfg['index'])
    yf_calls += 2

    print(f"{'Indicator':<22} {'Value':>10} {'52w High':>10} {'52w Low':>10} {'Dist High':>10} {'3m Chg':>10} {'12m Chg':>10}")
    print("-" * 90)

    if idx_data:
        print(f"{cfg['index_name']:<22} {fmt_price(idx_data.get('price')):>10} {fmt_price(idx_data.get('high_52w')):>10} {fmt_price(idx_data.get('low_52w')):>10} {fmt_pct(idx_data.get('dist_high_pct')):>10} {fmt_pct(idx_changes.get('3m')):>10} {fmt_pct(idx_changes.get('12m')):>10}")
    else:
        print(f"{cfg['index_name']:<22} {'ERROR':>10}")

    # Currency vs USD
    if cfg.get('currency'):
        fx_data = fetch_ticker_data(cfg['currency'])
        fx_changes = fetch_historical_changes(cfg['currency'])
        yf_calls += 2
        if fx_data:
            pair_label = cfg['currency'].replace('=X', '')
            print(f"{pair_label:<22} {fmt_price(fx_data.get('price'), 4):>10} {fmt_price(fx_data.get('high_52w'), 4):>10} {fmt_price(fx_data.get('low_52w'), 4):>10} {fmt_pct(fx_data.get('dist_high_pct')):>10} {fmt_pct(fx_changes.get('3m')):>10} {fmt_pct(fx_changes.get('12m')):>10}")

    # Bond yield (10Y)
    if cfg.get('bond_10y'):
        bond_data = fetch_ticker_data(cfg['bond_10y'])
        bond_changes = fetch_historical_changes(cfg['bond_10y'])
        yf_calls += 2
        if bond_data:
            print(f"{'10Y Yield':<22} {fmt_pct(bond_data.get('price'), 2, False):>10} {fmt_pct(bond_data.get('high_52w'), 2, False):>10} {fmt_pct(bond_data.get('low_52w'), 2, False):>10} {'':>10} {fmt_pct(bond_changes.get('3m')):>10} {fmt_pct(bond_changes.get('12m')):>10}")

    # Country ETF
    if cfg.get('etf'):
        etf_data = fetch_ticker_data(cfg['etf'])
        etf_changes = fetch_historical_changes(cfg['etf'])
        yf_calls += 2
        if etf_data:
            print(f"{cfg['etf'] + ' ETF':<22} {fmt_price(etf_data.get('price')):>10} {fmt_price(etf_data.get('high_52w')):>10} {fmt_price(etf_data.get('low_52w')):>10} {fmt_pct(etf_data.get('dist_high_pct')):>10} {fmt_pct(etf_changes.get('3m')):>10} {fmt_pct(etf_changes.get('12m')):>10}")

    print()

    # Sector ETFs (US only has a rich set)
    if cfg.get('sector_etfs'):
        print("SECTOR ETF PERFORMANCE:")
        print(f"{'Sector':<22} {'ETF':>6} {'Price':>10} {'Dist High':>10} {'3m Chg':>10} {'12m Chg':>10}")
        print("-" * 70)

        for sector_name, etf_ticker in cfg['sector_etfs'].items():
            if yf_calls >= 20:
                print(f"  (remaining sectors skipped -- yfinance call limit reached)")
                break

            etf_data = fetch_ticker_data(etf_ticker)
            etf_changes = fetch_historical_changes(etf_ticker)
            yf_calls += 2

            if etf_data:
                print(f"{sector_name:<22} {etf_ticker:>6} {fmt_price(etf_data.get('price')):>10} {fmt_pct(etf_data.get('dist_high_pct')):>10} {fmt_pct(etf_changes.get('3m')):>10} {fmt_pct(etf_changes.get('12m')):>10}")
            else:
                print(f"{sector_name:<22} {etf_ticker:>6} {'ERROR':>10}")

        print()

    return yf_calls


# ==============================================================================
# Layer 3: Sector
# ==============================================================================

def layer_sector(sector_name):
    """Fetch and display sector-specific indicators."""
    sector_key = sector_name.lower().strip()
    yf_calls = 0

    # Try to match sector
    matched = None
    for key in SECTOR_CONFIG:
        if sector_key in key or key in sector_key:
            matched = key
            break

    if matched is None:
        print(f"ERROR: Sector '{sector_name}' not found.")
        print(f"Supported sectors: {', '.join(sorted(SECTOR_CONFIG.keys()))}")
        return 0

    cfg = SECTOR_CONFIG[matched]
    display_name = matched.title()

    print("=" * 90)
    print(f"LAYER 3: SECTOR - {display_name}")
    print("=" * 90)
    print()

    # Sector ETFs
    print(f"{'ETF':<8} {'Name':<30} {'Price':>10} {'52w High':>10} {'52w Low':>10} {'Dist High':>10} {'3m Chg':>10} {'12m Chg':>10}")
    print("-" * 100)

    primary_etf = cfg['primary']
    primary_data = None

    for etf_ticker in cfg['etfs']:
        data = fetch_ticker_data(etf_ticker)
        changes = fetch_historical_changes(etf_ticker)
        yf_calls += 2

        if data:
            if etf_ticker == primary_etf:
                primary_data = data
            name = data.get('name', etf_ticker)[:29]
            print(f"{etf_ticker:<8} {name:<30} {fmt_price(data.get('price')):>10} {fmt_price(data.get('high_52w')):>10} {fmt_price(data.get('low_52w')):>10} {fmt_pct(data.get('dist_high_pct')):>10} {fmt_pct(changes.get('3m')):>10} {fmt_pct(changes.get('12m')):>10}")
        else:
            print(f"{etf_ticker:<8} {'':>30} {'ERROR':>10}")

    print()

    # Valuation data for primary ETF
    if primary_data:
        print("VALUATION (primary ETF):")
        pe = primary_data.get('pe')
        fwd_pe = primary_data.get('forward_pe')
        dy = primary_data.get('div_yield')

        print(f"  Trailing P/E:   {f'{pe:.1f}' if pe else 'N/A'}")
        print(f"  Forward P/E:    {f'{fwd_pe:.1f}' if fwd_pe else 'N/A'}")
        if dy is not None:
            print(f"  Dividend Yield: {dy*100:.2f}%")
        else:
            print(f"  Dividend Yield: N/A")
        print()

    # Top holdings of primary ETF
    if primary_etf:
        holdings = fetch_top_holdings(primary_etf)
        yf_calls += 1
        if holdings:
            print(f"TOP HOLDINGS ({primary_etf}):")
            for i, h in enumerate(holdings, 1):
                weight_str = f"{h['weight']*100:.1f}%" if h.get('weight') else 'N/A'
                symbol = h.get('symbol', '')
                name = h.get('name', symbol)[:35]
                print(f"  {i:>2}. {symbol:<8} {name:<36} {weight_str:>8}")
            print()

    return yf_calls


# ==============================================================================
# Full mode
# ==============================================================================

def layer_full():
    """Run all three layers with default countries."""
    total_calls = 0

    total_calls += layer_world()
    print()

    # Default countries: US, UK, DE (where the portfolio has positions)
    for country in ['US', 'UK', 'DE']:
        if total_calls >= 18:
            print(f"(Skipping {country} -- approaching yfinance call limit)")
            continue
        total_calls += layer_country(country)
        print()

    return total_calls


# ==============================================================================
# Main
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Macro Fragility - 3-layer macro data. Raw data, no judgments.'
    )
    subparsers = parser.add_subparsers(dest='layer', help='Data layer to query')

    # World
    subparsers.add_parser('world', help='Global macro indicators')

    # Country
    country_parser = subparsers.add_parser('country', help='Country-specific indicators')
    country_parser.add_argument('code', type=str, help='Country code (US, UK, DE, FR, JP, IT, ES, DK, EU)')

    # Sector
    sector_parser = subparsers.add_parser('sector', help='Sector-specific indicators')
    sector_parser.add_argument('name', type=str, help='Sector name (Technology, Healthcare, Financials, etc.)')

    # Full
    subparsers.add_parser('full', help='All three layers combined (world + US/UK/DE)')

    args = parser.parse_args()

    if not args.layer:
        parser.print_help()
        sys.exit(1)

    print()
    start_time = datetime.now()

    if args.layer == 'world':
        layer_world()
    elif args.layer == 'country':
        layer_country(args.code)
    elif args.layer == 'sector':
        layer_sector(args.name)
    elif args.layer == 'full':
        layer_full()

    elapsed = (datetime.now() - start_time).total_seconds()
    print(f"Data freshness: yfinance real-time/delayed quotes. Fetched {datetime.now().strftime('%Y-%m-%d %H:%M')} ({elapsed:.1f}s)")
    print("[Raw data. Reason from principles.md]")
    print()


if __name__ == '__main__':
    main()
