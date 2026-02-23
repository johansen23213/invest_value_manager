#!/usr/bin/env python3
"""
Thesis Monitor - Automated thesis assumption checker.

Reads each active thesis, extracts key assumptions (kill conditions, scenarios,
fair value), compares with current data, and generates divergence alerts.
Detects thesis drift BEFORE it becomes a loss.

For each active position in portfolio/current.yaml:
  1. Price vs Thesis: MoS%, P&L%, overvalued/thin/deep flags
  2. Kill Condition Proximity: extract KCs, flag APPROACHING/ELEVATED
  3. Conviction Drift: review staleness, probation status, LOW held too long
  4. Scenario Assessment: price vs bear/bull FV
  5. Portfolio-Level Alerts: concentration, conviction distribution

Usage:
  python3 tools/thesis_monitor.py              # Full monitor
  python3 tools/thesis_monitor.py --alerts     # Only show alerts section
  python3 tools/thesis_monitor.py --ticker X   # Monitor single position
"""

import sys
import os
import re
import argparse
import yaml
import yfinance as yf
from datetime import datetime, date
import warnings
warnings.filterwarnings('ignore')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORTFOLIO_FILE = os.path.join(BASE_DIR, 'portfolio', 'current.yaml')
THESIS_ACTIVE_DIR = os.path.join(BASE_DIR, 'thesis', 'active')

TODAY = date.today()


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_portfolio():
    """Load portfolio from current.yaml."""
    try:
        with open(PORTFOLIO_FILE, 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"ERROR: Cannot load portfolio: {e}")
        sys.exit(1)


def get_fx_rates():
    """Get EUR/USD and GBP/EUR exchange rates with fallbacks."""
    defaults = {'EURUSD': 1.04, 'GBPEUR': 1.19, 'DKKEUR': 0.134}
    fallbacks_used = []
    rates = {}

    for pair, key, default in [
        ('EURUSD=X', 'EURUSD', defaults['EURUSD']),
        ('GBPEUR=X', 'GBPEUR', defaults['GBPEUR']),
        ('DKKEUR=X', 'DKKEUR', defaults['DKKEUR']),
    ]:
        try:
            val = yf.Ticker(pair).info.get('previousClose')
            if not val:
                val = default
                fallbacks_used.append(f"{key}={val}")
        except Exception:
            val = default
            fallbacks_used.append(f"{key}={val}")
        rates[key] = val

    if fallbacks_used:
        print(f"FX WARNING: Using static fallback ({', '.join(fallbacks_used)})")

    return rates


def read_thesis(ticker):
    """Read thesis file for an active position. Returns content string or None."""
    thesis_path = os.path.join(THESIS_ACTIVE_DIR, ticker, 'thesis.md')
    if not os.path.exists(thesis_path):
        return None
    try:
        with open(thesis_path, 'r') as f:
            return f.read()
    except Exception:
        return None


def batch_fetch_prices(tickers, fx):
    """Fetch current price for all tickers. Returns dict {ticker: {price, currency, price_eur}}."""
    TICKER_MAP = {'LIGHT.NV': 'LIGHT.AS'}
    results = {}
    for ticker in tickers:
        yf_ticker = TICKER_MAP.get(ticker, ticker)
        try:
            info = yf.Ticker(yf_ticker).info
            price = info.get('currentPrice') or info.get('regularMarketPrice') or info.get('previousClose')
            currency = info.get('currency', 'USD')
            if price is None:
                results[ticker] = None
                continue
            price_eur = convert_to_eur(price, currency, fx)
            results[ticker] = {
                'price': price,
                'currency': currency,
                'price_eur': price_eur,
            }
        except Exception:
            results[ticker] = None
    return results


# ---------------------------------------------------------------------------
# Currency conversion
# ---------------------------------------------------------------------------

def convert_to_eur(value, currency, fx):
    """Convert a value from its native currency to EUR."""
    if currency == 'EUR':
        return value
    elif currency == 'USD':
        return value / fx['EURUSD']
    elif currency in ('GBp', 'GBX'):
        return (value / 100) * fx['GBPEUR']
    elif currency == 'GBP':
        return value * fx['GBPEUR']
    elif currency == 'DKK':
        return value * fx['DKKEUR']
    elif currency == 'SEK':
        return value * 0.088
    return value


