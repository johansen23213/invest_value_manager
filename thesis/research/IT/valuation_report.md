# Valuation Report: IT (Gartner, Inc.)

> **Date:** 2026-02-13
> **Status:** R1 Valuation Complete
> **Fair Value (Weighted):** $205
> **Current Price:** $153.63
> **MoS vs Weighted FV:** 25.0%
> **MoS vs Bear Case:** -7.5% (NEGATIVE -- bear is BELOW current price)

---

## Company Classification

**Type:** Subscription information services / Quality compounder with growth deceleration
**QS:** Tool 73, Adjusted 80 (Tier A)
**Moat:** WIDE (15/25) -- switching costs + intangible assets, AI vulnerability on lower tier
**Risk:** MEDIUM-HIGH (1 CRITICAL, 4 HIGH)

**Methods selected:**
1. **Primary:** Owner Earnings Yield (OEY) -- Tier A compounder with strong FCF
2. **Secondary:** DCF with scenarios -- validates cash flow-based valuation
3. **Cross-check:** EV/EBIT relative valuation vs peers -- reality check on multiple

---

## Method 1: Owner Earnings Yield (OEY) -- Weight 35%

### Calculation

```
FCF (FY2024): $1.38B
Depreciation: ~$140M
Maintenance Capex: $140M x 1.1 = $154M
Owner Earnings = $1.38B - $154M + $140M = $1.366B

Market Cap at current: $11.6B
OEY = $1.366B / $11.6B = 11.8%
```

### Growth Adjustment

The OEY method for Tier A compounders typically asks: what OEY is fair given the growth profile?

**Growth estimate derivation:**
- Revenue growth 2026: +2% (guided, DOGE + macro trough)
- Revenue growth 2027-2030: +5-6% (TAM 7% + pricing 2-3% - no share gain)
- Buyback contribution: ~6-8%/yr share count reduction (NOT 8% -- management is decelerating buybacks as cash tightens)
- Net EPS growth: ~10-12% normalized (6% revenue + 4-6% buyback effect)

**BUT: 2026 guidance shows FCF declining to $1.0-1.35B midpoint $1.175B -- a 15% decline from $1.38B.**

This is critical. The OEY calculation using trailing FCF overstates current earnings power. I must adjust:

```
ADJUSTED FCF (2026 guided midpoint): $1.175B
Adjusted OEY = $1.175B / $11.6B = 10.1%
```

### Fair Value via OEY

For a Tier A compounder with 10-12% expected EPS growth but:
- Revenue DECLINING in near-term
- AI disruption risk (CRITICAL)
- Gross margin declining trend
- High DCF sensitivity (TV 74.5% of EV)

A fair OEY of 6.5-8% is appropriate. This is HIGHER (more conservative) than the 5-6% I would use for a clean compounder like VRSK because:
- The growth trajectory is uncertain (2% guided vs 10% historical)
- AI disruption risk is real and partially manifesting
- CEO selling pattern adds governance discount

```
Fair OEY 6.5%: FV = $1.175B / 0.065 = $18.1B market cap / 72.1M shares = $251
Fair OEY 7.0%: FV = $1.175B / 0.070 = $16.8B market cap / 72.1M shares = $233
Fair OEY 7.5%: FV = $1.175B / 0.075 = $15.7B market cap / 72.1M shares = $218
Fair OEY 8.0%: FV = $1.175B / 0.080 = $14.7B market cap / 72.1M shares = $204
```

**Using 7.5% fair OEY (conservative for Tier A with risks): FV = $218**

**Reasoning for 7.5%:** VRSK (cleaner moat, no AI risk, 92% retention) would justify 5.5-6.0%. Gartner faces genuine AI disruption risk, declining margins, and revenue weakness. The 1.5-2pp OEY premium vs VRSK reflects: (a) AI vulnerability of lower-tier research (+0.5pp), (b) revenue decline guidance (+0.5pp), (c) CEO selling / governance (+0.25pp), (d) consulting segment structural decline (+0.25pp).

