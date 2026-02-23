#!/usr/bin/env python3
"""
Session Opener - Single command for Phase 0-1 session initialization.
Replaces running 6-8 separate tools at session start.

Outputs a concise, structured text briefing for instant CIO situational awareness.

Sections:
  1. PORTFOLIO SNAPSHOT  - NAV, cash, P&L per position
  2. STANDING ORDER TRIGGERS - Distance to trigger, TRIGGERED/NEAR flags
  3. EARNINGS NEXT 7 DAYS - From calendar.yaml
  4. FORWARD RETURNS (compact) - E[CAGR] per position, sorted, bottom 3 flagged
  5. PIPELINE HEALTH - Universe status counts
  6. ALERTS - Aggregated critical findings

Usage:
  python3 tools/session_opener.py              # Full briefing (all 6 sections)
  python3 tools/session_opener.py --quick      # Quick briefing (sections 2+3+6 only)
"""

import os
import sys
import re
import argparse
import yaml
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORTFOLIO_FILE = os.path.join(BASE_DIR, 'portfolio', 'current.yaml')
SO_FILE = os.path.join(BASE_DIR, 'state', 'standing_orders.yaml')
CALENDAR_FILE = os.path.join(BASE_DIR, 'state', 'calendar.yaml')
UNIVERSE_FILE = os.path.join(BASE_DIR, 'state', 'quality_universe.yaml')
THESIS_ACTIVE_DIR = os.path.join(BASE_DIR, 'thesis', 'active')


# ---------------------------------------------------------------------------
# YAML loader
# ---------------------------------------------------------------------------
def load_yaml(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f) or {}
    except Exception:
        return {}


# ---------------------------------------------------------------------------
# FX rates  (EUR base, same pattern as price_checker.py)
# ---------------------------------------------------------------------------
def get_fx_rates():
    """Get EUR/USD, GBP/EUR, DKK/EUR, CHF/EUR. Report fallbacks."""
    import yfinance as yf
    defaults = {'EURUSD': 1.04, 'GBPEUR': 1.19, 'DKKEUR': 0.134, 'CHFEUR': 1.07}
    fallbacks_used = []
    rates = {}

    pairs = [
        ('EURUSD=X', 'EURUSD'),
        ('GBPEUR=X', 'GBPEUR'),
        ('DKKEUR=X', 'DKKEUR'),
        ('CHFEUR=X', 'CHFEUR'),
    ]
    for yf_sym, key in pairs:
        try:
            val = yf.Ticker(yf_sym).info.get('previousClose')
            if not val:
                raise ValueError
            rates[key] = val
        except Exception:
            rates[key] = defaults[key]
            fallbacks_used.append(f"{key}={defaults[key]}")

    if fallbacks_used:
        print(f"  FX WARNING: static fallback ({', '.join(fallbacks_used)})")

    return rates


# ---------------------------------------------------------------------------
# Batch price fetch  (one yfinance download call)
# ---------------------------------------------------------------------------
def batch_fetch_prices(tickers, rates):
    """Fetch current prices for a list of tickers.
    Returns dict: {ticker: {'price': float, 'currency': str, 'price_eur': float,
                             'div_yield_pct': float, 'name': str}}
    """
    import yfinance as yf

    TICKER_MAP = {'LIGHT.NV': 'LIGHT.AS'}
    yf_to_orig = {}
    yf_tickers = []
    for t in tickers:
        yf_t = TICKER_MAP.get(t, t)
        yf_to_orig[yf_t] = t
        yf_tickers.append(yf_t)

    results = {}
    # Fetch individually to get .info (batch download only gives OHLC)
    for yf_t in yf_tickers:
        orig = yf_to_orig[yf_t]
        try:
            info = yf.Ticker(yf_t).info
            price = info.get('currentPrice') or info.get('regularMarketPrice') or info.get('previousClose')
            if price is None:
                continue
            currency = info.get('currency', 'USD')
            name = info.get('shortName', orig)

            # Div yield (already pct in yfinance)
            dy = info.get('dividendYield')
            dy_pct = 0.0
            if dy and isinstance(dy, (int, float)) and 0 <= dy <= 20:
                dy_pct = dy

            # Convert to EUR
            price_eur = _to_eur(price, currency, rates)

            results[orig] = {
                'price': price,
                'currency': currency,
                'price_eur': price_eur,
                'div_yield_pct': dy_pct,
                'name': name,
            }
        except Exception:
            pass

    return results


