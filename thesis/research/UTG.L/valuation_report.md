# INDEPENDENT ADVERSARIAL VALUATION: UTG.L (Unite Group PLC)

**Date:** 2026-02-08
**Agent:** Valuation Specialist (Independent Adversarial)
**Status:** Standing Order evaluation at 540 GBp trigger

---

## Company Classification

**Type of enterprise:** Asset-Heavy REIT (UK PBSA)
**Quality Score (tool):** 27 (Tier D) -- DISTORTED for REITs
**REIT-adjusted QS estimate:** ~50-55 (Tier C)
**Methods selected:** NAV-Based (primary) + DDM (secondary) + FFO Multiple (tertiary) + EV/EBITDA cross-check

**Rationale for Tier C treatment:** The quality_scorer.py penalizes REITs on FCF (negative due to development capex) and leverage (high by design for REITs). Adjusted for REIT-specific distortions, Unite is a Tier C company, meaning we apply conservative multiples and require higher MoS.

---

## KEY DATA INPUTS (Real, Verified)

| Metric | Value | Source |
|--------|-------|--------|
| **Current price** | 580 GBp | price_checker.py 2026-02-08 |
| **EPRA NTA per share** | 986p | H1 2025 results (Jun 2025) |
| **Adj EPS FY2025** | 47.5-48.25p | Company guidance (reiterated Jan 2026) |
| **Adj EPS FY2026E** | 43-44.5p (-7-10% guided) | Company guidance |
| **Dividend FY2025** | 37.3p | Company |
| **Dividend FY2026E** | ~37.3p (flat guided) | Company |
| **Occupancy FY2025/26** | 95.2% | Company actual |
| **Occupancy FY2026/27 target** | 93-96% | Company guidance |
| **Rental growth FY2025/26** | 4.0% | Company actual |
| **Rental growth FY2026/27E** | 2-3% | Company guidance |
| **LTV** | 26% | Company |
| **Net Debt/EBITDA** | 5.3x | Company |
| **Interest coverage** | 6.9x | Company |
| **Cost of debt** | 3.6% (2024) -> 4.1-4.5% (2026E) | Company/estimates |
| **UK 10Y Gilt** | 4.55% | TradingEconomics Feb 2026 |
| **Beta** | 1.24 (market) / 0.67 (adjusted) | Yahoo Finance / GuruFocus |
| **USAF portfolio yield** | 5.3% | Q4 2025 fund valuations |
| **LSAV portfolio yield** | 4.7% | Q4 2025 fund valuations |
| **Reservations 2026/27** | 64% (vs 67% prior year) | Jan 2026 trading update |
| **Analyst consensus target** | 884 GBp (range 757-1,205) | Various |
| **Stifel target** | 600 GBp (downgrade to Hold) | Stifel Nov 2025 |
| **Shares outstanding** | ~491M | Derived from market cap |

---

## WACC DERIVATION (Independent)

The thesis uses WACC of 6.4%. Let me recalculate independently.

### Cost of Equity (Ke)

```
Risk-Free Rate = 4.55% (UK 10Y Gilt, Feb 2026 - ACTUAL)
  Note: Thesis used 4.0% - outdated. Gilts have risen.

Beta = 1.24 (market beta from Yahoo Finance)
  Note: Thesis used 0.65. GuruFocus uses 0.67 (adjusted).
  PROBLEM: 1.24 reflects Unite's high price volatility (stock fell from 885p to 504p).
  This is NOT fundamental risk but market sentiment.
  For a defensive REIT, a market beta of 1.24 is excessive.
  I will use 0.85 as compromise - higher than thesis (0.65) but lower than
  raw market beta (1.24). REITs are rate-sensitive, justifying beta > 0.65.

Equity Risk Premium = 5.0% (UK consensus)

Ke = 4.55% + 0.85 * 5.0% = 4.55% + 4.25% = 8.80%
```

### Cost of Debt (Kd)

```
Cost of debt (pre-tax): 4.5% (FY2026E, guided rising from 3.6%)
Tax rate: 0% (UK REIT exempt)
Kd after-tax = 4.5%
```

### Capital Structure

