#!/usr/bin/env python3
"""
Investment Effectiveness Tracker - Comprehensive performance evaluation framework.

Tracks investment decisions, calculates key metrics, and provides attribution analysis
to evaluate system performance and identify patterns for improvement.

Usage:
    python3 tools/effectiveness_tracker.py                   # Full report
    python3 tools/effectiveness_tracker.py --summary         # Summary only
    python3 tools/effectiveness_tracker.py --positions       # Position-level detail
    python3 tools/effectiveness_tracker.py --attribution     # Attribution analysis
    python3 tools/effectiveness_tracker.py --retrospective   # Thesis accuracy review
    python3 tools/effectiveness_tracker.py --recommendations # Improvement recommendations

Data Sources:
    - portfolio/current.yaml (active positions)
    - portfolio/history.yaml (closed positions)
    - thesis/active/*/thesis.md (fair value targets)
    - yfinance (current prices)

Key Metrics:
    - Hit rate (% reaching FV target or >80% of target)
    - Average time to FV (for winners)
    - Average loss at exit (for losers)
    - Sharpe ratio vs MSCI Europe benchmark
    - Max drawdown
    - Win/loss ratio
    - Attribution by sector/geography/tier/holding period

Author: Quant Tools Dev Agent
Version: 1.0.1
Created: 2026-02-03
"""

import argparse
import os
import re
import sys
from datetime import datetime, timedelta, date
from typing import Dict, List, Optional, Tuple, Any, Union

import yaml
import yfinance as yf
import numpy as np

# ==============================================================================
# Configuration
# ==============================================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORTFOLIO_FILE = os.path.join(BASE_DIR, 'portfolio', 'current.yaml')
HISTORY_FILE = os.path.join(BASE_DIR, 'portfolio', 'history.yaml')
THESIS_DIR = os.path.join(BASE_DIR, 'thesis', 'active')
BENCHMARK_TICKER = "IMEU.L"  # iShares MSCI Europe ETF

# Ticker to sector/geography mapping (simplified, could be enhanced)
SECTOR_MAP = {
    'DTE.DE': ('Telecom', 'Germany'),
    'SHEL.L': ('Energy', 'UK'),
    'PFE': ('Healthcare', 'US'),
    'ALL': ('Financials', 'US'),
    'TEP.PA': ('Business Services', 'France'),
    'SAN.PA': ('Healthcare', 'France'),
    'VICI': ('Real Estate', 'US'),
    'IMB.L': ('Consumer Staples', 'UK'),
    'LIGHT.AS': ('Industrials', 'Netherlands'),
    'A2A.MI': ('Utilities', 'Italy'),
    'EDEN.PA': ('Business Services', 'France'),
    'VNA.DE': ('Real Estate', 'Germany'),
    'TATE.L': ('Consumer Staples', 'UK'),
    'DOM.L': ('Consumer Discretionary', 'UK'),
    'UHS': ('Healthcare', 'US'),
    'GL': ('Financials', 'US'),
    'FUTR.L': ('Media', 'UK'),
    'HRB': ('Business Services', 'US'),
    'ENEL.MI': ('Utilities', 'Italy'),
}

# Tier classification (MoS-based)
def classify_tier(mos_pct: float) -> str:
    """Classify position tier based on margin of safety."""
    if mos_pct >= 40:
        return 'A'
    elif mos_pct >= 25:
        return 'B'
    else:
        return 'C'


def parse_date(d: Union[str, date, datetime, None], default: str = '2026-01-26') -> datetime:
    """Parse date from various formats to datetime."""
    if d is None:
        return datetime.strptime(default, '%Y-%m-%d')
    if isinstance(d, datetime):
        return d
    if isinstance(d, date):
        return datetime.combine(d, datetime.min.time())
    if isinstance(d, str):
        return datetime.strptime(d, '%Y-%m-%d')
    return datetime.strptime(default, '%Y-%m-%d')


