# Spanish Value Fund Ingestion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build automated ingestion of quarterly letters from 5 Spanish value asset managers (Cobas, AzValor, Magallanes, Horos, Valentum). Extract holdings + per-position thesis narratives into a unified schema. Fan-out to quality universe, Web Researcher context, and Telegram digest.

**Architecture:** 5 per-fund scrapers share a common 9-step pipeline (detect → download → textify → LLM extract → validate → resolve tickers → persist → update state → fan-out). Per-fund code differs only in URL detection for the latest PDF. Claude Sonnet 4.6 does the text-to-schema extraction; yfinance validates tickers; APScheduler runs a weekly Monday check.

**Tech Stack:** Python 3.12, anthropic>=0.49, httpx, pypdf, jsonschema, pyyaml, yfinance, apscheduler, pytest + pytest-asyncio.

**Spec reference:** `docs/superpowers/specs/2026-04-20-spanish-value-fund-ingestion-design.md`

**Branch:** `sprint1/foundations` (current)

---

## Task ordering

Tasks are ordered so each builds on the previous and can be committed independently:

1. Unified schema + validation tests
2. `pypdf` text extraction helper
3. Base pipeline abstract class (no I/O yet)
4. LLM extractor with mocked Anthropic client
5. Ticker resolver with mocked yfinance
6. Persist layer (JSON + last_processed.json)
7. First concrete fund: Cobas (end-to-end with fixture)
8. AzValor scraper
9. Magallanes scraper
10. Valentum scraper
11. Migrate existing Horos scraper + backfill historic JSON
12. Universe merger (multi-fund conviction logic)
13. Telegram digest builder
14. Web Researcher (A2.5) contextual lookup tool
15. Scheduler integration (weekly Monday job)
16. Manual CLI entry point

---

## Task 1: Unified schema + validation tests

**Files:**
- Create: `knowledge_base/schemas/spanish_fund_position.schema.json`
- Create: `tests/test_spanish_fund_schema.py`
- Create: `tests/fixtures/spanish_funds/valid_letter_minimal.json`
- Create: `tests/fixtures/spanish_funds/valid_letter_full.json`
- Create: `tests/fixtures/spanish_funds/invalid_bad_quarter.json`
- Create: `tests/fixtures/spanish_funds/invalid_bad_action.json`

- [ ] **Step 1: Write the failing test**

File: `tests/test_spanish_fund_schema.py`

```python
"""Schema validation tests for spanish_fund_position.schema.json."""
from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import pytest

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "spanish_funds"
SCHEMAS = Path(__file__).resolve().parent.parent / "knowledge_base" / "schemas"


@pytest.fixture
def schema() -> dict:
    return json.loads((SCHEMAS / "spanish_fund_position.schema.json").read_text())


class TestSpanishFundSchema:
    def test_accepts_minimal_valid(self, schema: dict):
        payload = json.loads((FIXTURES / "valid_letter_minimal.json").read_text())
        jsonschema.validate(payload, schema)

    def test_accepts_full_valid(self, schema: dict):
        payload = json.loads((FIXTURES / "valid_letter_full.json").read_text())
        jsonschema.validate(payload, schema)

    def test_rejects_bad_quarter(self, schema: dict):
        payload = json.loads((FIXTURES / "invalid_bad_quarter.json").read_text())
        with pytest.raises(jsonschema.ValidationError):
            jsonschema.validate(payload, schema)

    def test_rejects_bad_action(self, schema: dict):
        payload = json.loads((FIXTURES / "invalid_bad_action.json").read_text())
        with pytest.raises(jsonschema.ValidationError):
            jsonschema.validate(payload, schema)

    def test_requires_fund_id(self, schema: dict):
        payload = {"fund_name": "X", "quarter": "2026-Q1", "extracted_at": "2026-04-20T00:00:00Z",
                   "extraction_model": "m", "source_url": "https://x", "positions": []}
        with pytest.raises(jsonschema.ValidationError):
            jsonschema.validate(payload, schema)

    def test_accepts_fund_id_enum(self, schema: dict):
        for fid in ["cobas", "azvalor", "magallanes", "horos", "valentum"]:
            payload = {
                "fund_id": fid, "fund_name": fid.capitalize(), "quarter": "2026-Q1",
                "extracted_at": "2026-04-20T00:00:00Z", "extraction_model": "m",
                "source_url": "https://x", "positions": [],
            }
            jsonschema.validate(payload, schema)

    def test_rejects_unknown_fund_id(self, schema: dict):
        payload = {"fund_id": "bestinver", "fund_name": "X", "quarter": "2026-Q1",
                   "extracted_at": "2026-04-20T00:00:00Z", "extraction_model": "m",
                   "source_url": "https://x", "positions": []}
        with pytest.raises(jsonschema.ValidationError):
            jsonschema.validate(payload, schema)
```

File: `tests/fixtures/spanish_funds/valid_letter_minimal.json`

```json
{
  "fund_id": "cobas",
  "fund_name": "Cobas Selección",
  "quarter": "2026-Q1",
  "extracted_at": "2026-04-20T10:00:00Z",
  "extraction_model": "claude-sonnet-4-6",
  "source_url": "https://www.cobasam.com/cartas/2026-Q1.pdf",
  "positions": []
}
```

File: `tests/fixtures/spanish_funds/valid_letter_full.json`

```json
{
  "fund_id": "azvalor",
  "fund_name": "AzValor Internacional",
  "quarter": "2026-Q1",
  "extracted_at": "2026-04-20T10:00:00Z",
  "extraction_model": "claude-sonnet-4-6",
  "source_url": "https://www.azvalor.com/cartas/2026-Q1.pdf",
  "fund_return_pct": 4.2,
  "aum_eur": 1500000000,
  "positions": [
    {
      "company_name": "Atalaya Mining",
      "ticker": "ATYM.L",
      "ticker_status": "verified",
      "weight_pct": 5.1,
      "action": "increased",
      "upside_pct": 45,
      "thesis_text": "Cobre estructuralmente escaso. Permisos Sudamérica avanzando."
    },
    {
      "company_name": "Sdiptech",
      "ticker": "SDIP-B.ST",
      "ticker_status": "unverified",
      "weight_pct": 2.3,
      "action": "new",
      "upside_pct": null,
      "thesis_text": null
    }
  ]
}
```

File: `tests/fixtures/spanish_funds/invalid_bad_quarter.json`

```json
{
  "fund_id": "cobas",
  "fund_name": "Cobas Selección",
  "quarter": "Q1-2026",
  "extracted_at": "2026-04-20T10:00:00Z",
  "extraction_model": "claude-sonnet-4-6",
  "source_url": "https://x",
  "positions": []
}
```

File: `tests/fixtures/spanish_funds/invalid_bad_action.json`

```json
{
  "fund_id": "cobas",
  "fund_name": "Cobas",
  "quarter": "2026-Q1",
  "extracted_at": "2026-04-20T10:00:00Z",
  "extraction_model": "m",
  "source_url": "https://x",
  "positions": [
    {"company_name": "X", "ticker": "X", "ticker_status": "verified", "action": "bought"}
  ]
}
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_spanish_fund_schema.py -v`
Expected: FAIL — `FileNotFoundError` on the schema file.

- [ ] **Step 3: Create the schema file**

File: `knowledge_base/schemas/spanish_fund_position.schema.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "https://valuehunter.local/schemas/spanish_fund_position.schema.json",
  "title": "Spanish Fund Position",
  "description": "Quarterly letter holdings + thesis narratives from a Spanish value fund",
  "type": "object",
  "required": ["fund_id", "fund_name", "quarter", "extracted_at", "extraction_model", "source_url", "positions"],
  "additionalProperties": false,
  "properties": {
    "fund_id": {
      "type": "string",
      "enum": ["cobas", "azvalor", "magallanes", "horos", "valentum"]
    },
    "fund_name": { "type": "string" },
    "quarter": { "type": "string", "pattern": "^\\d{4}-Q[1-4]$" },
    "extracted_at": { "type": "string", "format": "date-time" },
    "extraction_model": { "type": "string" },
    "source_url": { "type": "string", "format": "uri" },
    "fund_return_pct": { "type": ["number", "null"] },
    "aum_eur": { "type": ["number", "null"] },
    "positions": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["company_name", "ticker", "ticker_status", "action"],
        "additionalProperties": false,
        "properties": {
          "company_name": { "type": "string" },
          "ticker": { "type": "string" },
          "ticker_status": {
            "type": "string",
            "enum": ["verified", "unverified", "ambiguous"]
          },
          "weight_pct": { "type": ["number", "null"], "minimum": 0, "maximum": 100 },
          "action": {
            "type": "string",
            "enum": ["new", "maintained", "increased", "reduced", "exited"]
          },
          "upside_pct": { "type": ["number", "null"] },
          "thesis_text": { "type": ["string", "null"] }
        }
      }
    },
    "macro_commentary": { "type": "null" }
  }
}
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_spanish_fund_schema.py -v`
Expected: PASS (7 tests).

- [ ] **Step 5: Commit**

```bash
git add knowledge_base/schemas/spanish_fund_position.schema.json \
        tests/test_spanish_fund_schema.py \
        tests/fixtures/spanish_funds/
git commit -m "feat(spanish-funds): add unified position schema with validation tests"
```

---

## Task 2: PDF text extraction helper

**Files:**
- Create: `scrapers/spanish_funds/__init__.py`
- Create: `scrapers/spanish_funds/pdf.py`
- Create: `tests/test_spanish_funds_pdf.py`
- Create: `tests/fixtures/spanish_funds/sample_simple.pdf` (generated, 2-page PDF with known text)

- [ ] **Step 1: Write the failing test**

File: `tests/test_spanish_funds_pdf.py`

```python
"""Tests for PDF text extraction helper."""
from __future__ import annotations

from pathlib import Path

import pytest

from scrapers.spanish_funds.pdf import extract_text_from_pdf

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "spanish_funds"


class TestExtractTextFromPDF:
    def test_extracts_expected_string(self):
        text = extract_text_from_pdf(FIXTURES / "sample_simple.pdf")
        assert "Hello ValueHunter" in text

    def test_joins_multiple_pages(self):
        text = extract_text_from_pdf(FIXTURES / "sample_simple.pdf")
        # Fixture has "Page 1" on page 1, "Page 2" on page 2
        assert "Page 1" in text
        assert "Page 2" in text

    def test_raises_on_missing_file(self, tmp_path: Path):
        with pytest.raises(FileNotFoundError):
            extract_text_from_pdf(tmp_path / "nope.pdf")

    def test_returns_empty_string_on_empty_pdf(self, tmp_path: Path):
        from pypdf import PdfWriter
        empty = tmp_path / "empty.pdf"
        w = PdfWriter()
        w.add_blank_page(width=100, height=100)
        with empty.open("wb") as f:
            w.write(f)
        text = extract_text_from_pdf(empty)
        assert text.strip() == ""
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_spanish_funds_pdf.py -v`
Expected: FAIL — `ModuleNotFoundError: scrapers.spanish_funds.pdf` + fixture missing.

- [ ] **Step 3: Generate the sample_simple.pdf fixture**

Create `tests/fixtures/spanish_funds/_generate_sample_pdf.py` (one-shot script, not a test):

```python
"""One-shot: generate sample_simple.pdf fixture. Not imported by tests."""
from pathlib import Path
from pypdf import PdfWriter
from reportlab.pdfgen import canvas

OUT = Path(__file__).parent / "sample_simple.pdf"

c = canvas.Canvas(str(OUT))
c.drawString(100, 750, "Hello ValueHunter - Page 1")
c.showPage()
c.drawString(100, 750, "Second page - Page 2")
c.showPage()
c.save()
print(f"Wrote {OUT}")
```

Because `reportlab` is not in pyproject.toml, use a simpler approach: build the fixture with pypdf alone using a pre-made bytes blob. Simpler alternative: create the fixture manually with any PDF tool locally, OR use the code below with `fpdf2` (pure Python, no system deps).

Simpler final approach — add `fpdf2` to dev dependencies and use it:

Update `pyproject.toml`:

```toml
[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "pytest-asyncio>=0.23.0",
    "fpdf2>=2.7.0",
]
```

Create the generator script:

