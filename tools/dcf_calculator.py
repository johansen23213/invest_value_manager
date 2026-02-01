#!/usr/bin/env python3
"""
DCF Calculator - Discounted Cash Flow valuation tool.

Fetches historical Free Cash Flow via yfinance, projects future FCF,
calculates terminal value, and determines intrinsic value per share.

Usage:
  python3 tools/dcf_calculator.py AAPL                          # Default params
  python3 tools/dcf_calculator.py AAPL --growth 8 --terminal 2.5 --wacc 10
  python3 tools/dcf_calculator.py AAPL --years 10                # 10-year projection
  python3 tools/dcf_calculator.py AAPL --scenarios              # Bear/Base/Bull scenarios
  python3 tools/dcf_calculator.py AAPL MSFT GOOGL               # Batch analysis
  python3 tools/dcf_calculator.py AAPL --output dcf_results.csv # Save to CSV

Examples:
  python3 tools/dcf_calculator.py SAN.MC --growth 5 --terminal 2 --wacc 9
  python3 tools/dcf_calculator.py ASML.AS --scenarios
  python3 tools/dcf_calculator.py BNP.PA BBVA.MC SAN.MC --output eu_banks_dcf.csv
"""

import sys
import argparse
import csv
from typing import Optional, Dict, List, Tuple

import yfinance as yf
import pandas as pd


# ==============================================================================
# FX Rates (consistent with other tools)
# ==============================================================================

def get_fx_rates() -> Dict[str, float]:
    """Get FX rates for EUR conversion."""
    rates = {}
    pairs = {"USD": "EURUSD=X", "GBP": "GBPEUR=X"}
    defaults = {"USD": 1.04, "GBP": 1.19}
    for ccy, symbol in pairs.items():
        try:
            rates[ccy] = yf.Ticker(symbol).info.get("previousClose", defaults[ccy])
        except Exception:
            rates[ccy] = defaults[ccy]
    return rates


def to_eur(value: float, currency: str, rates: Dict[str, float]) -> float:
    """Convert value to EUR."""
    if not value:
        return 0
    if currency == "EUR":
        return value
    if currency == "USD":
        return value / rates.get("USD", 1.04)
    if currency in ("GBp", "GBX"):
        return (value / 100) * rates.get("GBP", 1.19)
    if currency == "GBP":
        return value * rates.get("GBP", 1.19)
    if currency in ("SEK", "NOK", "DKK"):
        return value * 0.087
    if currency == "CHF":
        return value * 0.95
    if currency == "JPY":
        return value * 0.0063
    return value  # assume EUR-ish


# ==============================================================================
# Data Fetching
# ==============================================================================

