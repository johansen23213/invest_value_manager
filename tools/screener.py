#!/usr/bin/env python3
"""
Value Stock Screener - Quantitative screening via yfinance
Usage:
  python3 tools/screener.py                          # Default: P/E<15, Yield>3%
  python3 tools/screener.py --pe-max 12 --yield-min 4
  python3 tools/screener.py --near-low               # Only stocks >15% below 52w high
  python3 tools/screener.py --sector banks            # Predefined sector lists
  python3 tools/screener.py --tickers AAPL MSFT GOOG  # Custom tickers
"""
import sys
import argparse
import yfinance as yf

SECTORS = {
    'eu_banks': ['BNP.PA', 'SAN.PA', 'ISP.MI', 'UCG.MI', 'BBVA.MC', 'SAN.MC', 'INGA.AS', 'DBK.DE', 'CSGN.SW', 'KBC.BR'],
    'eu_utilities': ['ENGI.PA', 'ENEL.MI', 'IBE.MC', 'EOAN.DE', 'FORTUM.HE', 'EDP.LS', 'SSE.L', 'NG.L', 'DTE.DE'],
    'eu_insurance': ['AXA.PA', 'LGEN.L', 'PHNX.L', 'AV.L', 'MUV2.DE', 'AGN.AS', 'MAP.MC'],
    'us_pharma': ['PFE', 'BMY', 'GILD', 'ABBV', 'MRK', 'JNJ', 'VTRS', 'TEVA', 'TAK'],
    'us_telecom': ['T', 'VZ', 'TMUS'],
    'us_value': ['MO', 'BTI', 'PM', 'KR', 'CAH', 'CI', 'CVS', 'HPQ', 'NUE', 'LYB', 'DOW'],
    'uk_value': ['BATS.L', 'IMB.L', 'VOD.L', 'WPP.L', 'ITV.L', 'BARC.L', 'LLOY.L', 'HSBA.L', 'RIO.L'],
    'oil_gas': ['TTE', 'SHEL', 'BP.L', 'REP.MC', 'GALP.LS', 'ENI.MI', 'EQNR.OL'],
    'japan': ['8001.T', '8058.T', '8053.T', '5020.T', '7203.T', '9432.T', '2914.T'],
    'canada': ['BNS.TO', 'CM.TO', 'ENB.TO', 'MFC.TO', 'SU.TO'],
    'reits': ['O', 'VICI', 'SPG', 'AMT', 'DLR'],
    'china': ['BABA', 'JD', '0005.HK', '9988.HK'],
    'all': [],  # populated dynamically
}
# 'all' = union of all sectors
SECTORS['all'] = list(set(t for tickers in SECTORS.values() for t in tickers))

def get_fx_rates():
    eurusd = yf.Ticker('EURUSD=X').info.get('previousClose', 1.04)
    gbpeur = yf.Ticker('GBPEUR=X').info.get('previousClose', 1.19)
    return eurusd, gbpeur

def screen(tickers, pe_max=15, pe_min=0, yield_min=3.0, near_low=False, mcap_min=0):
    eurusd, gbpeur = get_fx_rates()
    results = []

    for t in tickers:
        try:
            info = yf.Ticker(t).info
            price = info.get('currentPrice') or info.get('regularMarketPrice') or info.get('previousClose')
            pe = info.get('trailingPE')
            fpe = info.get('forwardPE')
            dy = info.get('dividendYield', 0)
            mcap = info.get('marketCap', 0)
            name = info.get('shortName', t)[:25]
            h52 = info.get('fiftyTwoWeekHigh', 0)
            l52 = info.get('fiftyTwoWeekLow', 0)
            currency = info.get('currency', '?')
            pb = info.get('priceToBook')

            if not price or not pe or pe <= 0:
                continue

            # Yield handling
            if dy and dy > 1:
                dy_pct = dy
            elif dy:
                dy_pct = dy * 100
            else:
                dy_pct = 0

            # Distance from 52w high
            dist_high = ((price - h52) / h52) * 100 if h52 else 0

            # EUR conversion
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

            # Apply filters
            if pe > pe_max or pe < pe_min:
                continue
            if dy_pct < yield_min:
                continue
            if near_low and dist_high > -15:
                continue
            if mcap_b < mcap_min:
                continue

            results.append({
                'ticker': t, 'name': name, 'price': price, 'currency': currency,
                'price_eur': price_eur, 'pe': pe, 'fpe': fpe,
                'yield': dy_pct, 'pb': pb, 'dist_high': dist_high,
                'mcap_b': mcap_b, 'h52': h52, 'l52': l52
            })
        except Exception as e:
            print(f"  SKIP {t}: {e}", file=sys.stderr)

    # Sort by P/E
    results.sort(key=lambda x: x['pe'])
    return results

