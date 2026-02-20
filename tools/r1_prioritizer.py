#!/usr/bin/env python3
"""
R1 Prioritizer — Ranks SCORED companies for R1 fundamental analysis.

Reads quality_universe.yaml, filters SCORED entries, ranks by quality and
proximity to entry, and flags earnings gates. Designed to be the first
step in Fase 2.7 R1 processing each session.

When R1_COMPLETE count >= 20 in the universe, auto-filters to distance_to_entry
<= 25% (near-entry focus). Use --include-far to override.

Shows E[CAGR] column for companies with FV + entry_price defined:
  E[CAGR] = (FV/entry)^(1/3) - 1 + dividend_yield

Usage:
  python3 tools/r1_prioritizer.py                  # Top 10 candidates
  python3 tools/r1_prioritizer.py --top 20          # Top 20
  python3 tools/r1_prioritizer.py --exclude-uk      # Skip UK #5 risk
  python3 tools/r1_prioritizer.py --near-entry-only  # Only <20% from entry (forced)
  python3 tools/r1_prioritizer.py --include-far      # Override auto near-entry filter
  python3 tools/r1_prioritizer.py --tier-a-only      # Only QS >= 75
  python3 tools/r1_prioritizer.py --no-ecagr         # Skip E[CAGR] (no yfinance calls)
"""

import sys
import os
import argparse
from datetime import date, datetime, timedelta

import yaml

import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
UNIVERSE_PATH = os.path.join(PROJECT_ROOT, "state", "quality_universe.yaml")
CALENDAR_PATH = os.path.join(PROJECT_ROOT, "state", "calendar.yaml")
SECTORS_DIR = os.path.join(PROJECT_ROOT, "world", "sectors")
CONTINUITY_PATH = os.path.join(PROJECT_ROOT, "state", "session_continuity.yaml")

# Tickers known to NOT be available on eToro (verified manually)
ETORO_UNAVAILABLE = {
    "MEGP.L",   # ME Group, not on eToro
    "LAGR-B.ST",  # Lagercrantz, not on eToro
    "STF.PA",   # STEF, not on eToro
}

# UK tickers: .L suffix. Already 5 UK positions = concentration risk
UK_SUFFIX = ".L"


def load_universe():
    if not os.path.exists(UNIVERSE_PATH):
        return []
    with open(UNIVERSE_PATH, "r") as f:
        data = yaml.safe_load(f) or {}
    return data.get("quality_universe", {}).get("companies", [])


def load_earnings_tickers(days_ahead=30):
    """Load tickers with earnings in next N days from calendar.yaml."""
    if not os.path.exists(CALENDAR_PATH):
        return {}
    with open(CALENDAR_PATH, "r") as f:
        data = yaml.safe_load(f) or {}

    today = date.today()
    cutoff = today + timedelta(days=days_ahead)
    earnings = {}

    for event in data.get("events", []):
        event_date = event.get("date")
        event_type = event.get("type", "")
        ticker = event.get("ticker", "")

        if not event_date or not ticker:
            continue

        # Parse date
        if isinstance(event_date, date):
            d = event_date
        else:
            try:
                d = datetime.strptime(str(event_date), "%Y-%m-%d").date()
            except (ValueError, TypeError):
                continue

        if today <= d <= cutoff and "earnings" in event_type.lower():
            earnings[ticker] = d

    return earnings


def get_stale_sector_views():
    """Self-contained: parse sector view dates, return dict of filename -> age_days.

    Only includes views with age > 14 days (BORDERLINE+). Also tracks which
    sector labels map to which files for flagging universe companies.
    """
    if not os.path.isdir(SECTORS_DIR):
        return {}, {}

    today = date.today()
    stale = {}  # filename -> age_days

    for f in os.listdir(SECTORS_DIR):
        if not f.endswith(".md") or f == "_TEMPLATE.md":
            continue
        filepath = os.path.join(SECTORS_DIR, f)
        try:
            with open(filepath, "r") as fh:
                header = "".join(fh.readline() for _ in range(10))
        except (OSError, IOError):
            continue
        m = re.search(
            r"(?:Ultima actualizacion|Last Updated|Creado|Updated):\s*(\d{4}-\d{2}-\d{2})",
            header, re.IGNORECASE,
        )
        if m:
            try:
                d = datetime.strptime(m.group(1), "%Y-%m-%d").date()
                age = (today - d).days
                if age > 14:
                    stale[f] = age
            except ValueError:
                pass

    return stale


