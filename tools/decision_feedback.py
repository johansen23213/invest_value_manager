#!/usr/bin/env python3
"""
Decision Feedback - Meta-learning engine for investment calibration.

Connects past investment decisions to actual outcomes. Reads decisions_log.yaml,
portfolio/current.yaml, and portfolio/history.yaml, fetches current prices, and
generates a calibration report showing where we are systematically right or wrong.

Usage:
    python3 tools/decision_feedback.py                    # Full calibration report
    python3 tools/decision_feedback.py --buys             # Only BUY decisions
    python3 tools/decision_feedback.py --sells            # Only SELL decisions
    python3 tools/decision_feedback.py --fv-accuracy      # Fair Value accuracy analysis
    python3 tools/decision_feedback.py --ticker TICKER    # Specific ticker history
    python3 tools/decision_feedback.py --patterns         # Pattern analysis only

Data Sources:
    - learning/decisions_log.yaml (decision history with reasoning)
    - portfolio/current.yaml (active positions with fair_value, conviction)
    - portfolio/history.yaml (closed positions with P&L)
    - yfinance (current prices via price_checker patterns)

Author: Quant Tools Dev Agent
Version: 1.0.1
Created: 2026-02-23
"""

import argparse
import os
import re
import sys
from datetime import datetime, date
from typing import Dict, List, Optional, Tuple, Any, Union

import yaml
import yfinance as yf

# ==============================================================================
# Configuration
# ==============================================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DECISIONS_FILE = os.path.join(BASE_DIR, 'learning', 'decisions_log.yaml')
PORTFOLIO_FILE = os.path.join(BASE_DIR, 'portfolio', 'current.yaml')
HISTORY_FILE = os.path.join(BASE_DIR, 'portfolio', 'history.yaml')


# ==============================================================================
# FX Handling (same pattern as price_checker.py)
# ==============================================================================

def get_fx_rates() -> Dict[str, float]:
    """Get FX rates with fallback defaults."""
    defaults = {
        'EURUSD': 1.04,
        'GBPEUR': 1.19,
        'DKKEUR': 0.134,
        'CHFEUR': 1.06,
    }
    rates = {}
    fallbacks_used = []

    pairs = {
        'EURUSD': 'EURUSD=X',
        'GBPEUR': 'GBPEUR=X',
    }

    for key, yf_ticker in pairs.items():
        try:
            val = yf.Ticker(yf_ticker).info.get('previousClose')
            if val and val > 0:
                rates[key] = val
            else:
                rates[key] = defaults[key]
                fallbacks_used.append(f"{key}={defaults[key]}")
        except Exception:
            rates[key] = defaults[key]
            fallbacks_used.append(f"{key}={defaults[key]}")

    # Derived rates
    rates['DKKEUR'] = defaults['DKKEUR']
    rates['CHFEUR'] = defaults['CHFEUR']

    if fallbacks_used:
        print(f"FX WARNING: Using static fallback rates ({', '.join(fallbacks_used)}). EUR amounts may be inaccurate.")

    return rates


def to_eur(price: float, currency: str, rates: Dict[str, float]) -> float:
    """Convert price to EUR."""
    if currency == 'EUR':
        return price
    elif currency == 'USD':
        return price / rates['EURUSD']
    elif currency in ('GBp', 'GBX'):
        return (price / 100) * rates['GBPEUR']
    elif currency == 'GBP':
        return price * rates['GBPEUR']
    elif currency == 'DKK':
        return price * rates['DKKEUR']
    elif currency == 'CHF':
        return price * rates['CHFEUR']
    return price  # Unknown currency, return as-is


def fmt_price(value: float, currency: str) -> str:
    """Smart format a price value with appropriate precision for its currency."""
    # For GBp values (pence), always integer
    if currency in ('GBp', 'GBX'):
        return f"{value:.0f}p"
    # For small values (<10), show 2 decimal places
    if abs(value) < 10:
        num_str = f"{value:.2f}"
    # For medium values (<100), show 1 decimal
    elif abs(value) < 100:
        num_str = f"{value:.1f}"
    # For large values, no decimals
    else:
        num_str = f"{value:.0f}"

    if currency == 'EUR':
        return f"EUR {num_str}"
    elif currency == 'USD':
        return f"${num_str}"
    elif currency == 'GBP':
        return f"GBP {num_str}"
    else:
        return f"{num_str} {currency}"


# ==============================================================================
# Data Loading
# ==============================================================================

def load_yaml(filepath: str) -> Dict:
    """Load YAML file safely."""
    if not os.path.exists(filepath):
        print(f"WARNING: File not found: {filepath}")
        return {}
    with open(filepath, 'r') as f:
        return yaml.safe_load(f) or {}


def parse_date(d: Any, default: str = '2026-01-26') -> datetime:
    """Parse date from various formats."""
    if d is None:
        return datetime.strptime(default, '%Y-%m-%d')
    if isinstance(d, datetime):
        return d
    if isinstance(d, date):
        return datetime.combine(d, datetime.min.time())
    if isinstance(d, str):
        try:
            return datetime.strptime(d, '%Y-%m-%d')
        except ValueError:
            return datetime.strptime(default, '%Y-%m-%d')
    return datetime.strptime(default, '%Y-%m-%d')


