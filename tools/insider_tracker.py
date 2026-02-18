#!/usr/bin/env python3
"""
Insider Tracker - Insider transactions, institutional holders, short interest, analyst consensus.
Raw data only. No judgments, no labels, no interpretations.
Uses yfinance as the sole data source.

Usage:
  python3 tools/insider_tracker.py ADBE
  python3 tools/insider_tracker.py ADBE NVO MONY.L
  python3 tools/insider_tracker.py ADBE --sections insider,short
  python3 tools/insider_tracker.py ADBE --compact
"""

import sys
import argparse
import yfinance as yf
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# ==============================================================================
# Data Extraction
# ==============================================================================

def safe_get_attr(ticker_obj, attr_name):
    """Safely get a yfinance Ticker attribute. Returns None on any failure."""
    try:
        val = getattr(ticker_obj, attr_name, None)
        if val is None:
            return None
        if isinstance(val, pd.DataFrame) and val.empty:
            return None
        return val
    except Exception:
        return None


def safe_info_get(info, key, default="N/A"):
    """Safely get a key from ticker.info dict."""
    val = info.get(key)
    if val is None:
        return default
    return val


def format_number(n, decimals=1):
    """Format large numbers with M/B suffixes."""
    if n == "N/A" or n is None:
        return "N/A"
    try:
        n = float(n)
    except (ValueError, TypeError):
        return str(n)
    if abs(n) >= 1e9:
        return f"{n / 1e9:.{decimals}f}B"
    if abs(n) >= 1e6:
        return f"{n / 1e6:.{decimals}f}M"
    if abs(n) >= 1e3:
        return f"{n / 1e3:.{decimals}f}K"
    return f"{n:.0f}"


def format_pct(val):
    """Format a decimal or percentage value as X.X%."""
    if val == "N/A" or val is None:
        return "N/A"
    try:
        val = float(val)
    except (ValueError, TypeError):
        return str(val)
    # yfinance sometimes returns as decimal (0.05), sometimes as percent (5.0)
    if abs(val) < 1:
        return f"{val * 100:.1f}%"
    return f"{val:.1f}%"


def format_currency(val, currency="USD"):
    """Format a price with currency symbol."""
    if val == "N/A" or val is None:
        return "N/A"
    try:
        val = float(val)
    except (ValueError, TypeError):
        return str(val)
    symbols = {'USD': '$', 'EUR': 'EUR ', 'GBP': 'GBP ', 'GBp': '', 'GBX': '',
               'DKK': 'DKK ', 'SEK': 'SEK ', 'NOK': 'NOK ', 'CHF': 'CHF '}
    sym = symbols.get(currency, f"{currency} ")
    if currency in ('GBp', 'GBX'):
        return f"{val:.0f}p"
    return f"{sym}{val:,.2f}"


def _get_col(df, candidates):
    """Find the first matching column name from candidates list."""
    for c in candidates:
        if c in df.columns:
            return c
    return None


def _row_val(row, col, default="N/A"):
    """Safely get a value from a DataFrame row."""
    if col is None:
        return default
    val = row.get(col, default)
    if val is None or (isinstance(val, float) and val != val):  # NaN check
        return default
    return val


# ==============================================================================
# Section Renderers
# ==============================================================================