# Lightweight sector label -> file mapping for stale-sector flagging
_SECTOR_TO_FILE = {
    "Technology": "technology", "Enterprise Software": "technology",
    "Financial Technology": "technology", "Software": "technology",
    "IT Services": "technology", "SaaS": "technology",
    "Health IT/SaaS": "technology", "Software/IT": "technology",
    "Software/ERP": "technology", "Tech/Software": "technology",
    "Industrials": "industrials", "Industrial Conglomerate": "industrials",
    "Specialty Industrial": "industrials", "Basic Materials": "industrials",
    "Specialty Chemicals": "industrials", "specialty-chemicals": "industrials",
    "Industrial Distribution": "industrials",
    "Industrial Equipment / Crane & Lifting": "industrials",
    "Industrial Gases": "industrials", "Industrials/Tools": "industrials",
    "Environmental Services/Facility": "industrials",
    "Testing/Inspection": "testing-inspection-certification",
    "Testing & Inspection": "testing-inspection-certification",
    "Testing/Inspection/Cert": "testing-inspection-certification",
    "Industrial Technology": "industrial-technology",
    "industrial-technology": "industrial-technology",
    "Safety/Environment": "industrial-technology",
    "Measurement/Instruments": "industrial-technology",
    "Scientific Instruments": "industrial-technology",
    "Industrial Automation": "industrial-technology",
    "Building Materials": "building-materials-cement",
    "Cement": "building-materials-cement",
    "Building Materials/Cement": "building-materials-cement",
    "building-products": "building-materials-cement",
    "Pharma": "pharma-healthcare", "Pharmaceuticals": "pharma-healthcare",
    "Healthcare": "pharma-healthcare", "Biotech": "pharma-healthcare",
    "Pharma/Biotech": "pharma-healthcare", "Pharma/Diagnostics": "pharma-healthcare",
    "Pharma/Oncology": "pharma-healthcare", "Pharma/Specialty": "pharma-healthcare",
    "Animal Health": "pharma-healthcare",
    "Healthcare Equipment": "healthcare-equipment",
    "Medical Devices": "healthcare-equipment",
    "Healthcare/Dental": "healthcare-equipment", "Healthcare/MedTech": "healthcare-equipment",
    "Consumer Discretionary": "consumer-discretionary",
    "Consumer Cyclical": "consumer-discretionary",
    "Retail": "consumer-discretionary", "fast-fashion-retail": "consumer-discretionary",
    "Consumer Staples": "consumer-staples", "Consumer Defensive": "consumer-staples",
    "Food & Beverage": "consumer-staples", "Household Products": "consumer-staples",
    "Beverages": "consumer-staples", "Personal Care": "consumer-staples",
    "Luxury": "luxury-goods", "Luxury Goods": "luxury-goods",
    "Insurance": "insurance", "Insurance Broker": "insurance",
    "Insurance/Broker": "insurance", "Insurance (Broker)": "insurance",
    "Insurance Data": "insurance", "Insurance/Specialty": "insurance",
    "Insurance/Specialty P&C": "insurance", "Insurance/Personal Auto": "insurance",
    "specialty-insurance": "insurance",
    "Asset Management": "asset-management",
    "Alternative Asset Management": "asset-management",
    "Financial Services": "asset-management", "asset-management": "asset-management",
    "Financial Data": "financial-data-analytics",
    "Financial Data & Analytics": "financial-data-analytics",
    "Data & Analytics": "financial-data-analytics",
    "Financial Data/Indices": "financial-data-analytics",
    "Information Services": "financial-data-analytics",
    "Research/Advisory": "financial-data-analytics",
    "Business Services": "business-services",
    "Professional Services": "business-services",
    "Pest Control/Business Services": "business-services",
    "HR/Payroll": "hr-payroll-processing",
    "HR & Payroll": "hr-payroll-processing",
    "HR/Payroll Services": "hr-payroll-processing",
    "Payments": "payments-fintech", "Payments/Fintech": "payments-fintech",
    "payments-fintech": "payments-fintech",
    "Digital Marketplaces": "digital-marketplaces",
    "Online Classifieds": "digital-marketplaces",
    "Communication Services": "telecom",
    "Media": "media-publishing", "Media/Publishing": "media-publishing",
    "Telecom": "telecom", "Telecommunications": "telecom",
    "Utilities": "utilities", "Energy": "energy", "Oil & Gas": "energy",
    "Real Estate": "real-estate", "REITs": "real-estate",
    "Property/REIT": "real-estate", "REIT": "real-estate",
    "Defense": "defense-aerospace", "Aerospace & Defense": "defense-aerospace",
    "Defense & Aerospace": "defense-aerospace", "Defense/Aerospace": "defense-aerospace",
    "defense-aerospace": "defense-aerospace",
    "Automotive": "automotive",
    "Self-Service/Vending": "self-service-vending", "Self-Service Vending": "self-service-vending",
    "Vending": "self-service-vending",
    "Environmental/Water": "environmental-water", "Water": "environmental-water",
    "Environmental Services": "environmental-water",
    "Water Treatment/Chemicals": "environmental-water",
    "Waste Management": "environmental-water",
    "Semiconductors": "semiconductors-equipment",
    "Semiconductor Equipment": "semiconductors-equipment",
    "Semiconductors/Equipment": "semiconductors-equipment",
    "Semiconductors/Power": "semiconductors-equipment",
    "Tech/Semiconductor": "semiconductors-equipment",
    "Live Entertainment": "live-entertainment", "Ticketing": "live-entertainment",
    "Security/Access Control": "security-access-control",
    "Shipping": "shipping-services", "shipping-services": "shipping-services",
    "LTL Logistics": "shipping-services", "Transportation": "shipping-services",
    "Commercial Kitchen": "commercial-kitchen-equipment",
    "commercial-kitchen-equipment": "commercial-kitchen-equipment",
    "UK Adviser Platforms": "uk-adviser-platforms",
    "financial-services": "asset-management",
}