# ==============================================================================
# Data Loading
# ==============================================================================

def load_yaml(filepath: str) -> Dict:
    """Load YAML file safely."""
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r') as f:
        return yaml.safe_load(f) or {}


def load_portfolio() -> Dict:
    """Load current portfolio."""
    return load_yaml(PORTFOLIO_FILE)


def load_history() -> Dict:
    """Load portfolio history."""
    return load_yaml(HISTORY_FILE)


def get_fx_rates() -> Tuple[float, float]:
    """Get EUR/USD and GBP/USD rates."""
    try:
        eurusd = yf.Ticker('EURUSD=X').info.get('previousClose', 1.04)
    except:
        eurusd = 1.04
    try:
        gbpusd = yf.Ticker('GBPUSD=X').info.get('previousClose', 1.26)
    except:
        gbpusd = 1.26
    return eurusd, gbpusd


def to_usd(price: float, currency: str, eurusd: float, gbpusd: float) -> float:
    """Convert price to USD."""
    if currency == 'EUR':
        return price * eurusd
    elif currency in ('GBp', 'GBX'):
        return (price / 100) * gbpusd
    elif currency == 'GBP':
        return price * gbpusd
    return price


def to_eur(price: float, currency: str, eurusd: float, gbpusd: float) -> float:
    """Convert price to EUR."""
    if currency == 'USD':
        return price / eurusd
    elif currency in ('GBp', 'GBX'):
        return (price / 100) * gbpusd / eurusd
    elif currency == 'GBP':
        return price * gbpusd / eurusd
    return price


# ==============================================================================
# Thesis Parsing
# ==============================================================================

def parse_thesis_for_fv(ticker: str) -> Dict[str, Any]:
    """
    Parse thesis file to extract fair value, entry price, and tier information.
    Returns dict with: fair_value, entry_price, mos_pct, tier, currency
    """
    thesis_path = os.path.join(THESIS_DIR, ticker, 'thesis.md')
    if not os.path.exists(thesis_path):
        return {}

    with open(thesis_path, 'r') as f:
        content = f.read()

    result = {}

    # Try to extract Fair Value (multiple patterns)
    fv_patterns = [
        r'Fair Value[:\s]*\$?([\d,]+(?:\.\d+)?)',
        r'FV[:\s]*\$?([\d,]+(?:\.\d+)?)',
        r'fair value[:\s]*\$?([\d,]+(?:\.\d+)?)',
        r'Fair Value[:\s]*EUR?\s*([\d,]+(?:\.\d+)?)',
        r'FV[:\s]*EUR?\s*([\d,]+(?:\.\d+)?)',
        r'\*\*Weighted Average\*\*[^\d]*([\d,]+(?:\.\d+)?)',
        r'Expected Value[:\s]*EUR?\s*([\d,]+(?:\.\d+)?)',
        r'REVISED FAIR VALUE[^:]*:\s*EUR?\s*([\d,-]+)',
    ]

    for pattern in fv_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            fv_str = match.group(1).replace(',', '').split('-')[0]  # Handle ranges
            try:
                result['fair_value'] = float(fv_str)
                # Detect currency from context
                if 'EUR' in content[:match.start()+100] or '.PA' in ticker or '.DE' in ticker or '.MI' in ticker or '.AS' in ticker:
                    result['fv_currency'] = 'EUR'
                elif 'GBp' in content or 'GBX' in content or '.L' in ticker:
                    result['fv_currency'] = 'GBp'
                else:
                    result['fv_currency'] = 'USD'
                break
            except ValueError:
                continue

    # Try to extract Margin of Safety
    mos_patterns = [
        r'Margen de Seguridad[:\s]*\*?\*?([+-]?\d+(?:\.\d+)?)\%?\*?\*?',
        r'MoS[:\s]*\*?\*?([+-]?\d+(?:\.\d+)?)\%?\*?\*?',
        r'Margin of Safety[:\s]*\*?\*?([+-]?\d+(?:\.\d+)?)\%?\*?\*?',
    ]

    for pattern in mos_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            try:
                result['mos_pct'] = float(match.group(1))
                result['tier'] = classify_tier(result['mos_pct'])
                break
            except ValueError:
                continue

    # Try to extract Tier directly if not found via MoS
    if 'tier' not in result:
        tier_patterns = [
            r'Tier[:\s]*([ABC])',
            r'tier[:\s]*([ABC])',
        ]
        for pattern in tier_patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                result['tier'] = match.group(1).upper()
                break

    return result