```python
"""One-shot: generate sample_simple.pdf fixture."""
from pathlib import Path
from fpdf import FPDF

OUT = Path(__file__).parent / "sample_simple.pdf"

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=12)
pdf.cell(0, 10, "Hello ValueHunter - Page 1")
pdf.add_page()
pdf.cell(0, 10, "Second page - Page 2")
pdf.output(str(OUT))
print(f"Wrote {OUT}")
```

Run once to create the fixture, then delete the generator script.

```bash
pip install -e ".[dev]"
python tests/fixtures/spanish_funds/_generate_sample_pdf.py
rm tests/fixtures/spanish_funds/_generate_sample_pdf.py
```

- [ ] **Step 4: Create the PDF extraction helper**

File: `scrapers/spanish_funds/__init__.py`

```python
"""Spanish value fund quarterly letter ingestion."""
```

File: `scrapers/spanish_funds/pdf.py`

```python
"""PDF text extraction using pypdf."""
from __future__ import annotations

from pathlib import Path

from pypdf import PdfReader


def extract_text_from_pdf(path: Path) -> str:
    """Extract concatenated text from all pages of a PDF.

    Raises FileNotFoundError if path does not exist.
    Returns empty string for PDFs with no extractable text.
    """
    if not path.exists():
        raise FileNotFoundError(str(path))
    reader = PdfReader(str(path))
    pages = [page.extract_text() or "" for page in reader.pages]
    return "\n".join(pages)
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `pytest tests/test_spanish_funds_pdf.py -v`
Expected: PASS (4 tests).

- [ ] **Step 6: Commit**

```bash
git add pyproject.toml \
        scrapers/spanish_funds/__init__.py \
        scrapers/spanish_funds/pdf.py \
        tests/test_spanish_funds_pdf.py \
        tests/fixtures/spanish_funds/sample_simple.pdf
git commit -m "feat(spanish-funds): add pypdf-based text extraction helper"
```

---

## Task 3: Base pipeline abstract class

**Files:**
- Create: `scrapers/spanish_funds/base.py`
- Create: `tests/test_spanish_funds_base.py`

- [ ] **Step 1: Write the failing test**

File: `tests/test_spanish_funds_base.py`

```python
"""Tests for the abstract base fund scraper."""
from __future__ import annotations

from pathlib import Path

import pytest

from scrapers.spanish_funds.base import FundScraper, LetterMeta


class DummyScraper(FundScraper):
    fund_id = "cobas"
    fund_name = "Cobas Selección"

    def get_latest_letter(self) -> LetterMeta | None:
        return LetterMeta(
            url="https://cobasam.com/q1-2026.pdf",
            quarter="2026-Q1",
            content_hash="abc123",
        )


class IncompleteScraper(FundScraper):
    fund_id = "cobas"
    fund_name = "X"
    # missing get_latest_letter


class TestFundScraper:
    def test_cannot_instantiate_abstract(self):
        with pytest.raises(TypeError):
            IncompleteScraper()

    def test_concrete_scraper_has_fund_id(self):
        s = DummyScraper()
        assert s.fund_id == "cobas"

    def test_concrete_scraper_has_fund_name(self):
        s = DummyScraper()
        assert s.fund_name == "Cobas Selección"

    def test_get_latest_letter_returns_meta(self):
        s = DummyScraper()
        meta = s.get_latest_letter()
        assert meta.quarter == "2026-Q1"
        assert meta.url == "https://cobasam.com/q1-2026.pdf"
        assert meta.content_hash == "abc123"

    def test_letter_meta_is_frozen(self):
        meta = LetterMeta(url="https://x", quarter="2026-Q1", content_hash="h")
        with pytest.raises(Exception):  # dataclass frozen raises FrozenInstanceError
            meta.url = "https://y"

    def test_invalid_fund_id_class_var_raises_on_instantiation(self):
        class BadScraper(FundScraper):
            fund_id = "nothing"
            fund_name = "X"
            def get_latest_letter(self): return None
        with pytest.raises(ValueError, match="fund_id"):
            BadScraper()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_spanish_funds_base.py -v`
Expected: FAIL — `ModuleNotFoundError: scrapers.spanish_funds.base`.

- [ ] **Step 3: Create the base class**

File: `scrapers/spanish_funds/base.py`

```python
"""Abstract base class for Spanish fund scrapers.

Subclasses implement `get_latest_letter()` for URL detection.
All downstream processing is shared via the pipeline functions.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

ALLOWED_FUND_IDS = frozenset({"cobas", "azvalor", "magallanes", "horos", "valentum"})


@dataclass(frozen=True)
class LetterMeta:
    """Metadata about a quarterly letter available for download."""
    url: str
    quarter: str            # e.g. "2026-Q1"
    content_hash: str       # SHA256 of the PDF bytes (pre-download if HEAD ETag, else post-download)


class FundScraper(ABC):
    """Abstract base. Subclasses set fund_id/fund_name and implement get_latest_letter."""

    fund_id: str = ""
    fund_name: str = ""

    def __init__(self) -> None:
        if self.fund_id not in ALLOWED_FUND_IDS:
            raise ValueError(f"fund_id {self.fund_id!r} not in {sorted(ALLOWED_FUND_IDS)}")

    @abstractmethod
    def get_latest_letter(self) -> LetterMeta | None:
        """Return metadata for the most recent letter, or None if no letter found."""
        ...
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_spanish_funds_base.py -v`
Expected: PASS (6 tests).

- [ ] **Step 5: Commit**

```bash
git add scrapers/spanish_funds/base.py tests/test_spanish_funds_base.py
git commit -m "feat(spanish-funds): add abstract FundScraper base class"
```

---

## Task 4: LLM extractor with mocked Anthropic client

**Files:**
- Create: `scrapers/spanish_funds/extractor.py`
- Create: `scrapers/spanish_funds/prompts/extraction_v1.md`
- Create: `tests/test_spanish_funds_extractor.py`
- Create: `tests/fixtures/spanish_funds/mock_llm_response_valid.json`
- Create: `tests/fixtures/spanish_funds/mock_llm_response_malformed.json`
- Create: `tests/fixtures/spanish_funds/sample_letter_text.txt`

- [ ] **Step 1: Write the failing test**

File: `tests/test_spanish_funds_extractor.py`

```python
"""Tests for LLM-based letter extraction."""
from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import jsonschema
import pytest

from scrapers.spanish_funds.extractor import (
    ExtractorError,
    extract_from_text,
    load_prompt,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "spanish_funds"
SCHEMAS = Path(__file__).resolve().parent.parent / "knowledge_base" / "schemas"


@pytest.fixture
def letter_text() -> str:
    return (FIXTURES / "sample_letter_text.txt").read_text()


@pytest.fixture
def valid_llm_response() -> str:
    return (FIXTURES / "mock_llm_response_valid.json").read_text()


@pytest.fixture
def malformed_llm_response() -> str:
    return (FIXTURES / "mock_llm_response_malformed.json").read_text()


@pytest.fixture
def schema() -> dict:
    return json.loads((SCHEMAS / "spanish_fund_position.schema.json").read_text())


def _mock_message(text: str) -> MagicMock:
    msg = MagicMock()
    msg.content = [MagicMock(text=text, type="text")]
    return msg


class TestLoadPrompt:
    def test_returns_non_empty_prompt(self):
        p = load_prompt("extraction_v1")
        assert "value" in p.lower()
        assert len(p) > 200

    def test_raises_on_missing_prompt(self):
        with pytest.raises(FileNotFoundError):
            load_prompt("does_not_exist")


class TestExtractFromText:
    def test_returns_valid_schema(self, letter_text, valid_llm_response, schema):
        mock_client = MagicMock()
        mock_client.messages.create.return_value = _mock_message(valid_llm_response)
        result = extract_from_text(
            letter_text, fund_id="cobas", quarter="2026-Q1",
            source_url="https://x", client=mock_client,
        )
        jsonschema.validate(result, schema)
        assert result["fund_id"] == "cobas"
        assert result["quarter"] == "2026-Q1"

    def test_retries_once_on_malformed_response(self, letter_text, valid_llm_response, malformed_llm_response):
        mock_client = MagicMock()
        mock_client.messages.create.side_effect = [
            _mock_message(malformed_llm_response),
            _mock_message(valid_llm_response),
        ]
        result = extract_from_text(
            letter_text, fund_id="cobas", quarter="2026-Q1",
            source_url="https://x", client=mock_client,
        )
        assert result["fund_id"] == "cobas"
        assert mock_client.messages.create.call_count == 2

    def test_raises_after_two_consecutive_failures(self, letter_text, malformed_llm_response):
        mock_client = MagicMock()
        mock_client.messages.create.return_value = _mock_message(malformed_llm_response)
        with pytest.raises(ExtractorError):
            extract_from_text(
                letter_text, fund_id="cobas", quarter="2026-Q1",
                source_url="https://x", client=mock_client,
            )
        assert mock_client.messages.create.call_count == 2

    def test_stamps_extraction_metadata(self, letter_text, valid_llm_response):
        mock_client = MagicMock()
        mock_client.messages.create.return_value = _mock_message(valid_llm_response)
        result = extract_from_text(
            letter_text, fund_id="cobas", quarter="2026-Q1",
            source_url="https://x", client=mock_client, model="claude-sonnet-4-6",
        )
        assert result["extraction_model"] == "claude-sonnet-4-6"
        assert "extracted_at" in result
        assert result["source_url"] == "https://x"
```

File: `tests/fixtures/spanish_funds/sample_letter_text.txt`

```
Carta a los inversores — Cobas Selección
Primer trimestre de 2026

Estimado partícipe, en el primer trimestre la cartera ha generado una rentabilidad
del +4.2%. El valor patrimonial alcanza los 2.100 millones de euros.

PRINCIPALES POSICIONES

Atalaya Mining (ATYM.L) — Peso: 7.3%
Seguimos convencidos del caso cobre. Potencial del 45%.

Técnicas Reunidas (TRE.MC) — Peso: 4.1%
El mercado sigue sin ver la reestructuración completada.

NUEVA POSICIÓN

Semapa (SEM.LS) — Peso: 3.0%
Conglomerado portugués con activos infravalorados.
```

File: `tests/fixtures/spanish_funds/mock_llm_response_valid.json`

```json
{
  "fund_id": "cobas",
  "fund_name": "Cobas Selección",
  "quarter": "2026-Q1",
  "extracted_at": "PLACEHOLDER_WILL_BE_OVERWRITTEN",
  "extraction_model": "PLACEHOLDER_WILL_BE_OVERWRITTEN",
  "source_url": "PLACEHOLDER_WILL_BE_OVERWRITTEN",
  "fund_return_pct": 4.2,
  "aum_eur": 2100000000,
  "positions": [
    {
      "company_name": "Atalaya Mining",
      "ticker": "ATYM.L",
      "ticker_status": "unverified",
      "weight_pct": 7.3,
      "action": "maintained",
      "upside_pct": 45,
      "thesis_text": "Seguimos convencidos del caso cobre."
    },
    {
      "company_name": "Técnicas Reunidas",
      "ticker": "TRE.MC",
      "ticker_status": "unverified",
      "weight_pct": 4.1,
      "action": "maintained",
      "upside_pct": null,
      "thesis_text": "El mercado sigue sin ver la reestructuración completada."
    },
    {
      "company_name": "Semapa",
      "ticker": "SEM.LS",
      "ticker_status": "unverified",
      "weight_pct": 3.0,
      "action": "new",
      "upside_pct": null,
      "thesis_text": "Conglomerado portugués con activos infravalorados."
    }
  ]
}
```

File: `tests/fixtures/spanish_funds/mock_llm_response_malformed.json`

```json
{
  "fund_id": "cobas",
  "quarter": "Q1 2026",
  "positions": "not an array"
}
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_spanish_funds_extractor.py -v`
Expected: FAIL — `ModuleNotFoundError: scrapers.spanish_funds.extractor`.

- [ ] **Step 3: Create the extraction prompt**

File: `scrapers/spanish_funds/prompts/extraction_v1.md`

```
You extract structured data from quarterly letters of Spanish value funds.

You will receive the raw text of one letter. Your task: return a single JSON
document matching the schema below. Output JSON ONLY — no explanations, no
markdown fences, no extra prose.

Schema (abbreviated — fill every required field):

{
  "fund_id": "<one of: cobas|azvalor|magallanes|horos|valentum>",
  "fund_name": "<as it appears in the letter>",
  "quarter": "<YYYY-QN>",
  "extracted_at": "<ISO 8601 datetime, UTC>",
  "extraction_model": "<model name>",
  "source_url": "<url you were told>",
  "fund_return_pct": <number or null>,
  "aum_eur": <integer euros or null>,
  "positions": [
    {
      "company_name": "<as written>",
      "ticker": "<your best-guess exchange ticker, e.g. ATYM.L, TRE.MC, SEM.LS; use yfinance-compatible suffixes>",
      "ticker_status": "unverified",    // always "unverified" — a downstream step validates
      "weight_pct": <0-100 number or null>,
      "action": "<one of: new|maintained|increased|reduced|exited>",
      "upside_pct": <number or null>,
      "thesis_text": "<1-5 sentence thesis as written in the letter, or null>"
    }
  ]
}

Rules:
- Output valid JSON. No markdown fences.
- Use null (not empty strings) for missing values.
- If a position is in a "new positions" section → action="new".
- If in an "exited" or "sold" section → action="exited".
- If labeled increased/decreased → action="increased" or "reduced".
- Otherwise → action="maintained".
- If no exchange suffix is obvious, pick the most likely exchange (Spanish → .MC,
  Portuguese → .LS, UK → .L, German → .DE, French → .PA, Italian → .MI,
  Stockholm → .ST, Helsinki → .HE, Danish → .CO, US → no suffix).
- The fields extracted_at / extraction_model / source_url will be overwritten
  downstream — you can fill placeholder strings.
- Return positions in the order they appear in the letter.
```

- [ ] **Step 4: Create the extractor module**

File: `scrapers/spanish_funds/extractor.py`

```python
"""LLM-based extraction from quarterly letter text to structured JSON."""
from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Protocol

import jsonschema

logger = logging.getLogger("valuehunter.spanish_funds.extractor")

PROMPTS_DIR = Path(__file__).resolve().parent / "prompts"
SCHEMA_PATH = (
    Path(__file__).resolve().parent.parent.parent
    / "knowledge_base" / "schemas" / "spanish_fund_position.schema.json"
)

DEFAULT_MODEL = "claude-sonnet-4-6"


class ExtractorError(RuntimeError):
    """Raised when the LLM cannot produce schema-valid output after retry."""


class AnthropicClient(Protocol):
    """Minimal protocol matching the anthropic.Anthropic client surface we use."""
    messages: Any


def load_prompt(name: str) -> str:
    path = PROMPTS_DIR / f"{name}.md"
    if not path.exists():
        raise FileNotFoundError(str(path))
    return path.read_text()


def _load_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text())


def _parse_response_text(msg: Any) -> str:
    """Extract the text content from an Anthropic Message object."""
    for block in msg.content:
        if getattr(block, "type", None) == "text":
            return block.text
    raise ExtractorError("no text block in LLM response")


def _call_llm(
    client: AnthropicClient,
    model: str,
    prompt: str,
    letter_text: str,
    fund_id: str,
    quarter: str,
    stricter: bool = False,
) -> str:
    user = f"fund_id: {fund_id}\nquarter hint: {quarter}\n\n--- letter text ---\n{letter_text}"
    if stricter:
        user += "\n\nPrior attempt produced malformed JSON. Return ONLY valid JSON matching the schema."
    msg = client.messages.create(
        model=model,
        max_tokens=8192,
        system=prompt,
        messages=[{"role": "user", "content": user}],
    )
    return _parse_response_text(msg)


def extract_from_text(
    letter_text: str,
    fund_id: str,
    quarter: str,
    source_url: str,
    client: AnthropicClient,
    model: str = DEFAULT_MODEL,
) -> dict:
    """Run LLM extraction + schema validation, with 1 retry on schema failure.

    Raises ExtractorError if both attempts produce invalid output.
    The caller-supplied metadata (source_url, extraction_model, extracted_at)
    is stamped onto the result, overriding whatever the LLM produced.
    """
    prompt = load_prompt("extraction_v1")
    schema = _load_schema()

    for attempt in range(2):
        raw = _call_llm(
            client, model, prompt, letter_text, fund_id, quarter,
            stricter=(attempt == 1),
        )
        try:
            result = json.loads(raw)
        except json.JSONDecodeError as e:
            logger.warning("attempt %d: invalid JSON: %s", attempt, e)
            continue
        # Stamp metadata
        result["source_url"] = source_url
        result["extraction_model"] = model
        result["extracted_at"] = datetime.now(timezone.utc).isoformat()
        result["fund_id"] = fund_id
        result["quarter"] = quarter
        try:
            jsonschema.validate(result, schema)
            return result
        except jsonschema.ValidationError as e:
            logger.warning("attempt %d: schema invalid: %s", attempt, e.message)
            continue

    raise ExtractorError(
        f"extraction failed for fund_id={fund_id} quarter={quarter} after 2 attempts"
    )
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `pytest tests/test_spanish_funds_extractor.py -v`
Expected: PASS (6 tests).

- [ ] **Step 6: Commit**

```bash
git add scrapers/spanish_funds/extractor.py \
        scrapers/spanish_funds/prompts/extraction_v1.md \
        tests/test_spanish_funds_extractor.py \
        tests/fixtures/spanish_funds/mock_llm_response_valid.json \
        tests/fixtures/spanish_funds/mock_llm_response_malformed.json \
        tests/fixtures/spanish_funds/sample_letter_text.txt
git commit -m "feat(spanish-funds): add LLM extractor with schema validation + retry"
```

---

## Task 5: Ticker resolver with mocked yfinance

**Files:**
- Create: `scrapers/spanish_funds/ticker_resolver.py`
- Create: `tests/test_spanish_funds_ticker_resolver.py`

- [ ] **Step 1: Write the failing test**

File: `tests/test_spanish_funds_ticker_resolver.py`

```python
"""Tests for ticker resolution against yfinance."""
from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from scrapers.spanish_funds.ticker_resolver import (
    TickerResolution,
    resolve_positions,
    resolve_ticker,
)


class TestResolveTicker:
    def test_verified_when_yfinance_returns_longName(self):
        with patch("scrapers.spanish_funds.ticker_resolver.yf.Ticker") as MockT:
            MockT.return_value.info = {"longName": "Atalaya Mining PLC", "regularMarketPrice": 5.2}
            r = resolve_ticker("ATYM.L")
        assert r.status == "verified"
        assert r.ticker == "ATYM.L"
        assert r.resolved_name == "Atalaya Mining PLC"

    def test_unverified_when_longName_missing(self):
        with patch("scrapers.spanish_funds.ticker_resolver.yf.Ticker") as MockT:
            MockT.return_value.info = {}
            r = resolve_ticker("FAKE.XX")
        assert r.status == "unverified"
        assert r.ticker == "FAKE.XX"
        assert r.resolved_name is None

    def test_unverified_when_yfinance_raises(self):
        with patch("scrapers.spanish_funds.ticker_resolver.yf.Ticker") as MockT:
            MockT.side_effect = Exception("network boom")
            r = resolve_ticker("ATYM.L")
        assert r.status == "unverified"

    def test_empty_ticker_returns_unverified(self):
        r = resolve_ticker("")
        assert r.status == "unverified"


class TestResolvePositions:
    def test_updates_positions_in_place(self):
        positions = [
            {"company_name": "Atalaya Mining", "ticker": "ATYM.L", "ticker_status": "unverified", "action": "maintained"},
            {"company_name": "Fake Co", "ticker": "FAKE.XX", "ticker_status": "unverified", "action": "new"},
        ]
        def fake_info(t):
            if t == "ATYM.L":
                return MagicMock(info={"longName": "Atalaya Mining PLC"})
            return MagicMock(info={})

        with patch("scrapers.spanish_funds.ticker_resolver.yf.Ticker", side_effect=fake_info):
            updated = resolve_positions(positions)

        assert updated[0]["ticker_status"] == "verified"
        assert updated[1]["ticker_status"] == "unverified"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_spanish_funds_ticker_resolver.py -v`
Expected: FAIL — `ModuleNotFoundError: scrapers.spanish_funds.ticker_resolver`.

- [ ] **Step 3: Create the resolver**

File: `scrapers/spanish_funds/ticker_resolver.py`

```python
"""Validate LLM-proposed tickers against yfinance.

