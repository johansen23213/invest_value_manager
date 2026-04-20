# Spanish Value Fund Ingestion — Design Spec

> **Date:** 2026-04-20
> **Author:** Joan Yanini + Claude Opus 4.7 (brainstorming session)
> **Status:** APPROVED — ready for implementation plan
> **Parent project:** ValueHunter v1.0 (evolution of invest_value_manager)
> **Sub-project:** 1 of 3 (followed by Spanish Small Cap Universe + Spanish Media Monitoring)

---

## Purpose

Extract holdings and thesis narratives from the quarterly letters of 5 Spanish value asset managers (Cobas, AzValor, Magallanes, Horos, Valentum) and integrate the signals into the existing ValueHunter pipeline in three ways: (1) seed the quality universe with pre-filtered ideas, (2) feed contextual thesis snippets to the Web Researcher agent during analysis, (3) notify operator of new letters via Telegram digest.

## Goals

1. Automated weekly check for new quarterly letters across the 5 funds.
2. Robust LLM-based extraction from heterogeneous PDF formats into a unified schema.
3. Ticker resolution with automatic verification against yfinance + manual fallback for edge cases.
4. Three integration points: quality universe merge, Web Researcher contextual lookup, Telegram digest.
5. Re-use the existing Horos scraper as migrated component in a unified package.

## Non-goals (v1)

- Scraping Spanish media (Rankia, Finect, Expansión) — scope of Sub-project 3.
- Screening the Spanish small cap universe (BME Growth, Mercado Continuo) — scope of Sub-project 2.
- Extracting macro commentary, management reflections, full performance attribution (Level 3 content).
- Supporting funds outside the approved 5 (e.g. Bestinver, True Value, Buy & Hold).
- Real-time or intra-quarter letter detection (weekly Monday check is sufficient).
- Backfilling historical letters older than the current deployment moment (one-shot import possible but out of scope).

## Scope — confirmed decisions

| # | Decision | Choice |
|---|----------|--------|
| D1 | Fund list | Cobas, AzValor, Magallanes, Horos (migrate existing), Valentum |
| D2 | Extraction depth | Level 2 — holdings + per-position thesis narratives (no macro commentary) |
| D3 | Extraction approach | Full auto download + LLM extraction (Claude Sonnet 4.6) |
| D4 | Integration surface | (B+C+D): Web Researcher context + Universe pipeline + Telegram digest |
| D5 | Horos treatment | Migrate to unified package; deprecate standalone scraper |
| D6 | Schema | Evolve `horos_position.schema.json` → `spanish_fund_position.schema.json` |
| D7 | Scheduling | Weekly APScheduler cron, Monday 08:00 UTC |

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│ SCHEDULER (APScheduler, Monday 08:00 UTC)                   │
│  └─ check_and_process_all_funds()                           │
└──────────────┬──────────────────────────────────────────────┘
               │
   ┌───────────┴───────────┬──────────┬──────────┬──────────┐
   ▼                       ▼          ▼          ▼          ▼
┌───────┐            ┌────────┐   ┌──────┐   ┌────────┐  ┌──────────┐
│ Cobas │            │AzValor │   │Magal │   │ Horos  │  │ Valentum │
│scraper│            │scraper │   │lanes │   │(migrat)│  │ scraper  │
└───┬───┘            └────┬───┘   └───┬──┘   └────┬───┘  └────┬─────┘
    │                     │           │           │           │
    └─────────┬───────────┴───────────┴───────────┴───────────┘
              ▼
    ┌─────────────────────────────────────────────────┐
    │  SHARED PIPELINE (base.py)                      │
    │  download_pdf → pdftotext → llm_extract →       │
    │  schema_validate → resolve_tickers → persist    │
    └──────────┬──────────────────────────────────────┘
               ▼
    ┌──────────────────────────────────────────────────┐
    │  KNOWLEDGE BASE                                  │
    │  /spanish_funds/{fund}/{YYYY-QN}.json            │
    └──────────┬───────────────────────────────────────┘
               │ fan-out
   ┌───────────┼───────────────┐
   ▼           ▼               ▼