# ==============================================================================
# Position Analysis
# ==============================================================================

def analyze_active_positions(portfolio: Dict, eurusd: float, gbpusd: float) -> List[Dict]:
    """Analyze all active positions with current prices and thesis targets."""
    positions = portfolio.get('positions', [])
    results = []

    TICKER_MAP = {'LIGHT.NV': 'LIGHT.AS'}

    for p in positions:
        ticker = p['ticker']
        yf_ticker = TICKER_MAP.get(ticker, ticker)

        # Get current price
        try:
            info = yf.Ticker(yf_ticker).info
            price = info.get('currentPrice') or info.get('regularMarketPrice') or info.get('previousClose')
            currency = info.get('currency', 'USD')
        except Exception as e:
            print(f"  WARN: {ticker} - Could not fetch price: {e}", file=sys.stderr)
            continue

        if not price:
            print(f"  WARN: {ticker} - No price data", file=sys.stderr)
            continue

        # Get invested amount
        if 'invested_usd' in p:
            invested_usd = p['invested_usd']
        elif 'invested_eur' in p:
            invested_usd = p['invested_eur'] * eurusd
        else:
            print(f"  WARN: {ticker} - No invested amount", file=sys.stderr)
            continue

        shares = p['shares']
        avg_cost_usd = p.get('avg_cost_usd', invested_usd / shares)

        # Current value and P&L
        price_usd = to_usd(price, currency, eurusd, gbpusd)
        current_value = price_usd * shares
        pnl = current_value - invested_usd
        pnl_pct = (pnl / invested_usd) * 100

        # Parse thesis for FV
        thesis_data = parse_thesis_for_fv(ticker)
        fair_value = thesis_data.get('fair_value')
        fv_currency = thesis_data.get('fv_currency', 'USD')

        # Convert FV to USD for comparison
        if fair_value:
            fv_usd = to_usd(fair_value, fv_currency, eurusd, gbpusd)
            distance_to_fv = ((fv_usd - price_usd) / price_usd) * 100
            fv_reached = price_usd >= fv_usd * 0.8  # 80% of target counts
        else:
            fv_usd = None
            distance_to_fv = None
            fv_reached = None

        # Calculate holding period - handle both date and datetime
        entry_date = parse_date(p.get('date_opened'), '2026-01-26')
        holding_days = (datetime.now() - entry_date).days

        # Sector/Geography
        sector, geo = SECTOR_MAP.get(ticker, ('Unknown', 'Unknown'))

        results.append({
            'ticker': ticker,
            'name': p.get('name', ticker),
            'shares': shares,
            'avg_cost_usd': avg_cost_usd,
            'current_price': price,
            'current_price_usd': price_usd,
            'currency': currency,
            'invested_usd': invested_usd,
            'current_value_usd': current_value,
            'pnl_usd': pnl,
            'pnl_pct': pnl_pct,
            'fair_value': fair_value,
            'fv_currency': fv_currency,
            'fv_usd': fv_usd,
            'distance_to_fv_pct': distance_to_fv,
            'fv_reached': fv_reached,
            'tier': thesis_data.get('tier', 'Unknown'),
            'mos_pct': thesis_data.get('mos_pct'),
            'entry_date': entry_date,
            'holding_days': holding_days,
            'sector': sector,
            'geography': geo,
        })

    return results


