# ADVERSARIAL VALUATION REPORT: LULU (Lululemon Athletica Inc.)

> **Date:** 2026-02-09
> **Agent:** valuation-specialist (adversarial mode)
> **Purpose:** Independent valuation to challenge thesis FV of $261
> **Price at analysis:** $172.85 / EUR 146.23

---

## EXECUTIVE SUMMARY

The thesis fair value of $261 is INFLATED by approximately 20-30%. The primary errors are:

1. **EPS estimate of $14.50 for "FY26E" is wrong.** LULU's own FY2025 guidance (fiscal year ending Jan 2026) is $12.92-$13.02, and FY2026 consensus (ending Jan 2027) is $12.33-$13.37. The thesis appears to have used a pre-guidance-cut number.

2. **Tariff impact underestimated.** Thesis says "~100bp GM impact, marginal." Actual: 280bp FY2026 gross margin headwind, with Q4 FY2025 alone seeing 580bp compression. Management itself said "negatives will outweigh positives" for FY2026 operating margin.

3. **Only 2 methods used (DCF + P/E), and P/E method used inflated EPS.**

4. **DCF uses default tool parameters** that imply 5% FCF growth -- not derived from projection-framework.

**My risk-adjusted fair value: $192-$205.** MoS vs current price: 10-16%.

---

## 1. CORRECTED FINANCIAL DATA

### FY2025 Actual/Guided Results (Fiscal Year Ending ~Feb 1, 2026)

| Metric | Thesis Assumption | Actual/Guided | Delta |
|--------|-------------------|---------------|-------|
| Revenue | ~$11B implied | $10.96-$11.05B (guided) | ~OK |
| EPS (used for P/E) | $14.50 "FY26E" | $12.92-$13.02 (FY25 guidance) | **-10% to -11%** |
| Operating Margin | 24-25% "normalized" | 23.7% FY25 actual, declining FY26 | Slightly high |
| FCF | ~$1.58B | $1.58B (TTM) | OK |
| ROIC | 25%+ | 27-30% (confirmed) | OK |
| Gross Margin | 59% | 58.5% Q3 FY25 | OK |
| Net Debt | ~$0.73B | Minimal debt, ~net cash | OK |

### Critical EPS Clarification

The thesis states "EPS FY26e: ~$14.50" but this is materially incorrect:

- **LULU's FY2024 actual EPS:** $14.64 (fiscal year ended Feb 2025)
- **FY2025 guidance (ending Jan 2026):** $12.92-$13.02 -- a DECLINE of 11% from FY2024
- **FY2026 consensus (ending Jan 2027):** $12.33-$13.37 (JPMorgan at $12.33, consensus median ~$13.20)

The EPS trajectory is DECLINING, not growing. The thesis $14.50 appears to be a pre-guidance-cut estimate from before Q1 FY2025 (June 2025) when LULU cut guidance from $14.58-$14.78 to the current range due to tariffs and US weakness. Shares tumbled 20% on that cut.

### Revenue Growth Rate Verification

| Period | Revenue | YoY Growth |
|--------|---------|------------|
| FY2022 | $8.11B | +30% |
| FY2023 | $9.62B | +19% |
| FY2024 | $9.62B | +0% (53rd week distortion) |
| FY2025E | $10.96-11.05B | +10% (guided) |
| FY2026E | ~$11.3B | +1.7% (consensus) |

The thesis claims "Revenue CAGR 14%." Over FY2022-FY2025, actual CAGR is approximately 10-11%, and this is decelerating. FY2026 consensus is only +1.7% revenue growth -- a dramatic slowdown driven by tariffs, US weakness, and tougher comps.

### FCF Analysis

Historical FCF:
- FY2022: $0.99B
- FY2023: $0.33B (anomaly -- heavy capex year)
- FY2024: $1.64B
- FY2025E: ~$1.58B (slight decline)

FCF Margin: $1.58B / $10.96B = **14.4%** (thesis said 15%, close enough)

Going forward, FCF will be pressured by:
- Lower operating income from tariffs (280bp GM headwind FY2026)
- Continued investment in international expansion
- No structural capex reduction expected