def convert_fv_to_price_currency(fv, fv_currency, stock_currency, fx):
    """Convert fair value to the stock's trading currency for MoS calculation."""
    if fv_currency == stock_currency:
        return fv

    # Convert to EUR first
    fv_eur = convert_to_eur(fv, fv_currency, fx)

    # Convert from EUR to target
    if stock_currency == 'EUR':
        return fv_eur
    elif stock_currency == 'USD':
        return fv_eur * fx['EURUSD']
    elif stock_currency in ('GBp', 'GBX'):
        return (fv_eur / fx['GBPEUR']) * 100
    elif stock_currency == 'GBP':
        return fv_eur / fx['GBPEUR']
    elif stock_currency == 'DKK':
        return fv_eur / fx['DKKEUR'] if fx['DKKEUR'] else fv_eur
    elif stock_currency == 'SEK':
        return fv_eur / 0.088
    return fv_eur


# ---------------------------------------------------------------------------
# Fair Value parsing (from portfolio/current.yaml fair_value field)
# ---------------------------------------------------------------------------

def parse_fair_value_from_portfolio(fv_str):
    """Parse fair_value string from current.yaml.

    Handles: "EUR 35.00 (...)", "190 GBp (...)", "$191 (...)", etc.
    Returns (value, currency) or (None, None).
    """
    if not fv_str:
        return None, None

    patterns = [
        (r'EUR\s+([0-9,]+(?:\.\d+)?)', 'EUR'),
        (r'\$\s*([0-9,]+(?:\.\d+)?)', 'USD'),
        (r'([0-9,]+(?:\.\d+)?)\s*GBp', 'GBp'),
        (r'DKK\s+([0-9,]+(?:\.\d+)?)', 'DKK'),
        (r'SEK\s+([0-9,]+(?:\.\d+)?)', 'SEK'),
    ]
    for pat, curr in patterns:
        m = re.match(pat, fv_str)
        if m:
            return float(m.group(1).replace(',', '')), curr

    # Bare number fallback
    m = re.match(r'([0-9,]+(?:\.\d+)?)', fv_str)
    if m:
        return float(m.group(1).replace(',', '')), 'USD'

    return None, None


# ---------------------------------------------------------------------------
# Kill Condition extraction from thesis
# ---------------------------------------------------------------------------

def extract_kill_conditions(thesis_content):
    """Extract kill conditions from thesis text.

    Finds KC sections, parses numbered items, and detects status markers
    (APPROACHING/ELEVATED/TRIGGERED) from the full line text and from
    explicit table rows elsewhere in the thesis.

    Returns list of dicts: {number, text, status}.
    """
    if not thesis_content:
        return []

    kcs = []
    seen_numbers = set()

    # Find the Kill Conditions section(s) -- bounded by next header or ---
    kc_sections = []
    for m in re.finditer(r'#+\s*(?:Kill Conditions|Updated Kill Conditions|Model Disruption Kill Conditions)[^\n]*\n', thesis_content, re.IGNORECASE):
        start = m.end()
        next_boundary = re.search(r'\n(?:##\s|---)', thesis_content[start:])
        end = start + next_boundary.start() if next_boundary else len(thesis_content)
        kc_sections.append(thesis_content[start:end])

    for section in kc_sections:
        # Process each line that starts with "N. " (numbered kill condition)
        for m in re.finditer(r'^(\d+)\.\s+(.+)$', section, re.MULTILINE):
            num = int(m.group(1))
            if num in seen_numbers:
                continue
            full_line = m.group(2).strip()

            # Extract the KC name (the bold text)
            name_match = re.match(r'\*{2}(.+?)\*{2}', full_line)
            if name_match:
                text = name_match.group(1).strip()
            else:
                text = full_line[:80]

            # Detect status from the FULL line (after the name)
            status = _detect_status_in_line(full_line)

            kcs.append({'number': num, 'text': text[:120], 'status': status})
            seen_numbers.add(num)

    # Also scan for explicit status in table rows elsewhere in thesis:
    # "| N | text | APPROACHING |" or "| N | text | ELEVATED | context |"
    for m in re.finditer(r'\|\s*(\d+)\s*\|[^|]*?\|\s*(APPROACHING|ELEVATED|TRIGGERED)\s*\|', thesis_content, re.IGNORECASE):
        num = int(m.group(1))
        status = m.group(2).upper()
        _update_kc_status(kcs, seen_numbers, num, status)

    return sorted(kcs, key=lambda x: x['number'])


