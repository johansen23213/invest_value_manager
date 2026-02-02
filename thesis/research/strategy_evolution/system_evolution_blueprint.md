# System Evolution Blueprint: Short Selling Support

**Date**: 2026-02-02
**Version**: 1.0
**Status**: DRAFT - Pending approval
**Purpose**: Technical system design for adding short selling (CFD) capability to Value Investor System v2.1.0

---

## 1. Current System Architecture Summary

### Inventory
| Component | Count | Location |
|-----------|-------|----------|
| Agents | 19 | `.claude/agents/{investment,portfolio,research,system}/` |
| Skills | 11 directories | `.claude/skills/` |
| Tools | 5 Python scripts | `tools/` |
| Active positions | 13 longs | `portfolio/current.yaml` |
| Watchlist entries | ~25 | `state/system.yaml` |

### Agent Breakdown
**Investment (4+3 micro)**: fundamental-analyst, investment-committee, review-agent, valuation-specialist, moat-assessor, risk-identifier
**Portfolio (5)**: performance-tracker, portfolio-ops, position-calculator, rebalancer, watchlist-manager
**Research (2)**: macro-analyst, sector-screener
**System (6)**: calendar-manager, file-system-manager, health-check, memory-manager, quant-tools-dev, system-evolver

### Current Flow (Longs Only)
```
sector-screener → fundamental-analyst → investment-committee → USER CONFIRMS → portfolio-ops
                                                                                    ↓
review-agent ← rebalancer ← performance-tracker ← watchlist-manager ← MONITOR LOOP
```

### What Breaks for Shorts
1. **fundamental-analyst**: only evaluates UNDERVALUATION (MoS >25%). No framework for overvaluation.
2. **investment-committee**: gate checks MoS >25%, moat, thesis. For shorts, criteria are inverted: overvaluation, broken moat, structural decline.
3. **review-agent**: "good earnings = hold" logic. For shorts, good earnings = danger, bad earnings = profit.
4. **portfolio/current.yaml**: no `shorts` section. Only tracks long positions.
5. **portfolio_stats.py**: calculates long-only metrics. No net/gross exposure.
6. **dynamic_screener.py**: filters for LOW P/E, HIGH yield (value). Shorts need HIGH P/E, NEGATIVE FCF, DECLINING revenue.
7. **portfolio-constraints skill**: no max short exposure, no net exposure limits.
8. **investment-rules skill**: no short-specific buy/sell criteria, no stop-loss rules.
9. **rebalancer**: no logic for short position profit-taking or stop-loss triggers.
10. **position-calculator**: no short sizing with mandatory stop-loss factored into max loss.

---

## 2. CLAUDE.md Changes

### 2.1 New Section: "Short Selling Rules" (insert after "Reglas Inmutables")

```markdown
## Short Selling Rules (CFD via eToro)

### Principios
- Shorts son un COMPLEMENTO al portfolio long. NUNCA la estrategia principal.
- Cada short DEBE tener stop-loss OBLIGATORIO (max loss = 2% del portfolio por posicion).
- Short thesis DEBE documentar: por que esta SOBREVALUADA, catalizador de caida, timeline.
- Review de shorts cada 2 semanas (vs mensual para longs). Shorts son time-sensitive.

### Criterios de Short
- Overvaluation clara: precio >50% por encima de fair value conservador
- Moat inexistente o en erosion activa (AI disruption, perdida de market share)
- Tendencia fundamental negativa: revenue declinando 2+ trimestres, FCF negativo, deuda creciente
- Catalizador identificado: earnings miss esperado, perdida de cliente clave, regulacion adversa
- Borrow cost (overnight fee eToro) < rendimiento esperado del short

### Limites Short
- Max gross short exposure: 15% del portfolio
- Max single short position: 3% del portfolio (half of long max)
- Max loss per short (stop-loss): 2% del portfolio
- Mandatory stop-loss: entry price + 25% (ajustable por volatilidad)
- Max holding period sin re-evaluacion: 14 dias
- Max short positions simultaneas: 3

### Costes eToro CFD
- Overnight fee: variable por instrumento (calcular ANTES de abrir)
- Si fee anualizado >8% del notional: NO abrir short (coste erosiona profit)
- Spread: verificar que spread < 1% del precio

### Flujo Obligatorio
short-screener/dynamic_screener --short → fundamental-analyst --mode short → investment-committee --mode short → USER CONFIRMS → portfolio-ops

### Nunca (Shorts)
- Short sin stop-loss documentado
- Short >3% del portfolio
- Short de empresa con short squeeze risk (>20% short interest, baja liquidez)
- Short de empresa con dividend ex-date proximo (short paga dividendo)
- Short sin catalizador temporal identificado
- Short de empresa que cumple nuestros criterios LONG (wide moat, undervalued)
```

### 2.2 Modified Section: "Flujo de Inversion OBLIGATORIO"

**Current:**
```markdown
## Flujo de Inversion OBLIGATORIO
Oportunidad → sector-screener → fundamental-analyst (/analyze) → investment-committee (/decide) → Recomendacion al usuario
```

**Proposed (replace entire section):**
```markdown
## Flujo de Inversion OBLIGATORIO

### Long Flow (sin cambios)
Oportunidad → sector-screener → fundamental-analyst (/analyze) → investment-committee (/decide) → Recomendacion al usuario

### Short Flow (NUEVO)
Candidato short → dynamic_screener --short / short signals → fundamental-analyst --mode short (/analyze-short) → investment-committee --mode short (/decide-short) → Recomendacion al usuario

NUNCA saltarse pasos en NINGUNO de los dos flujos.
```

### 2.3 Modified Section: "Reglas Inmutables" (add lines)

Add after existing rules:
```markdown
- Short max 3% por posicion, 15% gross short total
- Short SIEMPRE con stop-loss documentado (max loss 2% portfolio)
- Short review obligatorio cada 14 dias
- NUNCA short sin thesis documentada en thesis/short/{TICKER}/thesis.md
```

