# ValueHunter v1.0 — Architecture

> Evolution of `invest_value_manager` Framework v4.6 into a semi-autonomous, scheduler-driven value + special-situations fund assistant.

## Design Principles

1. **Evolve, don't rewrite.** All 45 existing tools and 24 skills are reused.
2. **Thin orchestration wrappers.** The 10 v1.0 agents delegate to the existing 24 skills/frameworks.
3. **File-based knowledge base.** YAML/JSON/Markdown, git-tracked, schema-validated.
4. **CIO identity preserved.** Governor orchestrates; human confirms trades; Governor never auto-executes.
5. **Model routing by judgement intensity.** Opus (Governor), Sonnet (judgement agents), Haiku (scoring/monitoring).

## Layer Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│  LAYER 0 — GOVERNOR (orchestrator/governor.py)                          │
│                                                                         │
│  State machine: IDLE → SCREENING → CANDIDATE_SELECTION →                │
│                 ANALYSIS_FANOUT → DECISION → NOTIFY → IDLE              │
│                                                                         │
│  Responsibilities:                                                      │
│    • Decide flow (weekly / on-demand / daily)                           │
│    • Sequence / parallelize agents                                      │
│    • Persist run state to orchestrator/runs/{run_id}.json               │
│    • Emit audit events                                                  │
│    • Call notifications/telegram.py on completion                       │
│                                                                         │
│  Model: claude-opus-4-6 (meta-decisions only, low-frequency)            │
└─────────────────────────────────────────────────────────────────────────┘
         │                                          │
         ▼ parallel fanout                          ▼ sequential
┌──────────────────────────────────┐      ┌────────────────────────────┐
│ LAYER 1 — SCREENING              │      │ LAYER 3 — PORTFOLIO        │
│                                  │      │                            │
│ A1.1 Quantitative Screener       │      │ A3.1 Decision Maker        │
│   • Model: haiku-4-5             │      │   • Model: sonnet-4-6      │
│   • yfinance + EDGAR             │      │   • Aggregates Layer 2     │
│   • Wraps dynamic_screener.py,   │      │   • Gates: MoS/ECAGR/risk  │
│     batch_scorer, quality_       │      │   • Emits decision JSON    │
│     universe                     │      │                            │
│                                  │      │ A3.2 Portfolio Monitor     │
│ A1.2 Special Situations Screener │      │   • Model: haiku-4-5       │
│   • Model: haiku-4-5             │      │   • Daily P&L, drift,      │
│   • SEC RSS + PR Newswire        │      │     events, filings        │
│   • NEW (Sprint 3)               │      │                            │
└──────────────────────────────────┘      └────────────────────────────┘
         │                                              ▲
         ▼ 5× parallel fanout on selected ticker        │
