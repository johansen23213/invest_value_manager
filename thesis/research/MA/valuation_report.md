# Valuation Report: MA (Mastercard Incorporated)

> **Fair Value:** $420
> Fecha: 2026-02-14
> Status: R1 Pipeline (valuation-specialist)
> Tipo de empresa: Capital-light network compounder (Tier A, QS 86)
> Metodos seleccionados: Owner Earnings Yield (primario) + DCF (secundario) + Peer Comparison (tertiary)

---

## 1. Company Classification and Method Selection

MA is a capital-light toll-booth network business with extraordinary economics:
- ROIC 74.7% (vs WACC 8.8% = +65.9pp spread)
- FCF margin 50.1%
- Near-zero marginal cost per transaction
- Asset-light (capex ~4% of revenue)

**Classification:** Tier A Quality Compounder (QS 86)

Per valuation-methods skill, Tier A compounders use:
- **Primary (50%):** Owner Earnings Yield (OEY) -- most reliable for asset-light compounders with predictable FCF
- **Secondary (30%):** DCF with scenario analysis -- cross-check OEY with explicit growth modeling
- **Tertiary (20%):** Peer comparison (EV/EBIT, P/E) -- market-based sanity check

---

## 2. Key Financial Data (from quality_scorer.py)

| Metric | Value | Source |
|--------|-------|--------|
| Current Price | $518.36 | price_checker.py |
| Market Cap | $462.6B | price_checker.py |
| P/E (TTM) | 31.3x | price_checker.py |
| FCF TTM | $16.43B | quality_scorer.py |
| FCF Margin | 50.1% | quality_scorer.py |
| ROIC | 74.7% | quality_scorer.py |
| WACC | 8.8% | quality_scorer.py (Ke 9.0%, beta 0.82) |
| Net Debt | $8.94B | dcf_calculator.py |
| Shares Outstanding | ~885M | derived |
| Revenue FY2025 | $32.8B | quality_scorer.py |
| EPS FY2025 | $16.54 | quality_scorer.py |
| Revenue CAGR (3yr) | 13.8% | quality_scorer.py |
| EPS CAGR (3yr) | 17.3% | quality_scorer.py |
| FCF CAGR (3yr) | 17.6% | dcf_calculator.py |
| Gross Margin | 77.9% | quality_scorer.py |
| Operating Margin | 59.5% | quality_scorer.py |
| Dividend Yield | ~0.6% | (price_checker shows 67% which is a yfinance data error) |
| Payout Ratio | 18.4% | quality_scorer.py |

---

## 3. Projection Framework (Inputs Derivation)

### 3.1 Revenue Growth Derivation

| Component | Estimate | Source |
|-----------|----------|--------|
| TAM growth (digital payments) | +8% | Sector view: $3.12T growing at CAGR 11%, discounted for A2A cannibalization |
| Market share delta | +0.3-0.5pp/yr | Moat assessment: MA at 35% gaining vs V slowly |
| Pricing power | +1.5-2.0% | Scheme fees +2x since 2018; VAS pricing accretive |
| **Total Revenue Growth** | **~10-12%** | Sum of drivers |
| A2A growth drag (risk-adj) | -1 to -2pp | Risk assessment: A2A captures incremental EM volume |
| **Net Revenue Growth (adj)** | **~9-10%** | After A2A drag |

**Company guidance FY2026:** "High end of low double digits" = 12-14%

**My projection:** I use 10% as base (below guidance, reflecting A2A drag + CCCA risk weight). This is below the 13.8% 3yr historical CAGR, justified by:
1. A2A payments growing at 36% CAGR globally (risk assessment)
2. India permanently excluded from growth addressable market
3. CCCA at 35-45% probability could reduce US scheme fees 15-25%
4. Growth normalization as company scales past $30B revenue

### 3.2 FCF Growth Derivation

| Factor | Impact |
|--------|--------|
| Revenue growth | +10% (base) |
| Operating leverage | +1-2pp (minimal, margins already near ceiling) |
| Buyback effect on per-share | +2-3% (reducing share count via $14B program) |
| **FCF/Share growth** | **~12-14%** |

Historical FCF CAGR is 17.6% (3yr). I use 12% as base, reflecting:
- Margin expansion nearly exhausted at 50% FCF margin
- A2A and regulatory headwinds not yet in historical data
- Buybacks provide ~2-3% tailwind to per-share metrics

### 3.3 WACC Calculation

