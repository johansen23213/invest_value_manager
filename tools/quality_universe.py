#!/usr/bin/env python3
"""
Quality Universe Tool - Persistent database of quality companies for Capital Deployment Machine.

Manages state/quality_universe.yaml with QS-scored companies, tracks prices,
detects actionable entries, and reports pipeline health metrics.

Supports two directions:
  - long (default): buy candidates. Entry price = price at or below which to buy.
  - short: fragility candidates. Entry price = price at or above which to open short.
    Fair value for shorts = TRUE value (price should converge DOWN to it).

Usage:
  python3 tools/quality_universe.py report              # Long universe (default)
  python3 tools/quality_universe.py report --fragility   # Short/fragility candidates only
  python3 tools/quality_universe.py actionable           # Long candidates within 15% of entry
  python3 tools/quality_universe.py actionable --fragility  # Short candidates at/above entry
  python3 tools/quality_universe.py add TICKER --qs 75 --fv 200 --entry 150 --sector "Technology" --tier A --currency USD
  python3 tools/quality_universe.py add TICKER --qs 75 --fv 200 --entry 150 --sector "Technology" --tier A --direction short
  python3 tools/quality_universe.py remove TICKER
  python3 tools/quality_universe.py coverage             # Sector coverage vs gaps
  python3 tools/quality_universe.py refresh              # Update prices for all companies (batch, rate-limit spaced)
  python3 tools/quality_universe.py stale                # Companies needing re-evaluation (by days since last scored)
  python3 tools/quality_universe.py stats                # Pipeline health metrics (raw data, no fixed targets)
"""

import sys
import os
import argparse
import time
from datetime import date, datetime

import yaml
import yfinance as yf

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
UNIVERSE_PATH = os.path.join(PROJECT_ROOT, "state", "quality_universe.yaml")
PORTFOLIO_PATH = os.path.join(PROJECT_ROOT, "portfolio", "current.yaml")
SECTORS_DIR = os.path.join(PROJECT_ROOT, "world", "sectors")

# ---------------------------------------------------------------------------
# FX helpers (same pattern as price_checker.py)
# ---------------------------------------------------------------------------

_fx_cache = {}
_fx_fallbacks_used = []


def get_fx_rates():
    """Fetch FX rates, with static fallback."""
    global _fx_cache, _fx_fallbacks_used
    defaults = {"EURUSD": 1.04, "GBPEUR": 1.19, "USDEUR": 1 / 1.04}
    fallbacks = []

    # EUR/USD
    try:
        eurusd = yf.Ticker("EURUSD=X").info.get("previousClose")
        if not eurusd:
            raise ValueError
    except Exception:
        eurusd = defaults["EURUSD"]
        fallbacks.append(f"EUR/USD={eurusd}")

    # GBP/EUR
    try:
        gbpeur = yf.Ticker("GBPEUR=X").info.get("previousClose")
        if not gbpeur:
            raise ValueError
    except Exception:
        gbpeur = defaults["GBPEUR"]
        fallbacks.append(f"GBP/EUR={gbpeur}")

    if fallbacks:
        _fx_fallbacks_used.extend(fallbacks)

    _fx_cache["EURUSD"] = eurusd
    _fx_cache["GBPEUR"] = gbpeur
    _fx_cache["USDEUR"] = 1 / eurusd
    _fx_cache["GBPUSD"] = gbpeur * eurusd  # approximate

    return eurusd, gbpeur


def print_fx_warning():
    if _fx_fallbacks_used:
        unique = list(dict.fromkeys(_fx_fallbacks_used))
        print(f"FX WARNING: Using static fallback rates ({', '.join(unique)}). EUR amounts may be inaccurate.")


# ---------------------------------------------------------------------------
# YAML I/O
# ---------------------------------------------------------------------------

def load_universe():
    """Load the quality universe YAML. Returns dict with 'quality_universe' key."""
    if not os.path.exists(UNIVERSE_PATH):
        return {"quality_universe": {"last_updated": str(date.today()), "companies": []}}
    with open(UNIVERSE_PATH, "r") as f:
        data = yaml.safe_load(f) or {}
    if "quality_universe" not in data:
        data["quality_universe"] = {"last_updated": str(date.today()), "companies": []}
    if data["quality_universe"].get("companies") is None:
        data["quality_universe"]["companies"] = []
    return data


def save_universe(data):
    """Write the quality universe YAML back to disk."""
    data["quality_universe"]["last_updated"] = str(date.today())
    with open(UNIVERSE_PATH, "w") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False, width=120)


def load_portfolio():
    """Load portfolio/current.yaml for cash info."""
    if not os.path.exists(PORTFOLIO_PATH):
        return None
    with open(PORTFOLIO_PATH, "r") as f:
        return yaml.safe_load(f)


