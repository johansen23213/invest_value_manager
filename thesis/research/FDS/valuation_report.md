> **Fair Value:** $225

# Valuation Report: FDS (FactSet Research Systems)

**Date:** 2026-02-13
**Analyst:** valuation-specialist (opus)
**Pipeline Stage:** R1

---

## Company Classification

**Type:** Stable/Defensive subscription software (100% recurring revenue)
**Quality Tier:** B (QS 73/100)
**Methods Selected:** DCF with SBC adjustment (Primary) + EV/EBIT Normalized (Secondary) + Owner Earnings Yield cross-check

Per the valuation-methods skill, Tier B stable/defensive companies use DCF (60% weight) + EV/EBIT (40% weight). Owner Earnings Yield is used as a sanity check, not a weighted component.

---

## Method 1: SBC-Adjusted DCF (60% weight)

### Input Derivation

All inputs derived from the projection-framework in the thesis, not defaults.

| Parameter | Value | Derivation |
|-----------|-------|------------|
| Base FCF | $617M | FY2025 reported FCF |
| SBC Deduction | $61M | FY2025 SBC (2.6% of revenue). Per INTU precedent: SBC must be deducted for software companies. |
| SBC-Adjusted FCF | $556M | $617M - $61M. This is the TRUE owner cash flow. |
| Growth Rate | 6% | TAM +4% + delta share +0.5% + pricing +2% = ~6.5%, rounded down conservatively |
| WACC | 9.0% | Calculated 7.4% (Ke 8.15%, Kd after-tax 3.3%, E/V 85%, D/V 15%) + 1.6pp premium for: cloud transition execution risk, competitive pressure from Bloomberg/AI, beta potentially understating risk |
| Terminal Growth | 2.5% | Slightly below GDP. Financial data industry is structurally growing but FDS is not a monopolist. |
| Projection Period | 5 years | Standard |

### DCF Tool Output (6% growth, 9% WACC, 2.5% terminal)

The DCF tool uses reported FCF ($617M), not SBC-adjusted. Results from tool:

| Scenario | FV (Tool) | MoS vs $204 |
|----------|-----------|-------------|
| Bear | $208 | +2.0% |
| Base | $271 | +32.6% |
| Bull | $359 | +75.9% |

### SBC Adjustment

The tool uses reported FCF. I must adjust for SBC ($61M/year) which is a real cost to shareholders through dilution:

**SBC as % of FCF:** $61M / $617M = 9.9%

Apply 10% haircut to all DCF scenarios:

| Scenario | FV (Tool) | SBC Haircut | FV (SBC-Adjusted) |
|----------|-----------|-------------|-------------------|
| Bear | $208 | -10% | **$187** |
| Base | $271 | -10% | **$244** |
| Bull | $359 | -10% | **$323** |

**Note on SBC adjustment method:** The 10% haircut is a simplification. A more precise method would be to run the DCF with $556M base FCF instead of $617M. However, the tool takes the FCF directly from yfinance (reported), so I apply the adjustment post-hoc. The 10% haircut is conservative and consistent with the INTU precedent (Session 66) where SBC was also deducted as a real cost.

### Sensitivity Matrix (from tool, pre-SBC adjustment)

| Growth / WACC | 7.5% | 9.0% | 10.5% |
|---------------|------|------|-------|
| 3.0% | $315 | $234 | $184 |
| 4.5% | $339 | $252 | $198 |
| **6.0%** | $364 | **$271** | $213 |
| 7.5% | $390 | $291 | $228 |
| 9.0% | $418 | $312 | $245 |

After 10% SBC haircut:

| Growth / WACC | 7.5% | 9.0% | 10.5% |
|---------------|------|------|-------|
| 3.0% | $284 | $211 | $166 |
| 4.5% | $305 | $227 | $178 |
| **6.0%** | $328 | **$244** | $192 |
| 7.5% | $351 | $262 | $205 |
| 9.0% | $376 | $281 | $221 |

**Key observations:**
- **TV as % of EV: 74.9%** -- HIGH. DCF is heavily dependent on terminal value assumptions.
- **FV Spread: 87%** -- HIGH sensitivity to inputs. DCF should not be trusted as a point estimate.
- At WACC 10.5% / Growth 3% (stressed scenario), SBC-adjusted FV = $166, which is 19% below current price -- meaningful downside risk exists.
- At WACC 9% / Growth 4.5% (modest deceleration), SBC-adjusted FV = $227, still above current price.

