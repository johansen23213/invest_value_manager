"""Tests for Horos legacy JSON → unified schema backfill."""
from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import pytest

from scripts.migrate_horos_to_unified_schema import migrate_legacy_json

SCHEMAS = Path(__file__).resolve().parent.parent / "knowledge_base" / "schemas"

LEGACY_SAMPLE = [
    {
        "letter_quarter": "2025-Q4",
        "fund": "HOROS_VALUE_INTERNACIONAL",
        "company": "Atalaya Mining",
        "ticker": "ATYM.L",
        "ticker_confidence": "EXACT",
        "weight_pct": 7.3,
        "action": "MAINTAINED",
        "thesis_summary": "Cobre estructural...",
        "upside_pct": 45,
        "source_url": "https://horosam.com/q4-2025.pdf",
        "scraped_date": "2026-01-15",
    },
    {
        "letter_quarter": "2025-Q4",
        "fund": "HOROS_VALUE_INTERNACIONAL",
        "company": "Semapa",
        "ticker": None,
        "ticker_confidence": "UNRESOLVED",
        "weight_pct": 3.0,
        "action": "NEW",
        "thesis_summary": None,
        "source_url": "https://horosam.com/q4-2025.pdf",
        "scraped_date": "2026-01-15",
    },
]


@pytest.fixture
def schema() -> dict:
    return json.loads((SCHEMAS / "spanish_fund_position.schema.json").read_text())


class TestMigrateLegacyJson:
    def test_groups_positions_into_single_letter(self, schema):
        migrated = migrate_legacy_json(LEGACY_SAMPLE)
        assert len(migrated) == 1
        letter = migrated[0]
        jsonschema.validate(letter, schema)
        assert letter["fund_id"] == "horos"
        assert letter["quarter"] == "2025-Q4"
        assert len(letter["positions"]) == 2

    def test_maps_legacy_status_to_unified(self):
        migrated = migrate_legacy_json(LEGACY_SAMPLE)
        positions = migrated[0]["positions"]
        by_name = {p["company_name"]: p for p in positions}
        # EXACT -> verified; UNRESOLVED -> unverified; action uppercase -> lowercase
        assert by_name["Atalaya Mining"]["ticker_status"] == "verified"
        assert by_name["Atalaya Mining"]["action"] == "maintained"
        # UNRESOLVED + null ticker: emit placeholder ticker "" ticker_status="unverified"
        assert by_name["Semapa"]["ticker_status"] == "unverified"
        assert by_name["Semapa"]["action"] == "new"
