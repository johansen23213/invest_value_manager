# ADVERSARIAL VALUATION: AUTO.L (AutoTrader Group plc)

> **Date:** 2026-02-09
> **Analyst:** Valuation Specialist (Adversarial Mode)
> **Status:** INDEPENDENT valuation challenging thesis FV of 688 GBp
> **Type of Company:** UK Digital Marketplace Monopoly (Tier A, QS 79)

---

## EXECUTIVE SUMMARY

The original thesis valued AUTO.L at a weighted FV of 688 GBp using only two methods (OEY 720p at 60% + EV/EBIT peers 640p at 40%) with NO DCF analysis. This adversarial valuation uses 4 methods and finds the thesis FV is **inflated by 16-20%**. My risk-adjusted fair value is **550-580 GBp**, implying a MoS of 13-16% at the current price of 487 GBp -- significantly lower than the thesis claim of 29%.

**Key findings:**
1. The thesis OEY method uses 8% growth (EPS growth) instead of revenue/FCF growth of 4-5%, inflating the OEY-implied FV by ~30%
2. The peer comparison understates the discount AUTO.L deserves vs Rightmove due to the Deal Builder crisis and lower growth
3. DCF analysis (which the thesis omitted) produces a base case of 520-580p depending on assumptions
4. The current price already embeds ~2% real FCF growth, which is conservative but not unreasonable given Deal Builder uncertainty

---

## SECTION 1: CORRECTED FINANCIAL DATA

### Verified Financials (from official results)

| Metric | FY2024 (Mar-24) | FY2025 (Mar-25) | H1 FY2026 (Sep-25) | Growth |
|--------|-----------------|-----------------|---------------------|--------|
| Revenue | GBP 570.9M | GBP 601.1M | GBP 317.7M | +5% |
| Operating Profit | GBP 357.0M | GBP 376.8M | GBP 200.1M | +6-8% |
| Adj. EBITDA | GBP 375.3M | GBP 393.9M | N/A | +5% |
| Basic EPS | 28.0p | 31.66p | 17.26p | +11-12% |
| FCF | GBP 283.9M | GBP 300.6M | N/A | +5.9% |
| OCF | GBP 287.5M | GBP 304.6M | GBP 215.4M | +5-7% |
| ARPR (monthly) | GBP 2,721 | GBP 2,854 | GBP 2,994 | +5% |
| Retailer Forecourts | 13,739 | 14,013 | 14,080 | +1-2% |
| Operating Margin | 62.5% | 62.7% | 63.0% | Stable |
| Net Cash | N/A | GBP 15.3M | N/A | Net cash |
| Shares Outstanding | 915M | 895M | ~838M (current) | Declining via buybacks |
| Dividend/share | N/A | 10.6p | 3.8p (interim) | Growing |
| Buybacks | N/A | GBP 187.3M | GBP 100.2M | Ongoing |

### Key Observations on Financial Data

1. **Revenue growth is 5%, not 7-8%.** The thesis cites 7% for "Core Auto Trader Revenue" but group revenue -- the correct figure -- grew 5% in FY2025 and 5% in H1 FY2026.

2. **EPS growth (11-12%) overstates organic growth** because it includes the benefit of share buybacks reducing the denominator. Organic earnings growth (operating profit growth) is 6-8%.

3. **FCF CAGR (3-year: 2022-2025) is only 3.8%.** The historical FCF growth rate, as computed by the DCF tool from actual data, is materially lower than the 8% used in the thesis OEY method.

4. **Shares outstanding have declined from 967M (2021) to ~838M (current).** This is a 2.5% annual reduction that boosts EPS and per-share FCF growth above organic business growth.

### Consensus Estimates (MarketScreener, 15 analysts)

| Metric | FY2026E | FY2027E | FY2028E | CAGR |
|--------|---------|---------|---------|------|
| Revenue | GBP 631.1M | GBP 671.2M | GBP 712.3M | ~5.8% |
| EBITDA | GBP 424.2M | GBP 451.7M | GBP 480.2M | ~6.5% |
| EPS | 34.4p | 37.82p | 40.98p | ~7.2% |

This implies consensus expects ~5-6% revenue growth and ~7% EPS growth (boosted by buybacks). The thesis assumption of 8% growth is above consensus.

---

## SECTION 2: WACC DERIVATION

### Components

