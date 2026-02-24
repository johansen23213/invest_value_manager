#!/usr/bin/env python3
"""
Ownership Cache — Shared data layer for all ownership intelligence tools.

Provides cached institutional holder + insider transaction data.
All ownership tools (graph, analyzer, heatmap) should use this module
to avoid redundant yfinance calls.

Cache location: state/ownership_snapshots/ownership_YYYY-MM-DD.yaml
Cache is considered fresh if saved today.

Usage as module:
    from ownership_cache import load_or_fetch, get_quality_funds

Usage as script:
    python3 tools/ownership_cache.py TICK1 TICK2 ...    # Fetch and cache
    python3 tools/ownership_cache.py --portfolio         # Fetch portfolio tickers
    python3 tools/ownership_cache.py --all               # Portfolio + standing orders
    python3 tools/ownership_cache.py --status             # Show cache status
"""

import os
import sys
import yaml
import warnings
from datetime import datetime, timedelta
from collections import defaultdict

warnings.filterwarnings('ignore')

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE_DIR = os.path.join(BASE, 'state', 'ownership_snapshots')
os.makedirs(CACHE_DIR, exist_ok=True)

INDEXER_KEYWORDS = [
    'vanguard', 'blackrock', 'ishares', 'spdr', 'state street', 'schwab',
    'fidelity 500', 'total stock', 'total market', 'russell',
    's&p 500', 'index fund', 'etf trust', 'geode capital',
    'northern trust', 'bank of new york', 'legal & general',
]


def is_indexer(name):
    nl = name.lower()
    return any(kw in nl for kw in INDEXER_KEYWORDS)


def _cache_path(date_str=None):
    if not date_str:
        date_str = datetime.now().strftime('%Y-%m-%d')
    return os.path.join(CACHE_DIR, f'ownership_{date_str}.yaml')


def load_cache(date_str=None):
    """Load cached ownership data for a specific date (default: today)."""
    path = _cache_path(date_str)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f) or {}
    return {}


