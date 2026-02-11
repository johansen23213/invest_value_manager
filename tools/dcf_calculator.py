#!/usr/bin/env python3
"""
DCF Calculator - Discounted Cash Flow valuation tool.

Fetches historical Free Cash Flow via yfinance, projects future FCF,
calculates terminal value, and determines intrinsic value per share.

IMPORTANT: Properly subtracts net debt (total debt - cash) from enterprise value
to arrive at equity value. This is critical for leveraged companies.

Usage:
  python3 tools/dcf_calculator.py AAPL                          # Default params
  python3 tools/dcf_calculator.py AAPL --growth 8 --terminal 2.5 --wacc 10
  python3 tools/dcf_calculator.py AAPL --years 10                # 10-year projection
  python3 tools/dcf_calculator.py AAPL --scenarios              # Bear/Base/Bull scenarios
  python3 tools/dcf_calculator.py AAPL --sensitivity            # Sensitivity matrix (growth x WACC)
  python3 tools/dcf_calculator.py AAPL --scenarios --sensitivity # Both combined
  python3 tools/dcf_calculator.py AAPL MSFT GOOGL               # Batch analysis
  python3 tools/dcf_calculator.py AAPL --output dcf_results.csv # Save to CSV

Examples:
  python3 tools/dcf_calculator.py SAN.MC --growth 5 --terminal 2 --wacc 9
  python3 tools/dcf_calculator.py ASML.AS --scenarios
  python3 tools/dcf_calculator.py BNP.PA BBVA.MC SAN.MC --output eu_banks_dcf.csv
  python3 tools/dcf_calculator.py WPP.L --scenarios              # LSE stock in GBp
  python3 tools/dcf_calculator.py ADBE --growth 8 --wacc 9 --sensitivity
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
    """Get FX rates for EUR conversion. Reports fallback usage."""
    rates = {}
    fallbacks_used = []
    pairs = {"USD": "EURUSD=X", "GBP": "GBPEUR=X"}
    defaults = {"USD": 1.04, "GBP": 1.19}
    for ccy, symbol in pairs.items():
        try:
            rate = yf.Ticker(symbol).info.get("previousClose")
            if rate:
                rates[ccy] = rate
            else:
                rates[ccy] = defaults[ccy]
                fallbacks_used.append(f"{ccy}={defaults[ccy]}")
        except Exception:
            rates[ccy] = defaults[ccy]
            fallbacks_used.append(f"{ccy}={defaults[ccy]}")
    if fallbacks_used:
        print(f"FX WARNING: Using static fallback rates ({', '.join(fallbacks_used)}). "
              f"EUR conversions may be inaccurate.", file=sys.stderr)
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
    Returns dict with FCF history, shares outstanding, currency, price, and net debt.

    CRITICAL: For LSE stocks (*.L), yfinance returns:
    - Price in GBp (pence)
    - FCF in GBP (pounds)
    This causes a 100x mismatch. We detect and normalize to GBP for internal calculations.
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

        # CRITICAL: Detect GBp (pence) pricing for LSE stocks
        is_gbp_pence = currency in ("GBp", "GBX")
        price_display_currency = currency
        if is_gbp_pence:
            price_normalized = price / 100
            currency_normalized = "GBP"
        else:
            price_normalized = price
            currency_normalized = currency

        # --- NET DEBT CALCULATION ---
        total_debt = info.get("totalDebt", 0) or 0
        total_cash = info.get("totalCash", 0) or 0
        net_debt = total_debt - total_cash

        # Get cashflow statement
        cashflow = stock.cashflow
        if cashflow is None or cashflow.empty:
            print(f"ERROR {ticker}: No cashflow data available", file=sys.stderr)
            return None

        # Extract Free Cash Flow (Operating CF - CapEx)
        fcf_keys = ["Free Cash Flow", "FreeCashFlow", "free cash flow"]
        ocf_keys = [
            "Total Cash From Operating Activities",
            "Operating Cash Flow",
            "TotalCashFromOperatingActivities",
        ]
        capex_keys = [
            "Capital Expenditures",
            "CapitalExpenditures",
            "capital expenditures",
        ]

        fcf_row = None
        for key in fcf_keys:
            if key in cashflow.index:
                fcf_row = cashflow.loc[key]
                break

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
                fcf_row = ocf_row + capex_row
            else:
                print(
                    f"ERROR {ticker}: Cannot calculate FCF (missing OCF or CapEx)",
                    file=sys.stderr,
                )
                return None

        fcf_history = fcf_row.dropna().tolist()[:years]
        fcf_history.reverse()

        if len(fcf_history) < 2:
            print(
                f"ERROR {ticker}: Insufficient FCF history ({len(fcf_history)} years)",
                file=sys.stderr,
            )
            return None

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
            "price_normalized": price_normalized,
            "currency": currency_normalized,
            "display_currency": price_display_currency,
            "is_gbp_pence": is_gbp_pence,
            "shares": shares,
            "fcf_history": fcf_history,
            "fcf_warning": fcf_warning,
            "net_debt": net_debt,
            "total_debt": total_debt,
            "total_cash": total_cash,
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
    net_debt: float = 0,
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
        net_debt: Net debt (total debt - cash). Subtracted from EV to get equity value.

    Returns:
        Dict with projected FCF, PV, terminal value, equity value, fair value/share
    """
    base_fcf = fcf_history[-1]

    projected_fcf = []
    pv_fcf = []
    for year in range(1, projection_years + 1):
        fcf = base_fcf * ((1 + growth_rate / 100) ** year)
        pv = fcf / ((1 + wacc / 100) ** year)
        projected_fcf.append(fcf)
        pv_fcf.append(pv)

    terminal_fcf = projected_fcf[-1] * (1 + terminal_growth / 100)
    terminal_value = terminal_fcf / ((wacc - terminal_growth) / 100)
    pv_terminal = terminal_value / ((1 + wacc / 100) ** projection_years)

    enterprise_value = sum(pv_fcf) + pv_terminal

    # Equity value = Enterprise Value - Net Debt
    equity_value = enterprise_value - net_debt
    if equity_value <= 0:
        equity_value = 0

    fair_value_per_share = equity_value / shares if shares > 0 else 0

    return {
        "base_fcf": base_fcf,
        "projected_fcf": projected_fcf,
        "pv_fcf": pv_fcf,
        "terminal_fcf": terminal_fcf,
        "terminal_value": terminal_value,
        "pv_terminal": pv_terminal,
        "enterprise_value": enterprise_value,
        "net_debt": net_debt,
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
    bear_growth_delta: float = -2.0,
    bear_wacc_delta: float = 1.0,
    bull_growth_delta: float = 2.0,
    bull_wacc_delta: float = -1.0,
) -> Dict[str, Dict]:
    """Run Bear/Base/Bull scenarios with configurable deltas."""
    net_debt = data.get("net_debt", 0)
    scenarios = {}

    scenarios["bear"] = calculate_dcf(
        data["fcf_history"], data["shares"],
        growth_rate=base_growth + bear_growth_delta, terminal_growth=base_terminal,
        wacc=base_wacc + bear_wacc_delta, projection_years=projection_years, net_debt=net_debt,
    )
    scenarios["base"] = calculate_dcf(
        data["fcf_history"], data["shares"],
        growth_rate=base_growth, terminal_growth=base_terminal,
        wacc=base_wacc, projection_years=projection_years, net_debt=net_debt,
    )
    scenarios["bull"] = calculate_dcf(
        data["fcf_history"], data["shares"],
        growth_rate=base_growth + bull_growth_delta, terminal_growth=base_terminal,
        wacc=base_wacc + bull_wacc_delta, projection_years=projection_years, net_debt=net_debt,
    )

    # Store deltas for display
    scenarios["_deltas"] = {
        "bear_growth": bear_growth_delta, "bear_wacc": bear_wacc_delta,
        "bull_growth": bull_growth_delta, "bull_wacc": bull_wacc_delta,
    }

    return scenarios