def _detect_status_in_line(line):
    """Detect KC status from a full line of text.

    Looks for APPROACHING/ELEVATED/TRIGGERED as standalone markers,
    typically in bold (**APPROACHING**) or after -- delimiter.
    """
    upper = line.upper()
    # Look for explicit status markers (bold or after --)
    if re.search(r'\*{2}TRIGGERED\*{2}|--\s*TRIGGERED\b', upper):
        return 'TRIGGERED'
    if re.search(r'\*{2}ELEVATED\*{2}|--\s*ELEVATED\b', upper):
        return 'ELEVATED'
    if re.search(r'\*{2}APPROACHING\*{2}|--\s*APPROACHING\b', upper):
        return 'APPROACHING'
    if re.search(r'\*{2}PENDING\*{2}|--\s*PENDING\b', upper):
        return 'NORMAL'
    return 'NORMAL'


def _update_kc_status(kcs, seen_numbers, num, status):
    """Update KC status if new status is more severe, or add new KC."""
    for kc in kcs:
        if kc['number'] == num:
            if _status_priority(status) > _status_priority(kc['status']):
                kc['status'] = status
            return
    kcs.append({'number': num, 'text': f'(KC#{num} - see thesis)', 'status': status})
    seen_numbers.add(num)


def _status_priority(status):
    """Higher = more severe."""
    return {'NORMAL': 0, 'APPROACHING': 1, 'ELEVATED': 2, 'TRIGGERED': 3}.get(status, 0)


# ---------------------------------------------------------------------------
# Scenario extraction from thesis (Bear / Bull FV)
# ---------------------------------------------------------------------------

def extract_scenario_fvs(thesis_content, ticker):
    """Extract bear and bull case fair values from thesis.

    Two-phase strategy:
    1. Find all lines containing "Bear FV", "Fair Value Bear", etc.
    2. From each matching line, extract the best value (prefer **bold** values
       which indicate the latest revision in comparison tables).
    3. Take the latest match by document position.

    Returns (bear_fv, bull_fv, bear_currency, bull_currency).
    """
    if not thesis_content:
        return None, None, None, None

    bear_fv, bear_curr = _extract_scenario('bear', thesis_content, ticker)
    bull_fv, bull_curr = _extract_scenario('bull', thesis_content, ticker)

    return bear_fv, bull_fv, bear_curr, bull_curr


def _extract_scenario(scenario_type, content, ticker):
    """Extract a single scenario (bear or bull) FV. Returns (value, currency)."""
    if scenario_type == 'bear':
        line_pats = [r'^.*(?:Fair Value Bear|Bear (?:Case )?FV|Bear FV|Bear Case|Bear Floor).*$']
    else:
        line_pats = [r'^.*(?:Fair Value Bull|Bull (?:Case )?FV|Bull FV|Bull Case).*$']

    best_val = None
    best_curr = None
    best_pos = -1

    for line_pat in line_pats:
        for m in re.finditer(line_pat, content, re.IGNORECASE | re.MULTILINE):
            line = m.group(0)
            line_pos = m.start()

            # Skip non-FV lines (MoS comparisons, commentary, etc.)
            lower = line.lower()
            if any(skip in lower for skip in ['mos vs', 'may be', 'downside', 'underwater', 'could lose', 'probability']):
                continue

            val, curr = _extract_value_from_line(line, ticker)
            if val is not None and val > 0 and line_pos > best_pos:
                best_pos = line_pos
                best_val = val
                best_curr = curr

    return best_val, best_curr


