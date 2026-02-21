#!/usr/bin/env python3
"""
Portfolio Dashboard — Visual overview of the fund's current state.

Reads LIVE data from:
  - portfolio/current.yaml (positions, cash)
  - state/standing_orders.yaml (SOs with triggers)
  - state/quality_universe.yaml (pipeline stages, QS)
  - state/pipeline_tracker.yaml (operational metadata)

Generates: docs/portfolio_dashboard.png (6-panel dashboard)

Usage:
    python3 tools/portfolio_dashboard.py
    python3 tools/portfolio_dashboard.py --no-prices   # skip yfinance, use invested_usd as proxy
"""

import sys
import os
import re
import yaml
import numpy as np

# Paths
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORTFOLIO = os.path.join(BASE, 'portfolio', 'current.yaml')
SOS = os.path.join(BASE, 'state', 'standing_orders.yaml')
UNIVERSE = os.path.join(BASE, 'state', 'quality_universe.yaml')
OUTPUT = os.path.join(BASE, 'docs', 'portfolio_dashboard.png')

# ─── Args ─────────────────────────────────────────────────────────────────────
USE_PRICES = '--no-prices' not in sys.argv

# ─── Sector & Geography Maps ──────────────────────────────────────────────────
SECTOR_MAP = {
    'ADBE': 'Technology', 'BYIT.L': 'Technology', 'MORN': 'Financial Data',
    'NVO': 'Healthcare', 'GL': 'Insurance', 'MONY.L': 'Digital Marketplaces',
    'AUTO.L': 'Digital Marketplaces', 'EDEN.PA': 'Business Services',
    'DTE.DE': 'Telecom', 'DOM.L': 'Consumer Staples', 'LULU': 'Consumer Discretionary',
}

GEO_MAP = {
    'ADBE': 'US', 'GL': 'US', 'NVO': 'EU', 'LULU': 'US', 'MORN': 'US',
    'EDEN.PA': 'EU', 'DTE.DE': 'EU', 'DOM.L': 'UK', 'MONY.L': 'UK',
    'AUTO.L': 'UK', 'BYIT.L': 'UK',
}

CONVICTION_COLORS = {'high': '#1B5E20', 'medium': '#1565C0', 'low': '#E65100'}
TIER_COLORS = {'A': '#2E7D32', 'B': '#1565C0', 'C': '#E65100', 'D': '#B71C1C'}

# ─── Helpers ──────────────────────────────────────────────────────────────────

def load_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def extract_number(text, prefix='', suffix=''):
    """Extract first number from a string like 'EUR 35.00' or '$191' or '240 GBp'."""
    if not text:
        return None
    # Remove commas
    text = str(text).replace(',', '')
    # Try to find number
    patterns = [
        r'[\$€£]?\s*([\d.]+)',
        r'([\d.]+)\s*(?:GBp|p|EUR|USD|\$)',
    ]
    for pat in patterns:
        m = re.search(pat, text)
        if m:
            try:
                return float(m.group(1))
            except ValueError:
                continue
    return None


def extract_qs_tier(fv_str):
    """Extract QS and Tier from fair_value string like '$390 (FTC-adjusted, was $394. QS Tool 76, Adj 73)'."""
    qs_tool = qs_adj = None
    tier = None
    if not fv_str:
        return qs_tool, qs_adj, tier
    m = re.search(r'QS\s*(?:Tool)?\s*(\d+)', str(fv_str))
    if m:
        qs_tool = int(m.group(1))
    m = re.search(r'Adj\s*(\d+)', str(fv_str))
    if m:
        qs_adj = int(m.group(1))
    m = re.search(r'Tier\s*([ABCD])', str(fv_str))
    if m:
        tier = m.group(1)
    return qs_tool, qs_adj, tier


def get_fx_rates():
    """Get EUR/USD and GBP/EUR rates."""
    if not USE_PRICES:
        return 1.05, 1.20  # fallback
    try:
        import yfinance as yf
        eurusd = yf.Ticker('EURUSD=X').fast_info.get('lastPrice', 1.05)
        gbpeur = yf.Ticker('GBPEUR=X').fast_info.get('lastPrice', 1.20)
        return eurusd, gbpeur
    except Exception:
        return 1.05, 1.20


