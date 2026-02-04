---
name: investment-rules
description: "Framework v3.0 - Quality Score cuantificable, MoS variable por tier, reglas de compra/venta, sizing dinámico"
user-invocable: false
disable-model-invocation: false
---

# Investment Rules - Framework v3.0

## CAMBIO FUNDAMENTAL vs v2.0

```
v2.0: "Compra barato" → Tiers por tipo de empresa
v3.0: "Compra calidad" → Tiers por Quality Score cuantificable
```

---

## PARTE 1: QUALITY SCORE (0-100)

### Principio: Si no se puede medir, no se puede gestionar

**TODOS los criterios son cuantificables. Usar `tools/quality_scorer.py` para cálculo.**

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
| **Revenue CAGR 5yr** | (Rev_now/Rev_5yr)^0.2 - 1 | >15%: 10, >10%: 8, >5%: 5, >0%: 2, <0%: 0 |
| **EPS CAGR 5yr** | (EPS_now/EPS_5yr)^0.2 - 1 | >15%: 10, >10%: 8, >5%: 5, >0%: 2, <0%: 0 |
| **Gross Margin Trend** | GM_now vs GM_3yr_avg | Expanding >1pp: 5, Stable: 3, Declining: 0 |

### 1.3 MOAT EVIDENCE (25 puntos)

| Métrica | Cálculo | Puntos |
|---------|---------|--------|
| **Gross Margin Premium** | GM vs sector median | >10pp: 10, >5pp: 7, ±5pp: 4, <-5pp: 0 |
| **Market Position** | Rank en mercado | #1-2: 8, #3-5: 5, #6-10: 2, >10: 0 |
| **ROIC Persistence** | Años ROIC>WACC en 10yr | 10/10: 7, 8-9: 5, 6-7: 3, <6: 0 |

### 1.4 CAPITAL ALLOCATION (10 puntos)

| Métrica | Cálculo | Puntos |
|---------|---------|--------|
| **Shareholder Returns** | Años consecutivos | 10+yr: 5, 5-9yr: 3, 1-4yr: 1, 0/cut: 0 |
| **Insider Ownership** | % insiders | >5%: 5, >2%: 3, >0.5%: 1, <0.5%: 0 |

---

## PARTE 2: QUALITY TIERS

| Tier | Quality Score | MoS Base | Descripción | Max Position |
|------|--------------|----------|-------------|--------------|
| **A** | 75-100 | 10-15% | Elite Compounders | 7% |
| **B** | 55-74 | 20-25% | Quality Value | 6% |
| **C** | 35-54 | 30-40% | Special Situations | 5% |
| **D** | <35 | N/A | **NO COMPRAR** | 0% |

### Ajustes al MoS Base

```
MoS Final = MoS Base + Ajustes

Ajustes (acumulables, max +15%):
+ Beta > 1.3: +5%
+ Sector cíclico: +5%
+ EM exposure >30%: +5%
+ Regulatory risk alto: +5%
+ Customer concentration >20%: +3%
```

---

## PARTE 3: CATEGORÍAS DE INVERSIÓN

### 3.1 Quality Compounders (20-40% portfolio)
- Quality Score ≥75 (Tier A)
- Hold 5+ años
- Target: 3-5 posiciones
- Ejemplos: GOOGL, META, V, MA, MSFT

### 3.2 Value with Quality (40-60% portfolio)
- Quality Score 55-74 (Tier B)
- Hold 2-5 años
- Target: 8-12 posiciones
- Ejemplos: ALL, DTE.DE, SAN.PA

### 3.3 Special Situations (10-25% portfolio)
- Quality Score 35-54 (Tier C) + catalyst claro
- Hold hasta catalyst (6-24 meses)
- Target: 2-5 posiciones
- Ejemplos: Turnarounds, spin-offs

---

