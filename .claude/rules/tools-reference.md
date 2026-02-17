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
python3 tools/dynamic_screener.py --index europe_all              # All European large/mid cap indices
python3 tools/dynamic_screener.py --index stoxx600 --pe-max 12 --yield-min 4
python3 tools/dynamic_screener.py --index europe_all --near-low 15  # >15% below 52w high
python3 tools/dynamic_screener.py --index europe_all --undiscovered # Default: <10 analysts, <15B mcap
python3 tools/dynamic_screener.py --index europe_all --undiscovered --undiscovered-analysts 5 --undiscovered-mcap 5
python3 tools/dynamic_screener.py --index sp500 --pe-max 10
python3 tools/dynamic_screener.py --index sp400 --pe-max 10 --yield-min 3  # US MidCap 400
python3 tools/dynamic_screener.py --index us_all --undiscovered    # SP500+SP400+Russell1000
python3 tools/dynamic_screener.py --index mib40 --min-fcf-yield 5
# Small & Mid Cap indices (added Session 72):
python3 tools/dynamic_screener.py --index sp600                    # S&P SmallCap 600 (US)
python3 tools/dynamic_screener.py --index sdax                     # SDAX (German Small Cap, ~70 companies)
python3 tools/dynamic_screener.py --index mdax                     # MDAX (German Mid Cap, ~50 companies)
python3 tools/dynamic_screener.py --index cac_mid60                # CAC Mid 60 (French Mid/Small Cap)
python3 tools/dynamic_screener.py --index cac_next20               # CAC Next 20 (French Mid Cap)
python3 tools/dynamic_screener.py --index ftse_aim100              # FTSE AIM 100 (UK Small Cap)
python3 tools/dynamic_screener.py --index smallcap_all             # All small caps (US + EU)
python3 tools/dynamic_screener.py --index europe_smallcap          # EU small caps only
python3 tools/dynamic_screener.py --index german_all               # DAX40 + MDAX + SDAX
python3 tools/dynamic_screener.py --index french_all               # CAC40 + CAC Mid60 + CAC Next20
python3 tools/dynamic_screener.py --index smallcap_all --undiscovered  # Best for value: low coverage small caps
```
- **Obtiene tickers PROGRAMÁTICAMENTE** de Wikipedia/yfinance (cero popularity bias)
- **pe_max default = 999 (no filter)** — quality compounders often have high P/E
- Índices US: sp500, sp400 (MidCap), sp600 (SmallCap), russell1000, us_all, us_all_caps, us_midcap, us_smallcap
- Índices EU: dax40, cac40, ibex35, aex25, ftse100, ftse250, mib40, omx_stockholm, bel20, stoxx600, europe_all, europe_all_caps, nordic
- Índices Small/Mid Cap: sdax, mdax, cac_mid60, cac_next20, ftse_aim100
- Composites: europe_smallcap, smallcap_all, german_all, french_all
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

## Consistency & System Tools

### consistency_checker.py - Compara decisión vs precedentes
```bash
python3 tools/consistency_checker.py "BUY NVO 4%"
python3 tools/consistency_checker.py "TRIM SHEL.L 50%"
python3 tools/consistency_checker.py "HOLD ADBE"
```
- Lee `learning/decisions_log.yaml` y busca precedentes similares (mismo action type, ticker, tier)
- Compara sizing de la decisión propuesta contra precedentes: coherente (<1.5pp diff), razonable (<3pp), o alerta (>3pp)
- Muestra top 3 precedentes con fecha, sizing, tier, MoS y razonamiento
- Análisis de coherencia: COHERENTE / INCONSISTENCIA DETECTADA / SIN PRECEDENTES COMPARABLES
- **Usar ANTES de decisiones importantes de BUY/ADD/TRIM/SELL**
- Si no hay precedentes, documenta que la decisión será un nuevo precedente

### drift_detector.py - Detecta cambios graduales en patrones
```bash
python3 tools/drift_detector.py               # Reporte estándar
python3 tools/drift_detector.py --verbose      # Con detalle por tier y últimos sizings
```
- Analiza 4 métricas desde `learning/decisions_log.yaml`:
  - **Sizing Trend**: compara primera mitad vs segunda mitad de decisiones, detecta drift >0.5pp
  - **MoS Threshold**: datos crudos de MoS mínimo/promedio aceptado por tier (no hardcoded thresholds)
  - **Conviction Distribution**: detecta si >85% de decisiones son "alta convicción" (posible inflación)
  - **Decision Frequency**: alerta si >14 días sin documentar decisiones
- Overall status: OK / REVIEW / ALERT con acción recomendada
- `--verbose` muestra detalle de sizings recientes y patrones documentados por tier
- **Ejecutar cada health-check (cada 14 días) para detectar drift inadvertido**

### opportunity_filter.py - Filtro fundamental Stage 2 sobre CSV de screener
```bash
python3 tools/opportunity_filter.py --csv screener_output.csv
python3 tools/opportunity_filter.py --csv file1.csv file2.csv --roic-min 20 --fcf-margin-min 15 --rev-cagr-min 8
python3 tools/opportunity_filter.py --csv results.csv --exclude AAPL MSFT --workers 8
python3 tools/opportunity_filter.py --csv results.csv --output filtered.csv
```
- Lee CSV outputs de `dynamic_screener.py` y aplica filtros fundamentales via yfinance
- Filtros parametrizables: ROIC min (default 15%), FCF margin min (default 10%), Revenue CAGR min (default 5%)
- Calcula para cada ticker: ROIC, FCF margin, Revenue CAGR, ROE, D/E, distancia a 52w high
- Fetching paralelo con `--workers` (default 6) para velocidad
- Summary por sector y geografía
- `--exclude` para excluir posiciones existentes
- `--output` guarda resultados filtrados a CSV
- **ADVERTENCIA**: Usa yfinance intensivamente. Respetar rate limiting si input tiene >50 tickers.
- **Workflow típico**: `dynamic_screener.py` (Stage 1: universo amplio) -> `opportunity_filter.py` (Stage 2: filtro fundamental)

### system_projection.py - Proyección Monte Carlo del sistema
```bash
python3 tools/system_projection.py                       # Default: 10,000 sims, sin aportaciones
python3 tools/system_projection.py --additions 500       # EUR 500/mes de aportaciones
python3 tools/system_projection.py --sims 50000          # 50,000 simulaciones
```
- Simulación Monte Carlo a 1, 3, 5 y 10 años con 3 escenarios (Bull/Base/Bear) ponderados
- Modela: retorno por tier (A/B/C), rotación gradual C->A, session alpha (decreciente), learning curve, cash drag, costes de transacción
- Fat tails via Student-t (5 df) + eventos discretos de drawdown/crash
- Output: tabla resumen con valor mediano, CAGR, P(return>0%), P(CAGR>8%), P(doblar), P(pérdida>20%), max drawdown
- Genera gráfico PNG en `docs/system_projection.png` (fan chart, distribuciones, evolución de calidad, escenarios)
- Supuestos explícitos e impresos al inicio (NO ocultos)
- Evaluación cualitativa de fortalezas, debilidades y riesgos existenciales
- **NOTA**: Los parámetros hardcodeados (INITIAL_VALUE, N_POSITIONS, CURRENT_TIERS) deben actualizarse manualmente si el portfolio cambia significativamente
- **Output: DATOS CRUDOS + supuestos explícitos (Framework v4.0)**

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
