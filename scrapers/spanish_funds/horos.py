"""Horos Asset Management letter scraper (unified package — URL detection only).

The actual text extraction is now handled by the shared LLM extractor. The
legacy regex-based scraper at scrapers/horos_scraper.py is deprecated but
kept in place for the backfill script.
"""
from __future__ import annotations

import re

import httpx
from bs4 import BeautifulSoup

from scrapers.spanish_funds.base import FundScraper, LetterMeta

HOROS_LETTERS_URL = "https://horosam.com/articulos/cartas-al-inversor/"
FILENAME_RE = re.compile(r"carta[^/]*?[\-_](\d{4})[\-_]q(\d)", re.IGNORECASE)


class HorosScraper(FundScraper):
    fund_id = "horos"
    fund_name = "Horos Value Internacional"

    def get_latest_letter(self) -> LetterMeta | None:
        resp = httpx.get(HOROS_LETTERS_URL, follow_redirects=True, timeout=30)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        candidates: list[tuple[int, int, str]] = []
        for a in soup.find_all("a", href=True):
            m = FILENAME_RE.search(a["href"])
            if m:
                y = int(m.group(1))
                q = int(m.group(2))
                candidates.append((y, q, a["href"]))
        if not candidates:
            return None

        candidates.sort(reverse=True)
        year, q, href = candidates[0]
        content_hash = self._fetch_content_hash(href)
        return LetterMeta(url=href, quarter=f"{year}-Q{q}", content_hash=content_hash)
