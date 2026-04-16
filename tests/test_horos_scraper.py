"""Tests for the Horos quarterly letter scraper."""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import pytest

from scrapers.horos_scraper import (
    _detect_quarter,
    _detect_fund_return,
    extract_positions,
    parse_letter_text,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures"
SCHEMAS = Path(__file__).resolve().parent.parent / "knowledge_base" / "schemas"

SOURCE_URL = "https://horosam.com/cartas/q4-2025.pdf"


@pytest.fixture
def letter_text() -> str:
    return (FIXTURES / "horos_letter_sample.txt").read_text()


@pytest.fixture
def horos_schema() -> dict:
    return json.loads(
        (SCHEMAS / "horos_position.schema.json").read_text()
    )


# ---------------------------------------------------------------------------
# TestParseLetterText
# ---------------------------------------------------------------------------

class TestParseLetterText:
    def test_extracts_quarter(self, letter_text: str):
        meta = parse_letter_text(letter_text, SOURCE_URL)
        assert meta["quarter"] == "2025-Q4"

    def test_extracts_fund_return(self, letter_text: str):
        meta = parse_letter_text(letter_text, SOURCE_URL)
        assert meta["fund_return_pct"] == pytest.approx(4.2)

    def test_preserves_source_url(self, letter_text: str):
        meta = parse_letter_text(letter_text, SOURCE_URL)
        assert meta["source_url"] == SOURCE_URL


# ---------------------------------------------------------------------------
# TestDetectQuarter
# ---------------------------------------------------------------------------

class TestDetectQuarter:
    def test_q4_2025(self):
        assert _detect_quarter("Q4 2025") == "2025-Q4"

    def test_spanish_cuarto_trimestre(self):
        assert _detect_quarter("cuarto trimestre de 2025") == "2025-Q4"

    def test_spanish_primer_trimestre(self):
        assert _detect_quarter("primer trimestre de 2026") == "2026-Q1"

    def test_compact_4t_format(self):
        assert _detect_quarter("4T 2025 resultados") == "2025-Q4"

    def test_no_quarter(self):
        assert _detect_quarter("nothing here") is None


# ---------------------------------------------------------------------------
# TestDetectFundReturn
# ---------------------------------------------------------------------------

class TestDetectFundReturn:
    def test_positive_return(self):
        assert _detect_fund_return("rentabilidad del +4.2%") == pytest.approx(4.2)

    def test_negative_return(self):
        assert _detect_fund_return("rentabilidad del -2.5%") == pytest.approx(-2.5)

    def test_no_return(self):
        assert _detect_fund_return("nothing here") is None


# ---------------------------------------------------------------------------
# TestExtractPositions
# ---------------------------------------------------------------------------

class TestExtractPositions:
    def test_finds_at_least_three_positions(self, letter_text: str):
        positions = extract_positions(letter_text, "2025-Q4", SOURCE_URL)
        assert len(positions) >= 3

    def test_has_tre_mc(self, letter_text: str):
        positions = extract_positions(letter_text, "2025-Q4", SOURCE_URL)
        tickers = [p["ticker"] for p in positions]
        assert "TRE.MC" in tickers

    def test_has_bab_l(self, letter_text: str):
        positions = extract_positions(letter_text, "2025-Q4", SOURCE_URL)
        tickers = [p["ticker"] for p in positions]
        assert "BAB.L" in tickers

    def test_detects_new_action_for_atym(self, letter_text: str):
        positions = extract_positions(letter_text, "2025-Q4", SOURCE_URL)
        atym = [p for p in positions if p["ticker"] == "ATYM.L"]
        assert len(atym) == 1
        assert atym[0]["action"] == "NEW"

    def test_detects_exited_action_for_gestamp(self, letter_text: str):
        positions = extract_positions(letter_text, "2025-Q4", SOURCE_URL)
        gest = [p for p in positions if p["ticker"] == "GEST.MC"]
        assert len(gest) == 1
        assert gest[0]["action"] == "EXITED"

    def test_maintained_for_main_positions(self, letter_text: str):
        positions = extract_positions(letter_text, "2025-Q4", SOURCE_URL)
        tre = [p for p in positions if p["ticker"] == "TRE.MC"]
        assert len(tre) == 1
        assert tre[0]["action"] == "MAINTAINED"

    def test_extracts_weight(self, letter_text: str):
        positions = extract_positions(letter_text, "2025-Q4", SOURCE_URL)
        tre = [p for p in positions if p["ticker"] == "TRE.MC"][0]
        assert tre["weight_pct"] == pytest.approx(5.2)

    def test_extracts_upside(self, letter_text: str):
        positions = extract_positions(letter_text, "2025-Q4", SOURCE_URL)
        tre = [p for p in positions if p["ticker"] == "TRE.MC"][0]
        assert tre["upside_pct"] == pytest.approx(50.0)

    def test_fund_is_horos_internacional(self, letter_text: str):
        positions = extract_positions(letter_text, "2025-Q4", SOURCE_URL)
        for pos in positions:
            assert pos["fund"] == "HOROS_VALUE_INTERNACIONAL"

    def test_ticker_confidence_is_exact(self, letter_text: str):
        positions = extract_positions(letter_text, "2025-Q4", SOURCE_URL)
        for pos in positions:
            assert pos["ticker_confidence"] == "EXACT"


# ---------------------------------------------------------------------------
# TestSchemaValidation
# ---------------------------------------------------------------------------

class TestSchemaValidation:
    def test_all_positions_validate(self, letter_text: str, horos_schema: dict):
        positions = extract_positions(letter_text, "2025-Q4", SOURCE_URL)
        assert len(positions) >= 3
        for pos in positions:
            jsonschema.validate(instance=pos, schema=horos_schema)

    def test_position_has_required_fields(self, letter_text: str):
        positions = extract_positions(letter_text, "2025-Q4", SOURCE_URL)
        for pos in positions:
            assert pos["letter_quarter"] is not None
            assert pos["company"] != ""
            assert pos["source_url"].startswith("https://")
