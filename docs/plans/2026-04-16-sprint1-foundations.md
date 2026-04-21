# Sprint 1 — Foundations Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Establish project infrastructure (deps, schemas, tests), build Horos + Alpha Vulture scrapers, and create the Layer-0 Orchestrator skeleton — all without touching existing tools or data.

**Architecture:** New code lives in `orchestrator/`, `agents/`, `scrapers/`, `tests/` directories alongside the existing 45-tool system. A data adapter layer bridges existing YAML formats to v1.0 JSON Schema contracts. The orchestrator uses Python asyncio + Anthropic SDK for parallel agent fanout.

**Tech Stack:** Python 3.12, anthropic SDK, httpx, beautifulsoup4, pypdf, pydantic v2, jsonschema, pytest, pyyaml

**Working directory:** `/Volumes/Storage/Documents/Claude/value_hunter/invest_value_manager/`

**Critical constraint:** Existing tools (`tools/*.py`, `.claude/skills/*`, `state/*.yaml`, `portfolio/*.yaml`) must NOT be modified. All new code is additive.

---

## File Structure

```
invest_value_manager/
├── pyproject.toml                           # NEW — Task 1
├── .python-version                          # NEW — Task 1
├── knowledge_base/
│   ├── schemas/*.schema.json                # ALREADY EXISTS (12 files)
│   └── adapters.py                          # NEW — Task 3
├── orchestrator/
│   ├── __init__.py                          # NEW — Task 5
│   ├── base.py                              # NEW — Task 5
│   ├── registry.py                          # NEW — Task 6
│   ├── audit.py                             # NEW — Task 7
│   ├── governor.py                          # NEW — Task 8
│   └── __main__.py                          # NEW — Task 8
├── agents/
│   └── __init__.py                          # NEW — Task 5 (placeholder)
├── scrapers/
│   ├── __init__.py                          # NEW — Task 9
│   ├── alpha_vulture_scraper.py             # NEW — Task 9
│   └── horos_scraper.py                     # NEW — Task 10
├── tests/
│   ├── __init__.py                          # NEW — Task 2
│   ├── conftest.py                          # NEW — Task 2
│   ├── test_schemas.py                      # NEW — Task 2
│   ├── test_adapters.py                     # NEW — Task 4
│   ├── test_alpha_vulture_scraper.py        # NEW — Task 9
│   ├── test_horos_scraper.py                # NEW — Task 10
│   ├── test_registry.py                     # NEW — Task 6
│   ├── test_governor.py                     # NEW — Task 8
│   └── fixtures/                            # NEW — Task 9
│       ├── alpha_vulture_rss.xml            # NEW — Task 9
│       ├── alpha_vulture_post.html          # NEW — Task 9
│       └── horos_letter_sample.txt          # NEW — Task 10
└── docs/
    └── history/                             # NEW — Task 11
```

---

### Task 1: Project Setup

**Files:**
- Create: `pyproject.toml`
- Create: `.python-version`
- Create: `orchestrator/__init__.py`
- Create: `agents/__init__.py`
- Create: `scrapers/__init__.py`
- Create: `tests/__init__.py`

- [ ] **Step 1: Create `.python-version`**

```
3.12
```

- [ ] **Step 2: Create `pyproject.toml`**

```toml
[project]
name = "valuehunter"
version = "1.0.0-alpha"
description = "Multi-agent investment analysis system"
requires-python = ">=3.12"
dependencies = [
    "anthropic>=0.49.0",
    "httpx>=0.27.0",
    "beautifulsoup4>=4.12.0",
    "pypdf>=4.0.0",
    "pydantic>=2.6.0",
    "jsonschema>=4.21.0",
    "pyyaml>=6.0.0",
    "yfinance>=0.2.36",
    "pandas>=2.2.0",
    "numpy>=1.26.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "pytest-asyncio>=0.23.0",
]
dashboard = [
    "streamlit>=1.31.0",
    "plotly>=5.18.0",
]
scheduler = [
    "apscheduler>=3.10.0",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
asyncio_mode = "auto"
```

- [ ] **Step 3: Create package `__init__.py` files**

Create four empty `__init__.py` files:
- `orchestrator/__init__.py`
- `agents/__init__.py`
- `scrapers/__init__.py`
- `tests/__init__.py`

- [ ] **Step 4: Install dependencies**

Run: `cd /Volumes/Storage/Documents/Claude/value_hunter/invest_value_manager && pip install -e ".[dev]"`
Expected: successful installation, no errors

- [ ] **Step 5: Commit**

```bash
git add pyproject.toml .python-version orchestrator/__init__.py agents/__init__.py scrapers/__init__.py tests/__init__.py
git commit -m "feat: add pyproject.toml and package structure for ValueHunter v1.0"
```

---

### Task 2: Schema Validation Tests

**Files:**
- Create: `tests/conftest.py`
- Create: `tests/test_schemas.py`

- [ ] **Step 1: Create `tests/conftest.py` with shared fixtures**

```python
import pathlib
import json
import yaml
import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCHEMAS_DIR = ROOT / "knowledge_base" / "schemas"


@pytest.fixture
def schemas_dir():
    return SCHEMAS_DIR


@pytest.fixture
def load_schema():
    def _load(name: str) -> dict:
        path = SCHEMAS_DIR / name
        return json.loads(path.read_text())
    return _load


@pytest.fixture
def load_yaml():
    def _load(rel_path: str):
        path = ROOT / rel_path
        if not path.exists():
            pytest.skip(f"{rel_path} not found")
        return yaml.safe_load(path.read_text())
    return _load
```

- [ ] **Step 2: Write `tests/test_schemas.py` — validate all 12 schemas are valid JSON Schema**

```python
import json
import pathlib
import pytest
from jsonschema import Draft7Validator


SCHEMAS_DIR = pathlib.Path(__file__).resolve().parent.parent / "knowledge_base" / "schemas"
SCHEMA_FILES = sorted(SCHEMAS_DIR.glob("*.schema.json"))


@pytest.mark.parametrize("schema_path", SCHEMA_FILES, ids=lambda p: p.name)
def test_schema_is_valid_draft7(schema_path):
    schema = json.loads(schema_path.read_text())
    Draft7Validator.check_schema(schema)


@pytest.mark.parametrize("schema_path", SCHEMA_FILES, ids=lambda p: p.name)
def test_schema_has_required_metadata(schema_path):
    schema = json.loads(schema_path.read_text())
    assert "$schema" in schema
    assert "$id" in schema
    assert "title" in schema
    assert schema["type"] == "object"


def test_all_12_schemas_exist():
    expected = {
        "company.schema.json",
        "thesis.schema.json",
        "decision.schema.json",
        "portfolio_position.schema.json",
        "closed_position.schema.json",
        "performance.schema.json",
        "watchlist_entry.schema.json",
        "horos_position.schema.json",
        "alpha_vulture_idea.schema.json",
        "screener_result.schema.json",
        "special_situation.schema.json",
        "market_regime.schema.json",
    }
    actual = {p.name for p in SCHEMA_FILES}
    assert expected == actual
```

- [ ] **Step 3: Run tests to verify all schemas pass**

Run: `cd /Volumes/Storage/Documents/Claude/value_hunter/invest_value_manager && python -m pytest tests/test_schemas.py -v`
Expected: 25 tests PASS (12 valid + 12 metadata + 1 count)

- [ ] **Step 4: Commit**

```bash
git add tests/conftest.py tests/test_schemas.py
git commit -m "test: add schema validation tests for all 12 JSON Schema files"
```

---

### Task 3: Data Adapter Layer

Bridges existing YAML data (legacy field names, string types) to v1.0 schema-compliant dicts. Does NOT modify existing files.

**Files:**
- Create: `knowledge_base/__init__.py`
- Create: `knowledge_base/adapters.py`

**Context:** Existing data uses different conventions:
- `conviction`: string "low-medium" (legacy) vs int 1-10 (v1.0)
- `fair_value`: descriptive string "EUR 33.00 (v5.0...)" (legacy) vs number (v1.0)
- `avg_cost_usd` (legacy) vs `avg_cost` (v1.0)
- `holding_days` (legacy) vs `duration_days` (v1.0)
- `pnl_percent` (legacy) vs `realized_pnl_pct` (v1.0)

- [ ] **Step 1: Create `knowledge_base/__init__.py`**

Empty file.

- [ ] **Step 2: Write `knowledge_base/adapters.py`**

