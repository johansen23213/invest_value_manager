# Plan de Implementación Completo — Short Selling + Contrathesis + Sistema Unificado

> **Estado:** PENDIENTE APROBACION DEL HUMANO
> **Origen:** Session 73 (2026-02-18)
> **Objetivo:** Todo operativo en la siguiente sesion. Sin fases. Sin periodos de aprendizaje.
> **Principio rector:** Tools = DATOS CRUDOS. Decisions = principles.md + precedentes + razonamiento.
> **Post-implementacion:** El sistema opera a capacidad completa desde el dia 1.

---

# PLAN 1: IMPLEMENTACION TOTAL

## 1.1 PRINCIPIOS Y DOCUMENTACION

### 1.1.1 Extender `learning/principles.md`

Añadir 3 principios nuevos al final (antes de "Como Usar Este Documento"):

**Principio 10: Catalizador como Ancla Temporal**
- En longs podemos esperar indefinidamente (compounding trabaja a favor)
- En shorts el tiempo trabaja en contra (carry cost)
- Pregunta guia: "¿Puedo identificar un evento concreto que forzara al mercado a reconocer la fragilidad?"
- Sin catalizador identificable → OBSERVAR, no shortear
- No hay plazo fijo. Hay razonamiento: "¿El coste acumulado hasta el catalizador es aceptable?"

**Principio 11: Asimetria Consciente**
- La mecanica de perdida es diferente en shorts
- Pregunta guia: "Si estoy equivocado, ¿cuanto puede subir y por que? ¿Hay riesgo de squeeze? ¿Evento binario que suba 50%+ overnight?"
- ESMA protege el balance total, pero la proteccion real es el razonamiento previo

**Principio 12: El Short Sirve al Portfolio, No es Portfolio**
- Pregunta guia: "¿Este short protege mis longs, genera cash para futuras compras, o mejora las metricas? ¿O es distraccion?"
- Los shorts son herramienta al servicio del portfolio long de quality compounders

### 1.1.2 Extender `.claude/rules/error-patterns.md`

Añadir 4 errores nuevos:

```
#44. Shortear sin catalizador
Sin catalizador con fecha → NO shortear. "Esta cara" no es thesis.

#45. No cubrir cuando catalizador pasa sin efecto
Si catalizador pasa y nada cambia → CUBRIR. No esperar "a que eventualmente caiga".

#46. Shortear empresa "cara" sin thesis de fragilidad (Tesla trap)
Precio alto ≠ short thesis. Necesita FRAGILIDAD ESTRUCTURAL documentada.
Si empresa "me viene a la mente" como short → es sesgo → VALIDAR.

#47. Apalancamiento excesivo en shorts
Razonar sobre leverage desde P1 (Sizing) y P11 (Asimetria). x1-x2 como precedente inicial.
```

### 1.1.3 Crear estructura de directorios

```bash
mkdir -p thesis/short/active
mkdir -p thesis/short/research
```

### 1.1.4 Crear template de thesis short

Crear `thesis/short/_TEMPLATE.md`:

```markdown
# [TICKER] — Short Thesis

> **Direction:** SHORT
> **Fair Value:** $XXX (lo que realmente vale)
> **Current Price:** $YYY
> **Overvaluation:** ZZ% ((Price - FV) / Price)
> **Catalizador:** [Evento que forzara reconocimiento]
> **Fecha Catalizador:** YYYY-MM-DD (o rango)
> **QS Tool:** XX | **QS Ajustado:** XX (Tier X)

## 1. ¿Por que el precio actual no se sostiene?

## 2. Dependencia oculta
[¿De que depende la valoracion actual que el mercado asume permanente?]

## 3. Catalizador
[Evento especifico con fecha]

## 4. Escenarios
| Escenario | Prob | Precio target | Retorno short |
|-----------|------|---------------|---------------|
| Bear (para empresa) | | | |
| Base | | | |
| Bull (malo para nosotros) | | | |

## 5. ¿Que puede salir mal? (para nuestro short)
- [Empresa mejora]
- [Short squeeze]
- [Catalizador se pospone]

## 6. Kill Conditions (cubrir si...)
- KC#1:
- KC#2:

## 7. Sizing y mecanica
- Instrumento: CFD short en eToro
- Leverage: x[1-2]
- Sizing: EUR [amount] ([X]% del portfolio)
- Stop loss: $[price]
- Carry estimado: ~EUR[X]/mes
```

---

## 1.2 TOOLS — MODIFICAR EXISTENTES

### 1.2.1 `dcf_calculator.py` — Añadir `--reverse` flag

**Que cambia:** Nuevo modo que dado precio actual, resuelve para growth rate implicito.

**Input modo --reverse:**
- Precio actual (yfinance)
- Shares outstanding, deuda neta (yfinance)
- FCF ultimo año (yfinance)
- WACC estimado (parametro o default)