### 2.4 Modified Section: "Tools Cuantitativos" (add entries)

Add after `correlation_matrix.py` section:
```markdown
#### short_cost_calculator.py - Coste CFD shorts
\```bash
python3 tools/short_cost_calculator.py TICKER --size 500 --days 30
\```
- Calcula overnight fee estimado para CFD short en eToro
- Input: ticker, position size EUR, holding period dias
- Output: fee total, fee anualizado %, breakeven price move needed
- **REGLA: NUNCA abrir short sin verificar coste primero**
```

Add `--short` flag documentation to dynamic_screener.py:
```markdown
python3 tools/dynamic_screener.py --index europe_all --short          # Overvalued candidates
python3 tools/dynamic_screener.py --index sp500 --short --pe-min 30   # Expensive US stocks
```

### 2.5 Modified: Self-check checklist

Add to SELF-CHECK block:
```markdown
- He evaluado oportunidades short? (SI/NO) → si mercado caro, deberia buscar shorts
```

Add to FINAL-CHECK block:
```markdown
- He considerado shorts como hedge? (SI/NO) → si portfolio tiene riesgo sectorial concentrado, un short puede reducir drawdown
```

### 2.6 Modified: "Arquitectura Multi-Agente" table

Add row:
```markdown
| **Research** | short-screener | Screening de candidatos short (overvalued, broken moat, declining) |
```

Update agent count from 19 to 20.

---

## 3. Agent Changes

### 3.1 Existing Agents: Modifications Required

#### fundamental-analyst.md
**File**: `/home/angel/value_invest2/.claude/agents/investment/fundamental-analyst.md`

**Changes needed:**
1. Add `--mode short` parameter handling in the Proceso section
2. Add short analysis framework

**Add after existing "## Proceso" section:**
```markdown
## Modo Short (--mode short)
Cuando se invoca con modo short, el analisis se INVIERTE:

### Que buscar (Short Thesis)
1. **Sobrevaluacion**: P/E >30x sin justificacion de growth, P/S >10x, EV/EBITDA >20x
2. **Moat en erosion**: perdida de market share, competidores ganando, tecnologia disrupting
3. **Fundamentales deteriorandose**: revenue decline 2+ trimestres, margenes comprimidos, FCF negativo
4. **Red flags contables**: receivables creciendo mas que revenue, goodwill >50% assets, ajustes non-GAAP excesivos
5. **Catalizador**: earnings miss inminente, perdida de contrato clave, regulacion adversa, insider selling

### Output (Short Thesis)
Escribir en thesis/short/{TICKER}/thesis.md:
- Fair value (conservador, sin discount por moat porque no hay moat)
- Current price vs fair value: OVERVALUATION %
- Catalizador y timeline esperado
- Stop-loss level (entry + 25% default)
- Max holding period recomendado
- Borrow cost estimate (via short_cost_calculator.py)
- Kill conditions: que haria CERRAR el short (buenas noticias, moat recuperado)

### Micro-Agents en modo Short
- valuation-specialist: calcula fair value (mismo DCF pero busca FV << precio actual)
- moat-assessor: evalua si moat esta ROTO o en erosion (inverso de buscar moat fuerte)
- risk-identifier: identifica riesgos del SHORT (squeeze, recovery, takeover, buyback)
```

#### investment-committee.md
**File**: `/home/angel/value_invest2/.claude/agents/investment/investment-committee.md`

**Changes needed:**
Add short gate review process.

**Add after existing "## Proceso" section:**
```markdown
## Modo Short (--mode short)
Gate review para posiciones short. Checklist DIFERENTE al de longs:

### Checklist Short (TODOS deben cumplirse)
- [ ] Precio actual verificado via `python3 tools/price_checker.py TICKER`
- [ ] Overvaluation >50% vs fair value conservador
- [ ] Fundamental decline documentado (no solo "parece caro")
- [ ] Catalizador identificado con timeline <6 meses
- [ ] Stop-loss calculado: entry + 25% = max loss < 2% portfolio
- [ ] Overnight fee calculado via `python3 tools/short_cost_calculator.py`
- [ ] Fee anualizado <8% del notional
- [ ] Short interest <20% (evitar squeeze)
- [ ] No hay dividend ex-date en proximo mes
- [ ] Liquidez suficiente (avg volume >$1M/day)
- [ ] Position size <= 3% portfolio
- [ ] Total short exposure post-trade <= 15% portfolio
- [ ] NO contradice ninguna posicion long activa (no short de algo que tenemos long)

### Decision Framework
| Criterios cumplidos | Decision |
|---------------------|----------|
| 13/13 | APPROVE SHORT |
| 11-12/13 | APPROVE con condiciones (documentar excepciones) |
| <11/13 | REJECT - insuficiente conviccion |
```

#### review-agent.md
**File**: `/home/angel/value_invest2/.claude/agents/investment/review-agent.md`

**Changes needed:**
Add short position review logic (inverted from longs).

**Add section:**
```markdown
## Review de Posiciones Short
Frecuencia: cada 14 dias (vs mensual para longs)

### Logica Invertida
- Buenas noticias para la empresa = PELIGRO para el short → evaluar cierre
- Malas noticias para la empresa = PROFIT → evaluar take-profit
- Precio subiendo = LOSING → verificar stop-loss, evaluar cierre anticipado
- Precio bajando = WINNING → ajustar stop-loss a breakeven si >10% profit

### Checklist Review Short
1. Precio actual vs entry: P&L del short
2. Precio vs stop-loss: distancia al max loss
3. Thesis sigue intacta? Fundamentales siguen deteriorandose?
4. Han surgido catalizadores positivos para la empresa? (= danger)
5. Overnight fees acumulados: estan erosionando profit?
6. Dias en posicion: se acerca al max holding period?
7. Short interest: ha subido? (squeeze risk creciente)

### Acciones
| Situacion | Accion |
|-----------|--------|
| Profit >30% | TAKE PROFIT (cerrar 50-100%) |
| Profit >15%, thesis debilitada | TAKE PROFIT (cerrar 100%) |
| Loss approaching stop-loss | CLOSE antes de que toque stop |
| Thesis invalidada (buenas noticias) | CLOSE inmediatamente |
| Fees >50% del profit potencial restante | CLOSE |
| >30 dias sin catalizador | CLOSE (time decay) |
```