---

## 2. WACC DERIVATION

### Thesis WACC: 10% (Rf 4%, Beta 1.3, ERP 5%)

| Parameter | Thesis | My Estimate | Source |
|-----------|--------|-------------|--------|
| Risk-Free Rate | 4.0% | 4.3% | 10Y Treasury current |
| Beta | 1.3 | 1.1-1.3 | yfinance 1.01-1.28, TradingView 1.28 |
| ERP | 5.0% | 5.5% | Current elevated ERP environment |
| Ke | 10.5% | 10.4-11.4% | Range based on beta uncertainty |
| Kd | ~4% | ~4% | Minimal debt, nearly irrelevant |
| D/V | ~3% | ~3% | Net cash essentially |
| **WACC** | **10%** | **10.5-11%** | Conservative given CEO uncertainty |

**My WACC: 10.5%**

Rationale for higher WACC:
- CEO transition creates execution uncertainty (interim Co-CEOs, search ongoing, Chip Wilson activist pressure)
- Consumer cyclical in late-cycle economy with tariff headwinds
- Beta of 1.28 (TradingView) with higher ERP of 5.5% = Ke of 11.3%
- Use 10.5% as midpoint, which is conservative but not extreme

---

## 3. MULTI-METHOD VALUATION

### Method 1: DCF (Corrected) -- Weight 40%

**Why 40% not 60%:** DCF is highly sensitive to growth assumptions, and LULU faces unusual uncertainty (CEO transition, tariffs, US deceleration). The range of plausible outcomes is wide, so DCF should get less weight than usual.

**Starting FCF:** $1.58B (FY2025 TTM)
**Growth assumption:** 6% base case (NOT 8-12% as thesis claims)

Derivation of 6% growth:
- FY2026 consensus revenue growth is only +1.7%
- Tariff headwinds compress margins by 280bp in FY2026
- Even if revenue recovers to 7-8% growth in FY2027+, FCF will lag due to margin compression
- International growth (China +46%) will moderate as base grows
- Historical 5Y FCF CAGR is 22%, but this includes pandemic recovery -- unsustainable
- Conservative approach: 4-5% FCF growth years 1-2 (tariff impact), 7-8% years 3-5 (recovery), fading to terminal
- Blended ~6% is appropriate for 5-year DCF

**DCF Results (6% growth, 10.5% WACC, 2.5% terminal):**

| Scenario | Growth/WACC/Terminal | Fair Value | MoS vs $172.85 |
|----------|---------------------|-----------|-----------------|
| Bear | 4%/11.5%/2.0% | $138 | -20.2% |
| Base | 6%/10.5%/2.5% | $203 | +17.3% |
| Bull | 8%/9.5%/3.0% | $277 | +60.0% |

**Expected DCF Value** = (0.25 x $138) + (0.50 x $203) + (0.25 x $277) = **$205**

Note: The DCF tool gave $202.82 for the base case with these exact parameters, confirming.

### Method 2: EV/EBIT Peer Comparison -- Weight 30%

**Peer Group:**

| Peer | P/E (TTM) | EV/EBITDA | Operating Margin | Growth | Notes |
|------|-----------|-----------|-----------------|--------|-------|
| NKE (Nike) | 37.4x | 24.2x | 7.9% | Declining | Turnaround, brand erosion |
| ONON (On Holdings) | 50.5x | 32.8x | ~15% | +30%+ | Hyper-growth |
| GPS (Gap) | ~12x | ~7.9x | ~7% | Flat | Mass market |
| UAA (Under Armour) | N/A | N/A | Negative | Turnaround | Distressed |
| VFC (VF Corp) | 35.7x | N/A | Low | Declining | Turnaround |

**LULU current:** P/E 12.0x, EV/EBITDA ~8.4x

**Analysis:**
- Nike at 24x EV/EBITDA has WORSE margins (7.9% vs LULU ~24%) and worse growth
- ONON at 33x is hyper-growth and not comparable (much higher growth, smaller base)
- Gap at 8x EV/EBITDA is mass-market with much lower margins
- LULU should trade BETWEEN Gap and Nike given its superior margins but decelerating growth

