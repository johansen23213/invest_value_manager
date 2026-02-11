#!/usr/bin/env python3
"""
Stage 2 Opportunity Filter
Reads CSV outputs from dynamic_screener.py and applies fundamental filters:
- ROIC > threshold
- FCF margin > threshold
- Revenue CAGR 5yr > threshold

Uses yfinance for fundamental data. Outputs filtered list with key metrics.
"""

import sys
import csv
import argparse
import yfinance as yf
import time
import warnings
from concurrent.futures import ThreadPoolExecutor, as_completed

warnings.filterwarnings("ignore")


def get_fundamentals(ticker):
    """Get ROIC, FCF margin, revenue CAGR for a ticker."""
    try:
        stock = yf.Ticker(ticker)
        info = stock.info or {}

        # Get financials
        income = stock.financials
        balance = stock.balance_sheet
        cashflow = stock.cashflow

        result = {
            "ticker": ticker,
            "name": info.get("shortName", "N/A"),
            "sector": info.get("sector", "N/A"),
            "industry": info.get("industry", "N/A"),
            "mcap_b": round(info.get("marketCap", 0) / 1e9, 1) if info.get("marketCap") else None,
            "pe": info.get("trailingPE"),
            "price": info.get("currentPrice") or info.get("regularMarketPrice"),
            "currency": info.get("currency", "USD"),
        }

        # ROIC = NOPAT / Invested Capital
        # NOPAT = Operating Income * (1 - tax_rate)
        # Invested Capital = Total Assets - Current Liabilities (or Total Equity + Total Debt)
        roic = None
        if income is not None and not income.empty and balance is not None and not balance.empty:
            try:
                # Operating income
                op_income = None
                for key in ["Operating Income", "EBIT"]:
                    if key in income.index:
                        op_income = income.loc[key].iloc[0]
                        break

                # Tax rate
                tax_provision = None
                pretax_income = None
                for key in ["Tax Provision", "Income Tax Expense"]:
                    if key in income.index:
                        tax_provision = income.loc[key].iloc[0]
                        break
                for key in ["Pretax Income", "Income Before Tax"]:
                    if key in income.index:
                        pretax_income = income.loc[key].iloc[0]
                        break

                tax_rate = 0.25  # default
                if tax_provision is not None and pretax_income is not None and pretax_income > 0:
                    tax_rate = max(0, min(0.5, tax_provision / pretax_income))

                # Invested capital
                total_assets = None
                current_liab = None
                for key in ["Total Assets"]:
                    if key in balance.index:
                        total_assets = balance.loc[key].iloc[0]
                        break
                for key in ["Current Liabilities"]:
                    if key in balance.index:
                        current_liab = balance.loc[key].iloc[0]
                        break

                if op_income and total_assets and current_liab:
                    nopat = op_income * (1 - tax_rate)
                    invested_capital = total_assets - current_liab
                    if invested_capital > 0:
                        roic = (nopat / invested_capital) * 100
            except Exception:
                pass

        # Also try returnOnCapital from info
        if roic is None:
            roic_info = info.get("returnOnCapital")
            if roic_info:
                roic = roic_info * 100 if roic_info < 1 else roic_info

        result["roic"] = round(roic, 1) if roic else None

        # FCF Margin = FCF / Revenue
        fcf_margin = None
        if cashflow is not None and not cashflow.empty and income is not None and not income.empty:
            try:
                fcf = None
                for key in ["Free Cash Flow"]:
                    if key in cashflow.index:
                        fcf = cashflow.loc[key].iloc[0]
                        break
                if fcf is None:
                    # Calculate: Operating CF - CapEx
                    op_cf = None
                    capex = None
                    for key in ["Operating Cash Flow", "Total Cash From Operating Activities"]:
                        if key in cashflow.index:
                            op_cf = cashflow.loc[key].iloc[0]
                            break
                    for key in ["Capital Expenditure", "Capital Expenditures"]:
                        if key in cashflow.index:
                            capex = cashflow.loc[key].iloc[0]
                            break
                    if op_cf is not None and capex is not None:
                        fcf = op_cf + capex  # capex is usually negative

                revenue = None
                for key in ["Total Revenue", "Revenue"]:
                    if key in income.index:
                        revenue = income.loc[key].iloc[0]
                        break

                if fcf is not None and revenue and revenue > 0:
                    fcf_margin = (fcf / revenue) * 100
            except Exception:
                pass

        # Fallback from info
        if fcf_margin is None:
            fcf_val = info.get("freeCashflow")
            rev_val = info.get("totalRevenue")
            if fcf_val and rev_val and rev_val > 0:
                fcf_margin = (fcf_val / rev_val) * 100

        result["fcf_margin"] = round(fcf_margin, 1) if fcf_margin else None

        # Revenue CAGR 5yr
        rev_cagr = None
        if income is not None and not income.empty:
            try:
                rev_row = None
                for key in ["Total Revenue", "Revenue"]:
                    if key in income.index:
                        rev_row = income.loc[key].dropna()
                        break

                if rev_row is not None and len(rev_row) >= 2:
                    # yfinance returns most recent first
                    latest = rev_row.iloc[0]
                    oldest = rev_row.iloc[-1]
                    years = len(rev_row) - 1

                    if oldest > 0 and latest > 0 and years > 0:
                        rev_cagr = ((latest / oldest) ** (1 / years) - 1) * 100
            except Exception:
                pass

        # Fallback
        if rev_cagr is None:
            rev_growth = info.get("revenueGrowth")
            if rev_growth:
                rev_cagr = rev_growth * 100

        result["rev_cagr"] = round(rev_cagr, 1) if rev_cagr else None

        # Extra useful metrics
        result["roe"] = round(info.get("returnOnEquity", 0) * 100, 1) if info.get("returnOnEquity") else None
        result["div_yield"] = round(info.get("dividendYield", 0) * 100, 1) if info.get("dividendYield") else None
        result["debt_equity"] = round(info.get("debtToEquity", 0) / 100, 2) if info.get("debtToEquity") else None

        # 52w metrics
        high52 = info.get("fiftyTwoWeekHigh")
        if high52 and result["price"]:
            result["dist_52h"] = round((result["price"] / high52 - 1) * 100, 1)
        else:
            result["dist_52h"] = None

        return result
    except Exception as e:
        return {"ticker": ticker, "error": str(e)}


