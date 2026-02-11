# BME.L - INDEPENDENT VALUATION REPORT

**Date:** 2026-02-08
**Analyst:** Valuation Specialist (Independent)
**Type of Company:** Cyclical Retailer in Earnings Trough
**Methods Selected:** EV/EBIT Mid-Cycle (Primary) + DCF with Scenarios (Secondary)

---

## STEP 0: CHALLENGING THE THESIS ASSUMPTIONS

The existing thesis (v2.0, dated 2026-02-03) calculates:
- EV/EBIT Mid-Cycle FV: 342p (EBIT 535M, 8x multiple)
- Conservative FV: 321p
- DCF Bear/Base/Bull: 217p / 424p / 736p

**Issues identified for adversarial review:**

1. **Normalized EBIT excludes FY25 (481M EBIT) without justification** -- FY25 actual EBIT was 591M per the company's results, not 481M. The thesis seems to confuse FY25 and FY26.
2. **FY26 is the trough year, not FY25** -- FY25 was still decent (EBITDA 620M, EBIT 591M). FY26E is the problem year (EBITDA 440-475M guided).
3. **DCF tool uses IFRS16-inflated net debt (GBP 2.31B)** -- should use pre-IFRS16 net debt (~GBP 860M). This is a data quality issue.
4. **8x EV/EBIT for a leveraged turnaround needs justification** vs peers.
5. **France (~15% revenue) likely low/negative margin at group level** -- needs separate treatment.
6. **Heron Foods underperformance** is structural, not cyclical -- needs haircut.
7. **12/13 adversarial reviews found ~15% FV inflation** -- maintain skepticism.

---

## METHOD 1: EV/EBIT MID-CYCLE (PRIMARY, 60% WEIGHT)

### Step 1: Derive Normalized EBIT

**Historical EBIT data (adjusted, pre-IFRS16):**

| Year | EBIT (GBP M) | Context |
|------|-------------|---------|
| FY21 | 611 | COVID boost (exceptional) |
| FY22 | 535 | Post-COVID normalization |
| FY23 | 614 | Strong year, pre-cost inflation |
| FY24 | 571 | Cost inflation starts |
| FY25 | 591 | Still decent, NI impact beginning |
| FY26E | ~410 | Trough (guided EBITDA 440-475M, less ~50M D&A) |

**Thesis used:** 535M (FY21-24 avg excluding FY25), then said "normalized 520-550M"
**Thesis then calculated with:** 535M

**My approach -- INCLUDE FY25, INCLUDE FY26E, EXCLUDE FY21 (COVID distortion):**

Using FY22-FY26E (full cycle including trough):
- FY22: 535
- FY23: 614
- FY24: 571
- FY25: 591
- FY26E: 410 (midpoint of guided EBITDA 457M less ~47M D&A)

**5-year average EBIT = (535 + 614 + 571 + 591 + 410) / 5 = 544M**

**However, this needs further adjustment:**

1. **Structural cost increase:** UK National Insurance adds ~GBP 30-40M permanently post-FY25. This is NOT cyclical. It must reduce the normalized figure.
2. **Heron Foods structural deterioration:** Clearance stocklot model breaking down. Heron contributes ~10% of revenue but margin is collapsing. Haircut ~GBP 15-20M from normalized.
3. **France at low margin:** France revenue ~GBP 560M/yr growing, but H1 FY26 EBITDA only 18M (vs 17M prior year). That implies ~6.5% EBITDA margin for France, so EBIT perhaps ~5% margin = ~28M. Not a drag, but not a driver either.

**Adjusted Normalized EBIT:**
- Raw 5-year average: 544M
- NI structural cost (-35M): 509M
- Heron margin deterioration (-15M): 494M
- **My Normalized EBIT: GBP 490-500M**

This compares to thesis's 535M -- a **7-9% reduction**.

### Step 2: Determine Appropriate Multiple

**Peer comparables (EV/EBIT):**

| Peer | EV/EBIT | Context |
|------|---------|---------|
| Dollar General (US) | 22.5x | Distressed, US premium |
| Dollar Tree (US) | ~18x | US premium, larger scale |
| Action (private) | ~15-16x (implied from 18.5x EBITDA) | Premium growth story |
| Target (US) | ~9x | Larger, lower growth |
| Consensus UK retail sector | 6-10x | |