# ==============================================================================
# Fair Value Parsing from current.yaml
# ==============================================================================

def parse_fv_from_string(fv_str: str) -> Tuple[Optional[float], str]:
    """
    Parse fair_value string from current.yaml.
    Handles formats like:
        "EUR 35.00 (v3.1...)"
        "190 GBp (v3.0...)"
        "$390 (FTC-adjusted...)"
        "$195 (v4.0...)"
        "345 GBp (adversarial...)"
        "$66 (v3.0...)"
        "240 GBp (v3.0...)"
        "$191 (...)"
    Returns (value, currency).
    """
    if not fv_str or not isinstance(fv_str, str):
        return None, 'USD'

    fv_str = fv_str.strip()

    # Pattern: EUR XX.XX
    m = re.match(r'EUR\s+([\d,.]+)', fv_str)
    if m:
        return float(m.group(1).replace(',', '')), 'EUR'

    # Pattern: $XX or $XX.XX
    m = re.match(r'\$([\d,.]+)', fv_str)
    if m:
        return float(m.group(1).replace(',', '')), 'USD'

    # Pattern: XXX GBp
    m = re.match(r'([\d,.]+)\s*GBp', fv_str)
    if m:
        return float(m.group(1).replace(',', '')), 'GBp'

    # Pattern: XXX SEK
    m = re.match(r'([\d,.]+)\s*SEK', fv_str)
    if m:
        return float(m.group(1).replace(',', '')), 'SEK'

    # Pattern: XXX DKK
    m = re.match(r'([\d,.]+)\s*DKK', fv_str)
    if m:
        return float(m.group(1).replace(',', '')), 'DKK'

    # Generic number at start (assume USD)
    m = re.match(r'([\d,.]+)', fv_str)
    if m:
        return float(m.group(1).replace(',', '')), 'USD'

    return None, 'USD'


# ==============================================================================
# Price Fetching
# ==============================================================================

def fetch_prices(tickers: List[str]) -> Dict[str, Dict]:
    """Fetch current prices for a list of tickers via yfinance."""
    results = {}
    for ticker in tickers:
        try:
            info = yf.Ticker(ticker).info
            price = info.get('currentPrice') or info.get('regularMarketPrice') or info.get('previousClose')
            currency = info.get('currency', 'USD')
            if price and price > 0:
                results[ticker] = {'price': price, 'currency': currency}
        except Exception as e:
            print(f"  WARN: Could not fetch {ticker}: {e}", file=sys.stderr)
    return results


# ==============================================================================
# Decision Extraction
# ==============================================================================

def extract_decisions(decisions_data: Dict) -> List[Dict]:
    """Extract all decisions into a flat list with normalized fields."""
    all_decisions = []

    # Sizing decisions (BUY/ADD)
    for d in decisions_data.get('sizing_decisions', []):
        entry = {
            'date': str(d.get('date', '')),
            'ticker': d.get('ticker', ''),
            'action': d.get('action', 'BUY'),
            'sizing': d.get('sizing', ''),
            'quality_score': d.get('context', {}).get('quality_score'),
            'tier': d.get('context', {}).get('tier'),
            'mos': d.get('context', {}).get('mos', ''),
            'conviction': d.get('context', {}).get('conviction', ''),
            'reasoning': d.get('reasoning', ''),
            'outcome': d.get('outcome', ''),
            'ecagr_3yr': d.get('context', {}).get('ecagr_3yr'),
            'category': 'sizing',
        }
        all_decisions.append(entry)

    # Trim/Sell decisions
    for d in decisions_data.get('trim_decisions', []):
        entry = {
            'date': str(d.get('date', '')),
            'ticker': d.get('ticker', ''),
            'action': d.get('action', 'SELL'),
            'sizing': d.get('context', {}).get('position_size', ''),
            'quality_score': d.get('context', {}).get('quality_score'),
            'tier': d.get('context', {}).get('tier'),
            'mos': d.get('context', {}).get('mos', ''),
            'conviction': '',
            'pnl': d.get('context', {}).get('pnl', ''),
            'reasoning': d.get('reasoning', ''),
            'outcome': d.get('outcome', ''),
            'category': 'trim_sell',
        }
        all_decisions.append(entry)

    # Hold decisions
    for d in decisions_data.get('hold_decisions', []):
        entry = {
            'date': str(d.get('date', '')),
            'ticker': d.get('ticker', ''),
            'action': d.get('action', 'HOLD'),
            'quality_score': d.get('context', {}).get('quality_score'),
            'tier': d.get('context', {}).get('tier'),
            'mos': d.get('context', {}).get('mos', ''),
            'conviction': '',
            'reasoning': d.get('reasoning', ''),
            'outcome': d.get('outcome', ''),
            'category': 'hold',
        }
        all_decisions.append(entry)

    # Short decisions
    for d in decisions_data.get('short_decisions', []):
        entry = {
            'date': str(d.get('date', '')),
            'ticker': d.get('ticker', ''),
            'action': d.get('action', 'SHORT'),
            'quality_score': d.get('context', {}).get('quality_score'),
            'tier': d.get('context', {}).get('tier'),
            'reasoning': d.get('reasoning', ''),
            'outcome': d.get('outcome', ''),
            'category': 'short',
        }
        all_decisions.append(entry)

    # Geography decisions (standing orders)
    for d in decisions_data.get('geography_decisions', []):
        if d.get('ticker'):
            entry = {
                'date': str(d.get('date', '')),
                'ticker': d.get('ticker', ''),
                'action': d.get('action', 'STANDING ORDER'),
                'sizing': d.get('sizing', ''),
                'quality_score': d.get('context', {}).get('quality_score'),
                'tier': d.get('context', {}).get('tier'),
                'mos': d.get('context', {}).get('mos', ''),
                'conviction': d.get('context', {}).get('conviction', ''),
                'reasoning': d.get('reasoning', ''),
                'outcome': d.get('outcome', ''),
                'category': 'geography_so',
            }
            all_decisions.append(entry)

    return all_decisions