```
Market Cap = 580p * 491M = GBP 2,848M
Net Debt = ~GBP 1,450M (from H1 2025)
Enterprise Value = GBP 4,298M

E/V = 66.3%
D/V = 33.7%
```

### WACC

```
WACC = (66.3% * 8.80%) + (33.7% * 4.5%)
     = 5.83% + 1.52%
     = 7.35%

vs. Thesis WACC: 6.4% (DIFFERENCE: +0.95pp)
```

**Why my WACC is higher:**
1. UK 10Y gilt is 4.55%, not 4.0% (thesis assumption was stale)
2. Beta of 0.85 vs 0.65 (REITs are rate-sensitive; 0.65 underestimates)
3. Cost of debt rising to 4.5% vs 3.6% used in older calculations

**This WACC difference is material.** It significantly impacts DDM and any income-based valuation.

---

## METHOD 1: NAV-BASED (Primary for REITs) -- Weight 35%

### What is the EPRA NTA of 986p actually worth?

**Key question: Is the 986p NAV reliable?**

The NAV was independently valued by CBRE and Knight Frank at 30 June 2025. The blended portfolio yields were:
- USAF: 5.3%
- LSAV: 4.7%
- Whole portfolio: ~5.1% net initial yield

**Cap rate analysis:**
- The 5.1% portfolio yield was used for June 2025 valuation
- Since then, Q4 2025 saw capital value declines of -0.7% (USAF) and -1.4% (LSAV)
- UK gilt yields have remained elevated at 4.55%
- If PBSA cap rates expand by 25-50bps (from 5.1% to 5.35-5.6%), NAV would compress materially

**NAV sensitivity to cap rate expansion:**

| Cap Rate | Estimated NAV/share | Change vs 986p |
|----------|-------------------|----------------|
| 5.1% (current) | 986p | 0% |
| 5.35% (+25bps) | ~940p | -4.7% |
| 5.6% (+50bps) | ~895p | -9.2% |
| 5.85% (+75bps) | ~855p | -13.3% |
| 6.1% (+100bps) | ~815p | -17.3% |

**Is 986p NAV conservative or aggressive?**

Arguments NAV is overstated:
1. PBSA vacancy rate rose to 11.2% in 2024/25 (from 3.5% prior year) - Cushman & Wakefield data
2. Pockets of oversupply in Sheffield (student-to-bed ratio 1.21:1), Leeds, Nottingham
3. International student demand falling (visa changes, affordability)
4. Cap rates could expand further if gilt yields stay elevated
5. Q4 2025 saw further property value declines (-0.7% to -1.4%)

Arguments NAV is reliable:
1. Independent CBRE/Knight Frank valuations
2. National student-to-bed ratio still >2:1
3. S&P BBB+ credit rating affirmed
4. Development pipeline yield on cost 6.8% > portfolio yield
5. 93% exposure to Russell Group universities (highest quality)

**My assessment:** NAV is likely slightly overstated due to rising vacancy and cap rate pressure. I will apply haircuts:

### NAV Scenarios

| Scenario | Haircut | NAV/share | Reasoning |
|----------|---------|-----------|-----------|
| Optimistic | -10% | 887p | Minor cap rate expansion, occupancy normalizes |
| Base | -20% | 789p | Cap rate expansion 50-75bps, occupancy at low end |
| Conservative | -30% | 690p | Cap rate expansion 100bps, prolonged occupancy weakness |
| Stress | -40% | 592p | Severe downturn, matches current price discount |

**CRITICAL CONTEXT:** UK REITs trade at average 18% discount to NAV (large-caps at -11%, mid-caps at -12%, small-caps at -25%). UTG at 580p vs NAV 986p = 41% discount. The average UK REIT discount widened to 35.6% at end-2024.

**But Unite's discount may be JUSTIFIED, not a "mistake":**
- PBSA vacancy rising from 3.5% to 11.2% is a structural shift
- Graduate Route visa cut from 24 to 18 months (Jan 2027) reduces demand
- Student affordability crisis is real
- Some cities (Sheffield, Leeds, Nottingham) approaching oversupply

**NAV-based Fair Value (adversarial):**
I weight toward the Base-Conservative scenarios:
- NAV FV = (887p * 20%) + (789p * 50%) + (690p * 30%) = 177 + 395 + 207 = **779p**

