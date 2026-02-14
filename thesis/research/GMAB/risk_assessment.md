# Risk Assessment: GMAB (Genmab A/S)

## Fecha: 2026-02-12

## Risk Score: MEDIUM-HIGH

**Rationale:** The Merus acquisition has fundamentally transformed Genmab's risk profile from "asset-light royalty collector with net cash" to "levered biotech with $5.5B debt, multiple binary clinical readouts, and own-commercialization execution risk." The thesis that GMAB is a low-risk quality compounder (QS 77 tool) needs to be qualified heavily by forward-looking risks that the legacy financial data does not capture.

---

## Matriz de Riesgos

| # | Categoria | Riesgo | Probabilidad | Impacto | Score | Mitigante |
|---|-----------|--------|-------------|---------|-------|-----------|
| 1 | Fundamental | Darzalex patent cliff / biosimilar entry (2028-2029) | Alta | Alto | CRITICAL | Pipeline diversification (Rina-S, petosemtamab) |
| 2 | Fundamental | Epcoritamab DLBCL-2 Phase 3 failure (1L DLBCL) | Media | Alto | HIGH | FL indication strong (Phase 3 met endpoints), combination trials |
| 3 | Fundamental | Own-commercialization execution failure | Media | Alto | HIGH | AbbVie partnership for epcoritamab; but Rina-S and petosemtamab are solo |
| 4 | Financiero | Merus acquisition leverage / debt servicing ($5.5B debt) | Media | Alto | HIGH | Target <3x leverage within 2 years; strong FCF generation |
| 5 | Fundamental | Petosemtamab Phase 3 failure (LiGeR-HN1/HN2) | Media | Alto | HIGH | Breakthrough Therapy Designation; strong Phase 2 data |
| 6 | Legal | AbbVie trade secret lawsuit (ProfoundBio/Rina-S) | Media | Alto | HIGH | Genmab refutes claims; pattern of AbbVie suing competitors |
| 7 | Competitivo | ADC/bispecific market crowding — Roche, Amgen, AZ, Pfizer | Alta | Medio | HIGH | Proprietary DuoBody/HexaBody platforms; first-mover in some indications |
| 8 | Regulatorio | IRA Medicare drug pricing — Darzalex could be selected | Media | Medio | MEDIUM | Darzalex is JNJ product; impact is on JNJ sales = lower royalties to GMAB |
| 9 | Geopolitico | Denmark/Greenland tariff risk (10-25% on Danish goods) | Baja | Medio | LOW | GMAB drugs not manufactured in/shipped from Denmark; IP-based model |
| 10 | Financiero | DKK/USD currency risk on reporting | Baja | Bajo | LOW | Reports in USD; DKK pegged to EUR; most revenue USD-denominated |
| 11 | Fundamental | Rina-S Phase 3 failure (RAINFOL-02, ovarian cancer) | Media | Medio | MEDIUM | BTD granted; encouraging Phase 1/2 data (55.6% ORR) |
| 12 | Fundamental | Pipeline concentration post-acasunlimab discontinuation | Media | Medio | MEDIUM | Three pillars remain: Epkinly, petosemtamab, Rina-S |
| 13 | ESG/Governance | 0% insider ownership — no skin in the game | Alta | Bajo | LOW | Institutional ownership 10.7%; Danish governance standards high |
| 14 | Valoracion | Value trap risk if pipeline disappoints + debt burden | Baja | Alto | MEDIUM | Near 52w low already; P/E 13x implies limited expectations |

---

## Top 3 Riesgos Criticos

### 1. Darzalex Patent Cliff and Revenue Concentration