def save_cache(data, date_str=None):
    """Save ownership data to cache."""
    path = _cache_path(date_str)
    with open(path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
    return path


def cache_is_fresh():
    """Check if today's cache exists."""
    return os.path.exists(_cache_path())


def get_latest_cache():
    """Get the most recent cache file and its date."""
    files = sorted([f for f in os.listdir(CACHE_DIR)
                    if f.startswith('ownership_') and f.endswith('.yaml')])
    if files:
        latest = files[-1]
        date_str = latest.replace('ownership_', '').replace('.yaml', '')
        return load_cache(date_str), date_str
    return {}, None


def get_previous_cache():
    """Get the most recent cache BEFORE today (for diffs)."""
    today = datetime.now().strftime('%Y-%m-%d')
    files = sorted([f for f in os.listdir(CACHE_DIR)
                    if f.startswith('ownership_') and f.endswith('.yaml')])
    for f in reversed(files):
        date_str = f.replace('ownership_', '').replace('.yaml', '')
        if date_str < today:
            return load_cache(date_str), date_str
    return {}, None


def fetch_ticker(ticker, top_funds=10, max_insiders=15):
    """Fetch ownership data for a single ticker from yfinance."""
    import yfinance as yf
    import pandas as pd

    entry = {'holders': [], 'insiders': [], 'fetched': datetime.now().strftime('%Y-%m-%d %H:%M')}

    try:
        t = yf.Ticker(ticker)

        # Institutional holders
        try:
            inst = t.institutional_holders
            if inst is not None and isinstance(inst, pd.DataFrame) and not inst.empty:
                holder_col = 'Holder' if 'Holder' in inst.columns else inst.columns[0]
                for _, row in inst.head(top_funds).iterrows():
                    name = str(row.get(holder_col, 'Unknown')).strip()
                    pct = row.get('% Out', row.get('pctHeld', 0))
                    shares = row.get('Shares', 0)
                    value = row.get('Value', 0)
                    if name and name != 'nan':
                        entry['holders'].append({
                            'name': name,
                            'pct': float(pct) if pct else 0,
                            'shares': int(shares) if shares else 0,
                            'value': float(value) if value else 0,
                            'is_indexer': is_indexer(name),
                        })
        except Exception:
            pass

        # Insider transactions
        try:
            ins = t.insider_transactions
            if ins is not None and isinstance(ins, pd.DataFrame) and not ins.empty:
                for _, row in ins.head(max_insiders).iterrows():
                    name = str(row.get('Insider', row.get('insider', 'Unknown'))).strip()
                    text = str(row.get('Text', row.get('text', '')))
                    shares = row.get('Shares', row.get('shares', 0))
                    date_val = str(row.get('Start Date', row.get('startDate', '')))

                    text_lower = text.lower() if text else ''
                    if 'buy back' in text_lower or 'buyback' in text_lower:
                        txn_type = 'BUYBACK'
                    elif 'purchase' in text_lower or 'buy' in text_lower or 'acquisition' in text_lower:
                        txn_type = 'BUY'
                    elif 'sale' in text_lower or 'sell' in text_lower or 'disposition' in text_lower:
                        txn_type = 'SELL'
                    elif 'option' in text_lower or 'exercise' in text_lower:
                        txn_type = 'OPTION'
                    else:
                        txn_type = 'OTHER'

                    # Extract position/title and value
                    position = str(row.get('Position', row.get('position', '')))
                    if position == 'nan' or not position:
                        position = ''
                    value = row.get('Value', row.get('value', 0))

                    if name and name != 'nan':
                        entry['insiders'].append({
                            'name': name,
                            'title': position[:50],
                            'type': txn_type,
                            'shares': int(shares) if shares else 0,
                            'value': float(value) if value and str(value) != 'nan' else 0,
                            'date': date_val[:10] if date_val and date_val != 'nan' else '',
                            'text': text[:80],
                        })
        except Exception:
            pass

    except Exception:
        pass

    return entry


def load_or_fetch(tickers, force_fresh=False, top_funds=10, verbose=True):
    """Load from cache if fresh, otherwise fetch from yfinance.

    Returns dict: {ticker: {holders: [...], insiders: [...]}}
    Only fetches tickers not already in today's cache.
    """
    data = {} if force_fresh else load_cache()
    missing = [t for t in tickers if t not in data]

    if missing and not force_fresh:
        # Check if we have ANY data (even stale) to avoid unnecessary fetches
        if not data:
            latest, latest_date = get_latest_cache()
            if latest and not force_fresh:
                # Use latest cache as starting point, only fetch truly missing
                for t in tickers:
                    if t in latest and t not in data:
                        data[t] = latest[t]
                missing = [t for t in tickers if t not in data]

    if missing:
        if verbose:
            print(f"  Fetching ownership data for {len(missing)} tickers (cached: {len(tickers) - len(missing)})...")
        for ticker in missing:
            if verbose:
                print(f"    {ticker}...", end=" ", flush=True)
            entry = fetch_ticker(ticker, top_funds=top_funds)
            data[ticker] = entry
            if verbose:
                print(f"h:{len(entry['holders'])} i:{len(entry['insiders'])}")

        # Save updated cache
        save_cache(data)
        if verbose:
            print(f"  Cache updated: {_cache_path()}")
    elif verbose:
        print(f"  Using cached data for {len(tickers)} tickers (fresh today)")

    # Return only requested tickers
    return {t: data.get(t, {'holders': [], 'insiders': []}) for t in tickers}


def get_quality_funds(ownership_data, min_stocks=2):
    """Identify quality funds (non-indexer holding min_stocks+ of the provided tickers).

    Returns: list of (fund_name, set_of_tickers)
    """
    fund_stocks = defaultdict(set)
    for ticker, data in ownership_data.items():
        for h in data.get('holders', []):
            if not h.get('is_indexer', False):
                fund_stocks[h['name']].add(ticker)

    quality = [(name, stocks) for name, stocks in fund_stocks.items()
               if len(stocks) >= min_stocks]
    quality.sort(key=lambda x: len(x[1]), reverse=True)
    return quality


def get_insider_sentiment(ownership_data, ticker):
    """Get insider sentiment summary for a ticker.

    Returns: (buys, sells, buybacks, options, net, signal)
    """
    data = ownership_data.get(ticker, {})
    insiders = data.get('insiders', [])
    buys = sum(1 for i in insiders if i.get('type') == 'BUY')
    sells = sum(1 for i in insiders if i.get('type') == 'SELL')
    buybacks = sum(1 for i in insiders if i.get('type') == 'BUYBACK')
    options = sum(1 for i in insiders if i.get('type') == 'OPTION')
    net = buys - sells

    if buys > 0 and net > 0:
        signal = 'BULLISH'
    elif net == 0 and buybacks > 0:
        signal = 'BB+'
    elif net == 0 or not insiders:
        signal = 'NEUTRAL'
    elif net >= -2:
        signal = 'CAUTIOUS'
    else:
        signal = 'BEARISH'

    return buys, sells, buybacks, options, net, signal


def compute_diff(current_data, previous_data):
    """Compute changes between two ownership snapshots.

    Returns: list of {ticker, new_holders, lost_holders, insider_change}
    """
    diffs = []
    all_tickers = set(current_data.keys()) | set(previous_data.keys())

    for ticker in all_tickers:
        curr = current_data.get(ticker, {})
        prev = previous_data.get(ticker, {})

        curr_holders = set(h['name'] for h in curr.get('holders', []))
        prev_holders = set(h.get('name', '') for h in prev.get('holders', []))
        new_holders = curr_holders - prev_holders
        lost_holders = prev_holders - curr_holders

        curr_ins = curr.get('insiders', [])
        prev_ins = prev.get('insiders', [])
        curr_net = sum(1 for i in curr_ins if i.get('type') == 'BUY') - sum(1 for i in curr_ins if i.get('type') == 'SELL')
        prev_net = sum(1 for i in prev_ins if i.get('type') == 'BUY') - sum(1 for i in prev_ins if i.get('type') == 'SELL')

        if new_holders or lost_holders or curr_net != prev_net:
            diffs.append({
                'ticker': ticker,
                'new_holders': list(new_holders),
                'lost_holders': list(lost_holders),
                'insider_change': curr_net - prev_net,
            })

    return diffs


# ─── CLI mode ────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    if '--status' in sys.argv:
        files = sorted([f for f in os.listdir(CACHE_DIR)
                        if f.startswith('ownership_') and f.endswith('.yaml')])
        print(f"Ownership Cache Status")
        print(f"  Location: {CACHE_DIR}")
        print(f"  Snapshots: {len(files)}")
        for f in files[-5:]:
            path = os.path.join(CACHE_DIR, f)
            data = load_cache(f.replace('ownership_', '').replace('.yaml', ''))
            print(f"    {f}: {len(data)} tickers")
        print(f"  Fresh today: {'YES' if cache_is_fresh() else 'NO'}")
        sys.exit(0)

    # Determine tickers to fetch
    tickers = []
    if '--portfolio' in sys.argv or '--all' in sys.argv or '--pipeline' in sys.argv:
        portfolio = yaml.safe_load(open(os.path.join(BASE, 'portfolio', 'current.yaml')))
        tickers = [p['ticker'] for p in portfolio.get('positions', [])]

    if '--all' in sys.argv or '--pipeline' in sys.argv:
        so_data = yaml.safe_load(open(os.path.join(BASE, 'state', 'standing_orders.yaml')))
        for so in so_data.get('standing_orders', []):
            t = so.get('ticker', '')
            if t and t not in tickers:
                tickers.append(t)

    if '--pipeline' in sys.argv:
        # Add top pipeline candidates from quality_universe (by QS, near entry)
        universe_path = os.path.join(BASE, 'state', 'quality_universe.yaml')
        if os.path.exists(universe_path):
            udata = yaml.safe_load(open(universe_path))
            companies = udata.get('quality_universe', {}).get('companies', [])
            # Filter: has thesis, long direction, reasonable distance
            pipeline = [
                c for c in companies
                if c.get('direction', 'long') == 'long'
                and c.get('pipeline_status') in ('SCORED', 'R1_COMPLETE', 'R3_COMPLETE', 'APPROVED', 'STANDING_ORDER')
                and c.get('ticker') not in tickers
            ]
            # Sort by QS descending, take top 20
            pipeline.sort(key=lambda c: -(c.get('qs_adj') or c.get('qs_tool') or 0))
            for c in pipeline[:20]:
                tickers.append(c['ticker'])
            print(f"  Pipeline: added {min(20, len(pipeline))} universe candidates (top by QS)")

    # Add any explicit tickers
    for arg in sys.argv[1:]:
        if not arg.startswith('--') and arg not in tickers:
            tickers.append(arg)

    if not tickers:
        print("Usage: python3 tools/ownership_cache.py [--portfolio|--all|--pipeline|TICK1 TICK2] [--status|--fresh]")
        sys.exit(1)

    print(f"Fetching/caching ownership data for {len(tickers)} tickers...")
    data = load_or_fetch(tickers, force_fresh='--fresh' in sys.argv)
    print(f"\nDone. {len(data)} tickers cached.")

    # Quick summary
    for ticker, d in data.items():
        h = len(d.get('holders', []))
        i = len(d.get('insiders', []))
        _, _, _, _, net, signal = get_insider_sentiment(data, ticker)
        print(f"  {ticker}: {h} holders, {i} insider txns, sentiment={signal}")
