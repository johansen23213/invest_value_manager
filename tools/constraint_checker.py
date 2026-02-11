#!/usr/bin/env python3
"""
Portfolio Context Tool - Raw data for principled decision-making.

Framework v4.0: This tool outputs DATA. The reasoning comes from YOU
applying principles (learning/principles.md) to this data.

The tool does NOT tell you what questions to ask or what to think.
That would be rules disguised as questions.

Usage:
  python3 tools/constraint_checker.py REPORT
  python3 tools/constraint_checker.py REPORT --drawdown 30     # Custom drawdown %
  python3 tools/constraint_checker.py CHECK TICKER AMOUNT_EUR
  python3 tools/constraint_checker.py CHECK TICKER AMOUNT_EUR --drawdown 30
"""
import sys
import os
import yaml

try:
    import yfinance as yf
except ImportError:
    print("ERROR: yfinance not installed. Run: pip install yfinance")
    sys.exit(1)

# ─── Mappings ────────────────────────────────────────────────────────────────

SECTOR_MAP = {
    'LIGHT.AS': 'Technology', 'HPQ': 'Technology', 'ADBE': 'Technology',
    'PFE': 'Healthcare', 'SAN.PA': 'Healthcare', 'UHS': 'Healthcare', 'NVO': 'Healthcare',
    'ALL': 'Financial Services', 'GL': 'Financial Services', 'EDEN.PA': 'Financial Services', 'MONY.L': 'Financial Services',
    'VICI': 'Real Estate', 'VNA.DE': 'Real Estate',
    'DTE.DE': 'Telecom',
    'SHEL.L': 'Energy',
    'IMB.L': 'Consumer Staples', 'TATE.L': 'Consumer Staples',
    'DOM.L': 'Consumer Cyclical',
    'TEP.PA': 'Industrials',
    'A2A.MI': 'Utilities',
    'HRB': 'Financial Services',
}

GEO_MAP = {
    'PFE': 'US', 'ALL': 'US', 'VICI': 'US', 'UHS': 'US', 'GL': 'US', 'HPQ': 'US', 'HRB': 'US', 'ADBE': 'US',
    'SHEL.L': 'UK', 'IMB.L': 'UK', 'TATE.L': 'UK', 'DOM.L': 'UK', 'MONY.L': 'UK',
    'DTE.DE': 'EU', 'TEP.PA': 'EU', 'SAN.PA': 'EU', 'LIGHT.AS': 'EU',
    'A2A.MI': 'EU', 'EDEN.PA': 'EU', 'VNA.DE': 'EU',
    'NVO': 'EU',
}

# ─── Helpers ─────────────────────────────────────────────────────────────────

def load_portfolio():
    path = os.path.join(os.path.dirname(__file__), '..', 'portfolio', 'current.yaml')
    with open(path) as f:
        return yaml.safe_load(f)

def get_fx_rates():
    defaults = {'EURUSD': 1.04, 'GBPEUR': 1.19}
    fallbacks_used = []

    try:
        eurusd = yf.Ticker('EURUSD=X').info.get('previousClose')
        if not eurusd:
            eurusd = defaults['EURUSD']
            fallbacks_used.append(f"EUR/USD={eurusd}")
    except Exception:
        eurusd = defaults['EURUSD']
        fallbacks_used.append(f"EUR/USD={eurusd}")
    try:
        gbpeur = yf.Ticker('GBPEUR=X').info.get('previousClose')
        if not gbpeur:
            gbpeur = defaults['GBPEUR']
            fallbacks_used.append(f"GBP/EUR={gbpeur}")
    except Exception:
        gbpeur = defaults['GBPEUR']
        fallbacks_used.append(f"GBP/EUR={gbpeur}")

    if fallbacks_used:
        print(f"FX WARNING: Using static fallback rates ({', '.join(fallbacks_used)}). "
              f"EUR amounts may be inaccurate.")

    return eurusd, gbpeur

