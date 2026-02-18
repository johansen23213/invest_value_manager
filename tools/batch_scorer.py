#!/usr/bin/env python3
"""
Batch Quality Scorer - Mass-screen and score companies across market indices.

Discovery tool: scores all companies in an index using the quality_scorer logic,
identifies qualifying companies (QS >= 55), and optionally adds NEW discoveries
to the quality universe.

Outputs RAW DATA only. No recommendations, no judgments.

Usage:
  python3 tools/batch_scorer.py --index sp500
  python3 tools/batch_scorer.py --tickers AAPL,MSFT,GOOG
  python3 tools/batch_scorer.py --all
  python3 tools/batch_scorer.py --index ftse250 --add-to-universe
  python3 tools/batch_scorer.py --index stoxx600 --new-only
  python3 tools/batch_scorer.py --index nordic --add-to-universe --dry-run
  python3 tools/batch_scorer.py --index sp500 --min-qs 75            # Only Tier A
  python3 tools/batch_scorer.py --index sp500 --save progress.csv    # Save to CSV
  python3 tools/batch_scorer.py --index dax40 --workers 5            # Fewer workers
"""

import sys
import os
import argparse
import csv
import time
import warnings
from datetime import date, datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

import yaml
import yfinance as yf

warnings.filterwarnings('ignore')

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_DIR = SCRIPT_DIR.parent
UNIVERSE_PATH = PROJECT_DIR / "state" / "quality_universe.yaml"

# ---------------------------------------------------------------------------
# Import scoring logic from quality_scorer.py
# ---------------------------------------------------------------------------

sys.path.insert(0, str(SCRIPT_DIR))
from quality_scorer import extract_profile, calculate_legacy_score

# ---------------------------------------------------------------------------
# Import index resolution from dynamic_screener.py
# ---------------------------------------------------------------------------

from dynamic_screener import (
    get_index_tickers,
    INDEX_SOURCES,
    COMPOSITE_INDICES,
)

# ---------------------------------------------------------------------------
# Universe I/O
# ---------------------------------------------------------------------------

def load_universe():
    """Load quality_universe.yaml. Returns dict with 'quality_universe' key."""
    if not UNIVERSE_PATH.exists():
        return {"quality_universe": {"last_updated": str(date.today()), "companies": []}}
    with open(UNIVERSE_PATH, "r") as f:
        data = yaml.safe_load(f) or {}
    if "quality_universe" not in data:
        data["quality_universe"] = {"last_updated": str(date.today()), "companies": []}
    if data["quality_universe"].get("companies") is None:
        data["quality_universe"]["companies"] = []
    return data


def save_universe(data):
    """Write quality_universe.yaml back to disk."""
    data["quality_universe"]["last_updated"] = str(date.today())
    with open(UNIVERSE_PATH, "w") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True,
                  sort_keys=False, width=120)


def get_universe_tickers(data):
    """Return set of tickers already in the universe."""
    companies = data["quality_universe"]["companies"]
    return {c["ticker"].upper() for c in companies}


def get_universe_entry(data, ticker):
    """Return the universe entry for a ticker, or None."""
    for c in data["quality_universe"]["companies"]:
        if c["ticker"].upper() == ticker.upper():
            return c
    return None


# ---------------------------------------------------------------------------
# Batch scoring
# ---------------------------------------------------------------------------