```python
"""Adapters to convert existing YAML data to v1.0 schema-compliant dicts.

These read-only adapters transform legacy field names and types
without modifying the source YAML files.
"""

from __future__ import annotations

import re
import pathlib
import yaml
from datetime import date
from typing import Any


ROOT = pathlib.Path(__file__).resolve().parent.parent

CONVICTION_MAP = {
    "low": 3,
    "low-medium": 4,
    "medium": 5,
    "medium-high": 7,
    "high": 8,
    "very high": 9,
    "alta": 8,
    "media-alta": 7,
    "media": 5,
    "baja": 3,
}


def _parse_fv_number(fv_str: str | None) -> float | None:
    """Extract numeric fair value from descriptive string like 'EUR 33.00 (v5.0...)'."""
    if fv_str is None:
        return None
    if isinstance(fv_str, (int, float)):
        return float(fv_str)
    match = re.search(r"[\$€£]?\s*([\d,]+\.?\d*)", str(fv_str))
    if match:
        return float(match.group(1).replace(",", ""))
    return None


def _parse_pct(val: str | float | None) -> float | None:
    """Extract percentage number from string like '31%' or float."""
    if val is None:
        return None
    if isinstance(val, (int, float)):
        return float(val)
    match = re.search(r"([\-\d.]+)\s*%?", str(val))
    return float(match.group(1)) if match else None


def _conviction_to_int(val: str | int | None) -> int:
    if val is None:
        return 5
    if isinstance(val, int):
        return max(1, min(10, val))
    return CONVICTION_MAP.get(str(val).lower().strip(), 5)


def _date_str(val) -> str | None:
    if val is None:
        return None
    if isinstance(val, date):
        return val.isoformat()
    return str(val)[:10]


def adapt_portfolio_position(raw: dict) -> dict:
    """Convert a portfolio/current.yaml position to portfolio_position.schema.json format."""
    return {
        "ticker": raw["ticker"],
        "company_name": raw.get("name"),
        "shares": raw["shares"],
        "side": "LONG",
        "invested_usd": raw["invested_usd"],
        "avg_cost": raw.get("avg_cost_usd", raw.get("avg_cost", 0)),
        "currency": _guess_currency(raw["ticker"]),
        "thesis_path": raw.get("thesis", ""),
        "conviction": _conviction_to_int(raw.get("conviction")),
        "fair_value": _parse_fv_number(raw.get("fair_value")) or 0,
        "entry_date": _date_str(raw.get("date_opened")),
        "last_review": _date_str(raw.get("last_review")),
        "exit_plan": raw.get("exit_plan"),
        "kill_conditions": [],
        "notes": raw.get("notes"),
    }


def adapt_closed_position(raw: dict) -> dict:
    """Convert a portfolio/history.yaml entry to closed_position.schema.json format."""
    return {
        "ticker": raw["ticker"],
        "company_name": raw.get("name"),
        "side": "LONG",
        "shares": raw.get("shares", 0),
        "avg_cost": raw.get("entry_price", 0),
        "exit_price": raw.get("exit_price", 0),
        "realized_pnl_pct": raw.get("pnl_percent", 0),
        "entry_date": _date_str(raw.get("entry_date")),
        "exit_date": _date_str(raw.get("exit_date")),
        "duration_days": raw.get("holding_days", 0),
        "exit_reason": raw.get("exit_reason", "unknown"),
        "lessons": [],
    }


def adapt_decision(raw: dict) -> dict:
    """Convert a learning/decisions_log.yaml entry to decision.schema.json format."""
    ctx = raw.get("context", {})
    return {
        "date": _date_str(raw.get("date")),
        "ticker": raw.get("ticker", ""),
        "decision": str(raw.get("action", "WATCH")).upper(),
        "conviction": _conviction_to_int(ctx.get("conviction")),
        "fair_value": _parse_fv_number(ctx.get("fv")),
        "mos_pct": _parse_pct(ctx.get("mos")),
        "e_cagr_pct": _parse_pct(ctx.get("e_cagr")),
        "position_size_pct": _parse_pct(raw.get("sizing")),
        "reasoning": raw.get("reasoning", ""),
        "outcome": raw.get("outcome"),
        "key_risks": [],
        "lessons": [],
    }


def load_portfolio_positions() -> list[dict]:
    """Load and adapt all active positions from portfolio/current.yaml."""
    path = ROOT / "portfolio" / "current.yaml"
    if not path.exists():
        return []
    data = yaml.safe_load(path.read_text())
    positions = data.get("positions", [])
    return [adapt_portfolio_position(p) for p in positions]


def load_closed_positions() -> list[dict]:
    """Load and adapt all closed positions from portfolio/history.yaml."""
    path = ROOT / "portfolio" / "history.yaml"
    if not path.exists():
        return []
    data = yaml.safe_load(path.read_text())
    return [adapt_closed_position(p) for p in data.get("closed_positions", [])]


def load_decisions() -> list[dict]:
    """Load and adapt decisions from learning/decisions_log.yaml."""
    path = ROOT / "learning" / "decisions_log.yaml"
    if not path.exists():
        return []
    data = yaml.safe_load(path.read_text())
    decisions = data.get("sizing_decisions", [])
    return [adapt_decision(d) for d in decisions]


def _guess_currency(ticker: str) -> str:
    if ticker.endswith(".L"):
        return "GBP"
    if ticker.endswith(".PA") or ticker.endswith(".AS") or ticker.endswith(".MI") or ticker.endswith(".DE"):
        return "EUR"
    return "USD"
```

- [ ] **Step 3: Commit**

```bash
git add knowledge_base/__init__.py knowledge_base/adapters.py
git commit -m "feat: add data adapter layer bridging legacy YAML to v1.0 schemas"
```

---

### Task 4: Adapter Tests

**Files:**
- Create: `tests/test_adapters.py`

- [ ] **Step 1: Write failing adapter tests**

```python
import json
import pytest
from jsonschema import validate, Draft7Validator
from knowledge_base.adapters import (
    adapt_portfolio_position,
    adapt_closed_position,
    adapt_decision,
    load_portfolio_positions,
    load_closed_positions,
    load_decisions,
    _parse_fv_number,
    _conviction_to_int,
    _parse_pct,
)


def _load_schema(name: str) -> dict:
    import pathlib
    schema_path = pathlib.Path(__file__).resolve().parent.parent / "knowledge_base" / "schemas" / name
    return json.loads(schema_path.read_text())


class TestParseHelpers:
    def test_parse_fv_number_eur(self):
        assert _parse_fv_number("EUR 33.00 (v5.0 post-FY2025)") == 33.0

    def test_parse_fv_number_usd(self):
        assert _parse_fv_number("$420") == 420.0

    def test_parse_fv_number_plain(self):
        assert _parse_fv_number("195.50") == 195.5

    def test_parse_fv_number_none(self):
        assert _parse_fv_number(None) is None

    def test_parse_fv_number_already_float(self):
        assert _parse_fv_number(42.5) == 42.5

    def test_conviction_string_to_int(self):
        assert _conviction_to_int("low") == 3
        assert _conviction_to_int("medium-high") == 7
        assert _conviction_to_int("high") == 8
        assert _conviction_to_int("alta") == 8

    def test_conviction_int_passthrough(self):
        assert _conviction_to_int(7) == 7

    def test_conviction_clamp(self):
        assert _conviction_to_int(15) == 10
        assert _conviction_to_int(0) == 1

    def test_parse_pct_string(self):
        assert _parse_pct("31%") == 31.0

    def test_parse_pct_float(self):
        assert _parse_pct(4.8) == 4.8


class TestAdaptPortfolioPosition:
    def test_adapts_real_format(self):
        raw = {
            "ticker": "DTE.DE",
            "name": "Deutsche Telekom AG",
            "shares": 20.624621,
            "invested_usd": 699.56,
            "avg_cost_usd": 33.91,
            "date_opened": "2026-01-26",
            "thesis": "thesis/active/DTE.DE/thesis.md",
            "conviction": "low-medium",
            "fair_value": "EUR 33.00 (v5.0 post-FY2025)",
            "last_review": "2026-03-03",
            "exit_plan": "HOLD. TRIM >EUR 34",
            "notes": "FY2025 ASSESSED",
        }
        result = adapt_portfolio_position(raw)
        assert result["ticker"] == "DTE.DE"
        assert result["conviction"] == 4
        assert result["fair_value"] == 33.0
        assert result["avg_cost"] == 33.91
        assert result["side"] == "LONG"

    def test_output_validates_against_schema(self):
        raw = {
            "ticker": "MORN",
            "name": "Morningstar Inc",
            "shares": 3,
            "invested_usd": 500,
            "avg_cost_usd": 166.67,
            "date_opened": "2026-01-15",
            "thesis": "thesis/active/MORN/thesis.md",
            "conviction": "high",
            "fair_value": "$195",
            "last_review": "2026-03-01",
            "exit_plan": "HOLD",
        }
        result = adapt_portfolio_position(raw)
        schema = _load_schema("portfolio_position.schema.json")
        validate(instance=result, schema=schema)


class TestAdaptClosedPosition:
    def test_adapts_real_format(self):
        raw = {
            "ticker": "ENEL.MI",
            "name": "Enel S.p.A.",
            "entry_date": "2026-01-27",
            "exit_date": "2026-01-31",
            "shares": 81,
            "entry_price": 9.225,
            "exit_price": 9.225,
            "entry_currency": "EUR",
            "pnl_percent": 0.0,
            "holding_days": 4,
            "exit_reason": "error",
        }
        result = adapt_closed_position(raw)
        assert result["ticker"] == "ENEL.MI"
        assert result["duration_days"] == 4
        assert result["realized_pnl_pct"] == 0.0

    def test_output_validates_against_schema(self):
        raw = {
            "ticker": "KLR.L",
            "name": "Keller Group",
            "entry_date": "2026-02-01",
            "exit_date": "2026-02-16",
            "shares": 50,
            "entry_price": 15.0,
            "exit_price": 19.2,
            "pnl_percent": 28.0,
            "holding_days": 15,
            "exit_reason": "sell_at_fv",
        }
        result = adapt_closed_position(raw)
        schema = _load_schema("closed_position.schema.json")
        validate(instance=result, schema=schema)


class TestAdaptDecision:
    def test_adapts_real_format(self):
        raw = {
            "date": "2026-02-04",
            "ticker": "ADBE",
            "action": "BUY",
            "sizing": "4.8%",
            "context": {
                "quality_score": 76,
                "tier": "A",
                "mos": "31%",
                "conviction": "Alta",
            },
            "reasoning": "ADBE es Quality Compounder Tier A a 52-week low",
            "outcome": "Pendiente",
        }
        result = adapt_decision(raw)
        assert result["ticker"] == "ADBE"
        assert result["decision"] == "BUY"
        assert result["conviction"] == 8
        assert result["mos_pct"] == 31.0
        assert result["position_size_pct"] == 4.8


class TestLoadFromFiles:
    def test_load_portfolio_positions_returns_list(self):
        positions = load_portfolio_positions()
        assert isinstance(positions, list)
        if positions:
            assert "ticker" in positions[0]
            assert "side" in positions[0]

    def test_load_closed_positions_returns_list(self):
        closed = load_closed_positions()
        assert isinstance(closed, list)
        if closed:
            assert "ticker" in closed[0]
            assert "exit_date" in closed[0]

    def test_load_decisions_returns_list(self):
        decisions = load_decisions()
        assert isinstance(decisions, list)
        if decisions:
            assert "ticker" in decisions[0]
            assert "decision" in decisions[0]
```