# ==============================================================================
# Sensitivity Analysis
# ==============================================================================

def run_sensitivity(
    data: Dict,
    base_growth: float,
    base_terminal: float,
    base_wacc: float,
    projection_years: int,
) -> Dict:
    """
    Run sensitivity matrix: Growth (5 steps) x WACC (3 steps).

    Growth steps:  base-3%, base-1.5%, base, base+1.5%, base+3%
    WACC steps:    base-1.5%, base, base+1.5%

    Returns dict with matrix of FV per share, base case DCF result,
    and metadata for display.
    """
    net_debt = data.get("net_debt", 0)

    growth_deltas = [-3.0, -1.5, 0.0, +1.5, +3.0]
    wacc_deltas = [-1.5, 0.0, +1.5]

    growth_values = [base_growth + d for d in growth_deltas]
    wacc_values = [base_wacc + d for d in wacc_deltas]

    # matrix[i][j] = FV per share for growth_values[i] x wacc_values[j]
    # None if WACC <= terminal growth (invalid Gordon Growth)
    matrix = []
    all_fv = []

    for g in growth_values:
        row = []
        for w in wacc_values:
            if w <= base_terminal:
                row.append(None)  # Invalid: WACC must exceed terminal growth
            else:
                dcf = calculate_dcf(
                    data["fcf_history"], data["shares"],
                    growth_rate=g, terminal_growth=base_terminal,
                    wacc=w, projection_years=projection_years, net_debt=net_debt,
                )
                fv = dcf["fair_value_per_share"]
                row.append(fv)
                all_fv.append(fv)
        matrix.append(row)

    # Base case DCF (for TV% calculation)
    base_dcf = calculate_dcf(
        data["fcf_history"], data["shares"],
        growth_rate=base_growth, terminal_growth=base_terminal,
        wacc=base_wacc, projection_years=projection_years, net_debt=net_debt,
    )

    # FV Spread = (max - min) / base as percentage
    base_fv = base_dcf["fair_value_per_share"]
    if all_fv and base_fv > 0:
        fv_spread = ((max(all_fv) - min(all_fv)) / base_fv) * 100
    else:
        fv_spread = 0.0

    # Terminal Value as % of Enterprise Value
    tv_pct = (
        base_dcf["pv_terminal"] / base_dcf["enterprise_value"] * 100
        if base_dcf["enterprise_value"] > 0 else 0
    )

    return {
        "matrix": matrix,
        "growth_values": growth_values,
        "wacc_values": wacc_values,
        "base_dcf": base_dcf,
        "base_fv": base_fv,
        "fv_spread": fv_spread,
        "tv_pct": tv_pct,
        "all_fv": all_fv,
    }


