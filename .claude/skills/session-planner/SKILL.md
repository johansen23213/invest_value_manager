# Session Planner — Dynamic Session Plan Mode

> Auto-activar al inicio de sesion en modo DASHBOARD o WAVE.
> Genera plan de trabajo priorizado basado en estado actual del sistema.
> El CIO llega, evalua, prioriza, presenta, y tras aprobacion, ejecuta.

---

## Cuando se Activa

| Senal del humano | Accion |
|------------------|--------|
| Saludo generico, "trabaja", "wave", "sesion", "autonomo" | **AUTO** — generar plan, presentar, esperar aprobacion |
| "planifica la sesion" o similar | **MANUAL** — generar plan |
| Instruccion directa ("analiza X", "compra Y") | **NO SE ACTIVA** — modo DIRECTO prevalece (plan como contexto mental) |

---

## Inputs Dinamicos (9 fuentes + 3 tools)

### Fuentes de Estado (leer)

| Fuente | Que extraer |
|--------|-------------|
| `state/calendar.yaml` | Earnings proximos 7d, catalysts, deadlines |
| `state/pipeline_tracker.yaml` | Pipelines OVERDUE y DUE TODAY |
| `state/standing_orders.yaml` | SOs near trigger (<10% distancia) |
| `state/watchlist.yaml` | Price alerts, short candidates |
| `state/system.yaml` | Market regime, last session summary, strategic direction |
| `portfolio/current.yaml` | Positions on probation, pending reviews, conviction levels |
| `state/quality_universe.yaml` | SCORED count, stale count, pipeline funnel |
| `state/session_continuity.yaml` | Prior session work, dedup signals, R1 cooldowns, handoff |

### Tools Rapidos (ejecutar)

| Tool | Que extraer |
|------|-------------|
| `python3 tools/forward_return.py --active-only` | Bottom 3 posiciones, rotation candidates, E[CAGR] column |
| `python3 tools/forward_return.py --pipeline-only --deployment-ready` | Pipeline candidates viable for deployment at current prices |
| `python3 tools/sector_health.py freshness --stale-only` | Sectores stale con dependencias de portfolio |
| `python3 tools/r1_prioritizer.py --top 5` | Top R1 candidates (with FANTASY-RISK flags + fantasy rate) |
| `python3 tools/r1_prioritizer.py --advancement` | R1_COMPLETE advancement: 3 sections (Ready/Approaching/Parked) + E[CAGR]@mkt |
| `python3 tools/quality_universe.py approaching` | Pipeline entries moving toward entry since last refresh |

---

## Logica de Priorizacion (8 niveles)

| P# | Condicion | Bloque | Ejemplo |
|----|-----------|--------|---------|
| P0 | Kill condition / CRITICAL news alert | URGENTE | Fraude detectado en posicion |
| P1 | Earnings <7d sin framework (posicion activa) | URGENTE | MONY.L FY results Monday |
| P2 | SO triggered o near (<5%) | URGENTE | RACE.MI at 5.3% de entry |
| P3 | Cash >25% + candidatos actionable en pipeline | PRIORIDAD NORMAL | 60% cash + 3 near-entry |
| P4 | R1 processing (obligatorio 3-5/sesion — L-08) | PRIORIDAD NORMAL | Top 5 de r1_prioritizer |
| P5 | Pipelines OVERDUE | PRIORIDAD NORMAL | risk-review 3d overdue |
| P6 | Rotation: bottom 3 con alternativa superior | PRIORIDAD NORMAL | BYIT.L bottom + IHP.L ready |
| P7 | Sector stale con portfolio deps | PRIORIDAD NORMAL | telecom.md 45d old, DTE.DE dep |
| P8 | System maintenance, universe expansion, health check | MANTENIMIENTO | batch_scorer new index |

**Reglas de clasificacion:**
- P0-P2 → bloque URGENTE (hacer PRIMERO, antes de cualquier wave)
- P3-P7 → bloque PRIORIDAD NORMAL (bulk del trabajo de la sesion)
- P8 → bloque MANTENIMIENTO (si queda contexto)
- P8e → Evolution micro-step (SIEMPRE al final — Fase 6)
- R1 processing (P4) SIEMPRE aparece — es obligatorio cada sesion
- Net exposure reasoning SIEMPRE aparece — es obligatorio cada sesion (P13)

---

## Dedup Logic (via `state/session_continuity.yaml`)

### Same-Day Dedup
Read `session_continuity.yaml` → `session.date` and `skip_if_same_day`:
- Si `session.date == today` Y `vigilance_fresh_until > now` → **SKIP vigilancia**. Mostrar: "News fresh from S[N]. Skipping."
- Si `so_fresh_until > now` → **SKIP SO price check**. Mostrar cached `nearest`.
- Si `rotation_done_today == true` → **SKIP rotation check**. Mostrar: "Rotation done S[N]."

### R1 Dedup
- `r1_prioritizer.py --top 10` already filters cooldowns (reads `session_continuity.yaml` → `r1_cooldowns`)
- Cross-check output vs `completed.r1_completed` to avoid same-session re-analysis