def _to_eur(price, currency, rates):
    """Convert price in given currency to EUR."""
    if currency == 'EUR':
        return price
    elif currency == 'USD':
        return price / rates['EURUSD']
    elif currency in ('GBp', 'GBX'):
        return (price / 100) * rates['GBPEUR']
    elif currency == 'GBP':
        return price * rates['GBPEUR']
    elif currency == 'DKK':
        return price * rates['DKKEUR']
    elif currency == 'CHF':
        return price * rates.get('CHFEUR', 1.07)
    elif currency == 'SEK':
        return price * 0.088
    return price


# ---------------------------------------------------------------------------
# Fair Value parsing from portfolio/current.yaml fair_value field
# ---------------------------------------------------------------------------
def parse_fair_value(fv_str):
    """Parse fair_value string from current.yaml.
    Handles: 'EUR 35.00 (...)', '190 GBp (...)', '$191 (...)', '580 GBp (...)',
             '$390 (...)','$66 (...)', '240 GBp (...)', '345 GBp (...)'.
    Returns (fv_number, fv_currency) or (None, None).
    """
    if not fv_str:
        return None, None
    s = str(fv_str).strip()

    # Try "$NNN" pattern
    m = re.match(r'\$\s*([0-9,]+(?:\.\d+)?)', s)
    if m:
        return float(m.group(1).replace(',', '')), 'USD'

    # Try "EUR NNN" pattern
    m = re.match(r'EUR\s+([0-9,]+(?:\.\d+)?)', s)
    if m:
        return float(m.group(1).replace(',', '')), 'EUR'

    # Try "NNN GBp" pattern
    m = re.match(r'([0-9,]+(?:\.\d+)?)\s*GBp', s, re.IGNORECASE)
    if m:
        return float(m.group(1).replace(',', '')), 'GBp'

    # Try "CHF NNN" pattern
    m = re.match(r'CHF\s+([0-9,]+(?:\.\d+)?)', s)
    if m:
        return float(m.group(1).replace(',', '')), 'CHF'

    # Try "DKK NNN" pattern
    m = re.match(r'DKK\s+([0-9,]+(?:\.\d+)?)', s)
    if m:
        return float(m.group(1).replace(',', '')), 'DKK'

    # Try "SEK NNN" pattern
    m = re.match(r'SEK\s+([0-9,]+(?:\.\d+)?)', s)
    if m:
        return float(m.group(1).replace(',', '')), 'SEK'

    # Fallback: just extract first number (assume same currency as stock)
    m = re.search(r'([0-9,]+(?:\.\d+)?)', s)
    if m:
        return float(m.group(1).replace(',', '')), None

    return None, None


def convert_fv_to_stock_currency(fv, fv_currency, stock_currency, rates):
    """Convert fair value to stock's trading currency."""
    if fv_currency == stock_currency:
        return fv
    if fv_currency is None:
        return fv  # assume same

    # Convert to EUR first
    fv_eur = fv
    if fv_currency == 'USD':
        fv_eur = fv / rates['EURUSD']
    elif fv_currency in ('GBp', 'GBX'):
        fv_eur = (fv / 100) * rates['GBPEUR']
    elif fv_currency == 'GBP':
        fv_eur = fv * rates['GBPEUR']
    elif fv_currency == 'DKK':
        fv_eur = fv * rates['DKKEUR']
    elif fv_currency == 'CHF':
        fv_eur = fv * rates.get('CHFEUR', 1.07)
    elif fv_currency == 'SEK':
        fv_eur = fv * 0.088

    # Convert from EUR to target
    if stock_currency == 'EUR':
        return fv_eur
    elif stock_currency == 'USD':
        return fv_eur * rates['EURUSD']
    elif stock_currency in ('GBp', 'GBX'):
        return (fv_eur / rates['GBPEUR']) * 100
    elif stock_currency == 'GBP':
        return fv_eur / rates['GBPEUR']
    elif stock_currency == 'DKK':
        return fv_eur / rates['DKKEUR'] if rates['DKKEUR'] else fv_eur
    elif stock_currency == 'CHF':
        return fv_eur / rates.get('CHFEUR', 1.07)
    elif stock_currency == 'SEK':
        return fv_eur / 0.088
    return fv_eur


