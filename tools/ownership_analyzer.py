#!/usr/bin/env python3
"""
Ownership Analyzer — Extracts actionable signals from institutional ownership data.

Three analysis modes:
  --risk       Overlap matrix + concentration analysis for portfolio positions
  --discover   Check if quality funds (holding 3+ our stocks) also hold candidates
  --sentiment  Net insider buy/sell sentiment per position
  (default)    Risk + Sentiment combined report

Smart Money Discovery:
  Identifies "quality funds" = non-indexer institutional holders appearing in 3+ portfolio stocks.
  Then checks candidate tickers (from pipeline/universe) for shared quality fund ownership.
  Higher overlap with quality funds = stronger conviction signal.

Usage:
    python3 tools/ownership_analyzer.py                    # Full risk + sentiment report
    python3 tools/ownership_analyzer.py --risk             # Overlap matrix only
    python3 tools/ownership_analyzer.py --sentiment        # Insider sentiment only
    python3 tools/ownership_analyzer.py --discover         # Smart money screen (top pipeline candidates)
    python3 tools/ownership_analyzer.py --discover TICK1 TICK2  # Check specific tickers
"""

import os
import sys
import yaml
import warnings
from collections import defaultdict
from itertools import combinations

warnings.filterwarnings('ignore')

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ─── Parse args ──────────────────────────────────────────────────────────────

MODE_RISK = '--risk' in sys.argv
MODE_DISCOVER = '--discover' in sys.argv
MODE_SENTIMENT = '--sentiment' in sys.argv
MODE_ALL = not (MODE_RISK or MODE_DISCOVER or MODE_SENTIMENT)

# Discover tickers (if provided after --discover)
DISCOVER_TICKERS = []
if MODE_DISCOVER:
    idx = sys.argv.index('--discover')
    DISCOVER_TICKERS = [a for a in sys.argv[idx+1:] if not a.startswith('--')]

TOP_FUNDS = 10  # fetch top 10 institutional holders per stock for better overlap detection

# ─── Load data ───────────────────────────────────────────────────────────────

def load_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

portfolio = load_yaml(os.path.join(BASE, 'portfolio', 'current.yaml'))
positions = portfolio.get('positions', [])
port_tickers = [p['ticker'] for p in positions]

# ─── Fetch ownership data ────────────────────────────────────────────────────

import yfinance as yf
import pandas as pd

# Data stores
inst_holders = {}     # ticker -> [(fund_name, pct_held, shares, value), ...]
insider_txns = {}     # ticker -> [(name, type, shares, date, text), ...]
fund_stocks = defaultdict(set)  # fund_name -> set of tickers it appears in

# Known indexer/passive fund parent names (aggregate holders are mostly passive)
INDEXER_KEYWORDS = [
    'vanguard', 'blackrock', 'ishares', 'spdr', 'state street', 'schwab',
    'fidelity 500', 'total stock', 'total market', 'russell',
    's&p 500', 'index fund', 'etf trust', 'geode capital',
    'northern trust', 'bank of new york', 'legal & general',
]

def is_indexer_name(name):
    nl = name.lower()
    return any(kw in nl for kw in INDEXER_KEYWORDS)


