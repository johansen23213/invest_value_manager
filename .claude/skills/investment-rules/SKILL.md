---
name: investment-rules
description: "Framework v4.0 - Quality Score, Principios Adaptativos, razonamiento sobre reglas"
user-invocable: false
disable-model-invocation: false
---

# Investment Rules - Framework v4.0

## EVOLUCIÓN DEL FRAMEWORK

```
v2.0: "Compra barato" → Value traps
v3.0: "Compra calidad" → Reglas mecánicas destruían valor
v4.0: "Principios adaptativos" → Razonamiento > reglas
```

**Cambio clave v4.0:** NO hay límites fijos (7%, 25%, 35%).
El sizing y constraints se deciden por razonamiento documentado.
Ver `learning/principles.md` y `learning/decisions_log.yaml`.

---

## PARTE 1: QUALITY SCORE (0-100) - Sin cambios

### Principio: Si no se puede medir, no se puede gestionar

**Usar `tools/quality_scorer.py` para cálculo.**

```
QUALITY SCORE = Financial (40) + Growth (25) + Moat Evidence (25) + Capital Allocation (10)
```

### 1.1 FINANCIAL QUALITY (40 puntos)

| Métrica | Cálculo | Puntos |
|---------|---------|--------|
| **ROIC Spread** | ROIC - WACC | >15pp: 15, >10pp: 12, >5pp: 8, >0pp: 4, <0pp: 0 |
| **FCF Margin** | FCF / Revenue | >20%: 10, >15%: 8, >10%: 5, >5%: 2, <5%: 0 |
| **Leverage** | Net Debt / EBITDA | <1x: 10, <2x: 8, <3x: 5, <4x: 2, >4x: 0 |
| **FCF Consistency** | Años FCF+ últimos 5 | 5/5: 5, 4/5: 4, 3/5: 2, <3/5: 0 |

### 1.2 GROWTH QUALITY (25 puntos)

| Métrica | Cálculo | Puntos |
|---------|---------|--------|
| **Revenue CAGR 5yr** | CAGR | >15%: 10, >10%: 8, >5%: 5, >0%: 2, <0%: 0 |
| **EPS CAGR 5yr** | CAGR | >15%: 10, >10%: 8, >5%: 5, >0%: 2, <0%: 0 |
| **Gross Margin Trend** | GM vs 3yr | Expanding >1pp: 5, Stable: 3, Declining: 0 |

### 1.3 MOAT EVIDENCE (25 puntos)

| Métrica | Cálculo | Puntos |
|---------|---------|--------|
| **Gross Margin Premium** | GM vs sector median | >10pp: 10, >5pp: 7, ±5pp: 4, <-5pp: 0 |
| **Market Position** | Rank | #1-2: 8, #3-5: 5, #6-10: 2, >10: 0 |
| **ROIC Persistence** | Años ROIC>WACC en 10yr | 10/10: 7, 8-9: 5, 6-7: 3, <6: 0 |

### 1.4 CAPITAL ALLOCATION (10 puntos)

| Métrica | Cálculo | Puntos |
|---------|---------|--------|
| **Shareholder Returns** | Años consecutivos | 10+yr: 5, 5-9yr: 3, 1-4yr: 1, 0/cut: 0 |
| **Insider Ownership** | % insiders | >5%: 5, >2%: 3, >0.5%: 1, <0.5%: 0 |

---

## PARTE 2: QUALITY TIERS

| Tier | Quality Score | MoS Típico | Descripción |
|------|--------------|------------|-------------|
| **A** | 75-100 | ~10-15% | Elite Compounders |
| **B** | 55-74 | ~20-25% | Quality Value |
| **C** | 35-54 | ~30-40% | Special Situations |
| **D** | <35 | N/A | **NO COMPRAR** |

**NOTA v4.0:** Los MoS son rangos orientativos, NO límites fijos.
El MoS específico se decide por razonamiento caso a caso.
Consultar `learning/decisions_log.yaml` para precedentes.

---

## PARTE 3: INVESTMENT COMMITTEE GATES v4.0

### Gate 1: Quality Score
```
[ ] Quality Score calculado: ___/100
[ ] Tier asignado: [A/B/C/D]
[ ] Si Tier D → STOP, no proceder
```

### Gate 2: Entendimiento del Negocio
```
[ ] Business Analysis Framework completado
[ ] Puedo explicar en 2 minutos
[ ] Sé POR QUÉ está barata + contra-tesis
```

### Gate 3: Proyección Fundamentada
```
[ ] Revenue growth derivado (no default)
[ ] WACC calculado (no default)
[ ] Escenarios Bear/Base/Bull
```

### Gate 4: Valoración Multi-Método
```
[ ] Método 1 apropiado al tipo: FV €___
[ ] Método 2: FV €___
[ ] MoS calculado: ___%
```

