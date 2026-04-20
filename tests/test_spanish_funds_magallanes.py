"""Tests for Magallanes URL detection."""
from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from scrapers.spanish_funds.magallanes import MagallanesScraper


MAGALLANES_HTML = """
<html><body>
  <a href="/docs/2026-Q1-carta-magallanes-european.pdf">1T 2026</a>
  <a href="/docs/2025-Q4-carta-magallanes-european.pdf">4T 2025</a>
</body></html>
"""


class TestMagallanesScraper:
    def test_fund_id_is_magallanes(self):
        assert MagallanesScraper().fund_id == "magallanes"

    def test_detects_latest(self):
        mock_response = MagicMock(status_code=200, text=MAGALLANES_HTML)
        mock_response.raise_for_status.return_value = None
        with patch("scrapers.spanish_funds.magallanes.httpx.get", return_value=mock_response):
            with patch.object(MagallanesScraper, "_fetch_content_hash", return_value="h"):
                meta = MagallanesScraper().get_latest_letter()
        assert meta.quarter == "2026-Q1"
        assert "2026-Q1" in meta.url

    def test_returns_none_when_empty(self):
        mock_response = MagicMock(status_code=200, text="<html></html>")
        mock_response.raise_for_status.return_value = None
        with patch("scrapers.spanish_funds.magallanes.httpx.get", return_value=mock_response):
            assert MagallanesScraper().get_latest_letter() is None