**Output modo --reverse:**
```
TICKER: ROP
Price: $321 | EV: $52.4B | FCF: $2.1B
WACC: 8.5% | Terminal growth: 2.5%

IMPLIED EXPECTATIONS:
  FCF growth implied:    4.1% /yr (10yr)

HISTORICAL CONTEXT:
  Historical FCF growth (5yr):  14.1% /yr
  Analyst consensus growth:     8-10% /yr

GAP: Implied 4.1% vs historical 14.1%

SCENARIO MATH:
  If gap closes (grows at historical): +XX%
  If market correct (grows at implied): 0%
  Ratio: X.X:1

SENSITIVITY (WACC vs Growth):
  [matrix]

[Raw data. Reason from principles.md]
```

**Con `--detailed`:** Añadir implied margin analysis, implied terminal multiple, probability-weighted scenarios.

**Con multiples tickers:** `python3 tools/dcf_calculator.py --reverse ROP ADBE NVO`

**Esfuerzo:** Medio. Usar `quant-tools-dev` agent.

### 1.2.2 `portfolio_stats.py` — Soportar shorts

**Que cambia:**
- Leer `short_positions:` section de `portfolio/current.yaml`
- Para shorts: P&L invertido (precio baja = ganancia)
- Seccion separada "SHORT POSITIONS" en output
- Nuevas lineas al final:
  ```
  LONG EXPOSURE:  EUR XXXX (XX.X%)
  SHORT EXPOSURE: EUR XXXX (XX.X%)
  NET EXPOSURE:   EUR XXXX (XX.X%)
  GROSS EXPOSURE: EUR XXXX (XX.X%)
  ```
- Si no hay shorts, funciona exactamente como ahora (retrocompatible)

**Esfuerzo:** Bajo. Añadir ~40 lineas.

### 1.2.3 `forward_return.py` — Soportar direccion short

**Que cambia:**
- Leer thesis de `thesis/short/active/` ademas de `thesis/active/`
- Para shorts: MoS% = (Price - FV) / Price * 100 (invertido)
- Nueva columna "Dir" (L/S) en output
- Seccion separada para shorts activos
- Si no hay shorts, funciona exactamente como ahora

**Esfuerzo:** Bajo. Modificar `process_position()` para invertir MoS si direction=short.

### 1.2.4 `constraint_checker.py` — Net exposure

**Que cambia:**
- Nuevo modo: `CHECK_SHORT TICKER AMOUNT`
- En REPORT: añadir secciones Long/Short/Net/Gross exposure
- Un short en un sector REDUCE exposicion neta a ese sector
- Sector y geo maps: extender con tickers nuevos segun se usen
- Si no hay shorts, funciona exactamente como ahora

**Esfuerzo:** Medio. Reestructurar `build_portfolio_state()` para manejar dos listas.

### 1.2.5 `effectiveness_tracker.py` — Seccion shorts

**Que cambia:**
- Seccion separada para shorts cerrados (win = precio bajo a target)
- Sharpe calculado sobre portfolio total (long + short)
- Si no hay shorts, funciona exactamente como ahora

**Esfuerzo:** Bajo-Medio.

### 1.2.6 `quality_universe.py` — Soportar direccion

**Que cambia:**
- Nuevo campo `direction: long` (default) o `direction: short` en cada entrada
- Nuevo flag `--fragility` que muestra solo direction=short
- Subcomando `actionable` muestra ambas direcciones con columna "Dir"
- Para shorts: "actionable" = precio > entry (sobrevalorada, acercandose al trigger por arriba)
- Stats: separar metricas long/short

**Esfuerzo:** Medio.

### 1.2.7 `consistency_checker.py` — Soportar shorts

**Que cambia:**
- Aceptar `"SHORT TICKER N%"` ademas de `"BUY TICKER N%"`
- Comparar vs precedentes short (cuando existan)

**Esfuerzo:** Bajo.

### 1.2.8 `drift_detector.py` — Short exposure drift

**Que cambia:**
- Detectar si exposicion short crecio inadvertidamente
- Si no hay shorts, funciona como ahora

**Esfuerzo:** Bajo.

### 1.2.9 `correlation_matrix.py` — Incluir shorts

**Que cambia:**
- Incluir shorts en la matrix
- Mostrar correlacion long-short para verificar que shorts son hedge genuino

**Esfuerzo:** Bajo.

---

## 1.3 TOOLS — CREAR NUEVOS

### 1.3.1 `insider_tracker.py` — Datos de insiders y sentimiento

**Proposito:** Extraer datos de yfinance que ya existen pero no usamos.

**Uso:**
```bash
python3 tools/insider_tracker.py TICKER
python3 tools/insider_tracker.py TICKER1 TICKER2
```

**Output:**
```
INSIDER ACTIVITY (6 months):
  Buys: X transactions, $X total
  Sells: X transaction, $X (10b5-1: X)
  Net: +/-$X

INSTITUTIONAL CHANGES:
  Top buyer: [name] +XX shares
  Top seller: [name] -XX shares
  Net institutional: +/-X.X% ownership

SHORT INTEREST:
  Short ratio: X.X days to cover
  % float short: X.X%

ANALYST CONSENSUS:
  Strong Buy: X | Buy: X | Hold: X | Sell: X
  Avg PT: $XXX | High: $XXX | Low: $XXX

[Raw data. Reason from principles.md]
```