def get_price(ticker):
    """Get current price for a ticker."""
    if not USE_PRICES:
        return None
    try:
        import yfinance as yf
        info = yf.Ticker(ticker).fast_info
        return info.get('lastPrice', None)
    except Exception:
        return None


def parse_trigger_price(trigger_str):
    """Parse trigger string like '<=EUR 295' or '<=950 GBp' or '<=$88'."""
    if not trigger_str:
        return None, None
    text = str(trigger_str).replace(',', '')
    currency = 'USD'
    if 'EUR' in text:
        currency = 'EUR'
    elif 'GBp' in text or 'GBp' in text.lower():
        currency = 'GBp'
    elif 'CHF' in text:
        currency = 'CHF'
    m = re.search(r'([\d.]+)', text)
    if m:
        return float(m.group(1)), currency
    return None, None


# ─── Load Data ────────────────────────────────────────────────────────────────

print("Loading data...")
portfolio = load_yaml(PORTFOLIO)
so_data = load_yaml(SOS)
universe = load_yaml(UNIVERSE)

positions = portfolio.get('positions', [])
cash_eur = portfolio.get('cash', {}).get('amount', 0)
standing_orders = so_data.get('standing_orders', [])
companies = universe.get('quality_universe', {}).get('companies', [])

# ─── FX ───────────────────────────────────────────────────────────────────────
print("Fetching FX rates...")
eurusd, gbpeur = get_fx_rates()

# ─── Build Position Data ──────────────────────────────────────────────────────

print("Building position data...")
pos_list = []
for p in positions:
    ticker = p['ticker']
    invested_usd = p.get('invested_usd', 0)
    invested_eur = invested_usd / eurusd
    shares = p.get('shares', 0)
    conviction = p.get('conviction', 'low')
    fv_str = p.get('fair_value', '')
    qs_tool, qs_adj, tier = extract_qs_tier(fv_str)
    # Use adjusted QS if available, else tool
    qs = qs_adj if qs_adj else (qs_tool if qs_tool else 50)
    if not tier:
        if qs >= 75:
            tier = 'A'
        elif qs >= 55:
            tier = 'B'
        elif qs >= 35:
            tier = 'C'
        else:
            tier = 'D'

    # Current value
    current_price = get_price(ticker) if USE_PRICES else None
    if current_price and shares:
        if ticker.endswith('.L'):
            # Price in pence, convert to EUR
            value_eur = (current_price / 100) * shares * gbpeur
        elif ticker.endswith('.DE') or ticker.endswith('.PA') or ticker.endswith('.MI'):
            value_eur = current_price * shares
        else:
            # USD
            value_eur = current_price * shares / eurusd
    else:
        value_eur = invested_eur

    pnl_eur = value_eur - invested_eur
    pnl_pct = (pnl_eur / invested_eur * 100) if invested_eur > 0 else 0

    sector = SECTOR_MAP.get(ticker, 'Other')
    geo = GEO_MAP.get(ticker, 'Other')

    pos_list.append({
        'ticker': ticker, 'invested_eur': invested_eur, 'value_eur': value_eur,
        'pnl_eur': pnl_eur, 'pnl_pct': pnl_pct, 'conviction': conviction,
        'qs': qs, 'tier': tier, 'sector': sector, 'geo': geo, 'shares': shares,
    })

total_invested = sum(p['value_eur'] for p in pos_list)
total_nav = total_invested + cash_eur

# ─── Pipeline Funnel ──────────────────────────────────────────────────────────

pipeline_counts = {}
for c in companies:
    status = c.get('pipeline_status', 'UNKNOWN')
    pipeline_counts[status] = pipeline_counts.get(status, 0) + 1

# ─── Plotting ─────────────────────────────────────────────────────────────────

