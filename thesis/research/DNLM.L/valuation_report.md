# Valuation Report: DNLM.L (Dunelm Group plc)

## Fecha: 2026-02-07
## Valorador: valuation-specialist (independiente)
## Framework: v4.0

---

## VALORACION: DNLM.L

**Tipo de empresa:** Stable/defensive retailer with cyclical exposure (UK homewares market leader)
**Quality Score:** 79 (Tier A)
**Moat:** NARROW trending WIDE (moat-assessor independent classification)
**Risk Score:** MEDIUM (1 CRITICAL + 3 HIGH risks identified by risk-identifier)

**Metodos seleccionados:** Owner Earnings Yield (primario) + EV/EBIT Normalizado (secundario)

**Justificacion de metodos:**
- Tier A (QS >= 75) prescribes OEY + Reverse DCF per valuation-methods skill
- However, DCF tool output is heavily distorted by IFRS 16 lease treatment (net debt includes GBP 247.5M in capitalized leases). This systematically understates fair value for a company that is effectively unlevered (0.33x net debt/EBITDA ex-leases)
- EV/EBIT Normalizado selected as secondary because it anchors to current earnings power and allows peer comparison
- DDM used as tertiary cross-check given 4.8% dividend yield and 10+ year dividend history
- DCF tool outputs used for sensitivity and reverse DCF analysis, with IFRS 16 caveat noted throughout

---

## CRITICAL RISK ADJUSTMENTS (from Round 1 independent reports)

Before calculating fair value, I must incorporate the material findings from the moat-assessor and risk-identifier that the thesis either missed or underestimated.

### 1. NIC + National Living Wage Headwind: GBP 18M annualized

The risk-identifier flagged a CONFIRMED regulatory cost increase of GBP 18M+ (employer NIC up 1.2pp to 15%, threshold lowered; NLW up 4.1% to GBP 12.71/hour from April 2026). This is 8-9% of pre-tax profit and was NOT mentioned in the thesis.

**Impact on my valuation:**
- Reduce FY26 PBT estimate from GBP 214-222M to GBP 196-204M (subtracting GBP 18M headwind)
- However, partial offset expected: Dunelm's 52.4% gross margin provides pricing power buffer; estimate 50% offset through productivity gains, pricing, and mix (GBP 9M absorbed, GBP 9M hits PBT)
- **Net adjusted PBT FY26: GBP 205-213M** (vs thesis assumption of GBP 214-222M)
- Reduce forward operating margin assumption from 12.3% (thesis) to 11.8-12.0%
- Reduce FCF growth estimate from 5% to 4% for years 1-2 (NIC/NLW absorb growth), then 5% from year 3 onward as offsets mature

### 2. Moat classified as NARROW (not WIDE)

The moat-assessor independently classified the moat as NARROW, not WIDE, primarily because: (a) zero switching costs in retail, (b) online commoditization threat from Temu/Amazon over 10-15 years. This affects the multiple I assign.

