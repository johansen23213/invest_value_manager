# Dashboard v1 MVP Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a complete, operational Streamlit dashboard with 4 pages (Glance, Portfolio, Pipeline, Spanish Funds) deployed to Streamlit Cloud with Google OAuth whitelist and `share_mode` anonymization, validated page-by-page by the `elena-dashboard-ux` skill.

**Architecture:** Streamlit multi-page app. Single entry point `dashboard/app.py` sets up sidebar + share_mode toggle. Pages in `dashboard/pages/` auto-detected. Centralized `data_loader.py` exposes `@st.cache_data` cached loaders (pages never touch filesystem/yfinance directly). `components.py` holds COLOR constants + share_mode-aware formatters.

**Tech Stack:** Python 3.12, Streamlit 1.31+, Plotly, pandas, pyyaml, yfinance, pytest.

**Spec reference:** `docs/superpowers/specs/2026-04-21-dashboard-v1-design.md`

**Branch:** `sprint1/foundations` (current)

---

## Testing strategy note

**TDD applies strictly to `data_loader.py` and `components.py`** — both are pure functions or cached wrappers around pure functions. Testable without Streamlit runtime.

**Pages (`dashboard/pages/*.py`) are NOT unit-tested.** Streamlit's testing ecosystem is limited; unit testing `st.metric()` calls produces brittle tests with no real coverage. Instead, every page phase ends with:
1. **Manual smoke checklist** (runs on localhost, listed in each page task)
2. **Invocation of `elena-dashboard-ux` skill** for UX validation (APPROVED or APPROVED_WITH_CHANGES applied before merge)

Do not invent page-level unit tests. They waste time.

---

## Task ordering

Tasks in execution order. Each is self-contained and committable.

1. Foundation: replace existing `dashboard/app.py` + requirements.txt + delete obsolete pages
2. `components.py` — COLOR contract + money/pct helpers (TDD)
3. `data_loader.py` part 1 — portfolio + standing orders + paths (TDD)
4. `data_loader.py` part 2 — universe + spanish funds + calendar (TDD)
5. `data_loader.py` part 3 — macro + prices + compute helpers (TDD)
6. `app.py` entry point — sidebar nav + share_mode + glossary
7. Glance page (`1_🏠_Glance.py`) + Elena review
8. Portfolio page (`2_📊_Portfolio.py`) + Elena review
9. Pipeline page (`3_🎯_Pipeline.py`) + Elena review
10. Spanish Funds page (`4_🇪🇸_Spanish_Funds.py`) + Elena review
11. Streamlit Cloud deployment + OAuth whitelist
12. README + screenshots + handoff

---

## Task 1: Foundation — reset dashboard structure

**Files:**
- Delete: `dashboard/app.py` (old single-file multi-page structure, 127 lines)
- Create: `dashboard/app.py` (new stub — placeholder until Task 6)
- Create: `dashboard/requirements.txt`
- Modify: `dashboard/__init__.py` (add docstring)
- Create: `dashboard/pages/` directory (empty, populated in Tasks 7-10)

- [ ] **Step 1: Read the existing `dashboard/app.py` to confirm what we're replacing**

Run: `cat dashboard/app.py`
Note: old structure uses `st.sidebar.selectbox` + conditional dispatch. We're switching to Streamlit's native multi-page (files in `pages/` subdirectory).

- [ ] **Step 2: Delete the old app.py and create minimal stub**

```bash
rm dashboard/app.py
```

Create `dashboard/app.py`:

```python
"""ValueHunter Dashboard v1 — entry point.

The actual pages live in dashboard/pages/ and are auto-detected by Streamlit.
This file configures the page, sidebar, and shared state (share_mode).

Full setup wired in Task 6. This is a minimal stub.
"""
from __future__ import annotations

import streamlit as st


def main():
    st.set_page_config(
        page_title="ValueHunter",
        page_icon="🦅",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.title("🦅 ValueHunter")
    st.caption("Sub-project 0.5 Dashboard v1 MVP — setup in progress")
    st.info("Pages loading… Sidebar navigation coming in Task 6.")


if __name__ == "__main__":
    main()
```

- [ ] **Step 3: Create requirements.txt for Streamlit Cloud**

File: `dashboard/requirements.txt`

```
streamlit>=1.31.0
pandas>=2.2.0
plotly>=5.18.0
pyyaml>=6.0.0
yfinance>=0.2.36
```

Note: Streamlit Cloud uses this file (not pyproject.toml) for deploy-time dependency resolution. Keeping it separate from the main project deps is intentional.

- [ ] **Step 4: Update `dashboard/__init__.py`**

```python
"""ValueHunter Dashboard v1 — Streamlit app for daily fund operation + sharing."""
```

- [ ] **Step 5: Create empty pages directory**

```bash
mkdir -p dashboard/pages
touch dashboard/pages/.gitkeep
```

- [ ] **Step 6: Verify Streamlit runs locally**

Run: `streamlit run dashboard/app.py --server.headless true --server.port 8765 &` (background), then `sleep 3 && curl -s http://localhost:8765/_stcore/health` → expect `ok`.

Kill background process: `pkill -f "streamlit run dashboard"`

- [ ] **Step 7: Commit**

```bash
git add dashboard/app.py dashboard/requirements.txt dashboard/__init__.py dashboard/pages/.gitkeep
git rm dashboard/app.py  # if still in index from delete
git commit -m "chore(dashboard): reset dashboard to multi-page skeleton for v1 rewrite"
```

Note: if `git rm` fails (already removed), skip it.

---

## Task 2: `components.py` — COLOR contract + formatters + share_mode helpers

**Files:**
- Create: `dashboard/components.py`
- Create: `tests/test_dashboard_components.py`

- [ ] **Step 1: Write the failing test**

File: `tests/test_dashboard_components.py`

```python
"""Tests for dashboard components: COLOR contract + formatters + share_mode."""
from __future__ import annotations

import pytest

from dashboard.components import (
    COLOR,
    CONVICTION_COLORS,
    PIPELINE_COLORS,
    TIER_COLORS,
    is_hex_color,
    money,
    pct,
    pct_of_portfolio,
)


class TestColorContract:
    def test_color_keys_complete(self):
        expected = {"urgent_red", "positive_green", "warning_amber", "info_blue",
                    "neutral_grey", "tier_a_gold", "muted"}
        assert set(COLOR.keys()) == expected

    def test_all_colors_are_valid_hex(self):
        for name, value in COLOR.items():
            assert is_hex_color(value), f"{name} = {value} is not valid hex"

    def test_pipeline_colors_all_valid(self):
        expected_stages = {"R1_NEW", "R1_COMPLETE", "R2", "R3", "R4_READY", "ACTIVE", "ARCHIVED"}
        assert set(PIPELINE_COLORS.keys()) == expected_stages
        for stage, color in PIPELINE_COLORS.items():
            assert is_hex_color(color), f"{stage} color {color} invalid"

    def test_conviction_colors_three_levels(self):
        assert set(CONVICTION_COLORS.keys()) == {"1_fund", "2_funds", "3+_funds"}
        for level, color in CONVICTION_COLORS.items():
            assert is_hex_color(color)

    def test_tier_colors_abc(self):
        assert set(TIER_COLORS.keys()) == {"A", "B", "C"}
        for tier, color in TIER_COLORS.items():
            assert is_hex_color(color)


class TestIsHexColor:
    def test_valid_6_digit(self):
        assert is_hex_color("#3FA34D")

    def test_valid_3_digit(self):
        assert is_hex_color("#abc")

    def test_missing_hash(self):
        assert not is_hex_color("3FA34D")

    def test_bad_char(self):
        assert not is_hex_color("#3FA34Z")

    def test_wrong_length(self):
        assert not is_hex_color("#3FA34")


class TestMoney:
    def test_share_mode_off_returns_euro(self):
        assert money(10500, share_mode=False) == "€10,500"

    def test_share_mode_on_returns_dash(self):
        assert money(10500, share_mode=True) == "—"

    def test_zero_value_share_mode_off(self):
        assert money(0, share_mode=False) == "€0"

    def test_large_value_formatting(self):
        assert money(1_234_567, share_mode=False) == "€1,234,567"

    def test_negative_value(self):
        assert money(-500, share_mode=False) == "€-500"


class TestPctOfPortfolio:
    def test_basic(self):
        assert pct_of_portfolio(500, 10000) == "5.0%"

    def test_one_decimal(self):
        assert pct_of_portfolio(123, 10000) == "1.2%"

    def test_zero_total_returns_zero(self):
        assert pct_of_portfolio(100, 0) == "0.0%"


class TestPct:
    def test_positive_signed(self):
        assert pct(4.2) == "+4.2%"

    def test_negative_signed(self):
        assert pct(-2.5) == "-2.5%"

    def test_zero_signed_positive(self):
        assert pct(0) == "+0.0%"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_dashboard_components.py -v`