### Handoff
- Incorporate `next_priorities` from previous session as context for P3-P7 classification
- If previous session flagged an evolution proposal with `Apply: NOW`, include as P8e item

---

## Template del Plan

```markdown
## SESSION PLAN — Sesion [N] | [Fecha]

### ESTADO RAPIDO
- Portfolio: [N] posiciones, EUR [X] invested, cash [Y]%
- Market Regime: [Opportunity/Fair-Value/Defensive] — [razonamiento 1 linea]
- P&L: [+/-X.X]%
- Probation: [tickers o "ninguno"]
- Pipeline: [N] SCORED sin R1, [N] near-entry, [N] deployment-ready (E[CAGR]>=threshold)
- Fantasy rate: [X]% ([N]/[M] R1s → OVERVALUED/FANTASY)
- Advancement: Section A [N] ready, [N] approaching

### URGENTE (hacer PRIMERO)
1. [P#] [Descripcion] — agentes: [lista] — ~[X]m
2. ...
(Si no hay items urgentes: "Sin urgencias detectadas.")

### PRIORIDAD NORMAL
1. [P#] [Descripcion] — agentes: [lista] — ~[X]m
2. [P4] R1 Processing: [N] candidatos ([tickers]) — fundamental-analyst x[N] paralelo — ~[X]m
3. [P13] Net Exposure Reasoning — macro_fragility + razonamiento — ~5m
...

### MANTENIMIENTO (si queda contexto)
1. [P8] [Descripcion] — ~[X]m
2. [P8e] Evolution micro-step (Fase 6) — ~5m
(Si no hay items: "Sistema saludable.")

### DEDUP APLICADO
- Vigilancia: [FRESH S{N} / DUE]
- SOs: [FRESH S{N} / DUE]
- Rotation: [DONE S{N} / DUE]
- R1 cooldowns: [N] filtered ([tickers])
- Handoff S{N}: [resumen de next_priorities]

### SECUENCIACION
- Wave 1: [items paralelos] — ~[X]m
- Wave 2: [items paralelos, post-Wave-1] — ~[X]m
- Wave 3: [items paralelos, post-Wave-2] — ~[X]m
Total estimado: ~[X]m
```

---

## Restricciones del Plan

1. **Max 4-5 heavy opus agents en paralelo** por wave (7 causa context overflow)
2. **Max 2 yfinance agents simultaneos** (rate limiting)
3. **R1 minimum 3 velocity units/sesion** (L-08) — SIEMPRE en el plan
4. **Net exposure reasoning** obligatorio (P13) — SIEMPRE en el plan
5. **Earnings prep antes de R1** — si hay earnings <7d, va en URGENTE antes de R1 wave
6. **Tools rapidos primero** — los 4 tools de input se ejecutan ANTES de generar el plan
7. **Tiempo realista** — no prometer mas de lo que cabe en contexto (~3-4 waves max)
8. **ANTI-FANTASY PROTOCOL (S105, tooling-enforced S106):**
   - Run `--advancement` FIRST: shows 3 sections (Ready/Approaching/Parked) with E[CAGR]@market
   - If Section A non-empty → prioritize R2→R3 (2 units each)
   - If 0 in Section A → new R1s, but use `--exclude-fantasy-risk` or `--pre-flight` to filter
   - `--pre-flight` shows ONLY candidates with E[CAGR]-at-entry >= threshold (12% Tier A, 15% Tier B)
   - `--exclude-fantasy-risk` filters out companies priced >150% of FV (guaranteed FANTASY R1)
   - **Fantasy rate** now auto-computed in footer. If >50% → system alarm with suggestions
   - R1 candidates MUST be on eToro (check ETORO_UNAVAILABLE in r1_prioritizer.py)
   - Use `quality_universe.py approaching` to catch stocks dropping toward entry between sessions
9. **EARNINGS AUTO-PREP GATE (S105):**
   - For ANY position with earnings <7 days: verify framework exists AND freshness <14 days
   - If framework missing → P1 URGENTE
   - If framework >14 days old → P1 refresh required before earnings

---

## Flujo de Ejecucion

```
1. Leer 7 fuentes de estado (archivos)
2. Ejecutar 3 tools rapidos (forward_return, sector_health, r1_prioritizer)
3. Clasificar items por P0-P8
4. Generar plan con template
5. Presentar plan al humano (plan mode)
6. Humano aprueba / ajusta
7. Ejecutar waves secuencialmente
```

### En Modo DIRECTO

Si el humano da instruccion directa, NO entrar en plan mode formal. Pero:
- Generar plan mental como contexto interno (que mas hay pendiente?)
- Ejecutar la instruccion directa como Wave 1
- Si queda contexto tras la instruccion, proponer siguiente accion basada en prioridades

---

## NO Hacer

- NO presentar el plan como menu de opciones — es MI recomendacion de trabajo
- NO esperar aprobacion item por item — el plan se aprueba en bloque
- NO incluir mas de 3-4 waves — ser realista con el contexto disponible
- NO ejecutar antes de aprobacion (excepto modo DIRECTO)
- NO incluir items que requieren confirmacion del humano como "trabajo autonomo" — earnings prep si, BUY execution no