**Impact on my valuation:**
- Reduce EV/EBIT multiple range from thesis's 10-12x to 10-11x
- Use OEY target yield of 7.5% (conservative for NARROW moat) vs thesis's 6-7%
- Do NOT assign "quality premium" above sector median for EV/EBIT; instead use sector median + 1x (vs thesis's +2x)

### 3. Consumer weakness duration: through end 2026 minimum, possibly into 2027

The risk-identifier provided evidence from KPMG, Fitch, and RSM that UK consumer weakness is not "2-3 quarters" as the thesis claims, but likely persists through end 2026 and potentially into H1 2027. Multiple forecasters project UK GDP at 0.8-1.2% and unemployment rising to 5.2%.

**Impact on my valuation:**
- Bear case duration extended: assume 2 years of subdued growth (0-2%), not 1 year
- Base case: first year at 3% growth (not 5%), then 5% from year 2
- Increase WACC by 0.5pp to 9.5% to reflect higher UK macro uncertainty and the correlated nature of risks #1, #4, #8 (all UK macro)

### 4. Adderley family sold 5% at 1,140p (July 2025)

The thesis incorrectly states "38.5% insider, no recent sales." The family sold GBP 114M of stock at 1,140p. Current holding is ~37.6% (or lower depending on source). The family sold ABOVE current price, which provides a ceiling reference.

**Impact on my valuation:**
- The family's sell price of 1,140p is a meaningful data point: informed insiders (47 years of company history) chose to diversify at that price. This suggests they did not see significant further upside above 1,100-1,200p
- Caps my fair value estimate: I should be cautious about FV estimates significantly above 1,200p
- Does not reduce fair value directly, but acts as a reality check on the OEY method which produces 1,400p+

### 5. New CEO (Oct 2025) - no homewares experience

Clodagh Moriarty joined from Sainsbury's (grocery). She sold GBP 587K of shares within 1 month. While her digital/retail credentials are strong, she has no homewares category experience.

**Impact on my valuation:**
- Adds execution risk; partially captured in the higher WACC (9.5% vs thesis 9%)
- Not a disqualifying factor but warrants monitoring

---

## Metodo 1: Owner Earnings Yield (Primario, 50% weight)

### Risk-Adjusted OEY Calculation

| Metric | Thesis Value | My Risk-Adjusted Value | Reasoning |
|--------|-------------|----------------------|-----------|
| FCF (last reported) | GBP 211M | GBP 211M | FY25 actual, verified |
| Forward FCF FY26E | Not specified | GBP 188M | FY25 211M minus NIC/NLW net impact (GBP 9M after partial offset), minus higher capex (GBP 50-60M guided vs ~GBP 37M prior), working capital normalization |
| Maintenance Capex | ~GBP 37M (D&A proxy) | GBP 40M | Slightly higher due to inner city expansion |
| Owner Earnings (FY25 actual) | ~GBP 174M (211M - 37M maint capex) | GBP 174M | Same calculation |
| Owner Earnings (FY26E forward) | Not calculated | GBP 152M | 188M forward FCF - 36M maintenance capex |
| Market Cap | GBP 1,898M | GBP 1,898M | 202.6M shares x 936.5p |

**Using FY25 actual Owner Earnings (backward-looking):**
- OEY = 174M / 1,898M = 9.2%
- Expected Growth = 4% (risk-adjusted, years 1-2)
- OEY + Growth = 13.2% vs WACC 9.5% = spread +3.7pp

**Using FY26E forward Owner Earnings (forward-looking, incorporating NIC/NLW):**
- OEY = 152M / 1,898M = 8.0%
- Expected Growth = 4% (years 1-2), then 5% (years 3+)
- OEY + Growth = 12.0% vs WACC 9.5% = spread +2.5pp

**Commentary:** The thesis calculated OEY of 11.1% using reported FCF of GBP 211M without separating maintenance capex from growth capex, and without adjusting for the NIC/NLW headwind. My risk-adjusted forward OEY of 8.0% is significantly lower but still provides a positive spread over WACC. The backward-looking OEY of 9.2% (using actual Owner Earnings) provides a more generous spread of +3.7pp.

### Implied Fair Value from OEY

For a NARROW moat Tier A company, what OEY target yield is appropriate?

**Precedent reasoning:**
- decisions_log.yaml shows OEY + Growth comparisons for Tier A: NVO ~12-14%, ADBE ~10-12%, MONY.L ~13-15%
- These were all purchased. The minimum accepted OEY + Growth was ~10%
- For DNLM.L, using forward OEY: 8.0% + 4% growth = 12.0%. This is within the range of accepted Tier A purchases
- However, I need to be conservative given the headwinds

**Target OEY of 7.5% (reflecting NARROW moat, not WIDE):**
- FV = Forward Owner Earnings / Target OEY = 152M / 0.075 = GBP 2,027M
- FV per share = 2,027M / 202.6M = **1,000p**

**Target OEY of 7.0% (slightly more generous, reflecting Tier A quality):**
- FV = 152M / 0.070 = GBP 2,171M
- FV per share = 2,171M / 202.6M = **1,072p**

**Target OEY of 8.0% (more conservative):**
- FV = 152M / 0.080 = GBP 1,900M
- FV per share = 1,900M / 202.6M = **938p**

**Thesis comparison:** The thesis used 7% target OEY with FY25 actual FCF (not OE) to get 1,491p. My approach differs in two critical ways:
1. I use Owner Earnings (FCF minus maintenance capex), not raw FCF
2. I use forward estimates incorporating NIC/NLW headwinds
3. These differences explain why my OEY fair value is 33% lower (1,036p vs 1,491p)

**Central OEY Fair Value: 1,036p** (average of 7.0% and 7.5% target yields)

---

## Metodo 2: EV/EBIT Normalizado (Secundario, 30% weight)

### EBIT Normalization

| Year | EBIT | Comment |
|------|------|---------|
| FY22 | GBP 251M | Peak (COVID home improvement boom) |
| FY23 | GBP 205M | Normalization |
| FY24 | GBP 219M | Recovery |
| FY25 | GBP 222M | Stable |
| FY26E | GBP 196-208M | Guided lower end + NIC/NLW headwind |

**Normalized EBIT (excl. COVID peak FY22):** Average of FY23-FY25 + FY26E (low) = (205 + 219 + 222 + 196) / 4 = **GBP 210.5M**

**Risk-adjusted EBIT:** Given that NIC/NLW is structural (not temporary), I weight FY26E more heavily: (219 + 222 + 196 + 205) / 4 = **GBP 210.5M**. However, the normalized forward run-rate incorporating the cost headwind is closer to GBP 205M.

**I will use GBP 208M** as normalized EBIT -- a blend that gives credit to the secular growth trend while incorporating the structural cost headwind.

### Multiple Selection

| Comparable | EV/EBIT (est.) | ROIC | Growth | Comment |
|------------|---------------|------|--------|---------|
| Next plc (NXT.L) | ~14-15x | ~50%+ | ~7% | Premium UK retailer, wider moat |
| B&M European Value (BME.L) | ~8x | ~20% | ~3% | Value retailer, weaker position |
| JD Sports (JD.L) | ~9-10x | ~15% | ~5% | Sports fashion, more cyclical |
| Howdens Joinery (HWDN.L) | ~14x | ~30% | ~6% | UK specialist, strong moat |
| UK Retail sector median | ~8-10x | varies | varies | |

**Dunelm positioning:**
- ROIC of 26% vs 9% WACC (spread +17pp) -- superior to B&M/JD, below Next/Howdens
- Growth of 4-5% -- mid-range
- GM of 52.4% -- exceptional for sector
- NARROW moat (not WIDE like Next or Howdens which have stronger switching costs/trade relationships)

**Base multiple: 10x EBIT**

Adjustments:
- Sector median for quality UK retailers: 10x (base)
- Superior ROIC (+17pp spread): +1x
- Strong GM (+17pp vs sector): already captured in ROIC
- NARROW moat (not WIDE): -0.5x
- NIC/NLW structural headwind (margin compression risk): -0.5x
- Consumer weakness duration (through end 2026): already captured in normalized EBIT
- **Final multiple: 10x EBIT**

**Note:** The thesis used 11x with a +2x quality premium. I use 10x because: (a) the moat-assessor classifies NARROW not WIDE, (b) NIC/NLW creates structural margin pressure, (c) the Adderley family sold at 1,140p which implies roughly 10.5-11x EV/EBIT at the time.

### EV/EBIT Fair Value Calculation

| Component | Value |
|-----------|-------|
| Normalized EBIT | GBP 208M |
| Multiple | 10x |
| Enterprise Value | GBP 2,080M |
| (-) Net Debt (ex-leases) | GBP 100M |
| (=) Equity Value | GBP 1,980M |
| Shares Outstanding | 202.6M |
| **Fair Value per share** | **977p** |

**Sensitivity on multiple:**

| Multiple | Fair Value | MoS vs 936.5p |
|----------|-----------|----------------|
| 8x (recession) | 780p | -17% |
| 9x (bearish) | 879p | -6% |
| 10x (base) | 977p | +4% |
| 11x (thesis) | 1,076p | +15% |
| 12x (bullish) | 1,174p | +25% |

**Central EV/EBIT Fair Value: 977p**

---

## Metodo 3: DDM - Tertiary Cross-Check (20% weight)

| Parameter | Value | Source / Reasoning |
|-----------|-------|-------------------|
| Ordinary DPS (FY25) | 43.5p | Reported |
| Dividend growth rate | 4% | Risk-adjusted: FY26 EPS pressure from NIC/NLW limits dividend growth vs thesis's 5% |
| Ke (cost of equity) | 9.5% | Risk-adjusted WACC |
| D1 | 45.24p | 43.5 x 1.04 |
| **Fair Value (Gordon Growth)** | **823p** | 45.24 / (0.095 - 0.04) |

**With partial special dividends:**
- Average special dividend last 3 years: ~25-35p per year
- Probability of continuation: 60% (lower than thesis's 80% due to NIC/NLW pressure on surplus cash)
- Expected annual special: ~18p (30p x 60%)
- Total expected dividend: 45.24 + 18 = 63.24p
- FV with specials: 63.24 / (0.095 - 0.04) = **1,150p**

**Central DDM estimate: 987p** (weighted 40% ordinary-only, 60% with specials: 823 x 0.4 + 1,150 x 0.6)

**Commentary on DDM divergence:**
- Ordinary-only DDM (823p) is significantly below the OEY and EV/EBIT estimates
- DDM with specials (1,150p) is significantly above
- This reflects genuine uncertainty about special dividend sustainability given NIC/NLW costs
- The weighted central estimate (987p) is consistent with the other methods

---

## Reconciliacion

| Metodo | Fair Value | Peso | Weighted |
|--------|-----------|------|----------|
| OEY (risk-adjusted, forward) | 1,036p | 50% | 518p |
| EV/EBIT 10x (normalized, risk-adjusted) | 977p | 30% | 293p |
| DDM (weighted ordinary + specials) | 987p | 20% | 197p |
| **Weighted Average** | | **100%** | **1,008p** |

**Weighted Fair Value: 1,008p**
**Current Price: 936.5p** (verified 2026-02-07 via price_checker.py)
**Margin of Safety: 7.1%**

**Divergencia entre metodos:** OEY gives 1,036p, EV/EBIT gives 977p, DDM gives 987p. Maximum divergence = (1,036 - 977) / 977 = 6.0%. **Well below the 30% threshold.** All three risk-adjusted methods converge tightly, which increases confidence in the valuation.

**CRITICAL COMPARISON vs thesis:**
- Thesis weighted FV: 1,328p (MoS 29.5%)
- My risk-adjusted FV: 1,008p (MoS 7.1%)
- **Difference: -24% (320p lower)**

**Why the difference?**
1. **NIC/NLW headwind not in thesis:** GBP 18M structural cost increase reduces forward earnings and FCF by ~GBP 9M net (after partial offset), reducing OEY and EV/EBIT estimates
2. **Moat-adjusted multiples:** Thesis used 11x EV/EBIT with +2x quality premium; I use 10x reflecting NARROW (not WIDE) moat and structural cost pressure
3. **OEY calculation method:** Thesis used raw FCF (GBP 211M) at 7% target yield = 1,491p. I use forward Owner Earnings (GBP 152M, after maintenance capex AND NIC/NLW) at 7.25% average target yield = 1,036p
4. **Higher WACC:** 9.5% vs thesis's 9.0% reflecting correlated UK macro risks
5. **Insider selling reality check:** Adderley family sold at 1,140p, capping the reasonable FV range

---

## DCF Cross-Validation

**IMPORTANT CAVEAT:** The DCF tool includes GBP 0.35B net debt (which incorporates IFRS 16 lease obligations of GBP 247.5M). This systematically UNDERSTATES fair value for Dunelm, which has only GBP 100M of real financial debt. The DCF outputs should be interpreted as conservative floors.

### DCF Sensitivity Table

| Growth | WACC 8.5% | WACC 9.0% | WACC 9.5% | WACC 10.0% | WACC 11.0% |
|--------|-----------|-----------|-----------|------------|------------|
| 0% | - | - | - | 997p | - |
| 1% | - | - | - | - | 920p |
| 2% | - | - | - | 1,101p | - |
| 3% | - | - | 1,080p (Bear) | 1,216p | - |
| 4% | - | - | 1,373p (Base) | - | - |
| 5% | - | 1,660p | - | - | - |
| 6% | 1,901p | - | - | - | - |

### Reverse DCF Analysis

**What growth rate does the market imply at 936.5p?**

| Scenario | Growth | WACC | Terminal | FV | vs Price |
|----------|--------|------|----------|-----|---------|
| A | 0% | 10% | 1.5% | 997p | +6.5% |
| B | -1% | 10% | 1.0% | 904p | -3.4% |
| C | 1% | 11% | 1.5% | 920p | -1.8% |

**Conclusion:** At 936.5p, the market is pricing in approximately **0% FCF growth at a 10% WACC**, or **-1% FCF growth at a 10% WACC with 1% terminal**. This implies the market expects:
- Either NO growth despite the company gaining market share and growing revenue 3-5%
- Or a substantially higher risk premium (~10-11% WACC) than the 9-9.5% I calculate

**My assessment:** 0% growth for a company gaining market share, expanding margins (despite competitor discounting), and in a market growing 3-4% is excessively pessimistic. Even with NIC/NLW headwinds, 2-3% FCF growth is a reasonable floor. The market is pricing in a scenario where ALL the downside risks materialize simultaneously.

---

## Escenarios

### Bear Case (25% probability)

| Assumption | Value |
|------------|-------|
| Revenue growth | 0% for 2 years (consumer recession), then 2% |
| Operating margin | 11.0% (NIC/NLW + competitive pressure fully hit) |
| WACC | 10.5% (UK recession premium) |
| Terminal growth | 1.5% |
| EV/EBIT multiple | 8x (recession) |
| PBT FY26-27 | GBP 180-190M |

**Bear Fair Value:**
- DCF (tool): ~904p (using -1% growth, 10% WACC, 1% terminal -- IFRS 16 distorted)
- EV/EBIT 8x on GBP 190M EBIT: EV 1,520M - 100M debt = 1,420M equity = 701p
- OEY: Forward FCF ~GBP 145M, OE ~GBP 110M. At 9% target OEY: 110M/0.09 / 202.6M = 603p
- **Bear case average: 736p**

**Bear case scenario requires:** UK recession AND NIC/NLW costs fully unmitigated AND margin compression from competitive discounting AND multiple contraction to 8x. This is a "everything goes wrong at once" scenario, but the correlated nature of UK macro risks means it is not implausible.

### Base Case (50% probability)

| Assumption | Value |
|------------|-------|
| Revenue growth | 3% year 1, then 5% from year 2 |
| Operating margin | 11.8% year 1, recovering to 12.0-12.3% by year 3 |
| WACC | 9.5% |
| Terminal growth | 2.0% |
| EV/EBIT multiple | 10x |
| PBT FY26 | GBP 205-213M |

**Base Fair Value:**
- OEY: 1,036p (central OEY estimate)
- EV/EBIT: 977p
- DDM: 987p
- **Base case: 1,008p** (weighted average of methods)

### Bull Case (25% probability)

| Assumption | Value |
|------------|-------|
| Revenue growth | 6% (consumer recovery + accelerating share gains) |
| Operating margin | 12.5-13.0% (operating leverage, NIC/NLW fully offset) |
| WACC | 9.0% (UK macro normalizes) |
| Terminal growth | 2.5% |
| EV/EBIT multiple | 12x (re-rating toward historical 13-14x) |
| PBT FY27+ | GBP 230M+ |

**Bull Fair Value:**
- DCF (tool): 1,901p (6% growth, 8.5% WACC -- but IFRS 16 distorted; add ~150p for lease adjustment)
- EV/EBIT 12x on GBP 225M EBIT: EV 2,700M - 100M = 2,600M equity = 1,283p
- OEY: Forward OE GBP 190M at 6% target yield: 190M/0.06 / 202.6M = 1,563p
- **Bull case average: 1,423p** (excluding IFRS16-distorted DCF outlier; average of EV/EBIT and OEY)

### Expected Value

**EV = (Bear x 0.25) + (Base x 0.50) + (Bull x 0.25)**
**EV = (736 x 0.25) + (1,008 x 0.50) + (1,423 x 0.25)**
**EV = 184 + 504 + 356 = 1,044p**

| Escenario | Fair Value | Probabilidad | Contribution |
|-----------|-----------|-------------|-------------|
| Bear | 736p | 25% | 184p |
| Base | 1,008p | 50% | 504p |
| Bull | 1,423p | 25% | 356p |
| **Expected** | **1,044p** | **100%** | **1,044p** |

---

## Resumen Final

**Precio actual: 936.5p**

| Measure | Value |
|---------|-------|
| MoS vs Weighted FV (1,008p) | 7.1% |
| MoS vs Expected Value (1,044p) | 10.3% |
| MoS vs Bear Case (736p) | **-21.4%** |
| MoS vs Bull Case (1,423p) | 34.2% |
| MoS vs Adderley sell price (1,140p) | 17.9% |

### Validacion vs Peers

| Metric | DNLM.L (current) | DNLM.L (at my FV 1,008p) | Next (NXT.L) | B&M (BME.L) | Howdens (HWDN.L) |
|--------|------------------|--------------------------|--------------|-------------|------------------|
| P/E | 12.2x | ~13.2x | 19.6x | 7.0x | 18.5x |
| EV/EBIT (est.) | ~9x | ~10x | ~15x | ~8x | ~14x |
| Div Yield | 4.8% | ~4.5% | 1.9% | 7.6% | 2.5% |

**Commentary:** My fair value of 1,008p implies a P/E of ~13.2x and EV/EBIT of ~10x. This is reasonable for a NARROW moat UK retailer with 52.4% gross margin and 26% ROIC. It positions Dunelm above B&M (lower quality) and well below Next/Howdens (wider moats, stronger growth profiles). The implied valuation is consistent with the company's quality -- not cheap enough to be a B&M-style value trap, not expensive enough to price in WIDE moat that it does not (yet) have.

### Validacion vs Precedentes (decisions_log.yaml)

| Ticker | QS | MoS at entry | Type |
|--------|-----|-------------|------|
| ADBE | 76 | 31% | Tier A |
| NVO | 82 | 38% | Tier A |
| MONY.L | 81 | 36% | Tier A |
| LULU | 82 | 34% | Tier A |
| AUTO.L | 79 | 29% | Tier A |
| BYIT.L | 81 | 35% | Tier A |
| **DNLM.L at 936.5p** | **79** | **7.1%** | **Tier A** |
| **DNLM.L at 900p** | **79** | **10.7%** | **Tier A** |
| **DNLM.L at 800p** | **79** | **20.6%** | **Tier A** |

**The precedent pattern is clear:** All Tier A purchases had MoS of 29-38%. DNLM.L at 936.5p has only 7.1% MoS -- well below ANY precedent. Even at the thesis's 900p entry trigger, MoS is only 10.7%, still below the minimum precedent of 29%.

To match the minimum precedent (AUTO.L at 29%), DNLM.L would need to be at ~715p. To match the median precedent (~34%), it would need to be at ~665p. These are substantially lower than current price.

### Key Question: Is the thesis FV of 1,328p correct?

**No.** After incorporating the risks identified by the independent moat-assessor and risk-identifier:

1. The NIC/NLW headwind (GBP 18M) reduces forward earnings power by ~4-5%
2. The NARROW moat classification (vs implied WIDE in thesis) reduces the appropriate multiple
3. The Adderley family selling at 1,140p provides a market-informed ceiling
4. The correlated UK macro risks (consumer + NIC/NLW + fiscal contraction) justify a higher WACC
5. The consumer weakness duration (through end 2026+, not "2-3 quarters") extends the recovery timeline

The thesis FV of 1,328p is **30% above my risk-adjusted FV of 1,008p**. The thesis used higher FCF (no NIC/NLW adjustment), higher multiples (WIDE moat premium), lower WACC (9% vs 9.5%), and a more optimistic growth trajectory.

---

## Sensibilidad DCF

### WACC vs Growth Rate (FV per share, using DCF tool with IFRS 16 caveat)

| | WACC 8.5% | WACC 9.0% | WACC 9.5% | WACC 10.0% | WACC 10.5% |
|---|-----------|-----------|-----------|------------|------------|
| Growth 2% | ~1,450p | ~1,300p | ~1,100p | ~1,000p | ~900p |
| Growth 3% | ~1,550p | ~1,400p | ~1,216p | ~1,100p | ~1,000p |
| Growth 4% | ~1,700p | ~1,500p | ~1,373p | ~1,200p | ~1,080p |
| Growth 5% | ~1,900p | ~1,660p | ~1,500p | ~1,350p | ~1,200p |
| Growth 6% | ~2,100p | ~1,900p | ~1,700p | ~1,500p | ~1,350p |

Note: Values marked ~ are interpolated from DCF tool runs. All include IFRS 16 lease obligations in net debt (conservative).

### Key Sensitivities

| Change | Impact on Base FV (1,008p) |
|--------|--------------------------|
| Growth +1pp (4% to 5%) | +60-80p (+6-8%) |
| Growth -1pp (4% to 3%) | -50-70p (-5-7%) |
| WACC +0.5pp (9.5% to 10%) | -80-100p (-8-10%) |
| WACC -0.5pp (9.5% to 9%) | +80-100p (+8-10%) |
| NIC/NLW fully offset (no impact) | +30-40p (+3-4%) |
| NIC/NLW not offset at all | -30-40p (-3-4%) |
| EV/EBIT +1x (10x to 11x) | +50p on EV/EBIT method (+5%) |

**Observation:** The valuation is moderately sensitive to WACC and growth assumptions but not excessively so. A swing of +/-1pp in WACC changes FV by 8-10%. The NIC/NLW headwind impact is meaningful but not transformative (3-4% of FV).

---

## 🔄 META-REFLECTION

### Dudas/Incertidumbres
- **IFRS 16 distortion in DCF tool:** The DCF tool systematically understates fair value for Dunelm because it includes GBP 247.5M of lease obligations in net debt. Dunelm has only GBP 100M of real financial debt. Adjusting for this would add approximately 120-150p to all DCF-derived fair values. I compensated by using OEY and EV/EBIT (ex-leases) as primary methods, but the DCF sensitivity table inherits this conservative bias.
- **NIC/NLW offset rate:** I assumed 50% offset (GBP 9M of 18M absorbed via productivity/pricing). The actual offset could range from 30% (weak consumer limits pricing power) to 70% (strong private label pricing power + automation). This creates a +/-GBP 4M uncertainty in forward PBT, translating to +/-20p in fair value.
- **Consumer weakness duration:** The consensus of professional forecasters (KPMG, Fitch, RSM) projects weakness through end 2026. However, forecasters are notoriously poor at predicting turning points. The actual recovery could come faster (if rate cuts materialize, housing stabilizes) or slower (if global trade war escalates, UK fiscal contraction deepens).
- **Adderley family stake interpretation:** I used the family's sell price of 1,140p as a ceiling reference. However, the family may have sold for purely personal reasons (estate planning, diversification) unrelated to their view on Dunelm's intrinsic value. This is inherently ambiguous.
- **Bear case severity:** My bear case FV of 736p implies a 21% decline from current price. This is plausible in a UK recession scenario, but Dunelm's defensive characteristics (homewares refresh/replace, market share gains during weakness, 0.33x leverage) provide meaningful downside protection that may make 736p too pessimistic.

### Sensibilidad Preocupante
- **The MoS of 7.1% is very thin for a Tier A company.** All precedent Tier A purchases had 29-38% MoS. This stock is NOT cheap enough to buy at current levels under our framework.
- **The downside to bear case is -21% vs upside to bull case of +34%.** The asymmetry is less favorable than the thesis claims (thesis: -12% down, +55% up), primarily because I use lower fair values.
- **Interims on 10 Feb (3 days away):** Binary event risk. If H1 PBT comes in below GBP 112M, the stock could fall 5-10% to 840-890p, which would bring MoS closer to 13-17% -- still below precedent minimums but more interesting.

### Discrepancias con Thesis
1. **Fair Value:** Thesis 1,328p vs my 1,008p (-24%). The difference is driven by NIC/NLW headwind (not in thesis), lower multiple (NARROW not WIDE moat), forward OE (not backward FCF), and higher WACC
2. **MoS:** Thesis 29.5% vs my 7.1%. The gap is entirely explained by the lower FV
3. **OEY calculation:** Thesis uses raw FCF at 7% yield (1,491p). I use forward Owner Earnings at 7.25% average yield (1,036p). The thesis method overstates because it (a) does not subtract maintenance capex and (b) does not incorporate the NIC/NLW headwind
4. **Growth trajectory:** Thesis assumes 5% sustainable from year 1. I assume 3% year 1 (consumer weakness + NIC/NLW), then 5% from year 2+
5. **Insider ownership:** Thesis says "38.5%, no recent sales" -- INCORRECT per risk-identifier. Family sold 5% at 1,140p in July 2025

### Sugerencias para el Sistema
1. **DCF tool IFRS 16 adjustment:** The DCF tool should offer a flag to exclude lease obligations from net debt (e.g., `--ex-leases`). For UK retailers with many leased stores, the current treatment materially understates equity value. This affects DNLM.L, NXT.L, and any other lease-heavy retailer.
2. **OEY calculation method needs standardization:** The thesis and I calculated OEY differently (FCF vs Owner Earnings). The system should standardize: OEY = (FCF - Maintenance Capex) / Market Cap, not FCF / Market Cap. Maintenance capex should be approximated as D&A x 1.1 per the DCF template skill.
3. **Forward vs backward inputs:** For companies facing structural cost increases (NIC/NLW) or revenue headwinds, forward estimates should be used for valuation, not trailing figures. The valuation-methods skill should explicitly require "use forward estimates if there is a known material change to earnings power."

### Preguntas para Orchestrator
1. **Is a 7.1% MoS sufficient for a Tier A purchase?** All precedents show 29-38%. Even at 900p (thesis entry), MoS is only 10.7%. The stock would need to fall to ~715p for a 29% MoS comparable to AUTO.L. Should the watchlist entry trigger be lowered from 900p to 750-800p?
2. **The interims on 10 Feb create a tactical opportunity.** If results disappoint and the stock falls to 800-850p, MoS would reach 16-21% -- still below precedent minimums but approaching. Should we set a conditional standing order at 800p instead of 900p?
3. **How much weight should we give to the Adderley family selling at 1,140p?** The family has 47 years of company knowledge. Their decision to sell GBP 114M of stock at 1,140p is a meaningful signal. Should this cap our FV ceiling?
4. **The correlated UK macro risk is the elephant in the room.** Consumer weakness + NIC/NLW + fiscal contraction are all the same bet. Adding DNLM.L as a 7th UK position compounds this exposure. Is the current UK weighting appropriate for adding another consumer-facing UK position?

---

**Valuation Date:** 2026-02-07
**Framework:** v4.0
**Valorador:** valuation-specialist (independent)
**Fair Value (risk-adjusted): 1,008p**
**Expected Value: 1,044p**
**Current Price: 936.5p**
**MoS vs FV: 7.1%**
**MoS vs Expected: 10.3%**
**MoS vs Bear: -21.4%**
