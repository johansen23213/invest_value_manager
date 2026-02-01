#!/usr/bin/env python3
"""
[DEPRECATED] European Mid-Cap Value Screener - Use tools/dynamic_screener.py instead.

This tool uses HARDCODED ticker lists which introduces popularity bias.
dynamic_screener.py fetches index components programmatically from Wikipedia
and supports parallel fetching, caching, and anti-bias features.

Migration examples:
  OLD: python3 tools/midcap_screener.py --max-pe 10 --min-yield 4
  NEW: python3 tools/dynamic_screener.py --index stoxx600 --pe-max 10 --yield-min 4 --mcap-max 15

  OLD: python3 tools/midcap_screener.py --exchange AS MI
  NEW: python3 tools/dynamic_screener.py --index stoxx600 --mcap-max 15 --max-analysts 10

  OLD: python3 tools/midcap_screener.py --sort fcf_yield
  NEW: python3 tools/dynamic_screener.py --index stoxx600 --undiscovered --sort fcf_yield

Legacy usage (still works but deprecated):
  python3 tools/midcap_screener.py                              # Default filters
  python3 tools/midcap_screener.py --max-pe 10 --min-yield 4.0
  python3 tools/midcap_screener.py --min-mcap 2 --max-mcap 10
  python3 tools/midcap_screener.py --sort fcf_yield
  python3 tools/midcap_screener.py --exchange AS
  python3 tools/midcap_screener.py --output results.csv
"""
import sys
import argparse
import yfinance as yf
import csv
from datetime import datetime

# DEPRECATION WARNING
print("\n" + "=" * 70, file=sys.stderr)
print("DEPRECATED: Use tools/dynamic_screener.py instead.", file=sys.stderr)
print("This tool uses hardcoded tickers (popularity bias).", file=sys.stderr)
print("Example: python3 tools/dynamic_screener.py --index stoxx600 --undiscovered", file=sys.stderr)
print("=" * 70 + "\n", file=sys.stderr)