def _extract_value_from_line(line, ticker):
    """Extract the best FV value from a single line.

    Preference: bold values (**X**) first, then last currency-annotated value.
    Returns (value, currency) or (None, None).
    """
    # Phase 1: Bold values: **$240** or **133 GBp** or **EUR 20.0**
    bold_matches = list(re.finditer(
        r'\*{2}\s*(?:EUR\s+)?(?:\$)?\s*([0-9,]+(?:\.\d+)?)\s*(?:GBp|EUR|DKK|SEK)?\s*\*{2}',
        line, re.IGNORECASE
    ))
    if bold_matches:
        m = bold_matches[0]
        try:
            val = float(m.group(1).replace(',', ''))
            if val > 0:
                return val, _detect_currency_in_text(m.group(0), line, ticker)
        except ValueError:
            pass

    # Phase 2: Currency-annotated values, take the last one
    all_values = []
    value_pats = [
        (r'\$\s*([0-9,]+(?:\.\d+)?)', 'USD'),
        (r'EUR\s+([0-9,]+(?:\.\d+)?)', 'EUR'),
        (r'([0-9,]+(?:\.\d+)?)\s*GBp', 'GBp'),
        (r'DKK\s+([0-9,]+(?:\.\d+)?)', 'DKK'),
        (r'SEK\s+([0-9,]+(?:\.\d+)?)', 'SEK'),
    ]

    for pat, curr in value_pats:
        for m in re.finditer(pat, line, re.IGNORECASE):
            try:
                val = float(m.group(1).replace(',', ''))
                if val > 0:
                    all_values.append((m.start(), val, curr))
            except ValueError:
                continue

    # Also bare numbers followed by 'p' (pence)
    for m in re.finditer(r'[:\s=]\s*([0-9,]+(?:\.\d+)?)\s*p\b', line):
        try:
            val = float(m.group(1).replace(',', ''))
            if val > 0:
                all_values.append((m.start(), val, 'GBp'))
        except ValueError:
            continue

    if all_values:
        all_values.sort(key=lambda x: x[0])
        _, val, curr = all_values[-1]
        return val, curr

    return None, None


def _detect_currency_in_text(match_text, line, ticker):
    """Detect currency from matched text or surrounding line."""
    if '$' in match_text:
        return 'USD'
    if 'EUR' in match_text:
        return 'EUR'
    lower = match_text.lower()
    if 'gbp' in lower or match_text.rstrip('*').rstrip().endswith('p'):
        return 'GBp'
    if 'DKK' in match_text:
        return 'DKK'
    if 'SEK' in match_text:
        return 'SEK'
    # Check the line context
    if 'GBp' in line:
        return 'GBp'
    if '$' in line:
        return 'USD'
    if 'EUR' in line:
        return 'EUR'
    return _infer_currency_from_ticker(ticker)


def _infer_currency_from_ticker(ticker):
    """Infer native currency from ticker suffix."""
    if ticker.endswith('.L'):
        return 'GBp'
    elif ticker.endswith('.PA') or ticker.endswith('.DE') or ticker.endswith('.MI'):
        return 'EUR'
    elif ticker.endswith('.CO'):
        return 'DKK'
    elif ticker.endswith('.ST'):
        return 'SEK'
    else:
        return 'USD'


# ---------------------------------------------------------------------------
# Country detection
# ---------------------------------------------------------------------------

def detect_country(ticker):
    """Detect country from ticker suffix."""
    suffix_map = {
        '.L': 'UK', '.PA': 'FR', '.DE': 'DE', '.MI': 'IT',
        '.MC': 'ES', '.AS': 'NL', '.CO': 'DK', '.ST': 'SE',
        '.HE': 'FI', '.OL': 'NO', '.SW': 'CH',
    }
    for suffix, country in suffix_map.items():
        if ticker.endswith(suffix):
            return country
    return 'US'


# ---------------------------------------------------------------------------
# Position analysis
# ---------------------------------------------------------------------------

