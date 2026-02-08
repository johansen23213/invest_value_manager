---
name: recommendation-context
description: "Template OBLIGATORIO para contextualizar cada recomendación de inversión con timing, noticias y movimiento de precio"
user-invocable: false
---

# Recommendation Context Framework

## Propósito
Asegurar que CADA recomendación de inversión incluye contexto suficiente para que el humano entienda el POR QUÉ AHORA.

---

## Cuándo Usar

**OBLIGATORIO para:**
- BUY de nueva posición
- ADD a posición existente
- SELL/TRIM de posición
- Activación de standing order

**NO necesario para:**
- Updates de monitoreo sin acción
- Health checks
- Reportes de estado

---

## Template de Recomendación Contextualizada

```markdown
## Recomendación: [BUY/ADD/SELL] [TICKER] [CANTIDAD] @ [PRECIO]

### 1. TIMING - ¿Por qué AHORA?

**Evento catalizador:**
[Qué pasó que creó esta oportunidad]

**Fecha del evento:**
[Cuándo ocurrió - hace X días]

**Incorporación en precio:**
[¿El mercado ya reaccionó? ¿Cuánto cayó/subió?]

---

### 2. NOTICIAS RECIENTES (últimos 7 días)

**Positivas:**
- [Noticia 1]
- [Noticia 2]

**Negativas:**
- [Noticia 1] → Por qué NO invalida thesis: [explicación]
- [Noticia 2] → Por qué NO invalida thesis: [explicación]

**Competidores:**
- [Noticia relevante de competidor si aplica]

---

### 3. MOVIMIENTO DE PRECIO

| Período | Precio | Cambio |
|---------|--------|--------|
| Actual | $XX | - |
| Hace 1 semana | $XX | X% |
| Hace 1 mes | $XX | X% |
| 52-week high | $XX | -X% |
| 52-week low | $XX | +X% |

**Causa del movimiento:**
[¿Por qué el precio está donde está?]

**Comparación vs mercado/sector:**
[¿Movimiento idiosincrático o general?]

---

### 4. SENTIMIENTO

**Analyst ratings:**
[X Buy / Y Hold / Z Sell]

**Cambios recientes:**
- [Upgrade/downgrade reciente si hay]

**Price targets:**
- Promedio: $XX
- Rango: $XX - $XX

---

### 5. THESIS EN CONTEXTO

**Quality Score:** XX/100 (Tier X)

**Fair Value:** $XX-XX

**MoS actual:** XX%

**MoS precedentes similares (de decisions_log.yaml):** [ticker, MoS aceptado, por qué]

**Catalizadores próximos:**
- [Catalizador 1] - [Fecha]
- [Catalizador 2] - [Fecha]

**Kill conditions:**
- [Kill condition 1]
- [Kill condition 2]

---

### 6. RESUMEN EJECUTIVO

[2-3 oraciones que respondan: ¿Por qué esta empresa, a este precio, en este momento?]

---

### Pre-Recommendation Checks
| Check | Status |
|-------|--------|
| Popularity Bias | ✅/❌ |
| News 48h | ✅/❌ |
| Timing Context | ✅/❌ |
| Constraints | ✅/❌ |
| Quality Score | ✅/❌ |
| Multi-Method | ✅/❌ |
| Why Cheap | ✅/❌ |
| Meta-Reflection | ✅/❌ |
| Sector View | ✅/❌ |
| Earnings Timing | ✅/❌ |
```

---

## Ejemplo Completo: NVO

```markdown
## Recomendación: BUY NVO 8 shares @ $48

### 1. TIMING - ¿Por qué AHORA?

**Evento catalizador:**
Novo Nordisk publicó guidance 2026 con ventas -5% a -13%, muy por debajo de
expectativas. CEO advirtió "it will get worse before it gets better".

**Fecha del evento:**
3-4 de Febrero 2026 (hace 1-2 días)

**Incorporación en precio:**
La acción cayó 18% en 2 días. El pánico YA OCURRIÓ. Compramos POST-caída,
no antes.

---

### 2. NOTICIAS RECIENTES (últimos 7 días)

**Positivas:**
- Wegovy pill alcanzó 170K pacientes en 4 semanas (mejor de esperado)
- CagriSema FDA filing aceptado

**Negativas:**
- Guidance 2026 -5% a -13% → Por qué NO invalida thesis: 2026 es año trough,
  no nueva normalidad. Wegovy pill y CagriSema son catalizadores 2H26.
- Zepbound tiene 59% de nuevas prescripciones → Por qué NO invalida thesis:
  GLP-1 TAM es $170B para 2033. Room for duopoly.

**Competidores:**
- Eli Lilly ganando share pero no reporta hasta Feb 6

---

### 3. MOVIMIENTO DE PRECIO

| Período | Precio | Cambio |
|---------|--------|--------|
| Actual | $48 | - |
| Hace 1 semana | $58 | -17% |
| Hace 1 mes | $52 | -8% |
| 52-week high | $100 | -52% |
| 52-week low | $44 | +9% |

**Causa del movimiento:**
Guidance shock + CEO warning = pánico vendedor

**Comparación vs mercado/sector:**
Movimiento 100% idiosincrático. S&P +0.5%, XLV (healthcare ETF) +0.2%.
NVO cayó sola.

---

### 4. SENTIMIENTO

**Analyst ratings:**
15 Buy / 5 Hold / 0 Sell

**Cambios recientes:**
- Jefferies: PT $85 → $65 (mantiene Buy)
- Goldman: PT $90 → $70 (mantiene Buy)

**Price targets:**
- Promedio: $72
- Rango: $55 - $95

---

### 5. THESIS EN CONTEXTO

**Quality Score:** 82/100 (Tier A)

**Fair Value:** DKK 491 (~$66)

**MoS actual:** 38%

**MoS precedentes Tier A (decisions_log):** ADBE 22%, MONY.L 36%, LULU 34%

**Catalizadores próximos:**
- CagriSema vs Zepbound head-to-head - Marzo 2026
- Wegovy pill ramp - Q1-Q2 2026

**Kill conditions:**
- CagriSema shows inferiority to Zepbound
- Market share <40%
- Gross margin <70%

---

### 6. RESUMEN EJECUTIVO

Novo Nordisk es un Quality Compounder (QS 82) que acaba de caer 18% por un
guidance shock que representa un año trough, no el nuevo normal. A $48, el
mercado valora la empresa como si el negocio de GLP-1 estuviera en declive
terminal, cuando la realidad es competencia temporal en un TAM de $170B.
Compramos POST-pánico con MoS de 38%, bien por encima de precedentes Tier A.

---

### Pre-Recommendation Checks
| Check | Status |
|-------|--------|
| Popularity Bias | ✅ From quality_compounders watchlist |
| News 48h | ✅ Guidance shock incorporated |
| Timing Context | ✅ Post-crash entry |
| Constraints | ✅ 4% position, US 33% |
| Quality Score | ✅ QS 82, Tier A |
| Multi-Method | ✅ OEY + Reverse DCF |
| Why Cheap | ✅ Guidance shock + competition fears |
| Meta-Reflection | ✅ Agent doubts about CagriSema noted |
| Sector View | ✅ pharma-healthcare.md exists |
| Earnings Timing | ✅ Just reported, no earnings soon |
```

---

## Reglas

1. **NUNCA presentar recomendación sin este contexto**
2. **Si no puedo completar alguna sección → investigar antes de recomendar**
3. **El humano debe poder entender el "por qué ahora" en 30 segundos**
4. **Noticias negativas SIEMPRE deben tener contra-argumento**
5. **Movimiento de precio SIEMPRE debe tener causa identificada**