- **Categoria:** Fundamental / Financiero
- **Descripcion:** Darzalex royalties represent approximately 60-65% of Genmab's total revenue (~$2.2B of ~$3.5-3.7B in 2025 guidance). Darzalex composition of matter patents expire in key markets: US composition patents March 2026, with US market exclusivity extending to ~2029 and EU loss of exclusivity expected ~2028. Multiple biosimilar developers are active: Celltrion (CT-P44, global Phase 3), Shanghai Henlius/Dr. Reddy's (HLX-15), and Xbrane Biopharma (preclinical). Worldwide Darzalex net sales were $11.7B in 2024, growing to est. $12.6-13.4B in 2025. Once biosimilars enter, typical erosion is 40-80% of branded sales within 3-5 years.
- **Evidencia:** DrugPatentWatch data shows US exclusivity ~2029; Celltrion announced global Phase 3 for CT-P44 biosimilar with EMA submission; GEN Engg News lists Darzalex in "Top 20 drugs heading for patent cliff 2026-2029."
- **Probabilidad:** Alta -- biosimilar entry is near-certain; the timing (2028-2030) and speed of erosion are the variables.
- **Impacto si materializa:** If Darzalex royalties decline 50% from peak by 2031 (~$1.1B lost annual revenue), that is approximately 30% of current total revenue. At current P/E multiples, stock could decline 25-40% unless pipeline products fill the gap. This is essentially a "ticking clock" — the question is whether the pipeline products ramp fast enough to offset.
- **Mitigante:** Pipeline diversification (petosemtamab $1B+ potential by 2029, Rina-S, Epkinly growing 73% YoY). JNJ has strong incentive to defend Darzalex patents aggressively. Subcutaneous formulation (Darzalex Faspro) may have additional patent protection.
- **Kill condition?:** YES — if biosimilar Darzalex is approved before pipeline products reach $1B+ annual revenue, the replacement gap could be terminal for the investment thesis. Monitor: (a) biosimilar approval timeline, (b) pipeline product ramp rates.

### 2. Merus Acquisition Leverage / Balance Sheet Transformation

- **Categoria:** Financiero / Fundamental
- **Descripcion:** Genmab's $8B acquisition of Merus (closed December 2025) was funded with ~$2.5B cash on hand + $5.5B new debt ($1.5B 6.25% secured notes due 2032, $1.0B 7.25% unsecured notes due 2033, plus ~$3B additional facilities). This transforms Genmab from a net cash company ($3.3B net cash as of Q3 2025) to a levered entity. The company targets gross leverage <3x within two years, but this depends on: (a) Darzalex royalties continuing to grow, (b) no major pipeline failures burning cash, (c) successful commercialization ramp. Interest expense alone could be $350-400M/year on $5.5B at 6.5-7.25% weighted average rate.
- **Evidencia:** Genmab Q3 2025 showed $3.4B cash, $142M debt (net cash $3.3B). Post-Merus, debt is ~$5.5B+ with cash substantially depleted. The quality_scorer.py output showing "Net Cash" and interest coverage 77.4x reflects PRE-acquisition financials. Post-acquisition, Net Debt/EBITDA is likely 3-4x and interest coverage drops to ~3-4x.
- **Probabilidad:** Media — the debt is real and already in place. The risk is that clinical failures or revenue shortfalls make deleveraging harder than planned.
- **Impacto si materializa:** If deleveraging fails (pipeline setbacks, Darzalex erosion faster than expected), Genmab could face: credit rating pressure, inability to invest in R&D, potential dilutive equity raise, or forced asset sales. In a stress scenario (EBITDA -30%), leverage could exceed 5x, potentially triggering covenant issues. Stock impact: -30-50%.
- **Mitigante:** Strong underlying FCF (~$1B+/year pre-acquisition); Darzalex still growing; target <3x within 2 years is achievable if base case holds.
- **Kill condition?:** YES — if Net Debt/EBITDA exceeds 4x for 2+ consecutive quarters, or if interest coverage falls below 2x. This signals the balance sheet is out of control.

### 3. Epcoritamab Phase 3 DLBCL-1 Failure + AbbVie Relationship Strain

