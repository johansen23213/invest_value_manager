# Dashboard v1 MVP — Design Spec

> **Date:** 2026-04-21
> **Author:** Joan Yanini + Claude Opus 4.7 (brainstorming) + Elena UX review
> **Status:** APPROVED — ready for implementation plan
> **Parent project:** ValueHunter v1.0 (invest_value_manager)
> **Sub-project:** 0.5 (interposed between Sub-project 1 Spanish Funds Ingestion DONE and Sub-project 2 Spanish Small Cap Screener)

---

## Purpose

Build a complete, functional, operational dashboard for day-to-day fund operation (Joan as daily operator) and external sharing with colleagues/investors (secondary audience). The dashboard surfaces the state of the ValueHunter system — portfolio positions, quality universe pipeline, Spanish value fund signals, and actionable alerts — in a single navigable web app.

## Goals

1. **Morning operator glance in under 30 seconds.** A home page that answers "what do I need to do today?" without clicks.
2. **Four core sections navigable via sidebar:** Glance (home), Portfolio, Pipeline & Universe, Spanish Funds.
3. **Shareable URL with authenticated access** — colleagues view the same state via whitelisted Google OAuth.
4. **Anonymization toggle** — `share_mode` replaces absolute € values with % when sharing externally, preventing leak of portfolio size or position sizing.
5. **Fast navigation post-first-load** — Streamlit cache with TTL keeps page transitions under 500ms after initial warm-up (~25s first load of the day).
6. **Unified UX validated by Elena** — every page passes Elena's UX review before merge (density, hierarchy, cognitive load, color semantics, affordance, shareability).
7. **Implementable in 3-5 days (~25h work)** — MVP, not Bloomberg clone.

## Non-goals (v1)

- Mobile-first or responsive-optimized layout (desktop-first; mobile works but not polished — documented limitation).
- Real-time data (<5 min freshness). Cache TTLs accept 5-60 min staleness by design.
- Editing capabilities. Dashboard is **read-only** — no triggering of trades, no writes to state files.
- Full historical performance reporting (Sharpe attribution, quality trajectory charts). Deferred to v2 Performance page (section 8 of full scope).
- Earnings calendar, news digest, alerts & digest history page. Deferred to v2 sections 5-7.
- Deep stock research page (per-ticker drill-down). Deferred.
- Complex auth flows (SAML, RBAC). Streamlit Cloud native Google OAuth whitelist is sufficient.
- Background cron refresh of state files. Staleness mitigated by manual `git push` after each session + user-triggered "Refresh data" button.

## Confirmed decisions

| # | Decision | Choice |
|---|----------|--------|
| D1 | Primary use case | Morning operator glance (Joan), colleagues secondary |
| D2 | MVP scope | 4 pages: Glance, Portfolio, Pipeline & Universe, Spanish Funds |
| D3 | Data refresh | `st.cache_data` with per-source TTL (5-60 min) + manual refresh button |
| D4 | Auth | Google OAuth whitelist via Streamlit Cloud |
| D5 | State sync Local → Remote | Manual `git commit` + `git push` (existing session workflow) |
| D6 | Stack | Streamlit 1.31+, Plotly for charts, pandas, pyyaml, yfinance |
| D7 | Deployment | Streamlit Cloud (`share.streamlit.io`), source = `sprint1/foundations` branch |
| D8 | Anonymization | `share_mode` session-state flag + `?share=1` URL param |
| D9 | Color contract | Unified COLOR constants in `components.py`, semantic (red=urgent, green=positive, amber=warning, blue=info, grey=inactive, gold=Tier A) |
| D10 | Glossary | Sidebar `st.expander` with ~10 terms always-available |
| D11 | UX validation | `elena-dashboard-ux` skill invoked per page before merge |

## Architecture