def print_sensitivity_matrix(ticker: str, data: Dict, sensitivity: Dict):
    """Print the sensitivity analysis matrix and confidence assessment."""
    display_currency = data["display_currency"]
    price_display = data["price"]
    price_normalized = data["price_normalized"]

    base_fv_display, _ = format_price_and_currency(sensitivity["base_fv"], data)

    print(f"\n{'='*80}")
    print(f"Sensitivity Analysis: {ticker}")
    print(f"Current Price: {price_display:.2f} {display_currency}")
    print(f"Base Fair Value: {base_fv_display:.2f} {display_currency}")
    print(f"{'='*80}")

    matrix = sensitivity["matrix"]
    growth_values = sensitivity["growth_values"]
    wacc_values = sensitivity["wacc_values"]

    # Header row: WACC values
    wacc_header = f"{'Growth \\ WACC':>14}"
    for w in wacc_values:
        wacc_header += f"  {w:>8.1f}%"
    print(f"\n{wacc_header}")
    print("-" * (14 + len(wacc_values) * 10 + 2))

    # Matrix rows
    for i, g in enumerate(growth_values):
        row_str = f"  {g:>8.1f}%    "
        for j, w in enumerate(wacc_values):
            fv = matrix[i][j]
            if fv is None:
                row_str += f"  {'N/A':>8}"
            else:
                fv_display, _ = format_price_and_currency(fv, data)
                row_str += f"  {fv_display:>8.1f}"
        print(row_str)

    # Display currency note
    print(f"\n  Values in {display_currency}")

    # FV Range from the matrix
    all_fv = sensitivity["all_fv"]
    if all_fv:
        min_fv_display, _ = format_price_and_currency(min(all_fv), data)
        max_fv_display, _ = format_price_and_currency(max(all_fv), data)
        print(f"\n  FV Range: {min_fv_display:.1f} - {max_fv_display:.1f} {display_currency}")

    # FV Spread
    fv_spread = sensitivity["fv_spread"]
    print(f"  FV Spread: {fv_spread:.0f}% (max-min relative to base)")

    # MoS at extremes
    if all_fv:
        mos_min = calculate_mos(min(all_fv), price_normalized)
        mos_max = calculate_mos(max(all_fv), price_normalized)
        print(f"  MoS Range: {mos_min:+.1f}% (worst) to {mos_max:+.1f}% (best)")

    # Sensitivity Data
    tv_pct = sensitivity["tv_pct"]
    print(f"\nSensitivity Data:")
    print(f"  Terminal Value as % of EV: {tv_pct:.1f}%")
    print(f"  FV Spread: {fv_spread:.0f}%")
    print(f"\n  [Apply learning/principles.md to interpret sensitivity]")


