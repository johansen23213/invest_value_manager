#!/usr/bin/env python3
"""
Pipeline Velocity — Track and visualize pipeline throughput metrics.

How fast are candidates moving through R1->R2->R3->R4? Where are the
bottlenecks? What's the average time from R1 to deployment? Makes pipeline
management data-driven instead of ad-hoc.

Reads: quality_universe.yaml, pipeline_tracker.yaml, calendar.yaml,
       session_continuity.yaml, decisions_log.yaml

Usage:
  python3 tools/pipeline_velocity.py              # Full pipeline metrics
  python3 tools/pipeline_velocity.py --funnel     # Funnel visualization
  python3 tools/pipeline_velocity.py --stale      # Stale pipeline items (stuck >21 days)
  python3 tools/pipeline_velocity.py --history    # Historical throughput per session
"""

import sys
import os
import argparse
import re
from datetime import date, datetime, timedelta
from collections import Counter

import yaml

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
UNIVERSE_PATH = os.path.join(PROJECT_ROOT, "state", "quality_universe.yaml")
CALENDAR_PATH = os.path.join(PROJECT_ROOT, "state", "calendar.yaml")
PIPELINE_TRACKER_PATH = os.path.join(PROJECT_ROOT, "state", "pipeline_tracker.yaml")
CONTINUITY_PATH = os.path.join(PROJECT_ROOT, "state", "session_continuity.yaml")
DECISIONS_LOG_PATH = os.path.join(PROJECT_ROOT, "learning", "decisions_log.yaml")

# Pipeline stages in logical order (for funnel / progression)
PIPELINE_ORDER = [
    "SCORED",
    "R1_COMPLETE",
    "R2_PAUSED",
    "R3_COMPLETE",
    "R4_APPROVED",
    "R4_CONDITIONAL",
    "R4_WATCHLIST",
    "APPROVED",
    "STANDING_ORDER",
    "ACTIVE",
    "FROZEN",
    "ARCHIVED",
]

# Stages that represent "in pipeline" (not yet deployed or inactive)
ACTIVE_PIPELINE_STAGES = {
    "R1_COMPLETE", "R2_PAUSED", "R3_COMPLETE",
    "R4_APPROVED", "R4_CONDITIONAL", "R4_WATCHLIST", "APPROVED",
}

# Stages where a standing order exists or is implied
SO_STAGES = {"STANDING_ORDER", "APPROVED", "R4_APPROVED"}

# Stages that have passed R1 (for cumulative funnel counting)
PAST_R1_STAGES = {
    "R1_COMPLETE", "R2_PAUSED", "R3_COMPLETE",
    "R4_APPROVED", "R4_CONDITIONAL", "R4_WATCHLIST",
    "APPROVED", "STANDING_ORDER", "ACTIVE",
}

PAST_R3_STAGES = {
    "R3_COMPLETE", "R4_APPROVED", "R4_CONDITIONAL", "R4_WATCHLIST",
    "APPROVED", "STANDING_ORDER", "ACTIVE",
}

PAST_R4_STAGES = {
    "R4_APPROVED", "R4_CONDITIONAL", "R4_WATCHLIST",
    "APPROVED", "STANDING_ORDER", "ACTIVE",
}

# Stage staleness thresholds (days in stage before considered stale)
STALENESS_THRESHOLDS = {
    "SCORED": 60,
    "R1_COMPLETE": 21,
    "R2_PAUSED": 30,
    "R3_COMPLETE": 14,
    "R4_APPROVED": 21,
    "R4_CONDITIONAL": 30,
    "R4_WATCHLIST": 30,
    "APPROVED": 21,
    "STANDING_ORDER": 60,
}


def load_yaml(path):
    """Load a YAML file, returning empty dict on failure."""
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r") as f:
            return yaml.safe_load(f) or {}
    except Exception:
        return {}


def load_universe():
    """Load companies from quality_universe.yaml."""
    data = load_yaml(UNIVERSE_PATH)
    return data.get("quality_universe", {}).get("companies", [])


def load_earnings_tickers(days_ahead=30):
    """Load tickers with earnings in next N days from calendar.yaml."""
    data = load_yaml(CALENDAR_PATH)
    today = date.today()
    cutoff = today + timedelta(days=days_ahead)
    earnings = {}

    for event in data.get("events", []):
        event_date = event.get("date")
        event_type = str(event.get("type", ""))
        ticker = event.get("ticker", "")
        if not event_date or not ticker:
            continue
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


