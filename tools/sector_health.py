#!/usr/bin/env python3
"""
Sector Health — Monitors staleness, coverage, cascades, and macro dependencies
across sector views, portfolio positions, and quality universe.

6 subcommands:
  freshness    — Staleness of all sector views with portfolio/watchlist deps
  coverage     — Map quality universe → sector views, show gaps
  cascade FILE — Show dependency chain for a sector view
  changes      — Detect status changes vs last snapshot
  snapshot     — Save current baseline to sector_health_cache.yaml
  macro-map    — Map macro themes → sector views → portfolio deps

Usage:
  python3 tools/sector_health.py freshness [--stale-only]
  python3 tools/sector_health.py coverage [--unmapped]
  python3 tools/sector_health.py cascade insurance.md [--all]
  python3 tools/sector_health.py changes
  python3 tools/sector_health.py snapshot
  python3 tools/sector_health.py macro-map
"""

import os
import re
import sys
import argparse
from datetime import date, datetime

import yaml

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
SECTORS_DIR = os.path.join(PROJECT_ROOT, "world", "sectors")
UNIVERSE_PATH = os.path.join(PROJECT_ROOT, "state", "quality_universe.yaml")
PORTFOLIO_PATH = os.path.join(PROJECT_ROOT, "portfolio", "current.yaml")
WATCHLIST_PATH = os.path.join(PROJECT_ROOT, "state", "watchlist.yaml")
CACHE_PATH = os.path.join(PROJECT_ROOT, "state", "sector_health_cache.yaml")

# ─── Macro → Sector Mapping ─────────────────────────────────────────────────
MACRO_SECTOR_MAP = {
    "interest_rates": [
        "insurance", "real-estate", "utilities", "telecom",
        "uk-adviser-platforms", "asset-management",
    ],
    "ai_disruption": [
        "technology", "hr-payroll-processing", "business-services",
        "digital-marketplaces", "financial-data-analytics", "media-publishing",
    ],
    "tariffs": [
        "automotive", "auto-eu", "luxury-goods", "industrials",
        "semiconductors-equipment", "building-materials-cement",
    ],
    "climate": [
        "insurance", "real-estate", "utilities",
        "building-materials-cement", "energy",
    ],
    "glp1": [
        "pharma-healthcare", "consumer-staples", "healthcare-equipment",
    ],
    "geopolitical": [
        "energy", "defense-aerospace", "semiconductors-equipment",
        "shipping-services",
    ],
    "currency_dxy": [
        "luxury-goods", "pharma-healthcare", "technology",
    ],
    "consumer_weakness": [
        "consumer-discretionary", "consumer-staples", "luxury-goods",
        "live-entertainment", "self-service-vending",
    ],
}

