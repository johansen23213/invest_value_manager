"""Orchestration: glues scraper + download + extract + resolve + persist."""
from __future__ import annotations

import hashlib
import logging
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

import httpx

from scrapers.spanish_funds.base import FundScraper, LetterMeta
from scrapers.spanish_funds.extractor import AnthropicClient, ExtractorError, extract_from_text
from scrapers.spanish_funds.pdf import extract_text_from_pdf
from scrapers.spanish_funds.persist import (
    already_processed,
    persist_letter,
    save_raw_pdf,
    update_last_processed,
)
from scrapers.spanish_funds.ticker_resolver import resolve_positions

logger = logging.getLogger("valuehunter.spanish_funds.pipeline")

SkipReason = Literal["no_letter_found", "already_processed", "download_failed", "extraction_failed"]


@dataclass
class PipelineResult:
    fund_id: str
    processed: bool
    quarter: str | None = None
    persisted_path: Path | None = None
    skipped_reason: SkipReason | None = None
    error: str | None = None


def _download_pdf(url: str) -> bytes:
    """Download PDF with 3× exponential backoff retry."""
    delays = [1, 2, 4]
    last_err: Exception | None = None
    for i, d in enumerate(delays):
        try:
            r = httpx.get(url, follow_redirects=True, timeout=60)
            r.raise_for_status()
            return r.content
        except httpx.HTTPError as e:
            last_err = e
            if i < len(delays) - 1:  # only sleep between attempts, not after the last one
                time.sleep(d)
    raise RuntimeError(f"download failed after {len(delays)} attempts: {last_err}")


def process_scraper(
    scraper: FundScraper,
    client: AnthropicClient,
    kb_root: Path | None = None,
) -> PipelineResult:
    fid = scraper.fund_id
    try:
        meta = scraper.get_latest_letter()
    except Exception as e:
        return PipelineResult(fund_id=fid, processed=False, error=str(e))

    if meta is None:
        return PipelineResult(fund_id=fid, processed=False, skipped_reason="no_letter_found")

    if already_processed(fid, meta.content_hash, kb_root=kb_root):
        return PipelineResult(
            fund_id=fid, processed=False, quarter=meta.quarter,
            skipped_reason="already_processed",
        )

    try:
        pdf_bytes = _download_pdf(meta.url)
    except Exception as e:
        return PipelineResult(fund_id=fid, processed=False,
                              quarter=meta.quarter, skipped_reason="download_failed", error=str(e))

    pdf_path = save_raw_pdf(pdf_bytes, fund_id=fid, quarter=meta.quarter, kb_root=kb_root)
    # If the content_hash wasn't trustworthy (e.g. no ETag), recompute on bytes for dedup safety.
    real_hash = hashlib.sha256(pdf_bytes).hexdigest()[:16]

    letter_text = extract_text_from_pdf(pdf_path)

    try:
        extracted = extract_from_text(
            letter_text,
            fund_id=fid,
            quarter=meta.quarter,
            source_url=meta.url,
            client=client,
        )
    except ExtractorError as e:
        return PipelineResult(fund_id=fid, processed=False,
                              quarter=meta.quarter, skipped_reason="extraction_failed", error=str(e))

    extracted["positions"] = resolve_positions(extracted.get("positions", []))

    path = persist_letter(extracted, kb_root=kb_root)
    try:
        update_last_processed(
            fid, quarter=meta.quarter,
            content_hash=real_hash, url_hash=meta.content_hash,
            kb_root=kb_root, extraction_model=extracted.get("extraction_model", ""),
        )
    except Exception as e:
        logger.error("update_last_processed failed after persist; rolling back %s: %s", path, e)
        try:
            path.unlink()
        except Exception as unlink_err:
            logger.error("rollback unlink failed: %s", unlink_err)
        raise
    return PipelineResult(fund_id=fid, processed=True, quarter=meta.quarter, persisted_path=path)