**LULU's Normalized EBIT:**
- FY2025E operating income: ~$2.5B (23.7% margin on $10.58B revenue)
- FY2026E operating income: ~$2.2-2.3B (assuming 280bp margin compression from tariffs on ~$11.3B revenue = ~20-21% margin)
- Normalized (mid-cycle) EBIT: ~$2.3-2.5B

**Appropriate EV/EBIT multiple for LULU:**
- Sector median (retail): 10-12x
- Premium for superior margins (+23pp vs sector): +2-3x
- Premium for brand moat: +1-2x
- Discount for decelerating growth: -2x
- Discount for CEO uncertainty: -1x
- **Fair multiple: 12-14x EV/EBIT**

**Valuation:**
- Conservative (12x on $2.3B EBIT): EV = $27.6B - $0.73B net debt = $26.9B / 118.6M shares = **$227/share**
- Midpoint (13x on $2.4B EBIT): EV = $31.2B - $0.73B = $30.5B / 118.6M = **$257/share**
- Aggressive (14x on $2.5B EBIT): EV = $35.0B - $0.73B = $34.3B / 118.6M = **$289/share**

Weighted (toward conservative given current headwinds): **$237/share**

Wait -- I need to sanity check this. At $237 = P/E of 237/13 = 18.2x on FY2025 EPS. That seems high for a company with declining EPS trajectory. Let me use FY2026 estimates:

On FY2026 consensus EPS of ~$13.20: $237/$13.20 = 18.0x forward P/E. Nike trades at 37x (in worse shape), ONON at 50x. 18x for LULU with 25%+ ROIC is actually defensible.

But the normalized EBIT approach assumes tariffs are temporary. If tariffs persist (which they might under current trade policy), the EBIT stays at $2.2-2.3B, and at 12x that gives:
- 12x on $2.25B = $27B EV, $26.3B equity = **$222/share**

**Method 2 Fair Value: $222** (conservative, tariffs persist) to **$237** (mid-case)
**Using $225 as base estimate.**

### Method 3: P/E Forward with Corrected EPS -- Weight 30%

**Corrected EPS Estimates:**

| Period | EPS | Source |
|--------|-----|--------|
| FY2025 (ending Jan 2026) | $12.92-$13.02 | Company guidance |
| FY2026 (ending Jan 2027) | $12.33-$13.37 | Analyst consensus |
| FY2027 (ending Jan 2028) | $12.40-$12.57 | Limited estimates |

**Appropriate P/E Multiple:**
- LULU 5-year avg P/E: 40x (when growth was 20%+)
- LULU 3-year avg P/E: 31x (growth decelerating)
- Current P/E: 12x (market pricing in permanent decline)
- Thesis used 20x -- what's justified?

Rational P/E framework for LULU:
- For a company with ROIC 25-30%, GM 58%, but DECLINING EPS and CEO uncertainty
- PEG ratio approach: If EPS grows 5-8% from current base, PEG of 1.5-2.0x = P/E of 7.5-16x
- If we believe in mean reversion to 8-10% EPS growth over 2-3 years: P/E 15-18x
- If current EPS decline is permanent: P/E 10-12x (current pricing)

**Scenario analysis:**

| Scenario | Forward EPS (FY26) | P/E Multiple | Fair Value | Probability |
|----------|-------------------|-------------|-----------|-------------|
| Bear: Permanent decline | $12.00 | 12x | $144 | 25% |
| Base: Stabilize, slow recovery | $13.00 | 15x | $195 | 50% |
| Bull: Product refresh works | $14.00 | 18x | $252 | 25% |

**Expected P/E Value** = (0.25 x $144) + (0.50 x $195) + (0.25 x $252) = **$196**

Critical difference vs thesis: Thesis used $14.50 EPS at 20x = $290. My corrected numbers: $13.00 EPS at 15x = $195. The thesis was 49% higher -- almost half from the inflated EPS, half from the higher multiple.