print("Generating dashboard...")
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    from matplotlib.gridspec import GridSpec
except ImportError:
    print("ERROR: matplotlib not installed. Run: pip install matplotlib")
    sys.exit(1)

fig = plt.figure(figsize=(22, 14))
fig.patch.set_facecolor('#FAFAFA')

gs = GridSpec(2, 3, hspace=0.38, wspace=0.35,
              left=0.05, right=0.96, top=0.91, bottom=0.06)

# ═══════════════════════════════════════════════════════════════════════════════
# PANEL 1: Allocation (Sector + Geography) — Double donut
# ═══════════════════════════════════════════════════════════════════════════════

ax1 = fig.add_subplot(gs[0, 0])

# Sector allocation
sector_totals = {}
for p in pos_list:
    sector_totals[p['sector']] = sector_totals.get(p['sector'], 0) + p['value_eur']
sector_totals['Cash'] = cash_eur

sector_labels = list(sector_totals.keys())
sector_values = list(sector_totals.values())
sector_colors = plt.cm.Set3(np.linspace(0, 1, len(sector_labels)))

# Outer ring: sector
wedges1, texts1, autotexts1 = ax1.pie(
    sector_values, labels=None, autopct='',
    radius=1.0, pctdistance=0.85,
    wedgeprops=dict(width=0.35, edgecolor='white', linewidth=1.5),
    colors=sector_colors, startangle=90
)

# Inner ring: geography
geo_totals = {}
for p in pos_list:
    geo_totals[p['geo']] = geo_totals.get(p['geo'], 0) + p['value_eur']
geo_totals['Cash'] = cash_eur

geo_labels = list(geo_totals.keys())
geo_values = list(geo_totals.values())
geo_cmap = {'US': '#1565C0', 'UK': '#C62828', 'EU': '#2E7D32', 'Cash': '#9E9E9E', 'Other': '#FF8F00'}
geo_colors_list = [geo_cmap.get(g, '#757575') for g in geo_labels]

wedges2, texts2, autotexts2 = ax1.pie(
    geo_values, labels=None, autopct='',
    radius=0.65, pctdistance=0.75,
    wedgeprops=dict(width=0.30, edgecolor='white', linewidth=1),
    colors=geo_colors_list, startangle=90
)

# Center text
ax1.text(0, 0, f'NAV\n€{total_nav:,.0f}', ha='center', va='center',
         fontsize=13, fontweight='bold', color='#212121')

# Legends
sector_legend_labels = [f'{l} ({v/total_nav*100:.0f}%)' for l, v in zip(sector_labels, sector_values)]
leg1 = ax1.legend(wedges1, sector_legend_labels, loc='upper left',
                   fontsize=7, title='Sector (outer)', title_fontsize=8,
                   bbox_to_anchor=(-0.35, 1.05), framealpha=0.8)
geo_legend_labels = [f'{l} ({v/total_nav*100:.0f}%)' for l, v in zip(geo_labels, geo_values)]
leg2 = ax1.legend(wedges2, geo_legend_labels, loc='lower left',
                   fontsize=7, title='Geography (inner)', title_fontsize=8,
                   bbox_to_anchor=(-0.35, -0.15), framealpha=0.8)
ax1.add_artist(leg1)

ax1.set_title('Allocation: Sector & Geography', fontsize=12, fontweight='bold', pad=15)

# ═══════════════════════════════════════════════════════════════════════════════
# PANEL 2: P&L Waterfall by Position
# ═══════════════════════════════════════════════════════════════════════════════

ax2 = fig.add_subplot(gs[0, 1])

sorted_pos = sorted(pos_list, key=lambda x: x['pnl_pct'], reverse=True)
tickers = [p['ticker'].replace('.L', '\n.L').replace('.PA', '\n.PA').replace('.DE', '\n.DE') for p in sorted_pos]
pnls = [p['pnl_pct'] for p in sorted_pos]
bar_colors = ['#2E7D32' if pnl >= 0 else '#C62828' for pnl in pnls]
edge_colors = [CONVICTION_COLORS.get(p['conviction'], '#757575') for p in sorted_pos]

