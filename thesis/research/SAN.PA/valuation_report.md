# ADVERSARIAL VALUATION REPORT: Sanofi SA (SAN.PA)

**Date:** 2026-02-09
**Analyst:** Valuation Specialist (Independent Adversarial)
**Context:** Adversarial review of existing active position
**Price at Analysis:** EUR 80.36

---

## Company Classification

| Field | Value |
|-------|-------|
| Type of Enterprise | Large-cap European pharma, dividend aristocrat |
| Quality Score | 59 (Tier B) -- NOT Tier A as thesis claims |
| ROIC Spread | -2.1pp (NEGATIVE -- below WACC) |
| Key Characteristic | 36% revenue concentration in single drug (Dupixent) with 2031-2033 patent cliff |

**Methods Selected:** DCF with explicit cliff (primary) + DDM (secondary) + Forward P/E comparables (tertiary)

**Rationale for method selection:**
- DCF: Appropriate for Tier B pharma with material patent cliff requiring explicit year-by-year modeling
- DDM: Sanofi is a 26-year dividend aristocrat; the dividend is a significant value component
- Forward P/E: Cross-check using business EPS (IFRS EPS distorted by intangible amortization)
- EV/EBIT REJECTED: Amortization of pharma intangibles makes EBIT non-comparable across peers

---

## Critical Data Points

### Financial Summary (FY2024 Actual)

| Metric | Value | Source |
|--------|-------|--------|
| Revenue | EUR 44.29B | yfinance |
| Gross Profit | EUR 31.08B (70.2%) | yfinance |
| EBIT | EUR 7.45B | yfinance |
| EBITDA | EUR 11.03B | yfinance |
| Net Income | EUR 5.56B | yfinance |
| FCF | EUR 5.89B | yfinance |
| OCF | EUR 9.08B | yfinance |
| R&D | EUR 7.39B (16.7% of revenue) | yfinance |
| Net Debt | EUR 12.67B | dcf_calculator |
| Shares | 1.208B | yfinance |
| Dividend | EUR 3.92/share (EUR 4.74B total) | yfinance |
| EV | EUR 110.5B | yfinance |

### FCF Trend (DECLINING)

| Year | FCF | YoY |
|------|-----|-----|
| 2021 | EUR 8.48B | - |
| 2022 | EUR 8.42B | -0.7% |
| 2023 | EUR 7.35B | -12.7% |
| 2024 | EUR 5.89B | -19.9% |
| **CAGR 2021-2024** | **-11.4%** | **NEGATIVE** |

**CRITICAL FINDING #1:** The thesis uses EUR 8.1B as "base FCF" claiming it is FY2025 estimate. But the actual trend is DECLINING at -11.4% CAGR. yfinance reports freeCashflow of EUR 15.94B for TTM which appears to be an error or includes Opella divestiture proceeds. The 2024 actual FCF of EUR 5.89B is the reliable data point. The thesis FCF of EUR 8.1B requires a 37% jump from 2024 actuals -- possible but unverified.

### Dupixent Revenue Concentration

- Dupixent = ~36% of total revenue (~EUR 14B in 2025E)
- Growing to management target EUR 22B by 2030
- Patent cliff: composition of matter expires 2031; method patents to 2033
- Biosimilar entry expected 2032-2033
- This is THE critical risk for valuation

---

## METHOD 1: DCF with Explicit Dupixent Cliff (Weight: 40%)

### WACC Derivation

| Component | Thesis | My Calculation | Comment |
|-----------|--------|----------------|---------|
| Risk-Free Rate | 2.4% | 2.4% | German 10Y Bund, agreed |
| Beta | 0.65 ("pharma typical") | 0.37 (yfinance) | Thesis REJECTED actual beta without justification |
| ERP | 5.5% | 5.5% | Agreed |
| Ke (raw) | 5.98% (with 0.65 beta) | 4.44% (with 0.37 beta) | Material difference |
| Ke (Blume adj) | N/A | 5.59% (adj beta 0.58) | - |
| Kd after-tax | 3.0% | 2.96% | Agreed |
| E/V weight | 88.5% | 88.5% | Agreed |
| D/V weight | 11.5% | 11.5% | Agreed |
| **Calculated WACC** | **5.63%** | **5.3%** (raw) / **5.6%** (adj) | Similar |
| **Applied WACC** | **8.0% ("floor")** | **See below** | Major disagreement |

