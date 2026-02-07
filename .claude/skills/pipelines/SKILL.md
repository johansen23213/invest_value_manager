# Pipelines - Rutinas Operativas del Fondo

> Framework v4.0 - Secuencias predefinidas de agentes con cadencia regular.
> Tracking de ejecucion en `state/system.yaml` seccion `pipeline_tracker`.

---

## Concepto

Los pipelines son **secuencias de agentes** que se ejecutan con cadencia regular.
Cada pipeline tiene: pasos definidos, agentes asignados, frecuencia, y tracking de ultima ejecucion.

El orchestrator consulta `pipeline_tracker` al inicio de cada sesion para determinar prioridades.

---

## PIPELINES PERIODICOS

### 1. `vigilance` | DIARIO

**Objetivo:** Detectar eventos que requieran accion inmediata.

| Paso | Accion | Ejecutor | Input | Output |
|------|--------|----------|-------|--------|
| 1a | Escanear noticias 48h posiciones + watchlist | `news-monitor` agent | WebSearch por ticker | state/news_digest.yaml |
| 1b | Detectar movimientos anomalos de precio | `market-pulse` agent | price_checker.py todas posiciones | state/market_pulse.yaml |
| | **1a y 1b en PARALELO** | | | |
| 2 | Si alerta CRITICA → investigar causa | Orchestrator | news_digest + market_pulse | Decision: STOP o continuar |
| 3 | Verificar standing orders vs precio actual | `watchlist-manager` agent | system.yaml standing_orders | Alertas de trigger cercano |
| 4 | Briefing estructurado al humano | Orchestrator | Todos los outputs anteriores | Resumen en pantalla |

**Condicion de salida:** Briefing presentado. Si CRITICO, no avanzar hasta resolver.

---

### 2. `rotation-check` | DIARIO

**Objetivo:** Verificar que el portfolio se mueve hacia mayor calidad.

| Paso | Accion | Ejecutor | Input | Output |
|------|--------|----------|-------|--------|
| 1 | Ranking posiciones por retorno esperado | `forward_return.py` tool | thesis files + yfinance | Ranking FER% |
| 2 | Evaluar Bottom 3 | Orchestrator | Ranking + thesis | Argumento para quedarse o rotar |
| 3 | Pipeline health | Orchestrator | system.yaml watchlist | Count thesis Tier A listas. Flag si <3 |
| 4 | Cash deployment | Orchestrator | Cash level + standing orders + Tier A MoS | Recomendacion deployment o reserva |
| 5 | Conviction update (si hay noticias materiales) | `portfolio-ops` agent | news_digest + earnings | portfolio/current.yaml actualizado |

**Condicion de salida:** Ranking presentado. Bottom 3 evaluado. Pipeline health reportado.

---

### 3. `opportunity-scan` | SEMANAL

**Objetivo:** Mantener pipeline de ideas lleno y detectar oportunidades.