**B&M specific factors:**

| Factor | Impact on Multiple | Reasoning |
|--------|-------------------|-----------|
| Sector median (UK retail) | 7-8x base | Starting point |
| (+) Superior ROIC (>30% historically) | +1x | Genuinely excellent returns on invested capital |
| (+) Market leader #1 position | +0.5x | Scale advantage in sourcing |
| (-) High leverage (net debt/EBITDA ~1.7x, rising) | -1x | Above management target, 8.125% bond is expensive |
| (-) Turnaround/execution risk | -0.5x | "Back to Basics" is unproven, CFO just resigned |
| (-) Heron structural issue | -0.5x | Not clear how to fix clearance stocklot model |
| (-) Action entering UK market | -0.5x | Long-term competitive threat from formidable operator |
| **Net adjustment** | **-1x** | |
| **Final multiple** | **7x** | Below sector mid-range, reflecting risks |

**Thesis used 8x.** I use 7x because:
1. The thesis underweights the cumulative negatives (leverage + CFO departure + Heron + Action)
2. B&M's margins are compressing (37.2% -> 36.5% -> 35% gross, 10.8% -> 7.7% EBITDA) -- this is NOT just cyclical
3. Adversarial pattern: 12/13 positions had inflated FV, often from generous multiples
4. A leveraged turnaround with an unproven strategy and no permanent CFO deserves a discount, not a market multiple

**Counter-argument for 8x:** If you believe the core business model is intact (ROIC >30% on new stores, <12 month payback), then the current problems are transitory and 8x is justified. But "transitory" has been said for 3 consecutive guidance cuts.

### Step 3: Calculate Fair Value

**Using 7x multiple:**
```
EV = Normalized EBIT x Multiple = 495M x 7x = GBP 3,465M
Less Net Debt (pre-IFRS16): GBP 860M
Equity Value: GBP 2,605M
Shares: 1.01B
Fair Value per Share: 258p
```

**Sensitivity to multiple:**

| Multiple | EV (GBP M) | Equity (GBP M) | FV/Share |
|----------|-----------|----------------|----------|
| 6x | 2,970 | 2,110 | 209p |
| 7x | 3,465 | 2,605 | 258p |
| 8x | 3,960 | 3,100 | 307p |
| 9x | 4,455 | 3,595 | 356p |

**Sensitivity to normalized EBIT:**

| Norm EBIT | @ 7x Multiple | FV/Share |
|-----------|---------------|----------|
| 450M (permanent impairment) | 3,150 - 860 = 2,290 | 227p |
| 495M (my estimate) | 3,465 - 860 = 2,605 | 258p |
| 535M (thesis estimate) | 3,745 - 860 = 2,885 | 286p |
| 575M (optimistic) | 4,025 - 860 = 3,165 | 313p |

**Method 1 Fair Value: 258p**

---

## METHOD 2: DCF WITH SCENARIOS (SECONDARY, 40% WEIGHT)

### WACC Derivation

```
Cost of Equity (Ke):
  Risk-Free Rate (UK 10Y Gilt): 4.50%
  Equity Risk Premium: 5.0%
  Beta: 0.46 (reported), adjusted to 0.80 for stress
  Rationale for 0.80: A stock that lost 50% in 12 months on 3 profit warnings
  is NOT a 0.46 beta business. The raw beta understates risk because
  the decline happened in a concentrated period. I use 0.80 which still
  reflects the defensive nature of discount retail but acknowledges
  the operational volatility demonstrated.
  Ke = 4.50% + (0.80 x 5.0%) = 8.50%

Cost of Debt (Kd):
  Blended rate: ~6.0% (mix of 3.5% 2028 and 8.125% 2030 bonds)
  Tax rate: 25%
  Kd after-tax = 6.0% x 0.75 = 4.5%

Capital Structure:
  Market Cap: GBP 1.75B
  Net Debt (exc leases): GBP 0.86B
  EV: GBP 2.61B
  E/V: 67%, D/V: 33%

WACC = (67% x 8.5%) + (33% x 4.5%) = 5.70% + 1.49% = 7.19%

Floor WACC: 9.0% (for leveraged turnaround with execution risk)
WACC Used: 9.0%
```

