# VICI Properties (VICI) - Independent Adversarial Valuation Report

**Date:** 2026-02-08
**Valuation Agent:** valuation-specialist (adversarial review)
**Framework:** v4.0 Principles-Based
**Thesis FV (anchor to challenge):** $33.75 (EV weighted from DDM + NAV + P/AFFO)

---

## Market Data (as of 2026-02-08)

| Metric | Value |
|--------|-------|
| Current Price | $28.76 |
| 52-Week High | $34.03 |
| 52-Week Low | $27.48 |
| P/E (trailing) | 10.9x |
| Dividend Yield | 6.1% |
| Market Cap | $30.7B |
| Shares Outstanding (diluted) | ~1,067M |
| 10-Year Treasury | 4.22% |
| Net Debt | ~$17.2B |

---

## Quality Score Assessment

**Tool output: QS = 54/100 (Tier C)**

| Component | Score | Key Driver |
|-----------|-------|------------|
| Financial Quality | 14/40 | ROIC spread -1.5pp (below WACC per tool), leverage 4.7x |
| Growth Quality | 18/25 | Revenue CAGR 26.4% (M&A-driven, not organic), EPS CAGR 9.2% |
| Moat Evidence | 17/25 | GM premium +39pp, strong market position |
| Capital Allocation | 5/10 | Low insider ownership (0.3%) |

**CRITICAL NOTE:** The thesis claims QS = 8/10 "Tier A" using a manual scoring rubric. The automated quality_scorer.py gives QS = 54 (Tier C). The divergence is significant and must be addressed:

- **ROIC spread is negative** per the tool. For REITs, this metric is distorted because high leverage is structural (not a weakness). However, even acknowledging this, the tool's negative ROIC spread flags that VICI's return on invested capital barely covers its cost of capital.
- **Leverage 4.7x** penalizes heavily in the tool. For REITs, 5.0-5.5x is industry standard for investment-grade net-lease REITs. This is a legitimate structural factor, not a weakness.
- **Insider ownership 0.3%** is genuinely low and a valid concern for alignment.
- **Revenue CAGR 26.4%** is inflated by the 2022 MGP merger. Organic growth is closer to 4-5%.

**My assessment:** The tool miscalibrates for REITs on leverage and ROIC. A REIT-adjusted QS would be approximately 60-65 (Tier B), NOT Tier A. The thesis claim of "Tier A" is overstated. VICI is a solid Tier B REIT with good but not exceptional quality characteristics.

---

## Company Type Classification

| Factor | Assessment |
|--------|------------|
| Type | Asset-heavy REIT (Gaming/Triple-Net) |
| Cash Flow | AFFO-based (not FCF) |
| Dividend | Central to value proposition |
| Methods Required | P/AFFO (primary) + NAV + DDM (minimum 3 for REITs) |

---

## KEY RISK: Caesars Regional Casino Lease (NOT IN ORIGINAL THESIS)

**This is the single most important finding of this adversarial review.**

The thesis does not adequately address the Caesars regional casino lease issue:

1. **Caesars pays ~$730M/year in rent** on regional casino assets
2. **Regional casino cash flow: ~$750M/year**
3. **Rent coverage ratio: ~1.03x** -- essentially breakeven
4. **Analysts project rent concession or restructuring is likely**

Potential resolution structures being discussed:
- Rent reduction on regional assets
- Caesars transferring a physical casino or land to VICI
- Extension of lease by 10+ years to mid-2040s
- Some combination of the above

**Impact on VICI:**
- Caesars represents **36-39% of total rent**
- If regional rent is reduced by 10-15%, that represents $73-110M annual rent reduction
- On total rent of $3.15B, this is a 2.3-3.5% hit to revenue
- On AFFO of ~$2.37/share, this is roughly $0.07-$0.10/share reduction

**Recent analyst actions driven by this concern:**
- Evercore ISI: Downgrade to In-Line, PT $36 to $32
- Wells Fargo: Downgrade to Equal-Weight, PT $36 to $32
- Scotiabank: Downgrade to Sector Perform, PT $36 to $30

---

## METHOD 1: P/AFFO Multiple (Primary, Weight 40%)

### AFFO Estimates

