# PROMPT PARA CLAUDE CODE — ValueHunter v1.0

Pega esto directamente en Claude Code desde la raíz del repositorio.

---

## PROMPT

You are a senior Python architect. Your task is to design and scaffold a multi-agent investment analysis system called **ValueHunter** from scratch.

Before writing any code, create a detailed **PLAN.md** file that covers everything below. Do not implement anything yet — only plan.

---

## CONTEXT

ValueHunter is a multi-agent system that replicates and improves upon the investment methodology of **Horos Asset Management** (Spanish value investing fund, horosam.com) and **Alpha Vulture Capital Management** (special situations + small caps, alphavulture.com).

The system has 4 layers:

- **Layer 0 — Orchestrator**: Central meta-agent. Decides which agents to activate, manages parallel vs sequential execution, maintains global state.
- **Layer 1 — Screening** (2 agents, parallel): Quantitative screener (yfinance + EDGAR) + Special Situations screener (SEC RSS feeds).
- **Layer 2 — Deep Analysis** (5 agents, parallel): Financial analyst (DCF/NAV/net cash) + Special situation modeler (merger arb, liquidations) + Business analyst (qualitative/moat) + Risk analyst (sizing, max DD) + Web researcher (Anthropic web search).
- **Layer 3 — Portfolio** (2 agents, sequential): Decision maker (BUY/SELL/WATCH/PASS with structured JSON output) + Portfolio monitor (daily P&L, alerts, thesis tracking).
- **Layer 4 — Knowledge Base**: Persistent file-based storage in Markdown + JSON. Structured under /companies, /portfolio, /learning, /universe.

**First use case (Sprint 1 focus):** Automatically extract Horos Asset Management quarterly letters, parse their positions and investment theses, store them in the Knowledge Base, and use them as a high-quality screening input for the system.

---

## WHAT TO PLAN

### 1. Repository structure
Full directory tree with every file and folder. Include:
- `/agents/` — one file per agent
- `/orchestrator/` — main orchestrator logic
- `/knowledge_base/` — data storage with JSON schemas
- `/tools/` — shared utilities (data fetchers, parsers, formatters)
- `/flows/` — the 3 execution flows (weekly screening, on-demand analysis, daily monitoring)
- `/config/` — settings, API keys structure, universe definition
- `/tests/` — test structure
- `CLAUDE.md` — instructions for Claude Code on how to work in this repo

### 2. JSON schemas
Define the exact schema for every key data file:
- `companies/{ticker}/fundamentals.json`
- `companies/{ticker}/thesis.md` (template)
- `companies/{ticker}/decisions.json`
- `portfolio/current_positions.json`
- `portfolio/performance.json`
- `universe/watchlist.json`
- `universe/horos_positions.json` (extracted from Horos letters)

### 3. Agent specifications
For each of the 10 agents, define:
- Exact inputs and outputs (typed)
- Which external APIs or data sources it uses
- What it calls next (orchestration contract)
- Estimated token cost per run (cheap/medium/expensive)
- Whether it runs with claude-haiku-4-5 (cheap tasks) or claude-sonnet-4-6 (complex reasoning)

### 4. Horos scraper module
Plan the module that:
- Fetches Horos quarterly letters (PDF from horosam.com/cartas or equivalent)
- Parses positions, tickers, thesis summaries, and estimated upside
- Stores results in `knowledge_base/universe/horos_positions.json`
- Runs on a monthly schedule

### 5. Tech stack decisions
Justify choices for:
- Orchestration: LangGraph vs custom Python state machine
- Scheduling: APScheduler vs cron
- Data: yfinance + SEC EDGAR API (free tier limits?)
- Notifications: Telegram bot vs email
- Dashboard: Streamlit (for now)
- Testing: pytest structure

### 6. Sprint roadmap
Break the build into 4 sprints of ~2 weeks each:
- Sprint 1: Knowledge Base schemas + Horos scraper + Quantitative screener
- Sprint 2: Analysis agents (Financial + Business + Web researcher)
- Sprint 3: Special situations agents + Risk agent + Decision maker
- Sprint 4: Portfolio monitor + Dashboard + Scheduler + Notifications

For each sprint list exact deliverables and acceptance criteria.

### 7. CLAUDE.md content
Write the full CLAUDE.md file that will guide future Claude Code sessions in this repo. Include: project overview, architecture summary, coding conventions, how to run each flow, how to add a new agent, and which commands to use.

---

## OUTPUT

Create the following files:
1. `PLAN.md` — the complete plan (this is the main deliverable)
2. `CLAUDE.md` — Claude Code instructions for this repo
3. `knowledge_base/schemas/` — all JSON schema files (use JSON Schema draft-07)
4. `README.md` — project overview

Do not write any agent code yet. Focus entirely on making the plan complete, precise, and implementable. The plan should be detailed enough that any developer (or Claude Code in a future session) can implement each sprint without ambiguity.

When done, summarize in 10 bullet points what you planned and ask for confirmation before any implementation begins.