def fetch_historical_fcf(ticker: str, years: int = 5) -> Optional[Dict]:
    """
    Fetch historical Free Cash Flow data via yfinance.
    Returns dict with FCF history, shares outstanding, currency, price.
    """
    try:
        stock = yf.Ticker(ticker)
        info = stock.info

        # Get current price
        price = info.get("currentPrice") or info.get("regularMarketPrice") or info.get("previousClose")
        if not price:
            print(f"ERROR {ticker}: No price data available", file=sys.stderr)
            return None

        # Get shares outstanding
        shares = info.get("sharesOutstanding")
        if not shares or shares <= 0:
            print(f"ERROR {ticker}: No shares outstanding data", file=sys.stderr)
            return None

        # Get currency
        currency = info.get("currency", "USD")
        name = info.get("shortName", ticker)

        # Get cashflow statement
        cashflow = stock.cashflow
        if cashflow is None or cashflow.empty:
            print(f"ERROR {ticker}: No cashflow data available", file=sys.stderr)
            return None

        # Extract Free Cash Flow (Operating CF - CapEx)
        # yfinance uses different field names depending on data source
        fcf_keys = ["Free Cash Flow", "FreeCashFlow", "free cash flow"]
        ocf_keys = ["Total Cash From Operating Activities", "Operating Cash Flow",
                    "TotalCashFromOperatingActivities"]
        capex_keys = ["Capital Expenditures", "CapitalExpenditures", "capital expenditures"]

        fcf_row = None
        for key in fcf_keys:
            if key in cashflow.index:
                fcf_row = cashflow.loc[key]
                break

        # If no direct FCF, calculate from OCF - CapEx
        if fcf_row is None:
            ocf_row = None
            capex_row = None
            for key in ocf_keys:
                if key in cashflow.index:
                    ocf_row = cashflow.loc[key]
                    break
            for key in capex_keys:
                if key in cashflow.index:
                    capex_row = cashflow.loc[key]
                    break

            if ocf_row is not None and capex_row is not None:
                # CapEx is usually negative, so we subtract (which adds absolute value)
                fcf_row = ocf_row + capex_row  # capex is negative
            else:
                print(f"ERROR {ticker}: Cannot calculate FCF (missing OCF or CapEx)", file=sys.stderr)
                return None

        # Convert to list, most recent first
        fcf_history = fcf_row.dropna().tolist()[:years]
        fcf_history.reverse()  # oldest to newest

        if len(fcf_history) < 2:
            print(f"ERROR {ticker}: Insufficient FCF history ({len(fcf_history)} years)", file=sys.stderr)
            return None

        # FCF volatility check - warn if DCF may be unreliable
        sector = info.get("sector", "Unknown")
        fcf_warning = None
        if len(fcf_history) >= 3:
            fcf_arr = [abs(f) for f in fcf_history if f != 0]
            if fcf_arr:
                cv = (max(fcf_arr) - min(fcf_arr)) / (sum(fcf_arr) / len(fcf_arr))
                if cv > 1.5:
                    fcf_warning = f"CAUTION: FCF highly volatile (CV={cv:.1f}). DCF may be unreliable for {sector}."
        if any(f <= 0 for f in fcf_history[-2:]):
            fcf_warning = f"CAUTION: Recent negative FCF. DCF unreliable for {sector}. Use EV/EBITDA or NAV instead."

        return {
            "ticker": ticker,
            "name": name,
            "price": price,
            "currency": currency,
            "shares": shares,
            "fcf_history": fcf_history,
            "fcf_warning": fcf_warning,
        }

    except Exception as e:
        print(f"ERROR {ticker}: {e}", file=sys.stderr)
        return None


# ==============================================================================
# DCF Calculation
# ==============================================================================

def calculate_dcf(
    fcf_history: List[float],
    shares: float,
    growth_rate: float,
    terminal_growth: float,
    wacc: float,
    projection_years: int = 5,
) -> Dict:
    """
    Perform DCF calculation.

    Args:
        fcf_history: List of historical FCF values (oldest to newest)
        shares: Shares outstanding
        growth_rate: Annual FCF growth rate (%) for projection period
        terminal_growth: Perpetual growth rate (%) for terminal value
        wacc: Weighted Average Cost of Capital (%)
        projection_years: Number of years to project

    Returns:
        Dict with projected FCF, PV, terminal value, equity value, fair value/share
    """
    # Start from most recent FCF
    base_fcf = fcf_history[-1]

    # Project future FCF
    projected_fcf = []
    pv_fcf = []
    for year in range(1, projection_years + 1):
        fcf = base_fcf * ((1 + growth_rate / 100) ** year)
        pv = fcf / ((1 + wacc / 100) ** year)
        projected_fcf.append(fcf)
        pv_fcf.append(pv)

    # Terminal value (Gordon Growth Model)
    terminal_fcf = projected_fcf[-1] * (1 + terminal_growth / 100)
    terminal_value = terminal_fcf / ((wacc - terminal_growth) / 100)
    pv_terminal = terminal_value / ((1 + wacc / 100) ** projection_years)

    # Total enterprise value = sum of PV of projected FCF + PV of terminal value
    enterprise_value = sum(pv_fcf) + pv_terminal

    # Equity value (assuming no net debt adjustment for simplicity)
    # In production, would subtract net debt
    equity_value = enterprise_value

    # Fair value per share
    fair_value_per_share = equity_value / shares

    return {
        "base_fcf": base_fcf,
        "projected_fcf": projected_fcf,
        "pv_fcf": pv_fcf,
        "terminal_fcf": terminal_fcf,
        "terminal_value": terminal_value,
        "pv_terminal": pv_terminal,
        "enterprise_value": enterprise_value,
        "equity_value": equity_value,
        "fair_value_per_share": fair_value_per_share,
        "sum_pv_fcf": sum(pv_fcf),
    }


