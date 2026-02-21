#!/usr/bin/env python3
"""
Risk Heatmap — Interactive HTML dashboard showing all risk dimensions per position.

Generates a sortable, color-coded heatmap where:
  Rows = portfolio positions
  Columns = risk dimensions (QS tier, MoS, insider sentiment, holder concentration,
            earnings proximity, conviction, E[CAGR])

Colors: green (low risk / positive) → yellow (moderate) → red (high risk / negative)

Also includes:
  - Ownership data caching (saves snapshots for temporal diff)
  - Change detection vs previous snapshot

Usage:
    python3 tools/risk_heatmap.py                  # Full heatmap with fresh data
    python3 tools/risk_heatmap.py --cached          # Use cached ownership data (fast)
    python3 tools/risk_heatmap.py --diff            # Show changes vs previous snapshot

Output: docs/risk_heatmap.html
"""

import os
import sys
import json
import yaml
import re
import warnings
from datetime import datetime, timedelta
from collections import defaultdict

warnings.filterwarnings('ignore')

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT = os.path.join(BASE, 'docs', 'risk_heatmap.html')
CACHE_DIR = os.path.join(BASE, 'state', 'ownership_snapshots')
os.makedirs(CACHE_DIR, exist_ok=True)

USE_CACHE = '--cached' in sys.argv
SHOW_DIFF = '--diff' in sys.argv

# ─── Load YAML files ────────────────────────────────────────────────────────

def load_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

portfolio = load_yaml(os.path.join(BASE, 'portfolio', 'current.yaml'))
calendar = load_yaml(os.path.join(BASE, 'state', 'calendar.yaml'))
system = load_yaml(os.path.join(BASE, 'state', 'system.yaml'))

positions = portfolio.get('positions', [])
events = calendar.get('events', []) if calendar else []

# ─── Extract position metadata ──────────────────────────────────────────────

def extract_number(s, prefix=''):
    """Extract numeric value from strings like '$390', 'EUR 35', '240 GBp'."""
    if not s:
        return None
    s = str(s)
    # Remove common prefixes
    for p in ['$', 'EUR ', 'GBp ', 'USD ', '£', 'CHF ']:
        s = s.replace(p, '')
    # Find first number
    m = re.search(r'[\d.]+', s)
    return float(m.group()) if m else None


def extract_qs_tier(fv_str):
    """Extract QS and tier from fair_value string like 'QS Tool 76, Adj 73'."""
    if not fv_str:
        return None, None
    s = str(fv_str)
    # Look for QS in notes or fair_value
    qs_match = re.search(r'(?:QS\s*(?:Tool\s*)?|Adj\s*)(\d+)', s)
    tier_match = re.search(r'Tier\s*([A-D])', s)
    qs = int(qs_match.group(1)) if qs_match else None
    tier = tier_match.group(1) if tier_match else None
    return qs, tier


def get_currency(fv_str):
    """Detect currency from fair_value string."""
    if not fv_str:
        return 'USD'
    s = str(fv_str)
    if 'EUR' in s:
        return 'EUR'
    if 'GBp' in s or 'GBP' in s:
        return 'GBp'
    if '$' in s:
        return 'USD'
    if 'CHF' in s:
        return 'CHF'
    return 'USD'


# ─── Fetch prices ───────────────────────────────────────────────────────────

import yfinance as yf
import pandas as pd

print("=" * 60)
print("RISK HEATMAP — Multi-Dimensional Position Risk Dashboard")
print("=" * 60)

# Get FX rates
print("\nFetching FX rates...", end=" ", flush=True)
fx = {}
try:
    for pair in ['EURUSD=X', 'GBPUSD=X', 'CHFUSD=X']:
        t = yf.Ticker(pair)
        h = t.history(period='1d')
        if not h.empty:
            fx[pair] = h['Close'].iloc[-1]
    print(f"EUR/USD={fx.get('EURUSD=X', 'N/A'):.4f}, GBP/USD={fx.get('GBPUSD=X', 'N/A'):.4f}")
except Exception as e:
    print(f"FX error: {e}")

eur_usd = fx.get('EURUSD=X', 1.05)
gbp_usd = fx.get('GBPUSD=X', 1.27)

