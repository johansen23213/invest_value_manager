# Risk Assessment: BYIT.L (Bytes Technology Group plc)

## Fecha: 2026-02-09

## Risk Score: HIGH

---

## Executive Summary

The thesis presents BYIT.L as a temporarily impaired Tier A compounder. My independent investigation reveals a materially more concerning picture. The single most important finding is that **Microsoft is systematically reclaiming Enterprise Agreement renewals from partners**, with LSP commission payouts projected to reach zero by 2026. The thesis frames Microsoft incentive changes as "cyclical" -- the evidence suggests they are **structural and accelerating**. Combined with 68% GII dependency on Microsoft, rising employee costs from UK NI increases, operating profit already declining 7%, and a governance legacy from the former CEO investigation, the risk profile is significantly higher than the thesis acknowledges.

The thesis FV of 455 GBp is overly optimistic. My risk-adjusted FV range is **320-380 GBp**, implying current MoS of only 5-20% rather than 35%.

---

## QS Reassessment: Challenging the 81 Score

The quality_scorer.py confirms QS 81 (Tier A). However, several components deserve scrutiny:

### Financial Quality: 28/40 -- CHALLENGE

| Sub-metric | Score | Challenge |
|-----------|-------|-----------|
| ROIC Spread | 4 pts (4.9pp) | **This is LOW for Tier A.** The thesis acknowledges this but explains it away as "asset-light distortion." While true that minimal invested capital inflates denominators, 4.9pp is objectively weak. For comparison, Softcat achieves ROIC ~36% with a similar business model. If the business model doesn't generate high ROIC spread, the "compounder" label is questionable. |
| FCF Margin | 10 pts (29.9%) | Valid. 30% FCF margin on GP is genuine quality. |
| Leverage | 10 pts (Net cash) | Valid. Net cash ~GBP 40M is a genuine strength. |
| FCF Consistency | 4 pts (4/5) | One miss in 5 years raises questions. What caused the miss? |

**My adjustment:** Financial Quality should be 26/40 (-2 for weak ROIC spread that is NOT just "asset-light distortion" -- Softcat achieves much higher ROIC with same model).

### Growth Quality: 21/25 -- CHALLENGE

| Sub-metric | Score | Challenge |
|-----------|-------|-----------|
| Revenue CAGR | 8 pts (10.5%) | **Historical.** Forward growth is uncertain. H1 FY2026 GP growth was 0.4%, OP growth was -7%. Management guides "double-digit GP growth" for FY2026 but Berenberg says this is unlikely. H1 was described as "well below market expectations." |
| EPS CAGR | 8 pts (13.5%) | **Historical.** Forward EPS growth will be compressed by NI cost increases, headcount growth, and Microsoft incentive erosion. |
| GM Trend | 5 pts (Expanding) | **Reversing.** GP/GII margin fell from 6.7% to 6.1% in H1. Operating efficiency ratio fell from 43.4% to 40.2%. |

**My adjustment:** Growth Quality should be 17/25 (-4 for forward growth deterioration that backward-looking metrics miss).

### Moat Evidence: 22/25 -- CHALLENGE

| Sub-metric | Score | Challenge |
|-----------|-------|-----------|
| GM Premium | 10 pts (+19.4pp) | Valid metric, but it's comparing to a broad "Technology" sector average which includes hardware and low-margin resellers. Compared to Softcat (direct peer), the premium narrows significantly. |
| Market Position | 5 pts | Valid. #1-2 UK public sector VAR. |
| ROIC Persistence | 7 pts | **Questionable.** If Microsoft takes EA renewals direct, the ROIC base erodes. The moat is partly a derivative of Microsoft's willingness to share economics with partners. |