def analyze_position(pos, price_data, fx, thesis_content):
    """Analyze a single position. Returns dict with all monitoring data."""
    ticker = pos['ticker']
    result = {
        'ticker': ticker,
        'name': pos.get('name', ticker),
        'price': None,
        'currency': None,
        'fv': None,
        'fv_currency': None,
        'fv_in_price_curr': None,
        'mos_pct': None,
        'pnl_pct': None,
        'conviction': (pos.get('conviction') or 'medium').lower(),
        'last_review': pos.get('last_review'),
        'days_since_review': None,
        'on_probation': False,
        'exit_plan': pos.get('exit_plan', ''),
        'kill_conditions': [],
        'kc_alerts': [],
        'bear_fv': None,
        'bull_fv': None,
        'bear_flag': None,
        'bull_flag': None,
        'price_flag': None,
        'review_overdue': False,
        'low_conviction_stale': False,
        'country': detect_country(ticker),
        'alerts': [],
        'error': None,
    }

    # Price data
    if price_data is None:
        result['error'] = 'No price data'
        return result

    result['price'] = price_data['price']
    result['currency'] = price_data['currency']

    # Fair Value from portfolio
    fv_str = pos.get('fair_value', '')
    fv, fv_curr = parse_fair_value_from_portfolio(fv_str)
    result['fv'] = fv
    result['fv_currency'] = fv_curr

    if fv is not None and fv_curr is not None:
        fv_in_price = convert_fv_to_price_currency(fv, fv_curr, result['currency'], fx)
        result['fv_in_price_curr'] = fv_in_price
        if result['price'] > 0:
            result['mos_pct'] = ((fv_in_price - result['price']) / fv_in_price) * 100

    # P&L calculation
    avg_cost_usd = pos.get('avg_cost_usd')
    if avg_cost_usd and result['price']:
        price_usd = result['price']
        curr = result['currency']
        if curr == 'EUR':
            price_usd = result['price'] * fx['EURUSD']
        elif curr in ('GBp', 'GBX'):
            gbpusd = fx['GBPEUR'] * fx['EURUSD']
            price_usd = (result['price'] / 100) * gbpusd
        elif curr == 'GBP':
            gbpusd = fx['GBPEUR'] * fx['EURUSD']
            price_usd = result['price'] * gbpusd
        elif curr == 'DKK':
            price_usd = result['price'] * fx['DKKEUR'] * fx['EURUSD']

        if avg_cost_usd > 0:
            result['pnl_pct'] = ((price_usd - avg_cost_usd) / avg_cost_usd) * 100

    # Price flags
    if result['mos_pct'] is not None:
        mos = result['mos_pct']
        if mos < 0:
            result['price_flag'] = 'OVERVALUED'
        elif mos < 10:
            result['price_flag'] = 'THIN MoS'
        elif mos > 40:
            result['price_flag'] = 'DEEP VALUE'
        else:
            result['price_flag'] = 'OK'

    # Last review analysis
    if result['last_review']:
        try:
            if isinstance(result['last_review'], str):
                lr = datetime.strptime(result['last_review'], '%Y-%m-%d').date()
            elif isinstance(result['last_review'], date):
                lr = result['last_review']
            else:
                lr = None
            if lr:
                result['days_since_review'] = (TODAY - lr).days
                if result['days_since_review'] > 30:
                    result['review_overdue'] = True
                if result['conviction'] == 'low' and result['days_since_review'] > 60:
                    result['low_conviction_stale'] = True
        except (ValueError, TypeError):
            pass

    # Probation detection from portfolio fields
    exit_plan = str(pos.get('exit_plan', '')).upper()
    notes = str(pos.get('notes', '')).upper()
    if 'PROBATION' in exit_plan or 'PROBATION' in notes:
        result['on_probation'] = True

    # Kill conditions
    kcs = extract_kill_conditions(thesis_content)
    result['kill_conditions'] = kcs
    result['kc_alerts'] = [kc for kc in kcs if kc['status'] in ('APPROACHING', 'ELEVATED', 'TRIGGERED')]

    # Scenario assessment
    bear_fv, bull_fv, bear_curr, bull_curr = extract_scenario_fvs(thesis_content, ticker)
    if bear_fv:
        bear_curr = bear_curr or fv_curr or _infer_currency_from_ticker(ticker)
        bear_in_price = convert_fv_to_price_currency(bear_fv, bear_curr, result['currency'], fx)
        result['bear_fv'] = bear_in_price
        if result['price'] and result['price'] < bear_in_price:
            result['bear_flag'] = 'BELOW BEAR CASE'
    if bull_fv:
        bull_curr = bull_curr or fv_curr or _infer_currency_from_ticker(ticker)
        bull_in_price = convert_fv_to_price_currency(bull_fv, bull_curr, result['currency'], fx)
        result['bull_fv'] = bull_in_price
        if result['price'] and result['price'] > bull_in_price:
            result['bull_flag'] = 'ABOVE BULL CASE'

    # Compile alerts
    if result['on_probation']:
        prob_detail = ''
        if result['conviction'] == 'low':
            prob_detail = f", LOW conviction"
        trigger_match = re.search(r'(?:exit trigger|hard exit)\s+(\d+\s*(?:GBp|p|USD|\$|EUR))', str(pos.get('exit_plan', '')), re.IGNORECASE)
        if trigger_match:
            prob_detail += f", exit trigger {trigger_match.group(1)}"
        result['alerts'].append(f"ON PROBATION{prob_detail}")

    if result['price_flag'] == 'OVERVALUED':
        result['alerts'].append(f"OVERVALUED: MoS {result['mos_pct']:+.1f}%")
    elif result['price_flag'] == 'THIN MoS':
        result['alerts'].append(f"THIN MoS: {result['mos_pct']:+.1f}%")

    if result['review_overdue']:
        result['alerts'].append(f"Review overdue ({result['days_since_review']}d)")

    if result['low_conviction_stale']:
        result['alerts'].append(f"LOW conviction held {result['days_since_review']}d without review")

    if result['bear_flag']:
        result['alerts'].append(result['bear_flag'])

    if result['bull_flag']:
        result['alerts'].append(result['bull_flag'])

    for kc in result['kc_alerts']:
        result['alerts'].append(f"KC#{kc['number']} {kc['status']}")

    return result


