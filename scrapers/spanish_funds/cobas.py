"""Cobas Asset Management letter scraper (URL detection only).

The letters page lists quarterly letters by filename pattern:
  Cobas_Seleccion_Carta_T{N}_{YEAR}.pdf
We parse the most recent (largest YEAR then largest N).
"""
from __future__ import annotations

import hashlib
import re

import httpx
from bs4 import BeautifulSoup

from scrapers.spanish_funds.base import FundScraper, LetterMeta

COBAS_LETTERS_URL = "https://www.cobasam.com/cartas-inversor/"
BASE_URL = "https://www.cobasam.com"
FILENAME_RE = re.compile(r"Cobas_Seleccion_Carta_T(\d)_(\d{4})\.pdf", re.IGNORECASE)


class CobasScraper(FundScraper):
    fund_id = "cobas"
    fund_name = "Cobas Selección"

    def get_latest_letter(self) -> LetterMeta | None:
        resp = httpx.get(COBAS_LETTERS_URL, follow_redirects=True, timeout=30)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        candidates: list[tuple[int, int, str]] = []  # (year, quarter, href)
        for a in soup.find_all("a", href=True):
            m = FILENAME_RE.search(a["href"])
            if m:
                q = int(m.group(1))
                y = int(m.group(2))
                candidates.append((y, q, a["href"]))
        if not candidates:
            return None

        candidates.sort(reverse=True)  # most recent first
        year, q, href = candidates[0]
        url = href if href.startswith("http") else f"{BASE_URL}{href}"
        content_hash = self._fetch_content_hash(url)
        return LetterMeta(url=url, quarter=f"{year}-Q{q}", content_hash=content_hash)

    def _fetch_content_hash(self, url: str) -> str:
        """HEAD request → prefer ETag; fall back to hashing the URL."""
        try:
            r = httpx.head(url, follow_redirects=True, timeout=30)
            etag = r.headers.get("etag", "").strip('"')
            if etag:
                return etag
        except Exception:
            pass
        return hashlib.sha256(url.encode()).hexdigest()[:16]
