# Tools Reference

> Auto-loaded. Tools outputan DATOS CRUDOS. No juicios ni recomendaciones.
> Todos incluyen FX fallback warning.

---

## Core Tools

| Tool | Comando | Proposito |
|------|---------|-----------|
| `session_opener.py` | `python3 tools/session_opener.py [--quick]` | Phase 0-1 session init: portfolio snapshot, SO triggers, earnings 7d, forward returns, pipeline health, alerts. ONE command replaces 6+ tools. `--quick` = SOs + earnings + alerts only. |
| `price_checker.py` | `python3 tools/price_checker.py TICKER1 TICKER2` | Precios via yfinance. UNICA fuente. NUNCA WebSearch. |
| `portfolio_stats.py` | `python3 tools/portfolio_stats.py` | P&L long+short, net/gross exposure, allocation. NUNCA a mano. |
| `effectiveness_tracker.py` | `python3 tools/effectiveness_tracker.py [--summary]` | Win rate, hit rate, Sharpe, attribution. Cada sesion. |
| `quality_scorer.py` | `python3 tools/quality_scorer.py TICKER [--detailed\|--raw]` | Quality Profile + Legacy Score. TOOL-FIRST. |
| `forward_return.py` | `python3 tools/forward_return.py [--active-only\|--pipeline-only\|--deployment-ready\|--signals]` | MoS%, Growth%, Yield%, E[CAGR]@market por posicion. `--deployment-ready` filtra pipeline a E[CAGR]>=threshold. `--signals` adds insider sentiment + quality fund overlap from ownership cache. |
| `thesis_monitor.py` | `python3 tools/thesis_monitor.py [--alerts\|--ticker X Y\|--ai-kc]` | Thesis assumption checker: MoS vs FV, kill condition proximity, conviction drift, bear/bull scenario flags, probation tracking, concentration. `--alerts` = alerts only. `--ticker` = specific positions. `--ai-kc` = AI disruption KC check across all positions (moat type detection, risk classification). |
| `portfolio_optimizer.py` | `python3 tools/portfolio_optimizer.py [--deploy\|--rotate\|--cash-drag]` | Portfolio-level E[CAGR]: position contribution, cash drag quantification, deployment simulation (best pipeline candidates), rotation simulation (swap weak→strong). Default = portfolio breakdown. |
| `quality_universe.py` | `python3 tools/quality_universe.py {report\|actionable\|add\|stale\|coverage\|stats\|archive\|approaching} [--fragility]` | Capital deployment machine. Universe. `approaching`=stocks moving toward entry (delta tracking). |
| `r1_prioritizer.py` | `python3 tools/r1_prioritizer.py [--top N] [--exclude-uk] [--near-entry-only] [--tier-a-only] [--exclude-fantasy-risk] [--pre-flight] [--advancement]` | R1 prioritizer + fantasy gates. `--advancement`=3-section pipeline with E[CAGR]@mkt. `--pre-flight`=only viable E[CAGR]. Fantasy rate in footer. Smart money + insider flags from ownership cache (auto). |
| `constraint_checker.py` | `python3 tools/constraint_checker.py {REPORT\|CHECK TICKER AMT\|CHECK_SHORT TICKER AMT}` | Concentracion, net/gross exposure, drawdown. Contexto, no juicio. |
| `correlation_matrix.py` | `python3 tools/correlation_matrix.py` | Correlaciones entre posiciones. |
| `insider_tracker.py` | `python3 tools/insider_tracker.py TICKER [--sections insider,institutional,short,analyst]` | Insider txns, institutional holders, short interest, analyst consensus. Datos crudos. |
| `portfolio_dashboard.py` | `python3 tools/portfolio_dashboard.py [--no-prices]` | Dashboard visual 6 paneles: allocation, P&L, quality map, pipeline funnel, SO proximity, summary. Output: docs/portfolio_dashboard.png. `--no-prices` skip yfinance. |
| `earnings_intel.py` | `python3 tools/earnings_intel.py [--days N\|--ticker TICK]` | Pre-earnings briefing: price/MoS/E[CAGR], insider activity, kill conditions, scenarios, frameworks. Default 7 days. |
| `command_center.py` | `python3 tools/command_center.py [--fresh]` | Session-start command center v2.2: KPIs + risk matrix + calendar + SOs + enhanced 3-tier insider scoring (STRONG/BULL/BEAR with C-suite detection) + phase transition detection (>=3 portfolio earnings/week) + pipeline funnel. Single interactive HTML. Output: docs/command_center.html. |
| `earnings_workflow.py` | `python3 tools/earnings_workflow.py [--week\|--phase\|TICKER\|TICKER --assess]` | Semi-automated earnings workflow. `--week` = earnings calendar + phase transition. `--phase` = quick phase transition check. `TICKER` = pre-earnings briefing (consensus, scenarios, KCs, decision tree). `TICKER --assess` = post-earnings assessment template with KC pass/fail. |
| `decision_feedback.py` | `python3 tools/decision_feedback.py [--buys\|--sells\|--fv-accuracy\|--patterns\|--ticker TICK]` | Meta-learning: connects past decisions to outcomes. FV calibration (gap vs market, toward/away), sell accuracy, conviction/QS-based returns, time-to-profit. |
| `pipeline_velocity.py` | `python3 tools/pipeline_velocity.py [--funnel\|--stale\|--history]` | Pipeline throughput metrics. Default = dashboard + bottleneck analysis. `--funnel` = conversion rates (universe→deployment). `--stale` = stuck candidates. `--history` = velocity units per session. Fantasy rate tracking. |