- **Categoria:** Fundamental / Legal
- **Descripcion:** The EPCORE DLBCL-1 Phase 3 trial MISSED its primary endpoint of overall survival (OS HR 0.96, essentially no benefit vs standard of care) in relapsed/refractory DLBCL (January 2026). While secondary endpoints were positive (26% PFS reduction, higher CR rates), failing the primary endpoint is a major setback. Simultaneously, AbbVie has sued Genmab for trade secret misappropriation related to ProfoundBio's ADC technology (March 2025). While both parties claim the epcoritamab collaboration continues unaffected, trust damage is real. The next major data readout — EPCORE DLBCL-2 (first-line DLBCL) — is expected in 2026 and is critical.
- **Evidencia:** AbbVie and Genmab press releases (January 16, 2026) confirming primary endpoint miss. EPCORE FL-1 met dual primary endpoints (positive), providing partial offset. AbbVie lawsuit filed March 2025 in W.D. Washington. Epkinly sales growing ($281M in 2024, up 73% in Q1 2025) but still small relative to $3B+ blockbuster target.
- **Probabilidad:** Media — DLBCL-1 failure already occurred. DLBCL-2 readout risk is binary. AbbVie lawsuit outcome uncertain but pattern of AbbVie suing competitors suggests this may be aggressive IP enforcement rather than merit-based.
- **Impacto si materializa:** If DLBCL-2 also fails, Epkinly's path to $3B+ blockbuster status narrows significantly (limited to FL and smaller indications). Revenue impact: $500M-1B lost potential by 2030. If AbbVie lawsuit succeeds and injunctive relief is granted on Rina-S, Genmab loses its most promising wholly-owned ADC pipeline. Combined: stock impact -20-35%.
- **Mitigante:** FL indication strong; combination trials ongoing; AbbVie collaborations typically resilient to IP disputes; Genmab has other pipeline assets beyond epcoritamab.
- **Kill condition?:** CONDITIONAL — if DLBCL-2 fails AND AbbVie obtains injunction on Rina-S, that would be a kill condition. Either alone is manageable.

---

## Additional Material Risks (Ranked by Severity)

### 4. Own-Commercialization Execution Risk

- **Categoria:** Fundamental
- **Descripcion:** Genmab is transitioning from a royalty/licensing model to own-commercialization (Rina-S, petosemtamab, TIVDAK in Europe). This requires building commercial infrastructure (sales teams, medical affairs, market access) across Europe and Japan — capabilities Genmab has never had to execute at scale. Manufacturing is outsourced to CDMOs, adding supply chain risk.
- **Evidencia:** Genmab shuffled C-suite roles to create Chief Commercial Officer and Chief Operations Officer positions (FiercePharma). JPMorgan downgraded in 2024 citing "underappreciated increases in operational expenditure" specifically from commercialization buildout. HC Wainwright cut 2026 EPS estimates from $2.14 to $1.68, reflecting higher spending.
- **Probabilidad:** Media — executing a first-time commercial launch in oncology is inherently risky.
- **Impacto si materializa:** Higher-than-expected SG&A burn, delayed launches, suboptimal market penetration. Could consume $200-400M in additional spending over 2-3 years without commensurate revenue, compressing margins from current ~32% operating to potentially 15-20%.
- **Mitigante:** AbbVie handles epcoritamab commercial (shared); experienced hires from big pharma; focused oncology market (smaller sales force needed vs primary care).

### 5. Petosemtamab Phase 3 Binary Risk

- **Categoria:** Fundamental
- **Descripcion:** Petosemtamab (from Merus acquisition, $8B) is in two Phase 3 trials for head and neck cancer (LiGeR-HN1 and LiGeR-HN2), with interim readouts expected in 2026. This is the crown jewel of the Merus deal — if it fails, Genmab paid $8B for a pipeline without a lead asset. Genmab's own target: $1B+ annual sales by 2029, multi-billion thereafter.
- **Evidencia:** FDA granted two Breakthrough Therapy Designations (positive signal). Phase 2 data at ASCO 2025 was "compelling" per management. But Phase 2 to Phase 3 success rates in oncology are ~30-40%.
- **Probabilidad:** Media (35-45% failure probability, given BTD and strong Phase 2 data, lower than base rate).
- **Impacto si materializa:** If both Phase 3 trials fail, the Merus acquisition would be a massive write-down ($5-7B goodwill impairment). With $5.5B debt, this creates existential balance sheet pressure. Stock impact: -40-60%.
- **Mitigante:** Two independent trials increase probability that at least one succeeds; BTD suggests FDA confidence; Phase 2 data strong.

### 6. ADC/Bispecific Competitive Intensity