def main():
    parser = argparse.ArgumentParser(description="Filter opportunities by ROIC, FCF margin, Revenue CAGR")
    parser.add_argument("--csv", nargs="+", required=True, help="CSV files from dynamic_screener.py")
    parser.add_argument("--roic-min", type=float, default=15, help="Min ROIC %% (default: 15)")
    parser.add_argument("--fcf-margin-min", type=float, default=10, help="Min FCF margin %% (default: 10)")
    parser.add_argument("--rev-cagr-min", type=float, default=5, help="Min Revenue CAGR %% (default: 5)")
    parser.add_argument("--workers", type=int, default=6, help="Parallel workers (default: 6)")
    parser.add_argument("--output", help="Save results to CSV")
    parser.add_argument("--exclude", nargs="*", default=[], help="Tickers to exclude")
    args = parser.parse_args()

    # Read all tickers from CSV files
    tickers = set()
    for csv_file in args.csv:
        try:
            with open(csv_file) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    ticker = row.get("Ticker", row.get("ticker", "")).strip()
                    if ticker:
                        tickers.add(ticker)
        except Exception as e:
            print(f"  Error reading {csv_file}: {e}")

    # Exclude existing positions
    exclude = set(args.exclude)
    tickers = tickers - exclude

    print(f"\nOpportunity Filter")
    print(f"  Input: {len(tickers)} tickers from {len(args.csv)} CSV files")
    print(f"  Filters: ROIC >{args.roic_min}%, FCF Margin >{args.fcf_margin_min}%, Rev CAGR >{args.rev_cagr_min}%")
    print(f"  Excluded: {len(exclude)} tickers")
    print(f"\nFetching fundamental data ({args.workers} workers)...")

    # Fetch fundamentals in parallel
    results = []
    errors = 0
    processed = 0

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(get_fundamentals, t): t for t in tickers}
        for future in as_completed(futures):
            processed += 1
            if processed % 25 == 0:
                print(f"  Progress: {processed}/{len(tickers)}")
            try:
                result = future.result()
                if "error" not in result:
                    results.append(result)
                else:
                    errors += 1
            except Exception:
                errors += 1

    print(f"\n  Fetched: {len(results)} OK, {errors} errors")

    # Apply filters
    passed = []
    for r in results:
        roic = r.get("roic")
        fcf_m = r.get("fcf_margin")
        rev_c = r.get("rev_cagr")

        if roic is None or fcf_m is None or rev_c is None:
            continue

        if roic >= args.roic_min and fcf_m >= args.fcf_margin_min and rev_c >= args.rev_cagr_min:
            passed.append(r)

    # Sort by ROIC descending
    passed.sort(key=lambda x: x.get("roic", 0), reverse=True)

    print(f"\n{'='*120}")
    print(f"PASSED ALL FILTERS: {len(passed)} companies")
    print(f"{'='*120}")
    print(f"{'Ticker':<10} {'Name':<30} {'Sector':<22} {'ROIC%':>6} {'FCFm%':>6} {'RevCAGR':>7} {'P/E':>6} {'MCap$B':>7} {'D52H%':>6} {'D/E':>5} {'Geo':<4}")
    print("-" * 120)

    for r in passed:
        geo = "US"
        t = r["ticker"]
        if ".L" in t: geo = "UK"
        elif ".DE" in t or ".PA" in t or ".MI" in t or ".MC" in t or ".AS" in t or ".BR" in t or ".ST" in t or ".HE" in t or ".LS" in t: geo = "EU"

        print(f"{r['ticker']:<10} {str(r.get('name',''))[:29]:<30} {str(r.get('sector',''))[:21]:<22} "
              f"{r.get('roic','N/A'):>6} {r.get('fcf_margin','N/A'):>6} {r.get('rev_cagr','N/A'):>7} "
              f"{r.get('pe','N/A') if r.get('pe') else 'N/A':>6} "
              f"{r.get('mcap_b','N/A'):>7} {r.get('dist_52h','N/A'):>6} "
              f"{r.get('debt_equity','N/A'):>5} {geo:<4}")

    # Summary by sector
    print(f"\n{'='*60}")
    print("SUMMARY BY SECTOR")
    print(f"{'='*60}")
    sectors = {}
    for r in passed:
        s = r.get("sector", "Unknown")
        sectors[s] = sectors.get(s, 0) + 1
    for s, c in sorted(sectors.items(), key=lambda x: -x[1]):
        print(f"  {s:<35} {c:>3} companies")

    # Summary by geography
    print(f"\n{'='*60}")
    print("SUMMARY BY GEOGRAPHY")
    print(f"{'='*60}")
    geos = {"US": 0, "UK": 0, "EU": 0}
    for r in passed:
        t = r["ticker"]
        if ".L" in t: geos["UK"] += 1
        elif any(x in t for x in [".DE",".PA",".MI",".MC",".AS",".BR",".ST",".HE",".LS"]): geos["EU"] += 1
        else: geos["US"] += 1
    for g, c in sorted(geos.items(), key=lambda x: -x[1]):
        print(f"  {g:<10} {c:>3} companies")

    # Save to CSV
    if args.output and passed:
        with open(args.output, "w", newline="") as f:
            fieldnames = ["ticker", "name", "sector", "industry", "roic", "fcf_margin", "rev_cagr",
                         "pe", "mcap_b", "dist_52h", "roe", "div_yield", "debt_equity", "price", "currency"]
            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(passed)
        print(f"\nResults saved to {args.output}")


if __name__ == "__main__":
    main()