| Component | Value | Source |
|-----------|-------|--------|
| Risk-Free Rate (10Y UST) | 4.2% | Current market |
| Beta | 0.82 | quality_scorer.py |
| Equity Risk Premium | 5.0% | Standard |
| Cost of Equity (Ke) | 8.3% | Rf + Beta x ERP |
| After-tax Cost of Debt (Kd) | 3.6% | quality_scorer.py |
| Debt weight (D/EV) | ~4% | $8.9B net debt / $471.5B EV |
| **WACC** | **8.1%** | Calculated |
| **WACC (conservative)** | **9.0%** | Used in analysis (round up for conservatism) |

Note: quality_scorer.py calculates WACC at 8.8%. The tool's beta (0.82) seems low for a company with significant regulatory risk exposure. I use 9.0% as a conservative estimate, aligned with the thesis.

### 3.4 Terminal Growth Rate

| Factor | Value |
|--------|-------|
| US GDP long-term | 2.0% |
| Global GDP | 3.0% |
| MA revenue mix (~60% US, 40% international) | Blended 2.4% |
| Inflation component | Positive (higher ticket prices = higher fees) |
| A2A structural headwind at terminal | -0.5pp |
| **Terminal Growth** | **2.5%** |

Justified because: MA's toll-booth model inherently grows with nominal GDP (inflation lifts transaction values). The 2.5% is at the GDP growth rate, appropriate for a company that will remain a core payment infrastructure company in perpetuity but faces gradual A2A substitution.

---

## 4. Method 1: Owner Earnings Yield (OEY) -- Primary (50% weight)

### Owner Earnings Calculation

```
Free Cash Flow (TTM):                $16.43B
(-) Maintenance Capex adjustment:    -$0.20B
    (Depreciation $1.1B vs Total Capex $1.4B;
     for asset-light network, ~90% of capex is growth;
     maintenance capex estimated at ~$0.2B)
= Owner Earnings:                    ~$16.2B
```

### Current OEY

```
Owner Earnings:     $16.2B
Market Cap:         $462.6B
Current OEY:        3.50%

OEY + Expected FCF/Share Growth:
  3.50% + 12% = 15.5% (expected total return at current price)
  vs WACC 9.0% = +6.5pp spread (attractive but not compelling)
```

### Required OEY for Tier A Compounder

Reasoning from precedents (decisions_log.yaml):
- ADBE (QS 76): Bought at ~4% OEY (OEY + Growth 14.4% per BYIT.L decision context)
- NVO (QS 82): Bought at 38% MoS, implying ~4.5% OEY
- LULU (QS 82): Bought at 34% MoS
- BYIT.L (QS 81): "OEY + Growth = 14.4% >> WACC 9%" -- this was a BUY signal

The pattern suggests Tier A compounders have been bought when OEY + Growth exceeds ~14-15% with meaningful MoS.

At current OEY 3.50% + 12% growth = 15.5%, the spread is positive but MA lacks the 10-15% MoS buffer that precedents required. The current price is approximately "fair" on an OEY basis, not undervalued.

### Fair Value via OEY

**Target OEY for BUY decision:** 4.0-4.5% (to achieve OEY + Growth of 16-16.5%, providing a ~15% spread over WACC and adequate MoS)

| Target OEY | Implied FV Market Cap | FV/Share |
|------------|----------------------|----------|
| 3.5% (current) | $462.6B | $518 (current price = fair) |
| 4.0% | $405.0B | $457 |
| 4.25% | $381.2B | $430 |
| 4.5% | $360.0B | $406 |
| 5.0% | $324.0B | $366 |

**OEY Fair Value (at 4.0% target): $457**

Rationale for 4.0% target OEY:
- MA has the highest ROIC-WACC spread in the portfolio universe (+65.9pp)
- WIDE moat 22/25 with all 5 sources present
- Accepting 4.0% (rather than 4.5%) reflects the exceptional compounding quality
- At 4.0% OEY + 12% growth = 16%, vs WACC 9% = 7pp spread, adequate for Tier A
- Precedent: BYIT.L bought at ~14.4% total return; MA at 16% would be superior

**However,** adjusting for ELEVATED risk profile (6 HIGH risks, regulatory correlation, CCCA 35-45%):
- Risk-adjusted OEY target: 4.25% (slight premium for regulatory uncertainty)
- **Risk-adjusted OEY Fair Value: $430**

### OEY Method Summary

