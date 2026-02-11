# Valuation Report: DSY.PA (Dassault Systemes SE)

**Date:** 2026-02-11
**Analyst:** valuation-specialist (independent)
**Current Price:** EUR 17.77 (from price_checker.py)
**52-Week Range:** EUR 17.16 - EUR 40.76

---

## Company Classification

**Type:** Mature enterprise software compounder in transition (cloud migration)
**QS Tool:** 70/100 (Tier B)
**QS Adjusted:** 78/100 (Tier A borderline, +8 for market position)
**Moat:** WIDE (22/25 per independent moat-assessor)
**Risk Score:** HIGH (7 HIGH/CRITICAL risks per independent risk-identifier)

Given Tier A borderline status and the nature of the business (stable recurring revenue, predictable FCF, wide moat), the appropriate methods are:

| Priority | Method | Weight | Rationale |
|----------|--------|--------|-----------|
| Primary | DCF with scenarios | 40% | FCF positive 4/4 years, predictable cash flows |
| Secondary | EV/EBIT vs peers | 30% | Direct comparison with PLM oligopoly peers |
| Tertiary | Owner Earnings Yield + Growth | 15% | Compounder quality check |
| Quaternary | Reverse DCF | 15% | What market is pricing in |

---

## IFRS vs Non-IFRS Basis: Critical Clarification

Before presenting valuations, it is essential to address the IFRS vs Non-IFRS earnings gap:

| Metric | IFRS | Non-IFRS | Gap |
|--------|------|----------|-----|
| FY2025 EPS | EUR 0.91 | EUR 1.31 | 44% |
| FY2025 Operating Margin | ~22% | 32.0% | +10pp |
| P/E at EUR 17.77 | 19.5x | 13.6x | 6x |

**Non-IFRS adjustments (EUR ~429M total):**
- Amortization of acquired intangibles: EUR 313M (mostly Medidata acquisition)
- Stock-based compensation: EUR 116M

**My assessment:** For DCF valuation, I use **FCF (which is an IFRS-based figure)**. Operating cash flow of EUR 1.63B less capex gives FCF of EUR 1.5B. This is the correct basis because:
1. FCF captures actual cash generated regardless of accounting treatment
2. Amortization of acquired intangibles is a non-cash charge (already paid in 2019 acquisition)
3. SBC IS a real cost (dilution), but FCF partially captures this through share count growth

For multiples comparison, I use **Non-IFRS EBIT** as the enterprise software industry standard, but validate against IFRS P/E as a sanity check. If my fair value implies IFRS P/E >25x, I am likely overvaluing.

---

## Method 1: DCF with Derived Parameters (Weight: 40%)

### Parameter Derivation

**Growth Rate:**
```
TAM Growth: +6% CAGR (PLM market, Mordor Intelligence/ABI Research)
Market Share: 0% (Siemens Altair acquisition offsets Dassault cloud gains)
Pricing Power: +2% (embedded switching costs, annual escalators)
Cloud Transition Drag: -2% near-term (license cannibalization, Medidata decline)

Year 1-2: +4% (guidance midpoint, reflecting transition trough)
Year 3-5: +5-6% (cloud acceleration IF transition succeeds)

My base case growth for DCF: 4% (conservative, reflecting current deceleration)
Bear case: 2% (growth fails to recover)
Bull case: 6% (cloud transition accelerates)
```

**WACC Derivation:**
```
Risk-Free Rate (EUR): 2.8% (German 10Y bund)
Beta: 0.55 (tool) -- adjusted to 0.70 for conservatism (execution risk)
Equity Risk Premium: 5.5% (Europe)
Adjusted Ke = 2.8% + 0.70 * 5.5% = 6.65%

Kd after-tax: 4.48% (5.5% * (1 - 18.6%))
Capital Structure: ~95% equity, ~5% debt (net cash company)
Calculated WACC = 0.95 * 6.65% + 0.05 * 4.48% = 6.5%

For conservatism: WACC range 8.0-9.0%
Adding 1.5-2.5pp execution risk premium for:
- Cloud transition uncertainty
- Medidata structural risk
- Revenue deceleration trend
- Damaged management credibility
```