**WACC Assessment:**

The calculated WACC of 5.3-5.6% is mathematically correct but impractical for DCF (creates extreme terminal value sensitivity). The thesis applied an 8% "floor for established companies" which is arbitrary but directionally reasonable.

My approach: Use 7.0% for base case (calculated WACC + 1.5pp company-specific risk premium for patent cliff concentration). This is MORE conservative than calculated but LESS conservative than the arbitrary 8% floor.

- **Bear WACC:** 9.0% (adds macro uncertainty, execution risk)
- **Base WACC:** 8.0% (reasonable conservatism given cliff; I concede to thesis here)
- **Bull WACC:** 6.5% (closer to calculated, assumes pipeline replaces Dupixent)

**Beta Discussion:** The thesis rejected beta 0.37 as "too low" and used 0.65 instead. This is INCORRECT. Pharma betas are genuinely low: Roche 0.20, AZN 0.19, GSK 0.27, AbbVie 0.33, Novartis 0.46, PFE 0.44. SAN.PA at 0.37 is ABOVE the pharma median. Using 0.65 (which would be typical of an industrial) overstates the WACC. However, the practical effect is minor because both lead to WACC floors anyway.

### Explicit Cliff Revenue Model

**Assumptions by Scenario:**

| Parameter | Bear | Base | Bull |
|-----------|------|------|------|
| Dupixent peak (2030) | EUR 22B | EUR 22B | EUR 22B |
| Cliff erosion (cumulative by 2034) | 50% | 35% | 20% |
| Non-Dupixent growth | 3% | 4% | 5% |
| FCF margin | 15.5% | 17.5% | 19.5% |
| WACC | 9.0% | 8.0% | 6.5% |
| Terminal growth | 1.5% | 2.0% | 2.5% |

### Year-by-Year Projection (Base Case)

| Year | Dupixent | Non-Dupixent | Total Revenue | FCF |
|------|----------|--------------|---------------|-----|
| 2026 | 15.3B | 34.0B | 49.3B | 8.6B |
| 2027 | 16.8B | 35.4B | 52.1B | 9.1B |
| 2028 | 18.4B | 36.8B | 55.1B | 9.7B |
| 2029 | 20.1B | 38.3B | 58.4B | 10.2B |
| 2030 | 22.0B | 39.8B | 61.8B | 10.8B |
| 2031 | 19.8B | 41.4B | 61.2B | 10.7B (cliff begins) |
| 2032 | 18.1B | 43.0B | 61.2B | 10.7B |
| 2033 | 15.8B | 44.8B | 60.6B | 10.6B |
| 2034 | 14.3B | 46.5B | 60.8B | 10.6B |
| 2035 | 14.3B | 48.4B | 62.7B | 11.0B |

### DCF Results with Cliff

| Scenario | PV of FCFs | PV of Terminal | EV | Equity | FV/Share | MoS |
|----------|-----------|---------------|-----|--------|----------|-----|
| **Bear** | 54.4B | 48.7B | 103.1B | 90.4B | **EUR 74.82** | -7.4% |
| **Base** | 62.6B | 92.1B | 154.7B | 142.0B | **EUR 116.90** | 31.2% |
| **Bull** | 84.9B | 188.6B | 273.6B | 260.9B | **EUR 215.99** | 62.8% |

### Sensitivity Table (DCF Fair Value by WACC and Cliff Severity)

