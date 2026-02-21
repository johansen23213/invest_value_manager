#!/usr/bin/env python3
"""
Earnings Intelligence — Pre-earnings preparation briefing.

Consolidates all relevant intelligence for upcoming earnings events:
- Current price, MoS%, E[CAGR]
- Insider activity (from ownership cache)
- Kill conditions (from thesis)
- Bear/base/bull scenarios (from earnings framework)
- Calendar action items

Usage:
  python3 tools/earnings_intel.py                 # Next 7 days
  python3 tools/earnings_intel.py --days 14        # Next 14 days
  python3 tools/earnings_intel.py --ticker MONY.L  # Specific ticker
"""

import os
import sys
import re
import yaml
import argparse
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CALENDAR_FILE = os.path.join(BASE, 'state', 'calendar.yaml')
PORTFOLIO_FILE = os.path.join(BASE, 'portfolio', 'current.yaml')
THESIS_ACTIVE = os.path.join(BASE, 'thesis', 'active')
THESIS_RESEARCH = os.path.join(BASE, 'thesis', 'research')


def load_yaml(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f) or {}
    except Exception:
        return {}


def get_earnings_events(days=7, ticker_filter=None):
    """Get earnings events from calendar within date range."""
    cal = load_yaml(CALENDAR_FILE)
    events = cal.get('events', [])
    today = datetime.now().date()
    cutoff = today + timedelta(days=days)

    earnings = []
    for ev in events:
        if not isinstance(ev, dict):
            continue
        ev_type = ev.get('type', '')
        if 'earnings' not in ev_type and ev_type != 'strategy':
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
        earnings.append(ev)

    earnings.sort(key=lambda x: x['_date'])
    return earnings


def get_position_type(ticker):
    """Determine if ticker is active position, pipeline, or external."""
    portfolio = load_yaml(PORTFOLIO_FILE)
    active_tickers = {p['ticker'] for p in portfolio.get('positions', [])}
    if ticker in active_tickers:
        return 'ACTIVE'

    # Check thesis/research
    if os.path.isdir(os.path.join(THESIS_RESEARCH, ticker)):
        return 'PIPELINE'

    return 'EXTERNAL'


def load_thesis(ticker):
    """Load thesis content for a ticker (active or research)."""
    for base_dir in [THESIS_ACTIVE, THESIS_RESEARCH]:
        path = os.path.join(base_dir, ticker, 'thesis.md')
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
    return None


def load_earnings_framework(ticker):
    """Load earnings framework file if it exists."""
    for base_dir in [THESIS_ACTIVE, THESIS_RESEARCH]:
        ticker_dir = os.path.join(base_dir, ticker)
        if not os.path.isdir(ticker_dir):
            continue
        for f in os.listdir(ticker_dir):
            if 'earnings' in f.lower() and 'framework' in f.lower() and f.endswith('.md'):
                path = os.path.join(ticker_dir, f)
                with open(path, 'r', encoding='utf-8') as fh:
                    return fh.read(), f
    return None, None


def extract_kill_conditions(thesis):
    """Extract kill conditions from thesis text. Prefers definition-style KCs."""
    if not thesis:
        return []
    kcs = {}
    # Pattern 1: Definition-style "**KC#N:** text" or "KC#N: text" at start of line/list
    for m in re.finditer(r'(?:^|\n)\s*(?:[-*]\s*)?\*?\*?KC\s*#?\s*(\d+)\*?\*?[:\s]+(.+?)(?:\n|$)', thesis, re.IGNORECASE):
        num = m.group(1)
        text = m.group(2).strip().rstrip('|').strip()
        if num not in kcs and len(text) > 10:
            # Skip inline references like "KC#1 or KC#2 triggered"
            if not re.match(r'(?:or|and|triggered|see|applies)', text, re.IGNORECASE):
                kcs[num] = f"KC#{num}: {text[:120]}"
    # Pattern 2: "Kill Condition #N:" style
    for m in re.finditer(r'Kill Condition\s*#?\s*(\d+)[:\s]+(.+?)(?:\n|$)', thesis, re.IGNORECASE):
        num = m.group(1)
        text = m.group(2).strip()
        if num not in kcs and len(text) > 10:
            kcs[num] = f"KC#{num}: {text[:120]}"
    # Sort by KC number
    return [kcs[k] for k in sorted(kcs.keys(), key=int)][:8]


