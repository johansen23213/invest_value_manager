#!/usr/bin/env python3
"""
Constraint Checker - Pre-validates BUY/ADD operations against portfolio constraints.
Prevents violations BEFORE recommending to the human.

Usage:
  python3 tools/constraint_checker.py CHECK TICKER AMOUNT_EUR
  python3 tools/constraint_checker.py CHECK TEP.PA 400
  python3 tools/constraint_checker.py REPORT
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
    'NVO': 'EU',  # Denmark, but EU for purposes of geo limits
}

# ─── Reference Points (Framework v4.0: ADVISORY, not limits) ─────────────────
# These are reference points for context, NOT hard limits.
# Decisions are made by reasoning from principles, not by checking numbers.
# See learning/principles.md for decision framework.

REFERENCE_POSITION_PCT = 7.0   # Typical max for Tier C; Tier A can be higher if justified
REFERENCE_SECTOR_PCT = 25.0   # Typical ceiling; can exceed with explicit reasoning
REFERENCE_GEO_PCT = 35.0      # Typical ceiling; depends on country risk assessment
REFERENCE_CASH_PCT = 5.0      # Typical floor; context determines appropriate level
REFERENCE_POSITIONS = 25      # No hard limit; depends on management capacity

# ─── Helpers ─────────────────────────────────────────────────────────────────

def load_portfolio():
    path = os.path.join(os.path.dirname(__file__), '..', 'portfolio', 'current.yaml')
    with open(path) as f:
        return yaml.safe_load(f)

def get_fx_rates():
    try:
        eurusd = yf.Ticker('EURUSD=X').info.get('previousClose', 1.04)
    except Exception:
        eurusd = 1.04
    try:
        gbpeur = yf.Ticker('GBPEUR=X').info.get('previousClose', 1.19)
    except Exception:
        gbpeur = 1.19
    return eurusd, gbpeur

def get_current_value_eur(ticker, shares, invested_usd, eurusd, gbpeur):
    """Get current market value in EUR. Falls back to invested_usd/eurusd on error."""
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
    """Try yfinance sector if not in hardcoded map."""
    try:
        s = yf.Ticker(ticker).info.get('sector', 'Unknown')
        return s if s else 'Unknown'
    except Exception:
        return 'Unknown'

def guess_geo(ticker):
    """Heuristic: .L = UK, .DE/.PA/.MI/.NV/.AS/.BR/.MC/.HE/.ST/.OL = EU, else US."""
    if ticker.endswith('.L'):
        return 'UK'
    eu_suffixes = ('.DE', '.PA', '.MI', '.NV', '.AS', '.BR', '.MC', '.HE', '.ST', '.OL')
    if any(ticker.endswith(s) for s in eu_suffixes):
        return 'EU'
    return 'US'

# ─── Core Logic ──────────────────────────────────────────────────────────────

def build_portfolio_state(portfolio, eurusd, gbpeur):
    """Returns dict with position values, sector/geo allocations, cash, total."""
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
            'name': p.get('name', ticker),
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

def check_constraints(state, new_ticker=None, amount_eur=0):
    """Check all constraints. If new_ticker/amount_eur provided, simulate purchase."""
    violations = []
    warnings = []

    pos_list = list(state['positions'])
    cash = state['cash_eur']
    total = state['total_eur']
    num_pos = state['num_positions']

    # Simulate purchase
    if new_ticker and amount_eur > 0:
        existing = [p for p in pos_list if p['ticker'] == new_ticker]
        new_sector = SECTOR_MAP.get(new_ticker, guess_sector(new_ticker))
        new_geo = GEO_MAP.get(new_ticker, guess_geo(new_ticker))
        if existing:
            existing[0]['value_eur'] += amount_eur
        else:
            pos_list.append({
                'ticker': new_ticker,
                'name': new_ticker,
                'value_eur': amount_eur,
                'sector': new_sector,
                'geo': new_geo,
            })
            num_pos += 1
        cash -= amount_eur

    # 1. Position sizing (ADVISORY - v4.0)
    for p in pos_list:
        pct = (p['value_eur'] / total) * 100 if total > 0 else 0
        if pct > REFERENCE_POSITION_PCT:
            warnings.append(f"POSITION {p['ticker']}: {pct:.1f}% above {REFERENCE_POSITION_PCT}% reference - requires reasoning")
        elif pct > REFERENCE_POSITION_PCT - 1:
            warnings.append(f"POSITION {p['ticker']}: {pct:.1f}% near {REFERENCE_POSITION_PCT}% reference")

    # 2. Sector concentration (ADVISORY - v4.0)
    sector_totals = {}
    for p in pos_list:
        sector_totals[p['sector']] = sector_totals.get(p['sector'], 0) + p['value_eur']
    for sec, val in sorted(sector_totals.items(), key=lambda x: -x[1]):
        pct = (val / total) * 100 if total > 0 else 0
        if pct > REFERENCE_SECTOR_PCT:
            warnings.append(f"SECTOR {sec}: {pct:.1f}% above {REFERENCE_SECTOR_PCT}% reference - consider correlation")
        elif pct > REFERENCE_SECTOR_PCT - 3:
            warnings.append(f"SECTOR {sec}: {pct:.1f}% near {REFERENCE_SECTOR_PCT}% reference")

    # 3. Geography concentration (ADVISORY - v4.0)
    geo_totals = {}
    for p in pos_list:
        geo_totals[p['geo']] = geo_totals.get(p['geo'], 0) + p['value_eur']
    for geo, val in sorted(geo_totals.items(), key=lambda x: -x[1]):
        pct = (val / total) * 100 if total > 0 else 0
        if pct > REFERENCE_GEO_PCT:
            warnings.append(f"GEO {geo}: {pct:.1f}% above {REFERENCE_GEO_PCT}% reference - assess country risk")
        elif pct > REFERENCE_GEO_PCT - 3:
            warnings.append(f"GEO {geo}: {pct:.1f}% near {REFERENCE_GEO_PCT}% reference")

    # 4. Cash level (ADVISORY - v4.0)
    cash_pct = (cash / total) * 100 if total > 0 else 0
    if cash_pct < REFERENCE_CASH_PCT:
        warnings.append(f"CASH: {cash_pct:.1f}% below {REFERENCE_CASH_PCT}% reference - consider opportunity cost")
    elif cash_pct < REFERENCE_CASH_PCT + 2:
        warnings.append(f"CASH: {cash_pct:.1f}% near {REFERENCE_CASH_PCT}% reference")

    # 5. Position count (ADVISORY - v4.0, no hard limit)
    if num_pos > REFERENCE_POSITIONS:
        warnings.append(f"POSITIONS: {num_pos} above {REFERENCE_POSITIONS} reference - ensure manageable")

    return violations, warnings, pos_list, sector_totals, geo_totals, cash, total

def print_report(state):
    violations, warnings, pos_list, sectors, geos, cash, total = check_constraints(state)

    print("=" * 70)
    print("PORTFOLIO CONSTRAINT REPORT")
    print("=" * 70)

    # Positions
    print(f"\n{'Ticker':<12} {'Sector':<20} {'Geo':>4} {'Value EUR':>10} {'Weight':>7}")
    print("-" * 55)
    for p in sorted(pos_list, key=lambda x: -x['value_eur']):
        pct = (p['value_eur'] / total) * 100
        flag = " *" if pct > REFERENCE_POSITION_PCT else ""
        print(f"{p['ticker']:<12} {p['sector']:<20} {p['geo']:>4} {p['value_eur']:>10.0f} {pct:>6.1f}%{flag}")
    print(f"{'CASH':<12} {'':20} {'':>4} {cash:>10.0f} {(cash/total)*100:>6.1f}%")
    print(f"{'TOTAL':<12} {'':20} {'':>4} {total:>10.0f} {'100.0%':>7}")

    # Sectors
    print(f"\n{'Sector':<25} {'Value EUR':>10} {'Weight':>7}")
    print("-" * 44)
    for sec, val in sorted(sectors.items(), key=lambda x: -x[1]):
        pct = (val / total) * 100
        flag = " *" if pct > REFERENCE_SECTOR_PCT else ""
        print(f"{sec:<25} {val:>10.0f} {pct:>6.1f}%{flag}")

    # Geographies
    print(f"\n{'Geography':<25} {'Value EUR':>10} {'Weight':>7}")
    print("-" * 44)
    for geo, val in sorted(geos.items(), key=lambda x: -x[1]):
        pct = (val / total) * 100
        flag = " *" if pct > REFERENCE_GEO_PCT else ""
        print(f"{geo:<25} {val:>10.0f} {pct:>6.1f}%{flag}")

    # Summary
    print(f"\nPositions: {state['num_positions']} (reference: {REFERENCE_POSITIONS})")
    print(f"Cash: {cash:.0f} EUR ({(cash/total)*100:.1f}%)")
    print(f"\n* = above reference point (Framework v4.0: requires explicit reasoning, not automatic action)")

    if warnings:
        print("\nCONSIDERATIONS (Framework v4.0 - ADVISORY):")
        for w in warnings:
            print(f"  [INFO] {w}")
    if not violations and not warnings:
        print("\n[INFO] All metrics within typical ranges.")

def print_check(state, ticker, amount_eur):
    print("=" * 70)
    print(f"CONSTRAINT CHECK: BUY {ticker} for {amount_eur:.0f} EUR")
    print("=" * 70)

    violations, warnings, pos_list, sectors, geos, cash, total = check_constraints(
        state, new_ticker=ticker, amount_eur=amount_eur
    )

    # Show simulated position
    for p in pos_list:
        if p['ticker'] == ticker:
            pct = (p['value_eur'] / total) * 100
            print(f"\n  {ticker} post-purchase: {p['value_eur']:.0f} EUR ({pct:.1f}%)")
            break

    # Show affected sector/geo
    sec = SECTOR_MAP.get(ticker, guess_sector(ticker))
    geo = GEO_MAP.get(ticker, guess_geo(ticker))
    if sec in sectors:
        print(f"  Sector {sec}: {(sectors[sec]/total)*100:.1f}%")
    if geo in geos:
        print(f"  Geography {geo}: {(geos[geo]/total)*100:.1f}%")
    print(f"  Cash after: {cash:.0f} EUR ({(cash/total)*100:.1f}%)")
    print(f"  Positions: {len([p for p in pos_list])}/{MAX_POSITIONS}")

    # Framework v4.0: No PASS/FAIL, only information for principled decision-making
    print(f"\n  FRAMEWORK v4.0: Decision requires reasoning from principles")
    print(f"  See learning/principles.md and learning/decisions_log.yaml")

    if warnings:
        print("\n  CONSIDERATIONS:")
        for w in warnings:
            print(f"    [INFO] {w}")
    else:
        print("\n  [INFO] All metrics within typical ranges after this purchase.")

# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    mode = sys.argv[1].upper()
    portfolio = load_portfolio()
    print("Fetching prices and FX rates...")
    eurusd, gbpeur = get_fx_rates()
    print(f"FX: EUR/USD={eurusd:.4f} | GBP/EUR={gbpeur:.4f}\n")
    state = build_portfolio_state(portfolio, eurusd, gbpeur)

    if mode == 'REPORT':
        print_report(state)
    elif mode == 'CHECK':
        if len(sys.argv) < 4:
            print("Usage: python3 tools/constraint_checker.py CHECK TICKER AMOUNT_EUR")
            sys.exit(1)
        ticker = sys.argv[2]
        amount_eur = float(sys.argv[3])
        print_check(state, ticker, amount_eur)
    else:
        print(f"Unknown mode: {mode}. Use CHECK or REPORT.")
        sys.exit(1)

if __name__ == '__main__':
    main()