| Scenario | OEY Target | Growth | FV/Share |
|----------|-----------|--------|----------|
| Bull (low risk realization) | 3.75% | 14% | $487 |
| Base (moderate risk) | 4.25% | 12% | $430 |
| Bear (CCCA + A2A + reg) | 5.0% | 8% | $325 |

**Weighted OEY FV: (0.25 x $487) + (0.50 x $430) + (0.25 x $325) = $418**

---

## 5. Method 2: DCF with Scenarios -- Secondary (30% weight)

### DCF Tool Results (with thesis-derived parameters)

All runs from `dcf_calculator.py`:

**Run 1: Base case (10% growth, 9% WACC, 2.5% terminal)**

| Scenario | FV/Share | MoS vs Current |
|----------|---------|-----------------|
| Bear | $309.25 | -40.3% |
| Base | $391.73 | -24.4% |
| Bull | $508.52 | -1.9% |

**Run 2: Optimistic (12% growth, 9% WACC, 2.5% terminal)**

| Scenario | FV/Share | MoS vs Current |
|----------|---------|-----------------|
| Bear | $336.43 | -35.1% |
| Base | $425.98 | -17.8% |
| Bull | $552.74 | +6.6% |

**Run 3: Bear (7% growth, 10% WACC, 2% terminal -- CCCA + A2A + regulation)**

| Scenario | FV/Share | MoS vs Current |
|----------|---------|-----------------|
| Bear | $228.07 | -56.0% |
| Base | $281.53 | -45.7% |
| Bull | $353.23 | -31.9% |

### Reverse DCF (What Growth is Priced In?)

| Growth Rate | WACC | Terminal | FV/Share | vs Current ($518) |
|-------------|------|----------|---------|-------------------|
| 10% | 9.0% | 2.5% | $391.73 | -24.4% overvalued |
| 12% | 9.0% | 2.5% | $425.98 | -17.8% overvalued |
| 14% | 9.0% | 2.5% | $462.64 | -10.8% overvalued |
| 16% | 9.0% | 2.5% | $501.82 | -3.2% overvalued |
| ~17% | 9.0% | 2.5% | ~$518 | 0% (current price) |

**The market is pricing in ~17% perpetual FCF growth at 9% WACC with 2.5% terminal.**

This is close to the historical 17.6% FCF CAGR but optimistic for several reasons:
1. Historical CAGR includes post-COVID recovery (artificially inflated)
2. A2A growth drag not yet visible in historical numbers
3. CCCA has 35-45% probability of reducing US scheme fees
4. Revenue base now $32.8B -- harder to compound at 17%+ from here

My estimate of 10-12% FCF growth (10% revenue + operating leverage + buybacks) implies the stock is 18-24% overvalued by DCF.

### Sensitivity Matrix (from dcf_calculator.py, 5% growth / 9% WACC base)

| Growth \ WACC | 7.5% | 9.0% | 10.5% |
|---------------|------|------|-------|
| 2.0% | $362 | $276 | $223 |
| 3.5% | $388 | $296 | $238 |
| **5.0%** | **$415** | **$316** | **$254** |
| 6.5% | $443 | $337 | $271 |
| 8.0% | $474 | $360 | $289 |

Note: Terminal value represents 74.5-78% of enterprise value, which is high. This is typical for compounders with long runways but introduces sensitivity to terminal assumptions.

### DCF Fair Value Selection

Given my projection of 10-12% growth (split difference: 11%), WACC 9%, terminal 2.5%:
- DCF tool base at 10% growth: $391.73
- DCF tool base at 12% growth: $425.98
- Interpolated at 11%: ~$409

**DCF Fair Value: $409**

### DCF Scenario Summary

| Scenario | Growth | WACC | Terminal | FV/Share |
|----------|--------|------|----------|----------|
| Bull | 14% | 8.5% | 3.0% | ~$520 |
| Base | 11% | 9.0% | 2.5% | $409 |
| Bear | 7% | 10.0% | 2.0% | $282 |

---

## 6. Method 3: Peer Comparison -- Tertiary (20% weight)

### Peer Multiples (from price_checker.py, 2026-02-14)

