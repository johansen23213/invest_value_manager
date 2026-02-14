# Counter-Analysis: ACGL (Arch Capital Group Ltd.)

## Fecha: 2026-02-13

## Resumen Ejecutivo

The thesis for ACGL is among the better-constructed ones in our pipeline -- the analyst correctly identifies P/B vs ROE as the primary framework for an insurer, acknowledges cycle risk, and documents QS adjustments with evidence. However, the thesis has significant blind spots: (1) the Chairman just sold $20M of stock in a single transaction, the largest insider sale in recent history, (2) the "fair" P/B of 1.85x is anchored to peak-cycle ROE and exceeds ACGL's own 5-year median P/B of 1.64x, (3) the Q4 2025 revenue miss of -13% vs consensus is a leading indicator the thesis largely brushes off, (4) social inflation risk to casualty reserves is completely absent from the thesis, and (5) the moat assessment scores 22/25 (near-perfect) for a culture-based advantage that has never been tested in a true post-ILS structural soft market. The thesis survives but requires material adjustments to fair value and entry price.

---

## Asunciones Clave Desafiadas

### 1. Sustainable ROE of 15-17% Through the Soft Market

**Thesis claim:** ACGL will sustain ROE of 15-17% even as the reinsurance cycle softens. This underpins the entire P/B valuation.

**Evidence in contra:**
- The thesis uses 2023-2025 ROE of 17-34% as the anchor. But the last comparable soft market (2016-2019) saw ROE drop to 7% (2017, cat year) and 10% (2018). The thesis acknowledges 2017 at ~7% but dismisses it as "anomalous catastrophe year."
- In the 2016-2019 soft market, ACGL's combined ratio was 88.2% (2016), 88.8% (2017), 81.0% (2018). The thesis base case assumes CR of 86-90%. But the CURRENT soft market has STRUCTURAL differences: ILS capital is now $120B+ and growing $10-20B/year (per Artemis/HSCM), creating permanent capacity that did not exist in the prior soft market. This means the next hard market may take LONGER to arrive and the soft market may be DEEPER.
- Goldman Sachs initiated with a SELL rating and $93 price target. While contrarian, Goldman is not a noise signal -- they have a specific thesis around cycle mean-reversion that deserves acknowledgment.
- If ROE normalizes to 12% (the bear case in the thesis), justified P/B drops to 1.3x and fair value drops to $85. The thesis assigns only 25% probability to this. Given that the soft market is already confirmed and accelerating, this probability is too low. I would assign 35-40%.

**Severidad: HIGH**

**Resolucion sugerida:** The base case should use mid-cycle ROE of 13-15% (not peak-adjacent 15-17%). This reduces fair P/B from 1.85x to approximately 1.5-1.7x, and fair value from $120 to $100-110. The bear case probability should be increased to 35%.

---

### 2. Fair Value of $120 (P/B 1.85x) Is Generous

**Thesis claim:** Fair P/B of 1.85x is conservative, below the Gordon Growth justified P/B of 3.33x.

**Evidence in contra:**
- ACGL's 5-year MEDIAN P/B is 1.64x. The thesis proposes a "fair" P/B of 1.85x -- a 13% PREMIUM to the median. This is being proposed at the START of a confirmed soft market, when multiples historically contract.
- ACGL's 5-year P/B range is 1.3x (Dec 2020) to 2.1x (Dec 2022). The current 1.53x is roughly mid-range, not deeply discounted. The thesis frames it as undervalued, but 1.53x on peak-cycle book value may be fully fair.
- The analyst acknowledges the Gordon Growth model produces a "theoretical" 3.33x that the market has "NEVER paid." This is honest. But then the base case of 1.85x is still above the 5-year median. If the market has historically refused to pay more than ~2.1x even at peak earnings, why is 1.85x at the START of a soft market the base case?
- Analyst consensus average price target is $108.67 (9 Buy, 8 Hold, 1 Sell). Our thesis FV of $120 is 10% ABOVE the average analyst target. Post-adversarial, our system has a documented pattern of FV overstatement (14/16 positions in the adversarial review project had inflated FV, avg -19%).
- Mizuho: $102 target. Wells Fargo: $109. RBC: $115. Goldman: $93. Our $120 is the most optimistic view among all coverage I can find.

**Severidad: HIGH**

**Resolucion sugerida:** Reduce base case fair P/B to 1.7x (closer to median but slightly above given quality premium). This gives FV = $65.11 x 1.7 = $111. With weighted average methodology: (P/B method $111 at 60%) + (P/E method $116 at 40%) = weighted $113. Round to $110. Entry price should be $82-85 (25% MoS for Tier B).

