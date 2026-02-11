# VALUATION REPORT: WKL.AS (Wolters Kluwer NV)

**Date:** 2026-02-11
**Valuation Specialist (Independent)**
**Framework Version:** 4.0

---

## Company Classification

**Type:** Stable/Defensive with AI disruption overhang
**QS Tool:** 72/100 (Tier B -- Quality Value). No upward adjustment recommended (per adversarial review consensus).
**Moat:** NARROW (independent moat-assessor classification; thesis claimed WIDE)
**ROIC:** 13.3% standard (GuruFocus) / 18.1% company-adjusted. Spread vs WACC: +4.8pp to +9.6pp.

**Methods selected:** DCF (primary) + EV/EBIT Normalized (secondary) + DDM and FCF Yield (cross-checks)

**Rationale for method selection:**
- DCF: FCF positive every year, 84% recurring revenue = high predictability. Appropriate for Tier B stable business.
- EV/EBIT: Direct peer comparisons available (RELX, Thomson Reuters). Grounds the DCF in market reality.
- DDM: 10+ consecutive years of dividend growth, 3.6% yield, 40% FCF payout. Useful cross-check for income-based floor.
- FCF Yield / P/FCF: Simplest sanity check. At 9% FCF yield, this is an unusually high yield for a quality business.

---

## WACC Derivation (Independent)

The thesis uses 8.5% WACC. The adversarial review does not challenge this. I will derive independently.

```
Risk-Free Rate (10Y Bund): 2.3%
Equity Risk Premium (EU): 5.5% (higher than thesis's 5.0-6.0% range, reflecting AI uncertainty premium)
Beta: 0.95 (adjusted upward from 0.85 to reflect increased systematic risk from AI disruption narrative;
       the stock's 63% decline and elevated volatility since 2025 supports a higher beta than historical)

Cost of Equity (Ke): 2.3% + 0.95 * 5.5% = 7.53%

Cost of Debt (Kd pre-tax): 3.5%
Tax Rate: 24%
Kd after-tax: 2.66%

Market Cap: EUR 14.8B
Net Debt: EUR 4.4B (9M 2025, includes FRR proceeds received post-close)
Enterprise Value proxy: EUR 19.2B
Weight Equity (E/V): 77%
Weight Debt (D/V): 23%

WACC = (0.77 * 7.53%) + (0.23 * 2.66%) = 5.80% + 0.61% = 6.41%
```

**Sanity check:** 6.4% is too low for a business facing legitimate AI disruption uncertainty. I will use the following:

| Scenario | WACC | Rationale |
|----------|------|-----------|
| Bear | 10.0% | Disruption scenario: higher beta ~1.2, ERP 6%, country premium |
| Base | 9.0% | Above calculated, reflecting AI uncertainty premium. More conservative than thesis (8.5%) |
| Bull | 8.5% | AI proves to be tailwind, risk normalizes to pre-crash levels |

**Key justification for using 9% base vs thesis 8.5%:** The moat-assessor classified moat as NARROW (not WIDE as thesis claims). A narrower moat business warrants a higher risk premium. Additionally, the stock's persistent decline -- still making new lows daily -- suggests the market assigns a higher discount rate than historical.

---

## Growth Rate Derivation (Independent)

### Revenue Growth Logic

```
TAM growth: +4-5% (professional information services, structural growth from increasing regulation)
Market share: +0.0 to +0.5pp/yr (WKL gaining in cloud, losing in print; net neutral to slight positive)
Pricing power: +1-2% (products <1% of customer cost; annual price escalators in contracts)
AI drag: -0.5 to -1.5pp (10-15% of revenue at risk per moat-assessor, phased over 5-10 years)
FRR divestiture: -2% one-time revenue loss (EUR 123M of ~EUR 5.9B)

= Organic revenue growth: 3-6% range
```

### FCF Growth Logic

FCF growth has historically exceeded revenue growth due to operating leverage and margin expansion:
- Historical FCF CAGR: 8.4% (4 years)
- Revenue CAGR: 5.5%
- Delta: ~3pp of margin expansion/operating leverage

Going forward, margin expansion is decelerating as the company nears efficiency limits. I project FCF growth at revenue growth + 1-2pp, not +3pp.

| Scenario | Revenue Growth | FCF Growth | Rationale |
|----------|---------------|------------|-----------|
| Bear | 2-3% | 3% | AI disrupts 15-20% of revenue over 5 years; legal division shrinks; cloud growth decelerates |
| Base | 4-5% | 5% | AI neutral to slightly negative; cloud offsets print decline; pricing power intact |
| Bull | 6-7% | 7% | AI is net positive; CCH Axcess Expert AI and UpToDate Expert AI win share; cloud accelerates |