def fetch_stock_data(ticker):
    """Fetch institutional holders + insider transactions for a ticker."""
    holders = []
    insiders = []

    try:
        t = yf.Ticker(ticker)

        # Institutional holders
        try:
            inst = t.institutional_holders
            if inst is not None and isinstance(inst, pd.DataFrame) and not inst.empty:
                holder_col = 'Holder' if 'Holder' in inst.columns else inst.columns[0]
                for _, row in inst.head(TOP_FUNDS).iterrows():
                    fund_name = str(row.get(holder_col, 'Unknown')).strip()
                    if not fund_name or fund_name == 'nan':
                        continue
                    pct = row.get('% Out', row.get('pctHeld', 0))
                    shares = row.get('Shares', 0)
                    value = row.get('Value', 0)
                    holders.append((fund_name, float(pct) if pct else 0, int(shares) if shares else 0, float(value) if value else 0))
                    fund_stocks[fund_name].add(ticker)
        except Exception:
            pass

        # Insider transactions
        try:
            ins = t.insider_transactions
            if ins is not None and isinstance(ins, pd.DataFrame) and not ins.empty:
                for _, row in ins.head(15).iterrows():
                    name = str(row.get('Insider', row.get('insider', 'Unknown'))).strip()
                    text = str(row.get('Text', row.get('text', '')))
                    shares = row.get('Shares', row.get('shares', 0))
                    date = str(row.get('Start Date', row.get('startDate', '')))

                    text_lower = text.lower() if text else ''
                    if 'buy back' in text_lower or 'buyback' in text_lower or 'repurchase' in text_lower:
                        txn_type = 'BUYBACK'
                    elif 'purchase' in text_lower or 'buy' in text_lower or 'acquisition' in text_lower:
                        txn_type = 'BUY'
                    elif 'sale' in text_lower or 'sell' in text_lower or 'disposition' in text_lower:
                        txn_type = 'SELL'
                    elif 'option' in text_lower or 'exercise' in text_lower:
                        txn_type = 'OPTION'
                    else:
                        txn_type = 'OTHER'

                    if name and name != 'nan':
                        insiders.append((name, txn_type, int(shares) if shares else 0, date, text[:60]))
        except Exception:
            pass

    except Exception as e:
        print(f"  FAILED {ticker}: {e}")

    return holders, insiders


# ─── Fetch portfolio data ────────────────────────────────────────────────────

print("=" * 70)
print("OWNERSHIP ANALYZER — Portfolio Institutional Intelligence")
print("=" * 70)
print(f"\nFetching data for {len(port_tickers)} portfolio positions...")

for ticker in port_tickers:
    print(f"  {ticker}...", end=" ", flush=True)
    h, i = fetch_stock_data(ticker)
    inst_holders[ticker] = h
    insider_txns[ticker] = i
    print(f"holders:{len(h)} insiders:{len(i)}")


# ─── RISK ANALYSIS ──────────────────────────────────────────────────────────

def analyze_risk():
    print("\n" + "=" * 70)
    print("SECTION 1: OWNERSHIP RISK ANALYSIS")
    print("=" * 70)

    # 1a. Concentration per position
    print("\n── Holder Concentration ──────────────────────────────────────────")
    print(f"{'Ticker':<10} {'Top1%':>6} {'Top3%':>6} {'#Holders':>9} {'Indexer%':>9} {'Risk':>10}")
    print("-" * 55)

    for ticker in port_tickers:
        holders = inst_holders.get(ticker, [])
        if not holders:
            print(f"{ticker:<10} {'N/A':>6} {'N/A':>6} {'N/A':>9} {'N/A':>9} {'NO DATA':>10}")
            continue

        # Sort by pct held
        sorted_h = sorted(holders, key=lambda x: x[1], reverse=True)
        top1_pct = sorted_h[0][1] * 100 if sorted_h[0][1] < 1 else sorted_h[0][1]
        top3_pct = sum(h[1] for h in sorted_h[:3]) * 100 if sorted_h[0][1] < 1 else sum(h[1] for h in sorted_h[:3])

        n_holders = len(holders)
        n_indexer = sum(1 for h in holders if is_indexer_name(h[0]))
        indexer_pct = n_indexer / n_holders * 100 if n_holders > 0 else 0

        # Risk classification
        if top3_pct > 30:
            risk = "HIGH"
        elif top3_pct > 20:
            risk = "MODERATE"
        else:
            risk = "LOW"

        print(f"{ticker:<10} {top1_pct:>5.1f}% {top3_pct:>5.1f}% {n_holders:>9} {indexer_pct:>8.0f}% {risk:>10}")

    # 1b. Overlap matrix
    print("\n── Institutional Overlap Matrix ──────────────────────────────────")
    print("  (Shared holders between positions — higher = more correlated selling risk)\n")

    # Build holder sets per ticker
    holder_sets = {}
    for ticker in port_tickers:
        holder_sets[ticker] = set(h[0] for h in inst_holders.get(ticker, []))

    # Find pairs with highest overlap
    overlaps = []
    for t1, t2 in combinations(port_tickers, 2):
        s1, s2 = holder_sets.get(t1, set()), holder_sets.get(t2, set())
        shared = s1 & s2
        total = s1 | s2
        if total:
            overlap_pct = len(shared) / len(total) * 100
            overlaps.append((t1, t2, len(shared), overlap_pct, shared))

    overlaps.sort(key=lambda x: x[3], reverse=True)

    print(f"{'Pair':<22} {'Shared':>7} {'Overlap%':>9} {'Risk':>8}  Shared Funds")
    print("-" * 80)
    for t1, t2, n_shared, pct, shared in overlaps[:15]:
        risk = "HIGH" if pct > 50 else "MODERATE" if pct > 30 else "LOW"
        fund_names = ', '.join(sorted(list(shared))[:3])
        if len(shared) > 3:
            fund_names += f" +{len(shared)-3}"
        print(f"{t1+'/'+t2:<22} {n_shared:>7} {pct:>8.1f}% {risk:>8}  {fund_names[:45]}")

    # 1c. Quality funds (non-indexer, holding 3+ of our stocks)
    print("\n── Quality Fund Detection ────────────────────────────────────────")
    print("  (Non-indexer funds holding 3+ portfolio stocks = potential smart money)\n")

    quality_funds = []
    for fund_name, stock_set in fund_stocks.items():
        portfolio_stocks = stock_set & set(port_tickers)
        if len(portfolio_stocks) >= 2 and not is_indexer_name(fund_name):
            quality_funds.append((fund_name, portfolio_stocks))

    quality_funds.sort(key=lambda x: len(x[1]), reverse=True)

    if quality_funds:
        print(f"{'Fund':<40} {'#Stocks':>8}  Stocks Held")
        print("-" * 75)
        for fund_name, stocks_held in quality_funds[:20]:
            print(f"{fund_name[:39]:<40} {len(stocks_held):>8}  {', '.join(sorted(stocks_held))}")
        print(f"\n  Total quality funds detected: {len(quality_funds)}")
    else:
        print("  No quality funds detected (need funds in 2+ portfolio stocks)")

    return quality_funds


