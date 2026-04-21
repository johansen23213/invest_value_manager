"""Tests for the quality_universe merger."""
from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from scrapers.spanish_funds.universe_merger import merge_letter


LETTER_A = {
    "fund_id": "cobas",
    "fund_name": "Cobas Selección",
    "quarter": "2026-Q1",
    "source_url": "https://x/cobas",
    "extracted_at": "2026-04-20T10:00:00Z",
    "extraction_model": "m",
    "positions": [
        {"company_name": "Atalaya Mining", "ticker": "ATYM.L", "ticker_status": "verified",
         "weight_pct": 7.3, "action": "maintained", "thesis_text": "Cobre escaso..."},
        {"company_name": "Semapa", "ticker": "SEM.LS", "ticker_status": "unverified",
         "weight_pct": 3.0, "action": "new", "thesis_text": "Portugal..."},
    ],
}
LETTER_B = {
    "fund_id": "azvalor",
    "fund_name": "AzValor Internacional",
    "quarter": "2026-Q1",
    "source_url": "https://x/az",
    "extracted_at": "2026-04-20T10:00:00Z",
    "extraction_model": "m",
    "positions": [
        {"company_name": "Atalaya Mining", "ticker": "ATYM.L", "ticker_status": "verified",
         "weight_pct": 5.1, "action": "increased", "thesis_text": "Permisos..."},
    ],
}


@pytest.fixture
def universe_path(tmp_path: Path) -> Path:
    p = tmp_path / "quality_universe.yaml"
    p.write_text("{}\n")  # empty mapping
    return p


class TestMergeLetter:
    def test_first_merge_creates_entry(self, universe_path):
        merge_letter(LETTER_A, universe_path=universe_path)
        data = yaml.safe_load(universe_path.read_text())
        assert "ATYM.L" in data
        atym = data["ATYM.L"]
        assert atym["conviction_signal"] == "1_fund"
        assert len(atym["sources"]) == 1
        assert atym["sources"][0]["fund"] == "cobas"

    def test_skips_unverified_positions(self, universe_path):
        merge_letter(LETTER_A, universe_path=universe_path)
        data = yaml.safe_load(universe_path.read_text())
        assert "SEM.LS" not in data

    def test_second_fund_appends_and_boosts_conviction(self, universe_path):
        merge_letter(LETTER_A, universe_path=universe_path)
        merge_letter(LETTER_B, universe_path=universe_path)
        data = yaml.safe_load(universe_path.read_text())
        atym = data["ATYM.L"]
        assert atym["conviction_signal"] == "2_funds"
        assert len(atym["sources"]) == 2
        funds_in_sources = {s["fund"] for s in atym["sources"]}
        assert funds_in_sources == {"cobas", "azvalor"}

    def test_reprocessing_same_fund_quarter_is_idempotent(self, universe_path):
        merge_letter(LETTER_A, universe_path=universe_path)
        merge_letter(LETTER_A, universe_path=universe_path)  # replay
        data = yaml.safe_load(universe_path.read_text())
        assert len(data["ATYM.L"]["sources"]) == 1

    def test_thesis_snippets_trimmed_to_500_chars(self, universe_path):
        long_letter = dict(LETTER_A)
        long_letter["positions"] = [dict(LETTER_A["positions"][0], thesis_text="x" * 2000)]
        merge_letter(long_letter, universe_path=universe_path)
        data = yaml.safe_load(universe_path.read_text())
        assert len(data["ATYM.L"]["thesis_snippets"]["cobas"]) == 500

    def test_creates_universe_file_when_missing(self, tmp_path):
        missing = tmp_path / "does-not-exist.yaml"
        # Will not crash — should create the file
        merge_letter(LETTER_A, universe_path=missing)
        assert missing.exists()
        data = yaml.safe_load(missing.read_text())
        assert "ATYM.L" in data