# ---------------------------------------------------------------------------
# Standing Order trigger parsing
# ---------------------------------------------------------------------------
def parse_trigger(trigger_str):
    """Parse trigger string like '<=EUR 295', '<=$88', '<=950 GBp', '<=CHF 80'.
    Returns (trigger_value, trigger_currency) or (None, None).
    """
    if not trigger_str:
        return None, None
    s = str(trigger_str).strip()

    # Handle conditional triggers (e.g., "CagriSema positive OR price <=$40")
    if 'OR' in s.upper():
        # Try to extract numeric part
        m = re.search(r'<=?\s*\$\s*([0-9,]+(?:\.\d+)?)', s)
        if m:
            return float(m.group(1).replace(',', '')), 'USD'
        return None, None

    # "<=EUR NNN"
    m = re.search(r'<=?\s*EUR\s+([0-9,]+(?:\.\d+)?)', s)
    if m:
        return float(m.group(1).replace(',', '')), 'EUR'

    # "<=$NNN"
    m = re.search(r'<=?\s*\$\s*([0-9,]+(?:\.\d+)?)', s)
    if m:
        return float(m.group(1).replace(',', '')), 'USD'

    # "<=NNN GBp" or "<=N,NNNp"
    m = re.search(r'<=?\s*([0-9,]+(?:\.\d+)?)\s*(?:GBp|p)\b', s, re.IGNORECASE)
    if m:
        return float(m.group(1).replace(',', '')), 'GBp'

    # "<=CHF NNN"
    m = re.search(r'<=?\s*CHF\s+([0-9,]+(?:\.\d+)?)', s)
    if m:
        return float(m.group(1).replace(',', '')), 'CHF'

    # "<=DKK NNN"
    m = re.search(r'<=?\s*DKK\s+([0-9,]+(?:\.\d+)?)', s)
    if m:
        return float(m.group(1).replace(',', '')), 'DKK'

    return None, None


