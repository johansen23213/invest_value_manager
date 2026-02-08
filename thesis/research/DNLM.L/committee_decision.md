# INVESTMENT COMMITTEE DECISION: DNLM.L (Dunelm Group plc)

**Date:** 2026-02-07
**Committee:** Investment Committee (10 Gates v4.0)
**Framework:** v4.0 -- Principios Adaptativos
**Buy-Pipeline Round:** 4 of 4 (Final Gate)

---

## VERDICT: WATCHLIST -- Entry trigger 750-800p

**NOT a BUY at 936.5p. NOT a BUY at 900p (thesis trigger). Entry lowered to 750-800p.**

Dunelm is a genuinely high-quality business (QS 79, Tier A, 0-1/10 value trap) that fails the valuation gate at current prices. The 4-round adversarial process exposed five material issues in the thesis: (1) a factual error on insider selling, (2) omission of GBP 18M NIC/NLW structural headwind, (3) omission of Temu/Amazon competitive threat, (4) omission of CEO transition risk, and (5) systematic optimism in the FV calculation resulting in a 24% overstatement vs the independent valuation.

The risk-adjusted FV of 1,008p (valuation-specialist) yields only 7.1% MoS at 936.5p -- grossly insufficient vs our Tier A precedent range of 29-38%. Even the thesis's 900p entry target delivers only 10.7% MoS against the independent FV. The entry trigger is lowered to 750-800p (MoS 20-26%) to bring the trade closer to framework consistency.

Wait for interim results on 10 February before setting any standing order.

---

## INDEPENDENT REPORTS RECEIVED

| Report | Agent | Key Finding |
|--------|-------|-------------|
| thesis.md | fundamental-analyst | QS 79 Tier A, FV 1,328p, MoS 29.5%, WATCHLIST 900p |
| moat_assessment.md | moat-assessor | NARROW moat (not WIDE), trending toward WIDE |
| risk_assessment.md | risk-identifier | MEDIUM risk, 1 CRITICAL + 3 HIGH, correlated UK macro |
| valuation_report.md | valuation-specialist | FV 1,008p (risk-adjusted), MoS 7.1% |
| counter_analysis.md | devil's-advocate | STRONG COUNTER, 9/19 challenges HIGH/CRITICAL |

**Conflict resolution (Round 3):**
- FV adopted: 1,008p (valuation-specialist, risk-adjusted)
- Thesis FV of 1,328p REJECTED (5 specific methodological/omission flaws)
- Moat classification: NARROW (moat-assessor)
- Entry trigger: 750-800p (committee, lowered from thesis 900p)

---

## GATE-BY-GATE EVALUATION

### Gate 0: Sector View Exists (HARD GATE)

```
[PASS] Sector view: world/sectors/consumer-discretionary.md
       Updated: 2026-02-07 with UK Homewares sub-section
       DNLM.L in Watchlist and Dependencias Activas
```

---

### Gate 1: QUALITY SCORE (CRITICAL)

```
[PASS] Quality Score: 79/100
[PASS] Tier: A (Quality Compounder)
[N/A]  Tier D check: NOT Tier D, proceed
```

Verified via `quality_scorer.py` tool on 2026-02-07.

| Category | Score | Max | Key Metrics |
|----------|-------|-----|-------------|
| Financial Quality | 32 | 40 | ROIC spread +16.8pp, FCF margin 11.9%, leverage 0.33x ex-leases, 4/5 FCF |
| Growth Quality | 15 | 25 | Revenue CAGR ~5%, EPS CAGR ~5%, GM expanding +60bp YoY |
| Moat Evidence | 22 | 25 | GM premium +17.4pp vs sector, #1 UK homewares, ROIC persistent |
| Capital Allocation | 10 | 10 | 10+ yr dividends, 37.6% insider (Adderley family, corrected) |
| **TOTAL** | **79** | **100** | **Tier A - Quality Compounder** |

Quality is genuine and undisputed by all four independent reports. Would be the 7th Tier A in portfolio (ADBE, NVO, MONY.L, LULU, AUTO.L, BYIT.L), advancing Principio 9 (Quality Gravitates Upward).