# ---------------------------------------------------------------------------
# Direction helpers
# ---------------------------------------------------------------------------

def _get_direction(c):
    """Get direction for a company entry. Defaults to 'long' for backwards compatibility."""
    return c.get("direction", "long")


def _is_long(c):
    return _get_direction(c) == "long"


def _is_short(c):
    return _get_direction(c) == "short"


def _filter_by_direction(companies, fragility=False):
    """Filter companies by direction. fragility=False -> long only, fragility=True -> short only."""
    if fragility:
        return [c for c in companies if _is_short(c)]
    else:
        return [c for c in companies if _is_long(c)]


def _get_qs_display(c):
    """Get QS display value, handling None gracefully."""
    val = c.get("qs_adj")
    if val is not None:
        return val
    val = c.get("qs_tool")
    if val is not None:
        return val
    return "?"


def _calc_distance_to_entry(native_price, entry_price, direction):
    """
    Calculate distance to entry price, direction-aware.

    For LONG: distance = (price - entry) / entry * 100
      Positive = above entry (not yet actionable), negative = below entry (actionable)
      Actionable when distance <= 15% (price near or below entry)

    For SHORT: distance = (entry - price) / entry * 100
      Positive = price below entry (not yet actionable for short), negative = price above entry (actionable)
      Actionable when distance <= 0% (price at or above entry)
      We also show "within 15%" as distance <= 15% for consistency (price within 15% below entry)
    """
    if native_price is None or entry_price is None or entry_price == 0:
        return None

    if direction == "short":
        # For shorts: we want to know how far BELOW entry the price is
        # Negative distance = price is ABOVE entry = ACTIONABLE for short
        # Positive distance = price is BELOW entry = not yet actionable
        return round((entry_price - native_price) / entry_price * 100, 1)
    else:
        # For longs: standard calculation
        return round((native_price - entry_price) / entry_price * 100, 1)


def _is_actionable_entry(c, distance_threshold=15.0):
    """
    Check if a company is near entry based on direction.

    Long: distance_to_entry <= threshold (price within N% of entry or below)
    Short: distance_to_entry <= threshold (price within N% of entry or above)
      For shorts, distance is inverted so this naturally works:
      dist <= 0 means price >= entry (ideal for short)
      dist <= threshold means price is within N% below entry (close to entry)

    NOTE: The threshold is a presentation filter, not a buy/sell signal.
    The orchestrator reasons about whether to act from principles.
    """
    dist = c.get("distance_to_entry")
    if dist is None:
        return False
    return dist <= distance_threshold


# ---------------------------------------------------------------------------
# Price fetching
# ---------------------------------------------------------------------------

def fetch_price(ticker):
    """Fetch current price for a single ticker via yfinance. Returns (price, currency) or (None, None)."""
    try:
        info = yf.Ticker(ticker).info
        price = info.get("currentPrice") or info.get("regularMarketPrice") or info.get("previousClose")
        currency = info.get("currency", "USD")
        name = info.get("shortName", ticker)
        return price, currency, name
    except Exception:
        return None, None, None


def price_in_native(price, api_currency, target_currency):
    """
    Convert the API-returned price to the company's native currency for comparison
    with fair_value and entry_price stored in native currency.

    For GBp tickers: yfinance returns in GBp (pence), our YAML stores in pence.
    For EUR tickers: yfinance may return in EUR directly.
    For USD tickers: yfinance returns in USD.
    """
    if price is None:
        return None

    # GBp/GBX are already pence — our YAML for GBp companies stores in pence
    if api_currency in ("GBp", "GBX") and target_currency == "GBp":
        return price
    if api_currency == "GBP" and target_currency == "GBp":
        return price * 100

    # Same currency
    if api_currency == target_currency:
        return price

    # USD -> EUR
    if api_currency == "USD" and target_currency == "EUR":
        return price * _fx_cache.get("USDEUR", 1 / 1.04)

    # EUR -> USD
    if api_currency == "EUR" and target_currency == "USD":
        return price * _fx_cache.get("EURUSD", 1.04)

    # Fallback: return as-is
    return price


# ---------------------------------------------------------------------------
# Currency symbol helper
# ---------------------------------------------------------------------------

def currency_symbol(currency):
    symbols = {"USD": "$", "EUR": "EUR ", "GBp": "", "GBP": "GBP "}
    return symbols.get(currency, "")


def currency_suffix(currency):
    if currency == "GBp":
        return "p"
    return ""