| Year | AFFO/Share | Source |
|------|-----------|--------|
| 2025E (guided) | $2.36-$2.37 | Company guidance (Q3 update) |
| 2026E (Evercore implied) | ~$2.40 | Derived from "trading at 12x 2026 AFFO" at ~$28.76 |
| 2026E (my estimate, pre-rent-reset) | $2.47 | 2025 AFFO $2.37 + 4.2% organic growth |
| 2026E (my estimate, post-rent-reset) | $2.40 | Assuming ~$0.07/share rent concession |

**I use the post-rent-reset estimate of $2.40/share for conservatism.** The Caesars regional rent issue is not a hypothetical -- it is actively being discussed and analyst downgrades cite it specifically.

### Multiple Selection

| REIT | Current Price | AFFO/Share (2025E) | P/AFFO | Notes |
|------|--------------|-------------------|--------|-------|
| VICI | $28.76 | $2.37 | 12.1x | Gaming REIT, tenant concentration |
| GLPI | $45.32 | $3.87 | 11.7x | Gaming peer, more diversified tenants |
| Realty Income (O) | $63.23 | ~$4.25 | 14.9x | Premium triple-net, 15,400+ properties |
| NNN REIT | ~$46 | ~$3.45 | 13.3x | Diversified triple-net retail |

**Observations:**
- VICI trades at 12.1x vs GLPI at 11.7x -- essentially in line with its closest peer
- The net-lease sector average is 13-15x
- VICI deserves a discount to the broader net-lease average because of:
  - Extreme tenant concentration (74% two tenants)
  - Caesars regional rent coverage issue
  - Less diversified asset base vs O or NNN
- VICI deserves a slight premium to GLPI because of:
  - Higher quality assets (Caesars Palace, MGM Grand, Venetian vs regional casinos)
  - Larger scale
  - Better growth pipeline (Golden Entertainment deal)

**My multiple: 12.0-13.0x (base 12.5x)**

This is BELOW the thesis assumption of 14x. The thesis anchors to "net-lease REIT sector average" but ignores that VICI's tenant concentration and the Caesars regional lease issue warrant a discount.

### P/AFFO Fair Value Calculation

| Scenario | AFFO/Share | Multiple | Fair Value |
|----------|-----------|----------|------------|
| Bear | $2.33 (rent cut + slow growth) | 11.0x | $25.63 |
| Base | $2.40 (post-rent-reset) | 12.5x | $30.00 |
| Bull | $2.50 (no rent cut, accretive deals) | 14.0x | $35.00 |

**P/AFFO Base Fair Value: $30.00**

---

## METHOD 2: NAV (Net Asset Value) (Weight 35%)

### Asset Valuation by Cap Rate

| Input | Value | Source |
|-------|-------|--------|
| Annualized Contractual Rent | $3.15B | Q3 2025 data |
| Potential Caesars rent adjustment | -$80M (midpoint estimate) | Analyst projections |
| Adjusted Annualized Rent | $3.07B | |

**Cap Rate Selection:**

The thesis uses 6.5% for "Class A gaming assets" and 7.0% for conservative. Let me verify:

- Recent VICI acquisition (Golden Entertainment): **7.5% cap rate** on $1.16B deal
- Net-lease average cap rates (Q4 2025): 5.5-7.0%
- Gaming-specific NNN cap rates: 6.5-8.0%
- 10-Year Treasury: 4.22%, meaning cap rate spread vs risk-free is only ~250-350 bps

The thesis's use of 6.5% for ALL assets is generous. VICI's portfolio is a mix of:
- **Las Vegas Strip assets** (Caesars Palace, MGM Grand, Venetian): Lower cap rate, 5.5-6.5%
- **Regional casino assets**: Higher cap rate, 7.0-8.5% (especially with thin rent coverage)
- **Non-gaming experiential**: 7.0-8.0%

**Blended Cap Rate:**
- Las Vegas Strip (~50% of rent): 6.0% average
- Regional casinos (~35% of rent): 7.5% average
- Non-gaming + other (~15% of rent): 7.5% average
- **Weighted average: 6.8%**

### NAV Calculation

| Component | Calculation | Value |
|-----------|------------|-------|
| Adjusted Rent | | $3.07B |
| Blended Cap Rate | | 6.8% |
| Implied Gross Asset Value | $3.07B / 6.8% | $45.15B |
| Less: Net Debt | | ($17.2B) |
| Equity Value | | $27.95B |
| Shares Outstanding | | 1,067M |
| **NAV/Share** | | **$26.19** |