# ─── Sector label → filename mapping ────────────────────────────────────────
# Maps quality_universe 'sector' field values to sector view filenames (no .md)
# This is the canonical mapping; sector_health_cache.yaml can override/extend
SECTOR_LABEL_TO_FILE = {
    # Technology / Software
    "Technology": "technology",
    "Enterprise Software": "technology",
    "Financial Technology": "technology",
    "Software": "technology",
    "IT Services": "technology",
    "SaaS": "technology",
    # Industrials
    "Industrials": "industrials",
    "Industrial Conglomerate": "industrials",
    "Specialty Industrial": "industrials",
    "Testing/Inspection": "testing-inspection-certification",
    "Testing & Inspection": "testing-inspection-certification",
    "Industrial Technology": "industrial-technology",
    "Building Materials": "building-materials-cement",
    "Cement": "building-materials-cement",
    # Healthcare
    "Pharma": "pharma-healthcare",
    "Pharmaceuticals": "pharma-healthcare",
    "Healthcare": "pharma-healthcare",
    "Biotech": "pharma-healthcare",
    "Healthcare Equipment": "healthcare-equipment",
    "Medical Devices": "healthcare-equipment",
    # Consumer
    "Consumer Discretionary": "consumer-discretionary",
    "Consumer Staples": "consumer-staples",
    "Food & Beverage": "consumer-staples",
    "Luxury": "luxury-goods",
    "Luxury Goods": "luxury-goods",
    "Footwear": "consumer-discretionary",
    # Financial
    "Insurance": "insurance",
    "Insurance Broker": "insurance",
    "Insurance/Broker": "insurance",
    "Asset Management": "asset-management",
    "Alternative Asset Management": "asset-management",
    "Financial Data": "financial-data-analytics",
    "Financial Data & Analytics": "financial-data-analytics",
    "Data & Analytics": "financial-data-analytics",
    # Services
    "Business Services": "business-services",
    "HR/Payroll": "hr-payroll-processing",
    "HR & Payroll": "hr-payroll-processing",
    "Payments": "payments-fintech",
    "Payments/Fintech": "payments-fintech",
    # Digital / Media
    "Digital Marketplaces": "digital-marketplaces",
    "Online Classifieds": "digital-marketplaces",
    "Media": "media-publishing",
    "Media/Publishing": "media-publishing",
    "Mobile Ad Tech": "mobile-ad-tech",
    # Infrastructure
    "Telecom": "telecom",
    "Telecommunications": "telecom",
    "Utilities": "utilities",
    "Energy": "energy",
    "Oil & Gas": "energy",
    "Real Estate": "real-estate",
    "REITs": "real-estate",
    # Defense / Automotive
    "Defense": "defense-aerospace",
    "Aerospace & Defense": "defense-aerospace",
    "Automotive": "automotive",
    # Specialty
    "Self-Service/Vending": "self-service-vending",
    "Vending": "self-service-vending",
    "Environmental/Water": "environmental-water",
    "Water": "environmental-water",
    "Semiconductors": "semiconductors-equipment",
    "Semiconductor Equipment": "semiconductors-equipment",
    "Live Entertainment": "live-entertainment",
    "Ticketing": "live-entertainment",
    "Security/Access Control": "security-access-control",
    "Shipping": "shipping-services",
    "Commercial Kitchen": "commercial-kitchen-equipment",
    "Promotional Products": "promotional-products",
    "UK Adviser Platforms": "uk-adviser-platforms",
    # yfinance / batch_scorer common labels
    "Communication Services": "telecom",
    "Consumer Cyclical": "consumer-discretionary",
    "Consumer Defensive": "consumer-staples",
    "Basic Materials": "industrials",
    "Defense & Aerospace": "defense-aerospace",
    "Defense/Aerospace": "defense-aerospace",
    "Environmental Services": "environmental-water",
    "Environmental Services/Facility": "industrials",
    "Financial Services": "asset-management",
    "Financial Data/Indices": "financial-data-analytics",
    "HR/Payroll Services": "hr-payroll-processing",
    "Health IT/SaaS": "technology",
    "Healthcare/Dental": "healthcare-equipment",
    "Healthcare/MedTech": "healthcare-equipment",
    "Household Products": "consumer-staples",
    "Industrial Distribution": "industrials",
    "Industrial Equipment / Crane & Lifting": "industrials",
    "Industrial Gases": "industrials",
    "Industrial Gases/Specialty Chemicals": "industrials",
    "Industrial Automation": "industrial-technology",
    "Industrials/Tools": "industrials",
    "Information Services": "financial-data-analytics",
    "Measurement/Instruments": "industrial-technology",
    "Professional Services": "business-services",
    "Property/REIT": "real-estate",
    "REIT": "real-estate",
    "Scientific Instruments": "industrial-technology",
    "Software/IT": "technology",
    "Software/ERP": "technology",
    "Specialty Chemicals": "industrials",
    "Tech/Semiconductor": "semiconductors-equipment",
    "Tech/Software": "technology",
    "Specialty Insurance": "insurance",
    "Transportation": "shipping-services",
    "Waste Management": "environmental-water",
    "Building Materials/Cement": "building-materials-cement",
    "Beverages": "consumer-staples",
    "Animal Health": "pharma-healthcare",
    "Food Products": "consumer-staples",
    "Spirits/Beverages": "consumer-staples",
    # Insurance variants
    "Insurance (Broker)": "insurance",
    "Insurance Data": "insurance",
    "Insurance/Personal Auto": "insurance",
    "Insurance/Specialty": "insurance",
    "Insurance/Specialty P&C": "insurance",
    # Pharma variants
    "Pharma/Biotech": "pharma-healthcare",
    "Pharma/Diagnostics": "pharma-healthcare",
    "Pharma/Oncology": "pharma-healthcare",
    "Pharma/Specialty": "pharma-healthcare",
    "Personal Care": "consumer-staples",
    # Semicondutors variants
    "Semiconductors/Equipment": "semiconductors-equipment",
    "Semiconductors/Power": "semiconductors-equipment",
    # Services
    "LTL Logistics": "shipping-services",
    "Pest Control/Business Services": "business-services",
    "Research/Advisory": "financial-data-analytics",
    "Testing/Inspection/Cert": "testing-inspection-certification",
    "Water Treatment/Chemicals": "environmental-water",
    # Retail
    "Retail": "consumer-discretionary",
    "fast-fashion-retail": "consumer-discretionary",
    # Safety
    "Safety/Environment": "industrial-technology",
    # lowercase labels from universe (added manually)
    "building-products": "building-materials-cement",
    "specialty-chemicals": "industrials",
    "specialty-insurance": "insurance",
    # Catch-alls from universe
    "Hospitality/Hotels": "consumer-discretionary",
    "Specialty Coatings": "industrials",
    "footwear-accessories": "consumer-discretionary",
    "veterinary-diagnostics": "pharma-healthcare",
}


