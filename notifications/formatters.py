"""Format agent results into human-readable messages."""
from __future__ import annotations
from typing import Any


def format_weekly_digest(result: dict[str, Any]) -> str:
    lines = ["\U0001f4ca *Weekly Screening Digest*", ""]
    screening = result.get("screening", {})
    lines.append(f"Candidates screened: {screening.get('total_candidates', 0)}")
    lines.append(f"Top picks: {', '.join(screening.get('top_tickers', []))}")
    lines.append("")
    decisions = result.get("decisions", [])
    if decisions:
        lines.append("*Decisions:*")
        for d in decisions:
            emoji = {"BUY": "\U0001f7e2", "SELL": "\U0001f534", "WATCH": "\U0001f7e1", "PASS": "\u26aa"}.get(d.get("decision", ""), "\u26aa")
            lines.append(f"{emoji} {d.get('ticker', '?')} \u2014 {d.get('decision', '?')} (conviction {d.get('conviction', '?')})")
    else:
        lines.append("No actionable decisions this week.")
    lines.append(f"\nTokens used: {result.get('total_tokens', 0):,}")
    return "\n".join(lines)


def format_daily_digest(result: dict[str, Any]) -> str:
    lines = ["\U0001f4c8 *Daily Portfolio Monitor*", ""]
    data = result.get("data", {})
    summary = data.get("portfolio_summary", {})
    lines.append(f"Positions: {summary.get('total_positions', '?')}")
    lines.append(f"Net P&L: {summary.get('net_pnl_pct', '?')}%")
    lines.append(f"On track: {summary.get('positions_on_track', '?')} | Drifting: {summary.get('positions_drifting', '?')} | Alert: {summary.get('positions_alert', '?')}")
    actions = data.get("action_items", [])
    if actions:
        lines.append("\n*Action items:*")
        for a in actions:
            lines.append(f"\u2022 {a}")
    lines.append(f"\n{data.get('summary', '')}")
    return "\n".join(lines)


def format_on_demand(result: dict[str, Any]) -> str:
    lines = [f"\U0001f50d *On-Demand Analysis: {result.get('ticker', '?')}*", ""]
    agents = result.get("agents", {})
    for aid, adata in agents.items():
        status = "\u2705" if adata.get("success") else "\u274c"
        lines.append(f"{status} {aid}")
    lines.append(f"\nAll succeeded: {result.get('all_succeeded')}")
    lines.append(f"Tokens: {result.get('total_tokens', 0):,}")
    return "\n".join(lines)
