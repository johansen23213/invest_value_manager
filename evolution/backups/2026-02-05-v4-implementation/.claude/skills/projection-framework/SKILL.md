---
name: projection-framework
description: Bottom-up projection methodology - no defaults, logical derivation of growth rates and margins. MANDATORY before DCF.
user-invocable: false
disable-model-invocation: false
---

# Projection Framework Skill

## Propósito
NUNCA usar "5% growth" o "9% WACC" sin justificación. Este framework obliga a derivar proyecciones desde la lógica del negocio.

## PRINCIPIO CORE
```
Proyección = f(TAM, market share, pricing, márgenes, reinversión)
NO: "Usaré 5% growth porque es un número razonable"
SI: "El TAM crece 3%, la empresa gana 0.5pp de share anual, y tiene 2% pricing power = ~5.5% growth en revenue"
```

---

## SECCIÓN 1: Proyección de Ingresos

### 1.1 Top-Down: TAM Analysis
```
TAM (Total Addressable Market) = €___ billion
  → Fuente: [citar]
  → Geografía cubierta: [global/regional/local]

TAM Growth Rate = ___% anual
  → Drivers de crecimiento: [listar]
  → Drivers de contracción: [listar]
  → Mi estimación: ___% (conservador: TAM growth × 0.8)
```

### 1.2 Market Share Analysis
```
Market Share Actual = ___%
  → Fuente: [citar]
  → Ranking vs competidores: #___

Market Share Trend (5 años):
  Año -5: ___%
  Año -3: ___%
  Año -1: ___%
  Actual: ___%
  → Tendencia: [ganando / perdiendo / estable]

Proyección Market Share:
  Año +3: ___% (why?)
  Año +5: ___% (why?)
```

### 1.3 Pricing Power Analysis
```
Historial de pricing:
  → ¿Han subido precios? ¿Cuánto? ¿Con qué frecuencia?
  → ¿Perdieron clientes al subir precios?

Pricing power score:
  [ ] Fuerte: pueden subir precios >inflación sin perder clientes
  [ ] Moderado: pueden igualar inflación
  [ ] Débil: presión de precios, márgenes comprimiendo
  [ ] Negativo: comoditización, guerra de precios

Proyección pricing: ___% anual
```

### 1.4 Revenue Projection Formula
```
Revenue Growth = TAM Growth + ΔMarket Share + Pricing

Ejemplo:
  TAM Growth: +3%
  Market Share: +0.5pp/año
  Pricing: +1.5%
  = Revenue Growth: ~5%

MI PROYECCIÓN:
  Base case: ___% (años 1-5)
  Bear case: ___% (TAM stagnant, share loss)
  Bull case: ___% (TAM accelerates, share gains)
```

---

## SECCIÓN 2: Proyección de Márgenes

### 2.1 Gross Margin Projection
```
Gross Margin Actual: ___%
Gross Margin 5y Average: ___%
Gross Margin Trend: [expanding / compressing / stable]

Drivers:
  → Input costs: [tendencia]
  → Mix shift: [hacia productos higher/lower margin?]
  → Scale benefits: [más volumen = mejor pricing con suppliers?]
  → Competitive pressure: [competidores forzando precio?]

Proyección Gross Margin:
  Año +3: ___% (why?)
  Año +5: ___% (why?)
```

### 2.2 Operating Margin Projection
```
Operating Margin Actual: ___%
Operating Margin 5y Average: ___%

Estructura de costos:
  → Fixed costs: ___% of revenue (SG&A fijo, depreciation)
  → Variable costs: ___% of revenue (COGS variable, comisiones)

Operating Leverage:
  → Si revenue sube 10%, ¿cuánto sube operating income?
  → OL ratio = Δ Operating Income / Δ Revenue
  → OL > 1 = operating leverage positivo

Proyección Operating Margin:
  → Con revenue growth de X%, operating margin llega a Y% porque [explicar]
```

### 2.3 FCF Conversion
```
Net Income to FCF Bridge:
  + Depreciation & Amortization
  - Capex de mantenimiento
  - Capex de crecimiento
  ± Working capital changes
  = Free Cash Flow

FCF Conversion = FCF / Net Income = ___%

Histórico FCF Conversion:
  Año -5: ___%
  Año -3: ___%
  Año -1: ___%
  → Tendencia: [mejorando / empeorando / estable]

Proyección FCF Conversion: ___% (why?)
```