**Thesis used 8.0%.** I use 9.0% because:
- Three consecutive guidance cuts = demonstrated execution risk
- CFO resignation during turnaround = heightened uncertainty
- Leverage above target with 8.125% bond = financial risk
- Adversarial context demands conservatism

### FCF Projection

**Starting point:** FY26E EBITDA midpoint 457M, FCF conversion ~50% = FCF ~228M

| Year | Revenue | EBITDA Margin | EBITDA | FCF Conv | FCF |
|------|---------|---------------|--------|----------|-----|
| FY26E (Y0) | 5.78B | 7.9% | 457M | 50% | 228M |
| FY27E (Y1) | 5.96B | 8.3% | 495M | 52% | 257M |
| FY28E (Y2) | 6.14B | 8.6% | 528M | 53% | 280M |
| FY29E (Y3) | 6.33B | 8.8% | 557M | 54% | 301M |
| FY30E (Y4) | 6.52B | 9.0% | 587M | 55% | 323M |
| Terminal | 6.72B | 9.0% | 605M | 55% | 333M |

### Bear Case (30% probability -- HIGHER than thesis's 25%)

I assign higher bear probability because of 3 consecutive guidance cuts.

```
Assumptions:
  Revenue growth: 2%/year (consumer weakness persists)
  EBITDA margin: stays at 8.0% (no recovery, NI + wages permanent)
  FCF conversion: 48% (working capital drag from clearance)
  WACC: 10% (+1% for risk)
  Terminal growth: 1.5%

Year 0 FCF: 228M
Y1: 228 x 1.02 = 233M, PV = 212M
Y2: 237M, PV = 196M
Y3: 242M, PV = 182M
Y4: 247M, PV = 169M
Y5: 252M, PV = 157M
Sum PV of FCF Years 1-5: 916M

Terminal Value = 252M x 1.015 / (0.10 - 0.015) = 256M / 0.085 = 3,008M
PV of Terminal = 3,008M / (1.10)^5 = 1,867M

Enterprise Value: 916M + 1,867M = 2,783M
Less Net Debt: 860M
Equity Value: 1,923M
Per Share: 190p
```

### Base Case (45% probability)

```
Assumptions:
  Revenue growth: 3.5%/year
  EBITDA margin: recovers to 9.0% by FY30 (gradual)
  FCF conversion: 53% normalized
  WACC: 9%
  Terminal growth: 2.0%

Y1 FCF: 257M, PV = 236M
Y2 FCF: 280M, PV = 236M
Y3 FCF: 301M, PV = 232M
Y4 FCF: 323M, PV = 229M
Y5 FCF: 333M, PV = 216M
Sum PV of FCF Years 1-5: 1,149M

Terminal Value = 333M x 1.02 / (0.09 - 0.02) = 340M / 0.07 = 4,851M
PV of Terminal = 4,851M / (1.09)^5 = 3,153M

Enterprise Value: 1,149M + 3,153M = 4,302M
Less Net Debt: 860M
Equity Value: 3,442M
Per Share: 341p
```

### Bull Case (25% probability)

```
Assumptions:
  Revenue growth: 5%/year (store rollout + LFL recovery)
  EBITDA margin: recovers to 10.0% by FY29
  FCF conversion: 55%
  WACC: 8.5% (-0.5% for execution)
  Terminal growth: 2.5%

Y1 FCF: 280M, PV = 258M
Y2 FCF: 315M, PV = 268M
Y3 FCF: 350M, PV = 274M
Y4 FCF: 380M, PV = 275M
Y5 FCF: 400M, PV = 266M
Sum PV of FCF Years 1-5: 1,341M

Terminal Value = 400M x 1.025 / (0.085 - 0.025) = 410M / 0.06 = 6,833M
PV of Terminal = 6,833M / (1.085)^5 = 4,545M

Enterprise Value: 1,341M + 4,545M = 5,886M
Less Net Debt: 860M
Equity Value: 5,026M
Per Share: 498p
```

### DCF Expected Value

```
EV = (Bear x 30%) + (Base x 45%) + (Bull x 25%)
EV = (190 x 0.30) + (341 x 0.45) + (498 x 0.25)
EV = 57 + 153 + 125
EV = 335p
```

**Method 2 Fair Value (Expected): 335p**
**Method 2 Bear Case: 190p**

---

## STRESS TEST: MARGINS STAY AT 8% PERMANENTLY

