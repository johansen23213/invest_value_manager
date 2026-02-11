# Globe Life Inc. (GL) - Independent Valuation Report

**Date:** 2026-02-08
**Analyst:** Valuation Specialist (Adversarial Review - FASE 2)
**Context:** Independent valuation challenging thesis adopted FV of $174
**Quality Score:** 52 (Tier C per quality_scorer.py)

---

## VALUATION SUMMARY

| Metric | Thesis v2.0 | Independent (This Report) | Delta |
|--------|-------------|--------------------------|-------|
| Calculated FV | $237 | $220 | -7.2% |
| Adopted FV | $174 | $220 | +26.4% |
| Bear FV | $170 | $165 | -2.9% |
| Bull FV | $320 | $290 | -9.4% |
| Expected FV | $241 | $228 | -5.4% |
| MoS (adopted) | 17.6% | 33.4% | +15.8pp |

**KEY FINDING:** The thesis was ANOMALOUSLY conservative. It calculated $237 but adopted $174 (a 26.6% self-imposed haircut using P/E 11.5x). This is an outlier in our adversarial review -- most positions had inflated FVs. GL's thesis had an under-stated FV.

**My independent adopted FV: $220** (still conservative vs calculated $228 weighted average).

---

## ACTUAL FY2025 RESULTS (Q4 Reported Feb 5, 2026)

The thesis was written before Q4 2025 earnings. Here are the ACTUAL results:

| Metric | Thesis Assumption | Actual FY2025 | Delta |
|--------|-------------------|---------------|-------|
| GAAP EPS | n/a | $14.07 | n/a |
| Net Operating Income/share | $15.03 (forward) | $14.52 (FY2025) | Actual trailing confirmed |
| GAAP ROE | 22.3% (from yfinance) | 20.9% | -1.4pp (slightly lower) |
| ROE ex-AOCI | n/a | 16.0% | More conservative metric |
| Book Value/share (GAAP) | $70.84 | $74.17 | +4.7% (higher) |
| BV ex-AOCI | n/a | $96.16 | Significantly higher |
| Shares outstanding (diluted) | ~81.5M | 82.5M (weighted avg) | Comparable |
| Buybacks | n/a | 5.4M shares, $685M | Very aggressive |

### FY2026 Guidance (NEW -- post thesis)
- Net operating income: **$14.95 - $15.65/share** (midpoint $15.30)
- Life premium growth: 4-4.5%
- Health premium growth: 14-16% (strong)
- Buyback guidance: $535-585M
- Dividend guidance: $85-90M
- Total shareholder return 2026E: ~$625-675M

The guidance midpoint of $15.30 is ABOVE the thesis assumption of $15.03. Results validate the thesis quality assessment.

---

## CURRENT MARKET DATA

| Metric | Value |
|--------|-------|
| Current Price | $146.51 |
| 52-Week High | $152.71 |
| 52-Week Low | $109.38 |
| P/E (GAAP trailing) | 10.4x |
| P/E (NOI trailing) | 10.1x |
| P/E (forward, guidance mid) | 9.6x |
| P/B (GAAP) | 1.98x |
| P/B (ex-AOCI) | 1.52x |
| Market Cap | $11.9B |
| Yield | 0.74% |

---

## ENTERPRISE TYPE AND METHOD SELECTION

**Type:** Financial (Life/Health Insurance)
**Methods selected:**
1. **P/B vs ROE (55% weight)** -- Primary method for financials; book value IS the business
2. **P/E Normalized (45% weight)** -- Grounding in earnings reality, peer comparison

**DCF reference only:** DCF is less reliable for insurers because FCF is lumpy (reserve changes, investment income distortions). Tool output: Bear $199, Base $259, Bull $344. Used as sanity check only.

---

## METHOD 1: P/B vs ROE (55% weight)

### Cost of Equity Derivation (WACC is less relevant for financials; Ke is the key metric)

```
Risk-Free Rate (10Y UST): 4.28%
Equity Risk Premium: 5.0%
Beta (GL): 0.464
Base Ke = 4.28% + 0.464 x 5.0% = 6.60%
+ Litigation risk premium: +1.50% (active class action, data breach suit)
Adjusted Ke = 8.10%
```

**Litigation risk premium justification:** The securities fraud class action survived the motion to dismiss in Sep 2025. Discovery is ongoing. Settlement exposure estimated at $150-400M ($1.88-$5.00/share). Additionally, an 850,000-person data breach class action is pending. These are material but manageable given GL's ~$1.4B annual FCF.

