"""Centralized data access for the dashboard.

All pages MUST import from here — never read filesystem or call yfinance
directly. Every loader is @st.cache_data wrapped with an appropriate TTL.

In tests, call `loader.clear()` to bust the cache between test cases.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import streamlit as st
import yaml


# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

def project_root() -> Path:
    """Return the invest_value_manager project root."""
    # dashboard/data_loader.py -> dashboard/ -> invest_value_manager/
    return Path(__file__).resolve().parent.parent


def _portfolio_path() -> Path:
    return project_root() / "portfolio" / "current.yaml"


def _standing_orders_path() -> Path:
    return project_root() / "state" / "standing_orders.yaml"


# ---------------------------------------------------------------------------
# Loaders (part 1)
# ---------------------------------------------------------------------------

@st.cache_data(ttl=900)  # 15 min
def load_portfolio() -> dict[str, Any]:
    """Return portfolio/current.yaml parsed. Empty skeleton if missing."""
    path = _portfolio_path()
    if not path.exists():
        return {"positions": [], "cash_usd": 0.0}
    return yaml.safe_load(path.read_text()) or {"positions": [], "cash_usd": 0.0}


@st.cache_data(ttl=300)  # 5 min
def load_standing_orders() -> list[dict[str, Any]]:
    """Return list of standing orders, empty if file missing."""
    path = _standing_orders_path()
    if not path.exists():
        return []
    data = yaml.safe_load(path.read_text()) or {}
    return data.get("standing_orders", [])