def extract_scenarios(thesis):
    """Extract bear/base/bull scenario summaries with FV and probability."""
    if not thesis:
        return {}
    scenarios = {}
    for label in ['Bear', 'Base', 'Bull']:
        best_text = None
        # Priority 1: "**Bear Case:** FV $X (Y% probability)" or similar
        m = re.search(rf'\*\*{label}\s*(?:Case|Scenario)?\*\*[:\s]*(.+?)(?:\n|$)', thesis, re.IGNORECASE)
        if m:
            text = m.group(1).strip()
            if len(text) > 10 and any(c.isdigit() for c in text):
                best_text = text
        # Priority 2: "Bear (X% probability): FV $Y" or "Bear: $Y"
        if not best_text:
            m = re.search(rf'(?:^|\n)\s*[-*]?\s*\*?\*?{label}(?:\s*(?:Case|Scenario))?\*?\*?\s*\(([^)]+)\)[:\s]*(.+?)(?:\n|$)', thesis, re.IGNORECASE)
            if m:
                prob = m.group(1).strip()
                text = m.group(2).strip()
                best_text = f"({prob}) {text}" if text else f"({prob})"
        # Priority 3: "| Bear | $X | Y%" in table
        if not best_text:
            m = re.search(rf'\|\s*\*?\*?{label}\s*(?:Case)?\*?\*?\s*\|(.+?)(?:\n|$)', thesis, re.IGNORECASE)
            if m:
                cells = [c.strip().strip('*') for c in m.group(1).split('|') if c.strip()]
                if cells:
                    best_text = ' | '.join(cells[:4])
        if best_text and len(best_text) > 5:
            scenarios[label] = best_text[:140]
    return scenarios


def extract_key_metrics(thesis, framework):
    """Extract key metrics to watch from earnings framework or thesis."""
    # Prefer framework over thesis for metrics
    source = framework or thesis
    if not source:
        return []
    metrics = []
    seen = set()

    # Pattern 1: "PASS: metric" / "FAIL: metric" (from earnings frameworks)
    for m in re.finditer(r'(?:PASS|FAIL)[:\s]+([^\n]{15,})', source, re.IGNORECASE):
        text = m.group(1).strip().rstrip('|').strip()
        short = text[:40]
        if short not in seen:
            seen.add(short)
            metrics.append(text[:140])

    # Pattern 2: "Watch: metric" or "Monitor: metric" at start of line
    for m in re.finditer(r'(?:^|\n)\s*(?:[-*]\s*)?(?:Watch|Monitor|Key)[:\s]+([^\n]{10,})', source, re.IGNORECASE):
        text = m.group(1).strip()
        short = text[:40]
        if short not in seen and not text.startswith('for'):
            seen.add(short)
            metrics.append(text[:140])

    # Pattern 3: "| Metric | Threshold |" table rows (from frameworks)
    for m in re.finditer(r'\|\s*([^|]{5,50})\s*\|\s*([^|]{5,50})\s*\|\s*(?:PASS|FAIL|Watch|Monitor)', source, re.IGNORECASE):
        metric_name = m.group(1).strip().strip('*')
        threshold = m.group(2).strip().strip('*')
        text = f"{metric_name}: {threshold}"
        short = text[:40]
        if short not in seen:
            seen.add(short)
            metrics.append(text[:140])

    return metrics[:6]