**My adjustment:** Moat Evidence should be 19/25 (-3 for moat partially dependent on Microsoft's goodwill, which is actively eroding).

### Capital Allocation: 10/10 -- ACCEPT WITH NOTE

Insider ownership 9.6% is genuinely good. Special dividends are positive. However, the former CEO was forced to resign over undisclosed share dealings (119 transactions over 3 years). While the investigation cleared him of broader misconduct, this represents a governance red flag that the 10/10 score doesn't capture.

### Adjusted Quality Score

| Category | Thesis | My Adjustment | Risk-Adjusted |
|----------|--------|---------------|---------------|
| Financial Quality | 28/40 | -2 | 26/40 |
| Growth Quality | 21/25 | -4 | 17/25 |
| Moat Evidence | 22/25 | -3 | 19/25 |
| Capital Allocation | 10/10 | 0 | 10/10 |
| **TOTAL** | **81** | **-9** | **72** |

**Risk-adjusted QS: 72 -- Tier B (Quality Value), NOT Tier A.**

The -9 point adjustment moves BYIT from Tier A to Tier B. This is significant because it changes the appropriate MoS framework from "Tier A: 10-15% typical" to "Tier B: 20-25% typical" based on precedents.

---

## Matriz de Riesgos

| # | Categoria | Riesgo | Probabilidad | Impacto | Score | Mitigante |
|---|-----------|--------|-------------|---------|-------|-----------|
| 1 | Fundamental | Microsoft EA direct sales takeover | Alta | Alto | **CRITICAL** | Services pivot, but 68% GII is Microsoft |
| 2 | Fundamental | Microsoft incentive compression is structural, not cyclical | Media-Alta | Alto | **HIGH** | Management says "settled into new structure" |
| 3 | Fundamental | Public sector spending cuts from 2026/27 | Media | Alto | **HIGH** | ~50% of GII is public sector, NHS mandates provide floor |
| 4 | Financiero | Operating cost inflation (NI increase + headcount) | Alta | Medio | **HIGH** | Headcount +12% while GP flat |
| 5 | Fundamental | Softcat competitive pressure and valuation divergence | Media | Medio | **MEDIUM** | BYIT gaining public sector share |
| 6 | Governance | Former CEO share dealing investigation legacy | Baja | Medio | **LOW** | FCA closed case, no sanctions |
| 7 | Valoracion | Value trap / dead money risk | Media | Medio | **MEDIUM** | Net cash, dividends provide floor |
| 8 | Fundamental | AI self-service reducing VAR need | Baja | Alto | **MEDIUM** | AI currently increasing complexity |
| 9 | Geopolitico | UK economic weakness / recession risk | Media-Baja | Medio | **LOW** | Defensive IT spending, public sector counter-cyclical |
| 10 | Fundamental | Single vendor concentration (68% Microsoft) | Alta | Alto | **CRITICAL** | Historical dependency, difficult to diversify quickly |
| 11 | Financiero | Analyst consensus deteriorating (4 Hold, 1 Buy) | Media | Bajo | **LOW** | Contrarian opportunity if thesis is right |

### Scoring Key:
- Alta x Alto = **CRITICAL**
- Alta x Medio OR Media x Alto = **HIGH**
- Media x Medio = **MEDIUM**
- Baja x cualquiera OR cualquiera x Bajo = **LOW**

---

## Top 3 Riesgos Criticos

### 1. Microsoft Enterprise Agreement Direct Sales Takeover -- CRITICAL

- **Categoria:** Fundamental
- **Descripcion:** Microsoft is systematically reclaiming Enterprise Agreement renewals from Licensing Solution Providers (LSPs). On January 1, 2023, Microsoft began taking over EA accounts through a new Direct Sales Model. Global EA commission payments to LSPs dropped from $2.5B (2023) to $1.67B (2024) to a projected $583M (2025), with payouts expected to reach ZERO by 2026. Microsoft reportedly reclaimed roughly one-third of large EA renewals last year and is expected to reclaim almost all by January 2026.
- **Evidencia:**
  - The Register (July 2025): "Bytes Technology Group among the first major casualties" -- shares dropped 25%+
  - US Cloud analysis: "Within just one year, Microsoft reclaimed roughly one-third of large EA renewals"
  - Global LSP commissions: $2.5B (2023) -> $1.67B (2024) -> $583M (2025) -> $0 (2026 projected)
  - 68% of Bytes' GII stems from Microsoft products
  - ~50% of Bytes' gross profit derives from Microsoft sales
- **Probabilidad:** Alta -- This is already happening, not speculative. The trend is accelerating.
- **Impacto si materializa:** Severe. If EA commissions go to zero for LSPs, Bytes loses a meaningful portion of its gross profit from Microsoft EA renewals. Even if Bytes retains CSP revenue, the EA loss could represent 15-25% of gross profit. At 25% GP loss, operating profit could decline 40%+, implying a stock price of 180-220 GBp.
- **Mitigante:** Bytes is pivoting to services (+40% growth), and CSP revenue (smaller EAs, cloud) is separate from the large EA direct sales takeover. Also, Bytes is a CSP partner, not purely an LSP. The distinction matters: CSP involves ongoing management and billing, which Microsoft cannot easily replicate. BUT the thesis treats this as a "cyclical adjustment" when the evidence says "structural industry shift."
- **Kill condition?:** **YES** -- If Microsoft confirms full EA takeover for ALL sizes (not just large accounts), this should be a kill condition. The thesis does not have this as a kill condition.

**CRITICAL NOTE:** The thesis (Section "My Counter-Thesis", point 1) states: "This is a cyclical adjustment to a new incentive structure, not a permanent impairment. Microsoft restructures partner programs every 2-3 years. Partners adapt, find new incentive streams, and margins normalize." **This is contradicted by the evidence.** The 2023+ changes are qualitatively different from previous restructurings: Microsoft is not just changing incentive rates -- they are taking EA renewals DIRECT. This is structural disintermediation, not a cyclical margin squeeze. The thesis assigns only 25% probability of being wrong. I would assign 50-60%.

---

### 2. Single-Vendor Concentration: 68% Microsoft Dependency -- CRITICAL

- **Categoria:** Fundamental
- **Descripcion:** 68% of Bytes' Gross Invoiced Income comes from Microsoft products. This creates extreme dependency on a single vendor's commercial decisions. Microsoft controls the economics of Bytes' business through: (a) incentive rates, (b) partner eligibility thresholds, (c) direct vs. partner sales allocation, (d) pricing policies. Every major negative event in Bytes' recent history traces back to a Microsoft decision.
- **Evidencia:**
  - 68% GII from Microsoft (company disclosure)
  - H1 FY2026 profit decline caused by Microsoft incentive restructuring
  - July 2025 profit warning caused by Microsoft EA direct sales
  - Historical precedent: Microsoft has progressively squeezed partner margins over multiple cycles (2013, 2022, 2023, 2025)
  - Microsoft's stated strategy is "partner quality over quantity" -- consolidating to fewer, larger partners
- **Probabilidad:** Alta -- The concentration is a structural fact. Microsoft's willingness to squeeze partners is demonstrated repeatedly.
- **Impacto si materializa:** A single adverse Microsoft decision can wipe 10-20% off Bytes' profitability in a single fiscal year, as H1 FY2026 demonstrated. If Microsoft decides to go even more direct (extending beyond large EAs to mid-market), the impact could be existential.
- **Mitigante:** Bytes' services segment (non-Microsoft) is growing 40%+. Cybersecurity and other vendor partnerships reduce dependency over time. But at 68%, diversification will take years.
- **Kill condition?:** **YES** -- Should be explicit: "If Microsoft dependency exceeds 70% AND Microsoft announces further direct sales expansion, EXIT."

---

### 3. Operating Cost Inflation vs. Flat Revenue Growth -- HIGH

- **Categoria:** Financiero
- **Descripcion:** Bytes is simultaneously experiencing: (a) GP growth near zero (+0.4% H1), (b) headcount growth of +12%, (c) employee cost increase of +5.9% to GBP 39.4M, (d) UK National Insurance employer rate increase from 13.8% to 15% (effective April 2025), (e) operating efficiency ratio declining from 43.4% to 40.2%. This is a classic margin scissors: costs rising while revenue stagnates.
- **Evidencia:**
  - H1 FY2026: GP +0.4%, employee costs +5.9%, OP -7.0%
  - Headcount up 12% YoY to 1,266
  - UK NI increase adds ~2% to payroll costs (OBR estimate)
  - Operating efficiency ratio: 43.4% -> 40.2% (-3.2pp in one half)
  - Berenberg downgrade specifically cited "disruption is unlikely to be limited to H1"
- **Probabilidad:** Alta -- Cost pressures are already biting. NI increase is a fait accompli. Headcount was hired for growth that hasn't materialized.
- **Impacto si materializa:** If the cost-revenue scissors persist for 2+ years, operating profit could decline 15-25% from peak. At current P/E of 14.6x, the market may already be partially pricing this in, but further deterioration could push P/E to 12-13x on lower earnings, implying 230-260 GBp.
- **Mitigante:** Variable remuneration declined (partly offsetting). Management guides improvement in H2 FY2026. Headcount growth is slowing (only +1.7% since Feb 2025 vs +12% YoY). Services revenue growth should eventually cover costs.
- **Kill condition?:** No, but should be monitored. If operating efficiency ratio falls below 35%, it indicates structural cost problem.

---

## Riesgos NO Mencionados en Thesis

| Riesgo | Severidad | Mencionado en thesis? | Comentario |
|--------|-----------|----------------------|------------|
| Microsoft EA direct sales takeover (LSP commissions -> $0 by 2026) | **CRITICAL** | NO -- Thesis mentions "incentive restructuring" but NOT the EA direct sales model | The thesis treats all Microsoft changes as one "cyclical adjustment." The EA direct sales takeover is qualitatively different and far more severe. |
| UK National Insurance increase (+2% payroll costs from April 2025) | **HIGH** | NO | Thesis mentions "labor costs manageable" but doesn't quantify the NI impact on a 1,266-person headcount |
| Headcount grew 12% while GP grew 0.4% | **HIGH** | Partially -- mentioned in H1 results but not flagged as risk | Thesis presents headcount growth as "investing for future" rather than as a cost risk if revenue doesn't recover |
| Former CEO Neil Murphy share dealing investigation | **MEDIUM** | NO | 119 undisclosed share transactions over 3 years. FCA closed case but this is a governance red flag not addressed in thesis |
| Berenberg downgrade: "disruption unlikely limited to H1" | **MEDIUM** | NO | Thesis references Berenberg TP cut but not the qualitative assessment that disruption continues |
| Public sector spending cuts from 2026/27 (UK government) | **HIGH** | Minimized | Thesis says "public sector recovery expected" based on NHS digital mandates, but UK government is planning real-terms spending cuts from 2026/27 for unprotected departments |
| NHS/public sector = 65% of GII (dual concentration) | **MEDIUM** | Partially | Thesis mentions ~50% public sector but the 65% figure from earnings call is higher |
| Analyst consensus deteriorating (4 Hold / 1 Buy; was more bullish) | **LOW** | NO | Multiple downgrades from Jefferies (Jan 2026), Berenberg (July 2025), Deutsche Bank |
| Microsoft marketplace enabling direct ISV-to-customer sales | **MEDIUM** | NO | Azure Marketplace private offers and direct ISV sales reduce VAR intermediation role |

---

## Fair Value Challenge

### Thesis FV: 455 GBp -- CHALLENGED

The thesis uses OEY (60% weight) + DCF (40% weight) to arrive at 455 GBp.

### My DCF Results (Multiple Scenarios)

| Scenario | Growth | WACC | Terminal | FV/Share | MoS vs 306p |
|----------|--------|------|----------|----------|-------------|
| Thesis Default | 5% | 9% | 2.5% | 500p | +63% |
| Thesis Conservative | 6% | 10% | 2% | 432p | +41% |
| **My Base Case** | 6% | 10% | 2% | **432p** | +41% |
| **My Bear Case** | 4% | 11% | 1.5% | **343p** | +12% |
| Very Bear (EA loss) | 2% | 11% | 1.5% | ~280p | -8% |

### Problems with Thesis Valuation

1. **OEY Method (60% weight):** The thesis calculates OEY + Growth = 14.4% using 8% GP growth. But H1 showed 0.4% GP growth, and Berenberg argues disruption continues. Using 5% GP growth (more realistic near-term), OEY + Growth = 11.4%, and the "fair value where OEY + Growth = 12%" becomes approximately 370-380p, not 470p.

2. **DCF Growth Rate:** The thesis uses 8% as base case. Historical FCF CAGR is 8.1%, but this includes periods before the Microsoft structural shift. Forward growth should be 4-6% until the services pivot matures, which could take 2-3 years.

3. **WACC of 9%:** The thesis argues for 9% based on defensive recurring revenue. But with 68% Microsoft dependency and structural headwinds, 10-11% WACC is more appropriate for the actual risk profile.

4. **EV/EBIT Peer Comparison:** Thesis says "BYIT at 11x vs Softcat at 20x is massive discount." But Softcat trades at 17.7x P/E (current data from price_checker: 1171 GBp, P/E 17.7x) -- the gap is 14.6x vs 17.7x, NOT 14x vs 25x as thesis suggests. Softcat's market also reflects its higher ROIC (36% vs Bytes' lower ROIC).

