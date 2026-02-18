#!/usr/bin/env python3
"""
Portfolio Statistics - Real-time P&L, allocation, and performance
Usage: python3 tools/portfolio_stats.py
Reads positions (long + short) from portfolio/current.yaml via yfinance

Supports:
  - Long positions (positions list)
  - Short positions (short_positions list) with inverted P&L and carry cost
  - Net/Gross exposure breakdown
"""
import yfinance as yf
import yaml
import os

PORTFOLIO_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'portfolio', 'current.yaml')

def load_portfolio():
    with open(PORTFOLIO_FILE, 'r') as f:
        return yaml.safe_load(f)

def get_fx():
    defaults = {'EURUSD': 1.04, 'GBPUSD': 1.38}
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
        gbpusd = yf.Ticker('GBPUSD=X').info.get('previousClose')
        if not gbpusd:
            gbpusd = defaults['GBPUSD']
            fallbacks_used.append(f"GBP/USD={gbpusd}")
    except Exception:
        gbpusd = defaults['GBPUSD']
        fallbacks_used.append(f"GBP/USD={gbpusd}")

    if fallbacks_used:
        print(f"FX WARNING: Using static fallback rates ({', '.join(fallbacks_used)}). Amounts may be inaccurate.")

    return eurusd, gbpusd

def to_usd(price, currency, eurusd, gbpusd):
    if currency == 'EUR':
        return price * eurusd
    elif currency in ('GBp', 'GBX'):
        return (price / 100) * gbpusd
    elif currency == 'GBP':
        return price * gbpusd
    return price

def fetch_price_usd(ticker, eurusd, gbpusd):
    """Fetch current price in USD for a ticker. Returns (price_usd, currency) or (None, None)."""
    TICKER_MAP = {'LIGHT.NV': 'LIGHT.AS'}
    yf_ticker = TICKER_MAP.get(ticker, ticker)
    info = yf.Ticker(yf_ticker).info
    price = info.get('currentPrice') or info.get('regularMarketPrice') or info.get('previousClose')
    currency = info.get('currency', 'USD')
    if price is None:
        return None, None
    return to_usd(price, currency, eurusd, gbpusd), currency