bars = ax2.bar(range(len(tickers)), pnls, color=bar_colors, edgecolor=edge_colors,
               linewidth=2.5, width=0.7, zorder=3)

# Labels on bars
for i, (bar, pnl, pos) in enumerate(zip(bars, pnls, sorted_pos)):
    y_offset = 0.5 if pnl >= 0 else -0.5
    va = 'bottom' if pnl >= 0 else 'top'
    ax2.text(i, pnl + y_offset, f'{pnl:+.1f}%', ha='center', va=va,
             fontsize=8, fontweight='bold', color=bar_colors[i])
    # Show EUR P&L
    ax2.text(i, pnl/2, f'€{pos["pnl_eur"]:+.0f}', ha='center', va='center',
             fontsize=6.5, color='white', fontweight='bold')

ax2.set_xticks(range(len(tickers)))
ax2.set_xticklabels(tickers, fontsize=8, fontweight='bold')
ax2.axhline(y=0, color='#424242', linewidth=0.8, linestyle='-')
ax2.set_ylabel('P&L (%)', fontsize=10)
ax2.set_title('P&L by Position', fontsize=12, fontweight='bold')
ax2.grid(axis='y', alpha=0.3, linestyle='--')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

# Conviction legend
conv_patches = [mpatches.Patch(edgecolor=c, facecolor='lightgray', linewidth=2, label=k.title())
                for k, c in CONVICTION_COLORS.items()]
ax2.legend(handles=conv_patches, loc='upper right', fontsize=7, title='Conviction (border)', title_fontsize=8)

# Total P&L annotation
total_pnl_eur = sum(p['pnl_eur'] for p in pos_list)
total_invested_eur = sum(p['invested_eur'] for p in pos_list)
total_pnl_pct = (total_pnl_eur / total_invested_eur * 100) if total_invested_eur > 0 else 0
ax2.annotate(f'Total: €{total_pnl_eur:+,.0f} ({total_pnl_pct:+.1f}%)',
             xy=(0.02, 0.95), xycoords='axes fraction',
             fontsize=9, fontweight='bold',
             color='#2E7D32' if total_pnl_eur >= 0 else '#C62828',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

# ═══════════════════════════════════════════════════════════════════════════════
# PANEL 3: Quality Map (QS vs Weight, color=tier)
# ═══════════════════════════════════════════════════════════════════════════════

ax3 = fig.add_subplot(gs[0, 2])

weights = [(p['value_eur'] / total_nav) * 100 for p in pos_list]
max_w = max(weights) if weights else 5
min_w = min(weights) if weights else 0
pad = max((max_w - min_w) * 0.25, 0.5)

for p in pos_list:
    weight = (p['value_eur'] / total_nav) * 100
    color = TIER_COLORS.get(p['tier'], '#757575')
    size = max(weight * 40, 100)
    alpha = 0.85 if p['conviction'] != 'low' else 0.55
    ax3.scatter(p['qs'], weight, s=size, c=color, alpha=alpha,
                edgecolors='white', linewidths=1.5, zorder=3)

# Smart label placement to avoid overlaps
label_positions = []
for p in pos_list:
    weight = (p['value_eur'] / total_nav) * 100
    # Try offsets: up, right-up, left-up, down
    offsets = [(0, 8), (8, 5), (-8, 5), (0, -10), (10, 0), (-10, 0)]
    best_offset = offsets[0]
    for ox, oy in offsets:
        candidate_x = p['qs'] + ox * 0.15
        candidate_y = weight + oy * 0.015 * (max_w - min_w + pad)
        conflict = False
        for lx, ly in label_positions:
            if abs(candidate_x - lx) < 4 and abs(candidate_y - ly) < 0.3:
                conflict = True
                break
        if not conflict:
            best_offset = (ox, oy)
            label_positions.append((candidate_x, candidate_y))
            break
    else:
        label_positions.append((p['qs'], weight))

    ax3.annotate(p['ticker'], (p['qs'], weight),
                 fontsize=7, fontweight='bold', ha='center', va='bottom',
                 xytext=best_offset, textcoords='offset points',
                 arrowprops=dict(arrowstyle='-', color='gray', lw=0.5, alpha=0.4)
                 if abs(best_offset[0]) > 5 or abs(best_offset[1]) > 8 else None)

# Set Y limits with padding
ax3.set_ylim(min_w - pad, max_w + pad * 1.5)

# Tier zones
ax3.axvspan(75, 100, alpha=0.06, color='#2E7D32', zorder=1)
ax3.axvspan(55, 75, alpha=0.06, color='#1565C0', zorder=1)
ax3.axvspan(35, 55, alpha=0.06, color='#E65100', zorder=1)
y_top = max_w + pad * 1.2
ax3.text(87, y_top, 'Tier A', fontsize=9, color='#2E7D32', fontweight='bold', ha='center', va='top')
ax3.text(65, y_top, 'Tier B', fontsize=9, color='#1565C0', fontweight='bold', ha='center', va='top')
ax3.text(45, y_top, 'Tier C', fontsize=9, color='#E65100', fontweight='bold', ha='center', va='top')

ax3.set_xlabel('Quality Score (Adjusted)', fontsize=10)
ax3.set_ylabel('Portfolio Weight (%)', fontsize=10)
ax3.set_title('Quality Map: QS vs Weight', fontsize=12, fontweight='bold')
ax3.set_xlim(30, 100)
ax3.grid(alpha=0.3, linestyle='--')
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)

