# INDEPENDENT VALUATION REPORT: Allstate Corporation (ALL)

> **Date:** 2026-02-08
> **Type:** Adversarial Review (FASE 2)
> **Analyst:** Valuation Specialist (Independent)
> **Thesis FV:** $240 | **This Report FV:** See below

---

## 1. MARKET DATA

| Metric | Value | Source |
|--------|-------|--------|
| Price (2026-02-08) | $207.55 | price_checker.py |
| 52-week High | $216.75 | price_checker.py |
| 52-week Low | $176.00 | price_checker.py |
| P/E (TTM) | 5.5x | price_checker.py |
| Dividend Yield | 2.1% | price_checker.py |
| Market Cap | $54.3B | price_checker.py |
| Quality Score | 56/100 (Tier B) | quality_scorer.py |
| Book Value / Share (Q4 2025) | $108.45 | Allstate IR |
| P/B (current) | 1.91x | $207.55 / $108.45 |
| Shares Outstanding (diluted) | ~267M | Derived from FY2025 EPS |
| FY2025 EPS (diluted) | $38.06 | Allstate Q4 2025 earnings release |
| FY2025 Adj Net Income ROE | 38.3% | Allstate Q4 2025 earnings release |
| FY2025 Combined Ratio (P&L) | 85.2 | Allstate Q4 2025 earnings release |
| FY2025 Net Income | $10.2B | Allstate Q4 2025 earnings release |
| Q4 2025 Combined Ratio | 72.9 | Allstate Q4 2025 earnings release |

---

## 2. CRITICAL CONTEXT: IS 2025 PEAK CYCLE?

### 2.1 Combined Ratio History

| Year | P&L Combined Ratio | Comment |
|------|-------------------|---------|
| 2019 | 92.5 | Normal |
| 2020 | 99.9 | COVID claims |
| 2021 | 103.6 | Loss year |
| 2022 | 92.4 | Turnaround begins |
| 2023 | 104.5 | CAT losses spike |
| 2024 | 94.3 | Recovery |
| **2025** | **85.2** | **Exceptional** |

**Average 2019-2024 (6 years): 97.9**
**Average 2019-2025 (7 years): 96.1**
**Average excl. loss years (2019, 2022, 2024): 93.1**

The 2025 combined ratio of 85.2 is EXCEPTIONALLY LOW by historical standards. This is not sustainable and the thesis must account for reversion. Management itself guided "mid-90s" for auto combined ratio in 2026.

### 2.2 ROE History (Estimated from Net Income / Equity)

| Year | Net Income | Approx ROE | Comment |
|------|-----------|------------|---------|
| 2018 | ~$2.0B | ~9% | Normal |
| 2019 | ~$4.8B | ~21% | Good year |
| 2020 | ~$5.4B | ~23% | COVID tailwind (auto claims down) |
| 2021 | ~$5.2B | ~20% | Good |
| 2022 | -$1.4B | -6% | Loss year (CAT + inflation) |
| 2023 | -$0.3B | -1% | Near-loss (CAT) |
| 2024 | $4.6B | ~23% | Recovery |
| **2025** | **$10.2B** | **~38%** | **Exceptional / Peak** |

**10-year median ROE: ~11.5%** (per GuruFocus)
**2019-2024 average (excluding outliers 2022/2023): ~18%**
**2019-2025 average (all years): ~15%**
**"Good years" average (2019, 2020, 2021, 2024): ~22%**

The thesis uses ROE 37% and claims it is sustainable. THIS IS THE KEY DISAGREEMENT. ROE 37% represents a peak-cycle number driven by:
1. Exceptionally low CAT losses in H2 2025 ($209M Q4 vs $2.2B Q1 2025)
2. Cumulative pricing actions from hard market repricing 2022-2024
3. Reserve releases (common at cycle peak)
4. Investment income benefiting from high rates

### 2.3 Affordability Headwind

