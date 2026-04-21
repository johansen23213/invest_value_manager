#!/usr/bin/env python3
"""
Command Center v2.2 — Unified session-start dashboard in a single interactive HTML page.

Panels:
  0. Alert Banner (thesis alerts: below-bear, KC approaching, thin MoS, probation, phase transition)
  1. KPI Row (NAV, Cash, Long, P&L, E[CAGR], vs SPY, Last Deploy, Cash Drag, Earnings)
  2. Position Risk Matrix (sortable, with E[CAGR] column + sparklines + enhanced insider signals)
  3. Earnings Week (next 7d earnings with framework status + phase transition warning)
  4. Forward Returns chart (E[CAGR] bars per position)
  5. Exposure Breakdown (geographic donut, sector donut, cash gauge + deployment monitor)
  6. Calendar Timeline (next 21 days)
  7. Standing Order Proximity (nearest triggers)
  8. Pipeline Funnel
  9. Smart Money (quality funds)

Uses shared ownership_cache for institutional data.
Uses yfinance for live prices, sparklines, and benchmark data.

Usage:
    python3 tools/command_center.py             # Full dashboard
    python3 tools/command_center.py --fresh      # Force-refresh ownership data

Output: docs/command_center.html
"""

import os
import sys
import json
import yaml
import re
import glob as globmod
import warnings
from datetime import datetime, timedelta
from collections import Counter

warnings.filterwarnings('ignore')

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT = os.path.join(BASE, 'docs', 'command_center.html')

sys.path.insert(0, os.path.join(BASE, 'tools'))
from ownership_cache import load_or_fetch, get_quality_funds, get_insider_sentiment
from forward_return import extract_growth_rate, read_thesis_file

FORCE_FRESH = '--fresh' in sys.argv

# ─── Load YAML ───────────────────────────────────────────────────────────────

def load_yaml(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f) or {}
    except Exception:
        return {}

portfolio = load_yaml(os.path.join(BASE, 'portfolio', 'current.yaml'))
calendar_data = load_yaml(os.path.join(BASE, 'state', 'calendar.yaml'))
system = load_yaml(os.path.join(BASE, 'state', 'system.yaml'))
so_data = load_yaml(os.path.join(BASE, 'state', 'standing_orders.yaml'))
pipeline = load_yaml(os.path.join(BASE, 'state', 'pipeline_tracker.yaml'))
universe = load_yaml(os.path.join(BASE, 'state', 'quality_universe.yaml'))
history = load_yaml(os.path.join(BASE, 'portfolio', 'history.yaml'))

positions = portfolio.get('positions', [])
events = calendar_data.get('events', []) or []
standing_orders = so_data.get('standing_orders', []) or []
companies = universe.get('quality_universe', {}).get('companies', [])
cash_eur = portfolio.get('cash', {}).get('amount', 0)

tickers = [p['ticker'] for p in positions]

# ─── Sector / Geography mappings ─────────────────────────────────────────────

SECTOR_MAP = {}
# Try to derive from quality_universe first, then fallback to file-structure
for c in companies:
    if c.get('sector'):
        SECTOR_MAP[c['ticker']] = c['sector']

# Fallback from file-structure knowledge (sector view assignments)
SECTOR_FALLBACK = {
    'DTE.DE': 'Telecom', 'EDEN.PA': 'Business Services',
    'DOM.L': 'Consumer Staples', 'GL': 'Insurance',
    'ADBE': 'Technology', 'NVO': 'Pharma/Healthcare',
    'MONY.L': 'Digital Marketplaces', 'LULU': 'Consumer Discretionary',
    'AUTO.L': 'Digital Marketplaces', 'MORN': 'Financial Data',
    'BYIT.L': 'Technology',
}
for t, s in SECTOR_FALLBACK.items():
    if t not in SECTOR_MAP:
        SECTOR_MAP[t] = s

def get_geography(ticker):
    suffix_map = {
        '.DE': 'Germany', '.PA': 'France', '.MI': 'Italy', '.L': 'UK',
        '.AS': 'Netherlands', '.BR': 'Belgium', '.MC': 'Spain',
        '.HE': 'Finland', '.SW': 'Switzerland', '.CO': 'Denmark',
    }
    for suffix, country in suffix_map.items():
        if ticker.endswith(suffix):
            return country
    return 'US'

# ─── Helpers ─────────────────────────────────────────────────────────────────

def extract_number(s):
    if not s: return None
    s = str(s)
    for p in ['$', 'EUR ', 'GBp ', 'USD ', '£', 'CHF ', '<=']:
        s = s.replace(p, '')
    m = re.search(r'[\d.]+', s)
    return float(m.group()) if m else None

def get_currency(s):
    if not s: return 'USD'
    s = str(s)
    if 'EUR' in s: return 'EUR'
    if 'GBp' in s or 'GBP' in s: return 'GBp'
    if 'CHF' in s: return 'CHF'
    return 'USD'

# ─── Fetch prices + FX + sparklines + benchmarks ─────────────────────────────

import yfinance as yf

print("=" * 60)
print("COMMAND CENTER v2.1 — Building session dashboard")
print("=" * 60)

print("\nFetching FX rates...", flush=True)
fx = {}
try:
    for pair in ['EURUSD=X', 'GBPUSD=X', 'CHFUSD=X']:
        t = yf.Ticker(pair)
        h = t.history(period='1d')
        if not h.empty:
            fx[pair] = h['Close'].iloc[-1]
except Exception:
    pass

eur_usd = fx.get('EURUSD=X', 1.05)
gbp_usd = fx.get('GBPUSD=X', 1.27)
chf_usd = fx.get('CHFUSD=X', 1.10)

# Fetch 30d history for all positions (sparklines + current price)
print("Fetching 30d prices for sparklines...", flush=True)
prices = {}
sparklines = {}
for ticker in tickers:
    try:
        t = yf.Ticker(ticker)
        h = t.history(period='1mo')
        if not h.empty:
            prices[ticker] = h['Close'].iloc[-1]
            # Normalize sparkline to list of floats
            closes = h['Close'].tolist()
            sparklines[ticker] = [round(c, 2) for c in closes[-30:]]
    except Exception:
        pass

print(f"  {len(prices)}/{len(tickers)} prices fetched")

# Extract growth from thesis files (same source as forward_return.py)
print("Extracting growth from thesis files...", flush=True)
thesis_growth = {}
for pos in positions:
    ticker = pos['ticker']
    thesis_path = pos.get('thesis', '')
    if thesis_path:
        content = read_thesis_file(thesis_path)
        if content:
            growth = extract_growth_rate(content, ticker)
            if growth is not None:
                thesis_growth[ticker] = growth  # decimal, e.g. 0.08

# Fetch dividend yields from yfinance
print("Fetching dividend yields...", flush=True)
div_yields = {}
for ticker in tickers:
    try:
        t = yf.Ticker(ticker)
        dy = t.info.get('dividendYield')
        if dy and isinstance(dy, (int, float)) and dy > 0:
            div_yields[ticker] = dy / 100  # yfinance returns as pct like 2.75 for 2.75%
    except Exception:
        pass

