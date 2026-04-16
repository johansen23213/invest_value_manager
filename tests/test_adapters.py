"""Tests for knowledge_base.adapters — legacy YAML → v1.0 schema conversion."""
import json
import pathlib
import datetime

import pytest
from jsonschema import validate, Draft7Validator

from knowledge_base.adapters import (
    _parse_fv_number,
    _conviction_to_int,
    _parse_pct,
    _guess_currency,
    _date_str,
    adapt_portfolio_position,
    adapt_closed_position,
    adapt_decision,
    load_portfolio_positions,
    load_closed_positions,
    load_decisions,
)

SCHEMAS_DIR = pathlib.Path(__file__).resolve().parent.parent / "knowledge_base" / "schemas"


def _load_schema(name: str) -> dict:
    return json.loads((SCHEMAS_DIR / name).read_text())


# ============================================================================
# TestParseHelpers
# ============================================================================

class TestParseHelpers:
    """Test low-level parsing/conversion helpers."""

    # --- _parse_fv_number ---

    def test_parse_fv_eur_with_version(self):
        assert _parse_fv_number("EUR 33.00 (v5.0 post-FY2025)") == 33.0

    def test_parse_fv_usd_dollar_sign(self):
        assert _parse_fv_number("$191 (v3.0)") == 191.0

    def test_parse_fv_gbp_trailing(self):
        assert _parse_fv_number("240 GBp (v3.0)") == 240.0

    def test_parse_fv_plain_number(self):
        assert _parse_fv_number("29.0") == 29.0

    def test_parse_fv_float_passthrough(self):
        assert _parse_fv_number(33.5) == 33.5

    def test_parse_fv_int_passthrough(self):
        assert _parse_fv_number(100) == 100.0

    def test_parse_fv_none(self):
        assert _parse_fv_number(None) is None

    def test_parse_fv_complex_string(self):
        fv = "EUR 29.0 (adversarial, MAINTAINED post-FY2025. QS Tool 59, Adj 67 Tier B.)"
        assert _parse_fv_number(fv) == 29.0

    def test_parse_fv_dollar_with_space(self):
        fv = "$390 (FTC-adjusted, MAINTAINED post-Q1 FY2026. QS Tool 76, Adj 73)"
        assert _parse_fv_number(fv) == 390.0

    def test_parse_fv_gbp_with_no_prefix(self):
        fv = "190 GBp (v3.0 maintained post-FY2025. All KCs passed. BASE+ case.)"
        assert _parse_fv_number(fv) == 190.0

    # --- _conviction_to_int ---

    def test_conviction_low_medium(self):
        assert _conviction_to_int("low-medium") == 4

    def test_conviction_high(self):
        assert _conviction_to_int("high") == 8

    def test_conviction_alta(self):
        assert _conviction_to_int("Alta") == 8

    def test_conviction_media_alta(self):
        assert _conviction_to_int("Media-Alta") == 7

    def test_conviction_medium(self):
        assert _conviction_to_int("medium") == 5

    def test_conviction_int_passthrough(self):
        assert _conviction_to_int(7) == 7

    def test_conviction_int_clamp_high(self):
        assert _conviction_to_int(15) == 10

    def test_conviction_int_clamp_low(self):
        assert _conviction_to_int(0) == 1

    def test_conviction_none_defaults_medium(self):
        assert _conviction_to_int(None) == 5

    def test_conviction_unknown_string(self):
        assert _conviction_to_int("unknown-level") == 5

    # --- _parse_pct ---

    def test_parse_pct_string_with_percent(self):
        assert _parse_pct("31%") == 31.0

    def test_parse_pct_decimal_string(self):
        assert _parse_pct("4.8%") == 4.8

    def test_parse_pct_float_passthrough(self):
        assert _parse_pct(42.5) == 42.5

    def test_parse_pct_int_passthrough(self):
        assert _parse_pct(50) == 50.0

    def test_parse_pct_none(self):
        assert _parse_pct(None) is None

    def test_parse_pct_invalid(self):
        assert _parse_pct("not-a-number") is None

    # --- _guess_currency ---

    def test_guess_currency_london(self):
        assert _guess_currency("DOM.L") == "GBP"

    def test_guess_currency_xetra(self):
        assert _guess_currency("DTE.DE") == "EUR"

    def test_guess_currency_paris(self):
        assert _guess_currency("EDEN.PA") == "EUR"

    def test_guess_currency_milan(self):
        assert _guess_currency("ENEL.MI") == "EUR"

    def test_guess_currency_amsterdam(self):
        assert _guess_currency("LIGHT.AS") == "EUR"

    def test_guess_currency_us(self):
        assert _guess_currency("ADBE") == "USD"

    def test_guess_currency_default(self):
        assert _guess_currency("MORN") == "USD"

    # --- _date_str ---

    def test_date_str_from_date(self):
        assert _date_str(datetime.date(2026, 1, 26)) == "2026-01-26"

    def test_date_str_from_datetime(self):
        assert _date_str(datetime.datetime(2026, 3, 3, 12, 0)) == "2026-03-03"

    def test_date_str_from_string(self):
        assert _date_str("2026-02-04") == "2026-02-04"

    def test_date_str_none(self):
        assert _date_str(None) is None