**Fuente:** yfinance (`ticker.insider_transactions`, `ticker.institutional_holders`, `ticker.major_holders`, `ticker.recommendations`, `ticker.info['shortRatio']`)

**Esfuerzo:** Bajo (1 sesion).

### 1.3.2 `narrative_checker.py` — Datos financieros vs narrativa

**Proposito:** Organizar tendencias financieras que revelan si la narrativa se sostiene.

**Uso:**
```bash
python3 tools/narrative_checker.py TICKER
```

**Output:**
```
FINANCIAL DATA TRENDS (3yr):

Deferred revenue:
  2023: $X → 2024: $X → 2025: $X (trend)

R&D / Revenue:
  2023: X% → 2024: X% → 2025: X%

Capex / Depreciation:
  Capex: $X | Depreciation: $X | Ratio: X.Xx

SBC / Revenue:
  2023: X% → 2024: X% → 2025: X%

Working capital signals:
  Receivables growing faster than revenue: YES/NO
  Inventory building: YES/NO/N/A

Gross margin trend:
  2023: X% → 2024: X% → 2025: X%

[Raw data. Reason from principles.md]
```

**Fuente:** yfinance (`ticker.financials`, `ticker.balance_sheet`, `ticker.cashflow`)

**Esfuerzo:** Bajo-Medio (1 sesion).

---

## 1.4 SKILLS — CREAR NUEVOS (5)

### 1.4.1 `contrathesis-framework` SKILL

**Proposito:** Framework de 4 filtros + 6 preguntas para todo analisis (long y short).

**Contenido:**
```
TODO analisis — long o short — incluye:

FILTRO 1: ¿Que asume el precio y por que?
  → dcf_calculator.py --reverse da los datos
  → ¿Es razon (datos macro reales) o emocion (miedo generico)?

FILTRO 2: ¿Quien opina y con que skin in the game?
  → insider_tracker.py da los datos
  → Ponderar por coste de equivocarse, no por volumen

FILTRO 3: ¿Datos primarios confirman o contradicen la narrativa?
  → narrative_checker.py da los datos
  → Si narrativa dice X y datos dicen Y, a largo plazo datos ganan

FILTRO 4: ¿Asimetria favorable?
  → ¿Cuanto pierdo si me equivoco vs cuanto gano si acierto?
  → No necesito certeza. Necesito asimetria.

6 PREGUNTAS COMPLEMENTARIAS:
1. ¿Que cree el consenso?
2. ¿De que depende esa creencia? (cadena de dependencias hasta dato primario)
3. ¿Quien tiene incentivo a mantenerla?
4. ¿Donde podria estar equivocado el consenso?
5. ¿Puedo verificar con datos primarios?
6. ¿En que marco temporal se resuelve?

Si consenso equivocado a la baja → LONG
Si consenso equivocado al alza → SHORT
Si consenso tiene razon → NO OPERAR
```

### 1.4.2 `cover-protocol` SKILL

**Proposito:** Espejo de exit-protocol para cerrar shorts. 6 gates:

```
Gate 1: ¿Fragilidad resuelta? (empresa mejoro fundamentalmente)
Gate 2: ¿Catalizador paso? (acertamos o no)
Gate 3: ¿Beneficio suficiente? (target alcanzado)
Gate 4: ¿Coste de carry aceptable? (acumulado vs beneficio)
Gate 5: ¿Mejor uso del capital? (oportunidad-coste)
Gate 6: ¿Friccion de cobertura?

Verdicts: HOLD SHORT / COVER PARTIAL / COVER FULL
```

### 1.4.3 `filing-analysis` SKILL

**Proposito:** Checklist de que buscar en Annual Reports/10-K.

```
- Risk factors nuevos vs año anterior
- Cambios de lenguaje ("expect" → "anticipate")
- Cambio de auditor (red flag)
- Off-balance sheet obligations
- Contingent liabilities nuevas
- Related party transactions
- Cambios en politicas contables
- Revenue concentration disclosure
- Insider transactions pattern (Form 4 / PDMR)
```

### 1.4.4 `skin-in-the-game` SKILL

**Proposito:** Framework para evaluar quien opina.

```
- Insider buying > insider selling (pero 10b5-1 = noise)
- Institucional añadiendo = smart money ve valor
- Analyst contra consenso > analyst que sigue manada
- Management comprando con dinero propio >> management con stock comp
- Short seller con track record > short seller desconocido
- Cuanto le cuesta a esta persona estar equivocada > cuantas personas opinan igual
```

### 1.4.5 `short-thesis-framework` SKILL

**Proposito:** Espejo de business-analysis-framework para fragilidad.

```
SECCION 0: QUALITY SCORE (mismo que long)
SECCION 1: ¿Por que el precio no se sostiene?
SECCION 2: Dependencia oculta (cadena de "¿de que depende?")
SECCION 3: Catalizador (P10 — obligatorio, con fecha)
SECCION 4: Escenario adverso (P11 — ¿que pasa si sube 50%?)
SECCION 5: Kill conditions para cubrir
SECCION 6: Sizing y mecanica (CFD, leverage, carry estimado)
```