def score_single_ticker(ticker):
    """
    Score a single ticker. Returns dict with scoring data or None on failure.
    Uses quality_scorer's extract_profile + calculate_legacy_score.
    """
    try:
        profile = extract_profile(ticker)
        if profile is None:
            return None

        legacy = calculate_legacy_score(profile)

        # Get current price
        info = yf.Ticker(ticker).info
        price = info.get("currentPrice") or info.get("regularMarketPrice") or info.get("previousClose")
        currency = info.get("currency", "USD")

        return {
            "ticker": ticker,
            "name": profile.get("name", ticker),
            "qs": legacy["total"],
            "tier": legacy["tier"],
            "category": legacy["category"],
            "sector": profile.get("sector", "Unknown"),
            "industry": profile.get("industry", "Unknown"),
            "currency": currency,
            "price": price,
            "market_cap": profile.get("market_cap", 0),
            # Key profile data for context
            "roic": profile.get("roic_current"),
            "roic_wacc_spread": profile.get("roic_wacc_spread"),
            "fcf_margin": profile.get("fcf_current_margin"),
            "gm_current": profile.get("gm_current"),
            "net_debt_ebitda": profile.get("net_debt_ebitda"),
            "rev_cagr": profile.get("rev_cagr"),
            "eps_cagr": profile.get("eps_cagr"),
            "insider_ownership": profile.get("insider_ownership", 0),
            "data_gaps": profile.get("data_gaps", []),
        }
    except Exception as e:
        return None


def batch_score(tickers, workers=10, batch_delay=2.0, batch_size=10):
    """
    Score a list of tickers in parallel batches.
    Returns list of result dicts (only successful scores).
    """
    results = []
    total = len(tickers)
    done = 0
    failed = 0
    batch_num = 0
    total_batches = (total + batch_size - 1) // batch_size

    print(f"\nScoring {total} tickers ({workers} workers, batches of {batch_size})...",
          file=sys.stderr)
    t0 = time.time()

    # Process in batches to respect rate limits
    for i in range(0, total, batch_size):
        batch = tickers[i:i + batch_size]
        batch_num += 1

        print(f"  Scoring batch {batch_num}/{total_batches} "
              f"({i + 1}-{min(i + batch_size, total)} of {total} tickers)...",
              file=sys.stderr)

        with ThreadPoolExecutor(max_workers=min(workers, len(batch))) as executor:
            futures = {executor.submit(score_single_ticker, t): t for t in batch}
            for future in as_completed(futures):
                ticker = futures[future]
                done += 1
                try:
                    result = future.result()
                    if result is not None:
                        results.append(result)
                    else:
                        failed += 1
                except Exception:
                    failed += 1

        # Rate limit between batches
        if i + batch_size < total:
            time.sleep(batch_delay)

    elapsed = time.time() - t0
    print(f"  Done: {done} processed, {len(results)} scored, {failed} failed "
          f"({elapsed:.0f}s)", file=sys.stderr)
    return results


# ---------------------------------------------------------------------------
# Formatting helpers
# ---------------------------------------------------------------------------

def fmt_pct(val):
    """Format a decimal as percentage string."""
    if val is None:
        return "N/A"
    return f"{val * 100:.1f}%"


def fmt_money_short(val):
    """Format market cap in B/M."""
    if val is None or val == 0:
        return "N/A"
    if abs(val) >= 1e9:
        return f"{val / 1e9:.1f}B"
    elif abs(val) >= 1e6:
        return f"{val / 1e6:.0f}M"
    return f"{val:,.0f}"


def fmt_price(val, currency):
    """Format price with currency indicator."""
    if val is None:
        return "N/A"
    if currency == "GBp":
        return f"{val:.0f}p"
    elif currency == "EUR":
        return f"EUR {val:.2f}"
    elif currency == "USD":
        return f"${val:.2f}"
    elif currency in ("GBX", "GBP"):
        return f"{val:.2f} {currency}"
    return f"{val:.2f} {currency}"


# ---------------------------------------------------------------------------
# Universe integration
# ---------------------------------------------------------------------------

def add_new_to_universe(data, new_discoveries, dry_run=False):
    """
    Add new qualifying companies to the universe.
    Returns count of companies added.
    """
    companies = data["quality_universe"]["companies"]
    existing_tickers = {c["ticker"].upper() for c in companies}
    today = str(date.today())
    added = 0

    for r in new_discoveries:
        ticker = r["ticker"].upper()
        if ticker in existing_tickers:
            continue

        entry = {
            "ticker": ticker,
            "name": r["name"],
            "direction": "long",
            "qs_tool": r["qs"],
            "qs_adj": r["qs"],
            "tier": r["tier"],
            "sector": r["sector"],
            "fair_value": 0,
            "entry_price": 0,
            "currency": r["currency"],
            "current_price": r["price"],
            "distance_to_entry": None,
            "pipeline_status": "SCORED",
            "thesis_path": "",
            "last_scored": today,
            "last_price_check": today,
            "notes": "Auto-scored by batch_scorer. Needs R1 analysis.",
        }

        if not dry_run:
            companies.append(entry)
            existing_tickers.add(ticker)

        added += 1

    return added