|                    | WACC 6.5% | WACC 7.0% | WACC 8.0% | WACC 9.0% |
|--------------------|-----------|-----------|-----------|-----------|
| 20% erosion (bull) | EUR 198 | EUR 177 | EUR 145 | EUR 122 |
| 35% erosion (base) | EUR 159 | EUR 142 | EUR 117 | EUR 99 |
| 50% erosion (bear) | EUR 125 | EUR 112 | EUR 92 | EUR 78 |

**Key observation:** Fair value ranges from EUR 78 to EUR 198 depending on assumptions. Terminal value accounts for 47-69% of enterprise value, making this method highly sensitive. Hence the need for multiple methods.

---

## METHOD 2: DDM -- Dividend Discount Model (Weight: 30%)

### Payout Ratio Clarification

| Metric | Value | Comment |
|--------|-------|---------|
| Payout (IFRS NI basis) | 85% | Misleading -- NI depressed by non-cash amortization |
| Payout (FCF basis) | 80% | Better measure -- FCF covers dividend |
| Payout ratio reported by yfinance | 97% | Uses trailing EPS which includes one-offs |

**CRITICAL FINDING #2:** The thesis flags 97% payout as "high but FCF-covered." The actual FCF payout is 80%, which is high for pharma but sustainable pre-cliff. Post-cliff, coverage becomes the risk.

### Post-Cliff Dividend Sustainability

| Scenario | FCF Post-Cliff (~2033) | Dividend Cost (~2033) | Coverage |
|----------|----------------------|----------------------|----------|
| Bear | ~EUR 6.0B | ~EUR 5.7B | 1.05x -- VERY TIGHT |
| Base | ~EUR 7.0B | ~EUR 5.7B | 1.23x -- Adequate |
| Bull | ~EUR 8.5B | ~EUR 5.7B | 1.49x -- Comfortable |

In the bear case, the dividend streak is at serious risk of being broken or growth frozen near zero. This fundamentally limits DDM upside.

### DDM Scenarios

| Scenario | Ke | Dividend Growth | D1 | Fair Value | MoS |
|----------|-----|----------------|-----|-----------|-----|
| **Bear** | 8.5% | 2.5% | EUR 4.02 | **EUR 66.97** | -20.0% |
| **Base** | 7.0% | 3.5% | EUR 4.06 | **EUR 115.92** | 30.7% |
| **Bull** | 6.5% | 4.5% | EUR 4.10 | **EUR 204.82** | 60.8% |

### DDM vs Thesis Comparison

| Parameter | Thesis DDM | My DDM | Comment |
|-----------|-----------|--------|---------|
| Ke | 8.0% | 7.0% | My Ke lower (actual beta) |
| Bear g | 4.0% | 2.5% | Thesis ignores cliff impact on dividend growth |
| Base g | 4.5% | 3.5% | Thesis assumes historical rate continues |
| Bull g | 5.0% | 4.5% | Similar |
| Bear FV | EUR 101.92 | EUR 66.97 | **-34% difference** |
| Base FV | EUR 117.04 | EUR 115.92 | Close |
| Bull FV | EUR 164.64 | EUR 204.82 | My bull higher due to lower Ke |

**KEY DISAGREEMENT:** The thesis bear DDM at EUR 101.92 uses 4% dividend growth with 8% Ke. I find 4% growth unsustainable through the cliff -- the bear case should model reduced dividend growth (2.5%), which drops fair value to EUR 67. This is a 34% gap that materially changes the downside assessment.

---

## METHOD 3: Forward P/E on Business EPS (Weight: 30%)

### Peer Comparison

| Ticker | EV/EBITDA | P/E | Fwd P/E | ROE | Yield | Beta |
|--------|-----------|-----|---------|-----|-------|------|
| ROG.SW | 12.7x | 22.2x | 16.4x | 37.3% | 2.7% | 0.20 |
| NOVN.SW | 10.8x | 21.6x | 15.8x | 30.8% | 3.1% | 0.46 |
| ABBV | 15.6x | 94.3x | 14.0x | N/M | 3.0% | 0.33 |
| AZN | 15.9x | 32.1x | 38.1x | 21.7% | 1.7% | 0.19 |
| GSK | 19.3x | 15.9x | 11.7x | 43.3% | 3.0% | 0.27 |
| PFE | 7.9x | 20.0x | 9.6x | 8.6% | 6.3% | 0.44 |
| **SAN.PA** | **8.7x** | **19.8x** | **9.0x** | **6.7%** | **4.9%** | **0.37** |

