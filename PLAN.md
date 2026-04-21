# ValueHunter v1.0 — Evolution Plan

## Context

`invest_value_manager/` is a production-grade, single-operator investment system (Framework v4.6, 116 sessions, 11 live positions, 45 Python tools, 24 agent-skills, 200+ universe candidates, 110+ logged decisions). Two top-level planning docs (`ARQUITECTURA_ValueHunter_v1.md`, `CLAUDE_CODE_PROMPT_ValueHunter.md`) sketch a "ValueHunter v1.0" 4-layer / 10-agent architecture. This plan evolves the system **in place**, preserving all existing tools, frameworks, thesis data, and decision history, filling the four concrete gaps:

1. **Layer-0 Orchestrator (Gobernador)** — no central governor exists today; sessions are human-driven.
2. **Special Situations pipeline** — frameworks exist (merger arb, spin-offs, liquidations) but neither screener nor modeler is coded.
3. **External idea-source scrapers** — Horos quarterly letters and Alpha Vulture coverage are not ingested.
4. **Knowledge Base schemas** — current state is loose YAML; JSON Schemas needed for contracts and validation.

Intended outcome: a semi-autonomous, scheduler-driven value + special-situations fund assistant where the Governor orchestrates 10 v1.0 agents, each delegating to the existing 24 skills/frameworks.

## Key Decisions (confirmed)

| # | Decision | Choice |
|---|----------|--------|
| D1 | Directory strategy | **Evolve in place** inside `invest_value_manager/`. No renames, no migrations. Rebrand docs to "ValueHunter" but keep path. |
| D2 | Agent reconciliation | **10 v1.0 agents orchestrate existing 24 skills**. The 10 are thin wrappers. |
| D3 | Sprint 1 scope | **Formalize schemas + Horos/AV scrapers + Orchestrator skeleton.** Existing screener stays as-is. |
| D4 | Orchestration engine | **Custom Python orchestrator** using Anthropic SDK + asyncio. No LangGraph. |
| D5 | Model policy | Sonnet 4.6 for judgement-heavy agents. Haiku 4.5 for structured scoring/monitoring. Opus 4.6 for Governor only. |

## Heritage Summary

**Keep (production)**: all 45 tools in `tools/`, all 24 skills in `.claude/skills/`, all rules in `.claude/rules/`, all state (`portfolio/`, `state/`, `thesis/active/`, `world/sectors/`, `learning/`).

**Refactor / formalize**: loose YAML → JSON Schema draft-07 contracts. Unified pipeline enum (R1-R4 vs S1-S4).

**Build new**: Layer-0 Orchestrator, Agent 1.2 Special Situations Screener, Agent 2.2 Special Situation Modeler, Agent 2.5 Web Researcher, Horos scraper, Alpha Vulture scraper, APScheduler loop, Telegram notifier, Streamlit dashboard, JSON Schemas.

**Retire**: nothing.

## Target Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│  LAYER 0 — GOVERNOR (orchestrator/governor.py)                  │
│  Decides which agents run, order, parallel vs sequential        │
│  Model: claude-opus-4-6 (meta-decisions only, low-frequency)    │
└─────────────────────────────────────────────────────────────────┘
         │                                          │
         ▼ parallel                                 ▼ sequential
┌──────────────────────────┐              ┌──────────────────────┐
│ LAYER 1 — SCREENING      │              │ LAYER 3 — PORTFOLIO  │
│ 1.1 Quant Screener       │              │ 3.1 Decision Maker   │
│ 1.2 Special Sits Screen. │              │ 3.2 Portfolio Monitor│
└──────────────────────────┘              └──────────────────────┘
         │                                          ▲
         ▼ 5× parallel fanout                       │