# ============================================================================
# TestAdaptPortfolioPosition
# ============================================================================

class TestAdaptPortfolioPosition:
    """Test adapt_portfolio_position with DTE.DE-like raw data."""

    RAW_DTE = {
        "ticker": "DTE.DE",
        "name": "Deutsche Telekom AG",
        "shares": 20.624621,
        "invested_usd": 699.56,
        "avg_cost_usd": 33.91,
        "date_opened": "2026-01-26",
        "thesis": "thesis/active/DTE.DE/thesis.md",
        "conviction": "low-medium",
        "fair_value": "EUR 33.00 (v5.0 post-FY2025. FY2026 EPS guide EUR 2.20 vs EUR 2.50 expected)",
        "last_review": "2026-03-03",
        "exit_plan": "HOLD. TRIM >EUR 34.",
        "notes": "FY2025 ASSESSED S109.",
    }

    def test_field_mapping(self):
        result = adapt_portfolio_position(self.RAW_DTE)
        assert result["ticker"] == "DTE.DE"
        assert result["company_name"] == "Deutsche Telekom AG"
        assert result["shares"] == 20.624621
        assert result["side"] == "LONG"
        assert result["invested_usd"] == 699.56
        assert result["avg_cost"] == 33.91  # mapped from avg_cost_usd
        assert result["conviction"] == 4     # "low-medium" → 4
        assert result["fair_value"] == 33.0  # extracted from string
        assert result["entry_date"] == "2026-01-26"  # mapped from date_opened
        assert result["thesis_path"] == "thesis/active/DTE.DE/thesis.md"
        assert result["currency"] == "EUR"   # guessed from .DE suffix

    def test_validates_against_schema(self):
        schema = _load_schema("portfolio_position.schema.json")
        result = adapt_portfolio_position(self.RAW_DTE)
        validate(instance=result, schema=schema)

    def test_us_ticker_defaults_usd(self):
        raw = {
            "ticker": "ADBE",
            "name": "Adobe Inc.",
            "shares": 2,
            "invested_usd": 541.2,
            "avg_cost_usd": 270.6,
            "conviction": "medium",
            "fair_value": "$390 (FTC-adjusted)",
        }
        result = adapt_portfolio_position(raw)
        assert result["currency"] == "USD"
        assert result["fair_value"] == 390.0
        assert result["conviction"] == 5

    def test_london_ticker_gbp(self):
        raw = {
            "ticker": "DOM.L",
            "name": "Domino's Pizza Group PLC",
            "shares": 175,
            "invested_usd": 436.52,
            "avg_cost_usd": 2.49,
            "conviction": "low",
            "fair_value": "240 GBp (v3.0)",
        }
        result = adapt_portfolio_position(raw)
        assert result["currency"] == "GBP"
        assert result["fair_value"] == 240.0
        assert result["conviction"] == 3

    def test_missing_fair_value_defaults_zero(self):
        raw = {
            "ticker": "TEST",
            "shares": 10,
            "invested_usd": 100,
            "avg_cost_usd": 10,
            "conviction": 5,
            "fair_value": None,
        }
        result = adapt_portfolio_position(raw)
        assert result["fair_value"] == 0.0


