#!/usr/bin/env python3
"""
Ownership Graph v2.0 — Interactive force-directed network with rich insider detail.

Nodes:
  - Stocks (circles): colored by status (portfolio/SO active/SO gated)
  - Funds (diamonds): institutional holders, sized by overlap
  - People (triangles): insiders with transaction detail, sized by total value

Edges:
  - Holds (green): fund holds stock
  - Insider buy (gold): personal purchase
  - Insider sell (red): personal sale
  - Buyback (teal): corporate buyback

Improvements v2.0:
  - Aggregated edges (one per person+stock, total value)
  - Edge width proportional to transaction value
  - Rich tooltips: title, value, shares, dates, pattern detection
  - Detail panel on click (full transaction history)
  - Person nodes sized by total value
  - Pattern detection: "Programmatic (10b5-1)" vs "Discretionary"

Output: docs/ownership_graph.html

Usage:
    python3 tools/ownership_graph.py
    python3 tools/ownership_graph.py --portfolio-only
    python3 tools/ownership_graph.py --top-funds 5
"""

import json
import os
import sys
import yaml
import re
import warnings
warnings.filterwarnings('ignore')

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT = os.path.join(BASE, 'docs', 'ownership_graph.html')

sys.path.insert(0, os.path.join(BASE, 'tools'))
from ownership_cache import load_or_fetch, is_indexer

PORTFOLIO_ONLY = '--portfolio-only' in sys.argv
FORCE_FRESH = '--fresh' in sys.argv
TOP_FUNDS = 5
for i, arg in enumerate(sys.argv):
    if arg == '--top-funds' and i + 1 < len(sys.argv):
        TOP_FUNDS = int(sys.argv[i + 1])

# ─── Load portfolio & standing orders ─────────────────────────────────────────

def load_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

portfolio = load_yaml(os.path.join(BASE, 'portfolio', 'current.yaml'))
so_data = load_yaml(os.path.join(BASE, 'state', 'standing_orders.yaml'))

positions = portfolio.get('positions', [])
standing_orders = so_data.get('standing_orders', []) if not PORTFOLIO_ONLY else []

stocks = {}
for p in positions:
    stocks[p['ticker']] = {
        'name': p.get('name', p['ticker']),
        'status': 'portfolio',
        'conviction': p.get('conviction', 'low'),
    }

for so in standing_orders:
    t = so.get('ticker', '')
    cat = so.get('category', 'GATED')
    if t not in stocks:
        stocks[t] = {
            'name': t,
            'status': f'so_{cat.lower()}',
            'conviction': 'none',
        }

print(f"Stocks to process: {len(stocks)} ({len(positions)} portfolio + {len(stocks) - len(positions)} SOs)")

# ─── Fetch ownership data ─────────────────────────────────────────────────────

all_tickers = list(stocks.keys())
ownership_data = load_or_fetch(all_tickers, force_fresh=FORCE_FRESH, top_funds=TOP_FUNDS)

# ─── Build graph nodes and edges ──────────────────────────────────────────────

nodes = []
edges = []
fund_stock_count = {}
node_ids = {}
node_counter = [0]

def get_node_id(name, node_type):
    key = f"{node_type}:{name}"
    if key not in node_ids:
        node_ids[key] = node_counter[0]
        node_counter[0] += 1
    return node_ids[key]

def fmt_value(v):
    if v >= 1_000_000: return f"${v / 1_000_000:.1f}M"
    if v >= 1_000: return f"${v / 1_000:.0f}K"
    return f"${v:.0f}"

def fmt_shares(s):
    if s >= 1_000_000: return f"{s / 1_000_000:.1f}M"
    if s >= 1_000: return f"{s / 1_000:.1f}K"
    return str(s)

# Add stock nodes
for ticker, info in stocks.items():
    nid = get_node_id(ticker, 'stock')
    nodes.append({
        'id': nid,
        'label': ticker,
        'name': info['name'],
        'type': 'stock',
        'status': info['status'],
        'conviction': info['conviction'],
    })

# ─── Process each ticker ─────────────────────────────────────────────────────