def estimate_stage_date(company):
    """Estimate when a company entered its current pipeline stage.

    Uses available signals: last_scored is typically updated when pipeline
    status changes, so it serves as the best proxy for stage entry date.
    Returns a date object or None.
    """
    # last_scored is updated when QS is run / pipeline status changes
    last_scored = company.get("last_scored")
    if last_scored:
        try:
            return datetime.strptime(str(last_scored), "%Y-%m-%d").date()
        except (ValueError, TypeError):
            pass

    # Fallback: last_price_check
    lpc = company.get("last_price_check")
    if lpc:
        try:
            return datetime.strptime(str(lpc), "%Y-%m-%d").date()
        except (ValueError, TypeError):
            pass

    return None


def is_near_entry(company, threshold_pct=15.0):
    """Check if company is near its entry price.

    distance_to_entry = (current_price - entry_price) / entry_price * 100
    Positive means price is above entry (needs to drop).
    Negative means price is below entry (already past entry -- immediate buy).
    Near entry: 0 <= dist <= threshold OR dist < 0 (below entry).
    """
    dist = company.get("distance_to_entry")
    if dist is None:
        return False
    # Below entry (negative) or within threshold above entry
    return dist <= threshold_pct


def is_gated(company, earnings_tickers):
    """Check if company is gated by upcoming earnings."""
    ticker = company.get("ticker", "")
    if ticker in earnings_tickers:
        return True
    # Also check notes for "gate" or "gated" keywords
    notes = str(company.get("notes", "")).lower()
    return "gate" in notes or "gated" in notes


def is_fantasy_risk(company, threshold_pct=30.0):
    """Check if entry price is >threshold% below current price.

    distance_to_entry > threshold means current price is far above entry.
    """
    dist = company.get("distance_to_entry")
    if dist is None:
        return True  # No entry data = treat as unknown
    return dist > threshold_pct


