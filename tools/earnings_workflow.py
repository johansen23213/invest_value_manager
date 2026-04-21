#!/usr/bin/env python3
"""
Earnings Workflow — Semi-automated post-earnings assessment workflow.

Cuts per-position earnings assessment from ~30 minutes to ~5 minutes by:
1. Compiling pre-earnings briefing from thesis, framework, portfolio
2. Parsing framework to extract metrics, scenarios, KCs automatically
3. Generating structured post-earnings assessment template

Modes:
  python3 tools/earnings_workflow.py --week           # Earnings calendar this week with status
  python3 tools/earnings_workflow.py --phase          # Quick phase transition check only
  python3 tools/earnings_workflow.py TICKER            # Pre-earnings briefing for one ticker
  python3 tools/earnings_workflow.py TICKER --assess   # Post-earnings assessment template

Complements earnings_intel.py (intelligence briefing) with workflow/action focus.
Outputs RAW DATA for the CIO to review and act on.
"""

import os
import sys
import re
import glob
import yaml
import argparse
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# --- Paths ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CALENDAR_FILE = os.path.join(BASE_DIR, 'state', 'calendar.yaml')
PORTFOLIO_FILE = os.path.join(BASE_DIR, 'portfolio', 'current.yaml')
PIPELINE_FILE = os.path.join(BASE_DIR, 'state', 'pipeline_tracker.yaml')
WATCHLIST_FILE = os.path.join(BASE_DIR, 'state', 'watchlist.yaml')
THESIS_ACTIVE_DIR = os.path.join(BASE_DIR, 'thesis', 'active')
THESIS_RESEARCH_DIR = os.path.join(BASE_DIR, 'thesis', 'research')
THESIS_SHORT_DIR = os.path.join(BASE_DIR, 'thesis', 'short', 'active')


# =============================================================================
# YAML / File I/O
# =============================================================================

