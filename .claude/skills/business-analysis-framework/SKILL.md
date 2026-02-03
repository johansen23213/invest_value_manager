---
name: business-analysis-framework
description: Deep business understanding framework - unit economics, business model, why cheap analysis. MANDATORY before any valuation.
user-invocable: false
disable-model-invocation: false
---

# Business Analysis Framework Skill

## Propósito
No compramos NADA que no entendamos profundamente. Este framework es OBLIGATORIO antes de cualquier valoración.

## SECCIÓN 1: Modelo de Negocio (responder TODO)

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

**Responder:** ¿Cuál es el modelo dominante? ¿Qué % de ingresos es recurrente vs one-time?

### 1.3 Unit Economics (CRÍTICO)
```
CAC (Customer Acquisition Cost) = €____
  → ¿Cómo adquieren clientes? (ventas directas, marketing, partnerships)
  → ¿Tendencia? (subiendo, bajando, estable)

LTV (Lifetime Value) = €____
  → Ingreso promedio por cliente × años de retención
  → ¿Churn rate? ¿Retention rate?

LTV/CAC Ratio = ____
  → <1x = DESTRUYE valor (REJECT)
  → 1-3x = Negocio mediocre
  → >3x = Buen negocio
  → >5x = Excelente (pero verificar si es sostenible)

Payback Period = ____ meses
  → Tiempo para recuperar CAC
  → <12 meses = excelente
  → >24 meses = riesgo si funding se seca
```

### 1.4 Estructura de Márgenes
```
Gross Margin = ____%
  → ¿De dónde viene? (escala, pricing power, eficiencia operativa)
  → ¿Tendencia 5 años?
  → ¿Comparable vs peers?

Operating Margin = ____%
  → ¿Cuánto es fijo vs variable?
  → ¿Hay operating leverage? (más ventas = más margen)

Net Margin = ____%
  → ¿Impuestos atípicos?
  → ¿Intereses excesivos?
```

### 1.5 Requerimientos de Capital
| Tipo de negocio | Capex | Working Capital | Ejemplo |
|-----------------|-------|-----------------|---------|
| Asset-light | Bajo | Bajo | Software, servicios |
| Asset-medium | Medio | Variable | Retail, distribución |
| Asset-heavy | Alto | Alto | Utilities, industrials |

**Responder:**
- ¿Cuánto capex de mantenimiento necesita? (% de revenue)
- ¿Cuánto capex de crecimiento necesita para crecer 10%?
- ¿El working capital es fuente o uso de cash?

---

## SECCIÓN 2: Por Qué Está Barata (OBLIGATORIO)

**NUNCA comprar algo barato sin saber POR QUÉ está barato.**

### 2.1 Narrativa del Mercado
¿Qué cree el mercado sobre esta empresa?
- [ ] Declive secular de la industria
- [ ] Disrupción tecnológica (ej: AI, e-commerce)
- [ ] Problemas de management/governance
- [ ] Balance deteriorándose
- [ ] Márgenes bajo presión
- [ ] Pérdida de market share
- [ ] Riesgo regulatorio
- [ ] Riesgo geopolítico
- [ ] Guidance decepcionante
- [ ] Sector out-of-favor (rotación cíclica)
- [ ] Otro: _________

### 2.2 Mi Contra-Tesis
Para CADA razón que el mercado cree, responder:
```
Mercado cree: [X]
Yo creo: [Y]
Mi evidencia: [Z]
Probabilidad de que yo esté equivocado: [%]
```

### 2.3 Checklist Value Trap
| Factor | Status | Comentario |
|--------|--------|------------|
| Industria en declive secular | SI/NO | |
| Disrupción tecnológica inminente | SI/NO | |
| Management destruyendo valor | SI/NO | |
| Balance deteriorándose (deuda subiendo, coverage bajando) | SI/NO | |
| Insider selling masivo (>5% en 12m) | SI/NO | |
| Dividend cut reciente o probable | SI/NO | |
| Pérdida market share >2pp en 3 años | SI/NO | |
| ROIC < WACC últimos 3 años | SI/NO | |
| FCF negativo >2 años consecutivos | SI/NO | |
| Goodwill >50% equity (riesgo impairment) | SI/NO | |

**REGLA:** Si >3 factores son SI → probable value trap → REJECT o Tier C (35% MoS mínimo)

### 2.4 Mi Ventaja Informacional
¿Por qué puedo ver algo que el mercado no ve?
- [ ] Horizonte temporal más largo (paciencia)
- [ ] Entiendo el negocio mejor (experiencia sectorial)
- [ ] El mercado sobre-reacciona a corto plazo (behavioral)
- [ ] Análisis cuantitativo que otros no hacen
- [ ] Información pública mal interpretada
- [ ] Otro: _________

**ADVERTENCIA:** Si no hay ventaja clara → probablemente el mercado tiene razón → cautela extrema.

---

## SECCIÓN 3: Catalizadores y Timeframe

### 3.1 Catalizadores Identificados
| Catalizador | Timeframe | Probabilidad | Impacto en precio |
|-------------|-----------|--------------|-------------------|
| | 0-6m / 6-12m / 1-2y / 2-5y | Alta/Media/Baja | +X% a +Y% |

### 3.2 Qué Tiene Que Pasar
Para que la thesis funcione, ¿qué específicamente debe ocurrir?
1. _________
2. _________
3. _________

### 3.3 Qué Me Haría Vender (kill conditions)
1. _________
2. _________
3. _________

---

## SECCIÓN 4: Conexión con Contexto Macro

### 4.1 Sensibilidad Macro
| Factor | Sensibilidad | Impacto actual |
|--------|-------------|----------------|
| Tasas de interés | Alta/Media/Baja/Ninguna | |
| Recesión | Alta/Media/Baja/Ninguna | |
| Inflación | Alta/Media/Baja/Ninguna | |
| USD strength | Alta/Media/Baja/Ninguna | |
| Commodity prices | Alta/Media/Baja/Ninguna | |

### 4.2 Fit con World View Actual
Leer `world/current_view.md` y responder:
- ¿El contexto macro es favorable, neutral, o adverso para este negocio?
- ¿Hay megatendencias que ayudan o perjudican?
- ¿El ciclo económico actual es apropiado para este tipo de empresa?

---

## OUTPUT REQUERIDO
Este framework debe producir una sección "BUSINESS UNDERSTANDING" en la thesis con:
1. Resumen del modelo de negocio (3-5 líneas)
2. Unit economics (CAC, LTV, LTV/CAC)
3. Estructura de márgenes y tendencia
4. Por qué está barata + mi contra-tesis
5. Checklist value trap completado
6. Catalizadores con timeframe
7. Fit con contexto macro

**REGLA DURA:** Si no puedo completar este framework → NO PUEDO VALORAR → NO PUEDO COMPRAR.
