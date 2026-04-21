#!/usr/bin/env python3
"""
Narrative Checker - Financial data trends that show whether market narratives
are supported by actual financial data. Raw data only, no judgments.

Usage:
  python3 tools/narrative_checker.py ADBE
  python3 tools/narrative_checker.py ADBE LULU NVO
"""

import sys
import argparse
import yfinance as yf
import warnings
warnings.filterwarnings('ignore')


# Currency symbol mapping
CURRENCY_SYMBOLS = {
    'USD': '$', 'EUR': 'EUR ', 'GBP': 'GBP ', 'GBp': 'GBp ',
    'GBX': 'GBp ', 'DKK': 'DKK ', 'NOK': 'NOK ', 'SEK': 'SEK ',
    'CHF': 'CHF ', 'JPY': 'JPY ',
}


# ==============================================================================
# Helpers
# ==============================================================================

def safe_get_row(df, names):
    """Try multiple row names, return the first match or None."""
    if df is None or df.empty:
        return None
    for name in names:
        if name in df.index:
            return df.loc[name]
    return None


def fmt_num(val, fmt_type='dollar', decimals=1, curr_sym='$'):
    """Format a number for display."""
    if val is None or (isinstance(val, float) and (val != val)):  # NaN check
        return 'N/A'
    try:
        val = float(val)
    except (ValueError, TypeError):
        return 'N/A'

    if fmt_type == 'dollar':
        abs_val = abs(val)
        sign = '-' if val < 0 else ''
        if abs_val >= 1e9:
            return f"{curr_sym}{sign}{abs_val / 1e9:.{decimals}f}B"
        elif abs_val >= 1e6:
            return f"{curr_sym}{sign}{abs_val / 1e6:.{decimals}f}M"
        else:
            return f"{curr_sym}{sign}{abs_val:.0f}"
    elif fmt_type == 'pct':
        return f"{val:.{decimals}f}%"
    elif fmt_type == 'ratio':
        return f"{val:.{decimals}f}x"
    return str(val)


def pct(numerator, denominator):
    """Calculate percentage, return None if impossible."""
    if numerator is None or denominator is None:
        return None
    try:
        n = float(numerator)
        d = float(denominator)
        if d == 0:
            return None
        return (n / d) * 100.0
    except (ValueError, TypeError):
        return None


def growth_rate(new, old):
    """Calculate growth rate as percentage, return None if impossible."""
    if new is None or old is None:
        return None
    try:
        n = float(new)
        o = float(old)
        if o == 0:
            return None
        return ((n - o) / abs(o)) * 100.0
    except (ValueError, TypeError):
        return None


def safe_float(val):
    """Convert to float, return None if impossible."""
    if val is None:
        return None
    try:
        f = float(val)
        if f != f:  # NaN
            return None
        return f
    except (ValueError, TypeError):
        return None


def get_periods(df, max_periods=4):
    """Get column dates sorted oldest to newest, up to max_periods."""
    if df is None or df.empty:
        return []
    cols = sorted(df.columns, reverse=False)  # oldest first
    return cols[-max_periods:]  # take last N (most recent)


def year_label(dt):
    """Extract year label from a datetime column."""
    try:
        return str(dt.year)
    except AttributeError:
        return str(dt)[:4]


# ==============================================================================
# Data extraction
# ==============================================================================

def extract_data(ticker_str):
    """Fetch all financial data for a ticker."""
    t = yf.Ticker(ticker_str)
    info = t.info

    if not info or 'symbol' not in info:
        return None

    data = {
        'ticker': ticker_str.upper(),
        'name': info.get('shortName', ticker_str),
        'currency': info.get('currency', 'USD'),
    }

    # Fetch statements (may be empty DataFrames)
    try:
        data['financials'] = t.financials
    except Exception:
        data['financials'] = None

    try:
        data['balance_sheet'] = t.balance_sheet
    except Exception:
        data['balance_sheet'] = None

    try:
        data['cashflow'] = t.cashflow
    except Exception:
        data['cashflow'] = None

    return data


# ==============================================================================
# Trend builders
# ==============================================================================