def load_cooldowns():
    """Load R1 cooldowns from session_continuity.yaml.

    Returns dict of ticker -> cooldown entry for active (non-expired) cooldowns.
    """
    if not os.path.exists(CONTINUITY_PATH):
        return {}
    try:
        with open(CONTINUITY_PATH, "r") as f:
            data = yaml.safe_load(f) or {}
    except Exception:
        return {}

    today = date.today()
    cooldowns = {}
    for entry in data.get("r1_cooldowns", []):
        ticker = entry.get("ticker", "")
        cooldown_until = entry.get("cooldown_until", "")
        if not ticker or not cooldown_until:
            continue
        try:
            cd_date = datetime.strptime(str(cooldown_until), "%Y-%m-%d").date()
            if cd_date > today:
                cooldowns[ticker] = entry
        except (ValueError, TypeError):
            continue
    return cooldowns


def count_r1_complete(companies):
    """Count R1_COMPLETE long companies in universe (for auto-filter threshold)."""
    return sum(
        1 for c in companies
        if c.get("pipeline_status") == "R1_COMPLETE"
        and c.get("direction", "long") == "long"
    )


def get_dividend_yields(tickers):
    """Batch-fetch dividend yields from yfinance for E[CAGR] calculation.

    Returns dict of ticker -> dividend_yield_pct (e.g., 2.5 for 2.5%).
    Only fetches for tickers that have both fair_value and entry_price.
    Gracefully handles failures.
    """
    import warnings
    warnings.filterwarnings('ignore')

    yields = {}
    if not tickers:
        return yields

    try:
        import yfinance as yf
    except ImportError:
        return yields

    # Map tickers that have different yfinance symbols
    TICKER_MAP = {'LIGHT.NV': 'LIGHT.AS'}

    for ticker in tickers:
        yf_ticker = TICKER_MAP.get(ticker, ticker)
        try:
            info = yf.Ticker(yf_ticker).info
            dy = info.get('dividendYield')
            if dy is not None and isinstance(dy, (int, float)) and dy >= 0:
                # yfinance dividendYield is already percentage (e.g., 2.97 = 2.97%)
                yields[ticker] = dy
            else:
                yields[ticker] = 0.0
        except Exception:
            yields[ticker] = 0.0

    return yields


