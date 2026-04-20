"""Tests for persistence of extracted letter data."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from scrapers.spanish_funds.persist import (
    already_processed,
    load_letter,
    persist_letter,
    save_raw_pdf,
    update_last_processed,
)


@pytest.fixture
def kb_root(tmp_path: Path) -> Path:
    (tmp_path / "spanish_funds").mkdir(parents=True)
    return tmp_path


@pytest.fixture
def sample_letter() -> dict:
    return {
        "fund_id": "cobas",
        "fund_name": "Cobas Selección",
        "quarter": "2026-Q1",
        "extracted_at": "2026-04-20T10:00:00Z",
        "extraction_model": "claude-sonnet-4-6",
        "source_url": "https://x",
        "positions": [],
    }


class TestPersistLetter:
    def test_writes_json_to_expected_path(self, kb_root, sample_letter):
        path = persist_letter(sample_letter, kb_root=kb_root)
        assert path == kb_root / "spanish_funds" / "cobas" / "2026-Q1.json"
        assert path.exists()
        loaded = json.loads(path.read_text())
        assert loaded["fund_id"] == "cobas"

    def test_load_round_trip(self, kb_root, sample_letter):
        persist_letter(sample_letter, kb_root=kb_root)
        loaded = load_letter("cobas", "2026-Q1", kb_root=kb_root)
        assert loaded == sample_letter

    def test_load_returns_none_when_missing(self, kb_root):
        assert load_letter("cobas", "2099-Q4", kb_root=kb_root) is None


class TestSaveRawPDF:
    def test_writes_pdf_bytes(self, kb_root):
        path = save_raw_pdf(b"PDFBYTES", fund_id="cobas", quarter="2026-Q1", kb_root=kb_root)
        assert path.exists()
        assert path.read_bytes() == b"PDFBYTES"
        assert path.name == "2026-Q1.pdf"


class TestLastProcessed:
    def test_update_and_check(self, kb_root):
        assert not already_processed("cobas", "abc123", kb_root=kb_root)
        update_last_processed("cobas", quarter="2026-Q1", content_hash="abc123", kb_root=kb_root)
        assert already_processed("cobas", "abc123", kb_root=kb_root)

    def test_different_hash_is_not_processed(self, kb_root):
        update_last_processed("cobas", quarter="2026-Q1", content_hash="abc123", kb_root=kb_root)
        assert not already_processed("cobas", "def456", kb_root=kb_root)