# ═══════════════════════════════════════════════════════════════════════════════
# Helpers
# ═══════════════════════════════════════════════════════════════════════════════

def load_yaml(path):
    if not os.path.exists(path):
        return {}
    with open(path, "r") as f:
        return yaml.safe_load(f) or {}


def save_yaml(path, data):
    with open(path, "w") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


def get_sector_files():
    """Return list of .md files in world/sectors/ excluding _TEMPLATE.md."""
    if not os.path.isdir(SECTORS_DIR):
        return []
    files = sorted(f for f in os.listdir(SECTORS_DIR)
                   if f.endswith(".md") and f != "_TEMPLATE.md")
    return files


def parse_sector_header(filepath):
    """Parse date and status from first 10 lines of a sector view.

    Returns (date_obj or None, status_str or None).
    """
    try:
        with open(filepath, "r") as f:
            lines = [f.readline() for _ in range(10)]
    except (OSError, IOError):
        return None, None

    found_date = None
    found_status = None

    for line in lines:
        if not line:
            continue

        # Date patterns
        # Pattern 1: > Ultima actualizacion: 2026-02-13
        # Pattern 2: > Last Updated: 2026-02-19
        # Pattern 3: > Sector view v1.0 | Creado: 2026-02-06
        date_match = re.search(
            r"(?:Ultima actualizacion|Last Updated|Creado|Updated):\s*(\d{4}-\d{2}-\d{2})",
            line, re.IGNORECASE,
        )
        if date_match and not found_date:
            try:
                found_date = datetime.strptime(date_match.group(1), "%Y-%m-%d").date()
            except ValueError:
                pass

        # Status patterns
        # > Status: **NEUTRAL** or > Status: NEUTRAL
        status_match = re.search(
            r"Status:\s*\**\s*(SOBREPONDERAR|NEUTRAL|INFRAPONDERAR|EVITAR)\s*\**",
            line, re.IGNORECASE,
        )
        if status_match and not found_status:
            found_status = status_match.group(1).upper()

    return found_date, found_status


def classify_age(days):
    """Classify staleness by age in days."""
    if days <= 7:
        return "FRESH"
    elif days <= 14:
        return "ACCEPTABLE"
    elif days <= 21:
        return "BORDERLINE"
    elif days <= 30:
        return "STALE"
    else:
        return "CRITICAL"


def get_portfolio_tickers():
    """Return dict of ticker → position info from portfolio."""
    data = load_yaml(PORTFOLIO_PATH)
    result = {}
    for pos in data.get("positions", []):
        ticker = pos.get("ticker", "")
        if ticker:
            result[ticker] = {
                "name": pos.get("name", ""),
                "conviction": pos.get("conviction", ""),
            }
    for pos in data.get("short_positions", []):
        ticker = pos.get("ticker", "")
        if ticker:
            result[ticker] = {
                "name": pos.get("name", ""),
                "conviction": pos.get("conviction", ""),
                "short": True,
            }
    return result