def fmt_price(value, currency):
    """Format a price with appropriate currency prefix/suffix."""
    if value is None:
        return "N/A"
    sym = currency_symbol(currency)
    suf = currency_suffix(currency)
    if currency == "GBp":
        return f"{value:.0f}{suf}"
    if value >= 1000:
        return f"{sym}{value:,.0f}"
    return f"{sym}{value:.2f}"


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_report(args):
    """Full universe report with current prices and distance to entry."""
    data = load_universe()
    all_companies = data["quality_universe"]["companies"]

    if not all_companies:
        print("Quality Universe is empty. Use 'add' to populate.")
        return

    fragility = getattr(args, "fragility", False)
    companies = _filter_by_direction(all_companies, fragility=fragility)

    if not companies:
        direction_label = "short/fragility" if fragility else "long"
        print(f"No {direction_label} candidates in the universe.")
        return

    # Fetch prices if not recently refreshed (refresh ALL, not just filtered)
    eurusd, gbpeur = get_fx_rates()

    today = str(date.today())
    needs_refresh = []
    for c in all_companies:
        if c.get("last_price_check") != today:
            needs_refresh.append(c)

    if needs_refresh:
        print(f"Fetching prices for {len(needs_refresh)} companies...")
        _batch_refresh(needs_refresh)
        save_universe(data)

    # Re-filter after refresh (companies list references same objects, but re-filter for safety)
    companies = _filter_by_direction(all_companies, fragility=fragility)

    # Count stats
    tier_a = sum(1 for c in companies if c.get("tier") == "A")
    tier_b = sum(1 for c in companies if c.get("tier") == "B")
    sectors = len(set(c.get("sector", "Unknown") for c in companies))

    direction_label = "FRAGILITY (Short)" if fragility else "Long"
    print(f"\nQuality Universe Report [{direction_label}] | {today}")
    print("=" * 130)
    print(f"Companies: {len(companies)} | Tier A: {tier_a} | Tier B: {tier_b} | Sectors: {sectors}")
    print()

    # Header
    if fragility:
        hdr = f"{'Ticker':<10} {'Name':<25} {'QS':>3} {'Tier':>4} {'Sector':<22} {'TrueVal':>10} {'Short@':>10} {'Price':>10} {'Dist%':>7} {'Pipeline':<16}"
    else:
        hdr = f"{'Ticker':<10} {'Name':<25} {'QS':>3} {'Tier':>4} {'Sector':<22} {'FV':>10} {'Entry':>10} {'Price':>10} {'Dist%':>7} {'Pipeline':<16}"
    print(hdr)
    print("-" * 130)

    # Sort: Tier A first, then by distance_to_entry ascending (closest to actionable first)
    def sort_key(c):
        tier_order = {"A": 0, "B": 1, "C": 2, "D": 3}
        dist = c.get("distance_to_entry")
        dist_val = dist if dist is not None else 9999
        return (tier_order.get(c.get("tier", "D"), 3), dist_val)

    sorted_companies = sorted(companies, key=sort_key)

    actionable = []
    for c in sorted_companies:
        cur = c.get("currency", "USD")
        dist = c.get("distance_to_entry")
        dist_str = f"{dist:+.1f}%" if dist is not None else "N/A"

        qs_display = _get_qs_display(c)
        pipeline = c.get("pipeline_status", "UNKNOWN")

        # Mark actionable
        marker = ""
        if _is_actionable_entry(c):
            marker = " *"
            actionable.append(c)

        row = (
            f"{c['ticker']:<10} "
            f"{(c.get('name') or c['ticker'])[:25]:<25} "
            f"{qs_display:>3} "
            f"{(c.get('tier') or '?'):>4} "
            f"{(c.get('sector') or 'Unknown')[:22]:<22} "
            f"{fmt_price(c.get('fair_value'), cur):>10} "
            f"{fmt_price(c.get('entry_price'), cur):>10} "
            f"{fmt_price(c.get('current_price'), cur):>10} "
            f"{dist_str:>7} "
            f"{pipeline:<16}"
            f"{marker}"
        )
        print(row)

    # Actionable section
    if actionable:
        if fragility:
            print(f"\nACTIONABLE SHORTS (within 15% of short entry or above):")
            for c in sorted(actionable, key=lambda x: x.get("distance_to_entry", 9999)):
                cur = c.get("currency", "USD")
                dist = c.get("distance_to_entry", 0)
                at_label = "AT/ABOVE SHORT ENTRY" if dist <= 0 else ""
                print(f"  {c['ticker']}: {fmt_price(c.get('current_price'), cur)} vs short@ {fmt_price(c.get('entry_price'), cur)} ({dist:+.1f}%) [{(c.get('pipeline_status') or '?')}] {at_label}")
        else:
            print(f"\nACTIONABLE (within 15% of entry):")
            for c in sorted(actionable, key=lambda x: x.get("distance_to_entry", 9999)):
                cur = c.get("currency", "USD")
                dist = c.get("distance_to_entry", 0)
                print(f"  {c['ticker']}: {fmt_price(c.get('current_price'), cur)} vs entry {fmt_price(c.get('entry_price'), cur)} ({dist:+.1f}%) [{(c.get('pipeline_status') or '?')}]")
    else:
        if fragility:
            print(f"\nACTIONABLE SHORTS: None (no short candidates within 15% of entry or above)")
        else:
            print(f"\nACTIONABLE: None (no companies within 15% of entry price)")

    # Pipeline health summary (only for the filtered direction)
    print()
    _print_pipeline_health(companies)
    print_fx_warning()
    print("\n[Raw data. Reason from principles.md]")