Expected: FAIL — `ModuleNotFoundError: dashboard.components`.

- [ ] **Step 3: Create the components module**

File: `dashboard/components.py`

```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_dashboard_components.py -v`
Expected: PASS (22 tests).

- [ ] **Step 5: Commit**

```bash
git add dashboard/components.py tests/test_dashboard_components.py
git commit -m "feat(dashboard): add COLOR contract + share_mode formatters"
```

---

## Task 3: `data_loader.py` part 1 — paths + portfolio + standing orders

**Files:**
- Create: `dashboard/data_loader.py`
- Create: `tests/test_dashboard_data_loader.py`
- Create: `tests/fixtures/dashboard/portfolio_sample.yaml`
- Create: `tests/fixtures/dashboard/standing_orders_sample.yaml`

- [ ] **Step 1: Create fixture files**

File: `tests/fixtures/dashboard/portfolio_sample.yaml`

```yaml
positions:
  - ticker: MORN
    name: Morningstar Inc
    shares: 2.9
    avg_cost_usd: 160.76
    invested_usd: 466.20
    tier: A
    conviction: HIGH
    fair_value: 195
    sector: Financial Data
    geo: US
cash_usd: 6860.44
```

File: `tests/fixtures/dashboard/standing_orders_sample.yaml`

```yaml
standing_orders:
  - ticker: RACE.MI
    action: BUY
    category: ACTIVE
    trigger: "<=EUR 295"
    current_distance: "2.2%"
    size_eur: 350
    fair_value: "EUR 355"
    mos_at_trigger: "16.9%"
    tier: "A (QS 82/84)"
    notes: "Committee approved."
  - ticker: ALFA.L
    action: BUY
    category: GATED
    trigger: "<=165 GBp"
    current_distance: "-3.4%"
    size_eur: 350
    fair_value: "240 GBp"
    mos_at_trigger: "33.6%"
    tier: "A (QS 83)"
    notes: "Triggered, Hormuz gates cleared."
```

- [ ] **Step 2: Write the failing test**

File: `tests/test_dashboard_data_loader.py`

```python
"""Tests for dashboard/data_loader.py."""
from __future__ import annotations

from pathlib import Path

import pytest

from dashboard.data_loader import (
    load_portfolio,
    load_standing_orders,
    project_root,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "dashboard"


class TestProjectRoot:
    def test_project_root_returns_invest_value_manager_dir(self):
        root = project_root()
        assert root.name == "invest_value_manager"
        assert (root / "pyproject.toml").exists()


class TestLoadPortfolio:
    def test_loads_positions_and_cash(self, monkeypatch):
        monkeypatch.setattr(
            "dashboard.data_loader._portfolio_path",
            lambda: FIXTURES / "portfolio_sample.yaml",
        )
        load_portfolio.clear()  # clear cache
        data = load_portfolio()
        assert data is not None
        assert len(data["positions"]) == 1
        assert data["positions"][0]["ticker"] == "MORN"
        assert data["cash_usd"] == 6860.44

    def test_returns_empty_skeleton_when_missing(self, monkeypatch, tmp_path):
        missing = tmp_path / "nope.yaml"
        monkeypatch.setattr("dashboard.data_loader._portfolio_path", lambda: missing)
        load_portfolio.clear()
        data = load_portfolio()
        assert data == {"positions": [], "cash_usd": 0.0}


class TestLoadStandingOrders:
    def test_loads_all_orders(self, monkeypatch):
        monkeypatch.setattr(
            "dashboard.data_loader._standing_orders_path",
            lambda: FIXTURES / "standing_orders_sample.yaml",
        )
        load_standing_orders.clear()
        orders = load_standing_orders()
        assert len(orders) == 2
        tickers = {o["ticker"] for o in orders}
        assert tickers == {"RACE.MI", "ALFA.L"}

    def test_empty_list_when_missing(self, monkeypatch, tmp_path):
        missing = tmp_path / "nope.yaml"
        monkeypatch.setattr("dashboard.data_loader._standing_orders_path", lambda: missing)
        load_standing_orders.clear()
        orders = load_standing_orders()
        assert orders == []
```

- [ ] **Step 3: Run test to verify it fails**

Run: `pytest tests/test_dashboard_data_loader.py -v`
Expected: FAIL — `ModuleNotFoundError: dashboard.data_loader`.

- [ ] **Step 4: Create the data_loader module (part 1)**

File: `dashboard/data_loader.py`

```python
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
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `pytest tests/test_dashboard_data_loader.py -v`
Expected: PASS (4 tests).

- [ ] **Step 6: Commit**

```bash
git add dashboard/data_loader.py tests/test_dashboard_data_loader.py tests/fixtures/dashboard/
git commit -m "feat(dashboard): add data_loader with portfolio + standing orders loaders"
```

---

## Task 4: `data_loader.py` part 2 — universe + spanish funds + calendar

**Files:**
- Modify: `dashboard/data_loader.py` (add 3 functions)
- Modify: `tests/test_dashboard_data_loader.py` (add tests)
- Create: `tests/fixtures/dashboard/quality_universe_sample.yaml`
- Create: `tests/fixtures/dashboard/calendar_sample.yaml`
- Create: `tests/fixtures/dashboard/spanish_funds_sample/cobas/2026-Q1.json`
- Create: `tests/fixtures/dashboard/spanish_funds_sample/azvalor/2026-Q1.json`

- [ ] **Step 1: Create fixtures**

File: `tests/fixtures/dashboard/quality_universe_sample.yaml`

```yaml
quality_universe:
  companies:
    - ticker: INTU
      name: Intuit Inc.
      tier: B
      qs_tool: 77
      qs_adj: 72
      sector: Financial Technology
      direction: long
      currency: USD
      current_price: 433.35
      entry_price: 290.0
      fair_value: 395.0
      distance_to_entry: 49.4
      distance_delta: 17.8
      pipeline_status: R3_COMPLETE
      notes: "DA STRONG COUNTER."
      thesis_path: thesis/research/INTU/thesis.md
    - ticker: ATYM.L
      name: Atalaya Mining
      tier: A
      qs_tool: 83
      qs_adj: 83
      sector: Mining
      direction: long
      currency: GBP
      current_price: 159.40
      entry_price: 165.0
      fair_value: 240.0
      distance_to_entry: -3.4
      distance_delta: 0
      pipeline_status: R4_READY
      notes: "Hormuz cleared."
      thesis_path: thesis/research/ALFA.L/thesis.md
```

File: `tests/fixtures/dashboard/calendar_sample.yaml`

```yaml
calendar:
  - date: "2026-04-24"
    type: earnings
    ticker: MEGP.L
    notes: "FY2025 results — 3rd attempt"
  - date: "2026-05-01"
    type: earnings
    ticker: ADBE
    notes: "Q2 earnings + CEO succession update"
  - date: "2026-06-15"
    type: catalyst
    ticker: NVO
    notes: "CagriSema phase 3 readout"
