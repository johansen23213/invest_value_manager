# Framework v3.0 - Diseño Final Mejorado

> **Fecha:** 2026-02-05
> **Status:** DISEÑO FINAL PARA IMPLEMENTACIÓN
> **Mejora sobre:** docs/evolution_proposal_fw_v3.0.md

---

## RESUMEN DE MEJORAS vs PROPUESTA ORIGINAL

| Aspecto | Propuesta Original | Diseño Final |
|---------|-------------------|--------------|
| Quality Score | 16 subrubros subjetivos | 12 métricas cuantificables |
| Umbrales | 80/60/40 | 75/55/35 (más realistas) |
| Implementación | Manual | 80% automatizable con tool |
| Sector allocation | Hard floor 10% tech | Flexible con target |
| ETFs | No mencionados | Permitidos hasta 15% |
| DCF | "Sanity check only" | Método secundario válido |

---

## PARTE 1: QUALITY SCORE CUANTIFICABLE (0-100)

### Principio: Si no se puede medir, no se puede gestionar

**TODOS los criterios son cuantificables con datos de yfinance o cálculo simple.**

```
QUALITY SCORE = Financial (40) + Growth (25) + Moat Evidence (25) + Capital Allocation (10)
```

### 1.1 FINANCIAL QUALITY (40 puntos)

| Métrica | Cálculo | Puntos |
|---------|---------|--------|
| **ROIC Spread** | ROIC - WACC | >15pp: 15, >10pp: 12, >5pp: 8, >0pp: 4, <0pp: 0 |
| **FCF Margin** | FCF / Revenue | >20%: 10, >15%: 8, >10%: 5, >5%: 2, <5%: 0 |
| **Leverage** | Net Debt / EBITDA | <1x: 10, <2x: 8, <3x: 5, <4x: 2, >4x: 0 |
| **FCF Consistency** | Años FCF+ en últimos 5 | 5/5: 5, 4/5: 4, 3/5: 2, <3/5: 0 |

**Fuentes de datos:**
- ROIC: `returnOnCapital` de yfinance o calcular (NOPAT/Invested Capital)
- WACC: Calcular con Rf + Beta*ERP (fórmula estándar)
- FCF: `freeCashFlow` de yfinance
- Revenue: `totalRevenue` de yfinance
- Net Debt: `totalDebt` - `cash` de yfinance
- EBITDA: `ebitda` de yfinance

### 1.2 GROWTH QUALITY (25 puntos)

| Métrica | Cálculo | Puntos |
|---------|---------|--------|
| **Revenue CAGR 5yr** | (Rev_now/Rev_5yr)^0.2 - 1 | >15%: 10, >10%: 8, >5%: 5, >0%: 2, <0%: 0 |
| **EPS CAGR 5yr** | (EPS_now/EPS_5yr)^0.2 - 1 | >15%: 10, >10%: 8, >5%: 5, >0%: 2, <0%: 0 |
| **Gross Margin Trend** | GM_now vs GM_3yr_avg | Expanding >1pp: 5, Stable ±1pp: 3, Declining: 0 |

**Fuentes de datos:**
- Revenue/EPS histórico: yfinance `financials` con fechas
- Gross Margin: `grossMargins` de yfinance

### 1.3 MOAT EVIDENCE (25 puntos)

| Métrica | Cálculo | Puntos |
|---------|---------|--------|
| **Gross Margin Premium** | GM empresa vs GM sector median | >10pp: 10, >5pp: 7, ±5pp: 4, <-5pp: 0 |
| **Market Position** | Rank en su mercado | #1-2: 8, #3-5: 5, #6-10: 2, >10: 0 |
| **ROIC Persistence** | Años ROIC>WACC en últimos 10 | 10/10: 7, 8-9/10: 5, 6-7/10: 3, <6/10: 0 |

**Notas:**
- Gross Margin sector: usar tabla de referencia por industria
- Market Position: dato cualitativo pero verificable (market share reports)
- ROIC Persistence: histórico calculable

### 1.4 CAPITAL ALLOCATION (10 puntos)

| Métrica | Cálculo | Puntos |
|---------|---------|--------|
| **Shareholder Returns** | Años consecutivos div/buyback | 10+yr: 5, 5-9yr: 3, 1-4yr: 1, 0 o cut: 0 |
| **Insider Ownership** | % owned by insiders | >5%: 5, >2%: 3, >0.5%: 1, <0.5%: 0 |

**Fuentes de datos:**
- Dividend history: `dividendYield` + research
- Insider ownership: `heldPercentInsiders` de yfinance

---

## PARTE 2: QUALITY TIERS Y MoS VARIABLE

### 2.1 Definición de Tiers