**Gate 1: PASS**

---

### Gate 2: Business Understanding

```
[PASS] Business Analysis Framework completed
[PASS] 2-minute explanation:
       Dunelm is the UK's #1 homewares specialist retailer (200+ stores, 41% digital).
       Revenue from own-brand and curated homewares (curtains, bedding, kitchenware, furniture).
       52.4% gross margin (+17pp vs sector) driven by ~30% private label penetration.
       Gaining market share (7.7% to 7.9%, targeting 10%) during consumer downturn.
       Down 25% from high after Q2 deceleration and profit guidance to low end.

[PASS with CAVEATS] Why cheap + counter-thesis understood:
       Market prices prolonged UK consumer weakness (correct concern).
       Market conflates Dunelm-specific performance with sector-wide weakness (my edge).
       GM improved 60bp DURING competitor discounting = pricing power evidence.
       BUT thesis overstates defensive characteristics ("consumer staple in disguise").
       CORRECTED classification: "defensive discretionary" per moat-assessor.

[PASS] Value trap checklist: 1/10 (corrected from thesis 0/10 for insider selling)
       Well below 3 threshold. No value trap concern.

[PASS with CAVEAT] Informational edge identified: longer time horizon + margin resilience
       misread by market. Edge partially offset by thesis errors exposed by adversarial process.
```

**Gate 2: CONDITIONAL PASS** -- Business understanding is solid. Thesis contained a factual error (insider selling: family sold 5% at 1,140p in Jul 2025, thesis stated "no recent sales") and three material omissions (NIC/NLW, Temu, CEO transition) corrected by independent agents.

---

### Gate 3: Projections

```
[PASS] Revenue growth derived (not default):
       TAM 3.5% + Share 0.5% + Pricing 1% = 5% (thesis base)
       Risk-adjusted: 3% year 1 (consumer weakness + NIC/NLW), 5% from year 2
       Derivation: KPMG/Fitch/RSM project UK weakness through end 2026

[PASS] WACC calculated (not default):
       Thesis: 9.0% (Rf 4.2% + Beta 0.9 x ERP 5.5%)
       Risk-adjusted: 9.5% (+0.5pp for correlated UK macro risks)
       ADOPTED: 9.5% -- consumer + NIC/NLW + fiscal risks are the same bet

[PASS] Terminal growth justified: 2.0% (conservative, below UK long-term GDP)

[PASS] Scenarios documented:
       Bear (25%): 0% rev growth 2yr, 11% OpM, 10.5% WACC -> FV 736p
       Base (50%): 3%/5% rev growth, 11.8-12% OpM, 9.5% WACC -> FV 1,008p
       Bull (25%): 6% rev growth, 12.5-13% OpM, 9.0% WACC -> FV 1,423p
       Expected Value: 1,044p
```

**Gate 3: PASS** -- Using valuation-specialist risk-adjusted projections.

---

### Gate 4: Valuation Multi-Method

```
[PASS] Methods appropriate for Tier A:
       Primary (50%): Owner Earnings Yield -- correct per skill
       Secondary (30%): EV/EBIT Normalized -- correct for stable retailer
       Tertiary (20%): DDM -- appropriate cross-check given 4.8% yield
```

#### Thesis vs Valuation-Specialist Divergence

| Method | Thesis FV | Valuation-Specialist FV | Delta |
|--------|-----------|------------------------|-------|
| OEY | 1,491p | 1,036p | -30% |
| EV/EBIT | 1,156p | 977p | -15% |
| DDM | 1,175p | 987p | -16% |
| **Weighted** | **1,328p** | **1,008p** | **-24%** |

#### FV Adopted: 1,008p (Valuation-Specialist)

Five specific reasons the thesis FV of 1,328p was rejected:

1. **OEY calculation error:** Thesis used raw FCF (GBP 211M). The valuation-methods skill defines OEY as Owner Earnings (FCF minus maintenance capex) / Market Cap. Forward Owner Earnings = GBP 152M (after NIC/NLW and maintenance capex). This single error inflated the OEY-derived FV by ~40%.