def compute_ecagr(fair_value, entry_price, div_yield_pct):
    """Compute E[CAGR] = (FV/entry)^(1/3) - 1 + dividend_yield.

    Args:
        fair_value: Fair value in native currency
        entry_price: Entry price in native currency
        div_yield_pct: Dividend yield as percentage (e.g., 2.5 for 2.5%)

    Returns:
        E[CAGR] as percentage (e.g., 14.5 for 14.5%), or None if inputs invalid.
    """
    if not fair_value or not entry_price or entry_price <= 0 or fair_value <= 0:
        return None

    # MoS convergence component: (FV/entry)^(1/3) - 1
    ratio = fair_value / entry_price
    mos_cagr = (ratio ** (1.0 / 3.0)) - 1.0

    # Add dividend yield (convert from pct to decimal, then back to pct)
    div_decimal = (div_yield_pct or 0.0) / 100.0
    ecagr = (mos_cagr + div_decimal) * 100.0

    return ecagr


def rank_candidates(companies, args, auto_near_entry_applied=False):
    """Filter and rank SCORED companies for R1 processing."""
    # Filter: only SCORED, only long direction
    scored = [
        c for c in companies
        if c.get("pipeline_status") == "SCORED"
        and c.get("direction", "long") == "long"
    ]

    # Optional filters
    if args.exclude_uk:
        scored = [c for c in scored if not c["ticker"].endswith(UK_SUFFIX)]

    # Near-entry filtering (manual --near-entry-only OR auto-applied)
    if args.near_entry_only:
        scored = [
            c for c in scored
            if c.get("distance_to_entry") is not None
            and c["distance_to_entry"] <= 20.0
        ]
    elif auto_near_entry_applied and not args.include_far:
        scored = [
            c for c in scored
            if c.get("distance_to_entry") is not None
            and c["distance_to_entry"] <= 25.0
        ]

    if args.tier_a_only:
        scored = [c for c in scored if c.get("tier") == "A"]

    # Cooldown filtering (skip recently-analyzed tickers unless price dropped >15%)
    cooled_entries = []
    if not args.ignore_cooldowns:
        cooldowns = load_cooldowns()
        filtered = []
        for c in scored:
            if c["ticker"] in cooldowns:
                cd = cooldowns[c["ticker"]]
                current = c.get("current_price") or c.get("distance_to_entry")
                analysis_price = cd.get("price_at_analysis", 0)
                # Override: if price dropped >15% since analysis, re-enable
                if analysis_price and current and c.get("current_price"):
                    drop = (analysis_price - c["current_price"]) / analysis_price
                    if drop >= 0.15:
                        c["_cooldown_override"] = True
                        filtered.append(c)
                        continue
                cooled_entries.append(cd)
            else:
                filtered.append(c)
        scored = filtered

    # Sort by composite priority:
    # 1. QS adjusted (desc) -- quality first
    # 2. Distance to entry (asc) -- closer to buy = higher priority
    # 3. Non-UK bonus (UK companies rank slightly lower due to concentration)
    def sort_key(c):
        qs = c.get("qs_adj") or c.get("qs_tool") or 0
        dist = c.get("distance_to_entry")
        dist_val = dist if dist is not None else 999

        # UK penalty: +50 to distance for sorting purposes
        uk_penalty = 50 if c["ticker"].endswith(UK_SUFFIX) else 0

        # Primary: QS descending (negate), Secondary: distance ascending
        return (-qs, dist_val + uk_penalty)

    scored.sort(key=sort_key)

    # Store cooled entries for footer display
    args._cooled_entries = cooled_entries

    return scored[:args.top]