# ==============================================================================
# Output Formatting
# ==============================================================================

def format_price_and_currency(price: float, data: Dict) -> Tuple[float, str]:
    """Format price for display. For LSE stocks (GBp), convert GBP to GBp."""
    if data["is_gbp_pence"]:
        return price * 100, data["display_currency"]
    else:
        return price, data["currency"]


def print_dcf_waterfall(
    ticker: str, data: Dict, dcf: Dict, price: float,
    currency: str, price_eur: float,
):
    """Print detailed DCF waterfall calculation."""
    fair_value_display, display_currency = format_price_and_currency(
        dcf["fair_value_per_share"], data,
    )
    price_display = data["price"]

    print(f"\n{'='*80}")
    print(f"DCF Analysis: {ticker} - {data['name']}")
    print(f"Current Price: {price_display:.2f} {data['display_currency']} ({price_eur:.2f} EUR)")
    print(f"{'='*80}")

    if data.get("fcf_warning"):
        print(f"\n!!  {data['fcf_warning']}")

    fcf_currency = data["currency"]
    print(f"\nHistorical Free Cash Flow (last {len(data['fcf_history'])} years):")
    for i, fcf in enumerate(data["fcf_history"]):
        print(f"  Year {-len(data['fcf_history'])+i+1:+d}: {fcf/1e9:>10.2f}B {fcf_currency}")

    if len(data["fcf_history"]) >= 2:
        first_fcf = data["fcf_history"][0]
        last_fcf = data["fcf_history"][-1]
        years = len(data["fcf_history"]) - 1
        if first_fcf > 0:
            cagr = ((last_fcf / first_fcf) ** (1 / years) - 1) * 100
            print(f"  Historical FCF CAGR: {cagr:+.1f}%")

    print(f"\nBase FCF (most recent): {dcf['base_fcf']/1e9:.2f}B {fcf_currency}")

    print("\nProjected FCF & Present Value:")
    print(f"{'Year':>6} {'FCF (B)':>12} {'Discount':>10} {'PV (B)':>12}")
    print("-" * 45)
    for i, (fcf, pv) in enumerate(zip(dcf["projected_fcf"], dcf["pv_fcf"]), 1):
        print(f"{i:>6} {fcf/1e9:>12.2f} {1/((1+args.wacc/100)**i):>9.3f}x {pv/1e9:>12.2f}")

    print(f"\nSum of PV(FCF): {dcf['sum_pv_fcf']/1e9:.2f}B {fcf_currency}")
    print("\nTerminal Value:")
    print(f"  Terminal FCF (Year {len(dcf['projected_fcf'])+1}): {dcf['terminal_fcf']/1e9:.2f}B {fcf_currency}")
    print(f"  Terminal Value (Gordon Growth): {dcf['terminal_value']/1e9:.2f}B {fcf_currency}")
    print(f"  PV of Terminal Value: {dcf['pv_terminal']/1e9:.2f}B {fcf_currency}")
    tv_pct = dcf["pv_terminal"] / dcf["enterprise_value"] * 100 if dcf["enterprise_value"] > 0 else 0
    print(f"    ({tv_pct:.1f}% of enterprise value)")

    print("\nValuation Summary:")
    print(f"  Enterprise Value: {dcf['enterprise_value']/1e9:.2f}B {fcf_currency}")
    net_debt = dcf.get("net_debt", 0)
    print(f"  (-) Net Debt: {net_debt/1e9:.2f}B {fcf_currency}")
    print(f"  (=) Equity Value: {dcf['equity_value']/1e9:.2f}B {fcf_currency}")
    print(f"  Shares Outstanding: {data['shares']/1e9:.2f}B")
    print(f"  Fair Value/Share: {fair_value_display:.2f} {data['display_currency']}")

    mos = calculate_mos(dcf["fair_value_per_share"], data["price_normalized"])
    print(f"\nMargin of Safety: {mos:+.1f}%")