#### portfolio-ops.md
**File**: `/home/angel/value_invest2/.claude/agents/portfolio/portfolio-ops.md`

**Changes needed:**
Add handling for `shorts` section in `portfolio/current.yaml`.

**Add section:**
```markdown
## Operaciones Short
Cuando el humano confirma apertura/cierre de short CFD en eToro:

### Abrir Short
1. Anadir entrada en `portfolio/current.yaml` seccion `shorts:`
2. Campos obligatorios: ticker, type (short_cfd), shares, entry_price, stop_loss, date_opened, daily_fee_estimate, thesis path
3. Anadir transaction en seccion `transactions:` con action: SHORT_OPEN
4. Actualizar state/system.yaml: short watchlist, monitoring, calendar (review en 14 dias)
5. Mover thesis de thesis/research/ a thesis/short/

### Cerrar Short
1. Calcular P&L: (entry_price - exit_price) * shares - total_fees
2. Mover de `shorts:` a `transactions:` con action: SHORT_CLOSE y P&L
3. Mover thesis a thesis/archive/short/
4. Actualizar performance metrics
```

#### rebalancer.md
**File**: `/home/angel/value_invest2/.claude/agents/portfolio/rebalancer.md`

**Changes needed:**
Add short-specific rebalancing triggers.

**Add section:**
```markdown
## Triggers Short
- Short profit >30% → TAKE PROFIT (presentar al humano)
- Short loss >15% (approaching stop) → EVALUATE CLOSE
- Short position grew >3% portfolio (due to long value decline) → TRIM short
- Total short exposure >15% → REDUCE shorts
- Net exposure <70% → REDUCE shorts (demasiado hedged, cash drag equivalente)
- Short >14 dias sin review → FORCE REVIEW via review-agent
```

#### position-calculator.md
**File**: `/home/angel/value_invest2/.claude/agents/portfolio/position-calculator.md`

**Changes needed:**
Add short sizing calculation.

**Add section:**
```markdown
## Short Position Sizing
Formula:
1. Max loss per short = 2% of portfolio value
2. Stop-loss distance = entry_price * 0.25 (25% above entry by default)
3. Max shares = max_loss / stop_loss_distance
4. Position value = max_shares * entry_price
5. Verify: position_value <= 3% of portfolio
6. If position_value > 3%: reduce shares until <= 3%

### Example
Portfolio = EUR 10,000
Max loss = EUR 200 (2%)
Entry price = EUR 50
Stop-loss = EUR 62.50 (50 * 1.25)
Stop distance = EUR 12.50
Max shares = 200 / 12.50 = 16 shares
Position value = 16 * 50 = EUR 800 (8%) → EXCEEDS 3% limit
Adjusted: 3% = EUR 300 → 6 shares → loss at stop = 6 * 12.50 = EUR 75 (0.75% portfolio) ✓
```

#### performance-tracker.md
**File**: `/home/angel/value_invest2/.claude/agents/portfolio/performance-tracker.md`

**Changes needed:**
Add net/gross exposure metrics and short attribution.

**Add to Metricas section:**
```markdown
### Short-Specific Metrics
- Gross exposure: sum(long_values) + sum(abs(short_values))
- Net exposure: sum(long_values) - sum(abs(short_values))
- Net/Gross ratio: net_exposure / gross_exposure (1.0 = all long, 0.0 = market neutral)
- Short P&L: (entry - current) * shares - accumulated_fees per short
- Short attribution: contribution of shorts to total portfolio return
- Short hit rate: % of shorts closed at profit
- Average short holding period
- Total fees paid on shorts
```

#### risk-identifier.md (micro-agent)
**File**: `/home/angel/value_invest2/.claude/agents/investment/micro/risk-identifier.md`

**Changes needed:**
Add short-specific risks.

**Add section:**
```markdown
## Short-Specific Risks
When analyzing a short candidate, MUST evaluate:
1. **Short squeeze**: high short interest (>15%), low float, meme stock potential
2. **Takeover/buyout**: acquirer offers premium, short gets crushed
3. **Share buyback**: company buying back = price support
4. **Dividend trap**: short must pay dividend on ex-date
5. **Borrow cost spike**: overnight fee can increase without notice
6. **Unlimited loss**: theoretically infinite loss (stop-loss is MANDATORY mitigation)
7. **Regulatory halt**: trading halt can prevent stop-loss execution
8. **Positive catalyst surprise**: unexpected good earnings, new product, CEO change
9. **Index inclusion**: being added to index = forced buying = price up
10. **Correlation risk**: short correlated with our longs = double loss in market rally
```

#### watchlist-manager.md
**File**: `/home/angel/value_invest2/.claude/agents/portfolio/watchlist-manager.md`

**Changes needed:**
Add short watchlist management parallel to buy watchlist.

**Add section:**
```markdown
## Short Watchlist
Maintain in state/system.yaml under `watchlist.short_candidates:`
Fields per entry:
- ticker
- current_price
- fair_value (why overvalued)
- target_entry (price to short AT)
- stop_loss
- catalyst
- catalyst_date
- overnight_fee_estimate
- status: watching | ready_to_short | rejected

### Monitoring
- Check prices weekly (vs daily for buy watchlist during high urgency)
- Alert if price reaches target_entry
- Alert if catalyst date approaching
- Remove if thesis invalidated (company improving)
```

### 3.2 New Agent: short-screener

**Decision**: Add `--short` flag to existing `sector-screener` agent rather than creating a new agent. This avoids agent proliferation while adding the capability.

However, if short screening becomes complex enough to warrant its own agent, create:

**File**: `/home/angel/value_invest2/.claude/agents/research/short-screener.md`

```markdown
---
name: short-screener
description: "Screens for overvalued/declining stocks as short candidates. Uses dynamic_screener.py --short and qualitative signals."
tools: Read, Glob, Grep, Bash, Write, WebSearch, WebFetch
model: opus
permissionMode: acceptEdits
skills:
  - investment-rules
  - screening-protocol
  - short-selling-rules
---

# Short Screener Sub-Agent

## Rol
Identifica candidatos para short selling. Busca empresas sobrevaluadas, con moats rotos, o en declive estructural.

## Cuando se activa
- Mensualmente como parte del screening regular
- Cuando macro-analyst identifica sector/tema sobrevaluado
- Cuando review-agent identifica empresas en declive que NO tenemos long

## Screening Cuantitativo
python3 tools/dynamic_screener.py --index europe_all --short
python3 tools/dynamic_screener.py --index sp500 --short

### Filtros Short (inversiones de filtros long)
- P/E >30x (sobrevaluado)
- FCF yield <0% (quemando cash)
- Revenue growth <-5% (declive)
- Debt/Equity >3x (apalancamiento peligroso)
- Near 52-week high (poco downside ya priced in)
- Analysts downgrades recientes

## Screening Cualitativo (WebSearch)
- Sectores en declive estructural (brick-and-mortar retail, legacy media, legacy auto sin EV)
- Empresas con escandalo contable reciente
- Empresas perdiendo market share a disruptores
- Management turnover negativo (CEO exits, CFO exits)
- Insider selling masivo

## Output
Para cada candidato viable:
1. Quick summary: por que es candidato short
2. Fair value estimate (conservador)
3. Overvaluation %
4. Catalizador esperado
5. Timeline
6. Recommend: ANALYZE (send to fundamental-analyst --mode short) o SKIP

## Anti-Patterns (NUNCA short estos)
- Empresa con wide moat intacto (aunque parezca cara, puede seguir subiendo)
- Empresa en nuestro portfolio long (conflicto)
- Empresa con <$1M avg daily volume (illiquida)
- Empresa con >20% short interest (squeeze risk)
- Empresa en sector que macro-analyst ve positivo
```

### 3.3 Decision: Separate short-thesis agent?

**Decision**: NO. `fundamental-analyst` handles both modes. Adding `--mode short` is cleaner than a new agent. The micro-agents (valuation-specialist, moat-assessor, risk-identifier) all work for both modes with the additions described above. This keeps the system at 20 agents (adding only short-screener) rather than 21+.

---

## 4. Skill Changes

### 4.1 New Skill: short-selling-rules

**Directory**: `/home/angel/value_invest2/.claude/skills/short-selling-rules/`
**File**: `/home/angel/value_invest2/.claude/skills/short-selling-rules/SKILL.md`

```markdown
---
name: short-selling-rules
description: Rules and constraints specific to short selling via CFD. Max exposure, stop-loss requirements, review frequency, cost limits.
user-invocable: false
disable-model-invocation: false
---

# Short Selling Rules Skill

## Instrument
- CFD (Contract for Difference) via eToro
- NOT direct short selling (not available on eToro for retail)
- CFD = synthetic short, subject to overnight fees

## Position Rules
| Rule | Limit |
|------|-------|
| Max single short | 3% portfolio |
| Max gross short exposure | 15% portfolio |
| Min net long exposure | 70% portfolio |
| Mandatory stop-loss | YES (entry + 25% default) |
| Max loss per short | 2% portfolio |
| Max simultaneous shorts | 3 |
| Review frequency | Every 14 days |
| Max hold without re-evaluation | 30 days |

## Entry Criteria (ALL must be true)
1. Overvaluation >50% vs conservative fair value
2. Fundamental decline documented (revenue, FCF, margins)
3. Catalyst identified with timeline <6 months
4. Stop-loss calculated, max loss <2% portfolio
5. Overnight fee <8% annualized
6. Short interest <20% (squeeze protection)
7. No upcoming dividend ex-date (30 days)
8. Avg daily volume >$1M
9. Does NOT conflict with any long position
10. Total short exposure post-trade <15%

## Exit Criteria (ANY triggers close)
1. Profit target reached (>30% of overvaluation gap closed)
2. Stop-loss hit
3. Thesis invalidated (company improving)
4. Holding period >30 days without catalyst materializing
5. Accumulated fees >50% of remaining profit potential
6. Short interest rising >20% (squeeze risk)
7. Takeover/buyout announced

## Cost Model (eToro CFD)
- Overnight fee: charged daily for holding overnight
- Typical: 0.02-0.05% per day (7-18% annualized)
- MUST calculate total expected cost BEFORE opening
- Formula: daily_fee * expected_holding_days
- If total_fee > 30% of expected_profit: DO NOT OPEN

## Thesis Template (Short)
Every short must have thesis/short/{TICKER}/thesis.md with:
- Company name, ticker, current price, fair value
- WHY overvalued (specific, quantified)
- Catalyst and expected timeline
- Entry price, stop-loss, target price
- Position size, max loss
- Estimated overnight fee (total and annualized)
- Kill conditions (what closes the short)
- Review schedule (every 14 days)
```

### 4.2 Modified Skill: investment-rules

**File**: `/home/angel/value_invest2/.claude/skills/investment-rules/SKILL.md`

**Add after "## Nunca" section:**
```markdown
## Short Selling (ver skill short-selling-rules para detalle)
- Short thesis OBLIGATORIA (thesis/short/{TICKER}/thesis.md)
- Overvaluation >50% para shortear
- Stop-loss SIEMPRE
- Review cada 14 dias
- Max 3% por short, 15% total short, min 70% net long
```

### 4.3 Modified Skill: portfolio-constraints

**File**: `/home/angel/value_invest2/.claude/skills/portfolio-constraints/SKILL.md`

