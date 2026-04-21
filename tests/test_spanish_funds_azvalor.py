"""Tests for AzValor URL detection."""
from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from scrapers.spanish_funds.azvalor import AzValorScraper


AZVALOR_HTML = """
<html><body>
  <a href="https://www.azvalor.com/app/uploads/2026/04/Carta-Trimestral-1T-2026.pdf">Carta 1T 2026</a>
  <a href="https://www.azvalor.com/app/uploads/2026/01/Carta-Trimestral-4T-2025.pdf">Carta 4T 2025</a>
</body></html>
"""


class TestAzValorScraper:
    def test_fund_id_is_azvalor(self):
        assert AzValorScraper().fund_id == "azvalor"

    def test_detects_latest_letter(self):
        mock_response = MagicMock(status_code=200, text=AZVALOR_HTML)
        mock_response.raise_for_status.return_value = None
        with patch("scrapers.spanish_funds.azvalor.httpx.get", return_value=mock_response):
            with patch.object(AzValorScraper, "_fetch_content_hash", return_value="h"):
                meta = AzValorScraper().get_latest_letter()
        assert meta.quarter == "2026-Q1"
        assert "1T-2026" in meta.url

    def test_returns_none_when_empty(self):
        mock_response = MagicMock(status_code=200, text="<html></html>")
        mock_response.raise_for_status.return_value = None
        with patch("scrapers.spanish_funds.azvalor.httpx.get", return_value=mock_response):
            assert AzValorScraper().get_latest_letter() is None

    def test_resolves_relative_href(self):
        HTML_RELATIVE = '<html><body><a href="/uploads/Carta-Trimestral-1T-2026.pdf">x</a></body></html>'
        mock_response = MagicMock(status_code=200, text=HTML_RELATIVE)
        mock_response.raise_for_status.return_value = None
        with patch("scrapers.spanish_funds.azvalor.httpx.get", return_value=mock_response), \
             patch.object(AzValorScraper, "_fetch_content_hash", return_value="h"):
            meta = AzValorScraper().get_latest_letter()
        assert meta.url.startswith("https://")
        assert "/uploads/Carta-Trimestral-1T-2026.pdf" in meta.url