### NAV Sensitivity

| Cap Rate | Asset Value | NAV/Share |
|----------|-------------|-----------|
| 6.0% | $51.17B | $31.82 |
| 6.5% | $47.23B | $28.13 |
| 6.8% (base) | $45.15B | $26.19 |
| 7.0% | $43.86B | $24.97 |
| 7.5% | $40.93B | $22.23 |

**NAV scenarios:**

| Scenario | Cap Rate | Rent | NAV/Share |
|----------|----------|------|-----------|
| Bear | 7.5% | $3.00B (rent cuts) | $20.90 |
| Base | 6.8% | $3.07B (partial reset) | $26.19 |
| Bull | 6.0% | $3.15B (no cuts, compression) | $31.82 |

**NAV Base Fair Value: $26.19**

**Thesis comparison:** The thesis gets NAV midpoint of $28.15 using a 6.75% blended cap rate and no rent adjustment. My $26.19 is 7% lower primarily because:
1. I adjust rent downward for probable Caesars regional concession (-$80M)
2. I use a slightly higher blended cap rate (6.8% vs implied 6.75%)

---

## METHOD 3: Dividend Discount Model (DDM) (Weight 25%)

### Input Derivation

| Parameter | Thesis Value | My Value | Rationale |
|-----------|-------------|----------|-----------|
| Current Dividend (D0) | $1.80 | $1.80 | Confirmed |
| Dividend Growth (g) | 4.5% | 3.5% | See below |
| Required Return (Ke) | 10% (conservative) | 8.7% | See below |

**Dividend Growth Rate (g):**

The thesis uses 4.5%. Let me derive independently:
- AFFO growth: 4-5% organically (post rent-reset, closer to 3-4%)
- Payout ratio: ~76% of AFFO
- Sustainable dividend growth = AFFO growth rate (since payout is stable)
- Historical dividend growth: 2020-2025 CAGR of ~6% (but inflated by MGP merger year)
- Post-merger normalized: ~4% growth
- Adjusting for Caesars rent risk: **3.5%** is my base case

**Required Return (Ke):**

The thesis calculates Ke = 7.82% then arbitrarily uses 10% "for conservatism." This is inconsistent methodology. Either derive Ke properly or explain why you use 10%.

My Ke derivation:
- Risk-Free Rate: 4.22% (10Y Treasury, current)
- Beta: 0.72 (Yahoo Finance)
- Equity Risk Premium: 5.0%
- Ke = 4.22% + (0.72 x 5.0%) = **7.82%**

I add a 0.9% premium for tenant concentration risk, giving:
- **Ke = 8.7%**

### DDM Calculation

```
D1 = $1.80 x (1 + 0.035) = $1.863

Fair Value = D1 / (Ke - g)
Fair Value = $1.863 / (0.087 - 0.035)
Fair Value = $1.863 / 0.052
Fair Value = $35.83
```

### DDM Sensitivity

| Ke \ g | 2.5% | 3.0% | 3.5% | 4.0% | 4.5% |
|--------|------|------|------|------|------|
| 7.5% | $36.90 | $41.18 | $46.58 | $53.49 | $62.70 |
| 8.0% | $33.55 | $36.90 | $41.18 | $46.58 | $53.49 |
| 8.7% | $29.77 | $32.49 | $35.83 | $40.00 | $45.38 |
| 9.0% | $28.38 | $30.83 | $33.84 | $37.60 | $42.40 |
| 10.0% | $24.60 | $26.51 | $28.82 | $31.68 | $35.14 |

**DDM is extremely sensitive to inputs.** A spread (Ke-g) of 4.5% gives $41, while 6.5% gives $29. This is why DDM should not be the primary method.

### DDM Scenarios

| Scenario | g | Ke | Fair Value |
|----------|---|-----|------------|
| Bear | 2.5% | 9.5% | $26.36 |
| Base | 3.5% | 8.7% | $35.83 |
| Bull | 4.5% | 8.0% | $53.49 |

**DDM Base Fair Value: $35.83**

**Thesis comparison:** The thesis uses Ke=10% and g=4.5% to get $34.18. My base case of $35.83 is similar but derived differently -- lower Ke (8.7% vs 10%) but also lower g (3.5% vs 4.5%). The thesis's approach of using 10% Ke is overly conservative on the discount rate but then offsets with aggressive growth. My approach is more balanced.

---