def get_watchlist_tickers():
    """Return set of tickers from watchlist (all sections)."""
    data = load_yaml(WATCHLIST_PATH)
    tickers = set()
    for section in ["quality_compounders", "quality_value", "ready_to_buy",
                     "on_watch", "tier_2", "short_candidates"]:
        for item in data.get(section, []) or []:
            t = item.get("ticker", "")
            if t:
                tickers.add(t)
    return tickers


def get_universe_companies():
    """Return list of companies from quality_universe.yaml."""
    data = load_yaml(UNIVERSE_PATH)
    return data.get("quality_universe", {}).get("companies", [])


def get_sector_mappings():
    """Load custom sector mappings from cache, merged with built-in."""
    cache = load_yaml(CACHE_PATH)
    custom = cache.get("sector_health_cache", {}).get("sector_mappings", {})
    merged = dict(SECTOR_LABEL_TO_FILE)
    merged.update(custom)
    return merged


def map_ticker_to_sector_file(ticker, companies, mappings):
    """Given a ticker, find its sector label in universe and map to sector file."""
    for c in companies:
        if c.get("ticker") == ticker:
            label = c.get("sector", "")
            if label in mappings:
                return mappings[label] + ".md"
            # Try case-insensitive partial match
            label_lower = label.lower()
            for key, val in mappings.items():
                if key.lower() == label_lower:
                    return val + ".md"
            return None
    return None


def build_sector_deps():
    """Build sector_file → {portfolio: [...], watchlist: [...]} from data."""
    portfolio = get_portfolio_tickers()
    watchlist = get_watchlist_tickers()
    companies = get_universe_companies()
    mappings = get_sector_mappings()

    deps = {}  # sector_file → { portfolio: [ticker,...], watchlist: [ticker,...] }

    # Portfolio positions
    for ticker in portfolio:
        sf = map_ticker_to_sector_file(ticker, companies, mappings)
        if not sf:
            # Try manual mapping from portfolio sector knowledge
            sf = _guess_sector_file_for_ticker(ticker)
        if sf:
            deps.setdefault(sf, {"portfolio": [], "watchlist": []})
            deps[sf]["portfolio"].append(ticker)

    # Watchlist
    for ticker in watchlist:
        sf = map_ticker_to_sector_file(ticker, companies, mappings)
        if not sf:
            sf = _guess_sector_file_for_ticker(ticker)
        if sf:
            deps.setdefault(sf, {"portfolio": [], "watchlist": []})
            if ticker not in deps[sf].get("portfolio", []):
                deps[sf]["watchlist"].append(ticker)

    return deps


def _guess_sector_file_for_ticker(ticker):
    """Fallback: try to match ticker to sector via known patterns."""
    # Known portfolio mappings that might not be in universe
    known = {
        "DTE.DE": "telecom.md",
        "EDEN.PA": "business-services.md",
        "DOM.L": "consumer-staples.md",
        "GL": "insurance.md",
        "ADBE": "technology.md",
        "NVO": "pharma-healthcare.md",
        "MONY.L": "digital-marketplaces.md",
        "LULU": "consumer-discretionary.md",
        "AUTO.L": "digital-marketplaces.md",
        "BYIT.L": "technology.md",
        "LYV": "live-entertainment.md",
    }
    return known.get(ticker)


# ═══════════════════════════════════════════════════════════════════════════════
# Subcommands
# ═══════════════════════════════════════════════════════════════════════════════

