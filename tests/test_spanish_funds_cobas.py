"""Tests for Cobas URL detection."""
from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from scrapers.spanish_funds.cobas import CobasScraper


COBAS_LETTERS_HTML = """
<html><body>
<div class="cartas-inversor">
  <a href="/uploads/Cobas_Seleccion_Carta_T1_2026.pdf">Carta 1T 2026</a>
  <a href="/uploads/Cobas_Seleccion_Carta_T4_2025.pdf">Carta 4T 2025</a>
</div>
</body></html>
"""


class TestCobasScraper:
    def test_fund_id_is_cobas(self):
        s = CobasScraper()
        assert s.fund_id == "cobas"

    def test_get_latest_letter_returns_most_recent_pdf(self):
        mock_response = MagicMock(status_code=200, text=COBAS_LETTERS_HTML)
        mock_response.raise_for_status.return_value = None
        with patch("scrapers.spanish_funds.cobas.httpx.get", return_value=mock_response):
            with patch.object(CobasScraper, "_fetch_content_hash", return_value="hash123"):
                meta = CobasScraper().get_latest_letter()
        assert meta is not None
        assert meta.quarter == "2026-Q1"
        assert "Cobas_Seleccion_Carta_T1_2026.pdf" in meta.url
        assert meta.content_hash == "hash123"

    def test_returns_none_when_no_letters_found(self):
        mock_response = MagicMock(status_code=200, text="<html><body>empty</body></html>")
        mock_response.raise_for_status.return_value = None
        with patch("scrapers.spanish_funds.cobas.httpx.get", return_value=mock_response):
            meta = CobasScraper().get_latest_letter()
        assert meta is None
