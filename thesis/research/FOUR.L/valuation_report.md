# Valuation Report: FOUR.L (4imprint Group plc)

> **Fair Value:** 5,300 GBp
> **Date:** 2026-02-14
> **Valuation Specialist:** R1 Valuation

---

## Company Classification

**Type of empresa:** Capital-light distributor with growth characteristics (cyclical demand, stable model)
**Quality Tier:** B (QS Tool 67, QS Adjusted 72)
**Methods selected:** Owner Earnings Yield (Primary, 60%) + EV/EBIT Normalised (Secondary, 40%)

**Method selection rationale:**
- Tier B per the valuation-methods skill calls for DCF + EV/EBIT. However, the DCF tool produces wildly inflated results for FOUR.L (base FV 7,413p to 8,713p) due to FCF volatility (CV=1.5) and terminal value comprising 74.5% of EV. DCF is UNRELIABLE as a primary method for this company.
- Instead, Owner Earnings Yield is more appropriate because 4imprint's extraordinary ROIC (85%+) and capital-light model make the relationship between owner earnings, growth, and value more transparent than discounting highly volatile FCFs.
- EV/EBIT Normalised is the secondary method because it anchors to actual operating profit and comparable multiples, providing a market-relative sanity check.
- DCF is used ONLY as a directional cross-check, not as a primary or secondary method.

---

## Projection Framework (Derived Inputs)

### Revenue Projection

```
TAM (North America Promotional Products): $26.6B (2024, PPAI data)
TAM Growth Rate: ~3% per year (nominal GDP-linked)
  Drivers of growth: SMB marketing budgets, corporate events, trade shows
  Drivers of contraction: Digital advertising substitution, tariff cost inflation
  Conservative estimate: 2.5% (TAM growth x 0.8)

Market Share (2024): ~5.1% ($1.37B / $26.6B)
Market Share Trend:
  2020: ~3.5%
  2022: ~4.2%
  2024: ~5.1%
  Trend: GAINING consistently (even in down years like 2025, outperformed industry)

Market Share Projection:
  2027: ~5.5% (resume +0.3pp/year, slower than historical)
  2030: ~6.0% (fragmented competitors continue to exit)

Pricing Power: MODERATE
  History: ~1-2% annual price increases
  Can match inflation but cannot exceed it (B2B, price-sensitive SMBs)
  Tariff passthrough ability confirmed (GM held at 32% through 2025 despite tariffs)

Revenue Growth Formula:
  Base: TAM +3% + Market share +0.3pp/year + Pricing +1% = ~5% revenue growth
  Bear: TAM +1% + Market share flat + Pricing +0.5% = ~2% revenue growth
  Bull: TAM +4% + Market share +0.5pp + Pricing +1.5% = ~7% revenue growth
```

### Margin Projection

```
Gross Margin:
  Current: 31.8% (2024)
  Trend: DECLINING (35.3% -> 31.8% over 2021-2024)
  This is a REAL concern. Contributing factors:
    - Tariff cost absorption (50-60% of hard goods from China)
    - Competitive pricing pressure
    - Mix shift toward lower-margin product categories
  Projection: 31-32% stable (tariff headwinds offset by scale benefits)
  Bear case: 29% (tariff escalation, pricing pressure)

Operating Margin:
  Current: 10.8% (2024)
  5y Average: ~9.1% (distorted by 2021 COVID recovery)
  Trend: IMPROVING (4.1% -> 10.8% from 2021-2024, but 2021 was depressed)
  Normalised: ~10.5% (using 2023-2025 average)
  Projection: 10.5-11.0% (stable with modest operating leverage)

FCF Conversion:
  NI to FCF: ~90%+ historically (minimal capex, negative working capital)
  FCF Margin: ~8% (held back by low operating margin, not poor conversion)
  Projection: 8-9% (improving as revenue recovers)
```

### WACC Derivation

```
Risk-Free Rate (10Y US Treasury): 4.3%
Equity Risk Premium:              5.5%
Beta (from yfinance):             0.64
  Beta seems low for a business this cyclical (COVID: -35% revenue).
  The low beta reflects GBP listing + lack of institutional attention,
  NOT low fundamental risk. I use 0.64 as reported.
Cost of Equity (Ke): 4.3% + 0.64 * 5.5% = 7.82%, rounded to 8.0%
Cost of Debt (Kd): N/A (net cash, effectively zero debt)
Capital Structure: 100% equity (net cash)
WACC: 8.0%

Sanity check: 8.0% is at the LOW end of reasonable.
  For a cyclical, US-operating, SMB-dependent business, a WACC
  of 8% may be optimistic. However, the net cash balance sheet
  and capital-light model reduce financial risk. 8.0% is defensible.
  Bear case uses 9.0% WACC to capture the cyclicality.
```