def build_active_position_map(portfolio_data: Dict) -> Dict[str, Dict]:
    """Build a map of active positions from current.yaml."""
    positions = {}
    for p in portfolio_data.get('positions', []):
        ticker = p.get('ticker', '')
        fv_val, fv_currency = parse_fv_from_string(str(p.get('fair_value', '')))
        positions[ticker] = {
            'shares': p.get('shares', 0),
            'avg_cost_usd': p.get('avg_cost_usd', 0),
            'invested_usd': p.get('invested_usd', 0),
            'date_opened': str(p.get('date_opened', '')),
            'conviction': p.get('conviction', ''),
            'fair_value': fv_val,
            'fv_currency': fv_currency,
            'fair_value_raw': str(p.get('fair_value', '')),
        }
    return positions


def build_closed_position_map(history_data: Dict) -> Dict[str, List[Dict]]:
    """Build a map of closed positions from history.yaml (may have multiple per ticker)."""
    closed = {}
    for p in history_data.get('closed_positions', []):
        ticker = p.get('ticker', '')
        if not ticker:
            continue
        if ticker not in closed:
            closed[ticker] = []
        closed[ticker].append({
            'entry_date': str(p.get('entry_date', '')),
            'exit_date': str(p.get('exit_date', '')),
            'entry_price': p.get('entry_price', p.get('entry_price_gbp', p.get('entry_price_usd', 0))),
            'exit_price': p.get('exit_price', p.get('exit_price_gbp', p.get('exit_price_usd', 0))),
            'entry_currency': p.get('entry_currency', 'USD'),
            'pnl_percent': p.get('pnl_percent', 0),
            'pnl_amount_eur': p.get('pnl_amount_eur', p.get('pnl_amount', 0)),
            'holding_days': p.get('holding_days', 0),
            'quality_score': p.get('quality_score'),
            'thesis_fv_at_entry': p.get('thesis_fv_at_entry'),
            'thesis_fv_adversarial': p.get('thesis_fv_adversarial', p.get('thesis_fv_v3', p.get('thesis_fv_v2'))),
            'exit_reason': p.get('exit_reason', ''),
            'fv_reached': p.get('fv_reached', False),
            'lesson_learned': p.get('lesson_learned', ''),
        })
    return closed


def build_adversarial_tracking(history_data: Dict) -> Dict[str, Dict]:
    """Build map from adversarial FV tracking section."""
    tracking = {}
    afv = history_data.get('adversarial_fv_tracking', {})
    for entry in afv.get('positions_to_track', []):
        ticker = entry.get('ticker', '')
        if ticker:
            tracking[ticker] = entry
    return tracking


# ==============================================================================
# Currency-to-USD conversion helper
# ==============================================================================

def to_usd(price: float, currency: str, rates: Dict[str, float]) -> float:
    """Convert price to USD for P&L comparison (avg_cost stored in USD)."""
    if currency == 'USD':
        return price
    elif currency in ('GBp', 'GBX'):
        return (price / 100) * rates['GBPEUR'] * rates['EURUSD']
    elif currency == 'GBP':
        return price * rates['GBPEUR'] * rates['EURUSD']
    elif currency == 'EUR':
        return price * rates['EURUSD']
    elif currency == 'DKK':
        return price * rates['DKKEUR'] * rates['EURUSD']
    elif currency == 'CHF':
        return price * rates['CHFEUR'] * rates['EURUSD']
    return price


# ==============================================================================
# Report: Decision Outcomes
# ==============================================================================