┌──────────┐ ┌──────────────┐ ┌─────────────┐
│ Universe │ │ Web          │ │ Telegram    │
│ Merger   │ │ Researcher   │ │ Digest      │
│ (flag    │ │ (contextual  │ │ (new/exit/  │
│  source) │ │  lookup at   │ │  top thesis)│
│          │ │  analysis)   │ │             │
└──────────┘ └──────────────┘ └─────────────┘
```

**Design principle:** per-fund scrapers differ ONLY in URL detection for the latest PDF. Everything downstream (text extraction, LLM parsing, schema validation, ticker resolution, persistence, fan-out) is shared in `base.py`.

## Components

### File structure

```
invest_value_manager/scrapers/spanish_funds/
├── __init__.py
├── base.py                      # Shared pipeline (abstract scraper + orchestration)
├── cobas.py                     # URL detection — Cobas
├── azvalor.py                   # URL detection — AzValor
├── magallanes.py                # URL detection — Magallanes
├── valentum.py                  # URL detection — Valentum
├── horos.py                     # Migrated from scrapers/horos_scraper.py
├── extractor.py                 # LLM extraction (Anthropic SDK) + schema validation
├── ticker_resolver.py           # LLM ticker proposal + yfinance validation
├── universe_merger.py           # Writes to state/quality_universe.yaml
├── digest_builder.py            # Telegram digest construction
├── cli.py                       # Manual trigger: --fund X --quarter YYYY-QN
└── prompts/
    └── extraction_v1.md         # Versioned LLM extraction prompt

invest_value_manager/knowledge_base/schemas/
└── spanish_fund_position.schema.json    # Unified schema (evolved from horos_position)

invest_value_manager/knowledge_base/spanish_funds/
├── cobas/
│   ├── raw/                     # Downloaded PDFs (immutable archive)
│   ├── 2026-Q1.json             # Extracted structured data
│   └── last_processed.json      # Detection state (hash + quarter + timestamp)
├── azvalor/
├── magallanes/
├── horos/
└── valentum/

invest_value_manager/tests/
├── test_spanish_funds_base.py
├── test_spanish_funds_extractor.py
├── test_ticker_resolver.py
├── test_universe_merger.py
├── test_digest_builder.py
└── fixtures/spanish_letters/
    ├── cobas_2025_q4_sample.pdf
    ├── azvalor_2025_q4_sample.pdf
    ├── magallanes_2025_q4_sample.pdf
    ├── horos_2025_q4_sample.pdf      # existing letter migrated as fixture
    ├── valentum_2025_q4_sample.pdf
    └── golden/
        ├── cobas_2025_q4_expected.json
        ├── azvalor_2025_q4_expected.json
        ├── magallanes_2025_q4_expected.json
        ├── horos_2025_q4_expected.json
        └── valentum_2025_q4_expected.json
```

### Component responsibilities

**`base.py`** — Abstract scraper class + orchestration. Defines the 9-step pipeline. Per-fund scrapers subclass it, implementing only `get_latest_letter_url()` and optional `parse_quarter_from_url()`.

**Per-fund scrapers** (`cobas.py`, `azvalor.py`, `magallanes.py`, `valentum.py`, `horos.py`) — Concrete implementations. Each knows the URL pattern of its fund's investor letters page and extracts the latest PDF URL.

**`extractor.py`** — Wraps Anthropic SDK call. Input: raw text + fund_id + quarter hint. Output: validated JSON matching schema. Retry 1× with stricter prompt if schema validation fails.

**`ticker_resolver.py`** — For each extracted position: validates the LLM-proposed ticker via `yfinance.Ticker(t).info`. Sets `ticker_status` to `verified`, `unverified`, or `ambiguous`.

**`universe_merger.py`** — Reads all verified positions across funds and merges into `state/quality_universe.yaml`. Multi-fund positions get a `conviction_signal` flag. Unverified positions are excluded from merge until manually resolved.

**`digest_builder.py`** — Builds formatted Telegram message from the diff of current quarter vs previous. Uses existing `telegram/` notifier wiring.

**`cli.py`** — Manual override for testing or reprocessing: `python -m scrapers.spanish_funds.cli --fund cobas --quarter 2026-Q1 [--dry-run]`.

## Data flow (per new letter detected)

```
1. DETECT     check_new_letter(fund)
                → compare URL hash vs last_processed.json
                → return new_pdf_url or None

2. DOWNLOAD   httpx GET PDF
                → save to knowledge_base/spanish_funds/{fund}/raw/{YYYY-QN}.pdf
                → retry 3× exp backoff on network failure

3. TEXTIFY    pdftotext
                → raw_text.txt (in memory, not persisted)