### OEY Fair Value: $218

---

## Method 2: DCF with Scenarios -- Weight 45%

### Parameter Derivation (from projection-framework)

**Growth Rate:**
```
TAM Growth: +7% (IT advisory/research, AI-driven demand)
Market Share: +0% (maintaining dominant #1 position)
Pricing Power: +2-3% (wallet retention 103% historically)
Government headwind (2026): -2%
Consulting structural decline: -0.5% drag on blended
= Net: ~7% normalizing in 2027-2030, after 2% trough in 2026

FCF Growth will lag revenue due to:
- 2026 FCF guided $1.0-1.35B (DOWN from $1.38B)
- Margin pressure from AI investment
- Historically, FCF CAGR was only +3.4% (below revenue CAGR of 9.8%)

Conservative FCF growth: 4-5% (below revenue growth due to reinvestment)
```

**WACC:**
```
Rf: 4.5% (US 10Y Treasury)
ERP: 5.5%
Beta: 1.04 (yfinance)
Ke = 4.5% + 1.04 x 5.5% = 10.2%

Kd: 4.0% (interest_expense / total_debt)
Tax rate: 9.6% (effective)
Kd after-tax = 3.6%

E/V: 78%, D/V: 22%
WACC = (0.78 x 10.2%) + (0.22 x 3.6%) = 8.75%

Rounding to 9.0% for conservatism (slight premium for AI uncertainty)
```

**Terminal Growth:**
```
Terminal growth: 2.5% -- at or slightly below GDP
Justification: Gartner is in a growing TAM (IT advisory), but at
terminal phase, growth normalizes to GDP-level. 2.5% is reasonable
for an information services monopoly with pricing power.
```

### DCF Tool Results

**Base Case (Growth 5%, WACC 9%, Terminal 2.5%):**
```
FV: $315.69 (+105.5% MoS)
TV as % of EV: 74.5% -- HIGH
FV Spread: 82% -- HIGH
```

**Conservative Case (Growth 3%, WACC 10%, Terminal 2%):**
```
FV: $234.02 (+52.3% MoS)
```

**Pessimistic Case (Growth 0%, WACC 9%, Terminal 2%):**
```
FV: $235.17 (+53.1% MoS)
```

**Bear Case (Growth -2%, WACC 9.5%, Terminal 1.5%):**
```
FV: $188.22 (+22.5% MoS)
```

**Extreme Bear (Growth -3%, WACC 10.5%, Terminal 1.5%):**
```
FV: $157.61 (+2.6% MoS) -- essentially FAIR VALUE AT CURRENT PRICE
```

**Catastrophic (Growth -5%, WACC 11%, Terminal 1%):**
```
FV: $129.40 (-15.8% MoS) -- current price is OVERVALUED
```

### Sensitivity Matrix (Growth x WACC)

| Growth \ WACC | 7.5% | 9.0% | 10.5% |
|---------------|------|------|-------|
| 2.0% | $364 | $275 | $220 |
| 3.5% | $390 | $295 | $235 |
| 5.0% | $418 | $316 | $252 |
| 6.5% | $448 | $338 | $269 |
| 8.0% | $479 | $361 | $288 |

### Reverse DCF: What Is the Market Pricing?

At $153.63 with WACC 10.5% and terminal 1.5%, the DCF gives ~$158. This means the market is pricing:
- Growth of approximately **-3% to -4%** at reasonable WACC (9-10%)
- OR growth of 0% at very high WACC (11%+)
- OR structural FCF decline of 5%+ per year

**The market is pricing Gartner as a DECLINING business.** If growth stabilizes at even 0-2%, the stock is significantly undervalued. If the market is right and revenue declines 3-5% for multiple years, the current price is approximately fair.

### DCF Assessment

The DCF shows HIGH sensitivity to inputs. I CANNOT rely on a point estimate. Instead, I use a range approach:

```
Conservative DCF range: $188 - $275
  Lower bound: Growth -2%, WACC 9.5% (revenue declines but stabilizes)
  Upper bound: Growth 2%, WACC 9% (trough in 2026, slow recovery)
  Midpoint: $232

My derived DCF estimate: $205 (weighted toward conservative)
  Reasoning: 2026 will be weak (guided decline), recovery is uncertain,
  AI disruption is real. I weight the lower end of the range.
```

### DCF Fair Value: $205

---

## Method 3: EV/EBIT Relative Valuation (Cross-Check) -- Weight 20%

### Normalized EBIT

```
2024 EBIT: ~$1.16B (18.5% operating margin on $6.3B revenue)
2023 EBIT: ~$1.17B (19.2% operating margin)
2022 EBIT: ~$1.23B (20.3% operating margin)
2021 EBIT: ~$1.07B (17.8% operating margin)

3-year average EBIT: ~$1.16B
Using 2024 EBIT: $1.16B (conservative -- represents recent margin compression)
```

### Peer Multiples

| Company | EV/EBIT | P/E | Growth | ROIC | Notes |
|---------|---------|-----|--------|------|-------|
| VRSK | ~27x | 27.5x | 5.4% | 38% | Pure data, WIDE moat, near-monopoly |
| FDS | ~25x | 30x | 8.0% | 19% | Financial data, strong retention |
| SPGI | ~28x | 38x | 13% | 8%* | Ratings moat, IHS distortion |
| MCO | ~25x | 36x | 4.5% | 24% | Ratings duopoly |
| **Peer Median** | **~26x** | **~33x** | **6.7%** | **21%** | |
| **IT (Gartner)** | **~11x** | **15.9x** | **2% guided** | **52%** | Massive discount |

### What Multiple Does Gartner Deserve?

**Arguments for premium vs peers:**
- ROIC 52% is HIGHEST in peer group (2x peer median)
- #1 market position (6x larger than nearest competitor)
- 82% subscription revenue with 103% wallet retention

**Arguments for discount vs peers:**
- Revenue DECLINING in 2026 (worst growth in peer group)
- AI disruption risk HIGHER than VRSK/SPGI/MCO
- Consulting segment in structural decline
- Gross margin declining
- CEO insider selling pattern

**My multiple assessment:**

Peers trade at 25-28x EV/EBIT. Gartner deserves a discount for:
- Revenue decline: -3x to -4x
- AI vulnerability: -2x to -3x
- Growth deceleration: -2x to -3x
- Consulting weakness: -1x

But a premium for:
- ROIC 52%: +2x to +3x
- Market dominance: +1x

**Net: Peer median 26x - 6x to -7x discount + 3x premium = 22-23x EV/EBIT**

However, I also consider a CONSERVATIVE scenario where the market assigns a lower multiple given genuine uncertainty:

**Base multiple: 18x EV/EBIT** (40% discount to peer median -- acknowledges real risk)
**Conservative multiple: 14-15x EV/EBIT** (near current)

```
At 18x EV/EBIT:
EV = $1.16B x 18 = $20.88B
Equity = $20.88B - $1.53B (net debt) = $19.35B
FV = $19.35B / 72.1M shares = $268

At 15x EV/EBIT (conservative):
EV = $1.16B x 15 = $17.4B
Equity = $17.4B - $1.53B = $15.87B
FV = $15.87B / 72.1M shares = $220

At 12x EV/EBIT (deep discount, near current):
EV = $1.16B x 12 = $13.92B
Equity = $13.92B - $1.53B = $12.39B
FV = $12.39B / 72.1M shares = $172
```

Using midpoint of conservative and base (15x and 18x):

### EV/EBIT Fair Value: $195 (at ~16.5x, significant discount to peers)