for ticker, info in stocks.items():
    stock_nid = get_node_id(ticker, 'stock')
    data = ownership_data.get(ticker, {})

    # --- Institutional holders ---
    for h in data.get('holders', [])[:TOP_FUNDS]:
        fund_name = h.get('name', 'Unknown')
        pct_held = h.get('pct', 0)
        shares = h.get('shares', 0)
        value = h.get('value', 0)

        if fund_name not in fund_stock_count:
            fund_stock_count[fund_name] = set()
        fund_stock_count[fund_name].add(ticker)

        fund_nid = get_node_id(fund_name, 'fund')
        if not any(n['id'] == fund_nid for n in nodes):
            nodes.append({
                'id': fund_nid,
                'label': fund_name[:30],
                'name': fund_name,
                'type': 'fund',
                'status': 'active',
                'detail': '',
            })

        pct_display = f'{float(pct_held)*100:.1f}%' if pct_held and float(pct_held) < 1 else f'{float(pct_held):.1f}%' if pct_held else ''
        edges.append({
            'source': fund_nid,
            'target': stock_nid,
            'type': 'holds',
            'weight': float(pct_held) if pct_held else 0.01,
            'label': pct_display,
            'detail': f'{fund_name}: {pct_display} ({fmt_shares(shares)} shares, {fmt_value(value)})',
        })

    # --- Insider transactions: aggregate by person ---
    insiders_by_name = {}
    for ins in data.get('insiders', []):
        name = ins.get('name', 'Unknown')
        if name not in insiders_by_name:
            insiders_by_name[name] = {
                'title': ins.get('title', ''),
                'transactions': [],
                'total_buy_value': 0,
                'total_sell_value': 0,
                'total_buy_shares': 0,
                'total_sell_shares': 0,
                'buyback_value': 0,
                'buyback_shares': 0,
                'dates': [],
            }
        agg = insiders_by_name[name]
        txn = ins.get('type', 'OTHER')
        value = ins.get('value', 0) or 0
        shares = ins.get('shares', 0) or 0
        date = ins.get('date', '')
        text = ins.get('text', '')

        agg['transactions'].append({
            'type': txn, 'value': value, 'shares': shares,
            'date': date, 'text': text,
        })
        if date:
            agg['dates'].append(date)

        if txn == 'BUY':
            agg['total_buy_value'] += value
            agg['total_buy_shares'] += shares
        elif txn == 'SELL':
            agg['total_sell_value'] += value
            agg['total_sell_shares'] += shares
        elif txn == 'BUYBACK':
            agg['buyback_value'] += value
            agg['buyback_shares'] += shares

    # Create person nodes and aggregated edges
    for person_name, agg in insiders_by_name.items():
        txns = agg['transactions']
        title = agg['title']

        # Pattern detection
        sell_dates = sorted([t['date'] for t in txns if t['type'] == 'SELL' and t['date']])
        is_programmatic = False
        if len(sell_dates) >= 3:
            # Check if sells happen at regular intervals (10b5-1 pattern)
            sell_shares = [t['shares'] for t in txns if t['type'] == 'SELL']
            if sell_shares:
                avg_sh = sum(sell_shares) / len(sell_shares)
                variance = sum((s - avg_sh) ** 2 for s in sell_shares) / len(sell_shares)
                cv = (variance ** 0.5) / avg_sh if avg_sh > 0 else 999
                if cv < 0.3:  # Low variation in share counts = programmatic
                    is_programmatic = True

        pattern = 'Programmatic (10b5-1)' if is_programmatic else 'Discretionary'

        # Determine dominant action
        total_value = agg['total_buy_value'] + agg['total_sell_value'] + agg['buyback_value']
        if agg['buyback_value'] > agg['total_sell_value'] and agg['buyback_value'] > agg['total_buy_value']:
            dominant = 'buyback'
        elif agg['total_buy_value'] > agg['total_sell_value']:
            dominant = 'insider_buy'
        elif agg['total_sell_value'] > 0:
            dominant = 'insider_sell'
        else:
            dominant = 'other'

        # Short title for label
        title_short = ''
        tl = title.lower()
        if 'chief executive' in tl or 'ceo' in tl: title_short = 'CEO'
        elif 'chief financial' in tl or 'cfo' in tl: title_short = 'CFO'
        elif 'chief operating' in tl or 'coo' in tl: title_short = 'COO'
        elif 'chief technology' in tl or 'cto' in tl: title_short = 'CTO'
        elif 'director' in tl and 'officer' in tl: title_short = 'Dir/Off'
        elif 'director' in tl: title_short = 'Director'
        elif 'officer' in tl: title_short = 'Officer'
        elif 'vp' in tl or 'vice president' in tl: title_short = 'VP'
        elif 'general counsel' in tl: title_short = 'GC'
        elif 'beneficial' in tl: title_short = 'Owner'
        else: title_short = title[:12]

        # Build transaction detail HTML for tooltip
        txn_lines = []
        for t in sorted(txns, key=lambda x: x.get('date', ''), reverse=True)[:8]:
            type_emoji = {'BUY': '+', 'SELL': '-', 'BUYBACK': 'BB', 'OPTION': 'OPT'}.get(t['type'], '?')
            v_str = fmt_value(t['value']) if t['value'] else ''
            txn_lines.append(f"{t['date']} [{type_emoji}] {fmt_shares(t['shares'])} sh {v_str}")

        detail_text = (
            f"<b>{person_name}</b><br>"
            f"<i>{title}</i><br>"
            f"Pattern: <b>{pattern}</b><br>"
            f"---<br>"
        )
        if agg['total_buy_value'] > 0:
            detail_text += f"Buys: {fmt_shares(agg['total_buy_shares'])} sh ({fmt_value(agg['total_buy_value'])})<br>"
        if agg['total_sell_value'] > 0:
            detail_text += f"Sells: {fmt_shares(agg['total_sell_shares'])} sh ({fmt_value(agg['total_sell_value'])})<br>"
        if agg['buyback_value'] > 0:
            detail_text += f"Buybacks: {fmt_shares(agg['buyback_shares'])} sh ({fmt_value(agg['buyback_value'])})<br>"
        detail_text += f"---<br>{'<br>'.join(txn_lines)}"

        label = person_name.split(' ')[-1][:12]
        if title_short:
            label = f"{label} ({title_short})"

        person_nid = get_node_id(person_name + ':' + ticker, 'person')
        nodes.append({
            'id': person_nid,
            'label': label,
            'name': person_name,
            'type': 'person',
            'status': dominant,
            'title': title,
            'title_short': title_short,
            'pattern': pattern,
            'total_value': total_value,
            'detail': detail_text,
            'n_txns': len(txns),
        })

        # Single aggregated edge per person+stock
        edge_label = ''
        if agg['total_sell_value'] > 0:
            edge_label = f"-{fmt_value(agg['total_sell_value'])}"
        elif agg['total_buy_value'] > 0:
            edge_label = f"+{fmt_value(agg['total_buy_value'])}"
        elif agg['buyback_value'] > 0:
            edge_label = f"BB {fmt_value(agg['buyback_value'])}"

        edges.append({
            'source': person_nid,
            'target': stock_nid,
            'type': dominant,
            'weight': max(0.3, min(5, total_value / 500_000)) if total_value else 0.3,
            'label': edge_label,
            'detail': detail_text,
        })

