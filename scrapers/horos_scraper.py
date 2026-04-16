"""Horos Asset Management quarterly letter scraper.

Extracts portfolio positions from Horos Value Internacional quarterly
letters (PDF), including company names, tickers, weights, upside estimates,
and position actions (NEW / MAINTAINED / EXITED).
"""

from __future__ import annotations

import json
import re
from datetime import date
from pathlib import Path
from typing import Any

import httpx
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_PATH = ROOT / "knowledge_base" / "universe" / "horos_positions.json"
LETTERS_URL = "https://horosam.com/articulos/cartas-al-inversor/"

# ---------------------------------------------------------------------------
# Regex patterns
# ---------------------------------------------------------------------------

TICKER_RE = re.compile(r"\(([A-Z0-9]+(?:\.[A-Z]{1,4})?)\)")
WEIGHT_RE = re.compile(r"[Pp]eso:?\s*([\d.]+)%")
UPSIDE_RE = re.compile(r"(?:potencial|upside|revalorización)[^.]*?([\d]+)%", re.IGNORECASE)

# Quarter detection patterns
QUARTER_PATTERNS: list[tuple[re.Pattern, Any]] = [
    # Q4 2025
    (re.compile(r"Q([1-4])\s+(\d{4})"), None),
    # cuarto trimestre de 2025, primer trimestre de 2026, etc.
    (re.compile(
        r"(primer|segundo|tercer|cuarto)\s+trimestre\s+de\s+(\d{4})",
        re.IGNORECASE,
    ), {
        "primer": "1", "segundo": "2", "tercer": "3", "cuarto": "4",
    }),
    # 4T 2025, 1T 2026
    (re.compile(r"([1-4])T\s+(\d{4})"), None),
]

FUND_RETURN_RE = re.compile(
    r"rentabilidad\s+del\s+([+-]?\d+(?:\.\d+)?)\s*%",
    re.IGNORECASE,
)

# Section header patterns for action detection
NEW_SECTION_RE = re.compile(r"NUEVA\s+POSICI[OÓ]N", re.IGNORECASE)
EXITED_SECTION_RE = re.compile(r"POSICI[OÓ]N\s+VENDIDA", re.IGNORECASE)
MAIN_SECTION_RE = re.compile(r"PRINCIPALES\s+POSICIONES", re.IGNORECASE)


# ---------------------------------------------------------------------------
# Pure functions
# ---------------------------------------------------------------------------

def _detect_quarter(text: str) -> str | None:
    """Extract the quarter identifier from letter text.

    Returns a string like ``"2025-Q4"`` or ``None``.
    """
    for pattern, mapping in QUARTER_PATTERNS:
        m = pattern.search(text)
        if m:
            if mapping is not None:
                # Spanish word → quarter number
                q_num = mapping.get(m.group(1).lower())
                year = m.group(2)
            else:
                q_num = m.group(1)
                year = m.group(2)
            if q_num and year:
                return f"{year}-Q{q_num}"
    return None


def _detect_fund_return(text: str) -> float | None:
    """Extract fund return percentage from text."""
    m = FUND_RETURN_RE.search(text)
    if m:
        return float(m.group(1))
    return None


def parse_letter_text(text: str, source_url: str) -> dict[str, Any]:
    """Parse top-level letter metadata: quarter and fund return.

    Returns a dict with keys: quarter, fund_return_pct, source_url.
    """
    quarter = _detect_quarter(text)
    fund_return_pct = _detect_fund_return(text)
    return {
        "quarter": quarter,
        "fund_return_pct": fund_return_pct,
        "source_url": source_url,
    }


def _determine_action(line_idx: int, section_boundaries: list[tuple[int, str]]) -> str | None:
    """Determine the action for a position based on which section it falls in."""
    current_section = "MAINTAINED"
    for boundary_idx, section_type in section_boundaries:
        if line_idx >= boundary_idx:
            current_section = section_type
        else:
            break
    return current_section