**Rationale for using 16.5x:** This is a 37% discount to peer median of 26x. This large discount reflects: (a) the revenue DECLINE guidance is unprecedented for Gartner, (b) AI disruption is showing in financial metrics (not just narrative), (c) peers like VRSK/SPGI have harder moats. If AI fears prove overdone, the multiple re-rates toward 20x+ ($260+). If AI disruption accelerates, the multiple stays at 12-14x ($170-$195).

---

## Reconciliation

| Method | Fair Value | Weight | Weighted |
|--------|-----------|--------|----------|
| OEY (7.5% yield) | $218 | 35% | $76.30 |
| DCF (conservative range) | $205 | 45% | $92.25 |
| EV/EBIT (16.5x) | $195 | 20% | $39.00 |
| **Weighted Average** | | **100%** | **$207.55** |

**Divergence between methods: 11.8%** ($218 highest vs $195 lowest). This is well within 30% threshold and suggests reasonable convergence.

### Weight Rationale

- **DCF gets 45% (highest):** For a business with $1.4B FCF and uncertain growth trajectory, the DCF anchors the valuation to cash flow reality. But HIGH sensitivity (TV 74.5%, spread 82%) reduces confidence.
- **OEY gets 35%:** The OEY approach is naturally conservative for Tier A compounders and validates the range. Adjusted for 2026 FCF guidance, it provides a solid check.
- **EV/EBIT gets 20% (lowest):** Relative valuation is useful but depends on assuming peers are correctly valued. In a SaaSpocalypse selloff, peers may ALSO be mispriced. Additionally, the multiple discount is subjective.

### Adjusted Fair Value: $205

Applying ~1% additional conservatism for:
1. Historical FCF CAGR of only +3.4% (below revenue growth -- cash conversion may not improve as projected)
2. Risk-identifier flagged 5 HIGH+ risks with 3 correlated (AI disruption cluster)
3. No insider buying at current levels (Pagliuca bought at $150-160 but CEO was selling at $507)

**Final Fair Value: $205**

---

## Scenarios

| Scenario | Revenue Growth (5yr avg) | FCF 2030E | Exit P/E | EPS 2030E | Fair Value | Prob |
|----------|------------------------|----------|---------|----------|-----------|------|
| Bear | -1% | $0.95B | 14x | $14 | $143 | 25% |
| Base | +4% | $1.35B | 20x | $21 | $205 | 50% |
| Bull | +7% | $1.80B | 26x | $30 | $310 | 25% |

### Bear Case ($143, 25% probability)

**Assumptions:**
- AI disrupts lower-tier research subscriptions, wallet retention drops to 93-95%
- Revenue growth: -1% average (flat to declining for 3 years, then stabilization)
- Consulting segment dies (goes to near-zero or is divested)
- Operating margin compresses to 16% (higher costs from AI investment, lower pricing power)
- Buybacks continue but at reduced pace ($1.0-1.2B/yr)
- Exit multiple: 14x P/E (priced as low-growth information services)
- EPS grows only 5-6%/yr (buyback-driven, no organic growth)

**This scenario implies the market is ROUGHLY CORRECT** at current price. Bear FV of $143 is 7% BELOW current $153.63.

### Base Case ($205, 50% probability)

**Assumptions:**
- DOGE headwind clears by mid-2026, CV growth recovers to 4-6%
- Research segment grows 4-5%, consulting restructured to break-even
- AI integration drives new client wins and upsell of AI advisory products
- Operating margin stabilizes at 18.5-19% (mix shift toward higher-margin research)
- Buybacks of $1.5-2.0B/yr continue, ~6% annual share count reduction
- Exit multiple: 20x P/E (moderate re-rating from 16x but well below historical 30-40x)
- EPS grows ~12-14%/yr (4% revenue + 6% buyback + margin)

### Bull Case ($310, 25% probability)