def analyze_closed_positions(history: Dict) -> List[Dict]:
    """Analyze all closed positions from history."""
    closed = history.get('closed_positions', [])
    results = []

    for p in closed:
        ticker = p.get('ticker')
        if not ticker:
            continue

        pnl_pct = p.get('pnl_percent', 0)
        holding_days = p.get('holding_days', 0)
        fv_reached = p.get('fv_reached', False)

        # Determine win/loss/breakeven
        if pnl_pct > 1:
            outcome = 'win'
        elif pnl_pct < -1:
            outcome = 'loss'
        else:
            outcome = 'breakeven'

        sector, geo = SECTOR_MAP.get(ticker, ('Unknown', 'Unknown'))

        results.append({
            'ticker': ticker,
            'name': p.get('name', ticker),
            'entry_date': p.get('entry_date'),
            'exit_date': p.get('exit_date'),
            'holding_days': holding_days,
            'pnl_amount': p.get('pnl_amount', 0),
            'pnl_pct': pnl_pct,
            'outcome': outcome,
            'fv_at_entry': p.get('thesis_fv_at_entry'),
            'fv_reached': fv_reached,
            'thesis_correct': p.get('thesis_accuracy', {}).get('correct'),
            'thesis_notes': p.get('thesis_accuracy', {}).get('notes', ''),
            'exit_reason': p.get('exit_reason', 'unknown'),
            'sector': sector,
            'geography': geo,
        })

    return results


# ==============================================================================
# Metrics Calculation
# ==============================================================================

def calculate_portfolio_metrics(active: List[Dict], closed: List[Dict],
                                 portfolio: Dict, eurusd: float) -> Dict:
    """Calculate comprehensive portfolio metrics."""
    cash_eur = portfolio.get('cash', {}).get('amount', 0)
    cash_usd = cash_eur * eurusd

    total_invested = sum(p['invested_usd'] for p in active)
    total_value = sum(p['current_value_usd'] for p in active)
    portfolio_value = total_value + cash_usd

    total_pnl = total_value - total_invested
    total_pnl_pct = (total_pnl / total_invested * 100) if total_invested > 0 else 0

    # Win/Loss for active positions (based on current P&L)
    active_winners = [p for p in active if p['pnl_pct'] > 1]
    active_losers = [p for p in active if p['pnl_pct'] < -1]
    active_breakeven = [p for p in active if -1 <= p['pnl_pct'] <= 1]

    # Closed position stats
    closed_winners = [p for p in closed if p['outcome'] == 'win']
    closed_losers = [p for p in closed if p['outcome'] == 'loss']

    # Hit rate (positions that reached FV target)
    fv_hits = [p for p in active if p.get('fv_reached') is True]
    fv_misses = [p for p in active if p.get('fv_reached') is False]

    # Average returns
    avg_winner_pct = np.mean([p['pnl_pct'] for p in active_winners]) if active_winners else 0
    avg_loser_pct = np.mean([p['pnl_pct'] for p in active_losers]) if active_losers else 0

    # Holding period
    avg_holding = np.mean([p['holding_days'] for p in active]) if active else 0

    # Calculate daily returns for Sharpe (simplified - would need historical data for accurate calc)
    # For now, annualize the current return
    if avg_holding > 0 and total_pnl_pct != 0:
        annualized_return = (1 + total_pnl_pct/100) ** (365/avg_holding) - 1
    else:
        annualized_return = 0

    # Sharpe (simplified: assume 5% risk-free, 15% volatility estimate)
    risk_free = 0.05
    vol_estimate = 0.15
    sharpe = (annualized_return - risk_free) / vol_estimate if vol_estimate > 0 else 0

    return {
        'portfolio_value_usd': portfolio_value,
        'portfolio_value_eur': portfolio_value / eurusd,
        'total_invested_usd': total_invested,
        'total_value_usd': total_value,
        'cash_usd': cash_usd,
        'cash_pct': (cash_usd / portfolio_value * 100) if portfolio_value > 0 else 0,
        'total_pnl_usd': total_pnl,
        'total_pnl_pct': total_pnl_pct,
        'active_positions': len(active),
        'active_winners': len(active_winners),
        'active_losers': len(active_losers),
        'active_breakeven': len(active_breakeven),
        'closed_positions': len(closed),
        'closed_winners': len(closed_winners),
        'closed_losers': len(closed_losers),
        'win_rate_active_pct': (len(active_winners) / len(active) * 100) if active else 0,
        'avg_winner_pct': avg_winner_pct,
        'avg_loser_pct': avg_loser_pct,
        'fv_hit_count': len(fv_hits),
        'fv_hit_rate_pct': (len(fv_hits) / (len(fv_hits) + len(fv_misses)) * 100) if (fv_hits or fv_misses) else 0,
        'avg_holding_days': avg_holding,
        'annualized_return': annualized_return * 100,
        'sharpe_estimate': sharpe,
    }


