#!/usr/bin/env python3
"""
Ownership Analyzer — Extracts actionable signals from institutional ownership data.

Uses shared ownership_cache.py for data (avoids redundant yfinance calls).

Three analysis modes:
  --risk       Overlap matrix + concentration analysis for portfolio positions
  --discover   Check if quality funds (holding 3+ our stocks) also hold candidates
  --sentiment  Net insider buy/sell sentiment per position
  (default)    Risk + Sentiment combined report

Usage:
    python3 tools/ownership_analyzer.py                    # Full risk + sentiment report
    python3 tools/ownership_analyzer.py --risk             # Overlap matrix only
    python3 tools/ownership_analyzer.py --sentiment        # Insider sentiment only
    python3 tools/ownership_analyzer.py --discover         # Smart money screen (top pipeline candidates)
    python3 tools/ownership_analyzer.py --discover TICK1 TICK2  # Check specific tickers
    python3 tools/ownership_analyzer.py --fresh            # Force fresh data (skip cache)
"""

import os
import sys
import yaml
import warnings
from collections import defaultdict
from itertools import combinations

warnings.filterwarnings('ignore')

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE, 'tools'))
from ownership_cache import load_or_fetch, get_quality_funds, get_insider_sentiment, is_indexer

# ─── Parse args ──────────────────────────────────────────────────────────────

MODE_RISK = '--risk' in sys.argv
MODE_DISCOVER = '--discover' in sys.argv
MODE_SENTIMENT = '--sentiment' in sys.argv
MODE_ALL = not (MODE_RISK or MODE_DISCOVER or MODE_SENTIMENT)
FORCE_FRESH = '--fresh' in sys.argv

DISCOVER_TICKERS = []
if MODE_DISCOVER:
    idx = sys.argv.index('--discover')
    DISCOVER_TICKERS = [a for a in sys.argv[idx+1:] if not a.startswith('--')]

# ─── Load data ───────────────────────────────────────────────────────────────

def load_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

portfolio = load_yaml(os.path.join(BASE, 'portfolio', 'current.yaml'))
positions = portfolio.get('positions', [])
port_tickers = [p['ticker'] for p in positions]

# ─── Fetch via shared cache ──────────────────────────────────────────────────

print("=" * 70)
print("OWNERSHIP ANALYZER — Portfolio Institutional Intelligence")
print("=" * 70)

ownership_data = load_or_fetch(port_tickers, force_fresh=FORCE_FRESH)


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
        holders = ownership_data.get(ticker, {}).get('holders', [])
        if not holders:
            print(f"{ticker:<10} {'N/A':>6} {'N/A':>6} {'N/A':>9} {'N/A':>9} {'NO DATA':>10}")
            continue

        sorted_h = sorted(holders, key=lambda x: x.get('pct', 0), reverse=True)
        top1_pct = sorted_h[0]['pct']
        if top1_pct < 1:
            top1_pct *= 100
        top3_raw = sum(h.get('pct', 0) for h in sorted_h[:3])
        top3_pct = top3_raw * 100 if top3_raw < 1 else top3_raw

        n_holders = len(holders)
        n_indexer = sum(1 for h in holders if h.get('is_indexer'))
        indexer_pct = n_indexer / n_holders * 100 if n_holders > 0 else 0

        risk = "HIGH" if top3_pct > 30 else "MODERATE" if top3_pct > 20 else "LOW"
        print(f"{ticker:<10} {top1_pct:>5.1f}% {top3_pct:>5.1f}% {n_holders:>9} {indexer_pct:>8.0f}% {risk:>10}")

    # 1b. Overlap matrix
    print("\n── Institutional Overlap Matrix ──────────────────────────────────")
    print("  (Shared holders between positions — higher = more correlated selling risk)\n")

    holder_sets = {}
    for ticker in port_tickers:
        holder_sets[ticker] = set(h['name'] for h in ownership_data.get(ticker, {}).get('holders', []))

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

    # 1c. Quality funds
    print("\n── Quality Fund Detection ────────────────────────────────────────")
    print("  (Non-indexer funds holding 2+ portfolio stocks = potential smart money)\n")

    quality_funds = get_quality_funds(ownership_data, min_stocks=2)

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
        buys, sells, buybacks, options, net, signal = get_insider_sentiment(ownership_data, ticker)
        insiders = ownership_data.get(ticker, {}).get('insiders', [])

        if not insiders:
            print(f"{ticker:<10} {'--':>5} {'--':>6} {'--':>6} {'--':>5} {'--':>5} {'NO DATA':>10}")
        else:
            print(f"{ticker:<10} {buys:>5} {sells:>6} {buybacks:>6} {options:>5} {net:>+5} {signal:>10}")

    # Detail for positions with notable insider activity
    print("\n── Notable Insider Transactions ──────────────────────────────────")
    for ticker in port_tickers:
        insiders = ownership_data.get(ticker, {}).get('insiders', [])
        buy_txns = [i for i in insiders if i.get('type') == 'BUY']
        sell_txns = [i for i in insiders if i.get('type') == 'SELL']
        bb_txns = [i for i in insiders if i.get('type') == 'BUYBACK']

        if buy_txns:
            print(f"\n  {ticker} — INSIDER BUYS:")
            for txn in buy_txns[:5]:
                date_str = txn.get('date', '?')[:10]
                print(f"    {txn['name'][:30]:<30} {txn.get('shares', 0):>10,} shares  {date_str}  {txn.get('text', '')}")

        if len(sell_txns) >= 3:
            print(f"\n  {ticker} — INSIDER SELLS ({len(sell_txns)} transactions):")
            for txn in sell_txns[:5]:
                date_str = txn.get('date', '?')[:10]
                print(f"    {txn['name'][:30]:<30} {txn.get('shares', 0):>10,} shares  {date_str}  {txn.get('text', '')}")

        if bb_txns:
            print(f"\n  {ticker} — CORPORATE BUYBACKS ({len(bb_txns)} transactions):")
            for txn in bb_txns[:3]:
                date_str = txn.get('date', '?')[:10]
                print(f"    {txn['name'][:30]:<30} {txn.get('shares', 0):>10,} shares  {date_str}  {txn.get('text', '')}")