**Assumptions:**
- AI adoption ACCELERATES demand for advisory (CIOs need MORE guidance, not less)
- Research segment grows 7-9% as new buyer categories (AI/ML teams) enter
- Consulting pivots to AI implementation advisory, stabilizes
- Operating margin expands to 21-22% (operating leverage at scale)
- Buybacks at depressed prices create massive per-share value accretion
- Exit multiple: 26x P/E (market recognizes durability of franchise)
- EPS grows 18-20%/yr

### Expected Value

```
EV = (Bear x 25%) + (Base x 50%) + (Bull x 25%)
EV = ($143 x 0.25) + ($205 x 0.50) + ($310 x 0.25)
EV = $35.75 + $102.50 + $77.50
EV = $215.75
```

### Summary

| Metric | Value |
|--------|-------|
| **Fair Value (weighted methods)** | **$205** |
| **Expected Value (prob-weighted scenarios)** | **$216** |
| Current Price | $153.63 |
| MoS vs Fair Value | 25.0% |
| MoS vs Expected Value | 28.8% |
| MoS vs Bear Case | **-7.5% (NEGATIVE)** |
| MoS vs Bull Case | 50.4% |

---

## Sensitivity Analysis (DCF)

### Growth x WACC Matrix (all values in USD)

| Growth \ WACC | 7.5% | 8.0% | 9.0% | 10.0% | 10.5% |
|---------------|------|------|------|-------|-------|
| -2% | $258 | $238 | $207 | $182 | $171 |
| 0% | $294 | $270 | $235 | $207 | $195 |
| 2% | $331 | $304 | $264 | $232 | $218 |
| 3.5% | $390 | $340 | $295 | $252 | $235 |
| 5% | $418 | $380 | $316 | $269 | $252 |

**Key observations:**
- At current price ($154), the market is pricing ~-3% growth at 10.5% WACC, or -5% growth at 11% WACC
- Even at 0% growth / 10% WACC, FV is $207 (35% upside)
- The downside scenario (structural -5% decline) gives FV $129 (16% downside)
- **The distribution is RIGHT-SKEWED:** upside scenarios are larger in magnitude than downside scenarios

### What Needs to Go Wrong for Current Price to Be Fair

For $153.63 to be fair value, you need ONE of these combinations:
1. Growth -3%, WACC 10.5%, Terminal 1.5% (moderate structural decline + high risk premium)
2. Growth -5%, WACC 11%, Terminal 1.0% (severe structural decline + very high risk)
3. Growth 0%, WACC 12%+, Terminal 1.0% (no growth but extreme risk premium)

**Assessment:** Scenario 1 is POSSIBLE but aggressive. Scenario 2 requires Gartner's business to deteriorate significantly beyond current guidance. Scenario 3 requires a risk premium normally reserved for distressed businesses, which Gartner is not (ROIC 52%, FCF $1.4B).

---

## Validation vs Peers

### Implied Multiples at My FV of $205

| Metric | At $205 FV | Current Market | Peer Median |
|--------|-----------|---------------|-------------|
| P/E | 21.2x | 15.9x | 33x |
| EV/EBIT | ~16x | ~11x | 26x |
| P/FCF | 10.7x | 8.4x | 25x |
| FCF Yield | 9.4% | 11.9% | 4.0% |

**My FV implies:**
- P/E of 21x -- still a 36% discount to peer median (33x). This is appropriate given AI risk + revenue decline
- EV/EBIT of 16x -- 38% discount to peer median (26x). Also appropriate
- FCF yield of 9.4% -- very high for a quality compounder, reflecting uncertainty discount

**Sanity check PASSED:** My FV does NOT imply bubble multiples. At $205, Gartner would still trade at a significant discount to peers, reflecting the real risks. If anything, $205 may be conservative if AI fears prove overblown.

### Validation vs Precedents (decisions_log.yaml)

