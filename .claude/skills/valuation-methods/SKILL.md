---
name: valuation-methods
description: Multiple valuation methods by company type - DCF, EV/EBIT, NAV, DDM, Sum-of-Parts. Minimum 2 methods per analysis.
user-invocable: false
disable-model-invocation: false
---

# Valuation Methods Skill

## Propósito
NO depender solo de DCF. Seleccionar método(s) apropiados según tipo de empresa.

## REGLA: Mínimo 2 métodos por análisis
Si los métodos divergen >30% → investigar por qué antes de decidir.

---

## Selección de Método por Tipo de Empresa

| Tipo | Método Primario | Método Secundario | Por qué |
|------|-----------------|-------------------|---------|
| **Crecimiento estable** (utilities, staples) | DCF | EV/EBIT normalizado | FCF predecible, earnings estables |
| **Cíclica** (autos, commodities, industrials) | EV/EBIT mid-cycle | P/B vs ROE histórico | Earnings volátiles, usar normalizado |
| **Asset-heavy** (real estate, infra) | NAV / Replacement cost | Dividend Discount | Activos tangibles son el valor |
| **Financiera** (banks, insurers) | P/B vs ROE | Dividend Discount | Balance es el negocio, P/E distorsionado |
| **Growth** (tech, biotech early) | DCF con escenarios | EV/Revenue vs growth | Earnings negativos, valorar potencial |
| **Turnaround** (distressed) | Sum-of-parts | Liquidation value | Incertidumbre alta, valorar piso |
| **Holding/Conglomerado** | Sum-of-parts | NAV | Partes valen más que el todo |
| **Dividend aristocrat** | DDM | DCF | Dividendo es el valor, FCF → dividendo |

---

## MÉTODO 1: DCF (Discounted Cash Flow)

### Cuándo usar
- Empresas con FCF positivo y predecible
- Crecimiento relativamente estable
- NO usar para cíclicas en pico/valle del ciclo

### Proceso
```bash
# SIEMPRE usar el tool, NUNCA calcular inline
python3 tools/dcf_calculator.py TICKER --scenarios

# Con parámetros derivados del projection-framework:
python3 tools/dcf_calculator.py TICKER --growth X --wacc Y --terminal Z --scenarios
```

### Output esperado
- Fair value Bear/Base/Bull
- Margen de seguridad vs precio actual

---

## MÉTODO 2: EV/EBIT Normalizado

### Cuándo usar
- Empresas cíclicas
- Cuando earnings actuales no son representativos
- Comparación con peers

### Proceso
```
1. Calcular EBIT normalizado (promedio 5-7 años, ajustado por ciclo)
2. Determinar múltiplo apropiado:
   - Sector múltiple promedio
   - Histórico de la empresa
   - Ajustar por calidad (growth, ROIC, moat)
3. EV = EBIT normalizado × Múltiplo
4. Equity Value = EV - Net Debt
5. Fair Value = Equity Value / Shares
```

### Tabla de múltiplos típicos
| Sector | EV/EBIT Rango | Comentario |
|--------|---------------|------------|
| Utilities | 10-14x | Estables, regulados |
| Consumer Staples | 12-16x | Defensivos, predecibles |
| Industrials | 8-12x | Cíclicos, capital intensive |
| Financials | N/A | Usar P/B |
| Tech (mature) | 12-18x | Depende de growth |
| Energy | 5-8x | Muy cíclico, commodity |
| Retail | 6-10x | Competitivo, márgenes bajos |
| Pharma | 10-14x | Pipeline risk |

### Ajustes al múltiplo
```
Base múltiplo (sector median): Xx

Ajustes:
  + Superior ROIC vs peers: +1-2x
  + Wide moat: +1-2x
  + Above-average growth: +1-2x
  - Below-average growth: -1-2x
  - High leverage: -1-2x
  - Governance concerns: -1-2x

Múltiplo final: Xx
```

---

## MÉTODO 3: NAV (Net Asset Value)