def print_decision_outcomes(decisions: List[Dict], active_map: Dict, closed_map: Dict,
                            prices: Dict, rates: Dict, filter_action: Optional[str] = None,
                            filter_ticker: Optional[str] = None):
    """Print decision outcome tracker."""
    print("=" * 110)
    print("DECISION OUTCOMES")
    print("=" * 110)
    print()

    # Filter decisions
    filtered = decisions
    if filter_action:
        if filter_action == 'BUY':
            filtered = [d for d in filtered if d['action'] in ('BUY', 'ADD')]
        elif filter_action == 'SELL':
            filtered = [d for d in filtered if 'SELL' in str(d['action']).upper() or 'TRIM' in str(d['action']).upper()]
        else:
            filtered = [d for d in filtered if filter_action.upper() in str(d['action']).upper()]
    if filter_ticker:
        filtered = [d for d in filtered if d['ticker'].upper() == filter_ticker.upper()]

    if not filtered:
        print("  No matching decisions found.")
        print()
        return

    # Sort by date
    filtered.sort(key=lambda x: x['date'])

    print(f"{'Date':<12} {'Ticker':<10} {'Action':<12} {'QS':>4} {'Tier':>5} {'Conviction':<8} {'Return':>8} {'Hold':>6} {'Verdict':<10}")
    print("-" * 110)

    winners = 0
    losers = 0
    open_count = 0
    winner_returns = []
    loser_returns = []
    all_returns = []

    for d in filtered:
        ticker = d['ticker']
        action = d['action']
        qs_str = str(d.get('quality_score', '')) if d.get('quality_score') else '-'
        # Truncate long QS strings (e.g. "48 tool / 70 adjusted (+22)")
        if len(qs_str) > 4:
            # Try to extract just the numeric part
            m = re.match(r'(\d+)', qs_str)
            qs_str = m.group(1) if m else qs_str[:4]
        tier_str = str(d.get('tier', '')) if d.get('tier') else '-'
        if len(tier_str) > 5:
            tier_str = tier_str[:1]  # Just keep first letter (A, B, C)
        conv_str = str(d.get('conviction', ''))[:7] if d.get('conviction') else '-'

        # Determine return
        return_str = '-'
        hold_str = '-'
        verdict = '-'

        if ticker in closed_map and action in ('BUY', 'ADD'):
            # Use closed position data
            closes = closed_map[ticker]
            # Find the closest close to this decision date
            best = None
            for c in closes:
                if c.get('entry_date', '') >= d['date'][:10] or not best:
                    best = c
            if best:
                pnl = best['pnl_percent']
                hold_days = best['holding_days']
                return_str = f"{pnl:+.1f}%"
                hold_str = f"{hold_days}d"
                if pnl > 1:
                    verdict = 'WINNER'
                    winners += 1
                    winner_returns.append(pnl)
                elif pnl < -1:
                    verdict = 'LOSER'
                    losers += 1
                    loser_returns.append(pnl)
                else:
                    verdict = 'FLAT'
                all_returns.append(pnl)

        elif ticker in active_map and action in ('BUY', 'ADD'):
            # Active position - compute return from current price
            pos = active_map[ticker]
            if ticker in prices:
                current_price = prices[ticker]['price']
                currency = prices[ticker]['currency']
                avg_cost_usd = pos['avg_cost_usd']
                if avg_cost_usd and avg_cost_usd > 0:
                    current_usd = to_usd(current_price, currency, rates)
                    pnl = (current_usd / avg_cost_usd - 1) * 100
                    entry_dt = parse_date(pos['date_opened'])
                    hold_days = (datetime.now() - entry_dt).days
                    return_str = f"{pnl:+.1f}%"
                    hold_str = f"{hold_days}d"
                    verdict = 'OPEN'
                    open_count += 1
                    all_returns.append(pnl)
                    if pnl > 1:
                        winner_returns.append(pnl)
                    elif pnl < -1:
                        loser_returns.append(pnl)

        elif 'SELL' in str(action).upper() or 'TRIM' in str(action).upper():
            # For sell decisions, show the P&L from closed_map or from the decision itself
            pnl_str = str(d.get('pnl', ''))
            if pnl_str:
                # Parse percentage from pnl string
                m = re.search(r'([+-]?\d+\.?\d*)%', pnl_str)
                if m:
                    pnl = float(m.group(1))
                    return_str = f"{pnl:+.1f}%"
                    all_returns.append(pnl)
                    if pnl > 1:
                        verdict = 'GOOD EXIT'
                        winners += 1
                        winner_returns.append(pnl)
                    elif pnl < -1:
                        verdict = 'LOSS EXIT'
                        losers += 1
                        loser_returns.append(pnl)
                    else:
                        verdict = 'FLAT EXIT'
                else:
                    return_str = pnl_str[:8]
                    verdict = 'CLOSED'
            elif ticker in closed_map:
                closes = closed_map[ticker]
                if closes:
                    best = closes[-1]
                    pnl = best['pnl_percent']
                    hold_days = best['holding_days']
                    return_str = f"{pnl:+.1f}%"
                    hold_str = f"{hold_days}d"
                    verdict = 'CLOSED'
            else:
                verdict = 'CLOSED'

        elif 'STANDING ORDER' in str(action).upper() or 'PAUSE' in str(action).upper():
            verdict = 'PENDING'

        print(f"{d['date']:<12} {ticker:<10} {str(action)[:11]:<12} {qs_str:>4} {tier_str:>5} {conv_str:<8} {return_str:>8} {hold_str:>6} {verdict:<10}")

    # Summary
    total_decided = winners + losers + open_count
    print()
    print("-" * 110)
    print(f"Total decisions shown: {len(filtered)}")
    if total_decided > 0:
        hit_rate = winners / (winners + losers) * 100 if (winners + losers) > 0 else 0
        avg_win = sum(winner_returns) / len(winner_returns) if winner_returns else 0
        avg_loss = sum(loser_returns) / len(loser_returns) if loser_returns else 0
        profit_factor = abs(avg_win / avg_loss) if avg_loss != 0 else float('inf')
        avg_all = sum(all_returns) / len(all_returns) if all_returns else 0

        print(f"Closed: {winners} winners, {losers} losers | Open: {open_count}")
        if winners + losers > 0:
            print(f"Hit rate (closed): {hit_rate:.0f}%")
        print(f"Avg winner: {avg_win:+.1f}% | Avg loser: {avg_loss:+.1f}% | Profit factor: {profit_factor:.2f}")
        print(f"Avg return (all): {avg_all:+.1f}%")
    print()