2. **GBP 18M NIC/NLW omission:** Confirmed structural regulatory cost (employer NIC up 1.2pp to 15%, threshold lowered; NLW up 4.1% from April 2026). Not mentioned anywhere in thesis. Reduces forward PBT by ~GBP 9M net (50% offset assumed via productivity/pricing).

3. **WIDE moat premium applied to NARROW moat:** Thesis used 11x EV/EBIT (+2x quality premium). Moat-assessor independently classified NARROW (zero switching costs, online commoditization threat). 10x is appropriate.

4. **WACC too low:** 9.0% does not reflect correlated UK macro risks (consumer weakness + NIC/NLW + fiscal contraction are the same bet). 9.5% justified.

5. **Insider reality check:** Adderley family sold GBP 114M at 1,140p (Jul 2025). FV of 1,328p implies informed 47-year insiders left 17% on the table. 1,008p is more consistent with insider behavior.

#### Method Convergence (Valuation-Specialist)

| Method | FV | Weight | Weighted |
|--------|-----|--------|----------|
| OEY (risk-adjusted, forward) | 1,036p | 50% | 518p |
| EV/EBIT 10x (normalized) | 977p | 30% | 293p |
| DDM (weighted ordinary + specials) | 987p | 20% | 197p |
| **Weighted Average** | | **100%** | **1,008p** |

Divergence between methods: 6.0% (well below 30% threshold). High confidence.

#### MoS at Various Prices

| Price | MoS vs 1,008p | MoS vs Bear (736p) |
|-------|--------------|---------------------|
| 936.5p (current) | 7.1% | -21.4% |
| 900p (thesis entry) | 10.7% | -18.2% |
| 800p | 20.6% | -8.0% |
| 750p | 25.6% | -1.9% |
| 715p | 29.1% | +2.9% |

**Gate 4: PASS on methodology. MoS assessment in Gate 5.**

---

### Gate 5: Margin of Safety (Razonado v4.0)

```
Tier: A (QS 79)
MoS Actual vs Base (1,008p): 7.1%
MoS Actual vs Bear (736p): -21.4% (NEGATIVE)
```

#### Precedent Analysis

| Ticker | QS | MoS at Entry | Price Context | Verdict |
|--------|-----|-------------|---------------|---------|
| NVO | 82 | 38% | -49% from high, -17% in 2 days | BUY |
| MONY.L | 81 | 36% | At 52-week low | BUY |
| BYIT.L | 81 | 35% | -47% from high | BUY |
| LULU | 82 | 34% | -58% from high | BUY |
| ADBE | 76 | 31% | At 52-week low | BUY |
| AUTO.L | 79 | 29% | -47% from high | BUY |
| **DNLM.L at 936.5p** | **79** | **7.1%** | **-25% from high** | **INSUFFICIENT** |
| **DNLM.L at 900p** | **79** | **10.7%** | | **INSUFFICIENT** |
| **DNLM.L at 800p** | **79** | **20.6%** | | **Approaching** |
| **DNLM.L at 750p** | **79** | **25.6%** | | **Acceptable** |

**Closest precedent:** AUTO.L -- same QS (79), same Tier A. Bought at 29% MoS.

**Deviation from precedent:** YES -- 22pp gap at current price. NOT approved.

#### Reasoning

1. **7.1% MoS provides no buffer** against the bear case (-21% downside). If even ONE of the correlated UK macro risks materializes fully (consumer recession, NIC/NLW unmitigated, fiscal contraction), the stock trades below current price.

2. **7.1% is below the minimum typical** for ANY tier per decisions_log pattern ("10-15% minimum typical" for Tier A).

3. **The thesis's 29.5% MoS was based on a flawed FV** of 1,328p. The corrected FV transforms this from "at precedent" to "well below precedent."

4. **Binary event in 3 days** (10 Feb interims). No reason to commit capital before a potential entry-creating event.

5. **Even at 900p, MoS is only 10.7%** -- still far below any Tier A precedent.

#### Entry Trigger: 750-800p