This is the critical question. What if B&M's EBITDA margin never recovers above 8%?

```
Revenue FY28E at 3% growth: ~GBP 6.1B
EBITDA at 8% permanent margin: GBP 488M
EBIT at ~7% (after D&A): GBP 427M

At 7x EV/EBIT: EV = 2,989M
Less net debt: 860M
Equity: 2,129M
Per share: 211p

At 6x EV/EBIT: EV = 2,562M
Less net debt: 860M
Equity: 1,702M
Per share: 169p (near current standing order trigger)
```

**This is sobering.** At 6x with permanent 8% EBITDA margin, the stock is worth 169p -- essentially the current standing order trigger. The margin recovery assumption is doing most of the valuation work.

---

## FRANCE SEGMENT: SEPARATE VALUATION

France contributes ~15% of group revenue (~GBP 560M/yr H1 annualized).

- H1 FY26 France EBITDA: GBP 18M (annualized ~36M)
- France EBITDA margin: ~6.5%
- LFL growth: 5.2% (strong)

France is **early-stage** (~100 stores) with good growth but thin margins. At 7x EBITDA, France is worth ~GBP 252M of EV, or ~GBP 25p per share. This is included in the group-level valuation above but is worth noting: France contributes real value but is not a significant margin accretor yet.

The risk is that France margins may NOT improve (Babou brand legacy issues). In a bearish scenario for France:
- France EBITDA: 20M (margin compression)
- Value: ~140M EV = 14p/share

---

## RECONCILIATION AND DIVERGENCE

| Method | Fair Value | Weight | Weighted |
|--------|-----------|--------|----------|
| EV/EBIT Mid-Cycle (7x, EBIT 495M) | 258p | 60% | 155p |
| DCF Expected Value | 335p | 40% | 134p |
| **Weighted Average** | | 100% | **289p** |

**Divergence between methods:** (335 - 258) / 258 = 30%

This is at the 30% threshold. The divergence is explained by:
- DCF gives significant weight to terminal value (which embeds margin recovery assumption)
- EV/EBIT uses a more conservative "today" multiple that doesn't assume full recovery
- The DCF's bull case (498p) pulls the expected value up materially

**I give more weight to the EV/EBIT method because:**
1. For a cyclical retailer in turnaround, normalized earnings are more reliable than FCF projections
2. The DCF terminal value is very sensitive to margin recovery assumptions that are unproven
3. The adversarial context (12/13 positions had inflated FV) suggests trusting the lower number

---

## COMPARISON WITH THESIS

| Item | Thesis Value | My Value | Delta |
|------|------------|----------|-------|
| Normalized EBIT | 535M | 495M | -7.5% |
| EV/EBIT Multiple | 8x | 7x | -12.5% |
| EV/EBIT FV | 342p | 258p | **-24.6%** |
| WACC | 8.0% | 9.0% | +100bps |
| DCF Bear | 217p | 190p | -12.4% |
| DCF Base | 424p | 341p | -19.6% |
| DCF Bull | 736p | 498p | -32.3% |
| Conservative FV | 321p | 258p | **-19.6%** |
| Weighted FV | 396p | 289p | **-27.0%** |

**The thesis inflates FV by 27% versus my independent assessment.** This is consistent with the adversarial pattern of ~15% average inflation, but worse -- BME.L's thesis was particularly generous with the multiple.

---

## ANALYST CONSENSUS COMPARISON

- **17 analyst consensus target:** 212p (per MarketScreener)
- **Consensus mean rating:** Outperform
- **My weighted FV:** 289p
- **My EV/EBIT FV:** 258p

My EV/EBIT FV (258p) is 22% above analyst consensus (212p). Analysts may be using trough earnings rather than normalized. Or they may be right that margins don't recover. This gap warrants caution.

**Implied multiples at my FV of 258p:**
- Market cap at 258p: GBP 2.6B
- EV: GBP 3.46B
- EV/EBITDA on FY26E (457M): 7.6x -- reasonable for a turnaround
- P/E on FY26E net income (194M per consensus): 13.4x -- somewhat elevated for a turnaround
- P/E on normalized earnings (~240M): 10.8x -- reasonable

