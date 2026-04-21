"""End-to-end pipeline test using a concrete scraper + mocked I/O."""
from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from scrapers.spanish_funds.base import LetterMeta
from scrapers.spanish_funds.cobas import CobasScraper
from scrapers.spanish_funds.extractor import ExtractorError
from scrapers.spanish_funds.pipeline import PipelineResult, process_scraper

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "spanish_funds"


@pytest.fixture
def valid_llm_response_text() -> str:
    return (FIXTURES / "mock_llm_response_valid.json").read_text()


def _mock_anthropic_msg(text: str) -> MagicMock:
    msg = MagicMock()
    msg.content = [MagicMock(text=text, type="text")]
    return msg


class TestProcessScraper:
    def test_full_pipeline_happy_path(self, valid_llm_response_text, tmp_path: Path):
        scraper = CobasScraper()
        letter_meta = LetterMeta(
            url="https://www.cobasam.com/q1-2026.pdf",
            quarter="2026-Q1",
            content_hash="fresh-hash",
        )
        with patch.object(CobasScraper, "get_latest_letter", return_value=letter_meta), \
             patch("scrapers.spanish_funds.pipeline._download_pdf", return_value=b"PDFBYTES"), \
             patch("scrapers.spanish_funds.pipeline.extract_text_from_pdf",
                   return_value="letter text"), \
             patch("scrapers.spanish_funds.pipeline.resolve_positions",
                   side_effect=lambda positions: [dict(p, ticker_status="verified") for p in positions]):
            mock_client = MagicMock()
            mock_client.messages.create.return_value = _mock_anthropic_msg(valid_llm_response_text)

            result = process_scraper(scraper, client=mock_client, kb_root=tmp_path)

        assert isinstance(result, PipelineResult)
        assert result.processed is True
        assert result.quarter == "2026-Q1"
        assert result.persisted_path.exists()
        letter = json.loads(result.persisted_path.read_text())
        assert letter["fund_id"] == "cobas"
        assert all(p["ticker_status"] == "verified" for p in letter["positions"])

    def test_skips_when_already_processed(self, tmp_path: Path):
        scraper = CobasScraper()
        letter_meta = LetterMeta(url="https://x", quarter="2026-Q1", content_hash="seen")

        # Pre-populate last_processed
        from scrapers.spanish_funds.persist import update_last_processed
        update_last_processed("cobas", "2026-Q1", "seen", kb_root=tmp_path)

        with patch.object(CobasScraper, "get_latest_letter", return_value=letter_meta):
            result = process_scraper(scraper, client=MagicMock(), kb_root=tmp_path)

        assert result.processed is False
        assert result.skipped_reason == "already_processed"

    def test_skips_when_no_letter_found(self, tmp_path: Path):
        scraper = CobasScraper()
        with patch.object(CobasScraper, "get_latest_letter", return_value=None):
            result = process_scraper(scraper, client=MagicMock(), kb_root=tmp_path)
        assert result.processed is False
        assert result.skipped_reason == "no_letter_found"

    def test_skips_when_download_fails(self, tmp_path: Path):
        scraper = CobasScraper()
        letter_meta = LetterMeta(url="https://x", quarter="2026-Q1", content_hash="hash1")
        with patch.object(CobasScraper, "get_latest_letter", return_value=letter_meta), \
             patch("scrapers.spanish_funds.pipeline._download_pdf",
                   side_effect=RuntimeError("connection refused")):
            result = process_scraper(scraper, client=MagicMock(), kb_root=tmp_path)
        assert result.processed is False
        assert result.skipped_reason == "download_failed"
        assert "connection refused" in result.error

    def test_skips_when_extraction_fails(self, tmp_path: Path):
        scraper = CobasScraper()
        letter_meta = LetterMeta(url="https://x", quarter="2026-Q1", content_hash="hash2")
        with patch.object(CobasScraper, "get_latest_letter", return_value=letter_meta), \
             patch("scrapers.spanish_funds.pipeline._download_pdf", return_value=b"PDFBYTES"), \
             patch("scrapers.spanish_funds.pipeline.extract_text_from_pdf", return_value="text"), \
             patch("scrapers.spanish_funds.pipeline.extract_from_text",
                   side_effect=ExtractorError("bad llm output")):
            result = process_scraper(scraper, client=MagicMock(), kb_root=tmp_path)
        assert result.processed is False
        assert result.skipped_reason == "extraction_failed"
        assert "bad llm output" in result.error

    def test_returns_error_when_get_latest_letter_raises(self, tmp_path: Path):
        scraper = CobasScraper()
        with patch.object(CobasScraper, "get_latest_letter",
                          side_effect=RuntimeError("network timeout")):
            result = process_scraper(scraper, client=MagicMock(), kb_root=tmp_path)
        assert result.processed is False
        assert result.error == "network timeout"
        assert result.skipped_reason is None