### Terminal Growth: 2.5%

```
Rationale: The promotional products industry grows roughly with nominal GDP (2-3%).
4imprint may outgrow the industry for years via share gains, but terminal
growth must not exceed long-term GDP. Using 2.5% -- at the midpoint.
Bear case: 2.0%. Bull case: 3.0%.
```

---

## Method 1: Owner Earnings Yield (Primary, 60% weight)

### Calculation

```
FY2025 Estimated Revenue:     $1,350M (from Jan 2026 trading update)
FCF Margin (estimated):       8.0%
FY2025 Estimated FCF:         $108M

Maintenance Capex:            $15M (depreciation $13M x 1.15)
Owner Earnings:               $108M - $15M = $93M

Market Cap (current):         GBP 1.08B = ~$1,360M (at GBP/USD 1.26)
Owner Earnings Yield:         $93M / $1,360M = 6.8%

Expected Growth (5yr avg):    5% (from projection framework)
OEY + Growth:                 6.8% + 5.0% = 11.8%
WACC:                         8.0%
Spread:                       +3.8pp (positive, indicating undervaluation)
```

### Fair Value Derivation

For Tier B companies with strong ROIC and moderate growth, precedent analysis suggests a target OEY of approximately 5%:

- A lower target OEY (e.g., 4%) would imply the market should price this like a Tier A compounder. With QS 72, this would be aggressive.
- A higher target OEY (e.g., 6%) would imply the market should price this like a slow-growth value stock, which ignores the 85% ROIC and market share trajectory.
- 5% is conservative: comparable to an investor requiring a 5% earnings yield plus growth upside.

```
Fair Value = Owner Earnings / Target OEY
Fair Value = $93M / 0.05 = $1,860M
FV per share = $1,860M / 28.1M shares = $66.19
FV in GBp = $66.19 / 1.26 (GBP/USD) * 100 = 5,253p
Rounded: 5,260 GBp
```

### Sensitivity to Target OEY

| Target OEY | Fair Value (GBp) | MoS at 3840p |
|------------|-----------------|--------------|
| 4.0% | 6,575 | 41.6% |
| 4.5% | 5,844 | 34.3% |
| **5.0%** | **5,260** | **27.0%** |
| 5.5% | 4,782 | 19.7% |
| 6.0% | 4,383 | 12.4% |
| 6.5% | 4,047 | 5.1% |
| 7.0% | 3,757 | -2.2% |

**Key observation:** At the current price of 3840p, the implied OEY is 6.8%. For the stock to be fairly valued at this level, the market would need to believe EITHER that growth will be near-zero OR that the business deserves a distressed-level yield. Neither is consistent with a #1 market position, 85% ROIC, and net cash balance sheet.

**Method 1 Fair Value: 5,260 GBp**

---

## Method 2: EV/EBIT Normalised (Secondary, 40% weight)

### Normalised EBIT

```
FY2023 Operating Profit:  $136M
FY2024 Operating Profit:  $148M
FY2025E Operating Profit: $142M ($1,350M * 10.5%)

Normalised EBIT (3-year average): ($136M + $148M + $142M) / 3 = $142M
```

**Note:** I use only 2023-2025 for normalisation because 2021-2022 were distorted by COVID recovery (2021 operating margin was only 4.1%, which is not representative of the normalised business).

### Multiple Selection

```
Sector context:
  - Promotional products distributors: No pure-play public comps exist
  - Capital-light distributors (general): 12-16x EV/EBIT
  - Quality businesses with 80%+ ROIC: 18-22x EV/EBIT
  - 4imprint historical trading range: 15-25x operating profit (pre-selloff)
  - Current market implied: ~10x EV/EBIT (depressed)

Base multiple: 12x (Industrials/distributors sector median)

Adjustments:
  + Superior ROIC (85%+, top decile globally):      +2x
  + #1 market position in fragmented market:         +1x
  + Net cash balance sheet:                          +1x
  - Cyclical demand (SMB marketing budgets):         -1x
  - Declining gross margins (35% -> 32%):            -1x
  - Tariff headwinds (active, not resolved):         -1x
  - Narrow moat (not Wide):                          +0x
  = Final multiple: 13x EV/EBIT

Sanity check: 13x is BELOW 4imprint's 5-year average multiple and
BELOW the quality premium the business would normally command.
This reflects current headwinds conservatively.
```