# ─── Post-process: classify funds ────────────────────────────────────────────

n_stocks = len(stocks)
indexer_threshold = max(n_stocks * 0.6, 3)

for node in nodes:
    if node['type'] == 'fund':
        fund_name = node['name']
        n_held = len(fund_stock_count.get(fund_name, set()))
        if n_held >= indexer_threshold or is_indexer(fund_name):
            node['status'] = 'indexer'
        elif n_held >= 3:
            node['status'] = 'quality'
        else:
            node['status'] = 'active'

print(f"\nGraph: {len(nodes)} nodes, {len(edges)} edges")
print(f"  Stocks: {sum(1 for n in nodes if n['type'] == 'stock')}")
print(f"  Funds: {sum(1 for n in nodes if n['type'] == 'fund')} "
      f"(indexers: {sum(1 for n in nodes if n.get('status') == 'indexer')}, "
      f"quality: {sum(1 for n in nodes if n.get('status') == 'quality')})")
print(f"  People: {sum(1 for n in nodes if n['type'] == 'person')}")

# ─── Generate HTML ────────────────────────────────────────────────────────────

graph_data = json.dumps({'nodes': nodes, 'edges': edges}, indent=2)

html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Ownership Graph — Value Investor System</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body { background: #1a1a2e; color: #e0e0e0; font-family: 'Segoe UI', system-ui, sans-serif; overflow: hidden; }
  svg { width: 100vw; height: 100vh; display: block; }

  #legend {
    position: fixed; left: 16px; bottom: 16px;
    background: rgba(22, 22, 40, 0.92); border: 1px solid #333;
    border-radius: 8px; padding: 14px 18px; font-size: 11px;
    min-width: 200px; z-index: 10; backdrop-filter: blur(8px);
  }
  #legend h3 { font-size: 13px; margin-bottom: 8px; color: #fff; }
  .section { margin-bottom: 6px; }
  .section-title { font-weight: 600; color: #aaa; margin-bottom: 3px; font-size: 10px; text-transform: uppercase; letter-spacing: 0.5px; }
  .item { display: flex; align-items: center; gap: 6px; margin: 2px 0; }
  .dot { width: 10px; height: 10px; border-radius: 50%; display: inline-block; }
  .diamond { width: 9px; height: 9px; transform: rotate(45deg); display: inline-block; }
  .tri { width: 0; height: 0; border-left: 5px solid transparent; border-right: 5px solid transparent; border-bottom: 9px solid; display: inline-block; }
  .line { width: 18px; height: 0; display: inline-block; border-radius: 1px; }

  #tooltip {
    position: fixed; display: none; background: rgba(18, 18, 35, 0.96);
    border: 1px solid #555; border-radius: 8px; padding: 12px 16px;
    font-size: 11px; max-width: 350px; z-index: 20; pointer-events: none;
    backdrop-filter: blur(10px); line-height: 1.5;
  }
  #tooltip b { color: #fff; }
  #tooltip i { color: #8898b0; }

  #detail-panel {
    position: fixed; right: 0; top: 0; width: 340px; height: 100vh;
    background: rgba(18, 18, 35, 0.96); border-left: 1px solid #333;
    padding: 20px; overflow-y: auto; z-index: 15;
    transform: translateX(100%); transition: transform 0.25s ease;
    backdrop-filter: blur(10px);
  }
  #detail-panel.open { transform: translateX(0); }
  #detail-panel h3 { font-size: 14px; color: #fff; margin-bottom: 4px; }
  #detail-panel .subtitle { font-size: 11px; color: #8898b0; margin-bottom: 12px; }
  #detail-panel .close-btn { position: absolute; top: 12px; right: 16px; cursor: pointer; color: #888; font-size: 18px; }
  #detail-panel .close-btn:hover { color: #fff; }
  #detail-panel .detail-content { font-size: 11px; line-height: 1.6; }
  #detail-panel .detail-content b { color: #fff; }
  #detail-panel .txn-row { padding: 4px 0; border-bottom: 1px solid rgba(40,40,70,0.4); }
  .txn-buy { color: #50c060; } .txn-sell { color: #f06060; } .txn-bb { color: #40b0c0; } .txn-opt { color: #b0b060; }
  .pattern-tag { display: inline-block; padding: 2px 8px; border-radius: 3px; font-size: 10px; font-weight: 600; margin: 4px 0; }
  .pattern-prog { background: rgba(64,176,192,0.2); color: #40b0c0; }
  .pattern-disc { background: rgba(224,160,80,0.2); color: #e0a050; }

  #info {
    position: fixed; right: 16px; top: 16px;
    background: rgba(22, 22, 40, 0.92); border: 1px solid #333;
    border-radius: 8px; padding: 10px 14px; font-size: 11px; color: #888;
    z-index: 10;
  }
  #info span { color: #fff; font-weight: 600; }

  #controls {
    position: fixed; left: 16px; top: 16px;
    background: rgba(22, 22, 40, 0.92); border: 1px solid #333;
    border-radius: 8px; padding: 10px 14px; font-size: 11px;
    z-index: 10; display: flex; gap: 6px; flex-wrap: wrap; align-items: center;
  }
  #controls button {
    background: #2a2a4a; color: #e0e0e0; border: 1px solid #444;
    border-radius: 4px; padding: 3px 8px; cursor: pointer; font-size: 10px;
  }
  #controls button:hover { background: #3a3a5a; }
  #controls button.active { background: #4a6a8a; border-color: #6a9aca; }
  #controls label { color: #aaa; font-size: 10px; }