**DCF SBC-Adjusted Fair Value: $244**

---

## Method 2: EV/EBIT Normalized (40% weight)

### Normalized EBIT

FDS has been in a period of margin expansion followed by recent compression due to cloud/AI investment. I normalize using the most recent 3 fiscal years:

| Year | EBIT (Operating Income) |
|------|------------------------|
| FY2023 | $630M |
| FY2024 | $700M |
| FY2025 | $748M |
| **Average** | **$693M** |

I use the 3-year average ($693M) rather than peak FY2025 because FY2026 guidance implies compression to ~$700M adjusted ($29.5-31.0% GAAP margin on ~$2,450M revenue). This smooths the investment cycle.

**SBC Adjustment:** Deducting SBC from EBIT for consistency with the DCF approach.
- SBC-adjusted EBIT = $693M - $61M = **$632M**

### Peer Multiple Analysis

| Peer | EV/EBIT (current) | Revenue Growth | ROIC | Notes |
|------|-------------------|---------------|------|-------|
| SPGI | ~28x | 10-12% | 15% | Premium: ratings + indices (monopoly) |
| MSCI | ~33x | 10-12% | 41% | Premium: monopoly indices, highest ROIC |
| VRSK | ~27x | 8-10% | 25%+ | Insurance analytics, proprietary data |
| ICE | ~23x | 6-8% | 10% | Exchanges + data |
| MCO | ~31x | 10-12% | 20% | Ratings monopoly |
| MORN | ~17x | 6-8% | 12% | Most comparable: data/analytics, similar growth |
| **FDS** | **~12x** | **5-6%** | **19%** | **Depressed** |
| **Median (ex-FDS)** | **~27x** | **~10%** | **~20%** | |

### Multiple Selection

FDS's appropriate multiple is NOT the peer median (27x) because:
1. **Lower growth:** FDS at 5-6% vs peer median ~10% justifies significant discount
2. **No monopoly position:** Unlike MSCI (indices) or SPGI/MCO (ratings), FDS has no regulatory-mandated product
3. **Margin compression phase:** Currently investing in cloud/AI, margins temporarily compressed
4. **NARROW moat (not WIDE):** Moat assessment classified FDS as NARROW, while MSCI/VRSK have stronger moat characteristics

However, FDS deserves ABOVE trough (12x) because:
1. **95%+ ASV retention** = extremely sticky revenue base
2. **ROIC 19% vs WACC 7.4%** = strong value creation (+11.1pp spread)
3. **27% FCF margins** = healthy cash generation
4. **24 consecutive years of dividend increases** = capital discipline
5. **MORN comparable** trades at 17x with similar growth profile

**Multiple derivation:**

```
Starting point: MORN at 17x (most comparable peer)
Adjustments:
  + Superior ROIC (19% vs 12%): +1x
  + Higher FCF margin (27% vs 20%): +1x
  + Better retention (95% vs MORN's lower): +0.5x
  - Margin compression uncertainty: -1x
  - AI disruption risk (3 correlated HIGH risks per risk assessment): -1.5x
  - Low insider ownership (0.4%): -0.5x
  = FAIR MULTIPLE: 15.5x (round to 15-16x)
```

I use **15x** (conservative end of range) to account for the MEDIUM-HIGH risk score and 3 correlated risks.

### EV/EBIT Valuation

```
SBC-adjusted normalized EBIT: $632M
Multiple: 15x
EV = $632M x 15x = $9,480M

Subtract net debt: $1,270M
Equity Value = $8,210M

Shares outstanding: 37.6M
Fair Value per share = $218
```

**Cross-check at 16x (mid-range):**
```
EV = $632M x 16x = $10,112M
Equity = $10,112M - $1,270M = $8,842M
FV = $8,842M / 37.6M = $235/share
```

**EV/EBIT range: $218 - $235.** Using 15x conservative: **$218**

### Validation: Implied Multiples at My FV

At $218 FV:
- Implied P/E: ~14x (vs current 13x, vs MORN 18x) -- reasonable
- Implied EV/Revenue: ~3.8x (vs current ~3.4x, vs MORN ~4x) -- reasonable
- Implied FCF yield: 7.2% ($556M SBC-adj / $8.2B equity) -- attractive

These implied multiples are internally consistent and do not require heroic assumptions.

**EV/EBIT Fair Value: $218**

---

## Method 3: Owner Earnings Yield (Cross-Check, not weighted)

Per valuation-methods skill, OEY is the primary method for Tier A. FDS is Tier B, so this serves as a sanity check only.