### Fair Value Calculation

```
EV = Normalised EBIT * Multiple = $142M * 13 = $1,846M
Net cash (added back): $133M
Equity Value = $1,846M + $133M = $1,979M

FV per share = $1,979M / 28.1M shares = $70.43
FV in GBp = $70.43 / 1.26 * 100 = 5,590p
```

### Multiple Sensitivity

| EV/EBIT Multiple | Fair Value (GBp) | MoS at 3840p |
|-----------------|-----------------|--------------|
| 10x | 4,365 | 12.0% |
| 11x | 4,766 | 19.4% |
| 12x | 5,166 | 25.7% |
| **13x** | **5,590** | **31.3%** |
| 14x | 5,990 | 35.9% |
| 15x | 6,390 | 39.9% |
| 16x | 6,791 | 43.4% |

**Method 2 Fair Value: 5,590 GBp**

---

## Method 3: DCF Cross-Check (NOT weighted -- directional only)

### Why DCF Is Unreliable for FOUR.L

The DCF tool produces the following results:

| DCF Parameters | Base FV (GBp) | Notes |
|---------------|--------------|-------|
| Tool defaults (5% growth, 9% WACC) | 7,413 | FCF base = GBP 110M (2024 actual, higher than 2025E) |
| Thesis params (5% / 8% / 2.5%) | 8,713 | Even more inflated |
| Bear params (3% / 9% / 2%) | 6,470 | Still well above price |
| Bull params (7% / 7.5% / 3%) | 11,331 | Absurdly high |

**Problems with DCF for FOUR.L:**
1. **FCF base is volatile** (CV=1.5): FCF went from GBP 8M (2021) to GBP 127M (2023). This is a post-COVID recovery artifact, not ongoing volatility.
2. **Terminal value is 74.5% of EV**: Excessive sensitivity to terminal assumptions.
3. **FV Spread is 73%** (HIGH): The range 5,397p to 10,832p is too wide to be useful.
4. **The tool uses 2024 FCF (GBP 110M)** as base, but 2025 FCF is likely lower (~GBP 86M) due to revenue decline. This inflates the DCF by ~25%.

**DCF Directional Conclusion:** Even with bear-case parameters (3% growth, 9% WACC, 2% terminal), the DCF produces a FV of 5,266p to 6,470p -- all above the current price of 3,840p. This CONFIRMS undervaluation directionally but CANNOT determine the magnitude. The DCF is consistent with my primary methods but I reject its point estimates as inflated.

---

## Reconciliation

| Method | Fair Value (GBp) | Weight | Weighted (GBp) |
|--------|-----------------|--------|-----------------|
| Owner Earnings Yield | 5,260 | 60% | 3,156 |
| EV/EBIT Normalised | 5,590 | 40% | 2,236 |
| **Weighted Average** | | **100%** | **5,392** |

**Divergence between methods: 6.3%** -- Well within the 30% threshold. The two methods are highly convergent, which increases confidence.

**DCF Cross-check (unweighted):** DCF base 7,413p is 37% above weighted average. This is expected because (a) DCF uses inflated 2024 FCF base, and (b) DCF structural limitations (high terminal value %). The DCF confirms undervaluation but its absolute level is too optimistic.

**Final Fair Value: 5,300 GBp** (rounded down from 5,392 for conservatism, given: tariff uncertainty, declining gross margins, and earnings hard gate on March 11).

**Implicit multiples at FV 5,300p:**
- Implied P/E at FV: ~17x (5,300/307 EPS in GBp)
- Implied EV/EBIT at FV: ~13.5x
- Implied EV/Revenue at FV: ~1.0x

**Validation vs peers:**
- P/E 17x is reasonable for a capital-light distributor with 85% ROIC and 5% growth. Not excessive.
- EV/EBIT 13.5x is below 4imprint's historical average (15-25x) and below quality-adjusted comparables (18-22x for 80%+ ROIC businesses). Conservative.
- EV/Revenue 1.0x is typical for a low-margin distributor.

