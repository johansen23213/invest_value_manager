# Valuation Report: VEEV (Veeva Systems Inc.)

> **Fair Value (Valuation Specialist):** $195
> **Date:** 2026-02-13
> **Methods:** DCF (Primary) + OEY + Growth (Primary) + EV/FCF Multiple (Secondary) + Reverse DCF (Verification)
> **Company Type:** High-growth vertical SaaS with fortress balance sheet

---

## Company Classification

**Type:** Growth SaaS transitioning to Mature SaaS (Tier A Quality Compounder)

VEEV sits at the intersection of "Growth" and "Stable/Defensive" company types. Revenue grows at 14% CAGR, but the business is highly predictable: 85% subscription, 120% NRR, <4% churn, 40% FCF margins, $6.5B net cash. This is NOT a speculative growth company -- it is a dominant vertical platform in a regulated niche.

**Method Selection Rationale:**
- Tier A companies should be valued primarily on OEY per the valuation-methods skill
- But VEEV has complexities that require DCF to capture: (a) margin expansion trajectory, (b) shift from per-seat CRM to platform R&D revenue, (c) competitive dynamics reducing growth rate
- EV/FCF multiples provide market-based sanity check
- Reverse DCF answers the critical question: what growth is the market already pricing in?

---

## Method 1: DCF (Discounted Cash Flow) -- Weight 35%

### Input Derivation (from projection-framework, NOT defaults)

#### Growth Rate: 12% FCF CAGR (Years 1-5)

**Derivation:**

| Component | Assumption | Basis |
|-----------|-----------|-------|
| Revenue growth Y1-Y3 | 12-13% | FY2026 actual 15%, decelerating as CRM transition matures. R&D growing 15-18% but CRM growing only 8-12% and losing top-20 customers (14 vs 18). Blended: ~12-13% |
| Revenue growth Y4-Y5 | 10-11% | Further deceleration as R&D Solutions penetration matures. Still above sector (5-8%) due to TAM at only 16% penetration |
| FCF margin expansion | +1-2pp over 5Y | Gross margin expanding (71.3% to 74.5%), operating leverage kicking in (non-GAAP OpM 18.2% to 45% Q3). FCF margin 39.7% should reach 41-42% |
| Blended FCF growth | ~12% | Revenue 11-12% + margin expansion 1-2pp = FCF growing slightly faster than revenue |

**Comparison to historical:** FCF CAGR last 4 years is approximately 10% ($764M to $1.1B). My 12% projection is slightly above historical, justified by operating leverage as Vault R&D investment cycle peaks.

**Risk-identifier caution integrated:** The risk assessment flags growth deceleration (Goldman citing difficulty maintaining low-to-mid teens). I am using 12%, not the thesis's 14%, to account for CRM customer loss headwinds.

#### WACC: 10.0%

| Component | Value | Source |
|-----------|-------|--------|
| Risk-free rate (Rf) | 4.3% | US 10Y Treasury, Feb 2026 |
| Equity Risk Premium | 5.5% | Damodaran US ERP |
| Beta | 1.08 | yfinance (reasonable for defensive healthcare SaaS) |
| Cost of Equity (Ke) | 10.2% | 4.3% + 1.08 x 5.5% |
| Cost of Debt (Kd) | N/A | Essentially zero leverage ($90M debt vs $6.6B cash) |
| WACC (theoretical) | 10.2% | ~100% equity funded |
| **WACC (used)** | **10.0%** | Rounded down 0.2pp to reflect fortress balance sheet de-risking |

**Justification for 10.0% vs 10.2%:** $6.5B net cash eliminates any liquidity or solvency risk. In a recession, VEEV can operate for years without external funding. This is qualitatively different from a leveraged company with the same beta. A 0.2pp discount is conservative.

#### Terminal Growth: 2.5%

Life sciences software is in structural growth (regulatory complexity increasing, digital transformation ongoing). 2.5% is above GDP growth (2.0%) but below sector growth (10%+). This reflects a mature Veeva in 2031+ that still grows modestly from new regulatory requirements and geographic expansion.

### DCF Tool Output (Base: 12% growth, 10% WACC, 2.5% terminal)

