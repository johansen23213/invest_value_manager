#!/usr/bin/env python3
"""
Test yfinance ownership/insider data coverage across US, UK, EU tickers.
Purpose: Evaluate data quality before building a permanent tool.

Usage:
    python3 tools/test_ownership_data.py
"""

import yfinance as yf
import pandas as pd
import sys
import traceback

# Suppress pandas future warnings
import warnings
warnings.filterwarnings('ignore')

TICKERS = {
    'US': ['ADBE', 'VRSK', 'ROP', 'GL'],
    'UK': ['MONY.L', 'AUTO.L', 'BYIT.L'],
    'EU': ['DTE.DE', 'EDEN.PA'],
    'ADR': ['NVO'],
}

PROPERTIES = [
    'insider_transactions',
    'insider_purchases',
    'institutional_holders',
    'mutualfund_holders',
]

# Tickers for which we print full raw data
DETAILED_TICKERS = ['ADBE', 'MONY.L', 'DTE.DE']

def separator(char='=', width=100):
    print(char * width)

def sub_separator(char='-', width=80):
    print(char * width)

def get_property_safe(ticker_obj, prop_name):
    """Safely get a property from a yfinance Ticker object."""
    try:
        val = getattr(ticker_obj, prop_name, None)
        if val is None:
            return None, "None returned"
        if isinstance(val, pd.DataFrame):
            if val.empty:
                return val, "Empty DataFrame"
            return val, "OK"
        return val, "OK (non-DataFrame)"
    except Exception as e:
        return None, f"ERROR: {e}"

def summarize_df(df, label):
    """Print summary of a DataFrame."""
    if df is None or (isinstance(df, pd.DataFrame) and df.empty):
        print(f"  {label}: NO DATA")
        return

    if not isinstance(df, pd.DataFrame):
        print(f"  {label}: {type(df)} - {df}")
        return

    print(f"  {label}:")
    print(f"    Rows: {len(df)}")
    print(f"    Columns: {list(df.columns)}")
    print(f"    Dtypes: {dict(df.dtypes)}")

    # Check for date columns and find most recent
    for col in df.columns:
        if 'date' in col.lower() or 'start' in col.lower():
            try:
                dates = pd.to_datetime(df[col], errors='coerce')
                valid_dates = dates.dropna()
                if len(valid_dates) > 0:
                    print(f"    Most recent '{col}': {valid_dates.max()}")
                    print(f"    Oldest '{col}': {valid_dates.min()}")
            except:
                pass

def print_full_data(df, label, max_rows=10):
    """Print full raw data for detailed inspection."""
    if df is None or (isinstance(df, pd.DataFrame) and df.empty):
        print(f"\n  {label}: NO DATA AVAILABLE")
        return

    if not isinstance(df, pd.DataFrame):
        print(f"\n  {label}: {type(df)} - {df}")
        return

    print(f"\n  {label} (showing up to {max_rows} rows of {len(df)}):")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 200)
    pd.set_option('display.max_colwidth', 40)
    print(df.head(max_rows).to_string(index=True))

