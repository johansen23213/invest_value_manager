# Scalability Policy

> Created: 2026-02-14 (Session 71 refactoring)
> Purpose: Rules that keep the system lean as it grows over 12+ months.

---

## 1. File Size Budgets

### Auto-Loaded Files (Capa 1) — Budget: <40 KB total

These files are injected every session. Every byte costs context on every interaction.

| File | Budget | Current | Action if exceeded |
|------|--------|---------|--------------------|
| `CLAUDE.md` | <8 KB | 6.5 KB | Move detail to skills, keep index only |
| `.claude/rules/*.md` (6 files) | <20 KB total | 19.2 KB | Archive old content, compact |
| `MEMORY.md` | <8 KB | 6.9 KB | Truncated to 200 lines by system |
| **Total Capa 1** | **<40 KB** | **32.8 KB** | |

### State Files — Budget: <30 KB total

| File | Budget | Current | Rotation policy |
|------|--------|---------|--------------------|
| `state/system.yaml` | <5 KB | 2.6 KB | Slim core, no growth expected |
| `state/calendar.yaml` | <8 KB | 5.2 KB | Archive past events to calendar_archive.yaml |
| `state/standing_orders.yaml` | <6 KB | 4.1 KB | Remove filled/cancelled orders quarterly |
| `state/watchlist.yaml` | <8 KB | 4.6 KB | Archive to_analyze items after 90 days |
| `state/pipeline_tracker.yaml` | <5 KB | 2.7 KB | Trim evolution_tracking to last 10 entries |

### Growth-Prone Files — Rotation Required

| File | Rotation trigger | Action |
|------|-----------------|--------|
| `learning/decisions_log.yaml` | >50 entries | Move oldest to `learning/archive/decisions_log_YYYY.yaml` |
| `state/calendar.yaml` | Events >30 days past | Move to `state/calendar_archive.yaml` |
| `portfolio/history.yaml` | >20 closed positions | Archive oldest to `portfolio/archive/` |
| `world/sectors/*.md` | >300 lines | Move history to `world/sectors/archive/` |
| Session history memory | >100 sessions | Summarize decades, keep last 20 detailed |

---

## 2. Architecture Principles

### 2.1 Auto-loaded = Index, Not Encyclopedia
CLAUDE.md and rules files should say WHAT to do and WHERE to find HOW. Skills contain the HOW.

### 2.2 One Truth, One Place
Never duplicate content between auto-loaded files and skills. Reference, don't copy.

### 2.3 Growing Files Must Have Rotation
Any file that grows over time (logs, calendars, decisions) MUST have a defined rotation policy.

### 2.4 State Split Architecture
`state/system.yaml` is slim core metadata only. Domain-specific state lives in dedicated files:
- Calendar events: `state/calendar.yaml`
- Standing orders: `state/standing_orders.yaml`
- Watchlist: `state/watchlist.yaml`
- Pipeline tracking: `state/pipeline_tracker.yaml`

### 2.5 On-Demand Over Pre-Loading
Skills, thesis files, sector views, and detailed protocols are read on-demand by agents. They are NOT loaded into every session's context.

---

## 3. Maintenance Cadence

| Check | Frequency | Tool/Method |
|-------|-----------|-------------|
| Capa 1 total size | Every health-check (14 days) | `wc -c` on auto-loaded files |
| State files total | Every health-check | `wc -c` on state/*.yaml |
| Calendar rotation | Monthly | Move past events to archive |
| Decisions log rotation | When >50 entries | Archive oldest year |
| Standing orders cleanup | Quarterly | Remove FILLED/CANCELLED |
| MEMORY.md review | Monthly | Prune stale entries |

---

## 4. Refactoring Results (2026-02-14)

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Capa 1 (auto-loaded) | ~110 KB / ~28K tokens | ~33 KB / ~8.4K tokens | **-70%** |
| CLAUDE.md | 470 lines / 19 KB | 145 lines / 6.5 KB | **-66%** |
| session-protocol.md | 703 lines / 23 KB | 71 lines / 2.3 KB | **-90%** |
| error-patterns.md | 337 lines / 24 KB | 42 lines / 2.3 KB | **-90%** |
| tools-reference.md | 287 lines / 16 KB | 47 lines / 2.8 KB | **-83%** |
| agent-protocol.md | 203 lines / 9 KB | 77 lines / 2.2 KB | **-74%** |
| meta-reflection.md | 231 lines / 6 KB | 22 lines / 0.9 KB | **-85%** |
| state/system.yaml | 1,492 lines / 84 KB | 59 lines / 2.6 KB (core) | **-97%** (split into 5 files) |
| State files total | 84 KB (monolithic) | 19.3 KB (5 split files) | **-77%** |

### What Was Preserved
- All functionality intact — skills contain full protocols
- All agents updated to reference correct split files
- Session-start hook reads from split files
- YAML validation passes on all state files

### Files Modified (28 total)
- 11 agent definitions
- 8 skill files
- 1 rule file (file-structure.md)
- 1 hook (session-start.sh)
- 1 state file fix (pipeline_tracker.yaml)
- 6 auto-loaded files (CLAUDE.md, 5 rules)
