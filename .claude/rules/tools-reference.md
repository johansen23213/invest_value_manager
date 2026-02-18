# Tools Reference

> Auto-loaded. Tools outputan DATOS CRUDOS. No juicios ni recomendaciones.
> Todos incluyen FX fallback warning.

---

## Core Tools

| Tool | Comando | Proposito |
|------|---------|-----------|
| `price_checker.py` | `python3 tools/price_checker.py TICKER1 TICKER2` | Precios via yfinance. UNICA fuente. NUNCA WebSearch. |
| `portfolio_stats.py` | `python3 tools/portfolio_stats.py` | P&L long+short, net/gross exposure, allocation. NUNCA a mano. |
| `effectiveness_tracker.py` | `python3 tools/effectiveness_tracker.py [--summary]` | Win rate, hit rate, Sharpe, attribution. Cada sesion. |
| `quality_scorer.py` | `python3 tools/quality_scorer.py TICKER [--detailed\|--raw]` | Quality Profile + Legacy Score. TOOL-FIRST. |
| `forward_return.py` | `python3 tools/forward_return.py [--active-only\|--pipeline-only]` | MoS%, Growth%, Yield% por posicion (L/S). Datos crudos. |
| `quality_universe.py` | `python3 tools/quality_universe.py {report\|actionable\|add\|stale\|coverage\|stats} [--fragility]` | Capital deployment machine. Universe de QS>=65. --fragility para shorts. |
| `constraint_checker.py` | `python3 tools/constraint_checker.py {REPORT\|CHECK TICKER AMT\|CHECK_SHORT TICKER AMT}` | Concentracion, net/gross exposure, drawdown. Contexto, no juicio. |
| `correlation_matrix.py` | `python3 tools/correlation_matrix.py` | Correlaciones entre posiciones. |
| `insider_tracker.py` | `python3 tools/insider_tracker.py TICKER [--sections insider,institutional,short,analyst]` | Insider txns, institutional holders, short interest, analyst consensus. Datos crudos. |

## Screening & Valuation

| Tool | Comando | Proposito |
|------|---------|-----------|
| `dynamic_screener.py` | `python3 tools/dynamic_screener.py --index {sp500\|us_all\|europe_all\|...}` | Screening programatico. Anti-bias. `--undiscovered` para small/mid. |
| `batch_scorer.py` | `python3 tools/batch_scorer.py --index {sp500\|...} [--new-only] [--add-to-universe] [--dry-run]` | Mass QS scoring de indices enteros. Discovery. Auto-add a universe. |
| `dcf_calculator.py` | `python3 tools/dcf_calculator.py TICKER [--scenarios] [--sensitivity] [--reverse]` | DCF + scenarios + sensitivity. --reverse = implied expectations (solve for growth). |
| `narrative_checker.py` | `python3 tools/narrative_checker.py TICKER` | Tendencias financieras (margins, R&D, SBC, receivables, FCF). Datos crudos. |
| `opportunity_filter.py` | `python3 tools/opportunity_filter.py --csv FILE [--roic-min N]` | Stage 2 sobre CSV de screener. ROIC, FCF margin, rev CAGR. |

## Macro & Risk

| Tool | Comando | Proposito |
|------|---------|-----------|
| `macro_fragility.py` | `python3 tools/macro_fragility.py {world\|country CODE\|sector NAME\|full}` | 3-layer macro data: world (VIX, yields, gold, oil, DXY, S&P), country (index, FX, ETF, sector ETFs), sector (ETFs, P/E, top holdings). Datos crudos. |

## Consistency & System

| Tool | Comando | Proposito |
|------|---------|-----------|
| `consistency_checker.py` | `python3 tools/consistency_checker.py "BUY TICKER N%"` | Compara vs precedentes (decisions_log). ANTES de decisiones. |
| `drift_detector.py` | `python3 tools/drift_detector.py [--verbose]` | Detecta sizing drift, conviction inflation. Cada 14 dias. |
| `system_projection.py` | `python3 tools/system_projection.py [--additions N]` | Monte Carlo 1-10 anos. Fat tails. |

## Indices Disponibles (dynamic_screener / batch_scorer)

US: `sp500`, `sp400`, `russell1000`, `us_all` | EU: `dax40`, `cac40`, `ftse100`, `ftse250`, `stoxx600`, `europe_all`, `nordic` | Otros: `mib40`, `ibex35`, `aex25`, `nikkei225`

## Countries Disponibles (macro_fragility)

`US`, `UK`, `DE`, `FR`, `JP`, `IT`, `ES`, `DK`, `EU`

## Sectors Disponibles (macro_fragility)

`technology`, `healthcare`, `financials`, `energy`, `industrials`, `consumer discretionary`, `consumer staples`, `utilities`, `real estate`, `materials`, `communication`, `semiconductors`, `defense`, `insurance`, `payments`, `biotech`, `pharma`, `luxury`, `telecom`

## Reglas

1. SIEMPRE tools antes de calculos inline
2. Calculo repetido >1x → crear tool (`quant-tools-dev`)
3. Precios SOLO via `price_checker.py`
4. Screening SOLO via `dynamic_screener.py` (screener.py/midcap_screener.py DEPRECATED)
5. Mass QS scoring via `batch_scorer.py` (NOT quality_scorer.py in loop)
6. yfinance: max ~50 tickers/sesion, max 2 agentes yfinance en paralelo
