---
name: agent-registry
description: Complete registry of all agents, their responsibilities, dependencies, and consistency protocol
user-invocable: false
---

# Agent Registry & Consistency Protocol (v4.1)

## Propósito
Documento de referencia ÚNICO para:
1. Inventario completo de agentes
2. Responsabilidades y single-responsibility principle
3. Skills que usa cada agente
4. Protocolo de propagación de cambios
5. Verificación de consistencia

---

## PASO 0 ESTÁNDAR (TODOS los agentes DEBEN seguir)

**CADA agente, al iniciar, DEBE:**

```markdown
## PASO 0: ONBOARDING OBLIGATORIO
**ANTES de ejecutar cualquier tarea:**
1. Leer `.claude/skills/system-context/SKILL.md` — Filosofía, ficheros clave, principios
2. Leer `.claude/skills/agent-registry/SKILL.md` — Mi rol, qué leo/escribo, dependencias
3. Leer skills específicos de mi dominio (listados en mi frontmatter)
4. Verificar que ficheros que voy a modificar existen y están en estado esperado
```

**TODOS los agentes tienen PASO 0 (actualizado 2026-02-05):**

| Dominio | Agente | PASO 0 |
|---------|--------|--------|
| **Vigilancia** | news-monitor | ✓ NUEVO |
| | market-pulse | ✓ NUEVO |
| | risk-sentinel | ✓ NUEVO |
| Inversión | fundamental-analyst | ✓ Completo |
| | investment-committee | ✓ Completo |
| | review-agent | ✓ Completo |
| | valuation-specialist | ✓ Completo |
| | moat-assessor | ✓ Añadido |
| | risk-identifier | ✓ Añadido |
| Research | opportunity-hunter | ✓ Completo |
| | sector-screener | ✓ Añadido |
| | macro-analyst | ✓ Completo |
| Portfolio | rebalancer | ✓ Añadido |
| | position-calculator | ✓ Añadido |
| | watchlist-manager | ✓ Añadido |
| | portfolio-ops | ✓ Añadido |
| | performance-tracker | ✓ Añadido |
| Sistema | calendar-manager | ✓ Tiene system-context |
| | health-check | ✓ Tiene system-context |
| | memory-manager | ✓ Añadido |
| | file-system-manager | ✓ Añadido |
| | system-evolver | ✓ Tiene system-context |
| | quant-tools-dev | ✓ Añadido |

---

## INVENTARIO DE AGENTES (24 total)

### Nivel 0: Orchestrator (CLAUDE.md)
El orchestrator (yo, Claude) delega a agentes especializados. Lee CLAUDE.md que contiene todas las reglas, protocolos y contexto.

---

### Dominio: VIGILANCIA (3) - NUEVO v2.2

> **Se ejecutan al INICIO de cada sesión, ANTES de cualquier otra cosa**

#### news-monitor
| Campo | Valor |
|-------|-------|
| Responsabilidad | Escanear noticias últimas 48h de todas las posiciones (long + short) y watchlist |
| Single-responsibility | Solo detecta y clasifica noticias, no decide acciones |
| Skills | news-classification, critical-thinking |
| Lee | portfolio/current.yaml (positions + short_positions), state/watchlist.yaml, state/standing_orders.yaml |
| Escribe | state/news_digest.yaml |
| Trigger | INICIO de cada sesión (Fase 0) |
| Alerta | CRÍTICO = STOP, informar humano inmediatamente |
| **Nuevo v4.1** | Para SHORT positions: noticias POSITIVAS = ALERTA (lógica invertida). Noticias que debilitan la tesis short son tan críticas como las que debilitan una tesis long. |

#### market-pulse
| Campo | Valor |
|-------|-------|
| Responsabilidad | Detectar movimientos anómalos de precio y buscar su CAUSA (long + short) |
| Single-responsibility | Solo detecta anomalías, no decide acciones |
| Skills | critical-thinking |
| Lee | portfolio/current.yaml (positions + short_positions), state/watchlist.yaml, state/standing_orders.yaml |
| Escribe | state/market_pulse.yaml |
| Tools | price_checker.py |
| Trigger | INICIO de cada sesión (en paralelo con news-monitor) |
| Alerta | Movimiento >5% sin causa = investigar |
| **Nuevo v4.1** | Para SHORTs: subida >5% sin causa = alerta (movimiento adverso). Bajada >5% en short = confirmación (positivo para portfolio). |