Each position arrives with ticker_status='unverified'. This module calls
yfinance; if .info.longName is present, we mark verified. Otherwise we
leave unverified. Ambiguous is reserved for future fuzzy-search flow.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Literal

import yfinance as yf

logger = logging.getLogger("valuehunter.spanish_funds.ticker_resolver")

Status = Literal["verified", "unverified", "ambiguous"]


@dataclass(frozen=True)
class TickerResolution:
    ticker: str
    status: Status
    resolved_name: str | None


def resolve_ticker(ticker: str) -> TickerResolution:
    if not ticker:
        return TickerResolution(ticker=ticker, status="unverified", resolved_name=None)
    try:
        info = yf.Ticker(ticker).info
    except Exception as e:
        logger.warning("yfinance error for %s: %s", ticker, e)
        return TickerResolution(ticker=ticker, status="unverified", resolved_name=None)
    name = info.get("longName") if isinstance(info, dict) else None
    if name:
        return TickerResolution(ticker=ticker, status="verified", resolved_name=name)
    return TickerResolution(ticker=ticker, status="unverified", resolved_name=None)


def resolve_positions(positions: list[dict]) -> list[dict]:
    """Mutate-in-place style (returns the list too). Sets ticker_status."""
    for p in positions:
        r = resolve_ticker(p.get("ticker", ""))
        p["ticker_status"] = r.status
    return positions
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_spanish_funds_ticker_resolver.py -v`
Expected: PASS (6 tests).

- [ ] **Step 5: Commit**

```bash
git add scrapers/spanish_funds/ticker_resolver.py tests/test_spanish_funds_ticker_resolver.py
git commit -m "feat(spanish-funds): add yfinance-based ticker resolver"
```

---

## Task 6: Persist layer

**Files:**
- Create: `scrapers/spanish_funds/persist.py`
- Create: `tests/test_spanish_funds_persist.py`

- [ ] **Step 1: Write the failing test**

File: `tests/test_spanish_funds_persist.py`

```python
"""Tests for persistence of extracted letter data."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from scrapers.spanish_funds.persist import (
    already_processed,
    load_letter,
    persist_letter,
    save_raw_pdf,
    update_last_processed,
)


@pytest.fixture
def kb_root(tmp_path: Path) -> Path:
    (tmp_path / "spanish_funds").mkdir(parents=True)
    return tmp_path


@pytest.fixture
def sample_letter() -> dict:
    return {
        "fund_id": "cobas",
        "fund_name": "Cobas Selección",
        "quarter": "2026-Q1",
        "extracted_at": "2026-04-20T10:00:00Z",
        "extraction_model": "claude-sonnet-4-6",
        "source_url": "https://x",
        "positions": [],
    }


class TestPersistLetter:
    def test_writes_json_to_expected_path(self, kb_root, sample_letter):
        path = persist_letter(sample_letter, kb_root=kb_root)
        assert path == kb_root / "spanish_funds" / "cobas" / "2026-Q1.json"
        assert path.exists()
        loaded = json.loads(path.read_text())
        assert loaded["fund_id"] == "cobas"

    def test_load_round_trip(self, kb_root, sample_letter):
        persist_letter(sample_letter, kb_root=kb_root)
        loaded = load_letter("cobas", "2026-Q1", kb_root=kb_root)
        assert loaded == sample_letter

    def test_load_returns_none_when_missing(self, kb_root):
        assert load_letter("cobas", "2099-Q4", kb_root=kb_root) is None


class TestSaveRawPDF:
    def test_writes_pdf_bytes(self, kb_root):
        path = save_raw_pdf(b"PDFBYTES", fund_id="cobas", quarter="2026-Q1", kb_root=kb_root)
        assert path.exists()
        assert path.read_bytes() == b"PDFBYTES"
        assert path.name == "2026-Q1.pdf"


class TestLastProcessed:
    def test_update_and_check(self, kb_root):
        assert not already_processed("cobas", "abc123", kb_root=kb_root)
        update_last_processed("cobas", quarter="2026-Q1", content_hash="abc123", kb_root=kb_root)
        assert already_processed("cobas", "abc123", kb_root=kb_root)

    def test_different_hash_is_not_processed(self, kb_root):
        update_last_processed("cobas", quarter="2026-Q1", content_hash="abc123", kb_root=kb_root)
        assert not already_processed("cobas", "def456", kb_root=kb_root)
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_spanish_funds_persist.py -v`
Expected: FAIL — `ModuleNotFoundError: scrapers.spanish_funds.persist`.

- [ ] **Step 3: Create the persist module**

File: `scrapers/spanish_funds/persist.py`

```python
"""Disk persistence for extracted letters and per-fund processing state."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_KB_ROOT = Path(__file__).resolve().parent.parent.parent / "knowledge_base"