</style>
</head>
<body>

<div id="controls">
  <button onclick="toggleInsiders()" id="btn-insiders" class="active">Insiders</button>
  <button onclick="toggleIndexers()" id="btn-indexers">Indexers</button>
  <button onclick="toggleLabels()" id="btn-labels" class="active">Labels</button>
  <button onclick="resetView()">Reset</button>
  <label>Click node for detail panel. Hover for tooltip. Scroll=zoom. Drag=pan.</label>
</div>

<div id="info">
  <span id="n-nodes">0</span> nodes &middot; <span id="n-edges">0</span> edges
</div>

<div id="tooltip"></div>

<div id="detail-panel">
  <span class="close-btn" onclick="closePanel()">&times;</span>
  <div id="panel-content"></div>
</div>

<div id="legend">
  <h3>Legend</h3>
  <div class="section">
    <div class="section-title">Nodes</div>
    <div class="item"><span class="dot" style="background:#e8863a"></span> Portfolio stock</div>
    <div class="item"><span class="dot" style="background:#f0c040"></span> Standing order</div>
    <div class="item"><span class="diamond" style="background:#4caf50"></span> Quality fund (3+)</div>
    <div class="item"><span class="diamond" style="background:#607d8b"></span> Active fund</div>
    <div class="item"><span class="tri" style="border-bottom-color:#50c060"></span> Insider buyer</div>
    <div class="item"><span class="tri" style="border-bottom-color:#f06060"></span> Insider seller</div>
    <div class="item"><span class="tri" style="border-bottom-color:#40b0c0"></span> Buyback</div>
  </div>
  <div class="section">
    <div class="section-title">Edges (width = value)</div>
    <div class="item"><span class="line" style="border-top: 2px solid #4caf80"></span> Fund holds</div>
    <div class="item"><span class="line" style="border-top: 2px solid #c08040"></span> Personal buy</div>
    <div class="item"><span class="line" style="border-top: 2px solid #e06060"></span> Personal sell</div>
    <div class="item"><span class="line" style="border-top: 2px solid #40b0c0"></span> Buyback</div>
  </div>