# ---------------------------------------------------------------------------
# SECTION 1: Portfolio Snapshot
# ---------------------------------------------------------------------------
def section_portfolio_snapshot(portfolio, prices, rates):
    """Render portfolio snapshot section."""
    positions = portfolio.get('positions', [])
    short_positions = portfolio.get('short_positions', []) or []
    cash_eur = portfolio.get('cash', {}).get('amount', 0)
    cash_usd = cash_eur * rates['EURUSD']

    rows = []
    total_invested_usd = 0
    total_value_usd = 0

    for p in positions:
        ticker = p['ticker']
        shares = p['shares']
        if 'invested_usd' in p:
            invested = p['invested_usd']
        elif 'invested_eur' in p:
            invested = p['invested_eur'] * rates['EURUSD']
        else:
            continue

        pd = prices.get(ticker)
        if not pd:
            rows.append({'ticker': ticker, 'error': 'No price'})
            continue

        price_usd = pd['price']
        currency = pd['currency']
        # Convert price to USD for P&L calc
        if currency == 'EUR':
            price_usd_conv = pd['price'] * rates['EURUSD']
        elif currency in ('GBp', 'GBX'):
            gbpusd = rates['GBPEUR'] * rates['EURUSD']  # GBP/EUR * EUR/USD = GBP/USD
            price_usd_conv = (pd['price'] / 100) * gbpusd
        elif currency == 'GBP':
            gbpusd = rates['GBPEUR'] * rates['EURUSD']
            price_usd_conv = pd['price'] * gbpusd
        elif currency == 'DKK':
            price_usd_conv = pd['price'] * rates['DKKEUR'] * rates['EURUSD']
        else:
            price_usd_conv = pd['price']  # assume USD

        value_usd = price_usd_conv * shares
        pnl_usd = value_usd - invested
        pnl_pct = (pnl_usd / invested) * 100 if invested else 0

        total_invested_usd += invested
        total_value_usd += value_usd

        # FV and conviction from portfolio
        fv_raw, fv_currency = parse_fair_value(p.get('fair_value'))
        conviction = (p.get('conviction', '?') or '?')[0].upper()

        rows.append({
            'ticker': ticker,
            'price': pd['price'],
            'currency': currency,
            'cost_usd': invested / shares if shares else 0,
            'value_usd': value_usd,
            'pnl_pct': pnl_pct,
            'conviction': conviction,
        })

    portfolio_total_usd = total_value_usd + cash_usd

    lines = []
    lines.append("")
    lines.append("=" * 86)
    lines.append("  1. PORTFOLIO SNAPSHOT")
    lines.append("=" * 86)
    lines.append(f"  {'Ticker':<10} {'Price':>10} {'Curr':>5} {'P&L%':>7} {'Weight%':>8} {'Conv':>5}")
    lines.append("  " + "-" * 50)

    for r in rows:
        if 'error' in r:
            lines.append(f"  {r['ticker']:<10} {'ERROR':>10}")
            continue
        weight = (r['value_usd'] / portfolio_total_usd * 100) if portfolio_total_usd else 0
        lines.append(f"  {r['ticker']:<10} {r['price']:>10.2f} {r['currency']:>5} {r['pnl_pct']:>+6.1f}% {weight:>7.1f}% {r['conviction']:>5}")

    cash_pct = (cash_usd / portfolio_total_usd * 100) if portfolio_total_usd else 0
    total_pnl_pct = ((total_value_usd - total_invested_usd) / total_invested_usd * 100) if total_invested_usd else 0
    lines.append("  " + "-" * 50)
    lines.append(f"  {'CASH':<10} {'':>10} {'EUR':>5} {'':>7} {cash_pct:>7.1f}%")
    lines.append(f"  NAV: EUR {portfolio_total_usd / rates['EURUSD']:,.0f} (${portfolio_total_usd:,.0f}) | "
                 f"Invested: {(1 - cash_pct/100)*100:.1f}% | Cash: EUR {cash_eur:,.0f} ({cash_pct:.1f}%) | "
                 f"Total P&L: {total_pnl_pct:+.1f}%")

    if short_positions:
        lines.append(f"  Short positions: {len(short_positions)} (see portfolio_stats.py for detail)")

    return '\n'.join(lines), cash_pct, total_pnl_pct