## RECONCILIATION

| Method | Fair Value | Weight | Weighted |
|--------|-----------|--------|----------|
| P/AFFO (12.5x, $2.40) | $30.00 | 40% | $12.00 |
| NAV (6.8% cap rate) | $26.19 | 35% | $9.17 |
| DDM (Ke=8.7%, g=3.5%) | $35.83 | 25% | $8.96 |
| **Weighted Average** | | **100%** | **$30.13** |

### Weight Justification

- **P/AFFO at 40%:** Most reliable for a gaming REIT -- directly comparable to peers and based on observable market multiples. I weight it highest.
- **NAV at 35%:** Essential for REITs as it values the underlying real estate. However, cap rates are subjective and sensitive. High weight but not dominant.
- **DDM at 25%:** Appropriate for income-oriented REITs but extremely sensitive to small changes in Ke-g spread. Lower weight because of this fragility.

### Method Divergence

| Method Pair | Divergence |
|-------------|------------|
| P/AFFO vs NAV | 14.5% ($30.00 vs $26.19) |
| P/AFFO vs DDM | 19.4% ($30.00 vs $35.83) |
| NAV vs DDM | 36.7% ($26.19 vs $35.83) |

**NAV vs DDM diverges >30%.** Explanation:
- NAV is a snapshot of current asset value at current cap rates. With 10Y at 4.22%, cap rates are relatively high, compressing NAV.
- DDM captures the GROWTH value of future dividends. VICI's 30-year leases with CPI escalators have significant future value that NAV does not capture.
- This divergence is expected and common for growing REITs. The P/AFFO method sits between them, which is why it gets the highest weight.

---

## SCENARIO ANALYSIS

### Bear Case (25% probability)

**Assumptions:**
- Caesars regional rent reduced 12-15% ($87-110M/year)
- No cap rate compression (rates remain elevated)
- AFFO growth slows to 2% (rent concessions offset organic growth)
- Market assigns 11x P/AFFO (tenant risk premium persists)

| Method | Bear FV |
|--------|---------|
| P/AFFO | $25.63 |
| NAV | $20.90 |
| DDM | $26.36 |
| **Weighted** | **$24.12** |

### Base Case (50% probability)

**Assumptions:**
- Caesars rent reset resolved with win-win (modest rent cut + lease extension)
- AFFO growth ~3-4% (organic + Golden Entertainment accretion)
- Market assigns 12.5x P/AFFO
- Cap rates stable at current levels

| Method | Base FV |
|--------|---------|
| P/AFFO | $30.00 |
| NAV | $26.19 |
| DDM | $35.83 |
| **Weighted** | **$30.13** |

### Bull Case (25% probability)

**Assumptions:**
- Caesars lease issue resolved favorably (minimal rent impact + asset transfer)
- Rate cuts compress cap rates by 50bps
- AFFO growth 5-6% (accretive acquisitions + favorable rates)
- Market assigns 14x P/AFFO as concentration fears fade

| Method | Bull FV |
|--------|---------|
| P/AFFO | $35.00 |
| NAV | $31.82 |
| DDM | $53.49 |
| **Weighted** | **$38.33** |

### Expected Value

```
EV = (Bear x 25%) + (Base x 50%) + (Bull x 25%)
EV = ($24.12 x 0.25) + ($30.13 x 0.50) + ($38.33 x 0.25)
EV = $6.03 + $15.07 + $9.58
EV = $30.68
```

---

## COMPARISON TO THESIS

| Metric | Thesis | Adversarial | Delta |
|--------|--------|-------------|-------|
| P/AFFO multiple | 14x | 12.5x | -1.5x |
| AFFO used | $2.37 (2025) | $2.40 (2026 post-reset) | +$0.03 |
| P/AFFO FV | $33.18 | $30.00 | -9.6% |
| NAV | $28.15 | $26.19 | -7.0% |
| DDM | $34.18 | $35.83 | +4.8% |
| **Weighted FV** | **$33.75** | **$30.13** | **-10.7%** |
| **Expected Value** | **$33.75** | **$30.68** | **-9.1%** |
| Quality Tier | A (8/10 manual) | B (QS ~60-65 adjusted) | Downgrade |

### Key Divergence Drivers

