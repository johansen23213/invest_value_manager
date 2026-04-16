"""
Data adapter layer: converts legacy YAML data to v1.0 schema-compliant dicts.

This module bridges the gap between existing YAML files (portfolio/current.yaml,
portfolio/history.yaml, learning/decisions_log.yaml) and the v1.0 JSON Schemas
(knowledge_base/schemas/*.schema.json) WITHOUT modifying the source files.
"""
from __future__ import annotations

import datetime
import pathlib
import re
from typing import Any

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# Conviction string → integer mapping
# ---------------------------------------------------------------------------
CONVICTION_MAP: dict[str, int] = {
    "low": 3,
    "low-medium": 4,
    "medium": 5,
    "medium-high": 7,
    "high": 8,
    "very high": 9,
    # Spanish equivalents
    "alta": 8,
    "media-alta": 7,
    "media": 5,
    "baja": 3,
}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def _parse_fv_number(fv_str: Any) -> float | None:
    """Extract fair-value number from descriptive strings.

    Examples:
        "EUR 33.00 (v5.0 ...)"  → 33.0
        "$191 (v3.0 ...)"       → 191.0
        "240 GBp (...)"         → 240.0
        29.0                    → 29.0
        None                    → None
    """
    if fv_str is None:
        return None
    if isinstance(fv_str, (int, float)):
        return float(fv_str)
    s = str(fv_str).strip()
    # Remove leading currency symbols/codes
    s = re.sub(r'^[A-Z]{2,3}\s*', '', s)  # "EUR 33.00 ..." → "33.00 ..."
    s = re.sub(r'^\$', '', s)              # "$191 ..." → "191 ..."
    # Extract first number (int or float, possibly negative)
    m = re.search(r'(-?\d[\d,]*\.?\d*)', s)
    if m:
        return float(m.group(1).replace(',', ''))
    return None


def _conviction_to_int(val: Any) -> int:
    """Convert conviction string to 1-10 integer.

    Handles: string labels, Spanish labels, integers, floats.
    Clamps result to [1, 10].
    """
    if val is None:
        return 5  # default to medium
    if isinstance(val, int):
        return max(1, min(10, val))
    if isinstance(val, float):
        return max(1, min(10, int(val)))
    key = str(val).strip().lower()
    result = CONVICTION_MAP.get(key, 5)
    return max(1, min(10, result))


def _parse_pct(val: Any) -> float | None:
    """Parse percentage from various formats.

    Examples:
        "31%"  → 31.0
        "4.8%" → 4.8
        31.0   → 31.0
        None   → None
    """
    if val is None:
        return None
    if isinstance(val, (int, float)):
        return float(val)
    s = str(val).strip().rstrip('%')
    try:
        return float(s)
    except ValueError:
        return None


def _guess_currency(ticker: str) -> str:
    """Infer currency from ticker suffix.

    .L → GBP, .DE/.PA/.MI/.AS → EUR, default USD.
    """
    if not isinstance(ticker, str):
        return "USD"
    t = ticker.upper()
    if t.endswith('.L'):
        return "GBP"
    for suffix in ('.DE', '.PA', '.MI', '.AS'):
        if t.endswith(suffix):
            return "EUR"
    return "USD"


def _date_str(val: Any) -> str | None:
    """Convert date or string to ISO date string.

    Handles datetime.date, datetime.datetime, and strings.
    """
    if val is None:
        return None
    if isinstance(val, datetime.datetime):
        return val.date().isoformat()
    if isinstance(val, datetime.date):
        return val.isoformat()
    return str(val).strip()


# ---------------------------------------------------------------------------
# Position adapters
# ---------------------------------------------------------------------------

def adapt_portfolio_position(raw: dict) -> dict:
    """Convert a raw portfolio/current.yaml position to v1.0 schema format.

    Key mappings:
        avg_cost_usd → avg_cost
        conviction (string) → conviction (int 1-10)
        fair_value (string) → fair_value (number)
        date_opened → entry_date
        name → company_name
        thesis → thesis_path
    """
    ticker = raw.get("ticker", "")
    result: dict[str, Any] = {
        "ticker": ticker,
        "shares": raw.get("shares", 0),
        "side": "LONG",
        "invested_usd": raw.get("invested_usd", 0),
        "avg_cost": raw.get("avg_cost_usd", raw.get("avg_cost", 0)),
        "conviction": _conviction_to_int(raw.get("conviction")),
        "fair_value": _parse_fv_number(raw.get("fair_value")),
    }
    # fair_value must be a number; default to 0 if parsing failed
    if result["fair_value"] is None:
        result["fair_value"] = 0.0

    # Optional fields
    if "name" in raw:
        result["company_name"] = raw["name"]
    if "currency" in raw:
        result["currency"] = raw["currency"]
    else:
        result["currency"] = _guess_currency(ticker)
    if "thesis" in raw:
        result["thesis_path"] = raw["thesis"]
    elif "thesis_path" in raw:
        result["thesis_path"] = raw["thesis_path"]
    if "date_opened" in raw:
        result["entry_date"] = _date_str(raw["date_opened"])
    elif "entry_date" in raw:
        result["entry_date"] = _date_str(raw["entry_date"])
    if "last_review" in raw:
        result["last_review"] = _date_str(raw["last_review"])
    if "exit_plan" in raw:
        result["exit_plan"] = raw["exit_plan"]
    if "notes" in raw:
        result["notes"] = raw["notes"]

    return result


