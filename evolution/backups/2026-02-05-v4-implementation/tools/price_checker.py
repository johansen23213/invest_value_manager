#!/usr/bin/env python3
"""
Price Checker - ÚNICA fuente de precios del sistema.
Usa yfinance API. NUNCA usar WebSearch para precios.
Usage: python3 tools/price_checker.py TICKER1 TICKER2 ...
"""
import sys
import yfinance as yf

def get_fx_rates():
    eurusd = yf.Ticker('EURUSD=X').info.get('previousClose', 1.04)
    gbpeur = yf.Ticker('GBPEUR=X').info.get('previousClose', 1.19)
    return eurusd, gbpeur

def get_price(ticker, eurusd, gbpeur):
    stock = yf.Ticker(ticker)
    info = stock.info
    price = info.get('currentPrice') or info.get('regularMarketPrice') or info.get('previousClose')
    currency = info.get('currency', '?')
    name = info.get('shortName', ticker)
    high52 = info.get('fiftyTwoWeekHigh', 'N/A')
    low52 = info.get('fiftyTwoWeekLow', 'N/A')
    mcap = info.get('marketCap', 0)
    pe = info.get('trailingPE', 'N/A')
    dy = info.get('dividendYield', 0)

    if price is None:
        return None

    # Convert to EUR
    if currency == 'USD':
        price_eur = price / eurusd
    elif currency in ('GBp', 'GBX'):
        price_eur = (price / 100) * gbpeur
    elif currency == 'GBP':
        price_eur = price * gbpeur
    elif currency == 'EUR':
        price_eur = price
    else:
        price_eur = price

    mcap_b = mcap / 1e9 if mcap else 0
    # yfinance sometimes returns yield as decimal (0.05), sometimes as percent (5.0)
    if dy and dy > 1:
        dy_pct = dy  # already in percent
    elif dy:
        dy_pct = dy * 100
    else:
        dy_pct = 0

    return {
        'ticker': ticker,
        'name': name,
        'price': price,
        'currency': currency,
        'price_eur': price_eur,
        'high52': high52,
        'low52': low52,
        'mcap_b': mcap_b,
        'pe': pe,
        'div_yield': dy_pct,
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 tools/price_checker.py TICKER1 TICKER2 ...")
        sys.exit(1)

    tickers = sys.argv[1:]
    eurusd, gbpeur = get_fx_rates()
    print(f"FX Rates: EUR/USD={eurusd:.4f} | GBP/EUR={gbpeur:.4f}")
    print(f"{'Ticker':<10} {'Name':<30} {'Price':>10} {'Curr':>5} {'EUR':>10} {'52wH':>10} {'52wL':>10} {'P/E':>8} {'Yield':>6} {'MCap(B)':>8}")
    print("-" * 118)

    for t in tickers:
        data = get_price(t, eurusd, gbpeur)
        if data:
            pe_str = f"{data['pe']:.1f}" if isinstance(data['pe'], (int, float)) else str(data['pe'])
            print(f"{data['ticker']:<10} {data['name']:<30} {data['price']:>10.2f} {data['currency']:>5} {data['price_eur']:>10.2f} {data['high52']:>10} {data['low52']:>10} {pe_str:>8} {data['div_yield']:>5.1f}% {data['mcap_b']:>7.1f}B")
        else:
            print(f"{t:<10} ERROR: No price data available")

if __name__ == '__main__':
    main()