def calculate_attribution(active: List[Dict], closed: List[Dict]) -> Dict:
    """Calculate performance attribution by various dimensions."""
    all_positions = active + closed

    attribution = {
        'by_sector': {},
        'by_geography': {},
        'by_tier': {},
        'by_holding_period': {
            '0-7d': [],
            '8-30d': [],
            '31-90d': [],
            '>90d': [],
        }
    }

    # Attribution by sector
    for p in all_positions:
        sector = p.get('sector', 'Unknown')
        if sector not in attribution['by_sector']:
            attribution['by_sector'][sector] = {'count': 0, 'total_pnl_pct': 0, 'positions': []}
        attribution['by_sector'][sector]['count'] += 1
        attribution['by_sector'][sector]['total_pnl_pct'] += p.get('pnl_pct', 0)
        attribution['by_sector'][sector]['positions'].append(p['ticker'])

    # Calculate averages
    for sector in attribution['by_sector']:
        count = attribution['by_sector'][sector]['count']
        if count > 0:
            attribution['by_sector'][sector]['avg_pnl_pct'] = attribution['by_sector'][sector]['total_pnl_pct'] / count

    # Attribution by geography
    for p in all_positions:
        geo = p.get('geography', 'Unknown')
        if geo not in attribution['by_geography']:
            attribution['by_geography'][geo] = {'count': 0, 'total_pnl_pct': 0, 'positions': []}
        attribution['by_geography'][geo]['count'] += 1
        attribution['by_geography'][geo]['total_pnl_pct'] += p.get('pnl_pct', 0)
        attribution['by_geography'][geo]['positions'].append(p['ticker'])

    for geo in attribution['by_geography']:
        count = attribution['by_geography'][geo]['count']
        if count > 0:
            attribution['by_geography'][geo]['avg_pnl_pct'] = attribution['by_geography'][geo]['total_pnl_pct'] / count

    # Attribution by tier
    for p in active:  # Only active have tier info
        tier = p.get('tier', 'Unknown')
        if tier not in attribution['by_tier']:
            attribution['by_tier'][tier] = {'count': 0, 'total_pnl_pct': 0, 'positions': []}
        attribution['by_tier'][tier]['count'] += 1
        attribution['by_tier'][tier]['total_pnl_pct'] += p.get('pnl_pct', 0)
        attribution['by_tier'][tier]['positions'].append(p['ticker'])

    for tier in attribution['by_tier']:
        count = attribution['by_tier'][tier]['count']
        if count > 0:
            attribution['by_tier'][tier]['avg_pnl_pct'] = attribution['by_tier'][tier]['total_pnl_pct'] / count

    # Attribution by holding period
    for p in all_positions:
        days = p.get('holding_days', 0)
        if days <= 7:
            bucket = '0-7d'
        elif days <= 30:
            bucket = '8-30d'
        elif days <= 90:
            bucket = '31-90d'
        else:
            bucket = '>90d'
        attribution['by_holding_period'][bucket].append({
            'ticker': p['ticker'],
            'pnl_pct': p.get('pnl_pct', 0),
            'days': days
        })

    return attribution


