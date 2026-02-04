# Tools Reference

> Este archivo se carga automáticamente junto con CLAUDE.md
> Contiene documentación de todos los tools cuantitativos en tools/

## Principio Core
**FUENTE ÚNICA de cálculos repetibles. NUNCA duplicar lógica inline.**

---

## Core Tools (uso diario)

### price_checker.py - FUENTE ÚNICA de precios
```bash
python3 tools/price_checker.py TICKER1 TICKER2 ...
```
- Obtiene precios via yfinance (única fuente autorizada)
- Conversión automática EUR/USD/GBP
- Muestra: precio, 52w high/low, P/E, yield, market cap
- **REGLA: NUNCA usar WebSearch para precios. NUNCA hardcodear precios.**

### portfolio_stats.py - Estado del portfolio
```bash
python3 tools/portfolio_stats.py
```
- Lee portfolio/current.yaml
- Calcula P&L real, allocation por sector/geo, Sharpe ratio
- Compara vs benchmark (MSCI Europe)
- Alertas de límites (sizing, concentración)
- **NUNCA calcular portfolio stats a mano**

### effectiveness_tracker.py - EVALUACIÓN DE EFECTIVIDAD
```bash
python3 tools/effectiveness_tracker.py           # Reporte completo
python3 tools/effectiveness_tracker.py --summary # Solo métricas
```
- Trackea win rate, hit rate (FV reached), Sharpe ratio estimado
- Attribution analysis por sector, geografía, tier, holding period
- Evaluación retrospectiva de tesis (on track / off track)
- Recomendaciones automáticas basadas en patrones
- **REGLA: Ejecutar CADA sesión para detectar problemas temprano**
- Complementar con portfolio/history.yaml para posiciones cerradas
- Ver skill: effectiveness-evaluation para framework completo

### dynamic_screener.py - Screening cuantitativo programático (TOOL PRINCIPAL)
```bash
python3 tools/dynamic_screener.py --index europe_all              # All European indices
python3 tools/dynamic_screener.py --index stoxx600 --pe-max 12 --yield-min 4
python3 tools/dynamic_screener.py --index europe_all --near-low 15  # >15% below 52w high
python3 tools/dynamic_screener.py --index europe_all --undiscovered # <10 analysts, <15B mcap
python3 tools/dynamic_screener.py --index sp500 --pe-max 10
python3 tools/dynamic_screener.py --index sp400 --pe-max 10 --yield-min 3  # US MidCap 400
python3 tools/dynamic_screener.py --index us_all --undiscovered    # SP500+SP400+Russell1000
python3 tools/dynamic_screener.py --index mib40 --min-fcf-yield 5
```
- **Obtiene tickers PROGRAMÁTICAMENTE** de Wikipedia/yfinance (cero popularity bias)
- Índices US: sp500, sp400 (MidCap), russell1000, us_all, us_midcap
- Índices EU: dax40, cac40, ibex35, aex25, ftse100, ftse250, mib40, omx_stockholm, bel20, stoxx600, europe_all, nordic
- Otros: nikkei225, all, custom
- Filtros: P/E, yield, FCF yield, debt/equity, market cap, distancia 52w high, num analistas
- Flag `--undiscovered`: filtra <10 analistas Y mcap <15B (máxima ineficiencia)
- Sort: pe, fcf_yield, div_yield, mcap, analysts, dist_high
- Cache de tickers con `--refresh` para forzar actualización
- **REEMPLAZA screener.py y midcap_screener.py (ambos DEPRECATED)**

### dcf_calculator.py - DCF (Discounted Cash Flow) valuation
```bash
python3 tools/dcf_calculator.py AAPL                          # Default params (growth 5%, terminal 2.5%, WACC 9%)
python3 tools/dcf_calculator.py AAPL --growth 8 --terminal 2 --wacc 10
python3 tools/dcf_calculator.py AAPL --years 10               # 10-year projection (default: 5)
python3 tools/dcf_calculator.py AAPL --scenarios              # Bear/Base/Bull scenarios
python3 tools/dcf_calculator.py AAPL MSFT GOOGL               # Batch analysis
python3 tools/dcf_calculator.py AAPL --output results.csv     # Save to CSV
```
- Descarga FCF histórico via yfinance (últimos 5 años)
- Calcula CAGR histórico de FCF para comparar con growth rate proyectado
- Proyecta FCF futuro (5-10 años configurable)
- Terminal value via Gordon Growth Model
- Calcula valor intrínseco por acción y Margin of Safety (MoS%)
- **Flag `--scenarios`**: calcula Bear (growth -2pp, wacc +1pp), Base, Bull (growth +2pp, wacc -1pp)
- Batch mode: múltiples tickers con tabla resumen
- Waterfall detallado: muestra FCF histórico, proyección año a año, PV de cada flujo, terminal value
- Conversión automática a EUR (consistente con otros tools)
- **Resta net debt automáticamente** del Enterprise Value para obtener Equity Value correcto (fix Sesión 21)
- **ADVERTENCIA**: DCF es sensible a inputs (GIGO). Siempre validar growth rate vs histórico y vs peers.
- **ADVERTENCIA**: Para empresas con alta deuda (ej: GIS $13B net debt), el net debt puede reducir drásticamente el fair value. Siempre verificar que el resultado tiene sentido vs P/E y comparables.

### constraint_checker.py - Pre-validación de constraints
```bash
python3 tools/constraint_checker.py CHECK TEP.PA 400    # Simula compra y verifica limits
python3 tools/constraint_checker.py REPORT               # Muestra violaciones actuales
```
- Verifica: posición max 7%, sector max 25%, geografía max 35%, cash min 5%, max 20 posiciones
- **REGLA: Ejecutar SIEMPRE antes de recomendar BUY/ADD al humano**

### correlation_matrix.py - Correlaciones entre posiciones
```bash
python3 tools/correlation_matrix.py
```
- Calcula matriz de correlación entre todas las posiciones del portfolio
- Útil para diversificación y gestión de riesgo

---

## Reglas de Tools

1. **SIEMPRE usar tools existentes antes de hacer cálculos inline**
2. **Si un cálculo se repite >1 vez → crear tool nuevo (delegar a quant-tools-dev agent)**
3. **Precios SIEMPRE via price_checker.py (NUNCA WebSearch, NUNCA hardcodear)**
4. **Portfolio stats SIEMPRE via portfolio_stats.py (NUNCA calcular a mano)**
5. **Screening sistemático SIEMPRE via dynamic_screener.py (NUNCA screener.py/midcap_screener.py que están DEPRECATED, NUNCA WebSearch manual)**
6. **DCF valuation SIEMPRE via dcf_calculator.py (NUNCA cálculos inline)**
7. **Tools deben ser agnósticos - parametrizables, reutilizables, documentados**

---

## Regla de Herramientas (Desarrollo)
**Si hago un cálculo Python inline más de 1 vez → DEBE convertirse en tool en tools/.**
Delegar a quant-tools-dev agent. NUNCA repetir código inline.

---

## Tools Deprecated (NO USAR)
- `screener.py` → usar `dynamic_screener.py`
- `midcap_screener.py` → usar `dynamic_screener.py`

---

## yfinance Rate Limiting
- Screening masivo (>50 tickers) en una sesión puede agotar el rate limit
- Espaciar screenings o usar cache
- No lanzar custom screening de 30+ tickers inmediatamente después de un screening grande
- No lanzar >2 agentes que usen yfinance en paralelo