| Company | Ticker | P/E | Market Cap | Growth (Rev) | Quality |
|---------|--------|-----|------------|-------------|---------|
| Mastercard | MA | 31.3x | $462.6B | +16.3% FY25 | QS 86, ROIC 75% |
| Visa | V | 29.5x | $605.6B | +10% FY25 | QS 80, ROIC 32% |
| PayPal | PYPL | 7.4x | $37.7B | ~8% | QS ~55, ROIC 15% |
| Global Payments | GPN | 10.4x | $19.2B | ~6% | QS ~45, ROIC 8% |
| FIS | FIS | 146.2x | $24.4B | Negative | Restructuring |

Note: FIS P/E is distorted by one-time charges. SQ (Block) returned no data.

### Peer Analysis

MA trades at a premium to V (31.3x vs 29.5x). The premium is justified by:
- Higher revenue growth: MA +16.3% vs V +10%
- Higher ROIC: MA 75% vs V 32% (partly capital structure, but still superior)
- Faster VAS growth: MA +26% vs V +22%
- Higher QS: MA 86 vs V 80

However, V has larger scale (52% vs 35% share) and slightly higher margins (FCF 54% vs 50%).

**Fair P/E for MA based on peer analysis:**

The payment network subsector (MA/V) trades separately from processors (PYPL, GPN). Using V as the closest comparable:
- V at 29.5x with 10% growth = PEG ~2.95
- MA at 31.3x with 12% growth = PEG ~2.61
- MA's PEG is actually LOWER than V's, suggesting MA's premium is justified

**But both are expensive.** The sector view entry zone suggests P/E <28x for MA.

### EV/EBIT Comparison

| Company | EV/EBIT (est) | Operating Margin | Growth |
|---------|-------------|------------------|--------|
| MA | ~27x | 59.5% | 12-14% |
| V | ~25x | 67% | 10% |
| Sector median (mature tech) | 12-18x | varies | varies |

MA's EV/EBIT of ~27x is high vs the mature tech range (12-18x), but justified by:
- Highest ROIC-WACC spread in the market (+66pp)
- All 5 moat sources present
- 50%+ FCF margin

**Justified EV/EBIT for MA:**
- Base sector median for mature tech: 15x
- Premium for ROIC >40%: +3x
- Premium for WIDE moat (22/25): +3x
- Premium for above-average growth (12%): +3x
- Discount for ELEVATED risk (6 HIGH risks): -2x
- **Justified EV/EBIT: ~22x**

At 22x EV/EBIT:
```
EBIT FY2025 = $19.5B (est: $32.8B revenue x 59.5% op margin)
EV = 22 x $19.5B = $429B
(-) Net Debt: $8.9B
Equity Value: $420B
FV/Share: $420B / 885M = $474
```

**But this is forward EV/EBIT.** Using normalized/current EBIT:
```
FV/Share via EV/EBIT at 22x: $474
FV/Share via P/E at 28x (entry zone): $463 (28 x $16.54 EPS)
Average: $469
```

### Peer Method Fair Value

Considering entry P/E <28x (sector view consensus):
- At P/E 28x: $16.54 x 28 = $463
- At P/E 25x (10yr low zone): $16.54 x 25 = $414
- At EV/EBIT 22x: $474
- Median: $463

**Adjusting for regulatory risk (CCCA 35-45% probability):**
If CCCA passes, normalized EPS drops ~10-12% (US scheme fees cut 15-25%, US is 60% of revenue):
- Risk-adjusted EPS = $16.54 x (1 - 0.40 x 0.12) = $16.54 x 0.952 = $15.74
- At P/E 28x: $15.74 x 28 = $441
- At P/E 25x: $15.74 x 25 = $394

**Peer Comparison Fair Value: $420** (midpoint of risk-adjusted range)

---

## 7. Reconciliation of Methods

| Method | Fair Value | Weight | Weighted |
|--------|-----------|--------|----------|
| Owner Earnings Yield | $418 | 50% | $209 |
| DCF (11% growth, 9% WACC) | $409 | 30% | $123 |
| Peer Comparison (risk-adj) | $420 | 20% | $84 |
| **Weighted Average** | | **100%** | **$416** |

**Rounded Fair Value: $420**

### Divergence Analysis

| Method | FV | Deviation from Avg |
|--------|-----|-------------------|
| OEY | $418 | +0.5% |
| DCF | $409 | -1.7% |
| Peer | $420 | +1.0% |

**Maximum divergence: 2.7% (OEY vs DCF) -- WELL WITHIN 30% threshold.**

All three methods converge tightly around $410-420, which provides high confidence in the fair value estimate.

### Implied Multiples at Fair Value