def build_revenue_margins(financials, periods):
    """Build revenue and margin trends."""
    revenue_row = safe_get_row(financials, ['Total Revenue', 'Revenue'])
    gp_row = safe_get_row(financials, ['Gross Profit'])
    oi_row = safe_get_row(financials, ['Operating Income', 'EBIT'])
    ni_row = safe_get_row(financials, ['Net Income', 'Net Income From Continuing Operations'])

    results = {'revenue': [], 'rev_growth': [], 'gross_margin': [], 'op_margin': [], 'net_margin': []}

    prev_rev = None
    for p in periods:
        rev = safe_float(revenue_row[p]) if revenue_row is not None and p in revenue_row.index else None
        gp = safe_float(gp_row[p]) if gp_row is not None and p in gp_row.index else None
        oi = safe_float(oi_row[p]) if oi_row is not None and p in oi_row.index else None
        ni = safe_float(ni_row[p]) if ni_row is not None and p in ni_row.index else None

        results['revenue'].append((year_label(p), rev))
        results['rev_growth'].append((year_label(p), growth_rate(rev, prev_rev)))
        results['gross_margin'].append((year_label(p), pct(gp, rev)))
        results['op_margin'].append((year_label(p), pct(oi, rev)))
        results['net_margin'].append((year_label(p), pct(ni, rev)))

        prev_rev = rev

    return results


def build_quality_indicators(financials, cashflow, periods):
    """Build R&D/Revenue, SBC/Revenue, Capex/Depreciation trends."""
    revenue_row = safe_get_row(financials, ['Total Revenue', 'Revenue'])
    rd_row = safe_get_row(financials, ['Research Development', 'Research And Development'])
    sbc_row = safe_get_row(cashflow, ['Stock Based Compensation'])
    capex_row = safe_get_row(cashflow, ['Capital Expenditures', 'Capital Expenditure'])
    dep_row = safe_get_row(cashflow, ['Depreciation', 'Depreciation And Amortization',
                                       'Depreciation Amortization Depletion'])

    results = {'rd_rev': [], 'sbc_rev': [], 'capex_dep': []}

    for p in periods:
        rev = safe_float(revenue_row[p]) if revenue_row is not None and p in revenue_row.index else None
        rd = safe_float(rd_row[p]) if rd_row is not None and p in rd_row.index else None
        sbc = safe_float(sbc_row[p]) if sbc_row is not None and p in sbc_row.index else None
        capex = safe_float(capex_row[p]) if capex_row is not None and p in capex_row.index else None
        dep = safe_float(dep_row[p]) if dep_row is not None and p in dep_row.index else None

        results['rd_rev'].append((year_label(p), pct(rd, rev)))
        results['sbc_rev'].append((year_label(p), pct(sbc, rev)))

        # Capex is often negative in yfinance; take abs
        capex_abs = abs(capex) if capex is not None else None
        dep_abs = abs(dep) if dep is not None else None
        if capex_abs is not None and dep_abs is not None and dep_abs != 0:
            results['capex_dep'].append((year_label(p), capex_abs / dep_abs))
        else:
            results['capex_dep'].append((year_label(p), None))

    return results


def build_balance_sheet_signals(financials, balance_sheet, periods):
    """Build receivables/inventory vs revenue growth, goodwill/assets."""
    revenue_row = safe_get_row(financials, ['Total Revenue', 'Revenue'])
    recv_row = safe_get_row(balance_sheet, ['Net Receivables', 'Accounts Receivable',
                                             'Receivables'])
    inv_row = safe_get_row(balance_sheet, ['Inventory'])
    gw_row = safe_get_row(balance_sheet, ['Goodwill'])
    ta_row = safe_get_row(balance_sheet, ['Total Assets'])

    results = {
        'recv_growth': None,
        'rev_growth_for_bs': None,
        'inv_growth': None,
        'rev_growth_for_inv': None,
        'has_inventory': False,
        'goodwill_assets': [],
    }

    # Use most recent two periods for growth comparison
    if len(periods) >= 2:
        p_old, p_new = periods[-2], periods[-1]

        rev_old = safe_float(revenue_row[p_old]) if revenue_row is not None and p_old in revenue_row.index else None
        rev_new = safe_float(revenue_row[p_new]) if revenue_row is not None and p_new in revenue_row.index else None
        results['rev_growth_for_bs'] = growth_rate(rev_new, rev_old)
        results['rev_growth_for_inv'] = results['rev_growth_for_bs']

        recv_old = safe_float(recv_row[p_old]) if recv_row is not None and p_old in recv_row.index else None
        recv_new = safe_float(recv_row[p_new]) if recv_row is not None and p_new in recv_row.index else None
        results['recv_growth'] = growth_rate(recv_new, recv_old)

        inv_old = safe_float(inv_row[p_old]) if inv_row is not None and p_old in inv_row.index else None
        inv_new = safe_float(inv_row[p_new]) if inv_row is not None and p_new in inv_row.index else None
        if inv_old is not None and inv_new is not None:
            results['has_inventory'] = True
            results['inv_growth'] = growth_rate(inv_new, inv_old)

    # Goodwill / Total Assets trend
    for p in periods:
        gw = safe_float(gw_row[p]) if gw_row is not None and p in gw_row.index else None
        ta = safe_float(ta_row[p]) if ta_row is not None and p in ta_row.index else None
        results['goodwill_assets'].append((year_label(p), pct(gw, ta)))

    return results


