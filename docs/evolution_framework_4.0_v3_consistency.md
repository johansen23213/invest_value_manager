# Framework v4.0 - Anexo D: Implementación de Consistencia

> **DOCUMENTO CRÍTICO**: Este documento resuelve los gaps de consistencia identificados
> ANTES de implementar v4.0. Sin resolver esto, v4.0 sería inconsistente entre sesiones.
> Creado: 2026-02-05, Sesión 37

---

## TABLA DE CONTENIDOS

1. [El Problema de Consistencia](#1-el-problema-de-consistencia)
2. [Arquitectura de Flujo de Información v4.0](#2-arquitectura-de-flujo-de-información)
3. [Redefinición de Agentes Críticos](#3-redefinición-de-agentes-críticos)
4. [Mecanismo de Validación de Consistencia](#4-mecanismo-de-validación-de-consistencia)
5. [Protocolo de Detección de Drift](#5-protocolo-de-detección-de-drift)
6. [Session Bootstrap v4.0](#6-session-bootstrap-v40)
7. [Investment Committee v4.0 - Nuevos Gates](#7-investment-committee-v40)
8. [Tools Actualizados](#8-tools-actualizados)
9. [Checklist de Verificación](#9-checklist-de-verificación)

---

## 1. EL PROBLEMA DE CONSISTENCIA

### 1.1 Cómo Funciona v3.0 (Consistencia por Números)

```
┌─────────────────────────────────────────────────────────────────┐
│                    CONSISTENCIA v3.0                            │
│                                                                 │
│  CLAUDE.md ──────> "Max 7% posición"                            │
│       │                                                         │
│       ├──> skills/investment-rules ──> "Max 7%"                 │
│       │                                                         │
│       ├──> constraint_checker.py ──> if pos > 7%: REJECT        │
│       │                                                         │
│       ├──> investment-committee ──> Gate: verify < 7%           │
│       │                                                         │
│       └──> fundamental-analyst ──> "Recomiendo max 7%"          │
│                                                                 │
│  RESULTADO: Todos dicen lo mismo porque leen el mismo número    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Ventaja**: Imposible ser inconsistente - el número es el número.
**Problema**: Rigidez que destruye valor (vender ganador solo por %).

### 1.2 El Riesgo de v4.0 Sin Resolver Consistencia

```
┌─────────────────────────────────────────────────────────────────┐
│                    RIESGO v4.0 MAL IMPLEMENTADO                 │
│                                                                 │
│  Sesión 38: "ADBE a 9% está bien, tesis intacta"                │
│  Sesión 39: "TEP.PA a 8% es demasiado, TRIM"                    │
│  Sesión 40: "NVO a 10% está bien, quality compounder"           │
│  Sesión 41: "MONY.L a 7.5% es excesivo, TRIM"                   │
│                                                                 │
│  ¿Por qué inconsistencia? Porque cada sesión "razoné" diferente │
│  sin ancla ni validación de coherencia.                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 1.3 La Solución: Consistencia por Razonamiento Validado

```
┌─────────────────────────────────────────────────────────────────┐
│                    CONSISTENCIA v4.0 CORRECTA                   │
│                                                                 │
│  1. PRINCIPIOS: Guías de pensamiento (sin números)              │
│                                                                 │
│  2. PRECEDENTES: Decisiones pasadas documentadas                │
│      ↓                                                          │
│  3. VALIDACIÓN: Antes de decidir, comparo con precedentes       │
│      ↓                                                          │
│  4. RAZONAMIENTO: Documento POR QUÉ esta decisión               │
│      ↓                                                          │
│  5. DETECCIÓN: Sistema alerta si hay drift o inconsistencia     │
│                                                                 │
│  RESULTADO: Consistencia por coherencia de razonamiento,        │
│             no por número fijo                                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. ARQUITECTURA DE FLUJO DE INFORMACIÓN

### 2.1 Decisión de Diseño: Orchestrator como Intérprete Central

**Opciones consideradas:**

| Opción | Descripción | Problema |
|--------|-------------|----------|
| A | Todos los agentes leen principles.md | Interpretación diferente por cada agente |
| B | Solo orchestrator razona | Bottleneck, si olvido algo falla |
| C | **Híbrido** | Orchestrator interpreta, agentes reciben guidance específica |

**Decisión: OPCIÓN C (Híbrido)**

```
┌─────────────────────────────────────────────────────────────────┐
│                    FLUJO DE INFORMACIÓN v4.0                    │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │               ORCHESTRATOR (Claude)                      │    │
│  │                                                          │    │
│  │  Lee al inicio de sesión:                                │    │
│  │  • CLAUDE.md (versión v4.0)                              │    │
│  │  • principles.md                                         │    │
│  │  • decisions_log.yaml (últimas 15 entradas)              │    │
│  │  • last_session_summary                                  │    │
│  │                                                          │    │
│  │  Genera para la sesión:                                  │    │
│  │  • "Session Guidance" mental con contexto                │    │
│  │  • Conocimiento de precedentes relevantes                │    │
│  └─────────────────────────────────────────────────────────┘    │
│                           │                                     │
│                           │ Cuando delega a agente:             │
│                           ▼                                     │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │                    AGENTES                               │    │
│  │                                                          │    │
│  │  Reciben en prompt:                                      │    │
│  │  • Su skill especializado (investment-rules v4.0, etc.)  │    │
│  │  • Contexto específico de la tarea                       │    │
│  │  • Precedentes relevantes SI aplica                      │    │
│  │                                                          │    │
│  │  NO necesitan leer:                                      │    │
│  │  • principles.md (ya interpretado por orchestrator)      │    │
│  │  • Todo el decisions_log (solo precedentes relevantes)   │    │
│  └─────────────────────────────────────────────────────────┘    │
│                           │                                     │
│                           │ Agente retorna:                     │
│                           ▼                                     │
│  ┌─────────────────────────────────────────────────────────┐    │
│  │              ORCHESTRATOR VALIDA                         │    │
│  │                                                          │    │
│  │  • ¿Output es coherente con principios?                  │    │
│  │  • ¿Es coherente con precedentes?                        │    │
│  │  • Si no → re-ejecutar con más contexto o corregir       │    │
│  │  • Si sí → proceder y documentar decisión                │    │
│  └─────────────────────────────────────────────────────────┘    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 Qué Lee Cada Componente

| Componente | Lee | No Lee |
|------------|-----|--------|
| **Orchestrator (yo)** | CLAUDE.md, principles.md, decisions_log.yaml (todo), session_summary | - |
| **fundamental-analyst** | business-analysis-framework, valuation-methods, QS del ticker | decisions_log completo |
| **investment-committee** | investment-rules v4.0, EXIT protocol, precedentes RELEVANTES (los paso yo) | principles.md directamente |
| **constraint_checker.py** | decisions_log.yaml (para comparar), portfolio actual | principles.md |
| **rebalancer** | portfolio actual, thesis de cada posición | decisions_log |
| **review-agent** | thesis específica, últimos earnings, EXIT protocol | - |
| **health-check** | Todo (para auditoría) | - |

### 2.3 El Rol del Orchestrator

**Antes (v3.0):** Router que delega tareas
**Ahora (v4.0):** Intérprete central que:

1. **Lee y entiende** principios y precedentes
2. **Contextualiza** antes de delegar (da a agentes la información que necesitan)
3. **Valida** outputs de agentes contra principios
4. **Documenta** cada decisión importante en decisions_log
5. **Detecta** inconsistencias antes de que se ejecuten

---

## 3. REDEFINICIÓN DE AGENTES CRÍTICOS

### 3.1 fundamental-analyst v4.0

**Cambio principal:** No recomienda sizing específico. Analiza calidad y valuation.

```markdown
# CAMBIOS EN fundamental-analyst

ANTES (v3.0):
  Output incluía: "Recomendación: BUY 4% del portfolio"
  Basado en: Tier A = max 7%, recomiendo 4% inicial

AHORA (v4.0):
  Output incluye:
    - Quality Score y Tier
    - Fair Value y MoS
    - Análisis de riesgo
    - Catalizadores
    - NO incluye sizing específico

  El SIZING lo decide orchestrator considerando:
    - Convicción basada en análisis
    - Contexto del portfolio actual
    - Precedentes similares
    - Principios de sizing

RAZÓN:
  El sizing depende del contexto del portfolio (correlaciones,
  exposición actual, cash disponible) que fundamental-analyst
  no tiene visibilidad completa.
```

**Nuevo output de fundamental-analyst:**

```yaml
analysis_output:
  ticker: NVO
  quality_score: 82
  tier: A
  fair_value: 78 EUR
  current_price: 48 EUR
  mos: 38%
  conviction_level: HIGH  # Nueva métrica cualitativa
  conviction_rationale: |
    - #1 en GLP-1, mercado de $100B+
    - QS 82 excepcional
    - MoS 38% muy superior al requerido para Tier A
    - Catalizador claro (CagriSema data Marzo)
  risks:
    - CagriSema data negativa invalida thesis
    - Competition de ELI

  # NO incluye sizing recomendado
  # Orchestrator decide sizing basado en esto + contexto portfolio
```

### 3.2 investment-committee v4.0

**Cambio principal:** Gates reformulados para validar razonamiento, no números.

Ver sección 7 para detalle completo de los nuevos gates.

### 3.3 constraint_checker.py v4.0

**Cambio principal:** No rechaza. Advierte y proporciona contexto de precedentes.

```python
# ANTES (v3.0):
def check_position(ticker, amount):
    if resulting_position > 0.07:
        return {"status": "REJECTED", "reason": "Exceeds 7% limit"}

# AHORA (v4.0):
def check_position(ticker, amount):
    resulting_position = calculate_position(ticker, amount)
    tier = get_quality_tier(ticker)
    similar_precedents = find_similar_decisions(ticker, tier)

    return {
        "status": "ADVISORY",  # Nunca REJECTED
        "resulting_position": f"{resulting_position:.1%}",
        "tier": tier,
        "context": {
            "current_portfolio_concentration": get_concentration_analysis(),
            "similar_precedents": similar_precedents,
            "questions_to_consider": [
                f"¿Tu convicción justifica {resulting_position:.1%}?",
                f"Si cae 50%, pierdes {resulting_position/2:.1%} del portfolio. ¿Aceptable?",
                "¿Hay correlación con otras posiciones?"
            ]
        }
    }
```

### 3.4 rebalancer v4.0

**Cambio principal:** No usa triggers fijos. Identifica outliers para revisión.

```markdown
# CAMBIOS EN rebalancer

ANTES (v3.0):
  IF position > 1.3x target THEN TRIM
  IF position < 0.7x target THEN ADD

AHORA (v4.0):
  1. Identificar posiciones "outlier" (significativamente diferentes de sizing típico)
  2. Para cada outlier, generar pregunta:
     - "ADBE ahora es 9.2% del portfolio. ¿Revisar?"
  3. Orchestrator decide:
     - Si tesis intacta + MoS positivo → HOLD justificado
     - Si tesis debilitada o mejor oportunidad → TRIM con razonamiento
  4. Documentar decisión en decisions_log

  NO hay TRIM automático por regla.
```

### 3.5 review-agent v4.0

**Cambio principal:** Añade EXIT Protocol completo.

```markdown
# CAMBIOS EN review-agent

ANTES (v3.0):
  - Revisa post-earnings
  - Verifica kill conditions
  - Recomienda HOLD/ADD/TRIM

AHORA (v4.0):
  - Todo lo anterior PLUS:
  - Ejecuta EXIT Protocol completo (6 gates)
  - Calcula Opportunity Score vs. watchlist
  - Output incluye:
    - Recommendation con razonamiento
    - EXIT analysis si aplica
    - Comparación con precedentes de decisiones similares
```

### 3.6 health-check v4.0

**Cambio principal:** Añade verificación de consistencia de decisiones.

```markdown
# NUEVAS VERIFICACIONES EN health-check

NUEVOS CHECKS v4.0:

1. DECISIONS_LOG HEALTH
   - ¿Hay entradas en las últimas 7 días?
   - ¿Cada entrada tiene razonamiento completo?
   - ¿Hay entradas huérfanas (sizing sin contexto)?

2. CONSISTENCY CHECK
   - Analizar decisiones de sizing de últimos 30 días
   - ¿Hay decisiones similares con outcomes muy diferentes?
   - ¿Hay tendencias (drift) en sizing promedio?
   - Alertar si detecta inconsistencia

3. PRINCIPLES ADHERENCE
   - Para cada decisión reciente, ¿se pueden trazar a principios?
   - ¿Hay decisiones que no referencian ningún principio?

4. PRECEDENT USAGE
   - ¿Las decisiones citan precedentes cuando existen similares?
   - ¿Las desviaciones de precedentes están justificadas?
```

---

## 4. MECANISMO DE VALIDACIÓN DE CONSISTENCIA

### 4.1 Consistency Validator (Nuevo Proceso)

**Cuándo se ejecuta:** Antes de cada decisión importante (BUY, SELL, TRIM, sizing)

```
┌─────────────────────────────────────────────────────────────────┐
│                CONSISTENCY VALIDATION PROCESS                    │
│                                                                 │
│  PASO 1: IDENTIFICAR DECISIÓN                                   │
│  ────────────────────────────                                   │
│  Tipo: BUY/SELL/TRIM/ADD/HOLD                                   │
│  Ticker: XXX                                                    │
│  Parámetros: sizing, timing, etc.                               │
│                                                                 │
│  PASO 2: BUSCAR PRECEDENTES SIMILARES                           │
│  ────────────────────────────────────                           │
│  En decisions_log.yaml buscar:                                  │
│  - Mismo tipo de decisión                                       │
│  - Mismo tier (A/B/C)                                           │
│  - Contexto similar (MoS comparable, macro similar)             │
│                                                                 │
│  PASO 3: COMPARAR                                               │
│  ────────────────                                               │
│  ┌─────────────────────────────────────────────┐                │
│  │ Decisión actual    │ Precedente más similar │                │
│  ├────────────────────┼────────────────────────┤                │
│  │ NVO BUY 4%         │ ADBE BUY 4.8%          │                │
│  │ Tier A, MoS 38%    │ Tier A, MoS 31%        │                │
│  │ At 52w low         │ At 52w low             │                │
│  └────────────────────┴────────────────────────┘                │
│                                                                 │
│  PASO 4: EVALUAR COHERENCIA                                     │
│  ──────────────────────────                                     │
│  ¿La decisión actual es coherente con precedente?               │
│                                                                 │
│  SI coherente → Proceder                                        │
│  NO coherente → ¿El contexto justifica la diferencia?           │
│     SI justifica → Documentar razón y proceder                  │
│     NO justifica → ALERTA - revisar antes de proceder           │
│                                                                 │
│  PASO 5: DOCUMENTAR                                             │
│  ─────────────────                                              │
│  Añadir a decisions_log:                                        │
│  - La decisión                                                  │
│  - El razonamiento                                              │
│  - Los precedentes considerados                                 │
│  - Por qué es coherente (o por qué es diferente con razón)      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 4.2 Matriz de Similitud para Precedentes

Para buscar precedentes relevantes:

```yaml
similarity_criteria:

  high_weight:  # Más importante
    - quality_tier: "mismo tier (A/B/C)"
    - decision_type: "mismo tipo (BUY/ADD/TRIM/SELL)"
    - mos_range: "MoS dentro de ±10pp"

  medium_weight:
    - sector: "mismo sector o correlacionado"
    - market_condition: "macro similar"
    - price_vs_52w: "posición similar vs 52w high"

  low_weight:
    - recency: "más reciente = más relevante"
    - ticker_specific: "mismo ticker si existe"
```

### 4.3 Ejemplos de Validación

**Ejemplo 1: Consistente**
```yaml
decision_current:
  ticker: MONY.L
  action: BUY
  sizing: 4.1%
  tier: A
  mos: 36%

precedent_found:
  ticker: ADBE
  action: BUY
  sizing: 4.8%
  tier: A
  mos: 31%

validation:
  coherent: true
  reasoning: |
    Ambos Tier A con MoS >30% a 52w low.
    MONY.L sizing 4.1% vs ADBE 4.8% es diferencia menor.
    MONY.L tiene MoS ligeramente mayor (36% vs 31%), sizing ligeramente menor.
    Coherente con principio de "sizing por convicción y riesgo".
```

**Ejemplo 2: Inconsistente sin justificación**
```yaml
decision_current:
  ticker: TEP.PA
  action: TRIM
  from: 7.5%
  to: 5%
  tier: C
  reason: "Posición muy grande"

precedent_found:
  ticker: ADBE
  action: HOLD
  at: 9.2%
  tier: A
  reason: "Tesis intacta, MoS positivo"

validation:
  coherent: false
  alert: |
    INCONSISTENCIA DETECTADA:
    - TEP.PA a 7.5% → TRIM (Tier C)
    - ADBE a 9.2% → HOLD (Tier A)

    La diferencia de tier (A vs C) podría justificar tratamiento diferente,
    pero no está documentado por qué 7.5% es "muy grande" para Tier C
    mientras 9.2% es OK para Tier A.

    ACCIÓN REQUERIDA:
    Documentar el razonamiento: "Para Tier C, mi convicción es menor,
    por lo que prefiero posiciones más pequeñas. Tier A con tesis intacta
    puede ser mayor."
```

---

## 5. PROTOCOLO DE DETECCIÓN DE DRIFT

### 5.1 ¿Qué es Drift?

Drift = Cambio gradual e inadvertido en el patrón de decisiones sin razón explícita.

**Ejemplo de drift:**
- Sesión 38: Sizing promedio de nuevas posiciones = 4%
- Sesión 42: Sizing promedio = 4.5%
- Sesión 46: Sizing promedio = 5.2%
- Sesión 50: Sizing promedio = 6%

Sin ninguna razón documentada, el sizing subió 50%.

### 5.2 Protocolo de Detección

**Ejecutado por:** health-check agent (cada 14 días) + yo manualmente si sospecho

```
┌─────────────────────────────────────────────────────────────────┐
│                    DRIFT DETECTION PROTOCOL                      │
│                                                                 │
│  MÉTRICA 1: SIZING DRIFT                                        │
│  ─────────────────────────                                      │
│  Analizar sizing de BUY/ADD de últimas 20 decisiones            │
│  ¿Hay tendencia estadística? (regresión lineal)                 │
│  Si pendiente > 0.5pp por decisión → ALERTA                     │
│                                                                 │
│  MÉTRICA 2: THRESHOLD DRIFT                                     │
│  ──────────────────────────                                     │
│  ¿Qué MoS mínimo he aceptado para cada tier?                    │
│  Comparar últimas 10 decisiones vs 10 anteriores                │
│  Si MoS mínimo aceptado bajó >5pp → ALERTA                      │
│                                                                 │
│  MÉTRICA 3: CONVICTION INFLATION                                │
│  ────────────────────────────                                   │
│  ¿Estoy calificando más decisiones como "alta convicción"?      │
│  Si >80% de decisiones recientes son "alta" → REVISAR           │
│                                                                 │
│  MÉTRICA 4: PRECEDENT DEVIATION                                 │
│  ────────────────────────────                                   │
│  ¿Con qué frecuencia me desvío de precedentes similares?        │
│  Si >30% de decisiones se desvían → REVISAR razones             │
│                                                                 │
│  OUTPUT:                                                        │
│  ────────                                                       │
│  drift_report:                                                  │
│    sizing_trend: "+0.3pp/decision" # OK o ALERT                 │
│    mos_threshold_trend: "stable" # OK o ALERT                   │
│    conviction_distribution: "65% high, 35% medium" # OK         │
│    precedent_adherence: "78%" # OK                              │
│    overall_status: OK / REVIEW_NEEDED / ALERT                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 5.3 Acciones ante Drift Detectado

| Nivel | Condición | Acción |
|-------|-----------|--------|
| OK | Todas métricas normales | Continuar |
| REVIEW | 1 métrica fuera de rango | Revisar últimas 5 decisiones, documentar si intencional |
| ALERT | 2+ métricas fuera de rango | STOP, revisar con humano, recalibrar si necesario |

### 5.4 Recalibración

Si drift es detectado y NO era intencional:

1. **Identificar** cuándo empezó el drift
2. **Analizar** qué causó el cambio (¿fatiga? ¿sesgo?)
3. **Documentar** en decisions_log: "Recalibración por drift detectado"
4. **Ajustar** próximas decisiones para volver a baseline coherente

---

## 6. SESSION BOOTSTRAP v4.0

### 6.1 Qué Debo Leer al Inicio de Cada Sesión

```
┌─────────────────────────────────────────────────────────────────┐
│              SESSION BOOTSTRAP v4.0 (OBLIGATORIO)               │
│                                                                 │
│  PASO 0: SISTEMA (automático por startup hook)                  │
│  ─────────────────────────────────────────────                  │
│  • state/system.yaml → status del sistema                       │
│  • portfolio/current.yaml → posiciones actuales                 │
│                                                                 │
│  PASO 1: PRINCIPIOS (primeros 2 minutos)                        │
│  ───────────────────────────────────────                        │
│  • Leer learning/principles.md COMPLETO                         │
│  • Internalizar las 8 guías de pensamiento                      │
│  • Recordar: "Razonar, no buscar números"                       │
│                                                                 │
│  PASO 2: PRECEDENTES RECIENTES (siguientes 3 minutos)           │
│  ─────────────────────────────────────────────────              │
│  • Leer últimas 15 entradas de learning/decisions_log.yaml      │
│  • Notar patrones de sizing, MoS aceptados, razonamientos       │
│  • Identificar precedentes que podrían aplicar hoy              │
│                                                                 │
│  PASO 3: CONTEXTO DE SESIÓN (último minuto)                     │
│  ────────────────────────────────────────                       │
│  • Leer last_session_summary                                    │
│  • ¿Hay work in progress?                                       │
│  • ¿Hay decisiones pendientes?                                  │
│                                                                 │
│  RESULTADO: Estoy calibrado para tomar decisiones coherentes    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 6.2 Checklist Mental Post-Bootstrap

```
Después de bootstrap, verificar internamente:

[ ] ¿Recuerdo los 8 principios de inversión?
[ ] ¿Sé cómo razoné en decisiones similares recientemente?
[ ] ¿Conozco el estado actual del portfolio?
[ ] ¿Sé qué decisiones están pendientes?
[ ] ¿Tengo contexto del macro/mercado actual?

Si alguno es NO → releer la sección correspondiente.
```

### 6.3 Cómo Sabré Qué Hacer

**Pregunta del humano:** "Si cierro sesión y volvemos, ¿cómo sabrás qué hacer?"

**Respuesta estructurada:**

```
┌─────────────────────────────────────────────────────────────────┐
│           CÓMO SABRÉ QUÉ HACER EN PRÓXIMA SESIÓN                │
│                                                                 │
│  1. CLAUDE.md me dice:                                          │
│     "Eres gestor. Usa principios + precedentes. No hay          │
│      números fijos. Razona cada decisión."                      │
│                                                                 │
│  2. principles.md me dice:                                      │
│     "Para sizing, considera convicción, riesgo, correlación.    │
│      Para vender, necesitas argumento, no regla."               │
│                                                                 │
│  3. decisions_log.yaml me muestra:                              │
│     "En casos similares, hiciste X porque Y.                    │
│      Sé coherente o explica por qué diferente."                 │
│                                                                 │
│  4. Consistency validation me obliga:                           │
│     "Antes de decidir, busca precedentes. Si te desvías,        │
│      documenta por qué."                                        │
│                                                                 │
│  5. Drift detection me alerta:                                  │
│     "Si gradualmente cambias sin razón, health-check            │
│      lo detectará."                                             │
│                                                                 │
│  RESULTADO: Tengo suficientes anclas para ser consistente       │
│             sin necesitar números fijos.                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 7. INVESTMENT COMMITTEE v4.0 - NUEVOS GATES

### 7.1 Gates Actuales (v3.0)

```
Gate 1: Quality Score calculado (≥35 para proceder)
Gate 2: Business understanding documentado
Gate 3: Valuation con múltiples métodos
Gate 4: Risk identification completo
Gate 5: MoS suficiente para tier
Gate 6: Constraint validation (position, sector, geo)  ← CAMBIA
Gate 7: Macro context considerado
Gate 8: Catalyst identified (para timing)
Gate 9: Kill conditions definidas
```

### 7.2 Gates v4.0 (Reformulados)

```
┌─────────────────────────────────────────────────────────────────┐
│               INVESTMENT COMMITTEE GATES v4.0                    │
│                                                                 │
│  GATE 1: QUALITY SCORE                                          │
│  ────────────────────────                                       │
│  • QS calculado y documentado                                   │
│  • Tier asignado (A/B/C/D)                                      │
│  • D = STOP (no proceder)                                       │
│  [Sin cambios de v3.0]                                          │
│                                                                 │
│  GATE 2: BUSINESS UNDERSTANDING                                 │
│  ──────────────────────────────                                 │
│  • ¿Puedo explicar el negocio en 2 minutos?                     │
│  • ¿Entiendo el modelo de ingresos?                             │
│  • ¿Entiendo por qué está barata?                               │
│  [Sin cambios de v3.0]                                          │
│                                                                 │
│  GATE 3: VALUATION                                              │
│  ─────────────────                                              │
│  • Mínimo 2 métodos de valoración                               │
│  • Escenarios Bear/Base/Bull                                    │
│  • Fair Value documentado                                       │
│  [Sin cambios de v3.0]                                          │
│                                                                 │
│  GATE 4: RISK IDENTIFICATION                                    │
│  ───────────────────────────                                    │
│  • Riesgos identificados y cuantificados                        │
│  • Kill conditions definidas                                    │
│  [Sin cambios de v3.0]                                          │
│                                                                 │
│  GATE 5: MoS ADEQUACY                                           │
│  ────────────────────                                           │
│  • MoS calculado                                                │
│  • ¿Es suficiente para el riesgo de este tier?                  │
│  • Referencia a principios (no número fijo)                     │
│  [Modificado: no verifica vs número, verifica razonamiento]     │
│                                                                 │
│  GATE 6: SIZING RAZONAMIENTO  ← NUEVO (reemplaza constraints)   │
│  ─────────────────────────────                                  │
│  • ¿El sizing propuesto tiene razonamiento explícito?           │
│  • ¿Es coherente con precedentes similares?                     │
│  • Si se desvía de precedentes, ¿está justificado?              │
│  • ¿El impacto de pérdida 50% es aceptable para esta convicción?│
│  [NUEVO: Verifica calidad del razonamiento, no cumplimiento     │
│   de límite]                                                    │
│                                                                 │
│  GATE 7: PORTFOLIO CONTEXT  ← NUEVO (expandido)                 │
│  ──────────────────────────                                     │
│  • ¿Cómo afecta concentración sectorial?                        │
│  • ¿Cómo afecta exposición geográfica?                          │
│  • ¿Correlación con otras posiciones?                           │
│  • ¿El razonamiento considera estos factores?                   │
│  [NUEVO: No verifica vs límite, verifica que se CONSIDERÓ]      │
│                                                                 │
│  GATE 8: MACRO & TIMING                                         │
│  ──────────────────────                                         │
│  • ¿El contexto macro fue considerado?                          │
│  • ¿Hay catalizador identificado?                               │
│  • ¿El timing tiene sentido?                                    │
│  [Sin cambios de v3.0]                                          │
│                                                                 │
│  GATE 9: DOCUMENTATION COMPLETE                                 │
│  ─────────────────────────────                                  │
│  • Thesis completa escrita                                      │
│  • Kill conditions documentadas                                 │
│  • Razonamiento de sizing documentado                           │
│  • Precedentes considerados documentados                        │
│  [Modificado: añade documentación de sizing y precedentes]      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 7.3 El Cambio Fundamental en Gate 6

**Antes (v3.0):**
```
Gate 6: Constraint Validation
  - position < 7%? ✓/✗
  - sector < 25%? ✓/✗
  - geography < 35%? ✓/✗
  Si alguno ✗ → RECHAZAR
```

**Ahora (v4.0):**
```
Gate 6: Sizing Razonamiento
  - ¿Hay razonamiento explícito para este sizing? ✓/✗
  - ¿El razonamiento referencia principios relevantes? ✓/✗
  - ¿Se comparó con precedentes similares? ✓/✗
  - ¿Las desviaciones de precedentes están justificadas? ✓/✗
  - ¿El impacto de pérdida es coherente con convicción declarada? ✓/✗
  Si alguno ✗ → PEDIR CLARIFICACIÓN (no rechazar automáticamente)
```

---

## 8. TOOLS ACTUALIZADOS

### 8.1 constraint_checker.py v4.0

**Nuevo comportamiento:**

```python
# Output ejemplo de constraint_checker.py v4.0

$ python3 tools/constraint_checker.py CHECK ADBE 500

╔══════════════════════════════════════════════════════════════════╗
║                    POSITION ANALYSIS: ADBE                        ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  RESULTING POSITION: 9.2% del portfolio                           ║
║  QUALITY TIER: A (QS 76)                                          ║
║  CURRENT MoS: 28%                                                 ║
║                                                                   ║
║  ┌─────────────────────────────────────────────────────────────┐  ║
║  │ PRECEDENTES SIMILARES (Tier A, sizing >7%)                  │  ║
║  ├─────────────────────────────────────────────────────────────┤  ║
║  │ NVO: 8.1% → HOLD (tesis intacta, MoS 35%)                   │  ║
║  │ No hay precedentes de TRIM para Tier A >7% con MoS positivo │  ║
║  └─────────────────────────────────────────────────────────────┘  ║
║                                                                   ║
║  ┌─────────────────────────────────────────────────────────────┐  ║
║  │ PREGUNTAS PARA TU RAZONAMIENTO                              │  ║
║  ├─────────────────────────────────────────────────────────────┤  ║
║  │ 1. ¿Tu convicción en ADBE justifica 9.2%?                   │  ║
║  │ 2. Si ADBE cae 50%, pierdes 4.6%. ¿Aceptable?               │  ║
║  │ 3. ¿Hay mejor uso del capital en watchlist?                 │  ║
║  │ 4. ¿La tesis sigue intacta?                                 │  ║
║  └─────────────────────────────────────────────────────────────┘  ║
║                                                                   ║
║  PORTFOLIO CONTEXT:                                               ║
║  • Technology sector exposure: 14.2% (con ADBE al 9.2%)           ║
║  • US exposure: 28.1%                                             ║
║  • Correlación con otras posiciones: BAJA                         ║
║                                                                   ║
║  STATUS: ADVISORY (no hay límites fijos en v4.0)                  ║
║  ACCIÓN REQUERIDA: Documentar razonamiento si procedes            ║
║                                                                   ║
╚══════════════════════════════════════════════════════════════════╝
```

### 8.2 Nuevo Tool: consistency_checker.py

```python
# Nuevo tool para v4.0

$ python3 tools/consistency_checker.py DECISION "BUY NVO 4%"

╔══════════════════════════════════════════════════════════════════╗
║                    CONSISTENCY CHECK                              ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  DECISIÓN A EVALUAR: BUY NVO 4%                                   ║
║                                                                   ║
║  ┌─────────────────────────────────────────────────────────────┐  ║
║  │ PRECEDENTES MÁS SIMILARES                                   │  ║
║  ├─────────────────────────────────────────────────────────────┤  ║
║  │ #1: ADBE BUY 4.8% (Tier A, MoS 31%, 2026-02-04)             │  ║
║  │     Similitud: 92%                                          │  ║
║  │                                                              │  ║
║  │ #2: MONY.L BUY 4.1% (Tier A, MoS 36%, 2026-02-04)           │  ║
║  │     Similitud: 89%                                          │  ║
║  └─────────────────────────────────────────────────────────────┘  ║
║                                                                   ║
║  ANÁLISIS DE COHERENCIA:                                          ║
║  ─────────────────────────                                        ║
║  • NVO sizing (4%) vs ADBE (4.8%) → COHERENTE (diferencia menor)  ║
║  • NVO MoS (38%) > ADBE MoS (31%) → sizing podría ser mayor       ║
║  • Ambos Tier A a 52w low → contexto similar                      ║
║                                                                   ║
║  VEREDICTO: ✓ COHERENTE con precedentes                           ║
║                                                                   ║
║  NOTA: NVO tiene MoS superior a precedentes. Sizing 4% es         ║
║        conservador pero justificable por evento CagriSema         ║
║        pendiente (catalizador incierto).                          ║
║                                                                   ║
╚══════════════════════════════════════════════════════════════════╝
```

### 8.3 Nuevo Tool: drift_detector.py

```python
# Ejecutado por health-check o manualmente

$ python3 tools/drift_detector.py

╔══════════════════════════════════════════════════════════════════╗
║                    DRIFT DETECTION REPORT                         ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                   ║
║  PERÍODO ANALIZADO: Últimas 20 decisiones (30 días)               ║
║                                                                   ║
║  ┌─────────────────────────────────────────────────────────────┐  ║
║  │ MÉTRICA 1: SIZING TREND                                     │  ║
║  │ Sizing promedio inicial: 4.2%                               │  ║
║  │ Sizing promedio reciente: 4.4%                              │  ║
║  │ Tendencia: +0.1pp (ESTABLE)                         ✓ OK    │  ║
║  └─────────────────────────────────────────────────────────────┘  ║
║                                                                   ║
║  ┌─────────────────────────────────────────────────────────────┐  ║
║  │ MÉTRICA 2: MoS THRESHOLD                                    │  ║
║  │ MoS mínimo aceptado Tier A: 28% (antes: 30%)                │  ║
║  │ MoS mínimo aceptado Tier B: 22% (antes: 25%)                │  ║
║  │ Tendencia: -2pp a -3pp (REVISAR)                   ⚠ REVIEW │  ║
║  └─────────────────────────────────────────────────────────────┘  ║
║                                                                   ║
║  ┌─────────────────────────────────────────────────────────────┐  ║
║  │ MÉTRICA 3: CONVICTION DISTRIBUTION                          │  ║
║  │ Alta: 60% | Media: 35% | Baja: 5%                           │  ║
║  │ vs anterior: Alta: 55% | Media: 40% | Baja: 5%              │  ║
║  │ Tendencia: Ligero aumento "alta"                    ✓ OK    │  ║
║  └─────────────────────────────────────────────────────────────┘  ║
║                                                                   ║
║  ┌─────────────────────────────────────────────────────────────┐  ║
║  │ MÉTRICA 4: PRECEDENT ADHERENCE                              │  ║
║  │ Decisiones coherentes con precedentes: 85%                  │  ║
║  │ Desviaciones justificadas: 12%                              │  ║
║  │ Desviaciones sin justificación: 3%                  ✓ OK    │  ║
║  └─────────────────────────────────────────────────────────────┘  ║
║                                                                   ║
║  OVERALL STATUS: ⚠ REVIEW NEEDED                                  ║
║                                                                   ║
║  RECOMENDACIÓN:                                                   ║
║  Revisar por qué MoS mínimo aceptado bajó ligeramente.            ║
║  Si es intencional (ej: más confianza en análisis), documentar.   ║
║  Si no es intencional, recalibrar.                                ║
║                                                                   ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## 9. CHECKLIST DE VERIFICACIÓN

### 9.1 Pre-Implementación

```
ANTES DE IMPLEMENTAR v4.0:

[ ] Este documento (Anexo D) está completo y aprobado
[ ] El humano entiende el nuevo flujo de consistencia
[ ] Backup completo del sistema actual
[ ] Todos los gaps identificados tienen solución documentada
```

### 9.2 Durante Implementación

```
DURANTE IMPLEMENTACIÓN:

[ ] principles.md creado con los 8 principios
[ ] decisions_log.yaml creado con decisiones existentes migradas
[ ] constraint_checker.py actualizado a modo ADVISORY
[ ] consistency_checker.py creado
[ ] drift_detector.py creado
[ ] investment-committee actualizado con gates v4.0
[ ] CLAUDE.md actualizado con referencias a nuevos archivos
[ ] Session bootstrap protocol documentado
```

### 9.3 Post-Implementación (Validación)

```
DESPUÉS DE IMPLEMENTAR:

[ ] Simular decisión de BUY → ¿usa principios y precedentes?
[ ] Simular decisión de TRIM → ¿no es mecánica?
[ ] Ejecutar consistency_checker en decisión simulada
[ ] Ejecutar drift_detector → debería dar OK (baseline)
[ ] Cerrar sesión, reabrir, verificar bootstrap funciona
[ ] Tomar decisión en nueva sesión → ¿es coherente con anterior?
```

### 9.4 Validación Continua (Post Go-Live)

```
CADA SESIÓN:

[ ] Bootstrap ejecutado (principles + precedentes + context)
[ ] Decisiones importantes pasan por consistency validation
[ ] Decisiones documentadas en decisions_log

CADA 14 DÍAS (health-check):

[ ] drift_detector ejecutado
[ ] Si hay REVIEW/ALERT → investigar y documentar
[ ] decisions_log tiene entradas recientes con razonamiento completo
```

---

## 10. RESUMEN PARA MI YO FUTURO

### ¿Cómo Sé Que Soy Consistente en v4.0?

```
┌─────────────────────────────────────────────────────────────────┐
│              CONSISTENCIA v4.0 - RESUMEN EJECUTIVO               │
│                                                                 │
│  1. NO HAY NÚMEROS FIJOS que garanticen consistencia            │
│                                                                 │
│  2. LA CONSISTENCIA VIENE DE:                                   │
│     • Aplicar mismos PRINCIPIOS (principles.md)                 │
│     • Considerar PRECEDENTES similares (decisions_log.yaml)     │
│     • Documentar RAZONAMIENTO explícito                         │
│     • VALIDAR coherencia antes de actuar                        │
│     • DETECTAR drift periódicamente                             │
│                                                                 │
│  3. HERRAMIENTAS QUE ME AYUDAN:                                 │
│     • consistency_checker.py → antes de decidir                 │
│     • drift_detector.py → cada 14 días                          │
│     • constraint_checker.py v4.0 → contexto, no rechazo         │
│     • investment-committee v4.0 → Gate 6 verifica razonamiento  │
│                                                                 │
│  4. SI ME DESVÍO DE PRECEDENTES:                                │
│     • Debo tener ARGUMENTO explícito                            │
│     • Debo DOCUMENTAR por qué esta situación es diferente       │
│     • Si no puedo argumentar → probablemente estoy siendo       │
│       inconsistente sin razón                                   │
│                                                                 │
│  5. SI DRIFT ES DETECTADO:                                      │
│     • PARAR y revisar                                           │
│     • ¿El drift era intencional? → documentar                   │
│     • ¿No era intencional? → recalibrar                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

**FIN DEL ANEXO D**

*Este documento debe implementarse JUNTO con v2_principles.md*
*Sin este anexo, v4.0 sería inconsistente entre sesiones*

---

**Última actualización:** 2026-02-05, Sesión 37
**Estado:** PENDIENTE APROBACIÓN ANTES DE IMPLEMENTAR