┌────────────────────────────────────────────────────────┴──────────────┐
│ LAYER 2 — DEEP ANALYSIS                                               │
│                                                                       │
│  A2.1 Financial Analyst          A2.2 Special Situation Modeler       │
│    sonnet-4-6, 8-15k tok           sonnet-4-6, 6-12k tok              │
│    DCF 3-scenario, NAV,            Merger-arb spread+prob,            │
│    net cash, ROIC, red flags       liquidation, spin-off, biotech     │
│    → dcf_calculator, quality_      → models/merger_arb, liquidation,  │
│      scorer, narrative_checker       spinoff, biotech_cash (NEW)      │
│                                                                       │
│  A2.3 Business Analyst           A2.4 Risk Analyst                    │
│    sonnet-4-6, 8-12k tok           haiku-4-5, 3-6k tok                │
│    Moat, mgmt, bull/bear,          7-dim risk, sizing cap,            │
│    catalysts                       thesis-break, FX, max-DD           │
│    → insider_tracker, ownership_   → risk_heatmap, constraint_        │
│      analyzer, sector_health         checker, drift_detector,         │
│                                      correlation_matrix               │
│                                                                       │
│  A2.5 Web Researcher                                                  │
│    haiku-4-5, 4-8k tok                                                │
│    News, earnings calls, 13F, Horos/AV/Seeking-Alpha coverage,        │
│    regulatory/litigation                                              │
│    → Anthropic native web_search + scrapers/horos, alpha_vulture      │
└───────────────────────────────────────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ LAYER 4 — KNOWLEDGE BASE (file-based, git-tracked, schema-validated)    │
│                                                                         │
│  knowledge_base/                                                        │
│    schemas/          12 JSON Schema draft-07 contracts                  │
│    companies/        {ticker}/ fundamentals.json, thesis.md,            │
│                      analysis_history.json, decisions.json              │
│    portfolio/        current_positions.json, closed_positions.json,     │
│                      performance.json                                   │
│    universe/         watchlist.json, horos_positions.json,              │
│                      alpha_vulture_ideas.json, screener_results.json    │
│    learning/         successful_patterns.md, failed_patterns.md,        │
│                      market_regimes.json                                │
│                                                                         │
│  EXISTING STATE PRESERVED (validated by same schemas):                  │
│    portfolio/current.yaml, history.yaml                                 │
│    state/system.yaml, calendar.yaml, watchlist.yaml,                    │
│          standing_orders.yaml, pipeline_tracker.yaml,                   │
│          quality_universe.yaml, session_continuity.yaml                 │
│    thesis/active/{TICKER}/thesis.md (+ generated thesis.json)           │
│    learning/principles.md, decisions_log.yaml                           │
│    world/sectors/*.md                                                   │
└─────────────────────────────────────────────────────────────────────────┘
```

## Execution Flows

### Flow 1 — Weekly Screening (Sunday)

```
Governor (weekly trigger)
   │
   ├─► A1.1 Quant Screener  ─┐
   │                         ├─► consolidate → top-5 watchlist
   └─► A1.2 Special Sits    ─┘
           │
           ▼
   ┌──────────────────────────────────────┐
   │  For each top-5 ticker (sequential): │
   │     fanout parallel:                 │
   │       A2.1 Financial                 │
   │       A2.2 Special Sit (if flagged)  │
   │       A2.3 Business                  │
   │       A2.4 Risk                      │
   │       A2.5 Web Research              │
   │     → A3.1 Decision Maker            │
   └──────────────────────────────────────┘
           │
           ▼
   notifications/telegram.py (digest)
```

### Flow 2 — On-Demand Analysis

```
User CLI: python -m orchestrator on-demand TICKER
   │
   ▼
Governor
   │
   ▼
A2.1 + A2.2 + A2.3 + A2.4 + A2.5 (parallel fanout)
   │
   ▼
A3.1 Decision Maker
   │
   ▼
Write to knowledge_base/companies/{ticker}/analysis_history.json
```

### Flow 3 — Daily Monitoring (weekdays 18:00)

```
Governor (daily trigger)
   │
   ▼
A3.2 Portfolio Monitor (all active positions)
   │
   ├─► price vs thesis drift
   ├─► event timeline updates
   ├─► new SEC filings per ticker
   └─► flag for review if thesis change detected
           │
           ▼
   notifications/telegram.py (digest or alerts only if changed)
```

## Agent Specifications

### Layer 1

| Agent | Model | Tokens | Key Outputs | Reused Assets |
|-------|-------|--------|-------------|---------------|
| A1.1 Quant Screener | haiku-4-5 | 2-5k | `screener_result.json` (0-100 scores) | `dynamic_screener.py`, `batch_scorer.py`, `quality_universe.py`, `quality_scorer.py` |
| A1.2 Special Sits Screener (NEW) | haiku-4-5 | 5-10k | `special_situation[]` tagged MERGER_ARB/SPINOFF/LIQUIDATION/NET_CASH/ODD_LOT/CVR | `scrapers/sec_edgar_rss`, `scrapers/pr_newswire` |

### Layer 2

| Agent | Model | Tokens | Key Outputs | Reused Assets |
|-------|-------|--------|-------------|---------------|
| A2.1 Financial Analyst | sonnet-4-6 | 8-15k | DCF 3-scen, NAV, net cash, ROIC trend, red flags, MoS | `dcf_calculator.py`, `quality_scorer.py`, `narrative_checker.py`, `forward_return.py`; skills `valuation-methods`, `projection-framework`, `filing-analysis` |
| A2.2 Special Sit Modeler (NEW) | sonnet-4-6 | 6-12k | merger-arb model, liq value, spin-off stub, biotech CVR | `models/*.py` (NEW); skill `contrathesis-framework` |
| A2.3 Business Analyst | sonnet-4-6 | 8-12k | moat, management, bull/bear, catalysts | `insider_tracker.py`, `ownership_analyzer.py`, `sector_health.py`; skills `business-analysis-framework`, `skin-in-the-game`, `quality-compounders`, `sector-deep-dive` |
| A2.4 Risk Analyst | haiku-4-5 | 3-6k | 7-dim risk score, sizing cap, FX, max-DD | `risk_heatmap.py`, `constraint_checker.py`, `drift_detector.py`, `correlation_matrix.py` |
| A2.5 Web Researcher | haiku-4-5 | 4-8k | news, earnings calls, 13F, Horos/AV hits, regulatory | Anthropic `web_search`; `scrapers/horos`, `scrapers/alpha_vulture` |

### Layer 3

| Agent | Model | Tokens | Key Outputs | Reused Assets |
|-------|-------|--------|-------------|---------------|
| A3.1 Decision Maker | sonnet-4-6 | 6-10k | `decision.json` with BUY/SELL/SHORT/COVER/WATCH/PASS + size + stop + review trigger | `consistency_checker.py`, `portfolio_optimizer.py`; skills `investment-rules`, `pre-execution-check`, `recommendation-context` |
| A3.2 Portfolio Monitor | haiku-4-5 | 2-4k/day | P&L snapshot, drift alerts, event timeline | `portfolio_stats.py`, `thesis_monitor.py`, `earnings_intel.py`, `session_opener.py` |

## Decision Gates (A3.1)

A3.1 emits BUY only if **all** gates pass:

1. **Conviction gate** — structured conviction ≥ 6 (Tier A/B).
2. **Return gate** — MoS > 30% OR (E[CAGR]@market > 12% AND Tier A with thesis intact per Principle 14).
3. **Risk gate** — A2.4 risk score < 7.
4. **Consistency gate** — `consistency_checker.py` finds no precedent conflict.
5. **Sizing gate** — `portfolio_optimizer.py` confirms headroom per `portfolio-constraints`.

SELL gates: 6 gates from `exit-protocol` skill (thesis invalidated / KC triggered / rotation / diversification / target hit / FV reached).
SHORT gates: `short-thesis-framework` — catalyst-anchored with date.
COVER gates: 6 gates from `cover-protocol`.

## State Persistence

- `orchestrator/runs/{run_id}.json` — each Governor run.
- `orchestrator/audit.jsonl` — append-only event log.
- `knowledge_base/companies/{ticker}/analysis_history.json` — per-agent outputs on each deep-dive.
- `knowledge_base/companies/{ticker}/decisions.json` — all decisions + outcomes for that ticker.

## Scheduler Jobs (APScheduler)

| Job | Cron | Flow |
|-----|------|------|
| weekly_screening | Sun 09:00 local | Flow 1 |
| daily_monitoring | Mon-Fri 18:00 local | Flow 3 |
| horos_scraper | Mon 02:00 (monthly) | scrape horosam |
| alpha_vulture_scraper | Daily 02:15 | scrape AV |

## Observability

- `audit.jsonl` — every agent call (start/end/duration/tokens/cost).
- `orchestrator/runs/` — per-run full transcripts.
- Streamlit dashboard reads KB + audit logs for live views.
- Telegram digest summarises each Governor run.