# Fallback: yfinance earnings growth only for tickers without thesis growth, and only if positive
for ticker in tickers:
    if ticker not in thesis_growth:
        try:
            eg = yf.Ticker(ticker).info.get('earningsGrowth')
            if eg and isinstance(eg, (int, float)) and eg > 0:  # Only use positive values
                thesis_growth[ticker] = eg
        except Exception:
            pass

# Fetch benchmarks (SPY and STOXX600 ETF)
print("Fetching benchmarks (SPY, STOXX600)...", flush=True)
# Find earliest position date for benchmark period
earliest_date = None
for pos in positions:
    try:
        d = datetime.strptime(str(pos.get('date_opened', '')), '%Y-%m-%d')
        if earliest_date is None or d < earliest_date:
            earliest_date = d
    except (ValueError, TypeError):
        pass

benchmark_returns = {}
if earliest_date:
    for bench_ticker, bench_name in [('SPY', 'S&P 500'), ('^STOXX', 'STOXX 600')]:
        try:
            t = yf.Ticker(bench_ticker)
            h = t.history(start=earliest_date.strftime('%Y-%m-%d'))
            if not h.empty and len(h) >= 2:
                benchmark_returns[bench_name] = (h['Close'].iloc[-1] / h['Close'].iloc[0] - 1) * 100
        except Exception:
            pass

print(f"  Benchmarks: {list(benchmark_returns.keys())}")

# ─── Cash Deployment Monitor ─────────────────────────────────────────────────

print("Computing deployment metrics...", flush=True)
today = datetime.now()

# Find most recent deployment date from current positions (date_opened)
last_deploy_date = None
last_deploy_ticker = '?'
for pos in positions:
    try:
        d = datetime.strptime(str(pos.get('date_opened', '')), '%Y-%m-%d')
        if last_deploy_date is None or d > last_deploy_date:
            last_deploy_date = d
            last_deploy_ticker = pos['ticker']
    except (ValueError, TypeError):
        pass

# Also check closed positions entry_date (in case we bought and sold more recently)
closed_positions = history.get('closed_positions', []) or []
for cp in closed_positions:
    try:
        d = datetime.strptime(str(cp.get('entry_date', '')), '%Y-%m-%d')
        if last_deploy_date is None or d > last_deploy_date:
            last_deploy_date = d
            last_deploy_ticker = cp.get('ticker', '?')
    except (ValueError, TypeError):
        pass

days_since_deploy = (today - last_deploy_date).days if last_deploy_date else 999

# SPY YTD return for cash drag YTD calculation
spy_ytd_return = 0.0
try:
    jan1 = datetime(today.year, 1, 1).strftime('%Y-%m-%d')
    spy_h = yf.Ticker('SPY').history(start=jan1)
    if not spy_h.empty and len(spy_h) >= 2:
        spy_ytd_return = (spy_h['Close'].iloc[-1] / spy_h['Close'].iloc[0] - 1) * 100
except Exception:
    pass

# Cash drag YTD: what we lost this year by holding cash instead of SPY
# (cash_pct will be computed after NAV, so we compute this later)

print(f"  Last deploy: {last_deploy_ticker} ({days_since_deploy}d ago) | SPY YTD: {spy_ytd_return:+.1f}%")

# ─── Ownership data (cached) ────────────────────────────────────────────────

print("Loading ownership data...")
ownership_data = load_or_fetch(tickers, force_fresh=FORCE_FRESH)

# Enhanced insider signal computation (3-tier: STRONG/BULLISH/BEARISH)
# Import from r1_prioritizer for consistent signal classification
try:
    from r1_prioritizer import compute_enhanced_insider_signal
    _HAS_ENHANCED_INSIDER = True
except ImportError:
    _HAS_ENHANCED_INSIDER = False

# ─── Compute portfolio KPIs ──────────────────────────────────────────────────

total_invested_eur = 0
total_value_eur = 0
position_data = []

for pos in positions:
    ticker = pos['ticker']
    price = prices.get(ticker)
    invested_usd = pos.get('invested_usd', 0)
    shares = pos.get('shares', 0)
    fv_str = str(pos.get('fair_value', ''))
    fv_num = extract_number(fv_str)
    currency = get_currency(fv_str)

    # Current value in EUR
    if price:
        if ticker.endswith(('.DE', '.PA', '.MI', '.AS', '.BR', '.MC', '.HE')):
            value_eur = price * shares
        elif ticker.endswith('.L'):
            value_eur = price * shares * gbp_usd / 100 / eur_usd  # GBp to EUR
        elif ticker.endswith('.SW'):
            value_eur = price * shares * chf_usd / eur_usd
        else:
            value_eur = price * shares / eur_usd  # USD to EUR
    else:
        value_eur = invested_usd / eur_usd

    invested_eur = invested_usd / eur_usd
    total_invested_eur += invested_eur
    total_value_eur += value_eur

    # MoS
    mos = 0
    if fv_num and price:
        mos = (fv_num - price) / fv_num * 100

    # E[CAGR] = (FV/Price)^(1/3) - 1 + Growth + DivYield
    ecagr = None
    if fv_num and price and price > 0:
        mos_cagr = (fv_num / price) ** (1/3) - 1
        growth = thesis_growth.get(ticker, 0)
        div_y = div_yields.get(ticker, 0)
        ecagr = round((mos_cagr + growth + div_y) * 100, 1)

    # QS/Tier from system.yaml
    tier = '?'
    qs = 0
    for sp in system.get('system', {}).get('portfolio_quality_analysis', {}).get('positions', []):
        if sp.get('ticker') == ticker:
            tier = sp.get('tier', '?')
            qs = sp.get('score', 0)
            break

    # Insider sentiment (enhanced 3-tier if available)
    buys, sells, buybacks, options, net, signal = get_insider_sentiment(ownership_data, ticker)
    ins_strong_count = 0
    ins_strong_value = 0
    ins_cluster = 0
    if _HAS_ENHANCED_INSIDER and ticker in ownership_data:
        insiders_raw = ownership_data[ticker].get('insiders', [])
        enhanced = compute_enhanced_insider_signal(insiders_raw)
        signal = enhanced.get('ins_signal', signal)  # Override with enhanced signal
        net = enhanced.get('ins_net', net)
        ins_strong_count = enhanced.get('strong_count', 0)
        ins_strong_value = enhanced.get('strong_total_value', 0)
        ins_cluster = enhanced.get('cluster_size', 0)

    # Earnings proximity
    days_to_earnings = None
    next_event = ''
    for evt in events:
        if not isinstance(evt, dict): continue
        if evt.get('ticker') == ticker and 'earnings' in str(evt.get('type', '')).lower():
            try:
                d = datetime.strptime(str(evt.get('date', '')), '%Y-%m-%d')
                days = (d - today).days
                if days >= 0 and (days_to_earnings is None or days < days_to_earnings):
                    days_to_earnings = days
                    next_event = evt.get('event', '')[:50]
            except (ValueError, TypeError):
                pass

    # Status flags
    exit_plan = str(pos.get('exit_plan', ''))
    on_probation = 'PROBATION' in exit_plan.upper()
    make_or_break = 'MAKE-OR-BREAK' in exit_plan.upper()

    pnl_pct = (value_eur - invested_eur) / invested_eur * 100 if invested_eur > 0 else 0

    position_data.append({
        'ticker': ticker,
        'name': pos.get('name', ticker),
        'value_eur': round(value_eur, 0),
        'invested_eur': round(invested_eur, 0),
        'pnl_pct': round(pnl_pct, 1),
        'mos': round(mos, 1),
        'ecagr': ecagr,
        'tier': tier,
        'qs': qs,
        'conviction': pos.get('conviction', 'low'),
        'insider_signal': signal,
        'insider_net': net,
        'ins_strong_count': ins_strong_count,
        'ins_strong_value': round(ins_strong_value, 0),
        'ins_cluster': ins_cluster,
        'days_to_earnings': days_to_earnings,
        'next_event': next_event,
        'on_probation': on_probation,
        'make_or_break': make_or_break,
        'weight_pct': 0,
        'sparkline': sparklines.get(ticker, []),
        'sector': SECTOR_MAP.get(ticker, 'Other'),
        'geography': get_geography(ticker),
    })