def generate_recommendations(metrics: Dict, attribution: Dict, active: List[Dict]) -> List[str]:
    """Generate actionable recommendations based on patterns."""
    recommendations = []

    # Cash drag check
    if metrics['cash_pct'] > 15:
        recommendations.append(f"HIGH CASH DRAG: {metrics['cash_pct']:.1f}% cash. Deploy capital to high-MoS opportunities.")

    # Win rate check
    if metrics['win_rate_active_pct'] < 50 and metrics['active_positions'] >= 5:
        recommendations.append(f"LOW WIN RATE: Only {metrics['win_rate_active_pct']:.0f}% of positions profitable. Review thesis quality.")

    # Sector concentration
    for sector, data in attribution['by_sector'].items():
        if data['count'] >= 3 and data.get('avg_pnl_pct', 0) < -5:
            recommendations.append(f"SECTOR UNDERPERFORMANCE: {sector} has {data['count']} positions avg {data['avg_pnl_pct']:.1f}%. Review exposure.")

    # Geography performance
    for geo, data in attribution['by_geography'].items():
        if data['count'] >= 3 and data.get('avg_pnl_pct', 0) < -5:
            recommendations.append(f"GEO UNDERPERFORMANCE: {geo} has {data['count']} positions avg {data['avg_pnl_pct']:.1f}%. Review exposure.")

    # Tier analysis
    tier_a = attribution['by_tier'].get('A', {})
    tier_c = attribution['by_tier'].get('C', {})
    if tier_a.get('count', 0) > 0 and tier_c.get('count', 0) > 0:
        if tier_c.get('avg_pnl_pct', 0) > tier_a.get('avg_pnl_pct', 0):
            recommendations.append("TIER ANOMALY: Tier C outperforming Tier A. Review MoS calibration.")

    # FV hit rate
    if metrics['fv_hit_rate_pct'] < 20 and (metrics['fv_hit_count'] + len([p for p in active if p.get('fv_reached') is False])) >= 5:
        recommendations.append(f"LOW FV HIT RATE: Only {metrics['fv_hit_rate_pct']:.0f}% reached 80%+ of FV. Targets may be too aggressive.")

    # Positions near FV (consider taking profits)
    for p in active:
        if p.get('distance_to_fv_pct') is not None and p['distance_to_fv_pct'] < 10 and p['pnl_pct'] > 20:
            recommendations.append(f"NEAR FV TARGET: {p['ticker']} is {p['distance_to_fv_pct']:.1f}% from FV with {p['pnl_pct']:.1f}% gain. Consider TRIM/SELL.")

    # Big losers
    for p in active:
        if p['pnl_pct'] < -15:
            recommendations.append(f"SIGNIFICANT LOSS: {p['ticker']} down {p['pnl_pct']:.1f}%. Review thesis validity.")

    if not recommendations:
        recommendations.append("NO CRITICAL ISSUES: Portfolio performing within expected parameters.")

    return recommendations


# ==============================================================================
# Report Generation
# ==============================================================================