## PARTE 4: REGLAS DE COMPRA (8 GATES)

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
[ ] Value trap checklist: ___/10 (si >3 → Tier C mínimo)
```

### Gate 3: Proyección Fundamentada
```
[ ] Revenue growth derivado (TAM/share/pricing): ___%
[ ] WACC calculado (Rf + Beta*ERP): ___%
[ ] Terminal growth justificado: ≤3%
[ ] Escenarios Bear/Base/Bull
```

### Gate 4: Valoración Multi-Método
```
[ ] Método 1 apropiado al tipo: [___] → FV €___
[ ] Método 2: [___] → FV €___
[ ] Si divergen >30%: explicación
```

### Gate 5: Margen de Seguridad
```
[ ] MoS vs Expected Value: ___%
[ ] MoS vs Base Case: ___%
[ ] ¿Cumple MoS del Tier?: [SI/NO]
```

### Gate 6: Contexto Macro
```
[ ] World view revisado (fecha: ___)
[ ] Sector view existe y revisado
[ ] Fit con ciclo económico
```

### Gate 7: Portfolio Fit
```
[ ] Position post-compra: ___% (max per tier)
[ ] Sector post-compra: ___% (max 25%)
[ ] Geografía post-compra: ___% (max 35%)
[ ] Cash post-compra: ___% (min 5%)
[ ] Total posiciones: ___ (max 20)
```

### Gate 8: Autocrítica
```
[ ] Asunciones no validadas listadas
[ ] Sesgos reconocidos
[ ] Kill conditions definidas
[ ] Qué me haría cambiar de opinión
```

**REGLA:** Si CUALQUIER gate falla → NO COMPRAR

---

## PARTE 5: REGLAS DE VENTA

### Por Valoración (escalonado)
| Trigger | Acción |
|---------|--------|
| Precio = 80% FV Base | Vender 25% |
| Precio = FV Base | Vender 50% (total 75%) |
| Precio = FV Bull | Vender resto |

### Por Thesis Invalidada (INMEDIATO)
- Quality Score cae a Tier D (<35)
- Kill conditions cumplidas
- ROIC < WACC 2+ años
- Dividend cut (para dividend stocks)
- Management fraud

### Por Quality Decay
- Si QS baja de Tier A a B: reevaluar sizing
- Si QS baja de Tier B a C: definir catalyst o vender
- Si QS baja a Tier D: vender en próxima ventana

### NO Vender Por
- Caída de precio sin cambio en fundamentales
- Miedo general del mercado
- Analyst downgrade sin nueva información

---

## PARTE 6: SIZING DINÁMICO

### Base Sizing por Tier
| Tier | Base Size | Max Size |
|------|-----------|----------|
| A | 4-5% | 7% |
| B | 3-4% | 6% |
| C | 2-3% | 5% |

### Ajustes
```
+ MoS > requisito +10pp: +1%
+ Wide moat confirmado: +1%
- Alta correlación (>0.7): -1%
- Late cycle + cíclica: -1%
- Small cap (<€2B): -0.5%
```

### Límites Absolutos
- Mínimo: 2% (below = not worth tracking)
- Máximo: 7% (nunca más, incluso alta convicción)
- Rebalanceo trigger: >10% de portfolio

---

## PARTE 7: SECTOR ALLOCATION

### Targets (flexibles, no hard floors)

| Sector | Mín | Target | Máx |
|--------|-----|--------|-----|
| Technology | 5% | 15-25% | 35% |
| Healthcare | 5% | 10-15% | 20% |
| Financials | 5% | 10-15% | 20% |
| Consumer | 5% | 10-15% | 20% |
| Industrials | 0% | 5-10% | 15% |
| Energy | 0% | 5-10% | 12% |
| Utilities | 0% | 5-8% | 12% |
| Real Estate | 0% | 5-10% | 12% |
| Telecom | 0% | 3-8% | 10% |

### Reglas de Allocation
1. Si sector <mínimo por >60 días: priorizar búsqueda
2. Si no hay ideas con MoS suficiente: aceptable estar bajo target
3. Revisión trimestral obligatoria
4. ETFs permitidos como placeholder (max 15% total)

---

## PARTE 8: ETFs PERMITIDOS (placeholder)

Para evitar cash drag mientras se buscan ideas individuales:

| ETF | Uso | Max |
|-----|-----|-----|
| QQQ/QQQM | Tech placeholder | 10% |
| VIG | Quality dividend | 10% |
| SPY/VOO | Market exposure | 10% |

**Total max ETFs: 15%**

Reglas:
- Vender cuando aparezca idea individual mejor
- NO contar para Quality Score del portfolio
- Revisar mensualmente si hay ideas para reemplazar

---

## PARTE 9: GROSS MARGIN REFERENCE BY SECTOR

| Sector | Median | Top Quartile |
|--------|--------|--------------|
| Software | 72% | >80% |
| Pharma | 67% | >75% |
| Consumer Staples | 38% | >45% |
| Industrials | 28% | >35% |
| Retail | 28% | >35% |
| Utilities | 40% | >50% |
| Telecom | 45% | >55% |
| Energy | 35% | >50% |

---

## PARTE 10: NUNCA (Inmutable)

1. Comprar Tier D (QS <35)
2. Operar sin thesis documentada
3. Usar apalancamiento
4. Saltarse Investment Committee
5. Comprar value trap (>3 factores)
6. Ignorar kill conditions
7. Usar defaults sin derivación
8. Comprar sin entender por qué está barata
9. Exceder 7% en una posición
10. Exceder 25% en un sector

---

## QUICK REFERENCE: Quality Score → Action

```
QS 75-100 (A): BUY con MoS 10-15%, hold forever
QS 55-74 (B):  BUY con MoS 20-25%, hold 2-5yr
QS 35-54 (C):  BUY SOLO con catalyst + MoS 30-40%
QS <35 (D):    DO NOT BUY EVER
```