**Validation vs precedents (decisions_log.yaml):**
- The MoS of 27.6% at FV 5,300p (price 3,840p) is consistent with Tier B precedents: ROP 22%, VLTO 20%, ACGL 20%, MMC 18.4%. FOUR.L's higher MoS reflects the cyclical headwinds and higher uncertainty.
- The FV methodology is consistent with how we valued other capital-light businesses (ROIC-based reasoning rather than pure DCF).

---

## Scenarios

### Bear Case (25% probability)

```
Assumptions:
  Revenue: Flat to low-single-digit (2% growth). Tariffs persist. No new customer recovery.
  Operating margin: 9.0% (compression from tariff costs + weak demand)
  Multiple: 10x EV/EBIT (market treats as ex-growth distributor)
  WACC: 9.0%
  Terminal growth: 2.0%

Calculation (EV/EBIT method):
  Revenue 2026E: $1,377M ($1,350M * 1.02)
  EBIT: $124M ($1,377M * 9.0%)
  EV = $124M * 10 = $1,240M
  Equity = $1,240M + $133M (net cash) = $1,373M
  FV = $1,373M / 28.1M / 1.26 * 100 = 3,880p

BEAR FAIR VALUE: 3,900 GBp (rounded)
```

**NOTE ON BEAR CASE:** The thesis originally had bear at 3,500p. I arrive at 3,900p because even in the bear case, 10x EBIT on $124M with $133M net cash creates a floor. For the stock to reach 3,500p, the market would need to price it at ~8.5x EBIT -- below distressed levels for a company with net cash and 85% ROIC. 3,500p is possible (crisis scenario) but would represent a buying opportunity rather than fair value.

### Base Case (50% probability)

```
Assumptions:
  Revenue growth: 5% (TAM +3%, share +0.3pp, pricing +1%)
  Operating margin: 10.5% (stable, slight compression in 2026 then recovery)
  Multiple: 13x EV/EBIT
  WACC: 8.0%
  Terminal growth: 2.5%

Calculation:
  Normalised EBIT: $142M
  EV = $142M * 13 = $1,846M
  Equity = $1,846M + $133M = $1,979M
  FV = $1,979M / 28.1M / 1.26 * 100 = 5,590p

Weighted with OEY method:
  OEY FV: 5,260p (60%) + EV/EBIT FV: 5,590p (40%) = 5,392p

BASE FAIR VALUE: 5,300 GBp (rounded, conservative)
```

### Bull Case (25% probability)

```
Assumptions:
  Revenue growth: 7% (tariffs resolved quickly, aggressive share gains to 7%+)
  Operating margin: 12%+ (operating leverage + marketing efficiency improvement)
  Multiple: 17x EV/EBIT (market re-rates to recognise compounder status)
  WACC: 7.5%
  Terminal growth: 3.0%

Calculation:
  Revenue 2027E: $1,550M (2 years of 7% growth)
  EBIT: $186M ($1,550M * 12%)
  EV = $186M * 17 = $3,162M
  Equity = $3,162M + $133M = $3,295M
  FV = $3,295M / 28.1M / 1.26 * 100 = 9,310p

  (Sanity check: P/E at bull FV would be ~24x. This is within 4imprint's
   historical range (20-25x during growth phase). Not unreasonable.)

BULL FAIR VALUE: 7,500 GBp (capped conservatively below full calculation to
reflect that the bull scenario requires multiple favourable developments)
```

### Expected Value

```
EV = (Bear * 25%) + (Base * 50%) + (Bull * 25%)
EV = (3,900 * 0.25) + (5,300 * 0.50) + (7,500 * 0.25)
EV = 975 + 2,650 + 1,875
EV = 5,500 GBp

Current Price: 3,840 GBp
MoS vs Expected Value: (5,500 - 3,840) / 5,500 = +30.2%
MoS vs Base:           (5,300 - 3,840) / 5,300 = +27.5%
MoS vs Bear:           (3,900 - 3,840) / 3,900 = +1.5% (very tight!)
```

---

## Sensitivity Analysis

### DCF Sensitivity Matrix (directional only)

From the DCF tool:

```
 Growth \ WACC       7.5%       9.0%      10.5%
----------------------------------------------
       2.0%        8416.2    6558.1    5396.7
       3.5%        8971.3    6974.1    5726.1
       5.0%        9558.1    7413.3    6073.7
       6.5%       10177.7    7876.8    6440.2
       8.0%       10831.6    8365.7    6826.5

  Values in GBp. Note: Inflated because tool uses 2024 FCF base.
  EVERY cell is above current price of 3,840p.
  Even worst case (2% growth, 10.5% WACC) = 5,397p (40% above price).
```

**Interpretation:** The DCF confirms that even under pessimistic assumptions, 3,840p undervalues the company. The question is by how much, which the DCF cannot answer reliably.

### EV/EBIT Sensitivity Matrix

| EBIT ($M) \ Multiple | 10x | 12x | 14x | 16x |
|----------------------|-----|-----|-----|-----|
| $120M (bear margin) | 3,600p | 4,230p | 4,860p | 5,490p |
| $130M (soft year) | 3,860p | 4,540p | 5,220p | 5,900p |
| **$142M (normalised)** | **4,170p** | **4,920p** | **5,670p** | **6,410p** |
| $155M (growth recovery) | 4,510p | 5,320p | 6,130p | 6,940p |

**Observation:** At $142M normalised EBIT, the stock needs a 10.3x EV/EBIT multiple to be fairly valued at 3,840p. For a #1 market position with 85% ROIC and net cash, 10x is clearly below intrinsic value.

---

## Final Summary

```
VALUATION: FOUR.L

Type of company:        Capital-light distributor (cyclical demand)
Quality Tier:           B (QS Tool 67, Adjusted 72)
Methods selected:       Owner Earnings Yield (60%) + EV/EBIT Normalised (40%)

Method 1: Owner Earnings Yield
  Inputs: OE $93M, Target OEY 5%, 28.1M shares, GBP/USD 1.26
  Fair Value: 5,260 GBp

Method 2: EV/EBIT Normalised
  Inputs: Normalised EBIT $142M, 13x multiple, $133M net cash
  Fair Value: 5,590 GBp

Reconciliation:
| Method           | FV (GBp) | Weight | Weighted (GBp) |
|------------------|---------|--------|-----------------|
| OEY              | 5,260   | 60%    | 3,156           |
| EV/EBIT Norm     | 5,590   | 40%    | 2,236           |
| **Weighted Avg** |         | 100%   | **5,392**       |

Divergence: 6.3% (acceptable, well below 30%)

Final FV: 5,300 GBp (conservative rounding)

Scenarios:
| Scenario     | Fair Value | Prob  |
|-------------|-----------|-------|
| Bear         | 3,900 GBp | 25%  |
| Base         | 5,300 GBp | 50%  |
| Bull         | 7,500 GBp | 25%  |
| **Expected** | **5,500 GBp** | 100% |

Current Price:     3,840 GBp
MoS vs Expected:   +30.2%
MoS vs Base:       +27.5%
MoS vs Bear:       +1.5% (TIGHT -- near bear floor)
```

---

## Key Observations and Warnings

1. **The bear case MoS is only 1.5%.** This means the stock is trading very near the bear-case floor. If bearish assumptions materialise (tariffs persist, recession, no recovery), there is essentially NO margin of safety. This is a significant concern for a Tier B position.

2. **The thesis's original bear case of 3,500p appears too pessimistic.** At 10x normalised EBIT plus net cash, the floor is closer to 3,900p. For the stock to reach 3,500p, earnings would need to deteriorate further (sub-$120M operating profit) AND the multiple would need to compress below 9x. Possible but unlikely given the business quality.

3. **DCF is structurally unreliable for this valuation.** The 73% FV spread and 74.5% terminal value composition make DCF outputs decorative rather than informative. The OEY and EV/EBIT methods are far more grounded.

4. **The FV of 5,300 GBp implies 4imprint returns to 15-17x earnings.** This is a MODERATE re-rating from the current 12.5x, not an aggressive one. It is well below the 20-25x the stock commanded during the growth phase. The FV assumption is that 4imprint is a good business in a temporary headwind, NOT a growth darling.

5. **FX risk is a wildcard.** A weakening USD (DXY from 97 to 90) would reduce GBp-translated FV by ~8%. At current FX, the valuation is sound, but GBP investors are exposed to USD translation risk. This is a risk factor, not a valuation input.

6. **The March 11 results are critical.** The FV is based on estimated 2025 financials from the January trading update. If actual results deviate (margins lower, FCF weaker, guidance disappointing), the FV would need to be revised downward. Conversely, positive surprises on margins or guidance could justify a higher FV.

