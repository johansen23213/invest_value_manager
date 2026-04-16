"""Alpha Vulture blog scraper — RSS parsing and situation classification.

Scrapes alphavulture.com for special-situation investment ideas including
merger arb, liquidations, spin-offs, net cash plays, and more.
"""

from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET
from datetime import date, datetime
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any

import httpx
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PATH = ROOT / "knowledge_base" / "universe" / "alpha_vulture_ideas.json"
RSS_URL = "https://alphavulture.com/feed/"

SITUATION_KEYWORDS: dict[str, list[str]] = {
    "MERGER_ARB": [
        "merger", "acquisition", "acquired", "tender offer",
        "definitive agreement", "deal price",
    ],
    "LIQUIDATION": [
        "liquidat", "wind down", "dissolv", "plan of dissolution",
    ],
    "SPINOFF": [
        "spin-off", "spinoff", "spin off", "spun off",
    ],
    "NET_CASH": [
        "net cash", "below cash", "cash shell", "cash per share", "trading below",
    ],
    "ODD_LOT": [
        "odd-lot", "odd lot",
    ],
    "CVR": [
        "contingent value right", "cvr",
    ],
    "TENDER_OFFER": [
        "tender offer", "self-tender", "modified dutch",
    ],
    "RIGHTS_OFFERING": [
        "rights offering", "rights issue",
    ],
    "STUB": [
        "stub value", "stub valuation", "sum-of-the-parts",
    ],
}


# ---------------------------------------------------------------------------
# Pure functions
# ---------------------------------------------------------------------------

def parse_rss_feed(xml_content: str) -> list[dict[str, Any]]:
    """Parse RSS XML and return a list of item dicts.

    Each dict has keys: title, url, pub_date, description.
    """
    root = ET.fromstring(xml_content)
    items: list[dict[str, Any]] = []
    for item_el in root.findall(".//item"):
        title = (item_el.findtext("title") or "").strip()
        url = (item_el.findtext("link") or "").strip()
        pub_date_raw = (item_el.findtext("pubDate") or "").strip()
        description = (item_el.findtext("description") or "").strip()

        # Parse RFC-2822 date to ISO date string
        pub_date: str | None = None
        if pub_date_raw:
            try:
                dt = parsedate_to_datetime(pub_date_raw)
                pub_date = dt.strftime("%Y-%m-%d")
            except (ValueError, TypeError):
                pub_date = pub_date_raw

        items.append({
            "title": title,
            "url": url,
            "pub_date": pub_date,
            "description": description,
        })
    return items


def _classify_situation(text: str) -> str:
    """Classify the special-situation type from free text using keyword matching.

    Returns the first matching situation type, or ``"OTHER"``.
    """
    text_lower = text.lower()
    for situation, keywords in SITUATION_KEYWORDS.items():
        for kw in keywords:
            if kw in text_lower:
                return situation
    return "OTHER"


def _extract_ticker(text: str) -> str | None:
    r"""Extract a stock ticker from text.

    Handles patterns like:
    - ``(ACME)``
    - ``(NYSE: ACME)``
    - ``ticker: ACME``
    """
    # Pattern 1: (NYSE: ACME) or (NASDAQ: ACME)
    m = re.search(r"\(\s*(?:NYSE|NASDAQ|AMEX|TSX|LSE)\s*:\s*([A-Z0-9.]+)\s*\)", text)
    if m:
        return m.group(1)

    # Pattern 2: ticker: ACME
    m = re.search(r"ticker:\s*([A-Z0-9.]+)", text, re.IGNORECASE)
    if m:
        return m.group(1).upper()

    # Pattern 3: (ACME) — all uppercase, 1-5 chars
    m = re.search(r"\(([A-Z]{1,5})\)", text)
    if m:
        return m.group(1)

    return None


def _extract_return(text: str) -> float | None:
    r"""Extract expected return percentage from text.

    Handles patterns like:
    - ``expected return: 5.9%``
    - ``spread of 5.9%``
    - ``spread approximately 5.9%``
    """
    patterns = [
        r"expected\s+return[:\s]+(\d+(?:\.\d+)?)\s*%",
        r"spread\s+(?:of\s+|approximately\s+|~\s*)?(\d+(?:\.\d+)?)\s*%",
    ]
    for pat in patterns:
        m = re.search(pat, text, re.IGNORECASE)
        if m:
            return float(m.group(1))
    return None