| Comparison | IT (Gartner) | Precedent | Notes |
|------------|-------------|-----------|-------|
| QS | 80 adj (Tier A) | ADBE 76, BYIT.L 68 adj, ROP 70 adj | IT is high Tier A |
| MoS at entry | 25% at $153, 37% at $130 | Tier A range 29-38% | Current MoS is LOW for Tier A |
| Bear MoS | -7.5% | NVO bear MoS ~15%+, AUTO.L >10% | NEGATIVE bear MoS = insufficient cushion |
| Moat | WIDE 15/25 | VRSK 19/25, BYIT.L ~15/25 | Lower-end WIDE |
| Risk | MEDIUM-HIGH | ADBE MEDIUM, ROP HIGH | Elevated |

**Verdict on precedent consistency:** Previous Tier A buys (ADBE, NVO, LULU, MONY.L, AUTO.L, BYIT.L) all had:
- MoS of 29-38% vs base FV
- POSITIVE MoS vs bear case (minimum ~10%)
- Risk rating of MEDIUM or less

IT at current $153 has:
- MoS of 25% vs base FV -- BELOW precedent minimum (29%)
- MoS of -7.5% vs bear -- NEGATIVE (unprecedented for Tier A buys)
- Risk rating MEDIUM-HIGH (highest risk for any Tier A candidate)

**This is inconsistent with Tier A buying precedents.** Either:
(a) Wait for $130-140 where MoS vs base is 32-37% and MoS vs bear is ~0-8%, OR
(b) Wait for Q1 2026 data that de-risks the AI narrative (CV acceleration, wallet retention stability)

---

## Comparison: Fundamental Analyst FV ($245) vs Valuation Specialist FV ($205)

The fundamental analyst estimated FV at $245. I arrive at $205, a -16.3% difference. Reasons for divergence:

| Factor | Fundamental Analyst | Valuation Specialist | Delta |
|--------|--------------------|--------------------|-------|
| OEY base FCF | $1.38B (trailing) | $1.175B (2026 guided midpoint) | -$0.205B (-15%) |
| OEY fair yield | 6% implied | 7.5% | More conservative |
| DCF growth | 5% | 4-5% used, anchored to conservative range | Slightly lower |
| DCF weight | 60% (high for high-sensitivity) | 45% | Reduced reliance on uncertain DCF |
| EV/EBIT multiple | Not explicitly used | 16.5x (heavy discount to peers) | New method adds conservatism |
| Bear scenario | $165 (7% above current) | $143 (7% below current) | Risk-identifier data (30% bear prob per risk-identifier) |

**Key driver of difference:** I use 2026 guided FCF ($1.175B midpoint) rather than trailing FCF ($1.38B) as the base. This is critical because management has explicitly guided for FCF DECLINE in 2026. Using trailing FCF overstates current earning power.

**Assessment:** The fundamental analyst's $245 is reasonable if growth recovers to 5%+ within 2 years. My $205 is more conservative and reflects the possibility that the 2026 trough extends into 2027 or that AI disruption proves more impactful than expected. The truth is likely between $205 and $245.

---

## Final Recommendation Context

```
Fair Value: $205
Expected Value (probability-weighted): $216
Current Price: $153.63

MoS vs FV: 25.0%
MoS vs EV: 28.8%
MoS vs Bear: -7.5% (NEGATIVE)

Entry recommendation: $130-140 (MoS 32-37% vs FV, 0-8% vs bear)
ADD trigger: $115-120 (MoS 42-44% vs FV, 16-20% vs bear)
```

---

## META-REFLECTION

### Dudas/Incertidumbres

1. **The DCF is HIGHLY sensitive to inputs.** Terminal value is 74.5% of enterprise value. Small changes in terminal growth or WACC swing FV by 30%+. This makes any DCF point estimate unreliable. I mitigate this by using a range approach and weighting the conservative end, but the uncertainty is real.

2. **2026 FCF guidance range is WIDE: $1.0-1.35B.** The low end ($1.0B) would give an OEY FV of $185. The high end ($1.35B) gives $250. This 35% range within management's OWN guidance shows how uncertain near-term cash generation is.