```

File: `tests/fixtures/dashboard/spanish_funds_sample/cobas/2026-Q1.json`

```json
{
  "fund_id": "cobas",
  "fund_name": "Cobas Selección",
  "quarter": "2026-Q1",
  "extracted_at": "2026-04-20T10:00:00Z",
  "extraction_model": "claude-sonnet-4-6",
  "source_url": "https://cobasam.com/q1-2026.pdf",
  "fund_return_pct": 4.2,
  "aum_eur": 2100000000,
  "positions": [
    {
      "company_name": "Atalaya Mining",
      "ticker": "ATYM.L",
      "ticker_status": "verified",
      "weight_pct": 7.3,
      "action": "maintained",
      "upside_pct": 45,
      "thesis_text": "Cobre estructuralmente escaso."
    }
  ]
}
```

File: `tests/fixtures/dashboard/spanish_funds_sample/azvalor/2026-Q1.json`

```json
{
  "fund_id": "azvalor",
  "fund_name": "AzValor Internacional",
  "quarter": "2026-Q1",
  "extracted_at": "2026-04-20T10:00:00Z",
  "extraction_model": "claude-sonnet-4-6",
  "source_url": "https://azvalor.com/q1-2026.pdf",
  "fund_return_pct": 5.1,
  "aum_eur": 1500000000,
  "positions": [
    {
      "company_name": "Atalaya Mining",
      "ticker": "ATYM.L",
      "ticker_status": "verified",
      "weight_pct": 5.1,
      "action": "increased",
      "upside_pct": 50,
      "thesis_text": "Permisos avanzando."
    }
  ]
}
```

- [ ] **Step 2: Write the failing tests**

Append to `tests/test_dashboard_data_loader.py`:

```python
from datetime import date

from dashboard.data_loader import (
    load_universe,
    load_spanish_funds,
    load_calendar,
)


class TestLoadUniverse:
    def test_returns_dataframe_with_expected_columns(self, monkeypatch):
        monkeypatch.setattr(
            "dashboard.data_loader._universe_path",
            lambda: FIXTURES / "quality_universe_sample.yaml",
        )
        load_universe.clear()
        df = load_universe()
        assert len(df) == 2
        for col in ("ticker", "name", "tier", "qs_tool", "pipeline_status", "distance_to_entry"):
            assert col in df.columns

    def test_empty_df_when_missing(self, monkeypatch, tmp_path):
        missing = tmp_path / "nope.yaml"
        monkeypatch.setattr("dashboard.data_loader._universe_path", lambda: missing)
        load_universe.clear()
        df = load_universe()
        assert len(df) == 0


class TestLoadCalendar:
    def test_filters_to_days_window(self, monkeypatch, tmp_path):
        monkeypatch.setattr(
            "dashboard.data_loader._calendar_path",
            lambda: FIXTURES / "calendar_sample.yaml",
        )
        # Pin "today" so the filter is deterministic
        monkeypatch.setattr("dashboard.data_loader._today", lambda: date(2026, 4, 21))
        load_calendar.clear()
        next_7 = load_calendar(days=7)
        assert len(next_7) == 1  # only MEGP.L within 7 days
        assert next_7.iloc[0]["ticker"] == "MEGP.L"

    def test_wider_window_includes_more(self, monkeypatch):
        monkeypatch.setattr(
            "dashboard.data_loader._calendar_path",
            lambda: FIXTURES / "calendar_sample.yaml",
        )
        monkeypatch.setattr("dashboard.data_loader._today", lambda: date(2026, 4, 21))
        load_calendar.clear()
        next_30 = load_calendar(days=30)
        assert len(next_30) == 2  # MEGP.L + ADBE

    def test_empty_when_missing(self, monkeypatch, tmp_path):
        missing = tmp_path / "nope.yaml"
        monkeypatch.setattr("dashboard.data_loader._calendar_path", lambda: missing)
        load_calendar.clear()
        df = load_calendar(days=30)
        assert len(df) == 0


class TestLoadSpanishFunds:
    def test_loads_latest_per_fund(self, monkeypatch):
        monkeypatch.setattr(
            "dashboard.data_loader._spanish_funds_root",
            lambda: FIXTURES / "spanish_funds_sample",
        )
        load_spanish_funds.clear()
        data = load_spanish_funds()
        assert "cobas" in data
        assert "azvalor" in data
        assert data["cobas"]["fund_name"] == "Cobas Selección"
        assert data["azvalor"]["quarter"] == "2026-Q1"

    def test_returns_empty_dict_when_dir_missing(self, monkeypatch, tmp_path):
        missing = tmp_path / "does_not_exist"
        monkeypatch.setattr("dashboard.data_loader._spanish_funds_root", lambda: missing)
        load_spanish_funds.clear()
        assert load_spanish_funds() == {}
```

- [ ] **Step 3: Run tests to verify they fail**

Run: `pytest tests/test_dashboard_data_loader.py -v`
Expected: FAIL — new functions + paths not defined yet.

- [ ] **Step 4: Extend data_loader.py**

Append to `dashboard/data_loader.py`:

```python
import json
from datetime import date, timedelta

import pandas as pd


def _universe_path() -> Path:
    return project_root() / "state" / "quality_universe.yaml"


def _calendar_path() -> Path:
    return project_root() / "state" / "calendar.yaml"


def _spanish_funds_root() -> Path:
    return project_root() / "knowledge_base" / "spanish_funds"


def _today() -> date:
    """Return today's date. Patched in tests for deterministic calendar filtering."""
    return date.today()


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
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `pytest tests/test_dashboard_data_loader.py -v`
Expected: PASS (10 tests total).

- [ ] **Step 6: Commit**

```bash
git add dashboard/data_loader.py tests/test_dashboard_data_loader.py tests/fixtures/dashboard/
git commit -m "feat(dashboard): add universe + calendar + spanish funds loaders"
```

---

## Task 5: `data_loader.py` part 3 — prices + macro + compute helpers

**Files:**
- Modify: `dashboard/data_loader.py`
- Modify: `tests/test_dashboard_data_loader.py`

- [ ] **Step 1: Write failing tests**

Append to `tests/test_dashboard_data_loader.py`:

```python
from unittest.mock import MagicMock, patch

from dashboard.data_loader import (
    compute_actions_today,
    compute_multi_fund_signals,
    load_macro,
    load_prices,
)


class TestLoadPrices:
    def test_returns_dict_keyed_by_ticker(self):
        # Patch yfinance to avoid real network
        mock_tickers = MagicMock()
        mock_tickers.tickers = {
            "MORN": MagicMock(info={"regularMarketPrice": 185.0}),
            "ATYM.L": MagicMock(info={"regularMarketPrice": 159.40}),
        }
        with patch("dashboard.data_loader.yf.Tickers", return_value=mock_tickers):
            load_prices.clear()
            prices = load_prices(("MORN", "ATYM.L"))
        assert prices["MORN"] == 185.0
        assert prices["ATYM.L"] == 159.40

    def test_missing_price_returns_none(self):
        mock_tickers = MagicMock()
        mock_tickers.tickers = {"FAKE.XX": MagicMock(info={})}
        with patch("dashboard.data_loader.yf.Tickers", return_value=mock_tickers):
            load_prices.clear()
            prices = load_prices(("FAKE.XX",))
        assert prices["FAKE.XX"] is None

    def test_empty_tuple_returns_empty_dict(self):
        load_prices.clear()
        assert load_prices(()) == {}


class TestLoadMacro:
    def test_returns_dict_from_tool_subprocess(self):
        fake_output = '{"vix": 19.1, "oil_wti": 87.19, "sp500": 7098.4, "gold": 4824, "dxy": 103.2}'
        with patch("dashboard.data_loader._run_macro_tool", return_value=fake_output):
            load_macro.clear()
            data = load_macro()
        assert data["vix"] == 19.1
        assert data["oil_wti"] == 87.19

    def test_returns_empty_dict_on_tool_failure(self):
        with patch("dashboard.data_loader._run_macro_tool", return_value=""):
            load_macro.clear()
            assert load_macro() == {}


class TestComputeActionsToday:
    def test_builds_prioritized_list(self, monkeypatch):
        # Minimal stubs for dependencies
        monkeypatch.setattr(
            "dashboard.data_loader.load_standing_orders",
            lambda: [
                {"ticker": "ALFA.L", "action": "BUY", "category": "GATED",
                 "current_distance": "-3.4%", "notes": "Hormuz cleared."},
                {"ticker": "RACE.MI", "action": "BUY", "category": "ACTIVE",
                 "current_distance": "2.2%", "notes": "—"},
            ],
        )
        monkeypatch.setattr("dashboard.data_loader.load_calendar", lambda days: pd.DataFrame(
            [{"date": date(2026, 4, 24), "type": "earnings", "ticker": "MEGP.L",
              "notes": "FY2025 results"}]
        ))
        compute_actions_today.clear()
        actions = compute_actions_today()
        assert len(actions) >= 2
        # Triggered SO (negative distance) should come before ACTIVE
        tickers = [a["ticker"] for a in actions]
        assert tickers.index("ALFA.L") < tickers.index("MEGP.L")


class TestComputeMultiFundSignals:
    def test_returns_tickers_in_two_or_more_funds(self, monkeypatch):
        monkeypatch.setattr("dashboard.data_loader.load_spanish_funds", lambda: {
            "cobas": {
                "fund_id": "cobas", "fund_name": "Cobas", "quarter": "2026-Q1",
                "positions": [
                    {"ticker": "ATYM.L", "ticker_status": "verified", "weight_pct": 7.3,
                     "action": "maintained", "thesis_text": "Cobre..."},
                    {"ticker": "TEF.MC", "ticker_status": "verified", "weight_pct": 3.0,
                     "action": "new", "thesis_text": "Telco turnaround..."},
                ],
            },
            "azvalor": {
                "fund_id": "azvalor", "fund_name": "AzValor", "quarter": "2026-Q1",
                "positions": [
                    {"ticker": "ATYM.L", "ticker_status": "verified", "weight_pct": 5.1,
                     "action": "increased", "thesis_text": "Permisos..."},
                ],
            },
        })
        compute_multi_fund_signals.clear()
        df = compute_multi_fund_signals()
        # Only ATYM.L is in 2+ funds
        tickers = df["ticker"].tolist()
        assert "ATYM.L" in tickers
        assert "TEF.MC" not in tickers  # only 1 fund
        atym_row = df[df["ticker"] == "ATYM.L"].iloc[0]
        assert atym_row["fund_count"] == 2

    def test_returns_empty_df_when_no_funds(self, monkeypatch):
        monkeypatch.setattr("dashboard.data_loader.load_spanish_funds", lambda: {})
        compute_multi_fund_signals.clear()
        df = compute_multi_fund_signals()
        assert len(df) == 0
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_dashboard_data_loader.py -v`
Expected: FAIL — new functions not defined.