def main():
    print()
    separator('=')
    print("YFINANCE OWNERSHIP DATA COVERAGE TEST")
    print("Testing: insider_transactions, insider_purchases, institutional_holders, mutualfund_holders")
    separator('=')

    # Phase 1: Coverage matrix
    print("\n" + "=" * 100)
    print("PHASE 1: COVERAGE MATRIX")
    print("=" * 100)

    results = {}

    for region, tickers in TICKERS.items():
        for ticker_str in tickers:
            print(f"\nFetching {ticker_str} ({region})...", end=" ", flush=True)
            try:
                t = yf.Ticker(ticker_str)
                results[ticker_str] = {'region': region, 'data': {}}

                for prop in PROPERTIES:
                    val, status = get_property_safe(t, prop)
                    row_count = len(val) if isinstance(val, pd.DataFrame) and not val.empty else 0
                    results[ticker_str]['data'][prop] = {
                        'value': val,
                        'status': status,
                        'rows': row_count,
                    }
                print("OK")
            except Exception as e:
                print(f"FAILED: {e}")
                results[ticker_str] = {'region': region, 'data': {}, 'error': str(e)}

    # Print coverage matrix
    print("\n" + "-" * 100)
    print(f"{'Ticker':<12} {'Region':<6} {'insider_txns':<20} {'insider_purch':<20} {'inst_holders':<20} {'mf_holders':<20}")
    print("-" * 100)

    for ticker_str, info in results.items():
        if 'error' in info:
            print(f"{ticker_str:<12} {info['region']:<6} ERROR: {info['error']}")
            continue

        cols = []
        for prop in PROPERTIES:
            d = info['data'].get(prop, {})
            status = d.get('status', 'N/A')
            rows = d.get('rows', 0)
            if status == 'OK':
                cols.append(f"{rows} rows")
            elif status == 'Empty DataFrame':
                cols.append("EMPTY")
            elif 'None' in str(status):
                cols.append("None")
            else:
                cols.append(status[:18])

        print(f"{ticker_str:<12} {info['region']:<6} {cols[0]:<20} {cols[1]:<20} {cols[2]:<20} {cols[3]:<20}")

    # Phase 2: Summary per property
    print("\n" + "=" * 100)
    print("PHASE 2: SUMMARY PER PROPERTY")
    print("=" * 100)

    for prop in PROPERTIES:
        print(f"\n--- {prop} ---")
        for ticker_str, info in results.items():
            if 'error' in info:
                continue
            d = info['data'].get(prop, {})
            val = d.get('value')
            status = d.get('status', 'N/A')

            print(f"\n  [{ticker_str}] ({info['region']}) - Status: {status}")
            if isinstance(val, pd.DataFrame) and not val.empty:
                summarize_df(val, f"{prop}")

    # Phase 3: Full raw data for detailed tickers
    print("\n" + "=" * 100)
    print("PHASE 3: FULL RAW DATA FOR DETAILED TICKERS")
    print("=" * 100)

    for ticker_str in DETAILED_TICKERS:
        info = results.get(ticker_str)
        if not info or 'error' in info:
            print(f"\n{ticker_str}: No data available")
            continue

        print(f"\n{'#' * 80}")
        print(f"# {ticker_str} ({info['region']}) - FULL RAW DATA")
        print(f"{'#' * 80}")

        for prop in PROPERTIES:
            d = info['data'].get(prop, {})
            val = d.get('value')
            print_full_data(val, prop, max_rows=15)

    # Phase 4: Analysis and recommendations
    print("\n" + "=" * 100)
    print("PHASE 4: ANALYSIS & RECOMMENDATIONS")
    print("=" * 100)

    print("\nCoverage by region:")
    for region in ['US', 'UK', 'EU', 'ADR']:
        tickers_in_region = [t for t, i in results.items() if i['region'] == region]
        for prop in PROPERTIES:
            has_data = []
            no_data = []
            for t in tickers_in_region:
                info = results[t]
                if 'error' in info:
                    no_data.append(t)
                    continue
                d = info['data'].get(prop, {})
                if d.get('rows', 0) > 0:
                    has_data.append(t)
                else:
                    no_data.append(t)
            print(f"  {region:<4} {prop:<25} HAS_DATA: {has_data}  NO_DATA: {no_data}")

    # Additional: try major_holders for context
    print("\n" + "=" * 100)
    print("BONUS: major_holders property (if available)")
    print("=" * 100)

    for ticker_str in DETAILED_TICKERS + ['GL', 'NVO']:
        try:
            t = yf.Ticker(ticker_str)
            mh = t.major_holders
            if mh is not None and isinstance(mh, pd.DataFrame) and not mh.empty:
                print(f"\n  [{ticker_str}] major_holders:")
                print(mh.to_string(index=True))
            else:
                print(f"\n  [{ticker_str}] major_holders: NO DATA")
        except Exception as e:
            print(f"\n  [{ticker_str}] major_holders: ERROR - {e}")

    print("\n" + "=" * 100)
    print("TEST COMPLETE")
    print("=" * 100)

if __name__ == '__main__':
    main()