def show_dashboard(companies):
    """Mode 1: Full pipeline velocity metrics dashboard."""
    today = date.today()
    earnings = load_earnings_tickers(30)
    continuity = load_yaml(CONTINUITY_PATH)

    # Group by pipeline status
    by_status = {}
    for c in companies:
        status = c.get("pipeline_status", "UNKNOWN")
        by_status.setdefault(status, []).append(c)

    print(f"\n{'=' * 80}")
    print(f"  PIPELINE VELOCITY METRICS | {today}")
    print(f"{'=' * 80}")

    # --- Current Inventory ---
    print(f"\nCURRENT INVENTORY:")
    print(f"  {'Stage':<20} {'Count':>5}  {'Avg Days':>9}  {'Oldest':<22} {'Gated':>6}")
    print(f"  {'-' * 70}")

    display_order = [
        "SCORED", "R1_COMPLETE", "R2_PAUSED", "R3_COMPLETE",
        "R4_APPROVED", "R4_CONDITIONAL", "R4_WATCHLIST",
        "APPROVED", "STANDING_ORDER", "FROZEN", "ACTIVE", "ARCHIVED",
    ]

    total_pipeline = 0
    for status in display_order:
        items = by_status.get(status, [])
        if not items:
            continue

        count = len(items)

        # Compute days in stage
        days_list = []
        oldest_ticker = None
        oldest_days = 0
        gated_count = 0

        for c in items:
            stage_date = estimate_stage_date(c)
            if stage_date:
                days_in = (today - stage_date).days
                days_list.append(days_in)
                if days_in > oldest_days:
                    oldest_days = days_in
                    oldest_ticker = c.get("ticker", "?")
            if is_gated(c, earnings):
                gated_count += 1

        avg_days = f"{sum(days_list) / len(days_list):.0f} days" if days_list else "N/A"
        oldest_str = f"{oldest_ticker} ({oldest_days}d)" if oldest_ticker else "N/A"
        gated_str = f"{gated_count} gated" if gated_count > 0 else "-"

        if status in ACTIVE_PIPELINE_STAGES:
            total_pipeline += count

        print(f"  {status:<20} {count:>5}  {avg_days:>9}  {oldest_str:<22} {gated_str:>6}")

    # --- Bottleneck Analysis ---
    print(f"\nBOTTLENECK ANALYSIS:")

    r1_items = by_status.get("R1_COMPLETE", [])
    r3_items = by_status.get("R3_COMPLETE", [])

    if r1_items:
        r1_days = []
        for c in r1_items:
            sd = estimate_stage_date(c)
            if sd:
                r1_days.append((today - sd).days)
        avg_r1 = sum(r1_days) / len(r1_days) if r1_days else 0

        # Near entry R1s (actionable) — only positive dist <= 20% (approaching entry)
        near_entry_r1 = [c for c in r1_items
                         if c.get("distance_to_entry") is not None
                         and 0 <= c["distance_to_entry"] <= 20.0]
        # Below entry (negative distance = below entry price already)
        below_entry_r1 = [c for c in r1_items
                          if c.get("distance_to_entry") is not None
                          and c["distance_to_entry"] < 0]
        fantasy_r1 = [c for c in r1_items if is_fantasy_risk(c)]
        gated_r1 = [c for c in r1_items if is_gated(c, earnings)]

        print(f"  R1_COMPLETE -> R2: {len(r1_items)} candidates, avg {avg_r1:.0f} days waiting")
        print(f"    Near entry (0-20%): {len(near_entry_r1)} | Below entry: {len(below_entry_r1)} | Gated: {len(gated_r1)} | Fantasy (>30%): {len(fantasy_r1)}")

        # Priority: below entry first, then near entry sorted by distance ascending
        priority_candidates = sorted(below_entry_r1, key=lambda c: c.get("distance_to_entry", 0))
        priority_candidates += sorted(near_entry_r1, key=lambda c: c.get("distance_to_entry", 999))
        if priority_candidates:
            top3 = priority_candidates[:3]
            names = ", ".join(
                f"{c['ticker']} ({c.get('distance_to_entry', 0):+.1f}%)"
                for c in top3
            )
            print(f"    Priority for advancement: {names}")

    if r3_items:
        r3_days = []
        for c in r3_items:
            sd = estimate_stage_date(c)
            if sd:
                r3_days.append((today - sd).days)
        avg_r3 = sum(r3_days) / len(r3_days) if r3_days else 0
        gated_r3 = [c for c in r3_items if is_gated(c, earnings)]
        ungated_r3 = [c for c in r3_items if not is_gated(c, earnings)]
        print(f"  R3_COMPLETE -> R4: {len(r3_items)} candidates, avg {avg_r3:.0f} days waiting")
        print(f"    Gated: {len(gated_r3)} | Ready for committee: {len(ungated_r3)}")
        if ungated_r3:
            # Show top 3 by QS descending
            top_r3 = sorted(ungated_r3, key=lambda c: -(c.get("qs_adj") or c.get("qs_tool") or 0))[:3]
            names = ", ".join(f"{c['ticker']} (QS {c.get('qs_adj') or c.get('qs_tool', '?')})" for c in top_r3)
            print(f"    Top candidates: {names}")

    # --- Velocity This Session ---
    print(f"\nVELOCITY (last recorded session):")
    completed = continuity.get("completed", {})
    velocity = completed.get("velocity_units", 0)
    advancements = completed.get("pipeline_advancement", [])
    session_info = continuity.get("session", {})
    session_id = session_info.get("id", "?")
    session_date = session_info.get("date", "?")

    velocity_label = "GOOD" if velocity >= 3 else ("OK" if velocity >= 1 else "LOW")
    print(f"  Session {session_id} ({session_date}): {velocity} units [{velocity_label}] (target: 3+)")
    if advancements:
        for adv in advancements:
            adv_short = str(adv)[:90]
            print(f"    - {adv_short}")

    # --- R1 Verdict Distribution ---
    print(f"\nR1 VERDICT DISTRIBUTION (current R1_COMPLETE):")
    r1_with_verdict = [c for c in r1_items if c.get("r1_verdict")]
    if r1_with_verdict:
        verdicts = Counter(c.get("r1_verdict") for c in r1_with_verdict)
        total_v = sum(verdicts.values())
        for v, count in sorted(verdicts.items(), key=lambda x: -x[1]):
            pct = count / total_v * 100
            bar = "#" * int(pct / 3)
            print(f"  {v:<14} {count:>3} ({pct:4.0f}%)  {bar}")
        fantasy_count = verdicts.get("FANTASY", 0) + verdicts.get("OVERVALUED", 0)
        fantasy_rate = fantasy_count / total_v * 100 if total_v else 0
        rate_label = "ALARM" if fantasy_rate > 50 else "OK"
        print(f"  Fantasy rate: {fantasy_rate:.0f}% [{rate_label}]")
    else:
        print(f"  No R1 verdicts recorded.")

    # --- Pipeline Health Summary ---
    print(f"\nPIPELINE HEALTH:")
    total_universe = len(companies)
    active_count = len(by_status.get("ACTIVE", []))
    so_count = sum(len(by_status.get(s, [])) for s in SO_STAGES)

    print(f"  Universe: {total_universe} | In pipeline: {total_pipeline} | Standing orders: {so_count} | Active: {active_count}")

    # Tier distribution across pipeline
    pipeline_items = [c for c in companies if c.get("pipeline_status") in ACTIVE_PIPELINE_STAGES]
    tier_a_pipeline = sum(1 for c in pipeline_items if c.get("tier") == "A")
    tier_b_pipeline = sum(1 for c in pipeline_items if c.get("tier") == "B")
    print(f"  Pipeline Tier A: {tier_a_pipeline} | Tier B: {tier_b_pipeline}")

    print(f"\n[Raw data. Pipeline velocity metrics.]")


