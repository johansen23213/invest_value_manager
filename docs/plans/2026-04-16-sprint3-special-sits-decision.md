# Sprint 3 — Special Situations + Decision Maker Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build special-situation financial models, SEC/PR scrapers, 3 remaining agents (Quant Screener, Special Sits Screener, Special Sit Modeler, Decision Maker), and wire the weekly screening flow.

**Architecture:** Financial models are pure Python math (no AI). Screener agents use haiku for classification. Decision Maker uses sonnet to aggregate all Layer 2 outputs and apply gates. Weekly flow fans out screeners in parallel, selects top-5, runs full analysis, then Decision Maker.

**Working directory:** `/Volumes/Storage/Documents/Claude/value_hunter/invest_value_manager/`

---

## Task 1: Special Situation Financial Models

**Files:**
- Create: `models/__init__.py`
- Create: `models/merger_arb.py`
- Create: `models/liquidation.py`
- Create: `models/spinoff.py`
- Create: `models/biotech_cash.py`
- Create: `tests/test_models.py`

Pure Python math — no AI, no API calls.

**merger_arb.py**: `calculate_merger_arb(current_price, deal_price, expected_close_date, break_fee_pct=0, close_probability_pct=90) -> dict` returning spread_pct, annualized_spread_pct, expected_return_pct (probability-weighted), risk_reward_ratio, days_to_close.

**liquidation.py**: `calculate_liquidation_value(assets: dict[str, float], haircuts: dict[str, float], liabilities: float, shares: int) -> dict` returning gross_asset_value, total_haircuts, net_liquidation_value, per_share_value, upside_pct (vs current price input).

**spinoff.py**: `calculate_stub_value(parent_price, parent_shares, spinoff_value_per_parent_share, spinoff_ratio) -> dict` returning implied_stub_value, stub_pct_of_parent, parent_ex_spinoff_value.

**biotech_cash.py**: `calculate_cash_runway(net_cash, monthly_burn_rate, pipeline_value=0, cvr_value=0) -> dict` returning months_until_zero, total_value_per_share (net_cash + pipeline + cvr), margin_of_safety_pct.

Tests: parametrized with known inputs/outputs. Commit: `"feat: add special situation financial models (merger arb, liquidation, spinoff, biotech)"`

## Task 2: SEC EDGAR RSS + PR Newswire Scrapers

**Files:**
- Create: `scrapers/sec_edgar_rss.py`
- Create: `scrapers/pr_newswire.py`
- Create: `tests/test_sec_edgar.py`
- Create: `tests/fixtures/edgar_rss_sample.xml`

**sec_edgar_rss.py**: Fetches EDGAR full-text search for keywords (merger, acquisition, liquidation, spin-off, tender). Uses `https://efts.sec.gov/LATEST/search-index?q=KEYWORD&forms=8-K,SC+14D9&dateRange=custom`. Parses results, classifies by situation type. Class `EdgarRSSWatcher` with `search(keywords, forms, days_back)` returning list of dicts matching `special_situation.schema.json`.

**pr_newswire.py**: Searches PR Newswire RSS for corporate action keywords. Simpler than EDGAR. Class `PRNewswireWatcher` with `search(keywords, days_back)`.

Tests with XML fixture. Commit: `"feat: add SEC EDGAR and PR Newswire scrapers for special situation detection"`

## Task 3: Quant Screener Agent (A1.1)

**Files:**
- Create: `agents/a11_quant_screener.py`
- Create: `agents/prompts/a11_quant_screener.md`
- Create: `tests/test_a11_quant_screener.py`

Wraps existing tools: dynamic_screener.py, batch_scorer.py, quality_universe.py. Model: haiku-4-5. Output: `screener_result.schema.json` compliant dict with scored candidates.

Same agent pattern as Sprint 2 (gather tool data → Claude → JSON). Commit: `"feat: add Quantitative Screener agent (A1.1)"`

## Task 4: Special Situations Screener Agent (A1.2)

**Files:**
- Create: `agents/a12_special_sits_screener.py`
- Create: `agents/prompts/a12_special_sits_screener.md`
- Create: `tests/test_a12_special_sits_screener.py`

Uses scrapers/sec_edgar_rss.py and scrapers/pr_newswire.py instead of subprocess tools. Model: haiku-4-5. Output: list of `special_situation.schema.json` dicts tagged by type. Commit: `"feat: add Special Situations Screener agent (A1.2)"`

## Task 5: Special Situation Modeler Agent (A2.2)

**Files:**
- Create: `agents/a22_special_sit_modeler.py`
- Create: `agents/prompts/a22_special_sit_modeler.md`
- Create: `tests/test_a22_special_sit_modeler.py`

Uses models/*.py for calculations + sonnet for narrative synthesis. Model: sonnet-4-6. Determines situation type from input, runs the appropriate model, sends results to Claude for thesis generation. Commit: `"feat: add Special Situation Modeler agent (A2.2)"`

## Task 6: Decision Maker Agent (A3.1)

**Files:**
- Create: `agents/a31_decision_maker.py`
- Create: `agents/prompts/a31_decision_maker.md`
- Create: `tests/test_a31_decision_maker.py`

Aggregates Layer 2 agent outputs. Applies decision gates:
1. Conviction ≥ 6
2. MoS > 30% OR E[CAGR] > 12% (Tier A)
3. Risk score < 7
4. Consistency check (invokes consistency_checker.py)

Model: sonnet-4-6. Output: `decision.schema.json` compliant dict. Validates output against schema.

Tools: consistency_checker.py, portfolio_optimizer.py. Commit: `"feat: add Decision Maker agent (A3.1) with investment gates"`

## Task 7: Weekly Screening Flow

**Files:**
- Create: `orchestrator/flows/weekly_screening.py`
- Modify: `orchestrator/governor.py` — replace weekly stub
- Create: `tests/test_weekly_flow.py`

Flow: A1.1 + A1.2 parallel → merge candidates → top-5 by score → for each: on-demand analysis (4 agents) → Decision Maker → aggregate results.

Wire into Governor's `run_weekly()`. Commit: `"feat: wire weekly screening flow with dual screener + analysis + decision pipeline"`
