# Tools Reference

> Este archivo se carga automáticamente junto con CLAUDE.md
> Contiene documentación de todos los tools cuantitativos en tools/

## Principio Core
**FUENTE ÚNICA de cálculos repetibles. NUNCA duplicar lógica inline.**

**Principio v4.0:** Tools outputan DATOS CRUDOS. No juicios, no categorías, no recomendaciones.
Todos los tools incluyen FX fallback warning si yfinance no responde.

---

## Core Tools (uso diario)

### price_checker.py - FUENTE ÚNICA de precios
```bash
python3 tools/price_checker.py TICKER1 TICKER2 ...
```
- Obtiene precios via yfinance (única fuente autorizada)
- Conversión automática EUR/USD/GBP con FX fallback warning
- Muestra: precio, 52w high/low, P/E, yield, market cap
- **REGLA: NUNCA usar WebSearch para precios. NUNCA hardcodear precios.**

### portfolio_stats.py - Estado del portfolio
```bash
python3 tools/portfolio_stats.py
```
- Lee portfolio/current.yaml
- Calcula P&L real, allocation por sector/geo
- FX fallback warning si yfinance no responde
- **NUNCA calcular portfolio stats a mano**

### effectiveness_tracker.py - EVALUACIÓN DE EFECTIVIDAD
```bash
python3 tools/effectiveness_tracker.py           # Reporte completo
python3 tools/effectiveness_tracker.py --summary # Solo métricas
```
- Trackea win rate, hit rate (FV reached), Sharpe ratio estimado
- Attribution analysis por sector, geografía, tier, holding period
- Evaluación retrospectiva de tesis (on track / off track)
- **REGLA: Ejecutar CADA sesión para detectar problemas temprano**
- Complementar con portfolio/history.yaml para posiciones cerradas
- Ver skill: effectiveness-evaluation para framework completo

### dynamic_screener.py - Screening cuantitativo programático (TOOL PRINCIPAL)
```bash
python3 tools/dynamic_screener.py --index europe_all              # All European indices (NO pe_max filter by default)
python3 tools/dynamic_screener.py --index stoxx600 --pe-max 12 --yield-min 4
python3 tools/dynamic_screener.py --index europe_all --near-low 15  # >15% below 52w high
python3 tools/dynamic_screener.py --index europe_all --undiscovered # Default: <10 analysts, <15B mcap
python3 tools/dynamic_screener.py --index europe_all --undiscovered --undiscovered-analysts 5 --undiscovered-mcap 5
python3 tools/dynamic_screener.py --index sp500 --pe-max 10
python3 tools/dynamic_screener.py --index sp400 --pe-max 10 --yield-min 3  # US MidCap 400
python3 tools/dynamic_screener.py --index us_all --undiscovered    # SP500+SP400+Russell1000
python3 tools/dynamic_screener.py --index mib40 --min-fcf-yield 5
```
- **Obtiene tickers PROGRAMÁTICAMENTE** de Wikipedia/yfinance (cero popularity bias)
- **pe_max default = 999 (no filter)** — quality compounders often have high P/E
- Índices US: sp500, sp400 (MidCap), russell1000, us_all, us_midcap
- Índices EU: dax40, cac40, ibex35, aex25, ftse100, ftse250, mib40, omx_stockholm, bel20, stoxx600, europe_all, nordic
- Otros: nikkei225, all, custom
- Filtros: P/E, yield, FCF yield, debt/equity, market cap, distancia 52w high, num analistas
- Flag `--undiscovered`: parametrizable (`--undiscovered-analysts`, `--undiscovered-mcap`)
- Outlier data flagged with neutral `[!]` marker (not "likely data error")
- Sort: pe, fcf_yield, div_yield, mcap, analysts, dist_high
- Cache de tickers con `--refresh` para forzar actualización
- FX fallback warning
- **REEMPLAZA screener.py y midcap_screener.py (ambos DEPRECATED)**