## Screening & Valuation

| Tool | Comando | Proposito |
|------|---------|-----------|
| `dynamic_screener.py` | `python3 tools/dynamic_screener.py --index {sp500\|us_all\|europe_all\|...}` | Screening programatico. Anti-bias. `--undiscovered` para small/mid. |
| `batch_scorer.py` | `python3 tools/batch_scorer.py --index {sp500\|...} [--new-only] [--add-to-universe] [--dry-run]` | Mass QS scoring de indices enteros. Discovery. Auto-add a universe. |
| `dcf_calculator.py` | `python3 tools/dcf_calculator.py TICKER [--scenarios] [--sensitivity] [--reverse]` | DCF + scenarios + sensitivity. --reverse = implied expectations (solve for growth). |
| `narrative_checker.py` | `python3 tools/narrative_checker.py TICKER` | Tendencias financieras (margins, R&D, SBC, receivables, FCF). Datos crudos. |
| `opportunity_filter.py` | `python3 tools/opportunity_filter.py --csv FILE [--roic-min N]` | Stage 2 sobre CSV de screener. ROIC, FCF margin, rev CAGR. |

## Ownership & Institutional Intelligence

| Tool | Comando | Proposito |
|------|---------|-----------|
| `ownership_graph.py` | `python3 tools/ownership_graph.py [--portfolio-only] [--top-funds N]` | Interactive force-directed graph: stocks ↔ funds/insiders. Output: docs/ownership_graph.html. |
| `ownership_analyzer.py` | `python3 tools/ownership_analyzer.py [--risk\|--sentiment\|--discover [TICKERS]]` | Institutional intelligence: overlap matrix, insider sentiment, smart money discovery. `--discover` checks pipeline candidates vs quality funds. |
| `risk_heatmap.py` | `python3 tools/risk_heatmap.py [--cached\|--diff]` | Interactive HTML heatmap: 7 risk dimensions per position. Caches ownership snapshots for temporal diff. Output: docs/risk_heatmap.html. |
| `ownership_cache.py` | `python3 tools/ownership_cache.py [--portfolio\|--all\|--pipeline\|--status\|--fresh] [TICKERS]` | Shared ownership data layer. `--pipeline` adds top 20 universe candidates by QS. All ownership tools use this cache. |
| `command_center.py` | `python3 tools/command_center.py [--fresh]` | Session-start command center: KPIs + risk matrix + calendar + SOs + insider sentiment + pipeline funnel. Single interactive HTML. Output: docs/command_center.html. |

## Macro & Risk

| Tool | Comando | Proposito |
|------|---------|-----------|
| `macro_fragility.py` | `python3 tools/macro_fragility.py {world\|country CODE\|sector NAME\|full}` | 3-layer macro data: world (VIX, yields, gold, oil, DXY, S&P), country (index, FX, ETF, sector ETFs), sector (ETFs, P/E, top holdings). Datos crudos. |

## Sector Health & Consistency

| Tool | Comando | Proposito |
|------|---------|-----------|
| `sector_health.py` | `python3 tools/sector_health.py {freshness\|coverage\|cascade\|changes\|snapshot\|macro-map}` | Staleness, coverage, cascades, macro deps de sector views. `freshness --stale-only` para alertas. Weekly obligatorio. |
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