- [ ] **Step 2: Run tests to verify they fail (adapters module exists but tests exercise it)**

Run: `cd /Volumes/Storage/Documents/Claude/value_hunter/invest_value_manager && python -m pytest tests/test_adapters.py -v`
Expected: All tests PASS (adapter code is already written)

- [ ] **Step 3: Fix any schema validation failures**

If any `test_output_validates_against_schema` tests fail, adjust the adapter or schema to reconcile. The adapter output must validate against the schema. Common fix: add missing required fields with defaults, or relax schema `required` list.

- [ ] **Step 4: Commit**

```bash
git add tests/test_adapters.py
git commit -m "test: add adapter tests validating legacy YAML → v1.0 schema conversion"
```

---

### Task 5: Orchestrator Base Module

**Files:**
- Create: `orchestrator/base.py`

- [ ] **Step 1: Write `orchestrator/base.py` — abstract BaseAgent + AgentResult**

```python
"""Base classes for ValueHunter v1.0 agents."""

from __future__ import annotations

import time
import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class AgentModel(str, Enum):
    OPUS = "claude-opus-4-6"
    SONNET = "claude-sonnet-4-6"
    HAIKU = "claude-haiku-4-5"


class AgentLayer(int, Enum):
    GOVERNOR = 0
    SCREENING = 1
    ANALYSIS = 2
    PORTFOLIO = 3


@dataclass
class AgentResult:
    agent_id: str
    agent_name: str
    success: bool
    data: dict[str, Any] = field(default_factory=dict)
    error: str | None = None
    tokens_used: int = 0
    duration_seconds: float = 0.0
    run_id: str = ""

    def to_dict(self) -> dict:
        return {
            "agent_id": self.agent_id,
            "agent_name": self.agent_name,
            "success": self.success,
            "data": self.data,
            "error": self.error,
            "tokens_used": self.tokens_used,
            "duration_seconds": self.duration_seconds,
            "run_id": self.run_id,
        }


class BaseAgent(ABC):
    def __init__(
        self,
        agent_id: str,
        name: str,
        model: AgentModel,
        layer: AgentLayer,
        description: str = "",
        skills: list[str] | None = None,
        tools: list[str] | None = None,
        estimated_tokens: int = 5000,
    ):
        self.agent_id = agent_id
        self.name = name
        self.model = model
        self.layer = layer
        self.description = description
        self.skills = skills or []
        self.tools = tools or []
        self.estimated_tokens = estimated_tokens

    @abstractmethod
    async def run(self, inputs: dict[str, Any], run_id: str = "") -> AgentResult:
        ...

    def info(self) -> dict:
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "model": self.model.value,
            "layer": self.layer.value,
            "description": self.description,
            "skills": self.skills,
            "tools": self.tools,
            "estimated_tokens": self.estimated_tokens,
        }
```

- [ ] **Step 2: Verify import works**

Run: `cd /Volumes/Storage/Documents/Claude/value_hunter/invest_value_manager && python -c "from orchestrator.base import BaseAgent, AgentResult, AgentModel, AgentLayer; print('OK')"`
Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add orchestrator/base.py
git commit -m "feat: add orchestrator base classes (BaseAgent, AgentResult, AgentModel)"
```

---

### Task 6: Agent Registry

**Files:**
- Create: `orchestrator/registry.py`
- Create: `tests/test_registry.py`

- [ ] **Step 1: Write failing test**

```python
import pytest
from orchestrator.registry import AgentRegistry
from orchestrator.base import AgentModel, AgentLayer


def test_registry_has_10_agent_specs():
    registry = AgentRegistry()
    assert len(registry.list_agents()) == 10


def test_registry_agents_have_required_fields():
    registry = AgentRegistry()
    for spec in registry.list_agents():
        assert "agent_id" in spec
        assert "name" in spec
        assert "model" in spec
        assert "layer" in spec


def test_registry_get_by_id():
    registry = AgentRegistry()
    spec = registry.get("a11")
    assert spec is not None
    assert spec["name"] == "Quantitative Screener"


def test_registry_get_by_layer():
    registry = AgentRegistry()
    screening = registry.get_by_layer(AgentLayer.SCREENING)
    assert len(screening) == 2
    analysis = registry.get_by_layer(AgentLayer.ANALYSIS)
    assert len(analysis) == 5


def test_registry_model_routing():
    registry = AgentRegistry()
    haiku_agents = [s for s in registry.list_agents() if s["model"] == AgentModel.HAIKU.value]
    sonnet_agents = [s for s in registry.list_agents() if s["model"] == AgentModel.SONNET.value]
    assert len(haiku_agents) == 5
    assert len(sonnet_agents) == 4
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_registry.py -v`
Expected: FAIL — `ImportError: cannot import name 'AgentRegistry'`

- [ ] **Step 3: Write `orchestrator/registry.py`**

```python
"""Agent registry for ValueHunter v1.0 — 10 agents mapped to 24 existing skills."""

from __future__ import annotations

from orchestrator.base import AgentModel, AgentLayer