# ==============================================================================
# Report: Fair Value Accuracy
# ==============================================================================

def print_fv_accuracy(active_map: Dict, closed_map: Dict, adversarial_map: Dict,
                       prices: Dict, rates: Dict):
    """Print Fair Value calibration analysis."""
    print("=" * 110)
    print("FAIR VALUE CALIBRATION")
    print("=" * 110)
    print()

    rows = []

    # Active positions: FV from current.yaml vs current price
    for ticker, pos in active_map.items():
        fv = pos.get('fair_value')
        fv_currency = pos.get('fv_currency', 'USD')
        if fv is None or fv <= 0:
            continue
        if ticker not in prices:
            continue

        current_price = prices[ticker]['price']
        price_currency = prices[ticker]['currency']

        # Convert both to EUR for comparison
        fv_eur = to_eur(fv, fv_currency, rates)
        price_eur = to_eur(current_price, price_currency, rates)
        avg_cost_eur = to_eur(pos['avg_cost_usd'], 'USD', rates) if pos.get('avg_cost_usd') else None

        if price_eur <= 0 or fv_eur <= 0:
            continue

        # FV gap
        fv_gap_pct = (fv_eur - price_eur) / price_eur * 100

        # Direction: is price moving toward or away from FV?
        if avg_cost_eur and avg_cost_eur > 0:
            entry_distance = abs(fv_eur - avg_cost_eur)
            current_distance = abs(fv_eur - price_eur)
            if current_distance < entry_distance * 0.95:
                direction = 'TOWARD'
            elif current_distance > entry_distance * 1.05:
                direction = 'AWAY'
            else:
                direction = 'FLAT'
        else:
            direction = '?'

        fv_display = fmt_price(fv, fv_currency)
        price_display = fmt_price(current_price, price_currency)

        rows.append({
            'ticker': ticker,
            'fv_display': fv_display,
            'price_display': price_display,
            'fv_gap_pct': fv_gap_pct,
            'direction': direction,
            'status': 'ACTIVE',
        })

    # Closed positions: compare thesis FV vs current price (was FV ever right?)
    for ticker, closes in closed_map.items():
        for c in closes:
            thesis_fv = c.get('thesis_fv_at_entry')
            exit_price = c.get('exit_price', 0)
            entry_currency = c.get('entry_currency', 'USD')

            if not thesis_fv or thesis_fv <= 0:
                continue

            # Get current price to see if FV was eventually right
            if ticker in prices:
                current_price = prices[ticker]['price']
                price_currency = prices[ticker]['currency']

                # Convert to EUR for comparison
                fv_eur = to_eur(thesis_fv, entry_currency, rates)
                current_eur = to_eur(current_price, price_currency, rates)
                exit_eur = to_eur(exit_price, entry_currency, rates)

                if fv_eur <= 0 or current_eur <= 0:
                    continue

                fv_gap_pct = (fv_eur - current_eur) / current_eur * 100

                # Was the sell right? Compare exit price vs current price
                if exit_eur > 0:
                    post_sell_return = (current_eur / exit_eur - 1) * 100
                    if post_sell_return > 5:
                        direction = 'SOLD TOO EARLY'
                    elif post_sell_return < -5:
                        direction = 'GOOD SELL'
                    else:
                        direction = 'NEUTRAL'
                else:
                    direction = '?'

                fv_display = fmt_price(thesis_fv, entry_currency)
                price_display = fmt_price(current_price, price_currency)

                rows.append({
                    'ticker': f"{ticker} (sold)",
                    'fv_display': fv_display,
                    'price_display': price_display,
                    'fv_gap_pct': fv_gap_pct,
                    'direction': direction,
                    'status': 'CLOSED',
                    'post_sell_return': post_sell_return if exit_eur > 0 else None,
                })

    if not rows:
        print("  No FV data available for analysis.")
        print()
        return

    # Print table
    print(f"{'Ticker':<18} {'FV@Decision':>12} {'Current':>12} {'FV Gap':>8} {'Direction':<15} {'Status':<8}")
    print("-" * 110)

    for r in sorted(rows, key=lambda x: x['fv_gap_pct'], reverse=True):
        print(f"{r['ticker']:<18} {r['fv_display']:>12} {r['price_display']:>12} {r['fv_gap_pct']:>+7.1f}% {r['direction']:<15} {r['status']:<8}")

    # Systematic bias analysis
    print()
    print("SYSTEMATIC BIAS ANALYSIS")
    print("-" * 60)

    active_rows = [r for r in rows if r['status'] == 'ACTIVE']
    closed_rows = [r for r in rows if r['status'] == 'CLOSED']

    if active_rows:
        avg_fv_gap = sum(r['fv_gap_pct'] for r in active_rows) / len(active_rows)
        toward = sum(1 for r in active_rows if r['direction'] == 'TOWARD')
        away = sum(1 for r in active_rows if r['direction'] == 'AWAY')
        flat = sum(1 for r in active_rows if r['direction'] == 'FLAT')
        total_active = len(active_rows)

        print(f"  Active positions ({total_active}):")
        print(f"    Avg FV gap vs current price: {avg_fv_gap:+.1f}% (FV {'above' if avg_fv_gap > 0 else 'below'} market)")
        print(f"    Moving TOWARD FV: {toward}/{total_active} ({toward/total_active*100:.0f}%)")
        print(f"    Moving AWAY from FV: {away}/{total_active} ({away/total_active*100:.0f}%)")
        print(f"    FLAT: {flat}/{total_active}")
        print()
        if total_active >= 3:
            if away > toward and away / total_active > 0.6:
                print(f"    >> FVs may be systematically OPTIMISTIC (>60% moving away)")
            elif toward > away and toward / total_active > 0.6:
                print(f"    >> FVs appear WELL-CALIBRATED (>60% moving toward)")
            else:
                print(f"    >> Mixed signals - no clear systematic bias")

    if closed_rows:
        sold_too_early = sum(1 for r in closed_rows if r['direction'] == 'SOLD TOO EARLY')
        good_sell = sum(1 for r in closed_rows if r['direction'] == 'GOOD SELL')
        neutral_sell = sum(1 for r in closed_rows if r['direction'] == 'NEUTRAL')
        total_closed = len(closed_rows)

        post_sell_returns = [r['post_sell_return'] for r in closed_rows if r.get('post_sell_return') is not None]
        avg_post_sell = sum(post_sell_returns) / len(post_sell_returns) if post_sell_returns else 0

        print()
        print(f"  Closed positions ({total_closed}):")
        print(f"    Avg post-sell return (if held): {avg_post_sell:+.1f}%")
        print(f"    Sold too early (>5% post-sell gain): {sold_too_early}/{total_closed}")
        print(f"    Good sell (>5% post-sell decline): {good_sell}/{total_closed}")
        print(f"    Neutral (<5% move): {neutral_sell}/{total_closed}")
        if total_closed >= 3:
            if sold_too_early > good_sell:
                print(f"    >> Sell timing may be TOO AGGRESSIVE (more stocks recovered after sell)")
            elif good_sell > sold_too_early:
                print(f"    >> Sell timing appears WELL-CALIBRATED (most continued declining)")
            else:
                print(f"    >> Mixed sell timing signals")

    print()