| Tier | Quality Score | MoS Requerido | Descripción | Holding Period |
|------|--------------|---------------|-------------|----------------|
| **A** | 75-100 | 10-15% | Elite Compounders | 5+ años |
| **B** | 55-74 | 20-25% | Quality Value | 2-5 años |
| **C** | 35-54 | 30-40% | Turnaround/Cyclical | 1-2 años |
| **D** | <35 | N/A | **NO COMPRAR** | - |

### 2.2 Por qué estos umbrales

Los umbrales son más bajos que la propuesta original (80/60/40) porque:
1. Con criterios cuantificables estrictos, menos empresas alcanzan scores altos
2. Incluso GOOGL/META probablemente scoren 70-85, no 90+
3. El mercado es eficiente; calidad excepcional es rara

### 2.3 MoS Ajustado dentro del Tier

```
MoS Final = MoS Base del Tier + Ajustes

Ajustes (acumulables):
- Beta > 1.3: +5% MoS
- Sector cíclico (energy, materials, industrials): +5% MoS
- Emerging market exposure >30%: +5% MoS
- Regulatory risk alto: +5% MoS
- Concentración cliente >20%: +3% MoS
```

---

## PARTE 3: MÉTODOS DE VALORACIÓN POR TIPO

### 3.1 Matriz de Métodos

| Tipo de Empresa | Quality Tier | Método Primario (60%) | Método Secundario (40%) |
|-----------------|--------------|----------------------|------------------------|
| **Compounder** | A | Owner Earnings Yield | Reverse DCF |
| **Stable Growth** | A-B | DCF con scenarios | EV/EBIT normalizado |
| **Cyclical** | B-C | EV/EBIT mid-cycle | P/B vs ROE histórico |
| **Financial** | Any | P/B vs ROE | DDM |
| **REIT** | Any | P/FFO + NAV discount | DDM |
| **Turnaround** | C | Sum-of-Parts | Liquidation value |

### 3.2 Owner Earnings Yield (para Tier A)

```
Owner Earnings = FCF - Estimated Maintenance Capex
Maintenance Capex ≈ Depreciation × 1.1 (heurística conservadora)

Owner Earnings Yield = Owner Earnings / Market Cap

Regla: OE Yield > 4% + Expected Growth → Atractivo
       OE Yield < 3% → Caro incluso para compounder
```

### 3.3 Reverse DCF (para validar)

```
Pregunta: "¿Qué crecimiento está implícito en el precio actual?"

Proceso:
1. Usar DCF tool con múltiples growth rates
2. Encontrar el growth rate que da FV = precio actual
3. Comparar con mi proyección de growth

Si Implied Growth > Mi Proyección → Caro
Si Implied Growth < Mi Proyección → Atractivo
```

### 3.4 DCF sigue siendo válido como método secundario

DCF NO se elimina. Se usa como:
- Método secundario para empresas estables
- Herramienta de escenarios Bear/Base/Bull
- Sanity check para otros métodos

---

## PARTE 4: CATEGORÍAS DE INVERSIÓN

### 4.1 Tres Categorías

```
PORTFOLIO v3.0:

┌─────────────────────────────────────────────────────────────────┐
│ QUALITY COMPOUNDERS (20-40% del portfolio)                      │
│ - Quality Score ≥75 (Tier A)                                    │
│ - MoS 10-15%                                                    │
│ - Hold 5+ años salvo thesis break                               │
│ - Target: 3-5 posiciones                                        │
├─────────────────────────────────────────────────────────────────┤
│ VALUE WITH QUALITY (40-60% del portfolio)                       │
│ - Quality Score 55-74 (Tier B)                                  │
│ - MoS 20-25%                                                    │
│ - Hold 2-5 años hasta fair value                                │
│ - Target: 8-12 posiciones                                       │
├─────────────────────────────────────────────────────────────────┤
│ SPECIAL SITUATIONS (10-25% del portfolio)                       │
│ - Quality Score 35-54 (Tier C) CON catalyst claro               │
│ - MoS 30-40%                                                    │
│ - Hold hasta catalyst (6-24 meses)                              │
│ - Target: 2-5 posiciones                                        │
└─────────────────────────────────────────────────────────────────┘
```

### 4.2 Regla de Concentración por Categoría

- Max 1 posición Compounder >7% (porque son de mayor convicción)
- Max posición Value: 6%
- Max posición Special Situation: 5%

---

## PARTE 5: SECTOR ALLOCATION FLEXIBLE

### 5.1 Targets (no hard floors)

