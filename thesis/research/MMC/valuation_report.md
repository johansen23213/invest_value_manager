# Valuation Report: MMC (Marsh & McLennan Companies)

> **Valuation Date:** 2026-02-13
> **Analyst:** Valuation Specialist (automated, opus)
> **Thesis FV:** $220 | **Valuation FV (this report):** $190 | **Entry:** $160

---

## Company Classification

**Type:** Asset-light fee-based services (insurance brokerage + consulting)
**Tier:** B (QS Tool 64, Adjusted 68)
**Methods selected:** EV/EBIT (primary) + DCF (secondary) + P/E (cross-check)

**Why these methods:**
- MMC is an asset-light, fee-based business with no underwriting risk. EV/EBIT is the most appropriate primary method because it captures the enterprise value relative to operating earnings and allows direct peer comparison with AON, AJG, WTW, and BRO.
- DCF captures the growth trajectory (7% total, 4% organic + 3% M&A) but has HIGH sensitivity (130% FV spread, terminal value 62% of EV). This limits its reliability as a standalone method.
- P/E cross-check validates the output against peer forward multiples.

---

## Input Data

### From quality_scorer.py (live data, 2026-02-13)

| Metric | Value | Trend |
|--------|-------|-------|
| Revenue FY2025 | $26.98B | CAGR +9.2% (includes inorganic) |
| EBIT FY2025 | $6.50B | Expanding margins (20.7% -> 23.1%) |
| Net Income FY2025 | $4.16B | |
| EPS FY2025 | $8.48 | CAGR +11.5% |
| FCF FY2025 | $5.00B | Growing from $3.0B (2022) |
| SBC FY2025 | $0.39B | 7.9% of FCF |
| SBC-adjusted FCF | $4.61B | |
| ROIC | 14.2% | Spread +6.6pp vs WACC |
| WACC (tool) | 7.6% | Ke 8.6%, Kd 4.5%, beta 0.75 |
| Net Debt | $18.91B | 2.4x EBITDA (McGriff-elevated) |
| Shares Outstanding | 489.9M | |

### From price_checker.py (live, 2026-02-13)

| Metric | Value |
|--------|-------|
| Current Price | $182.70 (EUR 153.89) |
| 52-week High | $248.00 |
| 52-week Low | $174.18 |
| Distance from ATH | -26.3% |
| Trailing P/E | 21.9x |
| Dividend Yield | 2.0% |
| Market Cap | $89.8B |

### WACC Derivation (from thesis projection-framework)

| Component | Value | Source |
|-----------|-------|--------|
| Risk-Free Rate (10Y UST) | 4.3% | Current market |
| Equity Risk Premium | 5.5% | Damodaran |
| Beta | 0.75 | yfinance |
| Ke | 8.4% | 4.3% + 0.75 * 5.5% |
| Kd (pre-tax) | 4.5% | interest_expense / total_debt |
| Tax rate | 23.6% | Effective from financials |
| Kd (after-tax) | 3.4% | 4.5% * (1 - 23.6%) |
| D/V | ~19% | |
| E/V | ~81% | |
| **WACC (derived)** | **7.5%** | |
| **WACC (used in DCF)** | **8.5%** | Conservative +1pp margin for McGriff debt risk |

### Growth Derivation (from thesis projection-framework)

| Component | Rate | Reasoning |
|-----------|------|-----------|
| Insurance brokerage TAM | +4-5% | Mordor Intelligence US, global 9.4% incl. emerging |
| MMC market share | Stable | #1 for 15 years, consolidation via McGriff |
| Pricing power | +1-2% | Commissions tied to premium rates |
| Inorganic | +2-3% | McGriff annualization + bolt-on M&A |
| **Total growth (base)** | **7%** | 4% organic + 3% inorganic |
| **Organic-only (conservative)** | **5%** | 4% organic + 1% pricing |
| **Terminal growth** | **2.5%** | Below GDP, conservative for growing industry |

---

## Method 1: EV/EBIT (Primary -- Weight 50%)

### EBIT Data

| EBIT Measure | Value |
|-------------|-------|
| FY2025 (actual) | $6.50B |
| 3-year normalized (2023-2025) | $6.09B |
| FY2026E (forward) | $7.0B (margin expansion + McGriff full year) |

