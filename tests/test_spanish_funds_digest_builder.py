"""Tests for Telegram digest construction."""
from __future__ import annotations

import pytest

from scrapers.spanish_funds.digest_builder import build_digest


LETTER_CURRENT = {
    "fund_id": "azvalor",
    "fund_name": "AzValor Internacional",
    "quarter": "2026-Q1",
    "fund_return_pct": 4.2,
    "aum_eur": 1_500_000_000,
    "positions": [
        {"company_name": "Atalaya Mining", "ticker": "ATYM.L", "ticker_status": "verified",
         "weight_pct": 5.1, "action": "new", "thesis_text": "Cobre estructural..."},
        {"company_name": "Telefónica", "ticker": "TEF.MC", "ticker_status": "verified",
         "weight_pct": 3.2, "action": "new", "thesis_text": "Turnaround operativo..."},
        {"company_name": "Alibaba", "ticker": "BABA", "ticker_status": "verified",
         "weight_pct": None, "action": "exited", "thesis_text": None},
        {"company_name": "Renault", "ticker": "RNO.PA", "ticker_status": "verified",
         "weight_pct": 4.0, "action": "increased", "thesis_text": None},
        {"company_name": "Naturgy", "ticker": "NTGY.MC", "ticker_status": "verified",
         "weight_pct": 2.0, "action": "reduced", "thesis_text": None},
        {"company_name": "Sdiptech", "ticker": "SDIP-B.ST", "ticker_status": "unverified",
         "weight_pct": 2.3, "action": "new", "thesis_text": None},
    ],
}


class TestBuildDigest:
    def test_header_contains_fund_and_quarter(self):
        msg = build_digest(LETTER_CURRENT, multi_fund_tickers=[])
        assert "AzValor" in msg
        assert "Q1 2026" in msg

    def test_groups_actions_with_emoji(self):
        msg = build_digest(LETTER_CURRENT, multi_fund_tickers=[])
        assert "🆕 NUEVAS (2)" in msg
        assert "❌ SALIDAS (1)" in msg
        assert "📈 INCREMENTOS (1)" in msg
        assert "📉 REDUCCIONES (1)" in msg

    def test_new_section_shows_thesis_snippet(self):
        msg = build_digest(LETTER_CURRENT, multi_fund_tickers=[])
        assert "Cobre estructural" in msg
        assert "Turnaround" in msg

    def test_multi_fund_tickers_flagged(self):
        msg = build_digest(LETTER_CURRENT, multi_fund_tickers=["ATYM.L", "TRE.MC"])
        assert "Multi-fund" in msg
        assert "ATYM.L" in msg

    def test_unverified_tail_section(self):
        msg = build_digest(LETTER_CURRENT, multi_fund_tickers=[])
        assert "RESOLUCIÓN MANUAL" in msg
        assert "Sdiptech" in msg

    def test_return_and_aum_in_header(self):
        msg = build_digest(LETTER_CURRENT, multi_fund_tickers=[])
        assert "+4.2%" in msg
        assert "€1.5B" in msg
