#!/usr/bin/env python3
"""
Command Center — Unified session-start dashboard in a single interactive HTML page.

Consolidates all critical information into one view:
  1. Portfolio KPIs (NAV, cash%, positions, avg risk score)
  2. Risk Heatmap (sortable, color-coded position risk matrix)
  3. Calendar Timeline (next 14 days, color by urgency)
  4. Standing Order Proximity (nearest triggers, visual bars)
  5. Insider Sentiment Summary (from ownership cache)
  6. Pipeline Status (funnel counts by stage)

Uses shared ownership_cache for institutional data (instant if cached today).
Uses yfinance for live prices and FX rates.

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
import warnings
from datetime import datetime, timedelta
from collections import defaultdict, Counter

warnings.filterwarnings('ignore')

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT = os.path.join(BASE, 'docs', 'command_center.html')

sys.path.insert(0, os.path.join(BASE, 'tools'))
from ownership_cache import load_or_fetch, get_quality_funds, get_insider_sentiment

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

positions = portfolio.get('positions', [])
events = calendar_data.get('events', []) or []
standing_orders = so_data.get('standing_orders', []) or []
companies = universe.get('quality_universe', {}).get('companies', [])
cash_eur = portfolio.get('cash', {}).get('amount', 0)

tickers = [p['ticker'] for p in positions]

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

# ─── Fetch prices + FX ──────────────────────────────────────────────────────

import yfinance as yf

print("=" * 60)
print("COMMAND CENTER — Building session dashboard")
print("=" * 60)

print("\nFetching FX rates + prices...", flush=True)
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

prices = {}
for ticker in tickers:
    try:
        t = yf.Ticker(ticker)
        h = t.history(period='2d')
        if not h.empty:
            prices[ticker] = h['Close'].iloc[-1]
    except Exception:
        pass

print(f"  {len(prices)}/{len(tickers)} prices fetched")

# ─── Ownership data (cached) ────────────────────────────────────────────────

print("Loading ownership data...")
ownership_data = load_or_fetch(tickers, force_fresh=FORCE_FRESH)

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
        if currency == 'GBp':
            mos = (fv_num - price) / fv_num * 100
        elif currency == 'EUR':
            mos = (fv_num - price) / fv_num * 100
        elif currency == 'CHF':
            mos = (fv_num - price) / fv_num * 100
        else:
            mos = (fv_num - price) / fv_num * 100

    # QS/Tier from system.yaml
    tier = '?'
    qs = 0
    for sp in system.get('system', {}).get('portfolio_quality_analysis', {}).get('positions', []):
        if sp.get('ticker') == ticker:
            tier = sp.get('tier', '?')
            qs = sp.get('score', 0)
            break

    # Insider sentiment
    buys, sells, buybacks, options, net, signal = get_insider_sentiment(ownership_data, ticker)

    # Earnings proximity
    today = datetime.now()
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
        'tier': tier,
        'qs': qs,
        'conviction': pos.get('conviction', 'low'),
        'insider_signal': signal,
        'insider_net': net,
        'days_to_earnings': days_to_earnings,
        'next_event': next_event,
        'on_probation': on_probation,
        'make_or_break': make_or_break,
        'weight_pct': 0,  # computed below
    })

nav_eur = total_value_eur + cash_eur
cash_pct = cash_eur / nav_eur * 100 if nav_eur > 0 else 0
long_pct = total_value_eur / nav_eur * 100 if nav_eur > 0 else 0

for pd_ in position_data:
    pd_['weight_pct'] = round(pd_['value_eur'] / nav_eur * 100, 1) if nav_eur > 0 else 0

# ─── Calendar data ───────────────────────────────────────────────────────────

today_date = datetime.now()
cal_items = []
for evt in events:
    if not isinstance(evt, dict): continue
    try:
        d = datetime.strptime(str(evt.get('date', '')), '%Y-%m-%d')
        days_away = (d - today_date).days
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
so_items = so_items[:15]  # top 15 nearest

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
        'session': system.get('system', {}).get('session_number', 0),
        'date': today_date.strftime('%Y-%m-%d %H:%M'),
    },
    'positions': position_data,
    'calendar': cal_items,
    'standing_orders': so_items,
    'funnel': funnel,
    'quality_funds': qf_summary,
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

  .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; padding-bottom: 12px; border-bottom: 1px solid #2a2a4a; }
  .header h1 { font-size: 20px; color: #fff; letter-spacing: -0.5px; }
  .header .meta { font-size: 11px; color: #666; }

  /* KPI Cards */
  .kpis { display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 10px; margin-bottom: 16px; }
  .kpi { background: linear-gradient(135deg, rgba(25,25,50,0.9), rgba(20,20,40,0.9)); border: 1px solid #2a2a4a; border-radius: 8px; padding: 12px; text-align: center; }
  .kpi-label { font-size: 9px; color: #666; text-transform: uppercase; letter-spacing: 1px; }
  .kpi-value { font-size: 24px; font-weight: 700; color: #fff; margin: 2px 0; }
  .kpi-detail { font-size: 10px; color: #888; }

  /* Grid layout */
  .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
  @media (max-width: 1200px) { .grid { grid-template-columns: 1fr; } }
  .full-width { grid-column: 1 / -1; }

  /* Panels */
  .panel { background: rgba(20,20,40,0.8); border: 1px solid #2a2a4a; border-radius: 8px; padding: 14px; }
  .panel h2 { font-size: 13px; color: #8898b0; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 10px; font-weight: 600; }

  /* Risk Heatmap Table */
  table { border-collapse: collapse; width: 100%; font-size: 12px; }
  th { background: #1a1a30; color: #778; font-size: 10px; font-weight: 600; text-transform: uppercase;
       padding: 6px 5px; cursor: pointer; white-space: nowrap; border-bottom: 1px solid #2a2a4a; letter-spacing: 0.3px; }
  th:hover { color: #aab; }
  td { padding: 5px; text-align: center; border-bottom: 1px solid rgba(40,40,70,0.5); }
  tr:hover td { background: rgba(80,120,200,0.06); }
  td.left { text-align: left; }

  .r0 { color: #f06060; } .r1 { color: #e0a050; } .r2 { color: #b0b060; } .r3 { color: #50c060; }
  .bg0 { background: rgba(220,50,50,0.12); } .bg1 { background: rgba(220,140,50,0.1); }
  .bg2 { background: rgba(160,160,80,0.08); } .bg3 { background: rgba(50,180,80,0.1); }

  .badge { display: inline-block; padding: 1px 6px; border-radius: 3px; font-size: 9px; font-weight: 600; }
  .badge-a { background: rgba(50,180,80,0.2); color: #50c060; }
  .badge-b { background: rgba(160,160,80,0.15); color: #b0b060; }
  .badge-c { background: rgba(220,50,50,0.2); color: #f06060; }
  .badge-prob { background: rgba(220,140,50,0.25); color: #e0a050; }
  .badge-mob { background: rgba(220,50,50,0.3); color: #ff6060; }
  .badge-ok { background: rgba(50,180,80,0.15); color: #50c060; }

  /* Calendar */
  .cal-item { display: flex; align-items: center; gap: 8px; padding: 5px 0; border-bottom: 1px solid rgba(40,40,70,0.3); font-size: 12px; }
  .cal-date { min-width: 70px; font-weight: 600; font-size: 11px; }
  .cal-ticker { min-width: 65px; font-weight: 600; color: #6ca0dc; }
  .cal-event { flex: 1; color: #aaa; font-size: 11px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .cal-days { min-width: 40px; text-align: right; font-size: 10px; font-weight: 600; }
  .urgency-critical { color: #ff5050; } .urgency-high { color: #e0a050; }
  .urgency-medium { color: #b0b060; } .urgency-low { color: #668; }

  /* SO bars */
  .so-item { display: flex; align-items: center; gap: 6px; padding: 4px 0; font-size: 11px; }
  .so-ticker { min-width: 65px; font-weight: 600; color: #6ca0dc; }
  .so-bar-bg { flex: 1; height: 14px; background: rgba(30,30,50,0.8); border-radius: 3px; overflow: hidden; position: relative; }
  .so-bar { height: 100%; border-radius: 3px; transition: width 0.3s; }
  .so-bar-label { position: absolute; right: 4px; top: 1px; font-size: 9px; color: #aaa; }
  .so-cat { min-width: 55px; font-size: 9px; text-transform: uppercase; }
  .cat-active { color: #50c060; } .cat-gated { color: #e0a050; }
  .cat-borderline { color: #668; } .cat-extreme { color: #445; }

  /* Funnel */
  .funnel { display: flex; flex-direction: column; gap: 4px; }
  .funnel-row { display: flex; align-items: center; gap: 8px; }
  .funnel-label { min-width: 90px; font-size: 11px; color: #888; text-align: right; }
  .funnel-bar { height: 20px; border-radius: 3px; display: flex; align-items: center; padding-left: 8px; font-size: 11px; font-weight: 600; color: #fff; min-width: 30px; }

  /* Quality funds */
  .qf-item { display: flex; gap: 8px; padding: 3px 0; font-size: 11px; border-bottom: 1px solid rgba(40,40,70,0.3); }
  .qf-name { min-width: 200px; color: #aaa; }
  .qf-count { min-width: 20px; font-weight: 600; color: #6ca0dc; }
  .qf-stocks { color: #668; font-size: 10px; }

  .footer { margin-top: 12px; font-size: 9px; color: #444; text-align: center; }
</style>
</head>
<body>

<div class="header">
  <h1>Command Center</h1>
  <div class="meta" id="meta"></div>
</div>

<div class="kpis" id="kpis"></div>

<div class="grid">
  <div class="panel full-width">
    <h2>Position Risk Matrix</h2>
    <table id="risk-table">
      <thead>
        <tr>
          <th data-col="ticker">Ticker</th>
          <th data-col="name">Name</th>
          <th data-col="weight_pct">Weight</th>
          <th data-col="pnl_pct">P&L</th>
          <th data-col="mos">MoS%</th>
          <th data-col="qs" title="Quality Score">QS</th>
          <th data-col="insider_net" title="Insider sentiment">Insider</th>
          <th data-col="days_to_earnings" title="Days to earnings">Earnings</th>
          <th data-col="conviction">Conv.</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody id="risk-tbody"></tbody>
    </table>
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
  Command Center v1.0 | Data is RAW — interpret with context | Click column headers to sort risk matrix
</div>

<script>
const D = """ + data_json + """;

// Meta
document.getElementById('meta').innerHTML =
  `Session ${D.kpis.session} | ${D.kpis.date} | NAV €${D.kpis.nav_eur.toLocaleString()}`;

// KPIs
document.getElementById('kpis').innerHTML = [
  {label: 'NAV', value: '€' + D.kpis.nav_eur.toLocaleString(), detail: `${D.kpis.n_positions} positions`, color: '#fff'},
  {label: 'Cash', value: D.kpis.cash_pct.toFixed(1) + '%', detail: '€' + D.kpis.cash_eur.toLocaleString(), color: D.kpis.cash_pct > 50 ? '#e0a050' : '#50c060'},
  {label: 'Long', value: D.kpis.long_pct.toFixed(1) + '%', detail: 'net exposure', color: '#6ca0dc'},
  {label: 'P&L', value: (D.kpis.total_pnl_pct >= 0 ? '+' : '') + D.kpis.total_pnl_pct + '%', detail: 'total return', color: D.kpis.total_pnl_pct >= 0 ? '#50c060' : '#f06060'},
  {label: 'Bearish', value: D.positions.filter(p => p.insider_signal === 'BEARISH').length, detail: 'insider alerts', color: D.positions.filter(p => p.insider_signal === 'BEARISH').length > 0 ? '#f06060' : '#50c060'},
  {label: 'Earnings <7d', value: D.positions.filter(p => p.days_to_earnings !== null && p.days_to_earnings <= 7).length, detail: 'imminent', color: D.positions.filter(p => p.days_to_earnings !== null && p.days_to_earnings <= 7).length > 0 ? '#e0a050' : '#50c060'},
].map(k => `<div class="kpi"><div class="kpi-label">${k.label}</div><div class="kpi-value" style="color:${k.color}">${k.value}</div><div class="kpi-detail">${k.detail}</div></div>`).join('');

// Risk table
let sortCol = 'mos', sortAsc = true;
function riskColor(val, thresholds) {
  // thresholds = [red, orange, yellow] (above yellow = green)
  if (val === null || val === undefined) return {cls: 'r2', bg: 'bg2'};
  if (val <= thresholds[0]) return {cls: 'r0', bg: 'bg0'};
  if (val <= thresholds[1]) return {cls: 'r1', bg: 'bg1'};
  if (val <= thresholds[2]) return {cls: 'r2', bg: 'bg2'};
  return {cls: 'r3', bg: 'bg3'};
}

function renderRiskTable() {
  const sorted = [...D.positions].sort((a, b) => {
    let va = a[sortCol], vb = b[sortCol];
    if (va === null) va = sortAsc ? 9999 : -9999;
    if (vb === null) vb = sortAsc ? 9999 : -9999;
    if (typeof va === 'string') return sortAsc ? va.localeCompare(vb) : vb.localeCompare(va);
    return sortAsc ? va - vb : vb - va;
  });
  document.getElementById('risk-tbody').innerHTML = sorted.map(p => {
    const mosC = riskColor(p.mos, [0, 10, 20]);
    const pnlC = riskColor(p.pnl_pct, [-10, -5, 0]);
    const insC = p.insider_signal === 'BEARISH' ? 'r0' : p.insider_signal === 'CAUTIOUS' ? 'r1' : p.insider_signal === 'BULLISH' ? 'r3' : 'r2';
    const earnDays = p.days_to_earnings;
    const earnC = earnDays !== null ? (earnDays <= 2 ? 'r0' : earnDays <= 7 ? 'r1' : earnDays <= 14 ? 'r2' : 'r3') : 'r2';
    const earnText = earnDays !== null ? earnDays + 'd' : '—';
    const tierBadge = p.tier === 'A' ? 'badge-a' : p.tier === 'C' ? 'badge-c' : 'badge-b';
    const statusBadge = p.make_or_break ? 'badge-mob' : p.on_probation ? 'badge-prob' : 'badge-ok';
    const statusText = p.make_or_break ? 'M-O-B' : p.on_probation ? 'PROBATION' : 'OK';
    const convC = p.conviction === 'high' ? 'r3' : p.conviction === 'medium' ? 'r2' : 'r1';
    const insText = p.insider_signal + (p.insider_net ? ` (${p.insider_net > 0 ? '+' : ''}${p.insider_net})` : '');
    return `<tr>
      <td class="left" style="font-weight:600;color:#fff">${p.ticker}</td>
      <td class="left" style="color:#888;font-size:10px">${p.name.substring(0,25)}</td>
      <td>${p.weight_pct}%</td>
      <td class="${pnlC.cls} ${pnlC.bg}">${p.pnl_pct > 0 ? '+' : ''}${p.pnl_pct}%</td>
      <td class="${mosC.cls} ${mosC.bg}">${p.mos > 0 ? '+' : ''}${p.mos}%</td>
      <td><span class="badge ${tierBadge}">${p.tier} ${p.qs}</span></td>
      <td class="${insC}">${insText}</td>
      <td class="${earnC}" title="${p.next_event}">${earnText}</td>
      <td class="${convC}">${p.conviction}</td>
      <td><span class="badge ${statusBadge}">${statusText}</span></td>
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

// Calendar
document.getElementById('calendar').innerHTML = D.calendar.map(c => {
  const urgCls = 'urgency-' + c.urgency;
  return `<div class="cal-item">
    <span class="cal-date ${urgCls}">${c.date}</span>
    <span class="cal-ticker">${c.ticker}</span>
    <span class="cal-event" title="${c.action}">${c.event}</span>
    <span class="cal-days ${urgCls}">${c.days_away === 0 ? 'TODAY' : c.days_away === 1 ? 'TOMORROW' : c.days_away + 'd'}</span>
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
      <span class="so-bar-label">${so.distance.toFixed(1)}% → ${so.trigger}</span>
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
  const w = Math.max(30, f.count / maxCount * 300);
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

print(f"\nCommand Center saved: {OUTPUT}")
print("Open in browser for full interactive dashboard.")

# Console summary
print(f"\n── DASHBOARD SUMMARY ─────────────────────────────────────────────")
print(f"  NAV: €{nav_eur:,.0f} | Cash: {cash_pct:.1f}% (€{cash_eur:,.0f}) | Long: {long_pct:.1f}%")
print(f"  Positions: {len(positions)} | Bearish insiders: {sum(1 for p in position_data if p['insider_signal'] == 'BEARISH')}")
print(f"  Earnings <7d: {sum(1 for p in position_data if p['days_to_earnings'] is not None and p['days_to_earnings'] <= 7)}")
print(f"  Calendar events (21d): {len(cal_items)} | SOs tracked: {len(so_items)}")
print(f"  Pipeline: {funnel['scored']} scored → {funnel['r1_complete']} R1 → {funnel['r3_complete']} R3 → {funnel['approved']} approved → {funnel['standing_order']} SO")