def calculate_mos(fair_value: float, current_price: float) -> float:
    """Calculate Margin of Safety percentage."""
    if current_price <= 0:
        return 0
    return ((fair_value - current_price) / current_price) * 100


# ==============================================================================
# Scenario Analysis
# ==============================================================================

def run_scenarios(
    data: Dict,
    base_growth: float,
    base_terminal: float,
    base_wacc: float,
    projection_years: int,
) -> Dict[str, Dict]:
    """
    Run Bear/Base/Bull scenarios.

    Bear: growth -2pp, wacc +1pp
    Base: as specified
    Bull: growth +2pp, wacc -1pp
    """
    scenarios = {}

    # Bear
    scenarios["bear"] = calculate_dcf(
        data["fcf_history"],
        data["shares"],
        growth_rate=base_growth - 2,
        terminal_growth=base_terminal,
        wacc=base_wacc + 1,
        projection_years=projection_years,
    )

    # Base
    scenarios["base"] = calculate_dcf(
        data["fcf_history"],
        data["shares"],
        growth_rate=base_growth,
        terminal_growth=base_terminal,
        wacc=base_wacc,
        projection_years=projection_years,
    )

    # Bull
    scenarios["bull"] = calculate_dcf(
        data["fcf_history"],
        data["shares"],
        growth_rate=base_growth + 2,
        terminal_growth=base_terminal,
        wacc=base_wacc - 1,
        projection_years=projection_years,
    )

    return scenarios


# ==============================================================================
# Output Formatting
# ==============================================================================

def print_dcf_waterfall(ticker: str, data: Dict, dcf: Dict, price: float,
                        currency: str, price_eur: float):
    """Print detailed DCF waterfall calculation."""
    print(f"\n{'='*80}")
    print(f"DCF Analysis: {ticker} - {data['name']}")
    print(f"Current Price: {price:.2f} {currency} ({price_eur:.2f} EUR)")
    print(f"{'='*80}")

    if data.get("fcf_warning"):
        print(f"\n⚠  {data['fcf_warning']}")

    # Historical FCF
    print(f"\nHistorical Free Cash Flow (last {len(data['fcf_history'])} years):")
    for i, fcf in enumerate(data['fcf_history']):
        print(f"  Year {-len(data['fcf_history'])+i+1:+d}: {fcf/1e9:>10.2f}B {currency}")

    # CAGR of historical FCF
    if len(data['fcf_history']) >= 2:
        first_fcf = data['fcf_history'][0]
        last_fcf = data['fcf_history'][-1]
        years = len(data['fcf_history']) - 1
        if first_fcf > 0:
            cagr = ((last_fcf / first_fcf) ** (1 / years) - 1) * 100
            print(f"  Historical FCF CAGR: {cagr:+.1f}%")

    print(f"\nBase FCF (most recent): {dcf['base_fcf']/1e9:.2f}B {currency}")

    # Projected FCF with PV
    print(f"\nProjected FCF & Present Value:")
    print(f"{'Year':>6} {'FCF (B)':>12} {'Discount':>10} {'PV (B)':>12}")
    print("-" * 45)
    for i, (fcf, pv) in enumerate(zip(dcf['projected_fcf'], dcf['pv_fcf']), 1):
        print(f"{i:>6} {fcf/1e9:>12.2f} {1/((1+args.wacc/100)**i):>9.3f}x {pv/1e9:>12.2f}")

    print(f"\nSum of PV(FCF): {dcf['sum_pv_fcf']/1e9:.2f}B {currency}")
    print(f"\nTerminal Value:")
    print(f"  Terminal FCF (Year {len(dcf['projected_fcf'])+1}): {dcf['terminal_fcf']/1e9:.2f}B {currency}")
    print(f"  Terminal Value (Gordon Growth): {dcf['terminal_value']/1e9:.2f}B {currency}")
    print(f"  PV of Terminal Value: {dcf['pv_terminal']/1e9:.2f}B {currency}")
    print(f"    ({dcf['pv_terminal']/dcf['equity_value']*100:.1f}% of total equity value)")

    print(f"\nValuation Summary:")
    print(f"  Enterprise Value: {dcf['enterprise_value']/1e9:.2f}B {currency}")
    print(f"  Equity Value: {dcf['equity_value']/1e9:.2f}B {currency}")
    print(f"  Shares Outstanding: {data['shares']/1e9:.2f}B")
    print(f"  Fair Value/Share: {dcf['fair_value_per_share']:.2f} {currency}")

    mos = calculate_mos(dcf['fair_value_per_share'], price)
    print(f"\nMargin of Safety: {mos:+.1f}%")
    if mos > 25:
        print("  >>> BUY signal (MoS > 25%)")
    elif mos > 0:
        print("  >>> Fair value, slight upside")
    else:
        print("  >>> OVERVALUED")