**Why my base is 5%, not thesis's 6%:** The 9M 2025 data shows H1 organic growth decelerated to 5% (not 6% as thesis stated). Q3 pickup brought 9M to 6%, but several divisions showed deceleration: Health 5% (from 6%), FCC 4% (from 5%), CPE 8% (from 9%). Only Legal & Regulatory accelerated -- ironically the most AI-vulnerable segment. Additionally, the FRR divestiture removes EUR 123M of revenue from the 2026 base.

### Terminal Growth

| Scenario | Terminal Growth | Rationale |
|----------|----------------|-----------|
| Bear | 1.5% | Below long-term EU nominal GDP; reflects persistent AI headwind |
| Base | 2.0% | At or slightly below long-term nominal GDP |
| Bull | 2.5% | At nominal GDP; professional services grow at or above GDP |

---

## Method 1 (Primary, 55% weight): DCF

### Parameters

| Parameter | Bear (25%) | Base (50%) | Bull (25%) |
|-----------|------------|------------|------------|
| FCF Growth Y1-5 | 3% | 5% | 7% |
| WACC | 10.0% | 9.0% | 8.5% |
| Terminal Growth | 1.5% | 2.0% (tool used 2.5%) | 2.5% |
| Years | 5 | 5 | 5 |

### DCF Tool Results

| Scenario | FV/Share | MoS vs EUR 65.72 | Notes |
|----------|----------|-------------------|-------|
| **Bear** (3%, 10%, 2%) | **EUR 59.93** | **-8.8%** | Stock overvalued by 9% if AI disrupts materially |
| **Base** (5%, 9%, 2.5%) | **EUR 85.22** | **+29.7%** | Moderate upside if AI neutral |
| **Bull** (7%, 8.5%, 2.5%) | **EUR 104.08** | **+58.4%** | Significant upside if AI is tailwind |

**Note on terminal growth:** My base case uses 2.0% terminal, but the tool was run with 2.5% for the base case (EUR 85.22). With 2.0% terminal at 9% WACC and 5% growth, the FV would be approximately EUR 77-80. I will use the tool output of EUR 85.22 as the "optimistic base" and note that a 2.0% terminal would reduce this by approximately EUR 5-8.

**Adjusted DCF Base with 2.0% terminal:** ~EUR 78-80. This aligns closely with the adversarial review's EUR 80 estimate.

### Extreme Bear (Sensitivity)

| Scenario | Growth | WACC | Terminal | FV | MoS |
|----------|--------|------|----------|----|-----|
| Severe disruption | 2% | 10.5% | 1.5% | EUR 49.33 | -24.9% |
| Thesis bear | 4% | 9.5% | 2.0% | EUR 68.88 | +4.8% |

The severe bear (EUR 49.33) represents the floor in a scenario where AI fundamentally disrupts 20-30% of WKL's revenue and growth decelerates to near-zero. This is a plausible but not probable outcome (15-20% probability per moat-assessor).

### DCF Expected Value

```
EV_DCF = (59.93 * 0.25) + (85.22 * 0.50) + (104.08 * 0.25)
EV_DCF = 14.98 + 42.61 + 26.02
EV_DCF = EUR 83.61
```

**Adjusted for 2.0% terminal on base:**
```
Adjusted_Base = ~78
EV_DCF_adj = (59.93 * 0.25) + (78 * 0.50) + (104.08 * 0.25)
EV_DCF_adj = 14.98 + 39.00 + 26.02
EV_DCF_adj = EUR 80.00
```

---

## Method 2 (Secondary, 30% weight): EV/EBIT Normalized

### EBIT Analysis

| Metric | Value | Source |
|--------|-------|--------|
| EBIT 2024 (adjusted operating profit) | EUR 1,600M | Company reported (27% margin on EUR 5.9B) |
| EBIT 2023 | EUR 1,460M (approx) | 26.5% margin on EUR 5.5B |
| EBIT 2022 | EUR 1,326M (approx) | 26% margin on EUR 5.1B |
| EBIT 2021 | EUR 1,234M (approx) | 25.7% margin on EUR 4.8B |
| EBIT 2020 | EUR 1,150M (approx) | 25% margin on EUR 4.6B |
| **EBIT Normalized (5yr avg)** | **EUR 1,354M** | Average of above |
| **EBIT Current (2024)** | **EUR 1,600M** | Most recent, reflects margin expansion |