# ─── SMART MONEY DISCOVERY ───────────────────────────────────────────────────

def discover_smart_money(quality_funds):
    print("\n" + "=" * 70)
    print("SECTION 3: SMART MONEY DISCOVERY")
    print("=" * 70)

    if not quality_funds:
        print("\n  No quality funds detected from portfolio analysis.")
        return

    quality_fund_names = set(f[0] for f in quality_funds)
    print(f"\n  Quality funds to track: {len(quality_fund_names)}")
    for name, stocks in quality_funds[:10]:
        print(f"    {name[:45]} → holds {', '.join(sorted(stocks))}")

    # Get candidate tickers
    if DISCOVER_TICKERS:
        candidates = DISCOVER_TICKERS
    else:
        try:
            universe = load_yaml(os.path.join(BASE, 'state', 'quality_universe.yaml'))
            companies = universe.get('quality_universe', {}).get('companies', [])
            candidates = []
            for c in companies:
                t = c.get('ticker', '')
                dist = c.get('distance_to_entry')
                if t not in port_tickers and dist is not None and dist < 40:
                    candidates.append(t)
            candidates = candidates[:20]
        except Exception:
            print("  Could not load quality_universe.yaml. Provide tickers: --discover TICK1 TICK2")
            return

    if not candidates:
        print("  No candidates to check.")
        return

    # Fetch candidate ownership data (also via cache)
    print(f"\n  Checking {len(candidates)} candidates for quality fund overlap...")
    candidate_data = load_or_fetch(candidates, force_fresh=FORCE_FRESH)

    results = []
    for ticker in candidates:
        holders = candidate_data.get(ticker, {}).get('holders', [])
        holder_names = set(h['name'] for h in holders)
        shared = holder_names & quality_fund_names
        results.append((ticker, len(shared), shared))

    results.sort(key=lambda x: x[1], reverse=True)

    print(f"\n{'Ticker':<12} {'QF Overlap':>11} {'Signal':>10}  Quality Funds Shared")
    print("-" * 75)
    for ticker, n_shared, shared in results:
        signal = "STRONG" if n_shared >= 3 else "MODERATE" if n_shared >= 2 else "WEAK" if n_shared >= 1 else "NONE"
        fund_str = ', '.join(list(shared)[:3])
        if len(shared) > 3:
            fund_str += f" +{len(shared)-3}"
        print(f"{ticker:<12} {n_shared:>11} {signal:>10}  {fund_str[:45]}")

    strong = [r for r in results if r[1] >= 2]
    if strong:
        print(f"\n  ACTIONABLE: {len(strong)} candidates with quality fund overlap >= 2:")
        for ticker, n_shared, shared in strong:
            print(f"    {ticker}: {n_shared} quality funds → {', '.join(shared)}")


# ─── MAIN ────────────────────────────────────────────────────────────────────

quality_funds = []

if MODE_ALL or MODE_RISK:
    quality_funds = analyze_risk()

if MODE_ALL or MODE_SENTIMENT:
    analyze_sentiment()

if MODE_DISCOVER:
    if not quality_funds:
        quality_funds = analyze_risk()
    discover_smart_money(quality_funds)

print("\n" + "=" * 70)
print("Ownership analysis complete. Data is RAW — interpret with context.")
print("=" * 70)