# ============================================================================
# TestAdaptClosedPosition
# ============================================================================

class TestAdaptClosedPosition:
    """Test adapt_closed_position with ENEL.MI-like raw data."""

    RAW_ENEL = {
        "ticker": "ENEL.MI",
        "name": "Enel S.p.A.",
        "entry_date": "2026-01-27",
        "exit_date": "2026-01-31",
        "shares": 81,
        "entry_price": 9.225,
        "exit_price": 9.225,
        "entry_currency": "EUR",
        "invested_eur": 747.00,
        "proceeds_eur": 747.00,
        "pnl_amount": 0.00,
        "pnl_percent": 0.0,
        "holding_days": 4,
        "thesis_fv_at_entry": None,
        "fv_reached": False,
        "exit_reason": "error",
    }

    def test_field_mapping(self):
        result = adapt_closed_position(self.RAW_ENEL)
        assert result["ticker"] == "ENEL.MI"
        assert result["company_name"] == "Enel S.p.A."
        assert result["side"] == "LONG"
        assert result["entry_date"] == "2026-01-27"
        assert result["exit_date"] == "2026-01-31"
        assert result["exit_reason"] == "error"
        assert result["duration_days"] == 4  # mapped from holding_days
        assert result["realized_pnl_pct"] == 0.0  # mapped from pnl_percent
        assert result["avg_cost"] == 9.225  # mapped from entry_price
        assert result["exit_price"] == 9.225

    def test_validates_against_schema(self):
        schema = _load_schema("closed_position.schema.json")
        result = adapt_closed_position(self.RAW_ENEL)
        validate(instance=result, schema=schema)

    def test_gbp_entry_price_fallback(self):
        raw = {
            "ticker": "SHEL.L",
            "name": "Shell plc",
            "entry_date": "2026-01-26",
            "exit_date": "2026-02-06",
            "shares": 10.85,
            "entry_price_gbp": 2689,
            "exit_price_gbp": 2774.50,
            "entry_currency": "GBp",
            "pnl_percent": 2.3,
            "holding_days": 11,
            "exit_reason": "thesis_invalidated",
            "quality_score": 36,
            "lesson_learned": "For cyclicals, EV/EBIT mid-cycle is correct.",
        }
        result = adapt_closed_position(raw)
        assert result["avg_cost"] == 2689.0
        assert result["exit_price"] == 2774.50
        assert result["qs_tier"] == "C"  # QS 36 → Tier C
        assert result["lessons"] == ["For cyclicals, EV/EBIT mid-cycle is correct."]
        # Validate against schema
        schema = _load_schema("closed_position.schema.json")
        validate(instance=result, schema=schema)

    def test_quality_score_tier_mapping(self):
        # Tier A (QS >= 75)
        raw_a = {"ticker": "T", "entry_date": "2026-01-01", "exit_date": "2026-02-01",
                 "exit_reason": "target_hit", "quality_score": 78}
        assert adapt_closed_position(raw_a)["qs_tier"] == "A"

        # Tier B (55-74)
        raw_b = {"ticker": "T", "entry_date": "2026-01-01", "exit_date": "2026-02-01",
                 "exit_reason": "target_hit", "quality_score": 60}
        assert adapt_closed_position(raw_b)["qs_tier"] == "B"

        # Tier D (< 35)
        raw_d = {"ticker": "T", "entry_date": "2026-01-01", "exit_date": "2026-02-01",
                 "exit_reason": "target_hit", "quality_score": 30}
        assert adapt_closed_position(raw_d)["qs_tier"] == "D"


# ============================================================================
# TestAdaptDecision
# ============================================================================

