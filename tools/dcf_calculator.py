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
  python3 tools/dcf_calculator.py AAPL --reverse                # Reverse DCF: implied expectations
  python3 tools/dcf_calculator.py ROP ADBE NVO --reverse        # Reverse DCF batch

Reverse DCF (--reverse) shows:
  - Implied FCF growth rate from current price
  - Enhanced gap analysis (revenue growth, EBIT margin, FCF conversion vs historical)
  - Scenario math (what growth/margin/multiple justifies current price)
  - Asymmetry ratio (bull upside vs bear downside)

Examples:
  python3 tools/dcf_calculator.py SAN.MC --growth 5 --terminal 2 --wacc 9
  python3 tools/dcf_calculator.py ASML.AS --scenarios
  python3 tools/dcf_calculator.py BNP.PA BBVA.MC SAN.MC --output eu_banks_dcf.csv
  python3 tools/dcf_calculator.py WPP.L --scenarios              # LSE stock in GBp
  python3 tools/dcf_calculator.py ADBE --growth 8 --wacc 9 --sensitivity
  python3 tools/dcf_calculator.py --reverse ROP ADBE NVO         # Reverse DCF batch
"""

import sys
import argparse
import csv
import math
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
# Helper: safe CAGR calculation
# ==============================================================================

def _safe_cagr(values: List[float], n_years: Optional[int] = None) -> Optional[float]:
    """
    Calculate CAGR from a list of values (oldest to newest).
    Returns percentage or None if insufficient/invalid data.
    """
    if not values or len(values) < 2:
        return None
    first = values[0]
    last = values[-1]
    n = n_years if n_years is not None else (len(values) - 1)
    if n <= 0 or first <= 0 or last <= 0:
        return None
    return ((last / first) ** (1.0 / n) - 1.0) * 100.0


def _safe_avg(values: List[float]) -> Optional[float]:
    """Average of non-None, non-zero values. Returns None if empty."""
    valid = [v for v in values if v is not None and v != 0]
    if not valid:
        return None
    return sum(valid) / len(valid)


# ==============================================================================
# Data Fetching
# ==============================================================================

def _extract_row(df: pd.DataFrame, keys: List[str], years: int = 5) -> List[float]:
    """Extract a row from a DataFrame by trying multiple key names, return list oldest-to-newest."""
    if df is None or df.empty:
        return []
    for key in keys:
        if key in df.index:
            vals = df.loc[key].dropna().tolist()[:years]
            vals.reverse()
            return vals
    return []


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

        # --- MARKET CAP ---
        market_cap = info.get("marketCap", 0) or 0
        if not market_cap:
            # Fallback: compute from price and shares
            market_cap = price_normalized * shares

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

        # --- FINANCIAL STATEMENT DATA ---
        # Revenue, EBIT/operating income, and operating cash flow for reverse DCF
        revenue_history = []
        revenue_growth_3yr = None
        ebit_history = []
        ebit_margin_history = []
        ocf_history = []

        try:
            financials = stock.financials
            if financials is not None and not financials.empty:
                # Revenue
                rev_keys = ["Total Revenue", "TotalRevenue", "Revenue"]
                revenue_history = _extract_row(financials, rev_keys, years)
                if len(revenue_history) >= 2:
                    n_rev = len(revenue_history) - 1
                    first_rev = revenue_history[0]
                    last_rev = revenue_history[-1]
                    if first_rev > 0 and last_rev > 0:
                        revenue_growth_3yr = ((last_rev / first_rev) ** (1 / n_rev) - 1) * 100

                # EBIT / Operating Income
                ebit_keys = [
                    "EBIT", "Operating Income", "OperatingIncome",
                    "Ebit", "operatingIncome",
                ]
                ebit_history = _extract_row(financials, ebit_keys, years)

                # Compute EBIT margins if we have both revenue and EBIT
                if revenue_history and ebit_history:
                    min_len = min(len(revenue_history), len(ebit_history))
                    for i in range(min_len):
                        rev = revenue_history[i]
                        ebit = ebit_history[i]
                        if rev and rev > 0:
                            ebit_margin_history.append((ebit / rev) * 100.0)
                        else:
                            ebit_margin_history.append(None)
        except Exception:
            pass  # Financial data is optional for reverse DCF context

        # Operating Cash Flow history (for FCF conversion ratio)
        try:
            ocf_history = _extract_row(cashflow, ocf_keys, years)
        except Exception:
            pass

        # FCF conversion ratio = FCF / revenue (for each year)
        fcf_conversion_history = []
        if revenue_history and fcf_history:
            min_len = min(len(revenue_history), len(fcf_history))
            for i in range(min_len):
                rev = revenue_history[i]
                fcf = fcf_history[i]
                if rev and rev > 0:
                    fcf_conversion_history.append((fcf / rev) * 100.0)
                else:
                    fcf_conversion_history.append(None)

        # Current EV/EBIT multiple
        ev_ebit_current = None
        ev = market_cap + net_debt
        if ebit_history and ebit_history[-1] and ebit_history[-1] > 0:
            ev_ebit_current = ev / ebit_history[-1]

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
            "market_cap": market_cap,
            "revenue_history": revenue_history,
            "revenue_growth_3yr": revenue_growth_3yr,
            "ebit_history": ebit_history,
            "ebit_margin_history": ebit_margin_history,
            "ocf_history": ocf_history,
            "fcf_conversion_history": fcf_conversion_history,
            "ev_ebit_current": ev_ebit_current,
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
# Reverse DCF (Implied Expectations)
# ==============================================================================

def calculate_reverse_dcf(
    data: Dict,
    wacc: float,
    terminal_growth: float,
    projection_years: int,
) -> Optional[float]:
    """
    Solve backwards for the implied FCF growth rate that justifies
    the current market price, using bisection method.

    Given market cap + net debt = EV, find the growth rate g such that
    calculate_dcf(g) produces fair_value_per_share ~= current price.

    Args:
        data: Dict from fetch_historical_fcf
        wacc: WACC in %
        terminal_growth: Terminal growth in %
        projection_years: Number of years for projection

    Returns:
        Implied growth rate in %, or None if bisection fails to converge
    """
    target_price = data["price_normalized"]
    fcf_history = data["fcf_history"]
    shares = data["shares"]
    net_debt = data.get("net_debt", 0)

    # Tolerance: 0.01% of target price
    tolerance = target_price * 0.0001

    # Search range: -20% to +50% growth rate
    lo = -20.0
    hi = 50.0
    max_iterations = 100

    def fv_at_growth(g: float) -> float:
        dcf = calculate_dcf(
            fcf_history, shares,
            growth_rate=g,
            terminal_growth=terminal_growth,
            wacc=wacc,
            projection_years=projection_years,
            net_debt=net_debt,
        )
        return dcf["fair_value_per_share"]

    # Check if solution is within bounds
    fv_lo = fv_at_growth(lo)
    fv_hi = fv_at_growth(hi)

    # If current price is below even the -20% growth scenario, implied growth < -20%
    if target_price < fv_lo:
        return lo
    # If current price is above even the +50% growth scenario, implied growth > 50%
    if target_price > fv_hi:
        return hi

    # Bisection
    for _ in range(max_iterations):
        mid = (lo + hi) / 2.0
        fv_mid = fv_at_growth(mid)

        if abs(fv_mid - target_price) < tolerance:
            return mid

        if fv_mid < target_price:
            lo = mid
        else:
            hi = mid

    # Return best estimate even if not perfectly converged
    return (lo + hi) / 2.0


def _solve_for_variable(
    data: Dict,
    wacc: float,
    terminal_growth: float,
    projection_years: int,
    variable: str,
    lo: float,
    hi: float,
) -> Optional[float]:
    """
    Generic bisection solver for reverse scenario math.
    Solves for the value of 'variable' that makes FV = current price.

    variable: 'wacc' or 'terminal_growth'
    """
    target_price = data["price_normalized"]
    fcf_history = data["fcf_history"]
    shares = data["shares"]
    net_debt = data.get("net_debt", 0)
    tolerance = target_price * 0.0001
    max_iterations = 100

    def fv_at(val: float) -> float:
        w = val if variable == "wacc" else wacc
        tg = val if variable == "terminal_growth" else terminal_growth
        if w <= tg:
            return 0
        dcf = calculate_dcf(
            fcf_history, shares,
            growth_rate=0,  # not used for these variables
            terminal_growth=tg,
            wacc=w,
            projection_years=projection_years,
            net_debt=net_debt,
        )
        return dcf["fair_value_per_share"]

    for _ in range(max_iterations):
        mid = (lo + hi) / 2.0
        fv_mid = fv_at(mid)
        if abs(fv_mid - target_price) < tolerance:
            return mid
        # For WACC: higher WACC = lower FV. For terminal: higher terminal = higher FV
        if variable == "wacc":
            if fv_mid > target_price:
                lo = mid
            else:
                hi = mid
        else:
            if fv_mid < target_price:
                lo = mid
            else:
                hi = mid

    return (lo + hi) / 2.0


def _solve_reverse_revenue_growth(
    data: Dict,
    wacc: float,
    terminal_growth: float,
    projection_years: int,
    fixed_margin: float,
    fixed_fcf_conversion: float,
) -> Optional[float]:
    """
    Solve for revenue CAGR that justifies current price, given fixed margin
    and FCF conversion. Uses revenue-based projection instead of FCF-based.

    fixed_margin: EBIT margin as decimal (e.g. 0.30 for 30%)
    fixed_fcf_conversion: FCF/EBIT ratio as decimal (e.g. 0.80 for 80%)
    """
    target_price = data["price_normalized"]
    shares = data["shares"]
    net_debt = data.get("net_debt", 0)
    revenue_history = data.get("revenue_history", [])

    if not revenue_history or revenue_history[-1] <= 0:
        return None

    base_revenue = revenue_history[-1]
    tolerance = target_price * 0.0001
    lo = -20.0
    hi = 50.0
    max_iterations = 100

    def fv_at_rev_growth(g: float) -> float:
        projected_fcf = []
        pv_fcf = []
        for year in range(1, projection_years + 1):
            rev = base_revenue * ((1 + g / 100) ** year)
            ebit = rev * fixed_margin
            fcf = ebit * fixed_fcf_conversion
            pv = fcf / ((1 + wacc / 100) ** year)
            projected_fcf.append(fcf)
            pv_fcf.append(pv)

        terminal_fcf = projected_fcf[-1] * (1 + terminal_growth / 100)
        tv = terminal_fcf / ((wacc - terminal_growth) / 100)
        pv_tv = tv / ((1 + wacc / 100) ** projection_years)

        ev = sum(pv_fcf) + pv_tv
        equity = max(ev - net_debt, 0)
        return equity / shares if shares > 0 else 0

    fv_lo = fv_at_rev_growth(lo)
    fv_hi = fv_at_rev_growth(hi)

    if target_price < fv_lo:
        return lo
    if target_price > fv_hi:
        return hi

    for _ in range(max_iterations):
        mid = (lo + hi) / 2.0
        fv_mid = fv_at_rev_growth(mid)
        if abs(fv_mid - target_price) < tolerance:
            return mid
        if fv_mid < target_price:
            lo = mid
        else:
            hi = mid

    return (lo + hi) / 2.0


def _solve_reverse_margin(
    data: Dict,
    wacc: float,
    terminal_growth: float,
    projection_years: int,
    fixed_rev_growth: float,
    fixed_fcf_conversion: float,
) -> Optional[float]:
    """
    Solve for EBIT margin that justifies current price, given fixed revenue growth
    and FCF conversion. Returns margin as percentage.
    """
    target_price = data["price_normalized"]
    shares = data["shares"]
    net_debt = data.get("net_debt", 0)
    revenue_history = data.get("revenue_history", [])

    if not revenue_history or revenue_history[-1] <= 0:
        return None

    base_revenue = revenue_history[-1]
    tolerance = target_price * 0.0001
    lo = 0.0
    hi = 80.0  # 80% EBIT margin as upper bound
    max_iterations = 100

    def fv_at_margin(m: float) -> float:
        margin_dec = m / 100.0
        projected_fcf = []
        pv_fcf = []
        for year in range(1, projection_years + 1):
            rev = base_revenue * ((1 + fixed_rev_growth / 100) ** year)
            ebit = rev * margin_dec
            fcf = ebit * fixed_fcf_conversion
            pv = fcf / ((1 + wacc / 100) ** year)
            projected_fcf.append(fcf)
            pv_fcf.append(pv)

        terminal_fcf = projected_fcf[-1] * (1 + terminal_growth / 100)
        tv = terminal_fcf / ((wacc - terminal_growth) / 100)
        pv_tv = tv / ((1 + wacc / 100) ** projection_years)

        ev = sum(pv_fcf) + pv_tv
        equity = max(ev - net_debt, 0)
        return equity / shares if shares > 0 else 0

    fv_lo = fv_at_margin(lo)
    fv_hi = fv_at_margin(hi)

    if target_price < fv_lo:
        return None  # Even 0% margin gives higher FV than price (shouldn't happen)
    if target_price > fv_hi:
        return None  # Even 80% margin is not enough

    for _ in range(max_iterations):
        mid = (lo + hi) / 2.0
        fv_mid = fv_at_margin(mid)
        if abs(fv_mid - target_price) < tolerance:
            return mid
        if fv_mid < target_price:
            lo = mid
        else:
            hi = mid

    return (lo + hi) / 2.0


def _solve_reverse_terminal_multiple(
    data: Dict,
    wacc: float,
    projection_years: int,
    growth_rate: float,
) -> Optional[float]:
    """
    Solve for the terminal EV/FCF multiple implied by current price.
    Instead of Gordon Growth terminal value, backs out the exit multiple.

    Returns terminal EV/FCF multiple.
    """
    target_price = data["price_normalized"]
    fcf_history = data["fcf_history"]
    shares = data["shares"]
    net_debt = data.get("net_debt", 0)

    if not fcf_history or fcf_history[-1] <= 0:
        return None

    base_fcf = fcf_history[-1]

    # Project FCF and PV of projection period
    projected_fcf = []
    pv_fcf = []
    for year in range(1, projection_years + 1):
        fcf = base_fcf * ((1 + growth_rate / 100) ** year)
        pv = fcf / ((1 + wacc / 100) ** year)
        projected_fcf.append(fcf)
        pv_fcf.append(pv)

    sum_pv = sum(pv_fcf)
    terminal_fcf = projected_fcf[-1]

    # target_price = (sum_pv + TV_pv - net_debt) / shares
    # TV_pv = (target_price * shares + net_debt) - sum_pv
    target_equity = target_price * shares
    target_ev = target_equity + net_debt
    pv_terminal_needed = target_ev - sum_pv

    if pv_terminal_needed <= 0:
        return 0  # No terminal value needed (already covered by projection period)

    # Terminal Value = pv_terminal_needed * (1 + wacc)^n
    terminal_value = pv_terminal_needed * ((1 + wacc / 100) ** projection_years)

    # Terminal EV/FCF multiple = Terminal Value / Terminal Year FCF
    if terminal_fcf > 0:
        return terminal_value / terminal_fcf
    return None


# ------------------------------------------------------------------------------
# Enhanced Reverse DCF Sections
# ------------------------------------------------------------------------------

def _print_enhanced_gap_analysis(
    data: Dict,
    implied_growth: float,
):
    """
    Print enhanced gap analysis comparing implied expectations vs historical
    across multiple dimensions: revenue growth, EBIT margin, FCF conversion.
    """
    revenue_history = data.get("revenue_history", [])
    ebit_margin_history = data.get("ebit_margin_history", [])
    fcf_conversion_history = data.get("fcf_conversion_history", [])
    fcf_history = data.get("fcf_history", [])

    print(f"\n{'- '*40}")
    print(f"ENHANCED GAP ANALYSIS")
    print(f"{'- '*40}")
    print(f"  Implied vs Historical:")

    # --- Revenue Growth ---
    rev_cagr_3yr = None
    rev_cagr_5yr = None
    if len(revenue_history) >= 4:
        rev_cagr_3yr = _safe_cagr(revenue_history[-4:])
    if len(revenue_history) >= 5:
        rev_cagr_5yr = _safe_cagr(revenue_history)
    elif len(revenue_history) >= 3:
        rev_cagr_3yr = _safe_cagr(revenue_history)

    rev_display_3yr = f"{rev_cagr_3yr:.1f}%" if rev_cagr_3yr is not None else "N/A"
    rev_display_5yr = f"{rev_cagr_5yr:.1f}%" if rev_cagr_5yr is not None else "N/A"

    # Use best available historical revenue CAGR for gap
    hist_rev = rev_cagr_5yr if rev_cagr_5yr is not None else rev_cagr_3yr
    if hist_rev is not None:
        gap_rev = implied_growth - hist_rev
        print(f"  Revenue Growth:  Implied {implied_growth:+.1f}%  vs  Hist 3Y {rev_display_3yr} / 5Y {rev_display_5yr}  -->  Gap: {gap_rev:+.1f}pp")
    else:
        print(f"  Revenue Growth:  Implied {implied_growth:+.1f}%  vs  Historical: Insufficient data")

    # --- EBIT Margin ---
    valid_margins = [m for m in ebit_margin_history if m is not None]
    margin_3yr = None
    margin_5yr = None
    current_margin = None
    if valid_margins:
        current_margin = valid_margins[-1]
    if len(valid_margins) >= 3:
        margin_3yr = sum(valid_margins[-3:]) / 3.0
    if len(valid_margins) >= 4:
        margin_5yr = sum(valid_margins) / len(valid_margins)

    margin_current_str = f"{current_margin:.1f}%" if current_margin is not None else "N/A"
    margin_3yr_str = f"{margin_3yr:.1f}%" if margin_3yr is not None else "N/A"
    margin_5yr_str = f"{margin_5yr:.1f}%" if margin_5yr is not None else "N/A"

    if current_margin is not None:
        hist_margin = margin_5yr if margin_5yr is not None else margin_3yr
        if hist_margin is not None:
            print(f"  EBIT Margin:     Current {margin_current_str}  |  Avg 3Y {margin_3yr_str} / Avg 5Y {margin_5yr_str}")
        else:
            print(f"  EBIT Margin:     Current {margin_current_str}  |  Avg: Insufficient data")
    else:
        print(f"  EBIT Margin:     Insufficient data")

    # --- FCF Conversion (FCF / Revenue) ---
    valid_conv = [c for c in fcf_conversion_history if c is not None]
    conv_3yr = None
    conv_5yr = None
    current_conv = None
    if valid_conv:
        current_conv = valid_conv[-1]
    if len(valid_conv) >= 3:
        conv_3yr = sum(valid_conv[-3:]) / 3.0
    if len(valid_conv) >= 4:
        conv_5yr = sum(valid_conv) / len(valid_conv)

    conv_current_str = f"{current_conv:.1f}%" if current_conv is not None else "N/A"
    conv_3yr_str = f"{conv_3yr:.1f}%" if conv_3yr is not None else "N/A"
    conv_5yr_str = f"{conv_5yr:.1f}%" if conv_5yr is not None else "N/A"

    if current_conv is not None:
        print(f"  FCF/Revenue:     Current {conv_current_str}  |  Avg 3Y {conv_3yr_str} / Avg 5Y {conv_5yr_str}")
    else:
        print(f"  FCF/Revenue:     Insufficient data")

    # --- FCF Growth CAGR (3Y and 5Y separate) ---
    fcf_cagr_3yr = None
    fcf_cagr_5yr = None
    if len(fcf_history) >= 4:
        fcf_cagr_3yr = _safe_cagr(fcf_history[-4:])
    if len(fcf_history) >= 5:
        fcf_cagr_5yr = _safe_cagr(fcf_history)
    elif len(fcf_history) >= 3:
        fcf_cagr_3yr = _safe_cagr(fcf_history)

    fcf_3yr_str = f"{fcf_cagr_3yr:.1f}%" if fcf_cagr_3yr is not None else "N/A"
    fcf_5yr_str = f"{fcf_cagr_5yr:.1f}%" if fcf_cagr_5yr is not None else "N/A"

    hist_fcf = fcf_cagr_5yr if fcf_cagr_5yr is not None else fcf_cagr_3yr
    if hist_fcf is not None:
        gap_fcf = implied_growth - hist_fcf
        print(f"  FCF Growth:      Implied {implied_growth:+.1f}%  vs  Hist 3Y {fcf_3yr_str} / 5Y {fcf_5yr_str}  -->  Gap: {gap_fcf:+.1f}pp")
    else:
        print(f"  FCF Growth:      Implied {implied_growth:+.1f}%  vs  Historical: Insufficient positive FCF data")

    # --- EV/EBIT multiple ---
    ev_ebit = data.get("ev_ebit_current")
    if ev_ebit is not None:
        print(f"  Current EV/EBIT: {ev_ebit:.1f}x")

    return {
        "rev_cagr_3yr": rev_cagr_3yr,
        "rev_cagr_5yr": rev_cagr_5yr,
        "margin_current": current_margin,
        "margin_3yr": margin_3yr,
        "margin_5yr": margin_5yr,
        "conv_current": current_conv,
        "conv_3yr": conv_3yr,
        "conv_5yr": conv_5yr,
        "fcf_cagr_3yr": fcf_cagr_3yr,
        "fcf_cagr_5yr": fcf_cagr_5yr,
        "ev_ebit_current": ev_ebit,
    }


def _print_scenario_math(
    data: Dict,
    implied_growth: float,
    wacc: float,
    terminal_growth: float,
    projection_years: int,
    gap_data: Dict,
):
    """
    Print scenario math: what needs to happen for current price to be fair value.
    Shows growth-only, margin-only, multiple-only, and combination scenarios.
    """
    display_currency = data["display_currency"]
    price_display = data["price"]
    price_normalized = data["price_normalized"]
    revenue_history = data.get("revenue_history", [])
    ebit_margin_history = data.get("ebit_margin_history", [])
    fcf_conversion_history = data.get("fcf_conversion_history", [])

    # Historical reference values
    hist_rev_growth = gap_data.get("rev_cagr_5yr") or gap_data.get("rev_cagr_3yr")
    hist_margin = gap_data.get("margin_current")
    hist_conv = gap_data.get("conv_current")
    ev_ebit = gap_data.get("ev_ebit_current")

    print(f"\n{'- '*40}")
    print(f"SCENARIO MATH: What justifies {price_display:.2f} {display_currency}?")
    print(f"{'- '*40}")

    has_any = False

    # Scenario A: Growth-only (holding margin and conversion at current levels)
    if hist_margin is not None and hist_conv is not None and revenue_history:
        # FCF conversion from EBIT perspective: FCF/Revenue = margin * (FCF/EBIT)
        # We use margin as-is and back out FCF/EBIT from the data
        fcf_ebit_ratio = 1.0
        ebit_history = data.get("ebit_history", [])
        fcf_history = data.get("fcf_history", [])
        if ebit_history and fcf_history:
            min_len = min(len(ebit_history), len(fcf_history))
            if min_len > 0 and ebit_history[-1] and ebit_history[-1] > 0:
                fcf_ebit_ratio = fcf_history[-1] / ebit_history[-1]

        implied_rev_growth = _solve_reverse_revenue_growth(
            data, wacc, terminal_growth, projection_years,
            fixed_margin=hist_margin / 100.0,
            fixed_fcf_conversion=fcf_ebit_ratio,
        )
        if implied_rev_growth is not None:
            hist_str = f"{hist_rev_growth:.1f}%" if hist_rev_growth is not None else "N/A"
            print(f"  Scenario A (Growth only):     Revenue CAGR must be {implied_rev_growth:+.1f}% for {projection_years}yr (vs historical {hist_str})")
            print(f"                                Holding EBIT margin at {hist_margin:.1f}%, FCF/EBIT at {fcf_ebit_ratio*100:.0f}%")
            has_any = True

    # Scenario B: Margin expansion only (holding revenue growth at historical level)
    if hist_rev_growth is not None and revenue_history:
        fcf_ebit_ratio = 1.0
        ebit_history = data.get("ebit_history", [])
        fcf_history = data.get("fcf_history", [])
        if ebit_history and fcf_history:
            min_len = min(len(ebit_history), len(fcf_history))
            if min_len > 0 and ebit_history[-1] and ebit_history[-1] > 0:
                fcf_ebit_ratio = fcf_history[-1] / ebit_history[-1]

        implied_margin = _solve_reverse_margin(
            data, wacc, terminal_growth, projection_years,
            fixed_rev_growth=hist_rev_growth,
            fixed_fcf_conversion=fcf_ebit_ratio,
        )
        if implied_margin is not None:
            margin_str = f"{hist_margin:.1f}%" if hist_margin is not None else "N/A"
            print(f"  Scenario B (Margin expansion): EBIT margin must reach {implied_margin:.1f}% (vs current {margin_str})")
            print(f"                                Holding revenue growth at {hist_rev_growth:.1f}%, FCF/EBIT at {fcf_ebit_ratio*100:.0f}%")
            has_any = True

    # Scenario C: Multiple expansion (what terminal EV/FCF multiple is implied)
    # Use historical FCF growth as the growth rate during projection period
    hist_fcf_growth = gap_data.get("fcf_cagr_5yr") or gap_data.get("fcf_cagr_3yr")
    growth_for_multiple = hist_fcf_growth if hist_fcf_growth is not None else 0.0

    implied_multiple = _solve_reverse_terminal_multiple(
        data, wacc, projection_years, growth_rate=growth_for_multiple,
    )
    if implied_multiple is not None:
        # For comparison, compute what Gordon Growth terminal would imply
        gordon_multiple = None
        if wacc > terminal_growth:
            gordon_multiple = (1 + terminal_growth / 100) / ((wacc - terminal_growth) / 100)
        ev_ebit_str = f"{ev_ebit:.1f}x" if ev_ebit is not None else "N/A"
        gordon_str = f"{gordon_multiple:.1f}x" if gordon_multiple is not None else "N/A"
        print(f"  Scenario C (Multiple expansion): Terminal EV/FCF must be {implied_multiple:.1f}x (Gordon Growth implies {gordon_str})")
        print(f"                                  Using FCF growth {growth_for_multiple:.1f}% during projection | Current EV/EBIT: {ev_ebit_str}")
        has_any = True

    # Scenario D: Combination (what if all three improve moderately)
    if hist_rev_growth is not None and hist_margin is not None and revenue_history:
        # Assume: revenue growth improves by +2pp, margin improves by +2pp, see resulting FV
        combo_rev_growth = hist_rev_growth + 2.0
        combo_margin = (hist_margin + 2.0) / 100.0

        fcf_ebit_ratio = 1.0
        ebit_history = data.get("ebit_history", [])
        fcf_history = data.get("fcf_history", [])
        if ebit_history and fcf_history:
            min_len = min(len(ebit_history), len(fcf_history))
            if min_len > 0 and ebit_history[-1] and ebit_history[-1] > 0:
                fcf_ebit_ratio = fcf_history[-1] / ebit_history[-1]

        base_revenue = revenue_history[-1]
        shares = data["shares"]
        net_debt = data.get("net_debt", 0)

        projected_fcf = []
        pv_fcf = []
        for year in range(1, projection_years + 1):
            rev = base_revenue * ((1 + combo_rev_growth / 100) ** year)
            ebit = rev * combo_margin
            fcf = ebit * fcf_ebit_ratio
            pv = fcf / ((1 + wacc / 100) ** year)
            projected_fcf.append(fcf)
            pv_fcf.append(pv)

        if projected_fcf:
            terminal_fcf = projected_fcf[-1] * (1 + terminal_growth / 100)
            tv = terminal_fcf / ((wacc - terminal_growth) / 100)
            pv_tv = tv / ((1 + wacc / 100) ** projection_years)
            ev = sum(pv_fcf) + pv_tv
            equity = max(ev - net_debt, 0)
            fv = equity / shares if shares > 0 else 0
            fv_display, _ = format_price_and_currency(fv, data)
            mos = calculate_mos(fv, price_normalized)
            print(f"  Scenario D (Combination):     Growth {combo_rev_growth:.1f}% + Margin {combo_margin*100:.1f}% --> FV {fv_display:.2f} {display_currency} (MoS: {mos:+.1f}%)")
            has_any = True

    if not has_any:
        print(f"  Insufficient historical data for scenario decomposition")


def _print_asymmetry_analysis(
    data: Dict,
    implied_growth: float,
    wacc: float,
    terminal_growth: float,
    projection_years: int,
    gap_data: Dict,
):
    """
    Print asymmetry analysis: bull vs bear fair values and upside/downside ratio.
    Uses historical ranges to define optimistic (P10) and pessimistic (P90) scenarios.
    """
    display_currency = data["display_currency"]
    price_normalized = data["price_normalized"]
    fcf_history = data["fcf_history"]
    shares = data["shares"]
    net_debt = data.get("net_debt", 0)

    # Derive bull and bear growth rates from historical data
    hist_fcf_cagr = gap_data.get("fcf_cagr_5yr") or gap_data.get("fcf_cagr_3yr")
    hist_rev_cagr = gap_data.get("rev_cagr_5yr") or gap_data.get("rev_cagr_3yr")

    # Best available historical growth reference
    hist_growth = hist_fcf_cagr if hist_fcf_cagr is not None else hist_rev_cagr

    if hist_growth is None:
        # Fallback: use implied growth as reference
        hist_growth = implied_growth

    # P10 Bull: optimistic = max(implied, historical) + 3pp growth, WACC -1pp
    bull_growth = max(implied_growth, hist_growth) + 3.0
    bull_wacc = max(wacc - 1.0, terminal_growth + 0.5)  # ensure WACC > terminal

    # P90 Bear: pessimistic = min(implied, historical) - 3pp growth, WACC +1.5pp
    bear_growth = min(implied_growth, hist_growth) - 3.0
    bear_wacc = wacc + 1.5

    # Calculate bull case FV
    bull_dcf = calculate_dcf(
        fcf_history, shares,
        growth_rate=bull_growth,
        terminal_growth=terminal_growth,
        wacc=bull_wacc,
        projection_years=projection_years,
        net_debt=net_debt,
    )
    bull_fv = bull_dcf["fair_value_per_share"]
    bull_fv_display, _ = format_price_and_currency(bull_fv, data)
    bull_return = calculate_mos(bull_fv, price_normalized)

    # Calculate bear case FV
    bear_dcf = calculate_dcf(
        fcf_history, shares,
        growth_rate=bear_growth,
        terminal_growth=terminal_growth,
        wacc=bear_wacc,
        projection_years=projection_years,
        net_debt=net_debt,
    )
    bear_fv = bear_dcf["fair_value_per_share"]
    bear_fv_display, _ = format_price_and_currency(bear_fv, data)
    bear_return = calculate_mos(bear_fv, price_normalized)

    # Asymmetry ratio = |upside| / |downside|
    upside = max(bull_return, 0)
    downside = abs(min(bear_return, 0))
    if downside > 0:
        asymmetry = upside / downside
    elif upside > 0:
        asymmetry = float('inf')
    else:
        asymmetry = 0.0

    print(f"\n{'- '*40}")
    print(f"ASYMMETRY ANALYSIS")
    print(f"{'- '*40}")
    print(f"  Bull case (P10 optimistic):  Growth {bull_growth:+.1f}%, WACC {bull_wacc:.1f}%")
    print(f"    Fair Value: {bull_fv_display:.2f} {display_currency}  -->  Return: {bull_return:+.1f}%")
    print(f"  Bear case (P90 pessimistic): Growth {bear_growth:+.1f}%, WACC {bear_wacc:.1f}%")
    print(f"    Fair Value: {bear_fv_display:.2f} {display_currency}  -->  Return: {bear_return:+.1f}%")

    if asymmetry == float('inf'):
        print(f"  Asymmetry ratio: INF (no downside in bear case)")
    elif asymmetry == 0.0 and upside == 0:
        print(f"  Asymmetry ratio: 0.00 (no upside in bull case)")
    else:
        print(f"  Asymmetry ratio: {asymmetry:.2f}x (>1 = favorable, <1 = unfavorable)")

    # Probability-weighted expected return (equal weight)
    expected_return = (bull_return + bear_return) / 2.0
    print(f"  Equal-weight expected return: {expected_return:+.1f}%")

    return {
        "bull_fv": bull_fv,
        "bear_fv": bear_fv,
        "bull_return": bull_return,
        "bear_return": bear_return,
        "asymmetry": asymmetry,
    }


def print_reverse_dcf(
    ticker: str,
    data: Dict,
    implied_growth: float,
    wacc: float,
    terminal_growth: float,
    projection_years: int,
    rates: Dict[str, float],
) -> Dict:
    """
    Print reverse DCF output for a single ticker.
    Includes: implied expectations, historical context, basic gap/scenario,
    then enhanced gap analysis, scenario math, and asymmetry analysis.

    Returns a result dict for the summary table.
    """
    price_display = data["price"]
    display_currency = data["display_currency"]
    price_normalized = data["price_normalized"]
    currency = data["currency"]
    fcf_history = data["fcf_history"]
    shares = data["shares"]
    net_debt = data.get("net_debt", 0)
    market_cap = data.get("market_cap", 0)

    # Enterprise Value (for display)
    ev = market_cap + net_debt
    # For GBp stocks, market_cap from yfinance is already in native currency (GBP)
    # but price is in pence, so market_cap = price_normalized * shares
    if data["is_gbp_pence"] and market_cap == 0:
        market_cap = price_normalized * shares
        ev = market_cap + net_debt

    # Most recent FCF and average 3yr FCF
    base_fcf = fcf_history[-1]
    avg_fcf_3yr = sum(fcf_history[-3:]) / min(3, len(fcf_history)) if fcf_history else base_fcf

    # Historical FCF CAGR
    fcf_cagr = None
    if len(fcf_history) >= 2:
        first_fcf = fcf_history[0]
        last_fcf = fcf_history[-1]
        n_years = len(fcf_history) - 1
        if first_fcf > 0 and last_fcf > 0:
            fcf_cagr = ((last_fcf / first_fcf) ** (1 / n_years) - 1) * 100

    # Revenue growth
    revenue_growth = data.get("revenue_growth_3yr")

    print(f"\n{'='*80}")
    print(f"REVERSE DCF: {ticker}")
    print(f"{data['name']}")
    print(f"Price: {price_display:.2f} {display_currency} | Market Cap: {market_cap/1e9:.1f}B | EV: {ev/1e9:.1f}B")
    print(f"FCF (most recent): {base_fcf/1e9:.2f}B | FCF (avg {min(3, len(fcf_history))}yr): {avg_fcf_3yr/1e9:.2f}B")
    print(f"WACC: {wacc:.1f}% | Terminal growth: {terminal_growth:.1f}% | Projection: {projection_years} years")
    print(f"{'='*80}")

    if data.get("fcf_warning"):
        print(f"\n!!  {data['fcf_warning']}")

    # IMPLIED EXPECTATIONS
    print(f"\nIMPLIED EXPECTATIONS:")
    if implied_growth <= -20.0:
        print(f"  FCF growth rate implied by current price: <-20.0% /yr ({projection_years}yr projection)")
    elif implied_growth >= 50.0:
        print(f"  FCF growth rate implied by current price: >50.0% /yr ({projection_years}yr projection)")
    else:
        print(f"  FCF growth rate implied by current price: {implied_growth:.1f}% /yr ({projection_years}yr projection)")

    # HISTORICAL CONTEXT
    print(f"\nHISTORICAL CONTEXT:")
    if fcf_cagr is not None:
        print(f"  FCF CAGR (from {len(fcf_history)}yr history): {fcf_cagr:.1f}% /yr")
    else:
        print(f"  FCF CAGR: N/A (insufficient positive FCF history)")
    if revenue_growth is not None:
        n_rev = len(data.get("revenue_history", [])) - 1
        print(f"  Revenue growth ({n_rev}yr avg): {revenue_growth:.1f}% /yr")
    else:
        print(f"  Revenue growth: N/A")

    # GAP ANALYSIS (original basic version)
    print(f"\nGAP ANALYSIS:")
    if fcf_cagr is not None:
        gap = fcf_cagr - implied_growth
        print(f"  Implied: {implied_growth:.1f}% | Historical FCF CAGR: {fcf_cagr:.1f}%")
        print(f"  Gap: {gap:.1f} pp")
    else:
        print(f"  Implied: {implied_growth:.1f}% | Historical FCF CAGR: N/A")

    # SCENARIO MATH (original basic version)
    print(f"\nSCENARIO MATH (if company grows at...):")

    scenarios_to_show = []

    if fcf_cagr is not None and fcf_cagr > implied_growth:
        midpoint = (fcf_cagr + implied_growth) / 2
        scenarios_to_show.append(("Historical rate", fcf_cagr))
        scenarios_to_show.append(("Midpoint", midpoint))
    elif fcf_cagr is not None:
        # Historical is lower than implied
        scenarios_to_show.append(("Historical rate", fcf_cagr))

    scenarios_to_show.append(("Implied rate", implied_growth))

    for label, g_rate in scenarios_to_show:
        dcf = calculate_dcf(
            fcf_history, shares,
            growth_rate=g_rate,
            terminal_growth=terminal_growth,
            wacc=wacc,
            projection_years=projection_years,
            net_debt=net_debt,
        )
        fv = dcf["fair_value_per_share"]
        fv_display, _ = format_price_and_currency(fv, data)
        mos = calculate_mos(fv, price_normalized)
        print(f"  {label} ({g_rate:.1f}%): Fair Value {fv_display:.2f} {display_currency} (MoS: {mos:+.1f}%)")

    # =========================================================================
    # ENHANCED REVERSE DCF SECTIONS (new)
    # =========================================================================

    # 1. Enhanced Gap Analysis
    gap_data = _print_enhanced_gap_analysis(data, implied_growth)

    # 2. Scenario Math (decomposed)
    _print_scenario_math(
        data, implied_growth, wacc, terminal_growth, projection_years, gap_data,
    )

    # 3. Asymmetry Analysis
    asym_data = _print_asymmetry_analysis(
        data, implied_growth, wacc, terminal_growth, projection_years, gap_data,
    )

    print(f"\n[Raw data. Reason from principles.md]")

    # Build result dict for summary table
    return {
        "ticker": ticker,
        "name": data["name"],
        "price_display": price_display,
        "display_currency": display_currency,
        "implied_growth": implied_growth,
        "fcf_cagr": fcf_cagr,
        "revenue_growth": revenue_growth,
        "gap": (fcf_cagr - implied_growth) if fcf_cagr is not None else None,
        "asymmetry": asym_data.get("asymmetry") if asym_data else None,
        "bull_return": asym_data.get("bull_return") if asym_data else None,
        "bear_return": asym_data.get("bear_return") if asym_data else None,
    }


def print_reverse_summary_table(results: List[Dict]):
    """Print summary table for batch reverse DCF analysis."""
    if not results or len(results) < 2:
        return

    print(f"\n{'='*110}")
    print(f"REVERSE DCF SUMMARY")
    print(f"{'='*110}")

    header = (
        f"{'Ticker':<10} {'Name':<22} {'Price':>10} "
        f"{'Implied':>9} {'FCF CAGR':>10} {'Rev Gr':>8} {'Gap':>8} {'Asym':>7} {'Bull':>8} {'Bear':>8}"
    )
    print(f"\n{header}")
    print("-" * 110)

    for r in sorted(results, key=lambda x: x.get("gap") or 0, reverse=True):
        implied_str = f"{r['implied_growth']:+.1f}%" if r['implied_growth'] is not None else "N/A"
        cagr_str = f"{r['fcf_cagr']:.1f}%" if r['fcf_cagr'] is not None else "N/A"
        rev_str = f"{r['revenue_growth']:.1f}%" if r['revenue_growth'] is not None else "N/A"
        gap_str = f"{r['gap']:+.1f}pp" if r['gap'] is not None else "N/A"
        asym_str = f"{r['asymmetry']:.2f}x" if r.get('asymmetry') is not None and r['asymmetry'] != float('inf') else "N/A"
        bull_str = f"{r['bull_return']:+.1f}%" if r.get('bull_return') is not None else "N/A"
        bear_str = f"{r['bear_return']:+.1f}%" if r.get('bear_return') is not None else "N/A"
        print(
            f"{r['ticker']:<10} {r['name'][:22]:<22} "
            f"{r['price_display']:>10.2f} "
            f"{implied_str:>9} {cagr_str:>10} {rev_str:>8} {gap_str:>8} {asym_str:>7} {bull_str:>8} {bear_str:>8}"
        )

    print(f"\nImplied = growth rate market prices in | Gap = Historical CAGR - Implied")
    print(f"Positive gap = market implies LESS growth than historical | Asym >1 = favorable risk/reward")
    print(f"\n[Raw data. Reason from principles.md]")


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
    currency: str, price_eur: float, wacc: float,
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
        print(f"{i:>6} {fcf/1e9:>12.2f} {1/((1+wacc/100)**i):>9.3f}x {pv/1e9:>12.2f}")

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
  python3 tools/dcf_calculator.py --reverse ROP ADBE NVO  # Reverse DCF
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
        "--reverse", action="store_true",
        help="Reverse DCF: solve for implied FCF growth rate given current price",
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

    args = parser.parse_args()

    # --reverse is mutually exclusive with --growth (user-specified)
    if args.reverse and '--growth' in sys.argv:
        print("ERROR: --reverse and --growth are mutually exclusive. "
              "--reverse solves for the growth rate.", file=sys.stderr)
        sys.exit(1)

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

    # ======================================================================
    # REVERSE DCF MODE
    # ======================================================================
    if args.reverse:
        reverse_results = []
        for ticker in args.tickers:
            print(f"\n{'#'*80}", file=sys.stderr)
            print(f"Processing (reverse): {ticker}", file=sys.stderr)
            print(f"{'#'*80}", file=sys.stderr)

            data = fetch_historical_fcf(ticker, years=5)
            if not data:
                continue

            implied_growth = calculate_reverse_dcf(
                data,
                wacc=args.wacc,
                terminal_growth=args.terminal,
                projection_years=args.years,
            )

            if implied_growth is None:
                print(f"ERROR {ticker}: Could not solve for implied growth rate", file=sys.stderr)
                continue

            result = print_reverse_dcf(
                ticker, data, implied_growth,
                wacc=args.wacc,
                terminal_growth=args.terminal,
                projection_years=args.years,
                rates=rates,
            )
            reverse_results.append(result)

        if len(reverse_results) > 1:
            print_reverse_summary_table(reverse_results)

        print()
        return

    # ======================================================================
    # STANDARD DCF MODE (existing behavior)
    # ======================================================================
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
            print_dcf_waterfall(ticker, data, dcf, price_normalized, currency, price_eur, wacc=args.wacc)

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