- At 750p, MoS 25.6% is within 4pp of minimum precedent (AUTO.L 29%)
- Deviation justifiable because Dunelm has the strongest OEY+Growth vs WACC spread (12-13% at these prices) of any Tier A candidate in our pipeline
- Below 800p, the 4.8%+ dividend yield provides real compensation while waiting
- 750p is plausible if interims disappoint and/or UK consumer weakness continues
- Going to 715p (full precedent match) may be overly demanding and could result in missing a genuinely excellent business

900p is NOT acceptable because 10.7% MoS provides no meaningful buffer and represents a massive unjustified deviation from all 6 Tier A precedents.

**Gate 5: FAIL at 936.5p. FAIL at 900p. CONDITIONAL PASS at 750-800p.**

---

### Gate 6: Macro Context

```
[PASS with CAUTION] World view reviewed (2026-02-05):
       UK GDP: +1.2% 2026 (stagnation, not recession)
       UK inflation: 2% (target achieved)
       Consumer confidence: -16 (weak, barely improving)
       BCE/Fed: Holding rates
       Tariffs: UK less exposed than US
       Iran-US: De-escalating (positive)

Cycle: LATE CYCLE for consumer discretionary
       UK consumer weakness projected through end 2026 (KPMG, Fitch, RSM)
       NIC/NLW costs hitting UK retailers from April 2025/2026
       Only 13% of consumers expect higher discretionary spending in 2026
       Dunelm management: "yet to see signs of sustained consumer recovery"

Fit empresa-ciclo:
       Dunelm is defensive WITHIN discretionary (homewares refresh/replace)
       NOT a consumer staple -- would be affected by genuine UK recession
       Late-cycle NOT ideal for consumer discretionary entry
       BUT stock already discounts significant pessimism (0% FCF growth implied)

Megatrends:
       AI: Neutral | Demographics: Slightly positive | Omnichannel: Positive
       Temu/Amazon: Negative (commodity category competition)
```

**Gate 6: PASS** -- Macro supports WATCHLIST. Late-cycle caution appropriate.

---

### Gate 7: Portfolio Fit (Razonado v4.0)

```
Portfolio context:
  19 positions, ~EUR 1,979 cash (~20%)
  6 Tier A: ADBE, NVO, MONY.L, LULU, AUTO.L, BYIT.L
  UK positions: AUTO.L, MONY.L, IMB.L, TATE.L, DOM.L, BYIT.L = 6

Sizing (if entry triggered at 750-800p):
  Proposed: 3.0-3.5% initial (~EUR 300-350)
  Consistent with Tier A precedents (3.4-4.8%, median 3.5%)
  At 50% loss: 1.5-1.75% portfolio impact -- acceptable for high conviction Tier A
  Precedent: AUTO.L 3.4%, BYIT.L 3.5%, LULU 3.5% (same tier, similar context)

UK geographic concentration:
  Current: 6 UK positions (~25-28% of portfolio)
  Post-DNLM.L: 7 UK positions (~28-31%)
  Sub-sectors: auto classifieds, price comparison, tobacco, food ingredients,
               pubs/restaurants, IT services, homewares -- LOW correlation
  Macro correlation: HIGH -- all exposed to UK GDP, confidence, NIC/NLW, GBP, BoE
  Assessment: ACCEPTABLE BUT AT THE MARGIN
  Constraint: No further UK consumer-facing positions after DNLM.L

Sectoral concentration:
  Consumer Discretionary: currently LULU only (~3%)
  Post-DNLM.L: ~6% -- well within reason
  Different sub-sectors (athleisure vs homewares), low correlation

Cash deployment:
  Current: ~EUR 1,979 (~20%)
  Post-purchase: ~EUR 1,629-1,679 (~16-17%)
  Adequate dry powder remains (Principio 4)

Correlation with existing:
  LOW: most positions (different sectors/geographies)
  MEDIUM: DOM.L (both UK consumer-facing)
  LOW: MONY.L, AUTO.L, BYIT.L (different consumer segments)
```

**Gate 7: CONDITIONAL PASS** -- Sizing at 3-3.5% appropriate. UK concentration at 7 positions is the margin. No further UK consumer-facing additions.