# ─── INSIDER SENTIMENT ───────────────────────────────────────────────────────

def analyze_sentiment():
    print("\n" + "=" * 70)
    print("SECTION 2: INSIDER SENTIMENT")
    print("=" * 70)

    print(f"\n{'Ticker':<10} {'Buys':>5} {'Sells':>6} {'BBack':>6} {'Opts':>5} {'Net':>5} {'Signal':>10}")
    print("-" * 55)

    for ticker in port_tickers:
        txns = insider_txns.get(ticker, [])
        if not txns:
            print(f"{ticker:<10} {'--':>5} {'--':>6} {'--':>6} {'--':>5} {'--':>5} {'NO DATA':>10}")
            continue

        buys = sum(1 for t in txns if t[1] == 'BUY')
        sells = sum(1 for t in txns if t[1] == 'SELL')
        buybacks = sum(1 for t in txns if t[1] == 'BUYBACK')
        options = sum(1 for t in txns if t[1] == 'OPTION')
        # Net = insider buys - insider sells (buybacks are corporate, not insider sentiment)
        net = buys - sells

        if buys > 0 and net > 0:
            signal = "BULLISH"
        elif net < -2:
            signal = "BEARISH"
        elif sells > 0 and buys == 0:
            signal = "CAUTIOUS"
        elif buybacks > 0 and sells == 0:
            signal = "CORP BB+"
        else:
            signal = "NEUTRAL"

        print(f"{ticker:<10} {buys:>5} {sells:>6} {buybacks:>6} {options:>5} {net:>+5} {signal:>10}")

    # Detail for positions with notable insider activity
    print("\n── Notable Insider Transactions ──────────────────────────────────")
    for ticker in port_tickers:
        txns = insider_txns.get(ticker, [])
        buys = [t for t in txns if t[1] == 'BUY']
        sells = [t for t in txns if t[1] == 'SELL']
        buybacks = [t for t in txns if t[1] == 'BUYBACK']

        if buys:
            print(f"\n  {ticker} — INSIDER BUYS:")
            for name, ttype, shares, date, text in buys[:5]:
                date_str = date[:10] if date and date != 'nan' else '?'
                print(f"    {name[:30]:<30} {shares:>10,} shares  {date_str}  {text}")

        if len(sells) >= 3:  # only show if pattern of selling
            print(f"\n  {ticker} — INSIDER SELLS ({len(sells)} transactions):")
            for name, ttype, shares, date, text in sells[:5]:
                date_str = date[:10] if date and date != 'nan' else '?'
                print(f"    {name[:30]:<30} {shares:>10,} shares  {date_str}  {text}")

        if buybacks:
            print(f"\n  {ticker} — CORPORATE BUYBACKS ({len(buybacks)} transactions):")
            for name, ttype, shares, date, text in buybacks[:3]:
                date_str = date[:10] if date and date != 'nan' else '?'
                print(f"    {name[:30]:<30} {shares:>10,} shares  {date_str}  {text}")