def extract_positions(
    text: str,
    quarter: str | None,
    source_url: str,
) -> list[dict[str, Any]]:
    """Extract portfolio positions from letter text.

    Scans line by line for tickers in parentheses and extracts surrounding
    context for company name, weight, upside, and action.
    """
    lines = text.split("\n")

    # Build section boundaries
    section_boundaries: list[tuple[int, str]] = []
    for i, line in enumerate(lines):
        if MAIN_SECTION_RE.search(line):
            section_boundaries.append((i, "MAINTAINED"))
        elif NEW_SECTION_RE.search(line):
            section_boundaries.append((i, "NEW"))
        elif EXITED_SECTION_RE.search(line):
            section_boundaries.append((i, "EXITED"))

    positions: list[dict[str, Any]] = []
    today = date.today().isoformat()

    for i, line in enumerate(lines):
        ticker_match = TICKER_RE.search(line)
        if not ticker_match:
            continue

        ticker = ticker_match.group(1)

        # Company name: text before the ticker in parens
        company = line[:ticker_match.start()].strip().rstrip("(").strip()
        # Clean trailing dash/em-dash
        company = re.sub(r"\s*[—–-]\s*$", "", company).strip()

        if not company:
            continue

        # Look ahead a few lines for weight, upside, thesis
        context_lines = lines[i : i + 4]
        context_text = " ".join(context_lines)

        # Weight
        weight_match = WEIGHT_RE.search(context_text)
        weight_pct = float(weight_match.group(1)) if weight_match else None

        # Upside
        upside_match = UPSIDE_RE.search(context_text)
        upside_pct = float(upside_match.group(1)) if upside_match else None

        # Thesis summary: the context lines minus the header line
        thesis_parts = [l.strip() for l in context_lines[1:] if l.strip()]
        thesis_summary = " ".join(thesis_parts)[:500] if thesis_parts else None

        # Action based on section
        action = _determine_action(i, section_boundaries)

        position: dict[str, Any] = {
            "letter_quarter": quarter,
            "letter_date": None,
            "fund": "HOROS_VALUE_INTERNACIONAL",
            "company": company,
            "ticker": ticker,
            "ticker_confidence": "EXACT",
            "thesis_summary": thesis_summary,
            "upside_pct": upside_pct,
            "weight_pct": weight_pct,
            "action": action,
            "sector": None,
            "geo": None,
            "market_cap_bucket": None,
            "source_url": source_url,
            "scraped_date": today,
        }
        positions.append(position)

    return positions


def extract_text_from_pdf(pdf_path: str | Path) -> str:
    """Extract text from a PDF file using pypdf."""
    from pypdf import PdfReader

    reader = PdfReader(str(pdf_path))
    pages_text: list[str] = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages_text.append(text)
    return "\n".join(pages_text)


# ---------------------------------------------------------------------------
# Scraper class (network-dependent)
# ---------------------------------------------------------------------------

class HorosScraper:
    """Scrapes Horos quarterly letters for position data."""

    def __init__(
        self,
        letters_url: str = LETTERS_URL,
        output_path: Path = OUTPUT_PATH,
    ):
        self.letters_url = letters_url
        self.output_path = output_path
        self._client = httpx.Client(
            timeout=30.0,
            headers={"User-Agent": "ValueHunter/1.0"},
        )

    def find_letter_urls(self) -> list[str]:
        """Scrape the Horos letters page for PDF links."""
        resp = self._client.get(self.letters_url)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        urls: list[str] = []
        for a_tag in soup.find_all("a", href=True):
            href = str(a_tag["href"])
            if href.lower().endswith(".pdf"):
                urls.append(href)
        return urls

    def download_pdf(self, url: str, dest_dir: Path | None = None) -> Path:
        """Download a PDF to a local path."""
        dest = (dest_dir or Path("/tmp")) / url.rsplit("/", 1)[-1]
        resp = self._client.get(url)
        resp.raise_for_status()
        dest.write_bytes(resp.content)
        return dest

    def scrape_letter(self, pdf_path: str | Path, source_url: str) -> list[dict[str, Any]]:
        """Extract positions from a single PDF letter."""
        text = extract_text_from_pdf(pdf_path)
        meta = parse_letter_text(text, source_url)
        quarter = meta.get("quarter")
        return extract_positions(text, quarter, source_url)

    def scrape_all(self) -> list[dict[str, Any]]:
        """Download and scrape all available quarterly letters."""
        urls = self.find_letter_urls()
        all_positions: list[dict[str, Any]] = []
        for url in urls:
            pdf_path = self.download_pdf(url)
            positions = self.scrape_letter(pdf_path, source_url=url)
            all_positions.extend(positions)
        return all_positions

    def save(
        self,
        positions: list[dict[str, Any]],
        path: Path | None = None,
    ) -> Path:
        """Save positions list as JSON."""
        out = path or self.output_path
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(positions, indent=2, ensure_ascii=False))
        return out