def cmd_actionable(args):
    """Show only companies within actionable range of entry price."""
    data = load_universe()
    all_companies = data["quality_universe"]["companies"]

    if not all_companies:
        print("Quality Universe is empty.")
        return

    fragility = getattr(args, "fragility", False)

    eurusd, gbpeur = get_fx_rates()

    # Refresh prices
    today = str(date.today())
    needs_refresh = [c for c in all_companies if c.get("last_price_check") != today]
    if needs_refresh:
        print(f"Fetching prices for {len(needs_refresh)} companies...")
        _batch_refresh(needs_refresh)
        save_universe(data)

    # Filter by direction, then by actionable
    companies = _filter_by_direction(all_companies, fragility=fragility)
    actionable = [c for c in companies if _is_actionable_entry(c)]

    if not actionable:
        direction_label = "short/fragility" if fragility else "long"
        print(f"\nNo actionable {direction_label} candidates. Patience is alpha.")
        print_fx_warning()
        return

    # Sort by distance ascending
    actionable.sort(key=lambda c: c.get("distance_to_entry", 9999))

    direction_label = "Fragility (Short)" if fragility else "Long"
    print(f"\nActionable Companies [{direction_label}] | {today}")
    print("=" * 110)
    if fragility:
        print(f"{'Ticker':<10} {'Name':<25} {'QS':>3} {'Tier':>4} {'Short@':>10} {'Price':>10} {'Dist%':>7} {'Pipeline':<16} {'Notes'}")
    else:
        print(f"{'Ticker':<10} {'Name':<25} {'QS':>3} {'Tier':>4} {'Entry':>10} {'Price':>10} {'Dist%':>7} {'Pipeline':<16} {'Notes'}")
    print("-" * 110)

    for c in actionable:
        cur = c.get("currency", "USD")
        dist = c.get("distance_to_entry", 0)
        qs_display = _get_qs_display(c)
        notes = c.get("notes", "") or ""
        # Truncate notes
        if len(notes) > 40:
            notes = notes[:37] + "..."

        if fragility:
            at_label = "AT/ABOVE SHORT ENTRY" if dist <= 0 else ""
        else:
            at_label = "AT/BELOW ENTRY" if dist <= 0 else ""

        print(
            f"{c['ticker']:<10} "
            f"{(c.get('name') or '')[:25]:<25} "
            f"{qs_display:>3} "
            f"{(c.get('tier') or '?'):>4} "
            f"{fmt_price(c.get('entry_price'), cur):>10} "
            f"{fmt_price(c.get('current_price'), cur):>10} "
            f"{dist:+.1f}% "
            f"{(c.get('pipeline_status') or '?'):<16} "
            f"{at_label}"
        )

    print_fx_warning()
    print("\n[Raw data. Reason from principles.md]")


def cmd_add(args):
    """Add or update a company in the universe."""
    data = load_universe()
    companies = data["quality_universe"]["companies"]

    ticker = args.ticker.upper()
    direction = getattr(args, "direction", "long") or "long"

    # Check if already exists
    existing = None
    for i, c in enumerate(companies):
        if c["ticker"].upper() == ticker:
            existing = i
            break

    entry = {
        "ticker": ticker,
        "name": args.name or ticker,
        "direction": direction,
        "qs_tool": args.qs,
        "qs_adj": args.qs_adj if args.qs_adj is not None else args.qs,
        "tier": args.tier.upper(),
        "sector": args.sector,
        "fair_value": args.fv,
        "entry_price": args.entry,
        "currency": args.currency.upper() if args.currency != "GBp" else "GBp",
        "current_price": None,
        "distance_to_entry": None,
        "pipeline_status": args.pipeline or "SCORED",
        "thesis_path": args.thesis,
        "last_scored": str(date.today()),
        "last_price_check": None,
        "notes": args.notes or "",
    }

    # Try to fetch name from yfinance if not provided
    if args.name is None:
        try:
            info = yf.Ticker(ticker).info
            entry["name"] = info.get("shortName", ticker)
        except Exception:
            pass

    if existing is not None:
        # Update existing
        companies[existing] = entry
        print(f"Updated {ticker} in quality universe.")
    else:
        companies.append(entry)
        print(f"Added {ticker} to quality universe.")

    save_universe(data)

    dir_label = "[SHORT]" if direction == "short" else "[LONG]"
    print(f"  Direction: {dir_label}")
    print(f"  QS: {entry['qs_tool']} (adj: {entry['qs_adj']}) | Tier {entry['tier']} | Sector: {entry['sector']}")
    if direction == "short":
        print(f"  True Value: {fmt_price(entry['fair_value'], entry['currency'])} | Short@: {fmt_price(entry['entry_price'], entry['currency'])}")
    else:
        print(f"  FV: {fmt_price(entry['fair_value'], entry['currency'])} | Entry: {fmt_price(entry['entry_price'], entry['currency'])}")
    print(f"  Pipeline: {entry['pipeline_status']}")
    if entry["notes"]:
        print(f"  Notes: {entry['notes']}")