nav_eur = total_value_eur + cash_eur
cash_pct = cash_eur / nav_eur * 100 if nav_eur > 0 else 0
long_pct = total_value_eur / nav_eur * 100 if nav_eur > 0 else 0

for pd_ in position_data:
    pd_['weight_pct'] = round(pd_['value_eur'] / nav_eur * 100, 1) if nav_eur > 0 else 0

# ─── Alerts ──────────────────────────────────────────────────────────────────

alerts = []
for p in position_data:
    ticker = p['ticker']
    # Overvalued (negative MoS)
    if p['mos'] < 0:
        alerts.append({'level': 'critical', 'msg': f"{ticker}: OVERVALUED (MoS {p['mos']:+.1f}%)"})
    elif p['mos'] < 10:
        alerts.append({'level': 'warning', 'msg': f"{ticker}: Thin MoS ({p['mos']:+.1f}%)"})
    # Probation / Make-or-break
    if p['make_or_break']:
        alerts.append({'level': 'critical', 'msg': f"{ticker}: MAKE-OR-BREAK upcoming"})
    elif p['on_probation']:
        alerts.append({'level': 'warning', 'msg': f"{ticker}: On PROBATION, {p['conviction']} conviction"})
    # Bearish insiders
    if p['insider_signal'] == 'BEARISH':
        alerts.append({'level': 'warning', 'msg': f"{ticker}: BEARISH insider signal (net {p['insider_net']})"})
    # Imminent earnings
    if p['days_to_earnings'] is not None and p['days_to_earnings'] <= 1:
        alerts.append({'level': 'critical', 'msg': f"{ticker}: Earnings {'TODAY' if p['days_to_earnings'] == 0 else 'TOMORROW'}"})
    # Low E[CAGR]
    if p['ecagr'] is not None and p['ecagr'] < 5:
        alerts.append({'level': 'warning', 'msg': f"{ticker}: Low E[CAGR] {p['ecagr']:.1f}% — rotation candidate"})

# ─── E[CAGR] portfolio average ───────────────────────────────────────────────

ecagr_values = [p['ecagr'] for p in position_data if p['ecagr'] is not None]
ecagr_weights = [p['value_eur'] for p in position_data if p['ecagr'] is not None]
portfolio_ecagr = sum(e * w for e, w in zip(ecagr_values, ecagr_weights)) / sum(ecagr_weights) if ecagr_weights else 0

# Cash drag: opportunity cost of cash at portfolio E[CAGR]
cash_drag_pct = cash_pct / 100 * portfolio_ecagr if portfolio_ecagr > 0 else 0

# Cash drag YTD: actual opportunity cost realized this year (cash % x SPY YTD return)
cash_drag_ytd = cash_pct / 100 * spy_ytd_return if spy_ytd_return > 0 else 0

# ─── Geographic + Sector exposure ────────────────────────────────────────────

geo_exposure = {}
sector_exposure = {}
for p in position_data:
    geo = p['geography']
    sec = p['sector']
    geo_exposure[geo] = geo_exposure.get(geo, 0) + p['value_eur']
    sector_exposure[sec] = sector_exposure.get(sec, 0) + p['value_eur']

# Add cash as "Cash" in geo/sector
geo_exposure['Cash'] = cash_eur
sector_exposure['Cash'] = cash_eur

# Convert to percentages
total_nav = nav_eur or 1
geo_pcts = {k: round(v / total_nav * 100, 1) for k, v in sorted(geo_exposure.items(), key=lambda x: -x[1])}
sector_pcts = {k: round(v / total_nav * 100, 1) for k, v in sorted(sector_exposure.items(), key=lambda x: -x[1])}

# ─── Earnings Week (next 7 days) ────────────────────────────────────────────

earnings_week = []
# Check for existing frameworks
framework_files = set()
for fp in globmod.glob(os.path.join(BASE, 'thesis', '**', 'earnings_framework*.md'), recursive=True):
    # Extract ticker from path
    parts = fp.split(os.sep)
    for i, part in enumerate(parts):
        if part in ('active', 'research', 'short'):
            if i + 1 < len(parts):
                framework_files.add(parts[i + 1])
            break

for evt in events:
    if not isinstance(evt, dict): continue
    evt_type = str(evt.get('type', '')).lower()
    if 'earnings' not in evt_type: continue
    try:
        d = datetime.strptime(str(evt.get('date', '')), '%Y-%m-%d')
        days_away = (d - today).days
        if 0 <= days_away <= 7:
            ticker = evt.get('ticker', '')
            has_framework = ticker in framework_files
            # Check if it's an active position
            is_position = ticker in tickers
            earnings_week.append({
                'date': str(evt.get('date', '')),
                'days_away': days_away,
                'ticker': ticker,
                'event': evt.get('event', '')[:60],
                'action': evt.get('action', '')[:100],
                'has_framework': has_framework,
                'is_position': is_position,
                'priority': evt.get('priority', 'medium'),
            })
    except (ValueError, TypeError):
        pass

earnings_week.sort(key=lambda x: x['days_away'])

# ─── Phase Transition Detection ──────────────────────────────────────────
# When >=3 portfolio stocks report same week, system enters "phase transition"
# mode where Psychology (F) is amplified and pre-committed frameworks are critical.

portfolio_earnings_count = sum(1 for e in earnings_week if e['is_position'])
pipeline_earnings_count = sum(1 for e in earnings_week if not e['is_position'])
is_phase_transition = portfolio_earnings_count >= 3 or (portfolio_earnings_count >= 2 and pipeline_earnings_count >= 3)
missing_frameworks = [e['ticker'] for e in earnings_week if not e['has_framework']]

if is_phase_transition:
    alerts.append({
        'level': 'critical',
        'msg': f"PHASE TRANSITION WEEK: {portfolio_earnings_count} positions + {pipeline_earnings_count} pipeline reporting. Pre-commit all decisions. F (Psychology) amplified."
    })
    if missing_frameworks:
        alerts.append({
            'level': 'critical',
            'msg': f"MISSING FRAMEWORKS: {', '.join(missing_frameworks)} — create BEFORE earnings"
        })

# ─── Calendar data ───────────────────────────────────────────────────────────