# Avg QS line
avg_qs = np.mean([p['qs'] for p in pos_list]) if pos_list else 0
ax3.axvline(x=avg_qs, color='#424242', linewidth=1, linestyle='--', alpha=0.7)
ax3.text(avg_qs + 1, min_w - pad * 0.5, f'Avg: {avg_qs:.0f}',
         fontsize=8, color='#424242', fontweight='bold')

# ═══════════════════════════════════════════════════════════════════════════════
# PANEL 4: Pipeline Funnel
# ═══════════════════════════════════════════════════════════════════════════════

ax4 = fig.add_subplot(gs[1, 0])

# Define funnel stages in order
funnel_stages = [
    ('SCORED', 'Scored (Universe)'),
    ('R1_COMPLETE', 'R1 Complete'),
    ('R2_PAUSED', 'R2 In Progress'),
    ('R3_COMPLETE', 'R3 Complete'),
    ('R4_APPROVED', 'R4 Approved'),
    ('R4_WATCHLIST', 'R4 Watchlist'),
    ('APPROVED', 'Approved (Legacy)'),
    ('STANDING_ORDER', 'Standing Order'),
    ('ACTIVE', 'Active (Portfolio)'),
    ('FROZEN', 'Frozen'),
]

stage_counts = []
stage_labels = []
for key, label in funnel_stages:
    count = pipeline_counts.get(key, 0)
    if count > 0:
        stage_counts.append(count)
        stage_labels.append(f'{label}\n({count})')

# Horizontal bar chart (reversed so biggest at top)
stage_counts_rev = stage_counts[::-1]
stage_labels_rev = stage_labels[::-1]

cmap = plt.cm.YlGnBu(np.linspace(0.2, 0.9, len(stage_counts_rev)))

bars4 = ax4.barh(range(len(stage_counts_rev)), stage_counts_rev,
                  color=cmap, edgecolor='white', linewidth=1, height=0.7)

for i, (bar, count) in enumerate(zip(bars4, stage_counts_rev)):
    ax4.text(bar.get_width() + 0.5, i, str(count), va='center', ha='left',
             fontsize=9, fontweight='bold', color='#424242')

ax4.set_yticks(range(len(stage_labels_rev)))
ax4.set_yticklabels(stage_labels_rev, fontsize=8)
ax4.set_xlabel('Number of Companies', fontsize=10)
ax4.set_title('Pipeline Funnel', fontsize=12, fontweight='bold')
ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)
ax4.grid(axis='x', alpha=0.3, linestyle='--')

