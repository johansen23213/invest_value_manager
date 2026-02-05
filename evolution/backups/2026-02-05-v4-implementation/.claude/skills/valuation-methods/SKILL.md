---
name: valuation-methods
description: "Framework v3.0 - Métodos de valoración por Quality Tier y tipo de empresa. Owner Earnings Yield para Compounders."
user-invocable: false
disable-model-invocation: false
---

# Valuation Methods v3.0

## Principio Fundamental

**El método de valoración depende del Quality Tier Y del tipo de empresa.**

```
Tier A (QS ≥75): Owner Earnings Yield + Reverse DCF
Tier B (QS 55-74): DCF + EV/EBIT o método apropiado al tipo
Tier C (QS 35-54): Conservative multiples + Liquidation floor
```

## REGLA: Mínimo 2 métodos por análisis

Si los métodos divergen >30% → investigar antes de decidir.

---

## MÉTODOS POR QUALITY TIER

### TIER A: Quality Compounders (QS ≥75)

#### Método Primario (60%): Owner Earnings Yield

```
Owner Earnings (OE) = FCF - Maintenance Capex
Maintenance Capex ≈ Depreciation × 1.1

Owner Earnings Yield = OE / Market Cap

Interpretación:
┌────────────┬─────────────────────────────────┐
│ OE Yield   │ Valoración                      │
├────────────┼─────────────────────────────────┤
│ > 5%       │ Muy atractivo (raro)            │
│ 4-5%       │ Atractivo                       │
│ 3-4%       │ Fair si growth >10%             │
│ < 3%       │ Caro (incluso para compounder)  │
└────────────┴─────────────────────────────────┘

REGLA: OE Yield + Expected Growth > 12% → Comprar
       OE Yield + Expected Growth < 10% → Esperar
```

**Ejemplo GOOGL:**
```
FCF = $70B
Depreciation = $15B
Maintenance Capex ≈ $16.5B
Owner Earnings = $70B - $16.5B + $15B = $68.5B
Market Cap = $2.2T
OE Yield = 3.1%
Expected Growth = 12%
OE Yield + Growth = 15.1% → COMPRAR si MoS OK
```

#### Método Secundario (40%): Reverse DCF

```
Pregunta: ¿Qué crecimiento implica el precio actual?

Proceso:
1. Fijar WACC (típico 8-10%)
2. Fijar terminal growth (2-3%)
3. Usar DCF tool con varios growth rates
4. Encontrar growth que da FV = precio actual

python3 tools/dcf_calculator.py TICKER --growth 6 --scenarios
python3 tools/dcf_calculator.py TICKER --growth 8 --scenarios
python3 tools/dcf_calculator.py TICKER --growth 10 --scenarios
python3 tools/dcf_calculator.py TICKER --growth 12 --scenarios

Interpretar:
- Si Implied Growth > Mi estimación → CARO
- Si Implied Growth < Mi estimación → BARATO
```

---

### TIER B: Quality Value (QS 55-74)

#### Matriz por Tipo de Empresa

| Tipo | Método 1 (60%) | Método 2 (40%) |
|------|----------------|----------------|
| **Stable/Defensive** | DCF con scenarios | EV/EBIT normalizado |
| **Cyclical** | EV/EBIT mid-cycle | P/B vs ROE histórico |
| **Financial** | P/B vs ROE | DDM |
| **Asset-Heavy/REIT** | NAV | DDM |
| **Dividend Stock** | DDM | DCF |

---

### TIER C: Special Situations (QS 35-54)

#### Enfoque Conservador

```
Método 1: Conservative Multiple (60%)
- Usar múltiplo inferior al sector
- EV/EBIT sector 10x → usar 7-8x
- Aplicar haircut por riesgo

Método 2: Downside Protection (40%)
- Liquidation value / Asset value
- ¿Qué vale si todo va mal?
- Este es tu floor
```

---

## DETALLE DE MÉTODOS

### 1. DCF (Discounted Cash Flow)

#### Cuándo usar
- Tier B empresas con FCF predecible
- NO usar solo para cíclicas en pico/valle
- NO confiar ciegamente (sanity check otros métodos)

#### Proceso
```bash
python3 tools/dcf_calculator.py TICKER --scenarios
python3 tools/dcf_calculator.py TICKER --growth X --wacc Y --terminal Z
```

#### Parámetros
| Parámetro | Fuente | Rango típico |
|-----------|--------|--------------|
| Growth | projection-framework | 2-15% |
| WACC | Rf + Beta*ERP + spread | 8-12% |
| Terminal | ≤GDP | 2-3% |
| Years | 5-10 | 5 standard |

---

### 2. EV/EBIT Normalizado

#### Cuándo usar
- Empresas cíclicas
- Cuando earnings actuales no son representativos
- Comparación con peers

#### Proceso
```
1. Calcular EBIT normalizado (promedio 5-7 años, ajustar por ciclo)
2. Determinar múltiplo:
   - Sector median
   - Histórico empresa
   - Ajustar por calidad

3. EV = EBIT norm × Múltiplo
4. Equity = EV - Net Debt
5. FV = Equity / Shares
```