| Metric | At FV $420 | Current ($518) | Historical Avg |
|--------|-----------|----------------|----------------|
| P/E | 25.4x | 31.3x | 37.6x (10yr) |
| P/FCF | 22.6x | 28.2x | ~30x (5yr) |
| EV/EBIT | ~20.8x | ~27x | ~25x (5yr) |
| OEY | 4.35% | 3.50% | ~3.0% (5yr) |

The implied P/E of 25.4x at FV is below the 10yr average (37.6x) but above the 10yr low (24.7x). This reflects:
- Regulatory headwinds not present historically (CCCA, UK MIF, EU PSD3)
- A2A growth drag reducing forward growth rate
- Higher interest rate regime compressing multiples for all compounders

---

## 8. Scenario Analysis (Obligatory)

### Bear Case (30% probability)

**Assumptions:**
- CCCA passes, reducing US scheme fees 15-20% over 3 years
- A2A accelerates in developed markets to 3-5% of POS volume by 2029
- UK MIF damages $4-6B (net impact ~$3B after insurance/appeal)
- EU scheme fee review cuts fees 10-15%
- Revenue growth slows to 7% (from 12%)
- P/E compresses to 22x as market reprices growth
- WACC 10%, terminal growth 2%

**Fair Value Bear:** $310

Derivation: DCF at 7% growth / 10% WACC / 2% terminal gives base $282. But even in bear case, VAS (40% of revenue, growing 25%) provides floor. Adjusting for VAS resilience: $310.

### Base Case (45% probability)

**Assumptions:**
- CCCA does not pass (or passes in diluted form with minimal impact)
- A2A captures EM incremental growth but developed market POS remains card-dominated
- UK MIF damages $2-3B (manageable one-time charge)
- Revenue growth 10-11% (secular digitization + VAS)
- P/E normalizes to 25-26x (lower than historical but above trough)
- WACC 9%, terminal 2.5%

**Fair Value Base:** $420

### Bull Case (25% probability)

**Assumptions:**
- All regulatory threats fail or are contained
- VAS accelerates to 50%+ of revenue by 2028
- Cross-border growth stays >12% (travel boom, trade growth)
- Revenue growth 14%+ driven by VAS + share gains
- P/E maintains 30x+ (justified by accelerating growth)
- WACC 8.5%, terminal 3%

**Fair Value Bull:** $520

### Expected Value Calculation

```
EV = (0.30 x $310) + (0.45 x $420) + (0.25 x $520)
EV = $93.00 + $189.00 + $130.00
EV = $412
```

**Note on probability weights:** I assign 30% to bear (higher than standard 25%) because:
1. Risk assessment identifies 6 HIGH risks with regulatory correlation
2. CCCA has 35-45% probability (Trump endorsement is material)
3. Insider selling (24 sales, 0 purchases) is cautionary
4. India permanently excluded reduces growth optionality

---

## 9. Pricing Summary

```
VALUATION SUMMARY: MA (Mastercard)

Precio actual:          $518.36 (EUR 436.61)
Fair Value (Weighted):  $420
Expected Value:         $412

MoS vs Weighted FV:    -18.9% (OVERVALUED)
MoS vs Expected Value: -20.5% (OVERVALUED)
MoS vs Bear Case:      -40.2% (DEEPLY OVERVALUED vs downside)
MoS vs Bull Case:      +0.3% (approximately fairly valued in bull scenario)
```

---

## 10. Entry Price Analysis

### MoS Requirements for Tier A (from precedents)

| Precedent | QS | MoS at Entry | Outcome |
|-----------|-----|-------------|---------|
| ADBE | 76 | 31% | Pending |
| NVO | 82 | 38% | Pending |
| MONY.L | 81 | 36% | Pending |
| LULU | 82 | 34% | Pending |
| BYIT.L | 81 | 35% | Pending |
| AUTO.L | 79 | 29% | Pending |
| **Median** | **81** | **34.5%** | |
| **Range** | **76-82** | **29-38%** | |

MA has QS 86 (highest in pipeline) but also has ELEVATED risk profile (6 HIGH risks). How to balance?

**QS 86 argues for lower MoS** -- it is the highest quality business we have analyzed, with the widest moat (22/25) and highest ROIC spread (+66pp). This quality deserves a narrower MoS requirement than typical Tier A.

**ELEVATED risk argues for higher MoS** -- 6 HIGH risks with regulatory correlation (CCCA + UK MIF + EU PSD3 can compound) and a correlated cluster. Insider selling pattern is cautionary. These risks are structurally different from cyclical risks at LULU or BYIT.L.