# Curated list of European mid-cap tickers across exchanges
# Focus on lesser-known names less likely to appear in popular searches
EUROPEAN_MIDCAPS = {
    'AS': [  # Amsterdam
        'AALB.AS', 'AGN.AS', 'AKZA.AS', 'AMG.AS', 'APAM.AS', 'BESI.AS',
        'FLOW.AS', 'GLPG.AS', 'IMCD.AS', 'JDE.AS', 'LIGHT.AS', 'ORN.AS',
        'POST.AS', 'RAND.AS', 'SBM.AS', 'TKA.AS', 'TWEKA.AS', 'VPK.AS'
    ],
    'BR': [  # Brussels
        'ABI.BR', 'ACKB.BR', 'AGRB.BR', 'APAM.BR', 'COLR.BR', 'GBLB.BR',
        'KBC.BR', 'LOTB.BR', 'PROX.BR', 'SOLB.BR', 'TELB.BR', 'TINC.BR',
        'UCB.BR', 'WDP.BR'
    ],
    'MI': [  # Milan
        'A2A.MI', 'AMP.MI', 'ATL.MI', 'AZM.MI', 'BAMI.MI', 'BGN.MI',
        'BPE.MI', 'BMED.MI', 'BZU.MI', 'CPR.MI', 'DIA.MI', 'ERG.MI',
        'FBK.MI', 'HER.MI', 'IP.MI', 'ISP.MI', 'LDO.MI', 'MB.MI',
        'PIRC.MI', 'PST.MI', 'SRG.MI', 'TEN.MI', 'TIT.MI', 'TRN.MI',
        'UCG.MI', 'UNI.MI'
    ],
    'MC': [  # Madrid
        'AENA.MC', 'ACS.MC', 'BBVA.MC', 'BKT.MC', 'CABK.MC', 'CLNX.MC',
        'ELE.MC', 'ENG.MC', 'FER.MC', 'GRF.MC', 'IAG.MC', 'IBE.MC',
        'ITX.MC', 'LOG.MC', 'MAP.MC', 'MRL.MC', 'REE.MC', 'REP.MC',
        'SAB.MC', 'SAN.MC', 'SCYR.MC', 'TEF.MC', 'VIS.MC'
    ],
    'HE': [  # Helsinki
        'ELISA.HE', 'FORTUM.HE', 'KNEBV.HE', 'KOJAMO.HE', 'NESTE.HE',
        'NOKIA.HE', 'ORNBV.HE', 'SAMPO.HE', 'STERV.HE', 'TIETO.HE',
        'UPM.HE', 'VALMT.HE', 'WRT1V.HE'
    ],
    'ST': [  # Stockholm
        'ABB.ST', 'ALIV-SDB.ST', 'ASSA-B.ST', 'ATCO-A.ST', 'AZN.ST',
        'BOL.ST', 'ELUX-B.ST', 'ESSITY-B.ST', 'EVO.ST', 'HEXA-B.ST',
        'HM-B.ST', 'ICA.ST', 'KINV-B.ST', 'NDA-SE.ST', 'SAND.ST',
        'SCA-B.ST', 'SEB-A.ST', 'SECU-B.ST', 'SHB-A.ST', 'SINCH.ST',
        'SKA-B.ST', 'SKF-B.ST', 'SWED-A.ST', 'TEL2-B.ST', 'TELIA.ST',
        'VOLV-B.ST'
    ],
    'OL': [  # Oslo
        'AKRBP.OL', 'BAKKA.OL', 'DNB.OL', 'EQNR.OL', 'GJF.OL',
        'MOWI.OL', 'ORK.OL', 'SALM.OL', 'STB.OL', 'TEL.OL', 'YAR.OL'
    ],
    'CO': [  # Copenhagen
        'CARL-B.CO', 'CHR.CO', 'COLO-B.CO', 'DSV.CO', 'GN.CO',
        'JYSK.CO', 'MAERSK-A.CO', 'MAERSK-B.CO', 'NOVO-B.CO',
        'ORSTED.CO', 'PNDORA.CO', 'RBREW.CO', 'TRYG.CO', 'VWS.CO'
    ],
    'DE': [  # Frankfurt
        'ADS.DE', 'AIR.DE', 'ALV.DE', 'BAS.DE', 'BAYN.DE', 'BEI.DE',
        'BMW.DE', 'CBK.DE', 'CON.DE', 'DAI.DE', 'DB1.DE', 'DBK.DE',
        'DHL.DE', 'DTE.DE', 'EOAN.DE', 'FME.DE', 'FRE.DE', 'HEI.DE',
        'HEN3.DE', 'IFX.DE', 'LHA.DE', 'LIN.DE', 'MRK.DE', 'MUV2.DE',
        'RWE.DE', 'SAP.DE', 'SIE.DE', 'VOW3.DE', 'VNA.DE'
    ],
    'PA': [  # Paris
        'AC.PA', 'AI.PA', 'AIR.PA', 'ATO.PA', 'BN.PA', 'BNP.PA',
        'CA.PA', 'CAP.PA', 'CS.PA', 'DSY.PA', 'ENGI.PA', 'EL.PA',
        'FP.PA', 'GLE.PA', 'KER.PA', 'MC.PA', 'ML.PA', 'OR.PA',
        'ORA.PA', 'PUB.PA', 'RI.PA', 'RMS.PA', 'SAN.PA', 'SGO.PA',
        'SU.PA', 'TEP.PA', 'TTE.PA', 'UG.PA', 'VIE.PA', 'VIV.PA'
    ],
    'L': [  # London
        'AAL.L', 'ABF.L', 'AV.L', 'BA.L', 'BARC.L', 'BATS.L', 'BP.L',
        'BT-A.L', 'CCH.L', 'CPG.L', 'CRDA.L', 'DGE.L', 'GSK.L',
        'HSBA.L', 'IMB.L', 'ITV.L', 'JMAT.L', 'LGEN.L', 'LLOY.L',
        'NG.L', 'NWG.L', 'PHNX.L', 'PRU.L', 'RIO.L', 'RR.L',
        'SBRY.L', 'SHEL.L', 'SSE.L', 'STAN.L', 'TSCO.L', 'VOD.L',
        'WPP.L', 'WTB.L'
    ]
}

def get_fx_rates():
    """Get EUR/USD and GBP/EUR rates"""
    try:
        eurusd = yf.Ticker('EURUSD=X').info.get('previousClose', 1.04)
        gbpeur = yf.Ticker('GBPEUR=X').info.get('previousClose', 1.19)
    except:
        eurusd, gbpeur = 1.04, 1.19  # fallback
    return eurusd, gbpeur

def to_eur(value, currency, eurusd, gbpeur):
    """Convert any currency to EUR"""
    if not value:
        return 0
    if currency == 'USD':
        return value / eurusd
    elif currency in ('GBp', 'GBX'):
        return (value / 100) * gbpeur
    elif currency == 'GBP':
        return value * gbpeur
    elif currency == 'EUR':
        return value
    elif currency in ('SEK', 'NOK', 'DKK'):  # Scandinavian - rough approximation
        return value * 0.09  # ~1 EUR = 11 SEK/NOK/DKK
    elif currency == 'CHF':
        return value * 0.95  # ~1 EUR = 1.05 CHF
    else:
        return value  # assume EUR if unknown