def get_current_value_eur(ticker, shares, invested_usd, eurusd, gbpeur):
    try:
        info = yf.Ticker(ticker).info
        price = info.get('currentPrice') or info.get('regularMarketPrice') or info.get('previousClose')
        currency = info.get('currency', 'USD')
        if price is None:
            raise ValueError("No price")
        if currency == 'USD':
            return price * shares / eurusd
        elif currency in ('GBp', 'GBX'):
            return (price / 100) * shares * gbpeur
        elif currency == 'GBP':
            return price * shares * gbpeur
        elif currency == 'EUR':
            return price * shares
        else:
            return price * shares / eurusd
    except Exception:
        return invested_usd / eurusd

def guess_sector(ticker):
    try:
        s = yf.Ticker(ticker).info.get('sector', 'Unknown')
        return s if s else 'Unknown'
    except Exception:
        return 'Unknown'

def guess_geo(ticker):
    if ticker.endswith('.L'):
        return 'UK'
    eu_suffixes = ('.DE', '.PA', '.MI', '.NV', '.AS', '.BR', '.MC', '.HE', '.ST', '.OL')
    if any(ticker.endswith(s) for s in eu_suffixes):
        return 'EU'
    return 'US'

# ─── Core Logic ──────────────────────────────────────────────────────────────

def build_portfolio_state(portfolio, eurusd, gbpeur):
    cash_eur = portfolio['cash']['amount']
    positions = portfolio.get('positions', [])

    pos_data = []
    for p in positions:
        ticker = p['ticker']
        val_eur = get_current_value_eur(ticker, p['shares'], p['invested_usd'], eurusd, gbpeur)
        sector = SECTOR_MAP.get(ticker, guess_sector(ticker))
        geo = GEO_MAP.get(ticker, guess_geo(ticker))
        pos_data.append({
            'ticker': ticker,
            'value_eur': val_eur,
            'sector': sector,
            'geo': geo,
        })

    total_invested = sum(pd['value_eur'] for pd in pos_data)
    total = total_invested + cash_eur

    return {
        'positions': pos_data,
        'cash_eur': cash_eur,
        'total_eur': total,
        'num_positions': len(pos_data),
    }

def analyze_context(state, new_ticker=None, amount_eur=0):
    pos_list = [dict(p) for p in state['positions']]
    cash = state['cash_eur']
    total = state['total_eur']
    num_pos = state['num_positions']

    if new_ticker and amount_eur > 0:
        existing = [p for p in pos_list if p['ticker'] == new_ticker]
        new_sector = SECTOR_MAP.get(new_ticker, guess_sector(new_ticker))
        new_geo = GEO_MAP.get(new_ticker, guess_geo(new_ticker))
        if existing:
            existing[0]['value_eur'] += amount_eur
        else:
            pos_list.append({
                'ticker': new_ticker,
                'value_eur': amount_eur,
                'sector': new_sector,
                'geo': new_geo,
            })
            num_pos += 1
        cash -= amount_eur
        total = sum(p['value_eur'] for p in pos_list) + cash

    sector_totals = {}
    for p in pos_list:
        sector_totals[p['sector']] = sector_totals.get(p['sector'], 0) + p['value_eur']

    geo_totals = {}
    for p in pos_list:
        geo_totals[p['geo']] = geo_totals.get(p['geo'], 0) + p['value_eur']

    return pos_list, sector_totals, geo_totals, cash, total, num_pos