def cmd_freshness(args):
    """Show staleness of all sector views with deps."""
    today = date.today()
    files = get_sector_files()
    deps = build_sector_deps()

    rows = []
    for f in files:
        filepath = os.path.join(SECTORS_DIR, f)
        d, status = parse_sector_header(filepath)
        age = (today - d).days if d else None
        classification = classify_age(age) if age is not None else "NO-DATE"
        dep_info = deps.get(f, {"portfolio": [], "watchlist": []})
        rows.append({
            "file": f,
            "date": d,
            "age": age,
            "class": classification,
            "status": status or "?",
            "portfolio": dep_info["portfolio"],
            "watchlist": dep_info["watchlist"],
        })

    # Sort: CRITICAL first, then STALE, BORDERLINE, etc.
    order = {"CRITICAL": 0, "STALE": 1, "BORDERLINE": 2, "NO-DATE": 3,
             "ACCEPTABLE": 4, "FRESH": 5}
    rows.sort(key=lambda r: (order.get(r["class"], 9), -(r["age"] or 0)))

    if args.stale_only:
        rows = [r for r in rows if r["class"] in ("BORDERLINE", "STALE", "CRITICAL", "NO-DATE")]

    if not rows:
        print("\nAll sector views are FRESH or ACCEPTABLE. No action needed.")
        return

    # Print
    print(f"\nSECTOR VIEW FRESHNESS | {today}")
    print("=" * 130)
    print(f"{'Sector View':<38} {'Date':>10} {'Age':>5} {'Status':<14} {'Class':<12} {'Portfolio Deps':<20} {'Watchlist Deps'}")
    print("-" * 130)

    stale_with_deps = 0
    for r in rows:
        date_str = str(r["date"]) if r["date"] else "N/A"
        age_str = f"{r['age']}d" if r["age"] is not None else "?"
        port_str = ", ".join(r["portfolio"]) if r["portfolio"] else "-"
        watch_str = ", ".join(r["watchlist"][:5]) if r["watchlist"] else "-"
        if len(r["watchlist"]) > 5:
            watch_str += f" +{len(r['watchlist']) - 5}"

        # Highlight stale with portfolio deps
        marker = ""
        if r["class"] in ("BORDERLINE", "STALE", "CRITICAL") and r["portfolio"]:
            marker = " *** PRIORITY"
            stale_with_deps += 1

        print(f"{r['file']:<38} {date_str:>10} {age_str:>5} {r['status']:<14} {r['class']:<12} {port_str:<20} {watch_str}{marker}")

    # Summary
    print("-" * 130)
    total = len(get_sector_files())
    by_class = {}
    for r in rows:
        by_class[r["class"]] = by_class.get(r["class"], 0) + 1
    class_str = " | ".join(f"{k}: {v}" for k, v in sorted(by_class.items(), key=lambda x: order.get(x[0], 9)))

    print(f"\nTotal views: {total} | Showing: {len(rows)} | {class_str}")
    if stale_with_deps:
        print(f"\n*** {stale_with_deps} STALE SECTOR(S) WITH PORTFOLIO DEPENDENCIES — refresh BEFORE R1 processing")
    print(f"\n[Raw data. sector_health.py snapshot to save baseline.]")