class TestAdaptDecision:
    """Test adapt_decision with ADBE-like raw data."""

    RAW_ADBE = {
        "date": "2026-02-04",
        "ticker": "ADBE",
        "action": "BUY",
        "sizing": "4.8%",
        "context": {
            "quality_score": 76,
            "tier": "A",
            "mos": "31%",
            "price_vs_52w": "At 52-week low",
            "conviction": "Alta",
            "macro": "Late cycle, flight to quality",
        },
        "reasoning": "ADBE is a Quality Compounder at 52-week low.\n",
        "outcome": "Pendiente - posicion recien abierta",
    }

    def test_field_mapping(self):
        result = adapt_decision(self.RAW_ADBE)
        assert result["date"] == "2026-02-04"
        assert result["ticker"] == "ADBE"
        assert result["decision"] == "BUY"    # mapped from action
        assert result["conviction"] == 8       # "Alta" → 8
        assert result["reasoning"] == "ADBE is a Quality Compounder at 52-week low.\n"
        assert result["position_size_pct"] == 4.8  # parsed from "4.8%"
        assert result["mos_pct"] == 31.0       # parsed from context.mos
        assert result["outcome"] == "Pendiente - posicion recien abierta"

    def test_validates_against_schema(self):
        schema = _load_schema("decision.schema.json")
        result = adapt_decision(self.RAW_ADBE)
        validate(instance=result, schema=schema)

    def test_add_action_maps_correctly(self):
        raw = {
            "date": "2026-02-05",
            "ticker": "HRB",
            "action": "ADD",
            "sizing": "de 2.7% a 5.7%",
            "context": {"conviction": "Media-Alta", "mos": "42%"},
            "reasoning": "Standing order triggered.\n",
        }
        result = adapt_decision(raw)
        assert result["decision"] == "ADD"
        assert result["conviction"] == 7  # "Media-Alta" → 7

    def test_ecagr_extracted(self):
        raw = {
            "date": "2026-02-20",
            "ticker": "MORN",
            "action": "BUY",
            "sizing": "3.9%",
            "context": {
                "conviction": "Medium",
                "ecagr_3yr": "15.6%",
                "mos": "17%",
            },
            "reasoning": "First E[CAGR]-framework buy.\n",
        }
        result = adapt_decision(raw)
        assert result["e_cagr_pct"] == 15.6
        assert result["mos_pct"] == 17.0


# ============================================================================
# TestLoadFromFiles
# ============================================================================

class TestLoadFromFiles:
    """Test file-loading functions with actual YAML data."""

    def test_load_portfolio_positions_returns_list(self):
        positions = load_portfolio_positions()
        assert isinstance(positions, list)
        assert len(positions) > 0

    def test_load_portfolio_positions_have_required_keys(self):
        positions = load_portfolio_positions()
        for pos in positions:
            assert "ticker" in pos
            assert "shares" in pos
            assert "side" in pos
            assert "invested_usd" in pos
            assert "avg_cost" in pos
            assert "conviction" in pos
            assert "fair_value" in pos
            assert isinstance(pos["conviction"], int)
            assert isinstance(pos["fair_value"], (int, float))

    def test_load_portfolio_positions_validate_against_schema(self):
        schema = _load_schema("portfolio_position.schema.json")
        positions = load_portfolio_positions()
        for pos in positions:
            validate(instance=pos, schema=schema)

    def test_load_closed_positions_returns_list(self):
        closed = load_closed_positions()
        assert isinstance(closed, list)
        assert len(closed) > 0

    def test_load_closed_positions_have_required_keys(self):
        closed = load_closed_positions()
        for pos in closed:
            assert "ticker" in pos
            assert "side" in pos
            assert "entry_date" in pos
            assert "exit_date" in pos
            assert "exit_reason" in pos

    def test_load_closed_positions_validate_against_schema(self):
        schema = _load_schema("closed_position.schema.json")
        closed = load_closed_positions()
        for pos in closed:
            validate(instance=pos, schema=schema)

    def test_load_decisions_returns_list(self):
        decisions = load_decisions()
        assert isinstance(decisions, list)
        assert len(decisions) > 0

    def test_load_decisions_have_required_keys(self):
        decisions = load_decisions()
        for dec in decisions:
            assert "date" in dec
            assert "ticker" in dec
            assert "decision" in dec
            assert "conviction" in dec
            assert "reasoning" in dec
            assert isinstance(dec["conviction"], int)

    def test_load_decisions_validate_against_schema(self):
        schema = _load_schema("decision.schema.json")
        decisions = load_decisions()
        for dec in decisions:
            validate(instance=dec, schema=schema)