# ---------------------------------------------------------------------------
# Output formatting
# ---------------------------------------------------------------------------

def print_full_report(results, alerts_only=False):
    """Print the thesis monitor report."""
    today_str = TODAY.strftime('%Y-%m-%d')
    n = len(results)

    print()
    print(f"=== THESIS MONITOR | {today_str} ===")
    print(f"{n} positions monitored")

    # --- ALERTS ---
    alert_positions = [r for r in results if r['alerts']]
    alert_positions.sort(key=lambda r: len(r['alerts']), reverse=True)

    print()
    if alert_positions:
        print("ALERTS (action required):")
        for r in alert_positions:
            for alert in r['alerts']:
                sev = "!!!" if any(x in alert for x in ['TRIGGERED', 'OVERVALUED', 'BELOW BEAR']) else "<!>"
                print(f"  {sev} {r['ticker']}: {alert}")
    else:
        print("ALERTS: None -- all positions nominal.")

    if alerts_only:
        print()
        print("[Raw data. Thesis monitoring context.]")
        return

    # --- POSITION HEALTH ---
    print()
    w = 120
    print("=" * w)
    print("POSITION HEALTH")
    print("=" * w)
    print(f"  {'Ticker':<10} {'Price':>10} {'FV':>10} {'MoS%':>7} {'P&L%':>7} {'Conv':>5} {'Last Review':>12} {'Days':>5} {'Status'}")
    print("  " + "-" * (w - 2))

    def sort_key(r):
        alert_count = len(r['alerts'])
        mos = r['mos_pct'] if r['mos_pct'] is not None else 999
        return (-alert_count, mos)

    for r in sorted(results, key=sort_key):
        if r['error']:
            print(f"  {r['ticker']:<10} {'ERR':>10} {'':>10} {'':>7} {'':>7} {'':>5} {'':>12} {'':>5} {r['error']}")
            continue

        price_str = f"{r['price']:.2f}" if r['price'] else 'N/A'
        fv_str = f"{r['fv']:.0f}" if r['fv'] else 'N/A'
        mos_str = f"{r['mos_pct']:+.1f}" if r['mos_pct'] is not None else 'N/A'
        pnl_str = f"{r['pnl_pct']:+.1f}" if r['pnl_pct'] is not None else 'N/A'
        conv_str = r['conviction'][0].upper() if r['conviction'] else '?'
        review_str = str(r['last_review']) if r['last_review'] else 'never'
        days_str = str(r['days_since_review']) if r['days_since_review'] is not None else '?'

        status_parts = []
        if r['on_probation']:
            status_parts.append('PROBATION')
        if r['price_flag'] and r['price_flag'] != 'OK':
            status_parts.append(r['price_flag'])
        if r['review_overdue']:
            status_parts.append('REVIEW DUE')
        if r['bear_flag']:
            status_parts.append(r['bear_flag'])
        if r['bull_flag']:
            status_parts.append(r['bull_flag'])
        if not status_parts:
            status_parts.append('OK')
        status = ' | '.join(status_parts)

        print(f"  {r['ticker']:<10} {price_str:>10} {fv_str:>10} {mos_str:>7} {pnl_str:>7} {conv_str:>5} {review_str:>12} {days_str:>5} {status}")

    print("  " + "-" * (w - 2))

    # --- KILL CONDITION WATCH ---
    kc_positions = [r for r in results if r['kc_alerts']]
    print()
    print("KILL CONDITION WATCH:")
    if kc_positions:
        for r in kc_positions:
            for kc in r['kc_alerts']:
                marker = "***" if kc['status'] == 'TRIGGERED' else "<!>"
                print(f"  {marker} {r['ticker']}: KC#{kc['number']} ({kc['text'][:80]}) -- {kc['status']}")
    else:
        print("  No kill conditions approaching or elevated.")

    # --- SCENARIO FLAGS ---
    scenario_flags = [r for r in results if r['bear_flag'] or r['bull_flag']]
    if scenario_flags:
        print()
        print("SCENARIO FLAGS:")
        for r in scenario_flags:
            if r['bear_flag']:
                print(f"  {r['ticker']}: Price {r['price']:.2f} < Bear FV {r['bear_fv']:.2f} -- {r['bear_flag']}")
            if r['bull_flag']:
                print(f"  {r['ticker']}: Price {r['price']:.2f} > Bull FV {r['bull_fv']:.2f} -- {r['bull_flag']}")

    # --- CONVICTION SUMMARY ---
    print()
    print("CONVICTION SUMMARY:")
    conv_counts = {'high': 0, 'medium': 0, 'low': 0}
    probation_list = []
    review_days = []

    for r in results:
        conv = r['conviction']
        conv_counts[conv] = conv_counts.get(conv, 0) + 1
        if r['on_probation']:
            probation_list.append(r['ticker'])
        if r['days_since_review'] is not None:
            review_days.append(r['days_since_review'])

    avg_review = sum(review_days) / len(review_days) if review_days else 0
    overdue = [r['ticker'] for r in results if r['review_overdue']]

    print(f"  HIGH: {conv_counts['high']} | MEDIUM: {conv_counts['medium']} | LOW: {conv_counts['low']}")
    if probation_list:
        print(f"  ON PROBATION: {len(probation_list)} ({', '.join(probation_list)})")
    else:
        print(f"  ON PROBATION: 0")
    print(f"  Avg days since review: {avg_review:.1f}")
    if overdue:
        print(f"  Overdue (>30d): {len(overdue)} ({', '.join(overdue)})")
    else:
        print(f"  Overdue (>30d): 0")

    # --- CONCENTRATION ---
    print()
    print("CONCENTRATION:")
    country_positions = {}
    for r in results:
        c = r['country']
        if c not in country_positions:
            country_positions[c] = []
        country_positions[c].append(r)

    for country, positions in sorted(country_positions.items(), key=lambda x: -len(x[1])):
        tickers = [r['ticker'] for r in positions]
        prob_count = sum(1 for r in positions if r['on_probation'])
        prob_note = f" -- {prob_count} on probation" if prob_count else ""
        if len(tickers) >= 3:
            print(f"  {country}: {len(tickers)} positions ({', '.join(tickers)}){prob_note}")
        else:
            print(f"  {country}: {len(tickers)} positions ({', '.join(tickers)})")

    print()
    print("[Raw data. Thesis monitoring context.]")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description='Thesis Monitor - Automated thesis assumption checker')
    parser.add_argument('--alerts', action='store_true', help='Only show alerts section')
    parser.add_argument('--ticker', nargs='+', help='Monitor specific ticker(s)')
    args = parser.parse_args()

    portfolio = load_portfolio()
    positions = portfolio.get('positions', [])

    if args.ticker:
        ticker_set = set(t.upper() for t in args.ticker)
        positions = [p for p in positions if p['ticker'].upper() in ticker_set]

    if not positions:
        print("No positions to monitor.")
        sys.exit(0)

    tickers = [p['ticker'] for p in positions]

    print(f"Thesis Monitor: loading prices for {len(tickers)} positions...")
    fx = get_fx_rates()
    print(f"FX: EUR/USD={fx['EURUSD']:.4f} | GBP/EUR={fx['GBPEUR']:.4f} | DKK/EUR={fx['DKKEUR']:.4f}")

    price_data = batch_fetch_prices(tickers, fx)

    results = []
    for pos in positions:
        ticker = pos['ticker']
        thesis_content = read_thesis(ticker)
        pd = price_data.get(ticker)
        result = analyze_position(pos, pd, fx, thesis_content)
        results.append(result)

    print_full_report(results, alerts_only=args.alerts)


if __name__ == '__main__':
    main()