### Method 4: Reverse DCF (Sanity Check)

At current price $172.85:
- Market Cap: ~$20.5B
- EV: ~$21.2B
- Using WACC 10.5%, terminal growth 2.5%:

The DCF tool with 7% growth gave $211, and with 4% growth/11% WACC gave $167.

This means current price implies approximately **4-5% perpetual FCF growth** -- which is NOT "no growth" as the thesis claims. Given that:
- FY2026 revenue growth is only 1.7%
- Margins are compressing
- CEO transition ongoing

4-5% implied growth is actually reasonable to slightly pessimistic, not "extremely pessimistic" as the thesis claims.

---

## 4. RECONCILIATION

| Method | Fair Value | Weight | Weighted |
|--------|-----------|--------|----------|
| DCF (corrected, base) | $203 | 40% | $81 |
| EV/EBIT (conservative) | $225 | 30% | $68 |
| P/E Forward (corrected) | $196 | 30% | $59 |
| **Weighted Average** | | 100% | **$207** |

**Divergence between methods:** DCF $203 vs P/E $196 = 3.6% (well within 30% threshold)

### Comparison vs Thesis

| Metric | Thesis | Adversarial | Delta |
|--------|--------|-------------|-------|
| DCF Base | $241 | $203 | **-16%** |
| P/E Method | $290 | $196 | **-32%** |
| Weighted FV | $261 | $207 | **-21%** |
| Bear Case | $190 | $144 | **-24%** |
| Expected Value | $246 | $192 | **-22%** |
| MoS vs Weighted | 34% | 16% | **-18pp** |

**Key drivers of the gap:**
1. **EPS correction:** $14.50 -> $13.00 = -10% impact on P/E method
2. **P/E multiple:** 20x -> 15x = -25% impact on P/E method
3. **Growth rate:** 5% default -> 6% corrected (similar, but WACC higher)
4. **WACC:** 10% -> 10.5% = -8% impact on DCF
5. **Tariff headwind** absent from thesis: 280bp FY2026 gross margin impact

---

## 5. SCENARIOS (CORRECTED)

### Bear Case (25% probability) -- $144

**Assumptions:**
- US business remains negative comps through FY2027
- International growth decelerates to 10-15% (China regulatory risk, competition)
- Tariffs persist and expand (China tensions escalate)
- New CEO is mediocre or search is prolonged >12 months
- Alo/Vuori continue gaining 2-3pp share annually
- EPS declines to $11-12 range
- Market applies 12x P/E (permanent de-rating)

**DCF equivalent:** $138 (4% growth, 11.5% WACC)

### Base Case (50% probability) -- $200

**Assumptions:**
- US stabilizes by Q2-Q3 FY2026, low-single-digit growth FY2027+
- International maintains 15-20% growth (deceleration from 33%)
- Tariff impact partially mitigated by FY2027 (supply chain shift to Vietnam/Cambodia)
- New CEO hired by mid-2026, competent but not transformational
- GM stabilizes at 56-57% (vs 58.5% current) after tariff absorption
- EPS recovers to $13-14 range by FY2027
- Market applies 15-16x P/E

**DCF equivalent:** $203 (6% growth, 10.5% WACC)

### Bull Case (25% probability) -- $255

**Assumptions:**
- Product refresh drives US comps positive by Q1 FY2026
- China continues 30%+ growth
- Tariffs rolled back or fully mitigated
- New CEO is exceptional (from a successful DTC brand)
- Buybacks accelerate with recovered FCF
- EPS recovers to $14+ by FY2027
- Market re-rates to 18-20x P/E

**DCF equivalent:** $277 (8% growth, 9.5% WACC)

### Expected Value

**EV = (0.25 x $144) + (0.50 x $200) + (0.25 x $255) = $200**

| Scenario | Fair Value | Probability | Contribution |
|----------|-----------|-------------|-------------|
| Bear | $144 | 25% | $36.00 |
| Base | $200 | 50% | $100.00 |
| Bull | $255 | 25% | $63.75 |
| **Expected** | **$200** | 100% | **$199.75** |

---

