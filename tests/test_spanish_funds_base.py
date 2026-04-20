"""Tests for the abstract base fund scraper."""
from __future__ import annotations

from pathlib import Path

import pytest

from scrapers.spanish_funds.base import FundScraper, LetterMeta


class DummyScraper(FundScraper):
    fund_id = "cobas"
    fund_name = "Cobas Selección"

    def get_latest_letter(self) -> LetterMeta | None:
        return LetterMeta(
            url="https://cobasam.com/q1-2026.pdf",
            quarter="2026-Q1",
            content_hash="abc123",
        )


class IncompleteScraper(FundScraper):
    fund_id = "cobas"
    fund_name = "X"
    # missing get_latest_letter


class TestFundScraper:
    def test_cannot_instantiate_abstract(self):
        with pytest.raises(TypeError):
            IncompleteScraper()

    def test_concrete_scraper_has_fund_id(self):
        s = DummyScraper()
        assert s.fund_id == "cobas"

    def test_concrete_scraper_has_fund_name(self):
        s = DummyScraper()
        assert s.fund_name == "Cobas Selección"

    def test_get_latest_letter_returns_meta(self):
        s = DummyScraper()
        meta = s.get_latest_letter()
        assert meta.quarter == "2026-Q1"
        assert meta.url == "https://cobasam.com/q1-2026.pdf"
        assert meta.content_hash == "abc123"

    def test_letter_meta_is_frozen(self):
        meta = LetterMeta(url="https://x", quarter="2026-Q1", content_hash="h")
        with pytest.raises(Exception):  # dataclass frozen raises FrozenInstanceError
            meta.url = "https://y"

    def test_invalid_fund_id_class_var_raises_on_instantiation(self):
        class BadScraper(FundScraper):
            fund_id = "nothing"
            fund_name = "X"
            def get_latest_letter(self): return None
        with pytest.raises(ValueError, match="fund_id"):
            BadScraper()