### Owner Earnings Calculation

```
FCF (FY2025):           $617M
- SBC:                  -$61M
- Growth Capex estimate: -$30M (FY2025 capex $109M; ~$79M maintenance = depreciation ~$72M x 1.1; growth capex = $109M - $79M = $30M)
= Owner Earnings:        $526M

Owner Earnings Yield = $526M / $7,600M market cap = 6.9%
Expected Growth: 5-6% (organic ASV growth)
OEY + Growth = 6.9% + 5.5% = 12.4%

vs WACC 9.0% --> Spread = +3.4pp (positive, indicates value creation)
```

### Reverse DCF Check

What growth does the current price ($204) imply?

From the sensitivity matrix:
- At WACC 9%, FV = $204 corresponds approximately to growth = **2.5-3.0%** (interpolating between $211 at 3% and $227 at 4.5%)

**Implied growth at current price: ~3%**

My base case growth estimate: 6%. The market is pricing in approximately half my growth rate. This suggests either:
(a) The market is right and AI/competition will halve FDS's growth (bear thesis), or
(b) The market is over-discounting temporary margin compression and AI fears (bull thesis)

**Assessment:** At 3% implied growth, the market is pricing FDS as if it were a mature utility with no growth tailwinds. Given 5.9% current organic ASV growth, 95%+ retention, and the wealth vertical growing at 10%, this seems pessimistic. However, the risk assessment identified 3 correlated HIGH risks (AI disruption, unit economics deterioration, competitive squeeze), which provides some justification for the market's skepticism.

---

## Method Reconciliation

| Method | Fair Value | Weight | Weighted |
|--------|-----------|--------|----------|
| DCF (SBC-adjusted) | $244 | 60% | $146 |
| EV/EBIT (15x, SBC-adj) | $218 | 40% | $87 |
| **Weighted Average** | | **100%** | **$233** |

**Divergence between methods: 11.9%** -- ACCEPTABLE (well below 30% threshold).

The convergence is reassuring. Both methods, using different approaches, arrive at $218-$244 range.

**Owner Earnings Yield cross-check:** OEY + Growth = 12.4% vs WACC 9.0% = positive spread (+3.4pp). Confirms the stock offers value creation at current price.

**Reverse DCF cross-check:** Market implies ~3% growth vs my 6% base. Either market is right or there is mispricing.

### Final Fair Value Determination

The weighted average is $233. However, I apply a **conservative bias** given:

1. **HIGH DCF sensitivity (87% FV spread, 74.9% TV as % of EV):** The DCF result is unreliable as a point estimate
2. **3 correlated HIGH risks** identified by risk-identifier: AI disruption + unit economics + competitive squeeze could materialize simultaneously
3. **MEDIUM-HIGH risk score:** Higher than typical Tier B
4. **Margin compression with uncertain duration:** If cloud investment lasts 3+ years, current margins are the "new normal"

I round down to **$225** (approximately 3.5% conservative haircut to weighted average).

This is $5 below the thesis FV of $230, reflecting the valuation-specialist's independent calculation with explicit SBC adjustments throughout.

---

## Scenarios

| | Bear | Base | Bull |
|--|------|------|------|
| **Revenue Growth** | 4% (ASV stalls, wealth slows) | 6% (ASV 5.5-6%, wealth +10%) | 8% (AI products, institutional recovery) |
| **Adj Operating Margin** | 33% (no recovery) | 36% (normalization FY2028) | 38% (expansion) |
| **SBC-Adj FCF Margin** | 21% | 24% | 27% |
| **WACC** | 10.5% | 9.0% | 8.0% |
| **Terminal Growth** | 2.0% | 2.5% | 3.0% |
| **EV/EBIT Multiple** | 12x | 15x | 18x |
| **DCF FV (SBC-adj)** | $166 | $244 | ~$310 |
| **EV/EBIT FV (SBC-adj)** | $174 | $218 | $265 |
| **Blended FV** | **$169** | **$233** | **$292** |
| **Rounded FV** | **$170** | **$225** | **$290** |
| **Probability** | **25%** | **50%** | **25%** |

### Bear Case Detail ($170)
- AI disruption accelerates: buy-side headcount falls 3-5%/year, FDS loses per-seat revenue
- Cloud transition costs overrun: adjusted operating margin stays at 33-34%, never returns to 36%+
- CUSIP antitrust adverse ruling reduces licensing revenue by 30%
- Bloomberg/SPGI competitive squeeze limits pricing power
- Growth decelerates to 4%, stock re-rates to 12x (current level = no recovery)