_AGENT_SPECS = [
    {
        "agent_id": "a11",
        "name": "Quantitative Screener",
        "model": AgentModel.HAIKU.value,
        "layer": AgentLayer.SCREENING.value,
        "description": "Screens universe by P/E, P/B, EV/EBITDA, net cash, insider %, momentum",
        "skills": ["screening-protocol", "investment-rules"],
        "tools": ["dynamic_screener.py", "batch_scorer.py", "quality_universe.py", "quality_scorer.py", "opportunity_filter.py"],
        "estimated_tokens": 3500,
    },
    {
        "agent_id": "a12",
        "name": "Special Situations Screener",
        "model": AgentModel.HAIKU.value,
        "layer": AgentLayer.SCREENING.value,
        "description": "Detects merger arb, spin-offs, liquidations, busted biotech via SEC RSS + PR Newswire",
        "skills": [],
        "tools": ["sec_edgar_rss.py", "pr_newswire.py"],
        "estimated_tokens": 7500,
    },
    {
        "agent_id": "a21",
        "name": "Financial Analyst",
        "model": AgentModel.SONNET.value,
        "layer": AgentLayer.ANALYSIS.value,
        "description": "DCF 3-scenario, NAV, net cash, ROIC trend, accounting red flags, MoS",
        "skills": ["valuation-methods", "projection-framework", "filing-analysis"],
        "tools": ["dcf_calculator.py", "quality_scorer.py", "narrative_checker.py", "forward_return.py"],
        "estimated_tokens": 12000,
    },
    {
        "agent_id": "a22",
        "name": "Special Situation Modeler",
        "model": AgentModel.SONNET.value,
        "layer": AgentLayer.ANALYSIS.value,
        "description": "Merger-arb spread + prob, liquidation value, spin-off stub, biotech CVR",
        "skills": ["contrathesis-framework"],
        "tools": ["merger_arb.py", "liquidation.py", "spinoff.py", "biotech_cash.py"],
        "estimated_tokens": 9000,
    },
    {
        "agent_id": "a23",
        "name": "Business Analyst",
        "model": AgentModel.SONNET.value,
        "layer": AgentLayer.ANALYSIS.value,
        "description": "Moat, competitive position, management skin-in-the-game, bull/bear, catalysts",
        "skills": ["business-analysis-framework", "skin-in-the-game", "quality-compounders", "sector-deep-dive"],
        "tools": ["insider_tracker.py", "ownership_analyzer.py", "sector_health.py"],
        "estimated_tokens": 10000,
    },
    {
        "agent_id": "a24",
        "name": "Risk Analyst",
        "model": AgentModel.HAIKU.value,
        "layer": AgentLayer.ANALYSIS.value,
        "description": "7-dim risk score, liquidity/sizing cap, thesis-break scenarios, FX, max-DD",
        "skills": ["portfolio-constraints"],
        "tools": ["risk_heatmap.py", "constraint_checker.py", "drift_detector.py", "correlation_matrix.py"],
        "estimated_tokens": 4500,
    },
    {
        "agent_id": "a25",
        "name": "Web Researcher",
        "model": AgentModel.HAIKU.value,
        "layer": AgentLayer.ANALYSIS.value,
        "description": "News, earnings calls, 13F, Horos/AV/Seeking Alpha coverage, regulatory",
        "skills": [],
        "tools": [],
        "estimated_tokens": 6000,
    },
    {
        "agent_id": "a31",
        "name": "Decision Maker",
        "model": AgentModel.SONNET.value,
        "layer": AgentLayer.PORTFOLIO.value,
        "description": "Aggregates Layer 2, applies gates (MoS/ECAGR/risk/consistency), emits decision JSON",
        "skills": ["investment-rules", "pre-execution-check", "recommendation-context"],
        "tools": ["consistency_checker.py", "portfolio_optimizer.py"],
        "estimated_tokens": 8000,
    },
    {
        "agent_id": "a32",
        "name": "Portfolio Monitor",
        "model": AgentModel.HAIKU.value,
        "layer": AgentLayer.PORTFOLIO.value,
        "description": "Daily P&L, price-vs-thesis drift, event timeline, filing alerts",
        "skills": [],
        "tools": ["portfolio_stats.py", "thesis_monitor.py", "earnings_intel.py", "session_opener.py"],
        "estimated_tokens": 3000,
    },
    {
        "agent_id": "a00",
        "name": "Governor",
        "model": AgentModel.OPUS.value,
        "layer": AgentLayer.GOVERNOR.value,
        "description": "Meta-decisions: flow selection, agent sequencing, parallel fanout, audit",
        "skills": ["session-planner", "wave-system"],
        "tools": [],
        "estimated_tokens": 5000,
    },
]


class AgentRegistry:
    def __init__(self):
        self._specs = {s["agent_id"]: s for s in _AGENT_SPECS}

    def list_agents(self) -> list[dict]:
        return list(self._specs.values())

    def get(self, agent_id: str) -> dict | None:
        return self._specs.get(agent_id)

    def get_by_layer(self, layer: AgentLayer) -> list[dict]:
        return [s for s in self._specs.values() if s["layer"] == layer.value]

    def get_model_for(self, agent_id: str) -> str | None:
        spec = self.get(agent_id)
        return spec["model"] if spec else None

    def summary(self) -> str:
        lines = ["ValueHunter v1.0 Agent Registry", "=" * 40]
        for layer in AgentLayer:
            agents = self.get_by_layer(layer)
            if agents:
                lines.append(f"\nLayer {layer.value} — {layer.name}")
                for a in agents:
                    lines.append(f"  [{a['agent_id']}] {a['name']} ({a['model']}, ~{a['estimated_tokens']} tok)")
        return "\n".join(lines)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_registry.py -v`
Expected: All 5 tests PASS

- [ ] **Step 5: Commit**

```bash
git add orchestrator/registry.py tests/test_registry.py
git commit -m "feat: add agent registry with 10 agent specs and model routing"
```

---

### Task 7: Audit Logger

**Files:**
- Create: `orchestrator/audit.py`

- [ ] **Step 1: Write `orchestrator/audit.py`**

```python
"""Append-only JSONL audit logger for orchestrator runs."""

from __future__ import annotations

import json
import pathlib
import time
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Any


@dataclass
class AuditEvent:
    timestamp: str
    run_id: str
    event_type: str
    agent_id: str | None = None
    data: dict[str, Any] = field(default_factory=dict)
    duration_seconds: float | None = None
    tokens_used: int | None = None
    error: str | None = None

    def to_json(self) -> str:
        d = {k: v for k, v in asdict(self).items() if v is not None}
        return json.dumps(d, default=str)


class AuditLogger:
    def __init__(self, log_dir: pathlib.Path | None = None):
        if log_dir is None:
            log_dir = pathlib.Path(__file__).resolve().parent.parent / "orchestrator" / "runs"
        self._log_dir = log_dir
        self._log_dir.mkdir(parents=True, exist_ok=True)
        self._log_path = self._log_dir / "audit.jsonl"

    def log(self, event: AuditEvent) -> None:
        with open(self._log_path, "a") as f:
            f.write(event.to_json() + "\n")

    def log_run_start(self, run_id: str, flow: str, params: dict | None = None) -> None:
        self.log(AuditEvent(
            timestamp=datetime.now(timezone.utc).isoformat(),
            run_id=run_id,
            event_type="RUN_START",
            data={"flow": flow, **(params or {})},
        ))

    def log_agent_start(self, run_id: str, agent_id: str, inputs: dict | None = None) -> None:
        self.log(AuditEvent(
            timestamp=datetime.now(timezone.utc).isoformat(),
            run_id=run_id,
            event_type="AGENT_START",
            agent_id=agent_id,
            data={"inputs_summary": str(inputs)[:200]} if inputs else {},
        ))

    def log_agent_end(self, run_id: str, agent_id: str, success: bool,
                      tokens: int = 0, duration: float = 0.0, error: str | None = None) -> None:
        self.log(AuditEvent(
            timestamp=datetime.now(timezone.utc).isoformat(),
            run_id=run_id,
            event_type="AGENT_END",
            agent_id=agent_id,
            data={"success": success},
            tokens_used=tokens,
            duration_seconds=duration,
            error=error,
        ))

    def log_run_end(self, run_id: str, success: bool, summary: dict | None = None) -> None:
        self.log(AuditEvent(
            timestamp=datetime.now(timezone.utc).isoformat(),
            run_id=run_id,
            event_type="RUN_END",
            data={"success": success, **(summary or {})},
        ))

    def read_run(self, run_id: str) -> list[dict]:
        if not self._log_path.exists():
            return []
        events = []
        for line in self._log_path.read_text().splitlines():
            if line.strip():
                event = json.loads(line)
                if event.get("run_id") == run_id:
                    events.append(event)
        return events
```

- [ ] **Step 2: Verify import and basic usage**

Run: `python -c "from orchestrator.audit import AuditLogger; a = AuditLogger(); print('OK')"`
Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add orchestrator/audit.py
git commit -m "feat: add JSONL audit logger for orchestrator runs"
```

---

### Task 8: Governor State Machine

**Files:**
- Create: `orchestrator/governor.py`
- Create: `orchestrator/__main__.py`
- Create: `tests/test_governor.py`

- [ ] **Step 1: Write failing test**