---

### Gate 8: Sector Understanding

```
[PASS] Sector view exists: world/sectors/consumer-discretionary.md
[PASS] Updated 2026-02-07 with UK Homewares sub-section
[PASS] TAM: ~GBP 17B UK homewares + furniture, ~4.2% CAGR
[PASS] Competitive dynamics: Dunelm #1 specialist, IKEA #1 overall,
       fragmented market, Temu/Amazon emerging threat documented
[PASS] Disruption risks: Temu/Amazon commoditization (5-10yr horizon)
[PASS] Sector position: NEUTRAL
```

**Gate 8: PASS**

---

### Gate 9: Autocritica

#### Assumptions Not Validated
1. NIC/NLW offset rate: 50% assumed (range 30-70%). Need management commentary at 10 Feb interims.
2. Consumer weakness duration: adopted KPMG/Fitch/RSM consensus (through end 2026), but forecasters have poor track records at calling turning points.
3. Adderley family selling motive: assumed informational (bearish signal), could be purely personal (benign).
4. Temu competitive overlap with Dunelm: extrapolated from platform-level data, actual category overlap uncertain.

#### Biases Recognized
- **Popularity bias:** Mitigated -- DNLM.L identified through systematic screening, not training data familiarity.
- **Confirmation bias:** Actively countered -- adopted STRONG COUNTER findings and lower FV despite compelling business quality.
- **Recency bias:** Aware that recent successful Tier A purchases could create momentum to "keep buying Tier A" at lower standards.

#### Kill Conditions (expanded from thesis + risk-identifier suggestions)
1. Gross Margin falls below 48% (currently 52.4%)
2. Market share declines 2 consecutive years (currently gaining)
3. FCF negative 2 consecutive years
4. Adderley family holding drops below 30% (currently ~37.6%)
5. Operating margin falls below 10.5% for 2 consecutive periods (currently 12.5%)
6. Digital sales penetration stalls or declines (currently 41%, growing 3pp/yr)
7. Dividend cut >30%
8. Net debt ex-leases exceeds 2.0x EBITDA (currently 0.33x)

#### What Would Change My Mind
- Interim results 10 Feb showing H1 PBT >= 114M, GM expanding, special dividend, positive H2 commentary -- could justify 850-900p entry with updated FV
- Stock falls to 750-800p -- entry per standing order
- UK consumer confidence improves materially above -10 for 2 consecutive months
- NIC/NLW impact proves smaller than feared (management guidance at interims)

**Gate 9: PASS**

---

### Gate 10: Counter-Analysis & Independent Assessments

#### Counter-Analysis (devil's-advocate)
```
[YES] counter_analysis.md exists
[STRONG COUNTER] Verdict: 19 total challenges, 1 CRITICAL + 8 HIGH
```

**Resolution of each HIGH/CRITICAL challenge:**

| # | Challenge | Severity | Resolution |
|---|-----------|----------|------------|
| 1 | Thesis FV 1,328p is 24% above independent 1,008p | CRITICAL | RESOLVED: Adopted 1,008p |
| 2 | MoS 7.1% grossly insufficient for Tier A | HIGH | RESOLVED: Entry lowered to 750-800p |
| 3 | OEY calculation uses raw FCF not Owner Earnings | HIGH | RESOLVED: Adopted valuation-specialist OEY |
| 4 | NIC/NLW GBP 18M headwind not in thesis | HIGH | RESOLVED: Incorporated in risk-adjusted FV |
| 5 | "Consumer staple" claim unsupported | HIGH | RESOLVED: Reclassified "defensive discretionary" |
| 6 | Insider selling factual error | HIGH | RESOLVED: Corrected to 37.6%, VT score 1/10 |
| 7 | Three risks correlated (UK macro theme) | HIGH | RESOLVED: WACC +0.5pp, WATCHLIST buffer |
| 8 | Consumer weakness duration understated | HIGH | RESOLVED: Adopted KPMG/Fitch/RSM consensus |
| 9 | Interim results binary event in 3 days | HIGH | RESOLVED: WAIT for results before committing |

