"""Centralized data access for the dashboard.

All pages MUST import from here — never read filesystem or call yfinance
directly. Every loader is @st.cache_data wrapped with an appropriate TTL.

In tests, call `loader.clear()` to bust the cache between test cases.
"""
from __future__ import annotations

import json
import subprocess
from datetime import date, timedelta
from pathlib import Path
from typing import Any

import pandas as pd
import streamlit as st
import yaml
import yfinance as yf


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


# ---------------------------------------------------------------------------
# Loaders (part 2) — prices, macro, compute helpers
# ---------------------------------------------------------------------------

@st.cache_data(ttl=900)  # 15 min
def load_prices(tickers: tuple[str, ...]) -> dict[str, float | None]:
    """Batch yfinance price fetch. Tuple key for cache hashability."""
    if not tickers:
        return {}
    try:
        t = yf.Tickers(" ".join(tickers))
    except Exception:
        return {ticker: None for ticker in tickers}
    out: dict[str, float | None] = {}
    for ticker in tickers:
        tk = t.tickers.get(ticker)
        if tk is None:
            out[ticker] = None
            continue
        info = getattr(tk, "info", {}) or {}
        price = info.get("regularMarketPrice")
        out[ticker] = float(price) if isinstance(price, (int, float)) else None
    return out


def _run_macro_tool() -> str:
    """Run tools/macro_fragility.py world --json and return stdout. Empty on failure."""
    try:
        result = subprocess.run(
            ["python3", "tools/macro_fragility.py", "world", "--json"],
            cwd=project_root(),
            capture_output=True,
            text=True,
            timeout=30,
        )
        if result.returncode != 0:
            return ""
        return result.stdout
    except Exception:
        return ""


@st.cache_data(ttl=3600)  # 1 hour
def load_macro() -> dict[str, Any]:
    """Load macro snapshot via macro_fragility.py world. Empty on failure."""
    raw = _run_macro_tool()
    if not raw:
        return {}
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {}


@st.cache_data(ttl=1800)  # 30 min
def compute_actions_today() -> list[dict[str, Any]]:
    """Derive prioritized daily action list from SOs + calendar + pipeline."""
    actions: list[dict[str, Any]] = []

    # 1. Triggered SOs (distance <= 0 or marked TRIGGERED)
    for so in load_standing_orders():
        dist_str = so.get("current_distance", "0%").replace("%", "")
        try:
            dist = float(dist_str)
        except ValueError:
            continue
        if dist <= 0:
            actions.append({
                "priority": "ALTA",
                "ticker": so["ticker"],
                "reason": f"TRIGGERED — {so.get('notes', '')}"[:120],
                "source": "standing_order",
            })

    # 2. Earnings in next 7 days
    cal = load_calendar(days=7)
    for _, row in cal.iterrows():
        if row.get("type") == "earnings":
            actions.append({
                "priority": "ALTA",
                "ticker": row["ticker"],
                "reason": f"Earnings {row['date']} — {row.get('notes', '')}"[:120],
                "source": "calendar",
            })

    # 3. Active SOs near trigger (not already triggered, distance in 0–5%)
    for so in load_standing_orders():
        if so.get("category") != "ACTIVE":
            continue
        dist_str = so.get("current_distance", "100%").replace("%", "")
        try:
            dist = float(dist_str)
        except ValueError:
            continue
        if 0 < dist <= 5:
            actions.append({
                "priority": "MEDIA",
                "ticker": so["ticker"],
                "reason": f"Near trigger ({dist:.1f}% away)",
                "source": "standing_order",
            })

    return actions


@st.cache_data(ttl=3600)  # 1 hour
def compute_multi_fund_signals() -> pd.DataFrame:
    """Return tickers held by 2+ Spanish funds with fund attribution."""
    funds = load_spanish_funds()
    rows: dict[str, dict[str, Any]] = {}
    for fund_id, letter in funds.items():
        fund_name = letter.get("fund_name", fund_id)
        for pos in letter.get("positions", []):
            if pos.get("ticker_status") != "verified":
                continue
            ticker = pos.get("ticker")
            if not ticker:
                continue
            entry = rows.setdefault(ticker, {
                "ticker": ticker, "company_name": pos.get("company_name", ""),
                "fund_count": 0, "funds": [],
            })
            entry["fund_count"] += 1
            entry["funds"].append({
                "fund_id": fund_id,
                "fund_name": fund_name,
                "weight_pct": pos.get("weight_pct"),
                "action": pos.get("action"),
                "thesis_text": pos.get("thesis_text"),
            })
    multi = [row for row in rows.values() if row["fund_count"] >= 2]
    if not multi:
        return pd.DataFrame(columns=["ticker", "company_name", "fund_count", "funds"])
    return pd.DataFrame(multi)