4. EXTRACT    Claude Sonnet 4.6 + prompts/extraction_v1.md + schema
                → structured JSON
                → retry 1× with stricter prompt on schema validation fail

5. VALIDATE   JSON Schema draft-07 validation
                → reject if malformed after retry
                → on persistent fail: save raw text, Telegram alert with snippet

6. RESOLVE    Per position: LLM ticker → yfinance.Ticker(t).info
                → verified | unverified | ambiguous
                → unverified positions persist but skip universe merge

7. PERSIST    Save to knowledge_base/spanish_funds/{fund}/{YYYY-QN}.json

8. UPDATE     last_processed.json { hash, quarter, timestamp, extraction_model }

9. FAN-OUT    universe_merger.merge() → state/quality_universe.yaml
              digest_builder.build() → telegram notifier
```

## Schema — `spanish_fund_position.schema.json`

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Spanish Fund Position",
  "type": "object",
  "required": ["fund_id", "fund_name", "quarter", "extracted_at", "extraction_model", "source_url", "positions"],
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
        "properties": {
          "company_name": { "type": "string" },
          "ticker": { "type": "string" },
          "ticker_status": {
            "type": "string",
            "enum": ["verified", "unverified", "ambiguous"]
          },
          "weight_pct": { "type": ["number", "null"] },
          "action": {
            "type": "string",
            "enum": ["new", "maintained", "increased", "reduced", "exited"]
          },
          "upside_pct": { "type": ["number", "null"] },
          "thesis_text": { "type": ["string", "null"] }
        }
      }
    },
    "macro_commentary": { "type": ["null"], "const": null }
  }
}
```

**Horos migration:** a one-shot script reads existing `horos_positions.json` entries and backfills them into the new schema (adding `fund_id: "horos"`, `ticker_status: "verified"` for entries that already passed the regex scraper, and `extraction_model: "regex-v1-legacy"` for provenance). No data is lost.

## Integration points (fan-out)

### 1. Universe Merger

Writes to `state/quality_universe.yaml`:

```yaml
ATYM.L:
  added_at: 2026-04-20
  sources:
    - { fund: cobas, quarter: 2026-Q1, weight: 7.3, action: maintained }
    - { fund: azvalor, quarter: 2026-Q1, weight: 5.1, action: increased }
  conviction_signal: "2_funds"    # 1_fund | 2_funds | 3+_funds
  thesis_snippets:                # max 2 entries, trimmed to 500 chars each
    cobas: "Cobre estructuralmente escaso..."
    azvalor: "Catalizador permisos Sudamérica..."
```

Multi-fund conviction rule: if `conviction_signal >= 2_funds`, flag `multi_fund_conviction: true` on the universe entry. `r1_prioritizer.py` may use this as a tiebreaker. **Consumed by** existing universe infrastructure — no downstream change required beyond reading the new `sources` array.

### 2. Web Researcher (A2.5) — contextual lookup

Add a new tool call to the A2.5 agent prompt: `lookup_spanish_funds(ticker)` → returns `{ holdings: [{fund, weight, action, quarter}], thesis_snippets: {...} }` if the ticker is held by any Spanish fund. Inject the result into the analysis context **before** R1 fundamental-analyst runs.

Implementation: add the tool wrapper in `agents/prompts/a25_web_researcher.md` + backing function in the web researcher module that reads from `knowledge_base/spanish_funds/*/` directly (no DB, just JSON file reads).

### 3. Telegram Digest

Format per new letter detected:

```
📬 Nueva carta: AzValor Q1 2026
   Retorno trimestre: +4.2% | AuM: €1.5B

🆕 NUEVAS (2)
   • ATYM.L Atalaya Mining (5.1%) — "Cobre estructural..."
   • TEF.MC Telefónica (3.2%) — "Turnaround operativo..."

❌ SALIDAS (1)
   • BABA Alibaba — tesis completada

📈 INCREMENTOS (3): RNO.PA, TRE.MC, SEM.LS
📉 REDUCCIONES (1): NTGY.MC

🔔 Multi-fund signals: ATYM.L (2 fondos), TRE.MC (3 fondos)
```

Unverified tickers appended as tail section:

```
⚠️ REQUIEREN RESOLUCIÓN MANUAL:
   • "Sdiptech" — ticker propuesto SDIP-B.ST no validado
   • "Greenvolt" — no encontrado
```

Sent via existing `telegram/` notifier (already wired to the Governor in recent commits).

## Error handling