---

## 1.5 SKILLS — MODIFICAR EXISTENTES (9)

### 1.5.1 `pre-execution-check` — Extender para shorts + reverse DCF

**Cambios:**
- Soportar standing orders SHORT (trigger es precio ALTO, no bajo)
- Añadir paso en Gate 5 (Thesis Validity): ejecutar `dcf_calculator.py --reverse TICKER` para confirmar que el gap sigue existiendo
- Para shorts: noticias POSITIVAS = alerta (posicion va en contra)
- Incorporar principio de frescura: cuanto mas viejo el analisis, mas importante revalidar

### 1.5.2 `exit-protocol` — Añadir COVER flow

**Cambios:**
- Referencia al cover-protocol skill para shorts
- Gate 4 (Opportunity Score): incluir shorts en el calculo de forward return neto

### 1.5.3 `business-analysis-framework` — Añadir Consensus Analysis

**Cambios:**
- Añadir SECCION 0.5 (despues de QS, antes de Modelo de Negocio):
  ```
  SECCION 0.5: CONSENSUS ANALYSIS (contrathesis-framework)
  ¿Que implica el precio? → dcf_calculator.py --reverse
  ¿Quien compra/vende? → insider_tracker.py
  ¿Datos confirman narrativa? → narrative_checker.py
  ```
- Esto aplica TANTO para longs como para shorts

### 1.5.4 `investment-rules` — Añadir seccion Short

**Cambios:**
- Añadir seccion "Short Thesis Evaluation":
  - QS bajo no basta — necesita gap entre QS real y QS implicito del precio
  - Empresa QS 50 que cotiza como QS 80 = potencial short
  - Empresa QS 30 que cotiza barata = NO short (ya refleja fragilidad)

### 1.5.5 `capital-deployment` — Añadir Fase E: Fragility Universe

**Cambios:**
- Fase E: Maintenance del fragility side del quality universe
- Screening de candidatos short cuando hay fragilidad macro detectada
- No es prioridad diaria como longs — es oportunista
- Usar quality_universe.py --fragility para monitorear

### 1.5.6 `pipelines` — Añadir fragility-watch

**Cambios:**
- Nuevo pipeline `fragility-watch` con cadencia semanal
- Escanear fragility entries en quality universe
- Verificar catalizadores vigentes
- Si short activo: verificar carry acumulado

### 1.5.7 `news-classification` — Shorts

**Cambios:**
- Clasificar noticias sobre shorts activos
- Impacto POSITIVO sobre un short = potencial problema (posicion va en contra)

### 1.5.8 `portfolio-constraints` — Net exposure

**Cambios:**
- Net exposure como metrica adicional
- Razonar sobre gross vs net, no solo long allocation
- Un short en sector X REDUCE exposicion neta al sector X

### 1.5.9 `rotation-engine` — Forward return neto

**Cambios:**
- Forward return NETO (incluyendo shorts)
- Los shorts generan forward return cuando aciertan — integrar en evaluacion

---

## 1.6 RULES — MODIFICAR (5)

### 1.6.1 `agent-protocol.md` — Arbol de decision

**Añadir ramas:**
```
├─ ANALIZAR fragilidad → fundamental-analyst (prompt --short-thesis)
├─ APROBAR short → investment-committee (modo SHORT_APPROVAL)
├─ RE-EVALUAR short → review-agent (prompt --short-review)
├─ CUBRIR short → cover-protocol skill → investment-committee
```

### 1.6.2 `session-protocol.md` — Extender fases

**Cambios por fase:**
```
FASE 0: Pre-execution check incluye shorts (trigger por arriba)
FASE 1: Vigilancia incluye shorts activos (positivo = alerta)
FASE 2: portfolio_stats.py muestra net exposure
FASE 2.5: forward_return.py incluye shorts
FASE 3: Standing orders incluye short orders. Pipeline incluye short pipeline.
FASE 4: Shorts si catalizador inminente + thesis aprobada
FASE 5: Effectiveness shorts separada + Sharpe total
```

### 1.6.3 `error-patterns.md` — Ya cubierto en 1.1.2

### 1.6.4 `tools-reference.md` — Nuevos tools y flags

**Añadir:**
```
| dcf_calculator.py --reverse | Reverse DCF. Implied expectations. |
| insider_tracker.py | Insider transactions, institucionales, short interest. |
| narrative_checker.py | Tendencias financieras vs narrativa. |
```

**Modificar entradas existentes:**
```
| portfolio_stats.py | + Net/Gross exposure si hay shorts |
| forward_return.py | + Direccion L/S, MoS invertido para shorts |
| constraint_checker.py | + CHECK_SHORT modo, net exposure |
| quality_universe.py | + --fragility flag, direction field |
```

### 1.6.5 `file-structure.md` — Nuevas ubicaciones

**Añadir:**
- `thesis/short/active/` — shorts con posicion abierta
- `thesis/short/research/` — candidatos short en analisis
- `thesis/short/_TEMPLATE.md` — template de thesis short
- Seccion `short_positions:` en `portfolio/current.yaml`
- Campo `direction` en `state/quality_universe.yaml`