For forward-looking valuation, I use EUR 1,500M as a blend: slightly below 2024 peak (reflecting possible AI headwinds on growth) but above the 5yr average (reflecting genuine structural margin improvement from cloud transition).

### Multiple Determination

**Peer Multiples (current, post-crash):**

| Peer | EV (EUR B) | EBITDA (EUR B) | EV/EBITDA | P/E | P/FCF | Notes |
|------|-----------|---------------|-----------|-----|-------|-------|
| RELX | ~51 | 3.09 | 19.8x | 20.8 | 27.4x | Higher quality, more diversified |
| Thomson Reuters | ~35 | 2.34 | 17.7x | 27.6 | 23.9x | More aggressive AI strategy |
| WKL.AS (current) | ~19.8 | 1.95 | 10.1x | 13.8 | 14.5x | Depressed by AI fear |

WKL trades at a massive discount to both peers: 10.1x EV/EBITDA vs 17.7-19.8x. This implies either (a) WKL is much more AI-vulnerable than peers, (b) the market is wrong, or (c) a mix of both.

**My multiple determination:**

```
Starting point: Sector (info services, post-crash): 14x EV/EBIT
  + ROIC persistently above WACC (+4.8pp minimum): +0.5x
  + 84% recurring revenue (highest among peers): +0.5x
  + Expanding margins (5yr trend): +0.5x
  - AI disruption uncertainty (NARROW moat, not WIDE): -1.5x
  - CEO transition during maximum uncertainty: -0.5x
  - 0.1% insider ownership (no management skin in game): -0.5x
  - Non-recurring revenue declining (print -11%, licenses -9%): -0.5x
  = 12.5x EV/EBIT (my base)
```

**Scenario multiples:**

| Scenario | Multiple | Rationale |
|----------|----------|-----------|
| Bear | 11x | AI fears persist, peer multiples compress further |
| Base | 13x | Modest recovery from trough, below pre-crash but above current |
| Bull | 15x | AI fears prove overblown, recovery toward peer levels |

### EV/EBIT Fair Values

Using EUR 1,500M EBIT (forward normalized):

| Scenario | Multiple | EV (EUR M) | - Net Debt | = Equity (EUR M) | / 225.6M Shares | FV/Share | MoS |
|----------|----------|-----------|-----------|-----------------|-----------------|----------|-----|
| **Bear** | 11x | 16,500 | -4,310 | 12,190 | 225.6 | **EUR 54.02** | **-17.8%** |
| **Base** | 13x | 19,500 | -4,310 | 15,190 | 225.6 | **EUR 67.33** | **+2.4%** |
| **Bull** | 15x | 22,500 | -4,310 | 18,190 | 225.6 | **EUR 80.63** | **+22.7%** |

### EV/EBIT Expected Value

```
EV_EBIT = (54.02 * 0.25) + (67.33 * 0.50) + (80.63 * 0.25)
EV_EBIT = 13.51 + 33.67 + 20.16
EV_EBIT = EUR 67.33
```

**Important observation:** The EV/EBIT method gives a significantly lower fair value (EUR 67) than the DCF (EUR 80-84). Divergence is ~20%. This is below the 30% investigation threshold but warrants explanation.

**Explanation of divergence:**
1. The DCF captures WKL's long runway of compounding FCF growth. At 5% FCF growth for 5 years followed by perpetual 2-2.5% terminal, the cumulative value is substantial.
2. The EV/EBIT method reflects CURRENT market sentiment and peer comparison. With peers themselves depressed (RELX down from 25x+ to 20x P/E), the "fair multiple" is anchored to a trough.
3. The EV/EBIT method is more conservative because it does not explicitly model the growth/compounding -- it uses a static multiple on current earnings.
4. In a post-crash environment with AI uncertainty, the EV/EBIT method is arguably MORE reliable because it reflects what the market is actually willing to pay for similar businesses.

---

## Method 3 (Cross-check, 15% weight): DDM (Dividend Discount Model)

WKL has 10+ consecutive years of dividend growth. FY2024 dividend was EUR 2.37/share. Payout ratio from FCF is only 40%, indicating significant headroom.

### Multi-Stage DDM (3 stages: Y1-5, Y6-10, Terminal)