def update_existing_in_universe(data, existing_matches):
    """
    Update qs_tool, current_price, last_scored, last_price_check for existing entries.
    NEVER modifies fair_value, entry_price, pipeline_status, notes, or thesis_path.
    Returns count of companies updated.
    """
    today = str(date.today())
    updated = 0

    for r in existing_matches:
        entry = get_universe_entry(data, r["ticker"])
        if entry is None:
            continue

        # Only update if our score is newer
        last_scored = entry.get("last_scored")
        if last_scored == today:
            continue  # Already scored today

        entry["qs_tool"] = r["qs"]
        entry["current_price"] = r["price"]
        entry["last_scored"] = today
        entry["last_price_check"] = today

        # Update tier based on new QS (but only qs_tool, not qs_adj)
        # Tier from qs_tool only -- qs_adj is manual and not touched
        updated += 1

    return updated


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def print_report(results, index_name, universe_tickers, args):
    """Print the batch scoring report."""
    today = str(date.today())
    min_qs = args.min_qs

    # Filter qualifying
    qualifying = [r for r in results if r["qs"] >= min_qs]

    # Split into new vs existing
    new_discoveries = [r for r in qualifying if r["ticker"].upper() not in universe_tickers]
    existing_matches = [r for r in qualifying if r["ticker"].upper() in universe_tickers]

    # Sort by QS descending
    qualifying.sort(key=lambda x: -x["qs"])
    new_discoveries.sort(key=lambda x: -x["qs"])
    existing_matches.sort(key=lambda x: -x["qs"])

    # Header
    print(f"\nBATCH SCORING REPORT | {index_name} | {today}")
    print("=" * 100)
    print(f"Scanned:                {len(results)} tickers successfully scored")
    print(f"Qualifying (QS >= {min_qs}): {len(qualifying)}")
    print(f"Already in universe:    {len(existing_matches)}")
    print(f"NEW discoveries:        {len(new_discoveries)}")

    # Count Tier A discoveries
    tier_a_new = [r for r in new_discoveries if r["tier"] == "A"]
    if tier_a_new:
        print(f"** TIER A NEW:          {len(tier_a_new)} **")

    # NEW DISCOVERIES section
    if new_discoveries and not args.existing_only:
        print(f"\n{'='*100}")

        if args.new_only:
            print(f"NEW DISCOVERIES (QS >= {min_qs}, not in universe):")
        else:
            print(f"NEW DISCOVERIES:")
        print(f"{'='*100}")

        _print_company_table(new_discoveries)

    # EXISTING section (score update)
    if existing_matches and not args.new_only:
        print(f"\n{'='*100}")
        print(f"ALREADY IN UNIVERSE (score reference):")
        print(f"{'='*100}")

        _print_company_table(existing_matches, show_existing=True)

    # Below threshold (optional, only if verbose)
    if args.verbose:
        below = [r for r in results if r["qs"] < min_qs]
        if below:
            below.sort(key=lambda x: -x["qs"])
            # Only show top 20 closest to threshold
            near_threshold = [r for r in below if r["qs"] >= min_qs - 10]
            if near_threshold:
                print(f"\n{'='*100}")
                print(f"NEAR THRESHOLD (QS {min_qs - 10}-{min_qs - 1}):")
                print(f"{'='*100}")
                _print_company_table(near_threshold[:20])

    # Summary stats
    if qualifying:
        print(f"\nSUMMARY STATISTICS (qualifying):")
        print(f"  Average QS:        {sum(r['qs'] for r in qualifying) / len(qualifying):.1f}")
        print(f"  Tier A:            {sum(1 for r in qualifying if r['tier'] == 'A')}")
        print(f"  Tier B:            {sum(1 for r in qualifying if r['tier'] == 'B')}")

        # Sector distribution
        sectors = {}
        for r in qualifying:
            s = r["sector"]
            sectors[s] = sectors.get(s, 0) + 1
        print(f"  Sectors:           {len(sectors)}")
        if len(sectors) <= 15:
            for s, count in sorted(sectors.items(), key=lambda x: -x[1]):
                print(f"    {s}: {count}")

    print(f"\n[Raw data. Reason from principles.md]")

    return new_discoveries, existing_matches