- [ ] **Step 3: Extend data_loader.py**

Append to `dashboard/data_loader.py`:

```python
import subprocess

import yfinance as yf


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
```

- [ ] **Step 4: Run all data_loader tests**

Run: `pytest tests/test_dashboard_data_loader.py -v`
Expected: PASS (all tests, ~18 total).

- [ ] **Step 5: Commit**

```bash
git add dashboard/data_loader.py tests/test_dashboard_data_loader.py
git commit -m "feat(dashboard): add prices + macro + action/multi-fund compute helpers"
```

---

## Task 6: `app.py` entry point — sidebar, share_mode, glossary

**Files:**
- Modify: `dashboard/app.py` (full rewrite of Task 1's stub)
- Create: `dashboard/sidebar.py` (extract sidebar logic)
- Create: `tests/test_dashboard_sidebar.py`

- [ ] **Step 1: Write failing test for sidebar helper**

File: `tests/test_dashboard_sidebar.py`

```python
"""Tests for sidebar helpers (share_mode resolution + URL param parsing)."""
from __future__ import annotations

from dashboard.sidebar import resolve_share_mode_from_params


class TestResolveShareMode:
    def test_share_param_1_enables(self):
        assert resolve_share_mode_from_params({"share": "1"}) is True

    def test_share_param_true_enables(self):
        assert resolve_share_mode_from_params({"share": "true"}) is True

    def test_share_param_absent_disables(self):
        assert resolve_share_mode_from_params({}) is False

    def test_share_param_0_disables(self):
        assert resolve_share_mode_from_params({"share": "0"}) is False

    def test_share_param_other_value_disables(self):
        assert resolve_share_mode_from_params({"share": "nope"}) is False
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_dashboard_sidebar.py -v`
Expected: FAIL — `ModuleNotFoundError: dashboard.sidebar`.

- [ ] **Step 3: Create sidebar module**

File: `dashboard/sidebar.py`

```python
"""Sidebar + glossary + share_mode for the dashboard."""
from __future__ import annotations

from typing import Mapping

import streamlit as st

from dashboard.data_loader import load_portfolio  # for freshness hint


GLOSSARY_TERMS: list[tuple[str, str]] = [
    ("QS", "Quality Score — composite quality metric (0-100) combining financial strength, growth, moat, capital allocation."),
    ("MoS", "Margin of Safety — percentage the current price is below Fair Value."),
    ("FV", "Fair Value — intrinsic value estimate per share."),
    ("E[CAGR]", "Expected Compound Annual Growth Rate to Fair Value."),
    ("Tier", "Quality tier (A ≥75 QS, B 55-74, C 35-54). Below 35 = do not buy."),
    ("R1-R4", "Adversarial buy pipeline rounds (parallel analysis → devil's advocate → resolution → committee)."),
    ("KC", "Kill Condition — pre-defined scenario that invalidates a thesis."),
    ("SO", "Standing Order — pre-approved buy/sell trigger with price level."),
    ("Conviction", "Number of Spanish value funds that currently hold a ticker (1/2/3+)."),
]


def resolve_share_mode_from_params(params: Mapping[str, str]) -> bool:
    """Parse share_mode from URL query params. `?share=1` or `?share=true` → True."""
    val = params.get("share", "").lower().strip()
    return val in ("1", "true")


def render_sidebar() -> None:
    """Render the persistent sidebar: settings, glossary, freshness."""
    with st.sidebar:
        st.markdown("### ⚙️ Settings")
        # Initialize share_mode on first load from URL param
        if "share_mode_initialized" not in st.session_state:
            params = st.query_params.to_dict() if hasattr(st, "query_params") else {}
            st.session_state.share_mode = resolve_share_mode_from_params(params)
            st.session_state.share_mode_initialized = True

        st.session_state.share_mode = st.checkbox(
            "Share mode (hide €)",
            value=st.session_state.share_mode,
            help="Anonymizes absolute € values for external sharing. % always visible.",
        )

        if st.button("🔄 Refresh data", use_container_width=True):
            st.cache_data.clear()
            st.rerun()

        st.caption(f"Share mode: {'ON' if st.session_state.share_mode else 'OFF'}")

        st.markdown("---")
        with st.expander("📖 Glossary", expanded=False):
            for term, definition in GLOSSARY_TERMS:
                st.markdown(f"**{term}** — {definition}")

        st.markdown("---")
        st.caption("🦅 ValueHunter Dashboard v1")
        st.caption("Desktop-optimized. Mobile acceptable.")
```

- [ ] **Step 4: Replace `dashboard/app.py`**

File: `dashboard/app.py` (overwrite Task 1's stub)

```python
"""ValueHunter Dashboard v1 — entry point.

Streamlit multi-page app. Pages auto-detected from dashboard/pages/.
This file:
- Sets the global page config (title, icon, layout).
- Renders the sidebar (settings, glossary, share_mode toggle).
- Shows a landing blurb when the user lands on / (before picking a page).
"""
from __future__ import annotations

import streamlit as st

from dashboard.sidebar import render_sidebar


def main() -> None:
    st.set_page_config(
        page_title="ValueHunter",
        page_icon="🦅",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    render_sidebar()

    st.title("🦅 ValueHunter")
    st.caption("Multi-agent investment analysis system — Dashboard v1")
    st.markdown(
        "Select a page from the sidebar:\n\n"
        "- **🏠 Glance** — morning operator glance (SOs, earnings, actions today)\n"
        "- **📊 Portfolio** — active positions, exposure, allocation\n"
        "- **🎯 Pipeline** — quality universe + adversarial pipeline funnel\n"
        "- **🇪🇸 Spanish Funds** — holdings from 5 Spanish value funds"
    )


if __name__ == "__main__":
    main()
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `pytest tests/test_dashboard_sidebar.py -v`
Expected: PASS (5 tests).

- [ ] **Step 6: Smoke test Streamlit runs**

Run: `streamlit run dashboard/app.py --server.headless true --server.port 8765 &`, then `sleep 4 && curl -s http://localhost:8765/_stcore/health`, expect `ok`. Kill: `pkill -f "streamlit run dashboard"`.

- [ ] **Step 7: Commit**

```bash
git add dashboard/app.py dashboard/sidebar.py tests/test_dashboard_sidebar.py
git commit -m "feat(dashboard): add entry point + sidebar with share_mode + glossary"
```

---

## Task 7: Glance page (`1_🏠_Glance.py`) + Elena review

**Files:**
- Create: `dashboard/pages/1_🏠_Glance.py`

Note: Streamlit's multi-page routing picks up files starting with a digit + underscore. Emoji in filename is rendered in sidebar nav. Use file literal name exactly.

- [ ] **Step 1: Create the Glance page**

File: `dashboard/pages/1_🏠_Glance.py`

```python
"""🏠 Glance — morning operator glance."""
from __future__ import annotations

import streamlit as st

from dashboard.components import COLOR, money, pct
from dashboard.data_loader import (
    compute_actions_today,
    load_calendar,
    load_macro,
    load_portfolio,
    load_prices,
    load_standing_orders,
)
from dashboard.sidebar import render_sidebar


st.set_page_config(page_title="Glance · ValueHunter", page_icon="🏠", layout="wide")
render_sidebar()

share_mode = st.session_state.get("share_mode", False)

st.title("🏠 Morning Glance")

# ---------------------------------------------------------------------------
# Header metrics bar
# ---------------------------------------------------------------------------
portfolio = load_portfolio()
positions = portfolio.get("positions", [])
cash_usd = portfolio.get("cash_usd", 0.0)
total_value = cash_usd + sum(p.get("invested_usd", 0) or 0 for p in positions)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Portfolio value", money(total_value, share_mode) if total_value else "—")
col2.metric("Cash", f"{(cash_usd / total_value * 100 if total_value else 0):.0f}%")
col3.metric("Positions", len(positions))
col4.metric("Shorts", 0)  # placeholder

st.markdown("---")

# ---------------------------------------------------------------------------
# Three alert panels
# ---------------------------------------------------------------------------
panel_left, panel_mid, panel_right = st.columns(3)

with panel_left:
    st.markdown("### 🔴 Triggered SOs")
    triggered = [
        so for so in load_standing_orders()
        if str(so.get("current_distance", "0%")).replace("%", "").lstrip("-").replace(".", "").isdigit()
        and float(str(so.get("current_distance", "0%")).replace("%", "")) <= 0
    ]
    if triggered:
        for so in triggered[:5]:
            st.markdown(
                f"- **{so['ticker']}** {so.get('trigger', '')} "
                f"<span style='color:{COLOR['urgent_red']}'>●</span>",
                unsafe_allow_html=True,
            )
    else:
        st.caption("No SOs triggered.")

    near = [
        so for so in load_standing_orders()
        if so.get("category") == "ACTIVE"
        and str(so.get("current_distance", "100%")).replace("%", "").replace(".", "").isdigit()
        and 0 < float(str(so.get("current_distance", "100%")).replace("%", "")) <= 5
    ]
    if near:
        with st.expander(f"+ {len(near)} near trigger"):
            for so in near:
                st.markdown(f"- {so['ticker']} ({so.get('current_distance', '?')})")

with panel_mid:
    st.markdown("### 📅 Earnings (7d)")
    cal = load_calendar(days=7)
    earnings = cal[cal["type"] == "earnings"] if "type" in cal.columns else cal
    if len(earnings) == 0:
        st.caption("No earnings in next 7 days.")
    else:
        for _, row in earnings.iterrows():
            st.markdown(f"- **{row['ticker']}** — {row['date']}")
            st.caption(str(row.get("notes", ""))[:80])

with panel_right:
    st.markdown("### ⚠️ Macro")
    macro = load_macro()
    if not macro:
        st.caption("Macro data unavailable.")
    else:
        vix = macro.get("vix")
        oil = macro.get("oil_wti")
        if vix is not None:
            interp = "constructive" if vix < 20 else "caution" if vix < 30 else "risk-off"
            st.markdown(f"- VIX **{vix:.1f}** — {interp}")
        if oil is not None:
            st.markdown(f"- Oil WTI **${oil:.0f}**")
        sp = macro.get("sp500")
        if sp is not None:
            st.markdown(f"- S&P 500 **{sp:,.0f}**")

st.markdown("---")

# ---------------------------------------------------------------------------
# Top actions
# ---------------------------------------------------------------------------
st.markdown("### 🎯 Top actions today")
actions = compute_actions_today()
if not actions:
    st.info("No priority actions detected.")
else:
    for i, action in enumerate(actions[:10], start=1):
        prio = action.get("priority", "MEDIA")
        prio_color = COLOR["urgent_red"] if prio == "ALTA" else COLOR["warning_amber"]
        st.markdown(
            f"{i}. <span style='color:{prio_color}'>[{prio}]</span> "
            f"**{action['ticker']}** — {action.get('reason', '')}",
            unsafe_allow_html=True,
        )

st.markdown("---")

# ---------------------------------------------------------------------------
# Kill conditions + pending events placeholders
# (full data layer comes from thesis parsing — deferred to v2)
# ---------------------------------------------------------------------------
kc_col, pe_col = st.columns(2)
with kc_col:
    st.markdown("### 🔴 Kill conditions")
    st.caption(
        "Kill condition proximity tracking requires thesis parsing (not yet implemented). "
        "See thesis/active/*/thesis.md for KC details."
    )
with pe_col:
    st.markdown("### ⏳ Pending events")
    st.caption("Manual tracking via notes in thesis files for now.")

st.caption(f"Share mode: {'ON (€ hidden)' if share_mode else 'OFF'}")
```

- [ ] **Step 2: Smoke test the page**

Run: `streamlit run dashboard/app.py --server.headless true --server.port 8765 &`, then `sleep 4 && curl -s http://localhost:8765/_stcore/health`, expect `ok`. Open browser manually at http://localhost:8765 and click 🏠 Glance in sidebar. Verify:
- [ ] Page loads without errors
- [ ] Header metrics display
- [ ] Three alert panels render (even if empty state captions)
- [ ] Top actions list displays
- [ ] Share mode toggle from sidebar hides € when ON

Kill: `pkill -f "streamlit run dashboard"`.

- [ ] **Step 3: Invoke Elena UX review**

Dispatch a subagent with the `elena-dashboard-ux` skill, passing the page file and the smoke test results as context. Require APPROVED or APPROVED_WITH_CHANGES with fixes applied before commit.

Pseudo-invocation:
```
Agent(description="Elena UX review Glance", subagent_type="general-purpose", model="sonnet",
      prompt="You are Elena per .claude/skills/elena-dashboard-ux/SKILL.md. Review the
              implemented Glance page at dashboard/pages/1_🏠_Glance.py. Verdict required:
              APPROVED | APPROVED_WITH_CHANGES (list fixes) | NEEDS_REDESIGN.")
```

If APPROVED_WITH_CHANGES, apply fixes, re-smoke, re-dispatch until APPROVED.

- [ ] **Step 4: Commit**

```bash
git add "dashboard/pages/1_🏠_Glance.py"
git commit -m "feat(dashboard): add Glance page (morning operator view)"
```

---

## Task 8: Portfolio page (`2_📊_Portfolio.py`) + Elena review

**Files:**
- Create: `dashboard/pages/2_📊_Portfolio.py`

- [ ] **Step 1: Create the Portfolio page**

File: `dashboard/pages/2_📊_Portfolio.py`

```python
"""📊 Portfolio — active positions, exposure, allocation."""
from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

from dashboard.components import COLOR, TIER_COLORS, money, pct, pct_of_portfolio
from dashboard.data_loader import load_portfolio, load_prices
from dashboard.sidebar import render_sidebar


st.set_page_config(page_title="Portfolio · ValueHunter", page_icon="📊", layout="wide")
render_sidebar()
share_mode = st.session_state.get("share_mode", False)

st.title("📊 Portfolio")

portfolio = load_portfolio()
positions = portfolio.get("positions", [])
cash_usd = portfolio.get("cash_usd", 0.0)

if not positions:
    st.info("No active positions. Portfolio state file is empty or missing.")
    st.stop()

# Fetch live prices for each position
tickers = tuple(p["ticker"] for p in positions if p.get("ticker"))
prices = load_prices(tickers)

# Enrich positions with current value + P&L
enriched = []
for p in positions:
    ticker = p.get("ticker")
    price = prices.get(ticker)
    invested = p.get("invested_usd", 0) or 0
    shares = p.get("shares", 0) or 0
    current_value = (price * shares) if (price and shares) else 0
    pnl_pct = ((current_value - invested) / invested * 100) if invested else 0
    enriched.append({
        "ticker": ticker,
        "name": p.get("name", ""),
        "tier": p.get("tier", ""),
        "sector": p.get("sector", ""),
        "geo": p.get("geo", ""),
        "invested_usd": invested,
        "current_value_usd": current_value,
        "pnl_pct": pnl_pct,
        "fair_value": p.get("fair_value", 0),
        "conviction": p.get("conviction", ""),
    })

total_value = cash_usd + sum(e["current_value_usd"] for e in enriched)
total_invested = sum(e["invested_usd"] for e in enriched)
total_pnl_pct = ((total_value - cash_usd - total_invested) / total_invested * 100) if total_invested else 0

# ---------------------------------------------------------------------------
# Metrics row
# ---------------------------------------------------------------------------
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Portfolio value", money(total_value, share_mode))
c2.metric("P&L", pct(total_pnl_pct))
c3.metric("Cash", pct_of_portfolio(cash_usd, total_value))
c4.metric("Positions", len(enriched))
c5.metric("Net exposure", pct_of_portfolio(total_value - cash_usd, total_value))

st.markdown("---")

# ---------------------------------------------------------------------------
# Filters + column toggle
# ---------------------------------------------------------------------------
filter_col, toggle_col, reset_col = st.columns([2, 1, 1])
with filter_col:
    sectors = sorted({e["sector"] for e in enriched if e["sector"]})
    sector_filter = st.selectbox("Sector filter", ["All"] + sectors)
with toggle_col:
    show_details = st.checkbox("Show details (entry, FV, MoS)", value=False)
with reset_col:
    if st.button("Reset"):
        st.rerun()

rows = enriched if sector_filter == "All" else [e for e in enriched if e["sector"] == sector_filter]

# ---------------------------------------------------------------------------
# Primary table (share_mode aware)
# ---------------------------------------------------------------------------
df = pd.DataFrame(rows)
if share_mode:
    # Hide absolute $ columns
    df["value"] = df["current_value_usd"].apply(lambda v: pct_of_portfolio(v, total_value))
    primary_cols = ["ticker", "name", "tier", "value", "pnl_pct", "conviction"]
else:
    df["invested"] = df["invested_usd"].apply(lambda v: f"${v:,.0f}")
    df["value"] = df["current_value_usd"].apply(lambda v: f"${v:,.0f}")
    primary_cols = ["ticker", "name", "tier", "value", "pnl_pct", "conviction"]

if show_details:
    primary_cols = primary_cols + ["fair_value"]
    df["fair_value"] = df["fair_value"].apply(lambda v: f"${v:,.0f}" if v else "—")

column_config = {
    "tier": st.column_config.TextColumn("Tier", help="Quality tier A/B/C (≥75 / 55-74 / 35-54)."),
    "pnl_pct": st.column_config.NumberColumn("P&L %", format="%+.1f%%"),
    "fair_value": st.column_config.TextColumn("FV", help="Fair Value estimate per share."),
    "conviction": st.column_config.TextColumn("Conviction"),
}
st.dataframe(
    df[primary_cols] if all(c in df.columns for c in primary_cols) else df,
    use_container_width=True,
    hide_index=True,
    column_config=column_config,
)

# ---------------------------------------------------------------------------
# Allocation charts
# ---------------------------------------------------------------------------
st.markdown("### Allocation")
chart_col1, chart_col2 = st.columns(2)
with chart_col1:
    sector_agg = df.groupby("sector")["current_value_usd"].sum().reset_index()
    if len(sector_agg):
        fig = px.pie(sector_agg, names="sector", values="current_value_usd", hole=0.4)
        fig.update_layout(height=320, margin=dict(t=10, b=10, l=10, r=10))
        st.plotly_chart(fig, use_container_width=True)
with chart_col2:
    if "geo" in df.columns:
        geo_agg = df.groupby("geo")["current_value_usd"].sum().reset_index()
        if len(geo_agg):
            fig = px.bar(geo_agg, x="geo", y="current_value_usd", labels={"current_value_usd": "USD" if not share_mode else "—"})
            fig.update_layout(height=320, margin=dict(t=10, b=10, l=10, r=10))
            st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------------------------------
# Shorts placeholder
# ---------------------------------------------------------------------------
st.markdown("### Shorts")
st.caption(
    "No short positions currently active. The system opens shorts when identifying "
    "overvalued or structurally fragile companies with a dated catalyst."
)

# Footer
with st.expander("Data sources"):
    st.caption("portfolio/current.yaml · live prices via yfinance (15 min cache)")
```

- [ ] **Step 2: Smoke test**

Run Streamlit as in Task 7 Step 2. Verify on Portfolio page:
- [ ] Loads without errors
- [ ] Metrics row shows 5 metrics
- [ ] Table renders with the 6-7 primary columns
- [ ] Sector filter changes rows shown
- [ ] Show details checkbox adds FV column
- [ ] Share mode hides absolute $
- [ ] Allocation charts display

Kill Streamlit.

- [ ] **Step 3: Invoke Elena UX review**

Same pattern as Task 7 Step 3, applied to Portfolio page.

- [ ] **Step 4: Commit**

```bash
git add "dashboard/pages/2_📊_Portfolio.py"
git commit -m "feat(dashboard): add Portfolio page with allocation + share_mode"
```

---

## Task 9: Pipeline page (`3_🎯_Pipeline.py`) + Elena review

**Files:**
- Create: `dashboard/pages/3_🎯_Pipeline.py`

- [ ] **Step 1: Create the Pipeline page**

File: `dashboard/pages/3_🎯_Pipeline.py`

```python
"""🎯 Pipeline — quality universe + adversarial pipeline funnel."""
from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from dashboard.components import (
    COLOR,
    CONVICTION_COLORS,
    PIPELINE_COLORS,
    TIER_COLORS,
)
from dashboard.data_loader import (
    compute_multi_fund_signals,
    load_universe,
)
from dashboard.sidebar import render_sidebar


st.set_page_config(page_title="Pipeline · ValueHunter", page_icon="🎯", layout="wide")
render_sidebar()

st.title("🎯 Pipeline & Universe")

df = load_universe()
if len(df) == 0:
    st.info("Quality universe is empty or unavailable.")
    st.stop()

# Enrich with conviction from spanish fund signals
multi_fund = compute_multi_fund_signals()
ticker_to_conviction: dict[str, str] = {}
ticker_to_funds: dict[str, list[str]] = {}
for _, row in multi_fund.iterrows():
    count = row["fund_count"]
    label = "3+_funds" if count >= 3 else "2_funds"
    ticker_to_conviction[row["ticker"]] = label
    ticker_to_funds[row["ticker"]] = [f["fund_id"] for f in row["funds"]]

df["conviction_signal"] = df["ticker"].map(lambda t: ticker_to_conviction.get(t, "1_fund"))

# ---------------------------------------------------------------------------
# Metrics row
# ---------------------------------------------------------------------------
c1, c2, c3, c4, c5 = st.columns(5)
universe_size = len(df)
c1.metric("Universe size", universe_size)
c2.metric("Tier A", (df["tier"] == "A").sum())
c3.metric("Actionable (entry ≤5%)", (df["distance_to_entry"].abs() <= 5).sum())
r1_complete = (df["pipeline_status"] == "R1_COMPLETE").sum()
c4.metric("R1_COMPLETE", f"{r1_complete}/{universe_size}")
r4_ready = (df["pipeline_status"] == "R4_READY").sum()
c5.metric("R4_READY", r4_ready)

st.markdown("---")

# ---------------------------------------------------------------------------
# Funnel
# ---------------------------------------------------------------------------
st.markdown("### Pipeline funnel")
with st.expander("What is the pipeline?", expanded=False):
    st.markdown(
        "Each company enters at **R1_NEW** after screening. Parallel adversarial rounds "
        "(R1 analysis → R2 devil's advocate → R3 resolution → R4 committee) progressively "
        "validate the thesis. **R4_READY** means the committee has approved and the company "
        "is waiting for entry price. **ACTIVE** means it's an open portfolio position."
    )

pipeline_order = ["R1_NEW", "R1_COMPLETE", "R2", "R3", "R4_READY", "ACTIVE"]
counts = [int((df["pipeline_status"] == stage).sum()) for stage in pipeline_order]
fig = go.Figure(go.Funnel(
    y=pipeline_order,
    x=counts,
    marker={"color": [PIPELINE_COLORS.get(s, COLOR["muted"]) for s in pipeline_order]},
    textinfo="value+percent previous",
))
fig.update_layout(height=320, margin=dict(t=20, b=10, l=80, r=10))
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------------------------------
# Filters
# ---------------------------------------------------------------------------
col1, col2, col3, col4 = st.columns([1, 1, 2, 1])
with col1:
    tier_filter = st.selectbox("Tier", ["All", "A", "B", "C"])
with col2:
    sector_filter = st.selectbox("Sector", ["All"] + sorted(df["sector"].dropna().unique().tolist()))
with col3:
    max_dist = st.slider("Max distance to entry (%)", 0, 100, 100)
with col4:
    if st.button("Reset filters"):
        st.rerun()

filtered = df.copy()
if tier_filter != "All":
    filtered = filtered[filtered["tier"] == tier_filter]
if sector_filter != "All":
    filtered = filtered[filtered["sector"] == sector_filter]
filtered = filtered[filtered["distance_to_entry"].abs() <= max_dist]

# ---------------------------------------------------------------------------
# Table
# ---------------------------------------------------------------------------
show_details = st.checkbox("Show details (QS, sector, funds)", value=False)
primary_cols = ["ticker", "name", "tier", "pipeline_status", "distance_to_entry", "conviction_signal"]
secondary_cols = ["qs_tool", "sector"]
cols = primary_cols + (secondary_cols if show_details else [])

column_config = {
    "tier": st.column_config.TextColumn("Tier", help="A ≥75, B 55-74, C 35-54, D <35 (not bought)."),
    "qs_tool": st.column_config.NumberColumn("QS", help="Quality Score 0-100."),
    "distance_to_entry": st.column_config.NumberColumn(
        "To entry %",
        help="Distance from current price to standing order trigger. Negative = at or below entry.",
        format="%.1f",
    ),
    "pipeline_status": st.column_config.TextColumn("Pipeline"),
    "conviction_signal": st.column_config.TextColumn(
        "Conviction",
        help="Spanish value fund overlap: 1/2/3+ funds hold this ticker.",
    ),
}

st.dataframe(
    filtered[[c for c in cols if c in filtered.columns]],
    use_container_width=True,
    hide_index=True,
    column_config=column_config,
)

st.caption(f"Showing {len(filtered)} of {len(df)} companies.")
```

- [ ] **Step 2: Smoke test**

Run Streamlit. Verify on Pipeline page:
- [ ] Page loads
- [ ] 5 metrics display
- [ ] Funnel chart renders with 6 stages
- [ ] Filters (tier, sector, max distance) change visible rows
- [ ] Reset filters button works
- [ ] Show details toggle adds columns
- [ ] Tooltips on column headers work

Kill Streamlit.

- [ ] **Step 3: Invoke Elena UX review**

Same pattern as Task 7 Step 3.

- [ ] **Step 4: Commit**

```bash
git add "dashboard/pages/3_🎯_Pipeline.py"
git commit -m "feat(dashboard): add Pipeline page with funnel + conviction signals"
```

---

## Task 10: Spanish Funds page (`4_🇪🇸_Spanish_Funds.py`) + Elena review

**Files:**
- Create: `dashboard/pages/4_🇪🇸_Spanish_Funds.py`

- [ ] **Step 1: Create the Spanish Funds page**

File: `dashboard/pages/4_🇪🇸_Spanish_Funds.py`

```python
"""🇪🇸 Spanish Funds — holdings from Cobas/AzValor/Magallanes/Horos/Valentum."""
from __future__ import annotations

from datetime import date

import pandas as pd
import streamlit as st

from dashboard.components import COLOR, CONVICTION_COLORS
from dashboard.data_loader import compute_multi_fund_signals, load_spanish_funds
from dashboard.sidebar import render_sidebar


st.set_page_config(page_title="Spanish Funds · ValueHunter", page_icon="🇪🇸", layout="wide")
render_sidebar()

st.title("🇪🇸 Spanish Value Funds")

funds = load_spanish_funds()
if not funds:
    st.info(
        "No Spanish fund data available. Run the weekly ingestion via "
        "`python -m scrapers.spanish_funds.cli --all` to populate."
    )
    st.stop()

# ---------------------------------------------------------------------------
# Top-level unique ticker count
# ---------------------------------------------------------------------------
unique_tickers = set()
for fund_id, letter in funds.items():
    for p in letter.get("positions", []):
        if p.get("ticker_status") == "verified" and p.get("ticker"):
            unique_tickers.add(p["ticker"])

c1, c2 = st.columns(2)
c1.metric("Funds processed", len(funds))
c2.metric("Unique tickers (verified)", len(unique_tickers))

st.markdown("---")

# ---------------------------------------------------------------------------
# Fund cards grid
# ---------------------------------------------------------------------------
st.markdown("### Fund overview")
fund_ids = ["cobas", "azvalor", "magallanes", "horos", "valentum"]
cols = st.columns(len(fund_ids))
for col, fid in zip(cols, fund_ids):
    letter = funds.get(fid)
    with col:
        if letter is None:
            st.markdown(f"**{fid.title()}**")
            st.caption("_No letter yet._")
            continue
        st.markdown(f"**{letter.get('fund_name', fid.title())}**")
        st.caption(f"Last: {letter.get('quarter', '?')}")
        aum = letter.get("aum_eur")
        ret = letter.get("fund_return_pct")
        if aum:
            aum_str = f"€{aum/1e9:.1f}B" if aum >= 1e9 else f"€{aum/1e6:.0f}M"
            st.caption(f"AuM: {aum_str}")
        if ret is not None:
            sign = "+" if ret >= 0 else ""
            st.caption(f"Return: {sign}{ret:.1f}%")
        st.caption(f"Positions: {len(letter.get('positions', []))}")
        src = letter.get("source_url")
        if src:
            st.markdown(f"[view letter ↗]({src})")

st.markdown("---")

# ---------------------------------------------------------------------------
# Multi-fund signals (HERO section — placed before per-fund tabs)
# ---------------------------------------------------------------------------
st.markdown("### 🔔 Multi-fund conviction signals")
st.caption("Tickers held by 2 or more Spanish value funds simultaneously.")

signals = compute_multi_fund_signals()
if len(signals) == 0:
    st.info("No multi-fund overlaps in the latest quarterly letters.")
else:
    for _, row in signals.iterrows():
        ticker = row["ticker"]
        count = row["fund_count"]
        label = "3+_funds" if count >= 3 else "2_funds"
        color = CONVICTION_COLORS[label]
        with st.expander(
            f"**{ticker}** — {row.get('company_name', '')} · **{count} funds**",
            expanded=False,
        ):
            fund_cols = st.columns(min(count, 3))
            for i, f in enumerate(row["funds"][:3]):
                with fund_cols[i]:
                    st.markdown(f"**{f.get('fund_name', f['fund_id'])}**")
                    weight = f.get("weight_pct")
                    action = f.get("action", "")
                    st.caption(
                        f"Weight: {weight:.1f}%" if weight is not None else "Weight: —"
                    )
                    st.caption(f"Action: {action}")
                    thesis = (f.get("thesis_text") or "")[:300]
                    if thesis:
                        st.markdown(f"> {thesis}")

st.markdown("---")

# ---------------------------------------------------------------------------
# Per-fund tabs with holdings table
# ---------------------------------------------------------------------------
st.markdown("### Per-fund holdings")
tabs = st.tabs([funds.get(fid, {}).get("fund_name", fid.title()) if funds.get(fid) else fid.title()
                for fid in fund_ids])
for tab, fid in zip(tabs, fund_ids):
    with tab:
        letter = funds.get(fid)
        if letter is None:
            st.caption("No letter processed yet.")
            continue
        positions = letter.get("positions", [])
        rows = []
        unverified = []
        for p in positions:
            if p.get("ticker_status") != "verified":
                unverified.append(p)
                continue
            rows.append({
                "company": p.get("company_name", ""),
                "ticker": p.get("ticker", ""),
                "weight_pct": p.get("weight_pct", None),
                "fund_view": p.get("action", ""),
                "thesis_snippet": (p.get("thesis_text") or "")[:200],
            })
        if rows:
            df = pd.DataFrame(rows)
            st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.caption("No verified holdings in this letter.")
        if unverified:
            with st.expander(f"⚠️ {len(unverified)} unverified ticker(s) pending resolution"):
                for p in unverified:
                    st.caption(f"- {p.get('company_name', '?')} (proposed: {p.get('ticker', '?')})")

st.markdown("---")
st.caption("Data source: knowledge_base/spanish_funds/*/*.json (latest quarter per fund)")
```

- [ ] **Step 2: Smoke test**

Run Streamlit. Verify on Spanish Funds page:
- [ ] Page loads
- [ ] Top metrics show counts
- [ ] 5 fund cards render (even if some say "No letter yet")
- [ ] Multi-fund signals section appears BEFORE per-fund tabs
- [ ] Tabs switch between funds
- [ ] Holdings table in each tab
- [ ] Unverified section expandable

Kill Streamlit.

- [ ] **Step 3: Invoke Elena UX review**

Same pattern as Task 7 Step 3.

- [ ] **Step 4: Commit**

```bash
git add "dashboard/pages/4_🇪🇸_Spanish_Funds.py"
git commit -m "feat(dashboard): add Spanish Funds page with multi-fund hero"
```

---

## Task 11: Streamlit Cloud deployment + OAuth whitelist

**Files:** none new (configuration is done via Streamlit Cloud UI)

- [ ] **Step 1: Create a GitHub issue or handoff note listing deploy steps**

This task is human-executed (can't be scripted). Document the steps clearly:

```markdown
# Dashboard Streamlit Cloud deploy checklist

1. Go to https://share.streamlit.io and log in with Joan's Google account.
2. Click "New app".
3. Fill in:
   - Repo: `johansen23213/invest_value_manager`
   - Branch: `sprint1/foundations`
   - Main file: `dashboard/app.py`
   - Python version: 3.12 (Advanced settings)
   - Requirements file: detect automatically from `dashboard/requirements.txt`
4. Click "Deploy".
5. Wait for build (first build ~3-5 min).
6. Verify app loads at assigned URL (will be something like
   `https://valuehunter-<hash>.streamlit.app`).
7. Open "Settings → Sharing → Restrict access".
8. Add Joan's email to whitelist. Deploy.
9. Verify Joan can access while an incognito session (not logged in) cannot.
10. Add colleague emails iteratively.
11. Document the final URL in `dashboard/README.md`.
```

- [ ] **Step 2: Run dashboard smoke locally before deploy**

Run all 4 pages locally via `streamlit run dashboard/app.py`. Verify:
- [ ] App starts
- [ ] All 4 pages accessible from sidebar
- [ ] No Python errors in terminal
- [ ] `?share=1` URL param activates share_mode (visit http://localhost:8501/?share=1)

- [ ] **Step 3: Verify `dashboard/requirements.txt` pins deps correctly**

Run: `cd /tmp && python3 -m venv venv_dashboard_test && source venv_dashboard_test/bin/activate && pip install -r /Volumes/Storage/Documents/Claude/value_hunter/invest_value_manager/dashboard/requirements.txt`
Expected: clean install with no conflict errors. Deactivate + delete `/tmp/venv_dashboard_test`.

- [ ] **Step 4: Commit the deploy checklist**

Create `dashboard/DEPLOY.md` with the checklist above:

```bash
# paste content from Step 1 into dashboard/DEPLOY.md
git add dashboard/DEPLOY.md
git commit -m "docs(dashboard): add Streamlit Cloud deploy checklist"
```

---

## Task 12: README + screenshots + handoff

**Files:**
- Create: `dashboard/README.md`

- [ ] **Step 1: Write dashboard README**

File: `dashboard/README.md`

```markdown
# ValueHunter Dashboard v1

Streamlit-based dashboard for ValueHunter daily fund operation and external sharing.

## Pages

- **🏠 Glance** — morning operator view: triggered SOs, earnings 7d, macro, top actions today.
- **📊 Portfolio** — active positions, allocation charts, P&L summary.
- **🎯 Pipeline** — quality universe with pipeline funnel + multi-fund conviction.
- **🇪🇸 Spanish Funds** — holdings from 5 Spanish value funds with multi-fund hero section.

## Running locally

```bash
cd invest_value_manager
pip install -r dashboard/requirements.txt
streamlit run dashboard/app.py
# open http://localhost:8501
```

## Share mode

Toggle "Share mode" in the sidebar, or append `?share=1` to the URL, to anonymize
absolute € values. Percentages and structural info remain visible.

## Deployed URL

Live instance (requires whitelisted Google account): see `DEPLOY.md` for setup and
the current URL (updated at deploy time).

## Data freshness

- Standing orders: 5 min cache.
- Prices (yfinance): 15 min cache.
- Universe, portfolio, spanish funds: 15 min cache.
- Macro: 1 h cache.
- Derived actions + multi-fund signals: 30-60 min cache.

Hit "🔄 Refresh data" in the sidebar to invalidate all caches.

## Data sync (Local → Remote)

The deployed dashboard reads repo files from GitHub. Local state changes
(new theses, portfolio updates, SOs) only reach the dashboard after
`git commit` + `git push` from the local workstation.

## Known limitations

- Mobile works but is not polished.
- Streamlit Cloud free tier RAM limit (1 GB) may constrain large universes.
- Real-time is not a goal — caches mean up to 60 min staleness.
- OAuth whitelist is managed manually in Streamlit Cloud settings.
```

- [ ] **Step 2: Add screenshots directory**

```bash
mkdir -p docs/dashboard_screenshots
touch docs/dashboard_screenshots/.gitkeep
```

Note: screenshots are captured manually from the live deployment after Task 11. One PNG per page, committed to `docs/dashboard_screenshots/{page_name}.png`.

- [ ] **Step 3: Commit**

```bash
git add dashboard/README.md docs/dashboard_screenshots/.gitkeep
git commit -m "docs(dashboard): add README + screenshots directory"
```

---

## Final verification

- [ ] **Run full test suite**

Run: `pytest tests/ --tb=short`
Expected: All tests pass. New tests added by this plan: ~30 across `test_dashboard_components.py`, `test_dashboard_data_loader.py`, `test_dashboard_sidebar.py`.

- [ ] **Verify all 4 pages render**

Run `streamlit run dashboard/app.py` locally, navigate to each page, check no errors.

- [ ] **Verify all Elena reviews resulted in APPROVED**

Each of Tasks 7-10 ended with an Elena verdict. Confirm the last verdict for each page was APPROVED (not APPROVED_WITH_CHANGES with unresolved fixes).

---

## Spec coverage check

| Spec section | Task(s) |
|---|---|
| Architecture | Task 1 (skeleton), Task 6 (entry point) |
| file structure | Tasks 1-12 follow it exactly |
| Glance page | Task 7 |
| Portfolio page | Task 8 |
| Pipeline page | Task 9 |
| Spanish Funds page | Task 10 |
| Data loaders with TTL | Tasks 3, 4, 5 |
| share_mode toggle + URL param | Task 6 (sidebar) |
| Color contract | Task 2 |
| Glossary sidebar | Task 6 |
| Elena UX validation per page | Tasks 7-10 Step 3 |
| Streamlit Cloud deploy | Task 11 |
| OAuth whitelist | Task 11 (manual step) |
| README + handoff | Task 12 |
| TDD on data_loader + components | Tasks 2-5 |
| Pages NOT unit tested (manual + Elena) | Clarified in "Testing strategy note" at top |

---

## Notes for implementer

- **Streamlit multi-page requires the emoji in the file name** for nice sidebar labels. If git/OS gives trouble with emoji filenames, fall back to `1_Glance.py` etc. and lose the emoji from the sidebar (functionally equivalent, cosmetically worse).
- **Elena UX review is a BLOCKING GATE per page** — do not mark Task 7-10 complete until she issues APPROVED. APPROVED_WITH_CHANGES → apply fixes → re-dispatch until APPROVED.
- **Pages must not import yfinance or read filesystem directly.** Enforce this in code review: if a page file contains `import yaml` or `import yfinance`, refactor to use `data_loader.py`.
- **Share mode is a session-state flag.** URL param only sets it at first render; after that, the sidebar toggle is authoritative for the session.

---

*Plan produced by `superpowers:writing-plans`. Implementation uses `superpowers:subagent-driven-development` or `superpowers:executing-plans`.*
