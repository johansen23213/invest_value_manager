# Framework v4.0 - Evolution Design Document

> **Documento de diseño para la evolución del sistema de inversión**
> Creado: 2026-02-05, Sesión 37
> Estado: PROPUESTA PENDIENTE DE IMPLEMENTACIÓN
> Autor: Claude (orchestrator) en colaboración con el humano

---

## TABLA DE CONTENIDOS

1. [Resumen Ejecutivo](#1-resumen-ejecutivo)
2. [Contexto y Motivación](#2-contexto-y-motivación)
3. [Diagnóstico v3.0 - Problemas Identificados](#3-diagnóstico-v30---problemas-identificados)
4. [Framework v4.0 - Diseño Completo](#4-framework-v40---diseño-completo)
5. [Parámetros Dinámicos - Especificación Completa](#5-parámetros-dinámicos---especificación-completa)
6. [Protocolo EXIT Estratégico](#6-protocolo-exit-estratégico)
7. [Limpieza Legacy - Plan Detallado](#7-limpieza-legacy---plan-detallado)
8. [Cambios en Agentes y Skills](#8-cambios-en-agentes-y-skills)
9. [Estructura de Ficheros Propuesta](#9-estructura-de-ficheros-propuesta)
10. [Plan de Implementación por Fases](#10-plan-de-implementación-por-fases)
11. [Checklist de Validación](#11-checklist-de-validación)
12. [Métricas de Éxito](#12-métricas-de-éxito)

---

## 1. RESUMEN EJECUTIVO

### Qué es v4.0

**Framework v4.0 = "Principios Adaptativos"**

| Versión | Filosofía | Problema |
|---------|-----------|----------|
| v1.0 | "Compra value" | Sin estructura |
| v2.0 | "Compra barato" | Value traps |
| v3.0 | "Quality First" | Reglas mecánicas |
| **v4.0** | **"Principios Adaptativos"** | - |

**Cambio fundamental:** De reglas fijas (7% max, 35% geo) a principios con contexto que el gestor (Claude) adapta con argumentos.

### Objetivos v4.0

1. **Eliminar reglas mecánicas absurdas** (ej: vender ganador solo porque >7%)
2. **Crear protocolo EXIT estratégico** (lo que falta en v3.0)
3. **Centralizar parámetros** en archivo configurable con justificaciones
4. **Limpiar legacy** (4 inconsistencias, 10 items obsoletos)
5. **Hacer el sistema auto-evolutivo con argumentos** (no cambios arbitrarios)

### Resultado esperado

Un sistema donde:
- Las "reglas" son principios con contexto y excepciones documentadas
- Puedo decidir NO vender un ganador >7% SI justifico por qué
- Existe proceso claro para EXIT estratégico (no solo kill conditions)
- Los parámetros están en UN lugar con explicación de por qué ese valor
- El sistema está limpio de código/config legacy

---

## 2. CONTEXTO Y MOTIVACIÓN

### La conversación que originó v4.0 (Sesión 37, 2026-02-05)

El humano planteó preguntas fundamentales después de ejecutar HRB ADD:

> "Hablas de Shell que monitorear y tenemos monitores y también tenemos protocolos para comprar, lo que no me queda claro es si tenemos un protocolo para cerrar operaciones cuando es momento de salirse y buscar otro activo mejor?"

**Observación clave #1:** Falta protocolo EXIT estratégico.

> "Si una acción ha subido y alcanza >7% vamos a vender solo por la regla? No sería mejor dejarla crecer más aunque se incumple regla?"

**Observación clave #2:** Las reglas mecánicas pueden ser contraproducentes.

> "Pienso que las reglas son parámetros fijos aprendidos del pasado, como una especie de bias y pienso que las reglas deberían de ser dinámicas y cambiantes en base a argumentos claro que un inversor profesional es capaz de adaptar."

**Observación clave #3:** Reglas fijas = bias histórico. Un gestor profesional adapta.

> "Necesito saber dónde y por qué usas parámetros y configuraciones fijas."

**Observación clave #4:** Falta transparencia sobre origen de parámetros.

### Mi reflexión inicial

Reconocí que:

1. **Las reglas actuales son arbitrarias:** ¿Por qué 7% y no 10%? ¿Por qué 35% geografía?
2. **El TRIM mecánico es absurdo:** Vender un ganador probado solo por regla = destruir valor
3. **Falta el proceso EXIT:** Tenemos entrada rigurosa, monitoreo, pero no salida estratégica
4. **Los parámetros no están justificados:** Adopté "best practices" sin cuestionar

### Lo que el humano quiere

1. **Reflexión completa** sobre reglas fijas vs. juicio dinámico
2. **Auditoría del sistema** para identificar legacy y parámetros hardcodeados
3. **Documento de evolución** para implementar en futuras sesiones
4. **Framework completo** paso a paso antes de implementar

---

## 3. DIAGNÓSTICO v3.0 - PROBLEMAS IDENTIFICADOS

### 3.1 Los 23 Parámetros Hardcodeados

**Ubicación actual:** Dispersos en CLAUDE.md, rules/, skills/, tools/

| # | Parámetro | Valor Actual | Ubicación | Origen/Justificación | Problema |
|---|-----------|--------------|-----------|----------------------|----------|
| 1 | Position max | 7% | file-structure.md, constraint_checker.py | "Diversificación estándar" | ¿Por qué igual para Tier A y Tier C? |
| 2 | Sector max | 25% | file-structure.md, constraint_checker.py | Evitar concentración | ¿Qué define "sector"? GICS? |
| 3 | Geography max | 35% | file-structure.md, constraint_checker.py | Riesgo país | ¿Aplica igual US que Italia? |
| 4 | Cash min | 5% | file-structure.md, rules.yaml | Reserva oportunidad | ¿Por qué 5%? |
| 5 | Cash drag threshold | 15% | session-protocol.md | Alerta | Arbitrario |
| 6 | Cash drag critical | 20% | session-protocol.md | Fallo del gestor | Arbitrario |
| 7 | Max positions | 20 | constraint_checker.py | Límite operativo | ¿Por qué 20? |
| 8 | MoS Tier A | 10-15% | CLAUDE.md | Quality compounder bajo riesgo | **JUSTIFICADO** |
| 9 | MoS Tier B | 20-25% | CLAUDE.md | Quality value riesgo medio | **JUSTIFICADO** |
| 10 | MoS Tier C | 30-40% | CLAUDE.md | Special situation alto riesgo | **JUSTIFICADO** |
| 11 | QS Tier A cutoff | 75+ | CLAUDE.md | Quality Score brackets | **JUSTIFICADO** |
| 12 | QS Tier B cutoff | 55-74 | CLAUDE.md | Quality Score brackets | **JUSTIFICADO** |
| 13 | QS Tier C cutoff | 35-54 | CLAUDE.md | Quality Score brackets | **JUSTIFICADO** |
| 14 | QS Tier D cutoff | <35 | CLAUDE.md | NO COMPRAR | **JUSTIFICADO** |
| 15 | Price alert 24h | 5% | session-protocol.md | Anomalía | Razonable |
| 16 | Price alert 7d | 10% | session-protocol.md | Anomalía | Razonable |
| 17 | Standing order near | 5% | session-protocol.md | Cercanía trigger | Razonable |
| 18 | Health check freq | 14 días | state/system.yaml | Auditoría | Arbitrario |
| 19 | World view staleness | 7 días | session-protocol.md | Actualizar macro | Arbitrario |
| 20 | Sector view staleness | 30 días | file-structure.md | Actualizar sector | Arbitrario |
| 21 | TRIM trigger | >1.3x target | rebalancer agent | Rebalanceo | ¿Por qué 1.3x? |
| 22 | ADD trigger | <0.7x target | rebalancer agent | Rebalanceo | ¿Por qué 0.7x? |
| 23 | Pipeline min | 3 thesis | session-protocol.md | Evitar cash drag | Arbitrario |

**Conclusión:**
- 7 parámetros **JUSTIFICADOS** (Quality Score framework)
- 16 parámetros **ARBITRARIOS** (necesitan revisión o dinamización)

### 3.2 Las 4 Inconsistencias Críticas

| # | Inconsistencia | Impacto | Solución |
|---|----------------|---------|----------|
| 1 | SHEL vs SHEL.L en transactions | Confusión en automatización | Normalizar a SHEL.L |
| 2 | LIGHT.NV vs LIGHT.AS | Ticker duplicado | Normalizar a LIGHT.AS |
| 3 | Posiciones cerradas sin thesis formal | Auditoría histórica difícil | Crear skeleton thesis |
| 4 | state/system.yaml = 1,204 líneas | Inmantenible | Compactar/particionar |

### 3.3 Los 10 Items Legacy/Unused

| # | Item | Ubicación | Razón | Acción |
|---|------|-----------|-------|--------|
| 1 | config/rules.yaml | /config/ | Duplica CLAUDE.md | ELIMINAR |
| 2 | config/memory_management.yaml | /config/ | No se usa | REVISAR/ELIMINAR |
| 3 | SYSTEM_LOAD_PROTOCOL.md | archive/deprecated/ | Reemplazado | ELIMINAR |
| 4 | evolution/backups/ (>3 meses) | /evolution/ | Viejos | ARCHIVAR |
| 5 | journal/decisions/ (viejos) | /journal/ | >3 meses | COMPACTAR |
| 6 | journal/reviews/ (viejos) | /journal/ | >3 meses | COMPACTAR |
| 7 | strategy/backtests/ | /strategy/ | Sin uso reciente | REVISAR |
| 8 | Standing orders expirados | state/system.yaml | Fechas pasadas | LIMPIAR |
| 9 | Standing orders duplicados | state/system.yaml | BUY + ADD mismo ticker | CONSOLIDAR |
| 10 | last_session_summary archivados | state/system.yaml | 4 copias | MOVER a archive/ |

### 3.4 Lo Que FALTA en v3.0

| Proceso | Estado | Consecuencia |
|---------|--------|--------------|
| Protocolo ENTRY | ✅ Completo (9 gates) | - |
| Protocolo MONITORING | ✅ Completo (vigilancia v3.0) | - |
| Protocolo TRIM | ⚠️ Mecánico | Vende ganadores sin razón |
| **Protocolo EXIT estratégico** | ❌ NO EXISTE | No sabemos cuándo salir |
| **Comparación oportunidad-coste** | ❌ NO EXISTE | No comparamos mantener vs. rotar |
| **Principios adaptativos** | ❌ NO EXISTE | Reglas fijas sin contexto |

---

## 4. FRAMEWORK v4.0 - DISEÑO COMPLETO

### 4.1 Filosofía Central

```
v3.0: "Sigue las reglas" (mecánico)
v4.0: "Aplica los principios con juicio" (adaptativo)
```

**Definición de PRINCIPIO vs REGLA:**

| Concepto | Definición | Ejemplo |
|----------|------------|---------|
| **Regla** | Instrucción fija sin contexto | "Máximo 7% por posición" |
| **Principio** | Guía con contexto y excepciones | "Evitar concentración excesiva. Tier A puede ser hasta 10% si tesis intacta y MoS >0%" |

### 4.2 Los 5 Pilares de v4.0

```
┌─────────────────────────────────────────────────────────────────────┐
│                      FRAMEWORK v4.0                                 │
│                   "Principios Adaptativos"                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                 │
│  │   PILAR 1   │  │   PILAR 2   │  │   PILAR 3   │                 │
│  │  Parámetros │  │  Protocolo  │  │  Decision   │                 │
│  │  Dinámicos  │  │    EXIT     │  │  Framework  │                 │
│  └─────────────┘  └─────────────┘  └─────────────┘                 │
│                                                                     │
│  ┌─────────────┐  ┌─────────────┐                                  │
│  │   PILAR 4   │  │   PILAR 5   │                                  │
│  │  Sistema    │  │  Auto-      │                                  │
│  │  Limpio     │  │  Evolución  │                                  │
│  └─────────────┘  └─────────────┘                                  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Pilar 1: Parámetros Dinámicos**
- Centralizar en `learning/parameters.yaml`
- Cada parámetro con justificación y condiciones de override
- Diferentes límites por Tier/Geografía/Situación

**Pilar 2: Protocolo EXIT Estratégico**
- Proceso estructurado para decidir cuándo salir
- Comparación oportunidad-coste
- No solo kill conditions, también "mejor uso del capital"

**Pilar 3: Decision Framework Adaptativo**
- Las "reglas" se convierten en principios con contexto
- Puedo hacer excepciones SI justifico por qué
- Documentación de excepciones para aprendizaje

**Pilar 4: Sistema Limpio**
- Eliminar legacy
- Resolver inconsistencias
- Compactar archivos monstruo

**Pilar 5: Auto-Evolución Argumentada**
- Cambios al sistema requieren justificación
- Registro de por qué se cambió cada parámetro
- Aprendizaje continuo basado en resultados

---

## 5. PARÁMETROS DINÁMICOS - ESPECIFICACIÓN COMPLETA

### 5.1 Nuevo Archivo: `learning/parameters.yaml`

Este archivo centraliza TODOS los parámetros del sistema con:
- Valor actual
- Justificación
- Condiciones de override
- Historial de cambios

```yaml
# =============================================================================
# PARAMETERS.YAML - Framework v4.0
# =============================================================================
# Fuente única de verdad para todos los parámetros del sistema.
# Cada parámetro incluye justificación y condiciones de override.
# NUNCA cambiar sin documentar el por qué en historial.
# =============================================================================

version: "4.0"
last_updated: 2026-02-XX
updated_by: "Claude + Humano"

# -----------------------------------------------------------------------------
# POSITION SIZING
# -----------------------------------------------------------------------------
position_sizing:
  principle: |
    Mayor calidad y convicción = mayor posición permitida.
    Pero crecimiento orgánico (ganancias) no debe forzar venta de ganadores.

  max_by_tier:
    tier_a:
      value: 10%
      justification: |
        Quality Compounders tienen menor riesgo de pérdida permanente.
        10% permite concentración en mejores ideas sin exceso.
      override_conditions:
        - "Si posición creció orgánicamente desde <10% y tesis intacta → HOLD hasta 12%"
        - "Si MoS < 0% (sobrevaluada) → TRIM a 7%"

    tier_b:
      value: 7%
      justification: |
        Quality Value tiene riesgo moderado.
        7% es balance entre convicción y diversificación.
      override_conditions:
        - "Si posición creció orgánicamente y MoS > 10% → HOLD hasta 9%"
        - "Si MoS < 0% → TRIM a 5%"

    tier_c:
      value: 5%
      justification: |
        Special Situations tienen mayor riesgo.
        Limitar exposición a ideas menos seguras.
      override_conditions:
        - "NINGUNA excepción. Tier C siempre max 5%"

  organic_growth_policy:
    principle: |
      Si una posición crece porque la acción sube (no porque añadí),
      NO es obligatorio vender solo por superar el límite.
    conditions_to_hold:
      - "Tesis original sigue intacta"
      - "MoS actual > 0% (no sobrevaluada)"
      - "No hay mejor oportunidad en pipeline"
      - "Documentar decisión de HOLD con argumentos"
    conditions_to_trim:
      - "Tesis debilitada"
      - "MoS < 0% (sobrevaluada significativamente)"
      - "Hay oportunidad claramente mejor en watchlist"
      - "Posición > tier_max + 5% (ej: Tier A > 15%)"

# -----------------------------------------------------------------------------
# GEOGRAPHY LIMITS
# -----------------------------------------------------------------------------
geography:
  principle: |
    Riesgo país NO es igual para todos.
    Países desarrollados estables pueden tener mayor exposición.

  limits_by_category:
    developed_stable:
      countries: ["US", "UK", "Germany", "France", "Netherlands", "Switzerland", "Denmark"]
      max: 50%
      justification: "Mercados profundos, rule of law, baja volatilidad política"

    developed_other:
      countries: ["Italy", "Spain", "Belgium", "Portugal", "Austria", "Ireland"]
      max: 35%
      justification: "Desarrollados pero con más riesgo político/fiscal"

    emerging:
      countries: ["Brazil", "Mexico", "India", "China", "Poland"]
      max: 15%
      justification: "Mayor volatilidad, riesgo divisa, governance concerns"

    frontier:
      countries: ["Georgia", "Vietnam", "Nigeria"]
      max: 5%
      justification: "Alto riesgo, baja liquidez, governance limitado"

  override_conditions:
    - "En crisis específica de país → reducir límite temporalmente"
    - "Si >80% de posiciones de una categoría son Tier A → puede extenderse 5%"

# -----------------------------------------------------------------------------
# SECTOR LIMITS
# -----------------------------------------------------------------------------
sector:
  principle: |
    Evitar concentración sectorial excesiva.
    Pero sectores defensivos pueden tener más peso en entornos inciertos.

  default_max: 25%

  adjustments:
    defensive_sectors:
      sectors: ["Healthcare", "Consumer Staples", "Utilities"]
      max: 30%
      condition: "En entorno macro incierto o recesión esperada"

    cyclical_sectors:
      sectors: ["Industrials", "Materials", "Consumer Discretionary"]
      max: 20%
      condition: "En late-cycle o recesión esperada"

    high_growth_sectors:
      sectors: ["Technology"]
      max: 25%
      condition: "Solo si posiciones son Tier A/B quality"

# -----------------------------------------------------------------------------
# CASH MANAGEMENT
# -----------------------------------------------------------------------------
cash:
  principle: |
    Cash es una posición. Ni demasiado (drag) ni demasiado poco (sin reserva).

  minimum: 5%
  justification_min: "Reserva para oportunidades súbitas o margin calls"

  target_range: [8%, 15%]
  justification_target: "Suficiente para 2-3 posiciones nuevas si aparecen oportunidades"

  drag_warning: 15%
  drag_critical: 20%
  justification_drag: |
    Cash >15% por >7 días indica falta de ideas o parálisis.
    Cash >20% es inaceptable salvo crisis documentada.

  override_conditions:
    - "Crisis de mercado documentada (ej: COVID, 2008) → cash hasta 30% OK"
    - "Pipeline >5 thesis listas con trigger cercano → cash 5% OK"

# -----------------------------------------------------------------------------
# PORTFOLIO COMPOSITION
# -----------------------------------------------------------------------------
portfolio:
  max_positions: 20
  justification: |
    20 posiciones permite diversificación sin dilución excesiva.
    Más de 20 → difícil seguir todas con profundidad.

  min_positions: 12
  justification_min: "Menos de 12 → concentración excesiva"

  target_composition:
    tier_a: "3-6 posiciones (core compounders)"
    tier_b: "6-10 posiciones (quality value)"
    tier_c: "4-6 posiciones (special situations)"
    tier_d: "0 posiciones (NUNCA)"

# -----------------------------------------------------------------------------
# REBALANCING
# -----------------------------------------------------------------------------
rebalancing:
  principle: |
    Rebalanceo por fundamentales, no por calendario.
    Evitar vender ganadores solo por regla.

  triggers:
    position_overweight:
      threshold: "tier_max + 3%"  # Ej: Tier A > 13%
      action: "REVISAR (no TRIM automático)"
      review_process: |
        1. ¿Tesis intacta?
        2. ¿MoS actual?
        3. ¿Hay mejor oportunidad?
        Solo TRIM si (2) o (3) son desfavorables.

    position_underweight:
      threshold: "<0.7x target"
      action: "CONSIDERAR ADD si MoS suficiente"

    monthly_review:
      enabled: false  # v4.0 elimina rebalanceo mensual forzado
      replaced_by: "Review continuo basado en eventos"

# -----------------------------------------------------------------------------
# QUALITY SCORE (sin cambios de v3.0 - JUSTIFICADO)
# -----------------------------------------------------------------------------
quality_score:
  note: "Estos parámetros están JUSTIFICADOS en v3.0, no cambian en v4.0"

  tier_a: { min: 75, max: 100, mos_required: "10-15%" }
  tier_b: { min: 55, max: 74, mos_required: "20-25%" }
  tier_c: { min: 35, max: 54, mos_required: "30-40%" }
  tier_d: { min: 0, max: 34, mos_required: "N/A - NO COMPRAR" }

  justification: |
    Los brackets de Quality Score y MoS requerido tienen lógica:
    - Mayor calidad → menor riesgo → menor MoS necesario
    - Tier D = empresas sin calidad suficiente, no importa el precio

# -----------------------------------------------------------------------------
# MONITORING THRESHOLDS
# -----------------------------------------------------------------------------
monitoring:
  price_alerts:
    daily_move: 5%
    weekly_move: 10%
    justification: "Movimientos mayores requieren investigar causa"

  staleness:
    world_view: 7  # días
    sector_view: 30  # días
    thesis_review: 90  # días sin evento material
    justification: "Información desactualizada → decisiones subóptimas"

  health_check: 14  # días
  justification_health: "Auditoría periódica del sistema"

# -----------------------------------------------------------------------------
# HISTORIAL DE CAMBIOS
# -----------------------------------------------------------------------------
change_history:
  - date: 2026-02-XX
    version: "4.0"
    changes:
      - "Position sizing por tier (antes: 7% fijo para todos)"
      - "Geography por categoría de país (antes: 35% fijo)"
      - "Eliminado rebalanceo mensual forzado"
      - "Añadido organic growth policy"
    rationale: |
      Sesión 37: El humano cuestionó por qué vender ganadores solo por regla.
      Reflexión: Las reglas mecánicas destruyen valor.
      Solución: Principios adaptativos con contexto.
```

### 5.2 Referencias Cruzadas

Cuando se implemente, actualizar:
- `CLAUDE.md` → referenciar `learning/parameters.yaml`
- `constraint_checker.py` → leer de `parameters.yaml`
- `rebalancer agent` → usar nueva lógica
- `investment-committee` → verificar contra principios, no reglas

---

## 6. PROTOCOLO EXIT ESTRATÉGICO

### 6.1 Por Qué Falta

v3.0 tiene:
- **ENTRY:** 9 gates rigurosos
- **MONITORING:** Vigilancia continua
- **TRIM:** Solo por violación de regla o kill condition

v3.0 NO tiene:
- Proceso para decidir "¿debería vender aunque no haya kill condition?"
- Comparación de "mantener X vs. comprar Y"
- Evaluación de mejor uso del capital

### 6.2 Nuevo Skill: `exit-protocol`

```markdown
# EXIT PROTOCOL - Framework v4.0

## Propósito
Proceso estructurado para decidir cuándo SALIR de una posición,
más allá de kill conditions o violaciones de reglas.

## Cuándo Ejecutar Este Protocolo

1. **Review trimestral** de cada posición
2. **Después de earnings** que cambian la narrativa
3. **Cuando hay oportunidad claramente mejor** en watchlist
4. **Cuando la posición está "dead money"** (>12 meses sin progreso hacia FV)
5. **Cuando el contexto macro cambia** materialmente

## El Framework EXIT

### Gate 1: ¿Kill Condition Activada?

```
SI alguna kill condition documentada se activa:
  → EXIT inmediato (proceso existente)
  → No necesita más análisis
```

### Gate 2: ¿Tesis Todavía Válida?

```
Verificar:
[ ] ¿El negocio sigue siendo el mismo?
[ ] ¿Las ventajas competitivas persisten?
[ ] ¿El management sigue alineado?
[ ] ¿Los fundamentales mejoran o empeoran?

SI tesis debilitada pero no kill condition:
  → Reducir posición 50%
  → Mover a "on probation" status
  → Re-evaluar en 90 días
```

### Gate 3: ¿MoS Actual?

```
Calcular MoS actual (precio actual vs FV):

SI MoS < -20% (muy sobrevaluada):
  → TRIM al menos 50%
  → Considerar EXIT completo

SI MoS entre -20% y 0%:
  → HOLD pero no ADD
  → Monitorear más frecuentemente

SI MoS > 0%:
  → Todavía hay upside
  → No vender por esta razón
```

### Gate 4: ¿Hay Mejor Oportunidad?

```
Comparar posición actual vs mejor candidato en watchlist:

Métrica: "Opportunity Score" = MoS_candidato / MoS_actual * (QS_candidato / QS_actual)

SI Opportunity Score > 1.5:
  → Considerar rotación
  → Pero verificar costes de transacción e impuestos

SI Opportunity Score > 2.0:
  → Rotación probablemente justificada
  → Documentar argumentos

EJEMPLO:
- SHEL.L actual: MoS 5%, QS 36
- NVO watchlist: MoS 38%, QS 82
- Opportunity Score = (38/5) * (82/36) = 7.6 * 2.28 = 17.3
- → Rotación claramente justificada
```

### Gate 5: ¿Dead Money?

```
SI posición lleva >12 meses sin progreso hacia FV:
  Y no hay catalizador identificado en próximos 6 meses:
  Y hay oportunidades con catalizadores claros:
  → Considerar EXIT para liberar capital

NOTA: "Dead money" no es fracaso. A veces el mercado tarda.
Pero capital atrapado tiene coste de oportunidad.
```

### Gate 6: Fricción de Salida

```
Antes de ejecutar EXIT, calcular:
- Impuestos sobre ganancias (si aplica)
- Comisiones
- Spread bid-ask
- Impacto en diversificación

SI fricción > 5% del valor:
  → Necesita Opportunity Score > 2.5 para justificar
```

## Output del Protocolo

```yaml
exit_decision:
  ticker: XXX
  date: YYYY-MM-DD
  gates_passed:
    - gate_1_kill_condition: "NO"
    - gate_2_thesis_valid: "DEBILITADA"
    - gate_3_mos_current: "-5%"
    - gate_4_better_opportunity: "NVO con OS 17.3"
    - gate_5_dead_money: "NO"
    - gate_6_friction: "2.3%"

  recommendation: "EXIT 100%"
  rationale: |
    Tesis debilitada + sobrevaluada + oportunidad claramente mejor.
    Rotación a NVO libera capital para mayor retorno esperado.

  alternative_considered: "HOLD"
  why_not_alternative: |
    MoS negativo significa downside > upside.
    NVO ofrece 38% MoS vs -5% aquí.
```

## Integración con Sistema

- Este protocolo se ejecuta via `review-agent` con flag `--exit-analysis`
- Output se guarda en `thesis/active/{ticker}/exit_analysis.md`
- Si recomendación es EXIT → pasa a `investment-committee` para aprobación
- El committee verifica los 6 gates antes de aprobar
```

### 6.3 Nuevo Agente: `exit-evaluator`

Opcional: Crear agente especializado o añadir capacidad a `review-agent`.

**Responsabilidad:** Ejecutar el protocolo EXIT cuando se le pide.

**Trigger:**
- Manual: "Evalúa si deberíamos salir de SHEL.L"
- Automático: Revisión trimestral de todas las posiciones

---

## 7. LIMPIEZA LEGACY - PLAN DETALLADO

### 7.1 Archivos a ELIMINAR

| Archivo | Razón | Verificación pre-eliminación |
|---------|-------|------------------------------|
| `config/rules.yaml` | Duplica CLAUDE.md | Confirmar que nada lo referencia |
| `config/memory_management.yaml` | No se usa | Confirmar que nada lo referencia |
| `archive/deprecated/SYSTEM_LOAD_PROTOCOL.md` | Reemplazado por session-protocol v2.0 | Ya está en deprecated/ |

### 7.2 Archivos a COMPACTAR

| Archivo | Tamaño actual | Target | Acción |
|---------|---------------|--------|--------|
| `state/system.yaml` | 1,204 líneas | <600 líneas | Ver sección 7.3 |
| `evolution/changelog.yaml` | 28K | <10K | Archivar entradas >6 meses |
| `journal/decisions/*` | Variable | Keep last 3 months | Mover viejos a archive/ |

### 7.3 Compactación de state/system.yaml

**Estructura actual (problema):**
```
state/system.yaml (1,204 líneas)
├── system info (50 líneas)
├── framework_v3_status (50 líneas)
├── portfolio_quality_analysis (100 líneas)
├── last_session_summary (200 líneas)
├── last_session_summary_archived x4 (400 líneas) ← PROBLEMA
├── calendar (300 líneas)
├── watchlist (200 líneas)
├── alerts (50 líneas)
├── standing_orders (200 líneas)
├── macro_snapshot (20 líneas)
├── maintenance (100 líneas)
```

**Estructura propuesta (v4.0):**
```
state/
├── system.yaml (~400 líneas)
│   ├── system info
│   ├── framework status
│   ├── current session summary ONLY
│   ├── maintenance
│   └── macro_snapshot
│
├── calendar.yaml (~150 líneas)
│   └── Eventos próximos 30 días
│
├── watchlist.yaml (~200 líneas)
│   └── quality_compounders, ready_to_buy, on_watch
│
├── standing_orders.yaml (~150 líneas)
│   └── Solo órdenes activas (no expiradas)
│
├── alerts.yaml (~50 líneas)
│   └── price_monitors
│
└── archive/
    └── session_summaries/
        └── session_31.md, session_32.md, etc.
```

### 7.4 Resolver Inconsistencias de Tickers

**SHEL vs SHEL.L:**
```bash
# En portfolio/current.yaml transactions:
# Buscar: "SHEL" (sin .L)
# Reemplazar por: "SHEL.L"

# Verificar que thesis/active/SHEL.L/ existe (SÍ existe)
# Verificar que NO existe thesis/active/SHEL/ (NO debe existir)
```

**LIGHT.NV vs LIGHT.AS:**
```bash
# En portfolio/current.yaml transactions:
# Buscar: "LIGHT.NV"
# Reemplazar por: "LIGHT.AS"

# Verificar que thesis/active/LIGHT.AS/ existe (SÍ existe)
```

### 7.5 Standing Orders Cleanup

**Eliminar expirados:**
- EVO.ST con expiry 2026-02-15 (si ya pasó)
- Cualquier otro con fecha pasada

**Consolidar duplicados:**
- V tiene BUY @ $280 y ADD @ $265 → mantener ambos pero clarificar orden de ejecución

---

## 8. CAMBIOS EN AGENTES Y SKILLS

### 8.1 Agentes a Modificar

| Agente | Cambio | Razón |
|--------|--------|-------|
| `rebalancer` | Usar nueva lógica de parameters.yaml | No TRIM automático |
| `review-agent` | Añadir `--exit-analysis` flag | Integrar protocolo EXIT |
| `investment-committee` | Verificar principios, no solo reglas | Permitir excepciones documentadas |
| `constraint-checker` | Leer de parameters.yaml | Centralizar parámetros |

### 8.2 Skills a Modificar

| Skill | Cambio | Razón |
|-------|--------|-------|
| `investment-rules` | Referenciar parameters.yaml | Source of truth único |
| `portfolio-constraints` | Actualizar con nuevos límites por tier | Sizing dinámico |
| `session-protocol` | Actualizar cash thresholds desde parameters | Consistencia |

### 8.3 Skills NUEVOS a Crear

| Skill | Propósito |
|-------|-----------|
| `exit-protocol` | Documentación del proceso EXIT (sección 6.2) |
| `parameter-management` | Cómo usar y modificar parameters.yaml |
| `exception-documentation` | Cómo documentar excepciones a principios |

### 8.4 Actualización de CLAUDE.md

**Secciones a modificar:**

1. **Quality Tiers table:** Actualizar max position por tier
2. **Reglas Duras:** Convertir en "Principios con Excepciones"
3. **Referencias:** Añadir `learning/parameters.yaml`
4. **Self-Check:** Añadir "¿Documenté excepciones?"

**Nueva sección a añadir:**

```markdown
## Framework v4.0 - Principios Adaptativos

### Diferencia con v3.0

v3.0 tenía REGLAS fijas: "máximo 7% por posición"
v4.0 tiene PRINCIPIOS con contexto: "máximo 10% Tier A, 7% Tier B, 5% Tier C,
con excepciones documentadas si posición creció orgánicamente"

### Fuente de Verdad de Parámetros

TODOS los parámetros del sistema están en `learning/parameters.yaml`.
Incluye valores, justificaciones, y condiciones de override.
NUNCA hardcodear parámetros en otros archivos.

### Excepciones

Puedo hacer excepciones a los principios SI:
1. Documento el argumento
2. El argumento es sólido (no "porque sí")
3. Registro la excepción para aprender de ella

Ejemplo válido: "HOLD ADBE al 11% porque MoS sigue siendo 15% y no hay mejor oportunidad"
Ejemplo inválido: "HOLD ADBE al 11% porque no quiero vender" (sin argumento)
```

---

## 9. ESTRUCTURA DE FICHEROS PROPUESTA

### 9.1 Estructura v4.0

```
/home/angel/value_invest2/
│
├── CLAUDE.md                      # Master spec (actualizado v4.0)
├── README.md                      # Project overview
│
├── .claude/
│   ├── agents/                    # 23 agentes (sin cambios estructurales)
│   ├── skills/                    # 30+ skills
│   │   ├── exit-protocol/         # NUEVO
│   │   ├── parameter-management/  # NUEVO
│   │   └── ...
│   ├── rules/                     # 6 rules (actualizar referencias)
│   ├── commands/
│   └── hooks/
│
├── learning/
│   ├── parameters.yaml            # NUEVO - Source of truth de parámetros
│   ├── system_config.yaml         # Mantener pero referenciar a parameters
│   ├── lessons.yaml
│   └── key_learnings.md
│
├── state/
│   ├── system.yaml                # COMPACTADO (~400 líneas)
│   ├── calendar.yaml              # NUEVO - Extraído de system.yaml
│   ├── watchlist.yaml             # NUEVO - Extraído de system.yaml
│   ├── standing_orders.yaml       # NUEVO - Extraído de system.yaml
│   ├── alerts.yaml                # NUEVO - Extraído de system.yaml
│   ├── news_digest.yaml           # Sin cambios
│   ├── market_pulse.yaml          # Sin cambios
│   ├── risk_alerts.yaml           # Sin cambios
│   └── archive/
│       └── session_summaries/     # NUEVO - Session summaries archivados
│
├── portfolio/
│   ├── current.yaml               # Tickers normalizados
│   ├── history.yaml               # COMPLETAR con trims
│   └── target_allocation.yaml
│
├── thesis/
│   ├── active/                    # 20 posiciones
│   ├── research/                  # Candidatos
│   ├── watchlist/                 # Con thesis parcial
│   └── archive/                   # Cerradas con lesson learned
│
├── world/
│   ├── current_view.md
│   └── sectors/                   # 13 sector views
│
├── tools/                         # 8 tools Python
│   └── constraint_checker.py      # ACTUALIZAR para leer parameters.yaml
│
├── docs/
│   ├── framework_v3.0_final_design.md
│   └── evolution_framework_4.0.md  # ESTE DOCUMENTO
│
├── config/                        # ELIMINAR (legacy)
│
├── evolution/                     # COMPACTAR
│   ├── changelog.yaml             # Solo últimos 6 meses
│   └── archive/                   # Viejos
│
└── archive/                       # Histórico
    ├── session_summaries/
    └── deprecated/                # VACIAR después de verificar
```

### 9.2 Archivos que Desaparecen

- `config/rules.yaml` → ELIMINADO
- `config/memory_management.yaml` → ELIMINADO
- `archive/deprecated/*` → ELIMINADO (después de verificar)

### 9.3 Archivos que se Crean

- `learning/parameters.yaml` → NUEVO
- `state/calendar.yaml` → Extraído de system.yaml
- `state/watchlist.yaml` → Extraído de system.yaml
- `state/standing_orders.yaml` → Extraído de system.yaml
- `state/alerts.yaml` → Extraído de system.yaml
- `state/archive/session_summaries/` → Directorio para summaries viejos
- `.claude/skills/exit-protocol/SKILL.md` → NUEVO

---

## 10. PLAN DE IMPLEMENTACIÓN POR FASES

### Fase 0: Preparación (15 min)
**Objetivo:** Backup y verificación pre-cambios

```
[ ] Crear backup completo del directorio
[ ] Verificar que portfolio_stats.py funciona
[ ] Verificar que constraint_checker.py funciona
[ ] Documentar estado actual para rollback si necesario
```

### Fase 1: Limpieza Legacy (30 min)
**Objetivo:** Eliminar archivos obsoletos y resolver inconsistencias

```
[ ] ELIMINAR config/rules.yaml
[ ] ELIMINAR config/memory_management.yaml
[ ] ELIMINAR archive/deprecated/SYSTEM_LOAD_PROTOCOL.md
[ ] NORMALIZAR ticker SHEL → SHEL.L en transactions
[ ] NORMALIZAR ticker LIGHT.NV → LIGHT.AS en transactions
[ ] LIMPIAR standing orders expirados
[ ] ARCHIVAR evolution/backups/ >3 meses
```

### Fase 2: Compactación system.yaml (45 min)
**Objetivo:** Particionar el archivo monstruo

```
[ ] CREAR state/calendar.yaml (extraer calendar section)
[ ] CREAR state/watchlist.yaml (extraer watchlist section)
[ ] CREAR state/standing_orders.yaml (extraer standing_orders section)
[ ] CREAR state/alerts.yaml (extraer alerts section)
[ ] CREAR state/archive/session_summaries/ directorio
[ ] MOVER last_session_summary_archived a archive/
[ ] VERIFICAR que system.yaml queda <500 líneas
[ ] ACTUALIZAR referencias en agentes que leen system.yaml
```

### Fase 3: Crear parameters.yaml (60 min)
**Objetivo:** Centralizar parámetros con justificaciones

```
[ ] CREAR learning/parameters.yaml con estructura de sección 5
[ ] DOCUMENTAR cada parámetro con justificación
[ ] DOCUMENTAR condiciones de override
[ ] VERIFICAR que todos los 23 parámetros están incluidos
```

### Fase 4: Actualizar Tools (30 min)
**Objetivo:** Que tools lean de parameters.yaml

```
[ ] MODIFICAR constraint_checker.py para leer de parameters.yaml
[ ] VERIFICAR que constraint_checker sigue funcionando
[ ] DOCUMENTAR cambios en tools-reference.md
```

### Fase 5: Crear Exit Protocol (45 min)
**Objetivo:** Documentar proceso EXIT que falta

```
[ ] CREAR .claude/skills/exit-protocol/SKILL.md
[ ] CREAR .claude/skills/exit-protocol/README.md
[ ] ACTUALIZAR review-agent para soportar --exit-analysis
[ ] DOCUMENTAR en agent-registry
```

### Fase 6: Actualizar CLAUDE.md (30 min)
**Objetivo:** Reflejar v4.0 en documento principal

```
[ ] ACTUALIZAR sección Quality Tiers con nuevos max positions
[ ] CONVERTIR "Reglas Duras" en "Principios Adaptativos"
[ ] AÑADIR referencia a parameters.yaml
[ ] AÑADIR referencia a exit-protocol
[ ] ACTUALIZAR versión a 4.0
```

### Fase 7: Actualizar Agentes y Skills (45 min)
**Objetivo:** Consistencia del sistema

```
[ ] ACTUALIZAR rebalancer para usar nueva lógica
[ ] ACTUALIZAR investment-committee para verificar principios
[ ] ACTUALIZAR investment-rules skill
[ ] ACTUALIZAR portfolio-constraints skill
[ ] VERIFICAR consistencia con agent-registry
```

### Fase 8: Validación (30 min)
**Objetivo:** Confirmar que todo funciona

```
[ ] EJECUTAR portfolio_stats.py → debe funcionar
[ ] EJECUTAR constraint_checker.py CHECK ADBE 500 → debe funcionar
[ ] EJECUTAR quality_scorer.py ADBE → debe funcionar
[ ] SIMULAR decisión de HOLD posición >7% → documentar excepción
[ ] SIMULAR exit analysis de SHEL.L → verificar protocolo
[ ] VERIFICAR que CLAUDE.md es coherente
[ ] VERIFICAR que no hay referencias rotas
```

### Fase 9: Documentación Final (15 min)
**Objetivo:** Registrar cambios

```
[ ] ACTUALIZAR state/system.yaml con framework_v4_status
[ ] ACTUALIZAR evolution/changelog.yaml
[ ] CREAR session summary de implementación
```

---

## 11. CHECKLIST DE VALIDACIÓN

### Pre-Implementación
```
[ ] Backup creado
[ ] Documento evolution_framework_4.0.md leído completamente
[ ] Humano aprobó el plan
[ ] No hay operaciones de mercado pendientes
```

### Post-Fase 1 (Limpieza)
```
[ ] config/rules.yaml no existe
[ ] config/memory_management.yaml no existe
[ ] Todos los tickers normalizados (grep "SHEL[^.]" returns 0)
[ ] Standing orders sin fechas pasadas
```

### Post-Fase 2 (Compactación)
```
[ ] state/system.yaml < 500 líneas
[ ] state/calendar.yaml existe y tiene eventos
[ ] state/watchlist.yaml existe y tiene entries
[ ] state/standing_orders.yaml existe y tiene orders
[ ] Ningún agente falla al leer state/
```

### Post-Fase 3 (Parameters)
```
[ ] learning/parameters.yaml existe
[ ] Contiene los 23 parámetros documentados
[ ] Cada parámetro tiene justificación
[ ] Cada parámetro tiene override_conditions si aplica
```

### Post-Fase 4 (Tools)
```
[ ] constraint_checker.py lee de parameters.yaml
[ ] constraint_checker.py CHECK funciona
[ ] constraint_checker.py REPORT funciona
```

### Post-Fase 5 (Exit Protocol)
```
[ ] .claude/skills/exit-protocol/SKILL.md existe
[ ] Contiene los 6 gates documentados
[ ] review-agent puede ejecutar exit analysis
```

### Post-Fase 6 (CLAUDE.md)
```
[ ] Versión dice 4.0
[ ] Referencia a parameters.yaml existe
[ ] Referencia a exit-protocol existe
[ ] "Reglas Duras" ahora dice "Principios Adaptativos"
```

### Post-Fase 7 (Agentes/Skills)
```
[ ] agent-registry tiene 23+ agentes
[ ] Todos los skills modificados son coherentes
[ ] No hay referencias a parámetros hardcodeados (excepto en parameters.yaml)
```

### Post-Fase 8 (Validación)
```
[ ] portfolio_stats.py funciona
[ ] constraint_checker.py funciona
[ ] Una decisión de excepción puede documentarse
[ ] Un exit analysis puede ejecutarse
```

### Validación Final
```
[ ] Sistema completo funciona
[ ] Humano puede operar normalmente
[ ] No hay regresiones
[ ] Documentación actualizada
```

---

## 12. MÉTRICAS DE ÉXITO

### Métricas Cuantitativas (medir en 3 meses)

| Métrica | Baseline v3.0 | Target v4.0 | Cómo Medir |
|---------|---------------|-------------|------------|
| Excepciones documentadas | 0 | 5+ | Contar en thesis/ |
| TRIMs por regla mecánica | 4 (SHEL, DTE, TEP, HRB) | 0 | Contar en transactions |
| TRIMs por argumento fundamental | 0 | 2+ | Contar en transactions |
| EXIT estratégicos | 0 | 1+ | Contar rotaciones por oportunidad-coste |
| Tiempo en encontrar parámetro | Variable | <30 seg | parameters.yaml |

### Métricas Cualitativas

| Aspecto | v3.0 | v4.0 Target |
|---------|------|-------------|
| ¿Puedo justificar cada TRIM? | A veces | Siempre |
| ¿Hay proceso para EXIT estratégico? | No | Sí (6 gates) |
| ¿Sé por qué cada parámetro tiene ese valor? | No | Sí (justificado) |
| ¿Sistema está limpio de legacy? | No | Sí |
| ¿Puedo adaptar reglas con argumento? | No | Sí |

### Criterio de Rollback

Si después de implementar v4.0:
- Más de 3 errores críticos en primeras 2 semanas
- Pérdida atribuible a cambios >5% del portfolio
- Humano expresa insatisfacción con nuevo sistema

→ Rollback a v3.0 desde backup

---

## ANEXO A: CONVERSACIÓN ORIGINAL (Sesión 37)

Para contexto futuro, aquí está el resumen de la conversación que originó v4.0:

**Humano (después de ejecutar HRB ADD):**
> "Vale hay cosas que me preocupan y creo que debemos de mejorar, por ejemplo hablas de Shell que monitorear y tenemos monitores y también tenemos protocolos para comprar, lo que no me queda claro es si tenemos un protocolo para cerrar operaciones cuando es momento de salirse y buscar otro activo mejor?"

**Humano (sobre TRIMs):**
> "En algunas ocasiones me hablas de hacer TRIM de operaciones porque incumple con alguna regla por ejemplo max 7% o country >35% etc.. entonces aquí tengo varias preguntas por ejemplo si una acción ha subido y alcanza >7% vamos a vender solo por la regla? no sería mejor dejarla crecer más aunque se incumple regla?"

**Humano (sobre reglas fijas):**
> "Por otro lado pienso que las reglas son parámetros fijos aprendidos del pasado, como una especie de bias y pienso que las reglas deberían de ser dinámicas y cambiantes en base a argumentos claro que un inversor profesional es capaz de adaptar y tú lo eres."

**Humano (sobre auditoría):**
> "Necesitaría varias cosas, primero reflexionar juntos sobre esto sin cambiar el sistema, necesitamos saber dónde y por qué usas parámetros y configuraciones fijas. Por otro lado este es un sistema que ha ido evolucionando contigo y veo fichero yaml y configuraciones y prompts que parece que son legacy y no usas. Puedes hacer un análisis y auditoría completa del directorio y del sistema completo?"

**Mi reflexión:**
- Reconocí que las reglas son arbitrarias (¿por qué 7%?)
- Reconocí que el TRIM mecánico destruye valor
- Identifiqué que falta protocolo EXIT
- Ejecuté auditoría completa: 23 parámetros hardcodeados, 4 inconsistencias, 10 items legacy

**Humano (pidiendo documento):**
> "Necesito que crees un documento en docs/evolution_framework_4.0.md en este documento quiero que dejes detalles la propuesta detallada de implementación para ti mismo en siguientes sesiones, quiero que cuando lo leas en un futuro tengas toda la información incluso de lo que hemos hablado para que a ti cuando te pida hacer los cambios sepas qué hacer."

---

## ANEXO B: PRINCIPIOS DE DISEÑO v4.0

### Principio 1: Argumentos > Reglas
Una decisión con argumento sólido es mejor que seguir una regla ciegamente.

### Principio 2: Documentar Excepciones
Cada excepción a un principio debe documentarse para aprender de ella.

### Principio 3: Source of Truth Único
Cada tipo de información tiene UN lugar canónico. No duplicar.

### Principio 4: Justificar Parámetros
Cada parámetro debe tener una razón documentada de por qué tiene ese valor.

### Principio 5: Evolución Argumentada
Cambios al sistema requieren argumento. No cambiar porque sí.

### Principio 6: Gestores Piensan, No Solo Ejecutan
Claude es gestor, no robot. Debe pensar, adaptar, y justificar.

---

## ANEXO C: GLOSARIO v4.0

| Término | Definición |
|---------|------------|
| **Regla** | Instrucción fija sin contexto ni excepciones |
| **Principio** | Guía con contexto, justificación, y condiciones de override |
| **Organic Growth** | Cuando posición crece porque la acción sube, no porque añadí |
| **Opportunity Score** | Métrica para comparar mantener vs. rotar: (MoS_nuevo/MoS_actual)*(QS_nuevo/QS_actual) |
| **EXIT Estratégico** | Vender por mejor uso del capital, no por kill condition |
| **Dead Money** | Posición sin progreso hacia FV por >12 meses sin catalizador |
| **Excepción Documentada** | Override a un principio con argumento explícito registrado |

---

**FIN DEL DOCUMENTO**

*Este documento debe leerse completamente antes de implementar v4.0.*
*Tiempo estimado de implementación: 5-6 horas distribuidas en 2-3 sesiones.*
*Requiere aprobación del humano antes de comenzar.*