**Peer Median (ex-AZN outlier):** Fwd P/E 14.0x, EV/EBITDA 12.7x

**SAN.PA Deserved Multiple Assessment:**

Starting point: Peer median Fwd P/E ~14x

Adjustments:
- (-2x) Lowest ROE in peer group (6.7% vs peer median ~31%)
- (-1x) Dupixent cliff concentration risk
- (+0.5x) 26-year dividend aristocrat
- (+0.5x) Diversified pipeline (25+ Phase 3)
- (-1x) IFRS earnings are meaningless; business EPS more representative but less transparent

**Deserved Fwd P/E: 10-12x** (on business EPS of ~EUR 8.93/share)

| Scenario | Multiple | Business EPS | Fair Value | MoS |
|----------|---------|-------------|-----------|-----|
| **Bear** | 10x | EUR 8.93 | **EUR 89.29** | 10.0% |
| **Base** | 12x | EUR 8.93 | **EUR 107.15** | 25.0% |
| **Bull** | 14x | EUR 8.93 | **EUR 125.00** | 35.7% |

**Note:** SAN.PA currently trades at 9x forward -- at the BOTTOM of my range. The market appears to price in a scenario between my bear and base.

---

## Reconciliation

### Method Weights

| Method | Weight | Rationale |
|--------|--------|-----------|
| DCF with Cliff | 40% | Primary method; captures explicit cliff impact |
| DDM | 30% | Highly relevant for 26-year dividend aristocrat |
| Fwd P/E | 30% | Market-based cross-check, avoids amortization distortion |

### Combined Fair Values

| Scenario | DCF | DDM | Fwd P/E | Weighted FV | MoS |
|----------|-----|-----|---------|-------------|-----|
| **Bear (25%)** | EUR 74.82 | EUR 66.97 | EUR 89.29 | **EUR 76.81** | -4.6% |
| **Base (50%)** | EUR 116.90 | EUR 115.92 | EUR 107.15 | **EUR 113.68** | 29.3% |
| **Bull (25%)** | EUR 142.29 | EUR 204.82 | EUR 125.00 | **EUR 155.86** | 48.4% |

**Expected Value (25/50/25):** EUR 115.01
**MoS vs Expected:** 30.1%
**MoS vs Bear:** -4.6% (OVERVALUED in bear case)

### Divergence Analysis

Method-level divergence (base case):
- DCF: EUR 116.90
- DDM: EUR 115.92
- Fwd P/E: EUR 107.15
- Max divergence: 9.1% (within 30% threshold -- PASS)

These three methods converge well for the base case, which increases confidence.

---

## Reverse DCF: What the Market Prices In

At EUR 80.36, using 2025E FCF of EUR 8.1B:
- **WACC 8%:** Market implies FCF growth of **-2%** (DECLINING forever)
- **WACC 9%:** Market implies FCF growth of **1%** (near-zero growth)

At EUR 80.36, using 2024 actual FCF of EUR 5.89B:
- **WACC 9%:** Market implies FCF growth of **6%** (reasonable growth)

**INTERPRETATION:** If FCF truly is EUR 8.1B (2025), the market is pricing in negative growth -- essentially pricing in a severe cliff with no pipeline replacement. If the more conservative EUR 5.89B (2024 actual) is used, the market prices in reasonable 6% growth, which means no cliff discount at all. The truth likely lies between.

---

## Comparison vs Original Thesis

