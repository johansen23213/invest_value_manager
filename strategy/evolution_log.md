# Strategy Evolution Log

## Current Strategy: Value + Quality v1.0
- **Base**: Classic value (P/E, P/B, yield, margin of safety)
- **Added**: Quality filters (moat, ROIC, debt levels)
- **Screening**: dynamic_screener.py (programmatic, anti-bias)
- **Status**: ACTIVE since 2026-01-26
- **Next review**: 2026-02-28 (monthly per Protocol 7)

## Strategy Backlog (prioritized per Protocol 7)

### HIGH PRIORITY (next sessions)
- [ ] Correlation matrix of current portfolio → reduce if >0.7
- [ ] Factor exposure analysis → what am I really exposed to?
- [ ] Stress test: portfolio in 2008, 2020, 2022 scenarios
- [ ] Value + Momentum 6m overlay → backtest if reduces drawdown

### MEDIUM PRIORITY
- [ ] Insider buying as confirmation filter
- [ ] Dividend growth rate > static yield
- [ ] Relative value intra-sector (cheapest pharma vs all pharma)
- [ ] Volatility-adjusted position sizing

### LOW PRIORITY
- [ ] Pair trading within sectors
- [ ] Macro regime detection (risk-on/risk-off)
- [ ] Seasonal patterns (verify with data before adopting)
- [ ] Geographic arbitrage (same business, different market price)

### EXPLORATORY
- [ ] Post-earnings drift at value prices
- [ ] Spin-off outperformance (historical data)
- [ ] Special situations screening automation

## Explorations Done
| Date | Sector/Geo | Method | Findings |
|------|-----------|--------|----------|
| 2026-01-30 | EU pharma, tobacco, insurance | screener.py (hardcoded) | Found TEP, IMB, VICI, Signify |
| 2026-01-31 | EU mid-caps | midcap_screener.py (hardcoded) | Deployed TEP, SAN, VICI, IMB, LIGHT |
| 2026-01-31 | CAC40, DAX, IBEX, SP500 | dynamic_screener.py (programmatic) | Tool validation - working |

## Unexplored Territories (rotate per Protocol 4)
- [ ] Japan (Nikkei 225 + mid-caps TSE)
- [ ] Nordic small-caps (Helsinki, Oslo, Copenhagen, Stockholm)
- [ ] Korean discount plays (KOSPI)
- [ ] Eastern Europe (Warsaw WIG20, Prague PX)
- [ ] Italian family businesses (Milan mid-caps)
- [ ] Australian resources/REITs (ASX)
- [ ] Singapore/HK REITs
- [ ] Canadian energy/midstream (TSX)
- [ ] Swiss industrials (SMI + mid-caps)
- [ ] Spin-offs last 12 months (any market)

## What Worked
(To be populated as positions mature - tracked per Protocol 7 Phase 1)

## What Failed / Discarded
| Date | Idea | Why discarded | Evidence |
|------|------|---------------|----------|
| 2026-01-31 | Hardcoded screener lists | Popularity bias - only found stocks I already knew | Replaced with dynamic_screener.py |

## System Evolution History (Protocol 6)
| Date | What changed | Why | Impact |
|------|-------------|-----|--------|
| 2026-01-31 | Created dynamic_screener.py | Hardcoded lists = biased | 610 EU tickers vs 90 before |
| 2026-01-31 | Added 7 operational protocols to CLAUDE.md | Vague rules weren't being executed | Concrete triggers + steps |
| 2026-01-31 | Created strategy/ directory | No structured strategy evolution | Backtests, monthly reviews, evolution log |