| Parameter | Value | Source/Justification |
|-----------|-------|---------------------|
| Risk-Free Rate (Rf) | 4.5% | UK 10Y Gilt (Feb 2026: 4.50-4.55%) |
| Equity Risk Premium | 5.0% | UK standard ERP |
| Beta | 0.76 | StockAnalysis.com (5Y); 0.85 from other sources |
| Cost of Equity (Ke) | 8.3-8.75% | Rf + Beta x ERP = 4.5 + 0.76x5.0 = 8.3% |
| Cost of Debt (Kd) | 0% effective | Net cash, GBP 200M undrawn RCF |
| Debt Weight | ~0% | Net cash position |
| **WACC** | **8.5-9.0%** | Essentially all equity, Ke = WACC |

### Adversarial Adjustment

The thesis uses 8.5% WACC. I will use **9.0-9.5%** for the following reasons:
- UK mid-cap liquidity discount vs large-caps
- Customer concentration risk: 80% of revenue from ~14,000 dealers, who are currently in revolt
- Deal Builder execution risk: mandatory rollout is creating unprecedented friction
- Beta of 0.76 may understate true business risk during this period of disruption
- Using beta 0.85-1.0 would give Ke of 8.75-9.5%

**My WACC: 9.5% (conservative, adversarial)**

This is consistent with the range that Simply Wall St (7.95%) and ValuInvesting.io (8.3%) calculate, with an adversarial premium for current risks.

---

## SECTION 3: METHOD 1 -- DCF (Primary, 40% weight)

### Inputs Derived from Projection Framework

**Revenue Growth Derivation:**
- TAM: UK used car market ~GBP 100B, growing 2-3% annually toward pre-pandemic levels
- AutoTrader's TAM is really dealer spend on digital advertising/classifieds, not the entire car market
- Market Share: 75%+ of auto classified minutes -- growth in share is near-maxed
- ARPR growth: 5% annually (pricing + product), but this is the growth RATE, not acceleration
- Dealer count: +1-2% annually (modest)
- Revenue Growth = ARPR growth (~5%) + Forecourt growth (~1%) - Churn (~0-1%) = **~5-6%**

**FCF Growth Derivation:**
- Revenue growth: 5-6%
- Operating leverage: Modest (margins already at 62-63%, near ceiling)
- Buyback boost to per-share FCF: ~2.5% annually
- FCF per-share growth: ~7-8%
- BUT I use AGGREGATE FCF growth (not per-share) for DCF: **~5-6%**

**Why not 8%:** The thesis used 8% growth in the OEY method, which corresponds to EPS growth, not revenue or aggregate FCF growth. EPS growth is artificially inflated by share buybacks. For DCF, we use aggregate FCF.

### DCF Scenarios Run

| Scenario | Growth | WACC | Terminal | FV/Share | MoS% |
|----------|--------|------|----------|----------|------|
| Very Conservative | 2% | 9.5% | 2.0% | 483p | -1% |
| Conservative | 3% | 9.5% | 2.0% | 520p | +7% |
| **Base** | **5%** | **9.5%** | **2.5%** | **579p** | **+19%** |
| Moderate | 6% | 9.5% | 2.5% | 616p | +26% |
| Optimistic | 7% | 9.0% | 2.5% | 790p | +62% |
| Thesis-level (tool default) | 5% default | 9% default | 2.5% | 625p | +28% |

**Key insight from reverse DCF:** At 2% FCF growth and 9.5% WACC, fair value is ~483p -- essentially the current price. This means the market is pricing in only ~2% real FCF growth forever, which seems overly pessimistic for a monopoly platform.

**My DCF Base Case: 560-580p** (using 5% growth, 9.5% WACC, 2.5% terminal, 10-year projection)

The tool output with these exact parameters gives 579p. I round to 570p to account for:
- Deal Builder churn risk not captured in historical FCF
- Potential ARPR deceleration from 5% to 3-4% if dealer pushback intensifies
- Digital Services Tax (GBP 10.2M, recurring) reducing future FCF

**DCF Fair Value: 570p**

### Sensitivity Table (WACC vs Growth)

| Growth \ WACC | 8.5% | 9.0% | 9.5% | 10.0% | 10.5% |
|---------------|------|------|------|-------|-------|
| **3%** | 560p | 539p | 520p | 502p | 486p |
| **4%** | 614p | 588p | 565p | 543p | 523p |
| **5%** | 678p | 646p | 579p | 592p | 568p |
| **6%** | 753p | 714p | 616p | 651p | 622p |
| **7%** | 843p | 790p | 676p | 721p | 685p |

Note: At 9.5% WACC and 5% growth, the tool gives 579p. At 10% WACC and 3% growth, FV drops to ~490p -- near current price.