But this is NOT what the market should pay. The market applies a discount to NAV for REITs.

**Appropriate discount to NAV for UTG:**
- Average UK REIT: -18%
- Average large-cap UK REIT: -11%
- Sector-wide at end-2024: -35.6%
- UTG historical range: +20% premium to -30% discount

Given the current headwinds (occupancy decline, visa risk, rising costs), a discount of 25-35% to NAV is appropriate for the next 12-18 months. Using 30% discount to my adjusted NAV of 789p:

**NAV Method Fair Value = 789p * (1 - 0.30) = 552p**

Wait -- this is important. The 30% discount to an already-haircut NAV gives 552p, BELOW the current price of 580p. Let me reconsider.

The correct approach: Apply haircut to NAV to get "true" NAV, then decide if any discount to that true NAV is warranted.

If cap rates expand 50bps (to ~5.6%), NAV goes to ~895p. Then apply a "normal" sector discount of -15% to -25%:
- At -15%: 895 * 0.85 = 761p
- At -20%: 895 * 0.80 = 716p
- At -25%: 895 * 0.75 = 671p

If cap rates expand 75bps (to ~5.85%), NAV goes to ~855p:
- At -15%: 855 * 0.85 = 727p
- At -20%: 855 * 0.80 = 684p
- At -25%: 855 * 0.75 = 641p

**NAV Method Fair Value range: 641-761p**
**NAV Method Fair Value (central): 700p** (using 75bps expansion + 20% discount)

---

## METHOD 2: DDM (Dividend Discount Model) -- Weight 30%

### Gordon Growth Model

**Current dividend:** 37.3p
**Guided FY2026:** ~37.3p (flat)

**Key question: What is the sustainable dividend growth rate?**

Thesis uses g = 2.5%. Let me verify:

**Sustainable growth = ROE * (1 - Payout)**
- ROE for REITs is complicated by property valuations
- Using FFO-based ROE: FFO ~48p / NTA 986p = 4.9% FFO yield on book
- Payout ratio = 37.3p / 48p = 77.7%
- Sustainable growth = 4.9% * (1 - 0.777) = 4.9% * 0.223 = 1.1%

But that is too mechanical for a REIT. Let me think about dividend growth drivers:
- Rental growth: 2-3% (guided near-term, 3-4% long-term historical)
- Development completions: add ~2-3% incremental income over time
- Cost of debt rising: -1pp headwind near-term
- Share buyback: +0.5pp boost (reducing share count)
- Disposition program: neutral to slightly negative (disposing weaker assets)

**Near-term dividend growth (2-3 years):** 0-1% (flat to modest)
- FY2026 EPS declining 7-10%, dividend flat
- FY2027 return to growth but modest
- Near-term headwinds dominate

**Long-term dividend growth (5+ years):** 2-3%
- Rental growth tracks inflation + some real growth
- Development pipeline adds beds at 6.8% yield on cost
- Empiric synergies (13.7M/year) fully realized

**My dividend growth assumption:**
- Years 1-3: 0% (flat)
- Years 4+: 2.0% (conservative long-term, below thesis 2.5%)

**Required return (Ke):** The thesis uses 8%. With current gilt at 4.55%, this seems LOW for a REIT with declining earnings and occupancy risk.

Appropriate required return:
- UK 10Y gilt: 4.55%
- REIT risk premium: 3.5-4.5% (based on CAPM with beta 0.85)
- Total Ke: 8.0-9.0%

I will use a range of 8.0% to 9.0% (Ke) and 1.5% to 2.5% (g).

### DDM Sensitivity Table

**Using D1 = 37.3p (flat dividend)**

| g \ Ke | 7.5% | 8.0% | 8.5% | 9.0% | 9.5% |
|--------|-------|-------|-------|-------|-------|
| **0.0%** | 497p | 466p | 439p | 414p | 393p |
| **0.5%** | 533p | 497p | 466p | 439p | 414p |
| **1.0%** | 574p | 533p | 497p | 466p | 439p |
| **1.5%** | 622p | 574p | 533p | 497p | 466p |
| **2.0%** | 679p | 622p | 574p | 533p | 497p |
| **2.5%** | 746p | 679p | 622p | 574p | 533p |
| **3.0%** | 830p | 746p | 679p | 622p | 574p |