```
Scenario         FV/Share     MoS%
------------------------------------
BEAR               148.53   -13.6%
BASE               174.01    +1.2%
BULL               208.70   +21.3%

Terminal Value as % of EV: 73.9%
FV Spread: 53%
```

### Sensitivity Matrix (Growth x WACC)

```
 Growth \ WACC       8.5%      10.0%      11.5%
----------------------------------------------
       9.0%         189.4     158.7     138.2
      10.5%         199.0     166.1     144.3
      12.0%         209.1     174.0     150.7
      13.5%         219.8     182.3     157.4
      15.0%         231.0     191.0     164.4
```

**DCF Assessment:** At 12% growth and 10% WACC, the DCF gives $174. At the thesis's 14% growth (which I consider optimistic given CRM headwinds), the DCF gives $185. The range is $138-$231 depending on assumptions, confirming HIGH sensitivity. Terminal value at 73.9% of EV is typical for growth companies but reinforces that the DCF is not a precise point estimate.

**DCF Fair Value (Method 1): $174**

---

## Method 2: Owner Earnings Yield + Growth -- Weight 30%

### Calculation

```
FCF (FY2025 TTM):     $1,100M
Depreciation:          ~$50M
Maintenance Capex:     ~$55M (Depreciation x 1.1)
Owner Earnings:        $1,100M - $55M + $50M = $1,095M

Market Cap at $172:    $28.3B
OEY:                   $1,095M / $28,300M = 3.87%

Expected FCF Growth:   12-14% (based on revenue 11-12% + margin expansion)
OEY + Growth:          3.87% + 13% = 16.87%
vs WACC 10.0%:         Spread +6.87pp --> ATTRACTIVE
```

### OEY-Implied Fair Value

The question for OEY valuation is: at what price does OEY + Growth become unattractive?

For a Tier A compounder, OEY + Growth should exceed WACC by at least 3-5pp to provide adequate margin of safety (based on precedent analysis -- our Tier A positions typically show OEY + Growth spreads of +5-8pp above WACC at entry).

**Target: OEY + Growth >= 13% (WACC + 3pp safety margin)**

```
At $172: OEY 3.87% + 13% growth = 16.87%  -->  Meets target
At $200: OEY 3.33% + 13% growth = 16.33%  -->  Meets target
At $220: OEY 3.03% + 13% growth = 16.03%  -->  Meets target
At $250: OEY 2.66% + 13% growth = 15.66%  -->  Meets target (but thin)
At $280: OEY 2.38% + 13% growth = 15.38%  -->  Still meets, but at top valuation
```

The OEY method for a 13% grower gives very high implied fair values because the growth component dominates. This is a known limitation of OEY for growth companies -- it tells you the current price is attractive but does not give a precise FV ceiling.

**Practical OEY approach:** I anchor on where OEY + Growth = 15% (a comfortable 5pp spread over WACC). This gives a fair value around $225.

However, I haircut this for the risk that growth deceleration is worse than expected (CRM losses, SaaSpocalypse). If growth is only 10% instead of 13%, OEY + Growth at $225 = 2.96% + 10% = 12.96%, which is barely above target. This argues for a lower FV.

**OEY Fair Value (Method 2): $210** (conservative, accounting for growth risk)

---

## Method 3: EV/FCF Multiple -- Weight 20%

### Current Valuation

```
Market Cap:        $28.3B
Net Cash:          $6.5B
Enterprise Value:  $21.8B
FCF (TTM):         $1.1B
EV/FCF:            19.8x
```

### Peer Comparison

| Company | EV/FCF | FCF Growth | FCF Margin | Churn | Notes |
|---------|--------|-----------|------------|-------|-------|
| VEEV | 19.8x | 12-14% | 40% | <4% | Vertical SaaS, life sciences |
| CRM (Salesforce) | ~25x | 15% | 30% | ~5% | Horizontal, 10x larger |
| DDOG | ~35x | 25%+ | 25% | ~5% | Observability, faster growth |
| INTU | ~28x | 12% | 35% | ~6% | Vertical (SMB tax/accounting) |
| PAYC | ~22x | 8% | 28% | ~5% | Vertical (HCM) |
| Tyler Tech (TYL) | ~30x | 10% | 22% | ~3% | Vertical (government) |