1. **P/AFFO multiple (-1.5x):** The thesis uses 14x which is the net-lease sector average. But VICI's tenant concentration (74% two tenants) and the Caesars regional rent issue warrant a discount. GLPI (closest peer) trades at 11.7x. A 12.5x multiple is generous relative to peer reality.

2. **NAV cap rate (+5bps):** The thesis uses 6.5-7.0% blended. I use 6.8% which is barely higher, but I also reduce rent by $80M for the Caesars concession. This is the main NAV driver.

3. **DDM growth rate (-1pp):** The thesis uses 4.5% sustainable dividend growth. I use 3.5% to account for Caesars rent reset impact and more conservative organic growth assumptions.

4. **Quality Tier downgrade:** The thesis manual scoring ignores that quality_scorer.py flags negative ROIC spread and very low insider ownership. A REIT-adjusted assessment places VICI at Tier B, not Tier A.

---

## FINAL VALUATION SUMMARY

```
VALUATION: VICI

Type of Company: Gaming REIT (Triple-Net)
Quality Tier: B (REIT-adjusted QS ~60-65)
Methods Used: P/AFFO (primary) + NAV + DDM

Scenarios:
| Scenario | Fair Value | Prob |
|----------|-----------|------|
| Bear     | $24.12    | 25%  |
| Base     | $30.13    | 50%  |
| Bull     | $38.33    | 25%  |
| Expected | $30.68    | 100% |

Current Price: $28.76
MoS vs Expected: +6.7%
MoS vs Bear: -16.1% (PRICE IS ABOVE BEAR CASE)
MoS vs Base: +4.8%

Thesis FV: $33.75
My FV (Expected): $30.68
Thesis overstatement: +10.0%
```

---

## PEER VALIDATION

### Implied Multiples at My FV

| Metric | At Current Price | At My Base FV | At Thesis FV |
|--------|-----------------|---------------|-------------|
| P/AFFO (2026E $2.40) | 12.0x | 12.6x | 14.1x |
| Dividend Yield | 6.3% | 6.0% | 5.3% |
| NAV Premium/Discount | +10% vs my NAV | +15% | +29% |

At my base FV of $30.13, VICI would trade at 12.6x P/AFFO -- reasonable and in line with GLPI (11.7x) plus a quality premium. The thesis FV implies 14.1x, which requires VICI to trade at a premium to the broader net-lease average -- hard to justify with 74% tenant concentration.

### Precedent Check

From decisions_log.yaml, the VNA.DE adversarial review found:
- Thesis FV overstatement: -25%
- ROIC below WACC was key factor
- NAV haircut was too aggressive

VICI's overstatement is -10%, which is more moderate. The thesis fundamentals are stronger (positive AFFO, covered dividend, good assets), but the FV was still inflated by using a too-generous P/AFFO multiple.

---

## DCF CROSS-CHECK (Reference Only)

The DCF tool uses standard FCF (not AFFO), making it imperfect for REITs. For reference:
- DCF (5% growth, 7% WACC, 2% terminal): Base $35.66, Bear $23.38
- DCF (4% growth, 7.5% WACC, 2% terminal): Base $28.91, Bear $18.79

The DCF range of $24-$36 broadly brackets my REIT-specific methods ($24-$38), providing additional validation.

---

## 🔄 META-REFLECTION

### Dudas/Incertidumbres

1. **Caesars rent reset magnitude is uncertain.** I assumed ~$80M reduction, but the actual outcome could range from $0 (no concession, asset transfer instead) to $150M+ (significant rent cut). This is the single largest uncertainty in the valuation.

2. **Cap rates are cyclical.** If the Fed cuts rates in 2026, cap rates could compress 50-100bps, which would significantly increase NAV. Conversely, if rates rise, NAV compresses further. My base case assumes stable rates.

3. **Quality Score calibration for REITs.** The automated tool gives QS 54 (Tier C) which is clearly too harsh for an investment-grade REIT with 100% rent collection history. But the thesis claim of "Tier A" with 8/10 also seems generous. Truth is likely Tier B.

4. **Golden Entertainment deal accretion.** The $1.16B deal at 7.5% cap rate closes mid-2026. If VICI's cost of capital is ~7%, the spread is only 50bps -- not highly accretive. But it adds a 15th tenant, which helps diversification.

### Sensibilidad Preocupante

- **DDM is wildly sensitive:** Changing Ke-g spread from 4.5% to 5.5% changes FV by 25%. This is why I weight DDM at only 25%.
- **NAV cap rate sensitivity:** Each 50bps change in cap rate moves NAV/share by $3-4.