Allstate is PROACTIVELY cutting premiums:
- Reduced premiums for 7.8M customers by avg 17% in 2025
- Auto rates reduced in 32 states by avg 9%
- Cumulative premium impact: ~$810M (2% of auto earned premiums)

This means 2026 premiums will face headwind. Combined ratio will normalize upward as:
- Rate cuts reduce revenue
- Expense improvements partially offset
- CAT losses are volatile (could spike any quarter)

### 2.4 Consensus EPS Estimates

| Period | EPS Estimate | Change from 2025 |
|--------|-------------|-------------------|
| FY2025 Actual | $38.06 | -- |
| FY2026 Consensus | $23.30 (range $19.85-$28.67) | **-39%** |
| FY2027 Consensus | $23.61 (range $20.43-$26.72) | -38% |

Analysts expect a MASSIVE 39% drop in EPS from 2025 to 2026. The $38 EPS is clearly not repeatable. Consensus clusters around $23-24 for normalized earnings.

---

## 3. VALUATION METHOD 1: P/B vs ROE (PRIMARY - 60% weight)

### 3.1 Framework

For financial companies, the justified P/B ratio is:

```
P/B Justified = (ROE - g) / (Ke - g)

Where:
- ROE = NORMALIZED return on equity
- g = sustainable growth rate
- Ke = cost of equity
```

### 3.2 Key Inputs

**Cost of Equity (Ke):**
```
Risk-Free Rate (Rf): 4.3% (10Y US Treasury, Feb 2026)
Beta: 0.85 (insurance, defensive)
Equity Risk Premium: 5.5%
Ke = 4.3% + 0.85 * 5.5% = 8.98% ~ 9.0%
```

**Sustainable Growth (g):**
```
g = ROE * (1 - Payout Ratio)
Dividend: $4.32/year (post 8% raise)
EPS normalized: $23.30
Payout = $4.32 / $23.30 = 18.5%
Retention = 81.5%
But buybacks return additional capital (significant for ALL)
Effective payout incl. buybacks ~55-65%
g = ROE * retention_effective = varies by scenario
```

### 3.3 Scenarios

**What is NORMALIZED ROE?**

The thesis uses 22% for the P/B base case and 37% for the thesis narrative. Let me evaluate:

| ROE Assumption | Justification | P/B Justified (Ke=9%, g=3%) | BV $108.45 | Fair Value |
|---------------|---------------|------------------------------|-----------|-----------|
| 12% (10yr median) | Long-term average per GuruFocus | 1.50x | $108.45 | $163 |
| 15% (mid-cycle) | Avg all years 2019-2025 | 2.00x | $108.45 | $217 |
| 18% ("good years") | Avg of non-loss years | 2.50x | $108.45 | $271 |
| 22% (thesis base) | Thesis assumption | 3.17x | $108.45 | $344 |
| 37% (peak) | FY2025 actual | 5.67x | $108.45 | $615 |

**My assessment of normalized ROE: 15-18%**

Arguments:
- The 10-year median (11.5%) is depressed by the 2022-2023 loss years which were exceptionally bad
- The 2025 ROE (38%) is boosted by one-time favorable conditions
- The "good years" average of ~22% includes 2020 (COVID auto claims windfall)
- Management is cutting prices, which will reduce ROE from peak
- Combined ratio will normalize from 85 to mid-90s (management guidance)
- Investment income may decline as rates normalize (Fed cutting slowly)
- Underwriting cycle transitioning to soft market (sector view: 2025-2026 transition)

**Realistic mid-cycle ROE: 15-18%**

This is higher than the 10-year median because:
- Transformative Growth program reduced expense ratio by 6.6 points since 2018 (structural)
- Better data/pricing algorithms (structural improvement)
- But offset by rate cuts and soft market dynamics

### 3.4 P/B Fair Value Calculation

**Bear Case (ROE = 13%):**
```
P/B = (13% - 2%) / (9% - 2%) = 11% / 7% = 1.57x
FV = 1.57 * $108.45 = $170
```