| Paso | Accion | Ejecutor | Input | Output |
|------|--------|----------|-------|--------|
| 1 | Verificar alertas de precio activas | `watchlist-manager` agent | system.yaml price_monitors | Alertas actualizadas |
| 2 | Verificar standing orders cercanos (<5%) | `watchlist-manager` agent | system.yaml standing_orders | Ordenes near-trigger |
| 3 | Revisar sector views: candidatos pendientes | Orchestrator | world/sectors/*.md | Lista candidatos no analizados |
| 4 | Buscar oportunidades nuevas | `opportunity-hunter` agent | Sector views + screeners | Nuevos candidatos |
| 5 | Si pipeline <3 thesis → screening | `sector-screener` agent | dynamic_screener.py | Tickers nuevos |
| 6 | Si candidato Tier A → analisis rapido | `fundamental-analyst` agent | QS primero, thesis si Tier A | Thesis completa o descarte |
| 7 | Actualizar pipeline | `portfolio-ops` agent | Resultados anteriores | system.yaml actualizado |

**Condicion de salida:** Pipeline >=3 thesis listas. Standing orders revisados.

---

### 4. `risk-review` | SEMANAL

**Objetivo:** Detectar riesgos que no estoy viendo.

| Paso | Accion | Ejecutor | Input | Output |
|------|--------|----------|-------|--------|
| 1 | Scan riesgos legales/regulatorios | `risk-sentinel` agent | WebSearch por posicion | state/risk_alerts.yaml |
| 2 | Verificar world view freshness | Orchestrator | world/current_view.md timestamp | Flag si >7 dias |
| 2b | Si stale → actualizar macro | `macro-analyst` agent | WebSearch macro | world/current_view.md |
| 3 | Concentracion portfolio | `constraint_checker.py` REPORT | portfolio/current.yaml | Datos crudos |
| 4 | Correlaciones entre posiciones | `correlation_matrix.py` | yfinance historico | Matriz correlacion |
| 5 | Evaluar desde principios | Orchestrator | Datos pasos 1-4 + principles.md | Assessment de riesgo |
| 6 | Verificar earnings proximos 7 dias | `calendar-manager` agent | system.yaml calendar | Flag para earnings-pipeline |

**Condicion de salida:** Risk assessment presentado. World view fresh. Earnings proximos identificados.

---

### 5. `position-review` | QUINCENAL

**Objetivo:** Verificar que cada posicion merece estar en el portfolio.

| Paso | Accion | Ejecutor | Input | Output |
|------|--------|----------|-------|--------|
| 1 | Seleccionar batch 5-6 posiciones | Orchestrator | FER ranking (bottom first) | Batch seleccionado |
| 2 | Re-evaluar cada posicion | `review-agent` (batch) | Thesis + precio actual + noticias | HOLD/ADD/TRIM/SELL por posicion |
| 3 | Si SELL/TRIM → gate obligatorio | `investment-committee` agent | Review output | Aprobacion o rechazo |
| 4 | Si ADD → sizing | `position-calculator` agent | Principios + precedentes | Sizing recomendado |
| 5 | Actualizar conviction + exit_plan | `portfolio-ops` agent | Review results | portfolio/current.yaml |
| 6 | Actualizar last_review en thesis | Orchestrator | Fecha | thesis files |
| 7 | Registrar decisiones importantes | Orchestrator | Decisiones tomadas | decisions_log.yaml |

**Rotacion de batches:**
```
Ejecucion 1: Bottom 6 por FER
Ejecucion 2: Medio 6-7
Ejecucion 3: Top 6-7
Ciclo completo: ~6 semanas
```

**Condicion de salida:** Batch revisado. Conviction actualizada. Acciones pendientes identificadas.

---

### 6. `system-health` | QUINCENAL

**Objetivo:** Verificar que el sistema funciona correctamente.

| Paso | Accion | Ejecutor | Input | Output |
|------|--------|----------|-------|--------|
| 1 | Auditoria ficheros y consistencia | `health-check` agent | Todos los ficheros | Health score |
| 2 | Compactar memoria si necesario | `memory-manager` agent | Active memory size | Memoria optimizada |
| 3 | Detectar drift en decisiones | `drift_detector.py` | decisions_log.yaml | Drift alerts |
| 4 | Auditar tools por reglas hardcodeadas | Orchestrator/grep | tools/*.py, skills/*.md | Issues encontrados |
| 5 | Verificar sector views staleness | Orchestrator | world/sectors/*.md timestamps | Sectors >30 dias flagged |
| 6 | Verificar thesis completas | `health-check` agent | thesis/active/ | Missing conviction/exit_plan |

**Condicion de salida:** Health score calculado. Issues corregidos o documentados.

---

### 7. `deep-performance` | MENSUAL

**Objetivo:** Evaluar si la estrategia funciona.

| Paso | Accion | Ejecutor | Input | Output |
|------|--------|----------|-------|--------|
| 1 | P&L completo con attribution | `performance-tracker` agent | portfolio/current.yaml + history.yaml | Return por posicion |
| 2 | Metricas de efectividad | `effectiveness_tracker.py` | portfolio + history | Win rate, Sharpe |
| 3 | Attribution analysis | `performance-tracker` agent | Datos P&L | Alpha por sector/geo/tier |
| 4 | Analisis de decisiones del mes | Orchestrator | decisions_log.yaml | Que salio bien/mal |
| 5 | Quality trajectory | `portfolio_stats.py` + `forward_return.py` | Portfolio actual | Avg QS tendencia |
| 6 | Informe al humano | Orchestrator | Todos los datos | Resumen ejecutivo |
| 7 | Ajustes estrategicos | Orchestrator | Performance patterns | Cambios si necesario |

**Condicion de salida:** Informe mensual presentado. Lecciones documentadas.

---

### 8. `macro-refresh` | MENSUAL

**Objetivo:** Actualizar vision del mundo y conectar con portfolio.

| Paso | Accion | Ejecutor | Input | Output |
|------|--------|----------|-------|--------|
| 1 | Analisis macro completo | `macro-analyst` agent | WebSearch macro/geopolitica | Analisis |
| 2 | Actualizar world view | `macro-analyst` agent | Analisis | world/current_view.md |
| 3 | Comparar vs anterior | Orchestrator | Diff world view | Clasificar: COSMETICO/MENOR/MATERIAL/CRITICO |
| 4 | Si MATERIAL → flag dependencias | Orchestrator | Sector views + thesis | Posiciones NEEDS_REVIEW |
| 5 | Verificar sector views dependientes | Orchestrator | world/sectors/*.md | Sectors que necesitan update |
| 6 | Portfolio implications | Orchestrator | Macro context + portfolio | Cash strategy, sectores a evitar |

**Condicion de salida:** World view actualizado. Implicaciones para portfolio documentadas.

---

## PIPELINES EVENT-DRIVEN

### 9. `buy-pipeline` | Trigger: candidato identificado

**Objetivo:** Proceso completo desde idea hasta compra. Análisis iterativo y adversarial en 4 rondas.

**Estructura de ficheros por análisis:**
```
thesis/research/{TICKER}/
  thesis.md              ← fundamental-analyst
  moat_assessment.md     ← moat-assessor
  risk_assessment.md     ← risk-identifier
  valuation_report.md    ← valuation-specialist
  counter_analysis.md    ← devil's-advocate
  committee_decision.md  ← investment-committee
```

#### RONDA 0: PREPARACIÓN
| Paso | Accion | Ejecutor | Input | Output |
|------|--------|----------|-------|--------|
| 0 | Verificar sector view existe | Orchestrator | `Glob("world/sectors/*{sector}*")` | Si no existe → STOP, crear |

#### RONDA 1: ANÁLISIS PROFUNDO (en paralelo donde posible)
| Paso | Accion | Ejecutor | Input | Output |
|------|--------|----------|-------|--------|
| 1A | Análisis fundamental completo | `fundamental-analyst` agent | Empresa + sector view | thesis.md |
| 1B | Evaluación independiente de moat | `moat-assessor` agent | Ticker + sector view | moat_assessment.md |
| 1C | Identificación independiente de riesgos | `risk-identifier` agent | Ticker + macro view | risk_assessment.md |
| | **1A, 1B, 1C en PARALELO** | | | |
| 2 | Valoración multi-método | `valuation-specialist` agent | thesis + moat + risk | valuation_report.md |
| 3 | Procesar META-REFLECTIONs (4 agentes) | Orchestrator | Outputs agentes | Conflictos identificados |

#### RONDA 2: DESAFÍO
| Paso | Accion | Ejecutor | Input | Output |
|------|--------|----------|-------|--------|
| 4 | Contra-análisis independiente | `devil's-advocate` agent | thesis + moat + risk + valuation | counter_analysis.md |
| 5 | Comparar thesis vs contra-thesis | Orchestrator | thesis + counter_analysis | Clasificar: WEAK/MODERATE/STRONG |

#### RONDA 3: RESOLUCIÓN (solo si conflictos críticos, max 2 iteraciones)
| Paso | Accion | Ejecutor | Input | Output |
|------|--------|----------|-------|--------|
| 6 | Resolver conflictos clave | Orchestrator o agente relevante | Preguntas específicas | Respuestas documentadas |
| | *Se ejecuta SOLO si hay desafíos HIGH/CRITICAL no resueltos o divergencias materiales entre agentes* | | | |

#### RONDA 4: DECISIÓN
| Paso | Accion | Ejecutor | Input | Output |
|------|--------|----------|-------|--------|
| 7 | Gate de aprobación (10 gates) | `investment-committee` agent | TODO (thesis + counter + moat + risk + valuation) | committee_decision.md |
| 8 | Calcular sizing | `position-calculator` agent | Principios + precedentes | Sizing |
| 9 | Contextualizar recomendación | Skill `recommendation-context` | Timing + noticias + precio | Contexto completo |
| 10 | Presentar al humano | Orchestrator | Todo | Recomendación estructurada |
| 11 | Si confirma → actualizar state | `portfolio-ops` agent | Confirmación | portfolio + system.yaml + sector view |
| 12 | Si watchlist → standing order | Orchestrator | Trigger price | system.yaml standing_orders |

**Condición de salida:** Decisión tomada con audit trail completo (6 ficheros en thesis/research/{TICKER}/).

---

### 10. `sell-pipeline` | Trigger: position-review flag, kill condition

**Objetivo:** Proceso completo para decidir y ejecutar una venta.

| Paso | Accion | Ejecutor | Input | Output |
|------|--------|----------|-------|--------|
| 1 | Exit analysis | `review-agent` --exit-analysis | Thesis + precio actual | Assessment |
| 2 | Exit protocol - 6 gates | Skill `exit-protocol` | Assessment | Gate results |
| 3 | Opportunity Score | Orchestrator | MoS/QS actual vs candidato | OS calculado |
| 4 | Gate de aprobacion | `investment-committee` agent | Exit analysis + OS | SELL aprobado o no |
| 5 | Presentar al humano | Orchestrator | Todo | Recomendacion + destino capital |
| 6 | Si confirma → actualizar state | `portfolio-ops` agent | Confirmacion | thesis→archive, portfolio, sector view, history.yaml |

---

### 11. `earnings-pipeline` | Trigger: earnings en proximos 7 dias

**Objetivo:** Preparar antes, evaluar despues de earnings.

| Paso | Accion | Ejecutor | Input | Output |
|------|--------|----------|-------|--------|
| **PRE (3 dias antes):** | | | | |
| 1 | Preparar escenarios bear/base/bull | Orchestrator | Thesis + consensus | Framework pre-earnings |
| 2 | Verificar consensus estimates | WebSearch | Ticker + earnings | Expectativas mercado |
| 3 | Definir triggers de accion | Orchestrator | Scenarios | "Si X → TRIM, Si Y → ADD" |
| **POST (dia siguiente):** | | | | |
| 4 | Leer resultados | WebSearch | Earnings release | Datos reales |
| 5 | Re-evaluar thesis | `review-agent` agent | Resultados vs thesis | Assessment |
| 6 | Actualizar conviction + FV | `portfolio-ops` agent | Assessment | Thesis + portfolio actualizados |
| 7 | Si sorpresa material → decision | `investment-committee` agent | Assessment | ADD/TRIM/HOLD |

---

## TRACKING

### Formato en system.yaml

```yaml
pipeline_tracker:
  vigilance:
    frequency: daily
    last_run: 2026-02-07
    next_due: 2026-02-08
    last_result: "0 criticas, 6 materiales"
  rotation_check:
    frequency: daily
    last_run: 2026-02-07
    next_due: 2026-02-08
    last_result: "Bottom 3: A2A.MI, IMB.L, VICI"
  opportunity_scan:
    frequency: weekly
    last_run: null
    next_due: 2026-02-08
    last_result: null
  risk_review:
    frequency: weekly
    last_run: null
    next_due: 2026-02-08
    last_result: null
  position_review:
    frequency: biweekly
    last_run: null
    next_due: 2026-02-08
    last_result: null
    current_batch: "bottom"
  system_health:
    frequency: biweekly
    last_run: 2026-02-04
    next_due: 2026-02-18
    last_result: "9.1/10"
  deep_performance:
    frequency: monthly
    last_run: null
    next_due: 2026-02-08
    last_result: null
  macro_refresh:
    frequency: monthly
    last_run: 2026-02-02
    next_due: 2026-03-02
    last_result: "Tariffs + Iran up"
```

### Dashboard Display (inicio de sesion)

```
PIPELINES:
  OVERDUE: opportunity-scan (due 2/5), position-review (due 2/3)
  HOY:    vigilance, rotation-check
  OK:     risk-review (due 2/12), system-health (due 2/18)
  OK:     deep-performance (due 3/01), macro-refresh (due 3/02)
```

### Reglas de Prioridad

1. **OVERDUE** se ejecuta PRIMERO (en orden: vigilance > risk > rotation > opportunity > position > performance)
2. **Diarios** se ejecutan siempre
3. **Semanales** pueden combinarse en una sesion si no son pesados
4. **Event-driven** interrumpen la secuencia si son urgentes (kill condition, earnings hoy)

### Actualizacion del Tracker

Despues de ejecutar un pipeline:
1. Actualizar `last_run` con fecha actual
2. Calcular `next_due` segun frecuencia
3. Actualizar `last_result` con resumen breve
4. Si position-review: rotar `current_batch`