**Thesis DDM used:** Ke=8%, g=2.5% --> 679p (but thesis claimed 720p, which uses D1=38.2p with growth applied to D0)

**My DDM assessment:**
- Most likely range: Ke 8.5-9.0%, g 1.5-2.0%
- Central: Ke = 8.5%, g = 2.0% --> **574p**
- Optimistic: Ke = 8.0%, g = 2.5% --> **679p**
- Conservative: Ke = 9.0%, g = 1.5% --> **497p**

**DDM Fair Value range: 497-679p**
**DDM Fair Value (central): 574p**

This is SIGNIFICANTLY below the thesis DDM of 720p (thesis was too optimistic on both g and Ke).

---

## METHOD 3: FFO/AFFO MULTIPLE -- Weight 25%

### What do peers actually trade at?

**Unite Group current multiples:**
- Price/FFO: 580p / 48p (FY2025E) = 12.1x
- Price/FFO: 580p / 43p (FY2026E trough) = 13.5x

**Stifel's approach:** Valued UTG at 6.5% dividend yield --> 37.3p / 6.5% = 574p. This is essentially a yield-based approach, not FFO multiple.

**Thesis claims UK PBSA REITs trade at 14-20x FFO historically.** But:
1. That was in a lower-rate environment (2019-2021)
2. Current rate environment suggests REIT multiples should be lower
3. Xior (European student housing) has EV/EBITDA of 41.6x but FFO/share has collapsed (not comparable)
4. With no direct UK PBSA peers remaining (Empiric acquired, GCP Student Living taken private), comparables are difficult

**Comparable multiple analysis:**

| Peer/Reference | P/FFO Multiple | Context |
|----------------|---------------|---------|
| UK diversified REITs (2025) | 10-14x | Sector average |
| UTG historical average (2015-2019) | 18-22x | Pre-COVID, low rates |
| UTG current | 12.1x (FY25) / 13.5x (FY26) | Current market |
| Stifel implied | 12.0x (at 574p/48p) | Nov 2025 target |
| Sector-appropriate range (current) | 11-14x | Rate-adjusted |

**My FFO Multiple Assessment:**

Using FY2026 trough FFO of ~43p (conservative):

| Multiple | Fair Value | Context |
|----------|-----------|---------|
| 11x | 473p | Bear - rates stay high, occupancy weak |
| 12x | 516p | Conservative - current market environment |
| 13x | 559p | Base - modest recovery expected |
| 14x | 602p | Moderately optimistic |
| 15x | 645p | Optimistic - occupancy fully recovers |
| 16x | 688p | Bull - sector re-rates on rate cuts |

Using FY2027E normalized FFO of ~47p (assumes occupancy recovery):

| Multiple | Fair Value | Context |
|----------|-----------|---------|
| 12x | 564p | Conservative |
| 13x | 611p | Base |
| 14x | 658p | Moderately optimistic |

**My FFO Multiple assessment:**
- FY2026 trough at 12-14x: 516-602p
- FY2027 normalized at 13-14x: 611-658p
- Central (blending trough + recovery): **580p**

**FFO Multiple Fair Value range: 516-658p**
**FFO Multiple Fair Value (central): 580p**

Note: This method produces a fair value almost exactly at the current price.

---

## METHOD 4: EV/EBITDA Cross-Check -- Weight 10%

**Unite's current EV/EBITDA:** Reported as ~12x (from thesis) to ~24x (from some sources). The discrepancy likely comes from different EBITDA definitions.

Using the thesis figure of ~12x:
- UK REIT M&A EV/EBITDA: 3-6x (general M&A) to 15-18x (listed REITs)
- For context, UK commercial property REITs trade at wide ranges

This method is less reliable for REITs due to EBITDA definition issues. I include it only as a sanity check.

**At 12x EV/EBITDA (current), the market is pricing Unite fairly** for the current environment.

**EV/EBITDA does not suggest significant under- or over-valuation.**

---

## RECONCILIATION OF METHODS

