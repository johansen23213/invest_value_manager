"""Tests for ticker resolution against yfinance."""
from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from scrapers.spanish_funds.ticker_resolver import (
    TickerResolution,
    resolve_positions,
    resolve_ticker,
)


class TestResolveTicker:
    def test_verified_when_yfinance_returns_longName(self):
        with patch("scrapers.spanish_funds.ticker_resolver.yf.Ticker") as MockT:
            MockT.return_value.info = {"longName": "Atalaya Mining PLC", "regularMarketPrice": 5.2}
            r = resolve_ticker("ATYM.L")
        assert r.status == "verified"
        assert r.ticker == "ATYM.L"
        assert r.resolved_name == "Atalaya Mining PLC"

    def test_unverified_when_longName_missing(self):
        with patch("scrapers.spanish_funds.ticker_resolver.yf.Ticker") as MockT:
            MockT.return_value.info = {}
            r = resolve_ticker("FAKE.XX")
        assert r.status == "unverified"
        assert r.ticker == "FAKE.XX"
        assert r.resolved_name is None

    def test_unverified_when_yfinance_raises(self):
        with patch("scrapers.spanish_funds.ticker_resolver.yf.Ticker") as MockT:
            MockT.side_effect = Exception("network boom")
            r = resolve_ticker("ATYM.L")
        assert r.status == "unverified"

    def test_empty_ticker_returns_unverified(self):
        r = resolve_ticker("")
        assert r.status == "unverified"


class TestResolvePositions:
    def test_updates_positions_in_place(self):
        positions = [
            {"company_name": "Atalaya Mining", "ticker": "ATYM.L", "ticker_status": "unverified", "action": "maintained"},
            {"company_name": "Fake Co", "ticker": "FAKE.XX", "ticker_status": "unverified", "action": "new"},
        ]
        def fake_info(t):
            if t == "ATYM.L":
                return MagicMock(info={"longName": "Atalaya Mining PLC"})
            return MagicMock(info={})

        with patch("scrapers.spanish_funds.ticker_resolver.yf.Ticker", side_effect=fake_info):
            updated = resolve_positions(positions)

        assert updated[0]["ticker_status"] == "verified"
        assert updated[1]["ticker_status"] == "unverified"
