"""Tests for the weekly scheduled job."""
from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock, patch

import yaml

from scheduler.cron import create_scheduler


class TestSchedulerIntegration:
    def test_spanish_funds_job_registered(self):
        scheduler = create_scheduler()
        job_ids = [j.id for j in scheduler.get_jobs()]
        assert "spanish_funds_weekly" in job_ids

    def test_spanish_funds_job_fires_on_monday_8am(self):
        scheduler = create_scheduler()
        job = next(j for j in scheduler.get_jobs() if j.id == "spanish_funds_weekly")
        trigger_str = str(job.trigger)
        assert "mon" in trigger_str.lower()
        assert "08" in trigger_str or "hour='8'" in trigger_str


class TestScheduledJobFunction:
    def test_calls_all_scrapers_and_notifies(self):
        from scrapers.spanish_funds.scheduled_job import run_weekly_check
        from scrapers.spanish_funds.pipeline import PipelineResult

        # Two processed, one skipped
        results = [
            PipelineResult(fund_id="cobas", processed=True, quarter="2026-Q1",
                           persisted_path=None),
            PipelineResult(fund_id="azvalor", processed=False, skipped_reason="already_processed"),
            PipelineResult(fund_id="magallanes", processed=False, skipped_reason="no_letter_found"),
        ]

        mock_scrapers = [MagicMock(fund_id="cobas"), MagicMock(fund_id="azvalor"), MagicMock(fund_id="magallanes")]

        with patch("scrapers.spanish_funds.scheduled_job.process_scraper", side_effect=results), \
             patch("scrapers.spanish_funds.scheduled_job._anthropic_client", return_value=MagicMock()), \
             patch("scrapers.spanish_funds.scheduled_job._all_scrapers", return_value=mock_scrapers), \
             patch("scrapers.spanish_funds.scheduled_job._send_telegram") as mock_send, \
             patch("scrapers.spanish_funds.scheduled_job.load_letter", return_value={
                 "fund_id": "cobas", "fund_name": "Cobas", "quarter": "2026-Q1",
                 "fund_return_pct": None, "aum_eur": None, "positions": [],
                 "source_url": "x", "extracted_at": "x", "extraction_model": "m",
             }):
            out = run_weekly_check()

        assert out["processed"] == 1
        assert out["skipped"] == 2
        # Telegram only sent for processed letters
        mock_send.assert_called_once()


class TestExtractMultiFundTickers:
    def test_returns_tickers_with_multi_fund_signal(self, tmp_path):
        from scrapers.spanish_funds.scheduled_job import _extract_multi_fund_tickers

        universe_path = tmp_path / "quality_universe.yaml"
        universe_path.write_text(yaml.safe_dump({
            "ATYM.L": {"conviction_signal": "2_funds", "sources": []},
            "SEM.LS": {"conviction_signal": "1_fund", "sources": []},
        }))
        letter = {
            "positions": [
                {"ticker": "ATYM.L"},
                {"ticker": "SEM.LS"},
                {"ticker": "OTHER.L"},
            ]
        }
        result = _extract_multi_fund_tickers(letter, universe_path=universe_path)
        assert result == ["ATYM.L"]

    def test_returns_empty_when_universe_missing(self, tmp_path):
        from scrapers.spanish_funds.scheduled_job import _extract_multi_fund_tickers

        missing = tmp_path / "does-not-exist.yaml"
        letter = {"positions": [{"ticker": "ATYM.L"}]}
        result = _extract_multi_fund_tickers(letter, universe_path=missing)
        assert result == []

    def test_three_plus_funds_included(self, tmp_path):
        from scrapers.spanish_funds.scheduled_job import _extract_multi_fund_tickers

        universe_path = tmp_path / "quality_universe.yaml"
        universe_path.write_text(yaml.safe_dump({
            "TICK.L": {"conviction_signal": "3+_funds", "sources": []},
        }))
        letter = {"positions": [{"ticker": "TICK.L"}]}
        result = _extract_multi_fund_tickers(letter, universe_path=universe_path)
        assert result == ["TICK.L"]


class TestTelegramAlertOnFailure:
    def _run_with_results(self, results, mock_scrapers):
        from scrapers.spanish_funds.scheduled_job import run_weekly_check

        with patch("scrapers.spanish_funds.scheduled_job.process_scraper", side_effect=results), \
             patch("scrapers.spanish_funds.scheduled_job._anthropic_client", return_value=MagicMock()), \
             patch("scrapers.spanish_funds.scheduled_job._all_scrapers", return_value=mock_scrapers), \
             patch("scrapers.spanish_funds.scheduled_job._send_telegram") as mock_send, \
             patch("scrapers.spanish_funds.scheduled_job.load_letter", return_value=None):
            out = run_weekly_check()
        return out, mock_send

    def test_alerts_on_download_failed(self):
        from scrapers.spanish_funds.pipeline import PipelineResult

        results = [
            PipelineResult(fund_id="cobas", processed=False,
                           skipped_reason="download_failed", error="timeout"),
        ]
        mock_scrapers = [MagicMock(fund_id="cobas")]
        out, mock_send = self._run_with_results(results, mock_scrapers)
        mock_send.assert_called_once()
        call_arg = mock_send.call_args[0][0]
        assert "download_failed" in call_arg
        assert "cobas" in call_arg

    def test_alerts_on_extraction_failed(self):
        from scrapers.spanish_funds.pipeline import PipelineResult

        results = [
            PipelineResult(fund_id="horos", processed=False,
                           skipped_reason="extraction_failed", error="llm error"),
        ]
        mock_scrapers = [MagicMock(fund_id="horos")]
        out, mock_send = self._run_with_results(results, mock_scrapers)
        mock_send.assert_called_once()

    def test_no_alert_on_no_letter_found(self):
        from scrapers.spanish_funds.pipeline import PipelineResult

        results = [
            PipelineResult(fund_id="cobas", processed=False,
                           skipped_reason="no_letter_found"),
        ]
        mock_scrapers = [MagicMock(fund_id="cobas")]
        out, mock_send = self._run_with_results(results, mock_scrapers)
        mock_send.assert_not_called()

    def test_no_alert_on_already_processed(self):
        from scrapers.spanish_funds.pipeline import PipelineResult

        results = [
            PipelineResult(fund_id="cobas", processed=False,
                           skipped_reason="already_processed"),
        ]
        mock_scrapers = [MagicMock(fund_id="cobas")]
        out, mock_send = self._run_with_results(results, mock_scrapers)
        mock_send.assert_not_called()
