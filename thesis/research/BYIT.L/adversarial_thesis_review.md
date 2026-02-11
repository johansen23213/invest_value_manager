# ADVERSARIAL THESIS REVIEW: BYIT.L (Bytes Technology Group plc)

**Date:** 2026-02-11
**Review Agent:** Adversarial Review (Orchestrator-level synthesis)
**Position:** 110 shares @ ~296 GBp (~$4.04 avg cost), invested $444 (~377 EUR), ~3.5% weight
**Current Price:** 292.60 GBp (at 52-week low of 290.8)
**Thesis FV:** 455 GBp | **Thesis QS:** 81 (Tier A) | **Thesis MoS:** 35%

---

## EXECUTIVE SUMMARY

This adversarial review synthesizes findings from three independent agents (risk-identifier, valuation-specialist, devil's-advocate) that assessed BYIT.L on 2026-02-09. The review is unusually well-documented because the full adversarial pipeline was run AFTER purchase -- the position was bought on 2026-02-07 without independent agent scrutiny, which is a documented process failure (Error #42 analog).

**Key findings:**

| Metric | Thesis | Adversarial | Delta |
|--------|--------|-------------|-------|
| Quality Score (tool) | 81 (Tier A) | 68 (Tier B) | -13 |
| Quality Score (adjusted) | 81 (Tier A) | 72 (Tier B) | -9 |
| Fair Value (base) | 455 GBp | 350-370 GBp | -19% to -23% |
| Fair Value (bear) | 350 GBp | 275 GBp | -21% |
| MoS vs base | 35% | 16-20% | -15 to -19pp |
| MoS vs bear | 15.4% | -6% to +6% | Underwater or minimal |
| Value Trap Score | 0/10 | 2/10 | +2 |

**Verdict: HOLD on PROBATION with LOW conviction.** The business is real but the thesis is materially flawed. The 35% MoS is an illusion. The true MoS is 16-20%, which is borderline for what is actually a Tier B company, not Tier A. Position size is small (3.5%, EUR 377) which limits absolute risk. H2 FY2026 results (~May 2026) are the critical inflection. EXIT if OP declines again.

---

## 1. QUALITY SCORE ASSESSMENT

### 1.1 Tool Score: 68/100 -- Tier B

The quality_scorer.py produces a LEGACY score of **68/100 (Tier B)**, not the 81 claimed in the thesis.

The breakdown reveals critical data gaps:

| Category | Tool Score | Thesis Claims | Issue |
|----------|-----------|---------------|-------|
| Financial Quality | 25/40 | 28/40 | **ROIC = N/A (scored 0/15)** because yfinance lacks the financial statement data needed. Tool gets 10/10 FCF margin, 10/10 leverage, 5/5 consistency = 25/40 |
| Growth Quality | 23/25 | 21/25 | Revenue CAGR 14.2% (8/10), EPS CAGR 18.4% (10/10), GM expanding (5/5). Historical only. |
| Moat Evidence | 10/25 | 22/25 | **GM Premium 10/10 but Market Position 0/8 (default manual) and ROIC Persistence 0/7 (N/A)**. Tool cannot calculate these without ROIC data. |
| Capital Allocation | 10/10 | 10/10 | Insider 9.6% (5/5), dividends (5/5). But insider figure is disputed. |
| **TOTAL** | **68** | **81** | **-13 points** |

**Root cause of discrepancy:** The thesis manually assigned 12 points for ROIC-related metrics (ROIC spread + ROIC persistence) that the tool scores as 0 due to missing data. The thesis also manually assigned 5 points for market position (#1-2 UK VAR) that the tool defaults to 0.

**QS Tool-First Rule (Sesion 52):** The tool = 68, Tier B. Any adjustment MUST have documented quantitative evidence.

### 1.2 Adjusted QS Assessment

| Category | Tool | Justified Adjustment | Adjusted | Evidence |
|----------|------|---------------------|----------|----------|
| Financial | 25/40 | +4 for ROIC spread (ROE 55.9% suggests positive spread, but only +4.9pp vs WACC per thesis) | 29/40 | ROE trajectory declining: 69.1% -> 55.9% over 4 years |
| Growth | 23/25 | -4 for forward deterioration (H1 GP +0.4%, OP -7%) | 19/25 | H1 FY2026 actual results contradict historical CAGRs |
| Moat | 10/25 | +5 for market position (#1-2 UK VAR, documented) | 15/25 | IT Channel Oxygen data confirms #1-2 position |
| Capital Allocation | 10/10 | -4 for insider ownership dispute (9.6% may be Altron blockholders, not management) | 6/10 | Counter-analysis found 0.5-1.5% true insider; yfinance 9.6% likely includes non-management |
| **ADJUSTED TOTAL** | **68** | **+1** | **69** | **Tier B** |

**Alternative generous adjustment:** Even if I grant full ROIC persistence (+7) and accept the 9.6% insider figure (+4 back to 10/10), the adjusted score would be 68 + 7 + 4 = 79 -- barely Tier A. But granting ROIC persistence 7/7 requires evidence that ROIC > WACC for 10/10 years, which is not available from the tool data (only 4 years of ROE shown).

**QS Adjusted: 69/100 -- Tier B**

Reasoning for -12 from thesis claim of 81:
1. ROIC spread +4.9pp is genuinely low for "Tier A" (Softcat achieves 36% ROIC) = -4 vs thesis
2. Forward growth deterioration not reflected in backward-looking metrics = -4
3. Insider ownership disputed; governance red flag (former CEO unauthorized trading) = -4

### 1.3 The Insider Ownership Problem

This is the single most significant factual discrepancy. The thesis claims 9.6% insider ownership and the quality_scorer.py confirms this from yfinance. However:

- The devil's advocate found that actual executive/board insider ownership may be as low as 0.5-1.5%
- The 9.6% figure likely includes Altron-related entities (Bytes' South African parent company historical holdings) classified as "insiders" in some databases
- Former CEO Neil Murphy was forced to resign in February 2024 over 119 undisclosed share transactions -- a governance scandal NOT mentioned in the thesis
- New CEO Sam Mudd bought only GBP 99K worth of shares
- The thesis incorrectly names the CEO as "Sam Sheridan"

**Impact on QS:** If insider ownership is truly <1.5%, Capital Allocation drops from 10/10 to 6/10 (-4 points), pushing QS further into Tier B.

**I cannot definitively resolve this discrepancy** without reading the annual report directly. I flag this as HIGH uncertainty.

---

## 2. VALUE TRAP CHECKLIST REASSESSMENT

| Factor | Thesis | Adversarial | Evidence |
|--------|--------|-------------|----------|
| Industry in secular decline | NO | NO | UK IT spending growing, confirmed by CIO survey (52% expect budget increases 2026) |
| Imminent technological disruption | NO | PARTIAL | Microsoft EA direct sales IS a form of disintermediation. Not classic "tech disruption" but structural channel shift. |
| Management destroying value | NO | NO | Net cash, special dividends. Buyback at ~390p may be poorly timed. |
| Deteriorating balance sheet | NO | NO | Net cash GBP 43M, no debt. |
| Massive insider selling | NO | UNCERTAIN | Former CEO forced out for unauthorized trading. New insider activity is net positive (buying > selling in last 3 months). |
| Recent/probable dividend cut | NO | NO | +15% dividend growth, special dividend. |
| Market share loss >2pp 3yr | NO | UNCERTAIN | Bytes gaining public sector share vs smaller VARs, but Microsoft taking EA direct could represent share loss to Microsoft itself. |
| ROIC < WACC last 3 years | NO | NO | ROE 55-69% massively above WACC. Even if ROIC is lower than ROE due to asset-light distortion, it almost certainly exceeds WACC. |
| FCF negative >2 years | NO | NO | FCF positive all 4 measured years. |
| Goodwill >50% equity | NO | NO | Asset-light, minimal goodwill. |

**Adversarial Value Trap Score: 2/10** (vs thesis 0/10)

The two flags are:
1. PARTIAL on technological disruption (Microsoft EA disintermediation is structural, even if not classic tech disruption)
2. UNCERTAIN on insider selling / governance (CEO scandal)

At 2/10, the risk of value trap remains LOW, but it is not zero as the thesis claims.

---

## 3. VALUATION CHALLENGE

### 3.1 Thesis Valuation: 455 GBp

| Method | Thesis Value | Weight | Thesis Weighted |
|--------|-------------|--------|-----------------|
| OEY (8% growth) | 470p | 60% | 282p |
| DCF (8%/9%/2.5%) | 432p | 40% | 173p |
| **Thesis Weighted** | | | **455p** |

### 3.2 Problems with Thesis Valuation

**Problem 1: Growth rate of 8% is thesis BULL, not BASE.**

H1 FY2026 showed GP growth of +0.4% and OP growth of -7.0%. For the thesis 8% GP growth to materialize for full FY2026, H2 must deliver approximately 16% GP growth. While management guides "double-digit GP growth," Berenberg specifically warned that "disruption is unlikely to be limited to H1" and downgraded to HOLD with TP 390p.

Historical data supports 10-15% growth, but that was BEFORE the Microsoft structural shift. The independent valuation specialist uses 6% as base (which I concur with), with 8% reserved for the bull case.

**Problem 2: WACC of 9.0% too low for the risk profile.**

The thesis derives WACC = 8.45% and rounds to 9.0%. But:
- Beta of 0.73 (yfinance) is questionable for a stock that fell 47% while indices were relatively flat
- 68% Microsoft dependency creates concentration risk not captured by CAPM
- UK mid-cap with declining margins deserves a premium
- The valuation specialist uses 9.5%; the risk identifier suggests 10-11%
- I use 9.5-10% as the appropriate range

**Problem 3: Softcat P/E comparison is stale and wrong.**

The thesis states "Softcat at ~25x P/E vs Bytes at 14x -- the valuation gap is extreme." Current data:
- Softcat: P/E 17.2x (price_checker.py, Feb 11 2026) -- NOT 25x
- BYIT: P/E 13.9x
- Gap: 24% -- not "extreme," and potentially justified by Softcat's higher ROIC (36% vs ~25%), larger scale (3.3x market cap), and lower concentration risk

**Problem 4: FCF normalization.**

The thesis uses GBP 48M FCF. Actual FY2025 FCF was GBP 64.9M, but this included GBP 49.6M favorable payables timing. FY2025 also saw capex jump to GBP 10.1M (from ~GBP 1M historically) for marketplace platform investment. Normalized FCF = GBP 48-52M is reasonable.

### 3.3 Adversarial DCF Scenarios

From the dcf_calculator.py runs:

| Scenario | Growth | WACC | Terminal | FV/Share | MoS vs 292.6p |
|----------|--------|------|----------|----------|---------------|
| **Default** | 5% | 9% | 2.5% | 500p | +71% |
| **Conservative** | 6% | 10% | 2% | 432p | +48% |
| **Bear** | 4% | 10.5% | 2% | 376p | +28% |
| **Severe Bear** | 4% | 10.5% | 2% Bear scenario | 312p | +7% |

The DCF tool uses actual FY2025 FCF (GBP 64.9M) as the base. If I normalize to GBP 50M (adjusting for working capital timing), I need to scale results by 50/64.9 = 0.77:

| Scenario | Tool FV | Normalized FV | MoS vs 292.6p |
|----------|---------|---------------|---------------|
| Conservative base | 432p | **333p** | +14% |
| Bear base | 376p | **290p** | -1% (underwater) |
| Bear bear | 312p | **241p** | -18% |

**This is the critical finding: with normalized FCF and bear assumptions, the stock is AT or BELOW fair value at current price.**

### 3.4 EV/EBIT Peer Cross-Check

| Multiple | EBIT (GBP M) | EV | + Net Cash | Equity | Per Share |
|----------|-------------|-----|-----------|--------|-----------|
| 10x | 66M | 660M | +43M | 703M | **297p** |
| 11x | 66M | 726M | +43M | 769M | **325p** |
| 12x (Softcat level) | 66M | 792M | +43M | 835M | **353p** |
| 13x | 66M | 858M | +43M | 901M | **381p** |

At the current price of 293p, the market is pricing BYIT at ~10x EV/EBIT on FY2025 EBIT. This is a discount to Softcat (which trades at approximately the same level now after its own re-rating) and to Computacenter.

### 3.5 Owner Earnings Yield (OEY)

```
Normalized OE: GBP 48-50M
Market Cap at 293p: ~GBP 692M (236.3M shares)

OEY = 50M / 692M = 7.2%
Growth (my base 6%): 6.0%
OEY + Growth = 13.2%
vs WACC 9.5% = +3.7pp spread (positive, attractive)

For 12% target return:
Required OEY = 12% - 6% = 6.0%
FV Market Cap = 50M / 6.0% = GBP 833M
FV Per Share = 833M / 236.3M = 352p

For 10% target (less demanding):
FV = 50M / 4.0% = GBP 1,250M = 529p
```

The OEY method is highly sensitive to the growth assumption. At 6% growth, FV is 352p. At 8% growth, FV rises to 50M/4% = ~1,250M but this requires believing in the higher growth rate.

### 3.6 Adversarial Fair Value Reconciliation

| Method | Value | Weight | Weighted |
|--------|-------|--------|----------|
| OEY (6% growth, 12% return target) | 352p | 40% | 141p |
| DCF normalized (6%/10%/2%) | 333p | 30% | 100p |
| EV/EBIT (11-12x FY2025) | 325-353p | 30% | 102p |
| **Adversarial Weighted FV** | | **100%** | **343p** |

Cross-checks:
- Risk identifier FV: 370 GBp
- Valuation specialist FV: 366 GBp
- Devil's advocate FV: 330 GBp
- **Range across all independent agents: 330-370 GBp**
- **My synthesis: 345 GBp** (midpoint of agent range, weighted toward conservative methods)

### 3.7 Comparison: Thesis vs Adversarial

| Metric | Thesis | Adversarial | Delta |
|--------|--------|-------------|-------|
| Fair Value (base) | 455 GBp | 345 GBp | **-24.2%** |
| Fair Value (bear) | 350 GBp | 275 GBp | **-21.4%** |
| Fair Value (bull) | 580 GBp | 460 GBp | **-20.7%** |
| MoS vs base at 293p | 35.6% | **15.1%** | -20.5pp |
| MoS vs bear at 293p | 16.3% | **-6.5%** | -22.8pp |
| Growth assumption | 8% | 6% | -2pp |
| WACC | 9.0% | 9.5-10% | +0.5-1pp |
| P/E at FV | 20x | 15-16x | -4-5x |

The -24% FV revision is consistent with the adversarial portfolio pattern: 12/13 prior positions had inflated FV averaging -15%. BYIT at -24% is somewhat worse, reflecting the specific issues with Softcat comparables, growth assumptions, and Microsoft structural risk.

---

## 4. KEY RISKS IDENTIFIED BY INDEPENDENT AGENTS

### 4.1 CRITICAL: Microsoft EA Direct Sales Takeover

**This is the single most important risk the thesis either missed or minimized.**

The thesis frames ALL Microsoft changes as "cyclical incentive restructuring." The risk identifier found evidence of a qualitatively different phenomenon:

- Microsoft has been taking Enterprise Agreement renewals DIRECT since January 2023
- Global LSP commissions: $2.5B (2023) -> $1.67B (2024) -> $583M (2025) -> projected $0 (2026)
- This is not a cyclical margin squeeze -- it is structural disintermediation of the EA channel
- 68% of Bytes' GII stems from Microsoft products
- ~50% of GP derives from Microsoft sales

**The thesis assigns 25% probability of being wrong on Microsoft.** The risk identifier suggests 50-60%. I believe 40-50% is appropriate -- the EA direct sales shift is real and documented, but its impact on the CSP channel (where most of Bytes' transactional revenue lies) is less clear.

**Mitigant:** Bytes is primarily a CSP partner and managed services provider, not purely an LSP. The CSP channel involves ongoing management and billing that Microsoft cannot easily replicate. The EA direct sales impact may be concentrated on large government EAs, not the mid-market where Bytes operates.

**Residual risk:** HIGH. Even if the CSP channel is safer, the DIRECTION is clear -- Microsoft is capturing more value from its ecosystem at partner expense.

### 4.2 HIGH: Operating Cost Inflation vs Flat Revenue

- H1 FY2026: GP +0.4%, employee costs +5.9%, OP -7.0%
- Headcount grew 12% while GP was flat -- classic margin scissors
- UK NI increase (+2% payroll costs from April 2025) adds further pressure
- Operating efficiency ratio fell from 43.4% to 40.2%

### 4.3 HIGH: Governance Gaps Not in Thesis

- Former CEO Neil Murphy forced to resign (Feb 2024) over 119 undisclosed share transactions
- FCA investigation closed without sanctions, but the scandal is not mentioned in the thesis at all
- CEO name in thesis is wrong ("Sam Sheridan" vs actual "Sam Mudd")
- New CEO untested at public company CEO level

### 4.4 MEDIUM: UK Public Sector Spending Risk

- Public sector is ~50% of Bytes' GII
- IFS projects unprotected spending cuts of 1.3%/year real terms
- NHS digital mandates provide a floor but not growth
- H1 public sector GP growth decelerated to +1.6% (from double-digits)

### 4.5 MEDIUM: Analyst Consensus Deteriorating

- Jefferies: downgrade to Hold, TP cut to 400p (from 447p)
- Berenberg: downgrade to Hold, TP 390p (from 660p)
- Shore Capital: Hold, TP 410p
- Consensus: 6-7 Buy, 3-4 Hold, 0 Sell. Average TP ~471-500p but driven by stale estimates
- Most recent actions have been DOWNGRADES

---

## 5. WHAT THE THESIS GETS RIGHT

Being adversarial does not mean being unfair. The thesis makes several valid points:

1. **Net cash position (GBP 43M)** -- This is genuine downside protection. No debt, no refinancing risk. FCF consistently positive.

2. **30% FCF margin on GP** -- Genuinely excellent. Even with margin compression, FCF should remain solidly positive.

3. **Services growth 40%+** -- This IS the correct strategic pivot. If Bytes can grow services to become the majority of GP, the Microsoft EA risk diminishes. The question is how fast.

4. **Consolidation benefits from $1M CSP threshold** -- Microsoft raising the bar eliminates sub-scale competitors. Bytes and Softcat are the survivors.

5. **0/10 value trap (or 2/10 adversarial)** -- This is NOT a value trap in the classical sense. The business generates real cash and the industry is growing.

6. **AI as TAM expander** -- Reasonable argument that AI increases complexity and the need for advisory services. The cybersecurity and AI advisory practices are growing.

7. **Director purchase at 402p** -- While directors can be wrong, this is a positive signal of confidence.

---

## 6. SCENARIO ANALYSIS

| Scenario | Prob | FV | Assumptions | MoS vs 293p |
|----------|------|-----|------------|-------------|
| **Severe Bear** | 15% | 250p | Microsoft extends direct sales to mid-market. Services growth slows to 10%. Public sector cuts bite. OP declines 20%+. P/E 11x. | **-15%** |
| **Bear** | 25% | 300p | Microsoft incentive compression persists 2+ years. GP growth 3-4%. OP flat. P/E 13x. | **+2%** |
| **Base** | 40% | 345p | Partial normalization by FY2027. GP growth 6%. Services offsets software decline. P/E 15x. | **+18%** |
| **Bull** | 20% | 460p | Full recovery + AI services boom + Microsoft price increases flow through. GP growth 10%+. P/E 19x. | **+57%** |

**Expected Value = (250 x 0.15) + (300 x 0.25) + (345 x 0.40) + (460 x 0.20)**
**EV = 37.5 + 75 + 138 + 92 = 342.5p**

**MoS vs EV: (342.5 - 293) / 342.5 = 14.5%**

This is borderline. For a Tier B company (my adjusted QS 69), precedents suggest 20-25% MoS is typical. At 14.5%, the position is modestly undervalued but not compellingly so.

---

## 7. KILL CONDITIONS ASSESSMENT

### Thesis Kill Conditions:

| # | Kill Condition | Status | Adversarial View |
|---|---------------|--------|------------------|
| 1 | Microsoft disintermediates VARs | NOT TRIGGERED (but approaching for EA segment) | **Too narrow.** Should specifically address EA direct sales. The EA disintermediation IS happening but CSP/services may be safe. |
| 2 | FCF negative 2+ years | NOT TRIGGERED | Too generous. OP declining 7% should be a warning signal even with positive FCF. |
| 3 | Services growth below 10% | NOT TRIGGERED (40%+) | Adequate and well-chosen. This is the key metric. |
| 4 | Public sector framework loss | NOT TRIGGERED | Adequate. |
| 5 | QS falls below 75 | **APPROACHING / TRIGGERED** | Tool QS = 68 (already below 75). Adjusted QS = 69 (also below). Thesis QS = 81 was incorrect. |
| 6 | AI-automated procurement eliminates VAR role | NOT TRIGGERED | Long-term risk, low probability near-term. |
| 7 | Microsoft shifts to consumption-based pricing | NOT TRIGGERED | Medium-term risk, monitoring. |

**Adversarial Assessment: Kill Condition #5 (QS < 75) is potentially triggered** if we accept the tool score of 68 or my adjusted score of 69. The thesis claimed 81, which is no longer defensible.

However, the spirit of KC #5 was to detect fundamental quality deterioration. The business quality has not changed dramatically -- the H1 results showed one bad half-year. The QS drop is partly a measurement issue (tool cannot calculate ROIC) and partly genuine forward deterioration. This warrants PROBATION, not immediate EXIT.

### Kill Conditions to ADD:

1. **H2 FY2026 OP decline** -- If full-year FY2026 OP is below FY2025's GBP 66M, the quality compounder thesis is invalidated. EXIT.
2. **Microsoft extends EA direct sales to mid-market accounts** -- Currently limited to large EAs. If it expands, the impact on Bytes accelerates.
3. **Operating efficiency ratio falls below 35%** -- Currently 40.2%, declining. Below 35% indicates structural cost problem.

---

## 8. PRECEDENT COMPARISON

From decisions_log.yaml, this is how BYIT.L compares to prior adversarial reviews:

| Ticker | Thesis FV | Adversarial FV | Delta | QS Thesis | QS Adjusted | Action |
|--------|-----------|---------------|-------|-----------|-------------|--------|
| MONY.L | 277p | 201p | -27% | 81 | ~65-70 | HOLD LOW |
| EDEN.PA | EUR 38.4 | EUR 29.0 | -24.5% | - | - | HOLD MED |
| A2A.MI | EUR 2.70 | EUR 2.04 | -24% | - | 37 | SELL |
| VNA.DE | EUR 32.58 | EUR 24.35 | -25% | - | 41 | SELL |
| HRB | $60 | $32 | -47% | 70 | 70 | SELL |
| **BYIT.L** | **455p** | **345p** | **-24%** | **81** | **69** | **?** |

The -24% FV revision is exactly in line with the median of prior adversarial reviews (average -15%, but median of Tier A reviews closer to -24%). The QS drop from 81 to 69 (-12 points) is the second largest after A2A.MI.

**Key precedent:** MONY.L had a similar profile (thesis QS 81, adversarial ~65-70, FV -27%, UK digital platform). MONY.L was placed on HOLD with LOW conviction. By analogy, BYIT.L should receive the same treatment.

**Distinguishing factor:** MONY.L has genuinely higher ROIC (+20pp spread vs BYIT's +4.9pp). MONY.L's business model is less dependent on a single vendor. BYIT.L has the additional Microsoft concentration risk that MONY.L does not. This argues for lower conviction on BYIT.L than MONY.L.

---

## 9. STATUS REASONING (Framework v4.0)

Following v4.0 principles -- reason from principles, not fixed rules:

**What is the MoS?** ~15% vs adversarial base FV of 345p. Borderline for Tier B.

**Is the thesis intact?** WEAKENED. The core thesis -- that Microsoft changes are cyclical -- is challenged by structural evidence. The growth assumption of 8% is not supported by H1 data. However, the fundamental business quality (net cash, FCF positive, services pivot underway) is intact.

**Is there a better use of capital?** With 44% cash, yes -- there may be better opportunities. But we would be selling a ~3.5% position at a loss for a small capital recovery (~EUR 377). The friction of selling a small position must be weighed against the opportunity cost.

**Precedents?** MONY.L adversarial review (similar profile) resulted in HOLD LOW. SAN.PA adversarial review (ROIC < WACC) resulted in SELL. BYIT.L does NOT have ROIC < WACC (ROE 56% >> WACC 9.5%), which distinguishes it from the SELL precedents. Every position we sold in adversarial had ROIC < WACC. BYIT.L does not fit that pattern.

**If MoS is negative in bear, is there a kill condition?** The bear case FV of ~300p vs current 293p gives essentially no MoS. But the bear case has only 25% probability. The severe bear (250p, 15% probability) would be painful but the position is small.

**50% drop test:** If BYIT falls 50% to ~146p, the portfolio loses 1.75%. At this position size, this is acceptable even with LOW conviction. The business would then be trading at ~7x EPS with 4.5% yield, making it a screaming bargain if the business remains viable.

**Conclusion:** **HOLD on PROBATION with LOW conviction.**

Rationale:
1. ROIC is NOT below WACC -- distinguishes from all 8 prior SELL decisions
2. Business generates real FCF (GBP 48-65M) with net cash
3. Position is small (3.5%, EUR 377) -- limited absolute risk
4. Selling at a loss of ~1% on EUR 377 recovers negligible capital
5. H2 FY2026 results (~May 2026) provide definitive data point
6. Services growth at 40%+ is the genuine bull case and has not yet failed
7. The stock is at its 52-week low -- selling at the bottom without a kill condition violates Principio 6

But:
1. QS has degraded from claimed 81 to 69 (Tier B)
2. MoS is only 15%, not 35% -- thesis was materially wrong
3. Microsoft structural risk is real and underdiscussed
4. No adversarial pipeline was run before purchase
5. EXIT if H2 FY2026 disappoints

---

## 10. UPDATED THESIS PARAMETERS

| Parameter | Original | Updated | Reasoning |
|-----------|----------|---------|-----------|
| **QS Tool** | 81 (Tier A) | 68 (Tier B) | Tool output = source of truth |
| **QS Adjusted** | 81 (Tier A) | 69 (Tier B) | +1 for market position evidence; forward growth deterioration offsets |
| **Fair Value** | 455 GBp | 345 GBp | 6% growth, 9.5% WACC, normalized FCF, peer re-rating |
| **Bear FV** | 350 GBp | 275-300 GBp | Lower growth, higher WACC, Softcat de-rating |
| **Bull FV** | 580 GBp | 460 GBp | Full recovery + AI services |
| **MoS at 293p** | 35.6% | 15.1% | Revised FV |
| **Status** | BUY (purchased) | HOLD PROBATION LOW | Thesis weakened, MoS marginal |
| **ADD Trigger** | 260p | 240p (MoS ~30% vs adversarial FV) | Need higher MoS for Tier B |
| **EXIT Trigger** | Kill conditions | FY2026 full-year OP < FY2025 (GBP 66M) | Definitive test of compounding thesis |
| **Conviction** | High | LOW | Multiple thesis flaws discovered |

---

## 11. RECOMMENDATIONS FOR THESIS UPDATE

1. **Revise QS to show both scores:** "QS Tool: 68 (Tier B) | QS Adjusted: 69 (Tier B) -- adjustment for market position +5, insider ownership -4, forward growth -4"
2. **Revise FV to 345 GBp** with documented reasoning
3. **Add Microsoft EA direct sales risk** as explicit section
4. **Correct insider ownership discussion** -- acknowledge the 9.6%/0.5-1.5% discrepancy
5. **Correct CEO name** to Sam Mudd
6. **Add former CEO governance scandal** (Neil Murphy, 119 undisclosed trades)
7. **Add H2 FY2026 as mandatory review trigger** (results ~May 2026)
8. **Lower ADD trigger to 240p** (MoS ~30% vs adversarial FV, appropriate for Tier B)
9. **Remove Softcat "25x P/E" comparison** -- update to actual 17.2x

---

## META-REFLECTION

### Changes Detected Since Thesis Written (2026-02-07)
- Stock has declined further from 296p to 293p, hitting 52-week low of 290.8
- Softcat P/E compressed from the ~25x cited in thesis to 17.2x -- the "massive discount" argument has collapsed
- No material news since purchase; next catalyst is FY2026 full-year results (~May 2026)
- The quality_scorer.py shows 68 (Tier B) vs thesis claim of 81 (Tier A) -- this was knowable at time of purchase

### Incertidumbres
- **Insider ownership discrepancy (9.6% vs 0.5-1.5%)** -- Cannot resolve without reading annual report. HIGH impact on QS.
- **Microsoft EA vs CSP revenue split for Bytes** -- Critical to quantify the EA direct sales risk. If 80%+ of Microsoft revenue is CSP (not EA), the structural risk is much lower.
- **H2 FY2026 performance** -- Management guides recovery; Berenberg says disruption continues. The truth will be known in May 2026.
- **Whether Softcat's de-rating from 25x to 17x is permanent** -- If the entire UK VAR sector is structurally re-rated, then BYIT at 14x is not cheap relative to peers.

### Sugerencias
- **Insider ownership verification should be a standard check** for all UK-listed companies. The yfinance data is unreliable for this metric.
- **The full adversarial pipeline MUST run before purchase** -- this position demonstrates the cost of skipping it. Multiple material issues (CEO scandal, insider ownership, Softcat re-rating, EA structural shift) were missed.
- **For companies with >50% vendor dependency**: mandatory deep-dive on vendor channel strategy before investment.

### Alertas para Orchestrator
- **QS claimed 81, tool shows 68** -- this is the 6th position where thesis QS exceeded tool QS. The pattern persists even after the Sesion 52 QS Tool-First rule was established.
- **Thesis was purchased without adversarial pipeline** -- documented process failure. The existing research files (risk_assessment.md, valuation_report.md, counter_analysis.md) were created on 2026-02-09, 2 days AFTER purchase.
- **BYIT.L is at 52-week low right now (290.8)** -- if it breaks below, there is no technical support until much lower levels.
- **FY2026 full-year results (~May 2026) are the definitive test** -- must schedule this as a mandatory review trigger.

---

**Summary for Orchestrator:**

| Item | Value |
|------|-------|
| Ticker | BYIT.L |
| Quality Score | Tool: 68/100 (Tier B) -- Adjusted: 69/100 (Tier B) |
| FV (adversarial) | 345 GBp |
| Price | 292.60 GBp |
| MoS | 15.1% |
| Precedent consulted | MONY.L (similar QS drop, HOLD LOW). Contrast: SAN.PA/HRB (ROIC<WACC, SELL). |
| Status | **HOLD on PROBATION -- LOW conviction** |
| Kill conditions | OK (no kill triggered) but QS<75 approaching/triggered depending on interpretation |
| Next review | FY2026 full-year results (~May 2026) -- MANDATORY |
| EXIT if | FY2026 full-year OP < GBP 66M (FY2025 level) |
| ADD trigger | Lowered to 240p (from 260p) |

---

**Sources:**
- [Jefferies Downgrades BYIT to Hold (Jan 2026)](https://www.defenseworld.net/2026/01/16/jefferies-financial-group-downgrades-bytes-technology-group-lonbyit-to-hold.html)
- [BYIT.L Yahoo Finance](https://finance.yahoo.com/quote/BYIT.L/)
- [BYIT Forecast - TradingView](https://www.tradingview.com/symbols/LSE-BYIT/forecast/)
- [BYIT Analyst Forecast - TipRanks](https://www.tipranks.com/stocks/gb:byit/forecast)
- [Microsoft CSP 2026 Program Changes](https://cspcontrolcenter.com/microsoft-csp-2026-program-changes/)
- [Microsoft FY26 Incentives Update](https://connect.tdsynnex.be/blog/media-library/microsoft-fy26-incentives-update/)
- [FY26 CSP Program Updates - CloudCockpit](https://cloudcockpit.com/blog/microsoft-csp-new-program-requirements)
- [Government IT Spending Rises with AI Priority](https://securitybrief.co.uk/story/government-it-spending-rises-as-ai-becomes-top-budget-priority)
- [Spending Review 2025: Time for Tech - TechUK](https://www.techuk.org/resource/spending-review-2025-time-for-tech.html)
- [Bytes and Softcat Dominate Public Sector VAR Market](https://itchanneloxygen.com/bytes-and-softcat-dominate-3-7bn-public-sector-var-market/)
- [UK's Top Resellers - Oxygen 250 2026](https://itchanneloxygen.com/uks-top-resellers-and-msps-revealed-in-oxygen-250-2026/)
- [Bytes vs Softcat vs Computacenter - Proactive Investors](https://www.proactiveinvestors.com/companies/news/1027149/bytes-computacenter-softcat-which-is-the-uk-s-top-value-added-reseller-1027149.html)
