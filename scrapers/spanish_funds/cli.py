"""Manual CLI entry point: trigger scraping for one fund or all."""
from __future__ import annotations

import argparse
import os
import sys
import tempfile
from pathlib import Path

from scrapers.spanish_funds.azvalor import AzValorScraper
from scrapers.spanish_funds.base import ALLOWED_FUND_IDS
from scrapers.spanish_funds.cobas import CobasScraper
from scrapers.spanish_funds.horos import HorosScraper
from scrapers.spanish_funds.magallanes import MagallanesScraper
from scrapers.spanish_funds.pipeline import process_scraper
from scrapers.spanish_funds.valentum import ValentumScraper


SCRAPERS = {
    "cobas": CobasScraper,
    "azvalor": AzValorScraper,
    "magallanes": MagallanesScraper,
    "horos": HorosScraper,
    "valentum": ValentumScraper,
}


def _anthropic_client():
    import anthropic
    return anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Manual Spanish fund letter scraper")
    parser.add_argument("--fund", choices=sorted(ALLOWED_FUND_IDS), help="Single fund to process")
    parser.add_argument("--all", action="store_true", help="Process all funds")
    parser.add_argument("--dry-run", action="store_true", help="Use a temporary KB root (no permanent writes)")
    args = parser.parse_args(argv)

    if not args.fund and not args.all:
        parser.error("Specify --fund X or --all")

    funds = sorted(SCRAPERS) if args.all else [args.fund]
    client = _anthropic_client()
    kb_root: Path | None = None
    if args.dry_run:
        kb_root = Path(tempfile.mkdtemp(prefix="spanish_funds_dryrun_"))
        print(f"[dry-run] writing to {kb_root}")

    for fund in funds:
        scraper = SCRAPERS[fund]()
        result = process_scraper(scraper, client=client, kb_root=kb_root)
        print(
            f"{fund}: processed={result.processed} "
            f"quarter={result.quarter or '-'} "
            f"skipped_reason={result.skipped_reason or '-'} "
            f"error={result.error or '-'}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