### My Risk-Adjusted Fair Value

| Method | Value | Weight |
|--------|-------|--------|
| DCF Conservative (6%, 10%, 2%) | 432p | 20% |
| DCF Bear (4%, 11%, 1.5%) | 343p | 30% |
| OEY adjusted (5% growth) | 380p | 30% |
| EV/EBIT 13x (discounted to Softcat, reflecting risk) | 350p | 20% |

**Weighted Risk-Adjusted FV: (432x0.20) + (343x0.30) + (380x0.30) + (350x0.20) = 86 + 103 + 114 + 70 = 373 GBp**

**Risk-Adjusted FV: ~370 GBp (vs thesis 455 GBp) -- 18% lower**

At 306 GBp, this implies MoS of ~17%, which is adequate for Tier B but not exceptional.

---

## Kill Conditions Assessment

### Thesis Kill Conditions -- Are They Adequate?

| # | Kill Condition | Adequate? | My Assessment |
|---|---------------|-----------|---------------|
| 1 | Microsoft structurally disintermediates VARs | **TOO NARROW** | This is already happening via EA direct sales. The thesis frames it as "launches a direct-sales platform" -- but it's not a platform, it's Microsoft's own sales team taking over accounts. Should trigger NOW for EA segment. |
| 2 | FCF negative 2+ years | **TOO GENEROUS** | FCF could remain positive while operating profit declines 30%+. A 2-year lag is too slow to react. |
| 3 | Services growth below 10% | **ADEQUATE** | This is the right metric to watch. If services can't offset Microsoft EA losses, the bull case collapses. |
| 4 | Major customer/framework loss | **ADEQUATE** | Loss of G-Cloud would be devastating. |
| 5 | QS falls below 75 | **ALREADY TRIGGERED** by my analysis | My risk-adjusted QS is 72. |