total_universe = sum(pipeline_counts.values())
ax4.annotate(f'Universe: {total_universe} companies',
             xy=(0.95, 0.05), xycoords='axes fraction', ha='right',
             fontsize=9, fontweight='bold', color='#1565C0',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

# ═══════════════════════════════════════════════════════════════════════════════
# PANEL 5: Standing Order Proximity
# ═══════════════════════════════════════════════════════════════════════════════

ax5 = fig.add_subplot(gs[1, 1])

so_entries = []
for so in standing_orders:
    ticker = so.get('ticker', '?')
    action = so.get('action', 'BUY')
    category = so.get('category', '?')
    trigger_str = so.get('trigger', '')
    distance_str = so.get('current_distance', '')
    tier_str = so.get('tier', '')
    fill_prob = so.get('fill_prob_6m', 0)

    # Parse distance
    dist = None
    if distance_str and distance_str != 'conditional':
        m = re.search(r'([\d.]+)', str(distance_str))
        if m:
            dist = float(m.group(1))

    if dist is not None:
        so_entries.append({
            'label': f'{ticker} ({action})',
            'distance': dist,
            'category': category,
            'fill_prob': fill_prob,
            'tier': tier_str,
        })

# Sort by distance, limit to top 15
so_entries.sort(key=lambda x: x['distance'])
so_entries = so_entries[:15]

if so_entries:
    labels5 = [e['label'] for e in so_entries]
    distances5 = [e['distance'] for e in so_entries]
    probs5 = [e['fill_prob'] for e in so_entries]

    cat_colors = {
        'ACTIVE': '#2E7D32', 'GATED': '#E65100', 'BORDERLINE': '#1565C0', 'EXTREME': '#B71C1C'
    }
    colors5 = [cat_colors.get(e['category'], '#757575') for e in so_entries]

    bars5 = ax5.barh(range(len(labels5)), distances5, color=colors5,
                      edgecolor='white', linewidth=1, height=0.65, alpha=0.85)

    for i, (bar, dist, prob) in enumerate(zip(bars5, distances5, probs5)):
        ax5.text(bar.get_width() + 0.3, i, f'{dist:.1f}%  (P:{prob}%)',
                 va='center', ha='left', fontsize=7.5, fontweight='bold', color='#424242')

    ax5.set_yticks(range(len(labels5)))
    ax5.set_yticklabels(labels5, fontsize=8, fontweight='bold')
    ax5.set_xlabel('Distance to Trigger (%)', fontsize=10)
    ax5.invert_yaxis()

    # Zone markers
    ax5.axvline(x=5, color='#2E7D32', linewidth=1, linestyle='--', alpha=0.5)
    ax5.axvline(x=15, color='#E65100', linewidth=1, linestyle='--', alpha=0.5)
    ax5.text(2.5, -0.7, 'HOT', fontsize=7, color='#2E7D32', ha='center', fontweight='bold')
    ax5.text(10, -0.7, 'WARM', fontsize=7, color='#E65100', ha='center', fontweight='bold')

    # Legend
    cat_patches = [mpatches.Patch(color=c, label=k, alpha=0.85)
                   for k, c in cat_colors.items() if any(e['category'] == k for e in so_entries)]
    ax5.legend(handles=cat_patches, loc='lower right', fontsize=7, title='Category', title_fontsize=8)

ax5.set_title('Standing Orders: Distance to Trigger', fontsize=12, fontweight='bold')
ax5.spines['top'].set_visible(False)
ax5.spines['right'].set_visible(False)
ax5.grid(axis='x', alpha=0.3, linestyle='--')

# ═══════════════════════════════════════════════════════════════════════════════
# PANEL 6: Portfolio Summary KPIs
# ═══════════════════════════════════════════════════════════════════════════════

ax6 = fig.add_subplot(gs[1, 2])
ax6.axis('off')

# Calculate KPIs
n_positions = len(pos_list)
cash_pct = (cash_eur / total_nav * 100) if total_nav > 0 else 0
invested_pct = 100 - cash_pct
avg_qs_val = np.mean([p['qs'] for p in pos_list]) if pos_list else 0
tier_dist = {}
for p in pos_list:
    tier_dist[p['tier']] = tier_dist.get(p['tier'], 0) + 1

# Conviction distribution
conv_dist = {}
for p in pos_list:
    conv_dist[p['conviction']] = conv_dist.get(p['conviction'], 0) + 1

# Pipeline summary
actionable = sum(1 for c in companies if c.get('pipeline_status') in
                 ['R4_APPROVED', 'APPROVED', 'STANDING_ORDER'])
advanced = sum(1 for c in companies if c.get('pipeline_status') in ['R3_COMPLETE'])

# KPI table
kpi_data = [
    ('NET ASSET VALUE', f'€{total_nav:,.0f}', '#212121'),
    ('Cash / Invested', f'€{cash_eur:,.0f} ({cash_pct:.0f}%) / €{total_invested:,.0f} ({invested_pct:.0f}%)', '#1565C0'),
    ('Positions', f'{n_positions}', '#212121'),
    ('Avg Quality Score', f'{avg_qs_val:.0f}', '#2E7D32' if avg_qs_val >= 70 else '#E65100'),
    ('Tier Distribution', '  '.join(f'{t}: {c}' for t, c in sorted(tier_dist.items())), '#212121'),
    ('Conviction', '  '.join(f'{k.title()}: {v}' for k, v in sorted(conv_dist.items())), '#212121'),
    ('Total P&L', f'€{total_pnl_eur:+,.0f} ({total_pnl_pct:+.1f}%)',
     '#2E7D32' if total_pnl_eur >= 0 else '#C62828'),
    ('', '', '#FFFFFF'),  # spacer
    ('PIPELINE', '', '#757575'),
    ('Universe Size', f'{total_universe}', '#212121'),
    ('Actionable (R4/SO)', f'{actionable}', '#2E7D32'),
    ('Advanced (R3)', f'{advanced}', '#1565C0'),
    ('Active SOs', f'{len([s for s in standing_orders if s.get("category") == "ACTIVE"])}', '#E65100'),
]

y_pos = 0.95
for label, value, color in kpi_data:
    if label == '':
        y_pos -= 0.03
        continue
    if label in ('NET ASSET VALUE', 'PIPELINE'):
        ax6.text(0.05, y_pos, label, fontsize=11, fontweight='bold', color=color,
                 transform=ax6.transAxes, va='top',
                 bbox=dict(boxstyle='round,pad=0.2', facecolor='#E3F2FD' if label == 'NET ASSET VALUE' else '#F3E5F5',
                           alpha=0.6))
        ax6.text(0.95, y_pos, value, fontsize=11, fontweight='bold', color=color,
                 transform=ax6.transAxes, va='top', ha='right')
    else:
        ax6.text(0.05, y_pos, label, fontsize=9, color='#616161',
                 transform=ax6.transAxes, va='top')
        ax6.text(0.95, y_pos, value, fontsize=9, fontweight='bold', color=color,
                 transform=ax6.transAxes, va='top', ha='right')
    y_pos -= 0.072

# Date
from datetime import datetime
ax6.text(0.5, 0.02, f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M")} | Live data from portfolio & universe',
         fontsize=7, color='#9E9E9E', ha='center', transform=ax6.transAxes)

ax6.set_title('Portfolio Summary', fontsize=12, fontweight='bold')

# ═══════════════════════════════════════════════════════════════════════════════
# Title & Save
# ═══════════════════════════════════════════════════════════════════════════════

fig.suptitle(
    f'Portfolio Dashboard | {datetime.now().strftime("%Y-%m-%d")} | '
    f'{n_positions} positions | €{total_nav:,.0f} NAV | {cash_pct:.0f}% cash',
    fontsize=15, fontweight='bold', color='#212121', y=0.97
)

plt.savefig(OUTPUT, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
print(f"\nDashboard saved: {OUTPUT}")
plt.close()