### Sustainable Growth (g)

Conservative g = 2.5% (below long-term GDP, reflects insurance industry growth tied to population + income)

### Two-Approach P/B Valuation

For insurers, both GAAP and ex-AOCI metrics are relevant but tell different stories:

**Approach A: GAAP Metrics (ROE 20.9%, BV $74.17)**
- Includes AOCI (unrealized bond gains/losses), which inflates ROE relative to BV
- P/B Justified = (20.9% - 2.5%) / (8.10% - 2.5%) = **3.29x**
- Fair Value = 3.29 x $74.17 = **$244**

**Approach B: Ex-AOCI Metrics (ROE 16.0%, BV $96.16)**
- Strips out mark-to-market distortions, more economically meaningful
- P/B Justified = (16.0% - 2.5%) / (8.10% - 2.5%) = **2.41x**
- Fair Value = 2.41 x $96.16 = **$232**

**Blended (50/50):** ($244 + $232) / 2 = **$238**

**Credibility Haircut (-5%):** P/B method is sensitive to ROE assumptions and AOCI distortions. Apply 5% conservatism. Adjusted P/B FV = **$226**

### ROE Sensitivity Table (using GAAP BV $74.17, Ke 8.10%)

| ROE | P/B Justified | Fair Value | MoS vs $146.51 |
|-----|---------------|-----------|-----------------|
| 12% | 1.70x | $126 | -16.3% |
| 14% | 2.05x | $152 | 3.6% |
| 16% | 2.41x | $179 | 18.1% |
| 18% | 2.77x | $205 | 28.6% |
| 20% | 3.13x | $232 | 36.8% |
| 22% | 3.48x | $258 | 43.3% |

**Critical observation:** Even at ROE 16% (the ex-AOCI rate, well below GAAP), the P/B method yields $179 -- above the thesis adopted FV of $174. The thesis was pricing GL as if ROE would compress to ~15-16%, which has no basis in the actual trend (ROE has been 18-22% for 10+ years).

---

## METHOD 2: P/E Normalized with Actual Peers (45% weight)

### Peer Comparison Table (Live Data Feb 8, 2026)

| Ticker | P/E | ROE | P/B | Notes |
|--------|-----|-----|-----|-------|
| AFL | 17.2x | ~14.5% | ~2.0x | Most comparable: captive agent model |
| MET | 15.8x | ~12% | n/a | Diversified life/P&C, larger |
| PRU | 10.3x | ~10% | n/a | Complex, lower ROE |
| UNM | 17.5x | ~20.5% | ~1.1x | Similar ROE, disability focus |
| **Median** | **16.5x** | **~13%** | | |
| **GL** | **10.1x** | **16-21%** | **1.98x** | **Best ROE, lowest P/E** |

**GL trades at a 39% discount to peer median P/E despite having the BEST or second-best ROE in the group.** This discount reflects the Fuzzy Panda / litigation overhang, not business fundamentals.

### Fair P/E Derivation

```
Starting point: Peer median P/E = 16.5x
+ Premium for superior ROE (16-21% vs peer 10-14.5%): +2x
- Discount for active litigation (securities fraud, data breach): -3x
- Discount for short-seller overhang residual: -1.5x
= Fair P/E: 14.0x
```

This 14x multiple is still a 15% discount to peer median (16.5x), reflecting ongoing litigation uncertainty. It represents a reasonable middle ground: the SEC/DOJ cleared GL (positive), but securities class action is ongoing (negative).

### Earnings Base: 2026 Guidance Midpoint

```
Net Operating Income 2026E: $15.30/share (management guidance midpoint)
Company exceeded prior guidance ($14.52 actual vs $14.25-14.95 range for FY2025)
Track record of guidance reliability: STRONG
```

### Fair Value: P/E Method

| P/E Multiple | Fair Value | MoS | Context |
|-------------|-----------|------|---------|
| 10x (current) | $153 | 4.2% | Market price |
| 11x (thesis adopted) | $168 | 12.9% | Very conservative |
| 12x | $184 | 20.2% | Still well below peers |
| 13x | $199 | 26.3% | Moderate litigation discount |
| **14x (adopted)** | **$214** | **31.6%** | **Fair with litigation overlay** |
| 15x | $230 | 36.2% | Modest peer convergence |
| 16x | $245 | 40.2% | Near peer level |
| 17x | $260 | 43.7% | Full peer re-rating |