3. **The bear case FV ($143) is BELOW current price.** This is unusual for a Tier A candidate. In our precedents, all Tier A buys had positive bear-case MoS. Either: (a) I am too conservative in my bear case (possible -- I used risk-identifier's 30% bear probability), or (b) the current price does not provide sufficient downside protection for a Tier A position (my view).

4. **FCF CAGR historical: +3.4%.** This is MUCH lower than revenue CAGR of +9.8%. The gap suggests either (a) heavy reinvestment absorbing cash flow, or (b) the buyback-funded EPS story masks weak operational FCF growth. This is a meaningful red flag that I cannot fully resolve.

5. **I diverge -16% from the fundamental analyst's FV.** This is within normal range but worth highlighting. The divergence is driven primarily by using forward (2026) FCF rather than trailing FCF. I believe the forward approach is more appropriate given the guided decline.

### Sensibilidad Preocupante

- **If terminal growth is 3% instead of 2.5%:** DCF FV jumps $30-40 (to $245-265). The terminal assumption matters enormously.
- **If 2026 FCF comes in at the LOW end ($1.0B):** OEY FV drops to $185. This alone would make the current price only 17% below FV -- borderline insufficient.
- **The range between extreme bear ($129) and bull ($310) is $181, or 118% of base case.** This is a VERY WIDE range for a quality compounder. The uncertainty is uncomfortable.

### Discrepancias con Thesis

- **Thesis FV: $245 vs my FV: $205.** Key difference is FCF base ($1.38B trailing vs $1.175B forward) and higher OEY requirement (7.5% vs ~6%).
- **Thesis entry: $140-150 vs my entry: $130-140.** I am $10 lower because my bear case is more severe ($143 vs $165), and I require positive bear MoS for Tier A consistency.
- **Thesis moat score was adjusted from 15/25 to "effectively 19/25" in the OEY weighting.** I do not make this adjustment -- I take the 15/25 as given and apply a higher OEY requirement instead.
- **Risk-identifier probability-weighted FV ($170-195) is 17% below my $205.** The risk assessment assigns 30% probability to bear (vs my 25%). If I used the risk-identifier's probabilities: EV = ($143 x 0.30) + ($205 x 0.45) + ($310 x 0.25) = $42.90 + $92.25 + $77.50 = $213. Even with more pessimistic probabilities, the EV supports $205+.

### Sugerencias para el Sistema

1. **DCF tool should accept FORWARD FCF as input.** Currently it uses trailing FCF from yfinance. For companies guiding FCF decline, the trailing number overstates earning power. A `--base-fcf` parameter would improve accuracy.

2. **OEY method needs formalization in valuation-methods skill.** The current skill describes it briefly but does not provide the "fair OEY" framework (how to determine what OEY is appropriate given growth, risk, and peer comparison). This would improve consistency across valuations.

3. **Bear case MoS should be a STANDARD metric in all valuations.** Our precedents show all Tier A buys had positive bear MoS. Making this explicit in the valuation template would catch situations like IT where the bear case is uncomfortably close to (or below) current price.

### Preguntas para Orchestrator

1. **The fundamental analyst estimated FV $245. I estimate $205. Which should the thesis use?** I recommend $205 as the working FV (more conservative, based on forward FCF), but note that the truth is likely between $205-$245. The entry price of $130-140 provides adequate MoS against either estimate.

2. **Should we set a precedent for "negative bear MoS" for Tier A?** All prior Tier A buys had positive bear MoS. IT would be the first with negative bear MoS if bought at current price. This is either (a) a reason to require a lower entry, or (b) evidence that IT should be treated as Tier B for position-sizing purposes despite QS 80.

3. **SaaSpocalypse cluster risk.** IT would be our 3rd information services position in pipeline (after VRSK and MORN). All three are caught in the same selloff. If we deploy capital into all three, we are making a concentrated bet that the SaaSpocalypse is overdone. Is this acceptable given Principio 3 (Diversificacion Sectorial)?

---