def show_funnel(companies):
    """Mode 2: Visual funnel showing conversion rates.

    Uses CUMULATIVE counts: 'passed R1' = all companies currently at R1+,
    not just those sitting at R1_COMPLETE right now.
    """
    today = date.today()
    earnings = load_earnings_tickers(30)

    total = len(companies)
    tier_a = [c for c in companies if c.get("tier") == "A"]
    tier_b = [c for c in companies if c.get("tier") == "B"]
    tier_other = [c for c in companies if c.get("tier") not in ("A", "B")]

    scored = [c for c in companies if c.get("pipeline_status") == "SCORED"]
    r1_current = [c for c in companies if c.get("pipeline_status") == "R1_COMPLETE"]
    r2_paused = [c for c in companies if c.get("pipeline_status") == "R2_PAUSED"]
    r3_current = [c for c in companies if c.get("pipeline_status") == "R3_COMPLETE"]
    r4_current = [c for c in companies if c.get("pipeline_status") in ("R4_APPROVED", "R4_CONDITIONAL", "R4_WATCHLIST")]
    approved = [c for c in companies if c.get("pipeline_status") == "APPROVED"]
    standing_order = [c for c in companies if c.get("pipeline_status") == "STANDING_ORDER"]
    active = [c for c in companies if c.get("pipeline_status") == "ACTIVE"]
    frozen = [c for c in companies if c.get("pipeline_status") == "FROZEN"]

    # Cumulative: all companies that have EVER passed through R1 (currently at R1+ stages)
    passed_r1 = [c for c in companies if c.get("pipeline_status") in PAST_R1_STAGES]
    passed_r3 = [c for c in companies if c.get("pipeline_status") in PAST_R3_STAGES]
    passed_r4 = [c for c in companies if c.get("pipeline_status") in PAST_R4_STAGES]

    # Combined deployment-ready
    deployment_ready = approved + r4_current + standing_order

    # R1 breakdown (current R1_COMPLETE only)
    r1_near = [c for c in r1_current
                if c.get("distance_to_entry") is not None
                and 0 <= c["distance_to_entry"] <= 20.0]
    r1_below = [c for c in r1_current
                 if c.get("distance_to_entry") is not None
                 and c["distance_to_entry"] < 0]
    r1_gated = [c for c in r1_current if is_gated(c, earnings)]
    r1_fantasy = [c for c in r1_current if is_fantasy_risk(c)]
    r1_actionable = [c for c in r1_current if c.get("r1_verdict") == "ACTIONABLE"]

    # Conversion rates (cumulative)
    non_scored = total - len(scored)  # Everything that progressed past SCORED
    r1_pct = len(passed_r1) / non_scored * 100 if non_scored else 0
    r3_of_r1 = len(passed_r3) / len(passed_r1) * 100 if passed_r1 else 0
    r4_of_r3 = len(passed_r4) / len(passed_r3) * 100 if passed_r3 else 0

    # Max bar width
    max_width = 60

    def bar(count, base, label, indent=2, detail=""):
        """Render a proportional bar."""
        if base <= 0:
            pct = 0
        else:
            pct = count / base * 100
        width = int(count / max(total, 1) * max_width)
        width = max(width, 1) if count > 0 else 0
        bar_str = "=" * width
        prefix = " " * indent
        pct_str = f"({pct:.1f}%)" if detail == "" else f"({pct:.1f}% {detail})"
        print(f"{prefix}{bar_str} {count:>3} {label} {pct_str}")

    print(f"\n{'=' * 80}")
    print(f"  PIPELINE FUNNEL | {today}")
    print(f"{'=' * 80}")

    print(f"\n  Universe: {total} companies")
    bar(len(tier_a), total, "Tier A", 4, "of universe")
    bar(len(tier_b), total, "Tier B", 4, "of universe")
    if tier_other:
        bar(len(tier_other), total, "Other", 4, "of universe")

    print()
    print(f"  Scored (awaiting R1):      {len(scored)} ({len(scored)/total*100:.0f}% of universe)")
    bar(len(scored), total, "SCORED", 4, "of universe")

    print()
    print(f"  Passed R1 (cumulative):    {len(passed_r1)}")
    bar(len(passed_r1), total, "passed R1", 4, "of universe")
    print(f"    Currently at R1_COMPLETE:  {len(r1_current)}")
    if r1_current:
        bar(len(r1_near), len(r1_current), "Near Entry (0-20%)", 6, "of R1")
        bar(len(r1_below), len(r1_current), "Below Entry (<0%)", 6, "of R1")
        bar(len(r1_actionable), len(r1_current), "ACTIONABLE verdict", 6, "of R1")
        bar(len(r1_gated), len(r1_current), "Earnings Gated", 6, "of R1")
        bar(len(r1_fantasy), len(r1_current), "Fantasy Risk (>30%)", 6, "of R1")
    if r2_paused:
        print(f"    R2 Paused:                 {len(r2_paused)}")
        for c in r2_paused:
            print(f"      {c['ticker']:<14} (paused, revisit later)")

    print()
    print(f"  Passed R3 (cumulative):    {len(passed_r3)}  ({r3_of_r1:.0f}% of R1 graduates)")
    bar(len(passed_r3), total, "passed R3", 4, "of universe")
    print(f"    Currently at R3_COMPLETE:  {len(r3_current)}")

    print()
    print(f"  Passed R4 (cumulative):    {len(passed_r4)}  ({r4_of_r3:.0f}% of R3 graduates)")
    bar(len(passed_r4), total, "passed R4", 4, "of universe")
    print(f"    R4_APPROVED/CONDITIONAL:   {len(r4_current)}")

    print()
    print(f"  Approved (with SO):        {len(approved)}")
    print(f"  Standing Orders:           {len(standing_order)}")
    print(f"  Deployment Ready total:    {len(deployment_ready)} ({len(deployment_ready)/total*100:.1f}% of universe)")
    bar(len(deployment_ready), total, "DEPLOYMENT READY", 4, "of universe")

    print()
    active_count = len(active)
    print(f"  Active Positions:          {active_count}")
    if frozen:
        print(f"  Frozen:                    {len(frozen)}")

    print(f"\n  OVERALL FUNNEL (cumulative stage counts):")
    funnel_stages = [
        ("Universe", total),
        ("Passed R1", len(passed_r1)),
        ("Passed R3", len(passed_r3)),
        ("Passed R4", len(passed_r4)),
        ("Deploy Ready", len(deployment_ready)),
        ("Active", active_count),
    ]
    labels_str = " -> ".join(f"{name}" for name, _ in funnel_stages)
    funnel_str = " -> ".join(f"{count}" for _, count in funnel_stages)
    print(f"  {labels_str}")
    print(f"  {funnel_str}")

    if total > 0 and len(passed_r1) > 0:
        deploy_rate = len(deployment_ready) / len(passed_r1) * 100
        print(f"  R1 -> Deployment Ready: {deploy_rate:.0f}% conversion")

    print(f"\n[Raw data. Pipeline velocity metrics.]")