## 6. CEO TRANSITION SCENARIO ANALYSIS (Binary Event)

| Scenario | Description | Impact on FV | Probability |
|----------|-------------|-------------|-------------|
| **Great CEO** | Experienced DTC/retail leader (e.g., from Nike, Adidas, Williams-Sonoma caliber) | +15-20% to base ($230-$240) | 25% |
| **Adequate CEO** | Competent operator, maintains trajectory | 0% (base case already assumes this) | 40% |
| **Bad CEO** | Wrong fit, internal politics, strategy confusion | -15-20% ($160-$170) | 20% |
| **Prolonged search** | >12 months with Co-CEOs, strategic drift | -10% ($180) | 15% |

**CEO-adjusted EV** = (0.25 x $235) + (0.40 x $200) + (0.20 x $165) + (0.15 x $180) = **$199**

This is nearly identical to the scenario-weighted EV of $200, confirming that the base case already incorporates appropriate CEO uncertainty.

The Chip Wilson activist angle adds another layer of uncertainty. If Wilson gains board seats, he could push for:
- Accelerated CEO replacement (potentially positive)
- Return to founder's vision (mixed -- could alienate evolved customer base)
- Board disruption during critical transition period (negative short-term)

---

## 7. SENSITIVITY ANALYSIS

### DCF Sensitivity Table (Fair Value per Share)

| WACC \ Growth | 4% | 5% | 6% | 7% | 8% |
|---------------|-----|-----|-----|-----|-----|
| **9.5%** | $199 | $218 | $241 | $270 | $304 |
| **10.0%** | $185 | $202 | $222 | $247 | $277 |
| **10.5%** | $173 | $188 | $203 | $225 | $252 |
| **11.0%** | $162 | $175 | $191 | $209 | $230 |
| **11.5%** | $152 | $164 | $178 | $194 | $213 |

**Key observation:** At 10.5% WACC, you need 7%+ FCF growth to get above $220. Given FY2026 revenue growth of only 1.7% and margin compression, achieving 7% FCF growth in the near term is challenging.

### P/E Sensitivity Table (Fair Value per Share)

| P/E \ EPS | $12.00 | $12.50 | $13.00 | $13.50 | $14.00 |
|-----------|--------|--------|--------|--------|--------|
| **12x** | $144 | $150 | $156 | $162 | $168 |
| **14x** | $168 | $175 | $182 | $189 | $196 |
| **16x** | $192 | $200 | $208 | $216 | $224 |
| **18x** | $216 | $225 | $234 | $243 | $252 |
| **20x** | $240 | $250 | $260 | $270 | $280 |

**To reach thesis FV of $261:** You need either 20x P/E on $13.00 EPS, or 18x on $14.50 EPS. The first requires the market to nearly double the current P/E from 12x; the second requires EPS to be $1.50 higher than current guidance.

### Validation vs Peers

LULU's current multiples vs peers:

| Multiple | LULU | NKE | ONON | GPS | Sector Median |
|----------|------|-----|------|-----|---------------|
| P/E TTM | 12.0x | 37.4x | 50.5x | 12.3x | ~15x |
| EV/EBITDA | 8.4x | 24.2x | 32.8x | 7.9x | ~10x |

At my FV of $200, implied P/E = $200/$13.00 = 15.4x. This is:
- Below NKE (37x) -- appropriate given LULU has better margins but worse momentum
- Below sector median (~15x) -- approximately at median, defensible for company with temporary headwinds
- Above GPS (12x) -- appropriate given LULU's vastly superior margins and ROIC

### Validation vs Adversarial Precedents

| Ticker | Thesis FV | Adversarial FV | Delta | Reason |
|--------|-----------|----------------|-------|--------|
| MONY.L | -- | -27% | -- | FV inflated |
| EDEN.PA | -- | -24.5% | -- | FV inflated |
| A2A.MI | EUR 2.70 | EUR 2.04 | -24% | SOLD |
| VNA.DE | EUR 32.58 | EUR 24.35 | -25% | SOLD |
| **LULU** | **$261** | **$200-207** | **-21 to -23%** | **Consistent with pattern** |