def adapt_closed_position(raw: dict) -> dict:
    """Convert a raw portfolio/history.yaml closed position to v1.0 schema format.

    Key mappings:
        holding_days → duration_days
        pnl_percent → realized_pnl_pct
        name → company_name
        exit_reason (string) → exit_reason (string, kept as-is)
        entry_price / entry_price_gbp / entry_price_eur → avg_cost
        entry_date / exit_date → entry_date / exit_date (ISO strings)
    """
    ticker = raw.get("ticker", "")
    result: dict[str, Any] = {
        "ticker": ticker,
        "side": raw.get("side", "LONG"),
        "entry_date": _date_str(raw.get("entry_date")),
        "exit_date": _date_str(raw.get("exit_date")),
        "exit_reason": raw.get("exit_reason", "unknown"),
    }

    # Optional fields
    if "name" in raw:
        result["company_name"] = raw["name"]
    if "shares" in raw:
        result["shares"] = raw["shares"]

    # avg_cost: prefer entry_price, fallback to entry_price_gbp, entry_price_eur
    avg_cost = raw.get("entry_price", raw.get("entry_price_gbp", raw.get("entry_price_eur")))
    if avg_cost is not None:
        result["avg_cost"] = float(avg_cost)

    # exit_price: prefer exit_price, fallback to exit_price_gbp, exit_price_eur, exit_price_usd
    exit_price = raw.get("exit_price", raw.get("exit_price_gbp", raw.get("exit_price_eur", raw.get("exit_price_usd"))))
    if exit_price is not None:
        result["exit_price"] = float(exit_price)

    if "holding_days" in raw:
        result["duration_days"] = raw["holding_days"]
    elif "duration_days" in raw:
        result["duration_days"] = raw["duration_days"]

    if "pnl_percent" in raw:
        result["realized_pnl_pct"] = float(raw["pnl_percent"])
    elif "realized_pnl_pct" in raw:
        result["realized_pnl_pct"] = float(raw["realized_pnl_pct"])

    if "quality_score" in raw:
        qs = raw["quality_score"]
        if qs is not None:
            if qs >= 75:
                result["qs_tier"] = "A"
            elif qs >= 55:
                result["qs_tier"] = "B"
            elif qs >= 35:
                result["qs_tier"] = "C"
            else:
                result["qs_tier"] = "D"

    if "lesson_learned" in raw:
        result["lessons"] = [raw["lesson_learned"]]
    elif "lessons" in raw:
        result["lessons"] = raw["lessons"]

    return result


def adapt_decision(raw: dict) -> dict:
    """Convert a raw learning/decisions_log.yaml sizing decision to v1.0 schema format.

    Key mappings:
        action → decision
        sizing (string "4.8%") → position_size_pct (float)
        context.conviction (string) → conviction (int 1-10)
        context.quality_score → (preserved for reference)
        reasoning → reasoning
    """
    # Map action to decision enum
    action = raw.get("action", raw.get("decision", "WATCH"))
    action_map = {
        "BUY": "BUY",
        "SELL": "SELL",
        "ADD": "ADD",
        "TRIM": "TRIM",
        "SHORT": "SHORT",
        "COVER": "COVER",
        "WATCH": "WATCH",
        "PASS": "PASS",
    }
    decision = action_map.get(action.upper(), "WATCH") if isinstance(action, str) else "WATCH"

    context = raw.get("context", {})

    # Conviction: from context first, then top-level
    conviction_raw = context.get("conviction", raw.get("conviction"))
    conviction = _conviction_to_int(conviction_raw)

    result: dict[str, Any] = {
        "date": _date_str(raw.get("date")),
        "ticker": raw.get("ticker", ""),
        "decision": decision,
        "conviction": conviction,
        "reasoning": raw.get("reasoning", ""),
    }

    # Optional: position_size_pct from sizing string
    sizing = raw.get("sizing")
    if sizing is not None:
        pct = _parse_pct(sizing)
        if pct is not None:
            result["position_size_pct"] = pct

    # Optional: fair_value from context.mos
    mos = context.get("mos")
    if mos is not None:
        result["mos_pct"] = _parse_pct(mos)

    # Optional: e_cagr
    ecagr = context.get("ecagr_3yr")
    if ecagr is not None:
        result["e_cagr_pct"] = _parse_pct(ecagr)

    # Optional: outcome → outcome
    outcome = raw.get("outcome")
    if outcome is not None:
        result["outcome"] = outcome

    return result


# ---------------------------------------------------------------------------
# File loaders
# ---------------------------------------------------------------------------

def load_portfolio_positions() -> list[dict]:
    """Read portfolio/current.yaml and return list of adapted portfolio positions."""
    path = ROOT / "portfolio" / "current.yaml"
    if not path.exists():
        return []
    data = yaml.safe_load(path.read_text())
    if not data or "positions" not in data:
        return []
    return [adapt_portfolio_position(p) for p in data["positions"]]


def load_closed_positions() -> list[dict]:
    """Read portfolio/history.yaml and return list of adapted closed positions."""
    path = ROOT / "portfolio" / "history.yaml"
    if not path.exists():
        return []
    data = yaml.safe_load(path.read_text())
    if not data or "closed_positions" not in data:
        return []
    return [adapt_closed_position(p) for p in data["closed_positions"]]


def load_decisions() -> list[dict]:
    """Read learning/decisions_log.yaml and return list of adapted decisions."""
    path = ROOT / "learning" / "decisions_log.yaml"
    if not path.exists():
        return []
    data = yaml.safe_load(path.read_text())
    if not data or "sizing_decisions" not in data:
        return []
    return [adapt_decision(d) for d in data["sizing_decisions"]]