# ---------------------------------------------------------------------------
# SECTION 2: Standing Order Triggers
# ---------------------------------------------------------------------------
def section_standing_orders(so_data, prices, rates):
    """Render standing order trigger section. Returns (text, triggered_list, near_list)."""
    orders = so_data.get('standing_orders', [])
    short_orders = so_data.get('short_orders', []) or []
    extreme = so_data.get('extreme_opportunity', []) or []

    triggered = []
    near = []

    lines = []
    lines.append("")
    lines.append("=" * 86)
    lines.append("  2. STANDING ORDER TRIGGERS")
    lines.append("=" * 86)
    lines.append(f"  {'Ticker':<10} {'Action':<5} {'Cat':<10} {'Current':>10} {'Trigger':>10} {'Dist%':>7} {'Status':>10}")
    lines.append("  " + "-" * 68)

    def process_order(order, is_short=False):
        ticker = order.get('ticker', '?')
        action = order.get('action', 'BUY')
        category = order.get('category', '?')
        trigger_str = order.get('trigger', '')
        trigger_val, trigger_currency = parse_trigger(trigger_str)

        if trigger_val is None:
            return f"  {ticker:<10} {action:<5} {category:<10} {'?':>10} {trigger_str:>10} {'cond':>7} {'GATED':>10}"

        pd = prices.get(ticker)
        if not pd:
            return f"  {ticker:<10} {action:<5} {category:<10} {'N/A':>10} {trigger_str:>10} {'?':>7} {'NO DATA':>10}"

        # Get price in same currency as trigger
        current_price = pd['price']
        stock_currency = pd['currency']

        # Convert trigger to stock currency for comparison
        if trigger_currency and trigger_currency != stock_currency:
            trigger_in_stock = convert_fv_to_stock_currency(trigger_val, trigger_currency, stock_currency, rates)
        else:
            trigger_in_stock = trigger_val

        if is_short:
            # Short: trigger when price >= target
            distance_pct = ((trigger_in_stock - current_price) / current_price) * 100
            if current_price >= trigger_in_stock:
                status = 'TRIGGERED'
                triggered.append(f"{ticker} SHORT ({action}) - price {current_price:.2f} >= trigger")
            elif distance_pct < 10:
                status = 'NEAR'
                near.append(f"{ticker} SHORT: {distance_pct:.1f}% to trigger")
            else:
                status = 'OK'
        else:
            # Long: trigger when price <= target
            distance_pct = ((current_price - trigger_in_stock) / trigger_in_stock) * 100
            if current_price <= trigger_in_stock:
                status = 'TRIGGERED'
                triggered.append(f"{ticker} {action} - price {current_price:.2f} {stock_currency} <= trigger {trigger_val:.0f} {trigger_currency or stock_currency}")
            elif distance_pct < 10:
                status = 'NEAR'
                near.append(f"{ticker} {action}: {distance_pct:.1f}% above trigger")
            else:
                status = 'OK'

        status_display = status
        if status == 'TRIGGERED':
            status_display = '>>> TRIG'
        elif status == 'NEAR':
            status_display = f'NEAR'

        return f"  {ticker:<10} {action:<5} {category:<10} {current_price:>10.2f} {trigger_val:>8.0f}{(trigger_currency or '?'):>2} {distance_pct:>+6.1f}% {status_display:>10}"

    for order in orders:
        lines.append(process_order(order))

    for order in short_orders:
        if isinstance(order, dict):
            lines.append(process_order(order, is_short=True))

    if extreme:
        lines.append("  " + "-" * 68)
        lines.append("  EXTREME (crash-only):")
        for ext in extreme:
            ticker = ext.get('ticker', '?')
            trigger_str = str(ext.get('trigger', '?'))
            dist = ext.get('distance_when_moved', '?')
            lines.append(f"  {ticker:<10} {'BUY':<5} {'EXTREME':<10} {'':>10} {trigger_str:>10} {str(dist):>7} {'WAIT':>10}")

    lines.append("  " + "-" * 68)
    active_count = sum(1 for o in orders if o.get('category') == 'ACTIVE')
    gated_count = sum(1 for o in orders if o.get('category') == 'GATED')
    border_count = sum(1 for o in orders if o.get('category') == 'BORDERLINE')
    lines.append(f"  Total: {len(orders)} SOs ({active_count} ACTIVE, {gated_count} GATED, {border_count} BORDERLINE) + {len(extreme)} EXTREME")

    return '\n'.join(lines), triggered, near


# ---------------------------------------------------------------------------
# SECTION 3: Earnings Next 7 Days
# ---------------------------------------------------------------------------
def section_earnings(calendar_data):
    """Render earnings next 7 days section. Returns (text, today_earnings)."""
    events = calendar_data.get('events', [])
    today = datetime.now().date()
    cutoff = today + timedelta(days=7)

    upcoming = []
    today_earnings = []

    for ev in events:
        if not isinstance(ev, dict):
            continue
        ev_type = ev.get('type', '')
        if ev_type not in ('earnings', 'earnings_pipeline', 'catalyst', 'watchlist_review'):
            continue
        date_str = str(ev.get('date', ''))
        try:
            ev_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            continue
        if ev_date < today or ev_date > cutoff:
            continue

        ticker = ev.get('ticker', '?')
        event_text = ev.get('event', '')
        priority = ev.get('priority', 'medium')
        action = ev.get('action', '')

        days_away = (ev_date - today).days
        day_label = 'TODAY' if days_away == 0 else f'+{days_away}d'

        if days_away == 0:
            today_earnings.append(ticker)

        upcoming.append({
            'date': ev_date,
            'day_label': day_label,
            'ticker': ticker,
            'event': event_text[:50],
            'priority': priority,
            'action': action[:60] if action else '',
            'type': ev_type,
        })

    upcoming.sort(key=lambda x: x['date'])

    lines = []
    lines.append("")
    lines.append("=" * 86)
    lines.append("  3. EARNINGS & EVENTS NEXT 7 DAYS")
    lines.append("=" * 86)

    if not upcoming:
        lines.append("  No earnings events in the next 7 days.")
    else:
        lines.append(f"  {'Date':<12} {'When':<6} {'Ticker':<10} {'Event':<50} {'Pri':<8}")
        lines.append("  " + "-" * 80)
        for ev in upcoming:
            pri_str = ev['priority'].upper() if ev['priority'] else ''
            lines.append(f"  {str(ev['date']):<12} {ev['day_label']:<6} {ev['ticker']:<10} {ev['event']:<50} {pri_str:<8}")
            if ev['action']:
                lines.append(f"  {'':>30} {ev['action']}")

    lines.append(f"  {len(upcoming)} events in window")

    return '\n'.join(lines), today_earnings