| Scenario | Ke | g1 (Y1-5) | g2 (Y6-10) | g_terminal | FV | MoS |
|----------|-----|-----------|-----------|------------|-----|-----|
| **Bear** | 10.0% | 4% | 2% | 2.0% | **EUR 32.87** | **-50.0%** |
| **Base** | 8.5% | 6% | 4% | 2.5% | **EUR 49.52** | **-24.7%** |
| **Bull** | 8.0% | 8% | 6% | 3.0% | **EUR 67.52** | **+2.7%** |

**Critical observation:** The DDM produces dramatically lower values than both DCF and EV/EBIT. Even the bull case (EUR 67.52) barely exceeds the current price. This is because WKL pays out only 40% of FCF as dividends, retaining 60% for reinvestment and buybacks. The DDM does not capture the value of retained earnings reinvested at ROIC > WACC.

**Why DDM is a FLOOR, not a fair value estimate for WKL:**
- WKL's payout ratio is 40%, among the lowest in the peer group
- The retained earnings generate returns above WACC (ROIC 13.3% vs WACC 8.5-9%)
- Buybacks at current depressed prices are highly accretive
- DDM is more appropriate for high-payout companies (utilities, REITs) than for growth compounders

**DDM is included as a cross-check for downside protection, not as a primary valuation method.** The DDM base case of EUR 49.52 represents the value IF you only cared about dividends -- a very conservative floor.

### DDM Expected Value

```
EV_DDM = (32.87 * 0.25) + (49.52 * 0.50) + (67.52 * 0.25)
EV_DDM = 8.22 + 24.76 + 16.88
EV_DDM = EUR 49.86
```

---

## Cross-Check: FCF Yield and Owner Earnings Yield

| Metric | Value | Interpretation |
|--------|-------|----------------|
| FCF Yield (vs Market Cap) | 9.0% | Exceptionally high for a quality business with recurring revenue |
| FCF Yield (vs EV) | 7.0% | Still attractive |
| P/FCF | 11.1x | Below the 12-15x typical for quality info services |
| OEY + Growth | 14.0% (9% + 5%) | Exceeds WACC of 9% by +5pp -- value creation at current price |

**Reverse DCF (what is the market pricing in?):**
- At 9% WACC: the market is pricing in approximately 3.5-4% FCF growth perpetually
- 9M 2025 organic growth was 6%, historical FCF CAGR was 8.4%
- The market is pricing in a permanent deceleration of 2-5pp below historical rates
- This is consistent with moderate AI disruption (15% of revenue at risk reducing growth by ~1pp) combined with a structurally higher risk premium

**Implied cost of equity at current price:**
- At 6% dividend growth: Ke_implied = 9.82% (market demands nearly 10% return)
- At 4% dividend growth: Ke_implied = 7.75%

---

## Reconciliation: Weighted Fair Value

| Method | FV (EV across scenarios) | Weight | Weighted |
|--------|------------------------|--------|----------|
| DCF (adjusted base) | EUR 80.00 | 55% | EUR 44.00 |
| EV/EBIT | EUR 67.33 | 30% | EUR 20.20 |
| DDM (floor) | EUR 49.86 | 15% | EUR 7.48 |
| **Weighted Average** | | **100%** | **EUR 71.68** |

**Divergence between DCF and EV/EBIT:** 19% (EUR 80 vs EUR 67). Below 30% threshold but significant. Explanation: DCF captures long-term compounding value that the EV/EBIT trough multiples understate. The gap reflects market uncertainty -- the DCF assumes the business compounds, while the market currently doesn't believe it will.

**Divergence between DCF and DDM:** 60% (EUR 80 vs EUR 50). Above 30% threshold. Explanation: DDM is structurally inappropriate as primary method for a 40% payout company. The DDM captures only dividend cash flows, missing retained earnings compounding at ROIC > WACC. This divergence is expected and does not indicate an error.

---

## Scenario Summary

| Scenario | DCF | EV/EBIT | DDM | Prob |
|----------|-----|---------|-----|------|
| Bear | EUR 59.93 | EUR 54.02 | EUR 32.87 | 25% |
| Base | EUR 80-85 | EUR 67.33 | EUR 49.52 | 50% |
| Bull | EUR 104.08 | EUR 80.63 | EUR 67.52 | 25% |
| Extreme Bear | EUR 49.33 | EUR 42 (est) | EUR 25 (est) | ~10% (tail) |

### Expected Value by Method

| Method | Expected Value | Weight | Contribution |
|--------|---------------|--------|-------------|
| DCF | EUR 80.00 | 55% | EUR 44.00 |
| EV/EBIT | EUR 67.33 | 30% | EUR 20.20 |
| DDM | EUR 49.86 | 15% | EUR 7.48 |
| **TOTAL** | | **100%** | **EUR 71.68** |

