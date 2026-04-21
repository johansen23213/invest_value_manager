"""Tests for Valentum URL detection."""
from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from scrapers.spanish_funds.valentum import ValentumScraper


VALENTUM_HTML = """
<html><body>
  <a href="https://valentum.es/wp-content/uploads/2026/04/Carta-1T-2026.pdf">Carta 1T 2026</a>
  <a href="https://valentum.es/wp-content/uploads/2026/01/Carta-4T-2025.pdf">Carta 4T 2025</a>
</body></html>
"""


class TestValentumScraper:
    def test_fund_id_is_valentum(self):
        assert ValentumScraper().fund_id == "valentum"

    def test_detects_latest(self):
        mock_response = MagicMock(status_code=200, text=VALENTUM_HTML)
        mock_response.raise_for_status.return_value = None
        with patch("scrapers.spanish_funds.valentum.httpx.get", return_value=mock_response):
            with patch.object(ValentumScraper, "_fetch_content_hash", return_value="h"):
                meta = ValentumScraper().get_latest_letter()
        assert meta.quarter == "2026-Q1"
        assert "1T-2026" in meta.url

    def test_returns_none_when_empty(self):
        mock_response = MagicMock(status_code=200, text="<html></html>")
        mock_response.raise_for_status.return_value = None
        with patch("scrapers.spanish_funds.valentum.httpx.get", return_value=mock_response):
            assert ValentumScraper().get_latest_letter() is None

    def test_resolves_relative_href(self):
        HTML_RELATIVE = '<html><body><a href="/wp-content/uploads/Carta-1T-2026.pdf">x</a></body></html>'
        mock_response = MagicMock(status_code=200, text=HTML_RELATIVE)
        mock_response.raise_for_status.return_value = None
        with patch("scrapers.spanish_funds.valentum.httpx.get", return_value=mock_response), \
             patch.object(ValentumScraper, "_fetch_content_hash", return_value="h"):
            meta = ValentumScraper().get_latest_letter()
        assert meta.url.startswith("https://")
        assert "/wp-content/uploads/Carta-1T-2026.pdf" in meta.url