**Add new section after "## Rebalanceo triggers":**
```markdown
## Short Exposure Limits
| Metric | Limit |
|--------|-------|
| Single short position | max 3% |
| Total gross short | max 15% |
| Net long exposure | min 70% |
| Gross exposure (long + |short|) | max 115% |

## Short Rebalancing Triggers
- Short profit >30% → TAKE PROFIT
- Short loss approaching stop → EVALUATE CLOSE
- Total short >15% → REDUCE
- Net exposure <70% → REDUCE shorts
- Short >14 days without review → FORCE REVIEW
```

### 4.4 New Skill: short-thesis-framework (sub-skill)

**Directory**: `/home/angel/value_invest2/.claude/skills/sub-skills/short-thesis-template/`
**File**: `/home/angel/value_invest2/.claude/skills/sub-skills/short-thesis-template/SKILL.md`

```markdown
---
name: short-thesis-template
description: Template for writing short thesis documents. Inverse of long thesis.
user-invocable: false
disable-model-invocation: false
---

# Short Thesis Template

## Required Structure

### Header
- Ticker, Company Name, Sector, Market Cap
- Current Price (via price_checker.py)
- Fair Value (conservative)
- Overvaluation: (current - FV) / FV as %
- Short Entry Target, Stop-Loss, Profit Target
- Position Size (max 3%), Max Loss (max 2% portfolio)
- Estimated Holding Period
- Overnight Fee (daily and total estimated)

### 1. Short Thesis Summary (3 sentences max)
Why is this company overvalued? What will cause the price to decline?

### 2. Overvaluation Analysis
- P/E vs sector median and historical
- P/S, EV/EBITDA vs peers
- DCF fair value vs current price
- Revenue/earnings trajectory (declining?)
- Margin compression evidence

### 3. Moat Erosion / Structural Decline
- What competitive advantage is breaking?
- Who is taking market share?
- Technology disruption?
- Regulatory headwinds?

### 4. Catalyst
- Specific event that will trigger price decline
- Expected timeline
- Probability estimate

### 5. Risk Analysis (Why This Short Could Fail)
- Short squeeze risk (short interest, float)
- Takeover possibility
- Management pivot/turnaround
- Macro tailwind for sector
- Stop-loss scenario

### 6. Cost Analysis
- Daily overnight fee
- Total estimated cost over holding period
- Breakeven: how much must price drop to cover fees + spread

### 7. Position Management
- Entry price
- Stop-loss (mandatory, max loss 2% portfolio)
- Profit target (take profit levels)
- Review dates (every 14 days)
- Kill conditions (close immediately if...)

### 8. Verdict
SHORT / PASS / WATCH
Confidence: HIGH / MEDIUM / LOW
```

---

## 5. Tool Changes

### 5.1 Existing Tools: Modifications

#### portfolio_stats.py
**File**: `/home/angel/value_invest2/tools/portfolio_stats.py`

**Changes needed:**
1. Read `shorts` section from `portfolio/current.yaml`
2. Calculate and display:
   - Long exposure (sum of long position values)
   - Short exposure (sum of abs(short position values))
   - Gross exposure (long + short)
   - Net exposure (long - short)
   - Net/Gross ratio
   - Short P&L per position (entry - current) * shares
   - Accumulated fees per short
   - Total short fees paid
   - Short contribution to portfolio return
3. Alerts:
   - Short exposure >15% → ALERT
   - Net exposure <70% → ALERT
   - Any short >3% → ALERT
   - Any short approaching stop-loss (within 5%) → CRITICAL ALERT
   - Any short held >14 days without review → ALERT

#### dynamic_screener.py
**File**: `/home/angel/value_invest2/tools/dynamic_screener.py`

**Changes needed:**
Add `--short` flag that inverts all filters:

```python
# New argument
parser.add_argument('--short', action='store_true', help='Screen for SHORT candidates (overvalued, declining)')

# When --short is active, default filters become:
# --pe-min 30 (expensive)
# --fcf-yield-max 0 (negative FCF)
# --revenue-growth-max -5 (declining)
# --near-high 10 (within 10% of 52w high)
# Sort by: pe DESC (most expensive first)
```

Specific filter additions for `--short` mode:
- `--pe-min`: minimum P/E (to find expensive stocks)
- `--revenue-growth-max`: maximum revenue growth (negative = declining)
- `--near-high`: within X% of 52-week high
- `--neg-fcf`: only show negative FCF companies
- `--high-debt`: Debt/Equity >2x

#### correlation_matrix.py
**File**: `/home/angel/value_invest2/tools/correlation_matrix.py`

**Changes needed:**
- Read shorts from `portfolio/current.yaml`
- Assign negative weight to short positions
- Show correlation between longs and shorts (ideally positive correlation = good hedge)
- Alert if a short is negatively correlated with longs (bad: both lose together)

### 5.2 New Tools

#### short_cost_calculator.py
**File**: `/home/angel/value_invest2/tools/short_cost_calculator.py`

**Purpose**: Calculate eToro CFD overnight fees for short positions.

```python
#!/usr/bin/env python3
"""
Short Cost Calculator - Estimates eToro CFD overnight fees for short positions.

Usage:
    python3 tools/short_cost_calculator.py TICKER --size 500 --days 30
    python3 tools/short_cost_calculator.py TICKER --size 500 --days 30 --fee-rate 0.03
    python3 tools/short_cost_calculator.py WPP.L AAPL --size 500 --days 14

Arguments:
    TICKER          One or more tickers
    --size          Position size in EUR (default: 500)
    --days          Expected holding period in days (default: 14)
    --fee-rate      Daily overnight fee rate as % (default: 0.03 = 3 basis points)

Output per ticker:
    - Current price
    - Position size (EUR)
    - Daily fee (EUR)
    - Total fee for holding period (EUR)
    - Fee as % of position (annualized)
    - Breakeven price move: how much stock must drop to cover fees + spread
    - VERDICT: ACCEPTABLE (<8% annualized) or EXPENSIVE (>8%)

Notes:
    - eToro actual overnight fees vary by instrument and market conditions
    - Default 0.03% daily (~11% annualized) is conservative estimate
    - For exact rates, check eToro instrument page before opening position
    - Weekends are charged (Fri night = 3x fee for Sat+Sun+Mon)
"""

# Implementation:
# 1. Get current price via yfinance
# 2. Calculate: daily_fee = size * fee_rate / 100
# 3. Adjust for weekends: total_days_charged = days + (days // 5) * 2
# 4. total_fee = daily_fee * total_days_charged
# 5. annualized_fee_pct = (daily_fee * 365 / size) * 100
# 6. spread_cost = price * 0.005 (estimate 0.5% spread)
# 7. breakeven_move = (total_fee + spread_cost_eur) / size * 100
# 8. Print results, verdict
```

