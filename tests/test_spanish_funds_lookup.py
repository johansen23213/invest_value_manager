"""Tests for the cross-fund contextual lookup used by the Web Researcher."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from scrapers.spanish_funds.lookup import lookup_spanish_funds


@pytest.fixture
def kb_root(tmp_path: Path) -> Path:
    root = tmp_path / "knowledge_base" / "spanish_funds"
    for fund_id, positions in (
        ("cobas", [
            {"company_name": "Atalaya Mining", "ticker": "ATYM.L", "ticker_status": "verified",
             "weight_pct": 7.3, "action": "maintained", "thesis_text": "Cobre..."},
        ]),
        ("azvalor", [
            {"company_name": "Atalaya Mining", "ticker": "ATYM.L", "ticker_status": "verified",
             "weight_pct": 5.1, "action": "increased", "thesis_text": "Permisos..."},
        ]),
    ):
        d = root / fund_id
        d.mkdir(parents=True)
        (d / "2026-Q1.json").write_text(json.dumps({
            "fund_id": fund_id, "fund_name": fund_id.capitalize(),
            "quarter": "2026-Q1", "source_url": "https://x",
            "extracted_at": "2026-04-20T10:00:00Z", "extraction_model": "m",
            "positions": positions,
        }))
    return tmp_path


class TestLookup:
    def test_finds_position_across_multiple_funds(self, kb_root):
        result = lookup_spanish_funds("ATYM.L", kb_root=kb_root / "knowledge_base")
        assert result["ticker"] == "ATYM.L"
        assert result["fund_count"] == 2
        fund_ids = {h["fund_id"] for h in result["holdings"]}
        assert fund_ids == {"cobas", "azvalor"}

    def test_uses_latest_quarter_only(self, kb_root):
        # Write an older quarter to one of the funds
        older = kb_root / "knowledge_base" / "spanish_funds" / "cobas" / "2025-Q4.json"
        older.write_text(json.dumps({
            "fund_id": "cobas", "fund_name": "Cobas", "quarter": "2025-Q4",
            "source_url": "https://x", "extracted_at": "2025-10-01T00:00:00Z",
            "extraction_model": "m",
            "positions": [
                {"company_name": "Old Pos", "ticker": "OLD.MC", "ticker_status": "verified",
                 "weight_pct": 1.0, "action": "exited", "thesis_text": None},
            ],
        }))
        result = lookup_spanish_funds("OLD.MC", kb_root=kb_root / "knowledge_base")
        # Not in the latest quarter, so should not appear
        assert result["fund_count"] == 0

    def test_returns_empty_when_no_match(self, kb_root):
        result = lookup_spanish_funds("NONE.XX", kb_root=kb_root / "knowledge_base")
        assert result["fund_count"] == 0
        assert result["holdings"] == []

    def test_ignores_unverified(self, kb_root):
        # Patch one of the files to have unverified status for ATYM.L
        path = kb_root / "knowledge_base" / "spanish_funds" / "cobas" / "2026-Q1.json"
        data = json.loads(path.read_text())
        data["positions"][0]["ticker_status"] = "unverified"
        path.write_text(json.dumps(data))
        result = lookup_spanish_funds("ATYM.L", kb_root=kb_root / "knowledge_base")
        assert result["fund_count"] == 1  # only azvalor remains