**Base Case (ROE = 16%):**
```
P/B = (16% - 3%) / (9% - 3%) = 13% / 6% = 2.17x
FV = 2.17 * $108.45 = $235
```

**Bull Case (ROE = 20%):**
```
P/B = (20% - 4%) / (9% - 4%) = 16% / 5% = 3.20x
FV = 3.20 * $108.45 = $347
```

**P/B Method Fair Value (Base): $235**

---

## 4. VALUATION METHOD 2: P/E with Normalized Earnings (40% weight)

### 4.1 Peer Multiples (Current)

| Peer | P/E (TTM) | P/B | ROE (recent) | Combined Ratio | Comment |
|------|-----------|-----|-------------|----------------|---------|
| Progressive (PGR) | 10.5x | ~3.4x | 34% | ~88% | Best-in-class auto |
| Travelers (TRV) | 11.0x | 2.1x | 19% | ~84% | Commercial leader |
| Chubb (CB) | 12.9x | ~1.5x | 14% core | ~81% | Premium global |
| **ALL** | **5.5x** | **1.9x** | **38%** | **85%** | **Peak earnings inflate P/E denominator** |

ALL's P/E of 5.5x looks absurdly cheap, but that is because 2025 earnings ($38 EPS) are at peak. Using NORMALIZED earnings:

### 4.2 Normalized EPS

| Method | EPS | Reasoning |
|--------|-----|-----------|
| FY2025 Actual | $38.06 | Peak - NOT repeatable |
| FY2026 Consensus | $23.30 | Analysts' normalized estimate |
| FY2024 Actual | $30.84 | Also elevated (repricing benefits) |
| FY2024+2026 avg | $27.07 | Blend of recent and forward |
| Mid-cycle estimate | $20-24 | Based on CR ~93-96% and normalized investment income |

**My normalized EPS estimate: $22-24 (using consensus $23.30 as anchor)**

Justification:
- Management is cutting prices (7.8M customers, avg 17%)
- Combined ratio will normalize to mid-90s from 85
- Soft market approaching (sector view)
- Investment income stable but not growing
- Share buybacks will modestly boost EPS (~2%/year)

### 4.3 What P/E is Justified?

| Factor | Impact on Multiple |
|--------|-------------------|
| Sector median P/E | ~10-12x |
| ALL has narrow moat (not wide) | -1x discount |
| Cyclical earnings (high variance) | -1x discount |
| Strong capital returns (buybacks + div) | +1x premium |
| Structural cost improvements | +0.5x premium |
| CAT loss exposure risk | -0.5x discount |

**Justified P/E: 9-11x on normalized earnings**

Note: The thesis uses 10x P/E on $24 EPS. This is actually reasonable. My concern is not the multiple but whether $24 EPS is truly normalized or still slightly elevated.

### 4.4 P/E Fair Value Calculation

**Bear Case (8x * $20):**
```
FV = 8 * $20 = $160
```
Assumes: Soft market, CR deteriorates to ~98%, CAT losses spike, rate cuts compress earnings

**Base Case (10x * $23):**
```
FV = 10 * $23.30 = $233
```
Assumes: Normalized CR ~94%, moderate rate cuts absorbed, stable investment income

**Bull Case (12x * $26):**
```
FV = 12 * $26 = $312
```
Assumes: CR stays favorable ~90%, structural improvements hold, re-rating to sector

**P/E Method Fair Value (Base): $233**

---

## 5. RECONCILIATION

| Method | Bear | Base | Bull | Weight |
|--------|------|------|------|--------|
| P/B vs ROE | $170 | $235 | $347 | 60% |
| P/E Normalized | $160 | $233 | $312 | 40% |
| **Weighted** | **$166** | **$234** | **$333** | **100%** |

**Divergence between methods: 0.9%** (base cases $235 vs $233) -- Excellent convergence.

---

## 6. SCENARIO ANALYSIS