def screen_midcaps(exchanges=None, max_pe=12, min_yield=3.0, min_mcap=1.0, max_mcap=15.0,
                   max_debt_equity=1.5, require_fcf=True):
    """
    Screen European mid-caps for value opportunities.

    Returns list of dicts with stock data.
    """
    eurusd, gbpeur = get_fx_rates()
    results = []

    # Build ticker list
    if exchanges:
        tickers = []
        for ex in exchanges:
            tickers.extend(EUROPEAN_MIDCAPS.get(ex.upper(), []))
    else:
        tickers = [t for ticker_list in EUROPEAN_MIDCAPS.values() for t in ticker_list]

    print(f"Screening {len(tickers)} European mid-caps...", file=sys.stderr)

    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            info = stock.info

            # Basic data
            price = info.get('currentPrice') or info.get('regularMarketPrice') or info.get('previousClose')
            if not price:
                continue

            name = info.get('shortName', ticker)[:30]
            currency = info.get('currency', '?')

            # Market cap (convert to EUR billions)
            mcap_local = info.get('marketCap', 0)
            if not mcap_local:
                continue
            mcap_eur = to_eur(mcap_local, currency, eurusd, gbpeur) / 1e9

            # Filter by market cap range
            if mcap_eur < min_mcap or mcap_eur > max_mcap:
                continue

            # Valuation metrics
            pe = info.get('trailingPE')
            if not pe or pe <= 0 or pe > max_pe:
                continue

            fwd_pe = info.get('forwardPE')
            pb = info.get('priceToBook')

            # Dividend yield
            div_yield = info.get('dividendYield', 0)
            if div_yield > 1:  # already in percent
                div_yield_pct = div_yield
            elif div_yield:
                div_yield_pct = div_yield * 100
            else:
                div_yield_pct = 0

            if div_yield_pct < min_yield:
                continue

            # Free cash flow
            fcf = info.get('freeCashflow', 0)
            if require_fcf and (not fcf or fcf <= 0):
                continue

            fcf_yield = (fcf / mcap_local * 100) if mcap_local else 0

            # Debt/Equity
            debt_equity = info.get('debtToEquity', 0) / 100  # yfinance returns in percentage
            if debt_equity > max_debt_equity:
                continue

            # Analyst coverage (proxy for popularity)
            num_analysts = info.get('numberOfAnalystOpinions', 0)

            # Sector
            sector = info.get('sector', 'Unknown')

            # 52-week range
            h52 = info.get('fiftyTwoWeekHigh', 0)
            l52 = info.get('fiftyTwoWeekLow', 0)
            dist_from_high = ((price - h52) / h52 * 100) if h52 else 0
            dist_from_low = ((price - l52) / l52 * 100) if l52 else 0

            # Price in EUR
            price_eur = to_eur(price, currency, eurusd, gbpeur)

            results.append({
                'ticker': ticker,
                'name': name,
                'exchange': ticker.split('.')[-1] if '.' in ticker else 'UK',
                'price': price,
                'currency': currency,
                'price_eur': price_eur,
                'mcap_eur': mcap_eur,
                'pe': pe,
                'fwd_pe': fwd_pe,
                'pb': pb,
                'div_yield': div_yield_pct,
                'fcf_yield': fcf_yield,
                'debt_equity': debt_equity,
                'num_analysts': num_analysts,
                'sector': sector,
                'dist_from_high': dist_from_high,
                'dist_from_low': dist_from_low,
                'h52': h52,
                'l52': l52,
            })

        except Exception as e:
            print(f"  SKIP {ticker}: {e}", file=sys.stderr)
            continue

    return results