---

## 1.7 STATE FILES — MODIFICAR (7)

### 1.7.1 `portfolio/current.yaml` — Añadir seccion shorts

**Añadir despues de `positions:`:**
```yaml
short_positions:
  # Empty until first short is opened
  # Structure per position:
  # - ticker: XXX
  #   direction: short
  #   shares: X
  #   entry_price_usd: X.XX
  #   invested_usd: X.XX
  #   date_opened: YYYY-MM-DD
  #   thesis: thesis/short/active/XXX/thesis.md
  #   catalyst: "description"
  #   catalyst_date: YYYY-MM-DD
  #   leverage: 1
  #   carry_cost_daily_eur: X.XX
  #   stop_loss: X.XX
  #   conviction: high/medium/low
  #   fair_value: "$XXX"
  #   exit_plan: "COVER if..."
```

### 1.7.2 `state/standing_orders.yaml` — Redesign + shorts

**Cambios estructurales:**
- Añadir campo `last_analysis_date` a CADA orden existente
- Añadir campo `freshness_note` (cuanto ha cambiado desde analisis)
- Renombrar concepto: son ALERTAS con thesis pre-escrita, no ordenes autonomas
- Soportar `action: SHORT` y `action: COVER`
- Para shorts: trigger es `">=$PRICE"` (por arriba)
- Para shorts: campo `catalyst` y `catalyst_date` obligatorios

**Añadir header actualizado:**
```yaml
# STANDING ORDERS - Price alerts with pre-written thesis
# NOT autonomous orders. Human alerts Claude when price hits trigger.
# Claude runs fast-track validation (pre-execution-check + reverse DCF) before recommending.
```

### 1.7.3 `state/watchlist.yaml` — Short candidates

**Añadir soporte:**
```yaml
short_candidates:
  # - ticker: XXX
  #   fragility: "description"
  #   catalyst: "description"
  #   catalyst_date: YYYY-MM-DD
  #   price_current: XXX
  #   fair_value: XXX
  #   overvaluation_pct: XX%
```

### 1.7.4 `state/quality_universe.yaml` — Direction field

**Cambio:** Añadir `direction: long` (default) a todas las entradas existentes.
Nuevas entradas short tendran `direction: short`.

### 1.7.5 `state/calendar.yaml` — Catalizadores short

**Cambio:** Soportar tipo `short_catalyst` ademas de tipos existentes.

### 1.7.6 `state/system.yaml` — Net exposure

**Cambio:** Añadir a `portfolio_quality_analysis`:
```yaml
exposure:
  long_eur: XXXX
  short_eur: 0
  net_eur: XXXX
  gross_eur: XXXX
  net_pct: XX.X%
```

### 1.7.7 `state/pipeline_tracker.yaml` — Fragility-watch

**Cambio:** Añadir pipeline:
```yaml
fragility_watch:
  cadence: weekly
  last_run: null
  description: "Scan fragility universe, verify catalysts, check carry costs"
```

---

## 1.8 AGENT REGISTRY — ACTUALIZAR

### Cambios en `agent-registry/SKILL.md`:

**fundamental-analyst:**
- Añadir: "Cuando invocado con prompt --short-thesis: invierte analisis, busca fragilidad"
- Añadir skill: contrathesis-framework, short-thesis-framework
- Añadir: Lee thesis/short/research/ ademas de thesis/research/

**devils-advocate:**
- Añadir: "Para shorts: Devil's advocate BULL — ¿por que podria el precio tener razon?"
- Prompt invertido cuando desafia thesis short

**investment-committee:**
- Añadir: modo SHORT_APPROVAL con gates adaptados (3 gates nuevos: catalizador, asimetria, servicio al portfolio)
- Lee thesis de thesis/short/ cuando aplica

**review-agent:**
- Añadir: modo --short-review
- ¿Thesis de fragilidad sigue intacta? ¿Catalizador vigente? ¿Carry aceptable?

**news-monitor:**
- Añadir: shorts activos en scan
- Noticias positivas sobre short = alerta

**market-pulse:**
- Añadir: shorts activos
- Short que sube significativamente = tan importante como long que cae

**portfolio-ops:**
- Soportar `action: SHORT` y `action: COVER` ademas de BUY/SELL
- Escribir en `short_positions:` section

**position-calculator:**
- Modo short: sizing razonado con awareness de asimetria (P11)

**watchlist-manager:**
- Soportar `type: short_candidate` en watchlist

**macro-analyst:**
- Ademas de "que sectores se benefician": "que sectores son vulnerables"
- Usar WebSearch para datos macro (sin tool macro_fragility)

---

## 1.9 CLAUDE.md — ACTUALIZAR

**Cambios:**
- Tabla de referencias: añadir short-thesis-framework, cover-protocol, contrathesis-framework, filing-analysis, skin-in-the-game
- Tabla de tools: añadir insider_tracker.py, narrative_checker.py, dcf_calculator.py --reverse
- Principios: mencionar P10-P12
- Nota: "El sistema opera en ambas direcciones (long + short) desde principios unificados"