def print_results(results, near_low=False):
    if near_low:
        print(f"\n{'Ticker':<10} {'Name':<26} {'Price':>8} {'EUR':>8} {'%offHi':>7} {'P/E':>6} {'FwdPE':>7} {'Yield':>6} {'P/B':>6} {'MCap':>8}")
        print("-" * 95)
        for r in results:
            fpe = f"{r['fpe']:.1f}" if r['fpe'] else "N/A"
            pb = f"{r['pb']:.2f}" if r['pb'] else "N/A"
            print(f"{r['ticker']:<10} {r['name']:<26} {r['price']:>8.2f} {r['price_eur']:>7.2f}€ {r['dist_high']:>+6.1f}% {r['pe']:>6.1f} {fpe:>7} {r['yield']:>5.1f}% {pb:>6} {r['mcap_b']:>7.1f}B")
    else:
        print(f"\n{'Ticker':<10} {'Name':<26} {'Price':>8} {'EUR':>8} {'P/E':>6} {'FwdPE':>7} {'Yield':>6} {'P/B':>6} {'MCap':>8}")
        print("-" * 88)
        for r in results:
            fpe = f"{r['fpe']:.1f}" if r['fpe'] else "N/A"
            pb = f"{r['pb']:.2f}" if r['pb'] else "N/A"
            print(f"{r['ticker']:<10} {r['name']:<26} {r['price']:>8.2f} {r['price_eur']:>7.2f}€ {r['pe']:>6.1f} {fpe:>7} {r['yield']:>5.1f}% {pb:>6} {r['mcap_b']:>7.1f}B")

    print(f"\n{len(results)} stocks passed filters")

def main():
    parser = argparse.ArgumentParser(description='Value Stock Screener')
    parser.add_argument('--pe-max', type=float, default=15, help='Max trailing P/E (default: 15)')
    parser.add_argument('--pe-min', type=float, default=0, help='Min trailing P/E (default: 0)')
    parser.add_argument('--yield-min', type=float, default=3.0, help='Min dividend yield %% (default: 3)')
    parser.add_argument('--near-low', action='store_true', help='Only stocks >15%% below 52w high')
    parser.add_argument('--mcap-min', type=float, default=0, help='Min market cap in $B (default: 0)')
    parser.add_argument('--sector', type=str, default=None, help=f'Sector: {", ".join(SECTORS.keys())}')
    parser.add_argument('--tickers', nargs='+', default=None, help='Custom list of tickers')
    args = parser.parse_args()

    if args.tickers:
        tickers = args.tickers
    elif args.sector:
        if args.sector not in SECTORS:
            print(f"Unknown sector. Available: {', '.join(SECTORS.keys())}", file=sys.stderr)
            sys.exit(1)
        tickers = SECTORS[args.sector]
    else:
        tickers = SECTORS['all']

    print(f"Screening {len(tickers)} tickers: P/E<{args.pe_max}, Yield>{args.yield_min}%{', near 52w low' if args.near_low else ''}", file=sys.stderr)

    results = screen(tickers, pe_max=args.pe_max, yield_min=args.yield_min,
                     near_low=args.near_low, mcap_min=args.mcap_min, pe_min=args.pe_min)
    print_results(results, near_low=args.near_low)

if __name__ == '__main__':
    main()