### Kill Conditions That Should Be Added

1. **Microsoft EA direct sales expansion to mid-market** -- If Microsoft extends direct sales below the "large EA" threshold, Bytes loses its last safe harbor in EA business.
2. **Operating efficiency ratio below 35%** -- Currently 40.2% and declining. Below 35% indicates structural cost problem.
3. **Microsoft dependency remains above 65% for 3+ years with no trend improvement** -- Diversification must happen.
4. **Two consecutive profit warnings** -- Already had one (July 2025). A second would indicate deeper problems.

---

## Riesgo Agregado

- Numero de riesgos HIGH+CRITICAL: **5** (EA takeover, vendor concentration, cost inflation, public sector cuts, Microsoft incentive structural)
- Riesgos correlacionados: **YES** -- Risks #1, #2, and the Microsoft incentive compression are all manifestations of the SAME root cause: Microsoft's strategic decision to capture more value from its ecosystem. These risks are not independent; they compound.
- The correlation factor is critical: a negative Microsoft decision doesn't just affect one risk -- it simultaneously worsens vendor dependency, margin compression, and EA revenue loss.

**Risk Score Final: HIGH**

Rationale: 5 HIGH/CRITICAL risks, 3 of which are correlated (same root cause: Microsoft strategy). The thesis's core assumption -- that Microsoft changes are cyclical -- is contradicted by structural evidence. The adjusted QS falls to Tier B. The risk-adjusted FV is 18% below thesis FV. While the business has genuine quality attributes (net cash, 30% FCF margin, services growth), the risk profile is materially higher than the thesis acknowledges.