</div>

<svg id="graph"></svg>

<script>
const DATA = """ + graph_data + """;

const W = window.innerWidth, H = window.innerHeight;
const svg = document.getElementById('graph');
svg.setAttribute('viewBox', `0 0 ${W} ${H}`);

const stockColors = {
  portfolio: '#e8863a', so_active: '#f0c040', so_gated: '#40b0a0',
  so_borderline: '#5080c0', so_extreme: '#3a5070', default: '#5080c0'
};
const fundColors = { quality: '#4caf50', active: '#607d8b', indexer: '#444' };
const edgeColors = { holds: '#4caf8060', insider_buy: '#c0804060', insider_sell: '#e0606060', buyback: '#40b0c060', other: '#55555540' };
const edgeColorsHi = { holds: '#4caf80', insider_buy: '#c08040', insider_sell: '#e06060', buyback: '#40b0c0', other: '#888' };
const personColors = { insider_buy: '#50c060', insider_sell: '#f06060', buyback: '#40b0c0', other: '#888' };

let showInsiders = true, showIndexers = false, showLabels = true, selectedNode = null;

const adjMap = {};
DATA.edges.forEach(e => {
  if (!adjMap[e.source]) adjMap[e.source] = [];
  if (!adjMap[e.target]) adjMap[e.target] = [];
  adjMap[e.source].push(e);
  adjMap[e.target].push(e);
});