def print_report(state, drawdown_pct=50):
    pos_list, sectors, geos, cash, total, num_pos = analyze_context(state)

    print("=" * 60)
    print("PORTFOLIO DATA")
    print("=" * 60)

    # Positions
    dd_label = f"{drawdown_pct}% Impact"
    print(f"\n{'Ticker':<10} {'Sector':<18} {'Geo':>3} {'EUR':>8} {'%':>6} {dd_label:>10}")
    print("-" * 60)
    for p in sorted(pos_list, key=lambda x: -x['value_eur']):
        pct = (p['value_eur'] / total) * 100
        impact = pct * drawdown_pct / 100
        print(f"{p['ticker']:<10} {p['sector']:<18} {p['geo']:>3} {p['value_eur']:>8.0f} {pct:>5.1f}% {impact:>9.1f}%")
    print(f"{'CASH':<10} {'':<18} {'':<3} {cash:>8.0f} {(cash/total)*100:>5.1f}%")
    print("-" * 60)
    print(f"{'TOTAL':<10} {'':<18} {'':<3} {total:>8.0f}")

    # Sectors
    print(f"\n{'Sector':<22} {'EUR':>8} {'%':>6}")
    print("-" * 38)
    for sec, val in sorted(sectors.items(), key=lambda x: -x[1]):
        print(f"{sec:<22} {val:>8.0f} {(val/total)*100:>5.1f}%")

    # Geographies
    print(f"\n{'Geography':<22} {'EUR':>8} {'%':>6}")
    print("-" * 38)
    for geo, val in sorted(geos.items(), key=lambda x: -x[1]):
        print(f"{geo:<22} {val:>8.0f} {(val/total)*100:>5.1f}%")

    print(f"\nPositions: {num_pos} | Cash: {cash:.0f} EUR ({(cash/total)*100:.1f}%)")
    print("\n[Apply learning/principles.md to reason about this data]")

def print_check(state, ticker, amount_eur, drawdown_pct=50):
    print("=" * 60)
    print(f"SIMULATED: BUY {ticker} for {amount_eur:.0f} EUR")
    print("=" * 60)

    pos_list, sectors, geos, cash, total, num_pos = analyze_context(
        state, new_ticker=ticker, amount_eur=amount_eur
    )

    # Find the position
    for p in pos_list:
        if p['ticker'] == ticker:
            pct = (p['value_eur'] / total) * 100
            impact = pct * drawdown_pct / 100
            print(f"\n{ticker}: {p['value_eur']:.0f} EUR ({pct:.1f}%) | {drawdown_pct}% drop = -{impact:.1f}% portfolio")
            break

    sec = SECTOR_MAP.get(ticker, guess_sector(ticker))
    geo = GEO_MAP.get(ticker, guess_geo(ticker))

    print(f"Sector {sec}: {(sectors.get(sec,0)/total)*100:.1f}%")
    print(f"Geography {geo}: {(geos.get(geo,0)/total)*100:.1f}%")
    print(f"Cash after: {cash:.0f} EUR ({(cash/total)*100:.1f}%)")
    print(f"Positions: {num_pos}")
    print("\n[Apply learning/principles.md to reason about this data]")

# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    import argparse as _argparse

    parser = _argparse.ArgumentParser(description=__doc__,
                                       formatter_class=_argparse.RawDescriptionHelpFormatter)
    parser.add_argument('mode', choices=['REPORT', 'CHECK', 'report', 'check'],
                        help='REPORT for portfolio overview, CHECK for simulated buy')
    parser.add_argument('ticker', nargs='?', help='Ticker for CHECK mode')
    parser.add_argument('amount', nargs='?', type=float, help='Amount EUR for CHECK mode')
    parser.add_argument('--drawdown', type=float, default=50,
                        help='Drawdown %% for impact calculation (default: 50)')

    args = parser.parse_args()
    mode = args.mode.upper()

    portfolio = load_portfolio()
    print("Fetching data...")
    eurusd, gbpeur = get_fx_rates()
    print(f"FX: EUR/USD={eurusd:.4f} | GBP/EUR={gbpeur:.4f}\n")
    state = build_portfolio_state(portfolio, eurusd, gbpeur)

    if mode == 'REPORT':
        print_report(state, drawdown_pct=args.drawdown)
    elif mode == 'CHECK':
        if not args.ticker or args.amount is None:
            print("Usage: constraint_checker.py CHECK TICKER AMOUNT_EUR [--drawdown 30]")
            sys.exit(1)
        print_check(state, args.ticker, args.amount, drawdown_pct=args.drawdown)
    else:
        print(f"Unknown mode: {mode}")
        sys.exit(1)

if __name__ == '__main__':
    main()