**Implied multiples at current 174p:**
- Market cap: GBP 1.76B
- EV: GBP 2.62B
- EV/EBITDA on FY26E (457M): 5.7x -- optically cheap
- EV/EBITDA on normalized (550M): 4.8x -- very cheap IF margins recover

---

## SCENARIOS SUMMARY

| Scenario | Fair Value | Probability | Weighted |
|----------|-----------|-------------|----------|
| Bear (permanent margin impairment) | 190p | 30% | 57p |
| Base (gradual recovery to 9%) | 258p | 45% | 116p |
| Bull (strong recovery to 10%+) | 380p | 25% | 95p |
| **Expected Value** | | 100% | **268p** |

**Note:** I use the EV/EBIT method for Base (258p) rather than DCF (341p) as my base anchor, given it is more appropriate for a cyclical retailer. The bull case uses a blended 380p (midway between 8x EV/EBIT = 307p and DCF bull discounted = 498p, weighted toward EV/EBIT).

### Final Point Estimate

```
SINGLE POINT ESTIMATE: 258p

This is my base case EV/EBIT mid-cycle value, which I consider
the most reliable method for this type of company. The expected
value of 268p confirms this is reasonable (within 4%).

Current Price: 174p
MoS vs Point Estimate (258p): 32.6%
MoS vs Expected Value (268p): 35.1%
MoS vs Bear Case (190p): 8.4%
```

---

## SENSITIVITY TABLE

### DCF Sensitivity (Base Case)

| | WACC 8% | WACC 9% | WACC 10% | WACC 11% |
|--------|---------|---------|----------|----------|
| **Growth 2%** | 304p | 260p | 225p | 198p |
| **Growth 3.5%** | 383p | 341p | 290p | 255p |
| **Growth 5%** | 470p | 400p | 348p | 310p |

### EV/EBIT Sensitivity

| | 6x | 7x | 8x | 9x |
|----------|------|------|------|------|
| **EBIT 450M** | 177p | 227p | 276p | 326p |
| **EBIT 495M** | 209p | 258p | 307p | 356p |
| **EBIT 535M** | 233p | 286p | 342p | 395p |

**Key observation:** At 6x EV/EBIT with permanent 8% margins (EBIT ~450M), fair value is 177p -- barely above current price. This is the downside scenario the bears are pricing in.

---

## VALIDATION

### vs Peers

| Metric | BME.L (at 174p) | Dollar General | Action |
|--------|-----------------|----------------|--------|
| EV/EBITDA (LTM) | 4.2x | 12.4x | 18.5x |
| EV/EBITDA (normalized) | ~4.8x | ~10x | ~15x |
| P/E | 7.0x | 25.3x | N/A |
| Growth (store count) | 5-6%/yr | 3%/yr | 13%/yr |
| ROIC | >30% | ~15% | ~25-30% |

B&M trades at a massive discount to all peers. Some discount is justified (UK focus, leverage, turnaround risk), but 4-5x EBITDA vs 12-18x for peers suggests the market is pricing in significant permanent impairment. If B&M's margins recover even partially, there is substantial upside.

### vs Precedents (decisions_log.yaml)

This would be a Tier C position (QS likely 40-50 range). Precedents:
- Tier C positions typically got 3-4% sizing max
- All Tier C positions in the adversarial review had inflated FV (avg -15%)
- Pattern: every thesis overrated QS by 1-2 tiers

### Implied P/E at my FV

At 258p with normalized net income ~240M:
- P/E = (258p x 1.01B) / 240M = 10.8x
- This is reasonable for a UK retailer with these characteristics
- Not screaming value, but not egregious

---

## STANDING ORDER ASSESSMENT

**Current standing order:** 169 GBp

At 169p:
- MoS vs my point estimate (258p): 34.5%
- MoS vs expected value (268p): 36.9%
- MoS vs bear case (190p): 11.1%