def render_insider_activity(ticker_obj, info):
    """Render insider transactions and holdings section."""
    lines = []
    lines.append("INSIDER ACTIVITY:")

    # Insider transactions
    txns = safe_get_attr(ticker_obj, 'insider_transactions')
    if txns is not None and isinstance(txns, pd.DataFrame) and len(txns) > 0:
        lines.append("  Recent transactions:")

        # Discover columns
        date_col = _get_col(txns, ['Start Date', 'startDate', 'Date'])
        name_col = _get_col(txns, ['Insider', 'insider', 'Name'])
        pos_col = _get_col(txns, ['Position', 'position', 'Title', 'Relation'])
        text_col = _get_col(txns, ['Text', 'Description'])
        shares_col = _get_col(txns, ['Shares', 'shares'])
        value_col = _get_col(txns, ['Value', 'value'])
        ownership_col = _get_col(txns, ['Ownership', 'ownership'])

        # Header
        lines.append(f"    {'Date':<12} {'Insider':<22} {'Title':<22} {'Description':<35} {'Shares':>10} {'Value':>12}")
        lines.append(f"    {'-' * 115}")

        # Show up to 10 most recent
        show = txns.head(10)
        for _, row in show.iterrows():
            date_val = str(_row_val(row, date_col, ''))[:10]
            name_val = str(_row_val(row, name_col, ''))[:20]
            pos_val = str(_row_val(row, pos_col, ''))[:20]
            text_val = str(_row_val(row, text_col, ''))[:33]

            shares_raw = _row_val(row, shares_col, 'N/A')
            if shares_raw != 'N/A':
                try:
                    shares_str = format_number(float(shares_raw), 0)
                except (ValueError, TypeError):
                    shares_str = str(shares_raw)
            else:
                shares_str = 'N/A'

            value_raw = _row_val(row, value_col, 'N/A')
            if value_raw != 'N/A':
                try:
                    value_str = format_number(float(value_raw))
                except (ValueError, TypeError):
                    value_str = str(value_raw)
            else:
                value_str = 'N/A'

            lines.append(f"    {date_val:<12} {name_val:<22} {pos_val:<22} {text_val:<35} {shares_str:>10} {value_str:>12}")

        lines.append(f"  ({len(txns)} total transactions on record)")
    else:
        lines.append("  Recent transactions: N/A")

    # Insider purchases summary
    purchases = safe_get_attr(ticker_obj, 'insider_purchases')
    if purchases is not None and isinstance(purchases, pd.DataFrame) and len(purchases) > 0:
        lines.append("")
        lines.append("  Purchase summary (recent):")
        for _, row in purchases.iterrows():
            label = str(row.iloc[0]) if len(row) > 0 else "N/A"
            vals = []
            for v in row.iloc[1:]:
                if isinstance(v, (int, float)) and v == v:  # not NaN
                    if abs(v) >= 1000:
                        vals.append(format_number(v))
                    elif abs(v) < 1:
                        vals.append(f"{v:.3f}")
                    else:
                        vals.append(f"{v:.0f}")
                else:
                    vals.append(str(v))
            lines.append(f"    {label}: {', '.join(vals)}")

    # Holdings percentages from info
    lines.append("")
    lines.append("  Holdings:")
    insider_pct = safe_info_get(info, 'heldPercentInsiders')
    inst_pct = safe_info_get(info, 'heldPercentInstitutions')
    lines.append(f"    Insiders: {format_pct(insider_pct)}")
    lines.append(f"    Institutions: {format_pct(inst_pct)}")

    return "\n".join(lines)


def render_institutional_holders(ticker_obj):
    """Render top institutional holders section."""
    lines = []
    lines.append("INSTITUTIONAL HOLDERS (top 5):")

    holders = safe_get_attr(ticker_obj, 'institutional_holders')
    if holders is not None and isinstance(holders, pd.DataFrame) and len(holders) > 0:
        show = holders.head(5)

        holder_col = _get_col(show, ['Holder', 'holder', 'Name'])
        shares_col = _get_col(show, ['Shares', 'shares', 'Position'])
        pct_col = _get_col(show, ['% Out', 'pctHeld', 'Percent'])
        value_col = _get_col(show, ['Value', 'value'])
        date_col = _get_col(show, ['Date Reported', 'dateReported'])

        lines.append(f"  {'Holder':<40} {'Shares':>12} {'% Out':>8} {'Value':>12} {'Date':>12}")
        lines.append(f"  {'-' * 86}")

        for _, row in show.iterrows():
            h_name = str(_row_val(row, holder_col, 'N/A'))[:38]
            h_shares = format_number(_row_val(row, shares_col, 'N/A'))
            h_pct = format_pct(_row_val(row, pct_col, 'N/A'))
            h_val = format_number(_row_val(row, value_col, 'N/A'))
            h_date = str(_row_val(row, date_col, 'N/A'))[:10]
            lines.append(f"  {h_name:<40} {h_shares:>12} {h_pct:>8} {h_val:>12} {h_date:>12}")
    else:
        lines.append("  N/A")

    return "\n".join(lines)