### Cuándo usar
- REITs, real estate companies
- Asset-heavy businesses
- Holdings con activos claramente valorables

### Proceso
```
1. Listar activos principales
2. Valorar cada activo a fair market value
   - Real estate: cap rate, comparables de mercado
   - Inversiones: precio de mercado
   - Otros activos: replacement cost o liquidation value
3. Sumar todos los activos
4. Restar todas las liabilities
5. NAV = Assets - Liabilities
6. NAV per share = NAV / Shares

Premium/Discount = (Precio - NAV) / NAV
```

### Interpretación
- Trading at discount to NAV: potencial value
- Pero verificar: ¿por qué el descuento?
  - Management malo
  - Activos overvalued en libros
  - Hidden liabilities
  - Liquidez baja

---

## MÉTODO 4: Dividend Discount Model (DDM)

### Cuándo usar
- Dividend aristocrats (10+ años de dividendo creciente)
- Utilities, REITs, financials maduros
- Cuando el dividendo es la principal forma de retorno

### Proceso (Gordon Growth Model)
```
Fair Value = D1 / (r - g)

Donde:
  D1 = Dividendo próximo año = D0 × (1 + g)
  r = Required return (Ke) = típico 8-12%
  g = Dividend growth rate sostenible

g sostenible = ROE × (1 - Payout Ratio)
  → Si payout 60% y ROE 15%: g = 15% × 40% = 6%
```

### Multi-stage DDM (para empresas en transición)
```
Fase 1 (años 1-5): High growth = g1
Fase 2 (años 6-10): Transition = fade from g1 to g2
Fase 3 (terminal): Mature growth = g2 (≤3%)

Calcular PV de dividendos en cada fase + terminal value
```

---

## MÉTODO 5: Sum-of-Parts (SOTP)

### Cuándo usar
- Conglomerados
- Holdings con múltiples negocios
- Turnarounds donde partes valen más por separado

### Proceso
```
1. Identificar segmentos de negocio
2. Valorar cada segmento independientemente:
   - Usar método apropiado para cada uno
   - Usar múltiplos de pure-play comparables
3. Sumar valores de todos los segmentos
4. Restar: corporate overhead, net debt
5. SOTP Value = Suma segmentos - overhead - net debt
```

### Conglomerate Discount
- Típico: 10-20% descuento vs SOTP
- Razones: complejidad, capital allocation, governance
- Si trading >20% discount: potencial activista target

---

## MÉTODO 6: P/B vs ROE (Financials)

### Cuándo usar
- Banks, insurers, asset managers
- Cualquier empresa donde book value es significativo

### Framework
```
P/B Justificado = (ROE - g) / (Ke - g)

Ejemplo:
  ROE = 12%
  g = 3%
  Ke = 10%
  P/B Justificado = (12% - 3%) / (10% - 3%) = 1.29x

Si trading a P/B < P/B Justificado → undervalued
```

### Tabla de referencia
| ROE | P/B Justo (asumiendo Ke=10%, g=3%) |
|-----|-------------------------------------|
| 8% | 0.7x |
| 10% | 1.0x |
| 12% | 1.3x |
| 15% | 1.7x |
| 18% | 2.1x |

---

## OUTPUT: Reconciliación de Métodos

Después de aplicar 2+ métodos, completar:

```
| Método | Fair Value | Peso | Weighted FV |
|--------|-----------|------|-------------|
| DCF Base | €___ | __% | €___ |
| EV/EBIT | €___ | __% | €___ |
| [Otro] | €___ | __% | €___ |
| **Weighted Average** | | 100% | **€___** |

Precio actual: €___
Margen de Seguridad: ___%

Si métodos divergen >30%:
→ Razón: [explicar]
→ Método más confiable para este caso: [X] porque [Y]
```

**REGLA:** El peso de cada método depende de la fiabilidad para este tipo específico de empresa. El método más apropiado según la tabla inicial tiene mayor peso.