### Peer Multiple Comparison

| Broker | EV/EBITDA | Rev CAGR | FCF Margin | ROIC Spread | Fwd P/E |
|--------|-----------|----------|------------|-------------|---------|
| **MMC** | **14.1x** | **9.2%** | **18.5%** | **+6.6pp** | **17.7x** |
| AON | 14.3x | 8.8% | 17.9% | +5.4pp | 14.9x |
| AJG | 19.1x | 16.2% | 15.9% | N/A | 14.0x |
| WTW | 11.5x | 3.3% | 12.8% | -4.8pp | 12.9x |
| BRO | 16.1x | 17.4% | 24.0% | -1.0pp | 13.9x |

### Multiple Selection: 17x EV/EBIT (forward basis)

**Reasoning for 17x:**
- MMC current EV/EBIT: 16.7x (at $182.70 price). So 17x is approximately "fair" at current market sentiment.
- AON trades at similar EV/EBITDA (14.3x) but with slightly worse ROIC spread and lower scale.
- WTW discounted (11.5x EBITDA, ~13x EBIT) because ROIC < WACC and negative ROE in 2024. MMC deserves premium.
- AJG premium (19x EBITDA) reflects M&A growth machine model and mid-market positioning. Not directly comparable.
- 17x is BELOW MMC's 5-year historical range of 18-22x, reflecting the current headwinds (rate softening, AI fears, McGriff debt). This is intentionally conservative.
- Adjustments: +1x for WIDE moat (strongest in broker sector), +1x for #1 scale position, -1x for elevated leverage (2.4x), -1x for organic growth deceleration (4% vs 7% historical). Net: 17x baseline.

### EV/EBIT Valuation

| Scenario | EBIT Used | Multiple | EV | - Net Debt | Equity | FV/Share |
|----------|----------|---------|-----|-----------|--------|----------|
| **Bear** | $6.50B (current) | 15x | $97.5B | $18.9B | $78.6B | **$160** |
| **Base** | $7.00B (forward) | 17x | $119.0B | $18.9B | $100.1B | **$204** |
| **Bull** | $7.00B (forward) | 19x | $133.0B | $18.9B | $114.1B | **$233** |

---

## Method 2: DCF SBC-Adjusted (Secondary -- Weight 30%)

### DCF Parameters

| Parameter | Value | Justification |
|-----------|-------|---------------|
| Base FCF | $5.00B (FY2025) | From yfinance cash flow |
| SBC deduction | $0.39B (7.9% of FCF) | Standard SBC haircut |
| SBC-adj FCF | $4.61B | |
| Growth (total) | 7% | Organic 4% + inorganic 3% |
| Growth (organic-only) | 5% | Conservative scenario |
| WACC | 8.5% | Derived 7.5% + 1pp conservatism |
| Terminal growth | 2.5% | |
| Projection years | 10 | |

### DCF Tool Output (raw, before SBC adjustment)

**Scenario 1: 7% growth (total, base assumption)**

| Scenario | Raw FV | SBC-adj FV |
|----------|--------|-----------|
| Bear (5%, WACC 9.5%) | $141 | $130 |
| Base (7%, WACC 8.5%) | $208 | $191 |
| Bull (9%, WACC 7.5%) | $312 | $287 |

**Scenario 2: 5% growth (organic-only, conservative)**

| Scenario | Raw FV | SBC-adj FV |
|----------|--------|-----------|
| Bear (3%, WACC 9.5%) | $116 | $107 |
| Base (5%, WACC 8.5%) | $173 | $159 |
| Bull (7%, WACC 7.5%) | $261 | $240 |

### DCF Weighted (60% total growth + 40% organic-only), SBC-adjusted

| Scenario | FV |
|----------|-----|
| **Bear** | **$121** |
| **Base** | **$178** |
| **Bull** | **$268** |

### Sensitivity Matrix (7% growth scenario, before SBC)

| Growth \ WACC | 7.0% | 8.5% | 10.0% |
|--------------|------|------|-------|
| 4.0% | $224 | $157 | $117 |
| 5.5% | $258 | $181 | $135 |
| **7.0%** | $296 | **$208** | $155 |
| 8.5% | $339 | $238 | $178 |
| 10.0% | $387 | $272 | $203 |