def print_scenario_table(
    ticker: str, scenarios: Dict[str, Dict], price: float,
    currency: str, price_eur: float, data: Dict = None,
):
    """Print scenario analysis table."""
    price_display = data["price"]

    print(f"\n{'='*80}")
    print(f"Scenario Analysis: {ticker}")
    print(f"Current Price: {price_display:.2f} {data['display_currency']} ({price_eur:.2f} EUR)")
    print(f"Net Debt: {data.get('net_debt', 0)/1e9:.2f}B {data['currency']}")
    print(f"{'='*80}")

    if data and data.get("fcf_warning"):
        print(f"\n!!  {data['fcf_warning']}")

    print(f"\n{'Scenario':<12} {'FV/Share':>12} {'MoS%':>8} {'EV':>12} {'Equity':>12}")
    print("-" * 60)

    for name in ["bear", "base", "bull"]:
        dcf = scenarios[name]
        fv = dcf["fair_value_per_share"]
        fv_display, _ = format_price_and_currency(fv, data)
        mos = calculate_mos(fv, data["price_normalized"])
        ev = dcf["enterprise_value"]
        eq = dcf["equity_value"]
        print(f"{name.upper():<12} {fv_display:>12.2f} {mos:>+7.1f}% {ev/1e9:>10.2f}B {eq/1e9:>10.2f}B")

    bear_fv_display, _ = format_price_and_currency(scenarios["bear"]["fair_value_per_share"], data)
    bull_fv_display, _ = format_price_and_currency(scenarios["bull"]["fair_value_per_share"], data)
    base_fv_display, _ = format_price_and_currency(scenarios["base"]["fair_value_per_share"], data)

    print(f"\nFair Value Range: {bear_fv_display:.2f} - {bull_fv_display:.2f} {data['display_currency']}")
    print(f"Base Case Fair Value: {base_fv_display:.2f} {data['display_currency']}")

    base_mos = calculate_mos(scenarios["base"]["fair_value_per_share"], data["price_normalized"])
    print(f"Base Case MoS: {base_mos:+.1f}%")