```
┌──────────────────────────────────────────────────────────────┐
│  Streamlit Cloud (share.streamlit.io)                        │
│  Source: github.com/johansen23213/invest_value_manager       │
│  Branch: sprint1/foundations                                 │
│  Auth: Google OAuth whitelist                                │
│  URL: https://valuehunter.streamlit.app/ (TBD during deploy) │
└──────────────────────────────┬───────────────────────────────┘
                               │ pip install + auto-deploy on push
                               ▼
┌──────────────────────────────────────────────────────────────┐
│  dashboard/app.py  (entry point, sidebar, share_mode)        │
│  └── Streamlit multi-page auto-detects dashboard/pages/      │
└──────────┬─────────┬─────────┬─────────┬─────────────────────┘
           ▼         ▼         ▼         ▼
    ┌─────────┐┌─────────┐┌─────────┐┌─────────────┐
    │pages/   ││pages/   ││pages/   ││pages/       │
    │1_Glance ││2_Portfo-││3_Pipe-  ││4_Spanish_   │
    │         ││lio      ││line     ││Funds        │
    └────┬────┘└────┬────┘└────┬────┘└──────┬──────┘
         │          │          │            │
         └──────────┴──────────┴────────────┘
                         │ all consume
                         ▼
        ┌─────────────────────────────────────┐
        │  dashboard/data_loader.py           │
        │  @st.cache_data(ttl=N) loaders      │
        │  - load_portfolio, load_prices,     │
        │  - load_universe, load_spanish_funds│
        │  - load_standing_orders,            │
        │  - load_calendar, load_macro,       │
        │  - compute_actions_today,           │
        │  - compute_multi_fund_signals       │
        └─────────────┬───────────────────────┘
                      │ reads (no writes)
                      ▼
        ┌─────────────────────────────────────┐
        │  Repo filesystem (read-only remote) │
        │  portfolio/, state/, thesis/,       │
        │  knowledge_base/spanish_funds/,     │
        │  world/, learning/                  │
        └─────────────────────────────────────┘
        ┌─────────────────────────────────────┐
        │  yfinance (external, cached 15 min) │
        └─────────────────────────────────────┘

Shared UI modules:
  dashboard/components.py  — COLOR constants, money()/pct() helpers,
                             reusable widgets (metric cards, pill, etc.)
```

**Design principle:** `data_loader.py` is the single source of truth for data access. Pages never touch filesystem or yfinance directly. `components.py` centralizes all styling decisions (color constants, share_mode-aware formatters) — pages contain layout logic only.

## File structure

```
dashboard/
├── __init__.py
├── app.py                    # entry point, sidebar, share_mode wiring
├── data_loader.py            # cached loaders + compute helpers
├── components.py             # COLOR contract, formatters, reusable widgets
├── requirements.txt          # dashboard-specific pip deps for Streamlit Cloud
├── README.md                 # setup local + deploy + auth notes
└── pages/
    ├── 1_🏠_Glance.py
    ├── 2_📊_Portfolio.py
    ├── 3_🎯_Pipeline.py
    └── 4_🇪🇸_Spanish_Funds.py

tests/
├── test_dashboard_data_loader.py    # mocked filesystem + yfinance
├── test_dashboard_components.py     # money(), pct(), share_mode, COLOR
└── fixtures/dashboard/              # sample portfolio.yaml, universe.yaml, etc.

docs/
└── dashboard_screenshots/           # one PNG per page for documentation
```

## Pages

### 🏠 1_Glance.py — Home (morning operator glance)

**Question answered:** "What do I need to do today?"

**Layout:**

```
┌─────────────────────────────────────────────────────────────┐
│ Portfolio €10.5k | P&L +1.4% | Cash 55% | Pos 11 | Sharpe … │  ← hide € in share_mode
└─────────────────────────────────────────────────────────────┘
┌──────────────────┬──────────────────┬──────────────────────┐
│ 🔴 TRIGGERED SO  │ 📅 EARNINGS 7D   │ ⚠️ MACRO (updated Nh) │
│ Mechanical sig   │ Framework status │ + interpretation     │
│ • ALFA.L 159p    │ • MEGP.L 2026-04 │ • VIX 19 ↓ constructve│
│ [+5 near expand] │ [+3 expand]      │ • Oil $87 ↓ energy dr│
└──────────────────┴──────────────────┴──────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│ 🎯 TOP ACTIONS DEL DÍA (narrative why-today, not dup of SO) │
│ 1. [ALTA] ALFA.L DEPLOY — Hormuz gates cleared              │
│ 2. [ALTA] MEGP.L results Apr 24 — prep framework            │
│ 3. [MEDIA] Refresh 8 stale sector views                     │
└─────────────────────────────────────────────────────────────┘
┌──────────────────────────┬──────────────────────────────────┐
│ 🔴 KILL CONDITIONS       │ ⏳ PENDING EVENTS                │
│ (threshold proximity)    │ (binary outcome)                 │
│ • GL KC#4 — 30% thresh   │ • ADBE successor announcement    │
└──────────────────────────┴──────────────────────────────────┘

Last update: 2 min ago  |  source: state/*.yaml + yfinance
```

**Data sources:** `load_standing_orders()`, `load_calendar(days=7)`, `load_macro()`, `compute_actions_today()`, `load_portfolio()` for header stats.