### Base Case Detail ($225)
- Cloud transition completes FY2028, margins normalize to 36% adjusted
- ASV growth stabilizes at 5-6%, driven by wealth (+10%) and Asia (+8%)
- AI creates new revenue streams (Mercury) but also reduces some buy-side seats (net neutral to mildly positive)
- Multiple recovers to 15x as investment phase ends and growth stabilizes
- Buyback ($1B authorized) provides 3-5% annual EPS accretion

### Bull Case Detail ($290)
- Mercury AI drives $100M+ in net new ASV within 2 years
- Wealth vertical accelerates to 12-15% growth, becoming 25%+ of total ASV
- Cloud-native platform enables margin expansion beyond historical levels
- Interest rate cuts drive capital markets recovery, buy-side hiring resumes
- Market re-rates to 18x as growth reaccelerates to 7-8%

### Expected Value

```
EV = ($170 x 25%) + ($225 x 50%) + ($290 x 25%)
EV = $42.50 + $112.50 + $72.50
EV = $227.50
```

---

## Valuation Summary

```
Precio actual:             $204.22
Fair Value (Base):         $225
Expected Value:            $228

MoS vs Base FV:           +10.2%
MoS vs Expected Value:    +11.5%
MoS vs Bear Case:         -16.7% (NEGATIVE -- price is ABOVE bear case)
```

### Comparison to Peer Multiples

| Metric | FDS (at $204) | FDS (at FV $225) | MORN (peer) | Sector Median |
|--------|---------------|------------------|-------------|---------------|
| P/E | 13.0x | 14.3x | 18.0x | ~28x |
| EV/EBIT | 12x | 13.2x | ~17x | ~27x |
| FCF Yield | 8.1%* | 7.4%* | 5.6% | ~3.5% |
| EV/Revenue | 3.4x | 3.7x | ~4x | ~10x |

*SBC-adjusted FCF yield

At my FV of $225, FDS would trade at P/E 14.3x -- still well below MORN (18x) and far below sector median (~28x). This is NOT aggressive. It implies the market continues to apply a significant discount for AI/competition risk, with only partial recovery from current trough levels.

### Validation vs Precedents

From decisions_log.yaml:
- **Tier B typical MoS acceptance:** 20-25%
- **ROP standing order:** $300 = 22% MoS for Tier B (upper end)
- **FDS at $204:** 10% MoS vs $225 FV -- BELOW the 20-25% typical range

This confirms the thesis conclusion: **$204 is NOT a compelling entry point for Tier B.** The MoS is insufficient given the MEDIUM-HIGH risk profile and 3 correlated HIGH risks.

**Entry at $180:** MoS = 20% vs $225 FV -- consistent with Tier B precedents.
**Entry at $170:** MoS = 24% vs $225 FV -- consistent with risk-identifier's recommendation ($160-170 range) given elevated risk.

---

## Sensitivity Tables (DCF Focus)

### WACC vs Growth (SBC-adjusted FV)

| | WACC 7.5% | WACC 8.0% | WACC 9.0% | WACC 10.0% | WACC 10.5% |
|---|-----------|-----------|-----------|------------|------------|
| **Growth 3%** | $284 | ~$260 | $211 | ~$185 | $166 |
| **Growth 4%** | ~$295 | ~$270 | ~$219 | ~$192 | $172 |
| **Growth 5%** | ~$316 | ~$290 | ~$233 | ~$200 | $185 |
| **Growth 6%** | $328 | ~$305 | $244 | ~$209 | $192 |
| **Growth 7%** | ~$340 | ~$315 | ~$253 | ~$218 | $200 |
| **Growth 8%** | $376 | ~$340 | $281 | ~$235 | $221 |

**Key breakeven points:**
- FV = $204 (current price): Growth 2.5-3% at WACC 9% -- market implied
- FV = $180 (entry target): Growth ~2% at WACC 9%, or Growth 6% at WACC 10.5%
- FV = $300 (bull): Growth 8%+ at WACC 8% -- requires optimistic assumptions

### EV/EBIT Multiple Sensitivity

| Multiple | FV (SBC-adj EBIT $632M) |
|----------|------------------------|
| 12x | $174 |
| 13x | $191 |
| 14x | $207 |
| **15x** | **$218** |
| 16x | $235 |
| 17x | $252 |
| 18x | $268 |
| 20x | $302 |