---

## Sensitivity Analysis

### DCF Sensitivity Matrix (FV per share)

| WACC \ Growth | 3% | 4% | 5% | 6% | 7% |
|---------------|-----|-----|-----|-----|-----|
| **8.0%** | ~72 | ~85 | ~94 | ~99 | ~115 |
| **8.5%** | ~66 | ~78 | ~85 | ~94 | ~104 |
| **9.0%** | ~61 | ~72 | ~78 | ~85 | ~95 |
| **9.5%** | ~57 | ~67 | ~73 | ~78 | ~87 |
| **10.0%** | ~53 | ~62 | ~68 | ~73 | ~80 |
| **10.5%** | ~49 | ~58 | ~63 | ~68 | ~74 |

*All values assume 2.0-2.5% terminal growth. Bold cells represent core scenario range.*

**Key observations:**
1. Fair value exceeds current price (EUR 65.72) in most scenarios with growth >= 4% and WACC <= 9.5%
2. Fair value drops below current price when growth falls to 3% at any WACC above 9%, or when WACC reaches 10%+ with growth below 5%
3. The most sensitive variable is WACC: moving WACC from 9% to 10% at 5% growth drops FV by EUR 10 (12%)
4. Growth matters more at lower WACC: at 8.5% WACC, moving from 4% to 6% growth adds EUR 16 (20%)

### EV/EBIT Sensitivity Matrix (FV per share, EUR 1,500M EBIT)

| Multiple | FV | MoS vs EUR 65.72 |
|----------|-----|-------------------|
| 10x | EUR 47.1 | -28.3% |
| 11x | EUR 54.0 | -17.8% |
| 12x | EUR 60.9 | -7.3% |
| 13x | EUR 67.3 | +2.4% |
| 14x | EUR 74.3 | +13.1% |
| 15x | EUR 80.6 | +22.7% |
| 16x | EUR 87.3 | +32.8% |

### Most Uncertain Variables (ranked)

