"""Tests for the weekly scheduled job."""
from __future__ import annotations

from unittest.mock import MagicMock, patch

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