def show_advancement_pipeline(companies):
    """Show R1_COMPLETE candidates with ACTIONABLE verdict needing R2+ advancement."""
    r1_complete = [
        c for c in companies
        if c.get("pipeline_status") == "R1_COMPLETE"
        and c.get("direction", "long") == "long"
    ]

    if not r1_complete:
        print("\nNo R1_COMPLETE candidates in universe.")
        return

    # Separate by R1 verdict
    actionable = [c for c in r1_complete if c.get("r1_verdict") in ("ACTIONABLE", "NEAR_ENTRY", "WATCHLIST")]
    non_actionable = [c for c in r1_complete if c not in actionable]

    # Check which ones already have R2/R3 completed (from session_continuity)
    continuity_r2 = set()
    continuity_r3 = set()
    if os.path.exists(CONTINUITY_PATH):
        try:
            with open(CONTINUITY_PATH, "r") as f:
                cont = yaml.safe_load(f) or {}
            completed = cont.get("completed", {})
            for item in completed.get("r2_completed", []):
                continuity_r2.add(item.get("ticker", ""))
            for item in completed.get("r3_completed", []):
                continuity_r3.add(item.get("ticker", ""))
        except Exception:
            pass

    today = date.today()
    print(f"\n=== R2 ADVANCEMENT PIPELINE | {today} ===")
    print(f"R1_COMPLETE total: {len(r1_complete)} | ACTIONABLE: {len(actionable)}")
    print("=" * 100)

    if actionable:
        print(f"\n{'#':>2} {'Ticker':<14} {'QS':>3} {'Tier':>4} {'Sector':<22} {'Dist%':>7} {'R1 Verdict':<14} {'Status'}")
        print("-" * 100)

        # Sort by QS descending, then distance ascending
        actionable.sort(key=lambda c: (-(c.get("qs_adj") or c.get("qs_tool") or 0), c.get("distance_to_entry") or 999))

        for i, c in enumerate(actionable, 1):
            qs = c.get("qs_adj") or c.get("qs_tool") or "?"
            tier = c.get("tier", "?")
            sector = (c.get("sector") or "Unknown")[:22]
            dist = c.get("distance_to_entry")
            dist_str = f"{dist:+.1f}%" if dist is not None else "N/A"
            verdict = c.get("r1_verdict", "?")
            ticker = c["ticker"]

            # Determine advancement status
            if ticker in continuity_r3:
                status = "R3 DONE -- needs R4"
            elif ticker in continuity_r2:
                status = "R2 DONE -- needs R3"
            else:
                status = "NO R2 -- ready for advancement"

            # Add gate info if present
            gate = c.get("gate") or c.get("pre_execution_condition") or ""
            if gate:
                status += f" (GATE: {gate[:40]})"

            print(f"{i:>2} {ticker:<14} {qs:>3} {tier:>4} {sector:<22} {dist_str:>7} {verdict:<14} {status}")

        print("-" * 100)

    if non_actionable:
        print(f"\nNON-ACTIONABLE R1_COMPLETE ({len(non_actionable)}):")
        for c in non_actionable[:5]:
            qs = c.get("qs_adj") or c.get("qs_tool") or "?"
            verdict = c.get("r1_verdict", "?")
            print(f"  {c['ticker']:<14} QS {qs:>3}  {verdict}")
        if len(non_actionable) > 5:
            print(f"  ... and {len(non_actionable) - 5} more")

    print(f"\n[Pipeline velocity: 1 R1 = 1 unit, 1 R2->R3 = 2 units, 1 R4 = 1 unit. Target: 3+ units/session]")