#### risk-sentinel
| Campo | Valor |
|-------|-------|
| Responsabilidad | Vigilar litigios, investigaciones regulatorias, cambios legales |
| Single-responsibility | Solo detecta riesgos exógenos, no valora empresas |
| Skills | risk-assessment, critical-thinking |
| Lee | portfolio/current.yaml, thesis/active/*, state/risk_alerts.yaml |
| Escribe | state/risk_alerts.yaml, actualiza thesis si detecta riesgo nuevo |
| Trigger | Semanal + on-demand |
| Alerta | ROJO = posible thesis-killer, evaluar SELL |

---

### Dominio: INVERSIÓN (5 principales + 3 independientes)

#### fundamental-analyst
| Campo | Valor |
|-------|-------|
| Responsabilidad | Análisis profundo de empresas con Framework v4.0 (LONG y SHORT) |
| Single-responsibility | Crea thesis completa con 5 fases obligatorias |
| Skills | business-analysis-framework, projection-framework, valuation-methods, thesis-template, agent-meta-reflection, **contrathesis-framework**, **short-thesis-framework** |
| Lee | world/current_view.md, **world/sectors/{sector}.md**, portfolio/current.yaml |
| Escribe | thesis/research/{TICKER}/thesis.md **o** thesis/short/research/{TICKER}/thesis.md |
| Dependencias | sector view DEBE existir antes de valorar |
| **v4.0** | Ya no delega a micro-agentes. El orchestrator lanza moat/risk/valuation en paralelo |
| **v4.1** | Cuando invocado con --short-thesis: invierte analisis, busca fragilidad. Usa short-thesis-framework |

#### investment-committee
| Campo | Valor |
|-------|-------|
| Responsabilidad | Gate obligatorio de **10 gates** antes de BUY/SELL. **SHORT_APPROVAL mode** para shorts (10+3 gates) |
| Single-responsibility | Valida que análisis es completo y decisión sólida. Evalúa thesis vs contra-thesis |
| Skills | investment-rules, portfolio-constraints, decision-template, committee-decision-template, business-analysis-framework, projection-framework, valuation-methods, sector-deep-dive, agent-meta-reflection, **short-thesis-framework**, **cover-protocol** |
| Lee | world/current_view.md, **world/sectors/{sector}.md**, portfolio/current.yaml, thesis del ticker, **counter_analysis.md, moat_assessment.md, risk_assessment.md, valuation_report.md** |
| Escribe | thesis/research/{TICKER}/committee_decision.md **o** thesis/short/research/{TICKER}/committee_decision.md |
| Dependencias | sector view DEBE existir (Gate 8). Counter-analysis evaluado (Gate 10) |
| **v4.0** | Gate 10: Counter-Analysis Gate. Desafíos CRITICAL deben resolverse antes de aprobar |
| **v4.1** | SHORT_APPROVAL mode: 3 gates adicionales — SHORT-1 (catalizador P10), SHORT-2 (asimetria P11), SHORT-3 (mejora portfolio total P12) |

#### review-agent
| Campo | Valor |
|-------|-------|
| Responsabilidad | Re-evaluación de posiciones activas (LONG y SHORT) con Framework v4.0 |
| Single-responsibility | Compara thesis vs realidad, recomienda HOLD/ADD/TRIM/SELL (longs) o HOLD/COVER (shorts) |
| Skills | re-evaluation-protocol, business-analysis-framework, projection-framework, valuation-methods, investment-rules, agent-meta-reflection, **cover-protocol** |
| Lee | world/current_view.md, **world/sectors/{sector}.md**, thesis/active/{TICKER}/ **o** thesis/short/active/{TICKER}/ |
| Escribe | Actualiza thesis con v4.0, journal/reviews/ |
| Dependencias | sector view DEBE existir antes de re-evaluar |
| **v4.1** | Output incluye conviction (high/medium/low) y exit_plan actualizado. --short-review mode: verifica fragilidad intacta, catalizador vigente, carry aceptable |

#### devil's-advocate (NUEVO)
| Campo | Valor |
|-------|-------|
| Responsabilidad | Contra-análisis adversarial independiente de thesis (LONG y SHORT) |
| Single-responsibility | Solo desafía, no decide. Busca evidencia en contra |
| Skills | critical-thinking, business-analysis-framework, valuation-methods, agent-meta-reflection, **contrathesis-framework** |
| Lee | thesis/research/{TICKER}/ **o** thesis/short/research/{TICKER}/ |
| Escribe | counter_analysis.md en el directorio correspondiente |
| Trigger | Después de Ronda 1 del buy-pipeline o S1 del short-pipeline |
| Output | Veredicto: WEAK COUNTER / MODERATE COUNTER / STRONG COUNTER |
| **v4.1** | Para shorts: Devil's advocate BULL — por que podria el precio tener razon? Prompt invertido |

#### valuation-specialist (independiente)
| Campo | Valor |
|-------|-------|
| Responsabilidad | Cálculo independiente de fair value multi-método |
| Single-responsibility | Solo calcula valor, no decide |
| Skills | valuation-methods, projection-framework, dcf-template, comparables-method, agent-meta-reflection |
| Lee | thesis.md + moat_assessment.md + risk_assessment.md, learning/principles.md, decisions_log.yaml |
| Escribe | thesis/research/{TICKER}/valuation_report.md |
| Dependencias | Preferible después de thesis + moat + risk para tener contexto completo |
| META-REFLECTION | SI — incluye sensibilidad, discrepancias, dudas |

#### moat-assessor (independiente)
| Campo | Valor |
|-------|-------|
| Responsabilidad | Evaluación independiente de ventajas competitivas |
| Single-responsibility | Solo evalúa moat con investigación propia. Puede discrepar con thesis |
| Skills | moat-framework, business-analysis-framework, critical-thinking, agent-meta-reflection |
| Lee | Ticker + sector view. Puede leer thesis si existe, pero investiga independientemente |
| Escribe | thesis/research/{TICKER}/moat_assessment.md |
| META-REFLECTION | SI — incluye discrepancias con thesis, incertidumbres |

#### risk-identifier (independiente)
| Campo | Valor |
|-------|-------|
| Responsabilidad | Identificación activa de riesgos con investigación independiente |
| Single-responsibility | Solo identifica riesgos. Busca lo que la thesis NO dice |
| Skills | risk-assessment, critical-thinking, agent-meta-reflection |
| Lee | Ticker + macro view + thesis (si existe). WebSearch obligatorio para litigación/regulación |
| Escribe | thesis/research/{TICKER}/risk_assessment.md |
| META-REFLECTION | SI — incluye riesgos subestimados, kill conditions sugeridas |

---

### Dominio: RESEARCH (3)

#### opportunity-hunter
| Campo | Valor |
|-------|-------|
| Responsabilidad | Búsqueda sistemática de oportunidades anti-sesgo |
| Single-responsibility | Encuentra candidatos de forma sistemática, no los analiza profundamente |
| Skills | screening-protocol, critical-thinking, agent-meta-reflection |
| Lee | world/sectors/*.md, state/watchlist.yaml, state/standing_orders.yaml |
| Escribe | N/A (output directo al orchestrator) |
| Dependencias | Usa dynamic_screener.py, verifica sector views existen |
| Cuándo usar | Cash sin oportunidades claras, búsqueda de ideas, post-venta, proactivamente semanal |
| **Nuevo v4.1** | Priorizar candidatos Tier A (QS >=75). Quality compounders son el objetivo principal |

#### sector-screener
| Campo | Valor |
|-------|-------|
| Responsabilidad | Screening sistemático de sectores |
| Single-responsibility | Encuentra empresas, no las analiza profundamente |
| Skills | screening-protocol, critical-thinking |
| Lee | **world/sectors/{sector}.md** (o crea si no existe) |
| Escribe | journal/log/, **world/sectors/{sector}.md** (crea/actualiza) |
| Dependencias | DEBE crear sector view ANTES de screening si no existe |

#### macro-analyst
| Campo | Valor |
|-------|-------|
| Responsabilidad | Análisis macro con implicaciones ACCIONABLES (long + short) |
| Single-responsibility | Actualiza world view, conecta macro con decisiones |
| Skills | macro-framework, critical-thinking |
| Lee | world/current_view.md, portfolio/current.yaml (positions + short_positions) |
| Escribe | world/current_view.md, **world/sectors/{sector}.md** (cuando aplica) |
| **Nuevo v4.1** | Output incluye "Portfolio Implications" - mapeo de macro a posiciones concretas (tailwind/headwind). Para shorts: macro headwinds para la empresa = tailwinds para el short. Incluye "Net Exposure Implications" cuando hay macro shift. |

---

### Dominio: PORTFOLIO (5)

#### rebalancer
| Campo | Valor |
|-------|-------|
| Responsabilidad | Rebalanceo por sizing + quality ranking + rotation opportunities |
| Single-responsibility | Identifica desviaciones de sizing Y calidad, propone ajustes |
| Skills | portfolio-constraints, investment-rules, **rotation-engine** |
| Lee | portfolio/current.yaml, **learning/principles.md** (Principio 9) |
| Escribe | journal/decisions/ |
| **Nuevo v4.1** | Ejecuta forward_return.py, evalúa bottom 3 posiciones, verifica pipeline |

#### position-calculator
| Campo | Valor |
|-------|-------|
| Responsabilidad | Cálculo de sizing óptimo (long + short) |
| Single-responsibility | Solo calcula, no decide |
| Skills | portfolio-constraints |
| Lee | portfolio/current.yaml (positions + short_positions), learning/principles.md (P10-P14 para portfolio bidireccional) |
| Escribe | N/A (output directo) |
| **Nuevo v4.1** | Para SHORTs: incluir carry cost anual (~7-8% eToro CFD) en cálculo, reasoning sobre duración esperada (P10 catalizador), output incluye "Carry Cost Impact" y "Max Loss Scenario" (squeeze risk P11). |

#### watchlist-manager
| Campo | Valor |
|-------|-------|
| Responsabilidad | Monitoreo de watchlist y triggers (long + short candidates) |
| Single-responsibility | Verifica triggers, recomienda acciones |
| Skills | investment-rules, portfolio-constraints |
| Lee | state/watchlist.yaml (incluyendo short_candidates section) |
| Escribe | state/watchlist.yaml |
| **Nuevo v4.1** | Sección short_candidates en watchlist.yaml. Para shorts: trigger = precio >= target (invertido). Monitorea catalizadores de fragilidad (P10). |

#### portfolio-ops
| Campo | Valor |
|-------|-------|
| Responsabilidad | Centraliza TODAS las escrituras de estado (long + short) |
| Single-responsibility | Solo escribe estado, no decide |
| Skills | portfolio-constraints, file-system-rules |
| Lee | portfolio/current.yaml (positions + short_positions), state/*.yaml (as needed) |
| Escribe | portfolio/current.yaml (positions + short_positions), state/*.yaml (tras confirmación humano) |
| **Nuevo v4.1** | Soporta 4 operaciones: BUY/SELL (longs → positions), SHORT/COVER (shorts → short_positions). Maneja campos conviction, exit_plan, last_review, y para shorts: carry_cost_annual, catalyst_date, entry_price (= precio al shortear). Mueve thesis entre thesis/short/research/ → thesis/short/active/ → thesis/archive/. |

#### performance-tracker
| Campo | Valor |
|-------|-------|
| Responsabilidad | Tracking de performance vs benchmark |
| Single-responsibility | Solo mide, no decide |
| Skills | portfolio-constraints |
| Lee | portfolio/current.yaml |
| Escribe | journal/reviews/ |

---

### Dominio: SISTEMA (5)

#### calendar-manager
| Campo | Valor |
|-------|-------|
| Responsabilidad | Gestión de calendario de eventos |
| Single-responsibility | Verifica fechas, alerta eventos |
| Skills | system-context |
| Lee | state/calendar.yaml |
| Escribe | state/calendar.yaml |

#### health-check
| Campo | Valor |
|-------|-------|
| Responsabilidad | Auditoría de salud del sistema cada 14 días |
| Single-responsibility | Verifica consistencia, no corrige |
| Skills | system-context, file-system-rules |
| Lee | Todo el sistema |
| Escribe | state/pipeline_tracker.yaml (health_score, issues) |
| Verifica | **Sector views existen para posiciones activas** |
| **Nuevo v4.1** | Verificar: todas las posiciones tienen conviction y exit_plan. forward_return.py ejecutado en sesión |

#### memory-manager
| Campo | Valor |
|-------|-------|
| Responsabilidad | Gestión de memoria 3 capas |
| Single-responsibility | Compacta y archiva, no crea contenido |
| Skills | memory-management-rules, summarization-template |
| Lee | Capa 1 memoria activa |
| Escribe | archive/, índices |

#### file-system-manager
| Campo | Valor |
|-------|-------|
| Responsabilidad | Autoridad ÚNICA sobre ubicación de ficheros |
| Single-responsibility | Decide dónde escribir, mueve ficheros |
| Skills | file-system-rules |
| Lee | Estructura de directorios |
| Escribe | state/file_moves.yaml |
| Conoce | **world/sectors/** como ubicación de sector views |

#### system-evolver
| Campo | Valor |
|-------|-------|
| Responsabilidad | Auto-mejora del sistema |
| Single-responsibility | Evalúa, propone, aplica cambios |
| Skills | evolution-protocol, system-context |
| Lee | Docs oficiales, sistema completo |
| Escribe | Agentes, skills, CLAUDE.md |

#### quant-tools-dev
| Campo | Valor |
|-------|-------|
| Responsabilidad | Desarrollo de herramientas Python |
| Single-responsibility | Crea tools reutilizables, no análisis |
| Skills | portfolio-constraints |
| Lee | tools/ existentes |
| Escribe | tools/*.py |

---

## PROTOCOLO DE CONSISTENCIA

### Principio Core
**Cuando hay un cambio sistémico, TODOS los agentes afectados DEBEN actualizarse en la misma sesión.**

### Tipos de Cambios y Propagación

#### Cambio Tipo A: Nuevo Skill/Framework
**Ejemplo:** Se crea business-analysis-framework
**Propagación:**
1. Identificar agentes que DEBEN usarlo
2. Actualizar PASO 0 de cada agente
3. Actualizar lista de skills en frontmatter
4. Verificar que output del agente refleja el framework
5. Documentar en agent-registry

#### Cambio Tipo B: Nueva Estructura de Ficheros
**Ejemplo:** Se crea world/sectors/
**Propagación:**
1. Actualizar file-system-rules skill
2. Actualizar file-system-manager agent
3. Identificar agentes que deben leer/escribir esa ubicación
4. Actualizar PASO 0 de agentes lectores
5. Actualizar sección "Escribe" de agentes escritores
6. Actualizar health-check para verificar existencia
7. Documentar en CLAUDE.md

#### Cambio Tipo C: Nuevo Tool
**Ejemplo:** Se crea constraint_checker.py
**Propagación:**
1. Documentar en quant-tools-dev agent
2. Identificar agentes que deben usarlo
3. Actualizar proceso de esos agentes
4. Añadir a CLAUDE.md sección Tools

### Checklist de Propagación de Cambios

```
ANTES de considerar un cambio "completo":

[ ] ¿Qué agentes leen esto? → Actualizar PASO 0
[ ] ¿Qué agentes escriben esto? → Actualizar sección "Escribe"
[ ] ¿Qué skills definen el framework? → Actualizar skill
[ ] ¿file-system-rules conoce la ubicación? → Actualizar si es fichero nuevo
[ ] ¿health-check debe verificarlo? → Añadir check
[ ] ¿CLAUDE.md lo documenta? → Añadir sección
[ ] ¿agent-registry está actualizado? → Actualizar este fichero
[ ] ¿Hay agentes redundantes? → Consolidar si aplica
```

### Verificación de Consistencia (ejecutar periódicamente)

```bash
# Verificar que todos los skills referenciados existen
grep -r "skills:" .claude/agents/ | # extraer skills | verificar existencia

# Verificar que ficheros en PASO 0 existen
grep -r "Read " .claude/agents/ | # extraer paths | verificar existencia

# Verificar que no hay agentes duplicados
# Comparar descriptions de agentes
```

---

## REGLAS DE SINGLE RESPONSIBILITY

### Por qué importa
- Agentes atómicos son más fáciles de mantener
- Cambios en un dominio no rompen otros
- Debugging más simple
- Composabilidad: combinar agentes pequeños > 1 agente grande

### Violaciones a evitar
1. **Agente que decide Y escribe estado** → Separar en 2: uno decide, otro escribe
2. **Agente que analiza Y vigila** → Separar análisis profundo de monitoreo
3. **Skill demasiado grande** → Dividir en sub-skills
4. **Agente sin skill propio** → Probablemente debería ser parte de otro agente

### Test de atomicidad
Para cada agente, preguntar:
1. ¿Puedo describir su responsabilidad en 1 oración?
2. ¿Tiene una razón clara para existir separado?
3. ¿Hay otro agente que hace lo mismo?

---

## MAPA DE DEPENDENCIAS

```
                    ┌─────────────────────┐
                    │    ORCHESTRATOR     │
                    │    (CLAUDE.md)      │
                    └──────────┬──────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
        ▼                      ▼                      ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│   INVERSIÓN   │    │   PORTFOLIO   │    │    SISTEMA    │
├───────────────┤    ├───────────────┤    ├───────────────┤
│fundamental-   │    │rebalancer     │    │calendar-mgr   │
│analyst ──────────┐ │position-calc  │    │health-check   │
│               │  │ │watchlist-mgr  │    │memory-mgr     │
│moat-assessor ─┤  │ │portfolio-ops  │    │file-system-mgr│
│risk-identifier┤  │ │performance    │    │system-evolver │
│valuation-spec ┤  │ └───────────────┘    │quant-tools-dev│
│               │  │                      └───────────────┘
│devil's-       │  │  ← Desafía thesis
│advocate ──────┘  │
│               │  │
│investment-    │◀─┘  ← Recibe TODO (thesis + counter + moat + risk + valuation)
│committee      │
│review-agent   │
└───────────────┘
        │
        │ ◀── depende de ──▶
        ▼
┌───────────────┐
│   RESEARCH    │
├───────────────┤
│opportunity-   │
│hunter         │
│sector-screener│
│macro-analyst  │
└───────────────┘
        │
        ▼
┌───────────────────────────────────────┐
│           SECTOR VIEWS                │
│     world/sectors/{sector}.md         │
│                                       │
│  Creado por: sector-screener          │
│              fundamental-analyst      │
│              macro-analyst            │
│                                       │
│  Leído por:  fundamental-analyst      │
│              investment-committee     │
│              review-agent             │
│              devil's-advocate         │
│                                       │
│  Verificado: health-check             │
└───────────────────────────────────────┘

BUY-PIPELINE FLOW:
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│fundamental-  │   │moat-assessor │   │risk-identifier│
│analyst       │   │              │   │              │
│→ thesis.md   │   │→ moat_assess │   │→ risk_assess │
└──────┬───────┘   └──────┬───────┘   └──────┬───────┘
       │  RONDA 1 (PARALELO)  │               │
       └──────────┬───────────┘───────────────┘
                  ▼
       ┌──────────────────┐
       │valuation-        │
       │specialist        │  RONDA 1 (secuencial)
       │→ valuation_report│
       └────────┬─────────┘
                ▼
       ┌──────────────────┐
       │devil's-advocate  │  RONDA 2
       │→ counter_analysis│
       └────────┬─────────┘
                ▼
       ┌──────────────────┐
       │investment-       │  RONDA 4
       │committee (10 g.) │
       │→ committee_dec.  │
       └──────────────────┘
```

---

## ACTUALIZACIÓN DE ESTE DOCUMENTO

**Cuándo actualizar agent-registry:**
- Se crea nuevo agente
- Se elimina agente
- Cambian responsabilidades de agente
- Se añade nuevo skill a agente
- Cambia dependencia (qué lee/escribe)

**Quién actualiza:**
- system-evolver (durante evaluaciones)
- Orchestrator (cuando hace cambios manuales)

**Frecuencia mínima:**
- Verificar cada 14 días (junto con health-check)