def show_stale(companies):
    """Mode 3: Stale pipeline items stuck too long in their stage."""
    today = date.today()
    earnings = load_earnings_tickers(60)

    stale_items = []
    near_entry_no_advancement = []

    for c in companies:
        status = c.get("pipeline_status", "")
        threshold = STALENESS_THRESHOLDS.get(status)
        if threshold is None:
            continue

        stage_date = estimate_stage_date(c)
        if not stage_date:
            continue

        days_in = (today - stage_date).days
        if days_in < threshold:
            continue

        ticker = c.get("ticker", "?")
        dist = c.get("distance_to_entry")
        verdict = c.get("r1_verdict", "")
        tier = c.get("tier", "?")

        # Determine reason stuck
        reason = ""
        action = ""

        if status == "R1_COMPLETE":
            if dist is not None and dist > 30:
                reason = f"Overvalued (+{dist:.0f}%)"
                action = "WAIT for pullback"
            elif is_gated(c, earnings):
                earn_date = earnings.get(ticker)
                reason = "Earnings gated"
                if earn_date:
                    reason += f" ({earn_date})"
                action = "WAIT for earnings"
            elif verdict in ("FANTASY", "OVERVALUED"):
                reason = f"{verdict}"
                if dist is not None:
                    reason += f" ({dist:+.0f}%)"
                action = "WAIT for pullback"
            elif dist is not None and dist < 0:
                reason = f"Below entry ({dist:+.0f}%)"
                action = "PRIORITY: RUN devil's-advocate"
                near_entry_no_advancement.append(c)
            else:
                reason = "No R2 advancement"
                action = "RUN devil's-advocate"
                if dist is not None and 0 <= dist <= 20.0:
                    near_entry_no_advancement.append(c)
        elif status == "R3_COMPLETE":
            if is_gated(c, earnings):
                reason = "Earnings gated"
                action = "WAIT for earnings"
            else:
                reason = "No R4 committee"
                action = "RUN investment-committee"
        elif status in ("R4_APPROVED", "APPROVED"):
            if dist is not None and dist > 20:
                reason = f"Price far from entry (+{dist:.0f}%)"
                action = "WAIT or adjust entry"
            else:
                reason = "Approved, no SO created"
                action = "CREATE standing order"
        elif status == "STANDING_ORDER":
            if dist is not None:
                reason = f"SO not triggered ({dist:+.0f}%)"
            else:
                reason = "SO not triggered"
            action = "Monitor price" if dist and dist < 20 else "Review entry realism"
        elif status == "SCORED":
            reason = "Awaiting R1"
            action = "Queue for R1 processing"
        elif status == "R2_PAUSED":
            reason = "R2 paused"
            action = "Review if conditions changed"
        else:
            reason = f"Stuck in {status}"
            action = "Review"

        stale_items.append({
            "ticker": ticker,
            "status": status,
            "days": days_in,
            "threshold": threshold,
            "reason": reason,
            "action": action,
            "tier": tier,
            "dist": dist,
        })

    # Sort by days in stage descending
    stale_items.sort(key=lambda x: -x["days"])

    print(f"\n{'=' * 100}")
    print(f"  STALE PIPELINE ITEMS | {today}")
    print(f"{'=' * 100}")

    if not stale_items:
        print(f"\n  No stale items. All pipeline candidates within expected timelines.")
        print(f"\n[Raw data. Pipeline velocity metrics.]")
        return

    # Group by status for clarity
    by_status = {}
    for item in stale_items:
        by_status.setdefault(item["status"], []).append(item)

    for status in PIPELINE_ORDER:
        items = by_status.get(status, [])
        if not items:
            continue

        threshold = STALENESS_THRESHOLDS.get(status, "?")
        print(f"\n  {status} (threshold: {threshold} days) -- {len(items)} stale:")
        print(f"  {'Ticker':<14} {'Tier':>4} {'Days':>5}  {'Dist%':>7}  {'Reason':<28} {'Action'}")
        print(f"  {'-' * 90}")

        for item in items:
            dist_str = f"{item['dist']:+.1f}%" if item["dist"] is not None else "N/A"
            print(f"  {item['ticker']:<14} {item['tier']:>4} {item['days']:>5}d {dist_str:>7}  {item['reason']:<28} {item['action']}")

    # Summary
    total_stale = len(stale_items)
    stale_r1 = len(by_status.get("R1_COMPLETE", []))
    stale_r3 = len(by_status.get("R3_COMPLETE", []))
    stale_scored = len(by_status.get("SCORED", []))

    print(f"\n  SUMMARY: {total_stale} stale items total")
    if stale_r1:
        print(f"    R1_COMPLETE: {stale_r1} (need R2 advancement or price drop)")
    if stale_r3:
        print(f"    R3_COMPLETE: {stale_r3} (need R4 committee)")
    if stale_scored:
        print(f"    SCORED: {stale_scored} (need R1 processing)")

    if near_entry_no_advancement:
        print(f"\n  URGENT: {len(near_entry_no_advancement)} near/below-entry R1_COMPLETE without R2:")
        for c in near_entry_no_advancement:
            dist = c.get("distance_to_entry")
            dist_str = f"{dist:+.1f}%" if dist is not None else "?"
            print(f"    {c['ticker']:<14} dist {dist_str} - PRIORITY for devil's-advocate")

    print(f"\n[Raw data. Pipeline velocity metrics.]")


