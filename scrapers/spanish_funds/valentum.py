"""Valentum letter scraper (URL detection only)."""
from __future__ import annotations

import re

import httpx
from bs4 import BeautifulSoup

from scrapers.spanish_funds.base import FundScraper, LetterMeta

VALENTUM_LETTERS_URL = "https://valentum.es/informacion-inversores/"
FILENAME_RE = re.compile(r"Carta[\-_](\d)T[\-_](\d{4})\.pdf", re.IGNORECASE)


class ValentumScraper(FundScraper):
    fund_id = "valentum"
    fund_name = "Valentum Magno"

    def get_latest_letter(self) -> LetterMeta | None:
        resp = httpx.get(VALENTUM_LETTERS_URL, follow_redirects=True, timeout=30)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        candidates: list[tuple[int, int, str]] = []
        for a in soup.find_all("a", href=True):
            m = FILENAME_RE.search(a["href"])
            if m:
                q = int(m.group(1))
                y = int(m.group(2))
                candidates.append((y, q, a["href"]))
        if not candidates:
            return None

        candidates.sort(reverse=True)
        year, q, href = candidates[0]
        content_hash = self._fetch_content_hash(href)
        return LetterMeta(url=href, quarter=f"{year}-Q{q}", content_hash=content_hash)