# ---------------------------------------------------------------------------
# SECTION 4: Forward Returns (compact)
# ---------------------------------------------------------------------------
def section_forward_returns(portfolio, prices, rates):
    """Render forward returns section. Returns (text, negative_return_tickers)."""
    positions = portfolio.get('positions', [])
    negative_ret = []

    rows = []
    for p in positions:
        ticker = p['ticker']
        pd = prices.get(ticker)
        if not pd:
            rows.append({'ticker': ticker, 'error': True})
            continue

        price = pd['price']
        currency = pd['currency']
        div_yield = pd.get('div_yield_pct', 0)

        fv_raw, fv_currency = parse_fair_value(p.get('fair_value'))
        if fv_raw is None:
            rows.append({'ticker': ticker, 'price': price, 'fv': None, 'mos': None, 'ecagr': None, 'currency': currency})
            continue

        # Convert FV to stock currency
        fv_in_stock = convert_fv_to_stock_currency(fv_raw, fv_currency, currency, rates)
        mos_pct = ((fv_in_stock - price) / price) * 100

        # E[CAGR] = (FV/Price)^(1/3) - 1 + growth + div_yield
        # Growth: try to extract from thesis, fallback to 0
        growth_pct = _extract_growth_from_thesis(ticker)
        ratio = fv_in_stock / price if price > 0 else 1
        mos_cagr = (ratio ** (1.0 / 3.0)) - 1.0
        ecagr = (mos_cagr + (growth_pct or 0) / 100.0 + div_yield / 100.0) * 100.0

        if ecagr < 0:
            negative_ret.append(ticker)

        rows.append({
            'ticker': ticker,
            'price': price,
            'currency': currency,
            'fv': fv_raw,
            'fv_currency': fv_currency,
            'mos': mos_pct,
            'growth': growth_pct,
            'div_yield': div_yield,
            'ecagr': ecagr,
        })

    # Sort by E[CAGR] descending
    valid = [r for r in rows if r.get('ecagr') is not None]
    invalid = [r for r in rows if r.get('ecagr') is None]
    valid.sort(key=lambda x: x['ecagr'], reverse=True)

    lines = []
    lines.append("")
    lines.append("=" * 86)
    lines.append("  4. FORWARD RETURNS")
    lines.append("=" * 86)
    lines.append(f"  {'Ticker':<10} {'Price':>10} {'FV':>10} {'MoS%':>7} {'Grw%':>6} {'Yld%':>6} {'E[CAGR]':>8}")
    lines.append("  " + "-" * 62)

    for i, r in enumerate(valid):
        fv_str = f"{r['fv']:.0f}{r['fv_currency'] or ''}" if r['fv'] else 'N/A'
        mos_str = f"{r['mos']:+.1f}" if r['mos'] is not None else 'N/A'
        grw_str = f"{r['growth']:.1f}" if r['growth'] is not None else '?'
        yld_str = f"{r['div_yield']:.1f}" if r['div_yield'] else '0.0'
        ecagr_str = f"{r['ecagr']:.1f}%"

        # Flag bottom 3
        suffix = ''
        if i >= len(valid) - 3:
            suffix = ' <-- bottom 3'

        lines.append(f"  {r['ticker']:<10} {r['price']:>10.2f} {fv_str:>10} {mos_str:>7} {grw_str:>6} {yld_str:>6} {ecagr_str:>8}{suffix}")

    for r in invalid:
        if r.get('error'):
            lines.append(f"  {r['ticker']:<10} {'ERROR':>10}")
        else:
            lines.append(f"  {r['ticker']:<10} {r.get('price', 0):>10.2f} {'N/A':>10} {'N/A':>7}")

    lines.append("  " + "-" * 62)
    lines.append(f"  E[CAGR] = (FV/Price)^(1/3) - 1 + Growth + Yield")

    return '\n'.join(lines), negative_ret