# ==============================================================================
# Report: Pattern Analysis
# ==============================================================================

def print_pattern_analysis(decisions: List[Dict], active_map: Dict, closed_map: Dict,
                            prices: Dict, rates: Dict):
    """Print pattern analysis: conviction vs outcome, QS vs outcome, time-to-profit."""
    print("=" * 110)
    print("PATTERN ANALYSIS")
    print("=" * 110)
    print()

    # Only analyze BUY/ADD decisions that have outcomes
    buy_decisions = [d for d in decisions if d['action'] in ('BUY', 'ADD')]

    # Compute returns for each buy decision
    buy_with_returns = []
    for d in buy_decisions:
        ticker = d['ticker']
        pnl = None

        if ticker in closed_map:
            closes = closed_map[ticker]
            if closes:
                pnl = closes[-1]['pnl_percent']

        elif ticker in active_map and ticker in prices:
            pos = active_map[ticker]
            if pos.get('avg_cost_usd') and pos['avg_cost_usd'] > 0:
                current_price = prices[ticker]['price']
                currency = prices[ticker]['currency']
                current_usd = to_usd(current_price, currency, rates)
                pnl = (current_usd / pos['avg_cost_usd'] - 1) * 100

        if pnl is not None:
            buy_with_returns.append({
                'ticker': ticker,
                'conviction': str(d.get('conviction', '')).lower(),
                'quality_score': d.get('quality_score'),
                'tier': str(d.get('tier', '')),
                'mos': d.get('mos', ''),
                'pnl': pnl,
                'date': d['date'],
                'action': d['action'],
            })

    if not buy_with_returns:
        print("  Insufficient data for pattern analysis.")
        print()
        return

    # --- By Conviction ---
    print("BY CONVICTION AT ENTRY")
    print("-" * 60)
    conviction_groups = {}
    for b in buy_with_returns:
        conv = b['conviction']
        if 'alta' in conv or 'high' in conv:
            bucket = 'HIGH'
        elif 'media' in conv or 'medium' in conv:
            bucket = 'MEDIUM'
        elif 'baja' in conv or 'low' in conv:
            bucket = 'LOW'
        else:
            bucket = 'UNKNOWN'
        if bucket not in conviction_groups:
            conviction_groups[bucket] = []
        conviction_groups[bucket].append(b)

    for conv_level in ['HIGH', 'MEDIUM', 'LOW', 'UNKNOWN']:
        if conv_level in conviction_groups:
            group = conviction_groups[conv_level]
            returns = [g['pnl'] for g in group]
            avg_ret = sum(returns) / len(returns)
            hit_rate = sum(1 for r in returns if r > 1) / len(returns) * 100
            tickers = [g['ticker'] for g in group]
            print(f"  {conv_level}: avg return {avg_ret:+.1f}%, hit rate {hit_rate:.0f}%, n={len(group)} ({', '.join(tickers)})")
    print()

    # --- By Quality Score ---
    print("BY QUALITY SCORE AT ENTRY")
    print("-" * 60)
    tier_groups = {'A (75+)': [], 'B (55-74)': [], 'C (35-54)': [], 'Unknown': []}
    for b in buy_with_returns:
        qs = b.get('quality_score')
        qs_num = None
        if qs is not None:
            try:
                qs_num = int(str(qs).split('-')[0].split('/')[0].strip())
            except (ValueError, IndexError):
                pass

        tier = b.get('tier', '')
        if (qs_num is not None and qs_num >= 75) or (tier and str(tier).upper() == 'A'):
            tier_groups['A (75+)'].append(b)
        elif (qs_num is not None and qs_num >= 55) or (tier and str(tier).upper() == 'B'):
            tier_groups['B (55-74)'].append(b)
        elif (qs_num is not None and qs_num >= 35) or (tier and str(tier).upper() == 'C'):
            tier_groups['C (35-54)'].append(b)
        else:
            tier_groups['Unknown'].append(b)

    for tier_label in ['A (75+)', 'B (55-74)', 'C (35-54)', 'Unknown']:
        group = tier_groups[tier_label]
        if group:
            returns = [g['pnl'] for g in group]
            avg_ret = sum(returns) / len(returns)
            hit_rate = sum(1 for r in returns if r > 1) / len(returns) * 100
            tickers = [g['ticker'] for g in group]
            print(f"  {tier_label}: avg return {avg_ret:+.1f}%, hit rate {hit_rate:.0f}%, n={len(group)} ({', '.join(tickers)})")
    print()

    # --- Time to Profit ---
    print("TIME TO PROFIT")
    print("-" * 60)
    active_returns = []
    for ticker, pos in active_map.items():
        if ticker in prices and pos.get('avg_cost_usd') and pos['avg_cost_usd'] > 0:
            current_price = prices[ticker]['price']
            currency = prices[ticker]['currency']
            current_usd = to_usd(current_price, currency, rates)
            pnl = (current_usd / pos['avg_cost_usd'] - 1) * 100
            entry_dt = parse_date(pos['date_opened'])
            hold_days = (datetime.now() - entry_dt).days
            active_returns.append({
                'ticker': ticker,
                'pnl': pnl,
                'hold_days': hold_days,
                'profitable': pnl > 0,
            })

    profitable = [a for a in active_returns if a['profitable']]
    underwater = [a for a in active_returns if not a['profitable']]

    if active_returns:
        print(f"  Active positions: {len(profitable)} profitable, {len(underwater)} underwater")
        if profitable:
            avg_days_profitable = sum(a['hold_days'] for a in profitable) / len(profitable)
            print(f"  Avg holding of profitable positions: {avg_days_profitable:.0f} days")
        if underwater:
            avg_loss_underwater = sum(a['pnl'] for a in underwater) / len(underwater)
            print(f"  Avg loss of underwater positions: {avg_loss_underwater:+.1f}%")
            for u in sorted(underwater, key=lambda x: x['pnl']):
                print(f"    {u['ticker']}: {u['pnl']:+.1f}% ({u['hold_days']}d)")
    print()

    # --- Sell Accuracy ---
    print("SELL ACCURACY (closed positions)")
    print("-" * 60)
    sell_accuracy_rows = []
    for ticker, closes in closed_map.items():
        for c in closes:
            exit_price = c.get('exit_price', 0)
            entry_currency = c.get('entry_currency', 'USD')
            pnl_at_sell = c.get('pnl_percent', 0)

            if ticker in prices and exit_price and exit_price > 0:
                current_price = prices[ticker]['price']
                price_currency = prices[ticker]['currency']

                exit_eur = to_eur(exit_price, entry_currency, rates)
                current_eur = to_eur(current_price, price_currency, rates)

                if exit_eur > 0:
                    return_if_held = (current_eur / exit_eur - 1) * 100
                    sell_accuracy_rows.append({
                        'ticker': ticker,
                        'pnl_at_sell': pnl_at_sell,
                        'return_if_held': return_if_held,
                        'exit_date': c.get('exit_date', ''),
                    })

    if sell_accuracy_rows:
        avg_pnl_at_sell = sum(r['pnl_at_sell'] for r in sell_accuracy_rows) / len(sell_accuracy_rows)
        avg_if_held = sum(r['return_if_held'] for r in sell_accuracy_rows) / len(sell_accuracy_rows)

        print(f"  Avg return at sell: {avg_pnl_at_sell:+.1f}%")
        print(f"  Avg return if held to today: {avg_if_held:+.1f}% (from exit price)")
        if avg_if_held > avg_pnl_at_sell + 5:
            print(f"  >> SELLING TOO EARLY: stocks gained {avg_if_held - avg_pnl_at_sell:+.1f}% more after sell")
        elif avg_if_held < avg_pnl_at_sell - 5:
            print(f"  >> GOOD TIMING: stocks declined further after sell")
        else:
            print(f"  >> NEUTRAL timing")

        print()
        print(f"  {'Ticker':<12} {'P&L@Sell':>9} {'If Held':>9} {'Delta':>9} {'Verdict':<15}")
        print(f"  {'-'*55}")
        for r in sorted(sell_accuracy_rows, key=lambda x: x['return_if_held'], reverse=True):
            delta = r['return_if_held'] - r['pnl_at_sell']
            if r['return_if_held'] > 5:
                v = 'SOLD TOO EARLY'
            elif r['return_if_held'] < -5:
                v = 'GOOD SELL'
            else:
                v = 'NEUTRAL'
            print(f"  {r['ticker']:<12} {r['pnl_at_sell']:>+8.1f}% {r['return_if_held']:>+8.1f}% {delta:>+8.1f}% {v:<15}")
    else:
        print("  No closed positions with current price data available.")
    print()