**Elena-incorporated fixes:**
- Sharpe metric in header: compute from `effectiveness_tracker.py` or remove (no `?` placeholder).
- SO panel vs TOP ACTIONS differentiated: SOs = mechanical signal, ACTIONS = narrative why-today context.
- Macro panel has interpretation appended (`↓ constructive`, `↑ energy drag`).
- `(+5 near)` and `(+3)` overflow become explicit `st.expander` elements.
- Kill conditions split: threshold proximity vs pending events (two panels).
- Macro freshness inline (`updated Nh ago` in panel header).

### 📊 2_Portfolio.py — Portfolio state

**Question answered:** "How is the portfolio doing?"

**Layout:**

- Metrics row: total value (€ or "—" in share_mode), P&L %, cash %, net exposure, gross exposure, positions count
- Primary table (7 columns, always visible): `ticker | name | tier | weight% | P&L | E[CAGR] | status`
- Secondary columns (toggle "Show details"): `entry | current | MoS | FV`
- Column tooltips: every internal-jargon header has `help` param (QS, MoS, FV, E[CAGR], tier)
- Row expand → mini-thesis (2-3 lines) + last review date with recency color (green <30d, yellow 30-60d, red >60d)
- Charts: allocation by sector (donut) + by geo (bars) side-by-side, colors from `COLOR` contract
- Shorts table: shown as placeholder with explicit empty state message ("No short positions. System opens shorts when identifying overvalued/fragile companies.")
- Footer: `st.expander("Data sources")` (collapsed) with file paths

**Data sources:** `load_portfolio()`, `load_prices(tuple(tickers))`.

**Elena-incorporated fixes:**
- 11 cols → 7 primary + 4 secondary toggle.
- Jargon tooltips mandatory on QS/MoS/FV/E[CAGR]/tier.
- `action` column renamed to `status`, styled as read-only pill (not button).
- "last review date" with relative age + recency color.
- Shorts empty state message (not blank).
- Filters: `st.selectbox` tier + sector above table + "Reset filters" button.

### 🎯 3_Pipeline.py — Pipeline & Universe

**Question answered:** "What's ready to act on, what's in the funnel?"

**Layout:**

- Metrics row: universe size (exact), tier A count, actionable count, R1_COMPLETE/total fraction, R4_READY count, velocity last session (colored: green ≥3, yellow 1-2, red 0)
- Plotly `go.Funnel` horizontal: Universe → R1_NEW → R1_COMPLETE → R2 → R3 → R4_READY → ACTIVE. Counts inside bars, conversion % between steps. Colors from `PIPELINE_COLORS`.
- `st.expander("What is the pipeline?")` collapsed by default with 3-sentence explanation for colleagues.
- Primary table (7 cols): `ticker | name | tier | pipeline_status | distance_to_entry | E[CAGR] | conviction_signal`
- Secondary columns (toggle): `QS | sector | fund_overlap`
- `conviction_signal` pill with tooltip showing fund names + weights on hover (replaces standalone `fund_overlap` column).
- `distance_to_entry` color-coded: green ≤0 (at entry), yellow 1-15%, grey >15%. Tooltip with sign convention.
- Filters: tier (A/B/C/All), sector, distance range. "Reset filters" button.
- Sidebar "jump to ticker" input filters table rows matching substring in any column.

**Data sources:** `load_universe()`, `load_spanish_funds()` (for fund overlap enrichment), `compute_multi_fund_signals()`.

**Elena-incorporated fixes:**
- 10 cols → 7 primary + 3 secondary (drop redundant `fund_overlap` standalone, merge into conviction pill tooltip).
- Metrics expressed as fractions (`R1_COMPLETE: 23/200 (12%)`) not absolutes.
- Plotly `go.Funnel` explicit, not "visual funnel."
- Color contract applied to pipeline stages (consistent between funnel and table pills).
- Reset filters button.
- `distance_to_entry` sign convention documented in tooltip.

### 🇪🇸 4_Spanish_Funds.py — Spanish Value Funds

**Question answered:** "What are Spanish value fund managers buying?"

**Layout:**

- Fund cards grid (5): Cobas, AzValor, Magallanes, Horos, Valentum. Each card shows:
  - Fund name, last processed quarter with recency badge (green <30d, yellow 30-60d, red >60d)
  - AuM (EUR) with label
  - Quarter return %
  - `#positions (vs prev quarter: ±N)` with relative change
  - "View letter" link (target=\_blank, with last-verified date)
- **🔔 Multi-fund signals section (HERO, placed BEFORE per-fund tabs per Elena):**
  - Tickers in ≥2 funds. Expand to see thesis side-by-side in fixed-height containers (3-line cap + "read more").
  - Fund names visible next to each ticker in diff view.