def cmd_remove(args):
    """Remove a company from the universe."""
    data = load_universe()
    companies = data["quality_universe"]["companies"]

    ticker = args.ticker.upper()
    original_len = len(companies)
    companies[:] = [c for c in companies if c["ticker"].upper() != ticker]

    if len(companies) < original_len:
        save_universe(data)
        print(f"Removed {ticker} from quality universe.")
    else:
        print(f"{ticker} not found in quality universe.")


def cmd_coverage(args):
    """Show sector coverage: which GICS sectors have sector views and universe companies."""
    data = load_universe()
    companies = data["quality_universe"]["companies"]

    # Define target sectors (from capital-deployment SKILL.md)
    target_sectors = [
        "Telecom",
        "Insurance",
        "Pharma/Healthcare",
        "Real Estate",
        "Business Services",
        "Consumer Staples",
        "Industrials",
        "Utilities",
        "Energy",
        "Media/Publishing",
        "Technology",
        "Financial Data",
        "Luxury Goods",
        "Payments/Fintech",
        "Semiconductors/Equipment",
        "Defense/Aerospace",
        "Healthcare Equipment",
        "Professional Services",
        "Environmental/Water",
        "Consumer Brands",
        "Digital Infrastructure",
        "Industrial Technology",
        "Testing/Inspection/Cert",
    ]

    # Scan existing sector views
    existing_views = set()
    if os.path.exists(SECTORS_DIR):
        for f in os.listdir(SECTORS_DIR):
            if f.endswith(".md") and f != "_TEMPLATE.md":
                existing_views.add(f.replace(".md", ""))

    # Map sector view filenames to sector names (approximate matching)
    view_map = {
        "telecom": "Telecom",
        "insurance": "Insurance",
        "pharma-healthcare": "Pharma/Healthcare",
        "real-estate": "Real Estate",
        "business-services": "Business Services",
        "consumer-staples": "Consumer Staples",
        "industrials": "Industrials",
        "utilities": "Utilities",
        "energy": "Energy",
        "media-publishing": "Media/Publishing",
        "technology": "Technology",
        "financial-data-analytics": "Financial Data",
        "luxury-goods": "Luxury Goods",
        "payments-fintech": "Payments/Fintech",
        "consumer-discretionary": "Consumer Brands",
        "digital-marketplaces": "Digital Infrastructure",
        "automotive": "Industrial Technology",
        "auto-eu": "Industrial Technology",
    }

    # Count companies per sector (from universe -- long only for coverage)
    long_companies = _filter_by_direction(companies, fragility=False)
    sector_counts = {}
    for c in long_companies:
        s = c.get("sector", "Unknown")
        sector_counts[s] = sector_counts.get(s, 0) + 1

    # Determine which target sectors have views
    covered_sectors = set()
    for view_name in existing_views:
        mapped = view_map.get(view_name)
        if mapped:
            covered_sectors.add(mapped)

    print(f"\nSector Coverage Report | {date.today()}")
    print("=" * 90)
    print(f"{'Sector':<30} {'Sector View':>12} {'Universe Cos':>14} {'Status'}")
    print("-" * 90)

    covered_count = 0
    for sector in target_sectors:
        has_view = sector in covered_sectors
        count = 0
        # Match universe companies to sector (fuzzy)
        for c in long_companies:
            cs = c.get("sector", "").lower()
            sl = sector.lower()
            if sl in cs or cs in sl or any(w in cs for w in sl.split("/")):
                count += 1

        if has_view:
            view_str = "YES"
            covered_count += 1
        else:
            view_str = "NO"

        status = ""
        if has_view and count > 0:
            status = "COVERED"
        elif has_view and count == 0:
            status = "VIEW ONLY (no universe companies)"
        elif not has_view and count > 0:
            status = "COMPANIES BUT NO VIEW"
        else:
            status = "GAP"

        print(f"{sector:<30} {view_str:>12} {count:>14} {status}")

    print(f"\nSummary: {covered_count}/{len(target_sectors)} sectors have views")
    print(f"Universe companies by sector (long):")
    for s, count in sorted(sector_counts.items(), key=lambda x: -x[1]):
        print(f"  {s}: {count}")

    # Show short candidates if any
    short_companies = _filter_by_direction(companies, fragility=True)
    if short_companies:
        print(f"\nFragility candidates (short): {len(short_companies)}")
        for c in short_companies:
            print(f"  {c['ticker']} ({c.get('sector', '?')})")