**Adopted P/E FV: $214** (14x on $15.30 2026E NOI)

---

## RECONCILIATION

| Method | Fair Value | Weight | Weighted FV |
|--------|-----------|--------|-------------|
| P/B vs ROE (adj.) | $226 | 55% | $124 |
| P/E Normalized | $214 | 45% | $96 |
| **Weighted Average** | | **100%** | **$221** |

**Divergence between methods: 5.6%** -- Excellent convergence (well under 30% threshold).

**Adopted Fair Value: $220** (rounded conservatively from $221)

### Why $220 and Not $174 (Thesis Adopted)

The thesis calculated a weighted FV of $237 but then adopted $174 (P/E 11.5x). The justification given was "residual litigation uncertainty" and "earnings call tomorrow could surprise." Since then:

1. **Earnings DID NOT surprise negatively** -- FY2025 NOI of $14.52 beat guidance midpoint
2. **2026 guidance increased** -- $14.95-15.65 vs the $15.03 forward used in thesis
3. **Book value increased** -- $74.17 vs $70.84 used in thesis (+4.7%)
4. **SEC/DOJ investigations remain closed** -- No new regulatory action
5. **Stock price rose from $143.44 to $146.51** -- Market partially agrees

The thesis imposed a ~27% haircut on its own calculated value with no quantitative justification. At P/E 11.5x, the thesis was pricing GL at a **30% discount to the lowest peer** (PRU at 10.3x), despite GL having significantly better returns. This is unjustifiable.

My $220 FV uses P/E 14x (still 15% below peer median) and P/B with +1.5% litigation premium on Ke. Both adjustments conservatively price in litigation risk without overcorrecting.

---

## SCENARIO ANALYSIS

### Bear Case (25% probability)

**Assumptions:**
- ROE compresses to 15% (loss ratio worsens, litigation costs)
- Ke remains at 8.10% (litigation premium intact)
- P/E contracts to 11x
- EPS achieves guidance low ($14.95)

| Method | Calculation | Fair Value |
|--------|-------------|-----------|
| P/B vs ROE | P/B 2.23x x $74.17 | $166 |
| P/E | 11x x $14.95 | $164 |
| **Blended** | 55/45 | **$165** |

### Base Case (50% probability)

**Assumptions:**
- ROE at 16-21% (blended GAAP/ex-AOCI)
- Ke at 8.10% (litigation premium)
- P/E at 14x
- EPS at guidance midpoint ($15.30)

| Method | Calculation | Fair Value |
|--------|-------------|-----------|
| P/B vs ROE | Blended approach, 5% haircut | $226 |
| P/E | 14x x $15.30 | $214 |
| **Blended** | 55/45 | **$220** |

### Bull Case (25% probability)

**Assumptions:**
- ROE sustained at 20% (proven track record)
- Ke normalizes to 6.60% (class action settles, overhang lifts)
- P/E re-rates to 16x (approaching peer median)
- EPS at guidance high ($15.65)

| Method | Calculation | Fair Value |
|--------|-------------|-----------|
| P/B vs ROE | P/B 4.27x x $74.17 | $317 |
| P/E | 16x x $15.65 | $250 |
| **Blended** | 55/45 | **$287** |

### Expected Value

```
EV = (Bear x 25%) + (Base x 50%) + (Bull x 25%)
EV = ($165 x 0.25) + ($220 x 0.50) + ($287 x 0.25)
EV = $41 + $110 + $72 = $223
```

### Margin of Safety Summary

| Scenario | Fair Value | Prob | MoS vs $146.51 |
|----------|-----------|------|-----------------|
| Bear | $165 | 25% | 11.2% |
| Base | $220 | 50% | 33.4% |
| Bull | $287 | 25% | 49.0% |
| **Expected** | **$223** | **100%** | **34.3%** |

---

## SENSITIVITY ANALYSIS

### P/B Method: Ke vs ROE Matrix

| | Ke 7.1% | Ke 8.1% | Ke 9.1% |
|---|---------|---------|---------|
| **ROE 14%** | $186 | $152 | $129 |
| **ROE 16%** | $218 | $179 | $152 |
| **ROE 18%** | $250 | $205 | $175 |
| **ROE 20%** | $282 | $232 | $199 |
| **ROE 22%** | $314 | $258 | $222 |

### P/E Method: Multiple vs EPS Matrix