### Gate 5: MoS Adequacy
```
[ ] ¿El MoS es suficiente para el riesgo de este tier?
[ ] ¿Es coherente con precedentes de tier similar?
NOTA: No hay número fijo. Razonar caso a caso.
```

### Gate 6: Sizing Razonamiento (NUEVO v4.0)
```
[ ] ¿El sizing propuesto tiene razonamiento explícito?
[ ] ¿Es coherente con precedentes similares?
[ ] Si se desvía de precedentes, ¿está justificado?
[ ] Si cae 50%, ¿el impacto es aceptable para esta convicción?
NOTA: No hay límite fijo. Razonar desde principios.
```

### Gate 7: Portfolio Context (NUEVO v4.0)
```
[ ] ¿Cómo afecta la concentración sectorial?
[ ] ¿Cómo afecta la exposición geográfica?
[ ] ¿Hay correlación con otras posiciones?
[ ] ¿El razonamiento considera estos factores?
NOTA: No verificar vs límites, verificar que se CONSIDERÓ.
```

### Gate 8: Contexto Macro y Timing
```
[ ] World view revisado
[ ] Sector view existe
[ ] Catalizador identificado
```

### Gate 9: Kill Conditions y Documentación
```
[ ] Kill conditions definidas
[ ] Thesis completa documentada
[ ] Razonamiento de sizing documentado
[ ] Precedentes considerados documentados
```

---

## PARTE 4: PRINCIPIOS DE SIZING (v4.0)

### Principio Central
El sizing refleja convicción y riesgo, NO un número fijo.

### Preguntas Guía
1. "Si cae 50%, ¿cuánto pierdo? ¿Es coherente con mi convicción?"
2. "¿Qué sizing usé en decisiones similares?"
3. "¿Por qué este caso sería diferente?"

### Patrones Observados (NO límites)
Basado en precedentes en `decisions_log.yaml`:
- Tier A (Quality Compounders): típicamente 3-5% inicial
- Tier B (Quality Value): típicamente 3-5% full position
- Tier C (Special Situations): típicamente 2-4%

### Proceso
1. Consultar `learning/decisions_log.yaml` para precedentes
2. Evaluar convicción específica de esta tesis
3. Considerar contexto del portfolio (concentración, correlación)
4. Documentar razonamiento explícito
5. Si me desvío de precedentes, explicar por qué

---

## PARTE 5: PRINCIPIOS DE VENTA (v4.0)

### Principio Central
**NUNCA vender solo porque "se rompió una regla".**

### Cuándo Vender (con argumento)

**Por Kill Condition (INMEDIATO):**
- Management fraud
- Pérdida permanente de ventaja competitiva
- QS cae a Tier D

**Por Valoración (razonado):**
- MoS se vuelve significativamente negativo (<-20%)
- Mejor oportunidad clara (Opportunity Score >2.0)

**Por Thesis Invalidada:**
- Los fundamentales que justificaban la compra ya no existen

### Cuándo NO Vender
- Solo porque posición creció a >X%
- Solo porque el mercado cayó
- Solo porque un analyst dijo algo
- Sin argumento explícito

### EXIT Protocol
Para decisiones de salida complejas, usar `.claude/skills/exit-protocol/SKILL.md`.
6 gates: Kill Condition → Tesis → MoS → Opportunity Score → Dead Money → Fricción

---

## PARTE 6: NUNCA (Inmutable)

1. **Comprar Tier D (QS <35)** - Esto SÍ es regla fija
2. **Operar sin thesis documentada**
3. **Usar apalancamiento**
4. **Saltarse Investment Committee**
5. **Usar defaults de growth/WACC sin derivación**
6. **Comprar sin entender por qué está barata**
7. **Vender sin argumento explícito**
8. **Ignorar kill conditions**

---

## PARTE 7: REFERENCIAS v4.0

| Necesito... | Ver... |
|-------------|--------|
| Principios de inversión | `learning/principles.md` |
| Precedentes de decisiones | `learning/decisions_log.yaml` |
| Validar consistencia | `tools/consistency_checker.py` |
| Detectar drift | `tools/drift_detector.py` |
| EXIT Protocol | `.claude/skills/exit-protocol/SKILL.md` |

---

## QUICK REFERENCE: Proceso v4.0

```
1. Calcular Quality Score → Determina tier
2. Si Tier D → STOP
3. Analizar negocio → Entender por qué barata
4. Valorar → MoS
5. Consultar precedentes → ¿Cómo decidí antes en casos similares?
6. Razonar sizing → Convicción + riesgo + contexto
7. Pasar 9 gates → Investment Committee
8. Documentar → decisions_log.yaml
```

---

**Framework Version:** 4.0
**Última actualización:** 2026-02-05