# Get prices for all positions
tickers = [p['ticker'] for p in positions]
print(f"Fetching prices for {len(tickers)} positions...")
prices = {}
for ticker in tickers:
    try:
        t = yf.Ticker(ticker)
        h = t.history(period='2d')
        if not h.empty:
            prices[ticker] = h['Close'].iloc[-1]
            print(f"  {ticker}: {prices[ticker]:.2f}")
    except Exception:
        print(f"  {ticker}: FAILED")


# ─── Fetch ownership data (with caching) ────────────────────────────────────

INDEXER_KEYWORDS = [
    'vanguard', 'blackrock', 'ishares', 'spdr', 'state street', 'schwab',
    'fidelity 500', 'total stock', 'total market', 'russell',
    's&p 500', 'index fund', 'etf trust', 'geode capital',
    'northern trust', 'bank of new york', 'legal & general',
]

def is_indexer(name):
    nl = name.lower()
    return any(kw in nl for kw in INDEXER_KEYWORDS)


def get_cache_path():
    today = datetime.now().strftime('%Y-%m-%d')
    return os.path.join(CACHE_DIR, f'ownership_{today}.yaml')


def load_cached_ownership():
    """Load most recent cached ownership data."""
    cache_file = get_cache_path()
    if os.path.exists(cache_file):
        return load_yaml(cache_file), cache_file
    # Try yesterday
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    alt_file = os.path.join(CACHE_DIR, f'ownership_{yesterday}.yaml')
    if os.path.exists(alt_file):
        return load_yaml(alt_file), alt_file
    return None, None