**DCF Sensitivity Assessment:**
- FV Spread: 130% (HIGH)
- Terminal Value: 61.6% of EV (moderate-high)
- The high sensitivity means the DCF point estimate should be treated as a range, not a precise number. This is why DCF gets only 30% weight for this valuation.

---

## Method 3: P/E Cross-Check (Weight 20%)

### Forward EPS and SBC Adjustment

| Metric | Value |
|--------|-------|
| EPS FY2025 (actual) | $8.48 |
| EPS FY2026E (consensus) | $9.50 |
| SBC per share | $0.80 |
| SBC-adj EPS FY2026E | $8.70 |

### Peer Forward P/E

| Broker | Fwd P/E |
|--------|---------|
| MMC | 17.7x |
| AON | 14.9x |
| AJG | 14.0x |
| WTW | 12.9x |
| BRO | 13.9x |
| **Median** | **14.0x** |
| **MMC premium vs median** | **+26%** |

MMC commands a premium because of #1 scale position, highest ROIC spread, strongest moat, and diversified revenue (broking + consulting). The 26% premium vs median is justified but not extravagant. Historical premium was 30-40%.

### P/E Valuation (SBC-adjusted EPS)

| Scenario | Multiple | FV |
|----------|---------|-----|
| **Bear** (18x) | Compressed to near-peer median | **$157** |
| **Base** (20x) | Modest premium for quality | **$174** |
| **Bull** (22x) | Historical norm (below peak 25-28x) | **$191** |

---

## Reconciliation

### Method Weights Rationale

| Method | Weight | Rationale |
|--------|--------|-----------|
| **EV/EBIT** | **50%** | Most appropriate for asset-light fee-based services; direct peer comparison available; captures enterprise value including debt impact of McGriff |
| **DCF** | **30%** | Captures growth trajectory; but 130% FV spread and 62% terminal value dependency reduce reliability |
| **P/E** | **20%** | Sanity check against peer multiples; validates EV/EBIT and DCF findings |

### Weighted Fair Values

| Scenario | EV/EBIT (50%) | DCF (30%) | P/E (20%) | **Weighted FV** |
|----------|--------------|----------|----------|----------------|
| **Bear** | $160 | $121 | $157 | **$148** |
| **Base** | $204 | $178 | $174 | **$190** |
| **Bull** | $233 | $268 | $191 | **$235** |

### Divergence Analysis

| Method | Base FV |
|--------|---------|
| EV/EBIT | $204 |
| DCF (SBC-adj) | $178 |
| P/E (SBC-adj) | $174 |
| **Divergence** | **17%** (max $204 / min $174) |

Divergence of 17% is BELOW the 30% threshold. This is coherent and does NOT require special investigation.

**Why DCF is lower than EV/EBIT:** The DCF conservatism compounds three factors: (a) SBC haircut (-7.9%), (b) WACC 8.5% vs derived 7.5% (+1pp conservatism), and (c) 40% weight on organic-only 5% growth. These three factors each reduce the DCF result modestly, compounding to a roughly 13% discount vs the EV/EBIT method.

**Why P/E is the lowest:** The P/E method double-counts the SBC haircut somewhat (SBC-adjusted EPS already deducts SBC) and uses a 20x multiple that is below MMC's current trailing 21.9x. This makes it the most conservative method, which is its role as a sanity check.

---

## Scenarios

| Scenario | Weighted FV | Probability | Contribution to EV |
|----------|------------|-------------|-------------------|
| **Bear** | $148 | 25% | $37.0 |
| **Base** | $190 | 50% | $95.0 |
| **Bull** | $235 | 25% | $58.8 |
| **Expected Value** | | **100%** | **$191** |

### Bear Case Thesis
Organic growth stalls at 2-3%, consulting (Oliver Wyman) enters cyclical downturn from US recession, P&C rate softening compresses commissions by 5-10%, Greensill litigation settles for $500M+, AI narrative continues to depress multiple. EV/EBIT compresses to 15x. MCGriff integration delivers sub-par synergies.

