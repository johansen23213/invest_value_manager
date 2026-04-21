"""Tests for new Horos URL detection."""
from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from scrapers.spanish_funds.horos import HorosScraper


HOROS_HTML = """
<html><body>
<div class="cartas">
  <a href="https://horosam.com/carta-2026-q1.pdf">Carta Q1 2026</a>
  <a href="https://horosam.com/carta-2025-q4.pdf">Carta Q4 2025</a>
</div>
</body></html>
"""


class TestHorosScraper:
    def test_fund_id_is_horos(self):
        assert HorosScraper().fund_id == "horos"

    def test_detects_latest(self):
        mock_response = MagicMock(status_code=200, text=HOROS_HTML)
        mock_response.raise_for_status.return_value = None
        with patch("scrapers.spanish_funds.horos.httpx.get", return_value=mock_response):
            with patch.object(HorosScraper, "_fetch_content_hash", return_value="h"):
                meta = HorosScraper().get_latest_letter()
        assert meta.quarter == "2026-Q1"

    def test_matches_carta_trimestral_pattern(self):
        HTML = '<html><body><a href="https://horosam.com/carta-trimestral-2026-q1.pdf">x</a></body></html>'
        mock_response = MagicMock(status_code=200, text=HTML)
        mock_response.raise_for_status.return_value = None
        with patch("scrapers.spanish_funds.horos.httpx.get", return_value=mock_response), \
             patch.object(HorosScraper, "_fetch_content_hash", return_value="h"):
            meta = HorosScraper().get_latest_letter()
        assert meta is not None
        assert meta.quarter == "2026-Q1"