#### Múltiplos por Sector
| Sector | EV/EBIT Rango | Notes |
|--------|---------------|-------|
| Utilities | 10-14x | Regulados |
| Consumer Staples | 12-16x | Defensivos |
| Industrials | 8-12x | Cíclicos |
| Tech (mature) | 12-18x | Depende growth |
| Energy | 5-8x | Commodity |
| Retail | 6-10x | Competitivo |
| Pharma | 10-14x | Pipeline risk |

#### Ajustes al Múltiplo
```
Base (sector median): Xx
+ Superior ROIC: +1-2x
+ Wide moat: +1-2x
+ Above-avg growth: +1-2x
- Below-avg growth: -1-2x
- High leverage: -1-2x
- Governance: -1-2x
= Final: Xx
```

---

### 3. P/B vs ROE (Financials)

#### Cuándo usar
- Banks, insurers, asset managers
- Empresas donde book value es significativo

#### Framework
```
P/B Justified = (ROE - g) / (Ke - g)

Ejemplo:
ROE = 12%, g = 3%, Ke = 10%
P/B = (12% - 3%) / (10% - 3%) = 1.29x

Si trading a P/B < P/B Justified → Undervalued
```

#### Tabla Referencia
| ROE | P/B Justo (Ke=10%, g=3%) |
|-----|--------------------------|
| 8% | 0.7x |
| 10% | 1.0x |
| 12% | 1.3x |
| 15% | 1.7x |
| 18% | 2.1x |

---

### 4. NAV (Net Asset Value)

#### Cuándo usar
- REITs
- Asset-heavy businesses
- Holdings

#### Proceso
```
1. Listar activos principales
2. Valorar cada uno a fair market value
   - Real estate: cap rate
   - Inversiones: market price
   - Otros: replacement cost
3. Sumar activos
4. Restar liabilities
5. NAV = Assets - Liabilities
6. NAV/share = NAV / Shares

Premium/Discount = (Price - NAV) / NAV
```

#### Interpretación
- Discount >20%: Potencial value
- Pero verificar: ¿por qué el descuento?

---

### 5. DDM (Dividend Discount Model)

#### Cuándo usar
- Dividend aristocrats (10+ años)
- Utilities, REITs, financials maduros

#### Gordon Growth Model
```
FV = D1 / (Ke - g)

D1 = D0 × (1 + g)
g = ROE × (1 - Payout)

Ejemplo:
D0 = $2, ROE = 15%, Payout = 60%
g = 15% × 40% = 6%
D1 = $2 × 1.06 = $2.12
Ke = 10%
FV = $2.12 / (10% - 6%) = $53
```

---

### 6. Sum-of-Parts (SOTP)

#### Cuándo usar
- Conglomerados
- Turnarounds donde partes valen más separadas

#### Proceso
```
1. Identificar segmentos
2. Valorar cada uno con método apropiado
3. Sumar valores
4. Restar: overhead, net debt
5. SOTP = Suma - overhead - debt
```

#### Conglomerate Discount
- Típico: 10-20%
- Si >20%: activista target potencial

---

## RECONCILIACIÓN DE MÉTODOS

### Template Obligatorio

```
| Método | Fair Value | Peso | Weighted |
|--------|-----------|------|----------|
| [M1] | €___ | 60% | €___ |
| [M2] | €___ | 40% | €___ |
| **Weighted Avg** | | 100% | **€___** |

Precio actual: €___
MoS vs Weighted: ___%
MoS vs Bear Case: ___%

Divergencia métodos: ___%
Si >30%: Razón: [explicar]
```

### Peso por Fiabilidad

El peso depende de qué método es más apropiado:

| Situación | Método 1 peso | Método 2 peso |
|-----------|---------------|---------------|
| Compounder claro | OEY 60% | Reverse DCF 40% |
| Stable con FCF | DCF 60% | EV/EBIT 40% |
| Cíclica | EV/EBIT 60% | P/B 40% |
| Financiera | P/B 60% | DDM 40% |
| REIT | NAV 50% | DDM 50% |

---

## QUICK REFERENCE

```
Tier A (QS ≥75):
  → Owner Earnings Yield + Reverse DCF
  → OEY + Growth > 12% = COMPRAR

Tier B (QS 55-74):
  → Método apropiado al tipo + secundario
  → MoS 20-25% vs weighted FV

Tier C (QS 35-54):
  → Conservative multiple + Liquidation floor
  → MoS 30-40% MÍNIMO
```

---

## REGLAS DURAS

1. **NUNCA solo 1 método**
2. **Peso según fiabilidad para el tipo**
3. **Si divergen >30%: investigar**
4. **DCF es sensible: no confiar ciegamente**
5. **Para Tier A: OEY > DCF como primario**
6. **SIEMPRE calcular MoS vs Bear Case también**