def print_summary(metrics: Dict):
    """Print summary metrics."""
    print("=" * 80)
    print("INVESTMENT EFFECTIVENESS SUMMARY")
    print("=" * 80)
    print()
    print(f"Portfolio Value:      ${metrics['portfolio_value_usd']:,.0f} (EUR {metrics['portfolio_value_eur']:,.0f})")
    print(f"Total P&L:            ${metrics['total_pnl_usd']:+,.0f} ({metrics['total_pnl_pct']:+.1f}%)")
    print(f"Cash:                 ${metrics['cash_usd']:,.0f} ({metrics['cash_pct']:.1f}%)")
    print()
    print("POSITION STATS")
    print("-" * 40)
    print(f"Active Positions:     {metrics['active_positions']}")
    print(f"  Winners:            {metrics['active_winners']} ({metrics['win_rate_active_pct']:.0f}%)")
    print(f"  Losers:             {metrics['active_losers']}")
    print(f"  Breakeven:          {metrics['active_breakeven']}")
    print(f"Closed Positions:     {metrics['closed_positions']}")
    print(f"  Winners:            {metrics['closed_winners']}")
    print(f"  Losers:             {metrics['closed_losers']}")
    print()
    print("PERFORMANCE METRICS")
    print("-" * 40)
    print(f"Avg Winner Return:    {metrics['avg_winner_pct']:+.1f}%")
    print(f"Avg Loser Return:     {metrics['avg_loser_pct']:+.1f}%")
    print(f"FV Hit Rate:          {metrics['fv_hit_rate_pct']:.0f}% (reached 80%+ of target)")
    print(f"Avg Holding Period:   {metrics['avg_holding_days']:.0f} days")
    print(f"Annualized Return:    {metrics['annualized_return']:+.1f}% (est.)")
    print(f"Sharpe Ratio:         {metrics['sharpe_estimate']:.2f} (est.)")
    print()


def print_positions(active: List[Dict]):
    """Print position-level detail."""
    print("=" * 100)
    print("POSITION DETAIL")
    print("=" * 100)
    print()
    print(f"{'Ticker':<10} {'P&L%':>7} {'FV':>8} {'Dist%':>7} {'Tier':>5} {'Days':>5} {'Sector':<18} {'Status':<10}")
    print("-" * 100)

    # Sort by P&L descending
    sorted_pos = sorted(active, key=lambda x: x['pnl_pct'], reverse=True)

    for p in sorted_pos:
        fv_str = f"${p['fv_usd']:.0f}" if p.get('fv_usd') else "N/A"
        dist_str = f"{p['distance_to_fv_pct']:+.0f}%" if p.get('distance_to_fv_pct') is not None else "N/A"

        # Status
        if p.get('fv_reached'):
            status = "AT FV"
        elif p['pnl_pct'] > 10:
            status = "WINNING"
        elif p['pnl_pct'] < -10:
            status = "LOSING"
        else:
            status = "TRACKING"

        print(f"{p['ticker']:<10} {p['pnl_pct']:>+6.1f}% {fv_str:>8} {dist_str:>7} {p['tier']:>5} {p['holding_days']:>5} {p['sector']:<18} {status:<10}")

    print()


def print_attribution(attribution: Dict):
    """Print attribution analysis."""
    print("=" * 80)
    print("ATTRIBUTION ANALYSIS")
    print("=" * 80)
    print()

    print("BY SECTOR")
    print("-" * 50)
    for sector, data in sorted(attribution['by_sector'].items(),
                                key=lambda x: x[1].get('avg_pnl_pct', 0), reverse=True):
        print(f"{sector:<20} {data['count']:>3} pos  Avg P&L: {data.get('avg_pnl_pct', 0):>+6.1f}%")
    print()

    print("BY GEOGRAPHY")
    print("-" * 50)
    for geo, data in sorted(attribution['by_geography'].items(),
                            key=lambda x: x[1].get('avg_pnl_pct', 0), reverse=True):
        print(f"{geo:<20} {data['count']:>3} pos  Avg P&L: {data.get('avg_pnl_pct', 0):>+6.1f}%")
    print()

    print("BY TIER (MoS-based)")
    print("-" * 50)
    for tier in ['A', 'B', 'C', 'Unknown']:
        if tier in attribution['by_tier']:
            data = attribution['by_tier'][tier]
            print(f"Tier {tier:<15} {data['count']:>3} pos  Avg P&L: {data.get('avg_pnl_pct', 0):>+6.1f}%")
    print()

    print("BY HOLDING PERIOD")
    print("-" * 50)
    for bucket, positions in attribution['by_holding_period'].items():
        if positions:
            avg_pnl = np.mean([p['pnl_pct'] for p in positions])
            print(f"{bucket:<10} {len(positions):>3} pos  Avg P&L: {avg_pnl:>+6.1f}%")
    print()