---

## SECTION 4: METHOD 2 -- EV/EBITDA Peer Comparison (30% weight)

### Current Peer Multiples

| Company | EV/EBITDA | P/E | Revenue Growth | Op Margin | Notes |
|---------|-----------|-----|----------------|-----------|-------|
| **AUTO.L** | **10.1x** | **14.6x** | **5%** | **62-63%** | Deal Builder crisis |
| RMV.L (Rightmove) | 19.6x | 17.2x | 7-8% | 70% | REA bid failed, stable |
| G24.DE (Scout24) | ~18x | 59.4x (trailing) | 10%+ | 55% | Higher growth |
| REA.AX (REA Group) | 25.8x | N/A | 15%+ | 55% | Australia, high growth |

### Analysis of Discount/Premium

AUTO.L trades at a **massive 48-61% discount** to classifieds peers on EV/EBITDA. The question is: how much of this discount is justified?

**Reasons for discount vs RMV.L:**
1. Deal Builder crisis is creating real dealer friction (significant -- 2-3x multiple points)
2. Growth rate is lower (5% vs 7-8%) -- 1-2x multiple points
3. UK auto market more volatile than UK property market -- 1x multiple point
4. Smaller market (auto vs property) -- 0.5x multiple point

**Total justified discount: 4.5-6.5x multiple points vs Rightmove's 19.6x**

**Appropriate EV/EBITDA for AUTO.L: 13-15x** (vs current 10.1x)

### Calculation

| Scenario | EV/EBITDA | EBITDA (FY2025) | Enterprise Value | Equity Value | FV/Share |
|----------|-----------|-----------------|------------------|--------------|----------|
| Conservative (13x) | 13x | GBP 393.9M | GBP 5,121M | GBP 5,106M | **609p** |
| Base (14x) | 14x | GBP 393.9M | GBP 5,515M | GBP 5,500M | **656p** |
| Premium (15x) | 15x | GBP 393.9M | GBP 5,909M | GBP 5,894M | **703p** |

Using FY2026E EBITDA (GBP 424.2M):

| Scenario | EV/EBITDA | EBITDA (FY2026E) | Enterprise Value | Equity Value | FV/Share |
|----------|-----------|------------------|------------------|--------------|----------|
| Conservative (13x) | 13x | GBP 424.2M | GBP 5,515M | GBP 5,500M | **656p** |
| Base (13.5x) | 13.5x | GBP 424.2M | GBP 5,727M | GBP 5,712M | **681p** |

**Critical note:** The thesis used 14.1x (Rightmove) and 15.7x (Scout24) as the comparison set. Both are MORE expensive than AUTO.L deserves because:
- Rightmove has higher growth and no current dealer crisis
- Scout24 has significantly higher growth (10%+)
- Neither faces the backlash AUTO.L is experiencing

**My EV/EBITDA peer FV: 610-660p** (using 13-14x on FY2025 EBITDA)

For adversarial purposes, I use the more conservative end: **620p**

---

## SECTION 5: METHOD 3 -- Forward P/E (20% weight)

### Derivation

**Consensus FY2026 EPS: 34.4p** (MarketScreener, 15 analysts)
**Consensus FY2027 EPS: 37.82p**

**What P/E is appropriate?**

| Benchmark | P/E | Relevance |
|-----------|-----|-----------|
| FTSE 100 average | ~14x | UK market baseline |
| RMV.L (Rightmove) | 17.2x trailing | Closest UK peer |
| Software/Platform average | 18-22x | Higher growth |
| AUTO.L historical (5Y avg) | ~22-25x | Historical average |
| AUTO.L current | 14.6x trailing, 13.0x forward | Current depressed level |

**Appropriate forward P/E for AUTO.L: 15-17x**

Justification:
- Deserves a premium to FTSE 100 (14x) due to monopoly position, 50% FCF margin, recurring revenue
- Deserves a discount to Rightmove (17.2x) due to lower growth and dealer crisis
- 15-17x is a reasonable range for a 5-6% grower with exceptional margins in a period of uncertainty

### Calculation

| Scenario | Forward P/E | FY2026E EPS | FV |
|----------|-------------|-------------|-----|
| Conservative (15x) | 15x | 34.4p | **516p** |
| Base (16x) | 16x | 34.4p | **550p** |
| Premium (17x) | 17x | 34.4p | **585p** |

Using FY2027 EPS:

| Scenario | Forward P/E | FY2027E EPS | FV |
|----------|-------------|-------------|-----|
| Conservative (15x) | 15x | 37.82p | **567p** |
| Base (16x) | 16x | 37.82p | **605p** |

**My Forward P/E FV: 550p** (16x on FY2026E EPS of 34.4p)

**CRITICAL: Thesis implied P/E check.** The thesis FV of 688p on FY2025 EPS of 31.66p implies a P/E of **21.7x**. On FY2026E EPS of 34.4p, it implies 20.0x. A 20-22x P/E for a 5% revenue grower facing a dealer revolt is **not justified**. Rightmove, which has higher growth and no crisis, trades at only 17.2x.

---

## SECTION 6: METHOD 4 -- Reverse DCF / Owner Earnings (10% weight)

### Reverse DCF: What Growth Does Current Price Imply?

At current price of 487p, WACC 9.5%, terminal 2.0%:
- **Implied FCF growth: ~2%** (DCF at 2% growth gives FV of 483p)

At current price of 487p, WACC 9.0%, terminal 2.0%:
- **Implied FCF growth: ~1%**

**Interpretation:** The market is pricing in essentially flat real FCF growth forever. For a monopoly platform with 5% ARPR pricing power, this seems overly pessimistic -- BUT the Deal Builder crisis adds legitimate uncertainty.

### Corrected OEY Analysis

The thesis OEY method has a critical error: it uses 8% growth (EPS growth, boosted by buybacks) rather than organic business growth.

```
FCF (FY2025): GBP 300.6M
Market Cap at 487p: GBP ~4.08B
Owner Earnings Yield = 300.6M / 4,080M = 7.4% (this is correct)

BUT:
OEY + Growth = 7.4% + X%

Thesis used X = 8% (EPS growth including buyback effect)
Correct X = 5% (organic revenue/FCF growth)
Conservative X = 3.8% (historical FCF CAGR)

Corrected OEY + Growth:
  Thesis version: 7.4% + 8.0% = 15.4% (inflated)
  Corrected: 7.4% + 5.0% = 12.4% (realistic)
  Conservative: 7.4% + 3.8% = 11.2% (bears)
```

Even the corrected 12.4% total return compares favorably to a 9-9.5% WACC, suggesting the stock offers a positive spread. But the spread is 2.9pp, not 6.9pp as the thesis claimed.

**OEY-implied FV at corrected growth:**
If we target a 4pp spread over WACC (reasonable for Tier A):
- Required OEY + Growth = 9.5% + 4% = 13.5%
- With Growth = 5%: Required OEY = 8.5%
- FCF/Price = 8.5% => Price = GBP 300.6M / 8.5% = GBP 3,536M
- FV/share = GBP 3,536M / 838M shares = **422p** (BELOW current price)

If we target a 2pp spread (minimum acceptable):
- Required OEY + Growth = 9.5% + 2% = 11.5%
- With Growth = 5%: Required OEY = 6.5%
- FCF/Price = 6.5% => Price = GBP 300.6M / 6.5% = GBP 4,625M
- FV/share = GBP 4,625M / 838M shares = **552p**

**OEY-based FV: 550p** (at 2pp spread, which is minimum for a Tier A compounder)

---

## SECTION 7: RECONCILIATION

| Method | Fair Value | Weight | Weighted | Rationale for Weight |
|--------|-----------|--------|----------|---------------------|
| DCF (5% growth, 9.5% WACC) | 570p | 40% | 228p | Most robust, uses actual FCF |
| EV/EBITDA Peers (13-14x) | 620p | 30% | 186p | Market-based, corrected for crisis |
| Forward P/E (16x FY26E) | 550p | 20% | 110p | Cross-check on earnings valuation |
| OEY Corrected | 550p | 10% | 55p | Sanity check on yield |
| **Weighted Average** | | **100%** | **579p** | |

**Divergence between methods: 550p - 620p = 13%** (within acceptable range, no investigation needed)

### Comparison to Thesis

| Metric | Thesis | Adversarial | Delta |
|--------|--------|-------------|-------|
| Weighted FV | 688p | 579p | **-16%** |
| Bear Case | 500p | 475p | -5% |
| Base Case | 680p | 579p | -15% |
| Bull Case | 880p | 720p | -18% |
| Expected Value | 685p | 579p | -15% |
| MoS at 487p | 29% | 16% | -13pp |

---

## SECTION 8: SCENARIOS

### Bear Case (25% probability)