| Item | Thesis | Adversarial | Delta | Significance |
|------|--------|-------------|-------|-------------|
| Quality Score | 9/10 Tier A | 59 Tier B | MASSIVE | Thesis overrates quality by 1-2 tiers |
| ROIC vs WACC | "10-15% vs 8%" | -2.1pp (NEGATIVE) | CRITICAL | Tool says ROIC < WACC |
| Base FCF | EUR 8.1B | EUR 5.89B (2024 actual) | -27% | Thesis uses estimated 2025, not verified |
| Cliff modeling | None explicit | Yes, 35% base erosion | Major | Thesis hand-waves the largest risk |
| DDM growth (bear) | 4.0% | 2.5% | -1.5pp | Thesis ignores cliff impact on dividends |
| Payout ratio | "97% but FCF-covered" | 80% FCF, 85% NI | Corrected | Less alarming than thesis suggests |
| Bear FV | EUR 97.90 | EUR 76.81 | **-21.5%** | Thesis significantly underestimates downside |
| Base FV | EUR 122.02 | EUR 113.68 | **-6.8%** | Modest difference |
| Expected FV | EUR 127.54 | EUR 115.01 | **-9.8%** | Thesis inflated by ~10% |
| MoS vs Expected | 36.9% | 30.1% | -6.8pp | Still positive but less compelling |
| MoS vs Bear | 17.8% | -4.6% | -22.4pp | Thesis thinks bear is safe; it is NOT |

### Key Disagreements (Ranked by Materiality)

1. **QUALITY SCORE: Thesis says Tier A (9/10), tool says Tier B (59/100) with NEGATIVE ROIC spread.** This is the most material disagreement. The thesis assigns near-perfect quality to a company with ROE 6.7% and ROIC below its cost of capital. The quality_scorer tool penalizes SAN.PA correctly for its below-WACC returns. However, pharma accounting (massive goodwill from acquisitions, intangible amortization) distorts both ROE and ROIC. On tangible equity, ROE is 48%. The truth is somewhere between: SAN.PA is Tier B, not Tier A.

2. **BEAR CASE: Thesis bear FV EUR 97.90 vs my EUR 76.81.** The thesis bear case is not actually bearish. It uses 4% DDM growth (which is the historical rate!) and WACC of only 9%. A true bear should model reduced dividend growth post-cliff. In my bear case, the stock is slightly OVERVALUED at EUR 80.36, meaning there is real downside risk.

3. **DUPIXENT CLIFF: Not explicitly modeled in thesis.** The thesis mentions the cliff as a risk but does not model it year-by-year. This is a serious omission for 36% of revenue. My explicit modeling shows that even with 35% base erosion, non-Dupixent growth largely offsets the cliff -- but this depends critically on pipeline execution.

4. **BASE FCF: EUR 8.1B vs EUR 5.89B.** The thesis uses a 2025 estimate that represents a 37% increase over 2024 actuals. While possible (Opella divestiture, one-time items), using this as a starting point for DCF growth projections is aggressive. Notably, if 2025 FCF really is EUR 8.1B, it represents a REVERSAL of a 3-year declining trend.

---

## Scenarios

| Scenario | Fair Value | Probability | MoS |
|----------|-----------|-------------|-----|
| Bear | EUR 76.81 | 25% | -4.6% |
| Base | EUR 113.68 | 50% | 29.3% |
| Bull | EUR 155.86 | 25% | 48.4% |
| **Expected** | **EUR 115.01** | **100%** | **30.1%** |

**Price at analysis:** EUR 80.36

---

## Verdict

SAN.PA is **moderately undervalued** with an expected fair value of EUR 115, representing 30% upside from current levels. However, the downside protection is WEAKER than the thesis suggests -- the bear case shows slight overvaluation at current price. This is NOT a Tier A compounder and should not be sized as one.

The thesis FV of EUR 127.54 is inflated by approximately 10%, primarily due to:
1. Not modeling the Dupixent cliff explicitly
2. Using an aggressive bear DDM growth rate that ignores cliff impact
3. Classifying the company as Tier A when it is objectively Tier B

**Conviction: MEDIUM** (not HIGH as thesis claims). The margin of safety is real but narrower than stated, and the downside is meaningful.