**Unresolved CRITICAL challenges: ZERO.**

#### Moat Assessment (moat-assessor)
```
[YES] moat_assessment.md exists
[NARROW] Classification -- differs from thesis "Medium-High"
ADOPTED: NARROW. Zero switching costs + online commoditization prevent WIDE.
```

| Moat Source | Rating | Durability |
|-------------|--------|------------|
| Cost advantage (private label + scale) | 4/5 | 15-20 years |
| Intangible assets (brand + Dorma) | 4/5 | 15-20 years |
| Efficient scale | 3/5 | 10-15 years |
| Switching costs | 1/5 | N/A |
| Network effects | 1/5 | N/A |

#### Risk Assessment (risk-identifier)
```
[YES] risk_assessment.md exists
[MEDIUM] Overall risk score
4 HIGH/CRITICAL risks identified:
  - UK consumer prolonged weakness (CRITICAL)
  - NIC/NLW GBP 18M headwind (HIGH)
  - Temu/Amazon disruption (HIGH)
  - UK macro stagnation (HIGH)

Risks NOT in thesis: NIC/NLW, insider selling error, Temu, CEO transition
Additional kill conditions adopted: OpM <10.5%, Adderley <30%, digital stalls
```

#### Valuation Report (valuation-specialist)
```
[YES] valuation_report.md exists
[YES] FV diverges >15% vs thesis: 1,008p vs 1,328p = 24% -- INVESTIGATED
      Root causes identified (5 flaws). 1,008p adopted.
[YES] Sensitivity documented: 736p (bear) to 1,423p (bull)
      Bear case downside -21% is material.
```

#### Systematic Finding

All three independent reports (moat, risk, valuation) reached MORE CONSERVATIVE conclusions than the thesis. This consistent directional bias toward optimism in the thesis is itself a finding that informed the committee's decision to adopt conservative parameters throughout.

**Gate 10: PASS** -- All CRITICAL/HIGH challenges resolved.

---

## FINAL RECOMMENDATION

```
WATCHLIST: DNLM.L (Dunelm Group plc)

Quality Score: 79/100 -- Tier A (Quality Compounder)
Fair Value (committee-adopted): 1,008p
Moat: NARROW (moat-assessor)
Risk: MEDIUM (1 CRITICAL + 3 HIGH, correlated UK macro theme)

Current Price: 936.5p | MoS: 7.1% -- INSUFFICIENT
Thesis Entry 900p: MoS 10.7% -- INSUFFICIENT

ENTRY TRIGGER: 750-800p (MoS 20-26%)
SIZING: 3.0-3.5% initial (~EUR 300-350)
ADD TRIGGER: 650p (MoS 35%+)

CONDITIONS FOR ENTRY:
  Path A: Price reaches 750-800p (after 10 Feb interims)
  Path B: Interim results on 10 Feb significantly de-risk thesis:
          H1 PBT >= 114M confirmed
          Management quantifies NIC/NLW showing <50% PBT impact
          Special dividend announced
          Positive H2 commentary with recovery indicators
          IF all four met, reconsider entry at 850-900p with updated FV

STANDING ORDER: Do NOT set until AFTER 10 Feb interim results.
Post-results: set at 800p if neutral, 750p if disappointing.

NEXT ACTION: Monitor interim results 10 February 2026. Re-evaluate.
```

---

## SCENARIOS SUMMARY

| Scenario | FV | Probability | Upside/Downside from 936.5p |
|----------|-----|------------|---------------------------|
| Bear | 736p | 25% | -21.4% |
| Base | 1,008p | 50% | +7.6% |
| Bull | 1,423p | 25% | +51.9% |
| **Expected** | **1,044p** | **100%** | **+11.5%** |

At 750p entry, the scenarios transform:

| Scenario | FV | Upside/Downside from 750p |
|----------|-----|--------------------------|
| Bear | 736p | -1.9% |
| Base | 1,008p | +34.4% |
| Bull | 1,423p | +89.7% |
| **Expected** | **1,044p** | **+39.2%** |