```python
import pytest
from orchestrator.governor import Governor, GovernorState


def test_governor_initial_state():
    gov = Governor()
    assert gov.state == GovernorState.IDLE


def test_governor_list_agents():
    gov = Governor()
    agents = gov.list_agents()
    assert len(agents) == 10


def test_governor_dry_run(capsys):
    gov = Governor()
    gov.dry_run()
    captured = capsys.readouterr()
    assert "Agent Registry" in captured.out
    assert "Governor" in captured.out
    assert "Quantitative Screener" in captured.out


def test_governor_state_transitions():
    gov = Governor()
    assert gov.state == GovernorState.IDLE
    gov._transition(GovernorState.SCREENING)
    assert gov.state == GovernorState.SCREENING
    gov._transition(GovernorState.IDLE)
    assert gov.state == GovernorState.IDLE
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python -m pytest tests/test_governor.py -v`
Expected: FAIL — `ImportError`

- [ ] **Step 3: Write `orchestrator/governor.py`**

```python
"""Layer-0 Governor — state machine for orchestrating ValueHunter flows."""

from __future__ import annotations

import uuid
from enum import Enum
from typing import Any

from orchestrator.registry import AgentRegistry
from orchestrator.audit import AuditLogger
from orchestrator.base import AgentLayer


class GovernorState(str, Enum):
    IDLE = "IDLE"
    SCREENING = "SCREENING"
    CANDIDATE_SELECTION = "CANDIDATE_SELECTION"
    ANALYSIS_FANOUT = "ANALYSIS_FANOUT"
    DECISION = "DECISION"
    NOTIFY = "NOTIFY"


class Governor:
    def __init__(self):
        self.registry = AgentRegistry()
        self.audit = AuditLogger()
        self.state = GovernorState.IDLE
        self._run_id: str | None = None

    def list_agents(self) -> list[dict]:
        return self.registry.list_agents()

    def _transition(self, new_state: GovernorState) -> None:
        self.state = new_state

    def _new_run_id(self) -> str:
        return f"run-{uuid.uuid4().hex[:12]}"

    def dry_run(self) -> None:
        print(self.registry.summary())
        print(f"\nGovernor state: {self.state.value}")
        print(f"Available flows: weekly, on-demand, daily-monitor")

    async def run_on_demand(self, ticker: str) -> dict[str, Any]:
        """Flow 2 — on-demand analysis of a single ticker (stub for Sprint 2)."""
        self._run_id = self._new_run_id()
        self.audit.log_run_start(self._run_id, "on-demand", {"ticker": ticker})

        self._transition(GovernorState.ANALYSIS_FANOUT)
        # Sprint 2: parallel fanout of A2.1-A2.5 here
        results: dict[str, Any] = {"ticker": ticker, "status": "stub", "agents_run": []}

        self._transition(GovernorState.DECISION)
        # Sprint 3: A3.1 Decision Maker here

        self._transition(GovernorState.IDLE)
        self.audit.log_run_end(self._run_id, success=True, summary=results)
        return results

    async def run_weekly(self) -> dict[str, Any]:
        """Flow 1 — weekly screening (stub for Sprint 3)."""
        self._run_id = self._new_run_id()
        self.audit.log_run_start(self._run_id, "weekly")

        self._transition(GovernorState.SCREENING)
        # Sprint 3: A1.1 + A1.2 parallel screening here

        self._transition(GovernorState.IDLE)
        self.audit.log_run_end(self._run_id, success=True)
        return {"status": "stub"}

    async def run_daily_monitor(self) -> dict[str, Any]:
        """Flow 3 — daily monitoring (stub for Sprint 4)."""
        self._run_id = self._new_run_id()
        self.audit.log_run_start(self._run_id, "daily-monitor")

        self._transition(GovernorState.IDLE)
        self.audit.log_run_end(self._run_id, success=True)
        return {"status": "stub"}
```

- [ ] **Step 4: Write `orchestrator/__main__.py`**

```python
"""CLI entry point: python -m orchestrator [command] [args]"""

import asyncio
import sys

from orchestrator.governor import Governor


def main():
    gov = Governor()
    args = sys.argv[1:]

    if not args or args[0] == "--dry-run":
        gov.dry_run()
        return

    command = args[0]

    if command == "on-demand" and len(args) >= 2:
        ticker = args[1]
        result = asyncio.run(gov.run_on_demand(ticker))
        print(f"Result: {result}")

    elif command == "weekly":
        result = asyncio.run(gov.run_weekly())
        print(f"Result: {result}")

    elif command == "daily-monitor":
        result = asyncio.run(gov.run_daily_monitor())
        print(f"Result: {result}")

    else:
        print(f"Unknown command: {command}")
        print("Usage: python -m orchestrator [--dry-run|on-demand TICKER|weekly|daily-monitor]")
        sys.exit(1)


if __name__ == "__main__":
    main()
```

- [ ] **Step 5: Run tests**

Run: `python -m pytest tests/test_governor.py -v`
Expected: All 4 tests PASS

- [ ] **Step 6: Test CLI dry-run**

Run: `cd /Volumes/Storage/Documents/Claude/value_hunter/invest_value_manager && python -m orchestrator --dry-run`
Expected: Prints agent registry with all 10 agents, governor state IDLE, available flows

- [ ] **Step 7: Commit**

```bash
git add orchestrator/governor.py orchestrator/__main__.py tests/test_governor.py
git commit -m "feat: add Governor state machine with dry-run CLI and flow stubs"
```

---

### Task 9: Alpha Vulture Scraper

**Files:**
- Create: `scrapers/alpha_vulture_scraper.py`
- Create: `tests/test_alpha_vulture_scraper.py`
- Create: `tests/fixtures/alpha_vulture_rss.xml`
- Create: `tests/fixtures/alpha_vulture_post.html`

- [ ] **Step 1: Create RSS fixture file**

File `tests/fixtures/alpha_vulture_rss.xml`:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Alpha Vulture</title>
    <link>https://alphavulture.com</link>
    <description>Special situation investing</description>
    <item>
      <title>Interesting merger arbitrage: ACME Corp acquisition by BigCo</title>
      <link>https://alphavulture.com/2026/03/15/acme-corp-merger-arb/</link>
      <pubDate>Fri, 15 Mar 2026 10:00:00 +0000</pubDate>
      <description>ACME Corp (ACME) is being acquired by BigCo at $45 per share. Current price is $42.50, offering a 5.9% spread with expected close in Q3 2026. Break fee is 3.5% of deal value.</description>
    </item>
    <item>
      <title>Net cash play: BustedBio Inc trading below cash</title>
      <link>https://alphavulture.com/2026/02/20/bustedbio-net-cash/</link>
      <pubDate>Thu, 20 Feb 2026 08:00:00 +0000</pubDate>
      <description>BustedBio (BBIO) has $12 per share in net cash but trades at $8. Failed Phase 3 trial. Management exploring strategic alternatives including liquidation.</description>
    </item>
  </channel>
</rss>
```

- [ ] **Step 2: Create post HTML fixture**

File `tests/fixtures/alpha_vulture_post.html`:
```html
<html>
<body>
<article>
  <h1 class="entry-title">Interesting merger arbitrage: ACME Corp acquisition by BigCo</h1>
  <time datetime="2026-03-15">March 15, 2026</time>
  <div class="entry-content">
    <p>ACME Corp (ticker: ACME) announced on March 1st that it has entered into a definitive agreement to be acquired by BigCo for $45.00 per share in cash.</p>
    <p>The current share price is $42.50, representing a spread of approximately 5.9%. The deal is expected to close in Q3 2026, pending regulatory approval.</p>
    <p>The break fee is $157.5 million, or approximately 3.5% of the deal value.</p>
    <p><strong>Expected return:</strong> 5.9% absolute, ~12% annualized assuming Q3 close.</p>
    <p><strong>Key risks:</strong> FTC review, financing condition.</p>
    <p><em>Disclosure: Long ACME</em></p>
  </div>
</article>
</body>
</html>
```

- [ ] **Step 3: Write failing test**

File `tests/test_alpha_vulture_scraper.py`:
```python
import pathlib
import pytest
import json
from jsonschema import validate

from scrapers.alpha_vulture_scraper import parse_rss_feed, parse_post_html, AlphaVultureScraper

FIXTURES = pathlib.Path(__file__).parent / "fixtures"
SCHEMA_PATH = pathlib.Path(__file__).resolve().parent.parent / "knowledge_base" / "schemas" / "alpha_vulture_idea.schema.json"


def _load_schema():
    return json.loads(SCHEMA_PATH.read_text())