At the current price ($204), FDS is trading at ~14x SBC-adjusted EBIT. My fair multiple of 15x implies only a modest re-rating.

---

## META-REFLECTION

### Dudas/Incertidumbres

- **SBC adjustment methodology:** I applied a flat 10% haircut to DCF values and deducted SBC from EBIT. This is simple but imprecise. A more rigorous approach would model SBC growth separately (SBC could grow faster than revenue if FDS needs to compete for AI talent). If SBC grows to 4-5% of revenue (still below software average), the impact on FV would be an additional 3-5% haircut. I chose not to apply this because FDS's historical SBC has been remarkably stable at 2.5-3% of revenue.

- **Terminal value dependency at 75%:** This is a structural weakness of DCF for subscription businesses with high margins and low capex. The business generates most of its value from the perpetuity. This makes the FV highly sensitive to terminal growth rate (2.0% vs 3.0% = ~$30-40 difference in FV). I cannot resolve this -- it is inherent to the business model. The EV/EBIT method provides a useful anchor.

- **3 correlated HIGH risks:** The risk-identifier flagged AI disruption, unit economics deterioration, and competitive squeeze as correlated. If all three materialize simultaneously (which they could -- AI enables competition AND reduces seats AND pressures pricing), the bear case could be more severe than $170. A "deep bear" of $130-140 is plausible if ASV growth goes to 2-3% and margins compress to 30%. I did NOT model this as a separate scenario because its probability is low (10-15%), but it represents meaningful tail risk.

- **Multiple selection for EV/EBIT:** Choosing 15x is judgment-heavy. Reasonable people could argue for 13-17x. At 13x, FV = $191 (below current price). At 17x, FV = $252. The range is wide, which reduces confidence in the point estimate.

### Sensibilidad Preocupante

- **DCF FV changes >20% with reasonable input variations:** Moving from 6% growth to 4% growth (plausible if AI disruption accelerates) drops SBC-adjusted FV from $244 to ~$178 -- a 27% decline. This is concerning because the growth rate uncertainty is genuine (current organic ASV is 5.9% but decelerating).

### Discrepancias con Thesis

- **FV $225 vs thesis $230:** Minor difference (-2.2%). The thesis used a round number; my calculation with explicit SBC adjustment throughout produces $225. Not a meaningful discrepancy.

- **Entry recommendation:** The thesis suggests $180 entry. The risk-identifier suggests $160-170. My valuation supports $180 (20% MoS vs $225 FV), but given the MEDIUM-HIGH risk score and 3 correlated risks, the risk-identifier's more conservative range ($160-170, providing 24-29% MoS) has merit. I lean toward $175 as a compromise: 22% MoS consistent with ROP precedent (22% MoS for Tier B).

### Sugerencias para el Sistema

- **Create standardized SBC adjustment protocol:** Currently each valuation treats SBC differently. After INTU precedent (SBC deducted for software), we should have a standard framework: (a) SBC < 2% of revenue: ignore, (b) SBC 2-5%: deduct from FCF/EBIT, (c) SBC > 5%: deduct and model dilution separately.

- **Add "implied growth rate" to standard DCF output:** The reverse DCF question ("what growth does the market price in?") is one of the most powerful analytical tools, but it requires manual interpolation from the sensitivity table. Adding it to the dcf_calculator.py tool would improve efficiency.

### Preguntas para Orchestrator

1. Should the entry price for FDS be revised from $180 (thesis) to $175 (compromise between thesis $180 and risk-identifier $160-170)?

2. The SBC adjustment reduced all FV estimates by ~10%. Should we retroactively apply this to other software companies in the universe (VRSK, MORN, PAYC, etc.) for consistency? This could change their entry prices.

3. Given that FDS is 12.2% above entry ($204 vs $180), it is listed as "actionable" in the quality universe. But given the MEDIUM-HIGH risk score, should we require a hard gate (Q2 FY2026 earnings in March 2026) before setting a standing order?

---

**Sources:**
- DCF outputs from `tools/dcf_calculator.py` (3 separate runs)
- Quality profile from `tools/quality_scorer.py`
- Current price from `tools/price_checker.py`
- Peer prices from `tools/price_checker.py`
- Thesis projections from `thesis/research/FDS/thesis.md`
- Moat assessment from `thesis/research/FDS/moat_assessment.md`
- Risk assessment from `thesis/research/FDS/risk_assessment.md`
- Precedents from `learning/decisions_log.yaml`
- Principles from `learning/principles.md`