┌──────────────────────────────────────────────────┴──────────────┐
│ LAYER 2 — DEEP ANALYSIS                                         │
│ 2.1 Financial Analyst  2.2 Special Sit Modeler                  │
│ 2.3 Business Analyst   2.4 Risk Analyst   2.5 Web Researcher    │
└─────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────┐
│ LAYER 4 — KNOWLEDGE BASE (file-based, git-tracked)              │
│ companies/{ticker}/   portfolio/   universe/   learning/        │
└─────────────────────────────────────────────────────────────────┘
```

## Evolution Map

| Existing path | Action | Notes |
|---------------|--------|-------|
| `tools/*.py` (45) | Keep | Reused as tool calls from 10 agents. |
| `.claude/skills/*` (24) | Keep + reference | Agents invoke these as sub-skills. |
| `.claude/rules/*.md` | Keep + extend | Add `rules/orchestrator-protocol.md`. |
| `portfolio/current.yaml` | Keep + schema | `schemas/portfolio_position.schema.json`. |
| `state/*.yaml` | Keep + schema | One schema per state file. |
| `thesis/active/{TICKER}/thesis.md` | Keep | MD primary; sibling `thesis.json` generated. |
| `learning/decisions_log.yaml` | Keep + schema | Schema added. |
| `world/sectors/*.md` | Keep | Free-form markdown. |
| `data/` | Keep | Scraper outputs join here. |
| `docs/*.html` | Keep | Dashboards stay; Streamlit companion added. |
| `telegram/` | Evolve | Wire to Governor notification hook. |
| Root ValueHunter planning docs | Archive | Move to `docs/history/`. |

## New Repository Structure (deltas only)

```
invest_value_manager/
├── orchestrator/                      # NEW — Layer 0
│   ├── governor.py                    # entry point, state machine, async fanout
│   ├── registry.py                    # 10-agent + 24-skill registry
│   ├── flows/
│   │   ├── weekly_screening.py        # Flow 1
│   │   ├── on_demand_analysis.py      # Flow 2
│   │   └── daily_monitoring.py        # Flow 3
│   └── audit.py                       # run_log.jsonl writer
├── agents/                            # NEW — 10 agent modules + prompts/
├── models/                            # NEW — merger_arb.py, liquidation.py, spinoff.py, biotech_cash.py
├── scrapers/                          # NEW — horos, alpha_vulture, sec_edgar_rss, pr_newswire
├── knowledge_base/
│   └── schemas/                       # NEW — 12 JSON Schema files
├── scheduler/cron.py                  # NEW — APScheduler
├── notifications/                     # NEW — telegram.py + formatters.py
├── dashboard/app.py                   # NEW — Streamlit
├── docs/ARCHITECTURE.md, MIGRATION.md # NEW
├── docs/history/                      # archived prior design docs
├── tests/                             # NEW — test_schemas, test_horos, test_merger_arb, test_governor
├── pyproject.toml                     # NEW
└── CLAUDE.md                          # EVOLVED
```

## JSON Schema Inventory (Sprint 1)

12 schemas under `knowledge_base/schemas/`, draft-07, strict `additionalProperties: false`:

| Schema | Validates |
|--------|-----------|
| `company.schema.json` | `knowledge_base/companies/{ticker}/fundamentals.json` |
| `thesis.schema.json` | `thesis/active/{TICKER}/thesis.json` |
| `decision.schema.json` | `learning/decisions_log.yaml` entries |
| `portfolio_position.schema.json` | `portfolio/current.yaml` items |
| `closed_position.schema.json` | `portfolio/history.yaml` items |
| `performance.schema.json` | `knowledge_base/portfolio/performance.json` |
| `watchlist_entry.schema.json` | `state/watchlist.yaml` |
| `horos_position.schema.json` | `knowledge_base/universe/horos_positions.json` |
| `alpha_vulture_idea.schema.json` | `knowledge_base/universe/alpha_vulture_ideas.json` |
| `screener_result.schema.json` | `knowledge_base/universe/screener_results.json` |
| `special_situation.schema.json` | per-situation tracking |
| `market_regime.schema.json` | `learning/market_regimes.json` |

## Agent Specifications

### Layer 1 — Screening

- **A1.1 Quantitative Screener** — haiku-4-5 — 2-5k tok. Reuses `dynamic_screener.py`, `batch_scorer.py`, `quality_universe.py`, `quality_scorer.py`, `opportunity_filter.py`.
- **A1.2 Special Situations Screener** (NEW) — haiku-4-5 — 5-10k tok. SEC EDGAR RSS + PR Newswire. Outputs `special_situation.schema.json[]`.

### Layer 2 — Deep Analysis (parallel fanout)

- **A2.1 Financial Analyst** — sonnet-4-6 — 8-15k. DCF 3-scenario, NAV, net cash, ROIC, red flags. Reuses `dcf_calculator.py`, `quality_scorer.py`, `narrative_checker.py`, `forward_return.py`; skills `valuation-methods`, `projection-framework`, `filing-analysis`.
- **A2.2 Special Situation Modeler** (NEW) — sonnet-4-6 — 6-12k. Merger-arb spread+prob, liquidation value, spin-off stub, biotech burn+CVR. Depends on `models/*.py`.
- **A2.3 Business Analyst** — sonnet-4-6 — 8-12k. Moat, mgmt, bull/bear, catalysts. Reuses `insider_tracker.py`, `ownership_analyzer.py`, `sector_health.py`; skills `business-analysis-framework`, `skin-in-the-game`, `quality-compounders`, `sector-deep-dive`.
- **A2.4 Risk Analyst** — haiku-4-5 — 3-6k. 7-dim risk, sizing cap, thesis-break, FX, max-DD. Reuses `risk_heatmap.py`, `constraint_checker.py`, `drift_detector.py`, `correlation_matrix.py`.
- **A2.5 Web Researcher** — haiku-4-5 — 4-8k. News, earnings, 13F, Horos/AV coverage, regulatory. Sources: Anthropic `web_search` + Horos/AV scrapers.

### Layer 3 — Portfolio

- **A3.1 Decision Maker** — sonnet-4-6 — 6-10k. Gates: MoS > 30% OR E[CAGR] > 12% with thesis intact; risk < 7; no precedent conflict. Reuses `consistency_checker.py`, `portfolio_optimizer.py`; skills `investment-rules`, `pre-execution-check`, `recommendation-context`.
- **A3.2 Portfolio Monitor** — haiku-4-5 — 2-4k/day. P&L, drift, events, new filings. Reuses `portfolio_stats.py`, `thesis_monitor.py`, `earnings_intel.py`, `session_opener.py`.

### Layer 0 — Governor

- **opus-4-6**, low-frequency meta-decisions. State machine: `IDLE → SCREENING → CANDIDATE_SELECTION → ANALYSIS_FANOUT → DECISION → NOTIFY → IDLE`. Audit to `orchestrator/runs/{run_id}.json`.

## Tech Decisions

| Concern | Choice |
|---------|--------|
| Orchestration | Custom Python + `anthropic` SDK + `asyncio` |
| Scheduling | APScheduler (in-process) |
| Notifications | Telegram + email fallback |
| Dashboard | Streamlit (alongside existing HTML) |
| Data validation | `jsonschema` + `pydantic` v2 |
| Web search | Anthropic native `web_search` tool |
| Scraping | `httpx` + `beautifulsoup4` + `pypdf` |
| Testing | `pytest` + fixtures |
| Python | 3.12 pinned in `pyproject.toml` |

## Sprint Plan (4 × 2 weeks)

### Sprint 1 — Foundations
1. `pyproject.toml` + `.python-version`.
2. 12 JSON Schemas under `knowledge_base/schemas/`.
3. `tests/test_schemas.py` — validates *every* existing YAML/JSON. 100% pass.
4. `scrapers/horos_scraper.py` — parses horosam.com quarterly PDFs.
5. `scrapers/alpha_vulture_scraper.py` — blog + Seeking Alpha author page.
6. `orchestrator/governor.py` skeleton — state machine + registry + audit log.
7. `docs/ARCHITECTURE.md`, `docs/MIGRATION.md`, updated `CLAUDE.md`.
8. Archive root planning docs to `docs/history/`.

**Accept:** `pytest` green; `python -m orchestrator.governor --dry-run` prints registry; Horos scraper parses ≥1 quarter; existing `tools/session_opener.py` unbroken.

### Sprint 2 — Deep Analysis Agents
9. `agents/a21_financial_analyst.py` + prompt.
10. `agents/a23_business_analyst.py` + prompt.
11. `agents/a24_risk_analyst.py` + prompt.
12. `agents/a25_web_researcher.py` + prompt.
13. `orchestrator/flows/on_demand_analysis.py` (Flow 2).

**Accept:** `python -m orchestrator on-demand MORN` in <90s with valid JSON; golden-file tests pass.

### Sprint 3 — Special Situations + Decision Maker
14. `models/merger_arb.py`, `liquidation.py`, `spinoff.py`, `biotech_cash.py`.
15. `agents/a12_special_sits_screener.py` + `scrapers/sec_edgar_rss.py` + `scrapers/pr_newswire.py`.
16. `agents/a22_special_sit_modeler.py`.
17. `agents/a31_decision_maker.py`.
18. `orchestrator/flows/weekly_screening.py` (Flow 1).

**Accept:** Weekly run emits ≥1 valid decision JSON; Telegram test message delivered.

### Sprint 4 — Monitoring, Scheduling, Dashboard
19. `agents/a32_portfolio_monitor.py` + `flows/daily_monitoring.py`.
20. `scheduler/cron.py` (APScheduler).
21. `notifications/telegram.py` + `formatters.py`.
22. `dashboard/app.py` (Streamlit).
23. Performance metrics backfill → `knowledge_base/portfolio/performance.json`.

**Accept:** Scheduler dry-run 48h hits all windows; dashboard renders; monitoring digest for 11 positions.

## CLAUDE.md Content Outline

1. Project identity ("ValueHunter v1.0, evolved from invest_value_manager v4.6")
2. Mission & methodology (Horos + Alpha Vulture)
3. Governance model (CIO preserved; Governor orchestrates)
4. 14 Principles (verbatim)
5. Architecture (pointer to `docs/ARCHITECTURE.md`)
6. Agent invocation conventions
7. Tool inventory (pointer to `.claude/rules/tools-reference.md`)
8. Skill inventory (pointer to `.claude/skills/`)
9. How to add a new agent
10. How to add a new skill
11. How to run each flow
12. Session protocol (6 phases, unchanged)
13. Error patterns (pointer to `.claude/rules/error-patterns.md`)
14. Memory rules (unchanged)

## Migration Notes

- No file moves. Data stays put.
- `thesis/active/{TICKER}/thesis.md` stays primary; sibling `thesis.json` generated on first analysis.
- `portfolio/current.yaml`, `history.yaml`, `state/*.yaml`, `learning/decisions_log.yaml` — unchanged; schemas validate.
- `knowledge_base/companies/{ticker}/` populated lazily by Agent 2.1.
- Root `/ARQUITECTURA_ValueHunter_v1.md`, `/CLAUDE_CODE_PROMPT_ValueHunter.md` → `docs/history/` (Sprint 1).

## Remaining Ambiguities (flag at Sprint-1 kickoff)

1. **Horos ticker inference** — Default: fuzzy-match + yfinance search; `null` when unresolved.
2. **Alpha Vulture paywall** — Default: free blog only; paid items stored as URL stubs.
3. **Decision Maker position-size** — Default: suggestion bounded by `portfolio-constraints`; human veto.
4. **Broker execution** — Manual eToro in Sprint 1-4 scope.
5. **Short-side agents** — Default: Special Situations Screener + Business Analyst cover short ideation; no separate short screener.
6. **Governor autonomy** — Default: daily autonomous monitoring; weekly digest; on-demand user-initiated; **never** auto-executes trades.
7. **Goodwill_pct backfill** — Default: run `batch_scorer.py --all-universe --goodwill` as final Sprint 1 task.

## Summary

**Sprint deliverable count:** 23 numbered deliverables across 4 sprints (8 + 5 + 5 + 5).

**Regression protection:** existing workflow `python3 tools/session_opener.py` must remain functional after every sprint.