---

## SECCIÓN 3: Derivación de WACC

### 3.1 Cost of Equity (Ke)
```
Risk-Free Rate = ___% (10Y Treasury actual)
Equity Risk Premium = ___% (típico 4-6%)
Beta = ___ (fuente: Yahoo Finance / Bloomberg)
  → ¿Beta tiene sentido para este negocio?
  → Si es muy volátil por liquidez (no fundamentales), ajustar

Ke = Rf + Beta × ERP = ___%
```

### 3.2 Cost of Debt (Kd)
```
Interest Expense / Total Debt = ___% (cost of debt actual)
Tax Rate = ___%
Kd after-tax = Cost of Debt × (1 - Tax Rate) = ___%
```

### 3.3 Capital Structure
```
Market Cap = €___
Total Debt = €___
Enterprise Value = €___

Weight Equity (E/V) = ___%
Weight Debt (D/V) = ___%
```

### 3.4 WACC Calculation
```
WACC = (E/V × Ke) + (D/V × Kd after-tax)
WACC = (__% × __%) + (__% × __%)
WACC = ___%

Sanity check:
  → ¿WACC < 8%? Solo para utilities/defensivos ultra-estables
  → ¿WACC > 12%? Solo para high-risk/emerging markets
  → Ajustar si no tiene sentido para el negocio
```

---

## SECCIÓN 4: Terminal Value Assumptions

### 4.1 Terminal Growth Rate
```
¿Puede esta empresa crecer forever a X%?

Criterios:
  → Terminal growth ≤ GDP growth (2-3%)
  → Si industria en declive: terminal growth puede ser negativo o 0%
  → Si industria creciendo >GDP: máximo 3% terminal

Mi terminal growth: ___% because [explicar]
```

### 4.2 Terminal Multiple (método alternativo)
```
EV/EBITDA terminal = ___x
  → Basado en: comparables maduros del sector
  → Típico rango: 6-10x para empresas estables

Comparar terminal value DCF vs terminal multiple:
  → Si divergen mucho, investigar por qué
```

---

## SECCIÓN 5: Escenarios Obligatorios

### Bear Case (25% probabilidad)
```
Assumptions:
  → Revenue growth: ___% (TAM stagnant + share loss)
  → Margin: ___% (compression from competition)
  → WACC: ___% (base + 1%)
  → Terminal growth: ___% (base - 0.5%)

Fair Value Bear: €___
```

### Base Case (50% probabilidad)
```
Assumptions:
  → Revenue growth: ___% (derivado de TAM + share + pricing)
  → Margin: ___% (histórico normalizado)
  → WACC: ___% (calculated)
  → Terminal growth: ___% (≤ GDP)

Fair Value Base: €___
```

### Bull Case (25% probabilidad)
```
Assumptions:
  → Revenue growth: ___% (TAM accelerates + share gains)
  → Margin: ___% (operating leverage kicks in)
  → WACC: ___% (base - 1%)
  → Terminal growth: ___% (base + 0.5%)

Fair Value Bull: €___
```

### Expected Value
```
EV = (Bear × 25%) + (Base × 50%) + (Bull × 25%)
EV = (€___ × 0.25) + (€___ × 0.50) + (€___ × 0.25)
EV = €___

Precio actual: €___
Margen de seguridad vs EV: ___%
Margen de seguridad vs Bear: ___%
```

---

## OUTPUT REQUERIDO

Este framework debe producir para la thesis:

1. **Tabla de proyección de ingresos** con lógica TAM/share/pricing
2. **Tabla de proyección de márgenes** con justificación
3. **WACC derivado** (no default)
4. **Tres escenarios** con fair values
5. **Expected value ponderado**
6. **Margen de seguridad** vs EV y vs Bear case

**REGLA DURA:** Si uso un número sin justificación lógica → la proyección no es válida → no puedo tomar decisión.

**USO CON DCF TOOL:**
```bash
# Después de derivar los parámetros con este framework:
python3 tools/dcf_calculator.py TICKER --growth [derivado] --wacc [derivado] --terminal [derivado] --scenarios
```