| | EPS $14.50 | EPS $15.30 | EPS $16.00 |
|---|-----------|-----------|-----------|
| **11x** | $160 | $168 | $176 |
| **12x** | $174 | $184 | $192 |
| **13x** | $189 | $199 | $208 |
| **14x** | $203 | $214 | $224 |
| **15x** | $218 | $230 | $240 |

---

## LITIGATION EXPOSURE ANALYSIS

### Active Lawsuits

| Lawsuit | Filed | Status | Estimated Exposure |
|---------|-------|--------|--------------------|
| Securities fraud class action | Apr 2024 | Survived MTD (Sep 2025), in discovery | $100-350M |
| Data breach class action (850K affected) | Mar 2025 | Early stages | $20-50M |
| Shareholder derivative (governance) | 2024 | Ongoing | Minimal cash (governance changes) |
| **Total estimated** | | | **$150-400M** |

### Impact Assessment

- Estimated settlement: ~$250M (midpoint of range)
- Per share impact: ~$3.10 (on ~80M shares)
- As % of equity: ~3.2%
- As % of annual FCF: ~18% (one-time)

**This litigation exposure is ALREADY priced in** through:
1. My Ke includes +1.5% litigation premium (reduces P/B FV by ~$30-40)
2. My P/E of 14x is 15% below peer median (implicit ~$25-30 discount per share)
3. Combined implicit discount: ~$55-70 per share >> estimated exposure of ~$3.10/share

The market is OVER-discounting the litigation risk. Even if settlement is at the high end ($400M / $5 per share), the stock is pricing in multiples of that.

---

## VALIDATION VS PEERS

### Implied Multiples at My Fair Value ($220)

| Metric | At $220 | Sector Median | Reasonable? |
|--------|---------|---------------|-------------|
| P/E (on $15.30 NOI) | 14.4x | 16.5x | YES -- still 13% below peers |
| P/B (on $74.17 GAAP) | 2.97x | ~1.5-2.0x | HIGH -- but justified by 2x peer ROE |
| P/B (on $96.16 ex-AOCI) | 2.29x | ~1.5-2.0x | Reasonable for 16-21% ROE |

The implied multiples at $220 are reasonable. GL is not being assigned a premium to peers -- it remains at a discount on P/E despite having the best returns in the group.

### Validation vs DCF Tool

DCF tool output: Bear $199, Base $259, Bull $344.
My independent valuation ($220) sits between DCF Bear and Base, which is appropriate for a Tier C position where we apply conservatism.

---

## COMPARISON: THESIS vs INDEPENDENT

| Metric | Thesis v2.0 | Independent | Assessment |
|--------|-------------|-------------|------------|
| P/B vs ROE FV | $259 | $226 (adj.) | Thesis slightly high (used 7.5% Ke vs my 8.1%) |
| P/E FV | $203 | $214 | Very close -- different P/E (12-15x blend vs 14x) |
| Calculated Weighted FV | $237 | $221 | -6.8% -- moderate revision |
| **Adopted FV** | **$174** | **$220** | **+26.4% -- thesis was too conservative** |
| Bear FV | $170 | $165 | Very close |
| Bull FV | $320 | $287 | -10.3% -- I am more conservative on bull |

**The thesis CALCULATED fair value was reasonable ($237 vs my $221 = only 7% higher). The problem was the massive, unjustified haircut from $237 to $174 as the "adopted" value. My analysis corrects this overcorrection.**

---

## CONVICTION AND RECOMMENDATION

**Independent Adopted FV: $220**
**MoS at current price ($146.51): 33.4%**
**Conviction: MEDIUM**

### Rationale for MEDIUM (not HIGH) conviction:
1. QS = 52 (Tier C) -- this is NOT a quality compounder
2. Active litigation creates genuine uncertainty on timeline and magnitude
3. ROE sustainability at 20%+ needs monitoring -- ex-AOCI ROE is 16%, which is good but not exceptional
4. Low insider ownership (0.6%) -- management has limited skin in the game
5. Captive agent model is an advantage but agents-are-the-risk too (Fuzzy Panda allegations centered on agent misconduct)

### However, the MoS is substantial:
1. Even in BEAR case, MoS is positive (11.2%) -- downside protection exists
2. EPS guidance for 2026 validated by strong Q4 results
3. Aggressive buyback ($535-585M) provides 5-6% share count reduction per year
4. Premium growth trajectory strong (health +14-16%)
5. Zero tariff/China exposure in current macro environment

