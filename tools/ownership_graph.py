#!/usr/bin/env python3
"""
Ownership Graph — Interactive force-directed network visualization.

Builds a bipartite graph: Stocks <-> Funds/Insiders
Data from yfinance (institutional_holders + insider_transactions).

Nodes:
  - Stocks (circles): colored by status (portfolio/SO active/SO gated/universe)
  - Funds (diamonds): colored by type (indexer filtered, active highlighted)
  - People (triangles): insiders with recent transactions

Edges:
  - Holds (green): fund holds stock
  - Insider buy (brown): insider purchased shares
  - Insider sell (salmon): insider sold shares

Output: docs/ownership_graph.html (standalone, opens in browser)

Usage:
    python3 tools/ownership_graph.py
    python3 tools/ownership_graph.py --portfolio-only    # skip SOs
    python3 tools/ownership_graph.py --top-funds 5       # top N funds per stock
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

# Args
PORTFOLIO_ONLY = '--portfolio-only' in sys.argv
USE_CACHE = '--cached' in sys.argv
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

# Build stock list with status
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

# ─── Fetch ownership data (via shared cache) ─────────────────────────────────

nodes = []
edges = []
fund_stock_count = {}  # fund_name -> set of stocks it holds (for indexer detection)

# Track node IDs
node_ids = {}
node_counter = [0]

def get_node_id(name, node_type):
    key = f"{node_type}:{name}"
    if key not in node_ids:
        node_ids[key] = node_counter[0]
        node_counter[0] += 1
    return node_ids[key]

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

# Load ownership data via shared cache
all_tickers = list(stocks.keys())
ownership_data = load_or_fetch(all_tickers, force_fresh=FORCE_FRESH, top_funds=TOP_FUNDS)

# Build graph from cached data
for ticker, info in stocks.items():
    stock_nid = get_node_id(ticker, 'stock')
    data = ownership_data.get(ticker, {})

    # --- Institutional holders ---
    for h in data.get('holders', [])[:TOP_FUNDS]:
        fund_name = h.get('name', 'Unknown')
        pct_held = h.get('pct', 0)

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
            })

        edges.append({
            'source': fund_nid,
            'target': stock_nid,
            'type': 'holds',
            'weight': float(pct_held) if pct_held else 0.01,
            'label': f'{float(pct_held)*100:.1f}%' if pct_held and float(pct_held) < 1 else f'{float(pct_held):.1f}%' if pct_held else '',
        })

    # --- Insider transactions ---
    for ins in data.get('insiders', [])[:10]:
        insider_name = ins.get('name', 'Unknown')
        txn_type_raw = ins.get('type', 'SELL')
        text = ins.get('text', '')

        if txn_type_raw in ('BUY', 'BUYBACK'):
            txn_type = 'insider_buy'
        else:
            txn_type = 'insider_sell'

        person_nid = get_node_id(insider_name, 'person')
        if not any(n['id'] == person_nid for n in nodes):
            nodes.append({
                'id': person_nid,
                'label': insider_name.split(' ')[-1][:15],
                'name': insider_name,
                'type': 'person',
                'status': txn_type,
            })

        edges.append({
            'source': person_nid,
            'target': stock_nid,
            'type': txn_type,
            'weight': 0.5,
            'label': text[:40] if text else '',
        })

# ─── Post-process: classify funds as indexer vs active ────────────────────────

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

# ─── Deduplicate edges ────────────────────────────────────────────────────────

seen_edges = set()
deduped_edges = []
for e in edges:
    key = (e['source'], e['target'], e['type'])
    if key not in seen_edges:
        seen_edges.add(key)
        deduped_edges.append(e)
edges = deduped_edges

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
    border-radius: 8px; padding: 16px 20px; font-size: 12px;
    min-width: 190px; z-index: 10; backdrop-filter: blur(8px);
  }
  #legend h3 { font-size: 14px; margin-bottom: 10px; color: #fff; }
  #legend .section { margin-bottom: 8px; }
  #legend .section-title { font-weight: 600; color: #aaa; margin-bottom: 4px; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; }
  #legend .item { display: flex; align-items: center; gap: 8px; margin: 3px 0; }
  #legend .dot { width: 10px; height: 10px; border-radius: 50%; display: inline-block; }
  #legend .diamond { width: 10px; height: 10px; transform: rotate(45deg); display: inline-block; }
  #legend .triangle { width: 0; height: 0; border-left: 5px solid transparent; border-right: 5px solid transparent; border-bottom: 10px solid; display: inline-block; }
  #legend .line { width: 20px; height: 2px; display: inline-block; border-radius: 1px; }

  #tooltip {
    position: fixed; display: none; background: rgba(22, 22, 40, 0.95);
    border: 1px solid #555; border-radius: 6px; padding: 10px 14px;
    font-size: 12px; max-width: 300px; z-index: 20; pointer-events: none;
    backdrop-filter: blur(8px);
  }
  #tooltip .tt-title { font-weight: 600; font-size: 13px; color: #fff; margin-bottom: 4px; }
  #tooltip .tt-type { color: #888; font-size: 11px; }
  #tooltip .tt-detail { margin-top: 4px; color: #ccc; }

  #info {
    position: fixed; right: 16px; top: 16px;
    background: rgba(22, 22, 40, 0.92); border: 1px solid #333;
    border-radius: 8px; padding: 12px 16px; font-size: 11px; color: #888;
    z-index: 10;
  }
  #info span { color: #fff; font-weight: 600; }

  #controls {
    position: fixed; left: 16px; top: 16px;
    background: rgba(22, 22, 40, 0.92); border: 1px solid #333;
    border-radius: 8px; padding: 12px 16px; font-size: 12px;
    z-index: 10; display: flex; gap: 8px; flex-wrap: wrap; align-items: center;
  }
  #controls button {
    background: #2a2a4a; color: #e0e0e0; border: 1px solid #444;
    border-radius: 4px; padding: 4px 10px; cursor: pointer; font-size: 11px;
  }
  #controls button:hover { background: #3a3a5a; }
  #controls button.active { background: #4a6a8a; border-color: #6a9aca; }
  #controls label { color: #aaa; font-size: 11px; }
</style>
</head>
<body>

<div id="controls">
  <button onclick="toggleInsiders()" id="btn-insiders" class="active">Insiders</button>
  <button onclick="toggleIndexers()" id="btn-indexers">Indexers</button>
  <button onclick="resetView()">Reset</button>
  <label>Click node to highlight. Scroll to zoom. Drag to pan.</label>
</div>

<div id="info">
  <span id="n-nodes">0</span> nodes &middot; <span id="n-edges">0</span> edges
</div>

<div id="tooltip"></div>

<div id="legend">
  <h3>Legend</h3>
  <div class="section">
    <div class="section-title">Node Shapes</div>
    <div class="item"><span class="dot" style="background:#6ca0dc"></span> Stock</div>
    <div class="item"><span class="diamond" style="background:#4caf50"></span> Fund</div>
    <div class="item"><span class="triangle" style="border-bottom-color:#e0a060"></span> Person</div>
  </div>
  <div class="section">
    <div class="section-title">Stock Colors</div>
    <div class="item"><span class="dot" style="background:#e8863a"></span> Portfolio</div>
    <div class="item"><span class="dot" style="background:#f0c040"></span> SO Active</div>
    <div class="item"><span class="dot" style="background:#40b0a0"></span> SO Gated</div>
    <div class="item"><span class="dot" style="background:#5080c0"></span> Other</div>
  </div>
  <div class="section">
    <div class="section-title">Fund Colors</div>
    <div class="item"><span class="diamond" style="background:#4caf50"></span> Quality (3+ stocks)</div>
    <div class="item"><span class="diamond" style="background:#607d8b"></span> Active</div>
    <div class="item"><span class="diamond" style="background:#444"></span> Indexer</div>
  </div>
  <div class="section">
    <div class="section-title">Edge Colors</div>
    <div class="item"><span class="line" style="background:#4caf80"></span> Holds</div>
    <div class="item"><span class="line" style="background:#c08040"></span> Insider buy</div>
    <div class="item"><span class="line" style="background:#e06060"></span> Insider sell</div>
  </div>
</div>

<svg id="graph"></svg>

<script>
const DATA = """ + graph_data + """;

const W = window.innerWidth, H = window.innerHeight;
const svg = document.getElementById('graph');
svg.setAttribute('viewBox', `0 0 ${W} ${H}`);

// Colors
const stockColors = {
  portfolio: '#e8863a', so_active: '#f0c040', so_gated: '#40b0a0',
  so_borderline: '#5080c0', so_extreme: '#3a5070', default: '#5080c0'
};
const fundColors = { quality: '#4caf50', active: '#607d8b', indexer: '#444' };
const edgeColors = { holds: '#4caf8080', insider_buy: '#c0804080', insider_sell: '#e0606080' };
const edgeColorsHi = { holds: '#4caf80', insider_buy: '#c08040', insider_sell: '#e06060' };

// State
let showInsiders = true;
let showIndexers = false;
let selectedNode = null;

// Build adjacency
const adjMap = {};
DATA.edges.forEach(e => {
  if (!adjMap[e.source]) adjMap[e.source] = [];
  if (!adjMap[e.target]) adjMap[e.target] = [];
  adjMap[e.source].push(e);
  adjMap[e.target].push(e);
});

// Node size
function nodeSize(n) {
  if (n.type === 'stock') {
    if (n.status === 'portfolio') return 12;
    if (n.status.startsWith('so_active')) return 9;
    return 7;
  }
  if (n.type === 'fund') {
    const conns = (adjMap[n.id] || []).length;
    return Math.max(4, Math.min(conns * 2.5, 14));
  }
  return 4;
}

function nodeColor(n) {
  if (n.type === 'stock') return stockColors[n.status] || stockColors.default;
  if (n.type === 'fund') return fundColors[n.status] || fundColors.active;
  if (n.type === 'person') return n.status === 'insider_buy' ? '#c08040' : '#e06060';
  return '#888';
}

function isVisible(n) {
  if (n.type === 'person' && !showInsiders) return false;
  if (n.type === 'fund' && n.status === 'indexer' && !showIndexers) return false;
  return true;
}

function edgeVisible(e) {
  const sn = DATA.nodes.find(n => n.id === e.source);
  const tn = DATA.nodes.find(n => n.id === e.target);
  if (!sn || !tn) return false;
  return isVisible(sn) && isVisible(tn);
}

// Simple force simulation
const nodes = DATA.nodes.map(n => ({
  ...n,
  x: W/2 + (Math.random() - 0.5) * W * 0.6,
  y: H/2 + (Math.random() - 0.5) * H * 0.6,
  vx: 0, vy: 0,
  size: nodeSize(n),
}));

const nodeMap = {};
nodes.forEach(n => nodeMap[n.id] = n);

// Force simulation
function simulate(iterations) {
  const alpha = 0.3;
  const repulsion = 800;
  const attraction = 0.008;
  const centerForce = 0.002;
  const damping = 0.85;

  for (let iter = 0; iter < iterations; iter++) {
    const decay = 1 - iter / iterations;

    // Repulsion (all pairs — use spatial hashing for perf)
    const visibleNodes = nodes.filter(n => isVisible(n));
    for (let i = 0; i < visibleNodes.length; i++) {
      for (let j = i + 1; j < visibleNodes.length; j++) {
        const a = visibleNodes[i], b = visibleNodes[j];
        let dx = b.x - a.x, dy = b.y - a.y;
        let dist = Math.sqrt(dx*dx + dy*dy) || 1;
        let force = repulsion * decay / (dist * dist);
        let fx = dx / dist * force, fy = dy / dist * force;
        a.vx -= fx; a.vy -= fy;
        b.vx += fx; b.vy += fy;
      }
    }

    // Attraction (edges)
    DATA.edges.forEach(e => {
      if (!edgeVisible(e)) return;
      const a = nodeMap[e.source], b = nodeMap[e.target];
      if (!a || !b) return;
      let dx = b.x - a.x, dy = b.y - a.y;
      let dist = Math.sqrt(dx*dx + dy*dy) || 1;
      let force = dist * attraction * decay;
      let fx = dx / dist * force, fy = dy / dist * force;
      a.vx += fx; a.vy += fy;
      b.vx -= fx; b.vy -= fy;
    });

    // Center gravity
    visibleNodes.forEach(n => {
      n.vx += (W/2 - n.x) * centerForce * decay;
      n.vy += (H/2 - n.y) * centerForce * decay;
    });

    // Apply velocities
    visibleNodes.forEach(n => {
      n.vx *= damping;
      n.vy *= damping;
      n.x += n.vx;
      n.y += n.vy;
      // Bounds
      n.x = Math.max(30, Math.min(W - 30, n.x));
      n.y = Math.max(30, Math.min(H - 30, n.y));
    });
  }
}

// Run simulation
console.time('simulation');
simulate(300);
console.timeEnd('simulation');

// Render
let transform = { x: 0, y: 0, k: 1 };

function render() {
  const els = [];

  // Edges
  DATA.edges.forEach(e => {
    if (!edgeVisible(e)) return;
    const a = nodeMap[e.source], b = nodeMap[e.target];
    if (!a || !b) return;

    const hi = selectedNode !== null && (e.source === selectedNode || e.target === selectedNode);
    const color = hi ? (edgeColorsHi[e.type] || '#888') : (edgeColors[e.type] || '#88888840');
    const width = hi ? 1.8 : 0.6;
    const opacity = selectedNode !== null ? (hi ? 1 : 0.08) : 0.5;

    els.push(`<line x1="${a.x}" y1="${a.y}" x2="${b.x}" y2="${b.y}" stroke="${color}" stroke-width="${width}" opacity="${opacity}"/>`);
  });

  // Nodes
  nodes.forEach(n => {
    if (!isVisible(n)) return;

    const hi = selectedNode === null || selectedNode === n.id ||
               (adjMap[selectedNode] || []).some(e => e.source === n.id || e.target === n.id);
    const opacity = hi ? 1 : 0.12;
    const color = nodeColor(n);
    const s = n.size;

    if (n.type === 'stock') {
      els.push(`<circle cx="${n.x}" cy="${n.y}" r="${s}" fill="${color}" opacity="${opacity}" stroke="${hi && selectedNode === n.id ? '#fff' : 'none'}" stroke-width="2" data-id="${n.id}" class="node"/>`);
      // Label
      if (s >= 7 && (selectedNode === null || hi)) {
        els.push(`<text x="${n.x}" y="${n.y - s - 3}" text-anchor="middle" fill="${hi ? '#fff' : '#aaa'}" font-size="${s >= 10 ? 11 : 9}" opacity="${opacity}" font-weight="${n.status === 'portfolio' ? 600 : 400}">${n.label}</text>`);
      }
    } else if (n.type === 'fund') {
      // Diamond
      const d = s;
      els.push(`<polygon points="${n.x},${n.y-d} ${n.x+d},${n.y} ${n.x},${n.y+d} ${n.x-d},${n.y}" fill="${color}" opacity="${opacity}" stroke="${hi && selectedNode === n.id ? '#fff' : 'none'}" stroke-width="1.5" data-id="${n.id}" class="node"/>`);
      if (hi && selectedNode !== null && (selectedNode === n.id || (adjMap[selectedNode] || []).some(e => e.source === n.id || e.target === n.id))) {
        els.push(`<text x="${n.x}" y="${n.y - d - 3}" text-anchor="middle" fill="#ccc" font-size="8" opacity="${opacity}">${n.label}</text>`);
      }
    } else if (n.type === 'person') {
      // Triangle
      const d = s + 1;
      els.push(`<polygon points="${n.x},${n.y-d} ${n.x+d},${n.y+d} ${n.x-d},${n.y+d}" fill="${color}" opacity="${opacity}" data-id="${n.id}" class="node"/>`);
    }
  });

  svg.innerHTML = `<g transform="translate(${transform.x},${transform.y}) scale(${transform.k})">${els.join('')}</g>`;

  // Info
  const visN = nodes.filter(isVisible).length;
  const visE = DATA.edges.filter(edgeVisible).length;
  document.getElementById('n-nodes').textContent = visN;
  document.getElementById('n-edges').textContent = visE;
}

render();

// Interaction: click to highlight
svg.addEventListener('click', (e) => {
  const el = e.target.closest('.node');
  if (el) {
    const id = parseInt(el.dataset.id);
    selectedNode = selectedNode === id ? null : id;
  } else {
    selectedNode = null;
  }
  render();
});

// Tooltip
const tooltip = document.getElementById('tooltip');
svg.addEventListener('mousemove', (e) => {
  const el = e.target.closest('.node');
  if (el) {
    const id = parseInt(el.dataset.id);
    const n = nodeMap[id];
    if (n) {
      const conns = (adjMap[n.id] || []).length;
      let detail = '';
      if (n.type === 'stock') detail = `Status: ${n.status} | Conviction: ${n.conviction || 'n/a'} | Connections: ${conns}`;
      else if (n.type === 'fund') detail = `Holds ${conns} of our stocks | Type: ${n.status}`;
      else detail = `${n.status === 'insider_buy' ? 'Buyer' : 'Seller'} | Connections: ${conns}`;

      tooltip.innerHTML = `<div class="tt-title">${n.name}</div><div class="tt-type">${n.type}</div><div class="tt-detail">${detail}</div>`;
      tooltip.style.display = 'block';
      tooltip.style.left = (e.clientX + 12) + 'px';
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
  transform.x += e.clientX - lastX;
  transform.y += e.clientY - lastY;
  lastX = e.clientX; lastY = e.clientY;
  render();
});
window.addEventListener('mouseup', () => { dragging = false; });

// Controls
function toggleInsiders() {
  showInsiders = !showInsiders;
  document.getElementById('btn-insiders').classList.toggle('active', showInsiders);
  simulate(50);
  render();
}
function toggleIndexers() {
  showIndexers = !showIndexers;
  document.getElementById('btn-indexers').classList.toggle('active', showIndexers);
  simulate(50);
  render();
}
function resetView() {
  transform = { x: 0, y: 0, k: 1 };
  selectedNode = null;
  render();
}
</script>
</body>
</html>"""

with open(OUTPUT, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\nOwnership graph saved: {OUTPUT}")
print("Open in browser to interact.")