| Scenario | Fair Value | Probability | Weighted |
|----------|-----------|-------------|----------|
| Bear | $166 | 25% | $41.50 |
| Base | $234 | 50% | $117.00 |
| Bull | $333 | 25% | $83.25 |
| **Expected Value** | | **100%** | **$242** |

### Bear Scenario Drivers
- Soft market deepens, CR deteriorates to 98-100%
- CAT losses spike ($8B+ annual, vs $5B 2025)
- Rate cuts compress margins before new repricing cycle
- ROE reverts to ~13% (near 10yr median)
- Market applies discount P/E 8x

### Base Scenario Drivers
- CR normalizes to ~93-95% (management guide: mid-90s auto)
- Structural cost improvements hold (6.6pp expense ratio improvement is sticky)
- Investment income stable with rates at ~4%
- ROE normalizes to ~16%
- Market applies fair P/E 10x on normalized earnings

### Bull Scenario Drivers
- Underwriting discipline persists, CR stays ~88-91%
- Strong buybacks ($4B program) boost EPS by 3-4%/year
- Re-rating as market recognizes structural improvements
- ROE sustains ~20%
- Market applies sector-average P/E 12x

---

## 7. COMPARISON TO THESIS

| Metric | Thesis | This Report | Delta |
|--------|--------|-------------|-------|
| Fair Value | $240 | $234 (base), $242 (expected) | **-2.5% to +0.8%** |
| ROE used | 22% (P/B base) | 16% (P/B base) | Thesis higher |
| BV used | $80 | $108.45 | Thesis used OLD BV |
| P/B result | $240 | $235 | Similar because BV offset |
| EPS used | $24 | $23.30 | Similar |
| P/E used | 10x | 10x | Same |
| P/E result | $240 | $233 | -3% |

### Key Finding

The thesis FV of $240 is actually CLOSE to my independent estimate of $234 (base) / $242 (expected), but FOR DIFFERENT REASONS:

1. **Thesis used ROE 22% on OLD BV ($80):** 3.0x * $80 = $240
2. **I use ROE 16% on CURRENT BV ($108.45):** 2.17x * $108.45 = $235

The BV has grown from ~$80 to $108.45 (up 35.6%), which compensates for using a lower (more conservative) ROE assumption. The final number is similar but the foundation is different and more robust.

3. **However, the thesis narrative about ROE 37% being sustainable is WRONG.** ROE 37% is peak cycle. Normalized ROE is 15-18%. The thesis got lucky that the FV number was similar despite incorrect ROE assumption, because it used stale BV.

---

## 8. MARGIN OF SAFETY

| Metric | Value |
|--------|-------|
| Current Price | $207.55 |
| Base FV | $234 |
| Expected FV | $242 |
| Bear FV | $166 |
| **MoS vs Base** | **11.3%** |
| **MoS vs Expected** | **14.2%** |
| **MoS vs Bear** | **-25.0%** (price ABOVE bear FV) |

### Interpretation

- MoS of 11-14% is THIN for a Tier B company (precedents suggest 20-25% typical)
- Price is 25% ABOVE the bear case, meaning if the bear scenario materializes, there is meaningful downside
- The stock is near 52-week high ($216.75), not an opportunistic entry
- Consensus EPS of $23.30 may still be optimistic if soft market is worse than expected

---

## 9. PEER COMPARISON (Sanity Check)

### Implied Multiples at My Base FV

| Metric | At Current Price $207.55 | At FV $234 | Peer Median |
|--------|-------------------------|-----------|-------------|
| P/E on 2026E $23.30 | 8.9x | 10.0x | 10.5-12.9x |
| P/B on $108.45 BV | 1.91x | 2.16x | 1.5-3.4x |
| ROE (normalized 16%) | -- | -- | 14-34% |

My FV implies P/E 10x and P/B 2.16x, which is reasonable vs peers:
- Lower P/E than PGR (10.5x) and CB (12.9x) -- justified by narrower moat and cyclicality
- P/B of 2.16x is in line with TRV (2.1x) which has similar ROE
- Not implying anything extreme