| Step | Failure mode | Handling |
|------|--------------|----------|
| Download | HTTP 4xx/5xx / timeout | Retry 3× exp backoff → fallback to manual drop inbox → Telegram alert |
| pdftotext | Corrupt PDF / no text extracted | Flag for manual drop → Telegram alert with source URL |
| LLM extract | Schema validation fail | Retry 1× with stricter prompt → on 2nd fail: persist raw text + Telegram alert with snippet |
| LLM extract | Hallucinated non-existent ticker | Caught downstream by ticker_resolver (yfinance returns no data) → `ticker_status=unverified`, listed in digest |
| LLM extract | Position weights don't sum to ~100% | Warning in digest, does not block pipeline (letters often show only top 10-20) |
| Ticker resolve | yfinance rate limit | Backoff + queue; does not block persist (unverified positions are acceptable transient state) |
| Universe merger | Conflict with existing position | Append to `sources[]` array (no overwrite); multi-fund is the expected case |
| Digest | Telegram API unreachable | Log locally, retry on next scheduler tick |

**Duplicate prevention:** `last_processed.json` per fund stores SHA256 hash of the downloaded PDF. If a subsequent fetch returns the same hash → skip (detects accidental re-uploads by the asset manager).

**Manual drop fallback:** if auto-download fails for a specific fund (e.g. CAPTCHA, paywall introduced), operator drops the PDF in `knowledge_base/spanish_funds/{fund}/inbox/` and the next scheduler tick picks it up and processes from step 3 (TEXTIFY) onward.

## Testing strategy

### Unit tests

- `test_spanish_funds_base.py` — pipeline orchestration with mocked sub-components.
- `test_spanish_funds_extractor.py` — LLM extraction with fixture PDFs → golden JSON comparison (tolerance on `thesis_text` free-form fields via semantic similarity or length-only check).
- `test_ticker_resolver.py` — mock yfinance responses for verified/unverified/ambiguous paths.
- `test_universe_merger.py` — multi-fund merge, conviction boost logic, existing-entry append.
- `test_digest_builder.py` — diff detection (new/exited/changed), formatting, unverified tail section.

### Integration tests

Five golden fixtures — one real quarterly letter per fund (Q4 2025 or earliest available), extracted JSON curated manually once, used as regression baseline. Tolerance policy:

- Exact match required on: fund_id, quarter, position count, tickers, actions, weights (±0.5pp).
- Soft match on: `thesis_text` (length within ±30%, keyword containment check).

### CI smoke test

Weekly CI job runs extraction over the 5 fixtures + full schema validation + real yfinance ticker resolution. Any regression fails the build. Uses existing pytest + CI infrastructure; no new tooling.

## Scheduling

Add to `orchestrator/scheduler.py`:

```python
scheduler.add_job(
    check_and_process_all_funds,
    CronTrigger(day_of_week='mon', hour=8, minute=0),
    id='spanish_funds_weekly',
)
```

- Cadence: Monday 08:00 UTC (09:00-10:00 Spanish time).
- Action: iterates the 5 funds; for each, runs the 9-step pipeline if a new letter is detected.
- Dry-run flag: `--dry-run` skips persist + Telegram (for testing).
- Manual trigger: `python -m scrapers.spanish_funds.cli --fund cobas --quarter 2026-Q1`.

## Rollout plan (sketch, detail in implementation plan)

1. Schema + base infrastructure (`base.py`, `extractor.py`, `ticker_resolver.py`, schema JSON).
2. First fund end-to-end: Cobas (or AzValor) — validates the pattern.
3. Migrate Horos into the new package + backfill existing JSON.
4. Add AzValor, Magallanes, Valentum — one at a time, each with its golden fixture.
5. Universe merger + Web Researcher integration.
6. Telegram digest builder.
7. Scheduler wiring + CI smoke test.

Each step merges independently; each has its own test fixture; partial rollouts are safe (failing fund = only that fund skipped, others proceed).

## Open questions deferred to implementation plan

- Exact URL patterns for each fund's letters page (requires manual inspection before coding each scraper).
- Whether `pdfplumber` or `pdftotext` CLI gives better text extraction on tabular holdings data.
- Whether the LLM extraction prompt should be one-shot or few-shot with examples.
- Back-fill scope: do we extract historical letters (last 4 quarters per fund) as one-off, or only forward?

---

*Spec prepared via superpowers:brainstorming skill. Next step: superpowers:writing-plans for implementation plan.*