The delta is consistent with the system-wide pattern of 15-25% FV inflation in original theses.

---

## 8. FINAL VALUATION SUMMARY

```
VALUATION: LULU

Type of Company: Consumer Cyclical / Retail Premium
Quality Tier: A (QS 82) -- CONFIRMED, quality metrics check out
Methods Selected: DCF + EV/EBIT + P/E Forward (3 methods)

Method 1: DCF (Corrected)
- Inputs: FCF $1.58B, Growth 6%, WACC 10.5%, Terminal 2.5%
- Fair Value: $203

Method 2: EV/EBIT Peer Comparison
- Inputs: Normalized EBIT $2.3B, Multiple 12-13x
- Fair Value: $225

Method 3: P/E Forward (Corrected EPS)
- Inputs: FY2026 EPS $13.00, Multiple 15x
- Fair Value: $195

Reconciliation:
| Method       | FV    | Weight | Weighted |
|-------------|-------|--------|----------|
| DCF          | $203  | 40%    | $81      |
| EV/EBIT      | $225  | 30%    | $68      |
| P/E Forward  | $196  | 30%    | $59      |
| **Weighted** |       | 100%   | **$207** |

Divergence: Max 15% (EV/EBIT vs P/E) -- within 30% threshold

Scenarios:
| Scenario     | Fair Value | Prob |
|-------------|-----------|------|
| Bear         | $144      | 25%  |
| Base         | $200      | 50%  |
| Bull         | $255      | 25%  |
| **Expected** | **$200**  | 100% |

Current Price: $172.85 / EUR 146.23
MoS vs Weighted FV ($207): +16.5%
MoS vs Expected ($200): +13.6%
MoS vs Bear ($144): -16.7% (LOSES money in bear case)
```

---

## 9. IMPLICATIONS FOR POSITION

The adversarial fair value of $200-$207 represents a meaningful reduction from the thesis $261:

**At current price $172.85:**
- MoS vs adversarial FV: **+16%** (thesis claimed 34%)
- MoS vs Bear case: **-17%** (thesis claimed -10%)

For a Tier A compounder, 16% MoS is at the LOW END of acceptable (precedents show 30-40% for recent buys). However, the quality metrics (ROIC 25-30%, GM 58.5%, net cash) are genuinely strong.

**Assessment:** The position is not a SELL, but it was bought at a price that offers limited margin of safety after adversarial correction. The entry at $171.62 is close to fair value, not deeply discounted as the thesis suggested.

**Key risk:** If bear case materializes (EPS declines to $11-12, market applies 12x), the position could lose 17%. For a 3.5% position, that is 0.6% portfolio impact -- manageable.

**Key catalyst:** Q4 FY2025 earnings (March 26-31, 2026) will reveal:
1. Holiday quarter results (ICR indicated "high end of guidance")
2. First FY2026 guidance including full tariff impact
3. CEO search update

---

## META-REFLECTION

### Dudas/Incertidumbres
- **FCF base year selection:** The DCF tool uses $1.58B (FY2025 TTM). If FY2026 FCF drops to $1.3-1.4B due to tariff margin compression, the DCF base is overstated. This is the single biggest uncertainty in my valuation.
- **EV/EBIT method gave higher FV ($225) than other methods.** This might be because I'm using "normalized" EBIT that assumes tariff mitigation over time. If tariffs persist, the EV/EBIT FV should be closer to $200.
- **Multiple selection is inherently subjective.** Why 15x P/E and not 13x or 17x? The range of reasonable multiples creates a wide FV band.

### Sensibilidad Preocupante
- A 2pp change in WACC (9.5% to 11.5%) swings DCF FV from $241 to $178 -- a $63 range (35% swing)
- A 2x change in P/E (14x to 16x) on the same EPS swings FV by $26 (13% swing)
- The DCF is more sensitive than the P/E method, which is why I weighted it 40% not 60%

