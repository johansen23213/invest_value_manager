# Tools Reference

> Auto-loaded. Tools outputan DATOS CRUDOS. No juicios ni recomendaciones.
> Todos incluyen FX fallback warning.

---

## Core Tools

| Tool | Comando | Proposito |
|------|---------|-----------|
| `price_checker.py` | `python3 tools/price_checker.py TICKER1 TICKER2` | Precios via yfinance. UNICA fuente. NUNCA WebSearch. |
| `portfolio_stats.py` | `python3 tools/portfolio_stats.py` | P&L, allocation sector/geo. NUNCA a mano. |
| `effectiveness_tracker.py` | `python3 tools/effectiveness_tracker.py [--summary]` | Win rate, hit rate, Sharpe, attribution. Cada sesion. |
| `quality_scorer.py` | `python3 tools/quality_scorer.py TICKER [--detailed\|--raw]` | Quality Profile + Legacy Score. TOOL-FIRST. |
| `forward_return.py` | `python3 tools/forward_return.py [--active-only\|--pipeline-only]` | MoS%, Growth%, Yield% por posicion. Datos crudos. |
| `quality_universe.py` | `python3 tools/quality_universe.py {report\|actionable\|add\|stale\|coverage\|stats}` | Capital deployment machine. Universe de QS>=65. |
| `constraint_checker.py` | `python3 tools/constraint_checker.py {REPORT\|CHECK TICKER AMT} [--drawdown N]` | Concentracion, impacto drawdown. Contexto, no juicio. |
| `correlation_matrix.py` | `python3 tools/correlation_matrix.py` | Correlaciones entre posiciones. |

## Screening & Valuation

| Tool | Comando | Proposito |
|------|---------|-----------|
| `dynamic_screener.py` | `python3 tools/dynamic_screener.py --index {sp500\|us_all\|europe_all\|...}` | Screening programatico. Anti-bias. `--undiscovered` para small/mid. |
| `dcf_calculator.py` | `python3 tools/dcf_calculator.py TICKER [--scenarios] [--sensitivity]` | DCF + scenarios + sensitivity matrix. Resta net debt. GIGO warning. |
| `opportunity_filter.py` | `python3 tools/opportunity_filter.py --csv FILE [--roic-min N]` | Stage 2 sobre CSV de screener. ROIC, FCF margin, rev CAGR. |

## Consistency & System

| Tool | Comando | Proposito |
|------|---------|-----------|
| `consistency_checker.py` | `python3 tools/consistency_checker.py "BUY TICKER N%"` | Compara vs precedentes (decisions_log). ANTES de decisiones. |
| `drift_detector.py` | `python3 tools/drift_detector.py [--verbose]` | Detecta sizing drift, conviction inflation. Cada 14 dias. |
| `system_projection.py` | `python3 tools/system_projection.py [--additions N]` | Monte Carlo 1-10 anos. Fat tails. |

## Indices Disponibles (dynamic_screener)

US: `sp500`, `sp400`, `russell1000`, `us_all` | EU: `dax40`, `cac40`, `ftse100`, `ftse250`, `stoxx600`, `europe_all`, `nordic` | Otros: `mib40`, `ibex35`, `aex25`, `nikkei225`

## Reglas

1. SIEMPRE tools antes de calculos inline
2. Calculo repetido >1x → crear tool (`quant-tools-dev`)
3. Precios SOLO via `price_checker.py`
4. Screening SOLO via `dynamic_screener.py` (screener.py/midcap_screener.py DEPRECATED)
5. yfinance: max ~50 tickers/sesion, max 2 agentes yfinance en paralelo