def _extract_growth_from_thesis(ticker):
    """Quick extraction of growth rate from thesis file. Returns pct or None."""
    thesis_path = os.path.join(THESIS_ACTIVE_DIR, ticker, 'thesis.md')
    if not os.path.exists(thesis_path):
        return None
    try:
        with open(thesis_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        return None

    patterns = [
        (r'Expected Growth[^:]*:\s*(?:~)?(\d+(?:\.\d+)?)\s*%', 'single'),
        (r'Revenue Growth Base:\s*(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)\s*%', 'range'),
        (r'GP Growth[^:]*:\s*(?:~)?(\d+(?:\.\d+)?)\s*%', 'single'),
        (r'GP CAGR[):\s]+(?:~)?(\d+(?:\.\d+)?)\s*%\s*\(base', 'single'),
        (r'(?:Expected )?Growth:\s*(\d+(?:\.\d+)?)\s*%', 'single'),
        (r'Revenue Growth:\s*(?:~)?(\d+(?:\.\d+)?)\s*%', 'single'),
        (r'growth of\s*(?:~)?(\d+(?:\.\d+)?)\s*%', 'single'),
    ]
    for pat, pat_type in patterns:
        m = re.search(pat, content, re.IGNORECASE)
        if m:
            groups = m.groups()
            if pat_type == 'range' and len(groups) >= 2:
                try:
                    return (float(groups[0]) + float(groups[1])) / 2
                except ValueError:
                    continue
            else:
                try:
                    val = float(groups[0])
                    if -50 <= val <= 50:
                        return val
                except ValueError:
                    continue
    return None


# ---------------------------------------------------------------------------
# SECTION 5: Pipeline Health
# ---------------------------------------------------------------------------
def section_pipeline_health(universe_data):
    """Render pipeline health section."""
    companies = universe_data.get('quality_universe', {}).get('companies', [])

    counts = {}
    for c in companies:
        status = c.get('pipeline_status', 'UNKNOWN')
        counts[status] = counts.get(status, 0) + 1

    total = len(companies)
    scored = counts.get('SCORED', 0)
    r1 = counts.get('R1_COMPLETE', 0)
    r3 = counts.get('R3_COMPLETE', 0)
    approved = counts.get('APPROVED', 0)
    so = counts.get('STANDING_ORDER', 0)
    other = total - scored - r1 - r3 - approved - so

    # Tier breakdown
    tiers = {}
    for c in companies:
        t = c.get('tier', '?')
        tiers[t] = tiers.get(t, 0) + 1

    lines = []
    lines.append("")
    lines.append("=" * 86)
    lines.append("  5. PIPELINE HEALTH")
    lines.append("=" * 86)
    lines.append(f"  Universe: {total} companies | "
                 f"Tier A: {tiers.get('A', 0)} | Tier B: {tiers.get('B', 0)} | Tier C: {tiers.get('C', 0)}")
    lines.append(f"  Pipeline: {scored} SCORED | {r1} R1_COMPLETE | {r3} R3_COMPLETE | {approved} APPROVED | {so} STANDING_ORDER")

    advanced = r1 + r3 + approved + so
    if advanced < 3:
        lines.append(f"  WARNING: Pipeline thin ({advanced} advanced) - need more R1 completions")
    else:
        lines.append(f"  Pipeline depth OK: {advanced} at R1+ stage")

    return '\n'.join(lines)


# ---------------------------------------------------------------------------
# SECTION 6: Alerts
# ---------------------------------------------------------------------------
def section_alerts(triggered_so, near_so, today_earnings, negative_ret, cash_pct):
    """Render alerts section."""
    lines = []
    lines.append("")
    lines.append("=" * 86)
    lines.append("  6. ALERTS")
    lines.append("=" * 86)

    has_alerts = False

    if triggered_so:
        has_alerts = True
        lines.append("  >>> ACTION REQUIRED: STANDING ORDERS TRIGGERED <<<")
        for t in triggered_so:
            lines.append(f"      {t}")

    if today_earnings:
        has_alerts = True
        lines.append(f"  >>> EARNINGS TODAY: {', '.join(today_earnings)} <<<")

    if near_so:
        has_alerts = True
        lines.append("  NEAR TRIGGER:")
        for n in near_so:
            lines.append(f"      {n}")

    if negative_ret:
        has_alerts = True
        lines.append(f"  NEGATIVE E[CAGR]: {', '.join(negative_ret)} -- rotation candidates")

    if cash_pct > 50:
        has_alerts = True
        lines.append(f"  CASH DRAG WARNING: {cash_pct:.1f}% cash -- requires justification (P14)")

    if not has_alerts:
        lines.append("  No critical alerts.")

    return '\n'.join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(description='Session Opener - Phase 0-1 Initialization Briefing')
    parser.add_argument('--quick', action='store_true',
                        help='Quick mode: only Standing Orders + Earnings + Alerts (sections 2, 3, 6)')
    args = parser.parse_args()

    start_time = datetime.now()
    print()
    print("=" * 86)
    print(f"  SESSION OPENER -- {start_time.strftime('%Y-%m-%d %H:%M')}")
    print("=" * 86)

    # Load all data files
    portfolio = load_yaml(PORTFOLIO_FILE)
    so_data = load_yaml(SO_FILE)
    calendar_data = load_yaml(CALENDAR_FILE)
    universe_data = load_yaml(UNIVERSE_FILE)

    # Collect all tickers we need prices for
    position_tickers = [p['ticker'] for p in portfolio.get('positions', [])]
    short_tickers = [s['ticker'] for s in (portfolio.get('short_positions', []) or [])]

    so_tickers = []
    for order in so_data.get('standing_orders', []):
        t = order.get('ticker', '')
        if t and t not in so_tickers:
            so_tickers.append(t)
    for order in (so_data.get('short_orders', []) or []):
        if isinstance(order, dict):
            t = order.get('ticker', '')
            if t and t not in so_tickers:
                so_tickers.append(t)

    all_tickers = list(set(position_tickers + short_tickers + so_tickers))

    # Single batch of FX + price fetches
    print(f"  Loading FX rates...")
    rates = get_fx_rates()
    print(f"  FX: EUR/USD={rates['EURUSD']:.4f} | GBP/EUR={rates['GBPEUR']:.4f} | "
          f"DKK/EUR={rates['DKKEUR']:.4f} | CHF/EUR={rates.get('CHFEUR', 0):.4f}")

    print(f"  Fetching prices for {len(all_tickers)} tickers...")
    prices = batch_fetch_prices(all_tickers, rates)
    print(f"  Got {len(prices)}/{len(all_tickers)} prices.")

    # Generate sections
    if args.quick:
        # Quick mode: sections 2, 3, 6 only
        so_text, triggered, near = section_standing_orders(so_data, prices, rates)
        earnings_text, today_earn = section_earnings(calendar_data)
        alerts_text = section_alerts(triggered, near, today_earn, [], 0)

        print(so_text)
        print(earnings_text)
        print(alerts_text)
    else:
        # Full mode: all 6 sections
        portfolio_text, cash_pct, total_pnl = section_portfolio_snapshot(portfolio, prices, rates)
        so_text, triggered, near = section_standing_orders(so_data, prices, rates)
        earnings_text, today_earn = section_earnings(calendar_data)
        fwd_text, negative_ret = section_forward_returns(portfolio, prices, rates)
        pipeline_text = section_pipeline_health(universe_data)
        alerts_text = section_alerts(triggered, near, today_earn, negative_ret, cash_pct)

        print(portfolio_text)
        print(so_text)
        print(earnings_text)
        print(fwd_text)
        print(pipeline_text)
        print(alerts_text)

    # Footer
    elapsed = (datetime.now() - start_time).total_seconds()
    print()
    print(f"  [Raw data. Session initialization context. Completed in {elapsed:.1f}s]")
    print()


if __name__ == '__main__':
    main()
