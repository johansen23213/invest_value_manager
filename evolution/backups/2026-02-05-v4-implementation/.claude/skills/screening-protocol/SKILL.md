---
name: screening-protocol
description: Systematic screening protocol for finding ALL companies in a sector. Anti-availability-bias.
user-invocable: false
disable-model-invocation: false
---

# Screening Protocol Skill

## Proceso OBLIGATORIO al explorar sector

### Paso 1: Universo completo
Buscar: "[sector] stocks screening P/E dividend yield [year]"
Objetivo: >10 empresas, no solo las famosas

### Paso 2: Filtros cuantitativos
Base: P/E <15x, yield >3%, market cap >$500M, debt/equity <2x

Ajustes por tipo:
- Defensive: yield >4%, payout <80%, ROE >10%
- Cyclical: P/FCF <10x, ROIC >WACC
- Growth value: PEG <1.5, sales growth >10%, P/E <20x

### Paso 3: Top 5-10 matches
Seleccionar por: margen seguridad, moat, menor riesgo

### Paso 4: Tabla comparativa
| Empresa | Ticker | P/E | Yield | Debt/Eq | Mkt Cap | Geo | Notas |

### Paso 5: Analizar top 2-3
NO analizar solo "la primera que conozco"

## Anti-sesgo
- Si <10 empresas encontradas → screening incompleto
- Si ninguna empresa desconocida → sesgo disponibilidad
- Comparar múltiples geografías
- Buscar ETF holdings para descubrir nombres

## Herramientas de búsqueda
- "[sector] stocks undervalued [year]"
- "[sector] high dividend yield stocks [year]"
- Sector ETF holdings
- Stock screeners (Yahoo, Finviz, TradingView)

## Regla de oro
Si 3+ sectores en región X no tienen value → cambiar a región Y