### Discrepancias con Thesis
The thesis FV of $261 is inflated by 21-23%. The main culprits:
1. Using pre-cut EPS of $14.50 vs actual guidance of $12.92-$13.02 (accounts for ~40% of the gap)
2. Using 20x P/E vs my 15x (accounts for ~35% of the gap)
3. DCF with lower WACC and default parameters (accounts for ~25% of the gap)

The thesis correctly identifies LULU as a quality business (QS 82 confirmed) with cyclical not structural problems. The bull case for the business is intact. But the PRICE PAID matters, and at $172 the margin of safety is thin, not deep.

### Sugerencias para el Sistema
1. **ALWAYS verify EPS estimates against current guidance.** The $14.50 EPS was stale data that inflated the P/E valuation by 32%.
2. **The DCF tool's default parameters (5% growth, 9% WACC) produced a $241 FV that appears in the thesis.** This suggests the analyst may have simply run the default and accepted the output without deriving parameters from the projection-framework. Enforce the rule: "NEVER DCF without projection-framework."
3. **Tariff impact should be a standard check** for all US-listed companies with significant international manufacturing (especially China/Vietnam sourcing).

### Preguntas para Orchestrator
1. **Should conviction be downgraded from HIGH to MEDIUM?** The MoS at 16% is well below the 30-40% range for recent Tier A buys (ADBE 31%, NVO 38%, MONY.L 36%). Is this position "earning its place"?
2. **Should the ADD triggers be revised?** Thesis has ADD at $160 and $145. With adversarial FV of $200, an ADD at $160 would still only give MoS of 20% -- still below typical Tier A entry points.
3. **Q4 earnings (late March) is a critical event.** First FY2026 guidance will confirm or refute the tariff impact severity. Consider waiting for this data before any ADD.

---

## Sources

- [Lululemon Q4 FY2025 Guidance Update (ICR Conference, Jan 12, 2026)](https://corporate.lululemon.com/media/press-releases/2026/01-12-2026-113012292)
- [JPMorgan Raises LULU Q4 EPS, FY2026 at $12.33](https://finance.yahoo.com/news/jpmorgan-raises-lululemon-lulu-q4-122128344.html)
- [Lululemon CEO Succession Plan](https://corporate.lululemon.com/media/press-releases/2025/12-11-2025-210527531)
- [LULU Q3 FY2025 Earnings Press Release](https://corporate.lululemon.com/media/press-releases/2025/12-11-2025-210611862)
- [LULU Q3 FY2025 Earnings Call Transcript (Motley Fool)](https://www.fool.com/earnings/call-transcripts/2025/12/12/lululemon-lulu-q3-2025-earnings-call-transcript/)
- [LULU Stock Forecast & Analyst Consensus (StockAnalysis)](https://stockanalysis.com/stocks/lulu/forecast/)
- [LULU Analyst Consensus (MarketBeat)](https://www.marketbeat.com/stocks/NASDAQ/LULU/forecast/)
- [Lululemon SWOT Analysis - Tariff Impact (Investing.com)](https://www.investing.com/news/swot-analysis/lululemons-swot-analysis-stock-faces-headwinds-as-us-growth-slows-tariffs-bite-93CH-4278441)
- [LULU EV/EBITDA (GuruFocus)](https://www.gurufocus.com/term/enterprise-value-to-ebitda/LULU)
- [LULU ROIC (GuruFocus)](https://www.gurufocus.com/term/roic/LULU)
- [Nike EV/EBITDA (GuruFocus)](https://www.gurufocus.com/term/enterprise-value-to-ebitda/NKE)
- [LULU Historical Free Cash Flow (MacroTrends)](https://www.macrotrends.net/stocks/charts/LULU/lululemon-athletica-inc/free-cash-flow)
- [Lululemon Shares Tumble 20% on Guidance Cut (CNBC, June 2025)](https://www.cnbc.com/2025/06/05/lululemon-lulu-earnings-q1-2025.html)
- [Chip Wilson Nominates Board Candidates (Retail TouchPoints)](https://www.retailtouchpoints.com/features/retail-movers-and-shakers/mcdonald-steps-down-as-lululemon-leader-company-begins-search-for-new-ceo)
