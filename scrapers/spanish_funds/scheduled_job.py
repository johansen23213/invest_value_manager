"""Scheduled job wrapper: runs all 5 fund scrapers and ships a digest."""
from __future__ import annotations

import asyncio
import logging
import os
from pathlib import Path
from typing import Any

from scrapers.spanish_funds.azvalor import AzValorScraper
from scrapers.spanish_funds.cobas import CobasScraper
from scrapers.spanish_funds.digest_builder import build_digest
from scrapers.spanish_funds.horos import HorosScraper
from scrapers.spanish_funds.magallanes import MagallanesScraper
from scrapers.spanish_funds.persist import load_letter
from scrapers.spanish_funds.pipeline import PipelineResult, process_scraper
from scrapers.spanish_funds.universe_merger import merge_letter
from scrapers.spanish_funds.valentum import ValentumScraper

logger = logging.getLogger("valuehunter.spanish_funds.scheduled_job")


def _extract_multi_fund_tickers(letter: dict, universe_path: Path | None = None) -> list[str]:
    """Return tickers from this letter that appear in the universe with 2+ fund coverage."""
    import yaml
    from scrapers.spanish_funds.universe_merger import DEFAULT_UNIVERSE_PATH
    path = universe_path or DEFAULT_UNIVERSE_PATH
    if not path.exists():
        return []
    try:
        data = yaml.safe_load(path.read_text()) or {}
    except Exception:
        return []
    result = []
    for pos in letter.get("positions", []):
        ticker = pos.get("ticker")
        if ticker and data.get(ticker, {}).get("conviction_signal", "1_fund") != "1_fund":
            result.append(ticker)
    return result


def _anthropic_client():
    import anthropic
    return anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


async def _send_telegram_async(message: str) -> bool:
    from notifications.telegram import TelegramNotifier
    return await TelegramNotifier().send(message)


def _send_telegram(message: str) -> bool:
    return asyncio.run(_send_telegram_async(message))


def _all_scrapers():
    return [CobasScraper(), AzValorScraper(), MagallanesScraper(), HorosScraper(), ValentumScraper()]


def run_weekly_check() -> dict[str, Any]:
    """Iterate all funds; process new letters; merge to universe; send digest."""
    client = _anthropic_client()
    processed = 0
    skipped = 0
    errors: list[str] = []

    for scraper in _all_scrapers():
        try:
            result: PipelineResult = process_scraper(scraper, client=client)
        except Exception as e:
            logger.exception("scraper %s failed", scraper.fund_id)
            errors.append(f"{scraper.fund_id}: {e}")
            skipped += 1
            continue

        if not result.processed:
            skipped += 1
            # Alert operator on real failures (not just "no new letter found")
            if result.skipped_reason in ("download_failed", "extraction_failed"):
                try:
                    _send_telegram(
                        f"⚠️ Spanish funds: {result.fund_id} {result.quarter or ''} — "
                        f"{result.skipped_reason}: {result.error}"
                    )
                except Exception:
                    logger.exception("alert send failed for %s", result.fund_id)
            continue

        processed += 1
        letter = load_letter(result.fund_id, result.quarter)
        if letter is None:
            continue
        try:
            merge_letter(letter)
        except Exception:
            logger.exception("universe merge failed for %s %s", result.fund_id, result.quarter)

        multi = _extract_multi_fund_tickers(letter)
        digest = build_digest(letter, multi_fund_tickers=multi)
        _send_telegram(digest)

    return {"processed": processed, "skipped": skipped, "errors": errors}