def get_price_and_mos(ticker, thesis):
    """Get current price and FV/MoS. Uses portfolio fair_value first, then thesis extraction."""
    try:
        import yfinance as yf
        t = yf.Ticker(ticker)
        info = t.info
        price = info.get('currentPrice') or info.get('regularMarketPrice') or info.get('previousClose')
        currency = info.get('currency', 'USD')
        div_yield = info.get('dividendYield', 0) or 0
    except Exception:
        return None, None, None, None, None

    if not price:
        return None, None, None, None, None

    # Try to get FV from portfolio/current.yaml first (most reliable source)
    portfolio = load_yaml(PORTFOLIO_FILE)
    for p in portfolio.get('positions', []):
        if p.get('ticker') == ticker:
            fv_str = p.get('fair_value', '')
            fv_match = re.search(r'([0-9,]+(?:\.\d+)?)', str(fv_str))
            if fv_match:
                try:
                    fv = float(fv_match.group(1).replace(',', ''))
                    mos = ((fv - price) / price) * 100
                    ecagr = ((fv / price) ** (1.0/3.0) - 1.0 + div_yield / 100.0) * 100
                    return price, currency, fv, mos, ecagr
                except (ValueError, ZeroDivisionError):
                    pass

    # Fallback: extract from thesis with multiple patterns
    if thesis:
        # Try header pattern first: "> **Fair Value:** EUR 29.0" or "**Fair Value:** 190 GBp"
        patterns = [
            r'^>?\s*\*\*Fair Value[:\*]*\s*(?:\$|EUR\s*|GBP\s*|DKK\s*|SEK\s*)?([0-9,]+(?:\.\d+)?)\s*(?:p|GBp|EUR|USD|DKK|SEK)?',
            r'Weighted Fair Value[:\s]+(?:\$|EUR\s*)?([0-9,]+(?:\.\d+)?)',
            r'\*\*Fair Value\*\*[:\s]*(?:\$|EUR\s*|GBP\s*|DKK\s*|SEK\s*)?([0-9,]+(?:\.\d+)?)',
        ]
        for pat in patterns:
            fv_match = re.search(pat, thesis, re.IGNORECASE | re.MULTILINE)
            if fv_match:
                try:
                    fv = float(fv_match.group(1).replace(',', ''))
                    if fv > 0:
                        mos = ((fv - price) / price) * 100
                        ecagr = ((fv / price) ** (1.0/3.0) - 1.0 + div_yield / 100.0) * 100
                        return price, currency, fv, mos, ecagr
                except (ValueError, ZeroDivisionError):
                    pass

    return price, currency, None, None, None


def get_insider_signals(ticker):
    """Get insider activity from ownership cache."""
    try:
        sys.path.insert(0, os.path.join(BASE, 'tools'))
        from ownership_cache import load_cache, get_latest_cache, get_insider_sentiment
    except ImportError:
        return None

    cache = load_cache()
    if not cache:
        cache, _ = get_latest_cache()
    if not cache or ticker not in cache:
        return None

    buys, sells, buybacks, options, net, signal = get_insider_sentiment(cache, ticker)
    insiders = cache.get(ticker, {}).get('insiders', [])

    # Get recent activity (last 3 transactions)
    recent = []
    for i in insiders[:3]:
        name = i.get('name', '?')[:20]
        txn_type = i.get('type', '?')
        date = i.get('date', '?')
        recent.append(f"  {date} {txn_type:>7} {name}")

    return {
        'buys': buys,
        'sells': sells,
        'buybacks': buybacks,
        'net': net,
        'signal': signal,
        'recent': recent,
    }


def get_portfolio_info(ticker):
    """Get portfolio-specific info (conviction, invested amount, exit plan)."""
    portfolio = load_yaml(PORTFOLIO_FILE)
    for p in portfolio.get('positions', []):
        if p.get('ticker') == ticker:
            return {
                'conviction': p.get('conviction', '?'),
                'invested': p.get('invested_usd', 0),
                'exit_plan': p.get('exit_plan', ''),
                'notes': p.get('notes', ''),
            }
    return None