---

## META-REFLECTION

### Dudas/Incertidumbres

1. **Base FCF uncertainty:** Is FY2025 FCF really EUR 8.1B or closer to EUR 5.89B (2024 actual)? This single input creates a ~25% swing in DCF fair value. The declining FCF trend (2021-2024: -11.4% CAGR) conflicts with the thesis assumption of EUR 8.1B for 2025. If FY2025 FCF confirms near EUR 8B, the base case is stronger. If it comes in at EUR 6-7B, the base case weakens significantly.

2. **ROIC measurement:** The quality_scorer gives ROIC spread of -2.1pp. However, pharma ROIC is distorted by massive goodwill from M&A. On tangible capital, returns are excellent. This creates a paradox: is SAN.PA destroying value (as ROIC suggests) or creating it (as tangible returns suggest)? For pricing purposes, the market uses business EPS which strips amortization -- this is why forward P/E is 9x (cheap) vs trailing P/E 19.8x (not cheap).

3. **Pipeline replacement:** The cliff model assumes non-Dupixent revenue grows 3-5% annually. This depends entirely on pipeline success (25+ Phase 3 readouts). If even 3-4 become blockbusters, the cliff is largely offset. If the pipeline disappoints broadly, the cliff is devastating. This is a binary risk that models poorly capture.

4. **DDM sensitivity:** The Gordon Growth Model is extremely sensitive to the gap between Ke and g. At Ke=7% and g=3.5%, FV is EUR 116. At Ke=7% and g=4%, FV is EUR 136 -- a 17% increase from 0.5pp of dividend growth. This makes DDM unreliable as a primary method despite Sanofi's dividend aristocrat status.

### Sensibilidad Preocupante

- WACC: Moving from 8% to 7% increases DCF base FV from EUR 117 to EUR 142 (+21%). This level of sensitivity means the WACC choice dominates the valuation.
- Cliff severity: Moving from 35% to 50% erosion drops base FV from EUR 117 to EUR 92 at 8% WACC (-21%).
- The combination of WACC and cliff severity creates a EUR 78-198 range -- a 2.5x spread that limits practical usefulness of DCF alone.

### Discrepancias con Thesis

1. The thesis bear case (EUR 97.90) provides a "comfortable" MoS of 17.8%. My bear case (EUR 76.81) shows the position is OVERVALUED by 4.6% in a downside scenario. This is the most consequential difference -- the thesis creates a false sense of downside protection.
2. The thesis Quality Score of 9/10 (Tier A) vs systematic tool 59 (Tier B) means the position is sized and conviction-rated inappropriately for a Tier B holding.
3. The thesis expected FV of EUR 127.54 is ~10% higher than my EUR 115.01. This is a moderate not extreme inflation.

### Sugerencias para el Sistema

1. **Create a pharma-specific valuation template** that: (a) uses business EPS not IFRS EPS, (b) requires explicit patent cliff modeling for any drug >20% of revenue, (c) uses tangible ROE alongside book ROE.
2. **Quality Scorer adjustment:** For pharma, the ROIC calculation on book equity is misleading due to acquisition goodwill. Consider adding a "tangible ROIC" metric.
3. **DDM should never be >40% weight** when payout approaches 80%+ of FCF. The model becomes unreliable as Ke-g narrows.

### Preguntas para Orchestrator

1. **Is SAN.PA appropriately sized?** At 5.0% of portfolio, it is sized like a Tier A conviction position. Given it is actually Tier B with weaker downside protection than thesis claims, should it be trimmed to 3-4%?
2. **Should we wait for FY2025 FCF confirmation?** The FCF data point (EUR 8.1B vs 5.89B) is the single biggest driver of valuation confidence. FY2025 results should be imminent.
3. **Does the negative ROIC spread warrant probation?** Every other Tier C position with ROIC < WACC has been sold (TEP.PA, LIGHT.AS, PFE). SAN.PA's ROIC issue may be accounting-driven, but it deserves investigation.

---