---

## 10. SENSITIVITY TABLE

### P/B Method Sensitivity (BV = $108.45)

| ROE \ Ke | 8.0% | 9.0% | 10.0% |
|----------|------|------|-------|
| **13%** | $217 | $170 | $139 |
| **15%** | $261 | $200 | $163 |
| **16%** | $289 | $217 | $174 |
| **18%** | $356 | $260 | $199 |
| **20%** | $437 | $313 | $228 |

### P/E Method Sensitivity

| EPS \ P/E | 8x | 10x | 12x |
|-----------|-----|------|------|
| **$20** | $160 | $200 | $240 |
| **$23** | $184 | $230 | $276 |
| **$24** | $192 | $240 | $288 |
| **$26** | $208 | $260 | $312 |

**Key observation:** FV is highly sensitive to ROE assumption. Moving from 16% to 18% ROE shifts P/B FV from $217 to $260 (+20%). This is the main source of uncertainty.

---

## 11. CONVICTION ASSESSMENT

| Factor | Score | Comment |
|--------|-------|---------|
| Earnings predictability | LOW | P&C insurance earnings are inherently volatile (CAT losses) |
| Valuation support | MODERATE | 10-14% MoS is thin but positive |
| Quality tier | Tier B (QS 56) | Not a compounder, not trash |
| Cycle position | LATE/PEAK | Transitioning from hard to soft market |
| Capital returns | STRONG | $4B buyback + 8% div raise |
| Management | MIXED | Good turnaround, but comp too high, buybacks during losses |
| Macro alignment | NEUTRAL | Rates stable supports investment income, but soft market risk |

**Overall Conviction: MEDIUM**

---

## 12. SUMMARY

```
VALUATION: ALL (Allstate Corporation)

Type: Financial (P&C Insurance)
Quality Score: 56/100 (Tier B)
Methods: P/B vs ROE (60%) + P/E Normalized (40%)

Method 1: P/B vs ROE
- Normalized ROE: 16% (vs thesis 22%, vs peak 38%)
- Ke: 9.0%
- BV/share: $108.45 (vs thesis $80)
- P/B Justified: 2.17x
- Fair Value: $235

Method 2: P/E Normalized
- Normalized EPS: $23.30 (consensus 2026E)
- P/E Justified: 10x
- Fair Value: $233

Reconciliation:
| Method      | FV   | Weight | Weighted |
|-------------|------|--------|----------|
| P/B vs ROE  | $235 | 60%    | $141     |
| P/E Norm    | $233 | 40%    | $93      |
| **Weighted**|      | 100%   | **$234** |

Divergence: 0.9% (excellent convergence)

Scenarios:
| Scenario    | Fair Value | Prob  |
|-------------|-----------|-------|
| Bear        | $166      | 25%   |
| Base        | $234      | 50%   |
| Bull        | $333      | 25%   |
| **Expected**| **$242**  | 100%  |

Price: $207.55
MoS vs Base: 11.3%
MoS vs Expected: 14.2%
MoS vs Bear: -25.0%

Thesis FV ($240) vs This Report ($234): CLOSE (-2.5%)
BUT thesis reasoning was flawed (ROE 37% unsustainable, old BV).
Result similar by accident (higher BV offsets lower P/B).
```

---

## META-REFLECTION

### Doubts/Uncertainties
1. **Normalized ROE is the biggest swing factor.** My 16% estimate could be 13% (if soft market is harsh) or 20% (if structural improvements truly stick). This alone moves FV from $170 to $313.
2. **The quality_scorer.py ROIC calculation for insurers is unreliable** (investment portfolio inflates capital base). The QS of 56 may understate quality since ROE of 16%+ normalized is solid for a P&C insurer.
3. **I am uncertain about the durability of the 6.6pp expense ratio improvement.** If this is truly structural (technology, automation), then normalized ROE should be higher than pre-2020 levels. If it is partly cyclical, then ROE reverts lower.
4. **CAT loss volatility makes any single-year earnings unreliable.** A single bad quarter can wipe a full year of underwriting income.