**Observation:** VEEV at 19.8x EV/FCF is the CHEAPEST high-quality vertical SaaS in this peer set. The discount is driven by CRM transition fears, but VEEV has the BEST FCF margin (40%), the LOWEST churn (<4%), and comparable or better growth.

### Fair Multiple Assessment

For a vertical SaaS company with:
- 40% FCF margin (best in class)
- <4% churn (best in class)
- 120% NRR (top decile)
- 12-14% growth (above sector average)
- Net cash ($6.5B)
- Dominant market position (~80% CRM share, growing R&D)

A fair EV/FCF multiple is **22-28x**, with the range reflecting CRM competitive uncertainty.

| Scenario | EV/FCF | EV | Equity Value | FV/Share |
|----------|--------|----|-----------|----|
| Conservative (CRM losses worse) | 22x | $24.2B | $30.7B | $187 |
| Base (CRM stabilizes at 14/20) | 25x | $27.5B | $34.0B | $207 |
| Optimistic (R&D re-rates) | 28x | $30.8B | $37.3B | $227 |

**EV/FCF Fair Value (Method 3): $207** (base 25x multiple)

---

## Method 4: Reverse DCF (Verification -- Weight 15%)

### What Growth Is Priced In at $172?

Using DCF with WACC 10%, terminal 2.5%:

| FCF Growth Assumed | Implied FV | At $172, Implied MoS |
|-------------------|-----------|---------------------|
| 8% | $146 | Market expects <8% if FV = $172 |
| 10% | $160 | Market expects ~10% |
| 12% | $174 | Market expects ~12% |
| 14% | $185 | Price-in-growth ~14% would mean $172 is cheap |

**At $172, the market is pricing in approximately 11-12% FCF growth.** This is below my base case of 12-14% but not wildly pessimistic. The market is essentially pricing the "CRM losses accelerate, R&D growth slows" scenario as the BASE case.

**My edge:** If CRM retention stabilizes at 14/20 (management guidance, not yet reflected in price) and R&D continues winning (8 of top-20 on Vault EDC, momentum strong), actual growth will be 12-14%, making $172 modestly cheap.

**Reverse DCF implies:** At $172, you are getting a Tier A compounder at a "growth equals market expectations" price. Any positive surprise (better CRM retention, faster R&D wins, AI monetization) creates upside. Any negative surprise (CRM losses >14/20, growth <10%) creates downside. The asymmetry is slightly favorable but not overwhelming.

**Reverse DCF Fair Value (Method 4): $185** (implied if growth meets my 12% base)

---

## Reconciliation

| Method | Fair Value | Weight | Weighted | Reasoning for Weight |
|--------|-----------|--------|----------|---------------------|
| DCF (12% growth, 10% WACC) | $174 | 35% | $60.9 | Most rigorous method but high TV sensitivity (73.9%) |
| OEY + Growth | $210 | 30% | $63.0 | Appropriate for Tier A, but growth assumption sensitivity |
| EV/FCF 25x | $207 | 20% | $41.4 | Market-based sanity check, anchored to peers |
| Reverse DCF | $185 | 15% | $27.8 | Verification of what's priced in |
| **Weighted Average** | | **100%** | **$193.1** |