cal_items = []
for evt in events:
    if not isinstance(evt, dict): continue
    try:
        d = datetime.strptime(str(evt.get('date', '')), '%Y-%m-%d')
        days_away = (d - today).days
        if -1 <= days_away <= 21:
            urgency = 'critical' if days_away <= 1 else 'high' if days_away <= 3 else 'medium' if days_away <= 7 else 'low'
            priority = evt.get('priority', 'medium')
            if priority == 'CRITICAL':
                urgency = 'critical'
            cal_items.append({
                'date': str(evt.get('date', '')),
                'days_away': days_away,
                'ticker': evt.get('ticker', ''),
                'event': evt.get('event', '')[:60],
                'type': evt.get('type', ''),
                'urgency': urgency,
                'action': evt.get('action', '')[:80],
            })
    except (ValueError, TypeError):
        pass

cal_items.sort(key=lambda x: x['days_away'])

# ─── Standing orders proximity ───────────────────────────────────────────────

so_items = []
for so in standing_orders:
    ticker = so.get('ticker', '')
    trigger = extract_number(so.get('trigger', ''))
    category = so.get('category', 'GATED')
    action = so.get('action', 'BUY')
    dist_str = so.get('current_distance', '')
    dist = extract_number(dist_str)

    so_items.append({
        'ticker': ticker,
        'action': action,
        'category': category,
        'trigger': so.get('trigger', ''),
        'distance': dist or 50,
        'size_eur': so.get('size_eur', 0),
        'tier': so.get('tier', '?'),
        'gate': so.get('gate', ''),
        'fill_prob': so.get('fill_prob_6m', 0),
    })

so_items.sort(key=lambda x: x['distance'])
so_items = so_items[:15]

# ─── Pipeline funnel ─────────────────────────────────────────────────────────

pipeline_counts = Counter()
for c in companies:
    status = c.get('pipeline_status', 'SCORED')
    pipeline_counts[status] += 1

funnel = {
    'scored': pipeline_counts.get('SCORED', 0),
    'r1_complete': pipeline_counts.get('R1_COMPLETE', 0),
    'r3_complete': pipeline_counts.get('R3_COMPLETE', 0),
    'approved': pipeline_counts.get('APPROVED', 0) + pipeline_counts.get('R4_APPROVED', 0),
    'standing_order': pipeline_counts.get('STANDING_ORDER', 0),
    'active': len(positions),
}

# ─── Quality funds summary ───────────────────────────────────────────────────

quality_funds = get_quality_funds(ownership_data, min_stocks=2)
qf_summary = [{'name': name[:35], 'count': len(stocks), 'stocks': ', '.join(sorted(stocks))}
               for name, stocks in quality_funds[:8]]

# ─── Build JSON payload ─────────────────────────────────────────────────────

dashboard_data = {
    'kpis': {
        'nav_eur': round(nav_eur, 0),
        'cash_eur': round(cash_eur, 0),
        'cash_pct': round(cash_pct, 1),
        'long_pct': round(long_pct, 1),
        'n_positions': len(positions),
        'total_pnl_pct': round((total_value_eur - total_invested_eur) / total_invested_eur * 100, 1) if total_invested_eur > 0 else 0,
        'portfolio_ecagr': round(portfolio_ecagr, 1),
        'cash_drag_pct': round(cash_drag_pct, 1),
        'cash_drag_ytd': round(cash_drag_ytd, 2),
        'spy_ytd_return': round(spy_ytd_return, 1),
        'days_since_deploy': days_since_deploy,
        'last_deploy_ticker': last_deploy_ticker,
        'last_deploy_date': last_deploy_date.strftime('%Y-%m-%d') if last_deploy_date else 'N/A',
        'benchmark_spy': round(benchmark_returns.get('S&P 500', 0), 1),
        'benchmark_stoxx': round(benchmark_returns.get('STOXX 600', 0), 1),
        'session': system.get('system', {}).get('session_number', 0),
        'date': today.strftime('%Y-%m-%d %H:%M'),
    },
    'alerts': alerts,
    'positions': position_data,
    'earnings_week': earnings_week,
    'phase_transition': is_phase_transition,
    'phase_portfolio_count': portfolio_earnings_count,
    'phase_pipeline_count': pipeline_earnings_count,
    'phase_missing_fw': missing_frameworks,
    'calendar': cal_items,
    'standing_orders': so_items,
    'funnel': funnel,
    'quality_funds': qf_summary,
    'geo_exposure': geo_pcts,
    'sector_exposure': sector_pcts,
}

data_json = json.dumps(dashboard_data, indent=2, default=str)

# ─── Generate HTML ──────────────────────────────────────────────────────────