function nodeSize(n) {
  if (n.type === 'stock') return n.status === 'portfolio' ? 14 : 8;
  if (n.type === 'fund') return Math.max(5, Math.min((adjMap[n.id] || []).length * 2.5, 14));
  if (n.type === 'person') {
    const v = n.total_value || 0;
    if (v >= 5_000_000) return 10;
    if (v >= 1_000_000) return 7;
    if (v >= 100_000) return 5;
    return 4;
  }
  return 4;
}

function nodeColor(n) {
  if (n.type === 'stock') return stockColors[n.status] || stockColors.default;
  if (n.type === 'fund') return fundColors[n.status] || fundColors.active;
  if (n.type === 'person') return personColors[n.status] || '#888';
  return '#888';
}

function isVisible(n) {
  if (n.type === 'person' && !showInsiders) return false;
  if (n.type === 'fund' && n.status === 'indexer' && !showIndexers) return false;
  return true;
}

function edgeVisible(e) {
  const sn = nodeMap[e.source], tn = nodeMap[e.target];
  return sn && tn && isVisible(sn) && isVisible(tn);
}

// Initialize positions
const nodes = DATA.nodes.map(n => ({
  ...n, x: W/2 + (Math.random()-0.5)*W*0.6, y: H/2 + (Math.random()-0.5)*H*0.6,
  vx: 0, vy: 0, size: nodeSize(n),
}));
const nodeMap = {};
nodes.forEach(n => nodeMap[n.id] = n);

function simulate(iterations) {
  const repulsion = 900, attraction = 0.007, centerForce = 0.002, damping = 0.85;
  for (let iter = 0; iter < iterations; iter++) {
    const decay = 1 - iter / iterations;
    const vis = nodes.filter(isVisible);
    for (let i = 0; i < vis.length; i++) {
      for (let j = i + 1; j < vis.length; j++) {
        const a = vis[i], b = vis[j];
        let dx = b.x - a.x, dy = b.y - a.y;
        let dist = Math.sqrt(dx*dx + dy*dy) || 1;
        let force = repulsion * decay / (dist * dist);
        let fx = dx/dist*force, fy = dy/dist*force;
        a.vx -= fx; a.vy -= fy; b.vx += fx; b.vy += fy;
      }
    }
    DATA.edges.forEach(e => {
      if (!edgeVisible(e)) return;
      const a = nodeMap[e.source], b = nodeMap[e.target];
      if (!a || !b) return;
      let dx = b.x - a.x, dy = b.y - a.y;
      let dist = Math.sqrt(dx*dx + dy*dy) || 1;
      let force = dist * attraction * decay;
      a.vx += dx/dist*force; a.vy += dy/dist*force;
      b.vx -= dx/dist*force; b.vy -= dy/dist*force;
    });
    vis.forEach(n => {
      n.vx += (W/2 - n.x) * centerForce * decay;
      n.vy += (H/2 - n.y) * centerForce * decay;
      n.vx *= damping; n.vy *= damping;
      n.x += n.vx; n.y += n.vy;
      n.x = Math.max(30, Math.min(W-30, n.x));
      n.y = Math.max(30, Math.min(H-30, n.y));
    });
  }
}

simulate(300);

let transform = { x: 0, y: 0, k: 1 };