def cmd_coverage(args):
    """Map universe companies to sector views, show gaps."""
    companies = get_universe_companies()
    mappings = get_sector_mappings()
    sector_files = set(get_sector_files())

    covered = []    # has sector view
    view_only = []  # sector view exists but no universe company maps to it
    gap = []        # universe company has no sector view
    unmapped = []   # sector label not in mapping table

    seen_files = set()

    for c in companies:
        ticker = c.get("ticker", "")
        label = c.get("sector", "")
        mapped_file = None

        if label in mappings:
            mapped_file = mappings[label] + ".md"
        else:
            # Case-insensitive
            for key, val in mappings.items():
                if key.lower() == label.lower():
                    mapped_file = val + ".md"
                    break

        if mapped_file:
            if mapped_file in sector_files:
                covered.append({"ticker": ticker, "sector": label, "file": mapped_file})
                seen_files.add(mapped_file)
            else:
                gap.append({"ticker": ticker, "sector": label, "expected": mapped_file})
        else:
            unmapped.append({"ticker": ticker, "sector": label})

    # View-only: sector files that no universe company maps to
    for f in sector_files:
        if f not in seen_files:
            view_only.append(f)

    if args.unmapped:
        # Show only unmapped
        if not unmapped:
            print("\nAll universe companies have sector mappings.")
            return
        print(f"\nUNMAPPED COMPANIES ({len(unmapped)}) — sector label not in mapping table")
        print("=" * 80)
        print(f"{'Ticker':<12} {'Sector Label'}")
        print("-" * 80)
        for u in sorted(unmapped, key=lambda x: x["sector"]):
            print(f"{u['ticker']:<12} {u['sector']}")
        print(f"\n[Add mappings to sector_health_cache.yaml → sector_mappings or update SECTOR_LABEL_TO_FILE in tool.]")
        return

    # Full report
    today = date.today()
    print(f"\nSECTOR COVERAGE REPORT | {today}")
    print("=" * 100)
    print(f"COVERED: {len(set(c['file'] for c in covered))} views cover {len(covered)} companies")
    print(f"VIEW ONLY: {len(view_only)} sector views with no universe companies mapped")
    print(f"GAP: {len(gap)} companies mapped to non-existent sector views")
    print(f"UNMAPPED: {len(unmapped)} companies with no sector label mapping")
    print()

    if gap:
        print("--- GAPS (sector view file missing) ---")
        for g in sorted(gap, key=lambda x: x["expected"]):
            print(f"  {g['ticker']:<12} sector='{g['sector']}' → expected {g['expected']}")
        print()

    if unmapped:
        print(f"--- UNMAPPED ({len(unmapped)} — use --unmapped for full list) ---")
        labels = sorted(set(u["sector"] for u in unmapped))
        for label in labels[:10]:
            count = sum(1 for u in unmapped if u["sector"] == label)
            print(f"  '{label}' ({count} companies)")
        if len(labels) > 10:
            print(f"  ... +{len(labels) - 10} more labels")
        print()

    if view_only:
        print("--- VIEW ONLY (no universe companies) ---")
        for v in sorted(view_only):
            print(f"  {v}")
        print()

    # Coverage by sector file
    file_counts = {}
    for c in covered:
        file_counts[c["file"]] = file_counts.get(c["file"], 0) + 1
    if file_counts:
        print("--- COVERAGE BY SECTOR VIEW ---")
        for f, count in sorted(file_counts.items(), key=lambda x: -x[1]):
            print(f"  {f:<38} {count} companies")

    print(f"\n[Raw data. Fix unmapped with sector_health_cache.yaml → sector_mappings.]")


def cmd_cascade(args):
    """Show dependency chain for a sector view."""
    deps = build_sector_deps()
    portfolio = get_portfolio_tickers()
    watchlist = get_watchlist_tickers()

    if args.all:
        # Show all sectors with any deps
        today = date.today()
        print(f"\nCASCADE MAP — ALL SECTORS WITH DEPENDENCIES | {today}")
        print("=" * 110)
        print(f"{'Sector View':<38} {'Age':>5} {'Status':<14} {'Portfolio':<25} {'Watchlist'}")
        print("-" * 110)

        files = get_sector_files()
        for f in sorted(files):
            dep = deps.get(f, {"portfolio": [], "watchlist": []})
            if not dep["portfolio"] and not dep["watchlist"]:
                continue
            filepath = os.path.join(SECTORS_DIR, f)
            d, status = parse_sector_header(filepath)
            age = (today - d).days if d else None
            age_str = f"{age}d" if age is not None else "?"
            port_str = ", ".join(dep["portfolio"]) or "-"
            watch_str = ", ".join(dep["watchlist"][:5]) or "-"
            if len(dep["watchlist"]) > 5:
                watch_str += f" +{len(dep['watchlist']) - 5}"
            print(f"{f:<38} {age_str:>5} {status or '?':<14} {port_str:<25} {watch_str}")

        print(f"\n[Sectors without dependencies not shown.]")
        return

    # Single sector cascade
    sector_file = args.sector_file
    if not sector_file:
        print("Error: specify sector file (e.g., 'insurance.md') or use --all")
        sys.exit(1)

    if not sector_file.endswith(".md"):
        sector_file += ".md"

    filepath = os.path.join(SECTORS_DIR, sector_file)
    if not os.path.exists(filepath):
        print(f"Error: {sector_file} not found in {SECTORS_DIR}")
        sys.exit(1)

    today = date.today()
    d, status = parse_sector_header(filepath)
    age = (today - d).days if d else None
    classification = classify_age(age) if age is not None else "NO-DATE"

    dep = deps.get(sector_file, {"portfolio": [], "watchlist": []})

    print(f"\nCASCADE: {sector_file}")
    print("=" * 80)
    print(f"  Date: {d or 'N/A'}  |  Age: {age}d  |  Status: {status or '?'}  |  Class: {classification}")
    print()

    if dep["portfolio"]:
        print("  PORTFOLIO DEPENDENCIES:")
        for t in dep["portfolio"]:
            info = portfolio.get(t, {})
            print(f"    [{t}] {info.get('name', '')} — conviction: {info.get('conviction', '?')}")
    else:
        print("  PORTFOLIO DEPENDENCIES: None")

    if dep["watchlist"]:
        print(f"\n  WATCHLIST DEPENDENCIES ({len(dep['watchlist'])}):")
        for t in dep["watchlist"]:
            print(f"    [{t}]")
    else:
        print("\n  WATCHLIST DEPENDENCIES: None")

    # Macro themes that affect this sector
    base = sector_file.replace(".md", "")
    affecting_themes = [theme for theme, sectors in MACRO_SECTOR_MAP.items() if base in sectors]
    if affecting_themes:
        print(f"\n  MACRO THEMES AFFECTING THIS SECTOR:")
        for theme in affecting_themes:
            print(f"    - {theme}")

    total_deps = len(dep["portfolio"]) + len(dep["watchlist"])
    if classification in ("BORDERLINE", "STALE", "CRITICAL") and total_deps > 0:
        print(f"\n  *** WARNING: {classification} ({age}d) with {total_deps} dependencies — REFRESH RECOMMENDED")

    print()


