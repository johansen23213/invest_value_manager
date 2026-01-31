#!/usr/bin/env python3
"""
Portfolio Statistics - Real-time P&L, allocation, and performance
Usage: python3 tools/portfolio_stats.py
Reads positions from portfolio/current.yaml via yfinance
"""
import yfinance as yf
import yaml
import os

PORTFOLIO_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'portfolio', 'current.yaml')

def load_portfolio():
    with open(PORTFOLIO_FILE, 'r') as f:
        return yaml.safe_load(f)

def get_fx():
    eurusd = yf.Ticker('EURUSD=X').info.get('previousClose', 1.04)
    gbpusd = yf.Ticker('GBPUSD=X').info.get('previousClose', 1.38)
    return eurusd, gbpusd

def to_usd(price, currency, eurusd, gbpusd):
    if currency == 'EUR':
        return price * eurusd
    elif currency in ('GBp', 'GBX'):
        return (price / 100) * gbpusd
    elif currency == 'GBP':
        return price * gbpusd
    return price

def main():
    portfolio = load_portfolio()
    positions = portfolio.get('positions', [])
    cash_eur = portfolio.get('cash', {}).get('amount', 0)

    eurusd, gbpusd = get_fx()
    cash_usd = cash_eur * eurusd

    print("=" * 80)
    print("PORTFOLIO STATUS")
    print("=" * 80)
    print(f"FX: EUR/USD={eurusd:.4f} | GBP/USD={gbpusd:.4f}")
    print()

    total_invested = 0
    total_value = 0

    print(f"{'Ticker':<10} {'Shares':>10} {'Avg $':>8} {'Now $':>8} {'Invested':>10} {'Value':>10} {'P&L':>10} {'%':>7} {'Alloc':>6}")
    print("-" * 82)

    rows = []
    for p in positions:
        ticker = p['ticker']
        shares = p['shares']
        invested = p['invested_usd']

        # Get current price
        yf_ticker = ticker
        info = yf.Ticker(yf_ticker).info
        price = info.get('currentPrice') or info.get('regularMarketPrice') or info.get('previousClose')
        currency = info.get('currency', 'USD')

        price_usd = to_usd(price, currency, eurusd, gbpusd)
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

    portfolio_total = total_value + cash_usd

    for r in rows:
        alloc = (r['value'] / portfolio_total) * 100
        print(f"{r['ticker']:<10} {r['shares']:>10.4f} ${r['avg']:>7.2f} ${r['price_usd']:>7.2f} ${r['invested']:>9.2f} ${r['value']:>9.2f} ${r['pnl']:>+9.2f} {r['pnl_pct']:>+6.1f}% {alloc:>5.1f}%")

    cash_alloc = (cash_usd / portfolio_total) * 100
    print("-" * 82)
    print(f"{'INVESTED':<10} {'':>10} {'':>8} {'':>8} ${total_invested:>9.2f} ${total_value:>9.2f} ${total_value-total_invested:>+9.2f} {((total_value-total_invested)/total_invested)*100:>+6.1f}% {(total_value/portfolio_total)*100:>5.1f}%")
    print(f"{'CASH':<10} {'':>10} {'':>8} {'':>8} {'':>10} ${cash_usd:>9.2f} {'':>10} {'':>7} {cash_alloc:>5.1f}%")
    print(f"{'TOTAL':<10} {'':>10} {'':>8} {'':>8} {'':>10} ${portfolio_total:>9.2f}")
    print()
    print(f"Portfolio: ${portfolio_total:,.0f} (€{portfolio_total/eurusd:,.0f})")
    print(f"Cash: €{cash_eur:,.0f} ({cash_alloc:.1f}%)")
    if cash_alloc > 15:
        print(f"⚠ CASH DRAG: {cash_alloc:.0f}% > 15% target. Deploy capital.")

if __name__ == '__main__':
    main()