---

## 6. File Structure Changes

### 6.1 portfolio/current.yaml

**Current structure** (positions only, no shorts):
```yaml
cash:
  amount: 3338.72
  currency: EUR
positions:
  - ticker: DTE.DE
    ...
transactions:
  - date: 2026-01-26
    action: BUY
    ...
```

**Proposed structure** (add `shorts` section between `positions` and `transactions`):
```yaml
cash:
  amount: 3338.72
  currency: EUR

positions:
  - ticker: DTE.DE
    name: "Deutsche Telekom AG"
    shares: 37.624621
    invested_usd: 1198.22
    avg_cost_usd: 31.85
    date_opened: 2026-01-26
    thesis: thesis/active/DTE/thesis.md
  # ... existing positions unchanged ...

shorts:
  # Empty until first short opened
  # Structure per short position:
  # - ticker: WPP.L
  #   name: "WPP plc"
  #   type: short_cfd
  #   shares: 100
  #   entry_price_gbp: 297      # price when short opened
  #   current_exposure_eur: 350  # current notional in EUR
  #   stop_loss_gbp: 371        # mandatory, entry + 25%
  #   profit_target_gbp: 200    # target close price
  #   date_opened: 2026-02-XX
  #   last_review: 2026-02-XX
  #   next_review: 2026-02-XX   # max 14 days from last
  #   daily_fee_eur: 0.11       # estimated daily overnight fee
  #   accumulated_fees_eur: 0   # total fees paid so far
  #   thesis: thesis/short/WPP.L/thesis.md

transactions:
  # Existing transactions unchanged
  # New transaction types for shorts:
  # - date: 2026-02-XX
  #   action: SHORT_OPEN
  #   ticker: WPP.L
  #   shares: 100
  #   entry_price_gbp: 297
  #   stop_loss_gbp: 371
  #   total_eur: 350
  #   notes: "Short CFD. Broken moat, AI disruption, Altman Z 1.06"
  #
  # - date: 2026-03-XX
  #   action: SHORT_CLOSE
  #   ticker: WPP.L
  #   shares: 100
  #   exit_price_gbp: 230
  #   pnl_eur: +XX
  #   fees_paid_eur: XX
  #   net_pnl_eur: +XX
  #   notes: "Closed short. Catalyst materialized (earnings miss)."
```

### 6.2 state/system.yaml

**Add sections:**

```yaml
# After existing watchlist section:
watchlist:
  # ... existing ready_to_buy, tier_2, on_watch, active_monitoring ...

  short_candidates:
    # Stocks being evaluated for short
    # - ticker: WPP.L
    #   current_price_gbp: 297
    #   fair_value_gbp: 200
    #   overvaluation_pct: 48%
    #   catalyst: "AI disruption eroding ad agency moat"
    #   catalyst_date: 2026-Q2
    #   status: analyzing  # watching | analyzing | ready_to_short | rejected
    #   overnight_fee_est: "~11% annualized"
    #   notes: "Altman Z 1.06. No moat. But need >50% overvaluation."

  active_short_monitoring:
    # Active short positions being monitored
    # - ticker: WPP.L
    #   entry: 297
    #   stop_loss: 371
    #   target: 200
    #   last_review: 2026-02-XX
    #   next_review: 2026-02-XX
    #   kill: "Price breaks above 320 (new resistance) or Q2 revenue stabilizes"

# Add to existing alerts section:
alerts:
  price_monitors:
    # ... existing monitors ...
  short_monitors:
    # - { ticker: WPP.L, stop_loss_gbp: 371, target_gbp: 200, note: "Short CFD. Review 14d." }

# Add to macro_snapshot or as new section:
exposure_snapshot:
  # Updated by portfolio_stats.py
  # long_exposure_eur: XXXX
  # short_exposure_eur: XXXX
  # gross_exposure_eur: XXXX
  # net_exposure_eur: XXXX
  # net_pct: XX%  # target: 70-100%
  # last_updated: 2026-XX-XX
```

### 6.3 thesis/ directory

**Current:**
```
thesis/
  active/       # Long positions held
  archive/      # Closed positions
  research/     # Under analysis
  watchlist/    # On watchlist
```

**Proposed (add):**
```
thesis/
  active/       # Long positions held (unchanged)
  archive/      # Closed long positions (unchanged)
  research/     # Under analysis (unchanged)
  watchlist/    # On watchlist (unchanged)
  short/        # Active short positions
    {TICKER}/
      thesis.md
  archive/
    short/      # Closed short positions (add subdirectory)
      {TICKER}/
        thesis.md
```

---

## 7. Risk Management Architecture

### 7.1 Portfolio-Level Controls

| Metric | Limit | Check Frequency | Tool |
|--------|-------|-----------------|------|
| Gross exposure | max 115% NAV | Every session start | portfolio_stats.py |
| Net long exposure | min 70% NAV | Every session start | portfolio_stats.py |
| Total short exposure | max 15% NAV | Every session start | portfolio_stats.py |
| Correlation long-short | Monitor | Monthly | correlation_matrix.py |
| Short count | max 3 | Before any new short | portfolio_stats.py |

### 7.2 Position-Level Controls