- Per-fund detail: `st.tabs` (not dropdown) with 5 tabs.
  - Each tab: holdings table with `company | ticker | weight | fund view | thesis snippet` (renamed `action` → `fund view` to avoid affordance confusion).
- Historical comparison: dropdown of quarters → "new/exited" diff with fund names attached (e.g. `NEW: ALBA.MC (Cobas + AzValor)`, `EXITED: BRK.B (Magallanes)`).
- Footer: Unverified tickers list + link to raw JSON.
- Top-of-page metric: "Total unique companies across all 5 funds: N"

**Data sources:** `load_spanish_funds()`, `compute_multi_fund_signals()`.

**Elena-incorporated fixes:**
- Multi-fund signals moved BEFORE per-fund tabs (hero first).
- `st.tabs` (not picker) for 5 funds at 14-16" viewport.
- Thesis snippets in fixed-height containers with "read more" expand.
- Fund names attached to new/exited diff entries.
- AuM labeled with currency.
- Last-processed recency badge on each fund card.
- `#positions` with relative change vs prev quarter.
- `action` column renamed `fund view` for affordance clarity.
- Top-level "total unique companies" metric.

## Data flow + caching

`data_loader.py` exposes cached loaders. TTLs per source:

| Loader | TTL | Rationale |
|--------|-----|-----------|
| `load_standing_orders()` | 5 min | First thing Joan checks; aggressive |
| `load_prices(tickers)` | 15 min | yfinance rate, acceptable freshness |
| `load_portfolio()` | 15 min | Synced to price refresh |
| `load_universe()` | 15 min | Universe + price enrichment |
| `load_spanish_funds()` | 15 min | Quarterly data but may update |
| `load_calendar(days)` | 15 min | Earnings dates stable |
| `load_macro()` | 1 h | VIX/oil don't move that fast |
| `compute_actions_today()` | 30 min | Derived; heavy compute |
| `compute_multi_fund_signals()` | 1 h | Quarterly changes |

Manual "Refresh data" button in sidebar invalidates all caches via `st.cache_data.clear()`.

**First load performance target:** ≤ 25s cold cache. ≤ 500ms page navigation post-warm. Refresh button ≤ 10s.

## Shared components (`components.py`)

### `share_mode` wiring

- Single session-state flag: `st.session_state.share_mode: bool`, default `False`.
- URL param `?share=1` sets it on mount.
- Sidebar toggle "Share mode (hide €)" bound to same flag.
- Pages read `st.session_state.share_mode` and pass to `money()` helper.

### Formatters

```python
def money(value: float, share_mode: bool) -> str:
    if share_mode:
        return "—"
    return f"€{value:,.0f}"

def pct_of_portfolio(value: float, total: float) -> str:
    return f"{value/total*100:.1f}%"

def pct(value: float) -> str:
    return f"{value:+.1f}%"
```

### Color contract (constants)

```python
COLOR = {
    "urgent_red":    "#E34B4B",
    "positive_green":"#3FA34D",
    "warning_amber": "#F5A623",
    "info_blue":     "#3B82F6",
    "neutral_grey":  "#9CA3AF",
    "tier_a_gold":   "#D4AF37",
    "muted":         "#6B7280",
}

PIPELINE_COLORS = {
    "R1_NEW":      COLOR["neutral_grey"],
    "R1_COMPLETE": "#93C5FD",
    "R2":          COLOR["info_blue"],
    "R3":          "#1D4ED8",
    "R4_READY":    COLOR["positive_green"],
    "ACTIVE":      COLOR["tier_a_gold"],
    "ARCHIVED":    COLOR["muted"],
}

CONVICTION_COLORS = {
    "1_fund":   COLOR["neutral_grey"],
    "2_funds":  COLOR["info_blue"],
    "3+_funds": COLOR["positive_green"],
}

TIER_COLORS = {
    "A": COLOR["tier_a_gold"],
    "B": COLOR["info_blue"],
    "C": COLOR["neutral_grey"],
}
```

All charts, pills, indicators use these constants. No color literals in pages.

### Sidebar structure (global, all pages)

- Page selector (auto from multi-page)
- **⚙️ Settings:** share mode toggle, Refresh data button, Last update timestamp
- **📖 Glossary (expander, collapsed by default):** QS, MoS, FV, E[CAGR], Tier A/B/C, R1-R4 Pipeline, KC, SO, Conviction — each with 1-sentence plain-language definition
- Footer: "This dashboard is optimized for desktop (≥14")" — soft mobile caption

### Empty + loading states