function render() {
  const els = [];

  // Edges
  DATA.edges.forEach(e => {
    if (!edgeVisible(e)) return;
    const a = nodeMap[e.source], b = nodeMap[e.target];
    if (!a || !b) return;
    const hi = selectedNode !== null && (e.source === selectedNode || e.target === selectedNode);
    const color = hi ? (edgeColorsHi[e.type] || '#888') : (edgeColors[e.type] || '#55555530');
    const width = hi ? Math.max(1.5, (e.weight || 0.5) * 1.2) : Math.max(0.4, (e.weight || 0.5) * 0.6);
    const opacity = selectedNode !== null ? (hi ? 1 : 0.06) : 0.5;
    els.push(`<line x1="${a.x}" y1="${a.y}" x2="${b.x}" y2="${b.y}" stroke="${color}" stroke-width="${width}" opacity="${opacity}"/>`);

    // Edge label (only when highlighted)
    if (hi && showLabels && e.label) {
      const mx = (a.x + b.x) / 2, my = (a.y + b.y) / 2;
      els.push(`<text x="${mx}" y="${my-3}" text-anchor="middle" fill="#ddd" font-size="8" font-weight="600">${e.label}</text>`);
    }
  });

  // Nodes
  nodes.forEach(n => {
    if (!isVisible(n)) return;
    const hi = selectedNode === null || selectedNode === n.id ||
               (adjMap[selectedNode] || []).some(e => e.source === n.id || e.target === n.id);
    const opacity = hi ? 1 : 0.1;
    const color = nodeColor(n);
    const s = n.size;

    if (n.type === 'stock') {
      els.push(`<circle cx="${n.x}" cy="${n.y}" r="${s}" fill="${color}" opacity="${opacity}" stroke="${selectedNode === n.id ? '#fff' : 'none'}" stroke-width="2" data-id="${n.id}" class="node"/>`);
      if (s >= 7 && showLabels && (selectedNode === null || hi)) {
        els.push(`<text x="${n.x}" y="${n.y - s - 3}" text-anchor="middle" fill="${hi ? '#fff' : '#aaa'}" font-size="${s >= 12 ? 11 : 9}" opacity="${opacity}" font-weight="600">${n.label}</text>`);
      }
    } else if (n.type === 'fund') {
      const d = s;
      els.push(`<polygon points="${n.x},${n.y-d} ${n.x+d},${n.y} ${n.x},${n.y+d} ${n.x-d},${n.y}" fill="${color}" opacity="${opacity}" stroke="${selectedNode === n.id ? '#fff' : 'none'}" stroke-width="1.5" data-id="${n.id}" class="node"/>`);
      if (hi && showLabels && selectedNode !== null) {
        els.push(`<text x="${n.x}" y="${n.y - d - 3}" text-anchor="middle" fill="#ccc" font-size="8">${n.label}</text>`);
      }
    } else if (n.type === 'person') {
      const d = s + 1;
      els.push(`<polygon points="${n.x},${n.y-d} ${n.x+d},${n.y+d} ${n.x-d},${n.y+d}" fill="${color}" opacity="${opacity}" data-id="${n.id}" class="node" stroke="${selectedNode === n.id ? '#fff' : 'none'}" stroke-width="1.5"/>`);
      if (showLabels && (selectedNode === null || hi) && s >= 5) {
        els.push(`<text x="${n.x}" y="${n.y + d + 10}" text-anchor="middle" fill="${hi ? '#ccc' : '#666'}" font-size="8" opacity="${opacity}">${n.label}</text>`);
      }
    }
  });

  svg.innerHTML = `<g transform="translate(${transform.x},${transform.y}) scale(${transform.k})">${els.join('')}</g>`;
  document.getElementById('n-nodes').textContent = nodes.filter(isVisible).length;
  document.getElementById('n-edges').textContent = DATA.edges.filter(edgeVisible).length;
}

render();

// Click -> detail panel
svg.addEventListener('click', (e) => {
  const el = e.target.closest('.node');
  if (el) {
    const id = parseInt(el.dataset.id);
    selectedNode = selectedNode === id ? null : id;
    if (selectedNode !== null) showDetailPanel(selectedNode);
    else closePanel();
  } else {
    selectedNode = null;
    closePanel();
  }
  render();
});