def cmd_changes(args):
    """Detect status changes vs last snapshot."""
    cache = load_yaml(CACHE_PATH)
    snapshot = cache.get("sector_health_cache", {}).get("status_snapshot", {})

    if not snapshot:
        print("\nNo snapshot found. Run 'sector_health.py snapshot' first.")
        return

    today = date.today()
    files = get_sector_files()
    deps = build_sector_deps()
    changes = []

    for f in files:
        filepath = os.path.join(SECTORS_DIR, f)
        d, current_status = parse_sector_header(filepath)

        prev = snapshot.get(f, {})
        prev_status = prev.get("status")

        if current_status and prev_status and current_status != prev_status:
            dep = deps.get(f, {"portfolio": [], "watchlist": []})
            total_deps = len(dep["portfolio"]) + len(dep["watchlist"])
            severity = "MATERIAL" if dep["portfolio"] else ("MINOR" if total_deps == 0 else "MINOR+WATCHLIST")
            changes.append({
                "file": f,
                "old": prev_status,
                "new": current_status,
                "severity": severity,
                "portfolio": dep["portfolio"],
                "watchlist": dep["watchlist"],
            })

    if not changes:
        snap_date = cache.get("sector_health_cache", {}).get("last_snapshot", "?")
        print(f"\nNo status changes detected since snapshot ({snap_date}).")
        print(f"[Raw data. {len(files)} sector views checked against {len(snapshot)} snapshot entries.]")
        return

    print(f"\nSTATUS CHANGES DETECTED | {today}")
    print("=" * 100)
    for ch in changes:
        print(f"\n  {ch['file']}: {ch['old']} → {ch['new']}  [{ch['severity']}]")
        if ch["portfolio"]:
            print(f"    Portfolio: {', '.join(ch['portfolio'])} — RE-EVAL NEEDED")
        if ch["watchlist"]:
            print(f"    Watchlist: {', '.join(ch['watchlist'][:5])}")

    material = [ch for ch in changes if ch["severity"] == "MATERIAL"]
    if material:
        print(f"\n*** {len(material)} MATERIAL CHANGE(S) — thesis re-evaluation required for portfolio positions")

    print(f"\n[{len(changes)} change(s) from {len(files)} views. Run snapshot to update baseline.]")