def cmd_refresh(args):
    """Update prices for ALL companies in the universe (batch with rate limiting)."""
    data = load_universe()
    companies = data["quality_universe"]["companies"]

    if not companies:
        print("Quality Universe is empty.")
        return

    get_fx_rates()

    print(f"Refreshing prices for {len(companies)} companies...")
    _batch_refresh(companies, verbose=True)
    save_universe(data)

    print(f"\nRefresh complete. {len(companies)} companies updated.")
    print_fx_warning()


def cmd_stale(args):
    """Show companies that may need re-evaluation, sorted by days since last scored."""
    data = load_universe()
    companies = data["quality_universe"]["companies"]

    if not companies:
        print("Quality Universe is empty.")
        return

    today = date.today()
    stale_list = []

    for c in companies:
        last_scored = c.get("last_scored")
        if last_scored:
            try:
                scored_date = datetime.strptime(str(last_scored), "%Y-%m-%d").date()
                days_ago = (today - scored_date).days
            except (ValueError, TypeError):
                days_ago = 999
        else:
            days_ago = 999

        stale_list.append((c, days_ago))

    # Sort by days_ago descending (most stale first)
    stale_list.sort(key=lambda x: -x[1])

    print(f"\nUniverse Staleness Report | {today}")
    print("=" * 110)
    print(f"{'Ticker':<10} {'Dir':<5} {'Name':<25} {'QS':>3} {'Tier':>4} {'Last Scored':>12} {'Days Ago':>9} {'Pipeline':<16}")
    print("-" * 110)

    for c, days_ago in stale_list:
        last_scored = c.get("last_scored", "never")
        days_str = str(days_ago) if days_ago < 999 else "never"
        qs_display = _get_qs_display(c)
        direction = _get_direction(c)
        dir_label = "S" if direction == "short" else "L"

        print(
            f"{c['ticker']:<10} "
            f"{dir_label:<5} "
            f"{(c.get('name') or c['ticker'])[:25]:<25} "
            f"{qs_display:>3} "
            f"{(c.get('tier') or '?'):>4} "
            f"{str(last_scored):>12} "
            f"{days_str:>9} "
            f"{(c.get('pipeline_status') or 'UNKNOWN'):<16}"
        )

    print(f"\nTotal: {len(companies)} companies")
    long_count = sum(1 for c in companies if _is_long(c))
    short_count = sum(1 for c in companies if _is_short(c))
    print(f"  Long: {long_count} | Short: {short_count}")
    print(f"Use judgment: earnings, regulatory changes, or material events warrant earlier re-evaluation.")