| Control | Rule | Enforcement |
|---------|------|-------------|
| Stop-loss | MANDATORY, entry + 25% default | investment-committee gate |
| Max loss per short | 2% of portfolio | position-calculator |
| Max size per short | 3% of portfolio | position-calculator |
| Review cycle | Every 14 days | calendar-manager |
| Max hold without review | 30 days | review-agent |
| Fee monitoring | Close if fees >50% remaining profit | review-agent |

### 7.3 Short Squeeze Protocol

If a short position experiences rapid price increase (>10% in 1 day):

1. **IMMEDIATE**: Check if stop-loss was triggered (eToro should auto-close)
2. **If not triggered**: Evaluate closing manually BEFORE stop-loss
3. **Check**: Is there unusual volume? Social media buzz? (meme stock risk)
4. **Check**: Has short interest spiked? (other shorts covering = squeeze)
5. **Decision tree**:
   - Thesis still intact + temporary spike → HOLD (but tighten stop to breakeven if in profit)
   - Thesis broken + spike → CLOSE immediately
   - Squeeze signals (volume >5x avg, social buzz) → CLOSE immediately regardless of thesis
6. **Post-mortem**: Document in thesis, update short-selling-rules if needed

### 7.4 Circuit Breakers

| Trigger | Action |
|---------|--------|
| Single short loss >2% portfolio | AUTO-CLOSE (stop-loss should handle) |
| Total short losses >5% portfolio in 30 days | PAUSE all new shorts for 30 days, review strategy |
| 3 consecutive short losses | PAUSE, review screening methodology |
| Market rally >5% in 1 week | Review ALL shorts, tighten stops |
| Black swan (market drop >10%) | Shorts likely profitable: TAKE PROFITS on winners |

---

## 8. Operational Flow (Complete Short Cycle)

```
Phase 1: SCREENING
  monthly → short-screener / dynamic_screener --short
  OR macro-analyst identifies overvalued sector
  OR review-agent identifies deteriorating company (not in our longs)
  Output: list of 3-5 candidates with quick rationale

Phase 2: ANALYSIS
  fundamental-analyst --mode short
  Delegates to:
    - valuation-specialist: DCF → fair value << current price?
    - moat-assessor: is moat broken/eroding?
    - risk-identifier: short-specific risks (squeeze, takeover, etc.)
  Output: thesis/short/{TICKER}/thesis.md (or thesis/research/ if not ready)

Phase 3: GATE
  investment-committee --mode short
  13-point checklist (Section 3.1 above)
  MUST PASS 11/13 minimum
  Output: APPROVE / REJECT with reasoning

Phase 4: COST CHECK
  python3 tools/short_cost_calculator.py TICKER --size XXX --days 14
  If fee >8% annualized → REJECT
  If breakeven move >15% → RECONSIDER (need big move just to break even)

Phase 5: SIZING
  position-calculator (short mode)
  Max 3% portfolio, max 2% loss at stop
  Output: shares, entry price, stop-loss, max loss EUR

Phase 6: RECOMMENDATION TO HUMAN
  Present: ticker, thesis summary, entry, stop, target, size, fees, max loss
  Human says YES → execute CFD short on eToro
  Human says NO → move to short watchlist or discard

Phase 7: EXECUTION & RECORDING
  Human confirms execution on eToro
  portfolio-ops updates:
    - portfolio/current.yaml (shorts section)
    - state/system.yaml (short monitoring, calendar)
    - thesis moved to thesis/short/

Phase 8: MONITORING (every 14 days minimum)
  review-agent checks:
    - Price vs entry, stop, target
    - Thesis still valid?
    - Accumulated fees
    - Any positive catalysts for company?
    - Short interest changes?
  Output: HOLD / TAKE PROFIT / CLOSE

Phase 9: EXIT
  Trigger: profit target, stop-loss, thesis broken, time limit, fee erosion
  Human closes CFD on eToro
  portfolio-ops records:
    - Transaction (SHORT_CLOSE with P&L)
    - Move thesis to archive
    - Update performance metrics

Phase 10: POST-MORTEM
  review-agent documents:
    - Was the short profitable?
    - Was the thesis correct?
    - What could we have done better?
    - Update short-selling-rules if lesson learned
```

---

## 9. Implementation Phases

### Phase 0: Document (THIS DOCUMENT) -- DONE
- Blueprint complete
- Decision pending based on strategy analysis results

### Phase 1: File Structure & Portfolio Tracking
**Estimated effort**: 1 session
**Changes**:
1. Create `thesis/short/` directory
2. Add `shorts:` section to `portfolio/current.yaml` (empty initially)
3. Add `short_candidates:`, `active_short_monitoring:`, `short_monitors:`, `exposure_snapshot:` to `state/system.yaml`
4. Modify `portfolio_stats.py` to read shorts and calculate net/gross exposure
**Risk**: LOW (additive changes only, nothing breaks for longs)

### Phase 2: Screening Capability
**Estimated effort**: 1 session
**Changes**:
1. Add `--short` flag to `dynamic_screener.py` with inverse filters
2. Create `short-screener.md` agent (or add mode to sector-screener)
**Risk**: LOW (new code, does not modify existing screening)

### Phase 3: Cost Calculator
**Estimated effort**: 0.5 session
**Changes**:
1. Create `tools/short_cost_calculator.py`
**Risk**: NONE (new tool, no dependencies)

### Phase 4: Agent Modifications
**Estimated effort**: 1-2 sessions
**Changes**:
1. Modify `fundamental-analyst.md` (add short mode)
2. Modify `investment-committee.md` (add short gate)
3. Modify `review-agent.md` (add short review logic)
4. Modify `portfolio-ops.md` (add short handling)
5. Modify `rebalancer.md` (add short triggers)
6. Modify `position-calculator.md` (add short sizing)
7. Modify `performance-tracker.md` (add short metrics)
8. Modify `risk-identifier.md` (add short risks)
9. Modify `watchlist-manager.md` (add short watchlist)
**Risk**: MEDIUM (modifying existing agents, must not break long flow)