---

## Scenario Analysis: What If the Market Is Right?

The market has priced BYIT at 306 GBp, down 47% from 563 GBp. The thesis says this is "overreaction." But consider:

**What the market may know:**
1. Microsoft EA direct sales are accelerating (multiple sources confirm)
2. H1 was disappointing AND Berenberg says H2 won't be much better
3. UK public sector spending faces real cuts from 2026/27
4. Headcount was hired for growth that didn't materialize
5. The competitive gap with Softcat is narrowing (Softcat P/E compressed too, but from 30x to 17.7x vs Bytes from 25x to 14.6x -- proportionally similar)

**What the market may NOT know:**
1. Services growth is genuinely strong at 40%+
2. Net cash position provides safety
3. AI advisory services could be a meaningful new revenue stream
4. Consolidation of smaller VARs due to $1M CSP threshold benefits Bytes

**Verdict:** The market is likely overreacting on the *degree* of impairment but may be right about the *direction*. The fair value is probably between the market price (306p) and the thesis FV (455p) -- my estimate of ~370p.

---

## 🔄 META-REFLECTION

### Dudas/Incertidumbres
- **Microsoft EA vs CSP distinction:** I'm not 100% certain how much of Bytes' Microsoft revenue is EA-related vs CSP-related. If the majority is CSP (which is NOT being taken direct), the EA risk is less severe than my assessment suggests. The thesis doesn't break this down and the earnings reports are vague.
- **Services growth sustainability:** 40% growth on a small base could decelerate rapidly as the base grows. I can't assess how sustainable this is without more granular data.
- **Berenberg "disruption continues" assessment vs management "settled into new structure":** These directly contradict each other. I leaned toward Berenberg (bearish) but management may have better visibility.
- **Softcat P/E compression:** If Softcat has also compressed from 30x to 17.7x, it suggests the entire UK VAR sector is being re-rated, not just Bytes. This could mean both are cheap or both are correctly repricing structural risk.