def _print_company_table(companies, show_existing=False):
    """Print formatted table of scored companies."""
    header = (
        f"{'Ticker':<12} {'Name':<28} {'QS':>3} {'Tier':>4} "
        f"{'Sector':<24} {'Price':>10} {'MCap':>8} "
        f"{'ROIC':>6} {'Spread':>7} {'FCF%':>6} {'RevCAGR':>8} {'Insider':>7}"
    )
    print(header)
    print("-" * len(header))

    for r in companies:
        roic_str = fmt_pct(r.get("roic")) if r.get("roic") is not None else "N/A"
        spread = r.get("roic_wacc_spread")
        spread_str = f"{spread * 100:+.1f}pp" if spread is not None else "N/A"
        fcf_str = fmt_pct(r.get("fcf_margin")) if r.get("fcf_margin") is not None else "N/A"
        rev_str = fmt_pct(r.get("rev_cagr")) if r.get("rev_cagr") is not None else "N/A"
        insider = r.get("insider_ownership", 0) or 0
        insider_str = fmt_pct(insider) if insider > 0 else "N/A"
        mcap_str = fmt_money_short(r.get("market_cap", 0))
        price_str = fmt_price(r.get("price"), r.get("currency", "USD"))

        # Tier A marker
        tier_marker = r["tier"]
        if r["tier"] == "A":
            tier_marker = "A *"

        print(
            f"{r['ticker']:<12} {r['name'][:28]:<28} {r['qs']:>3} {tier_marker:>4} "
            f"{r['sector'][:24]:<24} {price_str:>10} {mcap_str:>8} "
            f"{roic_str:>6} {spread_str:>7} {fcf_str:>6} {rev_str:>8} {insider_str:>7}"
        )

    # Data gap warnings
    companies_with_gaps = [r for r in companies if r.get("data_gaps")]
    if companies_with_gaps:
        print(f"\n  Data gaps detected for {len(companies_with_gaps)} companies "
              f"(scores may be lower due to missing data)")