- **Categoria:** Competitivo
- **Descripcion:** The bispecific antibody and ADC markets are becoming extremely crowded. Over 180 companies and 250+ therapeutic candidates are in development. Major competitors include Roche, Amgen, AstraZeneca, Pfizer, and Daiichi Sankyo. In DLBCL specifically, competitors include CAR-T therapies (Yescarta, Breyanzi), other bispecifics (Roche's glofitamab/Columvi), and ADCs.
- **Evidencia:** Market research shows next-gen bispecific market growing from $9.5B (2025) to $52B (2035) — massive growth but with massive competition. Genmab holds ~8-10% market share, behind Roche (~18%) and Amgen.
- **Probabilidad:** Alta — competition is already intensifying.
- **Impacto si materializa:** Pricing pressure, slower-than-expected market share gains, need for combination trials (higher cost), potential best-in-class challenges from later entrants.

---

## Riesgos NO Mencionados en Thesis

(No thesis exists yet — this assessment is part of the R1 parallel analysis. These are risks that a fundamental analyst might minimize or overlook in a bullish thesis.)

| Riesgo | Severidad | Likely Minimized? | Comentario |
|--------|-----------|-------------------|------------|
| Post-Merus balance sheet transformation (net cash -> $5.5B debt) | HIGH | YES | QS tool shows "Net Cash" which is PRE-acquisition. The current balance sheet is dramatically different. |
| AbbVie trade secret lawsuit targeting Rina-S IP | HIGH | YES | The lawsuit specifically targets the ADC technology underlying Rina-S, Genmab's most promising wholly-owned asset. An injunction would be devastating. |
| Acasunlimab discontinuation signaling pipeline thinning | MEDIUM | YES | Often framed as "portfolio discipline" but it also means one fewer shot on goal, and BioNTech's prior exit was a red flag. |
| 0% insider ownership | LOW | YES | Zero insiders buying signals lack of conviction or Danish compensation norms, but either way it means no alignment. |
| Epcoritamab DLBCL-1 primary endpoint failure already happened | HIGH | POSSIBLY | Analyst may focus on positive secondary endpoints and FL success, but missing OS is a fundamental issue for a drug claiming to be better than standard of care. |
| Interest expense consuming ~30-35% of operating profit post-Merus | HIGH | YES | At $350-400M/year interest on $5.5B debt vs ~$1.1-1.4B operating profit, this is a meaningful drag on earnings and FCF. |
| HC Wainwright EPS cuts: FY2026 from $2.14 to $1.68 (21% cut) | MEDIUM | POSSIBLY | Analyst cuts reflect higher spending expectations and are not yet in the P/E of 13x (which uses trailing earnings). |

---

## Kill Conditions Sugeridas

Based on my risk research, I suggest the following kill conditions for any GMAB thesis:

1. **Darzalex Biosimilar Approval Pre-Pipeline Ramp:** If a Darzalex biosimilar gains FDA/EMA approval AND combined pipeline product revenue (Epkinly + Rina-S + petosemtamab) is below $1.5B annual run rate at that time. This would confirm the replacement gap is real.

2. **Net Debt/EBITDA > 4x for 2 Consecutive Quarters:** Post-Merus leverage must come down. If it increases instead, the balance sheet is deteriorating and the investment thesis breaks.

3. **Petosemtamab Phase 3 Dual Failure:** If BOTH LiGeR-HN1 AND LiGeR-HN2 fail to meet primary endpoints, the Merus acquisition rationale collapses and goodwill impairment is likely.

4. **AbbVie Wins Injunction on Rina-S:** If a court grants injunctive relief preventing Genmab from commercializing Rina-S or its underlying ADC technology, a key pipeline pillar is destroyed.

5. **EPCORE DLBCL-2 (1L DLBCL) Fails Primary Endpoint:** If the first-line DLBCL trial also misses (after DLBCL-1 already missed OS), Epkinly's path to $3B+ blockbuster is severely impaired.

6. **Operating Profit Turns Negative for 2+ Quarters:** Given the combined burden of commercialization spending, Merus integration costs, and debt service, if profitability disappears, the model is broken.

7. **Darzalex Net Sales Decline YoY:** If Darzalex sales peak and begin declining before pipeline products have scaled, the revenue bridge breaks.

---

## Riesgo Agregado

- **Numero de riesgos HIGH+CRITICAL:** 6 (Darzalex cliff CRITICAL, Merus leverage HIGH, Epcoritamab DLBCL HIGH, Own-commercialization HIGH, Petosemtamab binary HIGH, AbbVie lawsuit HIGH)
- **Riesgos correlacionados?** YES, critically so:
  - **Cluster 1 (Revenue Replacement):** Darzalex cliff + epcoritamab DLBCL failure + pipeline delays are ALL correlated. If the replacement pipeline underperforms while Darzalex erodes, it is a triple hit.
  - **Cluster 2 (Balance Sheet Stress):** Merus leverage + own-commercialization spending + pipeline failures all compound. Each incremental failure makes the debt harder to service.
  - **Cluster 3 (AbbVie Nexus):** AbbVie is simultaneously Genmab's most important commercial partner (epcoritamab) and its legal adversary (trade secret suit). Deterioration of this relationship has ripple effects across multiple business lines.
- **Risk Score Final: MEDIUM-HIGH**

**Rationale for MEDIUM-HIGH (not HIGH):**
- Darzalex is still growing (est. $12.6-13.4B in 2025) and biosimilar entry is 2-4 years away
- FCF generation (~$1B+/year) provides buffer for debt servicing
- Pipeline has multiple shots on goal with strong Phase 2 data and FDA BTDs
- P/E 13x near 52-week low suggests significant risk is already priced in
- Net cash position pre-acquisition was exceptionally strong; even with debt, the company is not in financial distress

**But not MEDIUM because:**
- The balance sheet has changed FUNDAMENTALLY from what the QS tool reflects
- 6 risks at HIGH or CRITICAL level is exceptional concentration
- Correlated risk clusters mean multiple risks can cascade simultaneously
- The company is attempting a triple transformation simultaneously: (1) patent cliff navigation, (2) own-commercialization buildout, (3) largest acquisition in its history — any ONE of these is challenging; all three together is high-risk

---

## QS Tool Adjustment Warning

The quality_scorer.py output of QS 77 (Tier A) is based on HISTORICAL financials that do NOT reflect:

1. **Post-Merus balance sheet:** Net Cash -> ~$5.5B net debt. Leverage score should be 0/10 (was 10/10).
2. **Interest coverage:** Will drop from 77.4x to ~3-4x. Score impact: -8 to -10 points on financial quality.
3. **Gross margin declining:** 100% -> 95.4% trajectory reflects transition from pure royalties to own-commercialization (lower margin).
4. **Insider ownership:** 0% = 0/5 on capital allocation.

**Suggested QS Adjustment:** 77 (tool) -> 60-65 (adjusted), placing GMAB in Tier B, not Tier A. The primary drivers of downgrade: leverage transformation (-10 points on financial quality) and execution risk on the business model transition.

---

## 🔄 META-REFLECTION

### Dudas/Incertidumbres
- **Post-Merus balance sheet exact figures:** Q4 2025 / FY2025 results were reported Feb 5, 2026, but I could not find the exact post-closing balance sheet with Merus consolidated. The $5.5B debt figure is from the financing announcement; actual net debt post-close could be higher if Merus had its own obligations.
- **AbbVie lawsuit materiality:** I cannot assess the legal merits of the trade secret claim. The outcome is genuinely binary — if AbbVie wins an injunction, Rina-S is at risk. If it is settled (like most IP disputes), it may cost a few hundred million but preserve the asset.
- **Darzalex subcutaneous patent protection:** The SC formulation (Darzalex Faspro) may have additional patent protection via Halozyme's ENHANZE technology, potentially extending exclusivity beyond the base daratumumab patents. I could not confirm the exact SC patent expiry timeline.
- **2026 formal guidance:** Genmab was expected to provide 2026 guidance in February 2026 (their FY2025 report). This guidance — especially the EBITDA and debt targets — would significantly clarify the financial risk picture.

### Riesgos que Podrian Estar Subestimados
- **AbbVie relationship risk:** I classified this as HIGH but it could be CRITICAL. AbbVie is simultaneously the commercial partner for Epkinly (Genmab's second-largest revenue source) AND suing Genmab. If the relationship deteriorates beyond the legal dispute, it could affect epcoritamab development and commercial efforts.
- **Own-commercialization cost overruns:** JPMorgan's concern about "underappreciated opex increases" is well-founded. Building a global oncology commercial infrastructure while servicing $5.5B debt AND running multiple Phase 3 trials simultaneously is exceptionally capital-intensive.

### Discrepancias con Thesis
- No thesis exists yet for comparison. However, the QS tool score of 77 (Tier A) is MISLEADING because it reflects pre-Merus financials. Any thesis built on this QS without adjustment would materially overstate quality.

### Sugerencias para el Sistema
1. **QS Tool Enhancement:** The quality_scorer.py should have a mechanism to flag "material pending events" (like recent large acquisitions) that invalidate historical financial metrics. A --post-event flag or annotation would prevent misleading Tier classifications.
2. **Biotech-specific risk framework:** Pharma/biotech companies have unique risks (patent cliffs, pipeline binary outcomes, regulatory approvals) that the standard 6-category framework captures but doesn't weight appropriately. Consider a biotech-specific sub-module.
3. **Debt transformation detection:** When a company goes from net cash to levered (or vice versa), this is a regime change that should trigger automatic QS re-evaluation.

### Preguntas para Orchestrator
1. Should the fundamental analyst be notified that the QS 77 needs adjustment to ~60-65 BEFORE they complete their thesis? This significantly changes the MoS requirement.
2. Given 6 HIGH+CRITICAL risks and the MEDIUM-HIGH overall score, does the investment committee want a minimum MoS threshold higher than typical for this risk profile?
3. The Merus acquisition closed December 2025. FY2025 results were released Feb 5, 2026. Should we fetch the actual post-close balance sheet before finalizing the thesis?
4. Is there a pharma/biotech sector view in world/sectors/? If not, one should be created before the fundamental analyst proceeds with the thesis.

---

## Sources

- [DrugPatentWatch: Darzalex Patent Expiry](https://www.drugpatentwatch.com/p/biologics/tradename/DARZALEX)
- [Genmab 2024 Annual Report](https://ir.genmab.com/news-releases/news-release-details/genmab-publishes-2024-annual-report)
- [Genmab Q3 2025 Financial Results](https://ir.genmab.com/news-releases/news-release-details/genmab-announces-financial-results-nine-months-2025/)
- [Genmab Merus Acquisition Announcement](https://ir.genmab.com/news-releases/news-release-details/genmab-acquire-merus-expanding-late-stage-pipeline-and)
- [AbbVie Trade Secret Lawsuit vs Genmab](https://ir.genmab.com/news-releases/news-release-details/genmab-vigorously-defend-alleged-claims-trade-secret)
- [AbbVie-Genmab Legal Battle Analysis (Labiotech)](https://www.labiotech.eu/trends-news/abbvie-genmab-lawsuit/)
- [Genmab Epcoritamab DLBCL-1 Phase 3 Results](https://ir.genmab.com/news-releases/news-release-details/genmab-announces-topline-results-epcoritamab-duobodyr-cd3xcd20)
- [Genmab Acasunlimab Discontinuation](https://ir.genmab.com/news-releases/news-release-details/genmab-portfolio-prioritization-update)
- [Genmab Rina-S Ovarian Cancer Data](https://ir.genmab.com/news-releases/news-release-details/investigational-rinatabart-sesutecan-rina-sr-continues-show/)
- [Genmab Merus $2.5B Notes Offering](https://www.investing.com/news/company-news/genmab-closes-25-billion-notes-offering-to-fund-merus-acquisition-93CH-4389242)
- [Seeking Alpha: Genmab Darzalex Growth Analysis](https://seekingalpha.com/article/4862231-genmab-darzalex-growth-fuels-rally-upside-is-tight)
- [FiercePharma: Genmab C-Suite Shuffle for Commercialization](https://www.fiercepharma.com/pharma/genmab-shuffles-c-suite-commercialization-manufacturing-portfolio-grows)
- [FiercePharma: Epkinly DLBCL-1 Next Steps](https://www.fiercepharma.com/pharma/after-abbvie-and-genmabs-ph-3-survival-miss-epkinly-dlbcl-whats-next)
- [GEN Engg News: Top 20 Drugs Heading for Patent Cliff](https://www.genengnews.com/topics/drug-discovery/top-20-drugs-heading-for-the-patent-cliff-2026-2029/)
- [Morningstar: Darzalex Drives Genmab Growth](https://www.morningstar.com/company-reports/1211879-strong-royalty-revenue-from-darzalex-continues-to-drive-growth-for-narrow-moat-genmab)
- [CNBC: Denmark Pharma and Trump Tariffs](https://www.cnbc.com/2025/05/15/trumps-pharma-tariffs-threat-wont-slow-denmark-down.html)
- [Morningstar: European Pharma vs Trump 100% Tariffs](https://global.morningstar.com/en-nd/stocks/european-pharma-stock-investors-hold-their-nerve-trump-unveils-100-tariffs)
- [Investing.com: Genmab Q3 2025 Earnings Transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-genmab-q3-2025-sees-strong-growth-stock-dips-93CH-4339565)
- [HC Wainwright Q4 2025 Estimates](https://www.themarketsdaily.com/2026/01/30/what-is-hc-wainwrights-estimate-for-genmab-a-s-q4-earnings.html)