def parse_velocity_from_text(text):
    """Extract velocity units from a pipeline_tracker last_result string."""
    if not text:
        return None
    m = re.search(r'(\d+)\s*velocity\s*units?', text, re.IGNORECASE)
    if m:
        return int(m.group(1))
    return None


def parse_session_from_text(text):
    """Extract session ID from a pipeline_tracker last_result string."""
    if not text:
        return None
    m = re.search(r'S(\d+)[:\s]', text)
    if m:
        return int(m.group(1))
    return None


def show_history(companies):
    """Mode 4: Historical throughput (from available sources).

    Collects velocity data from session_continuity.yaml and pipeline_tracker.yaml.
    """
    today = date.today()
    tracker = load_yaml(PIPELINE_TRACKER_PATH)
    continuity = load_yaml(CONTINUITY_PATH)

    print(f"\n{'=' * 80}")
    print(f"  PIPELINE THROUGHPUT HISTORY | {today}")
    print(f"{'=' * 80}")

    # Collect velocity data from available sources
    history = []

    # Source 1: Current session from session_continuity.yaml
    session_data = continuity.get("session", {})
    completed = continuity.get("completed", {})
    session_id = session_data.get("id")
    session_date = session_data.get("date", "")
    velocity = completed.get("velocity_units", 0)

    if session_id:
        advancements = completed.get("pipeline_advancement", [])
        r1_new = 0
        r2_adv = 0
        r4_cmt = 0
        for adv in advancements:
            adv_lower = str(adv).lower()
            if "r2 complete" in adv_lower or "r2 done" in adv_lower:
                r2_adv += 1
            elif "r4" in adv_lower and ("approved" in adv_lower or "committee" in adv_lower):
                r4_cmt += 1
            elif "r1" in adv_lower:
                r1_new += 1

        history.append({
            "session": session_id,
            "date": session_date,
            "velocity": velocity,
            "r1_new": r1_new,
            "r2_adv": r2_adv,
            "r4_cmt": r4_cmt,
            "source": "continuity",
        })

    # Source 2: pipeline_tracker last_result fields
    for key in ["capital_deployment", "r1_processing"]:
        section = tracker.get(key, {})
        last_result = section.get("last_result", "")
        if not last_result:
            continue

        vel = parse_velocity_from_text(last_result)
        sess = parse_session_from_text(last_result)

        if sess and vel is not None:
            already_tracked = any(h["session"] == sess for h in history)
            if not already_tracked:
                history.append({
                    "session": sess,
                    "date": str(section.get("last_run", "?")),
                    "velocity": vel,
                    "r1_new": "?",
                    "r2_adv": "?",
                    "r4_cmt": "?",
                    "source": key,
                })

    # Source 3: efficiency stats from r1_processing
    r1_section = tracker.get("r1_processing", {})
    efficiency = r1_section.get("efficiency", {})
    fantasy_rate = efficiency.get("fantasy_rate_last_10", "?")

    if not history:
        print(f"\n  No historical velocity data available.")
        print(f"  velocity_units is tracked in session_continuity.yaml (current session only).")
        print(f"  Suggestion: Track velocity_units per session in a rolling log for trend analysis.")
        print(f"\n[Raw data. Pipeline velocity metrics.]")
        return

    # Sort by session descending
    history.sort(key=lambda h: h.get("session", 0), reverse=True)

    print(f"\nAVAILABLE VELOCITY DATA:")
    print(f"  {'Session':>8}  {'Date':<12} {'Velocity':>8}  {'R1 New':>7}  {'R2 Adv':>7}  {'R4 Cmt':>7}  {'Status':>8}  Source")
    print(f"  {'-' * 80}")

    for h in history:
        vel = h["velocity"]
        vel_label = "GOOD" if vel >= 3 else ("OK" if vel >= 1 else "LOW")
        sess_str = f"S{h['session']}" if h["session"] else "?"
        r1_str = str(h["r1_new"]) if h["r1_new"] != "?" else "?"
        r2_str = str(h["r2_adv"]) if h["r2_adv"] != "?" else "?"
        r4_str = str(h["r4_cmt"]) if h["r4_cmt"] != "?" else "?"
        print(f"  {sess_str:>8}  {h['date']:<12} {vel:>8}  {r1_str:>7}  {r2_str:>7}  {r4_str:>7}  {vel_label:>8}  {h['source']}")

    # Summary stats
    velocities = [h["velocity"] for h in history if h["velocity"] is not None]
    if velocities:
        avg_vel = sum(velocities) / len(velocities)
        max_vel = max(velocities)
        min_vel = min(velocities)
        avg_label = "GOOD" if avg_vel >= 3 else ("OK" if avg_vel >= 1 else "LOW")
        print(f"\n  Avg velocity: {avg_vel:.1f} units/session (target: 3.0+) [{avg_label}]")
        print(f"  Max: {max_vel} | Min: {min_vel} | Sessions tracked: {len(velocities)}")

    # Fantasy rate from efficiency tracking
    if fantasy_rate != "?":
        rate_pct = fantasy_rate * 100
        print(f"\n  Fantasy rate (last 10 R1s): {rate_pct:.0f}%")
        actionable_rate = efficiency.get("actionable_rate_last_10", "?")
        if actionable_rate != "?":
            print(f"  Actionable rate (last 10 R1s): {actionable_rate * 100:.0f}%")

    # R1 verdict distribution as historical indicator
    r1_items = [c for c in companies if c.get("pipeline_status") == "R1_COMPLETE" and c.get("r1_verdict")]
    if r1_items:
        verdicts = Counter(c.get("r1_verdict") for c in r1_items)
        total_v = sum(verdicts.values())
        actionable = verdicts.get("ACTIONABLE", 0)
        at_fv = verdicts.get("AT_FV", 0)
        productive = actionable + at_fv
        productive_rate = productive / total_v * 100 if total_v else 0
        print(f"\n  R1 productive rate (current R1_COMPLETE): {productive_rate:.0f}% ({productive}/{total_v} -> ACTIONABLE/AT_FV)")

    print(f"\n  NOTE: Full per-session history requires velocity_log in session_continuity.yaml.")
    print(f"  Currently only the latest session + pipeline_tracker last_result are available.")
    print(f"  Recommendation: add velocity_log[] rolling 10-session entries for trend analysis.")

    print(f"\n[Raw data. Pipeline velocity metrics.]")


def main():
    parser = argparse.ArgumentParser(
        description="Pipeline Velocity -- Track pipeline throughput and bottlenecks"
    )
    parser.add_argument(
        "--funnel", action="store_true",
        help="Funnel visualization with conversion rates"
    )
    parser.add_argument(
        "--stale", action="store_true",
        help="Stale pipeline items stuck too long (>threshold days)"
    )
    parser.add_argument(
        "--history", action="store_true",
        help="Historical throughput per session"
    )
    args = parser.parse_args()

    companies = load_universe()
    if not companies:
        print("Quality Universe is empty.")
        sys.exit(1)

    if args.funnel:
        show_funnel(companies)
    elif args.stale:
        show_stale(companies)
    elif args.history:
        show_history(companies)
    else:
        show_dashboard(companies)


if __name__ == "__main__":
    main()