def print_summary_table(results: List[Dict], currency_tag: str = ""):
    """Print summary table for batch analysis."""
    if not results:
        return

    print(f"\n{'='*100}")
    print(f"DCF Summary - All Tickers{currency_tag}")
    print(f"{'='*100}")

    header = (
        f"{'Ticker':<12} {'Name':<25} {'Price':>10} {'Fair Value':>12} "
        f"{'MoS%':>8} {'Equity\u20acB':>10}"
    )
    print(f"\n{header}")
    print("-" * 88)

    for r in sorted(results, key=lambda x: x["mos"], reverse=True):
        print(
            f"{r['ticker']:<12} {r['name'][:25]:<25} {r['price_display']:>10.2f} "
            f"{r['fair_value_display']:>12.2f} {r['mos']:>+7.1f}% {r['equity_value_eur_b']:>10.2f}"
        )

    n = len(results)
    avg_mos = sum(r["mos"] for r in results) / n
    mos_values = sorted([r["mos"] for r in results])
    median_mos = mos_values[len(mos_values) // 2]

    print(f"\n{n} stocks analyzed")
    print(f"Average MoS: {avg_mos:+.1f}% | Median: {median_mos:+.1f}%")
    print(f"\n[Apply learning/principles.md to reason about these valuations]")


def save_csv(results: List[Dict], filepath: str):
    """Save results to CSV."""
    if not results:
        print("No results to save.")
        return

    fieldnames = [
        "ticker", "name", "price", "currency", "price_eur",
        "fair_value", "fair_value_eur", "mos", "equity_value",
        "equity_value_eur_b", "base_fcf", "terminal_value_pct",
    ]

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
  python3 tools/dcf_calculator.py WPP.L --scenarios  # LSE stock in GBp
  python3 tools/dcf_calculator.py ADBE --growth 8 --wacc 9 --sensitivity
        """,
    )

    parser.add_argument("tickers", nargs="+", help="Ticker symbols (e.g., AAPL, SAN.MC, WPP.L)")
    parser.add_argument(
        "--growth", type=float, default=5.0,
        help="FCF growth rate %% for projection period (default: 5)",
    )
    parser.add_argument(
        "--terminal", type=float, default=2.5,
        help="Terminal perpetual growth rate %% (default: 2.5)",
    )
    parser.add_argument(
        "--wacc", type=float, default=9.0,
        help="Weighted Average Cost of Capital %% (default: 9)",
    )
    parser.add_argument(
        "--years", type=int, default=5,
        help="Projection period in years (default: 5)",
    )
    parser.add_argument(
        "--scenarios", action="store_true",
        help="Run Bear/Base/Bull scenario analysis",
    )
    parser.add_argument(
        "--sensitivity", action="store_true",
        help="Run sensitivity matrix (Growth x WACC)",
    )
    parser.add_argument(
        "--bear-growth-delta", type=float, default=-2.0,
        help="Bear scenario growth delta in pp (default: -2.0)",
    )
    parser.add_argument(
        "--bear-wacc-delta", type=float, default=1.0,
        help="Bear scenario WACC delta in pp (default: +1.0)",
    )
    parser.add_argument(
        "--bull-growth-delta", type=float, default=2.0,
        help="Bull scenario growth delta in pp (default: +2.0)",
    )
    parser.add_argument(
        "--bull-wacc-delta", type=float, default=-1.0,
        help="Bull scenario WACC delta in pp (default: -1.0)",
    )
    parser.add_argument("--output", type=str, help="Save results to CSV file")

    global args
    args = parser.parse_args()

    if args.wacc <= args.terminal:
        print("ERROR: WACC must be greater than terminal growth rate", file=sys.stderr)
        sys.exit(1)

    if args.years < 1 or args.years > 20:
        print("ERROR: Projection years must be between 1 and 20", file=sys.stderr)
        sys.exit(1)

    rates = get_fx_rates()
    print(
        f"FX Rates: EUR/USD={rates.get('USD', 1.04):.4f} | GBP/EUR={rates.get('GBP', 1.19):.4f}\n",
        file=sys.stderr,
    )

    results = []
    for ticker in args.tickers:
        print(f"\n{'#'*80}", file=sys.stderr)
        print(f"Processing: {ticker}", file=sys.stderr)
        print(f"{'#'*80}", file=sys.stderr)

        data = fetch_historical_fcf(ticker, years=5)
        if not data:
            continue

        price_normalized = data["price_normalized"]
        price_display = data["price"]
        currency = data["currency"]
        price_eur = to_eur(price_normalized, currency, rates)

        if args.scenarios:
            scenarios = run_scenarios(
                data,
                base_growth=args.growth,
                base_terminal=args.terminal,
                base_wacc=args.wacc,
                projection_years=args.years,
                bear_growth_delta=args.bear_growth_delta,
                bear_wacc_delta=args.bear_wacc_delta,
                bull_growth_delta=args.bull_growth_delta,
                bull_wacc_delta=args.bull_wacc_delta,
            )
            print_scenario_table(ticker, scenarios, price_normalized, currency, price_eur, data)
            dcf = scenarios["base"]
        else:
            dcf = calculate_dcf(
                data["fcf_history"],
                data["shares"],
                growth_rate=args.growth,
                terminal_growth=args.terminal,
                wacc=args.wacc,
                projection_years=args.years,
                net_debt=data.get("net_debt", 0),
            )
            print_dcf_waterfall(ticker, data, dcf, price_normalized, currency, price_eur)

        # Sensitivity analysis (runs AFTER base waterfall or scenarios)
        if args.sensitivity:
            sensitivity = run_sensitivity(
                data,
                base_growth=args.growth,
                base_terminal=args.terminal,
                base_wacc=args.wacc,
                projection_years=args.years,
            )
            print_sensitivity_matrix(ticker, data, sensitivity)

        fair_value = dcf["fair_value_per_share"]
        fair_value_display, _ = format_price_and_currency(fair_value, data)
        fair_value_eur = to_eur(fair_value, currency, rates)
        mos = calculate_mos(fair_value, price_normalized)
        equity_value_eur = to_eur(dcf["equity_value"], currency, rates)
        terminal_pct = (
            dcf["pv_terminal"] / dcf["enterprise_value"] * 100
            if dcf["enterprise_value"] > 0 else 0
        )

        results.append({
            "ticker": ticker,
            "name": data["name"],
            "price": price_normalized,
            "price_display": price_display,
            "currency": currency,
            "price_eur": price_eur,
            "fair_value": fair_value,
            "fair_value_display": fair_value_display,
            "fair_value_eur": fair_value_eur,
            "mos": mos,
            "equity_value": dcf["equity_value"],
            "equity_value_eur_b": equity_value_eur / 1e9,
            "base_fcf": dcf["base_fcf"],
            "terminal_value_pct": terminal_pct,
        })

    if len(results) > 1:
        print_summary_table(results, currency_tag=" (prices in display currency)")

    if args.output:
        save_csv(results, args.output)

    print()


if __name__ == "__main__":
    main()