| Method | Fair Value | Weight | Weighted FV |
|--------|-----------|--------|-------------|
| NAV-Based (haircut + discount) | 700p | 35% | 245p |
| DDM (central) | 574p | 30% | 172p |
| FFO Multiple (blended) | 580p | 25% | 145p |
| EV/EBITDA cross-check | ~580p | 10% | 58p |
| **Weighted Average** | | **100%** | **620p** |

**Divergence analysis:**
- NAV method (700p) vs DDM (574p) = 22% divergence
- NAV method (700p) vs FFO (580p) = 21% divergence
- DDM (574p) vs FFO (580p) = 1% divergence (excellent agreement)

**Key insight:** The income-based methods (DDM and FFO) converge around 574-580p, while the asset-based method (NAV) gives 700p. This divergence (22%) is BELOW the 30% threshold but still informative.

**Why the divergence exists:**
1. The NAV reflects property values at BOOK cap rates (~5.1-5.3%)
2. But the market is pricing the INCOME stream at a higher required yield (~8.5%)
3. This gap = the "NAV discount" = the market saying property values will decline OR income won't grow enough to justify asset values
4. This is NORMAL for REITs in a high-rate environment

**My assessment:** I give more weight to the income-based methods because:
- We are in a high-rate environment where income valuation matters more
- NAV depends on cap rate assumptions that may be stale
- The market clearly values Unite on income, not assets

**Adjusted weights favoring income methods:**
- NAV: 25% (reduced)
- DDM: 35% (increased)
- FFO: 30% (increased)
- EV/EBITDA: 10%

| Method | Fair Value | Adj Weight | Weighted FV |
|--------|-----------|------------|-------------|
| NAV-Based | 700p | 25% | 175p |
| DDM | 574p | 35% | 201p |
| FFO Multiple | 580p | 30% | 174p |
| EV/EBITDA | ~580p | 10% | 58p |
| **Adj Weighted Average** | | **100%** | **608p** |

---

## SCENARIO ANALYSIS

### BEAR CASE (25% probability)

**Assumptions:**
- Occupancy stays at 93% for 2 years
- Rental growth falls to 1-2%
- Dividend cut 5-10% (to ~34p)
- Interest rates stay high (gilts 4.5%+)
- Cap rates expand 75-100bps
- International student demand declines further
- Vacancy issues spread from regional cities

**Valuation:**
- DDM: D=34p, Ke=9.5%, g=1% --> 400p
- FFO Multiple: FY26 FFO 40p * 11x = 440p
- NAV: 855p * 0.65 = 556p
- Bear FV (blended): **450p**

### BASE CASE (50% probability)

**Assumptions:**
- Occupancy recovers to 94-96% over 18 months
- Rental growth 2-3%
- Dividend flat 37.3p, growing from FY2028
- BoE cuts modestly, gilts drift to 4.0-4.25%
- Empiric synergies on track (13.7M/year)
- International demand stabilizes at lower level

**Valuation:**
- DDM: D=37.3p, Ke=8.5%, g=2% --> 574p
- FFO Multiple: FY27 FFO 47p * 13x = 611p
- NAV: 895p * 0.80 = 716p
- Base FV (blended): **610p**

### BULL CASE (25% probability)

**Assumptions:**
- Occupancy recovers to 97%+ (supply-demand fundamentals win)
- Rental growth 4%+
- BoE cuts significantly, gilts fall to 3.5%
- Empiric synergies exceed targets
- Dividend grows 3-4% from FY2027
- Sector re-rates

**Valuation:**
- DDM: D=38.4p, Ke=7.5%, g=3% --> 853p
- FFO Multiple: FY27 FFO 50p * 15x = 750p
- NAV: 986p * 0.95 = 937p
- Bull FV (blended): **790p**

### EXPECTED VALUE

```
Expected Value = (450p * 25%) + (610p * 50%) + (790p * 25%)
               = 112.5p + 305p + 197.5p
               = 615p

vs. Thesis EV = 745p (DELTA: -130p, -17.4%)
```

---

## COMPARISON: THESIS FV vs ADVERSARIAL FV