def build_cashflow(financials, cashflow, periods):
    """Build FCF, FCF margin, OCF/NI trends."""
    revenue_row = safe_get_row(financials, ['Total Revenue', 'Revenue'])
    fcf_row = safe_get_row(cashflow, ['Free Cash Flow'])
    ocf_row = safe_get_row(cashflow, ['Total Cash From Operating Activities',
                                       'Operating Cash Flow',
                                       'Cash Flow From Continuing Operating Activities'])
    ni_row = safe_get_row(financials, ['Net Income', 'Net Income From Continuing Operations'])

    results = {'fcf': [], 'fcf_margin': [], 'ocf_ni': []}

    for p in periods:
        rev = safe_float(revenue_row[p]) if revenue_row is not None and p in revenue_row.index else None
        fcf = safe_float(fcf_row[p]) if fcf_row is not None and p in fcf_row.index else None
        ocf = safe_float(ocf_row[p]) if ocf_row is not None and p in ocf_row.index else None
        ni = safe_float(ni_row[p]) if ni_row is not None and p in ni_row.index else None

        results['fcf'].append((year_label(p), fcf))
        results['fcf_margin'].append((year_label(p), pct(fcf, rev)))

        if ocf is not None and ni is not None and ni != 0:
            results['ocf_ni'].append((year_label(p), ocf / ni))
        else:
            results['ocf_ni'].append((year_label(p), None))

    return results


def build_deferred_revenue(balance_sheet, periods):
    """Build deferred revenue trend if available."""
    dr_row = safe_get_row(balance_sheet, ['Deferred Revenue', 'Current Deferred Revenue'])

    if dr_row is None:
        return None

    results = {'values': [], 'growth': []}
    prev_val = None
    has_data = False

    for p in periods:
        val = safe_float(dr_row[p]) if p in dr_row.index else None
        if val is not None:
            has_data = True
        results['values'].append((year_label(p), val))
        results['growth'].append((year_label(p), growth_rate(val, prev_val)))
        prev_val = val

    return results if has_data else None


# ==============================================================================
# Output formatting
# ==============================================================================

def format_trend_line(label, data, fmt_type='dollar', decimals=1, indent=2, curr_sym='$'):
    """Format a trend line like: Revenue:  2022: $XX.XB -> 2023: $XX.XB -> 2024: $XX.XB"""
    prefix = ' ' * indent
    parts = []
    for year, val in data:
        parts.append(f"{year}: {fmt_num(val, fmt_type, decimals, curr_sym)}")
    line = ' -> '.join(parts) if parts else 'N/A'
    return f"{prefix}{label:<26s}{line}"


def has_any_data(data_list):
    """Check if any entry in a list of (year, value) tuples has non-None value."""
    return any(v is not None for _, v in data_list)