### Concerning Sensitivity
- FV changes >20% when ROE moves from 16% to 13% or to 20%. This is a wide uncertainty band.
- The P/E method is more stable (less sensitive to assumptions) but insurance P/E should be read with caution given earnings volatility.

### Discrepancies with Thesis
- **Thesis ROE assumption (37%) is WRONG** -- this is peak cycle, not normalized
- **Thesis BV ($80) was STALE** -- actual is $108.45 (grew 35%)
- **Net result similar by coincidence** -- $240 (thesis) vs $234 (independent)
- **Thesis did not model the affordability headwind** (rate cuts for 7.8M customers)
- **Thesis did not account for underwriting cycle transition** (hard to soft market)

### Suggestions for the System
1. For insurance companies, always track combined ratio trend vs industry average as the primary profitability metric, not ROE alone
2. ROE for insurers should always be normalized across a full underwriting cycle (8-12 years, or at minimum 5 years)
3. The quality_scorer.py should have an insurance-specific module that uses combined ratio, ROE, and reserve adequacy rather than generic ROIC

### Questions for Orchestrator
1. Given MoS of only 11-14% for a Tier B company, is this consistent with precedent? decisions_log.yaml shows Tier B requires ~20-25% MoS typically. This suggests HOLD (not ADD) is appropriate.
2. The stock is near its 52-week high ($207 vs $216 high). Is this the right time to be adding to a Tier B position, or should we be looking for Tier A opportunities with better MoS?
3. Should we set a lower conviction (from MEDIUM to LOW) given that we are in late-cycle for insurance underwriting?

---

**Sources:**
- [Allstate Q4 2025 Earnings Call Transcript](https://www.fool.com/earnings/call-transcripts/2026/02/05/allstate-all-q4-2025-earnings-call-transcript/)
- [Allstate Q4 2025 Slides](https://www.investing.com/news/company-news/allstate-q4-2025-slides-record-profits-amid-strategic-affordability-initiatives-93CH-4488362)
- [Allstate Q4 Earnings Beat - Nasdaq](https://www.nasdaq.com/articles/allstate-q4-earnings-beat-estimates-property-liability-unit-strength)
- [Allstate Insurance Journal Q4](https://www.insurancejournal.com/news/national/2026/02/05/856975.htm)
- [Allstate ROE Historical - MacroTrends](https://www.macrotrends.net/stocks/charts/ALL/allstate/roe)
- [Allstate Book Value - GuruFocus](https://www.gurufocus.com/term/book-value-per-share/ALL)
- [Allstate Combined Ratio - GuruFocus](https://www.gurufocus.com/term/combined-ratio_pct/ALL)
- [Allstate Shares Outstanding - MacroTrends](https://www.macrotrends.net/stocks/charts/ALL/allstate/shares-outstanding)
- [Allstate EPS History - MacroTrends](https://macrotrends.net/stocks/charts/ALL/allstate/eps-earnings-per-share-diluted)
- [Allstate Affordability Actions](https://www.insurancejournal.com/news/national/2026/02/06/857245.htm)
- [Allstate Analyst Estimates - Benzinga](https://www.benzinga.com/insights/analyst-ratings/26/02/50426227/deep-dive-into-allstate-stock-analyst-perspectives-10-ratings)
- [WallStreetZen ALL Forecast](https://www.wallstreetzen.com/stocks/us/nyse/all/stock-forecast)
- [Progressive P/B - GuruFocus](https://www.gurufocus.com/term/pb-ratio/PGR)
- [Travelers P/B - MacroTrends](https://www.macrotrends.net/stocks/charts/TRV/travelers/price-book)
- [Chubb Q4 2025 Results](https://news.chubb.com/2026-02-03-Chubb-Reports-Fourth-Quarter-Net-Income-of-3-21-Billion,-Up-24-7-)