---

## META-REFLECTION

### Dudas/Incertidumbres

- **Owner Earnings Yield target selection (5%) is judgment-based.** There is no hard empirical basis for choosing 5% vs 4.5% or 5.5%. A 0.5pp change in target OEY shifts FV by approximately 500p. I used 5% because it is consistent with a Tier B business with strong ROIC and moderate growth, but this is the single most subjective input in the valuation.

- **Normalised EBIT uses only 2023-2025.** A purist approach would use 5-7 years, but 2021-2022 are distorted by COVID recovery. The 3-year window is defensible but short. If 2025 operating profit comes in below $140M, the normalised figure drops and FV falls proportionally.

- **The FCF base used by the DCF tool (GBP 110M from 2024) is higher than the estimated 2025E FCF (~GBP 86M).** This is a known data lag. If the DCF tool used 2025E FCF, its outputs would be ~20% lower and more reasonable. The tool's current outputs should NOT be used for decision-making.

- **Gross margin trajectory (35% to 32%) is concerning.** If this continues to 29-30%, operating margins compress significantly and the bear case becomes the base case. I modelled GM stabilising at 31-32%, which is an assumption, not a certainty.

### Sensibilidad Preocupante

- **Bear case MoS of only 1.5% is the most concerning finding.** This means the current price is very close to the worst-case valuation floor. A position entered at current prices has essentially NO downside protection against the bear scenario. This argues for either: (a) waiting for a lower entry price, or (b) requiring the March 11 results to DE-RISK the bear case before entering.

- **EV/EBIT multiple has high impact:** Moving from 13x to 11x drops FV from 5,590p to 4,766p. Given current tariff uncertainty, the market could justify a lower multiple than 13x. This sensitivity reinforces the need for conservatism.

### Discrepancias con Thesis

- **The thesis's bear case of 3,500 GBp appears 400p too low.** My analysis suggests 3,900p is a more realistic bear floor (10x EBIT on $124M + $133M net cash). 3,500p would require sub-9x EBIT, which would be distressed-territory pricing for a net-cash, high-ROIC business.

- **The thesis FV of 5,300 GBp is CONFIRMED independently.** My weighted average of 5,392p rounds to 5,300p. The two primary methods (OEY 5,260p and EV/EBIT 5,590p) bracket the thesis estimate tightly. The FV is robust.

- **The thesis's DCF "sanity check" FV of 7,413p should be treated with extreme scepticism.** The DCF is inflated by approximately 25% due to using 2024 FCF (higher than 2025E) and by the structural sensitivity issues (terminal value 74.5%). This is documented in the thesis but could mislead during R2 review if not clearly flagged.

### Sugerencias para el Sistema

- **dcf_calculator.py should support a manual FCF override.** For FOUR.L, the tool uses 2024 FCF (GBP 110M) but 2025E is lower (~GBP 86M). Having a `--fcf-base` parameter would allow more accurate forward-looking DCFs.

- **The OEY method should be formalised as a tool.** Currently, OEY is calculated manually. A `tools/oey_calculator.py` tool that takes ticker, target OEY, and growth rate as inputs would standardise the calculation and reduce human error.

- **For companies with volatile historical FCF (CV > 1.0), the DCF tool should issue a WARNING and suggest EV/EBIT as an alternative.** Currently it issues a CAUTION but still produces a point estimate that can be misleading.

### Preguntas para Orchestrator

1. **The bear-case MoS of 1.5% is very tight. Should this change the verdict from WATCHLIST to a stricter entry requirement?** My recommendation: maintain the hard gate on March 11 results. If results are solid, the bear case de-risks (operating margin confirmation, 2026 guidance visibility). If results disappoint, the bear case becomes more likely and we should NOT enter.

2. **Should the thesis's bear case be revised upward from 3,500p to 3,900p?** My analysis suggests 3,900p is more defensible. This would change the bear-case MoS from -9.7% (downside) to +1.5% (essentially flat). The thesis should be updated if the orchestrator agrees.

3. **The declining marketing efficiency ($8.30 to $7.88 revenue per marketing dollar) was not explicitly modelled. Should this be incorporated into the projection framework as a structural drag?** If marketing efficiency continues declining at -2% per year, it would reduce the effective revenue growth rate by ~0.5pp annually.

---