def cmd_snapshot(args):
    """Save current baseline to sector_health_cache.yaml."""
    today = date.today()
    files = get_sector_files()
    deps = build_sector_deps()

    # Load existing cache to preserve sector_mappings
    cache = load_yaml(CACHE_PATH)
    existing = cache.get("sector_health_cache", {})
    custom_mappings = existing.get("sector_mappings", {})

    status_snapshot = {}
    for f in files:
        filepath = os.path.join(SECTORS_DIR, f)
        d, status = parse_sector_header(filepath)
        dep = deps.get(f, {"portfolio": [], "watchlist": []})
        status_snapshot[f] = {
            "status": status or "UNKNOWN",
            "last_updated": str(d) if d else None,
            "dep_count": len(dep["portfolio"]) + len(dep["watchlist"]),
        }

    new_cache = {
        "sector_health_cache": {
            "last_snapshot": str(today),
            "status_snapshot": status_snapshot,
            "sector_mappings": custom_mappings,
        }
    }

    save_yaml(CACHE_PATH, new_cache)
    print(f"\nSnapshot saved: {len(status_snapshot)} sector views → {CACHE_PATH}")
    print(f"Date: {today}")

    # Summary
    by_status = {}
    for info in status_snapshot.values():
        s = info["status"]
        by_status[s] = by_status.get(s, 0) + 1
    for s, count in sorted(by_status.items()):
        print(f"  {s}: {count}")

    total_deps = sum(info["dep_count"] for info in status_snapshot.values())
    print(f"  Total dependencies tracked: {total_deps}")


def cmd_macro_map(args):
    """Map macro themes → sector views → portfolio deps."""
    today = date.today()
    deps = build_sector_deps()
    sector_files = set(get_sector_files())

    print(f"\nMACRO → SECTOR → PORTFOLIO MAP | {today}")
    print("=" * 120)

    for theme, sectors in sorted(MACRO_SECTOR_MAP.items()):
        affected = []
        for sector_base in sectors:
            sf = sector_base + ".md"
            if sf not in sector_files:
                continue
            filepath = os.path.join(SECTORS_DIR, sf)
            d, status = parse_sector_header(filepath)
            age = (today - d).days if d else None
            classification = classify_age(age) if age is not None else "NO-DATE"
            dep = deps.get(sf, {"portfolio": [], "watchlist": []})
            affected.append({
                "file": sf,
                "age": age,
                "class": classification,
                "status": status,
                "portfolio": dep["portfolio"],
                "watchlist": dep["watchlist"],
            })

        if not affected:
            continue

        # Count portfolio deps in this theme
        port_tickers = set()
        for a in affected:
            port_tickers.update(a["portfolio"])

        header = f"\n  {theme.upper()}"
        if port_tickers:
            header += f"  →  portfolio: {', '.join(sorted(port_tickers))}"
        print(header)

        for a in affected:
            age_str = f"{a['age']}d" if a["age"] is not None else "?"
            marker = ""
            if a["class"] in ("BORDERLINE", "STALE", "CRITICAL"):
                marker = f" *** {a['class']}"
            if a["portfolio"]:
                marker += f" [{', '.join(a['portfolio'])}]"
            print(f"    {a['file']:<36} {age_str:>5} {a['status'] or '?':<14}{marker}")

    print(f"\n[Raw data. Stale sectors under active macro themes = highest refresh priority.]")


# ═══════════════════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Sector Health — staleness, coverage, cascades, macro dependencies"
    )
    subparsers = parser.add_subparsers(dest="command", help="Subcommand")

    # freshness
    p_fresh = subparsers.add_parser("freshness", help="Staleness of all sector views")
    p_fresh.add_argument("--stale-only", action="store_true",
                         help="Show only BORDERLINE, STALE, CRITICAL, NO-DATE")

    # coverage
    p_cov = subparsers.add_parser("coverage", help="Universe → sector view mapping")
    p_cov.add_argument("--unmapped", action="store_true",
                       help="Show only unmapped sector labels")

    # cascade
    p_cas = subparsers.add_parser("cascade", help="Dependency chain for a sector view")
    p_cas.add_argument("sector_file", nargs="?", default=None,
                       help="Sector view filename (e.g., insurance.md)")
    p_cas.add_argument("--all", action="store_true",
                       help="Show all sectors with dependencies")

    # changes
    subparsers.add_parser("changes", help="Status changes vs last snapshot")

    # snapshot
    subparsers.add_parser("snapshot", help="Save current baseline")

    # macro-map
    subparsers.add_parser("macro-map", help="Macro themes → sector → portfolio map")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    dispatch = {
        "freshness": cmd_freshness,
        "coverage": cmd_coverage,
        "cascade": cmd_cascade,
        "changes": cmd_changes,
        "snapshot": cmd_snapshot,
        "macro-map": cmd_macro_map,
    }

    dispatch[args.command](args)


if __name__ == "__main__":
    main()
