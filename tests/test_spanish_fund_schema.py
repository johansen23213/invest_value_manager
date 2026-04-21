"""Schema validation tests for spanish_fund_position.schema.json."""
from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import pytest

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "spanish_funds"
SCHEMAS = Path(__file__).resolve().parent.parent / "knowledge_base" / "schemas"


@pytest.fixture
def schema() -> dict:
    return json.loads((SCHEMAS / "spanish_fund_position.schema.json").read_text())


class TestSpanishFundSchema:
    def test_accepts_minimal_valid(self, schema: dict):
        payload = json.loads((FIXTURES / "valid_letter_minimal.json").read_text())
        jsonschema.validate(payload, schema)

    def test_accepts_full_valid(self, schema: dict):
        payload = json.loads((FIXTURES / "valid_letter_full.json").read_text())
        jsonschema.validate(payload, schema)

    def test_rejects_bad_quarter(self, schema: dict):
        payload = json.loads((FIXTURES / "invalid_bad_quarter.json").read_text())
        with pytest.raises(jsonschema.ValidationError):
            jsonschema.validate(payload, schema)

    def test_rejects_bad_action(self, schema: dict):
        payload = json.loads((FIXTURES / "invalid_bad_action.json").read_text())
        with pytest.raises(jsonschema.ValidationError):
            jsonschema.validate(payload, schema)

    def test_requires_fund_id(self, schema: dict):
        payload = {"fund_name": "X", "quarter": "2026-Q1", "extracted_at": "2026-04-20T00:00:00Z",
                   "extraction_model": "m", "source_url": "https://x", "positions": []}
        with pytest.raises(jsonschema.ValidationError):
            jsonschema.validate(payload, schema)

    def test_accepts_fund_id_enum(self, schema: dict):
        for fid in ["cobas", "azvalor", "magallanes", "horos", "valentum"]:
            payload = {
                "fund_id": fid, "fund_name": fid.capitalize(), "quarter": "2026-Q1",
                "extracted_at": "2026-04-20T00:00:00Z", "extraction_model": "m",
                "source_url": "https://x", "positions": [],
            }
            jsonschema.validate(payload, schema)

    def test_rejects_unknown_fund_id(self, schema: dict):
        payload = {"fund_id": "bestinver", "fund_name": "X", "quarter": "2026-Q1",
                   "extracted_at": "2026-04-20T00:00:00Z", "extraction_model": "m",
                   "source_url": "https://x", "positions": []}
        with pytest.raises(jsonschema.ValidationError):
            jsonschema.validate(payload, schema)