def print_scenario_table(ticker: str, scenarios: Dict[str, Dict], price: float,
                         currency: str, price_eur: float, data: Dict = None):
    """Print scenario analysis table."""
    print(f"\n{'='*80}")
    print(f"Scenario Analysis: {ticker}")
    print(f"Current Price: {price:.2f} {currency} ({price_eur:.2f} EUR)")
    print(f"{'='*80}")

    if data and data.get("fcf_warning"):
        print(f"\n⚠  {data['fcf_warning']}")

    print(f"\n{'Scenario':<12} {'FV/Share':>12} {'MoS%':>8} {'Equity Value':>15}")
    print("-" * 50)

    for name in ["bear", "base", "bull"]:
        dcf = scenarios[name]
        fv = dcf["fair_value_per_share"]
        mos = calculate_mos(fv, price)
        ev = dcf["equity_value"]
        print(f"{name.upper():<12} {fv:>12.2f} {mos:>+7.1f}% {ev/1e9:>13.2f}B")

    # Range
    bear_fv = scenarios["bear"]["fair_value_per_share"]
    bull_fv = scenarios["bull"]["fair_value_per_share"]
    print(f"\nFair Value Range: {bear_fv:.2f} - {bull_fv:.2f} {currency}")
    print(f"Base Case Fair Value: {scenarios['base']['fair_value_per_share']:.2f} {currency}")

    base_mos = calculate_mos(scenarios['base']['fair_value_per_share'], price)
    if base_mos > 25:
        print(">>> STRONG BUY (Base MoS > 25%)")
    elif base_mos > 15:
        print(">>> BUY (Base MoS > 15%)")
    elif base_mos > 0:
        print(">>> HOLD (Slight upside)")
    else:
        print(">>> OVERVALUED")


def print_summary_table(results: List[Dict], currency_tag: str = ""):
    """Print summary table for batch analysis."""
    if not results:
        return

    print(f"\n{'='*100}")
    print(f"DCF Summary - All Tickers{currency_tag}")
    print(f"{'='*100}")

    header = (f"{'Ticker':<12} {'Name':<25} {'Price':>10} {'Fair Value':>12} "
              f"{'MoS%':>8} {'Equity€B':>10} {'Signal':<12}")
    print(f"\n{header}")
    print("-" * 100)

    for r in sorted(results, key=lambda x: x["mos"], reverse=True):
        signal = "STRONG BUY" if r["mos"] > 25 else "BUY" if r["mos"] > 15 else "HOLD" if r["mos"] > 0 else "OVERVALUED"
        print(f"{r['ticker']:<12} {r['name'][:25]:<25} {r['price']:>10.2f} "
              f"{r['fair_value']:>12.2f} {r['mos']:>+7.1f}% {r['equity_value_eur_b']:>10.2f} "
              f"{signal:<12}")

    # Averages
    n = len(results)
    avg_mos = sum(r["mos"] for r in results) / n
    buy_count = sum(1 for r in results if r["mos"] > 25)
    hold_count = sum(1 for r in results if 0 <= r["mos"] <= 25)
    over_count = sum(1 for r in results if r["mos"] < 0)

    print(f"\n{n} stocks analyzed")
    print(f"Average MoS: {avg_mos:+.1f}%")
    print(f"Strong Buy (MoS>25%): {buy_count} | Hold (0-25%): {hold_count} | Overvalued: {over_count}")


def save_csv(results: List[Dict], filepath: str):
    """Save results to CSV."""
    if not results:
        print("No results to save.")
        return

    fieldnames = ["ticker", "name", "price", "currency", "price_eur",
                  "fair_value", "fair_value_eur", "mos", "equity_value",
                  "equity_value_eur_b", "base_fcf", "terminal_value_pct"]

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(results)

    print(f"\nResults saved to {filepath}")