def render_short_interest(info):
    """Render short interest section."""
    lines = []
    lines.append("SHORT INTEREST:")

    short_ratio = safe_info_get(info, 'shortRatio')
    short_pct = safe_info_get(info, 'shortPercentOfFloat')
    shares_short = safe_info_get(info, 'sharesShort')
    shares_short_prior = safe_info_get(info, 'sharesShortPriorMonth')
    short_date = safe_info_get(info, 'dateShortInterest')

    if short_ratio != "N/A":
        lines.append(f"  Short ratio: {short_ratio:.1f} days to cover")
    else:
        lines.append("  Short ratio: N/A")

    if short_pct != "N/A":
        lines.append(f"  Short % of float: {format_pct(short_pct)}")
    else:
        lines.append("  Short % of float: N/A")

    if shares_short != "N/A":
        lines.append(f"  Shares short: {format_number(shares_short)}")
    else:
        lines.append("  Shares short: N/A")

    if shares_short_prior != "N/A":
        lines.append(f"  Shares short prior month: {format_number(shares_short_prior)}")
        if shares_short != "N/A":
            try:
                chg = (float(shares_short) - float(shares_short_prior)) / float(shares_short_prior) * 100
                lines.append(f"  Month-over-month change: {chg:+.1f}%")
            except (ValueError, ZeroDivisionError):
                pass
    else:
        lines.append("  Shares short prior month: N/A")

    if short_date != "N/A":
        try:
            from datetime import datetime
            if isinstance(short_date, (int, float)):
                dt = datetime.fromtimestamp(short_date)
                lines.append(f"  Report date: {dt.strftime('%Y-%m-%d')}")
            else:
                lines.append(f"  Report date: {str(short_date)[:10]}")
        except Exception:
            lines.append(f"  Report date: {short_date}")

    return "\n".join(lines)


def render_analyst_consensus(ticker_obj, info, currency):
    """Render analyst consensus section."""
    lines = []
    lines.append("ANALYST CONSENSUS:")

    # Try recommendations_summary first, then recommendations
    rec_summary = safe_get_attr(ticker_obj, 'recommendations_summary')
    if rec_summary is not None and isinstance(rec_summary, pd.DataFrame) and len(rec_summary) > 0:
        # Use the most recent period row
        recent = rec_summary.iloc[0]
        sb = recent.get('strongBuy', recent.get('Strong Buy', 0)) or 0
        b = recent.get('buy', recent.get('Buy', 0)) or 0
        h = recent.get('hold', recent.get('Hold', 0)) or 0
        s = recent.get('sell', recent.get('Sell', 0)) or 0
        ss = recent.get('strongSell', recent.get('Strong Sell', 0)) or 0
        lines.append(f"  Strong Buy: {int(sb)} | Buy: {int(b)} | Hold: {int(h)} | Sell: {int(s)} | Strong Sell: {int(ss)}")

        # Show period label if available
        period_col = _get_col(rec_summary, ['period', 'Period'])
        if period_col and recent.get(period_col):
            lines.append(f"  Period: {recent[period_col]}")
    else:
        # Fallback: try recommendations
        recs = safe_get_attr(ticker_obj, 'recommendations')
        if recs is not None and isinstance(recs, pd.DataFrame) and len(recs) > 0:
            recent = recs.tail(5)
            lines.append("  Recent recommendations:")
            for _, row in recent.iterrows():
                firm = str(row.get('Firm', row.get('firm', 'N/A')))[:30]
                grade = str(row.get('To Grade', row.get('toGrade', 'N/A')))
                action = str(row.get('Action', row.get('action', '')))
                lines.append(f"    {firm:<30} {action:<12} {grade}")
        else:
            lines.append("  Recommendations: N/A")

    # Number of analysts
    num_analysts = safe_info_get(info, 'numberOfAnalystOpinions')
    if num_analysts != "N/A":
        lines.append(f"  Number of analysts: {int(num_analysts)}")

    # Recommendation key
    rec_key = safe_info_get(info, 'recommendationKey')
    if rec_key != "N/A":
        lines.append(f"  Consensus key: {rec_key}")

    # Target prices
    target_low = safe_info_get(info, 'targetLowPrice')
    target_mean = safe_info_get(info, 'targetMeanPrice')
    target_high = safe_info_get(info, 'targetHighPrice')
    target_median = safe_info_get(info, 'targetMedianPrice')

    if target_mean != "N/A" or target_low != "N/A" or target_high != "N/A":
        low_str = format_currency(target_low, currency) if target_low != "N/A" else "N/A"
        mean_str = format_currency(target_mean, currency) if target_mean != "N/A" else "N/A"
        median_str = format_currency(target_median, currency) if target_median != "N/A" else "N/A"
        high_str = format_currency(target_high, currency) if target_high != "N/A" else "N/A"
        lines.append(f"  Target prices: Low {low_str} | Mean {mean_str} | Median {median_str} | High {high_str}")

        # Current price for context
        current = safe_info_get(info, 'currentPrice')
        if current == "N/A":
            current = safe_info_get(info, 'regularMarketPrice')
        if current == "N/A":
            current = safe_info_get(info, 'previousClose')
        if current != "N/A" and target_mean != "N/A":
            try:
                diff_pct = (float(target_mean) - float(current)) / float(current) * 100
                lines.append(f"  Current price: {format_currency(current, currency)} (mean target {diff_pct:+.1f}% from current)")
            except (ValueError, ZeroDivisionError):
                pass
    else:
        lines.append("  Target prices: N/A")

    return "\n".join(lines)