### Phase 5: Skills & Rules
**Estimated effort**: 0.5 session
**Changes**:
1. Create `short-selling-rules` skill
2. Create `short-thesis-template` sub-skill
3. Modify `investment-rules` skill
4. Modify `portfolio-constraints` skill
5. Update CLAUDE.md with all new sections
**Risk**: LOW (additive)

### Phase 6: Paper Trading
**Estimated effort**: 2-4 weeks
**Process**:
1. Identify 1-2 short candidates using new screening
2. Run full flow (screen → analyze → committee) but do NOT execute
3. Track paper P&L manually in a separate file
4. After 2-4 weeks, evaluate: was the thesis correct? Would we have made money?
**Risk**: NONE (no real money)

### Phase 7: First Real Short
**Trigger conditions** (ALL must be true):
- Paper trading showed at least 1 profitable short
- eToro CFD costs verified with real instrument page
- ESMA leverage limits confirmed (retail: max 5:1 for equities)
- High conviction candidate identified (overvaluation >50%, clear catalyst)
- Portfolio in stable state (no urgent long actions pending)
**Process**:
1. Small position: 2% portfolio max for first short
2. Conservative stop-loss: entry + 20% (tighter than standard 25%)
3. Daily monitoring for first week
4. Full post-mortem after close

---

## 10. What We DON'T Change

1. **Long strategy**: Remains exactly as-is. Value investing with MoS tiers, quality scoring, same agents and flow.
2. **MoS thresholds for longs**: Tier A 15%, Tier B 25%, Tier C 35% -- unchanged.
3. **Position limits for longs**: 7% max per position, 25% sector, 35% geography -- unchanged.
4. **Investment philosophy**: We are primarily a long-only value fund. Shorts are a tactical overlay for:
   - Alpha generation (profit from overvaluation)
   - Portfolio hedging (reduce net exposure in expensive markets)
   - Improving Sharpe ratio (if longs and shorts are uncorrelated)
5. **Tool infrastructure**: price_checker.py, dcf_calculator.py work as-is for both longs and shorts.
6. **Session protocol**: Same startup sequence. Short monitoring added to existing checks, not replacing them.

---

## 11. Decision Dependencies

### Must Know Before Implementing

1. **eToro CFD specifics**:
   - Exact overnight fee formula per instrument (varies by market)
   - Spread on CFD shorts (wider than long positions?)
   - Can we set guaranteed stop-loss? (eToro offers this for fee)
   - ESMA leverage limits for retail CFD (max 5:1 equities, 2:1 crypto)
   - Available instruments: can we short European mid-caps or only large-caps?

2. **ESMA regulatory rules**:
   - Short selling disclosure >0.2% of issued share capital (not relevant for CFD?)
   - Temporary short selling bans during market stress (applies to CFD?)
   - Negative balance protection (eToro should cover this)

3. **Backtesting validation** (from separate strategy analysis):
   - Does adding shorts historically improve Sharpe ratio?
   - What is the optimal net exposure (70%? 80%? 90%?)
   - What short holding period is optimal?
   - Which screening criteria have best hit rate?

### Trigger to Implement

The decision to proceed requires ALL of:
- [ ] Strategy analysis shows Sharpe improvement >0.1 with shorts
- [ ] eToro CFD costs verified as <10% annualized for target instruments
- [ ] At least 1 high-conviction short candidate identified (>50% overvaluation)
- [ ] Portfolio long positions stable (no urgent rebalancing needed)
- [ ] Human explicitly approves short selling as strategy addition

### Timeline Estimate
- Phase 1-3 (infrastructure): 2-3 sessions
- Phase 4-5 (agents + rules): 2-3 sessions
- Phase 6 (paper trade): 2-4 weeks
- Phase 7 (first real short): After paper trade validation
- **Total**: ~1 month from decision to first real short

---

## Appendix A: File Changes Summary

| File | Action | Priority |
|------|--------|----------|
| `CLAUDE.md` | MODIFY (add short sections) | Phase 5 |
| `portfolio/current.yaml` | MODIFY (add shorts section) | Phase 1 |
| `state/system.yaml` | MODIFY (add short tracking) | Phase 1 |
| `tools/portfolio_stats.py` | MODIFY (net/gross exposure) | Phase 1 |
| `tools/dynamic_screener.py` | MODIFY (add --short flag) | Phase 2 |
| `tools/short_cost_calculator.py` | CREATE | Phase 3 |
| `tools/correlation_matrix.py` | MODIFY (handle shorts) | Phase 4 |
| `.claude/agents/research/short-screener.md` | CREATE | Phase 2 |
| `.claude/agents/investment/fundamental-analyst.md` | MODIFY | Phase 4 |
| `.claude/agents/investment/investment-committee.md` | MODIFY | Phase 4 |
| `.claude/agents/investment/review-agent.md` | MODIFY | Phase 4 |
| `.claude/agents/investment/micro/risk-identifier.md` | MODIFY | Phase 4 |
| `.claude/agents/portfolio/portfolio-ops.md` | MODIFY | Phase 4 |
| `.claude/agents/portfolio/rebalancer.md` | MODIFY | Phase 4 |
| `.claude/agents/portfolio/position-calculator.md` | MODIFY | Phase 4 |
| `.claude/agents/portfolio/performance-tracker.md` | MODIFY | Phase 4 |
| `.claude/agents/portfolio/watchlist-manager.md` | MODIFY | Phase 4 |
| `.claude/skills/short-selling-rules/SKILL.md` | CREATE | Phase 5 |
| `.claude/skills/sub-skills/short-thesis-template/SKILL.md` | CREATE | Phase 5 |
| `.claude/skills/investment-rules/SKILL.md` | MODIFY | Phase 5 |
| `.claude/skills/portfolio-constraints/SKILL.md` | MODIFY | Phase 5 |
| `thesis/short/` | CREATE directory | Phase 1 |

**Total: 8 files modified, 5 files created, 1 directory created, 1 agent added (19 → 20)**