def print_briefing(events):
    """Print formatted earnings intelligence briefing."""
    if not events:
        print("No earnings events in the specified timeframe.")
        return

    print()
    print("=" * 80)
    print(f"  EARNINGS INTELLIGENCE BRIEFING — {datetime.now().strftime('%Y-%m-%d')}")
    print(f"  {len(events)} events in view")
    print("=" * 80)

    # Fetch prices for all tickers at once
    tickers = list(set(ev.get('ticker', '') for ev in events))
    print(f"\n  Loading data for {len(tickers)} tickers...\n")

    for ev in events:
        ticker = ev.get('ticker', '')
        date = ev.get('_date')
        days_away = ev.get('_days_away', '?')
        event_text = ev.get('event', '')
        action = ev.get('action', '')
        pos_type = get_position_type(ticker)

        thesis = load_thesis(ticker)
        framework_content, framework_file = load_earnings_framework(ticker)

        print("-" * 80)
        day_label = "TODAY" if days_away == 0 else f"in {days_away}d"
        type_badge = f"[{pos_type}]"
        print(f"  {ticker}  {date}  ({day_label})  {type_badge}")
        print(f"  {event_text}")
        print("-" * 80)

        # Price + MoS
        price, currency, fv, mos, ecagr = get_price_and_mos(ticker, thesis)
        if price:
            price_line = f"  Price: {price:.2f} {currency}"
            if fv is not None:
                price_line += f" | FV: {fv:.0f} | MoS: {mos:+.1f}%"
            if ecagr is not None:
                price_line += f" | E[CAGR]: {ecagr:.1f}%"
            print(price_line)
        else:
            print(f"  Price: unavailable")

        # Portfolio info (if active position)
        port_info = get_portfolio_info(ticker)
        if port_info:
            print(f"  Conviction: {port_info['conviction']} | Invested: ${port_info['invested']:.0f}")
            if port_info['exit_plan']:
                print(f"  Exit Plan: {port_info['exit_plan'][:120]}")

        # Calendar action
        if action:
            print(f"  Action: {action[:140]}")

        # Insider signals
        insider = get_insider_signals(ticker)
        if insider:
            print(f"  Insiders: {insider['signal']} (net: {insider['net']:+d}, buys: {insider['buys']}, sells: {insider['sells']}, buybacks: {insider['buybacks']})")
            if insider['recent']:
                for line in insider['recent']:
                    print(line)

        # Kill conditions
        kcs = extract_kill_conditions(thesis)
        if kcs:
            print(f"  Kill Conditions:")
            for kc in kcs:
                print(f"    {kc}")

        # Scenarios
        scenarios = extract_scenarios(thesis)
        if not scenarios and framework_content:
            scenarios = extract_scenarios(framework_content)
        if scenarios:
            print(f"  Scenarios:")
            for label, text in scenarios.items():
                print(f"    {label}: {text}")

        # Key metrics
        metrics = extract_key_metrics(thesis, framework_content)
        if metrics:
            print(f"  Key Metrics to Watch:")
            for m in metrics:
                print(f"    - {m}")

        # Earnings framework reference
        if framework_file:
            print(f"  Framework: thesis/{'active' if pos_type == 'ACTIVE' else 'research'}/{ticker}/{framework_file}")

        print()

    # Summary
    print("=" * 80)
    active_count = sum(1 for ev in events if get_position_type(ev.get('ticker', '')) == 'ACTIVE')
    pipeline_count = sum(1 for ev in events if get_position_type(ev.get('ticker', '')) == 'PIPELINE')
    print(f"  Summary: {len(events)} events | {active_count} active positions | {pipeline_count} pipeline")
    print(f"  [Raw data. Reason from principles.md + earnings frameworks]")
    print("=" * 80)
    print()


def main():
    parser = argparse.ArgumentParser(description='Earnings Intelligence Briefing')
    parser.add_argument('--days', type=int, default=7, help='Lookahead window in days (default: 7)')
    parser.add_argument('--ticker', type=str, help='Filter to specific ticker')
    args = parser.parse_args()

    events = get_earnings_events(days=args.days, ticker_filter=args.ticker)
    print_briefing(events)


if __name__ == '__main__':
    main()