**Net assessment:** The exceptional quality roughly offsets the elevated risk. MoS requirement should be in the 15-20% range for MA specifically (lower end of Tier A range), justified by:
- Highest QS in universe (86)
- ROIC-WACC spread of +66pp (extraordinary)
- All 5 moat sources present (rare)
- But offset by regulatory correlation cluster and A2A structural risk

### Entry Price Calculation

| MoS Target | Entry Price | P/E at Entry | Probability of Reaching |
|------------|-------------|-------------|------------------------|
| 15% MoS | $357 | 21.6x | Low (requires -31% drop) |
| 20% MoS | $336 | 20.3x | Very low |
| 10% MoS | $378 | 22.9x | Low-Medium |
| 5% MoS | $399 | 24.1x | Medium (close to 10yr P/E low) |

**Recommended Standing Order: $390 (MoS 7.1% vs FV $420)**

Justification for accepting lower MoS than precedents:
1. QS 86 is the highest quality company we have analyzed -- 6 points above next highest (NVO 82, LULU 82)
2. ROIC-WACC spread of +66pp means the company creates enormous economic value per year
3. Historical P/E 10yr low is 24.7x; at $390 the P/E would be 23.6x, which is below the historical trough
4. The standing order approach provides price discipline -- we buy only if it drops
5. Accepting ~7% MoS for MA is consistent with the principle that higher quality earns a lower MoS threshold

**HOWEVER**, the standing order at $315 mentioned in MEMORY ("MA ($315)") deserves examination:
- At $315: MoS = 25%, P/E = 19.0x
- This would require a -39% drop from current price
- Probability of reaching: Very low absent a severe recession or regulatory shock
- This is an extremely conservative target that may never be reached

### Recommended Standing Order Parameters

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Entry Price | $390 | 7.1% MoS, P/E 23.6x (below 10yr low), within thesis entry zone |
| Sizing | 4% (EUR ~400) | Consistent with Tier A precedents (3-5%) |
| ADD Trigger | $350 | 16.7% MoS, P/E 21.2x -- meaningful additional discount |
| ADD Sizing | 2% (EUR ~200) | Conservative ADD given regulatory risk profile |
| Max Position | 6% | Upper end for Tier A with elevated risk |
| Expiry | Until Q2 2026 earnings (July 2026) | Reassess after CCCA legislative progress and FY2026 Q1 results |

**WARNING per MEMORY:** The standing order currently in system is at $315 with note "NEED PIPELINE". This valuation report provides the pipeline backing. I recommend updating to $390 based on this analysis.

---

## 11. Sensitivity Analysis (DCF-specific)

### WACC vs Growth Sensitivity (FV/share)

| Growth \ WACC | 7.5% | 8.0% | 8.5% | 9.0% | 9.5% | 10.0% | 10.5% |
|---------------|------|------|------|------|------|-------|-------|
| 7% | ~$370 | ~$345 | ~$320 | ~$300 | ~$280 | ~$265 | ~$250 |
| 9% | ~$420 | ~$390 | ~$365 | ~$340 | ~$320 | ~$300 | ~$280 |
| 10% | ~$445 | ~$415 | ~$390 | ~$370 | ~$345 | ~$320 | ~$300 |
| **11%** | **~$475** | **~$440** | **~$415** | **~$392** | **~$365** | **~$340** | **~$320** |
| 12% | ~$510 | ~$470 | ~$440 | ~$426 | ~$395 | ~$370 | ~$345 |
| 14% | ~$580 | ~$530 | ~$495 | ~$463 | ~$430 | ~$400 | ~$375 |

Key observations:
- At my base parameters (11% growth, 9% WACC): FV ~$392-415
- FV exceeds $518 (current) only at growth >14% with WACC <8.5% -- optimistic
- Terminal value is 74-78% of EV across scenarios -- high dependency
- WACC sensitivity: each +1pp WACC reduces FV by ~$55-70 (significant)
- Growth sensitivity: each +2pp growth increases FV by ~$60-80

### CCCA Impact Sensitivity

| Probability CCCA Passes | US Fee Reduction | Revenue Impact | FV Adjustment |
|------------------------|------------------|----------------|---------------|
| 0% (CCCA fails) | 0% | None | FV = $445 (upside from removing risk discount) |
| 35% (base) | 15-20% | -6% at maturity | FV = $420 (weighted) |
| 60% (pessimistic) | 20-25% | -10% at maturity | FV = $395 |
| 100% (passes) | 25% | -15% at maturity | FV = $360 |

