"""Tests for LLM-based letter extraction."""
from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import jsonschema
import pytest

from scrapers.spanish_funds.extractor import (
    ExtractorError,
    extract_from_text,
    load_prompt,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "spanish_funds"
SCHEMAS = Path(__file__).resolve().parent.parent / "knowledge_base" / "schemas"


@pytest.fixture
def letter_text() -> str:
    return (FIXTURES / "sample_letter_text.txt").read_text()


@pytest.fixture
def valid_llm_response() -> str:
    return (FIXTURES / "mock_llm_response_valid.json").read_text()


@pytest.fixture
def malformed_llm_response() -> str:
    return (FIXTURES / "mock_llm_response_malformed.json").read_text()


@pytest.fixture
def schema() -> dict:
    return json.loads((SCHEMAS / "spanish_fund_position.schema.json").read_text())


def _mock_message(text: str) -> MagicMock:
    msg = MagicMock()
    msg.content = [MagicMock(text=text, type="text")]
    return msg


class TestLoadPrompt:
    def test_returns_non_empty_prompt(self):
        p = load_prompt("extraction_v1")
        assert "value" in p.lower()
        assert len(p) > 200

    def test_raises_on_missing_prompt(self):
        with pytest.raises(FileNotFoundError):
            load_prompt("does_not_exist")


class TestExtractFromText:
    def test_returns_valid_schema(self, letter_text, valid_llm_response, schema):
        mock_client = MagicMock()
        mock_client.messages.create.return_value = _mock_message(valid_llm_response)
        result = extract_from_text(
            letter_text, fund_id="cobas", quarter="2026-Q1",
            source_url="https://x", client=mock_client,
        )
        jsonschema.validate(result, schema)
        assert result["fund_id"] == "cobas"
        assert result["quarter"] == "2026-Q1"

    def test_retries_once_on_malformed_response(self, letter_text, valid_llm_response, malformed_llm_response):
        mock_client = MagicMock()
        mock_client.messages.create.side_effect = [
            _mock_message(malformed_llm_response),
            _mock_message(valid_llm_response),
        ]
        result = extract_from_text(
            letter_text, fund_id="cobas", quarter="2026-Q1",
            source_url="https://x", client=mock_client,
        )
        assert result["fund_id"] == "cobas"
        assert mock_client.messages.create.call_count == 2

    def test_raises_after_two_consecutive_failures(self, letter_text, malformed_llm_response):
        mock_client = MagicMock()
        mock_client.messages.create.return_value = _mock_message(malformed_llm_response)
        with pytest.raises(ExtractorError):
            extract_from_text(
                letter_text, fund_id="cobas", quarter="2026-Q1",
                source_url="https://x", client=mock_client,
            )
        assert mock_client.messages.create.call_count == 2

    def test_stamps_extraction_metadata(self, letter_text, valid_llm_response):
        mock_client = MagicMock()
        mock_client.messages.create.return_value = _mock_message(valid_llm_response)
        result = extract_from_text(
            letter_text, fund_id="cobas", quarter="2026-Q1",
            source_url="https://x", client=mock_client, model="claude-sonnet-4-6",
        )
        assert result["extraction_model"] == "claude-sonnet-4-6"
        assert "extracted_at" in result
        assert result["source_url"] == "https://x"

    def test_forces_ticker_status_to_unverified(self, letter_text):
        """Even if LLM claims verified, extractor overwrites to unverified."""
        hallucinated = {
            "fund_id": "cobas",
            "fund_name": "Cobas",
            "quarter": "2026-Q1",
            "extracted_at": "PLACEHOLDER",
            "extraction_model": "PLACEHOLDER",
            "source_url": "PLACEHOLDER",
            "fund_return_pct": None,
            "aum_eur": None,
            "positions": [
                {
                    "company_name": "Fake Co",
                    "ticker": "FAKE.XX",
                    "ticker_status": "verified",
                    "weight_pct": 5.0,
                    "action": "new",
                    "upside_pct": None,
                    "thesis_text": None,
                }
            ],
        }
        import json as _json
        mock_client = MagicMock()
        mock_client.messages.create.return_value = _mock_message(_json.dumps(hallucinated))
        result = extract_from_text(
            letter_text, fund_id="cobas", quarter="2026-Q1",
            source_url="https://x", client=mock_client,
        )
        assert result["positions"][0]["ticker_status"] == "unverified"