| Metric | Thesis v2 | Adversarial | Delta |
|--------|-----------|-------------|-------|
| **NAV method** | 887p | 700p | -21% |
| **DDM method** | 720p | 574p | -20% |
| **FFO Multiple** | 645p | 580p | -10% |
| **Blended FV** | 745p | 608p | -18% |
| **Expected Value** | 745p | 615p | -17% |
| **Bear case** | 610p | 450p | -26% |
| **WACC used** | 6.4% | 7.35% | +0.95pp |
| **DDM Ke** | 8.0% | 8.5% | +0.5pp |
| **DDM g** | 2.5% | 2.0% | -0.5pp |
| **NAV haircut** | -10% | -10% to -15% cap rate, then -20% mkt discount | Much deeper |

**Key differences explained:**
1. **Gilt yield stale in thesis (4.0% vs 4.55% actual)** -- This alone increases Ke by ~0.47pp
2. **Beta too low in thesis (0.65 vs 0.85 used here)** -- REITs ARE rate-sensitive
3. **DDM growth rate optimistic (2.5% vs 2.0%)** -- Near-term dividend flat, sustainable growth ~2%
4. **NAV haircut insufficient** -- Thesis applies only -10%; PBSA vacancy rising to 11.2% in key markets
5. **No market discount to NAV in thesis** -- UK REITs trade at 18-35% discount; thesis just haircuts property values
6. **FFO multiple too high in thesis (14-16x)** -- In current rate environment, 12-14x is appropriate

---

## PRICE ACTION AND MARGIN OF SAFETY

```
Current price:              580 GBp
Adversarial Expected FV:    615p
Adversarial Base Case:      610p
Adversarial Bear Case:      450p
Thesis FV:                  745p

MoS vs Adversarial EV:     (615 - 580) / 615 = 5.7%
MoS vs Adversarial Base:   (610 - 580) / 610 = 4.9%
MoS vs Adversarial Bear:   (450 - 580) / 450 = -28.9% (OVERVALUED in bear)
MoS vs Thesis FV:          (745 - 580) / 745 = 22.1%

At Standing Order trigger 540p:
MoS vs Adversarial EV:     (615 - 540) / 615 = 12.2%
MoS vs Adversarial Base:   (610 - 540) / 610 = 11.5%
MoS vs Adversarial Bear:   (450 - 540) / 450 = -20.0% (still overvalued in bear)
MoS vs Thesis FV:          (745 - 540) / 745 = 27.5%
```

---

## SENSITIVITY TABLE: DDM (PRIMARY INCOME METHOD)

| g \ Ke | 7.5% | 8.0% | 8.5% | 9.0% | 9.5% |
|--------|-------|-------|-------|-------|-------|
| **1.0%** | 574p | 533p | 497p | 466p | 439p |
| **1.5%** | 622p | 574p | 533p | 497p | 466p |
| **2.0%** | 679p | 622p | 574p | 533p | 497p |
| **2.5%** | 746p | 679p | 622p | 574p | 533p |
| **3.0%** | 830p | 746p | 679p | 622p | 574p |

**Highlighted cells:** The thesis DDM (Ke=8%, g=2.5%) gives 679p. My central (Ke=8.5%, g=2.0%) gives 574p. A 0.5pp change in each input swings the value by ~100p or ~15%. This is HIGH sensitivity -- the model is fragile.

---

## VALIDATION CHECKS

### 1. Implied Multiple Validation

At my adversarial FV of 615p:
- Implied P/FFO (FY2025): 615/48 = 12.8x -- reasonable for current environment
- Implied P/FFO (FY2026 trough): 615/43 = 14.3x -- slightly generous for trough
- Implied dividend yield: 37.3/615 = 6.1% -- reasonable for income REIT
- Implied P/NAV: 615/986 = 0.62x (38% discount) -- high but within sector range

At thesis FV of 745p:
- Implied P/FFO (FY2025): 745/48 = 15.5x -- generous in current environment
- Implied P/FFO (FY2026 trough): 745/43 = 17.3x -- VERY generous for declining earnings
- Implied dividend yield: 37.3/745 = 5.0% -- low for an income REIT
- Implied P/NAV: 745/986 = 0.76x (24% discount) -- implies significant NAV discount compression

**Verdict:** The thesis FV of 745p implies the market will pay 17x trough FFO -- this seems aggressive given occupancy is declining and rates are high. My 615p is more reasonable at 14.3x trough FFO.

### 2. Stifel Cross-Check