| Sector | Mínimo | Target | Máximo | Rationale |
|--------|--------|--------|--------|-----------|
| **Technology** | 5% | 15-25% | 35% | Compounders viven aquí |
| Healthcare | 5% | 10-15% | 20% | Defensive + innovation |
| Financials | 5% | 10-15% | 20% | Incluye insurance |
| Consumer | 5% | 10-15% | 20% | Staples + discretionary |
| Industrials | 0% | 5-10% | 15% | Cyclical exposure |
| Energy | 0% | 5-10% | 12% | Hedge geopolítico |
| Utilities | 0% | 5-8% | 12% | Yield, defensive |
| Real Estate | 0% | 5-10% | 12% | Inflation hedge |
| Telecom | 0% | 3-8% | 10% | Yield, defensive |
| Materials | 0% | 0-5% | 8% | Cyclical, selectivo |

### 5.2 Flexibilidad vs Rigidez

**IMPORTANTE:** Estos son TARGETS, no constraints duros.

Reglas:
1. Si tech <5% por >60 días, priorizar búsqueda de ideas tech
2. Si ninguna idea tech tiene MoS suficiente, es ACEPTABLE estar <target
3. Revisar allocation trimestralmente
4. Documentar razón si significativamente fuera de target

### 5.3 ETFs como Placeholder (PERMITIDO)

Para evitar cash drag mientras se buscan ideas individuales:

| ETF | Uso | Max Allocation |
|-----|-----|----------------|
| QQQ/QQQM | Tech placeholder | 10% |
| VIG | Quality dividend placeholder | 10% |
| SPY/VOO | Market exposure temporal | 10% |

**Reglas ETFs:**
- Max 15% total en ETFs
- Vender cuando se encuentre idea individual de mayor convicción
- NO contar para Quality Score del portfolio

---

## PARTE 6: RESOLUCIÓN DE PREGUNTAS ABIERTAS

### 6.1 ¿Qué hacer con posiciones actuales QS < 55?

```
PROTOCOLO TRANSICIÓN:

1. Calcular QS para las 18 posiciones
2. Si QS ≥ 55: Mantener, actualizar thesis con QS
3. Si QS 35-54:
   - Reclasificar como Special Situation
   - Definir catalyst y timeline claro
   - Si no hay catalyst en 6 meses: considerar venta
4. Si QS < 35:
   - Evaluar caso por caso
   - Si cerca de FV: VENDER
   - Si muy por debajo de FV: HOLD hasta recuperación, luego VENDER
   - NO añadir más capital
```

### 6.2 ¿Cómo entrar a Quality Compounders?

```
OPCIONES (en orden de preferencia):

1. CORRECCIÓN DE MERCADO
   - Mantener lista de compounders con entry targets
   - Estar preparado para comprar en correcciones (-10-20%)
   - Ejemplo: GOOGL target $155-165 (actual $180)

2. COMPRA ESCALONADA
   - 50% de la posición target ahora si MoS ~10%
   - 50% si cae otro 10%
   - Solo para QS ≥ 80

3. POSITION SIZING REDUCIDO
   - Si MoS es 8-10% (insuficiente para full position)
   - Comprar 2% en lugar de 4%
   - Añadir si mejora el MoS

4. ETF PLACEHOLDER
   - Si no hay oportunidades: QQQ hasta 10%
   - Vender cuando aparezca idea individual
```

### 6.3 ¿Cómo calcular Owner Earnings sin maintenance capex explícito?

```python
# Heurística conservadora
maintenance_capex = depreciation * 1.1
owner_earnings = fcf - maintenance_capex + depreciation
# Simplificado: owner_earnings ≈ fcf * 0.9 (haircut 10%)
```

### 6.4 ¿Cómo hacer Reverse DCF?

```python
# Pseudo-código
for growth_rate in [2%, 4%, 6%, 8%, 10%, 12%, 15%]:
    fv = dcf_calculator(ticker, growth=growth_rate)
    if abs(fv - current_price) < threshold:
        implied_growth = growth_rate
        break

# Interpretar
if implied_growth < my_projection:
    print("Atractivo - mercado pesimista")
else:
    print("Caro - mercado optimista")
```

---

## PARTE 7: QUALITY SCORE RÁPIDO (para screening)

### 7.1 Quick Score (5 métricas clave)

Para screening inicial, antes de análisis completo:

| Métrica | Threshold | Pass/Fail |
|---------|-----------|-----------|
| ROIC > WACC | >5pp | PASS si cumple |
| FCF Positive | 3+ de últimos 5 años | PASS si cumple |
| Debt/EBITDA | <4x | PASS si cumple |
| Revenue Growth | >0% CAGR 5yr | PASS si cumple |
| Gross Margin | >Sector median | PASS si cumple |

