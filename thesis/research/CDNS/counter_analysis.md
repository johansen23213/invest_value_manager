# Counter-Analysis: CDNS (Cadence Design Systems)

## Fecha: 2026-02-18

---

## CRITICAL FINDING: THESIS VALUATION USES STALE CONSENSUS NUMBERS

**Before proceeding, the orchestrator must be aware that the thesis FV of $260 and entry of $230-240 were calculated using FY2026E consensus EPS of $6.52.** The actual Q4 2025 earnings (reported Feb 17) show:

- FY2025 non-GAAP EPS: **$7.14** (not $5.66 as thesis estimated)
- FY2026 guidance non-GAAP EPS: **$8.05-$8.15** (not $6.52 as thesis used)
- FY2025 revenue: **$5.297B** (in line with thesis estimate)
- FY2026 revenue guidance: **$5.9-6.0B** (in line with thesis estimate)

**The EPS used in the thesis is ~20% below actual FY2025 results and ~24% below FY2026 guidance.** This fundamentally changes the P/E-based valuation that drove the $260 FV. However, this does NOT necessarily make the stock cheaper -- it may mean the thesis used the wrong EPS numbers from the start, or that the difference between GAAP and non-GAAP is larger than assumed. At $283 current price, the forward P/E on $8.10 midpoint guidance is **35x** -- not 46x as the thesis states.

**This is a MODERATE challenge (not CRITICAL) because:** The thesis already acknowledged DCF produces much lower values ($118), and the P/E method was weighted only 20%. The EPS discrepancy suggests the thesis may have been using a different definition of EPS (possibly GAAP vs non-GAAP). FY2025 GAAP EPS was $4.06 vs non-GAAP $7.14 -- a 43% gap, which is among the widest in our universe.

---

## Resumen Ejecutivo

The CDNS thesis describes an exceptional business at a premium valuation. After independent investigation including Q4 2025 earnings (which beat expectations), I find the thesis **partially survives scrutiny** but has significant weaknesses in its valuation methodology, its treatment of the GAAP/non-GAAP gap, its minimization of insider selling, and its insufficient attention to the Synopsys-Ansys competitive escalation. The moat assessment is solid. The business quality is genuine. But the entry price framework needs revision, and several risks were inadequately addressed.

**Veredicto: MODERATE COUNTER**

---

## Asunciones Clave Desafiadas

### 1. QS 82 Tier A (Adjusted +8 from 74)

