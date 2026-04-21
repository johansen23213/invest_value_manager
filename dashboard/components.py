"""Shared UI components for ValueHunter Dashboard.

Owns: COLOR contract (semantic constants), share_mode-aware formatters,
reusable widget helpers. Pages import from here; never define colors inline.
"""
from __future__ import annotations

import re

# ---------------------------------------------------------------------------
# Color contract — semantic colors used across all pages.
# ---------------------------------------------------------------------------

COLOR: dict[str, str] = {
    "urgent_red":    "#E34B4B",   # triggered SOs, kill conditions, critical macro
    "positive_green":"#3FA34D",   # P&L positive, deployment ready, 3+ funds
    "warning_amber": "#F5A623",   # near-trigger, 30-60d stale, 2 funds
    "info_blue":     "#3B82F6",   # in-progress pipeline, general info
    "neutral_grey":  "#9CA3AF",   # empty, unknown, 1 fund
    "tier_a_gold":   "#D4AF37",   # Tier A quality (distinct from positive_green)
    "muted":         "#6B7280",   # secondary text, footnotes
}

PIPELINE_COLORS: dict[str, str] = {
    "R1_NEW":      COLOR["neutral_grey"],
    "R1_COMPLETE": "#93C5FD",
    "R2":          COLOR["info_blue"],
    "R3":          "#1D4ED8",
    "R4_READY":    COLOR["positive_green"],
    "ACTIVE":      COLOR["tier_a_gold"],
    "ARCHIVED":    COLOR["muted"],
}

CONVICTION_COLORS: dict[str, str] = {
    "1_fund":   COLOR["neutral_grey"],
    "2_funds":  COLOR["info_blue"],
    "3+_funds": COLOR["positive_green"],
}

TIER_COLORS: dict[str, str] = {
    "A": COLOR["tier_a_gold"],
    "B": COLOR["info_blue"],
    "C": COLOR["neutral_grey"],
}


_HEX_RE = re.compile(r"^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$")


def is_hex_color(value: str) -> bool:
    """Validate that value is a 3- or 6-digit hex color with leading #."""
    return bool(_HEX_RE.match(value))


# ---------------------------------------------------------------------------
# Formatters (share_mode aware)
# ---------------------------------------------------------------------------

def money(value: float, share_mode: bool) -> str:
    """Format an absolute euro value, redacted when share_mode is True."""
    if share_mode:
        return "—"
    return f"€{int(value):,}"


def pct_of_portfolio(value: float, total: float) -> str:
    """Format value as percentage of total. Zero total → '0.0%'."""
    if total == 0:
        return "0.0%"
    return f"{value / total * 100:.1f}%"


def pct(value: float) -> str:
    """Format as signed percentage with one decimal."""
    return f"{value:+.1f}%"