Stifel's target of 600p (at 6.5% dividend yield) is close to my adversarial EV of 615p. This confirms that independent analysis arrives at similar conclusions.

### 3. VNA.DE Lesson

We sold VNA.DE (Vonovia) at a -25% adversarial FV revision. The key lesson: large NAV discounts in REITs can persist for YEARS. VNA.DE traded at 40-55% discount to NAV for 2+ years. UTG's 41% discount could be similarly persistent.

---

## STANDING ORDER EVALUATION

**Current standing order:** 540 GBp

At 540p:
- MoS vs adversarial EV (615p): 12.2% -- INSUFFICIENT for Tier C (precedent: 30%+ required)
- MoS vs adversarial Bear (450p): -20% OVERVALUED
- MoS vs adversarial Base (610p): 11.5% -- INSUFFICIENT

**Recommendation:** The 540p trigger provides only 12% MoS against my adversarial EV of 615p. For a Tier C REIT with declining occupancy, rising costs, and significant immigration policy risk, this is insufficient margin of safety.

**Revised trigger level:**
- To achieve 25% MoS vs adversarial EV: 615 * 0.75 = 461p
- To achieve 20% MoS vs adversarial EV: 615 * 0.80 = 492p
- Compromise (15% MoS given structural tailwinds): 615 * 0.85 = 523p

**I recommend:** LOWER the trigger to 480-500p, OR CANCEL the standing order entirely.

The only scenario where 540p is justified is if you believe:
1. Gilt yields will fall significantly (to 3.5-4.0%)
2. Occupancy will recover to 97%+
3. The thesis DDM growth rate of 2.5% is achievable
4. The market will re-rate UK REITs

All four would need to materialize simultaneously, which is the BULL case (25% probability).

---

## SUMMARY

```
VALUATION: UTG.L (Unite Group PLC)

Type of enterprise: Asset-Heavy REIT (UK PBSA), Tier C
Methods selected: NAV + DDM + FFO Multiple + EV/EBITDA cross-check

Reconciliation:
| Method         | FV    | Weight | Weighted |
|----------------|-------|--------|----------|
| NAV-Based      | 700p  | 25%    | 175p     |
| DDM            | 574p  | 35%    | 201p     |
| FFO Multiple   | 580p  | 30%    | 174p     |
| EV/EBITDA      | 580p  | 10%    | 58p      |
| **Avg**        |       | 100%   | **608p** |

Escenarios:
| Escenario   | Fair Value | Prob |
|-------------|-----------|------|
| Bear        | 450p      | 25%  |
| Base        | 610p      | 50%  |
| Bull        | 790p      | 25%  |
| **Expected**| **615p**  | 100% |

Precio actual: 580 GBp
MoS vs Expected: 5.7%
MoS vs Bear: -28.9% (OVERVALUED)

Thesis FV: 745p
Adversarial FV: 615p
Delta: -17.4%
```

---

## META-REFLECTION

### Dudas/Incertidumbres

1. **Beta selection is the most impactful uncertainty.** At beta 0.65 (thesis), DDM gives 679p. At beta 0.85 (my choice), it gives 574p. At beta 1.24 (market), it would give even less. There is no "right" beta for a REIT -- it depends on whether you view rate sensitivity as systematic risk (it is) or temporary volatility (it will pass).

2. **NAV reliability is genuinely uncertain.** The EPRA NTA of 986p was independently valued, but the 11.2% PBSA vacancy rate is alarming. If this spreads from regional cities to Russell Group locations, NAV could decline more than my haircuts assume.

3. **Timing of recovery.** I assume FY2027 is the trough for occupancy, but the Cushman & Wakefield data suggests structural issues (affordability, visa changes) that could prolong weakness beyond FY2027.

4. **The 64% reservation rate for 2026/27 (vs 67% prior year)** is MILDLY concerning but not catastrophic. Unite reports prelim results Feb 24 with UCAS data -- this will be the key catalyst.

### Sensibilidad Preocupante

- **DDM is highly sensitive to inputs:** Changing Ke by 0.5pp and g by 0.5pp simultaneously moves FV by ~100p (17%). This means any DDM-based FV should be treated with a wide confidence interval.
- **NAV is sensitive to cap rates:** 25bps cap rate expansion = ~5% NAV decline. If cap rates expand 100bps over 2 years (possible in current environment), NAV drops 17%.