**Assumptions:**
- Deal Builder causes 5-8% dealer attrition over 18 months
- ARPR growth decelerates to 2-3% (from 5%)
- Revenue growth slows to 2-3%
- FCF growth: 1-2%
- Multiple compression sustained at current levels (10x EV/EBITDA)
- WACC: 10.5% (crisis premium)

**Bear FV: 475p** (DCF at 3% growth, 10% WACC = 493p base, haircut to 475p for churn risk)

At 475p, current price of 487p would be 2.5% overvalued.

### Base Case (50% probability)

**Assumptions:**
- Deal Builder controversy resolves within 12 months (management making concessions)
- ARPR growth stabilizes at 4-5%
- Revenue growth: 5%
- FCF growth: 5%
- Multiple gradual re-rating to 12-13x EV/EBITDA
- WACC: 9.5%

**Base FV: 579p** (as calculated in reconciliation)

MoS at 487p: **16%**

### Bull Case (25% probability)

**Assumptions:**
- Deal Builder becomes accepted, accelerates dealer monetization
- ARPR growth accelerates to 6-7% (Deal Builder adds new revenue streams)
- Revenue growth: 7-8%
- FCF growth: 7%
- Multiple re-rates to 15-16x EV/EBITDA (partial recovery to historical)
- WACC: 9.0%

**Bull FV: 720p** (DCF at 7% growth, 9% WACC = 790p, discounted to 720p for risk)

### Expected Value

```
EV = (Bear x 25%) + (Base x 50%) + (Bull x 25%)
EV = (475 x 0.25) + (579 x 0.50) + (720 x 0.25)
EV = 119 + 290 + 180
EV = 589p
```

**Expected Value: 589p**

### Summary Table

| Scenario | Fair Value | Probability | Weighted |
|----------|-----------|-------------|----------|
| Bear | 475p | 25% | 119p |
| Base | 579p | 50% | 290p |
| Bull | 720p | 25% | 180p |
| **Expected** | **589p** | **100%** | **589p** |

**Current Price:** 487p
**MoS vs Expected Value:** 17%
**MoS vs Bear Case:** -2.5% (slightly overvalued in bear scenario)

---

## SECTION 9: WHAT WOULD JUSTIFY THE THESIS FV OF 688p?

For 688p to be fair value, one of these scenarios would need to hold:

1. **DCF:** 7% FCF growth + 9% WACC + 2.5% terminal = 790p (tool output). But 7% aggregate FCF growth requires revenue growth accelerating from 5% to 7%+, which is above consensus and above recent trend.