### Riesgos que Podrian Estar Subestimados
- **Microsoft EA direct sales is potentially the most important risk and may be HIGHER than HIGH.** If Microsoft's trend of reclaiming EA renewals accelerates to ALL account sizes (not just "large"), the impact on Bytes could be catastrophic -- not just a margin squeeze but a structural erosion of 30-40% of gross profit.
- **UK public sector IT spending cuts from 2026/27** -- I scored this as HIGH but it could be CRITICAL if the Labour government faces fiscal pressure and cuts unprotected department IT budgets.

### Discrepancias con Thesis
1. **The most critical discrepancy:** The thesis treats ALL Microsoft changes as one "cyclical adjustment." My research reveals two separate phenomena: (a) incentive restructuring (cyclical-ish), and (b) EA direct sales takeover (structural). The thesis conflates them.
2. **QS 81 vs my 72:** The thesis uses backward-looking metrics that don't capture forward growth deterioration or the moat erosion from Microsoft's strategic shift.
3. **FV 455p vs my 370p:** 18% gap driven by growth rate assumptions and risk premium adjustments.
4. **"Probability I'm wrong: 25%" on Microsoft thesis:** I would say 50-60%. The evidence of structural shift is strong.
5. **Value trap score 0/10:** I would give it 2-3/10. Not a classic value trap, but "market share loss >2pp 3yr" could trigger if Microsoft takes EA direct AND Softcat captures the displaced business.

### Sugerencias para el Sistema
1. **For any company with >50% revenue from a single vendor:** Mandatory deep-dive on that vendor's channel strategy and historical behavior toward partners. The thesis should explicitly quantify vendor dependency risk.
2. **QS tool should have a "forward adjustment" mode:** Allow inputting expected growth rates vs historical to see how QS would change under stress scenarios.
3. **The kill condition "Microsoft structurally disintermediates VARs" is already partially triggered:** The EA direct sales model IS structural disintermediation of the EA channel. The thesis should acknowledge this explicitly.

### Preguntas para Orchestrator
1. **What percentage of Bytes' gross profit comes from EA commissions vs CSP margin vs services?** This is critical to quantify Risk #1 precisely. The thesis doesn't provide this breakdown.
2. **Should the position be reduced given that my risk-adjusted QS is 72 (Tier B)?** The purchase was justified as Tier A with 35% MoS. If it's actually Tier B, the MoS should be ~20-25% to be appropriate, and my risk-adjusted FV of 370p gives only 17% MoS at current price.
3. **Should we add the EA direct sales kill condition NOW?** The thesis currently has "Microsoft structurally disintermediates VARs" but this is too vague. A specific kill condition tied to EA direct sales expansion would be more actionable.
4. **Is there a pattern in our adversarial reviews of systematically finding that theses understate the primary risk?** This may be the same pattern seen in other reviews (A2A, VNA, TATE) where the headline risk was more severe than acknowledged.

---

**Assessment by:** Risk Identifier Agent (Independent)
**Date:** 2026-02-09
**Confidence:** Medium-High (key uncertainty: EA vs CSP revenue split)