# ==============================================================================
# Main
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Decision Feedback - Meta-learning calibration engine',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 tools/decision_feedback.py                    # Full calibration report
  python3 tools/decision_feedback.py --buys             # Only BUY decisions
  python3 tools/decision_feedback.py --sells            # Only SELL decisions
  python3 tools/decision_feedback.py --fv-accuracy      # Fair Value accuracy analysis
  python3 tools/decision_feedback.py --ticker ADBE      # Specific ticker history
  python3 tools/decision_feedback.py --patterns         # Pattern analysis only
        """)
    parser.add_argument('--buys', action='store_true', help='Show only BUY/ADD decisions')
    parser.add_argument('--sells', action='store_true', help='Show only SELL/TRIM decisions')
    parser.add_argument('--fv-accuracy', action='store_true', help='Fair Value accuracy analysis')
    parser.add_argument('--ticker', type=str, help='Filter by specific ticker')
    parser.add_argument('--patterns', action='store_true', help='Pattern analysis only')

    args = parser.parse_args()

    show_all = not any([args.buys, args.sells, args.fv_accuracy, args.patterns, args.ticker])

    # Load data
    print("Loading decision data...")
    decisions_data = load_yaml(DECISIONS_FILE)
    portfolio_data = load_yaml(PORTFOLIO_FILE)
    history_data = load_yaml(HISTORY_FILE)

    decisions = extract_decisions(decisions_data)
    active_map = build_active_position_map(portfolio_data)
    closed_map = build_closed_position_map(history_data)
    adversarial_map = build_adversarial_tracking(history_data)

    # Collect all tickers that need price fetching
    all_tickers = set()
    for d in decisions:
        if d.get('ticker'):
            all_tickers.add(d['ticker'])
    for t in active_map:
        all_tickers.add(t)
    for t in closed_map:
        all_tickers.add(t)

    print(f"Fetching prices for {len(all_tickers)} tickers...")
    rates = get_fx_rates()
    print(f"FX: EUR/USD={rates['EURUSD']:.4f} | GBP/EUR={rates['GBPEUR']:.4f}")
    prices = fetch_prices(list(all_tickers))
    print(f"Got prices for {len(prices)}/{len(all_tickers)} tickers")
    print()

    # Output sections
    # --ticker alone shows all decision types for that ticker
    ticker_only = args.ticker and not any([args.buys, args.sells, args.fv_accuracy, args.patterns])

    if show_all or args.buys or ticker_only:
        filter_action = 'BUY' if args.buys else None
        print_decision_outcomes(decisions, active_map, closed_map, prices, rates,
                                filter_action=filter_action, filter_ticker=args.ticker)

    if args.sells:
        print_decision_outcomes(decisions, active_map, closed_map, prices, rates,
                                filter_action='SELL', filter_ticker=args.ticker)

    if show_all or args.fv_accuracy:
        print_fv_accuracy(active_map, closed_map, adversarial_map, prices, rates)

    if show_all or args.patterns:
        print_pattern_analysis(decisions, active_map, closed_map, prices, rates)

    print("=" * 110)
    print(f"Report generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("[Raw data. Decision feedback for calibration.]")
    print("=" * 110)


if __name__ == '__main__':
    main()