def parse_post_html(html: str, source_url: str) -> dict[str, Any]:
    """Parse a blog post HTML page and extract structured data.

    Returns a dict with: title, ticker, situation_type, thesis_summary,
    expected_return_pct, pub_date, source_url.
    """
    soup = BeautifulSoup(html, "html.parser")

    # Title
    title_el = soup.find(class_="entry-title")
    title = title_el.get_text(strip=True) if title_el else ""

    # Publication date
    time_el = soup.find("time")
    pub_date: str | None = None
    if time_el and time_el.get("datetime"):
        pub_date = str(time_el["datetime"])
    elif time_el:
        pub_date = time_el.get_text(strip=True)

    # Content text
    content_el = soup.find(class_="entry-content")
    content_text = content_el.get_text(" ", strip=True) if content_el else ""

    # Combine title + content for analysis
    full_text = f"{title} {content_text}"

    ticker = _extract_ticker(full_text)
    situation_type = _classify_situation(full_text)
    expected_return_pct = _extract_return(full_text)
    thesis_summary = content_text[:500] if content_text else None

    return {
        "title": title,
        "ticker": ticker,
        "situation_type": situation_type,
        "thesis_summary": thesis_summary,
        "expected_return_pct": expected_return_pct,
        "pub_date": pub_date,
        "source_url": source_url,
    }


def build_idea(rss_item: dict[str, Any], post_data: dict[str, Any]) -> dict[str, Any]:
    """Assemble a dict conforming to ``alpha_vulture_idea.schema.json``.

    Merges RSS metadata with parsed post data.
    """
    return {
        "post_date": post_data.get("pub_date") or rss_item.get("pub_date"),
        "title": post_data.get("title") or rss_item.get("title", ""),
        "ticker": post_data.get("ticker"),
        "company_name": None,
        "situation_type": post_data.get("situation_type", "OTHER"),
        "thesis_summary": post_data.get("thesis_summary"),
        "expected_return_pct": post_data.get("expected_return_pct"),
        "annualized_return_pct": None,
        "catalyst_date": None,
        "deal_price": None,
        "spread_pct": None,
        "risk_factors": [],
        "access": "FREE",
        "source": "ALPHA_VULTURE_BLOG",
        "source_url": post_data.get("source_url") or rss_item.get("url", ""),
        "scraped_date": date.today().isoformat(),
        "our_status": "NEW",
        "notes": None,
    }


# ---------------------------------------------------------------------------
# Scraper class (network-dependent)
# ---------------------------------------------------------------------------

class AlphaVultureScraper:
    """Scrapes Alpha Vulture blog for special-situation ideas."""

    def __init__(self, rss_url: str = RSS_URL, output_path: Path = OUTPUT_PATH):
        self.rss_url = rss_url
        self.output_path = output_path
        self._client = httpx.Client(
            timeout=30.0,
            headers={"User-Agent": "ValueHunter/1.0"},
        )

    def fetch_rss(self) -> list[dict[str, Any]]:
        """Fetch and parse the RSS feed."""
        resp = self._client.get(self.rss_url)
        resp.raise_for_status()
        return parse_rss_feed(resp.text)

    def fetch_post(self, url: str) -> dict[str, Any]:
        """Fetch and parse a single blog post."""
        resp = self._client.get(url)
        resp.raise_for_status()
        return parse_post_html(resp.text, source_url=url)

    def scrape(self, max_posts: int = 10) -> list[dict[str, Any]]:
        """Scrape the RSS feed and fetch up to *max_posts* post pages.

        Returns a list of idea dicts conforming to the schema.
        """
        rss_items = self.fetch_rss()
        ideas: list[dict[str, Any]] = []
        for item in rss_items[:max_posts]:
            post_data = self.fetch_post(item["url"])
            idea = build_idea(item, post_data)
            ideas.append(idea)
        return ideas

    def save(self, ideas: list[dict[str, Any]], path: Path | None = None) -> Path:
        """Save ideas list as JSON."""
        out = path or self.output_path
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(ideas, indent=2, ensure_ascii=False))
        return out