def save_ownership_cache(data):
    """Save ownership data snapshot."""
    cache_file = get_cache_path()
    with open(cache_file, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
    print(f"  Ownership snapshot saved: {cache_file}")
    return cache_file


def get_previous_snapshot():
    """Get the most recent snapshot BEFORE today."""
    today = datetime.now().strftime('%Y-%m-%d')
    files = sorted([f for f in os.listdir(CACHE_DIR) if f.startswith('ownership_') and f.endswith('.yaml')])
    for f in reversed(files):
        date_str = f.replace('ownership_', '').replace('.yaml', '')
        if date_str < today:
            return load_yaml(os.path.join(CACHE_DIR, f)), date_str
    return None, None


# Fetch or load ownership data
ownership_data = {}

if USE_CACHE:
    cached, cache_path = load_cached_ownership()
    if cached:
        ownership_data = cached
        print(f"\nUsing cached ownership data: {cache_path}")
    else:
        print("\nNo cache found, fetching fresh data...")
        USE_CACHE = False

if not USE_CACHE:
    print(f"\nFetching ownership data for {len(tickers)} positions...")
    for ticker in tickers:
        print(f"  {ticker}...", end=" ", flush=True)
        entry = {'holders': [], 'insiders': []}

        try:
            t = yf.Ticker(ticker)

            # Institutional holders
            try:
                inst = t.institutional_holders
                if inst is not None and isinstance(inst, pd.DataFrame) and not inst.empty:
                    holder_col = 'Holder' if 'Holder' in inst.columns else inst.columns[0]
                    for _, row in inst.head(10).iterrows():
                        name = str(row.get(holder_col, 'Unknown')).strip()
                        pct = row.get('% Out', row.get('pctHeld', 0))
                        if name and name != 'nan':
                            entry['holders'].append({
                                'name': name,
                                'pct': float(pct) if pct else 0,
                                'is_indexer': is_indexer(name),
                            })
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

                        if name and name != 'nan':
                            entry['insiders'].append({
                                'name': name,
                                'type': txn_type,
                                'shares': int(shares) if shares else 0,
                                'text': text[:60],
                            })
            except Exception:
                pass

            print(f"h:{len(entry['holders'])} i:{len(entry['insiders'])}")
        except Exception as e:
            print(f"ERR: {e}")

        ownership_data[ticker] = entry

    # Save snapshot
    save_ownership_cache(ownership_data)


# ─── Compute risk scores per position ───────────────────────────────────────

today = datetime.now()
position_risks = []

for pos in positions:
    ticker = pos['ticker']
    risk = {'ticker': ticker, 'name': pos.get('name', ticker)}

    # 1. QS Tier
    fv_str = str(pos.get('fair_value', ''))
    notes_str = str(pos.get('notes', ''))
    combined = fv_str + ' ' + notes_str
    qs, tier = extract_qs_tier(combined)

    # Get from system.yaml positions if not in notes
    if not tier:
        for sp in system.get('system', {}).get('portfolio_quality_analysis', {}).get('positions', []):
            if sp.get('ticker') == ticker:
                tier = sp.get('tier', '?')
                qs = sp.get('score', 0)
                break

    risk['qs'] = qs or 0
    risk['tier'] = tier or '?'
    risk['tier_score'] = {'A': 3, 'B': 2, 'C': 1, 'D': 0}.get(tier, 0)

    # 2. Margin of Safety (current price vs FV)
    fv_num = extract_number(fv_str)
    currency = get_currency(fv_str)
    price = prices.get(ticker)

    if fv_num and price:
        # Convert price to same currency as FV
        if currency == 'GBp':
            # yfinance returns GBp for .L stocks
            price_in_currency = price  # already in pence
        elif currency == 'EUR' and ticker.endswith(('.DE', '.PA', '.MI', '.AS', '.BR', '.MC', '.HE')):
            price_in_currency = price  # already in EUR
        else:
            price_in_currency = price  # USD

        mos = (fv_num - price_in_currency) / fv_num * 100
        risk['mos'] = round(mos, 1)
    else:
        risk['mos'] = 0

    # 3. Insider Sentiment
    own = ownership_data.get(ticker, {})
    insiders = own.get('insiders', [])
    buys = sum(1 for i in insiders if i.get('type') == 'BUY')
    sells = sum(1 for i in insiders if i.get('type') == 'SELL')
    buybacks = sum(1 for i in insiders if i.get('type') == 'BUYBACK')
    net_insider = buys - sells
    risk['insider_net'] = net_insider
    risk['insider_buys'] = buys
    risk['insider_sells'] = sells
    risk['insider_buybacks'] = buybacks
    if buys > 0 and net_insider > 0:
        risk['insider_signal'] = 'BULLISH'
        risk['insider_score'] = 3
    elif net_insider == 0 and buybacks > 0:
        risk['insider_signal'] = 'BB+'
        risk['insider_score'] = 2.5
    elif net_insider == 0 or not insiders:
        risk['insider_signal'] = 'NEUTRAL'
        risk['insider_score'] = 2
    elif net_insider >= -2:
        risk['insider_signal'] = 'CAUTIOUS'
        risk['insider_score'] = 1
    else:
        risk['insider_signal'] = 'BEARISH'
        risk['insider_score'] = 0

    # 4. Holder Concentration
    holders = own.get('holders', [])
    if holders:
        sorted_h = sorted(holders, key=lambda x: x.get('pct', 0), reverse=True)
        top3_pct = sum(h.get('pct', 0) for h in sorted_h[:3])
        if top3_pct < 1:
            top3_pct *= 100  # normalize to percentage
        n_indexer = sum(1 for h in holders if h.get('is_indexer'))
        indexer_pct = n_indexer / len(holders) * 100
        risk['top3_pct'] = round(top3_pct, 1)
        risk['indexer_pct'] = round(indexer_pct, 0)
        risk['n_holders'] = len(holders)
        if top3_pct > 30:
            risk['concentration_score'] = 0  # high risk
        elif top3_pct > 20:
            risk['concentration_score'] = 1
        else:
            risk['concentration_score'] = 3
    else:
        risk['top3_pct'] = 0
        risk['indexer_pct'] = 0
        risk['n_holders'] = 0
        risk['concentration_score'] = 2  # unknown = moderate

    # 5. Earnings Proximity
    days_to_earnings = 999
    next_event = ''
    for evt in events:
        if not isinstance(evt, dict):
            continue
        evt_ticker = evt.get('ticker', '')
        evt_date_str = str(evt.get('date', ''))
        if evt_ticker == ticker and ('earnings' in evt.get('type', '') or evt.get('type') == 'catalyst'):
            try:
                evt_date = datetime.strptime(evt_date_str, '%Y-%m-%d')
                days = (evt_date - today).days
                if 0 <= days < days_to_earnings:
                    days_to_earnings = days
                    next_event = evt.get('event', '')[:40]
            except (ValueError, TypeError):
                pass

    risk['days_to_earnings'] = days_to_earnings if days_to_earnings < 999 else None
    risk['next_event'] = next_event
    if days_to_earnings <= 3:
        risk['earnings_score'] = 0  # imminent
    elif days_to_earnings <= 7:
        risk['earnings_score'] = 1
    elif days_to_earnings <= 30:
        risk['earnings_score'] = 2
    else:
        risk['earnings_score'] = 3

    # 6. Conviction
    conviction = pos.get('conviction', 'low')
    risk['conviction'] = conviction
    risk['conviction_score'] = {'high': 3, 'medium': 2, 'low': 1}.get(conviction, 0)

    # 7. On Probation / Kill Conditions
    exit_plan = str(pos.get('exit_plan', ''))
    on_probation = 'PROBATION' in exit_plan.upper()
    make_or_break = 'MAKE-OR-BREAK' in exit_plan.upper()
    risk['on_probation'] = on_probation
    risk['make_or_break'] = make_or_break
    if make_or_break:
        risk['status_score'] = 0
    elif on_probation:
        risk['status_score'] = 1
    else:
        risk['status_score'] = 3

    # Composite risk (simple average of all scores, 0-3 scale)
    scores = [risk['tier_score'], risk.get('insider_score', 2), risk.get('concentration_score', 2),
              risk.get('earnings_score', 3), risk['conviction_score'], risk.get('status_score', 3)]
    risk['composite'] = round(sum(scores) / len(scores), 2)

    position_risks.append(risk)

# Sort by composite risk (lowest = highest risk first)
position_risks.sort(key=lambda x: x['composite'])


# ─── Temporal diff ──────────────────────────────────────────────────────────

diff_data = []
if SHOW_DIFF:
    prev_snapshot, prev_date = get_previous_snapshot()
    if prev_snapshot:
        print(f"\n  Comparing vs snapshot from {prev_date}...")
        for ticker in tickers:
            curr = ownership_data.get(ticker, {})
            prev = prev_snapshot.get(ticker, {})

            # Compare holders
            curr_holders = set(h['name'] for h in curr.get('holders', []))
            prev_holders = set(h.get('name', '') for h in prev.get('holders', []))
            new_holders = curr_holders - prev_holders
            lost_holders = prev_holders - curr_holders

            # Compare insider sentiment
            curr_ins = curr.get('insiders', [])
            prev_ins = prev.get('insiders', [])
            curr_buys = sum(1 for i in curr_ins if i.get('type') == 'BUY')
            curr_sells = sum(1 for i in curr_ins if i.get('type') == 'SELL')
            prev_buys = sum(1 for i in prev_ins if i.get('type') == 'BUY')
            prev_sells = sum(1 for i in prev_ins if i.get('type') == 'SELL')

            if new_holders or lost_holders or (curr_buys - curr_sells) != (prev_buys - prev_sells):
                diff_data.append({
                    'ticker': ticker,
                    'new_holders': list(new_holders),
                    'lost_holders': list(lost_holders),
                    'insider_change': (curr_buys - curr_sells) - (prev_buys - prev_sells),
                })
    else:
        print("  No previous snapshot found for diff.")

# ─── Generate HTML ──────────────────────────────────────────────────────────

print(f"\nGenerating risk heatmap for {len(position_risks)} positions...")

# Prepare JSON data
heatmap_data = json.dumps(position_risks, indent=2)
diff_json = json.dumps(diff_data, indent=2) if diff_data else '[]'

html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Risk Heatmap — Value Investor System</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { background: #1a1a2e; color: #e0e0e0; font-family: 'Segoe UI', system-ui, sans-serif; padding: 20px; }

  h1 { font-size: 20px; color: #fff; margin-bottom: 4px; }
  .subtitle { font-size: 12px; color: #888; margin-bottom: 16px; }

  .heatmap-container { overflow-x: auto; }

  table { border-collapse: collapse; width: 100%; min-width: 900px; }
  th { background: #252545; color: #aaa; font-size: 11px; font-weight: 600; text-transform: uppercase;
       letter-spacing: 0.5px; padding: 10px 8px; cursor: pointer; user-select: none;
       border-bottom: 2px solid #333; position: relative; white-space: nowrap; }
  th:hover { color: #fff; }
  th .sort-arrow { font-size: 9px; margin-left: 4px; color: #666; }
  th.sorted .sort-arrow { color: #6ca0dc; }

  td { padding: 8px; text-align: center; font-size: 13px; border-bottom: 1px solid #2a2a4a;
       transition: all 0.15s ease; }
  tr:hover td { background: rgba(100, 160, 220, 0.08); }

  td.ticker { text-align: left; font-weight: 600; color: #fff; min-width: 80px; }
  td.name { text-align: left; color: #aaa; font-size: 11px; max-width: 160px; overflow: hidden;
            text-overflow: ellipsis; white-space: nowrap; }

  /* Risk cell colors */
  .risk-0 { background: rgba(220, 50, 50, 0.25); color: #f06060; }
  .risk-1 { background: rgba(220, 140, 50, 0.2); color: #e0a050; }
  .risk-2 { background: rgba(160, 160, 80, 0.15); color: #c0c060; }
  .risk-3 { background: rgba(50, 180, 80, 0.2); color: #50c060; }

  .badge { display: inline-block; padding: 2px 8px; border-radius: 3px; font-size: 10px;
           font-weight: 600; letter-spacing: 0.3px; }
  .badge-a { background: rgba(50, 180, 80, 0.25); color: #50c060; }
  .badge-b { background: rgba(160, 160, 80, 0.2); color: #c0c060; }
  .badge-c { background: rgba(220, 50, 50, 0.25); color: #f06060; }
  .badge-probation { background: rgba(220, 140, 50, 0.3); color: #e0a050; }
  .badge-mob { background: rgba(220, 50, 50, 0.35); color: #ff6060; }

  .composite-bar { display: inline-block; height: 8px; border-radius: 4px; min-width: 20px; }

  /* Summary cards */
  .summary { display: flex; gap: 12px; margin-bottom: 16px; flex-wrap: wrap; }
  .card { background: rgba(30, 30, 60, 0.8); border: 1px solid #333; border-radius: 8px;
          padding: 12px 16px; flex: 1; min-width: 140px; }
  .card-label { font-size: 10px; color: #888; text-transform: uppercase; letter-spacing: 0.5px; }
  .card-value { font-size: 22px; font-weight: 700; color: #fff; margin-top: 2px; }
  .card-detail { font-size: 11px; color: #aaa; margin-top: 2px; }

  .footer { margin-top: 16px; font-size: 10px; color: #555; }

  /* Diff section */
  .diff-section { margin-top: 20px; }
  .diff-item { background: rgba(30, 30, 60, 0.6); border: 1px solid #333; border-radius: 6px;
               padding: 10px 14px; margin-bottom: 8px; font-size: 12px; }
  .diff-ticker { font-weight: 600; color: #6ca0dc; }
  .diff-change-pos { color: #50c060; }
  .diff-change-neg { color: #f06060; }
</style>
</head>
<body>

<h1>Risk Heatmap</h1>
<p class="subtitle">Multi-dimensional risk dashboard | Generated """ + datetime.now().strftime('%Y-%m-%d %H:%M') + """</p>

<div class="summary" id="summary"></div>

<div class="heatmap-container">
<table id="heatmap">
  <thead>
    <tr>
      <th data-col="ticker">Ticker <span class="sort-arrow">▼</span></th>
      <th data-col="name">Name <span class="sort-arrow">▼</span></th>
      <th data-col="tier_score" title="Quality Score Tier (A=best, C=worst)">QS Tier <span class="sort-arrow">▼</span></th>
      <th data-col="mos" title="Margin of Safety (price vs fair value)">MoS% <span class="sort-arrow">▼</span></th>
      <th data-col="insider_score" title="Net insider buy/sell sentiment">Insider <span class="sort-arrow">▼</span></th>
      <th data-col="concentration_score" title="Top 3 holder concentration">Holders <span class="sort-arrow">▼</span></th>
      <th data-col="earnings_score" title="Days until next earnings/catalyst">Earnings <span class="sort-arrow">▼</span></th>
      <th data-col="conviction_score" title="Current conviction level">Convict. <span class="sort-arrow">▼</span></th>
      <th data-col="status_score" title="Position status (probation/make-or-break)">Status <span class="sort-arrow">▼</span></th>
      <th data-col="composite" title="Composite risk score (higher = lower risk)">Risk <span class="sort-arrow">▼</span></th>
    </tr>
  </thead>
  <tbody id="tbody"></tbody>
</table>
</div>

<div class="diff-section" id="diff-section"></div>

<div class="footer">
  Colors: <span style="color:#50c060">■ Low risk</span> &middot;
  <span style="color:#c0c060">■ Moderate</span> &middot;
  <span style="color:#e0a050">■ Elevated</span> &middot;
  <span style="color:#f06060">■ High risk</span>
  &middot; Click column headers to sort. Data is RAW — interpret with context.
</div>

<script>
const DATA = """ + heatmap_data + """;
const DIFF = """ + diff_json + """;

// Risk class mapping (0=high risk red, 3=low risk green)
function riskClass(score) {
  if (score === null || score === undefined) return 'risk-2';
  score = Math.round(score);
  return 'risk-' + Math.max(0, Math.min(3, score));
}

function mosClass(mos) {
  if (mos > 20) return 'risk-3';
  if (mos > 10) return 'risk-2';
  if (mos > 0) return 'risk-1';
  return 'risk-0';
}

function mosRiskScore(mos) {
  if (mos > 20) return 3;
  if (mos > 10) return 2;
  if (mos > 0) return 1;
  return 0;
}

// Summary cards
function renderSummary() {
  const n = DATA.length;
  const bearish = DATA.filter(d => d.insider_score <= 1).length;
  const imminent = DATA.filter(d => d.days_to_earnings !== null && d.days_to_earnings <= 7).length;
  const probation = DATA.filter(d => d.on_probation).length;
  const avgComposite = (DATA.reduce((s, d) => s + d.composite, 0) / n).toFixed(1);

  const riskLabel = avgComposite >= 2.5 ? 'LOW' : avgComposite >= 1.8 ? 'MODERATE' : 'ELEVATED';
  const riskColor = avgComposite >= 2.5 ? '#50c060' : avgComposite >= 1.8 ? '#c0c060' : '#f06060';

  document.getElementById('summary').innerHTML = `
    <div class="card">
      <div class="card-label">Positions</div>
      <div class="card-value">${n}</div>
      <div class="card-detail">${probation} on probation</div>
    </div>
    <div class="card">
      <div class="card-label">Avg Risk Score</div>
      <div class="card-value" style="color:${riskColor}">${avgComposite}/3.0</div>
      <div class="card-detail">${riskLabel}</div>
    </div>
    <div class="card">
      <div class="card-label">Insider Alerts</div>
      <div class="card-value" style="color:${bearish > 0 ? '#f06060' : '#50c060'}">${bearish}</div>
      <div class="card-detail">${bearish} bearish sentiment</div>
    </div>
    <div class="card">
      <div class="card-label">Earnings <7d</div>
      <div class="card-value" style="color:${imminent > 0 ? '#e0a050' : '#50c060'}">${imminent}</div>
      <div class="card-detail">imminent events</div>
    </div>
  `;
}

// Render table
let sortCol = 'composite';
let sortAsc = true;

function renderTable() {
  const sorted = [...DATA].sort((a, b) => {
    let va = a[sortCol], vb = b[sortCol];
    if (typeof va === 'string') return sortAsc ? va.localeCompare(vb) : vb.localeCompare(va);
    va = va ?? -999; vb = vb ?? -999;
    return sortAsc ? va - vb : vb - va;
  });

  const tbody = document.getElementById('tbody');
  tbody.innerHTML = sorted.map(d => {
    const tierBadge = d.tier === 'A' ? 'badge-a' : d.tier === 'C' ? 'badge-c' : 'badge-b';
    const statusBadge = d.make_or_break ? 'badge-mob' : d.on_probation ? 'badge-probation' : '';
    const statusText = d.make_or_break ? 'M-O-B' : d.on_probation ? 'PROBATION' : 'OK';

    const daysText = d.days_to_earnings !== null ? d.days_to_earnings + 'd' : '>30d';
    const insiderText = d.insider_signal + (d.insider_net !== 0 ? ' (' + (d.insider_net > 0 ? '+' : '') + d.insider_net + ')' : '');
    const holdersText = d.n_holders > 0 ? d.top3_pct + '% / ' + d.indexer_pct + '%idx' : 'N/A';

    // Composite bar width (0-3 mapped to 0-100%)
    const barWidth = Math.round(d.composite / 3 * 100);
    const barColor = d.composite >= 2.5 ? '#50c060' : d.composite >= 1.8 ? '#c0c060' : d.composite >= 1.2 ? '#e0a050' : '#f06060';

    return `<tr>
      <td class="ticker">${d.ticker}</td>
      <td class="name" title="${d.name}">${d.name}</td>
      <td class="${riskClass(d.tier_score)}"><span class="badge ${tierBadge}">${d.tier} (${d.qs})</span></td>
      <td class="${mosClass(d.mos)}">${d.mos > 0 ? '+' : ''}${d.mos}%</td>
      <td class="${riskClass(d.insider_score)}">${insiderText}</td>
      <td class="${riskClass(d.concentration_score)}">${holdersText}</td>
      <td class="${riskClass(d.earnings_score)}" title="${d.next_event}">${daysText}</td>
      <td class="${riskClass(d.conviction_score)}">${d.conviction}</td>
      <td class="${riskClass(d.status_score)}"><span class="badge ${statusBadge}">${statusText}</span></td>
      <td><span class="composite-bar" style="width:${barWidth}px;background:${barColor}"></span> ${d.composite}</td>
    </tr>`;
  }).join('');

  // Update sort indicators
  document.querySelectorAll('th').forEach(th => {
    th.classList.toggle('sorted', th.dataset.col === sortCol);
    const arrow = th.querySelector('.sort-arrow');
    if (arrow) arrow.textContent = th.dataset.col === sortCol ? (sortAsc ? '▲' : '▼') : '▼';
  });
}

// Diff section
function renderDiff() {
  if (!DIFF.length) return;
  const section = document.getElementById('diff-section');
  section.innerHTML = '<h3 style="color:#fff;margin-bottom:8px">Ownership Changes</h3>' +
    DIFF.map(d => {
      let changes = [];
      if (d.new_holders.length) changes.push(`<span class="diff-change-pos">+${d.new_holders.length} new holders: ${d.new_holders.join(', ')}</span>`);
      if (d.lost_holders.length) changes.push(`<span class="diff-change-neg">-${d.lost_holders.length} lost holders: ${d.lost_holders.join(', ')}</span>`);
      if (d.insider_change > 0) changes.push(`<span class="diff-change-pos">Insider sentiment improved (+${d.insider_change})</span>`);
      if (d.insider_change < 0) changes.push(`<span class="diff-change-neg">Insider sentiment worsened (${d.insider_change})</span>`);
      return `<div class="diff-item"><span class="diff-ticker">${d.ticker}</span> — ${changes.join(' | ')}</div>`;
    }).join('');
}

// Sort handler
document.querySelectorAll('th').forEach(th => {
  th.addEventListener('click', () => {
    const col = th.dataset.col;
    if (col === sortCol) sortAsc = !sortAsc;
    else { sortCol = col; sortAsc = true; }
    renderTable();
  });
});

renderSummary();
renderTable();
renderDiff();
</script>
</body>
</html>"""

with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\nRisk heatmap saved: {OUTPUT}")

# Print console summary
print("\n── RISK SUMMARY ──────────────────────────────────────────────────")
print(f"{'Ticker':<10} {'Tier':>4} {'MoS%':>6} {'Insider':>10} {'Holders':>10} {'Earn':>5} {'Conv':>6} {'Status':>10} {'Risk':>5}")
print("-" * 75)
for r in position_risks:
    earn_str = f"{r['days_to_earnings']}d" if r['days_to_earnings'] is not None else '>30d'
    status = 'M-O-B' if r['make_or_break'] else 'PROBATION' if r['on_probation'] else 'OK'
    print(f"{r['ticker']:<10} {r['tier']:>4} {r['mos']:>+5.1f}% {r['insider_signal']:>10} {r['top3_pct']:>5.1f}%top3 {earn_str:>5} {r['conviction']:>6} {status:>10} {r['composite']:>5.2f}")

print(f"\nAvg composite: {sum(r['composite'] for r in position_risks) / len(position_risks):.2f}/3.00")
print("Open docs/risk_heatmap.html in browser for interactive view.")