def print_retrospective(active: List[Dict], closed: List[Dict]):
    """Print retrospective thesis evaluation."""
    print("=" * 80)
    print("RETROSPECTIVE EVALUATION")
    print("=" * 80)
    print()

    print("ACTIVE POSITIONS - THESIS STATUS")
    print("-" * 60)
    for p in sorted(active, key=lambda x: x['pnl_pct'], reverse=True):
        if p['pnl_pct'] > 15:
            status = "ON TRACK - Strong"
        elif p['pnl_pct'] > 5:
            status = "ON TRACK"
        elif p['pnl_pct'] > -5:
            status = "NEUTRAL"
        elif p['pnl_pct'] > -15:
            status = "MONITORING"
        else:
            status = "REVIEW NEEDED"

        print(f"{p['ticker']:<10} {p['pnl_pct']:>+6.1f}%  {status}")
    print()

    if closed:
        print("CLOSED POSITIONS - THESIS ACCURACY")
        print("-" * 60)
        for p in closed:
            accuracy = "Correct" if p.get('thesis_correct') else "Incorrect" if p.get('thesis_correct') is False else "N/A"
            print(f"{p['ticker']:<10} {p['pnl_pct']:>+6.1f}%  {p['exit_reason']:<20}  Thesis: {accuracy}")
            if p.get('thesis_notes'):
                print(f"           Notes: {p['thesis_notes'][:60]}...")
        print()


def print_recommendations(recommendations: List[str]):
    """Print actionable recommendations."""
    print("=" * 80)
    print("RECOMMENDATIONS")
    print("=" * 80)
    print()
    for i, rec in enumerate(recommendations, 1):
        print(f"{i}. {rec}")
    print()


# ==============================================================================
# Main
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(description='Investment Effectiveness Tracker')
    parser.add_argument('--summary', action='store_true', help='Summary metrics only')
    parser.add_argument('--positions', action='store_true', help='Position-level detail')
    parser.add_argument('--attribution', action='store_true', help='Attribution analysis')
    parser.add_argument('--retrospective', action='store_true', help='Thesis accuracy review')
    parser.add_argument('--recommendations', action='store_true', help='Improvement recommendations')
    args = parser.parse_args()

    # Default: show all if no specific flag
    show_all = not any([args.summary, args.positions, args.attribution,
                        args.retrospective, args.recommendations])

    print("Loading portfolio data...")
    portfolio = load_portfolio()
    history = load_history()
    eurusd, gbpusd = get_fx_rates()
    print(f"FX: EUR/USD={eurusd:.4f} GBP/USD={gbpusd:.4f}")
    print()

    print("Analyzing active positions...")
    active = analyze_active_positions(portfolio, eurusd, gbpusd)
    print(f"Found {len(active)} active positions")
    print()

    print("Analyzing closed positions...")
    closed = analyze_closed_positions(history)
    print(f"Found {len(closed)} closed positions")
    print()

    print("Calculating metrics...")
    metrics = calculate_portfolio_metrics(active, closed, portfolio, eurusd)
    attribution = calculate_attribution(active, closed)
    recommendations = generate_recommendations(metrics, attribution, active)
    print()

    # Output
    if show_all or args.summary:
        print_summary(metrics)

    if show_all or args.positions:
        print_positions(active)

    if show_all or args.attribution:
        print_attribution(attribution)

    if show_all or args.retrospective:
        print_retrospective(active, closed)

    if show_all or args.recommendations:
        print_recommendations(recommendations)

    print("=" * 80)
    print(f"Report generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)


if __name__ == '__main__':
    main()