### Discrepancias con Thesis

The thesis FV of 745p is 17% above my adversarial assessment of 615p. The key drivers:
1. Thesis uses stale gilt yield (4.0% vs 4.55% actual) -- this alone accounts for ~50p
2. Thesis NAV haircut is too shallow (only 10%, no market discount applied)
3. Thesis DDM growth rate (2.5%) is optimistic given near-term headwinds
4. Thesis FFO multiple (14-16x) is too high for current rate environment

The thesis was written on 2026-02-03 and the gilt/rate environment has not changed materially since then, so the stale gilt assumption reflects an error in the original analysis, not subsequent market moves.

### Sugerencias para el Sistema

1. **Create a REIT-specific valuation template** that handles NAV discounts, cap rate sensitivity, and FFO-based valuation as first-class methods. The current valuation skill is equity-focused.
2. **The quality_scorer.py needs a REIT mode** that adjusts for FCF distortion and leverage norms. A raw QS of 27 (Tier D) for a BBB+ REIT with 6.9x interest coverage is misleading.
3. **Standing orders need periodic re-evaluation.** The UTG standing order at 540p was set when the thesis was created at 745p FV. If the adversarial FV is 615p, the trigger should be recalculated.

### Preguntas para Orchestrator

1. Given the adversarial FV of 615p vs current price of 580p (only 5.7% MoS), should the standing order be cancelled entirely, or lowered to 480-500p?
2. The Feb 24 prelim results with UCAS data will be critical. Should we wait for this before making any decision on the standing order?
3. Given our VNA.DE experience (sold at adversarial FV -25%), and UTG shows similar REIT NAV discount dynamics, should we apply the same lesson and deprioritize UTG?
4. Is UTG the best use of capital for a UK REIT position, or should we look at other UK REITs with better income characteristics?

---

## Sources

- [Unite Group H1 2025 Interim Results](https://www.unitegroup.com/wp-content/uploads/2025/07/Unite-Group-2025-Interims-statement-vF-1.pdf)
- [Unite Group Q4 Fund Valuations & Trading Update (Jan 2026)](https://www.investegate.co.uk/announcement/rns/unite-group--utg/trading-update-and-q4-fund-valuations/9342855)
- [Unite Group GBP 100M Buyback Announcement (QuotedData)](https://quoteddata.com/2026/01/unite-announces-100m-buyback-reflecting-revised-capital-allocation-strategy/)
- [Stifel Downgrade to Hold (Investing.com)](https://www.investing.com/news/stock-market-news/unite-group-stock-rating-cut-to-hold-by-stifel-on-occupancy-concerns-93CH-4476197)
- [Cushman & Wakefield UK Student Accommodation Report](https://www.cushmanwakefield.com/en/united-kingdom/insights/uk-student-accommodation-report)
- [UK PBSA Vacancy Rates Rising (Property Investor Today)](https://www.propertyinvestortoday.co.uk/breaking-news/2025/10/purpose-built-student-accommodation-his-trouble-as-vacancy-rates-rise/)
- [UK PBSA Market Trends (Charles Russell Speechlys)](https://www.charlesrussellspeechlys.com/en/insights/expert-insights/real-estate/2025/what-are-the-trends-in-the-purpose-built-student-accommodation-market-in-the-uk-over-the-last-12-months-and-how-will-they-change-in-the-next-12-months/)
- [UK REITs NAV Discount Analysis (Gravis Capital)](https://www.graviscapital.com/news/uk-reits-does-the-resurgence-still-have-legs)
- [UK 10Y Gilt Yield (TradingEconomics)](https://tradingeconomics.com/united-kingdom/government-bond-yield)
- [GuruFocus UTG WACC](https://www.gurufocus.com/term/wacc/LSE:UTG)
- [Knight Frank UK PBSA Q1 2025 Report](https://content.knightfrank.com/research/169/documents/en/uk-student-housing-q1-2025-12116.pdf)
- [Unite Group Analyst Forecast (MarketBeat)](https://www.marketbeat.com/stocks/LON/UTG/forecast/)