- **Thesis claim:** QS tool gives 74, adjusted to 82 by adding 8 points for market position (#2 in EDA duopoly).
- **Evidencia en contra:** The +8 adjustment is defensible -- CDNS IS definitively #2 in a duopoly. However, the QS of 74 WITHOUT adjustment already penalizes CDNS for: (a) declining gross margins (0/5), (b) zero insider ownership score (0/5), (c) zero shareholder returns score (0/5). These are REAL negatives, not tool artifacts. The thesis treats the 74 as an error to fix, but the tool is correctly identifying that CDNS has declining margins, low insider alignment, and no dividend. A Tier A company with 0/10 on capital allocation is unusual.
- **Counter-evidence:** Capital allocation score of 0/10 is the lowest in the entire Tier A pipeline. For comparison: ADBE (76 adj) has at least dividends; LULU (78 adj) has aggressive buybacks. CDNS's buybacks merely offset SBC dilution (net share reduction 1.8% over 3 years). Insiders own 0.3% and are NET SELLERS of $18.5M in the last 3 months (CEO $6.8M, CFO $8.9M, SVP $2M+).
- **Severidad:** LOW -- The market position adjustment is justified. But the 0/10 capital allocation is a genuine quality concern that the thesis minimizes.
- **Resolucion sugerida:** Accept QS 82 Tier A but FLAG the capital allocation weakness explicitly. The insider selling pattern is a negative signal even if through 10b5-1 plans.

### 2. Fair Value $260 Based on 40x FY2026E EPS of $6.52

- **Thesis claim:** FV = $260, derived primarily from 40x FY2026E EPS of $6.52.
- **Evidencia en contra:** FY2026 non-GAAP EPS guidance is $8.05-$8.15, which is 24% above the $6.52 the thesis used. At 40x the actual $8.10 midpoint, FV would be $324 -- well above the current price of $283. This suggests either: (a) the thesis used GAAP EPS rather than non-GAAP, or (b) the thesis used stale consensus estimates.
- **The CRITICAL question:** Should we use GAAP EPS ($4.06 FY2025, $4.95-5.05 FY2026 guided) or non-GAAP EPS ($7.14 FY2025, $8.05-$8.15 FY2026 guided)? The gap between GAAP and non-GAAP for CDNS is enormous:
  - FY2025: $4.06 GAAP vs $7.14 non-GAAP = **43% gap**
  - The primary driver: SBC ($455M in FY2025), amortization of acquired intangibles, and restructuring charges
  - SBC alone represents ~$1.66/share in FY2025
- **Independent assessment:** For a company where SBC is 8.6% of revenue and growing faster than revenue, using non-GAAP EPS dramatically overstates earnings. Our system standard (INTU precedent, Session 66) is to use SBC-adjusted FCF as the primary metric. Using non-GAAP P/E without adjusting for SBC gives a misleadingly low multiple.
- **Recalculated valuation at current price:**
  - At $283, P/E on FY2026 GAAP EPS ($5.00 midpoint) = **56.6x**
  - At $283, P/E on FY2026 non-GAAP EPS ($8.10 midpoint) = **34.9x**
  - At $283, EV/SBC-adj-FCF (TTM $1.03B, 273M shares) = **~75x**
  - The "truth" is between 35x and 57x depending on how you treat SBC
- **Severidad:** HIGH -- The thesis valuation methodology is internally inconsistent. It claims to use SBC-adjusted FCF for DCF but uses unadjusted (non-GAAP) EPS for the P/E method. The correct approach per our system: use SBC-adjusted metrics consistently. On that basis, CDNS is more expensive than the thesis acknowledges.
- **Resolucion sugerida:** Recalculate FV using consistent SBC-adjusted metrics. The P/E method should use GAAP EPS or explicitly adjust non-GAAP EPS for SBC. The thesis FV of $260 may be in the right ballpark if using ~52x GAAP FY2026 EPS ($5.00), but this should be stated explicitly.

### 3. EDA Duopoly Moat is "Impregnable"

- **Thesis claim:** WIDE moat, among the widest in technology. Switching costs extreme. No new entrant in 30+ years.
- **Evidencia en contra:** The moat IS genuinely wide. My independent research confirms:
  - No major customer has switched EDA vendors wholesale in 20+ years (PRIMARY DATA from industry)
  - Efabless, the most prominent open-source EDA commercializer, shut down in March 2025 (CONFIRMS moat)
  - OpenROAD/LibreLane are limited to academic use and trailing-edge nodes (180nm-12nm) -- irrelevant for leading-edge design
  - Foundry certification remains the ultimate barrier: even Siemens EDA at ~13% share cannot get full TSMC 3nm certification
- **Where the thesis is slightly overconfident:**
  - Synopsys-Ansys merger creates a **$35B silicon-to-systems platform** that directly competes with CDNS's fastest-growing segment (System Design & Analysis, 16% of FY2025 revenue). SNPS now commands TAM of $31B vs CDNS ~$16B. The thesis barely addresses this.
  - The SNPS-Ansys first integrated toolsets targeting multi-die packaging are expected H1 FY2026 -- this could impact new design starts tilting toward SNPS.
  - AI-native chip design from hyperscalers (Google, Amazon, Microsoft building internal tools) is a tail risk the thesis dismisses too quickly. These companies have unlimited budgets.
- **Severidad:** LOW -- The core EDA moat is genuine and among the strongest I have researched. The Synopsys-Ansys threat is real but addressed separately (see Desafio al Negocio).
- **Resolucion sugerida:** Maintain WIDE moat classification. Add SNPS-Ansys competitive monitoring as explicit tracking item.

### 4. Q4 2025 Beat Validates Thesis

- **Thesis claim:** Earnings framework set bull/base/bear scenarios. Q4 results match "BASE" scenario.
- **Actual Q4 results:**
  - Q4 revenue: $1.44B (in line with consensus $1.424B) -- slight beat
  - Q4 non-GAAP EPS: $1.99 vs consensus $1.90 -- 4.7% beat
  - Record backlog: $7.8B (vs thesis target >$7.0B) -- BULL scenario
  - FY2026 revenue guidance: $5.9-6.0B -- in line with thesis expectations
  - Non-GAAP operating margin: 44.6% FY2025, guided 44.75-45.75% FY2026 -- BULL
  - China at 13% of revenue, guided 12-13% for FY2026 -- neutral
- **Independent assessment:** The Q4 results are genuinely strong. Revenue growth of 14% FY2025, backlog at record $7.8B, margin expansion to 44.6%, and EPS growth of 20% non-GAAP all validate the business quality thesis. The stock rose ~7% after-hours on the results.
- **BUT:** Strong results do NOT mean the stock is cheap. The market already expected strong results (consensus was $1.90 EPS, got $1.99). At $283 post-earnings, the market has ALREADY priced in the positive results. The question is whether $283 offers sufficient MoS, not whether the business is good.
- **Severidad:** LOW -- Earnings validate the business thesis. They do not address the valuation challenge.
- **Resolucion sugerida:** Update thesis with actual Q4 results. The hard gate is PASSED. Proceed with pipeline but maintain price discipline.

### 5. AI/Chip Complexity Tailwind

- **Thesis claim:** AI is a structural tailwind driving chip complexity, which increases EDA tool demand.
- **Evidencia en contra:** The AI tailwind is REAL. However:
  - **It is widely known.** Every analyst covering CDNS mentions AI as a growth driver. This is CONSENSUS, not edge. The market has priced AI into 35x non-GAAP forward P/E.
  - **AI capex sustainability is uncertain.** If hyperscalers reduce AI infrastructure spending (as some bear cases suggest), chip design starts could decelerate. EDA is the most cycle-resistant sub-sector, but it is NOT immune.
  - **Q4 YoY revenue growth decelerated to 6.2%** (from 14.8% in FY2023 and 13.5% in FY2024). While this is partly seasonal (Q4 is typically weakest), it signals deceleration.
  - **The reverse DCF tells the story:** At $283, the market implies 41% annual FCF growth for 5 years. Historical FCF CAGR is 2.6%. The gap is 38pp. Even using revenue growth (15.8% CAGR) as a proxy, the market implies 2.5x the historical rate. The AI narrative must deliver MASSIVE acceleration to justify this.
- **Severidad:** MODERATE -- The AI tailwind is real but fully priced. This is not differentiated analysis; it is consensus (Source: Level 4 - CONSENSUS).
- **Resolucion sugerida:** The thesis should explicitly acknowledge that AI is consensus and already in the price. The edge, if any, must come from believing CDNS can grow FASTER than the market expects -- and there is limited evidence for this given FY2026 revenue guidance of 12-13% (below the 14% historical rate).

---

## Desafios por Categoria

### Negocio

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | Synopsys-Ansys creates silicon-to-systems competitor with $31B TAM vs CDNS $16B | SNPS completed $35B Ansys acquisition Jul 2025. First integrated toolsets H1 FY2026. $400M projected annual synergies. Directly competes with CDNS fastest-growing segment (System Design & Analysis). | HIGH |
| 2 | Q4 YoY revenue growth decelerated to 6.2% | Q4 2025 revenue $1.44B vs $1.356B Q4 2024 = 6.2% growth, down from 14% full-year. Possibly seasonal but signals deceleration risk. | LOW |
| 3 | CEO Devgan joined Lam Research board Feb 2026 | Minor distraction risk. CEO already owns only 0.1% of company. Adding outside board seat while on DOJ probation raises prioritization question. | LOW |
| 4 | Hexagon Design & Engineering acquisition pending | New acquisition during DOJ probation period. Increases execution risk and invested capital (further ROIC compression). | MODERATE |

### Valoracion

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | Thesis uses stale/inconsistent EPS for P/E valuation | Thesis used $6.52 FY2026E EPS. Actual FY2026 guidance is $8.05-$8.15 (non-GAAP) or $4.95-$5.05 (GAAP). Valuation methodology inconsistent between DCF (SBC-adjusted) and P/E (unadjusted). | HIGH |
| 2 | Reverse DCF implies 41% annual FCF growth -- heroic assumption | At $283, the market requires 41% annual FCF growth for 5 years. Historical FCF CAGR is 2.6%. Even revenue CAGR of 15.8% cannot bridge this gap without massive margin expansion AND SBC reduction. | HIGH |
| 3 | GAAP/non-GAAP gap is 43% -- among widest in universe | FY2025 GAAP EPS $4.06 vs non-GAAP $7.14. SBC of $455M ($1.66/share) is the primary driver. Buybacks offset only ~$0.30/share of dilution per year. Real economic earnings are much closer to GAAP. | MODERATE |
| 4 | PEG ratio of 3.0+ at current price remains rich | Even at 35x FY2026 non-GAAP, PEG is 35/15 = 2.3x. At 56x GAAP, PEG is far worse. Elite compounders (MSFT, ADBE) trade at PEG 2.0-2.8x. CDNS is at the ceiling. | MODERATE |
| 5 | EV/SBC-adjusted FCF at ~75x TTM | Only SNPS trades at a comparable multiple in the software universe. MSFT at 35x, ADBE at 30x, INTU at 35x. CDNS premium requires sustained 15%+ growth for a decade. | HIGH |

### Riesgos

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | Insider selling $18.5M in last 3 months | CEO Devgan sold $6.8M (9.27% of holdings), CFO Wall sold $8.9M, SVP Scannell $1.9M, SVP Teng $2.0M+. While via 10b5-1 plans, the aggregate is notable. Net insider shares: -37,100 (sold > purchased). | MODERATE |
| 2 | Export control probation constrains growth for 3 years | 3-year DOJ probation with mandatory audits through 2028. Any new violation triggers enhanced penalties. Export control regime is TIGHTENING. Compliance costs increasing. | MODERATE |
| 3 | Receivables growing 2.3x revenue growth rate | Narrative checker: receivables grew 31.1% vs revenue growth 13.5% in 2024. This can signal aggressive revenue recognition or collection challenges. Requires monitoring. | MODERATE |
| 4 | Inventory growing 3.1x revenue growth rate | Narrative checker: inventory grew 41.9% vs revenue growth 13.5%. Likely hardware (Palladium/Protium) buildup, but signals potential demand/supply mismatch. | LOW |
| 5 | FCF margin declining: 34.6% (2021) to 24.1% (2024) | Narrative checker confirms persistent FCF margin decline. OCF/NI also declining: 1.6x to 1.2x. Partially acquisition-driven but 4-year downtrend is concerning. TTM improved to 35.6% per Q4, but this is volatile. | MODERATE |
| 6 | SBC growing at 23% CAGR vs revenue 16% CAGR | SBC was $455M in FY2025 (8.6% of revenue). At this trajectory, hits 10% by 2027 and 12% (kill condition) by ~2029. The gap between GAAP and non-GAAP is widening, not narrowing. | MODERATE |

### Timing

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | Stock at $283 is 18-23% above thesis entry of $230-240 | Even after earnings beat, stock remains far above entry target. No catalyst to bring price to target unless broader market correction. | LOW |
| 2 | Analyst consensus PT $377 -- buying at $283 would be WITH consensus | Consensus says BUY with $377 target. If our thesis agrees at $283, we have no informational edge. Our edge should come from buying BELOW consensus. | MODERATE |
| 3 | AI narrative peak risk -- if AI capex cycle peaks in 2026-2027 | If hyperscaler AI spending decelerates (signs emerging from capex commentary), chip design starts could slow 12-18 months later. EDA is late-cycle within semi. | MODERATE |

---

## Conflictos con Otros Analisis

### vs Moat Assessment
- **Agreement:** Both assess WIDE moat. Moat assessor gives 9/10 overall strength. I concur.
- **Minor disagreement:** Moat assessor rates network effects as PARTIAL (7/10 in thesis). I agree with the moat assessor's more conservative classification.
- **Gap:** Moat assessor correctly identifies SNPS-Ansys as Medium (30%) probability threat but the thesis main body barely discusses it. This should be elevated in priority.

### vs Risk Assessment
- **Agreement:** Risk assessment correctly flagged the export control guilty plea as CRITICAL and noted it was missing from the original thesis. The thesis was subsequently updated to include it.
- **Agreement:** Risk assessment flagged that entry at $260 provides 0% MoS -- the thesis was correctly revised to $230-240.
- **Additional gap:** Risk assessment notes insider selling of $18.5M but thesis dismisses it as "no unusual selling." The data shows NET selling of 37,100 shares. CEO sold 9.27% of his personal holdings. This is not "no unusual selling."
- **Receivables/Inventory anomaly:** The narrative checker reveals receivables growing at 2.3x revenue and inventory at 3.1x revenue. Neither the thesis nor the risk assessment mentions this. This is a balance sheet quality signal that deserves investigation.

### vs Valuation Report
- **Critical conflict:** The valuation report uses $6.52 FY2026E EPS for the P/E method but $1,031M SBC-adjusted FCF for the DCF. These are inconsistent because the P/E uses non-GAAP earnings (excludes SBC) while the DCF adjusts for SBC. The FV should be derived using consistent treatment of SBC.
- **The valuation report itself acknowledges this:** "The DCF is penalizing CDNS disproportionately" and "The straight weighted average ($163) is misleading." The analyst then overrides the mechanical weighted average and selects $260 as FV. This is a judgment call that leans bullish.

---

## Veredicto Global

| Metric | Valor |
|--------|-------|
| Desafios totales | 17 |
| Desafios HIGH | 4 |
| Desafios MODERATE | 9 |
| Desafios LOW | 4 |
| Desafios CRITICAL | 0 |
| Desafios no resueltos por thesis | 7 (valuation methodology, receivables anomaly, inventory anomaly, insider selling characterization, SNPS-Ansys insufficient coverage, SBC trajectory, consensus alignment) |
| **Veredicto** | **MODERATE COUNTER** |

### Interpretacion

The thesis describes a genuinely excellent business. The EDA duopoly moat is real, the Q4 2025 earnings validated the growth thesis, and the AI tailwind is structural. **I cannot find evidence that the business is deteriorating.**

However, the thesis has significant **valuation methodology problems**:
1. The EPS used ($6.52) is stale and inconsistent with the SBC-adjusted approach used in DCF
2. The GAAP/non-GAAP gap (43%) is among the widest in our universe and the thesis does not adequately address this
3. At $283, the reverse DCF implies 41% FCF growth -- heroic
4. The thesis acknowledges being WITH consensus (analysts target $377) -- this means we have no edge

The risks are **inadequately addressed** in three areas:
1. Insider selling is dismissed when it is actually notable ($18.5M in 3 months, CEO sold 9% of holdings)
2. Receivables and inventory growing much faster than revenue is not mentioned
3. The SNPS-Ansys competitive threat to System Design & Analysis (CDNS's fastest-growing segment) deserves more attention

**Correction estimate:** The FV of $260 is in the right general range IF using ~52x GAAP FY2026 EPS ($5.00) or ~32x non-GAAP ($8.10). However, the 52x GAAP is rich for any company, and 32x non-GAAP ignores $1.66/share in SBC. A more defensible FV using SBC-adjusted metrics would be:
- SBC-adjusted FCF method: $1.03B TTM at 45x = $169/share (EV basis ~$171)
- GAAP P/E at 45x: 45 x $5.00 = $225
- Non-GAAP P/E at 35x (discounted for SBC growth): 35 x $8.10 = $284 (current price)
- Blend: ~$220-$230

**DA Fair Value estimate: $220-$230** (vs thesis $260, correction of ~12-15%)

---

## Recomendacion al Investment Committee

1. **The thesis must be updated with actual Q4 2025 earnings data.** The consensus estimates used are now stale. FY2025 non-GAAP EPS was $7.14, FY2026 guidance is $8.05-$8.15.

2. **Resolve the GAAP vs non-GAAP valuation inconsistency.** The P/E and DCF methods must use consistent SBC treatment. Per our INTU precedent, SBC-adjusted metrics should be primary.

3. **Investigate the receivables anomaly.** Receivables growing at 2.3x revenue is a yellow flag. Is this hardware delivery timing, or aggressive revenue recognition?

4. **Revise entry price.** If the committee agrees with DA's FV range of $220-$230, the entry price should be $195-$210 (providing 10-12% MoS for Tier A). If the committee maintains the thesis FV of $260, the entry of $230-240 provides only 8-12% MoS, which is at the low end for a company with 4 HIGH-severity challenges.

5. **Explicitly address insider selling in the thesis.** $18.5M in 3 months with CEO selling 9% of holdings is not "no unusual selling."

6. **Add SNPS-Ansys System Design monitoring.** If CDNS's System Design & Analysis segment growth drops below 20% for 2 consecutive quarters, the competitive threat is materializing.

7. **Monitor SBC trajectory aggressively.** FY2025 SBC was $455M (8.6% of revenue). If FY2026 SBC exceeds $520M (~8.7% of guided revenue), the trajectory toward the 12% kill condition is accelerating.

---

## 🔄 META-REFLECTION

### Dudas/Incertidumbres
- **The EPS discrepancy is the biggest unresolved issue.** I cannot determine with certainty whether the thesis analyst used GAAP EPS, non-GAAP EPS, or a blend. The thesis states "$6.52 FY2026E" which was the Street consensus for non-GAAP before Q4 results. The actual FY2026 guidance of $8.05-$8.15 is dramatically higher, suggesting the thesis was using pre-Q4 estimates. This needs R3 resolution.
- **Receivables growing 2.3x revenue:** I could not determine from available data whether this is hardware delivery timing (Palladium/Protium systems have lumpy receivables) or something more concerning. The 10-K would clarify.
- **FY2025 FCF data:** The thesis shows TTM FCF of $1,479M but the narrative checker shows FY2024 FCF of $1,118M. The TTM figure likely includes Q1-Q3 2025 data. Q4 2025 FCF margin of 35.6% (from StockStory) suggests full-year FY2025 FCF is strong, but I have not seen the official figure yet.

### Limitaciones de Este Analisis
- I could not access the full Q4 2025 earnings call transcript (paywalled/restricted). Segment-level detail beyond the headline numbers was limited.
- The GAAP vs non-GAAP reconciliation for FY2026 guidance needs the official earnings release tables, which I could not fully extract.
- I did not find specific evidence of CDNS losing design starts to SNPS-Ansys -- this threat is forward-looking and speculative at this point.

### Sugerencias para el Sistema
- **Standardize GAAP vs non-GAAP treatment in all thesis documents.** The CDNS thesis uses non-GAAP EPS for P/E but SBC-adjusted FCF for DCF. This inconsistency should be prevented by the thesis template.
- **Add receivables/inventory growth vs revenue growth as standard check in narrative_checker output.** The flags here (2.3x and 3.1x) are material and would have been caught earlier.
- **The reverse DCF tool is invaluable for this type of high-multiple stock.** The 41% implied FCF growth rate is the single most powerful piece of counter-evidence. Consider making reverse DCF mandatory for any stock trading above 50x earnings.

### Preguntas para Orchestrator
1. **Which EPS did the thesis use?** If $6.52 was FY2026 consensus non-GAAP before Q4 results, the thesis needs updating with $8.10 actual guidance. But this makes the non-GAAP P/E look cheap (35x) while GAAP P/E remains rich (57x). Which metric should govern?
2. **Should the entry price be revised down given 4 HIGH-severity challenges?** The current $230-240 entry already provides limited MoS. The DA estimate of $220-$230 FV would require entry at $195-$210.
3. **The receivables anomaly deserves resolution before R4.** Can the orchestrator direct a follow-up investigation using the 10-K data?
4. **Insider selling: should this be added as a formal monitoring item?** CEO selling 9% of holdings while company is on DOJ probation is a negative signal, even if via 10b5-1 plan.

---

## Sources

### Primary Data (Level 1)
- Cadence Q4/FY2025 Earnings Release (Feb 17, 2026): Q4 rev $1.44B, EPS $1.99, FY2025 rev $5.297B, FY2026 guide $5.9-6.0B, non-GAAP EPS $8.05-8.15
- insider_tracker.py: Net insider selling 37,100 shares, CEO sold $6.8M (9.27% of holdings)
- narrative_checker.py: Receivables +31.1% vs revenue +13.5%, Inventory +41.9% vs revenue +13.5%
- dcf_calculator.py --reverse: Implied FCF growth 41% vs historical 2.6% CAGR
- price_checker.py: Current price $283.46

### Secondary Analysis (Level 2)
- [Cadence Q4/FY2025 Results](https://investor.cadence.com/news/news-details/2026/Cadence-Reports-Fourth-Quarter-and-Fiscal-Year-2025-Financial-Results/default.aspx)
- [Cadence Q4 2025 Earnings Call Highlights](https://finance.yahoo.com/news/cadence-design-systems-q4-earnings-004311145.html)
- [DOJ: Cadence Guilty Plea $140M](https://www.justice.gov/opa/pr/cadence-design-systems-agrees-plead-guilty-and-pay-over-140-million-unlawfully-exporting)
- [DLA Piper: Cadence Case Analysis](https://www.dlapiper.com/en/insights/publications/2025/07/doj-and-bis-priorities-in-export-control-compliance)
- [Synopsys Ansys Integration](https://futurumgroup.com/insights/synopsys-wraps-up-ansys-acquisition-targeting-integrated-design-solutions/)
- [OpenROAD Project](https://theopenroadproject.org/)

### Opinion (Level 3) -- used for sentiment only
- [Seeking Alpha: CDNS Riding AI Supercycle](https://seekingalpha.com/article/4864221-cadence-design-systems-riding-the-ai-supercycle-but-with-expectations-at-the-limit)
- [TIKR: Down 25% From ATH](https://www.tikr.com/blog/down-25-from-all-time-highs-can-cadence-design-stock-give-better-returns-in-2026)

### Consensus (Level 4) -- used as comparison only
- Analyst consensus: 5 Strong Buy, 16 Buy, 5 Hold, 0 Sell. Mean PT $377.29. Consensus key: BUY.
- Short interest: 1.8% of float, 2.4 days to cover (LOW -- no bearish conviction from shorts)