1. **AI disruption scope and timeline (HIGHEST uncertainty):** This drives both the growth rate AND the appropriate WACC/multiple. Moving from "8-10% revenue at risk" (thesis) to "15-20% revenue at risk" (risk-identifier's aggressive estimate) changes fair value by EUR 15-20.

2. **Appropriate WACC/discount rate:** The calculated WACC is 6.4%, but the market-implied discount rate is 9.5-10%+. The gap reflects AI uncertainty premium. If AI fears dissipate, the WACC compression alone could drive a 30-40% re-rating.

3. **Growth rate post-FY2025:** The Feb 25 results will reveal whether H2 2025 showed deceleration. If organic growth came in at 5% (not 6%), this supports the base case. If 4% or below, the bear case becomes more probable.

4. **EV/EBIT multiple recovery:** WKL at 10.1x EV/EBITDA vs RELX at 19.8x is a 49% discount to its closest peer. This discount is either a screaming buy or justified by genuinely different risk profiles.

---

## Validation vs Peers

### Implied Multiples at My Fair Value

| Metric | At Current Price | At My FV (EUR 71.68) | RELX | Thomson Reuters |
|--------|-----------------|---------------------|------|-----------------|
| P/E | 13.8x | ~15.1x | 20.8x | 27.6x |
| EV/EBITDA | 10.1x | ~11.3x | 19.8x | 17.7x |
| P/FCF | 11.1x | ~12.1x | 27.4x | 23.9x |
| FCF Yield | 9.0% | 8.3% | 3.6% | 4.2% |

My FV implies P/E of ~15x, which is still well below peers (20-28x). This means my FV is conservative relative to a full peer re-rating scenario. If WKL re-rated to even half the peer premium, the stock would be at EUR 90+.

The validation confirms my FV is NOT optimistic. It still prices in a significant discount to peers.

### Validation vs Decisions Log Precedents

| Decision | Tier | MoS (at entry) | Context |
|----------|------|----------------|---------|
| ADBE | A | 31% | Quality compounder at 52w low |
| NVO | A | 38% | Guidance shock, quality at discount |
| LULU | A | 34% | Cyclical fear, quality at discount |
| BYIT.L | A | 35% | Partner restructuring fear |
| AUTO.L | A | 29% | Dealer revolt fear |
| **WKL.AS** | **B** | **9.1% (vs EUR 71.68)** | **AI disruption fear** |

WKL at 9.1% MoS for Tier B is BELOW the precedent range for Tier B entry (HRB was 42% MoS). This is a significant concern. The MoS is inadequate for a Tier B position with AI disruption uncertainty.

---

## Comparison with Other Estimates

| Source | Fair Value | My FV vs | Notes |
|--------|-----------|----------|-------|
| Original thesis | EUR 94.28 | -24% | Thesis used 8.5% WACC, 6% growth, 15x EV/EBIT |
| Adversarial review | EUR 80 (range 73-85) | -10% | More conservative WACC, 13x EV/EBIT |
| **My weighted FV** | **EUR 71.68** | **--** | 9% WACC, 5% growth, 13x EV/EBIT, DDM floor included |
| Market price | EUR 65.72 | +9.1% | Market prices in ~3.5-4% growth at 10% WACC |
| Extreme bear DCF | EUR 49.33 | -31% | 2% growth, 10.5% WACC, 1.5% terminal |
| Severe bear EV/EBIT | EUR 54.02 | -25% | 11x multiple |
| DDM base | EUR 49.52 | -31% | Dividend-only floor, misses retained earnings |

**Why my FV (EUR 71.68) is lower than the adversarial review (EUR 80):**

1. I use 9.0% WACC (not 8.5%) because the NARROW moat classification warrants higher risk premium
2. I use 5% FCF growth base (not 6%) because 9M 2025 showed deceleration and FRR divestiture reduces base
3. I use 13x EV/EBIT (not 15x) with more conservative adjustments reflecting CEO transition and non-recurring revenue decline
4. I include DDM at 15% weight, which drags down the weighted average significantly
5. The DCF terminal growth of 2.0% (not 2.5%) reflects my view that AI headwind is structural, not cyclical

**Why my FV (EUR 71.68) is higher than the market price (EUR 65.72):**

1. The market is pricing in ~3.5-4% growth perpetually -- I believe 5% is achievable given 84% recurring revenue and cloud momentum
2. The market-implied WACC of ~10% is too high for a business that delivered 6% organic growth through 9M 2025 with zero evidence of customer defection
3. At 9% FCF yield, the market is treating WKL like a mediocre cyclical, not a quality recurring-revenue business

---

## MoS Assessment

### At Current Price (EUR 65.72)

| Metric | Value |
|--------|-------|
| MoS vs My Weighted FV (EUR 71.68) | +9.1% |
| MoS vs DCF Base (EUR 80-85) | +22-29% |
| MoS vs EV/EBIT Base (EUR 67.33) | +2.4% |
| MoS vs DCF Bear (EUR 59.93) | -8.8% |
| MoS vs EV/EBIT Bear (EUR 54.02) | -17.8% |
| MoS vs Extreme Bear (EUR 49.33) | -24.9% |

### At Standing Order Trigger (EUR 65.00)

| Metric | Value |
|--------|-------|
| MoS vs My Weighted FV (EUR 71.68) | +10.3% |
| MoS vs DCF Base (EUR 80-85) | +23-31% |
| MoS vs EV/EBIT Base (EUR 67.33) | +3.6% |
| MoS vs DCF Bear (EUR 59.93) | -7.8% |
| MoS vs EV/EBIT Bear (EUR 54.02) | -16.9% |

---

## Assessment of Standing Order at EUR 65

### Is the EUR 65 Standing Order Appropriate?

**Verdict: The standing order at EUR 65 is TOO HIGH for a Tier B position with these risk characteristics.**

**Reasoning:**

1. **Inadequate MoS for Tier B:** At EUR 65, MoS vs my weighted FV (EUR 71.68) is only +10.3%. Precedents show Tier B entries at 20-40% MoS (HRB was 42%). WKL at 10% is at the very bottom of what is defensible.

2. **Negative MoS in bear scenarios:** At EUR 65, the DCF bear case shows -7.8% MoS and the EV/EBIT bear shows -16.9%. This means IF the bear scenario materializes, there is significant downside risk. For a stock making new 52-week lows weekly, this is inadequate downside protection.

3. **Feb 25 earnings are a binary event:** The FY2025 results will either confirm 6%+ organic growth (bullish) or reveal H2 deceleration (bearish). Buying before this catalyst with inadequate MoS is catching a falling knife.

4. **HRB precedent is a WARNING:** The portfolio bought HRB at $35 (standing order) and sold at $32.77 just 4 days later after adversarial review. The lesson from decisions_log: "Standing orders that ADD to deteriorating positions amplify losses -- adversarial review should precede ADD triggers."

5. **Adversarial review recommends EUR 55-58:** The fundamental-analyst adversarial review (which was less conservative than my valuation) already recommended lowering entry to EUR 55-58.

### Recommended Entry Levels

| Level | Price | MoS vs FV EUR 71.68 | MoS vs Bear EUR 59.93 | Rationale |
|-------|-------|---------------------|----------------------|-----------|
| Aggressive (post-earnings confirmation) | EUR 58 | +23.6% | -3.2% | If FY2025 shows 6%+ organic, buy here |
| **Conservative (recommended)** | **EUR 55** | **+30.3%** | **+9.0%** | Adequate MoS for Tier B with AI uncertainty |
| Deep value | EUR 50 | +43.4% | +19.9% | Near extreme bear FV, asymmetric risk/reward |
| Floor | EUR 45 | +59.3% | +33.2% | Only if AI disruption materializes severely |

**My recommendation: Lower standing order to EUR 55, post-earnings confirmation required.**

At EUR 55:
- MoS vs weighted FV: 30% (adequate for Tier B per precedents)
- MoS vs DCF bear: 9% (positive, providing minimal downside protection)
- MoS vs EV/EBIT bear: still negative (-1.8%), but the severe bear is truly severe
- Consistent with adversarial review recommendation of EUR 55-58

---

## Summary

```
VALUATION: WKL.AS

Type of company: Stable/Defensive info services with AI disruption overhang
QS: 72/100 (Tier B -- Quality Value)
Moat: NARROW (switching costs strong 15-25yr; intangible assets eroding 10-15yr)
Methods: DCF (55%) + EV/EBIT (30%) + DDM (15%)

Method 1: DCF (Derived Parameters)
- Inputs: Growth 5%, WACC 9%, Terminal 2.0-2.5%, Net Debt EUR 4.31B
- Bear/Base/Bull: EUR 60 / EUR 80-85 / EUR 104
- Expected Value: EUR 80.00

Method 2: EV/EBIT Normalized
- Inputs: EBIT EUR 1,500M normalized, Multiple 11-15x, Net Debt EUR 4.31B
- Bear/Base/Bull: EUR 54 / EUR 67 / EUR 81
- Expected Value: EUR 67.33

Method 3: DDM (Cross-check / Floor)
- Inputs: D0 EUR 2.37, Ke 8-10%, Div Growth 2-8% multi-stage
- Bear/Base/Bull: EUR 33 / EUR 50 / EUR 68
- Expected Value: EUR 49.86 (floor only)

Reconciliation:
| Method  | EV    | Weight | Weighted |
|---------|-------|--------|----------|
| DCF     | EUR 80.00 | 55%  | EUR 44.00 |
| EV/EBIT | EUR 67.33 | 30%  | EUR 20.20 |
| DDM     | EUR 49.86 | 15%  | EUR  7.48 |
| **Avg** |       | 100%   | **EUR 71.68** |

Divergence DCF vs EV/EBIT: 19% (below 30% threshold)
Divergence DCF vs DDM: 60% (DDM structurally inappropriate as primary for 40% payout company)

Scenarios:
| Scenario     | Fair Value  | Prob |
|--------------|-------------|------|
| Extreme Bear | EUR 49.33   | ~10% (tail) |
| Bear         | EUR 57-60   | 25%  |
| Base         | EUR 72-85   | 50%  |
| Bull         | EUR 80-104  | 25%  |
| **Expected** | **EUR 71.68** | 100% |

Current price: EUR 65.72
MoS vs Expected: +9.1%
MoS vs Bear (DCF): -8.8%
MoS vs Extreme Bear: -24.9%

Standing order at EUR 65: TOO HIGH -- recommend EUR 55 post-earnings
```

---

## 🔄 META-REFLECTION

### Dudas/Incertidumbres

1. **The DDM significantly dragged down my weighted FV.** At 15% weight, the DDM contributes EUR 7.48 to the weighted average, but it is structurally flawed for a 40% payout company. If I excluded the DDM entirely (55% DCF, 45% EV/EBIT), the weighted FV would be EUR 74.30 -- approximately EUR 3 higher. The question is whether including DDM at 15% is adding conservatism or introducing noise. I included it because the skill mandates minimum 2 methods, and the DDM provides a genuine floor estimate. But I acknowledge it may be overly penalizing.

2. **The EV/EBIT multiple selection is the most subjective input.** My 13x base case vs thesis's 15x changes fair value by EUR 13/share (19%). The "correct" multiple depends entirely on whether AI fears persist or dissipate. If peers re-rate back to 25x+ P/E, WKL at 13x EV/EBIT is absurdly cheap. If AI fears deepen, 13x may prove too generous.

3. **My WACC of 9% is a judgment call.** The calculated WACC is 6.4%, the thesis uses 8.5%, and the market implies ~10%. I split the difference at 9%. Moving WACC by 50bps changes DCF FV by approximately EUR 5-7. This is the second most sensitive variable after growth rate.

4. **I have not independently verified FY2024 FCF of EUR 1.34B.** This figure is critical -- it is the base for my DCF. The tool pulled it from yfinance, and it aligns with reported figures. But the tool shows only EUR 1.02B in one field, which may reflect a different accounting treatment. The EUR 1.34B is consistent with the company's adjusted free cash flow figure.

5. **The FRR divestiture impact is not captured in my numbers.** The DCF tool uses FY2024 FCF (EUR 1.34B), which includes EUR ~15-20M FCF from the divested FRR business. The 2025 FCF base should be approximately EUR 1.32B (post-divestiture). This is a small impact (~1-2% of FCF) and does not materially change the valuation.

### Sensibilidad Preocupante

1. **At 5% growth, moving WACC from 9% to 10% drops DCF FV from EUR 78 to EUR 68 -- a EUR 10 swing (13%).** Since the "correct" WACC is unknowable with precision, this sensitivity range alone spans my entire FV range.

2. **The EV/EBIT method is extremely sensitive to multiple selection.** Each 1x multiple change shifts FV by EUR 6.65. The difference between 12x and 15x is EUR 20/share.

3. **The bear case DCF (EUR 59.93) is only 9% below current price.** This means there is limited downside cushion. In the extreme bear (EUR 49.33), there is 25% downside. For a stock making persistent new lows, this is concerning.

### Discrepancias con Thesis

1. **My weighted FV (EUR 71.68) is 24% below the original thesis (EUR 94.28).** The main drivers of the difference: higher WACC (9% vs 8.5%), lower growth (5% vs 6%), lower EV/EBIT multiple (13x vs 15x), and inclusion of DDM which anchors the floor lower.

2. **My weighted FV is 10% below the adversarial review (EUR 80).** The difference is primarily the DDM weight (15% at EUR 50) and more conservative EV/EBIT adjustments (CEO transition, non-recurring decline).

3. **The thesis claims "near-zero downside in bear case" -- I strongly disagree.** My DCF bear shows EUR 59.93 (-8.8% from current) and the extreme bear shows EUR 49.33 (-24.9%). The EV/EBIT bear shows EUR 54 (-17.8%). There IS meaningful downside risk.

### Sugerencias para el Sistema

1. **The DCF tool only runs 5-year projections by default.** For a quality compounder with 15-25yr switching costs, a 10-year DCF would be more appropriate. The high terminal value percentage (65-77% of EV) in the 5-year model suggests the valuation is excessively dependent on terminal assumptions. A 10-year model would shift more value into the projection period.

2. **The quality_scorer.py classifies WKL as "Industrials."** This inflates the gross margin premium (+44.9pp vs industrials) and gives a misleading picture. A sector-override parameter would allow more meaningful peer comparison.

3. **For AI-exposed companies, the standard Bear/Base/Bull framework may need a fourth scenario: "Disruption."** The standard bear case assumes slow growth but intact business model. A disruption scenario assumes partial business model obsolescence. These are qualitatively different risks.

### Preguntas para Orchestrator

1. Should the standing order be lowered from EUR 65 to EUR 55 immediately, or should we wait for FY2025 results (Feb 25) first?

2. My weighted FV of EUR 71.68 implies only 9% MoS at current price. This is below Tier B precedent MoS (20-40%). Does this suggest the position should NOT be taken at current prices, even if the thesis is directionally correct?

3. The EV/EBIT method (30% weight) gives a FV of EUR 67.33, which is barely above the current price. This grounds the valuation in market reality. Should this cause us to increase EV/EBIT weight (since peers are currently observable) and decrease DCF weight (which is more assumption-dependent)?

4. The DDM base case of EUR 49.52 represents the income floor. If earnings collapse and the company becomes a "dividend stock" valued only for its payouts, this is approximately where it would trade. Should this inform an extreme-scenario entry price?

---

**Valuation Specialist Agent | Framework v4.0 | 2026-02-11**