---

## 1.10 ORDEN DE EJECUCION

No hay fases, pero hay DEPENDENCIAS logicas:

```
BLOQUE A (sin dependencias, paralelo):
  A1. Crear directorios thesis/short/
  A2. Crear template thesis short
  A3. Extender principles.md (P10-P12)
  A4. Extender error-patterns.md (#44-#47)
  A5. Crear skills nuevos (5): contrathesis, cover-protocol, filing-analysis,
      skin-in-the-game, short-thesis-framework

BLOQUE B (depende de A para contexto, tools en paralelo):
  B1. dcf_calculator.py --reverse (quant-tools-dev)
  B2. insider_tracker.py (quant-tools-dev)
  B3. narrative_checker.py (quant-tools-dev)
  B4. portfolio_stats.py short support (quant-tools-dev)
  B5. forward_return.py direction support (quant-tools-dev)
  B6. constraint_checker.py net exposure (quant-tools-dev)
  B7. quality_universe.py direction field (quant-tools-dev)
  B8. Otros tools menores (consistency_checker, drift_detector, correlation_matrix, effectiveness_tracker)

BLOQUE C (depende de A para contenido):
  C1. Modificar 9 skills existentes
  C2. Modificar 5 rules files
  C3. Actualizar agent-registry

BLOQUE D (depende de B+C para estructura):
  D1. Modificar state files (7)
  D2. Actualizar CLAUDE.md

BLOQUE E: VERIFICACION (depende de todo lo anterior) → Ver PLAN 2
```

**Max agentes en paralelo: 4** (leccion Session 72 — context overflow con 7).

En BLOQUE B, lanzar tools en batches:
- Batch 1: B1 + B2 + B3 (3 tools nuevos/modificados)
- Batch 2: B4 + B5 + B6 + B7 (4 tools modificados)
- Batch 3: B8 (menores)

---

# PLAN 2: REVISION DE CONSISTENCIA DEL SISTEMA

> **Objetivo:** Verificar que TODO el sistema es coherente despues de los cambios.
> **Cuando:** Inmediatamente despues de completar Plan 1.

## 2.1 VERIFICACION DE TOOLS (funcionalidad)

### 2.1.1 Test de retrocompatibilidad

Ejecutar CADA tool modificado con el portfolio ACTUAL (10 posiciones long, 0 shorts) y verificar que el output es identico o superior al anterior:

```bash
# Cada uno debe funcionar SIN shorts en el sistema
python3 tools/portfolio_stats.py
python3 tools/forward_return.py --active-only
python3 tools/constraint_checker.py REPORT
python3 tools/effectiveness_tracker.py --summary
python3 tools/quality_universe.py stats
python3 tools/quality_universe.py actionable
python3 tools/correlation_matrix.py
python3 tools/drift_detector.py
python3 tools/consistency_checker.py "BUY ROP 4%"
```

**Criterio:** Si CUALQUIER tool falla o produce output degradado, FIX antes de continuar.

### 2.1.2 Test de tools nuevos

```bash
# Cada uno debe producir output limpio
python3 tools/dcf_calculator.py --reverse ROP
python3 tools/dcf_calculator.py --reverse ADBE NVO DTE.DE
python3 tools/insider_tracker.py ADBE
python3 tools/insider_tracker.py NVO GL
python3 tools/narrative_checker.py ADBE
python3 tools/narrative_checker.py LULU
```

**Criterio:** Output debe terminar con `[Raw data. Reason from principles.md]`. Ningun juicio, etiqueta, o warning interpretativo.

### 2.1.3 Test de funcionalidad short (sin posiciones reales)

```bash
# Simular CHECK_SHORT
python3 tools/constraint_checker.py CHECK_SHORT NVDA 500
# Verificar que quality_universe soporta direction
python3 tools/quality_universe.py report
```

## 2.2 VERIFICACION DE SKILLS (contenido)

### 2.2.1 Checklist de referencias cruzadas

Para CADA skill nuevo y modificado, verificar:

```
[ ] ¿Referencia a principles.md incluye P10-P12 cuando relevante?
[ ] ¿Referencia a error-patterns incluye #44-#47 cuando relevante?
[ ] ¿Referencia a tools incluye nuevos tools (dcf --reverse, insider, narrative)?
[ ] ¿Referencia a file paths incluye thesis/short/ cuando relevante?
[ ] ¿No hay thresholds fijos hardcodeados?
[ ] ¿Termina con referencia a razonamiento desde principios?
```

### 2.2.2 Coherencia entre skills relacionados

```
[ ] contrathesis-framework ↔ business-analysis-framework: ¿seccion 0.5 referencia al skill correctamente?
[ ] cover-protocol ↔ exit-protocol: ¿estructura paralela? ¿mismos principios?
[ ] short-thesis-framework ↔ business-analysis-framework: ¿espejo correcto?
[ ] pre-execution-check: ¿soporta tanto long como short standing orders?
[ ] investment-rules: ¿seccion short es coherente con seccion long?
```

## 2.3 VERIFICACION DE RULES