# ─── SMART MONEY DISCOVERY ───────────────────────────────────────────────────

def discover_smart_money(quality_funds):
    print("\n" + "=" * 70)
    print("SECTION 3: SMART MONEY DISCOVERY")
    print("=" * 70)

    if not quality_funds:
        print("\n  No quality funds detected from portfolio analysis.")
        print("  Run without --discover first to identify quality funds.")
        return

    quality_fund_names = set(f[0] for f in quality_funds)
    print(f"\n  Quality funds to track: {len(quality_fund_names)}")
    for name, stocks in quality_funds[:10]:
        print(f"    {name[:45]} → holds {', '.join(sorted(stocks))}")

    # Get candidate tickers
    if DISCOVER_TICKERS:
        candidates = DISCOVER_TICKERS
    else:
        # Auto-select: pipeline candidates near entry
        try:
            universe = load_yaml(os.path.join(BASE, 'state', 'quality_universe.yaml'))
            companies = universe.get('quality_universe', {}).get('companies', [])
            # Filter: not in portfolio, distance < 40%, has pipeline status
            candidates = []
            for c in companies:
                t = c.get('ticker', '')
                dist = c.get('distance_to_entry')
                if t not in port_tickers and dist is not None and dist < 40:
                    candidates.append(t)
            candidates = candidates[:20]  # limit to 20 for API rate limits
        except Exception:
            print("  Could not load quality_universe.yaml. Provide tickers: --discover TICK1 TICK2")
            return

    if not candidates:
        print("  No candidates to check. Provide tickers or ensure universe has near-entry stocks.")
        return

    print(f"\n  Checking {len(candidates)} candidates for quality fund overlap...")
    print("-" * 70)

    results = []
    for ticker in candidates:
        print(f"  {ticker}...", end=" ", flush=True)
        holders, _ = fetch_stock_data(ticker)
        holder_names = set(h[0] for h in holders)
        shared = holder_names & quality_fund_names
        results.append((ticker, len(shared), shared, holders))
        print(f"quality_overlap: {len(shared)}/{len(quality_fund_names)}")

    # Sort by quality fund overlap
    results.sort(key=lambda x: x[1], reverse=True)

    print(f"\n{'Ticker':<12} {'QF Overlap':>11} {'Signal':>10}  Quality Funds Shared")
    print("-" * 75)
    for ticker, n_shared, shared, holders in results:
        if n_shared >= 3:
            signal = "STRONG"
        elif n_shared >= 2:
            signal = "MODERATE"
        elif n_shared >= 1:
            signal = "WEAK"
        else:
            signal = "NONE"

        fund_str = ', '.join(list(shared)[:3])
        if len(shared) > 3:
            fund_str += f" +{len(shared)-3}"
        print(f"{ticker:<12} {n_shared:>11} {signal:>10}  {fund_str[:45]}")

    # Highlight
    strong = [r for r in results if r[1] >= 2]
    if strong:
        print(f"\n  ACTIONABLE: {len(strong)} candidates with quality fund overlap >= 2:")
        for ticker, n_shared, shared, _ in strong:
            print(f"    {ticker}: {n_shared} quality funds → {', '.join(shared)}")


# ─── MAIN ────────────────────────────────────────────────────────────────────

quality_funds = []

if MODE_ALL or MODE_RISK:
    quality_funds = analyze_risk()

if MODE_ALL or MODE_SENTIMENT:
    analyze_sentiment()

if MODE_DISCOVER:
    if not quality_funds:
        # Need to run risk analysis first to identify quality funds
        quality_funds = analyze_risk()
    discover_smart_money(quality_funds)

print("\n" + "=" * 70)
print("Ownership analysis complete. Data is RAW — interpret with context.")
print("=" * 70)
