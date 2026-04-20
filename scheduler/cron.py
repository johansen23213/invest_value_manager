"""APScheduler configuration for ValueHunter automated flows."""
from __future__ import annotations
import asyncio
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

logger = logging.getLogger("valuehunter.scheduler")


def _run_async(coro):
    """Run async coroutine from sync scheduler context."""
    loop = asyncio.new_event_loop()
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


def _weekly_job():
    from orchestrator.governor import Governor
    logger.info("Starting weekly screening flow")
    gov = Governor()
    result = _run_async(gov.run_weekly())
    logger.info(f"Weekly screening complete: {result.get('screening', {}).get('total_candidates', 0)} candidates")


def _daily_job():
    from orchestrator.governor import Governor
    logger.info("Starting daily monitoring flow")
    gov = Governor()
    result = _run_async(gov.run_daily_monitor())
    logger.info(f"Daily monitoring complete: success={result.get('success')}")


def _spanish_funds_weekly_job():
    from scrapers.spanish_funds.scheduled_job import run_weekly_check
    logger.info("Starting Spanish value fund ingestion")
    result = run_weekly_check()
    logger.info(
        "Spanish funds ingestion complete: processed=%d skipped=%d errors=%s",
        result["processed"], result["skipped"], result["errors"],
    )


def create_scheduler() -> BackgroundScheduler:
    scheduler = BackgroundScheduler()
    scheduler.add_job(
        _weekly_job,
        CronTrigger(day_of_week="sun", hour=9, minute=0),
        id="weekly_screening",
        name="Weekly Screening (Sunday 09:00)",
    )
    scheduler.add_job(
        _daily_job,
        CronTrigger(day_of_week="mon-fri", hour=18, minute=0),
        id="daily_monitoring",
        name="Daily Monitoring (Mon-Fri 18:00)",
    )
    scheduler.add_job(
        _spanish_funds_weekly_job,
        CronTrigger(day_of_week="mon", hour=8, minute=0),
        id="spanish_funds_weekly",
        name="Spanish Value Fund Ingestion (Monday 08:00)",
    )
    return scheduler


def validate_scheduler() -> dict:
    """Print scheduled jobs without starting."""
    scheduler = create_scheduler()
    jobs = []
    for job in scheduler.get_jobs():
        jobs.append({"id": job.id, "name": job.name, "trigger": str(job.trigger)})
    return {"jobs": jobs, "count": len(jobs)}


if __name__ == "__main__":
    import sys
    if "--validate" in sys.argv:
        info = validate_scheduler()
        print(f"Scheduled {info['count']} jobs:")
        for j in info["jobs"]:
            print(f"  [{j['id']}] {j['name']} — {j['trigger']}")
    else:
        scheduler = create_scheduler()
        scheduler.start()
        print("Scheduler started. Press Ctrl+C to stop.")
        try:
            import time
            while True:
                time.sleep(60)
        except KeyboardInterrupt:
            scheduler.shutdown()