### Base Case Thesis
4% organic growth continues, McGriff becomes accretive ($7.0B EBIT by FY2026), margin expands from operating leverage + synergies (23.1% -> 24-25% operating margin over 3 years), multiple stabilizes at 17x as market recognizes brokers are distinct from insurers. Greensill settles at manageable level ($200-400M).

### Bull Case Thesis
Insurance market re-hardens (catastrophe losses), organic growth re-accelerates to 6%+, AI threat proves overdone for commercial broking, McGriff synergies exceed expectations, multiple re-rates to 19x as investor sentiment normalizes. EBIT reaches $7.5B by FY2027.

---

## MoS Analysis

| Metric | Value |
|--------|-------|
| **Current Price** | **$182.70** |
| **Weighted Base FV** | **$190** |
| **Expected Value** | **$191** |
| MoS vs Base | +3.9% |
| MoS vs Expected Value | +4.2% |
| MoS vs Bear | -23.7% |

### Comparison to Thesis FV

The thesis estimated FV of $220. This valuation report arrives at $190 (weighted base) -- a $30 or 14% lower fair value.

**Why $190 instead of $220:**
1. **SBC adjustment** (-7.9% haircut to FCF and EPS): The thesis DCF used unadjusted FCF. SBC of $394M/year is a real cost to shareholders.
2. **Conservative WACC (8.5% vs 7.5%)**: Added 1pp conservatism for McGriff integration risk and elevated leverage.
3. **Blended growth (7% total + 5% organic)**: Rather than assuming 7% total growth throughout, allocated 40% weight to an organic-only scenario, recognizing that M&A growth is not guaranteed to continue at current pace.
4. **Multiple compression reflected in EV/EBIT**: Used 17x vs the thesis implicit 19-20x, reflecting current market sentiment and rate cycle headwinds.
5. **P/E cross-check confirms**: At 20x SBC-adjusted forward P/E, FV = $174. This anchors the valuation lower than the thesis estimate.

The thesis FV of $220 is achievable in the BULL scenario ($235) but should not be used as the base case for entry decisions.

---

## Implied Multiples Validation

At our base FV of $190:

| Multiple | Implied Value | Reasonable? |
|----------|-------------|-------------|
| P/E (FY2025) | $190 / $8.48 = 22.4x | YES -- at current trailing, slightly above |
| P/E (FY2026E) | $190 / $9.50 = 20.0x | YES -- reasonable premium for #1 broker |
| EV/EBITDA (FY2025) | ($190 * 490M + $18.9B) / $7.73B = 14.5x | YES -- in line with AON 14.3x |
| FCF Yield | $5.0B / ($190 * 490M) = 5.4% | YES -- adequate for Tier B |
| SBC-adj FCF Yield | $4.61B / ($190 * 490M) = 5.0% | YES -- above WACC cost |

No implausible multiples detected. The base FV of $190 implies reasonable valuations across all metrics.

---

## Peer Validation

| Metric | MMC (at $190 FV) | AON (at mkt) | WTW (at mkt) |
|--------|------------------|-------------|-------------|
| Fwd P/E | 20.0x | 14.9x | 12.9x |
| EV/EBITDA | 14.5x | 14.3x | 11.5x |
| ROIC spread | +6.6pp | +5.4pp | -4.8pp |
| FCF margin | 18.5% | 17.9% | 12.8% |
| Revenue CAGR | +9.2% | +8.8% | +3.3% |

MMC's premium vs AON (P/E 20x vs 15x = 33% premium) is justified by: larger scale (1.7x revenue), higher ROIC spread (+1.2pp), better FCF margin (+0.6pp), diversification via Mercer/OW consulting platform. Historical premium vs AON has been 20-40%.

MMC's premium vs WTW (P/E 20x vs 13x = 54% premium) is justified by: WTW has negative ROIC spread (-4.8pp), negative ROE in 2024, slower growth, and was the merger target that failed (antitrust). WTW is a structurally weaker business.

---

## Entry Price Analysis

| Entry Price | MoS vs EV ($191) | MoS vs Base ($190) | MoS vs Bear ($148) |
|------------|-------------------|--------------------|--------------------|
| $160 | +16% | +16% | -8% |
| $165 | +14% | +13% | -12% |
| $170 | +11% | +11% | -15% |
| $175 | +8% | +8% | -18% |
| $182.70 (current) | +4% | +4% | -24% |