- Loader returns empty → `st.info("No [X] available. [1-line explanation]")`.
- Loader raises → `st.error("Could not load [X]: <truncated>")` + Retry button.
- Initial load: `st.spinner("Loading dashboard (first visit ~25s)...")` explicit.

## Rollout plan

**Total estimated: ~25h over 3-5 days.**

| Phase | Scope | Duration |
|-------|-------|----------|
| 1 | Foundation: `data_loader.py` + `components.py` + tests | 4h |
| 2 | Sidebar + navigation + share_mode wiring | 2h |
| 3 | Glance page + Elena review + iterate | 4h |
| 4 | Portfolio page + Elena review + iterate | 4h |
| 5 | Pipeline page + Elena review + iterate | 4h |
| 6 | Spanish Funds page + Elena review + iterate | 4h |
| 7 | Streamlit Cloud deploy + OAuth whitelist + smoke test | 2h |
| 8 | README + screenshots + handoff to colleagues | 1h |

Each page phase (3-6) ends with invocation of `elena-dashboard-ux` skill. Must achieve APPROVED or APPROVED_WITH_CHANGES+fixes applied before phase advances. NEEDS_REDESIGN → restart phase.

## Testing strategy

### Unit tests (automated, CI-ready)

- `test_dashboard_data_loader.py` — mocked filesystem fixtures, each loader returns expected schema shape
- `test_dashboard_components.py` — `money()` in both share_mode states, `pct_of_portfolio()` math, `COLOR` values valid hex
- `test_share_mode.py` — session_state toggle + URL param `?share=1` activates correctly

### Integration (manual smoke checklist)

- Open each page in localhost → no errors, no empty warnings
- Toggle share_mode ON → verify zero `€` occurrences in rendered output across all pages
- Click expand rows on Portfolio → expand works, mini-thesis shows
- Filter Pipeline by tier A → table filters, count updates in metrics
- Change fund tab on Spanish Funds → holdings update
- Hit "Refresh data" → all caches invalidated, recomputes visible

### Elena UX review (gate per page)

Before merge of any page to `sprint1/foundations`:
- Invoke `elena-dashboard-ux` skill with screenshot + description of current state
- Require APPROVED or APPROVED_WITH_CHANGES with listed fixes applied
- NEEDS_REDESIGN blocks merge → phase restart

### Performance benchmarks

- First load (cold cache): ≤ 25s
- Page navigation (warm cache): ≤ 500ms
- Manual refresh: ≤ 10s

## Deployment

1. Streamlit Cloud account under Joan's email.
2. Connect GitHub repo `github.com/johansen23213/invest_value_manager`, branch `sprint1/foundations`.
3. Main file: `dashboard/app.py`.
4. Python version: 3.12.
5. `dashboard/requirements.txt` lists: streamlit, pandas, plotly, pyyaml, yfinance.
6. Secrets (if any): `ANTHROPIC_API_KEY` via Streamlit Cloud secrets panel (only if a loader calls Claude; v1 does not).
7. Auth: "Restrict access" mode → whitelist emails (start with Joan, add colleagues iteratively).
8. Deploy → verify URL accessible, run integration smoke checklist.
9. Share URL + access instructions with colleagues.

## Known limitations (documented in README)

1. **Data staleness up to 24h** if Joan doesn't commit + push state changes. Mitigated by visible "Last update" timestamp + manual refresh button.
2. **Mobile not optimized** — layout degrades gracefully but tables require horizontal scroll; caption warns users.
3. **Streamlit Cloud free tier RAM = 1 GB** — if universe grows beyond ~500 companies or if many pages load simultaneously, may hit limits. Migration path: Streamlit paid tier or self-host.
4. **OAuth whitelist is manual** — Joan adds/removes colleague emails via Streamlit Cloud UI. No self-service.
5. **No E2E tests** — Streamlit testing ecosystem is limited. Manual smoke + Elena review cover this gap.
6. **Real-time yfinance prices cached 15 min** — dashboard is not suitable for pre-trade execution decisions; use `price_checker.py` locally for live prices.

## Open questions deferred to implementation plan

- Exact Plotly chart styling (donut thickness, bar height) — to be finalized in component implementation.
- Whether the share_mode URL param should be permanent (token in URL) or session-scoped — discuss during phase 2.
- Streamlit Cloud free tier build time limits (may require dropping some heavy loaders) — confirmed during phase 7 deploy.
- Whether to add a basic "dark mode" toggle — deferred unless Elena flags it in a post-deploy review.

---

*Spec prepared via `superpowers:brainstorming` skill with Elena UX validation. Next step: `superpowers:writing-plans` for implementation plan.*
