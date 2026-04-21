"""Tests for PDF text extraction helper."""
from __future__ import annotations

from pathlib import Path

import pytest

from scrapers.spanish_funds.pdf import extract_text_from_pdf

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "spanish_funds"


class TestExtractTextFromPDF:
    def test_extracts_expected_string(self):
        text = extract_text_from_pdf(FIXTURES / "sample_simple.pdf")
        assert "Hello ValueHunter" in text

    def test_joins_multiple_pages(self):
        text = extract_text_from_pdf(FIXTURES / "sample_simple.pdf")
        # Fixture has "Page 1" on page 1, "Page 2" on page 2
        assert "Page 1" in text
        assert "Page 2" in text

    def test_raises_on_missing_file(self, tmp_path: Path):
        with pytest.raises(FileNotFoundError):
            extract_text_from_pdf(tmp_path / "nope.pdf")

    def test_returns_empty_string_on_empty_pdf(self, tmp_path: Path):
        from pypdf import PdfWriter
        empty = tmp_path / "empty.pdf"
        w = PdfWriter()
        w.add_blank_page(width=100, height=100)
        with empty.open("wb") as f:
            w.write(f)
        text = extract_text_from_pdf(empty)
        assert text.strip() == ""