def load_yaml(path):
    """Load a YAML file safely."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f) or {}
    except Exception:
        return {}


def read_file(path):
    """Read a text file, return contents or None."""
    if not os.path.exists(path):
        return None
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception:
        return None


# =============================================================================
# FX Rates (same pattern as price_checker.py)
# =============================================================================

def get_fx_rates():
    """Get FX rates via yfinance with static fallbacks."""
    defaults = {'EURUSD': 1.04, 'GBPEUR': 1.19, 'DKKEUR': 0.134}
    fallbacks_used = []
    rates = {}

    try:
        import yfinance as yf
    except ImportError:
        print("FX WARNING: yfinance not available. Using static fallbacks.")
        return defaults['EURUSD'], defaults['GBPEUR'], defaults['DKKEUR'], ['ALL']

    for pair, key, default in [('EURUSD=X', 'EURUSD', defaults['EURUSD']),
                                ('GBPEUR=X', 'GBPEUR', defaults['GBPEUR']),
                                ('DKKEUR=X', 'DKKEUR', defaults['DKKEUR'])]:
        try:
            val = yf.Ticker(pair).info.get('previousClose')
            rates[key] = val if val else default
            if not val:
                fallbacks_used.append(f"{key}={default}")
        except Exception:
            rates[key] = default
            fallbacks_used.append(f"{key}={default}")

    if fallbacks_used:
        print(f"FX WARNING: Using static fallback rates ({', '.join(fallbacks_used)}).")

    return rates['EURUSD'], rates['GBPEUR'], rates['DKKEUR'], fallbacks_used


# =============================================================================
# Price fetching (same pattern as price_checker.py)
# =============================================================================

def get_current_price(ticker):
    """Get current price and currency via yfinance. Returns (price, currency) or (None, None)."""
    try:
        import yfinance as yf
        t = yf.Ticker(ticker)
        info = t.info
        price = info.get('currentPrice') or info.get('regularMarketPrice') or info.get('previousClose')
        currency = info.get('currency', '?')
        return price, currency
    except Exception:
        return None, None


# =============================================================================
# Fair Value Parsing (from portfolio current.yaml fair_value field)
# =============================================================================

def parse_fv_from_portfolio(fv_str):
    """Parse FV from current.yaml fair_value field.

    Examples:
        'EUR 35.00 (v3.1...)'     -> (35.0, 'EUR')
        '190 GBp (v3.0...)'       -> (190.0, 'GBp')
        '$191 (v3.0...)'          -> (191.0, 'USD')
        '$66 (v3.0...)'           -> (66.0, 'USD')
        '240 GBp (v3.0...)'      -> (240.0, 'GBp')
        '345 GBp (adversarial..)' -> (345.0, 'GBp')
        '580 GBp (re-eval...)'   -> (580.0, 'GBp')
        '$390 (FTC-adjusted...)'  -> (390.0, 'USD')
        '$196 (governance...)'    -> (196.0, 'USD')
        '$195 (v4.0...)'          -> (195.0, 'USD')
    """
    if not fv_str or not isinstance(fv_str, str):
        return None, None

    fv_str = fv_str.strip()

    # Try EUR prefix
    m = re.match(r'EUR\s+([0-9,]+(?:\.\d+)?)', fv_str)
    if m:
        return float(m.group(1).replace(',', '')), 'EUR'

    # Try $ prefix
    m = re.match(r'\$\s*([0-9,]+(?:\.\d+)?)', fv_str)
    if m:
        return float(m.group(1).replace(',', '')), 'USD'

    # Try GBp suffix
    m = re.match(r'([0-9,]+(?:\.\d+)?)\s*GBp', fv_str)
    if m:
        return float(m.group(1).replace(',', '')), 'GBp'

    # Try DKK prefix
    m = re.match(r'DKK\s+([0-9,]+(?:\.\d+)?)', fv_str)
    if m:
        return float(m.group(1).replace(',', '')), 'DKK'

    # Try SEK prefix
    m = re.match(r'SEK\s+([0-9,]+(?:\.\d+)?)', fv_str)
    if m:
        return float(m.group(1).replace(',', '')), 'SEK'

    # Bare number (assume same currency as position)
    m = re.match(r'([0-9,]+(?:\.\d+)?)', fv_str)
    if m:
        return float(m.group(1).replace(',', '')), None

    return None, None


def convert_to_eur(value, currency, eurusd, gbpeur, dkkeur):
    """Convert a value from native currency to EUR."""
    if value is None:
        return None
    if currency == 'EUR':
        return value
    elif currency == 'USD':
        return value / eurusd if eurusd else value
    elif currency in ('GBp', 'GBX'):
        return (value / 100) * gbpeur if gbpeur else value
    elif currency == 'GBP':
        return value * gbpeur if gbpeur else value
    elif currency == 'DKK':
        return value * dkkeur if dkkeur else value
    elif currency == 'SEK':
        return value * 0.088  # approximate
    return value


# =============================================================================
# Calendar Parsing
# =============================================================================

def get_earnings_events(days=7, ticker_filter=None):
    """Get earnings/earnings_pipeline events from calendar within date range."""
    cal = load_yaml(CALENDAR_FILE)
    events = cal.get('events', [])
    today = datetime.now().date()
    cutoff = today + timedelta(days=days)

    results = []
    for ev in events:
        if not isinstance(ev, dict):
            continue
        ev_type = str(ev.get('type', ''))
        if 'earnings' not in ev_type and ev_type not in ('watchlist_review',):
            continue
        date_str = str(ev.get('date', ''))
        try:
            ev_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError:
            continue
        if ev_date < today or ev_date > cutoff:
            continue
        ticker = ev.get('ticker', '')
        if ticker_filter and ticker != ticker_filter:
            continue
        ev['_date'] = ev_date
        ev['_days_away'] = (ev_date - today).days
        results.append(ev)

    results.sort(key=lambda x: (x['_date'], x.get('ticker', '')))
    return results


def is_completed(event):
    """Check if an earnings event is marked COMPLETED in calendar comments or action."""
    action = str(event.get('action', '')).upper()
    event_text = str(event.get('event', '')).upper()
    # Check if COMPLETED is in the action or event text
    return 'COMPLETED' in action or 'COMPLETED' in event_text


# =============================================================================
# Framework Discovery and Parsing
# =============================================================================

def find_earnings_framework(ticker):
    """Find the most recent earnings framework file for a ticker.
    Returns (file_path, relative_path) or (None, None).
    """
    candidates = []
    for base_dir, rel_prefix in [(THESIS_ACTIVE_DIR, 'thesis/active'),
                                  (THESIS_RESEARCH_DIR, 'thesis/research'),
                                  (THESIS_SHORT_DIR, 'thesis/short/active')]:
        ticker_dir = os.path.join(base_dir, ticker)
        if not os.path.isdir(ticker_dir):
            continue
        pattern = os.path.join(ticker_dir, 'earnings_framework*')
        for fpath in glob.glob(pattern):
            if fpath.endswith('.md'):
                mtime = os.path.getmtime(fpath)
                fname = os.path.basename(fpath)
                rel_path = f"{rel_prefix}/{ticker}/{fname}"
                candidates.append((fpath, rel_path, mtime))

    if not candidates:
        return None, None

    # Return the most recently modified
    candidates.sort(key=lambda x: x[2], reverse=True)
    return candidates[0][0], candidates[0][1]


def find_thesis_file(ticker):
    """Find the main thesis file for a ticker.
    Returns (file_path, relative_path) or (None, None).
    """
    for base_dir, rel_prefix in [(THESIS_ACTIVE_DIR, 'thesis/active'),
                                  (THESIS_RESEARCH_DIR, 'thesis/research')]:
        path = os.path.join(base_dir, ticker, 'thesis.md')
        if os.path.exists(path):
            return path, f"{rel_prefix}/{ticker}/thesis.md"
    return None, None


def extract_scenarios_from_framework(content):
    """Extract BULL/BASE/BEAR scenarios from earnings framework.

    Returns list of dicts with keys: name, probability, summary, metrics.
    """
    if not content:
        return []

    scenarios = []
    for label in ['BULL', 'BASE', 'BEAR']:
        scenario = {'name': label, 'probability': None, 'summary': None, 'metrics': []}

        # Pattern: "### BULL (probability 20%)" or "### BULL (probabilidad 20%)"
        m = re.search(
            rf'###\s*{label}\s*\((?:probability|probabilidad)\s*(\d+)%',
            content, re.IGNORECASE
        )
        if m:
            scenario['probability'] = int(m.group(1))

        # Extract the bold summary line after the header
        # Pattern: "**EBITDA > EUR 1,370M, 2026 guidance better than -8%**"
        m = re.search(
            rf'###\s*{label}[^\n]*\n\*\*(.+?)\*\*',
            content, re.IGNORECASE
        )
        if m:
            scenario['summary'] = m.group(1).strip()

        # Extract "Que buscar:" or "What to look for:" items
        pattern = rf'###\s*{label}[^\n]*\n(?:.*?\n)*?(?:Que buscar|What to look for)[:\s]*\n((?:\s*-\s+.+\n)+)'
        m = re.search(pattern, content, re.IGNORECASE)
        if m:
            items_text = m.group(1)
            for item_m in re.finditer(r'-\s+(.+)', items_text):
                item = item_m.group(1).strip()
                if item:
                    scenario['metrics'].append(item)

        # Extract implication
        impl_pat = rf'###\s*{label}.*?\*\*(?:Implicacion|Implication)\*?\*?[:\s]*(.+?)(?:\n\n|\n###|\Z)'
        m = re.search(impl_pat, content, re.IGNORECASE | re.DOTALL)
        if m:
            scenario['implication'] = m.group(1).strip().split('\n')[0].strip()
        else:
            scenario['implication'] = None

        scenarios.append(scenario)

    return scenarios


def _extract_kc_section(content):
    """Extract only the Kill Conditions section from content.

    Looks for headers like "## 4. KILL CONDITIONS" or "## KILL CONDITIONS"
    and returns only that section text. Returns full content if no section found.
    """
    if not content:
        return content

    # Find KC section header
    m = re.search(
        r'(##\s*\d*\.?\s*(?:KILL CONDITIONS?|Kill Conditions?)[^\n]*\n)',
        content, re.IGNORECASE
    )
    if not m:
        return content

    section_start = m.start()
    # Find the next ## header (end of KC section)
    remaining = content[m.end():]
    next_header = re.search(r'\n##\s', remaining)
    if next_header:
        section_end = m.end() + next_header.start()
    else:
        section_end = len(content)

    return content[section_start:section_end]


def extract_kc_from_framework(content):
    """Extract Kill Conditions from framework/thesis.

    Only searches within the Kill Conditions section to avoid false matches
    from other tables (POSICION ACTUAL, etc.).

    Returns list of dicts with: number, condition, status, threshold.
    """
    if not content:
        return []

    # Restrict search to KC section only
    kc_section = _extract_kc_section(content)

    kcs = []
    seen_numbers = set()

    # Pattern 1: Table format with explicit KC# prefix
    # "| KC#1 | ROIC deterioro | 25%+ | ROIC < 15% sustained |"
    for m in re.finditer(
        r'\|\s*(?:\*\*)?KC\s*#?\s*(\d+)(?:\*\*)?\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|',
        kc_section, re.IGNORECASE
    ):
        num = m.group(1)
        condition = m.group(2).strip().strip('*')
        status = m.group(3).strip().strip('*')
        threshold = m.group(4).strip().strip('*')
        if num not in seen_numbers and '---' not in condition:
            seen_numbers.add(num)
            kcs.append({
                'number': int(num),
                'condition': condition,
                'status': status,
                'threshold': threshold,
            })

    # Pattern 2: Table format "| # | Condition | Status | Threshold |"
    # where # is a small number (1-20) in a KC table context
    if not kcs:
        table_rows = re.findall(
            r'\|\s*(\d{1,2})\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|',
            kc_section, re.IGNORECASE
        )
        for num, condition, status, threshold in table_rows:
            if num in seen_numbers:
                continue
            num_int = int(num)
            # Reasonable KC numbers are 1-20
            if num_int < 1 or num_int > 20:
                continue
            condition_clean = condition.strip().strip('*')
            status_clean = status.strip().strip('*')
            threshold_clean = threshold.strip().strip('*')
            # Skip header rows and separator rows
            if 'condition' in condition_clean.lower() and ('status' in status_clean.lower() or 'threshold' in threshold_clean.lower()):
                continue
            if 'kill' in condition_clean.lower() and 'threshold' in threshold_clean.lower():
                continue
            if '---' in condition_clean or '---' in status_clean:
                continue
            # Skip rows that look like position data (Shares, Avg Cost, etc.)
            skip_words = ['shares', 'avg cost', 'current price', 'position', 'unrealized',
                          'quality score', 'fair value', 'mos actual', 'precio vs', 'dividend yield',
                          'conviction', 'metrica', 'metric', 'valor']
            if any(w in condition_clean.lower() for w in skip_words):
                continue
            seen_numbers.add(num)
            kcs.append({
                'number': num_int,
                'condition': condition_clean,
                'status': status_clean,
                'threshold': threshold_clean,
            })

    # Pattern 3: "KC#N: text" standalone lines
    if not kcs:
        for m in re.finditer(r'KC\s*#?\s*(\d+)[:\s]+(.+?)(?:\n|$)', kc_section, re.IGNORECASE):
            num = m.group(1)
            if num in seen_numbers:
                continue
            text = m.group(2).strip()
            if len(text) > 10:
                seen_numbers.add(num)
                kcs.append({
                    'number': int(num),
                    'condition': text[:120],
                    'status': '?',
                    'threshold': '?',
                })

    # Pattern 4: Bold KC headers within text "**KC#9:** text" or "| **9** | **MONY fails...**"
    for m in re.finditer(
        r'\*\*(?:KC\s*)?#?\s*(\d{1,2})\*\*[:\s|]+\*?\*?(.+?)(?:\*\*|\n|$)',
        kc_section, re.IGNORECASE
    ):
        num = m.group(1)
        if num in seen_numbers:
            continue
        text = m.group(2).strip().strip('*').strip()
        if len(text) > 5:
            num_int = int(num)
            if 1 <= num_int <= 20:
                seen_numbers.add(num)
                kcs.append({
                    'number': num_int,
                    'condition': text[:120],
                    'status': '?',
                    'threshold': '?',
                })

    kcs.sort(key=lambda x: x['number'])
    return kcs


def extract_decision_tree(content):
    """Extract the pre-committed decision tree from framework.

    Returns the raw text of the decision tree code block.
    """
    if not content:
        return None

    # Look for code block after "DECISION TREE" header
    m = re.search(
        r'(?:DECISION TREE|Decision Tree)[^\n]*\n+```\n?([\s\S]+?)```',
        content, re.IGNORECASE
    )
    if m:
        return m.group(1).strip()

    return None


def extract_consensus(content):
    """Extract consensus/expectations section from framework."""
    if not content:
        return None

    # Look for "CONSENSO" or "CONSENSUS" section
    m = re.search(
        r'##\s*\d*\.?\s*(?:CONSENSO|CONSENSUS)[^\n]*\n([\s\S]+?)(?=\n##\s|\Z)',
        content, re.IGNORECASE
    )
    if m:
        return m.group(1).strip()[:1500]  # Cap at reasonable length

    return None


def extract_checklist(content):
    """Extract POST-EARNINGS CHECKLIST items from framework.

    Returns list of checklist items (text only, no [x]/[ ] prefix).
    """
    if not content:
        return []

    # Find the checklist section
    m = re.search(
        r'(?:POST-EARNINGS CHECKLIST|Post-Earnings Checklist)[^\n]*\n+```\n?([\s\S]+?)```',
        content, re.IGNORECASE
    )
    if not m:
        # Try without code block
        m = re.search(
            r'(?:POST-EARNINGS CHECKLIST|Post-Earnings Checklist)[^\n]*\n((?:\s*\[.\]\s+.+\n)+)',
            content, re.IGNORECASE
        )
    if not m:
        return []

    items = []
    for line in m.group(1).split('\n'):
        # Match "[ ] item" or "[x] item"
        item_m = re.match(r'\s*\[(.)\]\s+(.+)', line)
        if item_m:
            items.append(item_m.group(2).strip())

    return items


def extract_metrics_table(content):
    """Extract metrics from consensus tables in framework.

    Returns list of dicts: {metric, expected, context}

    Handles formats:
    - | Revenue | EUR 2,955M | EUR 2,856M |
    - | **Revenue** | EUR 118.7B | "Increasing" |
    - | **EBITDA AL (adj)** | EUR 44.1B | ~EUR 45.3B |
    """
    if not content:
        return []

    # First extract the consensus section to avoid matching tables elsewhere
    consensus_section = extract_consensus(content)
    if not consensus_section:
        return []

    metrics = []
    seen = set()

    # Words that indicate header/non-metric rows
    header_words = {'metric', 'metrica', 'date', 'escenario', 'source', 'field',
                    'my base', 'company guide', 'company stated', 'consensus',
                    'fy2025', 'fy2026', 'fy2024', 'q4 2025', 'q1 2026', 'prior'}

    # Financial metric keywords (to identify real metrics vs header artifacts)
    metric_keywords = {'revenue', 'ebitda', 'ebit', 'net income', 'eps', 'fcf',
                       'dps', 'dividend', 'margin', 'growth', 'operating',
                       'free cash', 'capex', 'debt', 'leverage', 'solvency',
                       'combined ratio', 'nwp', 'gwp', 'roe', 'roic', 'roa',
                       'cev', 'anp', 'book value', 'nav', 'arpu', 'churn',
                       'subscribers', 'users', 'organic', 'like-for-like',
                       'same-store', 'comp', 'occupancy', 'adr', 'revpar',
                       'premium', 'claims', 'loss ratio', 'cash flow', 'profit'}

    # Pattern: table rows — handle **bold** and regular metric names
    # Match: | metric_text | value | (optionally more columns)
    for m in re.finditer(
        r'\|\s*(\*{0,2}[A-Z][^|]{2,40}?\*{0,2})\s*\|\s*([^|]{2,30})\s*\|',
        consensus_section
    ):
        raw_metric = m.group(1).strip().strip('*').strip()
        value = m.group(2).strip().strip('*').strip()

        # Skip separator rows
        if '---' in raw_metric or '---' in value:
            continue

        # Skip header rows
        if raw_metric.lower() in header_words:
            continue

        # Skip if value looks like a header
        if value.lower() in header_words:
            continue

        # Validate: metric should contain a financial keyword
        metric_lower = raw_metric.lower()
        is_financial = any(kw in metric_lower for kw in metric_keywords)
        if not is_financial:
            continue

        key = metric_lower[:25]
        if key not in seen:
            seen.add(key)
            metrics.append({'metric': raw_metric, 'expected': value, 'context': ''})

    return metrics[:15]


# =============================================================================
# Position / Portfolio Info
# =============================================================================

def get_position_info(ticker):
    """Get position info from portfolio/current.yaml.

    Returns dict with: shares, avg_cost_usd, invested_usd, conviction, fair_value,
    exit_plan, last_review, notes, date_opened, or None if not a position.
    """
    portfolio = load_yaml(PORTFOLIO_FILE)
    for p in portfolio.get('positions', []):
        if p.get('ticker') == ticker:
            return {
                'shares': p.get('shares'),
                'avg_cost_usd': p.get('avg_cost_usd'),
                'invested_usd': p.get('invested_usd'),
                'conviction': p.get('conviction', '?'),
                'fair_value': p.get('fair_value', ''),
                'exit_plan': p.get('exit_plan', ''),
                'last_review': p.get('last_review', ''),
                'notes': p.get('notes', ''),
                'date_opened': p.get('date_opened', ''),
                'type': 'ACTIVE',
            }
    for sp in portfolio.get('short_positions', []) or []:
        if sp.get('ticker') == ticker:
            return {
                'shares': sp.get('shares'),
                'avg_cost_usd': sp.get('entry_price_usd'),
                'invested_usd': sp.get('entry_price_usd', 0) * sp.get('shares', 0),
                'conviction': sp.get('conviction', '?'),
                'fair_value': '',
                'exit_plan': sp.get('exit_plan', ''),
                'last_review': sp.get('last_review', ''),
                'notes': sp.get('notes', ''),
                'date_opened': sp.get('date_opened', ''),
                'type': 'SHORT',
            }
    return None


def get_pipeline_info(ticker):
    """Check watchlist and research directories for pipeline info."""
    result = None
    watchlist = load_yaml(WATCHLIST_FILE)

    # Search all watchlist sections
    for section in ['quality_compounders', 'quality_value', 'ready_to_buy', 'on_watch', 'tier_2']:
        items = watchlist.get(section, []) or []
        for item in items:
            if isinstance(item, dict) and item.get('ticker') == ticker:
                result = {
                    'type': 'PIPELINE',
                    'section': section,
                    'entry': item.get('entry', '?'),
                    'fv': item.get('fv', '?'),
                    'notes': item.get('notes', ''),
                    'status': item.get('status', ''),
                }
                break
        if result:
            break

    # Check if thesis/research directory exists (fallback if not in watchlist)
    if not result and os.path.isdir(os.path.join(THESIS_RESEARCH_DIR, ticker)):
        result = {'type': 'PIPELINE', 'section': 'research', 'notes': 'Thesis in research dir'}

    # Enrich with quality_universe data
    qu_path = os.path.join(BASE_DIR, 'state', 'quality_universe.yaml')
    if os.path.exists(qu_path):
        try:
            qu = load_yaml(qu_path)
            for c in (qu.get('quality_universe', {}).get('companies', []) or []):
                if c.get('ticker') == ticker:
                    qu_data = {
                        'pipeline_status': c.get('pipeline_status', '?'),
                        'qu_fv': c.get('fair_value'),
                        'qu_entry': c.get('entry_price'),
                        'qu_qs': c.get('qs_adj') or c.get('qs_tool'),
                        'qu_tier': c.get('tier'),
                        'qu_goodwill_pct': c.get('goodwill_pct'),
                    }
                    if result:
                        result.update(qu_data)
                    else:
                        result = {'type': 'PIPELINE', 'section': 'universe', **qu_data}
                    break
        except Exception:
            pass

    return result


# =============================================================================
# Phase Transition Detection (shared logic)
# =============================================================================

def detect_phase_transition(events):
    """Detect if the current week qualifies as a phase transition week.

    Returns (is_transition, portfolio_events, pipeline_events, missing_frameworks) or
    (False, [], [], []) if no transition.
    """
    portfolio_events = [ev for ev in events if get_position_info(ev.get('ticker', '')) is not None]
    pipeline_events = [ev for ev in events if get_position_info(ev.get('ticker', '')) is None and not is_completed(ev)]
    missing_fw = [ev.get('ticker', '') for ev in events if not find_earnings_framework(ev.get('ticker', ''))[0] and not is_completed(ev)]

    is_transition = len(portfolio_events) >= 3 or (len(portfolio_events) >= 2 and len(pipeline_events) >= 3)

    return is_transition, portfolio_events, pipeline_events, missing_fw


def print_phase_transition(portfolio_events, pipeline_events, missing_fw):
    """Print the phase transition warning block."""
    print()
    print("!" * 80)
    print("  PHASE TRANSITION WEEK -- High earnings density detected")
    print("!" * 80)
    print(f"  {len(portfolio_events)} active positions + {len(pipeline_events)} pipeline reporting this week")
    print()
    print("  PROTOCOL:")
    print("  1. Verify ALL frameworks exist (check column above)")
    if missing_fw:
        print(f"     MISSING FRAMEWORKS: {', '.join(missing_fw)}")
    else:
        print("     All frameworks present")
    print("  2. Process by position size (largest first)")
    print("  3. Pre-commit decisions BEFORE market open on earnings day")
    print("  4. Batch post-earnings assessment (don't let queue build)")
    print("  5. Emotional check: F (Psychology) amplified this week")
    print()


# =============================================================================
# MODE 1: --week (Earnings Calendar View)
# =============================================================================

def mode_week():
    """Show all earnings events this week with status."""
    events = get_earnings_events(days=7)
    today = datetime.now().date()

    if not events:
        print("\nNo earnings events in the next 7 days.")
        print("\n[Raw data. Earnings workflow context.]")
        return

    print()
    print("=" * 100)
    print(f"  EARNINGS THIS WEEK  ({today.strftime('%Y-%m-%d')} to {(today + timedelta(days=7)).strftime('%Y-%m-%d')})")
    print("=" * 100)
    print(f"{'Date':<12} {'Ticker':<12} {'Event':<42} {'Status':<12} {'Framework?':<10}")
    print("-" * 100)

    for ev in events:
        ticker = ev.get('ticker', '?')
        date = ev.get('_date')
        event_text = str(ev.get('event', ''))[:40]
        days_away = ev.get('_days_away', 0)

        # Status
        completed = is_completed(ev)
        if completed:
            status = 'COMPLETED'
        elif days_away == 0:
            status = 'TODAY'
        elif days_away < 0:
            status = 'PAST'
        else:
            status = 'PENDING'

        # Framework exists?
        fw_path, fw_rel = find_earnings_framework(ticker)
        has_framework = 'YES' if fw_path else 'NO'

        # Position type
        pos = get_position_info(ticker)
        pos_type = pos['type'] if pos else ''
        if not pos_type:
            pipe = get_pipeline_info(ticker)
            pos_type = pipe['type'] if pipe else 'EXTERNAL'

        date_str = date.strftime('%a %m-%d') if date else '?'

        print(f"{date_str:<12} {ticker:<12} {event_text:<42} {status:<12} {has_framework:<10} [{pos_type}]")

    print("-" * 100)
    active_count = sum(1 for ev in events if get_position_info(ev.get('ticker', '')) is not None)
    pending_count = sum(1 for ev in events if not is_completed(ev))
    print(f"  {len(events)} events total | {active_count} active positions | {pending_count} pending")

    # Phase transition detection
    is_transition, portfolio_events, pipeline_events, missing_fw = detect_phase_transition(events)
    if is_transition:
        print_phase_transition(portfolio_events, pipeline_events, missing_fw)

    print()
    print("[Raw data. Earnings workflow context.]")


# =============================================================================
# MODE 1b: --phase (Quick Phase Transition Check)
# =============================================================================

def mode_phase():
    """Quick check: is this a phase transition week? Minimal output."""
    events = get_earnings_events(days=7)
    today = datetime.now().date()

    if not events:
        print(f"\n[{today}] No earnings events in the next 7 days. No phase transition.")
        return

    is_transition, portfolio_events, pipeline_events, missing_fw = detect_phase_transition(events)

    print()
    if is_transition:
        print_phase_transition(portfolio_events, pipeline_events, missing_fw)
        # List the portfolio tickers reporting
        if portfolio_events:
            print("  PORTFOLIO REPORTING:")
            for ev in sorted(portfolio_events, key=lambda e: e.get('_date', today)):
                ticker = ev.get('ticker', '?')
                date = ev.get('_date')
                date_str = date.strftime('%a %m-%d') if date else '?'
                completed = is_completed(ev)
                status = 'COMPLETED' if completed else 'PENDING'
                print(f"    {date_str}  {ticker:<12} {status}")
        if pipeline_events:
            print("  PIPELINE REPORTING:")
            for ev in sorted(pipeline_events, key=lambda e: e.get('_date', today)):
                ticker = ev.get('ticker', '?')
                date = ev.get('_date')
                date_str = date.strftime('%a %m-%d') if date else '?'
                print(f"    {date_str}  {ticker:<12}")
        print()
    else:
        print(f"  No phase transition this week.")
        print(f"  {len(portfolio_events)} portfolio + {len(pipeline_events)} pipeline earnings (below threshold)")
        print()

    print("[Raw data. Phase transition check.]")


# =============================================================================
# MODE 2: TICKER (Pre-Earnings Briefing)
# =============================================================================

def mode_briefing(ticker):
    """Generate pre-earnings briefing for a ticker."""
    print(f"\nLoading data for {ticker}...")

    # Get price
    price, currency = get_current_price(ticker)

    # Get position/pipeline info
    pos = get_position_info(ticker)
    pipe = get_pipeline_info(ticker) if not pos else None

    # Get FV from portfolio
    fv = None
    fv_currency = None
    if pos and pos.get('fair_value'):
        fv, fv_currency = parse_fv_from_portfolio(pos['fair_value'])

    # Calculate MoS and P&L
    mos_pct = None
    pnl_pct = None
    if fv is not None and price is not None and price > 0:
        # Convert FV to same currency as price for MoS calc
        if fv_currency and currency:
            if fv_currency == currency:
                mos_pct = ((fv - price) / price) * 100
            else:
                # Need FX rates for cross-currency
                eurusd, gbpeur, dkkeur, _ = get_fx_rates()
                fv_eur = convert_to_eur(fv, fv_currency, eurusd, gbpeur, dkkeur)
                price_eur = convert_to_eur(price, currency, eurusd, gbpeur, dkkeur)
                if fv_eur and price_eur and price_eur > 0:
                    mos_pct = ((fv_eur - price_eur) / price_eur) * 100

    if pos and pos.get('avg_cost_usd') and price:
        # Approximate P&L (not exact due to currency)
        avg_cost = pos['avg_cost_usd']
        if currency == 'USD':
            pnl_pct = ((price - avg_cost) / avg_cost) * 100

    # Find and read framework
    fw_path, fw_rel = find_earnings_framework(ticker)
    fw_content = read_file(fw_path) if fw_path else None

    # Find and read thesis
    thesis_path, thesis_rel = find_thesis_file(ticker)
    thesis_content = read_file(thesis_path) if thesis_path else None

    # Extract framework components
    scenarios = extract_scenarios_from_framework(fw_content)
    kcs = extract_kc_from_framework(fw_content or thesis_content)
    decision_tree = extract_decision_tree(fw_content)
    consensus = extract_consensus(fw_content)
    checklist = extract_checklist(fw_content)

    # Print briefing
    print()
    print("=" * 80)
    print(f"  PRE-EARNINGS BRIEFING: {ticker}")
    print("=" * 80)

    # Position line
    if pos:
        pos_line = f"  Position: {pos['shares']} shares"
        if pos.get('avg_cost_usd'):
            pos_line += f" @ {pos['avg_cost_usd']:.2f} USD avg"
        if price and currency:
            pos_line += f" | Current: {price:.2f} {currency}"
        if pnl_pct is not None:
            pos_line += f" | P&L: {pnl_pct:+.1f}%"
        print(pos_line)

        fv_line = f"  FV: {pos.get('fair_value', 'N/A')}"
        if mos_pct is not None:
            fv_line += f" | MoS: {mos_pct:.1f}%"
        fv_line += f" | Conviction: {pos.get('conviction', '?').upper()}"
        print(fv_line)

        if pos.get('exit_plan'):
            print(f"  Exit Plan: {pos['exit_plan'][:140]}")
    elif pipe:
        print(f"  Pipeline candidate [{pipe.get('section', '?')}]")
        if price and currency:
            print(f"  Current: {price:.2f} {currency}")
        if pipe.get('entry'):
            print(f"  Entry target: {pipe['entry']}")
        if pipe.get('fv'):
            print(f"  FV: {pipe['fv']}")
        if pipe.get('notes'):
            print(f"  Notes: {pipe['notes'][:140]}")
    else:
        if price and currency:
            print(f"  External (no position). Current: {price:.2f} {currency}")
        else:
            print(f"  External (no position). Price unavailable.")

    # Consensus
    if consensus:
        print()
        print("-" * 80)
        print("CONSENSUS / EXPECTATIONS:")
        print("-" * 80)
        # Print first ~25 lines of consensus
        for i, line in enumerate(consensus.split('\n')[:25]):
            print(f"  {line}")

    # Scenarios
    if scenarios:
        print()
        print("-" * 80)
        print("SCENARIOS (from framework):")
        print("-" * 80)
        for s in scenarios:
            prob_str = f" ({s['probability']}%)" if s['probability'] else ''
            print(f"  {s['name']}{prob_str}: {s['summary'] or 'N/A'}")
            if s.get('implication'):
                print(f"    -> {s['implication'][:120]}")

    # Kill Conditions
    if kcs:
        print()
        print("-" * 80)
        print("KILL CONDITIONS TO WATCH:")
        print("-" * 80)
        for kc in kcs:
            print(f"  KC#{kc['number']}: {kc['condition'][:70]}")
            print(f"          Status: {kc['status'][:50]} | Threshold: {kc['threshold'][:50]}")

    # Decision Tree
    if decision_tree:
        print()
        print("-" * 80)
        print("PRE-COMMITTED DECISIONS:")
        print("-" * 80)
        for line in decision_tree.split('\n'):
            print(f"  {line}")

    # Post-earnings checklist
    if checklist:
        print()
        print("-" * 80)
        print("POST-EARNINGS CHECKLIST:")
        print("-" * 80)
        for item in checklist:
            print(f"  [ ] {item}")

    # File references
    print()
    print("-" * 80)
    print("FILE REFERENCES:")
    if fw_rel:
        print(f"  Framework: {fw_rel}")
    else:
        print(f"  Framework: NOT FOUND")
    if thesis_rel:
        print(f"  Thesis:    {thesis_rel}")

    print()
    print("[Raw data. Earnings workflow context.]")


# =============================================================================
# Earnings Context (auto-populated financial data for assessment)
# =============================================================================

def fetch_earnings_context(ticker):
    """Fetch auto-populated financial data for post-earnings assessment.

    Returns dict with:
    - price_reaction: price before/after earnings, % change
    - yoy_financials: latest 2 years revenue, EPS, margins from yfinance
    - analyst_estimates: forward estimates if available
    """
    ctx = {
        'price_reaction': None,
        'yoy_financials': None,
        'latest_quarter': None,
        'analyst_estimates': None,
    }

    try:
        import yfinance as yf
        t = yf.Ticker(ticker)

        # --- Price Reaction (5-day history for pre/post earnings) ---
        try:
            hist = t.history(period='10d')
            if len(hist) >= 2:
                closes = [(idx.strftime('%Y-%m-%d'), row['Close']) for idx, row in hist.iterrows()]
                if len(closes) >= 2:
                    ctx['price_reaction'] = {
                        'recent_closes': closes[-5:],  # Last 5 days
                        'latest': closes[-1],
                        'prev': closes[-2],
                        'change_pct': ((closes[-1][1] - closes[-2][1]) / closes[-2][1]) * 100,
                    }
        except Exception:
            pass

        # --- YoY Financials (latest 2 years annual) ---
        try:
            financials = t.financials
            if not financials.empty:
                yoy = {}
                # Revenue
                if 'Total Revenue' in financials.index:
                    revs = [(str(c.year), financials.loc['Total Revenue'][c]) for c in financials.columns[:2]
                            if financials.loc['Total Revenue'][c] is not None]
                    if len(revs) >= 2:
                        yoy['revenue'] = revs
                        yoy['revenue_growth'] = ((revs[0][1] - revs[1][1]) / abs(revs[1][1])) * 100 if revs[1][1] else None

                # Operating Income
                if 'Operating Income' in financials.index:
                    ops = [(str(c.year), financials.loc['Operating Income'][c]) for c in financials.columns[:2]
                           if financials.loc['Operating Income'][c] is not None]
                    if len(ops) >= 2:
                        yoy['op_income'] = ops
                        yoy['op_growth'] = ((ops[0][1] - ops[1][1]) / abs(ops[1][1])) * 100 if ops[1][1] else None

                # Net Income
                if 'Net Income' in financials.index:
                    nis = [(str(c.year), financials.loc['Net Income'][c]) for c in financials.columns[:2]
                           if financials.loc['Net Income'][c] is not None]
                    if len(nis) >= 2:
                        yoy['net_income'] = nis

                # EPS
                eps_key = 'Basic EPS' if 'Basic EPS' in financials.index else 'Diluted EPS'
                if eps_key in financials.index:
                    eps_vals = [(str(c.year), financials.loc[eps_key][c]) for c in financials.columns[:2]
                               if financials.loc[eps_key][c] is not None]
                    if len(eps_vals) >= 2:
                        yoy['eps'] = eps_vals
                        yoy['eps_growth'] = ((eps_vals[0][1] - eps_vals[1][1]) / abs(eps_vals[1][1])) * 100 if eps_vals[1][1] else None

                # Margins
                if 'Total Revenue' in financials.index and 'Operating Income' in financials.index:
                    rev0 = financials.loc['Total Revenue'].iloc[0]
                    op0 = financials.loc['Operating Income'].iloc[0]
                    if rev0 and rev0 > 0 and op0 is not None:
                        yoy['op_margin_latest'] = (op0 / rev0) * 100

                if 'Total Revenue' in financials.index and 'Gross Profit' in financials.index:
                    rev0 = financials.loc['Total Revenue'].iloc[0]
                    gp0 = financials.loc['Gross Profit'].iloc[0]
                    if rev0 and rev0 > 0 and gp0 is not None:
                        yoy['gm_latest'] = (gp0 / rev0) * 100

                if yoy:
                    ctx['yoy_financials'] = yoy
                    ctx['latest_quarter'] = str(financials.columns[0].strftime('%Y-%m-%d')) if hasattr(financials.columns[0], 'strftime') else str(financials.columns[0])
        except Exception:
            pass

        # --- FCF from cashflow ---
        try:
            cf = t.cashflow
            if not cf.empty and 'Free Cash Flow' in cf.index:
                fcf_vals = [(str(c.year), cf.loc['Free Cash Flow'][c]) for c in cf.columns[:2]
                            if cf.loc['Free Cash Flow'][c] is not None]
                if fcf_vals and ctx.get('yoy_financials') is not None:
                    ctx['yoy_financials']['fcf'] = fcf_vals
        except Exception:
            pass

        # --- Analyst Estimates ---
        try:
            info = t.info
            if info:
                estimates = {}
                for key, label in [('forwardEps', 'Forward EPS'),
                                   ('forwardPE', 'Forward P/E'),
                                   ('earningsQuarterlyGrowth', 'Quarterly Earnings Growth'),
                                   ('revenueQuarterlyGrowth', 'Quarterly Revenue Growth')]:
                    val = info.get(key)
                    if val is not None:
                        estimates[label] = val
                if estimates:
                    ctx['analyst_estimates'] = estimates
        except Exception:
            pass

    except ImportError:
        pass

    return ctx


def fmt_large(val):
    """Format large numbers as B/M for display."""
    if val is None:
        return 'N/A'
    if abs(val) >= 1e9:
        return f"{val/1e9:.2f}B"
    elif abs(val) >= 1e6:
        return f"{val/1e6:.0f}M"
    else:
        return f"{val:,.0f}"


# =============================================================================
# MODE 3: TICKER --assess (Post-Earnings Assessment Template)
# =============================================================================

def mode_assess(ticker):
    """Generate post-earnings assessment template from framework."""
    print(f"\nLoading assessment data for {ticker}...")

    # Find and read framework
    fw_path, fw_rel = find_earnings_framework(ticker)
    fw_content = read_file(fw_path) if fw_path else None

    # Find and read thesis
    thesis_path, thesis_rel = find_thesis_file(ticker)
    thesis_content = read_file(thesis_path) if thesis_path else None

    # Get current price
    price, currency = get_current_price(ticker)

    # Get position info
    pos = get_position_info(ticker)
    pipe = get_pipeline_info(ticker) if not pos else None

    # Extract framework components
    scenarios = extract_scenarios_from_framework(fw_content)
    kcs = extract_kc_from_framework(fw_content or thesis_content)
    decision_tree = extract_decision_tree(fw_content)
    checklist = extract_checklist(fw_content)
    consensus_metrics = extract_metrics_table(fw_content)

    # Extract BASE scenario metrics for comparison template
    base_scenario = next((s for s in scenarios if s['name'] == 'BASE'), None)

    print()
    print("=" * 80)
    print(f"  POST-EARNINGS ASSESSMENT: {ticker}")
    print("=" * 80)

    if price and currency:
        print(f"  Current Price: {price:.2f} {currency}")
    if pos:
        print(f"  Position: {pos['shares']} shares | Conviction: {pos.get('conviction', '?').upper()}")
    elif pipe:
        pipe_details = f"Pipeline [{pipe.get('pipeline_status', pipe.get('section', '?'))}]"
        if pipe.get('qu_qs'):
            pipe_details += f" | QS {pipe['qu_qs']} Tier {pipe.get('qu_tier', '?')}"
        if pipe.get('qu_fv'):
            pipe_details += f" | FV {pipe['qu_fv']}"
        if pipe.get('qu_entry'):
            pipe_details += f" | Entry {pipe['qu_entry']}"
        if pipe.get('qu_goodwill_pct') and pipe['qu_goodwill_pct'] > 0.40:
            pipe_details += f" | HIGH-GW({pipe['qu_goodwill_pct']*100:.0f}%)"
        print(f"  {pipe_details}")

    # Fetch auto-populated market/financial data
    ctx = fetch_earnings_context(ticker)

    # MARKET REACTION section
    pr = ctx.get('price_reaction')
    if pr:
        print()
        print("-" * 80)
        print("MARKET REACTION (auto-populated):")
        print("-" * 80)
        print(f"  {'Date':<12} {'Close':>12}")
        print(f"  {'-'*12} {'-'*12}")
        for date, close in pr['recent_closes']:
            print(f"  {date:<12} {close:>12.2f}")
        chg = pr['change_pct']
        chg_emoji = "+" if chg >= 0 else ""
        print(f"\n  Latest move: {chg_emoji}{chg:.1f}% ({pr['prev'][0]} -> {pr['latest'][0]})")

    # YoY FINANCIAL SNAPSHOT
    yoy = ctx.get('yoy_financials')
    if yoy:
        print()
        print("-" * 80)
        print(f"YoY FINANCIAL SNAPSHOT (yfinance, latest filing: {ctx.get('latest_quarter', '?')}):")
        print("-" * 80)
        print(f"  {'Metric':<22} {'Latest':>14} {'Prior Year':>14} {'YoY Change':>12}")
        print(f"  {'-'*22} {'-'*14} {'-'*14} {'-'*12}")

        if 'revenue' in yoy:
            r = yoy['revenue']
            growth = f"{yoy['revenue_growth']:+.1f}%" if yoy.get('revenue_growth') is not None else '?'
            print(f"  {'Revenue':<22} {fmt_large(r[0][1]):>14} {fmt_large(r[1][1]):>14} {growth:>12}")

        if 'op_income' in yoy:
            o = yoy['op_income']
            growth = f"{yoy['op_growth']:+.1f}%" if yoy.get('op_growth') is not None else '?'
            print(f"  {'Operating Income':<22} {fmt_large(o[0][1]):>14} {fmt_large(o[1][1]):>14} {growth:>12}")

        if 'net_income' in yoy:
            n = yoy['net_income']
            ni_growth = ((n[0][1] - n[1][1]) / abs(n[1][1])) * 100 if n[1][1] else None
            growth_str = f"{ni_growth:+.1f}%" if ni_growth is not None else '?'
            print(f"  {'Net Income':<22} {fmt_large(n[0][1]):>14} {fmt_large(n[1][1]):>14} {growth_str:>12}")

        if 'eps' in yoy:
            e = yoy['eps']
            growth = f"{yoy['eps_growth']:+.1f}%" if yoy.get('eps_growth') is not None else '?'
            print(f"  {'EPS':<22} {e[0][1]:>14.2f} {e[1][1]:>14.2f} {growth:>12}")

        if 'fcf' in yoy:
            f_vals = yoy['fcf']
            if len(f_vals) >= 2:
                fcf_growth = ((f_vals[0][1] - f_vals[1][1]) / abs(f_vals[1][1])) * 100 if f_vals[1][1] else None
                growth_str = f"{fcf_growth:+.1f}%" if fcf_growth is not None else '?'
                print(f"  {'Free Cash Flow':<22} {fmt_large(f_vals[0][1]):>14} {fmt_large(f_vals[1][1]):>14} {growth_str:>12}")
            elif len(f_vals) >= 1:
                print(f"  {'Free Cash Flow':<22} {fmt_large(f_vals[0][1]):>14}")

        # Margins
        margins_line = "  Margins (latest):"
        if yoy.get('gm_latest'):
            margins_line += f"  GM {yoy['gm_latest']:.1f}%"
        if yoy.get('op_margin_latest'):
            margins_line += f"  OP {yoy['op_margin_latest']:.1f}%"
        if yoy.get('gm_latest') or yoy.get('op_margin_latest'):
            print(margins_line)

        print(f"\n  [NOTE: yfinance reflects FILED results. Just-reported quarter may not be reflected yet.]")

    # Analyst estimates
    est = ctx.get('analyst_estimates')
    if est:
        print()
        print("-" * 80)
        print("ANALYST ESTIMATES (yfinance):")
        print("-" * 80)
        for label, val in est.items():
            if isinstance(val, float):
                if 'Growth' in label or 'P/E' in label:
                    print(f"  {label}: {val:.2f}")
                else:
                    print(f"  {label}: {val:.2f}")
            else:
                print(f"  {label}: {val}")

    if not fw_content:
        print()
        print("  WARNING: No earnings framework found for this ticker.")
        print("  Assessment template requires a framework with scenarios, KCs, and decision tree.")
        print("  Create one first, then re-run --assess.")
        print()
        print("[Raw data. Earnings workflow context.]")
        return

    # RESULTS vs FRAMEWORK section
    print()
    print("-" * 80)
    print("RESULTS vs FRAMEWORK:")
    print("-" * 80)

    if consensus_metrics:
        print(f"  {'Metric':<25} {'Expected':<20} {'Actual':<15} {'vs Exp':<12} {'Scenario':<10}")
        print(f"  {'-'*25} {'-'*20} {'-'*15} {'-'*12} {'-'*10}")
        for m in consensus_metrics:
            print(f"  {m['metric']:<25} {m['expected']:<20} {'???':<15} {'???':<12} {'???':<10}")
    else:
        # Fallback: extract metrics from scenario descriptions
        print("  (No consensus table found in framework. Extracting from scenarios.)")
        print()
        if base_scenario and base_scenario.get('metrics'):
            print(f"  {'Metric (from BASE scenario)':<55} {'Actual':<15} {'Pass?':<10}")
            print(f"  {'-'*55} {'-'*15} {'-'*10}")
            for metric in base_scenario['metrics']:
                print(f"  {metric[:55]:<55} {'???':<15} {'???':<10}")
        else:
            print("  No metrics could be extracted from framework.")

    # Checklist (with blanks for user to fill)
    if checklist:
        print()
        print("-" * 80)
        print("CHECKLIST (fill in actuals):")
        print("-" * 80)
        for item in checklist:
            print(f"  [ ] {item}: ???")

    # Kill Condition check
    if kcs:
        print()
        print("-" * 80)
        print("KILL CONDITION CHECK:")
        print("-" * 80)
        for kc in kcs:
            print(f"  KC#{kc['number']}: {kc['condition'][:70]}")
            print(f"    Pre-earnings: {kc['status'][:50]}")
            print(f"    Post-earnings: ???  [PASS / FAIL / APPROACHING]")
            print()

    # Scenario Determination
    print("-" * 80)
    print("SCENARIO DETERMINATION:")
    print("-" * 80)
    if scenarios:
        for s in scenarios:
            prob_str = f" ({s['probability']}%)" if s['probability'] else ''
            print(f"  {s['name']}{prob_str}: {s['summary'] or 'N/A'}")
            if s.get('implication'):
                print(f"    -> {s['implication'][:120]}")
        print()
        print("  ACTUAL SCENARIO: ???  [BULL / BASE / BEAR / MIXED]")
    else:
        print("  No scenarios found in framework.")

    # Recommended Action (from decision tree)
    if decision_tree:
        print()
        print("-" * 80)
        print("PRE-COMMITTED ACTION (from decision tree):")
        print("-" * 80)
        for line in decision_tree.split('\n'):
            print(f"  {line}")
        print()
        print("  ACTUAL ACTION TAKEN: ???")

    # Updates Needed
    print()
    print("-" * 80)
    print("UPDATES NEEDED:")
    print("-" * 80)

    if pos:
        print(f"  [ ] portfolio/current.yaml -- update notes, last_review, exit_plan, fair_value")
        print(f"  [ ] state/calendar.yaml -- mark event as COMPLETED")
        print(f"  [ ] {thesis_rel or f'thesis/active/{ticker}/thesis.md'} -- add post-earnings addendum")
        print(f"  [ ] {fw_rel or 'framework file'} -- complete post-earnings checklist")
        print(f"  [ ] state/system.yaml -- update QS if thesis changes")
    elif pipe:
        print(f"  [ ] state/calendar.yaml -- mark event as COMPLETED")
        print(f"  [ ] {thesis_rel or f'thesis/research/{ticker}/thesis.md'} -- update with results")
        print(f"  [ ] {fw_rel or 'framework file'} -- complete post-earnings checklist")
        print(f"  [ ] state/watchlist.yaml -- update notes/status")
        print(f"  [ ] state/quality_universe.yaml -- update pipeline_status if advancing")
    else:
        print(f"  [ ] state/calendar.yaml -- mark event as COMPLETED")
        print(f"  [ ] Determine if further action needed")

    # File references
    print()
    print("-" * 80)
    print("FILE REFERENCES:")
    if fw_rel:
        print(f"  Framework: {fw_rel}")
    if thesis_rel:
        print(f"  Thesis:    {thesis_rel}")

    print()
    print("[Raw data. Earnings workflow context.]")


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Earnings Workflow — Pre/post-earnings assessment automation.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python3 tools/earnings_workflow.py --week            # Earnings calendar this week
  python3 tools/earnings_workflow.py --phase           # Quick phase transition check
  python3 tools/earnings_workflow.py EDEN.PA           # Pre-earnings briefing
  python3 tools/earnings_workflow.py MONY.L --assess   # Post-earnings assessment template
"""
    )
    parser.add_argument('ticker', nargs='?', help='Ticker symbol (e.g., EDEN.PA)')
    parser.add_argument('--week', action='store_true', help='Show earnings calendar for this week')
    parser.add_argument('--phase', action='store_true', help='Quick phase transition check (high earnings density)')
    parser.add_argument('--assess', action='store_true', help='Generate post-earnings assessment template')
    parser.add_argument('--days', type=int, default=7, help='Lookahead window in days (default: 7, used with --week)')

    args = parser.parse_args()

    if args.phase:
        mode_phase()
    elif args.week:
        mode_week()
    elif args.ticker and args.assess:
        mode_assess(args.ticker)
    elif args.ticker:
        mode_briefing(args.ticker)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
