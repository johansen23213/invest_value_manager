"""SEC EDGAR full-text search for special situation detection."""
from __future__ import annotations
import json
import re
from datetime import date, timedelta
from typing import Any
import httpx

EDGAR_SEARCH_URL = "https://efts.sec.gov/LATEST/search-index"
USER_AGENT = "ValueHunter/1.0 (joan.yanini@gmail.com)"

SITUATION_KEYWORDS = {
    "MERGER_ARB": ["definitive agreement", "merger agreement", "acquisition"],
    "LIQUIDATION": ["plan of dissolution", "liquidating distribution", "wind down"],
    "SPINOFF": ["spin-off", "distribution of shares", "separation"],
    "TENDER_OFFER": ["tender offer", "commencement of offer"],
    "RIGHTS_OFFERING": ["rights offering", "subscription rights"],
}


class EdgarSearchResult:
    def __init__(
        self,
        filing_type: str,
        company: str,
        cik: str,
        filed_date: str,
        title: str,
        url: str,
        situation_type: str = "OTHER",
    ):
        self.filing_type = filing_type
        self.company = company
        self.cik = cik
        self.filed_date = filed_date
        self.title = title
        self.url = url
        self.situation_type = situation_type

    def to_dict(self) -> dict:
        return {
            "filing_type": self.filing_type,
            "company": self.company,
            "cik": self.cik,
            "filed_date": self.filed_date,
            "title": self.title,
            "url": self.url,
            "situation_type": self.situation_type,
        }


class EdgarRSSWatcher:
    def __init__(self, client: httpx.Client | None = None):
        self._client = client or httpx.Client(
            timeout=30,
            headers={"User-Agent": USER_AGENT},
            follow_redirects=True,
        )

    def search(
        self,
        keywords: list[str] | None = None,
        forms: list[str] | None = None,
        days_back: int = 7,
    ) -> list[dict]:
        if keywords is None:
            keywords = ["merger", "acquisition", "liquidation", "spin-off", "tender offer"]
        if forms is None:
            forms = ["8-K", "SC 14D9", "S-1"]
        start_date = (date.today() - timedelta(days=days_back)).isoformat()
        end_date = date.today().isoformat()
        results = []
        for keyword in keywords:
            try:
                resp = self._client.get(
                    EDGAR_SEARCH_URL,
                    params={
                        "q": f'"{keyword}"',
                        "forms": ",".join(forms),
                        "dateRange": "custom",
                        "startdt": start_date,
                        "enddt": end_date,
                    },
                )
                if resp.status_code == 200:
                    hits = self._parse_response(resp.text, keyword)
                    results.extend(hits)
            except Exception:
                continue
        seen = set()
        deduped = []
        for r in results:
            key = (r["company"], r["filed_date"], r["filing_type"])
            if key not in seen:
                seen.add(key)
                deduped.append(r)
        return deduped

    def _parse_response(self, text: str, search_keyword: str) -> list[dict]:
        # EDGAR search returns JSON with "hits" array
        results = []
        try:
            data = json.loads(text)
            hits = data.get("hits", {}).get("hits", [])
            for hit in hits[:20]:
                source = hit.get("_source", {})
                sit_type = self._classify(
                    search_keyword,
                    source.get("display_names", [""])[0] if source.get("display_names") else "",
                )
                results.append(
                    {
                        "filing_type": source.get("form_type", ""),
                        "company": (
                            source.get("display_names", ["Unknown"])[0]
                            if source.get("display_names")
                            else "Unknown"
                        ),
                        "cik": source.get("entity_id", ""),
                        "filed_date": source.get("file_date", ""),
                        "title": (
                            source.get("display_names", [""])[0]
                            if source.get("display_names")
                            else ""
                        ),
                        "url": (
                            f"https://www.sec.gov/Archives/edgar/data/"
                            f"{source.get('entity_id', '')}/{source.get('file_num', '')}"
                            if source.get("entity_id")
                            else ""
                        ),
                        "situation_type": sit_type,
                    }
                )
        except (json.JSONDecodeError, KeyError):
            pass
        return results

    def _classify(self, keyword: str, title: str) -> str:
        combined = f"{keyword} {title}".lower()
        for sit_type, kws in SITUATION_KEYWORDS.items():
            if any(kw in combined for kw in kws):
                return sit_type
        return "OTHER"
