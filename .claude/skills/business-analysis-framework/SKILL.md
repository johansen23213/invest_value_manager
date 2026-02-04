---
name: business-analysis-framework
description: "Framework v3.0 - Deep business understanding + Quality Score. MANDATORY before any valuation."
user-invocable: false
disable-model-invocation: false
---

# Business Analysis Framework v3.0

## Propósito
No compramos NADA que no entendamos profundamente. Este framework es OBLIGATORIO antes de cualquier valoración.

## FLUJO v3.0

```
SECCIÓN 0: QUALITY SCORE (NUEVO - PRIMERO)
    ↓
SECCIÓN 1: Modelo de Negocio
    ↓
SECCIÓN 2: Por Qué Está Barata
    ↓
SECCIÓN 3: Catalizadores y Timeframe
    ↓
SECCIÓN 4: Conexión Macro
    ↓
OUTPUT → Thesis con QS + Business Understanding
```

---

## SECCIÓN 0: QUALITY SCORE (NUEVO - OBLIGATORIO)

### 0.1 Calcular Quality Score

**Usar `python3 tools/quality_scorer.py TICKER` si disponible, o calcular manualmente:**

#### FINANCIAL QUALITY (40 puntos)
| Métrica | Valor | Puntos |
|---------|-------|--------|
| ROIC Spread (ROIC - WACC) | ___pp | >15pp: 15, >10pp: 12, >5pp: 8, >0pp: 4, <0: 0 |
| FCF Margin (FCF/Revenue) | ___% | >20%: 10, >15%: 8, >10%: 5, >5%: 2, <5%: 0 |
| Leverage (ND/EBITDA) | ___x | <1x: 10, <2x: 8, <3x: 5, <4x: 2, >4x: 0 |
| FCF Consistency (años +) | ___/5 | 5: 5, 4: 4, 3: 2, <3: 0 |
| **Subtotal Financial** | | **/40** |

#### GROWTH QUALITY (25 puntos)
| Métrica | Valor | Puntos |
|---------|-------|--------|
| Revenue CAGR 5yr | ___% | >15%: 10, >10%: 8, >5%: 5, >0%: 2, <0%: 0 |
| EPS CAGR 5yr | ___% | >15%: 10, >10%: 8, >5%: 5, >0%: 2, <0%: 0 |
| Gross Margin Trend | ___ | Expanding: 5, Stable: 3, Declining: 0 |
| **Subtotal Growth** | | **/25** |

#### MOAT EVIDENCE (25 puntos)
| Métrica | Valor | Puntos |
|---------|-------|--------|
| GM Premium vs Sector | ___pp | >10pp: 10, >5pp: 7, ±5pp: 4, <-5pp: 0 |
| Market Position | #___ | #1-2: 8, #3-5: 5, #6-10: 2, >10: 0 |
| ROIC Persistence | ___/10yr | 10: 7, 8-9: 5, 6-7: 3, <6: 0 |
| **Subtotal Moat** | | **/25** |

#### CAPITAL ALLOCATION (10 puntos)
| Métrica | Valor | Puntos |
|---------|-------|--------|
| Shareholder Returns | ___yr | 10+: 5, 5-9: 3, 1-4: 1, 0: 0 |
| Insider Ownership | ___% | >5%: 5, >2%: 3, >0.5%: 1, <0.5%: 0 |
| **Subtotal CapAlloc** | | **/10** |

### 0.2 QUALITY SCORE TOTAL: ___/100

### 0.3 Tier Asignado

| Score | Tier | MoS Requerido | Acción |
|-------|------|---------------|--------|
| 75-100 | **A** | 10-15% | Quality Compounder |
| 55-74 | **B** | 20-25% | Quality Value |
| 35-54 | **C** | 30-40% | Special Situation (need catalyst) |
| <35 | **D** | N/A | **STOP - NO PROCEDER** |

**Si Tier D → NO CONTINUAR con el análisis. Documentar razón y archivar.**

---

## SECCIÓN 1: Modelo de Negocio

### 1.1 Qué problema resuelve
- ¿Qué dolor específico soluciona?
- ¿Para qué segmento de clientes?
- ¿Es un "must-have" o "nice-to-have"?

### 1.2 Cómo genera ingresos
| Tipo | Ejemplos | Características |
|------|----------|-----------------|
| Suscripción | SaaS, seguros, utilities | Recurrente, predecible |
| Transacción | Retail, pagos | Variable, depende de volumen |
| Consumibles | Pharma, CPG | Repeat purchase, sticky |
| Proyecto | Construcción, consultoría | Lumpy, backlog visibility |
| Licensing | IP, software | Alto margen, escalable |

**Responder:** ¿Cuál es el modelo dominante? ¿% recurrente vs one-time?

### 1.3 Unit Economics (CRÍTICO)
```
CAC (Customer Acquisition Cost) = €____
LTV (Lifetime Value) = €____
LTV/CAC Ratio = ____
  <1x = DESTRUYE valor (REJECT)
  1-3x = Negocio mediocre
  >3x = Buen negocio
  >5x = Excelente

Payback Period = ____ meses
  <12 meses = excelente
  >24 meses = riesgo
```