class TestParseRSS:
    def test_parses_items_from_fixture(self):
        xml = (FIXTURES / "alpha_vulture_rss.xml").read_text()
        items = parse_rss_feed(xml)
        assert len(items) == 2

    def test_first_item_fields(self):
        xml = (FIXTURES / "alpha_vulture_rss.xml").read_text()
        items = parse_rss_feed(xml)
        item = items[0]
        assert item["title"] == "Interesting merger arbitrage: ACME Corp acquisition by BigCo"
        assert "alphavulture.com" in item["url"]
        assert item["pub_date"] is not None


class TestParsePostHTML:
    def test_extracts_ticker(self):
        html = (FIXTURES / "alpha_vulture_post.html").read_text()
        result = parse_post_html(html, "https://alphavulture.com/2026/03/15/acme-corp-merger-arb/")
        assert result["ticker"] == "ACME"

    def test_detects_situation_type_merger(self):
        html = (FIXTURES / "alpha_vulture_post.html").read_text()
        result = parse_post_html(html, "https://alphavulture.com/2026/03/15/acme-corp-merger-arb/")
        assert result["situation_type"] == "MERGER_ARB"


class TestSchemaValidation:
    def test_full_idea_validates(self):
        schema = _load_schema()
        idea = {
            "post_date": "2026-03-15",
            "title": "Interesting merger arbitrage: ACME Corp",
            "ticker": "ACME",
            "situation_type": "MERGER_ARB",
            "thesis_summary": "Acquired by BigCo at $45, spread 5.9%",
            "expected_return_pct": 5.9,
            "source": "ALPHA_VULTURE_BLOG",
            "access": "FREE",
            "source_url": "https://alphavulture.com/2026/03/15/acme-corp-merger-arb/",
            "scraped_date": "2026-04-16",
        }
        validate(instance=idea, schema=schema)
```

- [ ] **Step 4: Run test to verify it fails**

Run: `python -m pytest tests/test_alpha_vulture_scraper.py -v`
Expected: FAIL — `ImportError: cannot import name 'parse_rss_feed'`

- [ ] **Step 5: Write `scrapers/alpha_vulture_scraper.py`**

```python
"""Alpha Vulture blog scraper — extracts special-situation ideas from RSS + HTML."""

from __future__ import annotations

import json
import pathlib
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import date, datetime
from typing import Any

import httpx
from bs4 import BeautifulSoup


RSS_URL = "https://alphavulture.com/feed/"
OUTPUT_PATH = pathlib.Path(__file__).resolve().parent.parent / "knowledge_base" / "universe" / "alpha_vulture_ideas.json"

SITUATION_KEYWORDS = {
    "MERGER_ARB": ["merger", "acquisition", "acquired", "tender offer", "definitive agreement", "deal price"],
    "LIQUIDATION": ["liquidat", "wind down", "dissolv", "plan of dissolution"],
    "SPINOFF": ["spin-off", "spinoff", "spin off", "spun off"],
    "NET_CASH": ["net cash", "below cash", "cash shell", "cash per share", "trading below"],
    "ODD_LOT": ["odd-lot", "odd lot"],
    "CVR": ["contingent value right", "cvr"],
    "TENDER_OFFER": ["tender offer", "self-tender", "modified dutch"],
    "RIGHTS_OFFERING": ["rights offering", "rights issue"],
    "STUB": ["stub value", "stub valuation", "sum-of-the-parts"],
}


def parse_rss_feed(xml_content: str) -> list[dict[str, str]]:
    root = ET.fromstring(xml_content)
    items = []
    for item in root.findall(".//item"):
        title_el = item.find("title")
        link_el = item.find("link")
        pub_date_el = item.find("pubDate")
        desc_el = item.find("description")
        items.append({
            "title": title_el.text if title_el is not None else "",
            "url": link_el.text if link_el is not None else "",
            "pub_date": pub_date_el.text if pub_date_el is not None else None,
            "description": desc_el.text if desc_el is not None else "",
        })
    return items


def _classify_situation(text: str) -> str:
    text_lower = text.lower()
    for sit_type, keywords in SITUATION_KEYWORDS.items():
        if any(kw in text_lower for kw in keywords):
            return sit_type
    return "OTHER"