def save_results_csv(results, filepath):
    """Save results to CSV for further processing."""
    if not results:
        print("No results to save.")
        return

    fieldnames = [
        "ticker", "name", "qs", "tier", "category", "sector", "industry",
        "currency", "price", "market_cap", "roic", "roic_wacc_spread",
        "fcf_margin", "gm_current", "net_debt_ebitda", "rev_cagr",
        "eps_cagr", "insider_ownership",
    ]

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(results)

    print(f"\nResults saved to {filepath}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    available_indices = (
        sorted(INDEX_SOURCES.keys()) +
        sorted(COMPOSITE_INDICES.keys()) +
        ["all"]
    )

    parser = argparse.ArgumentParser(
        description="Batch Quality Scorer - Mass-screen and score companies across indices.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Available indices: {', '.join(available_indices)}

Examples:
  python3 tools/batch_scorer.py --index sp500
  python3 tools/batch_scorer.py --tickers AAPL,MSFT,GOOG
  python3 tools/batch_scorer.py --all
  python3 tools/batch_scorer.py --index ftse250 --add-to-universe
  python3 tools/batch_scorer.py --index stoxx600 --new-only
  python3 tools/batch_scorer.py --index nordic --add-to-universe --dry-run
  python3 tools/batch_scorer.py --index sp500 --min-qs 75
  python3 tools/batch_scorer.py --index dax40 --save results.csv
        """,
    )

    # Input sources (mutually exclusive)
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("--index", type=str,
                             help=f"Index to score: {', '.join(available_indices)}")
    input_group.add_argument("--tickers", type=str,
                             help="Comma-separated list of tickers")
    input_group.add_argument("--all", action="store_true",
                             help="Score all available indices")

    # Filtering
    parser.add_argument("--min-qs", type=int, default=55,
                        help="Minimum QS to qualify (default: 55 = Tier B)")
    parser.add_argument("--new-only", action="store_true",
                        help="Show only NEW companies not in universe")
    parser.add_argument("--existing-only", action="store_true",
                        help="Show only companies already in universe")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Show near-threshold companies too")

    # Universe integration
    parser.add_argument("--add-to-universe", action="store_true",
                        help="Add qualifying NEW companies to quality_universe.yaml")
    parser.add_argument("--update-existing", action="store_true",
                        help="Update qs_tool and prices for existing universe entries")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be added without modifying files")

    # Performance
    parser.add_argument("--workers", type=int, default=10,
                        help="Parallel workers per batch (default: 10)")
    parser.add_argument("--batch-size", type=int, default=10,
                        help="Tickers per batch before rate-limit pause (default: 10)")
    parser.add_argument("--batch-delay", type=float, default=2.0,
                        help="Seconds to wait between batches (default: 2.0)")
    parser.add_argument("--refresh", action="store_true",
                        help="Force refresh index ticker cache from Wikipedia")

    # Output
    parser.add_argument("--save", type=str, default=None,
                        help="Save all results to CSV file")

    args = parser.parse_args()

    # --- Resolve tickers ---
    if args.all:
        index_name = "ALL"
        print(f"Batch Scorer - ALL indices", file=sys.stderr)
        tickers = get_index_tickers("all", force_refresh=args.refresh)
    elif args.tickers:
        index_name = "CUSTOM"
        tickers = [t.strip().upper() for t in args.tickers.split(",") if t.strip()]
        print(f"Batch Scorer - {len(tickers)} custom tickers", file=sys.stderr)
    else:
        index_name = args.index
        print(f"Batch Scorer - Index: {index_name}", file=sys.stderr)
        tickers = get_index_tickers(index_name, force_refresh=args.refresh)

    if not tickers:
        print("ERROR: No tickers found.", file=sys.stderr)
        sys.exit(1)

    # Deduplicate
    tickers = list(dict.fromkeys(tickers))
    print(f"  {len(tickers)} unique tickers to score", file=sys.stderr)

    # --- Score ---
    results = batch_score(
        tickers,
        workers=args.workers,
        batch_delay=args.batch_delay,
        batch_size=args.batch_size,
    )

    if not results:
        print("\nNo tickers could be scored. Check network connectivity.", file=sys.stderr)
        sys.exit(1)

    # --- Load universe for comparison ---
    universe_data = load_universe()
    universe_tickers = get_universe_tickers(universe_data)

    # --- Print report ---
    new_discoveries, existing_matches = print_report(
        results, index_name, universe_tickers, args
    )

    # --- Universe integration ---
    if args.add_to_universe and new_discoveries:
        added = add_new_to_universe(universe_data, new_discoveries, dry_run=args.dry_run)
        if args.dry_run:
            print(f"\n[DRY RUN] Would add {added} new companies to quality_universe.yaml")
        else:
            save_universe(universe_data)
            print(f"\nAdded {added} new companies to quality_universe.yaml")
            print(f"  Pipeline status: SCORED (needs R1 analysis)")

    if args.update_existing and existing_matches:
        updated = update_existing_in_universe(universe_data, existing_matches)
        if not args.dry_run:
            save_universe(universe_data)
            print(f"\nUpdated {updated} existing universe entries (qs_tool + price)")

    # --- Save CSV ---
    if args.save:
        save_results_csv(results, args.save)


if __name__ == "__main__":
    main()