def print_report(data):
    """Print the full narrative checker report for one ticker."""
    financials = data['financials']
    balance_sheet = data['balance_sheet']
    cashflow = data['cashflow']
    currency = data['currency']

    # Determine currency symbol for display
    curr_sym = CURRENCY_SYMBOLS.get(currency, currency + ' ' if currency else '$')

    # Get common periods (use financials as the base)
    periods = get_periods(financials)
    bs_periods = get_periods(balance_sheet)
    cf_periods = get_periods(cashflow)

    if not periods:
        print(f"  No annual financial data available for {data['ticker']}")
        return

    print("=" * 80)
    print(f"FINANCIAL DATA TRENDS: {data['ticker']} ({data['name']})")
    print(f"Currency: {currency}")
    print("=" * 80)

    # --- REVENUE & MARGINS ---
    rm = build_revenue_margins(financials, periods)

    print()
    print("REVENUE & MARGINS (annual):")
    if has_any_data(rm['revenue']):
        print(format_trend_line('Revenue:', rm['revenue'], 'dollar', curr_sym=curr_sym))
    if has_any_data(rm['rev_growth'][1:]):  # skip first which is always None
        print(format_trend_line('Rev Growth:', rm['rev_growth'][1:], 'pct'))
    if has_any_data(rm['gross_margin']):
        print(format_trend_line('Gross Margin:', rm['gross_margin'], 'pct'))
    if has_any_data(rm['op_margin']):
        print(format_trend_line('Op Margin:', rm['op_margin'], 'pct'))

    # --- QUALITY INDICATORS ---
    qi = build_quality_indicators(financials, cashflow, periods)

    has_qi = (has_any_data(qi['rd_rev']) or has_any_data(qi['sbc_rev']) or has_any_data(qi['capex_dep']))
    if has_qi:
        print()
        print("QUALITY INDICATORS:")
        if has_any_data(qi['rd_rev']):
            print(format_trend_line('R&D / Revenue:', qi['rd_rev'], 'pct'))
        if has_any_data(qi['sbc_rev']):
            print(format_trend_line('SBC / Revenue:', qi['sbc_rev'], 'pct'))
        if has_any_data(qi['capex_dep']):
            print(format_trend_line('Capex / Depreciation:', qi['capex_dep'], 'ratio'))

    # --- BALANCE SHEET SIGNALS ---
    bs = build_balance_sheet_signals(financials, balance_sheet, bs_periods)

    has_bs = (bs['recv_growth'] is not None or bs['has_inventory'] or has_any_data(bs['goodwill_assets']))
    if has_bs:
        print()
        print("BALANCE SHEET SIGNALS:")
        if bs['recv_growth'] is not None:
            print(f"  Receivables vs Revenue growth:")
            print(f"    Receivables growth: {fmt_num(bs['recv_growth'], 'pct')} | Revenue growth: {fmt_num(bs['rev_growth_for_bs'], 'pct')}")
        if bs['has_inventory']:
            print(f"  Inventory vs Revenue growth:")
            print(f"    Inventory growth: {fmt_num(bs['inv_growth'], 'pct')} | Revenue growth: {fmt_num(bs['rev_growth_for_inv'], 'pct')}")
        if has_any_data(bs['goodwill_assets']):
            print(format_trend_line('Goodwill / Total Assets:', bs['goodwill_assets'], 'pct'))

    # --- CASH FLOW ---
    cf = build_cashflow(financials, cashflow, cf_periods)

    has_cf = (has_any_data(cf['fcf']) or has_any_data(cf['fcf_margin']) or has_any_data(cf['ocf_ni']))
    if has_cf:
        print()
        print("CASH FLOW:")
        if has_any_data(cf['fcf']):
            print(format_trend_line('FCF:', cf['fcf'], 'dollar', curr_sym=curr_sym))
        if has_any_data(cf['fcf_margin']):
            print(format_trend_line('FCF Margin:', cf['fcf_margin'], 'pct'))
        if has_any_data(cf['ocf_ni']):
            print(format_trend_line('OCF / Net Income:', cf['ocf_ni'], 'ratio'))

    # --- DEFERRED REVENUE ---
    dr = build_deferred_revenue(balance_sheet, bs_periods)
    if dr is not None:
        print()
        print("DEFERRED REVENUE:")
        if has_any_data(dr['values']):
            print(format_trend_line('Deferred Revenue:', dr['values'], 'dollar', curr_sym=curr_sym))
        if has_any_data(dr['growth'][1:]):
            print(format_trend_line('Growth:', dr['growth'][1:], 'pct'))

    print()
    print("[Raw data. Reason from principles.md]")
    print()


# ==============================================================================
# Main
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Narrative Checker - Financial data trends. Raw data, no judgments.'
    )
    parser.add_argument('tickers', nargs='+', help='One or more ticker symbols')
    args = parser.parse_args()

    for i, ticker_str in enumerate(args.tickers):
        if i > 0:
            print()  # separator between tickers

        try:
            data = extract_data(ticker_str)
            if data is None:
                print(f"ERROR: No data available for {ticker_str.upper()}")
                continue
            print_report(data)
        except Exception as e:
            print(f"ERROR processing {ticker_str.upper()}: {e}")


if __name__ == '__main__':
    main()