html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Command Center — Value Investor System</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { background: #0f0f1e; color: #e0e0e0; font-family: 'Segoe UI', system-ui, -apple-system, sans-serif; padding: 16px; }

  .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; padding-bottom: 10px; border-bottom: 1px solid #2a2a4a; }
  .header h1 { font-size: 20px; color: #fff; letter-spacing: -0.5px; }
  .header .meta { font-size: 11px; color: #666; }

  /* Alert Banner */
  .alert-banner { margin-bottom: 12px; border-radius: 8px; overflow: hidden; }
  .alert-banner:empty { display: none; }
  .alert-item { padding: 6px 14px; font-size: 11px; font-weight: 600; display: flex; align-items: center; gap: 8px; }
  .alert-critical { background: rgba(220,50,50,0.15); color: #ff6060; border-left: 3px solid #ff4040; }
  .alert-warning { background: rgba(220,140,50,0.12); color: #e0a050; border-left: 3px solid #e0a050; }

  /* KPI Cards */
  .kpis { display: grid; grid-template-columns: repeat(auto-fit, minmax(115px, 1fr)); gap: 8px; margin-bottom: 14px; }
  .kpi { background: linear-gradient(135deg, rgba(25,25,50,0.9), rgba(20,20,40,0.9)); border: 1px solid #2a2a4a; border-radius: 8px; padding: 10px; text-align: center; }
  .kpi-label { font-size: 8px; color: #666; text-transform: uppercase; letter-spacing: 1px; }
  .kpi-value { font-size: 22px; font-weight: 700; color: #fff; margin: 1px 0; }
  .kpi-detail { font-size: 9px; color: #888; }

  /* Grid layout */
  .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
  @media (max-width: 1200px) { .grid { grid-template-columns: 1fr; } }
  .full-width { grid-column: 1 / -1; }

  /* Panels */
  .panel { background: rgba(20,20,40,0.8); border: 1px solid #2a2a4a; border-radius: 8px; padding: 14px; }
  .panel h2 { font-size: 12px; color: #8898b0; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 10px; font-weight: 600; }

  /* Risk Heatmap Table */
  table { border-collapse: collapse; width: 100%; font-size: 11px; }
  th { background: #1a1a30; color: #778; font-size: 9px; font-weight: 600; text-transform: uppercase;
       padding: 5px 4px; cursor: pointer; white-space: nowrap; border-bottom: 1px solid #2a2a4a; letter-spacing: 0.3px; }
  th:hover { color: #aab; }
  td { padding: 4px; text-align: center; border-bottom: 1px solid rgba(40,40,70,0.5); }
  tr:hover td { background: rgba(80,120,200,0.06); }
  td.left { text-align: left; }

  .r0 { color: #f06060; } .r1 { color: #e0a050; } .r2 { color: #b0b060; } .r3 { color: #50c060; }
  .bg0 { background: rgba(220,50,50,0.12); } .bg1 { background: rgba(220,140,50,0.1); }
  .bg2 { background: rgba(160,160,80,0.08); } .bg3 { background: rgba(50,180,80,0.1); }

  .badge { display: inline-block; padding: 1px 5px; border-radius: 3px; font-size: 9px; font-weight: 600; }
  .badge-a { background: rgba(50,180,80,0.2); color: #50c060; }
  .badge-b { background: rgba(160,160,80,0.15); color: #b0b060; }
  .badge-c { background: rgba(220,50,50,0.2); color: #f06060; }
  .badge-prob { background: rgba(220,140,50,0.25); color: #e0a050; }
  .badge-mob { background: rgba(220,50,50,0.3); color: #ff6060; }
  .badge-ok { background: rgba(50,180,80,0.15); color: #50c060; }
  .badge-fw { background: rgba(80,180,220,0.2); color: #60b8e0; }
  .badge-nofw { background: rgba(100,100,120,0.2); color: #888; }

  /* Earnings week */
  .ew-item { display: flex; align-items: center; gap: 8px; padding: 6px 0; border-bottom: 1px solid rgba(40,40,70,0.3); font-size: 12px; }
  .ew-date { min-width: 85px; font-weight: 600; font-size: 11px; }
  .ew-ticker { min-width: 65px; font-weight: 700; }
  .ew-event { flex: 1; color: #aaa; font-size: 11px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .ew-badge { min-width: 70px; text-align: right; }
  .ew-position { color: #6ca0dc; }
  .ew-pipeline { color: #888; }

  /* Forward returns bars */
  .fr-item { display: flex; align-items: center; gap: 6px; padding: 3px 0; font-size: 11px; }
  .fr-ticker { min-width: 60px; font-weight: 600; color: #6ca0dc; }
  .fr-bar-bg { flex: 1; height: 16px; background: rgba(30,30,50,0.8); border-radius: 3px; overflow: hidden; position: relative; }
  .fr-bar { height: 100%; border-radius: 3px; }
  .fr-label { position: absolute; right: 6px; top: 1px; font-size: 10px; color: #ddd; font-weight: 600; }

  /* Donut charts */
  .donut-container { display: flex; gap: 20px; justify-content: center; flex-wrap: wrap; }
  .donut-wrap { text-align: center; }
  .donut-wrap h3 { font-size: 10px; color: #778; text-transform: uppercase; margin-bottom: 6px; letter-spacing: 0.5px; }
  .donut-legend { display: flex; flex-wrap: wrap; gap: 4px 12px; justify-content: center; margin-top: 8px; }
  .donut-legend-item { font-size: 9px; color: #aaa; display: flex; align-items: center; gap: 3px; }
  .donut-legend-dot { width: 8px; height: 8px; border-radius: 2px; }

  /* Cash drag gauge */
  .gauge-container { text-align: center; margin-top: 8px; }
  .gauge-label { font-size: 10px; color: #778; text-transform: uppercase; margin-bottom: 4px; }
  .gauge-value { font-size: 20px; font-weight: 700; }
  .gauge-detail { font-size: 10px; color: #888; margin-top: 2px; }
  .gauge-sub { font-size: 11px; font-weight: 600; margin-top: 6px; }
  .deploy-info { font-size: 10px; color: #888; margin-top: 4px; }

  /* Calendar */
  .cal-item { display: flex; align-items: center; gap: 8px; padding: 4px 0; border-bottom: 1px solid rgba(40,40,70,0.3); font-size: 11px; }
  .cal-date { min-width: 70px; font-weight: 600; font-size: 10px; }
  .cal-ticker { min-width: 60px; font-weight: 600; color: #6ca0dc; }
  .cal-event { flex: 1; color: #aaa; font-size: 10px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .cal-days { min-width: 40px; text-align: right; font-size: 10px; font-weight: 600; }
  .urgency-critical { color: #ff5050; } .urgency-high { color: #e0a050; }
  .urgency-medium { color: #b0b060; } .urgency-low { color: #668; }

  /* SO bars */
  .so-item { display: flex; align-items: center; gap: 6px; padding: 3px 0; font-size: 11px; }
  .so-ticker { min-width: 60px; font-weight: 600; color: #6ca0dc; }
  .so-bar-bg { flex: 1; height: 14px; background: rgba(30,30,50,0.8); border-radius: 3px; overflow: hidden; position: relative; }
  .so-bar { height: 100%; border-radius: 3px; }
  .so-bar-label { position: absolute; right: 4px; top: 1px; font-size: 9px; color: #aaa; }
  .so-cat { min-width: 50px; font-size: 9px; text-transform: uppercase; }
  .cat-active { color: #50c060; } .cat-gated { color: #e0a050; }
  .cat-borderline { color: #668; } .cat-extreme { color: #445; }

  /* Funnel */
  .funnel { display: flex; flex-direction: column; gap: 3px; }
  .funnel-row { display: flex; align-items: center; gap: 8px; }
  .funnel-label { min-width: 90px; font-size: 10px; color: #888; text-align: right; }
  .funnel-bar { height: 18px; border-radius: 3px; display: flex; align-items: center; padding-left: 8px; font-size: 10px; font-weight: 600; color: #fff; min-width: 28px; }

  /* Quality funds */
  .qf-item { display: flex; gap: 8px; padding: 3px 0; font-size: 10px; border-bottom: 1px solid rgba(40,40,70,0.3); }
  .qf-name { min-width: 180px; color: #aaa; }
  .qf-count { min-width: 18px; font-weight: 600; color: #6ca0dc; }
  .qf-stocks { color: #668; font-size: 9px; }

  /* Sparkline */
  .sparkline { vertical-align: middle; }

  .footer { margin-top: 12px; font-size: 9px; color: #444; text-align: center; }
</style>
</head>
<body>

<div class="header">
  <h1>Command Center</h1>
  <div class="meta" id="meta"></div>
</div>

<div class="alert-banner" id="alert-banner"></div>

<div class="kpis" id="kpis"></div>

<div class="grid">
  <div class="panel full-width">
    <h2>Position Risk Matrix</h2>
    <table id="risk-table">
      <thead>
        <tr>
          <th data-col="ticker">Ticker</th>
          <th data-col="name">Name</th>
          <th data-col="weight_pct">Wt%</th>
          <th data-col="pnl_pct">P&L</th>
          <th data-col="mos">MoS%</th>
          <th data-col="ecagr" title="Expected CAGR 3yr">E[CAGR]</th>
          <th data-col="qs" title="Quality Score">QS</th>
          <th data-col="insider_net" title="Insider sentiment">Insider</th>
          <th data-col="days_to_earnings" title="Days to earnings">Earn</th>
          <th data-col="conviction">Conv</th>
          <th>Status</th>
          <th>30d</th>
        </tr>
      </thead>
      <tbody id="risk-tbody"></tbody>
    </table>
  </div>

  <div class="panel full-width" id="earnings-week-panel" style="display:none">
    <h2>Earnings This Week</h2>
    <div id="earnings-week"></div>
  </div>

  <div class="panel">
    <h2>Forward Returns — E[CAGR]</h2>
    <div id="forward-returns"></div>
  </div>

  <div class="panel">
    <h2>Exposure Breakdown</h2>
    <div class="donut-container" id="donuts"></div>
    <div class="gauge-container" id="cash-gauge"></div>
  </div>

  <div class="panel">
    <h2>Calendar — Next 21 Days</h2>
    <div id="calendar"></div>
  </div>

  <div class="panel">
    <h2>Standing Orders — Proximity</h2>
    <div id="standing-orders"></div>
  </div>

  <div class="panel">
    <h2>Pipeline Funnel</h2>
    <div id="funnel"></div>
  </div>

  <div class="panel">
    <h2>Smart Money — Quality Funds</h2>
    <div id="quality-funds"></div>
  </div>
</div>

<div class="footer">
  Command Center v2.2 | Data is RAW — interpret with context | Click column headers to sort
</div>

<script>
const D = """ + data_json + """;

// Meta
document.getElementById('meta').innerHTML =
  `Session ${D.kpis.session} | ${D.kpis.date} | NAV &euro;${D.kpis.nav_eur.toLocaleString()}`;

// Alert Banner
const bannerEl = document.getElementById('alert-banner');
if (D.alerts.length > 0) {
  bannerEl.innerHTML = D.alerts.map(a =>
    `<div class="alert-item alert-${a.level}">${a.level === 'critical' ? '!!!' : '<!>'} ${a.msg}</div>`
  ).join('');
}

// KPIs
const benchSpy = D.kpis.benchmark_spy;
const benchStoxx = D.kpis.benchmark_stoxx;
const pnl = D.kpis.total_pnl_pct;
const vsSpy = benchSpy ? (pnl - benchSpy).toFixed(1) : 'N/A';
const vsStoxx = benchStoxx ? (pnl - benchStoxx).toFixed(1) : 'N/A';
const deployDays = D.kpis.days_since_deploy;
const deployColor = deployDays <= 30 ? '#50c060' : deployDays <= 60 ? '#e0a050' : '#f06060';

document.getElementById('kpis').innerHTML = [
  {label: 'NAV', value: '&euro;' + D.kpis.nav_eur.toLocaleString(), detail: `${D.kpis.n_positions} positions`, color: '#fff'},
  {label: 'Cash', value: D.kpis.cash_pct.toFixed(1) + '%', detail: '&euro;' + D.kpis.cash_eur.toLocaleString(), color: D.kpis.cash_pct > 50 ? '#e0a050' : '#50c060'},
  {label: 'Long', value: D.kpis.long_pct.toFixed(1) + '%', detail: 'net exposure', color: '#6ca0dc'},
  {label: 'P&L', value: (pnl >= 0 ? '+' : '') + pnl + '%', detail: 'total return', color: pnl >= 0 ? '#50c060' : '#f06060'},
  {label: 'E[CAGR]', value: D.kpis.portfolio_ecagr.toFixed(1) + '%', detail: 'wtd portfolio', color: D.kpis.portfolio_ecagr >= 12 ? '#50c060' : D.kpis.portfolio_ecagr >= 8 ? '#b0b060' : '#e0a050'},
  {label: 'vs SPY', value: (typeof vsSpy === 'string' ? vsSpy : (vsSpy >= 0 ? '+' : '') + vsSpy + 'pp'), detail: `SPY ${benchSpy ? (benchSpy >= 0 ? '+' : '') + benchSpy + '%' : 'N/A'}`, color: vsSpy === 'N/A' ? '#666' : parseFloat(vsSpy) >= 0 ? '#50c060' : '#f06060'},
  {label: 'Last Deploy', value: deployDays + 'd', detail: D.kpis.last_deploy_ticker + ' (' + D.kpis.last_deploy_date + ')', color: deployColor},
  {label: 'Cash Drag', value: D.kpis.cash_drag_pct.toFixed(1) + 'pp', detail: 'yr opportunity cost', color: D.kpis.cash_drag_pct > 3 ? '#f06060' : D.kpis.cash_drag_pct > 1.5 ? '#e0a050' : '#50c060'},
  {label: 'Earnings', value: D.positions.filter(p => p.days_to_earnings !== null && p.days_to_earnings <= 7).length, detail: 'within 7 days', color: D.positions.filter(p => p.days_to_earnings !== null && p.days_to_earnings <= 7).length > 0 ? '#e0a050' : '#50c060'},
].map(k => `<div class="kpi"><div class="kpi-label">${k.label}</div><div class="kpi-value" style="color:${k.color}">${k.value}</div><div class="kpi-detail">${k.detail}</div></div>`).join('');

// Sparkline SVG generator
function sparkSVG(data, w, h) {
  if (!data || data.length < 2) return '';
  const min = Math.min(...data), max = Math.max(...data);
  const range = max - min || 1;
  const pts = data.map((v, i) => {
    const x = (i / (data.length - 1)) * w;
    const y = h - ((v - min) / range) * (h - 2) - 1;
    return `${x.toFixed(1)},${y.toFixed(1)}`;
  });
  const color = data[data.length - 1] >= data[0] ? '#50c060' : '#f06060';
  return `<svg class="sparkline" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}">
    <polyline points="${pts.join(' ')}" fill="none" stroke="${color}" stroke-width="1.2" stroke-linejoin="round"/>
  </svg>`;
}

// Risk table
let sortCol = 'ecagr', sortAsc = false;
function riskColor(val, thresholds) {
  if (val === null || val === undefined) return {cls: 'r2', bg: 'bg2'};
  if (val <= thresholds[0]) return {cls: 'r0', bg: 'bg0'};
  if (val <= thresholds[1]) return {cls: 'r1', bg: 'bg1'};
  if (val <= thresholds[2]) return {cls: 'r2', bg: 'bg2'};
  return {cls: 'r3', bg: 'bg3'};
}

function renderRiskTable() {
  const sorted = [...D.positions].sort((a, b) => {
    let va = a[sortCol], vb = b[sortCol];
    if (va === null || va === undefined) va = sortAsc ? 9999 : -9999;
    if (vb === null || vb === undefined) vb = sortAsc ? 9999 : -9999;
    if (typeof va === 'string') return sortAsc ? va.localeCompare(vb) : vb.localeCompare(va);
    return sortAsc ? va - vb : vb - va;
  });
  document.getElementById('risk-tbody').innerHTML = sorted.map(p => {
    const mosC = riskColor(p.mos, [0, 10, 20]);
    const pnlC = riskColor(p.pnl_pct, [-10, -5, 0]);
    const ecagrC = p.ecagr !== null ? riskColor(p.ecagr, [5, 10, 15]) : {cls: 'r2', bg: ''};
    const insC = p.insider_signal === 'BEARISH' ? 'r0' : p.insider_signal === 'CAUTIOUS' ? 'r1' : p.insider_signal === 'STRONG' ? 'r3' : p.insider_signal === 'BULLISH' ? 'r3' : 'r2';
    const earnDays = p.days_to_earnings;
    const earnC = earnDays !== null ? (earnDays <= 2 ? 'r0' : earnDays <= 7 ? 'r1' : earnDays <= 14 ? 'r2' : 'r3') : 'r2';
    const earnText = earnDays !== null ? earnDays + 'd' : '\\u2014';
    const tierBadge = p.tier === 'A' ? 'badge-a' : p.tier === 'C' ? 'badge-c' : 'badge-b';
    const statusBadge = p.make_or_break ? 'badge-mob' : p.on_probation ? 'badge-prob' : 'badge-ok';
    const statusText = p.make_or_break ? 'M-O-B' : p.on_probation ? 'PROB' : 'OK';
    const convC = p.conviction === 'high' ? 'r3' : p.conviction === 'medium' ? 'r2' : 'r1';
    const insText = p.insider_signal === 'STRONG'
      ? `STRONG (${p.ins_strong_count} C-suite, ${p.ins_strong_value >= 1000000 ? (p.ins_strong_value/1000000).toFixed(1)+'M' : p.ins_strong_value >= 1000 ? Math.round(p.ins_strong_value/1000)+'K' : p.ins_strong_value})`
      : p.insider_signal + (p.insider_net ? ` (${p.insider_net > 0 ? '+' : ''}${p.insider_net})` : '');
    const ecagrText = p.ecagr !== null ? p.ecagr.toFixed(1) + '%' : 'N/A';
    const spark = sparkSVG(p.sparkline, 60, 18);
    return `<tr>
      <td class="left" style="font-weight:600;color:#fff">${p.ticker}</td>
      <td class="left" style="color:#888;font-size:10px">${p.name.substring(0,22)}</td>
      <td>${p.weight_pct}%</td>
      <td class="${pnlC.cls} ${pnlC.bg}">${p.pnl_pct > 0 ? '+' : ''}${p.pnl_pct}%</td>
      <td class="${mosC.cls} ${mosC.bg}">${p.mos > 0 ? '+' : ''}${p.mos}%</td>
      <td class="${ecagrC.cls}" style="font-weight:600">${ecagrText}</td>
      <td><span class="badge ${tierBadge}">${p.tier} ${p.qs}</span></td>
      <td class="${insC}" style="font-size:10px">${insText}</td>
      <td class="${earnC}" title="${p.next_event}">${earnText}</td>
      <td class="${convC}">${p.conviction}</td>
      <td><span class="badge ${statusBadge}">${statusText}</span></td>
      <td>${spark}</td>
    </tr>`;
  }).join('');
}
renderRiskTable();

document.querySelectorAll('#risk-table th').forEach(th => {
  th.addEventListener('click', () => {
    const col = th.dataset.col;
    if (!col) return;
    if (col === sortCol) sortAsc = !sortAsc;
    else { sortCol = col; sortAsc = col === 'ticker' || col === 'name'; }
    renderRiskTable();
  });
});

// Earnings Week + Phase Transition
if (D.earnings_week.length > 0) {
  document.getElementById('earnings-week-panel').style.display = '';
  let ewHTML = '';
  if (D.phase_transition) {
    ewHTML += `<div style="background:rgba(220,50,50,0.15);border:1px solid rgba(220,50,50,0.3);border-radius:6px;padding:10px;margin-bottom:10px">
      <div style="color:#ff6060;font-weight:700;font-size:12px">PHASE TRANSITION WEEK</div>
      <div style="color:#e0a050;font-size:11px;margin-top:4px">${D.phase_portfolio_count} portfolio + ${D.phase_pipeline_count} pipeline reporting. Psychology (F) amplified.</div>
      <div style="color:#aaa;font-size:10px;margin-top:4px">Protocol: Pre-commit ALL decisions before market open. Process by position size. Batch assessments.</div>
      ${D.phase_missing_fw.length > 0 ? '<div style="color:#ff6060;font-size:10px;margin-top:4px">MISSING FRAMEWORKS: ' + D.phase_missing_fw.join(', ') + '</div>' : ''}
    </div>`;
  }
  ewHTML += D.earnings_week.map(e => {
    const dayText = e.days_away === 0 ? 'TODAY' : e.days_away === 1 ? 'TOMORROW' : e.days_away + 'd';
    const dayC = e.days_away <= 1 ? 'urgency-critical' : e.days_away <= 3 ? 'urgency-high' : 'urgency-medium';
    const tickerC = e.is_position ? 'ew-position' : 'ew-pipeline';
    const fwBadge = e.has_framework ? '<span class="badge badge-fw">FRAMEWORK</span>' : '<span class="badge badge-nofw">NO FW</span>';
    const typeBadge = e.is_position ? '<span class="badge badge-a">POSITION</span>' : '<span class="badge badge-b">PIPELINE</span>';
    return `<div class="ew-item">
      <span class="ew-date ${dayC}">${e.date} (${dayText})</span>
      <span class="ew-ticker ${tickerC}">${e.ticker}</span>
      <span class="ew-event" title="${e.action}">${e.event}</span>
      <span class="ew-badge">${typeBadge} ${fwBadge}</span>
    </div>`;
  }).join('');
  document.getElementById('earnings-week').innerHTML = ewHTML;
}

// Forward Returns (E[CAGR] horizontal bars)
const frSorted = [...D.positions].filter(p => p.ecagr !== null).sort((a, b) => b.ecagr - a.ecagr);
const maxEcagr = Math.max(...frSorted.map(p => Math.abs(p.ecagr)), 1);
document.getElementById('forward-returns').innerHTML = frSorted.map(p => {
  const pct = Math.min(100, Math.abs(p.ecagr) / maxEcagr * 100);
  const color = p.ecagr >= 15 ? '#50c060' : p.ecagr >= 10 ? '#6ca0dc' : p.ecagr >= 5 ? '#b0b060' : '#f06060';
  return `<div class="fr-item">
    <span class="fr-ticker">${p.ticker}</span>
    <div class="fr-bar-bg">
      <div class="fr-bar" style="width:${pct}%;background:${color}"></div>
      <span class="fr-label">${p.ecagr.toFixed(1)}%</span>
    </div>
  </div>`;
}).join('');

// Donut Charts (Geographic + Sector)
function donutSVG(data, size, title) {
  const colors = ['#6ca0dc', '#50c060', '#e0a050', '#f06060', '#b080d0', '#80d0c0', '#d0a060', '#8080c0', '#c06080', '#60c0b0', '#556'];
  const total = Object.values(data).reduce((s, v) => s + v, 0) || 1;
  const entries = Object.entries(data);
  let html = `<div class="donut-wrap"><h3>${title}</h3><svg width="${size}" height="${size}" viewBox="0 0 ${size} ${size}">`;
  const cx = size / 2, cy = size / 2, r = size * 0.38, inner = size * 0.22;
  let cumAngle = -Math.PI / 2;

  entries.forEach(([label, val], i) => {
    const angle = (val / total) * Math.PI * 2;
    const midAngle = cumAngle + angle / 2;
    const x1o = cx + r * Math.cos(cumAngle), y1o = cy + r * Math.sin(cumAngle);
    const x2o = cx + r * Math.cos(cumAngle + angle), y2o = cy + r * Math.sin(cumAngle + angle);
    const x1i = cx + inner * Math.cos(cumAngle + angle), y1i = cy + inner * Math.sin(cumAngle + angle);
    const x2i = cx + inner * Math.cos(cumAngle), y2i = cy + inner * Math.sin(cumAngle);
    const large = angle > Math.PI ? 1 : 0;
    const color = label === 'Cash' ? '#334' : colors[i % colors.length];
    html += `<path d="M${x1o},${y1o} A${r},${r} 0 ${large} 1 ${x2o},${y2o} L${x1i},${y1i} A${inner},${inner} 0 ${large} 0 ${x2i},${y2i} Z" fill="${color}" stroke="#0f0f1e" stroke-width="1">
      <title>${label}: ${val}%</title></path>`;
    cumAngle += angle;
  });

  html += `</svg><div class="donut-legend">`;
  entries.forEach(([label, val], i) => {
    const color = label === 'Cash' ? '#334' : colors[i % colors.length];
    html += `<span class="donut-legend-item"><span class="donut-legend-dot" style="background:${color}"></span>${label} ${val}%</span>`;
  });
  html += `</div></div>`;
  return html;
}

document.getElementById('donuts').innerHTML =
  donutSVG(D.geo_exposure, 150, 'Geography') +
  donutSVG(D.sector_exposure, 150, 'Sector');

// Cash Drag Gauge + Deployment Monitor
const cdPct = D.kpis.cash_drag_pct;
const cdColor = cdPct > 3 ? '#f06060' : cdPct > 1.5 ? '#e0a050' : '#50c060';
const cdYtd = D.kpis.cash_drag_ytd;
const cdYtdColor = cdYtd > 2 ? '#f06060' : cdYtd > 0.5 ? '#e0a050' : '#50c060';
const dDays = D.kpis.days_since_deploy;
const dColor = dDays <= 30 ? '#50c060' : dDays <= 60 ? '#e0a050' : '#f06060';
document.getElementById('cash-gauge').innerHTML = `
  <div class="gauge-label">Cash Drag</div>
  <div class="gauge-value" style="color:${cdColor}">${cdPct.toFixed(1)}pp/yr</div>
  <div class="gauge-detail">${D.kpis.cash_pct.toFixed(0)}% cash x ${D.kpis.portfolio_ecagr.toFixed(1)}% E[CAGR] = ${cdPct.toFixed(1)}pp lost annually</div>
  <div class="gauge-sub" style="color:${cdYtdColor}">YTD drag: ${cdYtd.toFixed(2)}pp <span style="color:#666">(${D.kpis.cash_pct.toFixed(0)}% cash x SPY ${D.kpis.spy_ytd_return >= 0 ? '+' : ''}${D.kpis.spy_ytd_return.toFixed(1)}% YTD)</span></div>
  <svg width="200" height="12" style="margin-top:6px">
    <rect x="0" y="0" width="200" height="12" rx="6" fill="#1a1a30"/>
    <rect x="0" y="0" width="${Math.min(200, D.kpis.cash_pct / 100 * 200)}" height="12" rx="6" fill="${cdColor}" opacity="0.7"/>
    <text x="100" y="10" text-anchor="middle" fill="#ccc" font-size="8">${D.kpis.cash_pct.toFixed(0)}% idle</text>
  </svg>
  <div class="deploy-info" style="margin-top:8px">Last deployment: <span style="color:${dColor};font-weight:600">${dDays}d ago</span> (${D.kpis.last_deploy_ticker} on ${D.kpis.last_deploy_date})</div>
`;

// Calendar
document.getElementById('calendar').innerHTML = D.calendar.map(c => {
  const urgCls = 'urgency-' + c.urgency;
  return `<div class="cal-item">
    <span class="cal-date ${urgCls}">${c.date}</span>
    <span class="cal-ticker">${c.ticker}</span>
    <span class="cal-event" title="${c.action}">${c.event}</span>
    <span class="cal-days ${urgCls}">${c.days_away === 0 ? 'TODAY' : c.days_away === 1 ? 'TMW' : c.days_away + 'd'}</span>
  </div>`;
}).join('') || '<div style="color:#555;font-size:12px">No events in next 21 days</div>';

// Standing Orders
document.getElementById('standing-orders').innerHTML = D.standing_orders.map(so => {
  const maxDist = 30;
  const barPct = Math.max(5, Math.min(100, (1 - so.distance / maxDist) * 100));
  const barColor = so.distance < 5 ? '#50c060' : so.distance < 10 ? '#b0b060' : so.distance < 15 ? '#e0a050' : '#556';
  const catCls = 'cat-' + so.category.toLowerCase();
  return `<div class="so-item">
    <span class="so-ticker">${so.ticker}</span>
    <span class="so-cat ${catCls}">${so.category}</span>
    <div class="so-bar-bg">
      <div class="so-bar" style="width:${barPct}%;background:${barColor}"></div>
      <span class="so-bar-label">${so.distance.toFixed(1)}% \\u2192 ${so.trigger}</span>
    </div>
  </div>`;
}).join('');

// Funnel
const funnelData = [
  {label: 'Universe', count: D.funnel.scored + D.funnel.r1_complete + D.funnel.r3_complete + D.funnel.approved + D.funnel.standing_order, color: '#445'},
  {label: 'R1 Complete', count: D.funnel.r1_complete, color: '#5a6a8a'},
  {label: 'R3 Complete', count: D.funnel.r3_complete, color: '#6a8aaa'},
  {label: 'R4 Approved', count: D.funnel.approved, color: '#4a9a6a'},
  {label: 'Standing Order', count: D.funnel.standing_order, color: '#50c060'},
  {label: 'Active', count: D.funnel.active, color: '#e8863a'},
];
const maxCount = Math.max(...funnelData.map(f => f.count), 1);
document.getElementById('funnel').innerHTML = '<div class="funnel">' + funnelData.map(f => {
  const w = Math.max(28, f.count / maxCount * 280);
  return `<div class="funnel-row">
    <span class="funnel-label">${f.label}</span>
    <div class="funnel-bar" style="width:${w}px;background:${f.color}">${f.count}</div>
  </div>`;
}).join('') + '</div>';

// Quality Funds
document.getElementById('quality-funds').innerHTML = D.quality_funds.map(qf =>
  `<div class="qf-item">
    <span class="qf-name">${qf.name}</span>
    <span class="qf-count">${qf.count}</span>
    <span class="qf-stocks">${qf.stocks}</span>
  </div>`
).join('') || '<div style="color:#555;font-size:12px">No quality funds detected</div>';
</script>
</body>
</html>"""

with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\nCommand Center v2.2 saved: {OUTPUT}")
print("Open in browser for full interactive dashboard.")

# Console summary
print(f"\n── DASHBOARD SUMMARY ─────────────────────────────────────────────")
print(f"  NAV: EUR{nav_eur:,.0f} | Cash: {cash_pct:.1f}% (EUR{cash_eur:,.0f}) | Long: {long_pct:.1f}%")
print(f"  P&L: {(total_value_eur - total_invested_eur) / total_invested_eur * 100:.1f}% | E[CAGR]: {portfolio_ecagr:.1f}% | Cash drag: {cash_drag_pct:.1f}pp/yr")
print(f"  Last deploy: {last_deploy_ticker} ({days_since_deploy}d ago) | Cash drag YTD: {cash_drag_ytd:.2f}pp (SPY {spy_ytd_return:+.1f}%)")
if benchmark_returns:
    print(f"  Benchmarks: " + " | ".join(f"{k}: {v:+.1f}%" for k, v in benchmark_returns.items()))
print(f"  Alerts: {len(alerts)} ({sum(1 for a in alerts if a['level'] == 'critical')} critical)")
print(f"  Earnings this week: {len(earnings_week)} | Calendar (21d): {len(cal_items)}")
print(f"  Pipeline: {funnel['scored']} scored -> {funnel['r1_complete']} R1 -> {funnel['r3_complete']} R3 -> {funnel['approved']} approved -> {funnel['standing_order']} SO")