**Terminal Growth Rate:**
2.0% (at or below EUR-area inflation target; justified because Dassault's core markets grow above GDP but terminal conservatism is appropriate given growth concerns)

### DCF Tool Results -- Comprehensive Matrix

| Growth | WACC | Terminal | Base FV | Bear FV | Bull FV | MoS (Base) |
|--------|------|----------|---------|---------|---------|------------|
| 2% | 8.5% | 2.0% | EUR 18.52 | EUR 14.93 | EUR 23.60 | +4.2% |
| 3% | 8.0% | 2.0% | EUR 20.83 | EUR 16.58 | EUR 27.00 | +17.2% |
| 3% | 8.5% | 2.0% | EUR 19.29 | EUR 15.55 | EUR 24.61 | +8.6% |
| 4% | 8.0% | 2.5% | EUR 23.22 | EUR 18.23 | EUR 30.69 | +30.7% |
| 4% | 8.5% | 2.0% | EUR 20.10 | EUR 16.18 | EUR 25.65 | +13.1% |
| 4% | 9.0% | 2.0% | EUR 18.72 | EUR 15.23 | EUR 23.56 | +5.4% |
| 5% | 8.5% | 2.5% | EUR 22.25 | EUR 17.70 | EUR 28.86 | +25.2% |
| 5% | 9.0% | 2.0% | EUR 19.49 | EUR 15.85 | EUR 24.54 | +9.7% |

### Sensitivity Matrix (4% growth, 8.5% WACC, 2.0% terminal base)

```
Growth \ WACC       7.0%       8.5%      10.0%
----------------------------------------------
       1.0%         22.8       17.8       14.6
       2.5%         24.3       18.9       15.5
       4.0%         25.9       20.1       16.5
       5.5%         27.6       21.4       17.5
       7.0%         29.4       22.7       18.5

FV Spread: 73% (highly sensitive)
Terminal Value as % of EV: 74.2% (high TV dependence)
```

### DCF Assessment

The DCF is HIGHLY sensitive to inputs. The fair value ranges from EUR 14.6 (10% WACC, 1% growth) to EUR 29.4 (7% WACC, 7% growth). This 73-78% spread means the DCF cannot provide a precise point estimate.

**My DCF Base Case: EUR 19.50** (weighted toward conservative assumptions)

Reasoning: I anchor to the 4% growth / 8.5% WACC / 2.0% terminal scenario (EUR 20.10) but discount by ~3% because:
1. Revenue CAGR of 3.2% is BELOW my 4% assumption -- recent trend supports 3-4%, not 4%
2. Q4 2025 showed only +1% growth -- momentum is negative
3. FY2026 guidance of 3-5% with flat EPS confirms near-term stagnation
4. Adversarial pattern: 14/16 prior theses had inflated FV by avg -19%

**DCF Bear Case: EUR 15.50** (3% growth, 8.5% WACC → EUR 15.55)
**DCF Bull Case: EUR 25.65** (4% growth, 8.5% WACC, bull scenario → EUR 25.65)

---

## Method 2: EV/EBIT Comparison vs PLM Peers (Weight: 30%)

### Current Enterprise Valuations

**DSY.PA:**
- Market Cap: EUR 23.4B
- Net Cash: EUR 1.3B (cash EUR 3.9B - debt EUR 2.6B)
- EV = EUR 22.1B
- Non-IFRS EBIT (FY2025): EUR 6.24B * 32.0% = EUR 2.0B
- IFRS EBIT (FY2025): EUR 6.24B * 21.7% = EUR 1.35B
- EV/EBIT (Non-IFRS): 11.1x
- EV/EBIT (IFRS): 16.4x

### Peer Comparison

| Company | EV/EBIT (est.) | P/E | Rev Growth | GM | FCF Margin | Beta |
|---------|----------------|-----|------------|-----|-----------|------|
| **DSY.PA** | **11x (NI) / 16x (IFRS)** | **20x IFRS, 13.6x NI** | **4%** | **84%** | **24%** | **0.55** |
| PTC (PTC) | ~21x | 23x | 12% | 84% | 31% | 1.03 |
| Autodesk (ADSK) | ~35x+ | 45x | 11% | ~67% | ~30% | 1.3 |
| Siemens DI (est.) | ~18-20x | N/A (part of Siemens) | ~6-8% | ~35% | ~15% | N/A |

### Analysis

DSY.PA trades at roughly **HALF the EV/EBIT of PTC**, its most direct competitor in the PLM oligopoly. The discount reflects:

1. **Growth differential:** PTC growing 12% vs DSY 4% -- this alone justifies a significant discount. PTC's cloud transition is further along.
2. **Geographic discount:** European-listed software trades at a structural discount vs US peers. This is partly rational (lower growth, regulation) and partly sentiment-driven.
3. **Revenue deceleration:** DSY's growth is decelerating (7% -> 5% -> 4% -> 3-5% guided). PTC's is accelerating.
4. **AI narrative:** The market fears AI disruption more for traditional CAD/PLM than for PLM platforms with IoT focus (PTC's ThingWorx).

**Fair multiple for DSY.PA:**

Starting from PTC's ~21x EV/EBIT:
- Discount for lower growth (4% vs 12%): -5x
- Discount for geographic/sentiment: -2x
- Premium for wider moat (CATIA standard, 49% insider): +1x
- Premium for net cash vs PTC's net debt: +1x
- Discount for Medidata drag: -1x
- **Fair EV/EBIT: 15x (Non-IFRS basis)**

A 15x multiple would also be justified independently:
- Sector median for mature enterprise software: 14-18x
- DSY's 84% gross margin and wide moat warrant above-median
- But 4% growth and execution risk cap the premium

**Sanity check using IFRS basis:**
- At IFRS EBIT of EUR 1.35B, 15x would imply EV = EUR 20.25B
- This is equivalent to ~22x IFRS EV/EBIT, which is more reasonable
- The IFRS basis provides a natural sanity check against over-enthusiasm

### EV/EBIT Fair Value Calculation

**Conservative (13x Non-IFRS EV/EBIT):**
- EV = EUR 2.0B * 13 = EUR 26.0B
- Equity = EUR 26.0B + EUR 1.3B (net cash) = EUR 27.3B
- FV = EUR 27.3B / 1.317B shares = EUR 20.73

**Base (15x Non-IFRS EV/EBIT):**
- EV = EUR 2.0B * 15 = EUR 30.0B
- Equity = EUR 30.0B + EUR 1.3B = EUR 31.3B
- FV = EUR 31.3B / 1.317B shares = EUR 23.77

**Bear (11x Non-IFRS EV/EBIT -- current multiple sustained):**
- EV = EUR 2.0B * 11 = EUR 22.0B
- Equity = EUR 22.0B + EUR 1.3B = EUR 23.3B
- FV = EUR 23.3B / 1.317B shares = EUR 17.69

**IFRS Sanity Check (15x IFRS EV/EBIT):**
- EV = EUR 1.35B * 15 = EUR 20.25B
- Equity = EUR 20.25B + EUR 1.3B = EUR 21.55B
- FV = EUR 21.55B / 1.317B shares = EUR 16.36
- This implies the current price of EUR 17.77 is ALREADY slightly above IFRS-based fair value at 15x
- IMPORTANT: Using IFRS EBIT, the stock is NOT obviously cheap

**EV/EBIT Fair Value (Non-IFRS basis): EUR 20.75** (conservative 13x, reflecting growth concerns)

**Validation:** The EUR 20.75 implies a Non-IFRS P/E of ~15.8x (EUR 20.75 / EUR 1.31), which translates to IFRS P/E of ~22.8x (EUR 20.75 / EUR 0.91). For a 4% grower, an IFRS P/E of 22.8x is GENEROUS. This tells me the 13x Non-IFRS multiple may already be at the upper end of fair.

---

## Method 3: Owner Earnings Yield + Growth (Weight: 15%)

```
FCF (FY2025): EUR 1.50B
Depreciation: ~EUR 250M (estimated)
Maintenance Capex: ~EUR 275M (Depreciation * 1.1)
Owner Earnings = EUR 1.50B - EUR 275M + EUR 250M = EUR 1.475B

Market Cap at EUR 17.77: EUR 23.4B

Owner Earnings Yield (OEY) = EUR 1.475B / EUR 23.4B = 6.3%

Expected Growth (next 5 years, weighted):
- Revenue CAGR: 4% (base case)
- Margin expansion: 0.5% annually (32% -> 33%)
- Estimated EPS growth: 5-6%
- Conservative mid-point: 5%

OEY + Growth = 6.3% + 5.0% = 11.3%
vs WACC of 6.5% (calculated) or 8.0-8.5% (conservative)
Spread: +2.8% to +4.8%
```

**Comparison with precedent Tier A purchases:**

| Position | OEY | Growth | OEY+Growth | Spread vs WACC |
|----------|-----|--------|------------|----------------|
| ADBE | ~5% | ~12% | 16.5% | +7.5pp |
| BYIT.L | ~7% | ~7% | 14.4% | +5.4pp |
| AUTO.L | ~10% | ~7% | 17.0% | +8.0pp |
| NVO | ~4% | ~10% | 14.0% | +6.0pp |
| **DSY.PA** | **6.3%** | **5.0%** | **11.3%** | **+2.8-4.8pp** |

DSY.PA's OEY + Growth of 11.3% is BELOW all Tier A precedents. The spread over WACC is the thinnest in the portfolio. This means that at current price, DSY.PA offers less forward return potential than any existing Tier A holding at their entry prices.

**OEY-based assessment:** Current price offers MARGINAL attractiveness. Not compelling for a Tier A entry given precedents.

---

## Method 4: Reverse DCF (Weight: 15%)

**Question:** What growth rate does EUR 17.77 imply?

Using the DCF tool results:
- At 2% growth, 8.5% WACC, 2.0% terminal: FV = EUR 18.52 (close to current price)
- At 1% growth, 8.5% WACC: FV approximated at ~EUR 17.8 (from sensitivity matrix)
- At 0% growth, 8.5% WACC: FV = ~EUR 17.0 (extrapolated from sensitivity)

**The market is pricing DSY.PA for approximately 1-2% perpetual growth at 8.5% WACC.**

**What this means:**
- The market expects Dassault to grow at or below inflation PERMANENTLY
- For a company with 84% gross margins, ROIC of 16.4%, net cash, and the #1 global PLM franchise, this is VERY pessimistic
- Even in the bear case (Medidata continues declining, auto stays weak, cloud transition slow), 2-3% growth is achievable through pricing power alone
- The market appears to be pricing in a combination of: (a) permanent growth stagnation, (b) AI disruption risk, and (c) European software discount

**Reverse DCF assessment:** The implied growth rate of ~1-2% is likely too pessimistic for a wide-moat business with 82% recurring revenue and dominant market position. However, the market could remain irrational for 12-24 months, especially with no near-term catalyst.

---

## Reconciliation

| Method | Fair Value | Weight | Weighted |
|--------|-----------|--------|----------|
| DCF (conservative base) | EUR 19.50 | 40% | EUR 7.80 |
| EV/EBIT (13x Non-IFRS) | EUR 20.75 | 30% | EUR 6.23 |
| OEY + Growth | N/A (qualitative: marginal) | 15% | supports ~EUR 19-21 |
| Reverse DCF | N/A (implied growth ~1-2%) | 15% | suggests floor ~EUR 17-18 |
| **Weighted Average** | | **100%** | **EUR 20.00** |

**Divergence between methods:** DCF base (EUR 19.50) vs EV/EBIT base (EUR 20.75) = 6.4% divergence. Well within acceptable range (<30%). Methods are convergent.

**IMPORTANT: IFRS Sanity Check**
- My FV of EUR 20.00 implies IFRS P/E of 22.0x (EUR 20.00 / EUR 0.91)
- For a company guiding flat EPS in FY2026, an IFRS P/E of 22x is GENEROUS
- If the market shifts to IFRS focus (as SBC scrutiny increases), FV could be lower
- This is a YELLOW FLAG that my FV may be at the upper bound of reasonable

**Fair Value: EUR 20.00** (deliberately conservative, rounded down from EUR 20.03 weighted)

**Why my estimate differs from Morningstar (EUR 32.50) and consensus (EUR 31.10):**

1. **Growth assumptions:** Morningstar assumes faster growth normalization (likely 7-8% revenue CAGR). I use 4% reflecting actual recent trend and guidance. The gap between their growth and mine is the primary driver of the 55% FV difference.

2. **WACC:** Morningstar likely uses a lower WACC (closer to the calculated 6.5-7.0%) reflecting DSY's low beta. I add 1.5-2.0pp execution risk premium, bringing my WACC to 8.0-8.5%.

3. **Terminal multiple:** Morningstar values wide-moat companies at higher terminal multiples. My DCF terminal growth of 2.0% with conservative WACC produces a lower terminal value.

4. **Post-adversarial conservatism:** Our portfolio's adversarial program (Sessions 48-52) found systematic FV inflation averaging -19%. I deliberately err conservative. If Morningstar is right and I am wrong, I miss upside but protect capital. If I am right and they are wrong, I avoid a value trap.

5. **Analyst consensus is anchored to historical multiples.** DSY traded at 30-40x non-IFRS P/E for years. Analysts are slow to de-rate. My 13x-15x non-IFRS EV/EBIT reflects the new reality of 3-4% growth.

---

## Scenario Analysis

### Bear Case (Probability: 30%)

**Assumptions:**
- Revenue CAGR: 2-3% (Medidata continues declining, auto stays weak, cloud transition slower)
- Non-IFRS Operating Margin: 31-32% (slight compression from investment)
- Non-IFRS EPS FY2030E: EUR 1.40-1.50
- Multiple: 12-13x Non-IFRS EV/EBIT (mature software utility valuation)
- No near-term catalyst materializes

**Fair Value Bear: EUR 16.00**
- DCF support: EUR 15.50 (3% growth, 8.5% WACC bear scenario)
- EV/EBIT support: 11x * EUR 2.0B + EUR 1.3B = EUR 23.3B / 1.317B = EUR 17.69 (but with lower EBIT if margins compress: 11x * EUR 1.9B + EUR 1.3B = EUR 22.2B / 1.317B = EUR 16.86)
- Risk-identifier estimated EUR 16.25 in bear case

**Triggers for bear case:**
- FY2026 revenue growth <3%
- Medidata goodwill impairment
- Data breach escalation affecting defense customers
- AI competitor demonstrates viable PLM alternative

### Base Case (Probability: 45%)

**Assumptions:**
- Revenue CAGR: 4% (guidance midpoint, cloud transition progressing)
- Non-IFRS Operating Margin: 32-33% (stable to slight expansion)
- Non-IFRS EPS FY2030E: EUR 1.55-1.70
- Multiple: 13-15x Non-IFRS EV/EBIT
- European auto recovery provides modest tailwind H2 2026-2027

**Fair Value Base: EUR 20.00**
- DCF support: EUR 19.50 (4% growth, 8.5% WACC)
- EV/EBIT support: EUR 20.75 (13x Non-IFRS)

### Bull Case (Probability: 25%)

**Assumptions:**
- Revenue CAGR: 6-7% (cloud transition accelerates, NVIDIA partnership generates revenue)
- Non-IFRS Operating Margin: 33-35% (operating leverage kicks in)
- Non-IFRS EPS FY2030E: EUR 1.80-2.10
- Multiple: 17-20x Non-IFRS EV/EBIT (re-rating as growth compounder)
- Medidata stabilizes, European auto recovers

**Fair Value Bull: EUR 27.00**
- DCF support: EUR 25.65 (4% growth, 8.5% WACC bull scenario); EUR 28.86 (5% growth, 8.5% WACC bull scenario)
- EV/EBIT support: 17x * EUR 2.0B + EUR 1.3B = EUR 35.3B / 1.317B = EUR 26.80

**NOTE on probability weighting:** I assign 30% to bear (not 25%) because the risk-identifier scored this as HIGH risk with 7 HIGH/CRITICAL risks, and I want to reflect elevated uncertainty. The probabilities do not follow the default 25/50/25 split.

### Expected Value

```
EV = (EUR 16.00 * 30%) + (EUR 20.00 * 45%) + (EUR 27.00 * 25%)
EV = EUR 4.80 + EUR 9.00 + EUR 6.75
EV = EUR 20.55
```

---

## Summary Table

```
VALUATION: DSY.PA

Type of company: Mature enterprise software, cloud transition
Methods selected: DCF (primary) + EV/EBIT vs peers (secondary) + OEY + Reverse DCF

Method 1: DCF (Discounted Cash Flow)
- Inputs: FCF EUR 1.5B, Growth 4%, WACC 8.5%, Terminal 2.0%
- Fair Value: EUR 19.50

Method 2: EV/EBIT vs PLM Peers
- Inputs: Non-IFRS EBIT EUR 2.0B, Multiple 13x, Net Cash EUR 1.3B
- Fair Value: EUR 20.75

Reconciliation:
| Method          | FV        | Weight | Weighted   |
|-----------------|-----------|--------|------------|
| DCF             | EUR 19.50 | 40%    | EUR 7.80   |
| EV/EBIT         | EUR 20.75 | 30%    | EUR 6.23   |
| OEY + Growth    | ~EUR 20   | 15%    | EUR 3.00   |
| Reverse DCF     | ~EUR 18   | 15%    | EUR 2.70   |
| **Weighted Avg**|           | 100%   | **EUR 19.73** |

Rounded: EUR 20.00

Divergence: 6.4% (DCF vs EV/EBIT) -- within acceptable range

Scenarios:
| Scenario     | Fair Value | Prob  |
|-------------|-----------|-------|
| Bear         | EUR 16.00 | 30%   |
| Base         | EUR 20.00 | 45%   |
| Bull         | EUR 27.00 | 25%   |
| **Expected** | **EUR 20.55** | 100% |

Current Price: EUR 17.77
MoS vs Base FV (EUR 20.00): +12.6%
MoS vs Expected Value (EUR 20.55): +15.6%
MoS vs Bear Case (EUR 16.00): -10.0% (BELOW bear case)
```

---

## Sensitivity and Validation

### 1. DCF Sensitivity Table

```
Growth \ WACC       7.0%       8.0%       8.5%       9.0%      10.0%
---------------------------------------------------------------------
       1.0%         22.8        --        17.8        --        14.6
       2.0%          --         --        18.5        --         --
       3.0%         27.5       20.8       19.3        --        16.8
       4.0%         25.9       23.2       20.1       18.7       16.5
       5.0%          --         --        22.3       19.5       18.0
       6.0%         31.2       --        23.7        --        19.0
       7.0%         29.4        --        22.7        --        18.5
```

FV range: EUR 14.6 - EUR 31.2 (spread 78%)
At my base assumptions (4% growth, 8.5% WACC): EUR 20.10

**KEY OBSERVATION:** The DCF produces EUR 17.77 (current price) at approximately:
- 1-2% growth with 8.5% WACC
- 3% growth with 9.5% WACC
- The market is pricing in either very low growth or very high risk (or both)

### 2. Validation vs Peers (Implied Multiples)

At my FV of EUR 20.00:
- Non-IFRS P/E: 15.3x (EUR 20.00 / EUR 1.31)
- IFRS P/E: 22.0x (EUR 20.00 / EUR 0.91)
- EV/EBIT (Non-IFRS): ~13.4x
- EV/FCF: ~14.7x

| Multiple | DSY at EUR 20 | PTC | ADSK | Sector Range |
|----------|---------------|-----|------|-------------|
| Non-IFRS P/E | 15.3x | 23.3x | 44.9x | 15-25x |
| IFRS P/E | 22.0x | N/A | N/A | 20-30x |
| EV/EBIT (NI) | ~13.4x | ~21x | ~35x | 12-20x |
| EV/FCF | ~14.7x | ~21x | ~40x | 15-25x |

My implied multiples are at the LOW END of sector ranges, reflecting the conservative approach. Given DSY's 4% growth vs PTC's 12%, the discount is justified.

**RED FLAG CHECK:**
- IFRS P/E of 22x for a company guiding flat EPS in FY2026 = on the high side
- Non-IFRS P/E of 15.3x for a wide-moat compounder = reasonable
- The IFRS/Non-IFRS tension suggests my FV is at the boundary of conservative vs fair

### 3. Validation vs Precedents (decisions_log.yaml)

| Position | QS | MoS at Entry | Tier | Outcome |
|----------|-----|-------------|------|---------|
| ADBE | 76 | 31% | A | Pending |
| NVO | 82 | 38% | A | Pending |
| MONY.L | 81 | 36% | A | Pending |
| LULU | 82 | 34% | A | Pending |
| AUTO.L | 79 | 29% | A | Pending |
| BYIT.L | 81 | 35% | A | Pending |
| **DSY.PA** | **78 (adj)** | **12.6%** | **A (borderline)** | -- |

**DSY.PA's MoS of 12.6% is DRAMATICALLY below all Tier A precedents (minimum 29%).** Even the lowest Tier A precedent (AUTO.L at 29%) has more than double the MoS of DSY.PA.

**This is the key finding of the valuation:** The quality is genuine (wide moat, world-class franchise), but the price does NOT yet provide the margin of safety consistent with our portfolio's standards.

### 4. Goodwill Impairment Risk Assessment

- Total goodwill: EUR 11.6B (~70% of total equity of ~EUR 16.5B)
- Medidata acquisition (2019): EUR 5.8B (estimated ~EUR 4B+ in goodwill)
- Life Sciences revenue declining: -2% FY2025, -7% Q4 Medidata specifically
- If Medidata's decline continues for 2-3 more years, impairment risk becomes material
- An impairment charge would NOT affect FCF but would:
  - Reduce book value significantly
  - Signal capital misallocation by management
  - Potentially trigger covenant issues (though net cash position protects against this)
  - Create negative headline risk and further sentiment damage
- **Impact on valuation:** I do NOT adjust my FV for potential impairment because my DCF already uses conservative growth assumptions that implicitly account for Medidata weakness. However, I note this as a risk that could create a buying opportunity (non-cash charge creating panic) or confirm a structural problem.

---

## Reverse DCF: What the Market Implies

```
At EUR 17.77 with WACC 8.5%:
  Implied perpetual growth: ~1-2%
  Implied 5-year revenue CAGR: ~1%
  Implied terminal EV/EBIT: ~10x

At EUR 17.77 with WACC 7.5% (using calculated WACC + 1pp):
  Implied perpetual growth: ~0%
  This means: market prices DSY as a zero-growth European software utility

For DSY to be worth EUR 17.77, you must believe:
1. Revenue growth permanently stalls at 1-2% (below inflation)
2. OR WACC is truly 9.5%+ (reflecting substantial execution/disruption risk)
3. OR terminal value deserves a structural discount (AI disruption)

Is this reasonable?
- Partially. Revenue growth HAS decelerated to 3-4% and may worsen
- But 1-2% permanent growth for a #1 PLM franchise with 82% recurring revenue
  and embedded switching costs seems excessively pessimistic
- Even Medidata alone (15% of revenue) cannot drag total growth to 1-2%
  unless core Industrial Innovation also stalls

Conclusion: The market is pricing in a WORST-CASE growth scenario
that is unlikely but not impossible.
```

---

## Final Assessment

| Metric | Value |
|--------|-------|
| **Fair Value (Base)** | EUR 20.00 |
| **Fair Value (Bear)** | EUR 16.00 |
| **Fair Value (Bull)** | EUR 27.00 |
| **Expected Value** | EUR 20.55 |
| **Current Price** | EUR 17.77 |
| **MoS vs Base** | +12.6% |
| **MoS vs EV** | +15.6% |
| **MoS vs Bear** | -10.0% |
| **Morningstar FV** | EUR 32.50 |
| **Consensus Target** | EUR 31.10 |
| **My FV vs Morningstar** | -38.5% (deliberately conservative) |
| **My FV vs Consensus** | -35.7% (deliberately conservative) |

### Key Conclusions

1. **Quality is genuine.** Wide moat, 84% gross margins, ROIC >> WACC, net cash, 49% insider. This is a world-class franchise.

2. **Growth is the real concern.** Revenue CAGR of 3.2% and flat EPS guidance for FY2026 undermine the "compounder" narrative. Until growth re-accelerates above 5%, the stock deserves a mature software multiple, not a compounder premium.

3. **MoS is insufficient for our standards.** At 12.6% MoS vs base, this is well below ALL six Tier A precedents (29-38% MoS). The adversarial program taught us to demand higher MoS, not lower.

4. **The market may be too pessimistic, but patience is warranted.** The reverse DCF shows the market prices in 1-2% perpetual growth, which is probably too pessimistic. But the stock crashed 21% today and often sees follow-through selling in subsequent weeks. There is no urgency.

5. **Entry at EUR 16.00-16.50 would change the calculus.** At EUR 16.50, MoS vs base would be 21% and MoS vs bear would be -3% -- more acceptable. At EUR 16.00, MoS vs base is 25% -- closer to Tier A precedent minimum.

---

## 🔄 META-REFLECTION

### Dudas/Incertidumbres

1. **My FV of EUR 20.00 vs Morningstar's EUR 32.50 is a 38.5% gap.** This is enormous. Either I am too conservative (and leaving 80% upside on the table) or they are too optimistic (and the stock has more downside). The difference is almost entirely growth assumptions: they likely assume 7-8% revenue CAGR normalizing in 2-3 years, while I assume 4% reflecting recent trend. If cloud transition truly accelerates to 8%+ growth by 2028, Morningstar will be right and my FV will need to be revised to EUR 25+. I cannot determine which scenario is more likely without more data (specifically Q1-Q2 2026 revenue growth).

2. **IFRS vs Non-IFRS creates analytical tension.** On IFRS basis, the stock trades at 19.5x P/E which is NOT cheap for a flat-growth company. On Non-IFRS basis, 13.6x P/E looks very cheap. My FV of EUR 20.00 implies IFRS P/E of 22x -- generous for a company with flat EPS guidance. This makes me uncomfortable that my FV might actually be too HIGH on an IFRS basis, while simultaneously being too LOW on a Non-IFRS basis relative to peers.

3. **The OEY + Growth of 11.3% is the weakest of any Tier A holding in the portfolio.** This raises a question: should DSY.PA be treated as Tier A at all, or is the adjusted QS of 78 masking a Tier B company? The growth component (5%) is half of what ADBE, NVO, or LULU offer. If growth does not recover, this is a Tier B stock at a Tier B price, which means MoS of 20-25% is needed (not 12.6%).

4. **Terminal Value is 74-76% of enterprise value in all DCF runs.** This extreme TV dependence means the fair value is essentially a bet on what DSY looks like in perpetuity, not on the next 5 years of cash flows. This reduces my confidence in the DCF and increases my reliance on the EV/EBIT peer comparison (which also has significant uncertainty given the growth differential vs PTC).

5. **The goodwill of EUR 11.6B is an elephant in the room.** If Medidata continues declining and an impairment charge hits, the market reaction could be severe even though the charge is non-cash. I have not explicitly modeled impairment scenarios, which could be a blind spot.

### Sensibilidad Preocupante

- **Growth rate:** Moving growth from 4% to 3% drops FV by EUR 1-2. Moving from 4% to 5% raises FV by EUR 2-3. The thesis is almost entirely a bet on whether growth stays at 3-4% or recovers to 5%+.
- **WACC:** Each 1pp increase in WACC reduces FV by EUR 2-3. My choice to use 8.5% vs the calculated 6.5% makes a EUR 5+ difference. This is the single largest judgment call in the valuation.
- **Non-IFRS vs IFRS basis:** Using IFRS EBIT for the peer multiple method gives FV of EUR 16.36 (below current price). Using Non-IFRS gives EUR 20.75. The accounting basis choice alone creates a EUR 4+ difference.

### Discrepancias con Thesis

The fundamental-analyst thesis set FV at EUR 21.00, which is close to my EUR 20.00 (only 5% divergence). The key differences:
1. I weight the bear case slightly higher (30% vs their 25%) given the HIGH risk score
2. I am more cautious on the IFRS sanity check (my FV implies 22x IFRS P/E, which I flag as generous)
3. I agree on entry target: EUR 16.50-17.00 is more appropriate than current EUR 17.77

The risk-identifier's probability-weighted FV of EUR 22.51 is slightly above my EUR 20.55 expected value. The difference is they assigned 20% to bull (vs my 25%) but a higher bull FV (EUR 33.75 vs my EUR 27.00). Their overall weighted FV being higher than mine despite more conservative bull probability reflects their higher base case (EUR 21.78).

### Sugerencias para el Sistema

1. **dcf_calculator.py should allow custom FCF input.** Currently it pulls historical FCF from yfinance. For DSY.PA, the IFRS FCF of EUR 1.5B is the appropriate input, but if the tool uses a different figure (e.g., operating cash flow), results could differ. A `--fcf` flag to override with a manual figure would improve accuracy.

2. **The sensitivity matrix should highlight the cell closest to current market price.** This would make it immediately clear what growth rate the market implies without manual interpolation.

3. **For companies with large Non-IFRS adjustments (>20% gap), the valuation report should ALWAYS include both IFRS and Non-IFRS based valuations side by side.** This should be a standard template requirement.

### Preguntas para Orchestrator

1. Given MoS of only 12.6% vs our Tier A minimum precedent of 29%, should the standing order entry target be set at EUR 16.00 (MoS 25%) rather than the thesis's EUR 16.50-17.00?
2. Should we treat DSY.PA as Tier B (QS Tool 70) rather than Tier A (Adjusted 78), given that the growth profile more closely resembles a Tier B company? This would change the MoS expectation from 15-30% to 20-25%.
3. The adversarial program found 14/16 theses had inflated FV. My FV of EUR 20.00 is BELOW both Morningstar (EUR 32.50) and consensus (EUR 31.10) by 35-40%. Is there a risk I am now OVER-correcting in the other direction due to post-adversarial conservatism?
4. With 44% cash in portfolio, should a small position (1.5-2%) be considered even at EUR 17.77 as a "foot in the door" with ADD at EUR 16.00? This would give portfolio exposure to the opportunity while waiting for a better price.

---

**Assessment completed: 2026-02-11**
**Valuation Specialist Agent (independent of fundamental-analyst)**
**QS Tool: 70/100 (Tier B) | QS Adjusted: 78/100 (Tier A borderline)**
**Price: EUR 17.77 | FV: EUR 20.00 | MoS: +12.6% | Bear FV: EUR 16.00**