### dcf_calculator.py - DCF (Discounted Cash Flow) valuation
```bash
python3 tools/dcf_calculator.py AAPL                          # Default params (growth 5%, terminal 2.5%, WACC 9%)
python3 tools/dcf_calculator.py AAPL --growth 8 --terminal 2 --wacc 10
python3 tools/dcf_calculator.py AAPL --years 10               # 10-year projection (default: 5)
python3 tools/dcf_calculator.py AAPL --scenarios              # Bear/Base/Bull with configurable deltas
python3 tools/dcf_calculator.py AAPL --scenarios --bear-growth-delta -3 --bear-wacc-delta 2
python3 tools/dcf_calculator.py AAPL --sensitivity            # Sensitivity matrix (Growth x WACC)
python3 tools/dcf_calculator.py AAPL --scenarios --sensitivity # Both combined
python3 tools/dcf_calculator.py AAPL MSFT GOOGL               # Batch analysis
python3 tools/dcf_calculator.py AAPL --output results.csv     # Save to CSV
```
- Descarga FCF histórico via yfinance (últimos 5 años)
- Calcula CAGR histórico de FCF para comparar con growth rate proyectado
- Proyecta FCF futuro (5-10 años configurable)
- Terminal value via Gordon Growth Model
- Calcula valor intrínseco por acción y Margin of Safety (MoS%)
- **Flag `--scenarios`**: Bear/Base/Bull con deltas parametrizables:
  - `--bear-growth-delta` (default: -2pp), `--bear-wacc-delta` (default: +1pp)
  - `--bull-growth-delta` (default: +2pp), `--bull-wacc-delta` (default: -1pp)
- **Flag `--sensitivity`**: matriz 5x3 de Growth x WACC mostrando FV en cada combinación
  - Reports TV% of EV and FV Spread as raw data (no categorization)
  - Combinable con `--scenarios` (ambos outputs se muestran)
- Batch mode: summary table with MoS (no buy/hold/over categorization)
- Conversión automática a EUR con FX fallback warning
- **Resta net debt automáticamente** del Enterprise Value para obtener Equity Value correcto
- **ADVERTENCIA**: DCF es sensible a inputs (GIGO). Siempre validar growth rate vs histórico y vs peers.

### quality_scorer.py - Quality Profile + Legacy Score (v4.0)
```bash
python3 tools/quality_scorer.py TICKER                   # Profile + legacy score
python3 tools/quality_scorer.py TICKER --raw             # Profile only (no legacy score)
python3 tools/quality_scorer.py TICKER --detailed        # Profile + legacy breakdown by category
python3 tools/quality_scorer.py TICKER --legacy          # Legacy score only (backward compat)
python3 tools/quality_scorer.py TICKER1 TICKER2 ...      # Batch analysis con summary table
```
- **PRIMARY OUTPUT: Quantitative Profile** with multi-year trajectories:
  - Returns on Capital: ROIC trajectory, ROE trajectory, WACC (real Kd + effective tax), ROIC-WACC spread
  - Margins & Cash Flow: GM trajectory + trend + vs sector, OpM trajectory, FCF trajectory + consistency
  - Leverage: Net Debt/EBITDA, interest coverage
  - Growth: Revenue trajectory + CAGR, EPS trajectory + CAGR
  - Capital Allocation: insider %, institutional %, dividend yield, payout ratio
  - Data Gaps: explicitly reported at top (no silent inflation)
- **WACC improvements v4.0**: Real cost of debt (interest_expense/total_debt), effective tax rate from financials
- **ROIC improvements v4.0**: Proper NOPAT/Invested_Capital with actual tax rate
- **N/A = 0 points** in legacy score (not inflated defaults)
- **LEGACY SCORE (deprecating)**: at bottom, clearly marked. Uses arbitrary thresholds.
  - Tier A (75-100), Tier B (55-74), Tier C (35-54), Tier D (<35): Below minimum threshold
- **REGLA: Ejecutar SIEMPRE antes de cualquier análisis fundamental**
- **REGLA: Tier D = calidad mínima insuficiente, no proceder**
- **REGLA: QS Tool-First** — thesis muestra AMBOS: QS Tool + QS Ajustado (si difiere)

### constraint_checker.py - Portfolio Context Tool (Framework v4.0)
```bash
python3 tools/constraint_checker.py REPORT                      # Default 50% drawdown
python3 tools/constraint_checker.py REPORT --drawdown 30        # Custom drawdown %
python3 tools/constraint_checker.py CHECK ADBE 400              # Simula compra
python3 tools/constraint_checker.py CHECK ADBE 400 --drawdown 30
```
- **Framework v4.0**: Provee DATOS CRUDOS, no juzga
- Muestra: concentración por posición, sector, geografía
- Calcula impacto con drawdown parametrizable (default 50%)
- FX fallback warning
- **NO tiene "reference points" ni "warnings" - solo contexto para decidir**
- Ver `learning/principles.md` para framework de decisión