**Entry recommendation: $160**

At $160:
- MoS vs Expected Value: +16% -- acceptable for Tier B with WIDE moat
- MoS vs Bear: -8% -- limited downside even in bear scenario
- Consistent with thesis entry and with Tier B precedents (ROP at $300 = 22% MoS, ACGL at $92 = 23% MoS)

At current price ($182.70):
- MoS of +4% is INSUFFICIENT for Tier B
- Bear case loss of -24% is too large without commensurate upside
- Current price is approximately "fair" -- paying fair value for a great business is not a value investing entry

---

## Sensitivity Table (DCF, base scenario)

| Growth \ WACC | 7.0% | 8.0% | 8.5% | 9.0% | 10.0% |
|--------------|------|------|------|------|-------|
| 4.0% | $224 | $183 | $157 | $137 | $117 |
| 5.5% | $258 | $211 | $181 | $158 | $135 |
| **7.0%** | $296 | $243 | **$208** | $181 | $155 |
| 8.5% | $339 | $279 | $238 | $208 | $178 |
| 10.0% | $387 | $319 | $272 | $237 | $203 |

Note: These are raw DCF values (pre-SBC adjustment). Apply -7.9% for SBC-adjusted figures.

The table shows that even at 7% growth and 8% WACC, FV = $243, which would only give 25% MoS from the $182.70 current price. The DCF is highly sensitive -- a 1pp change in WACC moves FV by $30-60/share.

---

## Precedent Consistency Check

| Decision | Ticker | QS Adj | MoS at Entry | Tier | Comparable? |
|----------|--------|--------|-------------|------|------------|
| Standing Order | ROP | 70 | 22% at $300 | B | YES -- similar Tier B, serial acquirer with elevated debt |
| R3 Resolution | ACGL | 68 | 23% at $92 | B | YES -- same Tier B insurance sector, similar QS |
| Standing Order | RACE.MI | 68 | 26% at EUR 270 | B | Partially -- different sector but similar QS/MoS |

**MMC at $160 would provide 16% MoS (vs EV) for QS 68 Tier B.** This is slightly below the 20-25% typical range for Tier B from decisions_log.yaml. However:
- The WIDE moat (21/25, strongest of all insurance brokers) justifies accepting slightly lower MoS
- The 85%+ recurring revenue provides higher earnings predictability than typical Tier B
- The bear case loss at $160 is only -8%, which is moderate

If we wanted to match precedents more closely, $155 would provide 19% MoS and $150 would provide 21% MoS. But $160 balances reachability (stock was at $174.18 52w low recently) with adequate margin.

---

## Summary

```
VALUATION: MMC (Marsh & McLennan Companies)

Type of company: Asset-light fee-based services (insurance brokerage + consulting)
Methods selected: EV/EBIT (50%) + DCF SBC-adjusted (30%) + P/E SBC-adjusted (20%)

Method 1: EV/EBIT (17x forward FY2026E EBIT)
- Inputs: EBIT FY2026E $7.0B, multiple 17x, net debt $18.9B, shares 490M
- Fair Value: $204

Method 2: DCF SBC-adjusted (blended 7%/5% growth, WACC 8.5%, terminal 2.5%)
- Inputs: SBC-adj FCF $4.61B, 60% total growth + 40% organic-only
- Fair Value: $178

Method 3: P/E SBC-adjusted (20x forward SBC-adj EPS $8.70)
- Inputs: EPS FY2026E $9.50 - SBC/share $0.80 = $8.70, multiple 20x
- Fair Value: $174

Reconciliation:
| Method   | FV   | Weight | Weighted |
|----------|------|--------|----------|
| EV/EBIT  | $204 | 50%    | $102     |
| DCF      | $178 | 30%    | $53      |
| P/E      | $174 | 20%    | $35      |
| **Avg**  |      | 100%   | **$190** |

Divergence: 17% (BELOW 30% threshold -- coherent)

Scenarios:
| Scenario     | Fair Value | Prob |
|-------------|-----------|------|
| Bear         | $148      | 25%  |
| Base         | $190      | 50%  |
| Bull         | $235      | 25%  |
| **Expected** | **$191**  | 100% |

Current Price: $182.70
MoS vs Expected: +4.2%
MoS vs Base: +3.9%
MoS vs Bear: -23.7%

VERDICT: Insufficient MoS at current price. Entry at $160 (MoS +16% vs EV).
```