def main():
    portfolio = load_portfolio()
    positions = portfolio.get('positions', [])
    short_positions = portfolio.get('short_positions', [])
    cash_eur = portfolio.get('cash', {}).get('amount', 0)

    eurusd, gbpusd = get_fx()
    cash_usd = cash_eur * eurusd

    print("=" * 80)
    print("PORTFOLIO STATUS")
    print("=" * 80)
    print(f"FX: EUR/USD={eurusd:.4f} | GBP/USD={gbpusd:.4f}")
    print()

    # =========================================================================
    # LONG POSITIONS
    # =========================================================================
    total_invested = 0
    total_value = 0

    print("LONG POSITIONS")
    print(f"{'Ticker':<10} {'Shares':>10} {'Avg $':>8} {'Now $':>8} {'Invested':>10} {'Value':>10} {'P&L':>10} {'%':>7} {'Alloc':>6}")
    print("-" * 82)

    rows = []
    for p in positions:
        ticker = p['ticker']
        shares = p['shares']
        # Support both USD and EUR invested amounts
        if 'invested_usd' in p:
            invested = p['invested_usd']
        elif 'invested_eur' in p:
            invested = p['invested_eur'] * eurusd  # Convert EUR to USD
        else:
            print(f"  WARN: {ticker} missing invested amount, skipping")
            continue

        price_usd, currency = fetch_price_usd(ticker, eurusd, gbpusd)
        if price_usd is None:
            print(f"  WARN: {ticker} - no price data, skipping")
            continue

        value = price_usd * shares
        pnl = value - invested
        pnl_pct = (pnl / invested) * 100

        total_invested += invested
        total_value += value

        rows.append({
            'ticker': ticker, 'shares': shares, 'avg': invested/shares,
            'price_usd': price_usd, 'invested': invested, 'value': value,
            'pnl': pnl, 'pnl_pct': pnl_pct
        })

    # We need portfolio_total for allocation % — compute after shorts too
    # For now, store long rows and print after we know the total

    # =========================================================================
    # SHORT POSITIONS
    # =========================================================================
    short_rows = []
    total_short_exposure = 0  # absolute market value of shorts
    total_short_pnl = 0

    for s in short_positions:
        ticker = s['ticker']
        shares = s['shares']
        entry_price_usd = s.get('entry_price_usd', 0)
        carry_cost = s.get('carry_cost_accrued', 0)

        price_usd, currency = fetch_price_usd(ticker, eurusd, gbpusd)
        if price_usd is None:
            print(f"  WARN: {ticker} (SHORT) - no price data, skipping")
            continue

        market_value = price_usd * shares  # current exposure (absolute)
        # Short P&L: profit when price drops
        pnl = (entry_price_usd - price_usd) * shares - carry_cost
        entry_total = entry_price_usd * shares
        pnl_pct = (pnl / entry_total) * 100 if entry_total > 0 else 0

        total_short_exposure += market_value
        total_short_pnl += pnl

        short_rows.append({
            'ticker': ticker, 'shares': shares,
            'entry_price_usd': entry_price_usd, 'price_usd': price_usd,
            'market_value': market_value, 'pnl': pnl, 'pnl_pct': pnl_pct,
            'carry_cost': carry_cost, 'date_opened': s.get('date_opened', ''),
            'name': s.get('name', '')
        })

    # =========================================================================
    # COMPUTE TOTALS (need both longs and shorts before printing allocations)
    # =========================================================================
    long_exposure = total_value
    short_exposure = total_short_exposure
    # Portfolio total = long market value + cash (shorts are a liability, not an asset to add)
    # For allocation purposes: total assets = long value + cash
    # Net exposure = long - short
    portfolio_total = total_value + cash_usd

    # =========================================================================
    # PRINT LONG POSITIONS
    # =========================================================================
    for r in rows:
        alloc = (r['value'] / portfolio_total) * 100 if portfolio_total > 0 else 0
        print(f"{r['ticker']:<10} {r['shares']:>10.4f} ${r['avg']:>7.2f} ${r['price_usd']:>7.2f} ${r['invested']:>9.2f} ${r['value']:>9.2f} ${r['pnl']:>+9.2f} {r['pnl_pct']:>+6.1f}% {alloc:>5.1f}%")

    cash_alloc = (cash_usd / portfolio_total) * 100 if portfolio_total > 0 else 0
    print("-" * 82)
    if total_invested > 0:
        print(f"{'INVESTED':<10} {'':>10} {'':>8} {'':>8} ${total_invested:>9.2f} ${total_value:>9.2f} ${total_value-total_invested:>+9.2f} {((total_value-total_invested)/total_invested)*100:>+6.1f}% {(total_value/portfolio_total)*100:>5.1f}%")
    else:
        print(f"{'INVESTED':<10} {'':>10} {'':>8} {'':>8} ${'0.00':>9} ${'0.00':>9}")
    print(f"{'CASH':<10} {'':>10} {'':>8} {'':>8} {'':>10} ${cash_usd:>9.2f} {'':>10} {'':>7} {cash_alloc:>5.1f}%")
    print(f"{'TOTAL':<10} {'':>10} {'':>8} {'':>8} {'':>10} ${portfolio_total:>9.2f}")
    print()

    # =========================================================================
    # PRINT SHORT POSITIONS
    # =========================================================================
    print("=" * 80)
    print("SHORT POSITIONS")
    print("=" * 80)

    if not short_rows:
        print("No short positions.")
    else:
        print(f"{'Ticker':<10} {'Name':<20} {'Shares':>7} {'Entry $':>8} {'Now $':>8} {'Mkt Val':>10} {'P&L':>10} {'%':>7} {'Carry':>8}")
        print("-" * 92)
        for r in short_rows:
            name_trunc = r['name'][:19] if r['name'] else ''
            print(f"{r['ticker']:<10} {name_trunc:<20} {r['shares']:>7.2f} ${r['entry_price_usd']:>7.2f} ${r['price_usd']:>7.2f} ${r['market_value']:>9.2f} ${r['pnl']:>+9.2f} {r['pnl_pct']:>+6.1f}% ${r['carry_cost']:>7.2f}")
        print("-" * 92)
        print(f"{'SHORT TOTAL':<10} {'':>20} {'':>7} {'':>8} {'':>8} ${total_short_exposure:>9.2f} ${total_short_pnl:>+9.2f}")

    print()

    # =========================================================================
    # EXPOSURE SUMMARY
    # =========================================================================
    net_exposure = long_exposure - short_exposure
    gross_exposure = long_exposure + short_exposure
    # Denominator for exposure %: total capital base = long value + cash
    # (this represents the total assets available)
    capital_base = portfolio_total  # long value + cash

    print("=" * 80)
    print("EXPOSURE SUMMARY")
    print("=" * 80)
    print(f"  Long exposure:   ${long_exposure:>10,.2f}  ({(long_exposure/capital_base)*100:>5.1f}% of portfolio)" if capital_base > 0 else f"  Long exposure:   ${long_exposure:>10,.2f}")
    print(f"  Short exposure:  ${short_exposure:>10,.2f}  ({(short_exposure/capital_base)*100:>5.1f}% of portfolio)" if capital_base > 0 else f"  Short exposure:  ${short_exposure:>10,.2f}")
    print(f"  Net exposure:    ${net_exposure:>10,.2f}  ({(net_exposure/capital_base)*100:>5.1f}% of portfolio)" if capital_base > 0 else f"  Net exposure:    ${net_exposure:>10,.2f}")
    print(f"  Gross exposure:  ${gross_exposure:>10,.2f}  ({(gross_exposure/capital_base)*100:>5.1f}% of portfolio)" if capital_base > 0 else f"  Gross exposure:  ${gross_exposure:>10,.2f}")
    print(f"  Cash:            ${cash_usd:>10,.2f}  ({cash_alloc:>5.1f}% of portfolio)")
    print()

    print(f"Portfolio: ${portfolio_total:,.0f} (EUR {portfolio_total/eurusd:,.0f})")
    print(f"Cash: EUR {cash_eur:,.0f} ({cash_alloc:.1f}%)")
    if total_short_pnl != 0:
        combined_pnl = (total_value - total_invested) + total_short_pnl
        print(f"Combined P&L (long + short): ${combined_pnl:>+,.2f}")
    print()
    print("[Raw data. Reason from principles.md]")

if __name__ == '__main__':
    main()