### forward_return.py - Forward Return Components (v4.0)
```bash
python3 tools/forward_return.py                    # Todas las posiciones
python3 tools/forward_return.py --ticker ADBE NVO  # Tickers específicos
python3 tools/forward_return.py --active-only       # Solo posiciones activas
python3 tools/forward_return.py --pipeline-only     # Solo pipeline research
```
- Muestra MoS%, Growth%, Yield% como **columnas separadas** (no composite FER)
- Lee fair value de thesis files, precios actuales de yfinance
- Incluye conviction como dato (no aplica multiplicadores)
- **No hay TOP 3 / BOTTOM 3** — el display order es por MoS% descending
- FX fallback warning
- **Output: DATOS CRUDOS solamente (Framework v4.0)**
- Usado en FASE 2.5 (Rotation Check) del session-protocol
- **REGLA: Ejecutar cada sesión como parte del Rotation Check**

### quality_universe.py - Capital Deployment Machine (NUEVO Sesion 61)
```bash
python3 tools/quality_universe.py report              # Full universe con precios y distancia a entry
python3 tools/quality_universe.py actionable           # Empresas dentro del 15% del entry
python3 tools/quality_universe.py add TICKER --qs 75 --fv 200 --entry 150 --sector "Tech" --tier A
python3 tools/quality_universe.py remove TICKER
python3 tools/quality_universe.py coverage             # Gaps de cobertura sectorial
python3 tools/quality_universe.py refresh              # Update precios (batch con rate limiting)
python3 tools/quality_universe.py stale                # Empresas que necesitan re-evaluación (por días desde último scoring)
python3 tools/quality_universe.py stats                # Métricas de salud del pipeline (datos crudos, sin targets fijos)
```
- Base de datos persistente de empresas QS >= 65 en `state/quality_universe.yaml`
- Parte del pipeline `capital-deployment` (PRIORIDAD #1 mientras cash > 25%)
- `report`: Muestra universe completo con precios live, distancia a entry, pipeline status
- `actionable`: Filtra solo empresas dentro del 15% del entry price
- `coverage`: Mapea 23 sectores GICS, muestra cuales tienen sector view y empresas
- `stats`: Pipeline health metrics vs targets (universe size, R1+ count, sectors, actionable)
- FX conversion automatica + fallback warning
- **Output: DATOS CRUDOS solamente (Framework v4.0)**
- **REGLA: Ejecutar `actionable` al inicio de cada sesion (FASE 0 del Capital Deployment)**
- Skill completo: `.claude/skills/capital-deployment/SKILL.md`

### correlation_matrix.py - Correlaciones entre posiciones
```bash
python3 tools/correlation_matrix.py
```
- Calcula matriz de correlación entre todas las posiciones del portfolio
- Útil para diversificación y gestión de riesgo

---

## FX Fallback Warning (transversal)

Todos los tools que usan FX rates ahora reportan si caen a rates estáticas:
```
FX WARNING: Using static fallback rates (EUR/USD=1.04). EUR amounts may be inaccurate.
```
Esto permite detectar cuando los datos de precio/valor están basados en rates potencialmente desactualizadas.

---

## Reglas de Tools

1. **SIEMPRE usar tools existentes antes de hacer cálculos inline**
2. **Si un cálculo se repite >1 vez → crear tool nuevo (delegar a quant-tools-dev agent)**
3. **Precios SIEMPRE via price_checker.py (NUNCA WebSearch, NUNCA hardcodear)**
4. **Portfolio stats SIEMPRE via portfolio_stats.py (NUNCA calcular a mano)**
5. **Screening sistemático SIEMPRE via dynamic_screener.py (NUNCA screener.py/midcap_screener.py que están DEPRECATED, NUNCA WebSearch manual)**
6. **DCF valuation SIEMPRE via dcf_calculator.py (NUNCA cálculos inline)**
7. **Tools deben ser agnósticos - parametrizables, reutilizables, documentados**
8. **Tools outputan DATOS CRUDOS — no juicios, categorías ni recomendaciones**

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