### Discrepancias con Thesis

The thesis FV of $33.75 is 10% above my independent estimate of $30.68. The thesis is not egregiously wrong -- it is within a reasonable range -- but it systematically leans optimistic:
- Uses sector-average multiple (14x) instead of peer-adjusted multiple (12.5x)
- Does not incorporate Caesars rent reset risk in any scenario
- Claims Tier A quality when objective metrics suggest Tier B
- DDM uses 10% Ke (too high) offset by 4.5% g (too high), resulting in a reasonable but poorly derived number

### Sugerencias para el Sistema

1. **REIT-specific quality scorer needed.** The current quality_scorer.py penalizes all high-leverage businesses equally. REITs structurally use high leverage and should have different benchmarks for Debt/EBITDA and ROIC.

2. **Rent coverage analysis should be mandatory for REIT theses.** The Caesars regional rent coverage of 1.03x is a material risk that the thesis completely missed. Any REIT thesis should include tenant-level rent coverage for top 3 tenants.

3. **Cap rate sensitivity table should be standard in all REIT valuations.** The NAV methodology is only as good as the cap rate assumption.

### Preguntas para Orchestrator

1. **Q4 2025 earnings on Feb 25:** Should we wait 17 days for actual results before making any portfolio decision? They will likely provide 2026 AFFO guidance which would resolve the biggest uncertainty.

2. **Caesars rent reset:** Is the orchestrator aware of any timeline for resolution? This could change the valuation significantly if resolved before or during Q4 earnings call.

3. **Position sizing implication:** At 6.7% MoS vs Expected FV, this is thin margin for a Tier B REIT. Precedents suggest Tier B needs ~20-25% MoS. Current position appears fairly valued at best. Should we consider TRIM?

4. **Conviction level:** Given three analyst downgrades (Evercore, Wells Fargo, Scotiabank) in 2 months, and the Caesars rent overhang, should conviction be downgraded from the thesis's implicit "high" to "low-medium"?

---

## Sources

- [VICI Q3 2025 Earnings Release](https://investors.viciproperties.com/news/news-details/2025/VICI-Properties-Inc--Announces-Third-Quarter-2025-Results/default.aspx)
- [VICI Investor Presentation Nov 2025](https://s1.q4cdn.com/751481880/files/doc_presentations/2025/Nov/03/VICI-Investor-Presentation-Nov-25.pdf)
- [Evercore ISI Downgrade](https://www.investing.com/news/analyst-ratings/vici-properties-stock-rating-downgraded-by-evercore-isi-on-gaming-lease-concerns-93CH-4383154)
- [Scotiabank Downgrade](https://www.marketbeat.com/instant-alerts/vici-properties-nysevici-downgraded-to-sector-perform-rating-by-scotiabank-2026-01-30/)
- [Caesars Lease Concerns - Casino.org](https://www.casino.org/news/vici-admits-caesars-regional-casinos-lease-has-been-overhang/)
- [VICI May Reduce Caesars Rent](https://vegasonlinecasino.com/vici-may-evaluate-reducing-rent-for-caesars-regional-casinos/)
- [Golden Entertainment Acquisition](https://investors.viciproperties.com/news/news-details/2025/VICI-Properties-Inc--Announces-1-16-Billion-Sale-Leaseback-Transaction-With-Golden-Entertainment/default.aspx)
- [Net Lease Cap Rates Q4 2025](https://thesiliconreview.com/2026/01/the-silicon-reviewjan-2026net-lease-cap-rates-stable-q4-2025)
- [GLPI Q3 2025 Results](https://www.globenewswire.com/news-release/2025/10/30/3177952/29133/en/Gaming-and-Leisure-Properties-Reports-Record-Third-Quarter-2025-Results-and-Updates-2025-Full-Year-Guidance.html)
- [Realty Income 2026 Outlook - Seeking Alpha](https://seekingalpha.com/article/4858800-realty-income-my-best-reit-idea-for-2026)
- [10Y Treasury - FRED](https://fred.stlouisfed.org/series/DGS10)
- [VICI AFFO Consensus - StockAnalysis](https://stockanalysis.com/stocks/vici/)
- [VICI Price Target Consensus - MarketBeat](https://www.marketbeat.com/stocks/NYSE/VICI/forecast/)