The asymmetry at 750p is dramatically superior: -2% down vs +90% up (Bull), +34% up (Base).

---

## META-REFLECTION

### Dudas sobre esta decision

- **Am I being too demanding on MoS?** The OEY+Growth vs WACC spread at current prices is the best in our pipeline. When three independent methods converge tightly (6% divergence), perhaps less MoS is justified because valuation uncertainty is lower. Counter-argument: MoS protects against risks we have not identified, not just valuation errors.

- **Adderley family selling is ambiguous.** If purely personal diversification (benign), using their 1,140p sell price as a FV ceiling is overly conservative. We cannot know their actual motive.

- **Consumer recovery could come faster than KPMG/Fitch project.** If Q3 2026 recovery materializes, stock re-rates to 1,100-1,200p before reaching 750-800p trigger, and we miss a genuine quality compounder. This is the real risk of the WATCHLIST decision -- missing the opportunity.

- **The interims on 10 Feb (3 days) are the key swing factor.** Strong results with NIC/NLW management commentary could materially change the FV estimate upward. Path B (conditional entry at 850-900p post-results) may become the operative path.

### Debilidades del analisis recibido

- **Factual error in thesis (insider selling):** The buy-pipeline adversarial process caught it (validating the system design), but this should not have reached Round 4. The fundamental-analyst should have searched for insider transactions as a mandatory step.

- **OEY calculation inconsistency:** Thesis used raw FCF / Market Cap; valuation-specialist correctly used (FCF - Maintenance Capex) / Market Cap per the skill. This discrepancy reveals a standardization gap in the valuation-methods skill that needs explicit enforcement.

- **Backward-looking FCF for forward-looking valuation:** Thesis used FY25 actual FCF for a company facing known forward cost headwinds. When material structural changes to earnings exist (NIC/NLW), forward estimates should be mandatory.

### Sugerencias de mejora

1. **Standardize OEY in valuation-methods skill:** Add: "OEY = (FCF - D&A x 1.1) / Market Cap. NEVER use raw FCF / Market Cap."
2. **Mandatory insider selling check in fundamental-analyst:** Add to PASO 0: "WebSearch '[company] insider selling [current year - 1]' before writing thesis."
3. **Forward vs backward requirement:** When known material cost changes exist, valuation MUST use forward estimates.
4. **DCF tool IFRS 16 flag:** For lease-heavy businesses, note distortion. Consider --ex-leases option.
5. **UK macro correlation auto-flag:** When evaluating 6th+ UK position, constraint_checker should flag correlated macro exposure as a data point.

### Preguntas para Orchestrator

1. Should we set 800p standing order NOW (pre-interims) in case stock gaps down on results? Risk: results disappoint, stock opens at 800p, bounces before we act. Counter-risk: results are good, stock goes up, order never fills (which is the correct outcome).
2. Thesis needs correction (insider error, NIC/NLW). Should this wait until after interims when we have more data?
3. Is 7 UK positions genuinely the limit? Should we formalize this constraint?

---

## AUDIT TRAIL

| Round | Agent | Output | Key Decision |
|-------|-------|--------|-------------|
| 1 (parallel) | fundamental-analyst | thesis.md | FV 1,328p, WATCHLIST 900p |
| 1 (parallel) | moat-assessor | moat_assessment.md | NARROW moat |
| 1 (parallel) | risk-identifier | risk_assessment.md | MEDIUM risk, 1C+3H |
| 1 (sequential) | valuation-specialist | valuation_report.md | FV 1,008p, MoS 7.1% |
| 2 | devil's-advocate | counter_analysis.md | STRONG COUNTER |
| 3 | orchestrator | Conflict resolution | Adopted 1,008p FV, 750-800p entry |
| 4 | investment-committee | committee_decision.md | WATCHLIST 750-800p |

---

**Committee Decision Date:** 2026-02-07
**Framework:** v4.0
**Gates Passed:** 8 PASS, 1 CONDITIONAL, 1 FAIL-at-current-price (PASS at 750-800p)
**Verdict:** WATCHLIST -- Entry 750-800p post-interims
**Next Review:** After 10 February 2026 interim results