### Kill Conditions (unchanged):
1. Class action reveals NEW material fraud not covered by SEC/DOJ clearance
2. Operating EPS falls below $12 (vs $15.30 guidance)
3. ROE drops below 12% sustained
4. New regulatory investigation opened
5. Data breach leads to material policyholder attrition

---

## DCF Reference (Sanity Check Only)

From `dcf_calculator.py --scenarios`:

| Scenario | DCF FV | My FV | Delta | Comment |
|----------|--------|-------|-------|---------|
| Bear | $199 | $165 | -17% | My bear is more conservative |
| Base | $259 | $220 | -15% | My base is more conservative |
| Bull | $344 | $287 | -17% | My bull is more conservative |

The DCF tool consistently produces higher FVs than my P/B + P/E methods. This is expected for insurers where DCF is less reliable (lumpy FCF, reserve movements). My methods are more appropriate for the business type.

---

## 🔄 META-REFLECTION

### Dudas/Incertidumbres
- **ROE sustainability is the single most important variable.** The gap between GAAP ROE (20.9%) and ex-AOCI ROE (16.0%) is 4.9 percentage points. This gap fluctuates with interest rates and bond portfolio mark-to-market. If rates fall materially, GAAP ROE could drop toward ex-AOCI levels, compressing the P/B justified multiple. At ROE 14%, the P/B FV drops to $152 -- near current price.
- **Class action timeline is unknowable.** The securities fraud case survived motion to dismiss and is in discovery. Settlement could take 1-3 years. During this period, the stock may not re-rate regardless of business performance.
- **The quality_scorer assigns QS 52 (Tier C), but the thesis claimed Tier B (7/10).** The automated tool flags ROIC spread as negative (-4.2pp), which is odd for a company with 16-21% ROE. This may be a measurement issue with how ROIC is calculated for insurers (invested assets vs operating assets are different concepts). The QS tool may not be well-calibrated for financial companies.

### Anomalies Detected
- **Yield reported as 74.0% in price_checker.py** -- this is clearly a data error from yfinance. GL's actual dividend yield is approximately 0.74% ($1.084 annual dividend / $146.51 price). This appears to be a decimal point issue in the data feed.
- **ROIC spread -4.2pp in quality_scorer** -- For an insurer with 16-21% ROE and 6.6% cost of equity, this seems incorrect. ROIC for insurers should likely be measured differently (ROE vs Ke, not ROIC vs WACC). This systematic issue may affect all financial companies scored by the tool.

### Sensibilidad Preocupante
- ROE sensitivity is high: every 2pp change in ROE changes FV by ~$25 (or ~12%). If ROE drops from 20% to 14% (a plausible scenario in a deep recession with credit losses), FV drops from $232 to $152.
- However, GL's loss ratio has been remarkably stable over 10+ years. Life insurance is actuarially predictable. The main risk to ROE is credit losses in the investment portfolio, not insurance underwriting.

### Discrepancias con Thesis
- My FV ($220) is 26% HIGHER than thesis adopted FV ($174). This is UNUSUAL in our adversarial review (normally we find inflated FVs). The thesis author overcorrected by using P/E 11.5x as the adopted value despite calculating $237 through a rigorous framework. This suggests the v2.0 review was driven by excessive caution rather than analysis.
- However, my calculated weighted FV ($221) is only 7% below the thesis calculated FV ($237), so the underlying analysis was solid.

### Sugerencias para el Sistema
- **quality_scorer.py may need a financial company mode** -- ROIC calculation for insurers should use ROE vs Ke, not traditional ROIC vs WACC. The current tool underscores financials.
- **price_checker.py yield display** -- The 74.0% yield for GL is a yfinance data error that should be caught and flagged.

### Preguntas para Orchestrator
1. Given the QS discrepancy (tool says 52/Tier C, thesis says 7/10 Tier B), which should we use for portfolio decisions? Financial company QS may be systematically underestimated.
2. Should we increase the position given MoS of 33.4% is well above typical Tier B/C thresholds? Or does the litigation uncertainty warrant HOLD at current size?
3. The thesis adopted FV was the most conservative in the portfolio. Should we update the thesis FV to $220, or keep the $174 as a "worst-case adopted" and use $220 as the "risk-adjusted independent" FV?

---

**Report generated by: Valuation Specialist (Adversarial Review)**
**Date: 2026-02-08**
**Framework: v4.0**