### 1.4 Estructura de Márgenes
```
Gross Margin = ____% (vs sector median: ___%)
Operating Margin = ____%
Net Margin = ____%
FCF Margin = ____% (KEY para Quality Score)

Tendencia 5 años: [Expandiendo / Estable / Comprimiendo]
```

### 1.5 Requerimientos de Capital
| Tipo | Capex % Rev | Working Capital | Ejemplo |
|------|-------------|-----------------|---------|
| Asset-light | <5% | Bajo | Software |
| Asset-medium | 5-10% | Variable | Retail |
| Asset-heavy | >10% | Alto | Utilities |

**Responder:**
- Capex mantenimiento: ___% de revenue
- Working capital es: [fuente / uso] de cash

---

## SECCIÓN 2: Por Qué Está Barata (OBLIGATORIO)

### 2.1 Narrativa del Mercado
¿Qué cree el mercado?
- [ ] Declive secular de industria
- [ ] Disrupción tecnológica
- [ ] Problemas de management
- [ ] Balance deteriorándose
- [ ] Márgenes bajo presión
- [ ] Pérdida de market share
- [ ] Riesgo regulatorio
- [ ] Riesgo geopolítico
- [ ] Guidance decepcionante
- [ ] Sector out-of-favor
- [ ] Otro: _________

### 2.2 Mi Contra-Tesis
Para CADA razón marcada:
```
Mercado cree: [X]
Yo creo: [Y]
Mi evidencia: [Z]
Prob de que esté equivocado: [%]
```

### 2.3 Value Trap Checklist
| Factor | SI/NO | Comentario |
|--------|-------|------------|
| Industria en declive secular | | |
| Disrupción tecnológica inminente | | |
| Management destruyendo valor | | |
| Balance deteriorándose | | |
| Insider selling masivo (>5% 12m) | | |
| Dividend cut reciente/probable | | |
| Pérdida market share >2pp 3yr | | |
| ROIC < WACC últimos 3 años | | |
| FCF negativo >2 años | | |
| Goodwill >50% equity | | |

**TOTAL: ___/10 factores SI**

**REGLA:**
- 0-2 factores: OK
- 3 factores: Tier C mínimo (MoS ≥30%)
- >3 factores: probable value trap → REJECT o MoS ≥40%

### 2.4 Mi Ventaja Informacional
¿Por qué puedo ver algo que el mercado no ve?
- [ ] Horizonte temporal más largo
- [ ] Entiendo el negocio mejor
- [ ] Mercado sobre-reacciona
- [ ] Análisis cuantitativo diferenciado
- [ ] Información pública mal interpretada
- [ ] Ninguna clara → **CAUTELA EXTREMA**

---

## SECCIÓN 3: Catalizadores y Timeframe

### 3.1 Catalizadores Identificados
| Catalizador | Timeframe | Prob | Impacto |
|-------------|-----------|------|---------|
| | 0-6m/6-12m/1-2y | H/M/L | +X% |

### 3.2 Qué Tiene Que Pasar
1. _________
2. _________
3. _________

### 3.3 Kill Conditions (OBLIGATORIO)
1. _________
2. _________
3. _________

**REGLA:** Sin kill conditions definidas → NO COMPRAR

---

## SECCIÓN 4: Conexión Macro

### 4.1 Sensibilidad Macro
| Factor | Sensibilidad | Impacto Actual |
|--------|-------------|----------------|
| Tasas de interés | H/M/L/Ninguna | |
| Recesión | H/M/L/Ninguna | |
| Inflación | H/M/L/Ninguna | |
| USD strength | H/M/L/Ninguna | |
| Commodity prices | H/M/L/Ninguna | |

### 4.2 Fit con World View
Leer `world/current_view.md` y responder:
- ¿Contexto macro es favorable/neutral/adverso?
- ¿Megatendencias ayudan o perjudican?
- ¿Ciclo económico apropiado para este tipo?

---

## OUTPUT REQUERIDO

Este framework debe producir sección "BUSINESS UNDERSTANDING" en thesis con:

```markdown
## Business Understanding

### Quality Score: [XX]/100 → Tier [A/B/C]

### Modelo de Negocio
[3-5 líneas]

### Unit Economics
- LTV/CAC: X
- FCF Margin: X%
- Capital intensity: [light/medium/heavy]

### Por Qué Está Barata
- Narrativa mercado: [X]
- Mi contra-tesis: [Y]
- Value trap score: X/10

### Catalizadores
| Catalyst | Timeline | Prob |
|----------|----------|------|
| | | |

### Kill Conditions
1. [X]
2. [Y]

### Fit Macro
[1-2 líneas]
```

---

## REGLAS DURAS

1. **NO valorar sin Quality Score calculado**
2. **NO proceder si Tier D**
3. **NO comprar sin contra-tesis documentada**
4. **NO comprar con >3 factores value trap sin MoS ≥40%**
5. **NO comprar sin kill conditions definidas**
6. **SIEMPRE leer world/current_view.md antes de análisis**