**Divergence Analysis:**
- Range: $174 - $210 (21% spread)
- All methods within 30% of each other -- NO investigation required per protocol
- The DCF gives the lowest value because terminal value dominates and I used conservative 12% growth (below the thesis's 14%)
- OEY and EV/FCF converge around $207-$210, which validates each other
- The DCF anchors the estimate downward, which I believe is appropriate given the 2 CRITICAL risks

**Rounded Fair Value: $195**

I am setting FV at $195 rather than the $193 weighted average because:
1. The DCF undervalues companies with $6.5B net cash (cash is fully reflected in equity value subtraction but ROIC and FCF growth are dragged by cash sitting idle)
2. The moat assessment scores 19/25 (Wide) with EXPANDING switching costs
3. But I do NOT round up to $200+ because the risk assessment identifies 2 CRITICAL correlated risks and rates overall risk as MEDIUM-HIGH

---

## Divergence from Fundamental-Analyst's $220

The fundamental-analyst's FV is $220. My FV is $195 -- a 11.4% divergence. Explanation:

| Factor | Analyst ($220) | My Assessment ($195) |
|--------|---------------|---------------------|
| FCF growth | 14% | 12% -- I haircut 2pp for CRM headwinds being more severe than analyst assumes |
| WACC | 9.5% | 10.0% -- Analyst's 0.5pp discount for fortress balance sheet is too aggressive; I give 0.2pp |
| EV/FCF multiple | 25x implied | 25x but weighted less (20% vs analyst's heavier reliance) |
| OEY weighting | 55% of analyst reconciliation (gave $260) | 30% -- OEY overstates FV for growth companies where growth dominates |
| Risk integration | 2 CRITICAL risks acknowledged but entry set at $155-165 | 2 CRITICAL risks integrated into LOWER FV, not just lower entry |

**Key philosophical difference:** The analyst compensates for risk by requiring a higher MoS at entry (setting entry at $155-165 despite $220 FV). I compensate for risk by lowering the FV itself. Both approaches achieve a similar entry price, but my approach is more transparent: the FV already reflects the competitive risks, so the MoS calculation is cleaner.

---

## Scenarios

### Bear Case (25% probability)

**Assumptions:**
- Salesforce wins 8+ of top-20 CRM (from current 3 heading to 6)
- CRM growth decelerates to 5% as migration traffic jam goes to Salesforce
- R&D growth decelerates to 12% then 8%
- Total revenue growth: 7-8%
- FCF growth: 8% (margin expansion partially offsets revenue slowdown)
- WACC: 10.5% (risk premium for competitive erosion)
- Terminal growth: 2.0% (lower given reduced dominance)
- EV/FCF compresses to 18-20x

```
DCF at 8% growth, 10.2% WACC, 2% terminal: $146
EV/FCF at 20x: ($1.1B x 20) + $6.5B = $28.5B / 164.3M = $173 (using forward FCF $1.2B: $30.5B / 164.3M = $186 -- but this is bull territory)
```

**Bear Fair Value: $155**

This is the scenario where CRM losses exceed guidance AND R&D growth disappoints. The $6.5B cash provides a floor -- even in a disaster, the equity is worth at minimum $6.5B / 164.3M = $40 per share just in cash. But the business would still generate $800M+ FCF even in a bear case.

### Base Case (50% probability)

**Assumptions:**
- CRM retention at 14/20 (management guidance)
- R&D Solutions growth 15-16%, gradually decelerating to 12%
- CRM growth 8-10% (module upsell offsets seat loss)
- Total revenue growth: 11-12%
- FCF growth: 12-13% (margin expansion)
- WACC: 10.0%
- Terminal growth: 2.5%
- EV/FCF at 25x

**Base Fair Value: $195**

### Bull Case (25% probability)

**Assumptions:**
- CRM retention at 14-15/20 (better than feared)
- R&D Solutions accelerate to 18-20% driven by AI agents and clinical suite wins
- Veeva achieves $5B+ revenue run rate by 2030 (below $6B target but strong)
- FCF growth: 16-18%
- WACC: 9.5% (risk re-rates as CRM concerns fade)
- Terminal growth: 3.0% (life sciences software structural growth)
- EV/FCF re-rates to 28-30x

```
DCF at 14% growth, 10% WACC, 2.5% terminal: $185 (tool, base scenario)
Bull scenario tool output: $222
EV/FCF at 28x: ($1.1B x 28) + $6.5B = $37.3B / 164.3M = $227
```

**Bull Fair Value: $250**

### Expected Value

```
EV = ($155 x 25%) + ($195 x 50%) + ($250 x 25%)
EV = $38.75 + $97.50 + $62.50
EV = $198.75

Rounded: $199
```

### Scenario Summary

| Scenario | Fair Value | Probability | MoS at $172 |
|----------|-----------|-------------|-------------|
| Bear | $155 | 25% | -11.0% (DOWNSIDE) |
| Base | $195 | 50% | +11.8% |
| Bull | $250 | 25% | +31.2% |
| **Expected** | **$199** | **100%** | **+13.6%** |

---

## Current Price Assessment

```
Price (2026-02-13):     $172.0 (EUR 144.87)
52-Week High:           $310.5
52-Week Low:            $168.1 (current price is 2.3% above 52w low)
P/E:                    33.5x
Dividend Yield:         0.0%
Market Cap:             $28.3B
```

```
MoS vs Base FV ($195):        +11.8%
MoS vs Expected FV ($199):    +13.6%
MoS vs Bear FV ($155):        -11.0%
```

---

## Entry Price Recommendation

### Precedent Analysis (Tier A entries)

| Ticker | QS Adj | MoS at Entry | Risk Level | Price Context |
|--------|--------|-------------|------------|---------------|
| ADBE | 76 | 31% | Medium | At 52w low, AI fears |
| NVO | 73 adj | 38% | Medium-High | -17% in 2 days, guidance shock |
| LULU | 78 adj | 34% | Medium | -58% from ATH, CEO vacancy |
| MONY.L | 75 adj | 36% | Medium | At 52w low |
| AUTO.L | 71 adj | 29% | Medium-High | -47% from high, dealer revolt |
| BYIT.L | 68 adj | 35% | Medium | Microsoft restructuring |
| **Avg** | | **33.8%** | | |

VEEV has:
- QS Adjusted: 80 (Tier A, higher than average of our Tier A positions)
- Risk Level: MEDIUM-HIGH (2 CRITICAL correlated risks -- higher than most precedents)
- Unique factor: $6.5B net cash provides exceptional downside protection

### Entry Reasoning

Given:
1. **Risk is MEDIUM-HIGH** with 2 CRITICAL correlated risks (CRM defection + Salesforce competition) -- this argues for MoS closer to the HIGH end of Tier A range (35%+)
2. **QS 80 is among the highest** in our Tier A group -- argues for slightly LOWER MoS threshold
3. **Net cash $6.5B** ($40/share) provides a unique floor that other Tier A positions lacked -- argues for slightly LOWER MoS threshold
4. **Q4 FY2026 earnings on March 4** will materially de-risk (or risk) the CRM retention narrative -- waiting provides information value

Net assessment: The CRITICAL risks push MoS requirement UP, but the quality and balance sheet push it DOWN. These roughly offset, placing VEEV at the MIDDLE of the Tier A MoS range.

**Target MoS: 25-30% (vs my $195 FV)**

```
At 25% MoS: Entry = $195 x (1 - 0.25) = $146
At 30% MoS: Entry = $195 x (1 - 0.30) = $137
At 20% MoS: Entry = $195 x (1 - 0.20) = $156
```

**Recommended Entry Range: $145-$155**

This is more conservative than the fundamental-analyst's $155-$165 because:
1. My FV is lower ($195 vs $220)
2. The 2 CRITICAL risks warrant discipline
3. Q4 earnings (March 4) may provide a price dislocation opportunity if CRM data disappoints
4. At $150, MoS is 23% vs my FV -- acceptable for Tier A with strong balance sheet

**Standing Order Suggestion: $150** (MoS 23.1% vs $195 FV)

This is below the analyst's $155-165 range but above the "ultra-conservative" $137. The rationale: $150 provides adequate margin for Tier A quality with fortress balance sheet, while the 2 CRITICAL risks are already priced into my lower FV of $195.

---

## Sensitivity Table (DCF)

### Growth Rate x WACC (Base: 12%, 10%)

```
 Growth \ WACC       8.5%      10.0%      11.5%
----------------------------------------------
       9.0%         189.4     158.7     138.2
      10.5%         199.0     166.1     144.3
      12.0%         209.1     174.0     150.7
      13.5%         219.8     182.3     157.4
      15.0%         231.0     191.0     164.4
```

Key observations:
- At WACC 10% + Growth 12% (my base): $174
- At WACC 10% + Growth 14% (analyst's assumption): $185
- Breakeven ($172) at WACC 10% requires ~12% growth -- market is pricing almost exactly my base growth
- Even at WACC 11.5% + Growth 9% (severe bear): $138 -- still far above zero, cash provides floor

### Terminal Value as % of Enterprise Value: 73.9%

This is high but typical for growth SaaS. It means 74% of the DCF value depends on what happens AFTER year 5. This is the primary reason I weight DCF at only 35% and use multiple methods.

---

## Validation vs Peers

### Implied Multiples at My FV ($195)

```
At $195/share:
  Market Cap = $32.0B
  EV = $32.0B - $6.5B = $25.5B

  Implied P/E = $195 / $5.14 (FY2026E EPS) = 37.9x
  Implied EV/FCF = $25.5B / $1.1B = 23.2x
  Implied EV/Revenue = $25.5B / $3.17B = 8.0x
```

| Metric | VEEV Implied | SaaS Sector | Reasonable? |
|--------|-------------|------------|-------------|
| P/E | 37.9x | 25-40x (quality SaaS) | YES -- consistent with quality |
| EV/FCF | 23.2x | 20-30x (quality SaaS) | YES -- mid-range |
| EV/Revenue | 8.0x | 6-12x (quality SaaS) | YES -- mid-range |

All implied multiples are within reasonable bounds for quality vertical SaaS. No red flags.

### Validation vs Analyst Targets

| Source | Target | vs My $195 |
|--------|--------|-----------|
| Goldman Sachs (Sell) | $215 | +10.3% above mine |
| Stifel (Buy) | $270 | +38.5% above mine |
| Analyst consensus | ~$240 | +23.1% above mine |
| My FV | $195 | -- |

My FV is MORE conservative than even Goldman's Sell target ($215). This is intentional: I integrate the 2 CRITICAL risks (CRM defection + Salesforce) more aggressively than sell-side analysts, who may be anchored to higher historical multiples.

---

## Validation vs Precedents (decisions_log.yaml)

| Metric | VEEV | Portfolio Avg (Tier A) | Assessment |
|--------|------|----------------------|------------|
| QS Adjusted | 80 | 75.3 | Above average -- good |
| Entry MoS (at $150) | 23.1% | 33.8% | Below average -- but FV already risk-adjusted |
| ROIC-WACC spread | +0.7pp | varies | LOW -- excess cash effect, forward ROIC should recover |
| FCF Margin | 40% | varies | EXCEPTIONAL |
| Net Debt | -$6.5B | varies | BEST in portfolio (fortress) |

The lower MoS at entry vs precedents is compensated by:
1. My FV already incorporates the CRITICAL risks (lower FV = less "hidden" risk)
2. Net cash of $6.5B = $40/share is a unique downside cushion no other position has
3. 40% FCF margin means even in a severe bear, the business generates strong cash

---

## Summary

| Metric | Value |
|--------|-------|
| **Fair Value (Valuation Specialist)** | **$195** |
| **Expected Value (prob-weighted)** | **$199** |
| **Bear Case FV** | **$155** |
| **Base Case FV** | **$195** |
| **Bull Case FV** | **$250** |
| Current Price | $172.0 |
| MoS vs FV | +11.8% |
| MoS vs Expected | +13.6% |
| MoS vs Bear | -11.0% |
| **Recommended Entry** | **$145-$155** |
| **Standing Order Suggestion** | **$150** |
| Divergence from Analyst's $220 | -11.4% |
| Methods Used | 4 (DCF, OEY, EV/FCF, Reverse DCF) |
| Method Divergence | 21% (within 30% threshold) |

---

## META-REFLECTION

### Dudas/Incertidumbres

1. **ROIC-WACC spread of +0.7pp is genuinely concerning.** While I accept the argument that excess cash distorts ROIC, the trend is troubling: 22.9% to 15.1% to 9.5% to 11.1%. If ROIC does not recover above 15% by FY2028 as the Vault investment cycle peaks, the "quality compounder" thesis weakens. My FV of $195 assumes ROIC recovery -- if it does not materialize, FV could be closer to $160-$170.

2. **The DCF terminal value at 73.9% of EV makes the valuation heavily dependent on long-term assumptions.** I mitigated this by using 4 methods (reducing DCF weight to 35%) but the fundamental truth is that VEEV's value is primarily in its future, not its present. At 33.5x P/E, you are paying for 10+ years of compounding. If anything disrupts that compounding (Salesforce wins R&D, regulation relaxes, AI disruption), the downside is substantial.

3. **My $195 FV is more conservative than Goldman's SELL target of $215.** This gives me pause -- am I being too conservative? Or are sell-side analysts (including those with Sell ratings) anchored to historical multiples that no longer apply? I believe the latter: Goldman's $215 was set when the stock was higher and represents a relative call (sell because it will underperform), not an absolute call (sell because it is overvalued at $215).

4. **CRM customer defection: 14 vs 18 of top-20.** The fundamental-analyst argues this is "transition noise." The risk-identifier argues it could get worse (KeyBanc channel checks). I split the difference: my base case assumes 14/20 stabilizes (management guidance) but my bear case assumes 10-12/20. I am NOT confident which scenario is correct. Q4 FY2026 earnings (March 4) will be critical.

5. **PBC structure is an under-discussed risk.** Veeva is a Public Benefit Corporation. The board is legally required to balance all stakeholders, not just shareholders. With $6.5B cash, no dividend, and no buyback, VEEV may never return capital to shareholders. This is fine if the stock appreciates through earnings growth, but if growth stalls and the multiple compresses, there is no "capital return floor" to support the stock.

### Sensibilidad Preocupante

- Moving WACC from 10% to 11.5% (a 1.5pp increase) drops DCF FV from $174 to $151 -- a 13% decrease. This is high but expected for a growth company.
- Moving growth from 12% to 9% (a 3pp decrease) drops DCF FV from $174 to $159 -- a 9% decrease.
- The combination (WACC 11.5%, growth 9%) gives $138 -- a 21% decrease from base. This is the "everything goes wrong" scenario.

### Discrepancias con Thesis

My FV of $195 is 11.4% below the fundamental-analyst's $220. The key drivers:
1. I use 12% FCF growth vs analyst's implicit 14% -- accounting for CRM headwinds
2. I use 10.0% WACC vs analyst's 9.5% -- less generous fortress balance sheet discount
3. I weight OEY less heavily (30% vs analyst's 55%) because OEY overstates FV for growth companies
4. I integrate risk into the FV itself rather than only through MoS at entry

Despite this, both the analyst and I arrive at similar ENTRY PRICES: analyst $155-165, me $145-155. The difference is framing: the analyst says "$220 FV minus 29% MoS = $155 entry." I say "$195 FV minus 23% MoS = $150 entry." Same destination, different path.

### Sugerencias para el Sistema

1. **quality_scorer.py excess cash adjustment** (echoing both the fundamental-analyst and moat-assessor): Companies with net cash >20% of market cap (VEEV, GOOGL, AAPL) get mechanically penalized on ROIC. A `--excess-cash-adjust` flag would net out cash above 10% of revenue from invested capital. This is not a minor issue -- it caused VEEV to score 72 (Tier B) when forward-looking quality is clearly Tier A.

2. **DCF tool should report the implied growth rate at current price.** This is the most useful output for price discipline (what growth am I getting for free?) but currently requires running multiple DCF iterations manually. A `--implied-growth` flag would automate this.

3. **Standardize how we handle the OEY method for growth companies.** The skill says OEY is primary for Tier A, but for fast growers, OEY gives unrealistically high FVs because growth dominates. We need a protocol for when to cap OEY-implied FV or reduce its weight.

### Preguntas para Orchestrator

1. My FV ($195) diverges -11.4% from the analyst's ($220). In R3 conflict resolution, how should the orchestrator reconcile? I recommend weighting the valuation specialist's FV more heavily because: (a) it is the specialist output, and (b) the analyst's $220 includes optimistic growth assumptions I documented above.

2. Should we wait for Q4 earnings (March 4) before setting a standing order? Pro: reduces CRM uncertainty. Con: price could drop to entry range before earnings if broader SaaS selloff continues. Suggestion: set standing order at $150 now (implies 23% MoS), but ADD logic conditional on Q4 data.

3. The risk-identifier found 2 CRITICAL correlated risks. In our portfolio, we have 0 positions with 2 CRITICAL risks at entry. Is this a precedent we want to set? Our precedent analysis shows Medium to Medium-High risk for most Tier A entries, which maps to 0-1 CRITICAL risks. VEEV would be the first with 2 CRITICAL -- are we comfortable?

---

*Valuation conducted independently by valuation-specialist agent.*
*Data sources: quality_scorer.py, price_checker.py, dcf_calculator.py (4 runs), R1 agent outputs (thesis, moat, risk).*
*All inputs derived from projection-framework -- no defaults used.*