def main():
    parser = argparse.ArgumentParser(description="R1 Prioritizer -- Rank SCORED companies for R1 analysis")
    parser.add_argument("--top", type=int, default=10, help="Number of candidates to show (default: 10)")
    parser.add_argument("--exclude-uk", action="store_true", help="Exclude UK tickers (.L)")
    parser.add_argument("--near-entry-only", action="store_true", help="Only show companies within 20%% of entry (forced)")
    parser.add_argument("--include-far", action="store_true", help="Override auto near-entry filter (show all distances)")
    parser.add_argument("--tier-a-only", action="store_true", help="Only show Tier A (QS >= 75)")
    parser.add_argument("--ignore-cooldowns", action="store_true", help="Bypass R1 cooldowns (show all including recently analyzed)")
    parser.add_argument("--advancement", action="store_true", help="Show R1_COMPLETE ACTIONABLE candidates needing R2 advancement")
    parser.add_argument("--no-ecagr", action="store_true", help="Skip E[CAGR] calculation (avoids yfinance calls)")
    args = parser.parse_args()
    args._cooled_entries = []  # populated by rank_candidates

    companies = load_universe()
    if not companies:
        print("Quality Universe is empty.")
        sys.exit(1)

    # --advancement mode: show R1_COMPLETE ACTIONABLE candidates without R2
    if args.advancement:
        show_advancement_pipeline(companies)
        sys.exit(0)

    # Count totals
    all_scored = [c for c in companies if c.get("pipeline_status") == "SCORED" and c.get("direction", "long") == "long"]
    total_universe = len([c for c in companies if c.get("direction", "long") == "long"])

    # Auto near-entry filter: when R1_COMPLETE count >= 20, focus on near-entry
    r1_complete_count = count_r1_complete(companies)
    auto_near_entry_applied = False
    if r1_complete_count >= 20 and not args.near_entry_only and not args.include_far:
        auto_near_entry_applied = True

    # Load earnings calendar + stale sector views
    earnings = load_earnings_tickers(30)
    stale_sectors = get_stale_sector_views()

    # Rank
    candidates = rank_candidates(companies, args, auto_near_entry_applied)

    if not candidates:
        msg = f"\nNo SCORED candidates match filters. Total SCORED: {len(all_scored)}/{total_universe}"
        if auto_near_entry_applied:
            msg += "\n  Auto-filter applied (R1_COMPLETE >= 20, distance <= 25%). Use --include-far to see all."
        print(msg)
        sys.exit(0)

    # E[CAGR] computation (only when not --no-ecagr)
    ecagr_map = {}  # ticker -> ecagr_pct
    if not args.no_ecagr:
        # Collect tickers that need E[CAGR] (have both FV and entry_price)
        ecagr_tickers = []
        for c in candidates:
            fv = c.get("fair_value")
            ep = c.get("entry_price")
            if fv and ep and fv > 0 and ep > 0:
                ecagr_tickers.append(c["ticker"])

        # Batch-fetch dividend yields for E[CAGR] calculation
        div_yields = {}
        if ecagr_tickers:
            print(f"Fetching dividend yields for {len(ecagr_tickers)} tickers...")
            div_yields = get_dividend_yields(ecagr_tickers)

        # Compute E[CAGR] for each candidate
        for c in candidates:
            ticker = c["ticker"]
            fv = c.get("fair_value")
            ep = c.get("entry_price")
            if fv and ep and fv > 0 and ep > 0:
                dy = div_yields.get(ticker, 0.0)
                ecagr = compute_ecagr(fv, ep, dy)
                if ecagr is not None:
                    ecagr_map[ticker] = ecagr

    # Determine if we show E[CAGR] column (at least one computed)
    show_ecagr = len(ecagr_map) > 0

    # Print header
    today = date.today()
    print(f"\nR1 PRIORITY QUEUE | {today}")
    print(f"SCORED: {len(all_scored)}/{total_universe} long companies need R1")

    if auto_near_entry_applied:
        print(f"Auto-filtered to near-entry (R1_COMPLETE >= 20, dist <= 25%). Use --include-far to see all.")

    col_width = 130 if show_ecagr else 120
    print("=" * col_width)

    if show_ecagr:
        print(f"{'#':>2} {'Ticker':<12} {'QS':>3} {'Tier':>4} {'Sector':<24} {'Dist%':>7} {'E[CAGR]':>8} {'Currency':>8} {'Flags'}")
    else:
        print(f"{'#':>2} {'Ticker':<12} {'QS':>3} {'Tier':>4} {'Sector':<24} {'Dist%':>7} {'Currency':>8} {'Flags'}")
    print("-" * col_width)

    for i, c in enumerate(candidates, 1):
        qs = c.get("qs_adj") or c.get("qs_tool") or "?"
        tier = c.get("tier", "?")
        sector = (c.get("sector") or "Unknown")[:24]
        dist = c.get("distance_to_entry")
        dist_str = f"{dist:+.1f}%" if dist is not None else "N/A"
        currency = c.get("currency", "USD")

        # E[CAGR] string
        ecagr_val = ecagr_map.get(c["ticker"])
        ecagr_str = f"{ecagr_val:.1f}%" if ecagr_val is not None else "-"

        # Build flags
        flags = []

        # eToro availability
        if c["ticker"] in ETORO_UNAVAILABLE:
            flags.append("NO-ETORO")

        # UK concentration warning
        if c["ticker"].endswith(UK_SUFFIX):
            flags.append("UK#5")

        # Earnings gate
        if c["ticker"] in earnings:
            earn_date = earnings[c["ticker"]]
            flags.append(f"EARNINGS {earn_date.strftime('%b %d')}")

        # Near entry highlight
        if dist is not None and dist <= 15.0:
            flags.append("NEAR-ENTRY")

        # Stale score warning
        last_scored = c.get("last_scored")
        if last_scored:
            try:
                scored_date = datetime.strptime(str(last_scored), "%Y-%m-%d").date()
                days_stale = (today - scored_date).days
                if days_stale > 90:
                    flags.append(f"STALE({days_stale}d)")
            except (ValueError, TypeError):
                pass

        # Stale sector view warning
        sector_label = c.get("sector", "")
        sector_file = _SECTOR_TO_FILE.get(sector_label)
        if sector_file:
            sf_name = sector_file + ".md"
            if sf_name in stale_sectors:
                flags.append(f"STALE-SECTOR({stale_sectors[sf_name]}d)")
        elif sector_label:
            # No mapping found -- might be missing sector view
            expected = sector_label.lower().replace("/", "-").replace(" ", "-") + ".md"
            sector_files = set(os.listdir(SECTORS_DIR)) if os.path.isdir(SECTORS_DIR) else set()
            if expected not in sector_files:
                flags.append("NO-SECTOR-VIEW")

        flags_str = " | ".join(flags) if flags else ""

        if show_ecagr:
            print(f"{i:>2} {c['ticker']:<12} {qs:>3} {tier:>4} {sector:<24} {dist_str:>7} {ecagr_str:>8} {currency:>8}  {flags_str}")
        else:
            print(f"{i:>2} {c['ticker']:<12} {qs:>3} {tier:>4} {sector:<24} {dist_str:>7} {currency:>8}  {flags_str}")

    # Summary
    print("-" * col_width)
    print(f"Showing {len(candidates)}/{len(all_scored)} SCORED candidates")

    # Tier breakdown of all scored
    tier_a_scored = sum(1 for c in all_scored if c.get("tier") == "A")
    tier_b_scored = sum(1 for c in all_scored if c.get("tier") == "B")
    near_entry_scored = sum(1 for c in all_scored if c.get("distance_to_entry") is not None and c["distance_to_entry"] <= 20.0)
    uk_scored = sum(1 for c in all_scored if c["ticker"].endswith(UK_SUFFIX))

    print(f"\nAll SCORED breakdown:")
    print(f"  Tier A: {tier_a_scored} | Tier B: {tier_b_scored} | Near entry (<20%%): {near_entry_scored} | UK: {uk_scored}")
    print(f"  R1_COMPLETE in universe: {r1_complete_count}")

    if show_ecagr:
        print(f"\nE[CAGR] = (FV/entry)^(1/3) - 1 + div_yield. Threshold: >=12% Tier A, >=15% Tier B.")

    if earnings:
        earning_scored = [t for t in earnings if any(c["ticker"] == t and c.get("pipeline_status") == "SCORED" for c in companies)]
        if earning_scored:
            print(f"  Earnings gate (next 30d): {', '.join(earning_scored)}")

    # Cooldown footer
    cooled = getattr(args, "_cooled_entries", [])
    if cooled:
        print(f"\nCOOLDOWN SKIPPED ({len(cooled)}):")
        for cd in sorted(cooled, key=lambda x: x.get("cooldown_until", "")):
            t = cd.get("ticker", "?")
            v = cd.get("verdict", "?")
            s = cd.get("session", "?")
            cu = cd.get("cooldown_until", "?")
            print(f"  {t:<14} {v:<14} S{s}  cooldown until {cu}")
        print(f"  [Use --ignore-cooldowns to bypass]")

    print(f"\n[Raw data. Select 3-5 for R1 processing this session.]")


if __name__ == "__main__":
    main()