---

### 3. The QS Adjustment from 57 to 68 (+11 Points) Is Justified but Conservative -- The Moat Assessment's QS of 78-82 Is NOT

**Thesis claim:** QS adjusted to 68 (Tier B). Moat assessment suggests 78-82 (Tier A).

**Evidence in contra:**
- The thesis analyst correctly adjusts +8 for ROIC structural distortion (using ROE) and +3 for GM trend data gap. This is well-documented. The net 68 is defensible.
- HOWEVER, the moat assessment independently suggests QS 78-82 (Tier A), which represents a +21-25 point adjustment from the tool. This is ABOVE the max QS adjustment of +20 without committee approval (per the ROP precedent). The moat assessor appears to have exceeded their mandate.
- The moat assessment adds points for market position (5/8), shareholder returns (buybacks), and full ROIC replacement with ROE. While each is individually defensible, the cumulative effect pushes ACGL from low Tier B (57) to mid Tier A (80) -- a transformation that should be treated with extreme skepticism given the documented pattern of QS inflation in our system (Error #43: 5/6 Tier A positions had inflated QS).
- At 68, ACGL is Tier B. At 78+, it would be Tier A. This tier boundary matters: it determines MoS expectations, sizing, and mental model. Given the system's DOCUMENTED HISTORY of QS inflation, the conservative 68 should be maintained.
- The risk assessment correctly notes: "a company entering a soft market with peak earnings deserves a more conservative treatment" -- this argues AGAINST upward QS adjustment.

**Severidad: MODERATE**

**Resolucion sugerida:** Maintain QS at 68 (Tier B) as the thesis recommends. Reject the moat assessment's 78-82 suggestion. The insurance-specific QS adjustment protocol should cap at +15 until the quality_scorer.py is updated with an --insurer flag.

---

### 4. Chairman Pasquesi's $20M Stock Sale Is Material and Underdiscussed

**Thesis claim:** Insider selling is "moderate and appears routine (scheduled dispositions). This is NEUTRAL."

**Evidence in contra:**
- John Pasquesi, Chairman of the Board, sold 203,866 shares on December 12, 2025 at $93.90 ($19.1M), plus 8,800 shares on December 15 at $94.17 ($829K). Total: approximately **$20M in a single week**.
- This is not a routine scheduled sale of a few thousand shares. This is the CHAIRMAN liquidating $20M in stock, representing a significant portion of his holdings, within days.
- The CFO Francois Morin sold $757K separately (November 2025). Maamoun Rajeh (President, Arch Re) sold 10,000 shares (August 2025). Total insider selling in the quarter: ~$21M.
- The thesis says "no pattern of aggressive liquidation." A $20M sale by the Chairman IS aggressive liquidation. The fact that it occurred in December 2025, shortly before Q4 earnings and at the onset of the confirmed soft market, is a timing signal that deserves investigation.
- Marc Grandisson (former CEO) sold ~$45M since 2021 while retaining $220M+. This is presented as "confidence." But net selling post-CEO transition is a data point, not a comfort factor.
- For context: insider ownership is only 3.2-4.2% of shares. The $20M sale represents a meaningful reduction in Pasquesi's personal stake.

**Severidad: HIGH**

**Resolucion sugerida:** Reclassify insider activity from NEUTRAL to NEGATIVE. A $20M Chairman sale at the start of a soft market is a material negative signal. This should be documented as a risk factor and considered when determining MoS.

---

### 5. Social Inflation / Casualty Reserve Risk Is Completely Absent from the Thesis

**Thesis claim:** [Not mentioned at all. The thesis does not contain the words "social inflation" or "nuclear verdicts."]

**Evidence in contra:**
- Nuclear verdicts hit 135 cases and $31.3B in awards in 2024 -- the highest since tracking began. This is a secular trend, not cyclical.
- US liability claims have climbed 57% over the past decade (Swiss Re Institute). Annual increase of 7% in 2023, far outpacing economic inflation.
- Swiss Re added $2B+ to US casualty reserves in Q3 alone. The industry-wide concern about reserve adequacy for 2019-2021 accident years is well-documented.
- ACGL's thesis notes "favorable prior-year development of $167M" as a positive sign. But consistent favorable development can mask inadequacy: if the industry as a whole is strengthening reserves and ACGL continues to release reserves, it could mean ACGL is BEHIND the curve, not ahead of it.
- The risk assessment mentions social inflation in passing (Risk #7) but rates it "Baja" probability. Given the industry data, this is too generous. The probability of social inflation continuing to impact casualty reserves is HIGH -- it is a secular trend, not an "if."
- ACGL is "leaning into casualty and moderating property" per management commentary. This means they are INCREASING exposure to the segment most affected by social inflation at the same time they are reducing exposure to property (where pricing is softening). This is a double risk: soft property market + social inflation in casualty.

**Severidad: HIGH**

**Resolucion sugerida:** Social inflation should be added as a standalone HIGH-severity risk. The thesis should explicitly address: (1) what % of ACGL's reserves are casualty/liability, (2) what the reserve development trajectory looks like for accident years 2019-2021 specifically, (3) whether ACGL's shift toward casualty increases or decreases this risk. This is a gap that requires R2-level investigation before committee approval.

---

## Desafios por Categoria

### Negocio

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | "Underwriting discipline moat" is a culture moat that has never been tested in a structural soft market with permanent ILS capital | ILS capital now $120B+ and growing $10-20B/yr; cat bonds at record $58B. 2016-2019 soft market did NOT have this structural capital. The next cycle may be fundamentally different. | MODERATE |
| 2 | CEO transition risk downplayed | Papadopoulo is a veteran, but Grandisson's departure + board member Vollaro leaving May 2026 = multiple governance changes simultaneously. Two departures in 18 months from a culture-dependent moat. | MODERATE |
| 3 | Revenue miss in Q4 2025 (-13% vs consensus) is a leading indicator | NPW in insurance declined 4%. This is the EARLIEST signal of cycle-driven volume pressure. The thesis presents this as "positive discipline" but the market sees deceleration. If revenue continues declining while CR rises, earnings compression could be faster than modeled. | MODERATE |
| 4 | Three-platform diversification benefit may be overstated | Mortgage segment is only ~6% of GPW. Counter-cyclical benefit is mathematically limited. If P&C earnings decline 30% in a soft market, mortgage's $1B underwriting income offsets only ~20% of the shortfall. | LOW |
| 5 | ACGL shifting from property to casualty at worst possible time | Management says "leaning into casualty and moderating property." But casualty is the segment most exposed to social inflation, nuclear verdicts, and litigation funding. This strategic shift increases reserve risk. | MODERATE |

### Valoracion

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | FV of $120 is above ALL analyst targets except the most bullish | Consensus avg $108.67. Mizuho $102. Wells Fargo $109. RBC $115. Goldman $93. Our $120 is the outlier. System documented pattern of FV inflation (14/16 positions). | HIGH |
| 2 | P/B base of 1.85x exceeds 5-year median of 1.64x | Proposing above-median valuation at start of soft market. Historically P/B contracts in soft markets (1.3x in Dec 2020). If P/B reverts to median (1.64x), FV = $107. If soft market pushes to 1.3x, price = $85. | HIGH |
| 3 | Beta of 0.38-0.42 makes WACC artificially low | Beta 0.42 gives Ke ~6.5%. But ACGL has declined 6.8% vs Dow +7.1% over 52 weeks, implying actual risk is higher than beta suggests. Using 0.7 beta (more typical for insurers), Ke = 7.9%, reducing justified P/B from 3.33x to ~2.0x. The thesis acknowledges this in meta-reflection but does not adjust. | MODERATE |
| 4 | Bear case probability of 25% is too low | Soft market already confirmed and accelerating. Cat risk is unpredictable. Both risks co-occurring (soft market + major cat) is the scenario the thesis assigns implied probability of ~6%. Historical precedent: this happened in 2017. | MODERATE |
| 5 | Normalized EPS of $10.50 may be too high | Risk assessment suggests mid-cycle EPS of $8-9. If we use $9 at 11x P/E = $99 (i.e., ACGL is fairly valued TODAY, not at a 20% discount). The thesis uses $10.50 which is above even the 3-year average for a company ENTERING a soft market. | MODERATE |

### Riesgos

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | Social inflation completely missing from thesis | 135 nuclear verdicts in 2024, $31.3B awards. Liability claims up 57% in a decade. Swiss Re added $2B+ to casualty reserves. ACGL shifting toward casualty exposure. | HIGH |
| 2 | Chairman's $20M stock sale misclassified as "NEUTRAL" | $20M single-week sale by Board Chairman. Occurs at start of soft market. Largest insider transaction in recent history. | HIGH |
| 3 | DTA amortization cliff late 2026/early 2027 underexplored | $1.2B deferred tax asset declining ~$100M/year. When exhausted, effective tax rate steps up. The thesis mentions it but doesn't quantify the EPS impact. At $100M/year, this is ~$0.27/share drag. | MODERATE |
| 4 | Bermuda tax evolution risk may be understated | Bermuda CIT is 15% but Pillar Two is a "living framework." OECD may expand scope. QRTCs are subject to legislative continuation. The tax advantage vs onshore competitors is permanently narrowed. | LOW |
| 5 | Climate catastrophe models are systematically wrong on tails | Insurance industry surprised by losses exceeding models in 5 of last 8 years. If models underestimate by 30%, PML of $1.9B could become $2.5B+ actual losses. | MODERATE |

### Timing

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | We are buying at the START of a confirmed soft market, not at the trough | Soft market officially began at Jan 2026 renewals (-14.7% property cat). Historical soft markets last 3-5 years. Entry NOW means potentially 2-4 years of deteriorating fundamentals before recovery. | HIGH |
| 2 | Better entry likely available in 12-18 months | If EPS normalizes to $8-9 and P/B compresses to 1.3-1.5x, stock could trade at $85-97 in 2027. Patience may be rewarded. | MODERATE |
| 3 | Q1 2026 results will show California wildfire impact + first soft market quarter | Q1 already has $547M wildfire losses. Combined with soft market pricing, Q1 2026 could be the inflection quarter that resets expectations. Buying before this data is available adds information risk. | MODERATE |
| 4 | Hurricane season 2026 (Jun-Nov) adds binary event risk | At current price, a major hurricane could drop the stock 15-25% (per risk assessment). Waiting until post-hurricane season dramatically reduces this binary risk. | LOW |

---

## Conflictos con Otros Analisis

### Moat Assessment vs Thesis: QS Divergence

The moat assessment produced QS Adjusted of 78-82 (Tier A), while the thesis uses 68 (Tier B). This is a +10-14 point divergence. The moat assessor's score represents a +21-25 point adjustment from the tool score (57), which exceeds our system maximum of +20 without committee approval (per the ROP precedent). The thesis is MORE conservative and should be the reference score.

### Risk Assessment vs Thesis: Cycle Positioning

The risk assessment explicitly asks: "Should the fundamental analyst use mid-cycle earnings ($8-9) rather than current earnings ($11.47) for the valuation?" This is a direct challenge to the thesis's normalized EPS of $10.50. The risk assessment also notes that "the valuation specialist should use mid-cycle earnings" -- a recommendation the thesis does not follow. Using $9 normalized EPS at 12x P/E gives FV = $108, not $120.

### Risk Assessment vs Thesis: Market Pricing

The risk assessment provides a detailed analysis of "Why P/E is Only 8.6x" and concludes with a balanced question: "Is the market correctly pricing the cycle turn (in which case 8.6x is fair or even generous), or is it underestimating Arch's ability to navigate cycles better than peers?" The thesis implicitly assumes the latter. I lean toward the former -- the market may be correct that peak-cycle earnings at 8.6x is fair value for a company entering a soft market.

---

## Veredicto Global

| Metric | Valor |
|--------|-------|
| Desafios HIGH/CRITICAL | **6** of 19 total |
| Desafios no resueltos por thesis | **5** (social inflation gap, Chairman sale misclassification, mid-cycle EPS, FV above consensus, timing at soft market start) |
| Veredicto | **MODERATE COUNTER** |

### Score: 13/19

Breakdown:
- Business challenges: 4/10 (strong business, real but manageable cycle risk)
- Valuation challenges: 6/10 (FV clearly overstated, needs reduction)
- Risk challenges: 5/10 (social inflation gap is serious, insider sale misclassified)
- Timing challenges: 4/10 (entering at start of soft market is suboptimal)

Deductions for thesis self-awareness: -2 (the thesis has unusually good autocritica section that anticipates several of these challenges)

### Interpretacion:

**MODERATE COUNTER:** The thesis correctly identifies ACGL as a high-quality insurer with genuine competitive advantages. The business is real, the moat is real, and the track record is exceptional. HOWEVER, the valuation is anchored to peak-cycle metrics, the fair value of $120 exceeds analyst consensus and the stock's own historical P/B range, insider selling is material and misclassified, social inflation is a blind spot, and the timing (entering at the START of a soft market) adds risk that is not reflected in the MoS.

The thesis does NOT need to be rejected. It needs to be ADJUSTED:
- FV: $120 --> $105-110
- Entry: $92 --> $80-85
- Bear probability: 25% --> 35%
- Social inflation: must be investigated in R2 before committee
- Insider selling: reclassify to NEGATIVE

---

## Recomendacion al Investment Committee

Before ACGL can proceed to R4 (committee approval), the following must be resolved:

1. **REDUCE fair value from $120 to $105-110.** The $120 is the most bullish view among all analysts. Apply mid-cycle ROE (13-15%) and P/B closer to the 5-year median (1.65-1.7x). The risk assessment's own recommendation of mid-cycle EPS ($8-9) supports this.

2. **REDUCE entry price from $92 to $80-85.** At $92 with FV $110, MoS is only 16% -- below the Tier B minimum pattern (20-25%). An entry at $82 provides 25% MoS.

3. **INVESTIGATE social inflation exposure.** This is a material gap. The thesis must address: (a) what % of reserves are casualty/liability, (b) reserve development for 2019-2021 accident years, (c) whether the shift from property to casualty increases this risk.

4. **RECLASSIFY insider selling.** The Chairman's $20M sale is not routine. Acknowledge it as a NEGATIVE signal and factor into conviction assessment.

5. **INCREASE bear case probability to 35%.** The soft market is confirmed. ILS capital is structural. Both increase the probability and potential duration of below-average returns.

6. **DOCUMENT the timing risk explicitly.** We are entering at the top of the cycle, not the bottom. The thesis should acknowledge this and explain why NOW rather than in 12-18 months when fundamentals will have normalized.

If these adjustments are made, ACGL at $80-85 becomes a compelling Tier B insurance position with adequate MoS and clear catalysts (cycle turn, buyback accretion, mortgage stability). At $92-100, the risk/reward is inadequate given the cycle positioning.

---

## META-REFLECTION

### Dudas/Incertidumbres
- I could not find granular data on ACGL's casualty reserve composition by accident year. The social inflation challenge is documented at the industry level but I cannot confirm how much ACGL-specific exposure exists. It is possible that ACGL's discipline extends to reserving and they are ahead of the industry on this. But the thesis provides zero evidence either way.
- Historical combined ratio data for 2016-2019 was incomplete from web sources. I found 88.2% (2016), 88.8% (2017), 81.0% (2018), ~84% (2019 est.). The thesis cites CR deterioration to 95% in the bear case, which seems conservative (ACGL never hit 95% except possibly in catastrophe quarters). This actually weakens the bear case somewhat.
- The Chairman's stock sale COULD be pre-planned (Rule 10b5-1). I could not confirm this. If it is a scheduled plan set up months ago, it is less concerning. If it is discretionary, it is very concerning.
- I was unable to retrieve full historical P/B data from web sources. The 5-year range of 1.3x-2.1x is based on search results from YCharts, but I could not independently verify annual figures for all years.

### Limitaciones de Este Analisis
- No access to 10-K filings for detailed reserve triangles, casualty reserve breakdown, or historical combined ratios by segment
- Could not confirm whether Pasquesi's stock sale was a 10b5-1 pre-planned transaction or discretionary
- Goldman Sachs' specific bear thesis was not available in search results -- only the rating and price target ($93)
- ILS market growth projections are consensus estimates; actual capital deployment could be higher or lower

### Sugerencias para el Sistema
- The quality_scorer.py --insurer flag should be implemented before evaluating more insurance companies. The current tool systematically underscores ALL insurers, requiring manual adjustment that introduces subjectivity.
- Social inflation should be added as a standard risk factor in the risk-identifier agent's checklist for ANY company with casualty/liability insurance exposure.
- A "cycle position" field should be added to the quality universe for cyclical businesses (insurance, commodities, banking) to flag when we are buying at cycle peaks.

### Preguntas para Orchestrator
1. Given that ACGL at $99.85 is still 8.5% above our $92 entry price, and this analysis suggests the entry should be $80-85, there is NO urgency. Should we defer R4 until the price approaches the revised entry range?
2. Should we investigate Goldman Sachs' specific bear thesis before proceeding? Their $93 target is close to our current standing order of $92, which suggests they see fundamental issues we may be missing.
3. The social inflation gap is material. Should we commission a specific R2 investigation on ACGL's casualty reserve composition before proceeding to committee?
4. The pattern of our FV estimates being consistently higher than analyst consensus (documented: 14/16 positions had inflated FV) -- should we implement a systematic "consensus discount" of 5-10% as a sanity check?

---