function showDetailPanel(nodeId) {
  const n = nodeMap[nodeId];
  if (!n) return;
  const panel = document.getElementById('detail-panel');
  const content = document.getElementById('panel-content');

  let html = `<h3>${n.name}</h3>`;

  if (n.type === 'stock') {
    html += `<div class="subtitle">${n.status.toUpperCase()} | Conviction: ${n.conviction || 'n/a'}</div>`;
    // Show all connected insiders and funds
    const conns = adjMap[nodeId] || [];
    const funds = conns.filter(e => nodeMap[e.source]?.type === 'fund');
    const people = conns.filter(e => nodeMap[e.source]?.type === 'person');

    if (funds.length) {
      html += `<div class="detail-content"><b>Institutional Holders (${funds.length})</b><br>`;
      funds.forEach(e => {
        const fn = nodeMap[e.source];
        html += `<div class="txn-row">${fn?.name || '?'}: ${e.label}</div>`;
      });
      html += '</div><br>';
    }
    if (people.length) {
      html += `<div class="detail-content"><b>Insiders (${people.length})</b><br>`;
      people.forEach(e => {
        const pn = nodeMap[e.source];
        if (pn?.detail) html += `<div class="txn-row">${pn.detail}</div>`;
      });
      html += '</div>';
    }
  } else if (n.type === 'person') {
    html += `<div class="subtitle">${n.title || ''}</div>`;
    const patCls = n.pattern?.includes('10b5-1') ? 'pattern-prog' : 'pattern-disc';
    html += `<span class="pattern-tag ${patCls}">${n.pattern || 'Unknown'}</span>`;
    if (n.detail) html += `<div class="detail-content" style="margin-top:8px">${n.detail}</div>`;
  } else if (n.type === 'fund') {
    html += `<div class="subtitle">${n.status?.toUpperCase() || ''}</div>`;
    const conns = adjMap[nodeId] || [];
    html += `<div class="detail-content"><b>Holds ${conns.length} of our stocks:</b><br>`;
    conns.forEach(e => {
      const sn = nodeMap[e.target];
      html += `<div class="txn-row">${sn?.label || '?'}: ${e.label}</div>`;
    });
    html += '</div>';
  }

  content.innerHTML = html;
  panel.classList.add('open');
}

function closePanel() {
  document.getElementById('detail-panel').classList.remove('open');
}

// Tooltip on hover
const tooltip = document.getElementById('tooltip');
svg.addEventListener('mousemove', (e) => {
  const el = e.target.closest('.node');
  if (el) {
    const id = parseInt(el.dataset.id);
    const n = nodeMap[id];
    if (n) {
      let html = '';
      if (n.type === 'person') {
        html = n.detail || `<b>${n.name}</b>`;
      } else if (n.type === 'fund') {
        const conns = (adjMap[n.id] || []).length;
        html = `<b>${n.name}</b><br><i>${n.status}</i><br>Holds ${conns} of our stocks`;
      } else {
        const conns = (adjMap[n.id] || []).length;
        html = `<b>${n.label}</b> — ${n.name}<br><i>${n.status}</i> | ${n.conviction || ''}<br>${conns} connections`;
      }
      tooltip.innerHTML = html;
      tooltip.style.display = 'block';
      tooltip.style.left = (e.clientX + 14) + 'px';
      tooltip.style.top = (e.clientY - 10) + 'px';
    }
  } else {
    tooltip.style.display = 'none';
  }
});

// Zoom
svg.addEventListener('wheel', (e) => {
  e.preventDefault();
  const scale = e.deltaY > 0 ? 0.9 : 1.1;
  const rect = svg.getBoundingClientRect();
  const mx = e.clientX - rect.left, my = e.clientY - rect.top;
  transform.k *= scale;
  transform.x = mx - (mx - transform.x) * scale;
  transform.y = my - (my - transform.y) * scale;
  render();
}, { passive: false });

// Pan
let dragging = false, lastX, lastY;
svg.addEventListener('mousedown', (e) => {
  if (e.target.closest('.node')) return;
  dragging = true; lastX = e.clientX; lastY = e.clientY;
});
window.addEventListener('mousemove', (e) => {
  if (!dragging) return;
  transform.x += e.clientX - lastX; transform.y += e.clientY - lastY;
  lastX = e.clientX; lastY = e.clientY;
  render();
});
window.addEventListener('mouseup', () => { dragging = false; });

function toggleInsiders() {
  showInsiders = !showInsiders;
  document.getElementById('btn-insiders').classList.toggle('active', showInsiders);
  simulate(50); render();
}
function toggleIndexers() {
  showIndexers = !showIndexers;
  document.getElementById('btn-indexers').classList.toggle('active', showIndexers);
  simulate(50); render();
}
function toggleLabels() {
  showLabels = !showLabels;
  document.getElementById('btn-labels').classList.toggle('active', showLabels);
  render();
}
function resetView() {
  transform = { x: 0, y: 0, k: 1 };
  selectedNode = null; closePanel(); render();
}
</script>
</body>
</html>"""

with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\nOwnership graph v2.0 saved: {OUTPUT}")
print("Open in browser to interact.")