def cmd_stats(args):
    """Pipeline health metrics -- raw data, no fixed targets."""
    data = load_universe()
    companies = data["quality_universe"]["companies"]

    # Load portfolio for cash info
    portfolio = load_portfolio()
    cash_amount = 0
    cash_currency = "EUR"

    if portfolio:
        cash_info = portfolio.get("cash", {})
        cash_amount = cash_info.get("amount", 0)
        cash_currency = cash_info.get("currency", "EUR")

    # Direction counts
    long_companies = _filter_by_direction(companies, fragility=False)
    short_companies = _filter_by_direction(companies, fragility=True)

    # Counts (long universe -- primary pipeline)
    total = len(companies)
    total_long = len(long_companies)
    total_short = len(short_companies)
    tier_a = sum(1 for c in long_companies if c.get("tier") == "A")
    tier_b = sum(1 for c in long_companies if c.get("tier") == "B")

    # Pipeline status counts (long)
    status_counts = {}
    for c in long_companies:
        s = c.get("pipeline_status", "UNKNOWN")
        status_counts[s] = status_counts.get(s, 0) + 1

    r1_plus = sum(1 for c in long_companies if c.get("pipeline_status", "") in ("R1_COMPLETE", "R2_COMPLETE", "R3_COMPLETE", "APPROVED", "STANDING_ORDER"))
    approved = sum(1 for c in long_companies if c.get("pipeline_status", "") in ("APPROVED", "STANDING_ORDER"))

    # Standing orders: count from standing_orders.yaml
    standing_orders_count = 0
    so_path = os.path.join(PROJECT_ROOT, "state", "standing_orders.yaml")
    if os.path.exists(so_path):
        try:
            with open(so_path, "r") as f:
                so_data = yaml.safe_load(f) or {}
            so = so_data.get("standing_orders", [])
            if so:
                standing_orders_count = len(so)
        except Exception:
            pass

    # Sectors covered (long)
    sectors = set(c.get("sector", "Unknown") for c in long_companies)

    # Actionable (long)
    actionable_long = sum(1 for c in long_companies if _is_actionable_entry(c))

    # Actionable (short)
    actionable_short = sum(1 for c in short_companies if _is_actionable_entry(c))

    # Staleness (all)
    today = date.today()
    stale_30 = 0
    stale_90 = 0
    for c in companies:
        last_scored = c.get("last_scored")
        if last_scored:
            try:
                scored_date = datetime.strptime(str(last_scored), "%Y-%m-%d").date()
                days_ago = (today - scored_date).days
                if days_ago > 90:
                    stale_90 += 1
                elif days_ago > 30:
                    stale_30 += 1
            except (ValueError, TypeError):
                stale_90 += 1
        else:
            stale_90 += 1

    print(f"\nPipeline Health Metrics | {date.today()}")
    print("=" * 50)
    print(f"Universe total:      {total:>5}")
    print(f"  Long candidates:   {total_long:>5}")
    print(f"  Short candidates:  {total_short:>5}")
    print(f"Long breakdown:")
    print(f"  Tier A:            {tier_a:>5}")
    print(f"  Tier B:            {tier_b:>5}")
    print(f"  R1+ thesis:        {r1_plus:>5}")
    print(f"  Approved (R4+):    {approved:>5}")
    print(f"Standing orders:     {standing_orders_count:>5}")
    print(f"Sectors covered:     {len(sectors):>5}")
    print(f"Actionable (long):   {actionable_long:>5}")
    if total_short > 0:
        print(f"Actionable (short):  {actionable_short:>5}")
    print(f"Scored >30d ago:     {stale_30:>5}")
    print(f"Scored >90d ago:     {stale_90:>5}")
    print(f"Cash available:      {cash_currency} {cash_amount:,.0f}")
    print()

    print("Pipeline Status Breakdown (long):")
    for status in ("UNSCREENED", "SCORED", "R1_COMPLETE", "R2_COMPLETE", "R3_COMPLETE", "APPROVED", "STANDING_ORDER", "REJECTED"):
        count = status_counts.get(status, 0)
        if count > 0:
            print(f"  {status:<20} {count:>3}")

    if not status_counts:
        print("  (no companies)")

    # Short pipeline summary
    if short_companies:
        print()
        print("Fragility Pipeline (short):")
        short_status_counts = {}
        for c in short_companies:
            s = c.get("pipeline_status", "UNKNOWN")
            short_status_counts[s] = short_status_counts.get(s, 0) + 1
        for status, count in sorted(short_status_counts.items()):
            print(f"  {status:<20} {count:>3}")
        print(f"  Short candidates by sector:")
        short_sectors = {}
        for c in short_companies:
            s = c.get("sector", "Unknown")
            short_sectors[s] = short_sectors.get(s, 0) + 1
        for s, count in sorted(short_sectors.items(), key=lambda x: -x[1]):
            print(f"    {s}: {count}")

    print("\n[Raw data. Reason from principles.md]")


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _batch_refresh(companies, verbose=False, batch_size=5, delay=1.0):
    """Fetch prices for a list of companies, in batches with rate limit spacing."""
    today = str(date.today())

    for i in range(0, len(companies), batch_size):
        batch = companies[i : i + batch_size]

        for c in batch:
            ticker = c["ticker"]
            direction = _get_direction(c)
            try:
                price, api_currency, name = fetch_price(ticker)
                target_currency = c.get("currency", "USD")
                native_price = price_in_native(price, api_currency, target_currency)

                c["current_price"] = round(native_price, 2) if native_price is not None else None
                c["last_price_check"] = today

                # Update name if we got a better one
                if name and (not c.get("name") or c["name"] == ticker):
                    c["name"] = name

                # Calculate distance to entry (direction-aware)
                entry = c.get("entry_price")
                if native_price is not None and entry and entry > 0:
                    c["distance_to_entry"] = _calc_distance_to_entry(native_price, entry, direction)
                else:
                    c["distance_to_entry"] = None

                if verbose:
                    dist = c.get("distance_to_entry")
                    dist_str = f"{dist:+.1f}%" if dist is not None else "N/A"
                    cur = c.get("currency", "USD")
                    dir_label = " [S]" if direction == "short" else ""
                    print(f"  {ticker:<10} {fmt_price(native_price, cur):>10} (entry {fmt_price(entry, cur):>10}) dist: {dist_str}{dir_label}")

            except Exception as e:
                c["current_price"] = None
                c["distance_to_entry"] = None
                c["last_price_check"] = today
                if verbose:
                    print(f"  {ticker:<10} ERROR: {e}")

        # Rate limit spacing between batches
        if i + batch_size < len(companies):
            time.sleep(delay)