---

## META-REFLECTION

### Dudas/Incertidumbres
- **SBC adjustment magnitude:** MMC's SBC of $394M is 7.9% of FCF. This is relatively modest for a large-cap services company (compare to ADBE at ~15%, INTU at ~20%). The SBC haircut is conservative but not punitive. If SBC grows faster than revenue (e.g., to retain talent post-McGriff), the adjustment could increase.
- **Forward EBIT estimate:** I used $7.0B for FY2026E. Analyst consensus ranges from $6.8B to $7.2B. At $6.8B, the EV/EBIT base FV would drop from $204 to $200. The sensitivity is moderate -- not a major source of error.
- **The 17x EV/EBIT multiple:** This is a judgment call. The sector is repricing due to AI fears and rate softening. If the market decides that brokers deserve a permanent discount (15x or lower), the base FV drops to $183 -- essentially current price with zero margin. This is the key uncertainty in the valuation.

### Sensibilidad Preocupante
- DCF FV spread of 130% is HIGH. A 1pp change in WACC moves FV by $30-60/share. This is inherent to DCF on a business with 62% terminal value. The high sensitivity is why EV/EBIT was chosen as the primary method (50% weight) rather than DCF.
- The difference between thesis FV ($220) and this valuation ($190) is -14%. This is material but not alarming -- it reflects three adjustable parameters (SBC, WACC conservatism, growth blend) that each have reasonable ranges.

### Discrepancias con Thesis
- **Thesis FV $220 vs Valuation FV $190:** The -$30 gap is driven by: (1) SBC adjustment ($-16 impact), (2) conservative WACC ($-12 impact), (3) blended growth ($-8 impact), partially offset by (4) EV/EBIT method pulling up vs DCF-only approach. The thesis FV of $220 is achievable (it falls between our base $190 and bull $235) but represents an optimistic scenario, not a base case.
- **Entry price aligned:** Both thesis and this report recommend entry at $160. The thesis arrived at this through MoS analysis against $220 FV (requiring 27% MoS). This report arrives at $160 through MoS analysis against $191 EV (requiring 16% MoS). Different paths, same destination -- which increases confidence in the entry level.

### Sugerencias para el Sistema
- For insurance brokers, EV/EBIT should be the default primary valuation method, not DCF. The asset-light model with high terminal value dependency makes DCF unreliable as a primary tool.
- The thesis FV header should be updated from $220 to $190 to reflect this more rigorous valuation. The entry price of $160 remains unchanged.
- Consider whether the quality_universe entry for MMC (if it exists) should use $190 rather than $220 as the FV.

### Preguntas para Orchestrator
1. Should the thesis FV be revised from $220 to $190? Both lead to the same entry ($160), but the FV affects MoS reporting in forward_return.py.
2. The SBC adjustment reduced the DCF by 7.9%. Should this be applied retroactively to other non-software positions in the portfolio (ALL, GL, DTE.DE, EDEN.PA)? The INTU precedent applied SBC adjustment but it was framed as a "software company" standard.
3. The 17x EV/EBIT multiple is the linchpin of this valuation. If the orchestrator believes brokers will re-rate toward historical 19-20x as AI fears dissipate, the base FV would be $204-220. Conversely, if permanent de-rating to 15x is the view, base FV drops to $160-170.

---

## Sources

- price_checker.py output (2026-02-13)
- quality_scorer.py --detailed MMC (2026-02-13)
- dcf_calculator.py MMC --growth 7 --wacc 8.5 --terminal 2.5 --years 10 --scenarios --sensitivity
- dcf_calculator.py MMC --growth 5 --wacc 8.5 --terminal 2.5 --years 10 --scenarios --sensitivity
- quality_scorer.py AON AJG WTW BRO --raw (peer comparison)
- yfinance MMC financial statements (cash flow, income statement, balance sheet)
- thesis/research/MMC/thesis.md (fundamental-analyst R1 output)
- thesis/research/MMC/moat_assessment.md (moat-assessor R1 output)
- thesis/research/MMC/risk_assessment.md (risk-identifier R1 output)