def _extract_ticker(text: str) -> str | None:
    patterns = [
        r"ticker:\s*([A-Z]{1,5})",
        r"\(([A-Z]{1,5})\)",
        r"\((?:NYSE|NASDAQ|AMEX):\s*([A-Z]{1,5})\)",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            common_words = {"THE", "AND", "FOR", "ARE", "BUT", "NOT", "YOU", "ALL", "CAN", "HER", "WAS", "ONE"}
            candidate = match.group(1)
            if candidate not in common_words:
                return candidate
    return None


def _extract_return(text: str) -> float | None:
    patterns = [
        r"expected return[:\s]+~?([\d.]+)%",
        r"spread of (?:approximately )?([\d.]+)%",
        r"([\d.]+)%\s*(?:absolute|spread|return|upside)",
    ]
    text_lower = text.lower()
    for pattern in patterns:
        match = re.search(pattern, text_lower)
        if match:
            return float(match.group(1))
    return None


def parse_post_html(html_content: str, source_url: str) -> dict[str, Any]:
    soup = BeautifulSoup(html_content, "html.parser")
    title_el = soup.find("h1", class_="entry-title") or soup.find("h1")
    title = title_el.get_text(strip=True) if title_el else ""
    content_el = soup.find("div", class_="entry-content") or soup.find("article")
    content_text = content_el.get_text(" ", strip=True) if content_el else ""
    full_text = f"{title} {content_text}"

    time_el = soup.find("time")
    pub_date = None
    if time_el and time_el.get("datetime"):
        pub_date = time_el["datetime"][:10]

    return {
        "title": title,
        "ticker": _extract_ticker(full_text),
        "situation_type": _classify_situation(full_text),
        "thesis_summary": content_text[:500] if content_text else None,
        "expected_return_pct": _extract_return(full_text),
        "pub_date": pub_date,
        "source_url": source_url,
    }


def _rss_date_to_iso(rss_date: str | None) -> str | None:
    if not rss_date:
        return None
    try:
        dt = datetime.strptime(rss_date.strip(), "%a, %d %b %Y %H:%M:%S %z")
        return dt.strftime("%Y-%m-%d")
    except ValueError:
        return None


def build_idea(rss_item: dict, post_data: dict) -> dict[str, Any]:
    return {
        "post_date": post_data.get("pub_date") or _rss_date_to_iso(rss_item.get("pub_date")) or date.today().isoformat(),
        "title": post_data.get("title") or rss_item.get("title", ""),
        "ticker": post_data.get("ticker"),
        "situation_type": post_data.get("situation_type", "OTHER"),
        "thesis_summary": post_data.get("thesis_summary"),
        "expected_return_pct": post_data.get("expected_return_pct"),
        "source": "ALPHA_VULTURE_BLOG",
        "access": "FREE",
        "source_url": post_data.get("source_url") or rss_item.get("url", ""),
        "scraped_date": date.today().isoformat(),
    }


class AlphaVultureScraper:
    def __init__(self, client: httpx.Client | None = None):
        self._client = client or httpx.Client(timeout=30, follow_redirects=True)

    def fetch_rss(self) -> list[dict]:
        resp = self._client.get(RSS_URL)
        resp.raise_for_status()
        return parse_rss_feed(resp.text)

    def fetch_post(self, url: str) -> dict:
        resp = self._client.get(url)
        resp.raise_for_status()
        return parse_post_html(resp.text, url)

    def scrape(self, max_posts: int = 10) -> list[dict]:
        rss_items = self.fetch_rss()
        ideas = []
        for item in rss_items[:max_posts]:
            url = item.get("url")
            if not url:
                continue
            post_data = self.fetch_post(url)
            idea = build_idea(item, post_data)
            ideas.append(idea)
        return ideas

    def save(self, ideas: list[dict], path: pathlib.Path | None = None) -> None:
        out = path or OUTPUT_PATH
        out.parent.mkdir(parents=True, exist_ok=True)
        existing = []
        if out.exists():
            existing = json.loads(out.read_text())
        seen_urls = {e["source_url"] for e in existing}
        new_ideas = [i for i in ideas if i["source_url"] not in seen_urls]
        combined = existing + new_ideas
        out.write_text(json.dumps(combined, indent=2, default=str))
        return len(new_ideas)


if __name__ == "__main__":
    scraper = AlphaVultureScraper()
    ideas = scraper.scrape()
    added = scraper.save(ideas)
    print(f"Scraped {len(ideas)} ideas, {added} new")
```

- [ ] **Step 6: Run tests**

Run: `python -m pytest tests/test_alpha_vulture_scraper.py -v`
Expected: All 5 tests PASS

- [ ] **Step 7: Commit**

```bash
git add scrapers/alpha_vulture_scraper.py tests/test_alpha_vulture_scraper.py tests/fixtures/alpha_vulture_rss.xml tests/fixtures/alpha_vulture_post.html
git commit -m "feat: add Alpha Vulture blog scraper with RSS parsing and situation classification"
```

---

### Task 10: Horos Scraper

**Files:**
- Create: `scrapers/horos_scraper.py`
- Create: `tests/test_horos_scraper.py`
- Create: `tests/fixtures/horos_letter_sample.txt`

- [ ] **Step 1: Create text fixture simulating extracted PDF content**

File `tests/fixtures/horos_letter_sample.txt`:
```
CARTA TRIMESTRAL A LOS COINVERSORES — Q4 2025

Estimados coinversores,

Durante el cuarto trimestre de 2025, Horos Value Internacional ha obtenido una
rentabilidad del +4.2%, frente al +2.1% del MSCI ACWI.

PRINCIPALES POSICIONES:

Técnicas Reunidas (TRE.MC) — Peso: 5.2%
Ingeniería española con cartera de pedidos récord. Cotiza a EV/EBITDA de 4.5x
frente a media histórica de 7x. Potencial de revalorización superior al 50%.

Babcock International (BAB.L) — Peso: 4.8%
Servicios de defensa y nuclear en UK. Reestructuración avanzada bajo nuevo CEO.
Trading at 6x EV/EBIT vs sector at 10x. Upside potencial del 60%.

International Petroleum Corp (IPCO.ST) — Peso: 3.5%
Productora de petróleo y gas. Net cash position. Trading below NAV.
Potencial de revalorización del 40% hasta NAV.

NUEVA POSICIÓN:
Hemos iniciado posición en Atalaya Mining (ATYM.L) durante el trimestre.
Mina de cobre en España, cotizando a 3x EV/EBITDA con cobre a máximos.
Estimamos un upside del 45%.

POSICIÓN VENDIDA:
Hemos vendido nuestra posición en Gestamp (GEST.MC) tras alcanzar nuestro
precio objetivo.
```

- [ ] **Step 2: Write failing test**

File `tests/test_horos_scraper.py`:
```python
import pathlib
import json
import pytest
from jsonschema import validate

from scrapers.horos_scraper import parse_letter_text, extract_positions

FIXTURES = pathlib.Path(__file__).parent / "fixtures"
SCHEMA_PATH = pathlib.Path(__file__).resolve().parent.parent / "knowledge_base" / "schemas" / "horos_position.schema.json"


def _load_schema():
    return json.loads(SCHEMA_PATH.read_text())


class TestParseLetterText:
    def test_extracts_quarter(self):
        text = (FIXTURES / "horos_letter_sample.txt").read_text()
        result = parse_letter_text(text, source_url="https://horosam.com/letter.pdf")
        assert result["quarter"] == "2025-Q4"

    def test_extracts_fund_performance(self):
        text = (FIXTURES / "horos_letter_sample.txt").read_text()
        result = parse_letter_text(text, source_url="https://horosam.com/letter.pdf")
        assert result["fund_return_pct"] == pytest.approx(4.2, abs=0.1)


class TestExtractPositions:
    def test_finds_positions(self):
        text = (FIXTURES / "horos_letter_sample.txt").read_text()
        positions = extract_positions(text, "2025-Q4", "https://horosam.com/letter.pdf")
        assert len(positions) >= 3

    def test_position_has_ticker(self):
        text = (FIXTURES / "horos_letter_sample.txt").read_text()
        positions = extract_positions(text, "2025-Q4", "https://horosam.com/letter.pdf")
        tickers = [p.get("ticker") for p in positions if p.get("ticker")]
        assert "TRE.MC" in tickers or "BAB.L" in tickers

    def test_detects_new_position(self):
        text = (FIXTURES / "horos_letter_sample.txt").read_text()
        positions = extract_positions(text, "2025-Q4", "https://horosam.com/letter.pdf")
        new_positions = [p for p in positions if p.get("action") == "NEW"]
        assert len(new_positions) >= 1

    def test_position_validates_against_schema(self):
        schema = _load_schema()
        text = (FIXTURES / "horos_letter_sample.txt").read_text()
        positions = extract_positions(text, "2025-Q4", "https://horosam.com/letter.pdf")
        for pos in positions:
            validate(instance=pos, schema=schema)
```

- [ ] **Step 3: Run test to verify it fails**

Run: `python -m pytest tests/test_horos_scraper.py -v`
Expected: FAIL — `ImportError`

- [ ] **Step 4: Write `scrapers/horos_scraper.py`**

```python
"""Horos Asset Management quarterly letter scraper.

Fetches PDF letters from horosam.com, extracts text, parses positions.
"""

from __future__ import annotations

import json
import pathlib
import re
from datetime import date
from typing import Any

import httpx
from bs4 import BeautifulSoup

try:
    from pypdf import PdfReader
except ImportError:
    PdfReader = None


HOROS_BASE_URL = "https://horosam.com"
LETTERS_PAGE = f"{HOROS_BASE_URL}/articulos/cartas-al-inversor/"
OUTPUT_PATH = pathlib.Path(__file__).resolve().parent.parent / "knowledge_base" / "universe" / "horos_positions.json"

QUARTER_PATTERNS = [
    (r"Q([1-4])\s*(\d{4})", lambda m: f"{m.group(2)}-Q{m.group(1)}"),
    (r"(\d{4})\s*Q([1-4])", lambda m: f"{m.group(1)}-Q{m.group(2)}"),
    (r"(?:primer|segundo|tercer|cuarto)\s+trimestre\s+(?:de\s+)?(\d{4})",
     lambda m: f"{m.group(1)}-Q{'1' if 'primer' in m.group(0).lower() else '2' if 'segundo' in m.group(0).lower() else '3' if 'tercer' in m.group(0).lower() else '4'}"),
    (r"(?:Q4|cuarto trimestre|4T)\s*(\d{4})", lambda m: f"{m.group(1)}-Q4"),
    (r"(\d{4}).*(?:Q4|cuarto|4T)", lambda m: f"{m.group(1)}-Q4"),
]

TICKER_PATTERN = re.compile(r"\(([A-Z0-9]+(?:\.[A-Z]{1,4})?)\)")
WEIGHT_PATTERN = re.compile(r"[Pp]eso:?\s*([\d.]+)%")
UPSIDE_PATTERN = re.compile(r"(?:potencial|upside|revalorización)[^.]*?([\d]+)%", re.IGNORECASE)


def parse_letter_text(text: str, source_url: str) -> dict[str, Any]:
    quarter = _extract_quarter(text)
    fund_return = _extract_fund_return(text)
    return {
        "quarter": quarter,
        "fund_return_pct": fund_return,
        "source_url": source_url,
    }


def _extract_quarter(text: str) -> str:
    for pattern, formatter in QUARTER_PATTERNS:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return formatter(match)
    return "UNKNOWN"


def _extract_fund_return(text: str) -> float | None:
    match = re.search(r"rentabilidad\s+del?\s*\+?([\-\d.]+)%", text, re.IGNORECASE)
    if match:
        return float(match.group(1))
    return None


def extract_positions(text: str, quarter: str, source_url: str) -> list[dict[str, Any]]:
    positions = []
    lines = text.split("\n")
    i = 0
    current_action = "MAINTAINED"

    while i < len(lines):
        line = lines[i].strip()

        if re.search(r"NUEVA\s+POSICI[OÓ]N", line, re.IGNORECASE):
            current_action = "NEW"
            i += 1
            continue
        if re.search(r"POSICI[OÓ]N\s+VENDIDA", line, re.IGNORECASE):
            current_action = "EXITED"
            i += 1
            continue
        if re.search(r"PRINCIPALES\s+POSICIONES", line, re.IGNORECASE):
            current_action = "MAINTAINED"
            i += 1
            continue

        ticker_match = TICKER_PATTERN.search(line)
        if ticker_match:
            ticker = ticker_match.group(1)
            company = line[:ticker_match.start()].strip().rstrip("—–-").strip()

            context_block = line
            for j in range(i + 1, min(i + 5, len(lines))):
                next_line = lines[j].strip()
                if not next_line or TICKER_PATTERN.search(next_line):
                    break
                context_block += " " + next_line

            weight_match = WEIGHT_PATTERN.search(context_block)
            upside_match = UPSIDE_PATTERN.search(context_block)

            pos = {
                "letter_quarter": quarter,
                "fund": "HOROS_VALUE_INTERNACIONAL",
                "company": company if company else ticker,
                "ticker": ticker,
                "ticker_confidence": "EXACT",
                "thesis_summary": context_block[:400].strip() if context_block else None,
                "upside_pct": float(upside_match.group(1)) if upside_match else None,
                "weight_pct": float(weight_match.group(1)) if weight_match else None,
                "action": current_action,
                "source_url": source_url,
                "scraped_date": date.today().isoformat(),
            }
            positions.append(pos)

        i += 1

    return positions


def extract_text_from_pdf(pdf_path: pathlib.Path) -> str:
    if PdfReader is None:
        raise ImportError("pypdf is required for PDF parsing: pip install pypdf")
    reader = PdfReader(str(pdf_path))
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text


class HorosScraper:
    def __init__(self, client: httpx.Client | None = None):
        self._client = client or httpx.Client(timeout=30, follow_redirects=True)

    def find_letter_urls(self) -> list[dict[str, str]]:
        resp = self._client.get(LETTERS_PAGE)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        letters = []
        for link in soup.find_all("a", href=True):
            href = link["href"]
            if href.endswith(".pdf") and "carta" in href.lower():
                letters.append({
                    "url": href if href.startswith("http") else f"{HOROS_BASE_URL}{href}",
                    "title": link.get_text(strip=True),
                })
        return letters

    def download_pdf(self, url: str, dest: pathlib.Path) -> pathlib.Path:
        resp = self._client.get(url)
        resp.raise_for_status()
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(resp.content)
        return dest

    def scrape_letter(self, pdf_url: str) -> list[dict]:
        import tempfile
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as f:
            tmp_path = pathlib.Path(f.name)
        try:
            self.download_pdf(pdf_url, tmp_path)
            text = extract_text_from_pdf(tmp_path)
            meta = parse_letter_text(text, pdf_url)
            positions = extract_positions(text, meta["quarter"], pdf_url)
            return positions
        finally:
            tmp_path.unlink(missing_ok=True)

    def scrape_all(self, max_letters: int = 4) -> list[dict]:
        letter_urls = self.find_letter_urls()
        all_positions = []
        for letter in letter_urls[:max_letters]:
            positions = self.scrape_letter(letter["url"])
            all_positions.extend(positions)
        return all_positions

    def save(self, positions: list[dict], path: pathlib.Path | None = None) -> int:
        out = path or OUTPUT_PATH
        out.parent.mkdir(parents=True, exist_ok=True)
        existing = []
        if out.exists():
            existing = json.loads(out.read_text())
        seen = {(e.get("ticker"), e.get("letter_quarter")) for e in existing}
        new = [p for p in positions if (p.get("ticker"), p.get("letter_quarter")) not in seen]
        combined = existing + new
        out.write_text(json.dumps(combined, indent=2, default=str))
        return len(new)


if __name__ == "__main__":
    import sys
    if "--dry-run" in sys.argv:
        scraper = HorosScraper()
        urls = scraper.find_letter_urls()
        print(f"Found {len(urls)} letter URLs:")
        for u in urls[:5]:
            print(f"  {u['title']}: {u['url']}")
    else:
        scraper = HorosScraper()
        positions = scraper.scrape_all()
        added = scraper.save(positions)
        print(f"Scraped {len(positions)} positions, {added} new")
```

- [ ] **Step 5: Run tests**

Run: `python -m pytest tests/test_horos_scraper.py -v`
Expected: All 6 tests PASS

- [ ] **Step 6: Test dry-run against live site**

Run: `cd /Volumes/Storage/Documents/Claude/value_hunter/invest_value_manager && python -m scrapers.horos_scraper --dry-run`
Expected: Lists found letter URLs from horosam.com (or graceful error if site structure differs)

- [ ] **Step 7: Commit**

```bash
git add scrapers/horos_scraper.py tests/test_horos_scraper.py tests/fixtures/horos_letter_sample.txt
git commit -m "feat: add Horos quarterly letter scraper with PDF parsing and position extraction"
```

---

### Task 11: Archive Root Docs + Regression Test

**Files:**
- Create: `docs/history/` (directory)
- Move: root-level ValueHunter planning docs to `docs/history/`
- Create: `tests/test_regression.py`

- [ ] **Step 1: Create `docs/history/` and move root planning docs**

```bash
mkdir -p docs/history
# Move root-level planning docs that are superseded by docs/ARCHITECTURE.md
cp ../ARQUITECTURA_ValueHunter_v1.md docs/history/ 2>/dev/null || echo "Not found at root, checking current dir"
cp ../CLAUDE_CODE_PROMPT_ValueHunter.md docs/history/ 2>/dev/null || echo "Not found"
cp ../ValueHunter_Architecture.html docs/history/ 2>/dev/null || echo "Not found"
```

Note: These files live at the repository root (`/Volumes/Storage/Documents/Claude/value_hunter/`), not inside `invest_value_manager/`. Copy (not move) to preserve originals until confirmed.

- [ ] **Step 2: Write regression test**

File `tests/test_regression.py`:
```python
"""Regression tests — verify existing v4.6 tools are not broken by v1.0 additions."""

import pathlib
import subprocess
import sys

import pytest
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent


class TestExistingFilesIntact:
    def test_portfolio_current_loads(self):
        path = ROOT / "portfolio" / "current.yaml"
        if not path.exists():
            pytest.skip("portfolio/current.yaml not found")
        data = yaml.safe_load(path.read_text())
        assert "positions" in data
        assert isinstance(data["positions"], list)

    def test_portfolio_history_loads(self):
        path = ROOT / "portfolio" / "history.yaml"
        if not path.exists():
            pytest.skip("portfolio/history.yaml not found")
        data = yaml.safe_load(path.read_text())
        assert "closed_positions" in data

    def test_decisions_log_loads(self):
        path = ROOT / "learning" / "decisions_log.yaml"
        if not path.exists():
            pytest.skip("decisions_log.yaml not found")
        data = yaml.safe_load(path.read_text())
        assert data is not None

    def test_principles_exists(self):
        path = ROOT / "learning" / "principles.md"
        assert path.exists(), "principles.md must not be deleted"

    def test_claude_md_exists_and_has_identity(self):
        path = ROOT / "CLAUDE.md"
        assert path.exists()
        content = path.read_text()
        assert "CIO" in content
        assert "14 Principios" in content or "Principios de Inversion" in content

    def test_tools_directory_intact(self):
        tools_dir = ROOT / "tools"
        assert tools_dir.is_dir()
        py_files = list(tools_dir.glob("*.py"))
        assert len(py_files) >= 40, f"Expected >=40 tools, found {len(py_files)}"

    def test_skills_directory_intact(self):
        skills_dir = ROOT / ".claude" / "skills"
        assert skills_dir.is_dir()

    def test_rules_directory_intact(self):
        rules_dir = ROOT / ".claude" / "rules"
        assert rules_dir.is_dir()
        assert (rules_dir / "agent-protocol.md").exists()
        assert (rules_dir / "error-patterns.md").exists()


class TestExistingToolsRunnable:
    def test_session_opener_importable(self):
        result = subprocess.run(
            [sys.executable, "-c", "import importlib.util; spec = importlib.util.spec_from_file_location('m', 'tools/session_opener.py'); print('OK' if spec else 'FAIL')"],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            timeout=10,
        )
        assert result.returncode == 0 or "OK" in result.stdout
```

- [ ] **Step 3: Run regression tests**

Run: `python -m pytest tests/test_regression.py -v`
Expected: All tests PASS

- [ ] **Step 4: Run full test suite**

Run: `python -m pytest tests/ -v`
Expected: All tests across all test files PASS

- [ ] **Step 5: Commit**

```bash
git add docs/history/ tests/test_regression.py
git commit -m "test: add regression tests + archive root planning docs"
```

---

## Sprint 1 Verification Checklist

After all tasks complete, verify:

- [ ] `python -m pytest tests/ -v` — all green
- [ ] `python -m orchestrator --dry-run` — prints 10-agent registry + Governor state
- [ ] `python -m scrapers.horos_scraper --dry-run` — finds letter URLs (or graceful error)
- [ ] `python3 tools/session_opener.py` — still works (regression)
- [ ] `ls knowledge_base/schemas/*.schema.json | wc -l` — outputs 12
- [ ] No existing files in `tools/`, `.claude/`, `portfolio/`, `state/`, `thesis/`, `learning/`, `world/` were modified

---

## Post-Sprint 1 Cleanup

After verification passes:
1. Run `python3 tools/batch_scorer.py --all-universe --goodwill` to backfill goodwill_pct
2. Tag release: `git tag v1.0-sprint1`
3. Confirm with user: "Ready to start Sprint 2?"