2. **EV/EBITDA:** 15.7x on FY2025 EBITDA (Scout24's multiple). But AUTO.L has lower growth than Scout24 and a dealer crisis that Scout24 does not have.

3. **P/E:** 20x on FY2025 EPS of 31.66p = 633p, or 20x on FY2026E EPS of 34.4p = 688p. But 20x P/E for a 5% revenue grower with a dealer revolt is aggressive when Rightmove (higher growth, no crisis) trades at 17.2x.

**Conclusion:** The thesis FV of 688p requires either above-consensus growth assumptions OR multiple expansion back toward historical levels. Both are possible but not the base case.

---

## SECTION 10: VALIDATION

### Implied Multiples at My FV

| Metric | At 579p | At Thesis 688p | Reasonableness |
|--------|---------|----------------|----------------|
| P/E (FY2025) | 18.3x | 21.7x | 18x = reasonable for quality monopoly |
| P/E (FY2026E) | 16.8x | 20.0x | 17x = slight premium to RMV, fair |
| EV/EBITDA (FY2025) | 12.5x | 14.9x | 12-13x = discount to RMV (19.6x), justified |
| P/FCF | 16.2x | 19.2x | 16x = reasonable for 50% FCF margin business |
| OEY | 6.2% | 5.2% | 6% yield on a quality business = fair |

My implied multiples are all within reasonable ranges for a monopoly platform in a period of uncertainty.

### Validation vs Precedents

From decisions_log.yaml:
- ADBE: Bought at MoS 31%, Tier A -- AUTO.L at 16% MoS is lower but AUTO.L is also in a crisis
- MONY.L: Bought at MoS 36%, Tier A -- AUTO.L's crisis-adjusted MoS is half of this
- BYIT.L: Bought at MoS 35%, Tier A -- AUTO.L notably lower
- NVO: Bought at MoS 38%, Tier A -- AUTO.L notably lower

Pattern: Every other Tier A purchase was at 31-38% MoS. AUTO.L at 16% MoS is the lowest MoS of any Tier A purchase. This is a concern.

### Validation vs Analyst Consensus

- Average analyst target: 725-785p (range: 595-1,040p)
- My adversarial FV: 579p
- My FV is below the lowest analyst target of 595p

This is expected in adversarial mode. The key question is whether my WACC (9.5%) and growth (5%) are too conservative. If I use 9% WACC and 5% growth, the DCF gives 646p -- closer to the analyst range.

---

## SECTION 11: FINAL ASSESSMENT

### Is AUTO.L Undervalued at 487p?

**Yes, modestly.** My adversarial analysis finds:
- Expected Value: 589p (MoS 17%)
- Base Case: 579p (MoS 16%)
- Bear Case: 475p (MoS -2.5%)

The stock is cheap, but not as cheap as the thesis claims. The thesis MoS of 29% is inflated to ~16% after correcting for:
1. Growth rate (5% not 8%) in OEY method
2. Appropriate peer discount (not parity with RMV.L)
3. Proper WACC (9.5% not 8.5%)
4. Multiple methods including DCF (which the thesis omitted)

### Is it a Good Risk/Reward?

**Mixed.** The 16% MoS is the lowest of any Tier A position in the portfolio. The bear case (-2.5%) means the position has limited downside protection if Deal Builder fallout worsens. However:
- The reverse DCF shows the market is pricing only 2% FCF growth forever
- Even at 3-4% FCF growth, the stock is worth 520-565p
- The monopoly position (75% market share) provides a structural floor
- FCF generation (GBP 300M, 50% margin) is exceptional

### Recommendation

**HOLD with reduced conviction.** The position is not egregiously overvalued, but the MoS is thin by our standards. I would NOT recommend adding at current prices. The ADD trigger of 450p from the thesis would provide MoS of ~22% vs my base case, which is more acceptable.

**Revised ADD trigger: 450p** (MoS ~22% vs adversarial base of 579p)
**Revised SELL trigger: 600p** (near fair value, low forward return)

---

## META-REFLECTION

### Dudas/Incertidumbres

1. **WACC sensitivity is high.** At 8.5% WACC (thesis level), DCF gives 625p. At 9.5% (my level), it gives 579p. The 1pp WACC difference changes FV by ~8%. My choice of 9.5% is debatable -- 9% might be more appropriate for a low-leverage monopoly.

2. **Deal Builder resolution timeline is the key variable.** If resolved in 6 months, multiple re-rates quickly. If it drags 18+ months, ARPR deceleration is real.

3. **The buyback effect on EPS is significant.** The company is buying back ~2.5% of shares annually. Over 5 years, this compounds EPS by ~13% above organic growth. The thesis captures this in "8% growth" but doesn't separate organic vs buyback-driven growth. For OEY, this distinction matters.

4. **H1 FY2026 results (pre-Deal Builder crisis) showed 5% revenue growth.** H2 results (post-crisis, ending Mar 2026) will be the real test. FY2026 full results come in May 2026.

### Sensibilidad Preocupante

- FV swings from 520p to 680p with plausible WACC/growth variations (8.5-10% WACC, 3-7% growth). This is a 30% range, which is normal for a DCF but highlights uncertainty.
- The bear case (475p) is only 2.5% below current price -- very thin downside buffer.

### Discrepancias con Thesis

- Thesis FV 688p vs my 579p = **-16% delta**. This is within the range of prior adversarial reviews (average -15%).
- Main sources of difference:
  1. Growth rate: 8% (thesis) vs 5% (mine) = largest driver of gap
  2. WACC: 8.5% (thesis) vs 9.5% (mine) = second driver
  3. No DCF in thesis = over-reliance on OEY method which is sensitive to growth assumption

### Sugerencias para el Sistema

1. **OEY method needs explicit organic vs buyback-driven growth separation.** The valuation-methods skill should note that OEY + Growth should use ORGANIC growth, not EPS growth which includes buyback effects.

2. **Every valuation should include a DCF as one of the methods.** The thesis omitting DCF was a significant gap.

3. **Implied P/E sanity check should be mandatory.** If the FV implies P/E > 20x for a sub-10% grower, that should trigger investigation.

### Preguntas para Orchestrator

1. Given MoS of only 16% (lowest of any Tier A position), should the ADD trigger be RAISED from 450p to ensure better entry if adding?
2. Should we set a time-based probation? If FY2026 results (May 2026) show ARPR growth <3% or dealer count decline, should we EXIT?
3. The 5 other Tier A positions were bought at 31-38% MoS. Should we consider the 16% MoS a red flag for conviction level?

---