**Assessment:** The 169p trigger provides marginally better entry but the MoS vs bear case is thin (11%). Given 3 consecutive guidance cuts, the bear case (margins don't recover) is realistic at 30% probability.

**My recommendation:** If entering, a trigger of 155-160p would provide better bear case protection:
- At 155p: MoS vs bear = 18.4%, MoS vs base = 39.9%
- At 160p: MoS vs bear = 15.8%, MoS vs base = 38.0%

---

## 🔄 META-REFLECTION

### Dudas/Incertidumbres
1. **Normalized EBIT is the swing variable.** My 495M vs thesis's 535M -- a 40M difference -- creates an 8% gap in FV. The "correct" number depends entirely on whether NI cost inflation and Heron margin erosion are permanent (they likely are) or temporary.
2. **The 7x vs 8x multiple debate.** This single turn of multiple difference changes FV by ~50p (20%). I use 7x because of accumulating negatives (leverage, CFO departure, Heron, Action), but 8x would be defensible if the "Back to Basics" strategy works.
3. **DCF tool unreliable for this company.** The dcf_calculator.py output (717p base case) is wildly wrong because it uses IFRS16 net debt (2.31B) and apparently inflated FCF figures. I had to do DCF manually, which introduces calculation risk.
4. **France is a wild card.** If France margins expand meaningfully (from 6.5% to 9%+ EBITDA), that could add 20-30p of value. But the Babou legacy suggests this may take years.
5. **Analyst consensus at 212p is sobering.** 17 analysts covering this stock with more information than I have target only 212p. My 258p is 22% above consensus. Either I'm more right than 17 analysts (unlikely), or I'm still too optimistic.

### Sensibilidad Preocupante
- FV changes >20% with a 1-turn change in EV/EBIT multiple (7x vs 8x)
- FV changes ~15% depending on whether normalized EBIT is 450M or 535M
- The bear case (190p) is only 9% above current price -- very thin cushion
- Terminal value accounts for ~70% of DCF value -- excessive reliance on long-term recovery

### Discrepancias con Thesis
- Thesis FV 321p vs my 258p = **-19.6% lower** (within adversarial pattern of ~15%)
- Thesis uses 8x multiple; I use 7x (key driver of difference)
- Thesis uses 535M EBIT; I use 495M (secondary driver)
- Thesis's DCF bull case (736p) appears extremely optimistic (7% WACC for a leveraged retailer)
- Thesis assigns 25% bear probability; I assign 30% given 3 consecutive guidance cuts

### Sugerencias para el Sistema
1. **dcf_calculator.py needs manual override for net debt.** The tool picked up IFRS16 lease liabilities as net debt (GBP 2.31B vs actual GBP 860M pre-IFRS16). For retailers with large lease books, this makes the DCF output useless.
2. **Need a standardized "peer multiple" database** rather than ad-hoc WebSearch each time.
3. **Standing order triggers should be stress-tested against bear case** -- a trigger that offers <15% MoS vs bear is too risky for Tier C.

### Preguntas para Orchestrator
1. **Should the standing order be revised?** My analysis suggests 169p offers thin bear case protection (11% MoS vs bear). Consider lowering to 155p.
2. **Is 30% bear probability sufficient?** Three consecutive guidance cuts is an unusual pattern. Should we increase bear weight to 35-40%?
3. **How to handle the DCF tool's IFRS16 net debt issue?** This affects all retailers and REITs. Should we flag for quant-tools-dev to add a `--net-debt-override` parameter?

---

*Valuation report written independently by valuation-specialist.*
*Date: 2026-02-08*

**Sources:**
- [MarketScreener BME.L](https://www.marketscreener.com/quote/stock/B-M-EUROPEAN-VALUE-RETAIL-16686539/) - Analyst consensus, forward estimates
- [MoatMind B&M Analysis](https://www.moatmind.com/p/b-and-m-value-retail-stock-analysis-march-2025-growth-moat-valuation) - Historical financials, peer context
- [StockAnalysis BME.L](https://stockanalysis.com/quote/lon/BME/) - Current metrics
- [3i Group Action Portfolio](https://www.3i.com/private-equity/our-portfolio/action/) - Action valuation at 18.5x EBITDA
- [Alpha Spread DG Valuation](https://www.alphaspread.com/security/nyse/dg/relative-valuation/ratio/enterprise-value-to-ebitda) - Dollar General peer comps
- [DirectorsTalk FY25 Results](https://www.directorstalkinterviews.com/bm-european-value-retail-fy25-revenue-hits-5-6bn/4121200218) - FY25 actual results
- [DirectorsTalk FY26 Guidance](https://www.directorstalkinterviews.com/bm-lowers-fy26-outlook-following-7m-freight-cost-adjustment-and-cfo-resignation/4121221675) - FY26 guidance revision