### 2.3.1 agent-protocol.md

```
[ ] Arbol de decision tiene ramas para short (analizar, aprobar, re-evaluar, cubrir)
[ ] Instrucciones v4.0 para agentes incluyen mencion de shorts
[ ] Verificacion post-agente aplica a output de shorts
```

### 2.3.2 session-protocol.md

```
[ ] CADA fase menciona shorts cuando aplica
[ ] Fase 0: pre-execution check cubre short triggers
[ ] Fase 1: vigilancia incluye shorts
[ ] Fase 2: portfolio_stats muestra net exposure
[ ] Fase 2.5: forward_return incluye shorts
[ ] Fase 3: standing orders incluye short orders
```

### 2.3.3 file-structure.md

```
[ ] thesis/short/ documentado
[ ] short_positions en current.yaml documentado
[ ] short_candidates en watchlist documentado
[ ] direction en quality_universe documentado
```

### 2.3.4 tools-reference.md

```
[ ] TODOS los tools nuevos listados
[ ] TODOS los flags nuevos documentados
[ ] Reglas (precios via price_checker, screening via dynamic_screener) siguen vigentes
```

## 2.4 VERIFICACION DE STATE FILES

```
[ ] portfolio/current.yaml: seccion short_positions existe (vacia)
[ ] state/standing_orders.yaml: header actualizado, last_analysis_date en cada orden
[ ] state/watchlist.yaml: seccion short_candidates existe (vacia)
[ ] state/quality_universe.yaml: todas las entradas tienen direction: long
[ ] state/system.yaml: seccion exposure existe
[ ] state/pipeline_tracker.yaml: fragility_watch pipeline existe
[ ] state/calendar.yaml: soporte para short_catalyst type
```

## 2.5 VERIFICACION DE AGENT REGISTRY

```
[ ] Todos los agentes tienen responsabilidades actualizadas
[ ] Skills listados incluyen nuevos skills donde aplica
[ ] Lee/Escribe incluye thesis/short/ donde aplica
[ ] Mapa de dependencias actualizado con flujo short
[ ] Buy-pipeline flow incluye Short-pipeline flow (S1-S4)
```

## 2.6 VERIFICACION CLAUDE.md

```
[ ] Tabla de referencias tiene TODOS los skills nuevos
[ ] Tabla de tools tiene TODOS los tools nuevos/flags
[ ] Principios mencionan P10-P12
[ ] Nota sobre operacion bidireccional
```

## 2.7 VERIFICACION DE ANTI-SESGO

```
[ ] NINGUN tool nuevo emite juicio, etiqueta, o warning interpretativo
[ ] TODOS los tools terminan con "[Raw data. Reason from principles.md]"
[ ] NINGUN skill tiene thresholds fijos (porcentajes, ratios, etc.)
[ ] Error patterns #44-#47 no contienen numeros fijos
[ ] Principios P10-P12 son preguntas guia, no reglas
[ ] dcf_calculator.py --reverse NO dice "OVERVALUED" o "UNDERVALUED"
[ ] insider_tracker.py NO dice "BULLISH SIGNAL" o "BEARISH"
[ ] narrative_checker.py NO dice "WARNING" o "RED FLAG"
```

## 2.8 TEST INTEGRADO

Simular un flujo completo de sesion con el nuevo sistema:

```
1. Fase 0: Leer principles.md (confirmar P10-P12 presentes)
2. Fase 0: price_checker.py con standing orders (long + short si hay)
3. Fase 1: Simular news-monitor incluyendo shorts
4. Fase 2: portfolio_stats.py (confirmar net exposure aparece)
5. Fase 2.5: forward_return.py (confirmar seccion shorts aparece si hay)
6. Fase 3: Verificar standing orders (confirmar last_analysis_date visible)
7. Herramientas nuevas: dcf_calculator.py --reverse sobre 3 posiciones activas
8. Herramientas nuevas: insider_tracker.py sobre 2 posiciones
9. Herramientas nuevas: narrative_checker.py sobre 1 posicion
```

---

# PLAN 3: MIGRACION Y LIMPIEZA DEL PORTFOLIO

> **Objetivo:** Adaptar el portfolio actual y state files al nuevo sistema.
> **Cuando:** Despues de Plan 1 (implementacion) y Plan 2 (verificacion).

## 3.1 STANDING ORDERS — MIGRACION

### 3.1.1 Añadir `last_analysis_date` a cada orden

Recorrer las 22 standing orders y añadir:
```yaml
last_analysis_date: YYYY-MM-DD  # fecha de la thesis/committee que la aprobo
```

### 3.1.2 Clasificar por frescura

| Categoria | Criterio | Accion |
|-----------|----------|--------|
| FRESH | Analysis < 14 dias, sin earnings entre medio | Mantener como esta |
| AGING | Analysis 14-30 dias, o earnings pendientes | Marcar "revalidar antes de ejecutar" |
| STALE | Analysis > 30 dias | Marcar "REVALIDATION REQUIRED" |

### 3.1.3 Flag standing orders con WARNING