**Regla:** Si 4/5 PASS → Proceder a análisis completo
Si <4/5 PASS → Descartar o flag para revisión especial

---

## PARTE 8: GROSS MARGIN POR SECTOR (Referencia)

Para calcular Moat Evidence (Gross Margin Premium):

| Sector | Median GM | Top Quartile | Notes |
|--------|-----------|--------------|-------|
| Software | 70-75% | >80% | SaaS típico |
| Pharma | 65-70% | >75% | Patented drugs |
| Consumer Staples | 35-40% | >45% | Brands matter |
| Industrials | 25-30% | >35% | Scale matters |
| Retail | 25-30% | >35% | Private label |
| Financials | N/A | N/A | Use NIM instead |
| Utilities | 35-45% | >50% | Regulated |
| Telecom | 40-50% | >55% | Infrastructure |
| Energy | 30-40% | >50% | Integrated |
| REITs | 60-70% | >75% | Property type |

---

## PARTE 9: CHECKLIST DE IMPLEMENTACIÓN

### Fase 1: Core System
- [ ] CLAUDE.md → v3.0
- [ ] .claude/skills/investment-rules/SKILL.md → REESCRIBIR
- [ ] .claude/skills/business-analysis-framework/SKILL.md → Añadir QS
- [ ] .claude/skills/valuation-methods/SKILL.md → Reorganizar
- [ ] CREAR .claude/skills/quality-compounders/SKILL.md

### Fase 2: Agents y Tools
- [ ] fundamental-analyst.md → Añadir QS fase
- [ ] investment-committee.md → Añadir QS gate
- [ ] sector-screener.md → Filtros quality
- [ ] CREAR tools/quality_scorer.py
- [ ] Modificar tools/dynamic_screener.py

### Fase 3: Portfolio Re-eval
- [ ] QS para 18 posiciones
- [ ] Asignar tiers
- [ ] Identificar acciones

### Fase 4: State Update
- [ ] state/system.yaml → version 3.0
- [ ] portfolio/current.yaml → añadir campos

### Fase 5: Verificación
- [ ] Consistencia total
- [ ] No conflictos v2/v3
- [ ] Test mental de flujo

---

## PARTE 10: EJEMPLO APLICADO

### GOOGL Quality Score

```
FINANCIAL QUALITY (40 pts):
- ROIC Spread: ~25% ROIC - 9% WACC = 16pp → 15 pts
- FCF Margin: ~25% → 10 pts
- Leverage: Net cash → 10 pts
- FCF Consistency: 5/5 → 5 pts
SUBTOTAL: 40/40

GROWTH QUALITY (25 pts):
- Revenue CAGR 5yr: ~12% → 8 pts
- EPS CAGR 5yr: ~15% → 10 pts
- Gross Margin Trend: Stable → 3 pts
SUBTOTAL: 21/25

MOAT EVIDENCE (25 pts):
- Gross Margin Premium: 55% vs 40% software = +15pp → 10 pts
- Market Position: #1 search, #2 cloud → 8 pts
- ROIC Persistence: 10/10 → 7 pts
SUBTOTAL: 25/25

CAPITAL ALLOCATION (10 pts):
- Shareholder Returns: Buybacks 5+ yr → 3 pts
- Insider Ownership: ~0.1% → 0 pts
SUBTOTAL: 3/10

TOTAL: 89/100 → TIER A
MoS Requerido: 10-12%
```

### IMB.L Quality Score (posición actual)

```
FINANCIAL QUALITY (40 pts):
- ROIC Spread: ~15% ROIC - 9% WACC = 6pp → 8 pts
- FCF Margin: ~15% → 8 pts
- Leverage: ~3x → 5 pts
- FCF Consistency: 5/5 → 5 pts
SUBTOTAL: 26/40

GROWTH QUALITY (25 pts):
- Revenue CAGR 5yr: ~-2% → 0 pts
- EPS CAGR 5yr: ~0% → 2 pts
- Gross Margin Trend: Stable → 3 pts
SUBTOTAL: 5/25

MOAT EVIDENCE (25 pts):
- Gross Margin Premium: 40% vs 38% staples = +2pp → 4 pts
- Market Position: #2 tobacco UK → 8 pts
- ROIC Persistence: 8/10 → 5 pts
SUBTOTAL: 17/25

CAPITAL ALLOCATION (10 pts):
- Shareholder Returns: 10+ yr div + buyback → 5 pts
- Insider Ownership: ~0.3% → 0 pts
SUBTOTAL: 5/10

TOTAL: 53/100 → TIER C (borderline)
Acción: Reclasificar como Special Situation, definir catalyst
```

---

**FIN DEL DISEÑO - LISTO PARA IMPLEMENTACIÓN**
