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
  python3 tools/constraint_checker.py CHECK_SHORT TICKER AMOUNT_EUR
  python3 tools/constraint_checker.py CHECK_SHORT TICKER AMOUNT_EUR --drawdown 30
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

def get_short_value_eur(ticker, shares, entry_price_usd, eurusd, gbpeur):
    """Get current market value of a short position in EUR.

    Returns (market_value_eur, unrealized_pnl_eur).
    market_value_eur = current price * shares converted to EUR (this is the exposure).
    unrealized_pnl_eur = (entry_price - current_price) * shares converted to EUR.
    """
    try:
        info = yf.Ticker(ticker).info
        price = info.get('currentPrice') or info.get('regularMarketPrice') or info.get('previousClose')
        currency = info.get('currency', 'USD')
        if price is None:
            raise ValueError("No price")

        def to_eur(val, cur):
            if cur == 'USD':
                return val / eurusd
            elif cur in ('GBp', 'GBX'):
                return (val / 100) * gbpeur
            elif cur == 'GBP':
                return val * gbpeur
            elif cur == 'EUR':
                return val
            else:
                return val / eurusd

        market_val_eur = to_eur(price * shares, currency)
        # entry_price_usd is always in USD per the YAML schema
        entry_val_eur = entry_price_usd * shares / eurusd
        pnl_eur = entry_val_eur - market_val_eur  # positive = short is profitable
        return market_val_eur, pnl_eur
    except Exception:
        fallback = entry_price_usd * shares / eurusd
        return fallback, 0.0

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

    # Short positions
    short_positions = portfolio.get('short_positions', []) or []
    short_data = []
    for sp in short_positions:
        ticker = sp['ticker']
        shares = sp['shares']
        entry_price = sp.get('entry_price_usd', 0)
        carry_accrued = sp.get('carry_cost_accrued', 0.0)
        market_val, pnl = get_short_value_eur(ticker, shares, entry_price, eurusd, gbpeur)
        sector = SECTOR_MAP.get(ticker, guess_sector(ticker))
        geo = GEO_MAP.get(ticker, guess_geo(ticker))
        short_data.append({
            'ticker': ticker,
            'value_eur': market_val,  # current market exposure
            'entry_value_eur': entry_price * shares / eurusd,
            'pnl_eur': pnl,
            'carry_accrued_eur': carry_accrued / eurusd if carry_accrued else 0.0,
            'sector': sector,
            'geo': geo,
        })

    total_long = sum(pd['value_eur'] for pd in pos_data)
    total_short = sum(sd['value_eur'] for sd in short_data)
    total = total_long + cash_eur  # NAV = long + cash (shorts are liabilities reflected in cash/margin)

    return {
        'positions': pos_data,
        'short_positions': short_data,
        'cash_eur': cash_eur,
        'total_long': total_long,
        'total_short': total_short,
        'total_eur': total,
        'num_positions': len(pos_data),
        'num_shorts': len(short_data),
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

def print_exposure_summary(state):
    """Print net/gross exposure data for portfolio with shorts."""
    total_long = state['total_long']
    total_short = state['total_short']
    total_nav = state['total_eur']

    net_exposure = total_long - total_short
    gross_exposure = total_long + total_short

    print(f"\n{'=' * 60}")
    print("EXPOSURE DATA")
    print(f"{'=' * 60}")
    print(f"  Long exposure:    {total_long:>8.0f} EUR ({(total_long/total_nav)*100:>5.1f}% of NAV)")
    print(f"  Short exposure:   {total_short:>8.0f} EUR ({(total_short/total_nav)*100:>5.1f}% of NAV)")
    print(f"  Net exposure:     {net_exposure:>8.0f} EUR ({(net_exposure/total_nav)*100:>5.1f}% of NAV)")
    print(f"  Gross exposure:   {gross_exposure:>8.0f} EUR ({(gross_exposure/total_nav)*100:>5.1f}% of NAV)")
    print(f"  Cash:             {state['cash_eur']:>8.0f} EUR ({(state['cash_eur']/total_nav)*100:>5.1f}% of NAV)")

def print_short_positions(state):
    """Print short positions section."""
    shorts = state['short_positions']
    if not shorts:
        return

    print(f"\n{'=' * 60}")
    print("SHORT POSITIONS")
    print(f"{'=' * 60}")
    print(f"\n{'Ticker':<10} {'Sector':<18} {'Geo':>3} {'Mkt Val':>8} {'P&L':>8} {'Carry':>7}")
    print("-" * 60)
    for s in sorted(shorts, key=lambda x: -x['value_eur']):
        print(f"{s['ticker']:<10} {s['sector']:<18} {s['geo']:>3} {s['value_eur']:>8.0f} {s['pnl_eur']:>+8.0f} {s['carry_accrued_eur']:>7.1f}")
    total_short_val = sum(s['value_eur'] for s in shorts)
    total_pnl = sum(s['pnl_eur'] for s in shorts)
    total_carry = sum(s['carry_accrued_eur'] for s in shorts)
    print("-" * 60)
    print(f"{'TOTAL':<10} {'':<18} {'':<3} {total_short_val:>8.0f} {total_pnl:>+8.0f} {total_carry:>7.1f}")

def print_report(state, drawdown_pct=50):
    pos_list, sectors, geos, cash, total, num_pos = analyze_context(state)

    print("=" * 60)
    print("PORTFOLIO DATA")
    print("=" * 60)

    # Long Positions
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

    # Short Positions (if any)
    print_short_positions(state)

    # Sectors (long only for concentration)
    print(f"\n{'Sector':<22} {'EUR':>8} {'%':>6}")
    print("-" * 38)
    for sec, val in sorted(sectors.items(), key=lambda x: -x[1]):
        print(f"{sec:<22} {val:>8.0f} {(val/total)*100:>5.1f}%")

    # Net sector exposure (long - short) if shorts exist
    if state['short_positions']:
        print(f"\n{'Sector (net)':<22} {'Long':>8} {'Short':>8} {'Net':>8} {'%':>6}")
        print("-" * 55)
        # Collect short sector totals
        short_sector_totals = {}
        for s in state['short_positions']:
            short_sector_totals[s['sector']] = short_sector_totals.get(s['sector'], 0) + s['value_eur']
        all_sectors = set(list(sectors.keys()) + list(short_sector_totals.keys()))
        net_sector = {}
        for sec in all_sectors:
            l = sectors.get(sec, 0)
            s = short_sector_totals.get(sec, 0)
            net_sector[sec] = l - s
        for sec, net in sorted(net_sector.items(), key=lambda x: -abs(x[1])):
            l = sectors.get(sec, 0)
            s = short_sector_totals.get(sec, 0)
            print(f"{sec:<22} {l:>8.0f} {s:>8.0f} {net:>8.0f} {(net/total)*100:>5.1f}%")

    # Geographies
    print(f"\n{'Geography':<22} {'EUR':>8} {'%':>6}")
    print("-" * 38)
    for geo, val in sorted(geos.items(), key=lambda x: -x[1]):
        print(f"{geo:<22} {val:>8.0f} {(val/total)*100:>5.1f}%")

    print(f"\nPositions: {num_pos} long, {state['num_shorts']} short | Cash: {cash:.0f} EUR ({(cash/total)*100:.1f}%)")

    # Exposure summary (always show, even if no shorts -- useful context)
    print_exposure_summary(state)

    print("\n[Raw data. Reason from principles.md]")

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

    # Exposure impact (if shorts exist, show updated exposure)
    total_long_after = sum(p['value_eur'] for p in pos_list)
    total_short = state['total_short']
    net_after = total_long_after - total_short
    gross_after = total_long_after + total_short
    print(f"\nNet exposure after: {net_after:.0f} EUR ({(net_after/total)*100:.1f}%)")
    print(f"Gross exposure after: {gross_after:.0f} EUR ({(gross_after/total)*100:.1f}%)")

    print("\n[Raw data. Reason from principles.md]")

def print_check_short(state, ticker, amount_eur, drawdown_pct=50):
    """Simulate opening a short position of AMOUNT_EUR on TICKER."""
    print("=" * 60)
    print(f"SIMULATED: SHORT {ticker} for {amount_eur:.0f} EUR")
    print("=" * 60)

    total_nav = state['total_eur']
    total_long = state['total_long']
    total_short_before = state['total_short']
    cash = state['cash_eur']

    # The new short
    sec = SECTOR_MAP.get(ticker, guess_sector(ticker))
    geo = GEO_MAP.get(ticker, guess_geo(ticker))

    # After opening short
    total_short_after = total_short_before + amount_eur
    net_before = total_long - total_short_before
    net_after = total_long - total_short_after
    gross_before = total_long + total_short_before
    gross_after = total_long + total_short_after

    print(f"\nShort {ticker}: {amount_eur:.0f} EUR")
    print(f"Sector: {sec}")
    print(f"Geography: {geo}")

    # Position as % of NAV
    pct_of_nav = (amount_eur / total_nav) * 100
    print(f"Short size: {pct_of_nav:.1f}% of NAV")

    # Drawdown impact: if the shorted stock RISES by drawdown_pct, we LOSE
    loss_eur = amount_eur * drawdown_pct / 100
    loss_pct = (loss_eur / total_nav) * 100
    print(f"If {ticker} rises {drawdown_pct}%: loss {loss_eur:.0f} EUR ({loss_pct:.1f}% of NAV)")

    # Exposure changes
    print(f"\n--- Exposure Impact ---")
    print(f"  Net exposure:   {net_before:>8.0f} ({(net_before/total_nav)*100:>5.1f}%) -> {net_after:>8.0f} ({(net_after/total_nav)*100:>5.1f}%)")
    print(f"  Gross exposure: {gross_before:>8.0f} ({(gross_before/total_nav)*100:>5.1f}%) -> {gross_after:>8.0f} ({(gross_after/total_nav)*100:>5.1f}%)")
    print(f"  Short total:    {total_short_before:>8.0f} ({(total_short_before/total_nav)*100:>5.1f}%) -> {total_short_after:>8.0f} ({(total_short_after/total_nav)*100:>5.1f}%)")

    # Sector concentration impact (net)
    long_sectors = {}
    for p in state['positions']:
        long_sectors[p['sector']] = long_sectors.get(p['sector'], 0) + p['value_eur']
    short_sectors = {}
    for s in state['short_positions']:
        short_sectors[s['sector']] = short_sectors.get(s['sector'], 0) + s['value_eur']

    # Add the new short
    short_sectors_after = dict(short_sectors)
    short_sectors_after[sec] = short_sectors_after.get(sec, 0) + amount_eur

    # Show net sector for affected sector
    long_in_sec = long_sectors.get(sec, 0)
    short_in_sec_before = short_sectors.get(sec, 0)
    short_in_sec_after = short_sectors_after.get(sec, 0)
    net_sec_before = long_in_sec - short_in_sec_before
    net_sec_after = long_in_sec - short_in_sec_after

    print(f"\n--- Sector {sec} (net) ---")
    print(f"  Long:  {long_in_sec:>8.0f} EUR")
    print(f"  Short: {short_in_sec_before:>8.0f} -> {short_in_sec_after:>8.0f} EUR")
    print(f"  Net:   {net_sec_before:>8.0f} ({(net_sec_before/total_nav)*100:>5.1f}%) -> {net_sec_after:>8.0f} ({(net_sec_after/total_nav)*100:>5.1f}%)")

    # Carry cost projection
    # eToro typical overnight fee ~7-8% annualized on short positions
    carry_low = amount_eur * 0.07
    carry_high = amount_eur * 0.08
    print(f"\n--- Carry Cost Projection ---")
    print(f"  Annual carry: {carry_low:.0f} - {carry_high:.0f} EUR ({carry_low/total_nav*100:.2f}% - {carry_high/total_nav*100:.2f}% of NAV)")
    print(f"  Monthly carry: {carry_low/12:.0f} - {carry_high/12:.0f} EUR")
    print(f"  Daily carry: {carry_low/365:.1f} - {carry_high/365:.1f} EUR")

    # Existing short positions
    if state['short_positions']:
        print(f"\n--- Existing Short Positions ---")
        for s in state['short_positions']:
            print(f"  {s['ticker']}: {s['value_eur']:.0f} EUR ({s['sector']})")

    print(f"\nCash: {cash:.0f} EUR ({(cash/total_nav)*100:.1f}%) [no cash consumed by short, but margin required]")
    print(f"Positions: {state['num_positions']} long, {state['num_shorts'] + 1} short (after)")

    print("\n[Raw data. Reason from principles.md]")

# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    import argparse as _argparse

    parser = _argparse.ArgumentParser(description=__doc__,
                                       formatter_class=_argparse.RawDescriptionHelpFormatter)
    parser.add_argument('mode', choices=['REPORT', 'CHECK', 'CHECK_SHORT', 'report', 'check', 'check_short'],
                        help='REPORT for portfolio overview, CHECK for simulated buy, CHECK_SHORT for simulated short')
    parser.add_argument('ticker', nargs='?', help='Ticker for CHECK/CHECK_SHORT mode')
    parser.add_argument('amount', nargs='?', type=float, help='Amount EUR for CHECK/CHECK_SHORT mode')
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
    elif mode == 'CHECK_SHORT':
        if not args.ticker or args.amount is None:
            print("Usage: constraint_checker.py CHECK_SHORT TICKER AMOUNT_EUR [--drawdown 30]")
            sys.exit(1)
        print_check_short(state, args.ticker, args.amount, drawdown_pct=args.drawdown)
    else:
        print(f"Unknown mode: {mode}")
        sys.exit(1)

if __name__ == '__main__':
    main()