Ordenes sin pipeline adversarial completo:
- CMCSA ($26) — WARNING: No adversarial pipeline
- WPP.L (200p) — WARNING: No adversarial pipeline, UNDER REVIEW
- FGP.L (165p) — WARNING: No adversarial pipeline

**Accion:** Marcar como `status: REQUIRES_PIPELINE` en el YAML. No ejecutar sin completar pipeline.

### 3.1.4 Actualizar header del fichero

Cambiar de "Pre-approved, execute when price hits trigger" a "Price alerts with pre-written thesis. Fast-track validation required before execution."

### 3.1.5 Reverse DCF scan de standing orders cercanos

Ejecutar `dcf_calculator.py --reverse` sobre los standing orders mas cercanos al trigger:
- RSG (6.3% away)
- ROP (7.1% away)
- ADP (8.8% away)
- ACGL (10.6% away)
- FOUR.L (11.5% away)
- DSY.PA (15.0% away)

**Proposito:** Verificar si los triggers tienen sentido. Si el reverse DCF revela que el mercado ya implica pesimismo extremo a precio ACTUAL (no solo al trigger), razonar si comprar antes del trigger esta justificado.

## 3.2 POSICIONES ACTIVAS — NO REQUIEREN MIGRACION ESTRUCTURAL

Las 10 posiciones actuales son long. No cambia nada en su estructura.

**Acciones menores:**
- Verificar que TODAS tienen `conviction` y `exit_plan` en current.yaml (ya lo tienen)
- Verificar que TODAS tienen thesis con `> **Fair Value:** $XXX` header canonico

## 3.3 QUALITY UNIVERSE — MIGRACION

### 3.3.1 Añadir `direction: long` a todas las entradas

Script o edicion manual para añadir `direction: long` a las 76 entradas existentes.

### 3.3.2 Verificar integridad

```bash
python3 tools/quality_universe.py stats
```

Confirmar que count no cambio y que el campo direction aparece.

## 3.4 PORTFOLIO/CURRENT.YAML — AÑADIR SECCION

Añadir al final de positions (antes de transactions):

```yaml
short_positions: []
  # No short positions currently open.
  # System fully operational for shorts from this session forward.
```

## 3.5 SYSTEM.YAML — ACTUALIZAR

```yaml
session_number: 73  # o el que corresponda
last_session: 2026-02-XX

exposure:
  long_eur: XXXX  # calcular con portfolio_stats
  short_eur: 0
  net_eur: XXXX
  gross_eur: XXXX

strategic_direction:
  current: "Sistema unificado operativo. Capital deployment + contrathesis activa."
  rationale: "Sistema extendido a bidireccional. Buscar gaps en ambas direcciones."
  set_date: 2026-02-XX
```

## 3.6 WATCHLIST — AÑADIR SECCION

```yaml
short_candidates: []
  # No short candidates currently under analysis.
```

## 3.7 FIRST OPERATIONAL RUN

Despues de toda la migracion, ejecutar un ciclo completo de sesion normal:

```
1. Fase 0 completa (con nuevos principios + pre-execution check extendido)
2. Fase 1 (vigilancia incluyendo mencion de capacidad short)
3. Fase 2 (portfolio_stats con net exposure — sera 100% long, 0% short, correcto)
4. Fase 2.5 (forward_return — solo longs, correcto)
5. Fase 3 (standing orders con last_analysis_date visible)
6. Ejecutar reverse DCF sobre posiciones activas — primera data real del nuevo sistema
7. Ejecutar reverse DCF sobre standing orders cercanos — decision data
8. Evaluar: ¿hay gaps evidentes? ¿Algun trigger necesita ajuste?
9. Fase 5 (meta-reflexion — documentar primera sesion con sistema nuevo)
```

## 3.8 MEMORY — ACTUALIZAR

Actualizar MEMORY.md con:
- Session 73: Implementacion completa sistema unificado
- Nuevos tools, skills, principios
- Standing orders migrados
- Estado del sistema post-cambio

---

# RESUMEN EJECUTIVO

| Plan | Items | Estimacion |
|------|-------|------------|
| **Plan 1: Implementacion** | 3 principios, 4 errores, 2 tools nuevos, 1 flag nuevo, 9 tools modificados, 5 skills nuevos, 9 skills modificados, 5 rules, 7 state files, agent-registry, CLAUDE.md | ~1 sesion larga |
| **Plan 2: Verificacion** | 8 categorias de checks, test retrocompatibilidad, test anti-sesgo | ~30 min post-implementacion |
| **Plan 3: Migracion** | Standing orders (22), quality universe (76 entries), state files, first operational run | ~30 min post-verificacion |

**Riesgo principal:** Romper tools existentes al añadir soporte short. Mitigacion: test retrocompatibilidad ANTES de continuar (Plan 2.1.1).

**Criterio de exito:** Sesion normal funciona exactamente como antes para el portfolio 100% long. Sistema ADEMAS puede analizar, aprobar y ejecutar shorts si se detecta oportunidad.

---

*Documento creado: Session 73, 2026-02-18*
*Para mi yo futuro. Ejecutar en orden: Plan 1 → Plan 2 → Plan 3.*
