"""Centralized data access for the dashboard.

All pages MUST import from here — never read filesystem or call yfinance
directly. Every loader is @st.cache_data wrapped with an appropriate TTL.

In tests, call `loader.clear()` to bust the cache between test cases.
"""
from __future__ import annotations

import json
from datetime import date, timedelta
from pathlib import Path
from typing import Any

import pandas as pd
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


def _universe_path() -> Path:
    return project_root() / "state" / "quality_universe.yaml"


def _calendar_path() -> Path:
    return project_root() / "state" / "calendar.yaml"


def _spanish_funds_root() -> Path:
    return project_root() / "knowledge_base" / "spanish_funds"


def _today() -> date:
    """Return today's date. Patched in tests for deterministic calendar filtering."""
    return date.today()


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


@st.cache_data(ttl=900)  # 15 min
def load_universe() -> pd.DataFrame:
    """Return quality universe as DataFrame. Empty DataFrame if file missing."""
    path = _universe_path()
    if not path.exists():
        return pd.DataFrame()
    data = yaml.safe_load(path.read_text()) or {}
    companies = data.get("quality_universe", {}).get("companies", [])
    if not companies:
        return pd.DataFrame()
    return pd.DataFrame(companies)


@st.cache_data(ttl=900)  # 15 min
def load_calendar(days: int) -> pd.DataFrame:
    """Return calendar events within `days` from today. Empty if file missing."""
    path = _calendar_path()
    if not path.exists():
        return pd.DataFrame()
    data = yaml.safe_load(path.read_text()) or {}
    events = data.get("calendar", [])
    if not events:
        return pd.DataFrame()
    df = pd.DataFrame(events)
    df["date"] = pd.to_datetime(df["date"]).dt.date
    today = _today()
    end = today + timedelta(days=days)
    return df[(df["date"] >= today) & (df["date"] <= end)].reset_index(drop=True)


@st.cache_data(ttl=900)  # 15 min
def load_spanish_funds() -> dict[str, dict[str, Any]]:
    """Return {fund_id: latest_letter_dict} for each fund with any processed letter."""
    root = _spanish_funds_root()
    if not root.exists() or not root.is_dir():
        return {}
    out: dict[str, dict[str, Any]] = {}
    for fund_dir in sorted(root.iterdir()):
        if not fund_dir.is_dir():
            continue
        # Skip "raw" subdirectories and last_processed.json — only quarter files
        quarter_files = sorted(fund_dir.glob("[0-9]*.json"))
        if not quarter_files:
            continue
        latest = quarter_files[-1]
        out[fund_dir.name] = json.loads(latest.read_text())
    return out