def _print_pipeline_health(companies):
    """Print a compact pipeline health summary."""
    # Filter to only the direction that was passed in (already filtered by caller)
    r1_plus = sum(1 for c in companies if c.get("pipeline_status", "") in ("R1_COMPLETE", "R2_COMPLETE", "R3_COMPLETE", "APPROVED", "STANDING_ORDER"))
    approved = sum(1 for c in companies if c.get("pipeline_status", "") in ("APPROVED", "STANDING_ORDER"))

    # Standing orders from standing_orders.yaml
    standing_orders_count = 0
    so_path = os.path.join(PROJECT_ROOT, "state", "standing_orders.yaml")
    if os.path.exists(so_path):
        try:
            with open(so_path, "r") as f:
                so_data = yaml.safe_load(f) or {}
            so = so_data.get("standing_orders", [])
            if so:
                standing_orders_count = len(so)
        except Exception:
            pass

    sectors = len(set(c.get("sector", "Unknown") for c in companies))
    actionable = sum(1 for c in companies if _is_actionable_entry(c))

    print("Pipeline Health:")
    print(f"  R1+ thesis: {r1_plus}  |  Approved: {approved}  |  Standing orders: {standing_orders_count}")
    print(f"  Sectors covered: {sectors}  |  Actionable now: {actionable}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Quality Universe Tool - Capital Deployment Machine pipeline database.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Commands:
  report      Full universe with current prices and distance to entry
  actionable  Only companies within 15%% of entry price
  add         Add or update a company
  remove      Remove a company
  coverage    Sector coverage analysis
  refresh     Update prices for all companies (batch)
  stats       Pipeline health metrics

Flags:
  --fragility   (report, actionable) Show short/fragility candidates only
  --direction   (add) Set direction: long (default) or short
"""
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # report
    report_parser = subparsers.add_parser("report", help="Full universe report")
    report_parser.add_argument("--fragility", action="store_true", default=False, help="Show short/fragility candidates only")

    # actionable
    actionable_parser = subparsers.add_parser("actionable", help="Companies within actionable range of entry price")
    actionable_parser.add_argument("--fragility", action="store_true", default=False, help="Show short/fragility candidates only")

    # add
    add_parser = subparsers.add_parser("add", help="Add or update a company")
    add_parser.add_argument("ticker", help="Ticker symbol")
    add_parser.add_argument("--qs", type=int, required=True, help="Quality Score (tool)")
    add_parser.add_argument("--qs-adj", type=int, default=None, help="Quality Score (adjusted, defaults to --qs)")
    add_parser.add_argument("--fv", type=float, required=True, help="Fair value in native currency (for shorts: TRUE value price converges to)")
    add_parser.add_argument("--entry", type=float, required=True, help="Entry price (for longs: buy at/below; for shorts: short at/above)")
    add_parser.add_argument("--sector", type=str, required=True, help="Sector name")
    add_parser.add_argument("--tier", type=str, required=True, choices=["A", "B", "C"], help="Quality tier")
    add_parser.add_argument("--currency", type=str, default="USD", help="Currency (USD, EUR, GBp)")
    add_parser.add_argument("--direction", type=str, default="long", choices=["long", "short"], help="Direction: long (default) or short (fragility)")
    add_parser.add_argument("--pipeline", type=str, default=None, help="Pipeline status (SCORED, R1_COMPLETE, APPROVED, etc.)")
    add_parser.add_argument("--thesis", type=str, default=None, help="Path to thesis file")
    add_parser.add_argument("--name", type=str, default=None, help="Company name (auto-fetched if omitted)")
    add_parser.add_argument("--notes", type=str, default=None, help="Notes")

    # remove
    remove_parser = subparsers.add_parser("remove", help="Remove a company")
    remove_parser.add_argument("ticker", help="Ticker symbol to remove")

    # coverage
    subparsers.add_parser("coverage", help="Sector coverage analysis")

    # refresh
    subparsers.add_parser("refresh", help="Refresh prices for all companies")

    # stale
    subparsers.add_parser("stale", help="Companies needing re-evaluation (by days since last scored)")

    # stats
    subparsers.add_parser("stats", help="Pipeline health metrics (raw data)")

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        sys.exit(1)

    cmd_map = {
        "report": cmd_report,
        "actionable": cmd_actionable,
        "add": cmd_add,
        "remove": cmd_remove,
        "coverage": cmd_coverage,
        "refresh": cmd_refresh,
        "stale": cmd_stale,
        "stats": cmd_stats,
    }

    cmd_map[args.command](args)


if __name__ == "__main__":
    main()