# ==============================================================================
# Main
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="DCF Calculator - Discounted Cash Flow valuation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 tools/dcf_calculator.py AAPL
  python3 tools/dcf_calculator.py AAPL --growth 8 --terminal 2.5 --wacc 10
  python3 tools/dcf_calculator.py AAPL --years 10 --scenarios
  python3 tools/dcf_calculator.py AAPL MSFT GOOGL --output results.csv
  python3 tools/dcf_calculator.py SAN.MC BNP.PA --scenarios
        """,
    )

    parser.add_argument("tickers", nargs="+", help="Ticker symbols (e.g., AAPL, SAN.MC)")
    parser.add_argument("--growth", type=float, default=5.0,
                        help="FCF growth rate %% for projection period (default: 5)")
    parser.add_argument("--terminal", type=float, default=2.5,
                        help="Terminal perpetual growth rate %% (default: 2.5)")
    parser.add_argument("--wacc", type=float, default=9.0,
                        help="Weighted Average Cost of Capital %% (default: 9)")
    parser.add_argument("--years", type=int, default=5,
                        help="Projection period in years (default: 5)")
    parser.add_argument("--scenarios", action="store_true",
                        help="Run Bear/Base/Bull scenario analysis")
    parser.add_argument("--output", type=str,
                        help="Save results to CSV file")

    global args
    args = parser.parse_args()

    # Validation
    if args.wacc <= args.terminal:
        print("ERROR: WACC must be greater than terminal growth rate", file=sys.stderr)
        sys.exit(1)

    if args.years < 1 or args.years > 20:
        print("ERROR: Projection years must be between 1 and 20", file=sys.stderr)
        sys.exit(1)

    # FX rates
    rates = get_fx_rates()
    print(f"FX Rates: EUR/USD={rates.get('USD', 1.04):.4f} | GBP/EUR={rates.get('GBP', 1.19):.4f}\n",
          file=sys.stderr)

    # Process each ticker
    results = []
    for ticker in args.tickers:
        print(f"\n{'#'*80}", file=sys.stderr)
        print(f"Processing: {ticker}", file=sys.stderr)
        print(f"{'#'*80}", file=sys.stderr)

        # Fetch data
        data = fetch_historical_fcf(ticker, years=5)
        if not data:
            continue

        price = data["price"]
        currency = data["currency"]
        price_eur = to_eur(price, currency, rates)

        if args.scenarios:
            # Scenario analysis
            scenarios = run_scenarios(
                data,
                base_growth=args.growth,
                base_terminal=args.terminal,
                base_wacc=args.wacc,
                projection_years=args.years,
            )
            print_scenario_table(ticker, scenarios, price, currency, price_eur, data)

            # Use base case for CSV
            dcf = scenarios["base"]
        else:
            # Single DCF
            dcf = calculate_dcf(
                data["fcf_history"],
                data["shares"],
                growth_rate=args.growth,
                terminal_growth=args.terminal,
                wacc=args.wacc,
                projection_years=args.years,
            )
            print_dcf_waterfall(ticker, data, dcf, price, currency, price_eur)

        # Store for summary
        fair_value = dcf["fair_value_per_share"]
        fair_value_eur = to_eur(fair_value, currency, rates)
        mos = calculate_mos(fair_value, price)
        equity_value_eur = to_eur(dcf["equity_value"], currency, rates)
        terminal_pct = dcf["pv_terminal"] / dcf["equity_value"] * 100

        results.append({
            "ticker": ticker,
            "name": data["name"],
            "price": price,
            "currency": currency,
            "price_eur": price_eur,
            "fair_value": fair_value,
            "fair_value_eur": fair_value_eur,
            "mos": mos,
            "equity_value": dcf["equity_value"],
            "equity_value_eur_b": equity_value_eur / 1e9,
            "base_fcf": dcf["base_fcf"],
            "terminal_value_pct": terminal_pct,
        })

    # Summary table (if multiple tickers)
    if len(results) > 1:
        print_summary_table(results, currency_tag=" (all values in local currency)")

    # Save CSV
    if args.output:
        save_csv(results, args.output)

    print()  # trailing newline


if __name__ == "__main__":
    main()
