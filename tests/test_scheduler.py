"""Tests for scheduler.cron — APScheduler job configuration."""
import pytest

from scheduler.cron import validate_scheduler, create_scheduler


class TestValidateScheduler:
    def test_returns_two_jobs(self):
        info = validate_scheduler()
        assert info["count"] == 3

    def test_weekly_screening_job_present(self):
        info = validate_scheduler()
        ids = [j["id"] for j in info["jobs"]]
        assert "weekly_screening" in ids

    def test_daily_monitoring_job_present(self):
        info = validate_scheduler()
        ids = [j["id"] for j in info["jobs"]]
        assert "daily_monitoring" in ids

    def test_weekly_job_sunday(self):
        info = validate_scheduler()
        weekly = next(j for j in info["jobs"] if j["id"] == "weekly_screening")
        assert "sun" in weekly["trigger"].lower()

    def test_daily_job_weekdays(self):
        info = validate_scheduler()
        daily = next(j for j in info["jobs"] if j["id"] == "daily_monitoring")
        assert "mon" in daily["trigger"].lower()
        assert "fri" in daily["trigger"].lower()

    def test_create_scheduler_returns_background(self):
        from apscheduler.schedulers.background import BackgroundScheduler
        sched = create_scheduler()
        assert isinstance(sched, BackgroundScheduler)