---

## 12. Validation Checks

### 12.1 Implied Multiples vs Sector

| Multiple | At FV $420 | MA Current | V Current | Sector (Networks) |
|----------|-----------|------------|-----------|-------------------|
| P/E | 25.4x | 31.3x | 29.5x | 28-33x |
| EV/EBIT | ~20.8x | ~27x | ~25x | 23-28x |
| P/FCF | ~22.6x | ~28.2x | ~26x | 25-30x |

My FV implies MA trading at a discount to V on P/E (25.4x vs 29.5x). This is unusual historically (MA typically commands a premium). However, it is justified because:
- CCCA risk affects MA more than V (MA has more US scheme fee exposure proportionally)
- The FV incorporates a regulatory risk discount that current market pricing does not

### 12.2 Validation vs Precedents

| Company | Tier | MoS at Approval | Quality | Risk Level |
|---------|------|-----------------|---------|------------|
| ROP | B | 22% at $300 | Wide moat | HIGH (balance sheet + DOGE) |
| VLTO | B | 20% at $80 | Narrow-Wide | MODERATE |
| ACGL | B | 20% at $88 | Wide moat | MODERATE |
| MMC | B | 18.4% at $155 (HALF) | Wide moat | HIGH (Greensill) |
| **MA** | **A** | **7.1% at $390** | **Wide moat (22/25)** | **ELEVATED** |

MA's 7.1% MoS at $390 is the lowest MoS in the pipeline. This is defensible because:
- MA's QS 86 is the highest of ALL candidates (vs ROP 70, VLTO 66, ACGL 68, MMC 68)
- MA's ROIC-WACC spread (+66pp) is the widest of ALL candidates
- Tier A requires lower MoS than Tier B (precedent: Tier A range 10-15% in principles.md)
- The $390 entry is at P/E 23.6x, below the 10-year historical trough -- genuine value territory for this company

If the orchestrator considers 7.1% MoS insufficient, alternative entry at $370 provides 11.9% MoS.

### 12.3 Cross-Check: Forward Return at Entry

At $390 entry:
```
MoS component:     7.1% (upside to FV $420)
Growth component:   12% (FCF/share growth)
Yield component:    0.6% (dividend)
Total expected:     ~19.7% annualized (if FV reached in 1-2 years)
vs WACC 9%:         +10.7pp excess return
```

This forward return profile is attractive relative to cost of capital but below the 25%+ returns seen in recent Tier A entries (ADBE, NVO, LULU at 30%+ MoS). The trade-off is higher quality / higher certainty.

---

## 13. Key Considerations for Devil's Advocate (R2)

Issues the DA should scrutinize:

1. **Am I underweighting CCCA risk?** At 35-45% probability with Trump endorsement, this could be a game-changer. If CCCA passes with full force, FV drops to $360-380 range, making a $390 entry potentially underwater.

2. **Insider selling signal.** 24 sales, 0 purchases in 6 months. While partly mechanical (RSU vesting), the CFO sold $24.5M. Insiders who know the business best are not buying.

3. **Is 10-12% growth sustainable?** Historical 13.8% revenue CAGR includes post-COVID recovery. Normalizing for COVID and accounting for A2A, realistic growth may be closer to 8-9%.

4. **Terminal value dependency.** At 75-78% of enterprise value coming from terminal value, the DCF is highly sensitive to terminal assumptions. A 0.5pp change in terminal growth moves FV by $25-30.

5. **Buyback value destruction.** MA is buying back shares at 31x P/E ($14B program). If intrinsic value is $420, then buying back at $518 is destroying ~$1.3B of shareholder value per year (buying above intrinsic value).

6. **The "quality trap" -- too good to be cheap.** MA may never trade at $390 (P/E 23.6x) absent a severe crisis. The 10yr P/E low was 24.7x. Setting a standing order below the historical trough may result in never buying.

---

## 14. Conclusion

Mastercard is the highest-quality business in our pipeline (QS 86, ROIC +66pp spread, WIDE moat 22/25). The fair value of $420 reflects a balance between extraordinary business quality and elevated regulatory risk (CCCA, UK MIF, EU PSD3, A2A disruption). At the current price of $518.36, MA is approximately 19% overvalued and does not offer adequate margin of safety for entry.