# ==============================================================================
# Main
# ==============================================================================

def process_ticker(ticker_str, sections=None, compact=False):
    """Process and display all data for a single ticker."""
    all_sections = ['insider', 'institutional', 'short', 'analyst']
    if sections is None:
        sections = all_sections

    try:
        t = yf.Ticker(ticker_str)
        info = t.info or {}
    except Exception as e:
        print(f"ERROR: Could not fetch data for {ticker_str}: {e}")
        return

    name = info.get('shortName', info.get('longName', ticker_str))
    currency = info.get('currency', 'USD')

    print("=" * 80)
    print(f"INSIDER & MARKET DATA: {ticker_str} ({name})")
    print("=" * 80)
    print()

    rendered = []

    if 'insider' in sections:
        rendered.append(render_insider_activity(t, info))

    if 'institutional' in sections:
        rendered.append(render_institutional_holders(t))

    if 'short' in sections:
        rendered.append(render_short_interest(info))

    if 'analyst' in sections:
        rendered.append(render_analyst_consensus(t, info, currency))

    print("\n\n".join(rendered))
    print()
    print("[Raw data. Reason from principles.md]")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Insider Tracker - Raw insider, institutional, short interest, and analyst data via yfinance.",
        epilog="Examples:\n"
               "  python3 tools/insider_tracker.py ADBE\n"
               "  python3 tools/insider_tracker.py ADBE NVO MONY.L\n"
               "  python3 tools/insider_tracker.py ADBE --sections insider,short\n"
               "  python3 tools/insider_tracker.py ADBE --compact\n",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('tickers', nargs='+', help='One or more ticker symbols')
    parser.add_argument('--sections', type=str, default=None,
                        help='Comma-separated sections to show: insider,institutional,short,analyst (default: all)')
    parser.add_argument('--compact', action='store_true',
                        help='Compact output (fewer rows per section)')

    args = parser.parse_args()

    sections = None
    if args.sections:
        sections = [s.strip().lower() for s in args.sections.split(',')]
        valid = {'insider', 'institutional', 'short', 'analyst'}
        invalid = set(sections) - valid
        if invalid:
            print(f"ERROR: Invalid sections: {invalid}. Valid: {valid}")
            sys.exit(1)

    for i, ticker in enumerate(args.tickers):
        if i > 0:
            print()
        process_ticker(ticker.upper() if '.' not in ticker else ticker, sections, args.compact)


if __name__ == '__main__':
    main()