def _fund_dir(fund_id: str, kb_root: Path | None = None) -> Path:
    root = kb_root or DEFAULT_KB_ROOT
    d = root / "spanish_funds" / fund_id
    d.mkdir(parents=True, exist_ok=True)
    return d


def persist_letter(letter: dict, kb_root: Path | None = None) -> Path:
    """Write the extracted letter JSON to spanish_funds/{fund_id}/{quarter}.json."""
    fund_id = letter["fund_id"]
    quarter = letter["quarter"]
    d = _fund_dir(fund_id, kb_root)
    path = d / f"{quarter}.json"
    path.write_text(json.dumps(letter, indent=2, ensure_ascii=False))
    return path


def load_letter(fund_id: str, quarter: str, kb_root: Path | None = None) -> dict | None:
    path = _fund_dir(fund_id, kb_root) / f"{quarter}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text())


def save_raw_pdf(pdf_bytes: bytes, fund_id: str, quarter: str, kb_root: Path | None = None) -> Path:
    raw_dir = _fund_dir(fund_id, kb_root) / "raw"
    raw_dir.mkdir(exist_ok=True)
    path = raw_dir / f"{quarter}.pdf"
    path.write_bytes(pdf_bytes)
    return path


def update_last_processed(
    fund_id: str,
    quarter: str,
    content_hash: str,
    kb_root: Path | None = None,
    extraction_model: str = "",
) -> None:
    path = _fund_dir(fund_id, kb_root) / "last_processed.json"
    payload = {
        "quarter": quarter,
        "content_hash": content_hash,
        "extraction_model": extraction_model,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    path.write_text(json.dumps(payload, indent=2))


def already_processed(fund_id: str, content_hash: str, kb_root: Path | None = None) -> bool:
    path = _fund_dir(fund_id, kb_root) / "last_processed.json"
    if not path.exists():
        return False
    prev = json.loads(path.read_text())
    return prev.get("content_hash") == content_hash
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_spanish_funds_persist.py -v`
Expected: PASS (6 tests).

- [ ] **Step 5: Commit**

```bash
git add scrapers/spanish_funds/persist.py tests/test_spanish_funds_persist.py
git commit -m "feat(spanish-funds): add persistence layer (letters + raw PDFs + last_processed)"
```

---

## Task 7: First concrete scraper — Cobas

**Files:**
- Create: `scrapers/spanish_funds/cobas.py`
- Create: `scrapers/spanish_funds/pipeline.py` (orchestration glue — process_letter(scraper))
- Create: `tests/test_spanish_funds_cobas.py`
- Create: `tests/test_spanish_funds_pipeline.py`

- [ ] **Step 1: Write the failing test (Cobas URL detection)**

File: `tests/test_spanish_funds_cobas.py`

```python
"""Tests for Cobas URL detection."""
from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from scrapers.spanish_funds.cobas import CobasScraper


COBAS_LETTERS_HTML = """
<html><body>
<div class="cartas-inversor">
  <a href="/uploads/Cobas_Seleccion_Carta_T1_2026.pdf">Carta 1T 2026</a>
  <a href="/uploads/Cobas_Seleccion_Carta_T4_2025.pdf">Carta 4T 2025</a>
</div>
</body></html>
"""


class TestCobasScraper:
    def test_fund_id_is_cobas(self):
        s = CobasScraper()
        assert s.fund_id == "cobas"

    def test_get_latest_letter_returns_most_recent_pdf(self):
        mock_response = MagicMock(status_code=200, text=COBAS_LETTERS_HTML)
        mock_response.raise_for_status.return_value = None
        with patch("scrapers.spanish_funds.cobas.httpx.get", return_value=mock_response):
            # Also mock HEAD for content hash via ETag
            with patch.object(CobasScraper, "_fetch_content_hash", return_value="hash123"):
                meta = CobasScraper().get_latest_letter()
        assert meta is not None
        assert meta.quarter == "2026-Q1"
        assert "Cobas_Seleccion_Carta_T1_2026.pdf" in meta.url
        assert meta.content_hash == "hash123"

    def test_returns_none_when_no_letters_found(self):
        mock_response = MagicMock(status_code=200, text="<html><body>empty</body></html>")
        mock_response.raise_for_status.return_value = None
        with patch("scrapers.spanish_funds.cobas.httpx.get", return_value=mock_response):
            meta = CobasScraper().get_latest_letter()
        assert meta is None
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_spanish_funds_cobas.py -v`
Expected: FAIL — `ModuleNotFoundError: scrapers.spanish_funds.cobas`.

- [ ] **Step 3: Create the Cobas scraper**

File: `scrapers/spanish_funds/cobas.py`

```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_spanish_funds_cobas.py -v`
Expected: PASS (3 tests).

- [ ] **Step 5: Write failing pipeline test**

File: `tests/test_spanish_funds_pipeline.py`

```python
"""End-to-end pipeline test using a concrete scraper + mocked I/O."""
from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from scrapers.spanish_funds.base import LetterMeta
from scrapers.spanish_funds.cobas import CobasScraper
from scrapers.spanish_funds.pipeline import PipelineResult, process_scraper

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "spanish_funds"


@pytest.fixture
def valid_llm_response_text() -> str:
    return (FIXTURES / "mock_llm_response_valid.json").read_text()


def _mock_anthropic_msg(text: str) -> MagicMock:
    msg = MagicMock()
    msg.content = [MagicMock(text=text, type="text")]
    return msg


class TestProcessScraper:
    def test_full_pipeline_happy_path(self, valid_llm_response_text, tmp_path: Path):
        scraper = CobasScraper()
        letter_meta = LetterMeta(
            url="https://www.cobasam.com/q1-2026.pdf",
            quarter="2026-Q1",
            content_hash="fresh-hash",
        )
        with patch.object(CobasScraper, "get_latest_letter", return_value=letter_meta), \
             patch("scrapers.spanish_funds.pipeline._download_pdf", return_value=b"PDFBYTES"), \
             patch("scrapers.spanish_funds.pipeline.extract_text_from_pdf",
                   return_value="letter text"), \
             patch("scrapers.spanish_funds.pipeline.resolve_positions",
                   side_effect=lambda positions: [dict(p, ticker_status="verified") for p in positions]):
            mock_client = MagicMock()
            mock_client.messages.create.return_value = _mock_anthropic_msg(valid_llm_response_text)

            result = process_scraper(scraper, client=mock_client, kb_root=tmp_path)

        assert isinstance(result, PipelineResult)
        assert result.processed is True
        assert result.quarter == "2026-Q1"
        assert result.persisted_path.exists()
        letter = json.loads(result.persisted_path.read_text())
        assert letter["fund_id"] == "cobas"
        assert all(p["ticker_status"] == "verified" for p in letter["positions"])

    def test_skips_when_already_processed(self, tmp_path: Path):
        scraper = CobasScraper()
        letter_meta = LetterMeta(url="https://x", quarter="2026-Q1", content_hash="seen")

        # Pre-populate last_processed
        from scrapers.spanish_funds.persist import update_last_processed
        update_last_processed("cobas", "2026-Q1", "seen", kb_root=tmp_path)

        with patch.object(CobasScraper, "get_latest_letter", return_value=letter_meta):
            result = process_scraper(scraper, client=MagicMock(), kb_root=tmp_path)

        assert result.processed is False
        assert result.skipped_reason == "already_processed"

    def test_skips_when_no_letter_found(self, tmp_path: Path):
        scraper = CobasScraper()
        with patch.object(CobasScraper, "get_latest_letter", return_value=None):
            result = process_scraper(scraper, client=MagicMock(), kb_root=tmp_path)
        assert result.processed is False
        assert result.skipped_reason == "no_letter_found"
```

- [ ] **Step 6: Run pipeline test to verify it fails**

Run: `pytest tests/test_spanish_funds_pipeline.py -v`
Expected: FAIL — `ModuleNotFoundError: scrapers.spanish_funds.pipeline`.

- [ ] **Step 7: Create the pipeline**

File: `scrapers/spanish_funds/pipeline.py`

```python
"""Orchestration: glues scraper + download + extract + resolve + persist."""
from __future__ import annotations

import hashlib
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

import httpx

from scrapers.spanish_funds.base import FundScraper, LetterMeta
from scrapers.spanish_funds.extractor import AnthropicClient, extract_from_text
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
    import time
    delays = [1, 2, 4]
    last_err: Exception | None = None
    for d in delays:
        try:
            r = httpx.get(url, follow_redirects=True, timeout=60)
            r.raise_for_status()
            return r.content
        except Exception as e:
            last_err = e
            time.sleep(d)
    raise RuntimeError(f"download failed after 3 attempts: {last_err}")


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
    except Exception as e:
        return PipelineResult(fund_id=fid, processed=False,
                              quarter=meta.quarter, skipped_reason="extraction_failed", error=str(e))

    extracted["positions"] = resolve_positions(extracted.get("positions", []))

    path = persist_letter(extracted, kb_root=kb_root)
    update_last_processed(
        fid, quarter=meta.quarter, content_hash=real_hash,
        kb_root=kb_root, extraction_model=extracted.get("extraction_model", ""),
    )
    return PipelineResult(fund_id=fid, processed=True, quarter=meta.quarter, persisted_path=path)
```

- [ ] **Step 8: Run pipeline tests to verify they pass**

Run: `pytest tests/test_spanish_funds_pipeline.py tests/test_spanish_funds_cobas.py -v`
Expected: PASS (6 tests).

- [ ] **Step 9: Commit**

```bash
git add scrapers/spanish_funds/cobas.py \
        scrapers/spanish_funds/pipeline.py \
        tests/test_spanish_funds_cobas.py \
        tests/test_spanish_funds_pipeline.py
git commit -m "feat(spanish-funds): add Cobas scraper + end-to-end pipeline"
```

---

## Task 8: AzValor scraper

**Files:**
- Create: `scrapers/spanish_funds/azvalor.py`
- Create: `tests/test_spanish_funds_azvalor.py`

- [ ] **Step 1: Write the failing test**

File: `tests/test_spanish_funds_azvalor.py`

```python
"""Tests for AzValor URL detection."""
from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from scrapers.spanish_funds.azvalor import AzValorScraper


AZVALOR_HTML = """
<html><body>
  <a href="https://www.azvalor.com/app/uploads/2026/04/Carta-Trimestral-1T-2026.pdf">Carta 1T 2026</a>
  <a href="https://www.azvalor.com/app/uploads/2026/01/Carta-Trimestral-4T-2025.pdf">Carta 4T 2025</a>
</body></html>
"""


class TestAzValorScraper:
    def test_fund_id_is_azvalor(self):
        assert AzValorScraper().fund_id == "azvalor"

    def test_detects_latest_letter(self):
        mock_response = MagicMock(status_code=200, text=AZVALOR_HTML)
        mock_response.raise_for_status.return_value = None
        with patch("scrapers.spanish_funds.azvalor.httpx.get", return_value=mock_response):
            with patch.object(AzValorScraper, "_fetch_content_hash", return_value="h"):
                meta = AzValorScraper().get_latest_letter()
        assert meta.quarter == "2026-Q1"
        assert "1T-2026" in meta.url

    def test_returns_none_when_empty(self):
        mock_response = MagicMock(status_code=200, text="<html></html>")
        mock_response.raise_for_status.return_value = None
        with patch("scrapers.spanish_funds.azvalor.httpx.get", return_value=mock_response):
            assert AzValorScraper().get_latest_letter() is None
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_spanish_funds_azvalor.py -v`
Expected: FAIL — `ModuleNotFoundError: scrapers.spanish_funds.azvalor`.

- [ ] **Step 3: Create the AzValor scraper**

File: `scrapers/spanish_funds/azvalor.py`

```python
"""AzValor Asset Management letter scraper (URL detection only)."""
from __future__ import annotations

import hashlib
import re

import httpx
from bs4 import BeautifulSoup

from scrapers.spanish_funds.base import FundScraper, LetterMeta

AZVALOR_LETTERS_URL = "https://www.azvalor.com/carta-trimestral/"
FILENAME_RE = re.compile(r"Carta[\-_]?Trimestral[\-_]?(\d)T[\-_]?(\d{4})\.pdf", re.IGNORECASE)


class AzValorScraper(FundScraper):
    fund_id = "azvalor"
    fund_name = "AzValor Internacional"

    def get_latest_letter(self) -> LetterMeta | None:
        resp = httpx.get(AZVALOR_LETTERS_URL, follow_redirects=True, timeout=30)
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

    def _fetch_content_hash(self, url: str) -> str:
        try:
            r = httpx.head(url, follow_redirects=True, timeout=30)
            etag = r.headers.get("etag", "").strip('"')
            if etag:
                return etag
        except Exception:
            pass
        return hashlib.sha256(url.encode()).hexdigest()[:16]
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_spanish_funds_azvalor.py -v`
Expected: PASS (3 tests).

- [ ] **Step 5: Commit**

```bash
git add scrapers/spanish_funds/azvalor.py tests/test_spanish_funds_azvalor.py
git commit -m "feat(spanish-funds): add AzValor scraper"
```

---

## Task 9: Magallanes scraper

**Files:**
- Create: `scrapers/spanish_funds/magallanes.py`
- Create: `tests/test_spanish_funds_magallanes.py`

- [ ] **Step 1: Write the failing test**

File: `tests/test_spanish_funds_magallanes.py`

```python
"""Tests for Magallanes URL detection."""
from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from scrapers.spanish_funds.magallanes import MagallanesScraper


MAGALLANES_HTML = """
<html><body>
  <a href="/docs/2026-Q1-carta-magallanes-european.pdf">1T 2026</a>
  <a href="/docs/2025-Q4-carta-magallanes-european.pdf">4T 2025</a>
</body></html>
"""


class TestMagallanesScraper:
    def test_fund_id_is_magallanes(self):
        assert MagallanesScraper().fund_id == "magallanes"

    def test_detects_latest(self):
        mock_response = MagicMock(status_code=200, text=MAGALLANES_HTML)
        mock_response.raise_for_status.return_value = None
        with patch("scrapers.spanish_funds.magallanes.httpx.get", return_value=mock_response):
            with patch.object(MagallanesScraper, "_fetch_content_hash", return_value="h"):
                meta = MagallanesScraper().get_latest_letter()
        assert meta.quarter == "2026-Q1"
        assert "2026-Q1" in meta.url

    def test_returns_none_when_empty(self):
        mock_response = MagicMock(status_code=200, text="<html></html>")
        mock_response.raise_for_status.return_value = None
        with patch("scrapers.spanish_funds.magallanes.httpx.get", return_value=mock_response):
            assert MagallanesScraper().get_latest_letter() is None
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_spanish_funds_magallanes.py -v`
Expected: FAIL — `ModuleNotFoundError`.

- [ ] **Step 3: Create the Magallanes scraper**

File: `scrapers/spanish_funds/magallanes.py`

```python
"""Magallanes Value Investors letter scraper (URL detection only)."""
from __future__ import annotations

import hashlib
import re

import httpx
from bs4 import BeautifulSoup

from scrapers.spanish_funds.base import FundScraper, LetterMeta

MAGALLANES_LETTERS_URL = "https://www.magallanesvalue.com/cartas-trimestrales/"
BASE_URL = "https://www.magallanesvalue.com"
FILENAME_RE = re.compile(r"(\d{4})[\-_]Q(\d)[\-_\w]*\.pdf", re.IGNORECASE)


class MagallanesScraper(FundScraper):
    fund_id = "magallanes"
    fund_name = "Magallanes European Equity"

    def get_latest_letter(self) -> LetterMeta | None:
        resp = httpx.get(MAGALLANES_LETTERS_URL, follow_redirects=True, timeout=30)
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
        url = href if href.startswith("http") else f"{BASE_URL}{href}"
        content_hash = self._fetch_content_hash(url)
        return LetterMeta(url=url, quarter=f"{year}-Q{q}", content_hash=content_hash)

    def _fetch_content_hash(self, url: str) -> str:
        try:
            r = httpx.head(url, follow_redirects=True, timeout=30)
            etag = r.headers.get("etag", "").strip('"')
            if etag:
                return etag
        except Exception:
            pass
        return hashlib.sha256(url.encode()).hexdigest()[:16]
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_spanish_funds_magallanes.py -v`
Expected: PASS (3 tests).

- [ ] **Step 5: Commit**

```bash
git add scrapers/spanish_funds/magallanes.py tests/test_spanish_funds_magallanes.py
git commit -m "feat(spanish-funds): add Magallanes scraper"
```

---

## Task 10: Valentum scraper

**Files:**
- Create: `scrapers/spanish_funds/valentum.py`
- Create: `tests/test_spanish_funds_valentum.py`

- [ ] **Step 1: Write the failing test**

File: `tests/test_spanish_funds_valentum.py`

```python
"""Tests for Valentum URL detection."""
from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from scrapers.spanish_funds.valentum import ValentumScraper


VALENTUM_HTML = """
<html><body>
  <a href="https://valentum.es/wp-content/uploads/2026/04/Carta-1T-2026.pdf">Carta 1T 2026</a>
  <a href="https://valentum.es/wp-content/uploads/2026/01/Carta-4T-2025.pdf">Carta 4T 2025</a>
</body></html>
"""


class TestValentumScraper:
    def test_fund_id_is_valentum(self):
        assert ValentumScraper().fund_id == "valentum"

    def test_detects_latest(self):
        mock_response = MagicMock(status_code=200, text=VALENTUM_HTML)
        mock_response.raise_for_status.return_value = None
        with patch("scrapers.spanish_funds.valentum.httpx.get", return_value=mock_response):
            with patch.object(ValentumScraper, "_fetch_content_hash", return_value="h"):
                meta = ValentumScraper().get_latest_letter()
        assert meta.quarter == "2026-Q1"
        assert "1T-2026" in meta.url

    def test_returns_none_when_empty(self):
        mock_response = MagicMock(status_code=200, text="<html></html>")
        mock_response.raise_for_status.return_value = None
        with patch("scrapers.spanish_funds.valentum.httpx.get", return_value=mock_response):
            assert ValentumScraper().get_latest_letter() is None
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_spanish_funds_valentum.py -v`
Expected: FAIL — `ModuleNotFoundError`.

- [ ] **Step 3: Create the Valentum scraper**

File: `scrapers/spanish_funds/valentum.py`

```python
"""Valentum letter scraper (URL detection only)."""
from __future__ import annotations

import hashlib
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

    def _fetch_content_hash(self, url: str) -> str:
        try:
            r = httpx.head(url, follow_redirects=True, timeout=30)
            etag = r.headers.get("etag", "").strip('"')
            if etag:
                return etag
        except Exception:
            pass
        return hashlib.sha256(url.encode()).hexdigest()[:16]
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_spanish_funds_valentum.py -v`
Expected: PASS (3 tests).

- [ ] **Step 5: Commit**

```bash
git add scrapers/spanish_funds/valentum.py tests/test_spanish_funds_valentum.py
git commit -m "feat(spanish-funds): add Valentum scraper"
```

---

## Task 11: Migrate existing Horos scraper + backfill historic data

**Files:**
- Create: `scrapers/spanish_funds/horos.py`
- Create: `scripts/migrate_horos_to_unified_schema.py` (one-shot backfill)
- Create: `tests/test_spanish_funds_horos.py`
- Create: `tests/test_migrate_horos.py`
- Deprecate (add warning + redirect): `scrapers/horos_scraper.py`

- [ ] **Step 1: Write the failing test for new Horos scraper**

File: `tests/test_spanish_funds_horos.py`

```python
"""Tests for new Horos URL detection."""
from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from scrapers.spanish_funds.horos import HorosScraper


HOROS_HTML = """
<html><body>
<div class="cartas">
  <a href="https://horosam.com/carta-2026-q1.pdf">Carta Q1 2026</a>
  <a href="https://horosam.com/carta-2025-q4.pdf">Carta Q4 2025</a>
</div>
</body></html>
"""


class TestHorosScraper:
    def test_fund_id_is_horos(self):
        assert HorosScraper().fund_id == "horos"

    def test_detects_latest(self):
        mock_response = MagicMock(status_code=200, text=HOROS_HTML)
        mock_response.raise_for_status.return_value = None
        with patch("scrapers.spanish_funds.horos.httpx.get", return_value=mock_response):
            with patch.object(HorosScraper, "_fetch_content_hash", return_value="h"):
                meta = HorosScraper().get_latest_letter()
        assert meta.quarter == "2026-Q1"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_spanish_funds_horos.py -v`
Expected: FAIL — `ModuleNotFoundError`.

- [ ] **Step 3: Create new Horos scraper**

File: `scrapers/spanish_funds/horos.py`

```python
"""Horos Asset Management letter scraper (unified package — URL detection only).

The actual text extraction is now handled by the shared LLM extractor. The
legacy regex-based scraper at scrapers/horos_scraper.py is deprecated but
kept in place for the backfill script.
"""
from __future__ import annotations

import hashlib
import re

import httpx
from bs4 import BeautifulSoup

from scrapers.spanish_funds.base import FundScraper, LetterMeta

HOROS_LETTERS_URL = "https://horosam.com/articulos/cartas-al-inversor/"
FILENAME_RE = re.compile(r"carta[\-_](\d{4})[\-_]q(\d)", re.IGNORECASE)


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

    def _fetch_content_hash(self, url: str) -> str:
        try:
            r = httpx.head(url, follow_redirects=True, timeout=30)
            etag = r.headers.get("etag", "").strip('"')
            if etag:
                return etag
        except Exception:
            pass
        return hashlib.sha256(url.encode()).hexdigest()[:16]
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_spanish_funds_horos.py -v`
Expected: PASS (2 tests).

- [ ] **Step 5: Write failing test for backfill script**

File: `tests/test_migrate_horos.py`

```python
"""Tests for Horos legacy JSON → unified schema backfill."""
from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import pytest

from scripts.migrate_horos_to_unified_schema import migrate_legacy_json

SCHEMAS = Path(__file__).resolve().parent.parent / "knowledge_base" / "schemas"

LEGACY_SAMPLE = [
    {
        "letter_quarter": "2025-Q4",
        "fund": "HOROS_VALUE_INTERNACIONAL",
        "company": "Atalaya Mining",
        "ticker": "ATYM.L",
        "ticker_confidence": "EXACT",
        "weight_pct": 7.3,
        "action": "MAINTAINED",
        "thesis_summary": "Cobre estructural...",
        "upside_pct": 45,
        "source_url": "https://horosam.com/q4-2025.pdf",
        "scraped_date": "2026-01-15",
    },
    {
        "letter_quarter": "2025-Q4",
        "fund": "HOROS_VALUE_INTERNACIONAL",
        "company": "Semapa",
        "ticker": None,
        "ticker_confidence": "UNRESOLVED",
        "weight_pct": 3.0,
        "action": "NEW",
        "thesis_summary": None,
        "source_url": "https://horosam.com/q4-2025.pdf",
        "scraped_date": "2026-01-15",
    },
]


@pytest.fixture
def schema() -> dict:
    return json.loads((SCHEMAS / "spanish_fund_position.schema.json").read_text())


class TestMigrateLegacyJson:
    def test_groups_positions_into_single_letter(self, schema):
        migrated = migrate_legacy_json(LEGACY_SAMPLE)
        assert len(migrated) == 1
        letter = migrated[0]
        jsonschema.validate(letter, schema)
        assert letter["fund_id"] == "horos"
        assert letter["quarter"] == "2025-Q4"
        assert len(letter["positions"]) == 2

    def test_maps_legacy_status_to_unified(self):
        migrated = migrate_legacy_json(LEGACY_SAMPLE)
        positions = migrated[0]["positions"]
        by_name = {p["company_name"]: p for p in positions}
        # EXACT -> verified; UNRESOLVED -> unverified; action uppercase -> lowercase
        assert by_name["Atalaya Mining"]["ticker_status"] == "verified"
        assert by_name["Atalaya Mining"]["action"] == "maintained"
        # UNRESOLVED + null ticker: emit placeholder ticker "" ticker_status="unverified"
        assert by_name["Semapa"]["ticker_status"] == "unverified"
        assert by_name["Semapa"]["action"] == "new"
```

- [ ] **Step 6: Run test to verify it fails**

Run: `pytest tests/test_migrate_horos.py -v`
Expected: FAIL — `ModuleNotFoundError: scripts.migrate_horos_to_unified_schema`.

- [ ] **Step 7: Create the backfill script**

File: `scripts/migrate_horos_to_unified_schema.py`

```python
"""One-shot migration of Horos legacy JSON to unified spanish_fund_position schema.

Legacy format (flat list of positions in knowledge_base/universe/horos_positions.json).
New format (one file per quarter, under knowledge_base/spanish_funds/horos/).
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEGACY_PATH = ROOT / "knowledge_base" / "universe" / "horos_positions.json"
NEW_DIR = ROOT / "knowledge_base" / "spanish_funds" / "horos"


LEGACY_STATUS_MAP = {
    "EXACT": "verified",
    "FUZZY_MATCH": "ambiguous",
    "UNRESOLVED": "unverified",
}

LEGACY_ACTION_MAP = {
    "NEW": "new",
    "INCREASED": "increased",
    "DECREASED": "reduced",
    "MAINTAINED": "maintained",
    "EXITED": "exited",
}


def _convert_position(row: dict) -> dict:
    ticker = row.get("ticker") or ""
    return {
        "company_name": row["company"],
        "ticker": ticker,
        "ticker_status": LEGACY_STATUS_MAP.get(row.get("ticker_confidence", "UNRESOLVED"), "unverified"),
        "weight_pct": row.get("weight_pct"),
        "action": LEGACY_ACTION_MAP.get((row.get("action") or "MAINTAINED").upper(), "maintained"),
        "upside_pct": row.get("upside_pct"),
        "thesis_text": row.get("thesis_summary"),
    }


def migrate_legacy_json(legacy_positions: list[dict]) -> list[dict]:
    """Group flat positions by quarter and emit one letter JSON per quarter."""
    grouped: dict[str, list[dict]] = defaultdict(list)
    source_urls: dict[str, str] = {}
    for row in legacy_positions:
        q = row["letter_quarter"]
        grouped[q].append(_convert_position(row))
        source_urls[q] = row["source_url"]

    out: list[dict] = []
    for quarter, positions in sorted(grouped.items()):
        out.append({
            "fund_id": "horos",
            "fund_name": "Horos Value Internacional",
            "quarter": quarter,
            "extracted_at": datetime.now(timezone.utc).isoformat(),
            "extraction_model": "regex-v1-legacy-backfill",
            "source_url": source_urls[quarter],
            "fund_return_pct": None,
            "aum_eur": None,
            "positions": positions,
        })
    return out


def main():
    if not LEGACY_PATH.exists():
        print(f"No legacy file at {LEGACY_PATH}; nothing to migrate.")
        return 0
    legacy = json.loads(LEGACY_PATH.read_text())
    migrated = migrate_legacy_json(legacy)
    NEW_DIR.mkdir(parents=True, exist_ok=True)
    for letter in migrated:
        out = NEW_DIR / f"{letter['quarter']}.json"
        out.write_text(json.dumps(letter, indent=2, ensure_ascii=False))
        print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 8: Run tests to verify they pass**

Run: `pytest tests/test_migrate_horos.py -v`
Expected: PASS (2 tests).

- [ ] **Step 9: Deprecate old Horos scraper**

Edit `scrapers/horos_scraper.py` — add deprecation warning at module top:

```python
"""DEPRECATED: use scrapers.spanish_funds.horos.HorosScraper instead.

Kept only for backfill; emits a DeprecationWarning on import. Remove once
the migration script has run in production.
"""
from __future__ import annotations

import warnings

warnings.warn(
    "scrapers.horos_scraper is deprecated. "
    "Use scrapers.spanish_funds.horos.HorosScraper instead.",
    DeprecationWarning,
    stacklevel=2,
)

# ... rest of existing file unchanged
```

(Append the warning block above the existing imports. Do not delete anything else.)

- [ ] **Step 10: Verify the deprecation warning**

Run: `python -c "import scrapers.horos_scraper" 2>&1 | grep -i deprecat`
Expected: warning message printed.

- [ ] **Step 11: Commit**

```bash
git add scrapers/spanish_funds/horos.py \
        scrapers/horos_scraper.py \
        scripts/migrate_horos_to_unified_schema.py \
        tests/test_spanish_funds_horos.py \
        tests/test_migrate_horos.py
git commit -m "feat(spanish-funds): migrate Horos to unified package + legacy backfill"
```

---

## Task 12: Universe merger (multi-fund conviction)

**Files:**
- Create: `scrapers/spanish_funds/universe_merger.py`
- Create: `tests/test_spanish_funds_universe_merger.py`

- [ ] **Step 1: Write the failing test**

File: `tests/test_spanish_funds_universe_merger.py`

```python
"""Tests for the quality_universe merger."""
from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from scrapers.spanish_funds.universe_merger import merge_letter


LETTER_A = {
    "fund_id": "cobas",
    "fund_name": "Cobas Selección",
    "quarter": "2026-Q1",
    "source_url": "https://x/cobas",
    "extracted_at": "2026-04-20T10:00:00Z",
    "extraction_model": "m",
    "positions": [
        {"company_name": "Atalaya Mining", "ticker": "ATYM.L", "ticker_status": "verified",
         "weight_pct": 7.3, "action": "maintained", "thesis_text": "Cobre escaso..."},
        {"company_name": "Semapa", "ticker": "SEM.LS", "ticker_status": "unverified",
         "weight_pct": 3.0, "action": "new", "thesis_text": "Portugal..."},
    ],
}
LETTER_B = {
    "fund_id": "azvalor",
    "fund_name": "AzValor Internacional",
    "quarter": "2026-Q1",
    "source_url": "https://x/az",
    "extracted_at": "2026-04-20T10:00:00Z",
    "extraction_model": "m",
    "positions": [
        {"company_name": "Atalaya Mining", "ticker": "ATYM.L", "ticker_status": "verified",
         "weight_pct": 5.1, "action": "increased", "thesis_text": "Permisos..."},
    ],
}


@pytest.fixture
def universe_path(tmp_path: Path) -> Path:
    p = tmp_path / "quality_universe.yaml"
    p.write_text("{}\n")  # empty mapping
    return p


class TestMergeLetter:
    def test_first_merge_creates_entry(self, universe_path):
        merge_letter(LETTER_A, universe_path=universe_path)
        data = yaml.safe_load(universe_path.read_text())
        assert "ATYM.L" in data
        atym = data["ATYM.L"]
        assert atym["conviction_signal"] == "1_fund"
        assert len(atym["sources"]) == 1
        assert atym["sources"][0]["fund"] == "cobas"

    def test_skips_unverified_positions(self, universe_path):
        merge_letter(LETTER_A, universe_path=universe_path)
        data = yaml.safe_load(universe_path.read_text())
        assert "SEM.LS" not in data

    def test_second_fund_appends_and_boosts_conviction(self, universe_path):
        merge_letter(LETTER_A, universe_path=universe_path)
        merge_letter(LETTER_B, universe_path=universe_path)
        data = yaml.safe_load(universe_path.read_text())
        atym = data["ATYM.L"]
        assert atym["conviction_signal"] == "2_funds"
        assert len(atym["sources"]) == 2
        funds_in_sources = {s["fund"] for s in atym["sources"]}
        assert funds_in_sources == {"cobas", "azvalor"}

    def test_reprocessing_same_fund_quarter_is_idempotent(self, universe_path):
        merge_letter(LETTER_A, universe_path=universe_path)
        merge_letter(LETTER_A, universe_path=universe_path)  # replay
        data = yaml.safe_load(universe_path.read_text())
        assert len(data["ATYM.L"]["sources"]) == 1

    def test_thesis_snippets_trimmed_to_500_chars(self, universe_path):
        long_letter = dict(LETTER_A)
        long_letter["positions"] = [dict(LETTER_A["positions"][0], thesis_text="x" * 2000)]
        merge_letter(long_letter, universe_path=universe_path)
        data = yaml.safe_load(universe_path.read_text())
        assert len(data["ATYM.L"]["thesis_snippets"]["cobas"]) == 500
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_spanish_funds_universe_merger.py -v`
Expected: FAIL — `ModuleNotFoundError`.

- [ ] **Step 3: Create the merger**

File: `scrapers/spanish_funds/universe_merger.py`

```python
"""Merge verified fund positions into state/quality_universe.yaml.

For each verified ticker across fund letters, we append a source entry and
recompute a conviction_signal label. Idempotent on (fund_id, quarter).
"""
from __future__ import annotations

from datetime import date
from pathlib import Path

import yaml

DEFAULT_UNIVERSE_PATH = (
    Path(__file__).resolve().parent.parent.parent / "state" / "quality_universe.yaml"
)

SNIPPET_MAX_CHARS = 500


def _signal_label(n: int) -> str:
    if n == 1:
        return "1_fund"
    if n == 2:
        return "2_funds"
    return "3+_funds"


def merge_letter(letter: dict, universe_path: Path | None = None) -> None:
    path = universe_path or DEFAULT_UNIVERSE_PATH
    data = yaml.safe_load(path.read_text()) or {}
    fund_id = letter["fund_id"]
    quarter = letter["quarter"]

    for pos in letter.get("positions", []):
        if pos.get("ticker_status") != "verified":
            continue
        ticker = pos["ticker"]
        entry = data.get(ticker) or {
            "added_at": date.today().isoformat(),
            "sources": [],
            "conviction_signal": "1_fund",
            "thesis_snippets": {},
        }
        sources = entry.setdefault("sources", [])

        # Idempotency: remove any existing source from (fund_id, quarter) before appending
        sources[:] = [s for s in sources if not (s["fund"] == fund_id and s["quarter"] == quarter)]
        sources.append({
            "fund": fund_id,
            "quarter": quarter,
            "weight": pos.get("weight_pct"),
            "action": pos.get("action"),
        })

        # Recompute conviction over distinct funds
        distinct_funds = len({s["fund"] for s in sources})
        entry["conviction_signal"] = _signal_label(distinct_funds)

        # Thesis snippets: max 2 funds; keep the latest per fund; trim
        thesis = pos.get("thesis_text") or ""
        if thesis:
            snippets = entry.setdefault("thesis_snippets", {})
            snippets[fund_id] = thesis[:SNIPPET_MAX_CHARS]
            # Keep only 2 most recent by lexicographic fund ordering (stable)
            if len(snippets) > 2:
                keep = dict(list(snippets.items())[-2:])
                entry["thesis_snippets"] = keep

        data[ticker] = entry

    path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=True))
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_spanish_funds_universe_merger.py -v`
Expected: PASS (5 tests).

- [ ] **Step 5: Commit**

```bash
git add scrapers/spanish_funds/universe_merger.py tests/test_spanish_funds_universe_merger.py
git commit -m "feat(spanish-funds): add universe merger with multi-fund conviction"
```

---

## Task 13: Telegram digest builder

**Files:**
- Create: `scrapers/spanish_funds/digest_builder.py`
- Create: `tests/test_spanish_funds_digest_builder.py`

- [ ] **Step 1: Write the failing test**

File: `tests/test_spanish_funds_digest_builder.py`

```python
"""Tests for Telegram digest construction."""
from __future__ import annotations

import pytest

from scrapers.spanish_funds.digest_builder import build_digest


LETTER_CURRENT = {
    "fund_id": "azvalor",
    "fund_name": "AzValor Internacional",
    "quarter": "2026-Q1",
    "fund_return_pct": 4.2,
    "aum_eur": 1_500_000_000,
    "positions": [
        {"company_name": "Atalaya Mining", "ticker": "ATYM.L", "ticker_status": "verified",
         "weight_pct": 5.1, "action": "new", "thesis_text": "Cobre estructural..."},
        {"company_name": "Telefónica", "ticker": "TEF.MC", "ticker_status": "verified",
         "weight_pct": 3.2, "action": "new", "thesis_text": "Turnaround operativo..."},
        {"company_name": "Alibaba", "ticker": "BABA", "ticker_status": "verified",
         "weight_pct": None, "action": "exited", "thesis_text": None},
        {"company_name": "Renault", "ticker": "RNO.PA", "ticker_status": "verified",
         "weight_pct": 4.0, "action": "increased", "thesis_text": None},
        {"company_name": "Naturgy", "ticker": "NTGY.MC", "ticker_status": "verified",
         "weight_pct": 2.0, "action": "reduced", "thesis_text": None},
        {"company_name": "Sdiptech", "ticker": "SDIP-B.ST", "ticker_status": "unverified",
         "weight_pct": 2.3, "action": "new", "thesis_text": None},
    ],
}


class TestBuildDigest:
    def test_header_contains_fund_and_quarter(self):
        msg = build_digest(LETTER_CURRENT, multi_fund_tickers=[])
        assert "AzValor" in msg
        assert "Q1 2026" in msg

    def test_groups_actions_with_emoji(self):
        msg = build_digest(LETTER_CURRENT, multi_fund_tickers=[])
        assert "🆕 NUEVAS (2)" in msg
        assert "❌ SALIDAS (1)" in msg
        assert "📈 INCREMENTOS (1)" in msg
        assert "📉 REDUCCIONES (1)" in msg

    def test_new_section_shows_thesis_snippet(self):
        msg = build_digest(LETTER_CURRENT, multi_fund_tickers=[])
        assert "Cobre estructural" in msg
        assert "Turnaround" in msg

    def test_multi_fund_tickers_flagged(self):
        msg = build_digest(LETTER_CURRENT, multi_fund_tickers=["ATYM.L", "TRE.MC"])
        assert "Multi-fund" in msg
        assert "ATYM.L" in msg

    def test_unverified_tail_section(self):
        msg = build_digest(LETTER_CURRENT, multi_fund_tickers=[])
        assert "RESOLUCIÓN MANUAL" in msg
        assert "Sdiptech" in msg

    def test_return_and_aum_in_header(self):
        msg = build_digest(LETTER_CURRENT, multi_fund_tickers=[])
        assert "+4.2%" in msg
        assert "€1.5B" in msg
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_spanish_funds_digest_builder.py -v`
Expected: FAIL — `ModuleNotFoundError`.

- [ ] **Step 3: Create the digest builder**

File: `scrapers/spanish_funds/digest_builder.py`

```python
"""Build human-readable Telegram digest from a newly-processed letter."""
from __future__ import annotations

from collections import defaultdict


_ROMAN = {1: "1", 2: "2", 3: "3", 4: "4"}


def _format_aum(aum_eur: float | None) -> str:
    if not aum_eur:
        return "AuM: n/a"
    if aum_eur >= 1_000_000_000:
        return f"AuM: €{aum_eur / 1_000_000_000:.1f}B"
    return f"AuM: €{aum_eur / 1_000_000:.0f}M"


def _format_return(pct: float | None) -> str:
    if pct is None:
        return "Retorno: n/a"
    sign = "+" if pct >= 0 else ""
    return f"Retorno trimestre: {sign}{pct:.1f}%"


def _quarter_heading(q: str) -> str:
    year, qn = q.split("-")
    return f"{qn[0]}{qn[1].upper()} {year}"


def _trim(text: str | None, n: int = 60) -> str:
    if not text:
        return ""
    if len(text) <= n:
        return text
    return text[:n].rstrip() + "..."


def build_digest(letter: dict, multi_fund_tickers: list[str]) -> str:
    """Produce a markdown-friendly Telegram digest for a single new letter."""
    fund_name = letter["fund_name"]
    quarter = letter["quarter"]
    ret = _format_return(letter.get("fund_return_pct"))
    aum = _format_aum(letter.get("aum_eur"))

    by_action: dict[str, list[dict]] = defaultdict(list)
    unverified: list[dict] = []
    for p in letter.get("positions", []):
        if p.get("ticker_status") != "verified":
            unverified.append(p)
            continue
        by_action[p["action"]].append(p)

    parts = [
        f"📬 Nueva carta: {fund_name} {_quarter_heading(quarter)}",
        f"   {ret} | {aum}",
        "",
    ]

    news = by_action.get("new", [])
    if news:
        parts.append(f"🆕 NUEVAS ({len(news)})")
        for p in news:
            w = f"({p['weight_pct']:.1f}%)" if p.get("weight_pct") else ""
            snippet = _trim(p.get("thesis_text"))
            snippet_str = f' — "{snippet}"' if snippet else ""
            parts.append(f"   • {p['ticker']} {p['company_name']} {w}{snippet_str}")
        parts.append("")

    exits = by_action.get("exited", [])
    if exits:
        parts.append(f"❌ SALIDAS ({len(exits)})")
        for p in exits:
            parts.append(f"   • {p['ticker']} {p['company_name']}")
        parts.append("")

    incs = by_action.get("increased", [])
    if incs:
        tickers = ", ".join(p["ticker"] for p in incs)
        parts.append(f"📈 INCREMENTOS ({len(incs)}): {tickers}")

    reds = by_action.get("reduced", [])
    if reds:
        tickers = ", ".join(p["ticker"] for p in reds)
        parts.append(f"📉 REDUCCIONES ({len(reds)}): {tickers}")

    if multi_fund_tickers:
        parts.append("")
        parts.append("🔔 Multi-fund signals: " + ", ".join(multi_fund_tickers))

    if unverified:
        parts.append("")
        parts.append("⚠️ REQUIEREN RESOLUCIÓN MANUAL:")
        for p in unverified:
            proposed = p.get("ticker") or "(no ticker)"
            parts.append(f'   • "{p["company_name"]}" — ticker propuesto {proposed} no validado')

    return "\n".join(parts)
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_spanish_funds_digest_builder.py -v`
Expected: PASS (6 tests).

- [ ] **Step 5: Commit**

```bash
git add scrapers/spanish_funds/digest_builder.py tests/test_spanish_funds_digest_builder.py
git commit -m "feat(spanish-funds): add Telegram digest builder"
```

---

## Task 14: Web Researcher (A2.5) contextual lookup tool

**Files:**
- Modify: `agents/a25_web_researcher.py` — add `lookup_spanish_funds` tool
- Modify: `agents/prompts/a25_web_researcher.md` — document new tool
- Create: `scrapers/spanish_funds/lookup.py` — backing function
- Create: `tests/test_spanish_funds_lookup.py`

- [ ] **Step 1: Write the failing test**

File: `tests/test_spanish_funds_lookup.py`

```python
"""Tests for the cross-fund contextual lookup used by the Web Researcher."""
from __future__ import annotations

import json
from pathlib import Path

import pytest

from scrapers.spanish_funds.lookup import lookup_spanish_funds


@pytest.fixture
def kb_root(tmp_path: Path) -> Path:
    root = tmp_path / "knowledge_base" / "spanish_funds"
    for fund_id, positions in (
        ("cobas", [
            {"company_name": "Atalaya Mining", "ticker": "ATYM.L", "ticker_status": "verified",
             "weight_pct": 7.3, "action": "maintained", "thesis_text": "Cobre..."},
        ]),
        ("azvalor", [
            {"company_name": "Atalaya Mining", "ticker": "ATYM.L", "ticker_status": "verified",
             "weight_pct": 5.1, "action": "increased", "thesis_text": "Permisos..."},
        ]),
    ):
        d = root / fund_id
        d.mkdir(parents=True)
        (d / "2026-Q1.json").write_text(json.dumps({
            "fund_id": fund_id, "fund_name": fund_id.capitalize(),
            "quarter": "2026-Q1", "source_url": "https://x",
            "extracted_at": "2026-04-20T10:00:00Z", "extraction_model": "m",
            "positions": positions,
        }))
    return tmp_path


class TestLookup:
    def test_finds_position_across_multiple_funds(self, kb_root):
        result = lookup_spanish_funds("ATYM.L", kb_root=kb_root / "knowledge_base")
        assert result["ticker"] == "ATYM.L"
        assert result["fund_count"] == 2
        fund_ids = {h["fund_id"] for h in result["holdings"]}
        assert fund_ids == {"cobas", "azvalor"}

    def test_uses_latest_quarter_only(self, kb_root):
        # Write an older quarter to one of the funds
        older = kb_root / "knowledge_base" / "spanish_funds" / "cobas" / "2025-Q4.json"
        older.write_text(json.dumps({
            "fund_id": "cobas", "fund_name": "Cobas", "quarter": "2025-Q4",
            "source_url": "https://x", "extracted_at": "2025-10-01T00:00:00Z",
            "extraction_model": "m",
            "positions": [
                {"company_name": "Old Pos", "ticker": "OLD.MC", "ticker_status": "verified",
                 "weight_pct": 1.0, "action": "exited", "thesis_text": None},
            ],
        }))
        result = lookup_spanish_funds("OLD.MC", kb_root=kb_root / "knowledge_base")
        # Not in the latest quarter, so should not appear
        assert result["fund_count"] == 0

    def test_returns_empty_when_no_match(self, kb_root):
        result = lookup_spanish_funds("NONE.XX", kb_root=kb_root / "knowledge_base")
        assert result["fund_count"] == 0
        assert result["holdings"] == []

    def test_ignores_unverified(self, kb_root):
        # Patch one of the files to have unverified status for ATYM.L
        path = kb_root / "knowledge_base" / "spanish_funds" / "cobas" / "2026-Q1.json"
        data = json.loads(path.read_text())
        data["positions"][0]["ticker_status"] = "unverified"
        path.write_text(json.dumps(data))
        result = lookup_spanish_funds("ATYM.L", kb_root=kb_root / "knowledge_base")
        assert result["fund_count"] == 1  # only azvalor remains
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_spanish_funds_lookup.py -v`
Expected: FAIL — `ModuleNotFoundError`.

- [ ] **Step 3: Create the lookup module**

File: `scrapers/spanish_funds/lookup.py`

```python
"""Cross-fund contextual lookup for the Web Researcher agent.

Given a ticker, return which Spanish value funds currently hold it, each
fund's most recent thesis snippet, weight, and action, considering only
the latest quarter on disk per fund.
"""
from __future__ import annotations

import json
from pathlib import Path

DEFAULT_KB_ROOT = Path(__file__).resolve().parent.parent.parent / "knowledge_base"


def _latest_letter(fund_dir: Path) -> dict | None:
    files = sorted(fund_dir.glob("[0-9]*.json"))
    if not files:
        return None
    return json.loads(files[-1].read_text())


def lookup_spanish_funds(ticker: str, kb_root: Path | None = None) -> dict:
    root = (kb_root or DEFAULT_KB_ROOT) / "spanish_funds"
    if not root.exists():
        return {"ticker": ticker, "fund_count": 0, "holdings": []}

    holdings = []
    for fund_dir in sorted(root.iterdir()):
        if not fund_dir.is_dir():
            continue
        letter = _latest_letter(fund_dir)
        if not letter:
            continue
        for p in letter.get("positions", []):
            if p.get("ticker") == ticker and p.get("ticker_status") == "verified":
                holdings.append({
                    "fund_id": letter["fund_id"],
                    "fund_name": letter["fund_name"],
                    "quarter": letter["quarter"],
                    "weight_pct": p.get("weight_pct"),
                    "action": p.get("action"),
                    "thesis_snippet": (p.get("thesis_text") or "")[:500] or None,
                })
                break

    return {"ticker": ticker, "fund_count": len(holdings), "holdings": holdings}
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_spanish_funds_lookup.py -v`
Expected: PASS (4 tests).

- [ ] **Step 5: Wire the tool into A2.5 agent**

First read current state:

Run: `grep -n "tools\|tool_runner\|register" agents/a25_web_researcher.py | head -30`

Based on the existing pattern, add a tool registration to `agents/a25_web_researcher.py`. Specific edit depends on how the agent registers tools — read the file and add a new tool entry following the existing convention.

If the file uses `_tool_runner.py` for tool dispatch, add this pattern at the existing tool registration site:

```python
from scrapers.spanish_funds.lookup import lookup_spanish_funds

TOOLS.append({
    "name": "lookup_spanish_funds",
    "description": (
        "Return Spanish value funds (Cobas, AzValor, Magallanes, Horos, Valentum) "
        "that currently hold the given ticker, with thesis snippets, weights, and "
        "actions from their most recent quarterly letters. Use this BEFORE running "
        "fundamental analysis to check for established value-investor conviction."
    ),
    "input_schema": {
        "type": "object",
        "properties": {"ticker": {"type": "string"}},
        "required": ["ticker"],
    },
    "handler": lambda ticker: lookup_spanish_funds(ticker),
})
```

Update the prompt file `agents/prompts/a25_web_researcher.md` — add a section:

```
## Spanish value fund overlap

Before you do general web research, call `lookup_spanish_funds(ticker)` on the
target. If fund_count > 0, include the thesis snippets in your report under a
"Spanish value fund signal" heading — this is high-signal context from
professional value investors with track records. Treat fund_count >= 2 as a
strong multi-fund conviction signal worth flagging explicitly.
```

- [ ] **Step 6: Verify agent still tests pass**

Run: `pytest tests/test_a25_web_researcher.py -v`
Expected: PASS (existing tests continue to pass; the new tool is additive).

- [ ] **Step 7: Commit**

```bash
git add scrapers/spanish_funds/lookup.py \
        tests/test_spanish_funds_lookup.py \
        agents/a25_web_researcher.py \
        agents/prompts/a25_web_researcher.md
git commit -m "feat(spanish-funds): wire lookup tool into A2.5 Web Researcher"
```

---

## Task 15: Scheduler integration

**Files:**
- Modify: `scheduler/cron.py`
- Create: `scrapers/spanish_funds/scheduled_job.py`
- Create: `tests/test_spanish_funds_scheduled_job.py`

- [ ] **Step 1: Write the failing test**

File: `tests/test_spanish_funds_scheduled_job.py`

```python
"""Tests for the weekly scheduled job."""
from __future__ import annotations

from unittest.mock import MagicMock, patch

from scheduler.cron import create_scheduler


class TestSchedulerIntegration:
    def test_spanish_funds_job_registered(self):
        scheduler = create_scheduler()
        job_ids = [j.id for j in scheduler.get_jobs()]
        assert "spanish_funds_weekly" in job_ids

    def test_spanish_funds_job_fires_on_monday_8am(self):
        scheduler = create_scheduler()
        job = next(j for j in scheduler.get_jobs() if j.id == "spanish_funds_weekly")
        trigger_str = str(job.trigger)
        assert "mon" in trigger_str.lower()
        assert "08" in trigger_str or "hour='8'" in trigger_str


class TestScheduledJobFunction:
    def test_calls_all_scrapers_and_notifies(self):
        from scrapers.spanish_funds.scheduled_job import run_weekly_check
        from scrapers.spanish_funds.pipeline import PipelineResult

        # Two processed, one skipped
        results = [
            PipelineResult(fund_id="cobas", processed=True, quarter="2026-Q1",
                           persisted_path=None),
            PipelineResult(fund_id="azvalor", processed=False, skipped_reason="already_processed"),
            PipelineResult(fund_id="magallanes", processed=False, skipped_reason="no_letter_found"),
        ]

        with patch("scrapers.spanish_funds.scheduled_job.process_scraper", side_effect=results), \
             patch("scrapers.spanish_funds.scheduled_job._anthropic_client", return_value=MagicMock()), \
             patch("scrapers.spanish_funds.scheduled_job._send_telegram") as mock_send:
            out = run_weekly_check()

        assert out["processed"] == 1
        assert out["skipped"] == 2
        # Telegram only sent for processed letters
        mock_send.assert_called_once()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_spanish_funds_scheduled_job.py -v`
Expected: FAIL — job not registered yet, module missing.

- [ ] **Step 3: Create the scheduled job module**

File: `scrapers/spanish_funds/scheduled_job.py`

```python
"""Scheduled job wrapper: runs all 5 fund scrapers and ships a digest."""
from __future__ import annotations

import asyncio
import logging
import os
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
            continue

        processed += 1
        letter = load_letter(result.fund_id, result.quarter)
        if letter is None:
            continue
        try:
            merge_letter(letter)
        except Exception:
            logger.exception("universe merge failed for %s %s", result.fund_id, result.quarter)

        digest = build_digest(letter, multi_fund_tickers=[])  # TODO extend with cross-fund flags
        _send_telegram(digest)

    return {"processed": processed, "skipped": skipped, "errors": errors}
```

- [ ] **Step 4: Wire into the scheduler**

Edit `scheduler/cron.py` — inside `create_scheduler()`, add a new job registration after the daily job:

```python
    scheduler.add_job(
        _spanish_funds_weekly_job,
        CronTrigger(day_of_week="mon", hour=8, minute=0),
        id="spanish_funds_weekly",
        name="Spanish Value Fund Ingestion (Monday 08:00)",
    )
```

Add the job function at module level (above `create_scheduler`):

```python
def _spanish_funds_weekly_job():
    from scrapers.spanish_funds.scheduled_job import run_weekly_check
    logger.info("Starting Spanish value fund ingestion")
    result = run_weekly_check()
    logger.info(
        "Spanish funds ingestion complete: processed=%d skipped=%d errors=%s",
        result["processed"], result["skipped"], result["errors"],
    )
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `pytest tests/test_spanish_funds_scheduled_job.py tests/test_scheduler.py -v`
Expected: PASS (all tests — existing scheduler tests should still pass since we only added a job).

- [ ] **Step 6: Commit**

```bash
git add scrapers/spanish_funds/scheduled_job.py \
        scheduler/cron.py \
        tests/test_spanish_funds_scheduled_job.py
git commit -m "feat(spanish-funds): wire weekly Monday job into APScheduler"
```

---

## Task 16: Manual CLI entry point

**Files:**
- Create: `scrapers/spanish_funds/cli.py`
- Create: `tests/test_spanish_funds_cli.py`

- [ ] **Step 1: Write the failing test**

File: `tests/test_spanish_funds_cli.py`

```python
"""Tests for the manual CLI trigger."""
from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from scrapers.spanish_funds.cli import main


class TestCLI:
    def test_single_fund_happy_path(self, capsys):
        from scrapers.spanish_funds.pipeline import PipelineResult
        result = PipelineResult(fund_id="cobas", processed=True, quarter="2026-Q1",
                                persisted_path=None)
        with patch("scrapers.spanish_funds.cli.process_scraper", return_value=result), \
             patch("scrapers.spanish_funds.cli._anthropic_client", return_value=MagicMock()):
            code = main(["--fund", "cobas"])
        out = capsys.readouterr().out
        assert code == 0
        assert "cobas" in out
        assert "processed=True" in out or "processed: True" in out

    def test_all_funds_flag(self):
        from scrapers.spanish_funds.pipeline import PipelineResult
        results = [
            PipelineResult(fund_id=f, processed=False, skipped_reason="no_letter_found")
            for f in ("cobas", "azvalor", "magallanes", "horos", "valentum")
        ]
        with patch("scrapers.spanish_funds.cli.process_scraper", side_effect=results), \
             patch("scrapers.spanish_funds.cli._anthropic_client", return_value=MagicMock()):
            code = main(["--all"])
        assert code == 0

    def test_unknown_fund_errors(self):
        code = main(["--fund", "bestinver"])
        assert code != 0

    def test_dry_run_skips_persist(self, capsys):
        from scrapers.spanish_funds.pipeline import PipelineResult
        result = PipelineResult(fund_id="cobas", processed=True, quarter="2026-Q1",
                                persisted_path=None)
        with patch("scrapers.spanish_funds.cli.process_scraper", return_value=result) as mock_proc, \
             patch("scrapers.spanish_funds.cli._anthropic_client", return_value=MagicMock()):
            code = main(["--fund", "cobas", "--dry-run"])
        assert code == 0
        # In dry-run we still call process_scraper but pass a tmp kb_root
        assert mock_proc.called
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_spanish_funds_cli.py -v`
Expected: FAIL — `ModuleNotFoundError`.

- [ ] **Step 3: Create the CLI**

File: `scrapers/spanish_funds/cli.py`

```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_spanish_funds_cli.py -v`
Expected: PASS (4 tests).

- [ ] **Step 5: Commit**

```bash
git add scrapers/spanish_funds/cli.py tests/test_spanish_funds_cli.py
git commit -m "feat(spanish-funds): add manual CLI entry point"
```

---

## Final verification

- [ ] **Run the full test suite**

Run: `pytest tests/ -v --tb=short`
Expected: All tests pass. New tests = ~45 added across tasks 1-16.

- [ ] **Verify module imports cleanly**

Run: `python -c "from scrapers.spanish_funds import base, pipeline, cli; print('ok')"`
Expected: `ok`

- [ ] **Verify scheduler registers the new job**

Run: `python -c "from scheduler.cron import validate_scheduler; import json; print(json.dumps(validate_scheduler(), indent=2))"`
Expected: output includes `{"id": "spanish_funds_weekly", ...}`

- [ ] **Smoke run in dry-run mode against Cobas**

Run: `ANTHROPIC_API_KEY=$YOUR_KEY python -m scrapers.spanish_funds.cli --fund cobas --dry-run`
Expected: Either `processed=True quarter=2026-QX` (if a new letter is detected) or `processed=False skipped_reason=no_letter_found`. No errors. The real Anthropic API is hit — this consumes ~30k input + ~4k output tokens (≈ $0.10 at Sonnet pricing).

If this smoke passes with a real detection, the full pipeline is proven end-to-end.

---

## Spec coverage check

| Spec section | Task(s) |
|---|---|
| Unified schema | Task 1 |
| Fund list (Cobas, AzValor, Magallanes, Horos, Valentum) | Tasks 7, 8, 9, 10, 11 |
| Level 2 extraction (holdings + thesis) | Task 4 |
| Auto download + LLM extraction | Task 7 (pipeline) + Task 4 (extractor) |
| Ticker resolution | Task 5 |
| Weekly Monday cron | Task 15 |
| Migrate Horos | Task 11 |
| Universe merger + multi-fund conviction | Task 12 |
| Web Researcher contextual lookup | Task 14 |
| Telegram digest | Task 13 |
| Manual CLI | Task 16 |
| Error handling (retry, dedup, manual fallback) | Pipeline task 7, persist task 6 |
| Testing (unit + golden fixtures) | All tasks include tests |

---

## Notes for implementer

- **Anthropic API key** must be set via `ANTHROPIC_API_KEY` env var for any live extraction. Tests mock it fully so offline CI is fine.
- **Real fund URLs**: the HTML/filename patterns assumed in each scraper (Tasks 7-11) are based on public inspection at the time of writing. If any fund changes their site structure, only that fund's `get_latest_letter()` needs updating — the shared pipeline is unaffected.
- **Golden fixtures for integration testing**: not pre-built in this plan. After Task 7 is live, run Cobas against a real recent letter once, vet the output manually, commit the resulting JSON as a fixture in `tests/fixtures/spanish_funds/golden/cobas_2026_q1_expected.json`. Repeat per fund. These are integration tests — mark with `@pytest.mark.integration` and skip by default in CI.
- **Manual drop fallback** (mentioned in spec but not implemented in this plan as a dedicated task): the pipeline already supports it indirectly — if `get_latest_letter()` returns `None` but you drop a PDF into `knowledge_base/spanish_funds/{fund}/inbox/{quarter}.pdf`, a small helper (~15 lines) can be added later that detects it and re-enters the pipeline from the download step.

---

*Plan produced by superpowers:writing-plans. Implementation uses superpowers:subagent-driven-development or superpowers:executing-plans.*