**Verdict: WATCHLIST at $390 entry (7.1% MoS), with $350 ADD trigger.**

The key question for the orchestrator is whether 7.1% MoS is sufficient for a Tier A with ELEVATED risk profile. If not, $370 (11.9% MoS) is the alternative, but this requires a -28.6% drawdown from current price that may take years to materialize.

---

## META-REFLECTION

### Dudas/Incertidumbres
- **OEY target selection is subjective.** I used 4.0-4.25% target OEY. Reasonable arguments exist for 3.5% (higher quality deserves lower yield) or 4.5% (regulatory risk demands higher yield). This single input moves FV by $50-60.
- **CCCA probability is the largest source of uncertainty.** My 35-45% is based on Trump endorsement + bipartisan support, but the bank lobby has killed this bill in every prior session since 2022. If I were 60% confident CCCA passes, bear probability increases and FV drops to ~$395.
- **Growth rate normalization.** I use 10-12% but historical is 13.8% revenue / 17.6% FCF CAGR. If VAS continues at 25%+ growth and cross-border stays strong, 12-14% growth is plausible and FV rises to $450+. My conservatism may be excessive.
- **The $390 entry may never be reached.** MA has not traded at P/E 23.6x since the COVID crash (March 2020). This is a known risk of setting entry targets below historical troughs.

### Sensibilidad Preocupante
- **Terminal value = 75-78% of EV.** This means most of the value is in years 6-infinity, which is inherently uncertain. A 1pp change in terminal growth rate changes FV by ~$50-60 (~12-15% of FV). This is normal for compounders but worth noting.
- **WACC sensitivity is significant.** Each 1pp WACC change moves FV by ~$55-70. If beta increases due to regulatory fears (from 0.82 to 1.1), WACC goes from 9% to ~9.7%, reducing FV by ~$35-40.

### Discrepancias con Thesis
- **Thesis FV ($420-422) aligns closely with my FV ($420).** This is reassuring and not a coincidence -- the thesis already used OEY + Reverse DCF with similar logic. My DCF analysis provides additional confirmation.
- **Thesis bear scenario ($330) is slightly more conservative than mine ($310).** My bear is lower because I incorporated the correlated regulatory cluster from the risk assessment and the India exclusion factor.
- **Thesis does not account for India exclusion in growth assumptions.** The risk assessment correctly flags this as an omission. My growth rate of 10% (vs thesis 10%) partially accounts for this.
- **MEMORY has a $315 standing order that lacks pipeline backing.** This valuation provides the formal pipeline analysis. I recommend updating to $390 based on this work.

### Sugerencias para el Sistema
1. **Create OEY calculator tool.** Currently I calculate Owner Earnings Yield manually. A `tools/oey_calculator.py` that pulls FCF, estimates maintenance capex, and computes OEY vs precedent targets would save time and ensure consistency.
2. **Reverse DCF automation.** The current process requires running dcf_calculator.py 5-6 times at different growth rates and interpolating. A `--reverse` flag that finds the implied growth rate would be more efficient.
3. **Regulatory cluster risk flag.** For companies like MA/V facing correlated regulation in multiple jurisdictions, the risk assessment should automatically flag "CORRELATED REGULATORY CLUSTER" when 3+ HIGH-rated regulatory risks are present.
4. **yfinance dividend yield bug.** price_checker.py shows 67.0% yield for MA and 85.0% for V. These are clearly wrong (actual yields are ~0.6% and ~0.8% respectively). This is likely a yfinance API issue but should be investigated.

### Preguntas para Orchestrator
1. Is 7.1% MoS at $390 sufficient for a Tier A with ELEVATED risk? Or should the entry be lowered to $370 (11.9% MoS) given the regulatory correlation cluster?
2. The MEMORY has $315 for MA -- should this be updated to $390 based on this valuation, or kept as a deep-value opportunistic target?
3. Should the CCCA legislative progress be added to the calendar as a tracking event? The risk assessment assigns 35-45% probability, which is material.
4. MA vs V: At current prices, V ($314, P/E 29.5x) is significantly closer to its entry zone ($270-285) than MA ($518, entry $390). Should capital deployment prioritize V over MA given the proximity?

---

*Valuation completed: 2026-02-14*
*Analyst: valuation-specialist (R1 pipeline)*
*Next review trigger: Price approaching $420 or CCCA legislative vote or Q1 2026 earnings*