def print_table(results, sort_by='pe'):
    """Print results as formatted table"""
    if not results:
        print("\nNo stocks passed filters.")
        return

    # Sort
    if sort_by == 'pe':
        results.sort(key=lambda x: x['pe'])
    elif sort_by == 'fcf_yield':
        results.sort(key=lambda x: x['fcf_yield'], reverse=True)
    elif sort_by == 'div_yield':
        results.sort(key=lambda x: x['div_yield'], reverse=True)
    elif sort_by == 'mcap':
        results.sort(key=lambda x: x['mcap_eur'])
    elif sort_by == 'analysts':
        results.sort(key=lambda x: x['num_analysts'])

    print(f"\n{'Ticker':<12} {'Name':<30} {'Exch':<5} {'Price€':>8} {'MCap€B':>7} {'P/E':>6} {'FwdPE':>7} {'Yld%':>5} {'FCF%':>5} {'D/E':>5} {'Analysts':>9} {'Sector':<20}")
    print("-" * 145)

    for r in results:
        fwd_pe = f"{r['fwd_pe']:.1f}" if r['fwd_pe'] else "N/A"
        pb = f"{r['pb']:.2f}" if r['pb'] else "N/A"

        print(f"{r['ticker']:<12} {r['name']:<30} {r['exchange']:<5} "
              f"{r['price_eur']:>8.2f} {r['mcap_eur']:>7.1f} "
              f"{r['pe']:>6.1f} {fwd_pe:>7} "
              f"{r['div_yield']:>5.1f} {r['fcf_yield']:>5.1f} "
              f"{r['debt_equity']:>5.2f} {r['num_analysts']:>9} "
              f"{r['sector']:<20}")

    print(f"\n{len(results)} stocks passed filters")

    # Summary stats
    avg_pe = sum(r['pe'] for r in results) / len(results)
    avg_yield = sum(r['div_yield'] for r in results) / len(results)
    avg_fcf = sum(r['fcf_yield'] for r in results) / len(results)
    avg_analysts = sum(r['num_analysts'] for r in results) / len(results)

    print(f"\nAverages: P/E={avg_pe:.1f} | Yield={avg_yield:.1f}% | FCF={avg_fcf:.1f}% | Analysts={avg_analysts:.0f}")

    # Low coverage opportunities
    low_coverage = [r for r in results if r['num_analysts'] < 5]
    if low_coverage:
        print(f"\n{len(low_coverage)} stocks with <5 analyst coverage (potential inefficiency):")
        for r in sorted(low_coverage, key=lambda x: x['num_analysts'])[:10]:
            print(f"  {r['ticker']:<12} {r['name']:<30} {r['num_analysts']} analysts | P/E={r['pe']:.1f} | Yield={r['div_yield']:.1f}%")

def save_csv(results, filename):
    """Save results to CSV"""
    if not results:
        print("No results to save.")
        return

    with open(filename, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['ticker', 'name', 'exchange', 'price', 'currency', 'price_eur',
                     'mcap_eur', 'pe', 'fwd_pe', 'pb', 'div_yield', 'fcf_yield',
                     'debt_equity', 'num_analysts', 'sector', 'dist_from_high',
                     'dist_from_low', 'h52', 'l52']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"\nResults saved to {filename}")

def main():
    parser = argparse.ArgumentParser(
        description='[DEPRECATED] European Mid-Cap Value Screener - Use tools/dynamic_screener.py --undiscovered instead',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 tools/midcap_screener.py                           # Default: P/E<12, Yield>3%, 1B-15B
  python3 tools/midcap_screener.py --max-pe 10 --min-yield 4
  python3 tools/midcap_screener.py --exchange AS MI          # Amsterdam & Milan only
  python3 tools/midcap_screener.py --sort fcf_yield          # Sort by FCF yield
  python3 tools/midcap_screener.py --output results.csv      # Save to CSV
        """
    )

    parser.add_argument('--max-pe', type=float, default=12, help='Max trailing P/E (default: 12)')
    parser.add_argument('--min-yield', type=float, default=3.0, help='Min dividend yield %% (default: 3.0)')
    parser.add_argument('--min-mcap', type=float, default=1.0, help='Min market cap B (default: 1.0)')
    parser.add_argument('--max-mcap', type=float, default=15.0, help='Max market cap B (default: 15.0)')
    parser.add_argument('--max-debt-equity', type=float, default=1.5, help='Max debt/equity (default: 1.5)')
    parser.add_argument('--allow-negative-fcf', action='store_true', help='Allow negative free cash flow')
    parser.add_argument('--exchange', nargs='+', help='Filter by exchange (AS, MI, PA, L, etc.)')
    parser.add_argument('--sort', choices=['pe', 'fcf_yield', 'div_yield', 'mcap', 'analysts'],
                       default='pe', help='Sort by field (default: pe)')
    parser.add_argument('--output', type=str, help='Save results to CSV file')

    args = parser.parse_args()

    print(f"European Mid-Cap Screener", file=sys.stderr)
    print(f"Filters: P/E<{args.max_pe}, Yield>{args.min_yield}%, {args.min_mcap}B-{args.max_mcap}B MCap, D/E<{args.max_debt_equity}", file=sys.stderr)
    if args.exchange:
        print(f"Exchanges: {', '.join(args.exchange)}", file=sys.stderr)
    print(f"", file=sys.stderr)

    results = screen_midcaps(
        exchanges=args.exchange,
        max_pe=args.max_pe,
        min_yield=args.min_yield,
        min_mcap=args.min_mcap,
        max_mcap=args.max_mcap,
        max_debt_equity=args.max_debt_equity,
        require_fcf=not args.allow_negative_fcf
    )

    print_table(results, sort_by=args.sort)

    if args.output:
        save_csv(results, args.output)

if __name__ == '__main__':
    main()
