# INVESTMENT COMMITTEE -- R4 GATE REVIEW: IT (Gartner, Inc.)

## Date: 2026-02-14
## Verdict: WATCHLIST -- Entry $120-130 (conditional on Q1 2026 data)

---

## GATE 0: SECTOR VIEW EXISTS

- [x] Sector identified: Business Services / Information Services
- [x] Sector view found: `world/sectors/business-services.md` (updated 2026-02-13)
- [x] Sector view reviewed: Status NEUTRAL. IT flagged as "R1 COMPLETE, QS 80 adj (A), FV $245, Entry $145."
- **Sector view verified. Proceeding to Gate 1.**

---

## PASO 0.5: PRECEDENTES CONSULTADOS

### Most similar precedents:

**1. ROP (Roper Technologies) -- Tier B, Standing Order at $300, 4%, MoS 22%**
- Relevance: Both are US information services companies caught in SaaSpocalypse. Both have QS tool distortions (ROP by goodwill, IT by market position default). Both have WIDE moats. Both face per-seat pricing risk from AI. Both approved as standing orders, not immediate buys.
- ROP MoS accepted: 22% at $300 vs FV $385. Standing order, not immediate buy.
- ROP sizing: 4% (standard Tier B).
- ROP outcome: Standing order pending. Not yet triggered.
- Key difference: ROP has growing FCF ($2.47B). IT has DECLINING FCF ($1.4B -> $1.2B -> $1.135B guided). This is a material difference.

**2. ADBE (Adobe) -- Tier A, BUY at $270, 4.8%, MoS 31%**
- Relevance: Both are US information services / software companies. Both are Tier A (thesis claims). Both face AI narrative risk. Both bought during selloffs.
- ADBE MoS accepted: 31% at 52-week low.
- ADBE sizing: 4.8% (Tier A).
- ADBE outcome: Holding, FTC trial Oct 2026 is binary risk.
- Key difference: ADBE has stable FCF and growing Creative Cloud. IT has declining revenue and guided FCF decline. ADBE bear MoS was positive; IT bear MoS is NEGATIVE.

**3. MMC (Marsh McLennan) -- Tier B, Standing Order at $155, HALF POSITION (2%), MoS 18.4%**
- Relevance: Both are Tier B with WIDE moats in services sector. Both have binary event risk (MMC: Greensill trial; IT: AI disruption trajectory).
- MMC MoS accepted: 18.4% -- LOWEST ever for Tier B, justified by exceptional WIDE moat + half-position due to Greensill binary.
- Key difference: MMC has 85%+ recurring revenue growing steadily. IT has recurring revenue but growth is stalling/declining.

### Consistency assessment:

If I were to approve IT at $158 (current price):
- MoS vs base FV ($190 R3-resolved): 17% -- BELOW MMC's 18.4% floor, and IT has MORE risk (declining revenue, AI disruption, securities investigations).
- MoS vs bear ($143 valuation specialist, $165 thesis): -10% to +4% -- NEGATIVE or borderline. ALL prior Tier A/B buys had positive bear MoS.
- Sizing 4% at Tier B is consistent with ROP/VLTO/ACGL precedents.

**Deviation from precedents would be required to approve at current price. I cannot justify this deviation.**

---

## GATE 1: QUALITY SCORE -- CONDITIONAL PASS (Tier B, not Tier A)

### QS Tool Results (2026-02-14):

```
QS Tool (today): 64/100 -- Tier B
QS Tool (thesis date, 2026-02-13): 73/100 -- Tier B
```

**CRITICAL FINDING: The QS tool NOW reports 64, not 73.**

The drop from 73 to 64 is driven by:
- FY2025 data now incorporated by yfinance:
  - ROIC dropped: 52.1% (FY2024) -> 36.0% (FY2025) -- still excellent but trajectory reversed
  - EPS CAGR: 0/10 (NaN for FY2025 EPS, likely due to data gap) vs 10/10 previously
  - Revenue CAGR: 5.9% (5/10) vs 9.8% previously (would have been 5/10 either way)
  - GM Trend: now "Stable" (3/5) vs "Declining" (0/5) -- improvement
- Financial quality remains strong: 36/40

### Adjustment Assessment:

The thesis claimed +7 adjustment for market position (0 -> 7/8). This is valid:
- Gartner is undisputed #1 in IT research/advisory (6x larger than Forrester/IDC)
- Market position default of 0/8 is a known tool bias (flagged in decisions_log.yaml, Sessions 52, 66, 71)
- +7 is conservative (full points would be +8 for clear #1)

However, the EPS CAGR showing 0/10 is likely a data artifact (FY2025 EPS not yet fully loaded). The thesis used 20% EPS CAGR (10/10). Let me reason about the correct QS:

**Base tool today: 64**
- Market position correction: +7 (valid, documented)
- EPS CAGR data fix: The tool shows NaN for FY2025 EPS. Historical EPS CAGR of ~13-15% (factoring in the FY2025 earnings decline) would score 8/10 (>10%). That is roughly +8 vs the 0/10 the tool assigns. However, FY2025 EPS declined significantly (net income -42% YoY per risk assessment). The actual EPS trajectory 2022-2025 is: $10.08, $11.17, $16.12, ~$9.67 (FY2025). This 3-year CAGR is approximately -1.4% -- which would score 0/10. The tool is CORRECT if FY2025 EPS is this low.
- GM Trend now Stable (3/5): The tool updated to show FY2025 GM at 68.4% (vs 67.7% FY2024). This is an improvement but the 4-year trend 69.1% -> 67.8% -> 67.7% -> 68.4% is mixed, not clearly expanding. 3/5 is appropriate.

**Corrected QS: 64 + 7 (market position) = 71 -- Tier B**

The thesis claimed QS 80 (Tier A). The R3 resolution adjusted to QS 78. My independent assessment: **QS 71, Tier B.**

Reasons for disagreeing with the thesis's QS 80:
1. FY2025 ROIC dropped to 36% (still strong, but the accelerating trajectory 27->30->36->52 that justified the "compounder" narrative has REVERSED to 52->36)
2. FY2025 EPS declined materially -- the 20% EPS CAGR was backward-looking and masked by buybacks
3. Revenue is now guided to DECLINE in FY2026 -- this is not a compounder characteristic
4. FCF declined 13% FY2024->FY2025 and is guided lower in FY2026
5. The devil's advocate correctly noted that +7 from a single item is the largest single-item adjustment in system history

The devil's advocate recommended QS 77 (+4 adjustment). I am between the DA's 77 and my calculated 71. The difference is whether EPS CAGR should use the tool's current data (which may be incomplete) or a manual estimate. Given FY2025 net income decline of 42%, I lean toward the lower end.

**VERDICT: QS 71 (Tier B). NOT Tier A.**

This has material implications:
- Tier B MoS precedents: 18.4-22% (MMC to ROP range)
- Tier B sizing: 2-4% (4% standard, 2% for binary events)
- The thesis was built on Tier A assumptions. At Tier B, the entry discipline is stricter.

- [x] Quality Score calculated: 64 tool / 71 adjusted
- [x] Tier assigned: B
- [ ] Tier D -> N/A (not Tier D)
- [x] QS verified with tool + manual calculation

---

## GATE 2: BUSINESS UNDERSTANDING -- PASS

- [x] Business Analysis Framework completed (in thesis.md)
- [x] Can explain in 2 minutes:

Gartner is the #1 global research and advisory firm for IT decision-makers. It sells multi-year subscriptions ($25K-$250K/seat) to CIOs, CTOs, and enterprise technology leaders who need vendor-neutral guidance on technology purchasing decisions (cloud, AI, cybersecurity, ERP, etc.). The Magic Quadrant framework is the gold standard for vendor evaluation in enterprise IT procurement. 82% of revenue is recurring subscription research. The business is capital-light (3-4% capex/revenue), generates $1.2B FCF, and has ROIC of 36%.

- [x] Know WHY it is cheap + counter-thesis:

**Why cheap:** 70% decline from 52-week high driven by (1) SaaSpocalypse AI disruption fears -- market thinks AI will replace analyst advisory, (2) DOGE federal government contract losses, (3) Q4 2025 earnings miss + weak 2026 guidance showing revenue DECLINE for the first time in modern Gartner history. P/E compressed from 35-40x to 16x.

**Counter-thesis:** AI is a PARTIAL threat to the consulting segment (9% of revenue, already -12.8%) but NOT to core research (82% of revenue) because (a) proprietary data/benchmarks cannot be replicated by AI, (b) Magic Quadrant authority is institutional/political, not just informational, (c) analyst inquiry model requires human context. The 70% decline is disproportionate to the fundamental deterioration. Wallet retention remains 96-103% (clients are NOT leaving).

**My assessment of the counter-thesis:** PARTIALLY valid. The franchise is real but the counter-thesis understates three issues: (1) FCF is declining, not growing -- contradicts "compounder" narrative, (2) revenue guided to DECLINE in FY2026 -- unprecedented for Gartner, (3) AI disruption is showing in current financials (management admitted AI "led to slowing growth"), not just a future risk.

- [x] Value trap checklist: 0.5/10 (only MAYBE on AI disruption)
- [x] Informational advantage: Longer time horizon + market conflating consulting weakness with research weakness

---

## GATE 3: PROJECTION FUNDAMENTADA -- CONDITIONAL PASS

- [x] Revenue growth derived from TAM/share/pricing:
  - TAM growth: +7% (IT advisory, AI-driven demand)
  - Market share: +0% (maintaining #1)
  - Pricing: +2-3%
  - Government headwind (2026): -2%
  - **Net: 2% guided for 2026, recovering to 5-6% in 2027-2030**
  - **BUT: 2026 dollar guidance is DECLINE (-0.6%), not +2%**

- [x] WACC calculated:
  - Ke = 4.5% + 1.04 x 5.5% = 10.2%
  - Kd after-tax = 4.0% x (1-24.7%) = 3.0%
  - WACC = 8.5-9.0% (tool says 8.5%, thesis used 8.8%, valuation specialist used 9.0%)
  - **Note: tax rate discrepancy. Tool uses 24.7% effective FY2025 vs thesis's 9.6%. The 24.7% from the tool is based on more recent data and changes the Kd after-tax. WACC of 8.5% is reasonable.**

- [x] Terminal growth justified: 2.5% (at/below GDP, reasonable for information services with pricing power)

- [x] Scenarios documented:

| Scenario | Valuation Specialist | Thesis | Devil's Advocate |
|----------|---------------------|--------|------------------|
| Bear | $143 (25%) | $165 (25%) | $80-120 |
| Base | $205 (50%) | $245 (50%) | $160-185 |
| Bull | $310 (25%) | $375 (25%) | N/A |

**The three analyses diverge significantly on fair value.** The R3 resolution settled on $190, which is between the valuation specialist ($205) and the devil's advocate ($160-185). I will use $190 as the working FV.

---

## GATE 4: VALUATION MULTI-METHOD -- CONDITIONAL PASS

### Method 1: Owner Earnings Yield (35% weight per valuation specialist)

```
FCF FY2025: $1.2B (actual, NOT thesis's $1.4B trailing FY2024)
Depreciation: ~$140M
Maintenance Capex: $154M
Owner Earnings: $1.186B
Market Cap: $11.4B (at $158.58)
OEY: 10.4%

Fair OEY for Tier B with declining FCF: 7.5-8.0%
FV at 7.5% OEY: $218
FV at 8.0% OEY: $204
Midpoint: $211
```

### Method 2: DCF (45% weight)

```
Conservative range: $188-$275
At growth 3.5%, WACC 9%, terminal 2.5%: $295 (tool output)
At growth 0%, WACC 9%, terminal 2%: $235 (tool output)
At growth -2%, WACC 9.5%, terminal 1.5%: $188 (tool output)

Midpoint conservative: $205
Heavily conservative (weighting decline probability): $195
```

### Method 3: EV/EBIT (20% weight)

```
EBIT normalized: $1.16B
Fair multiple: 16.5x (37% discount to peer 26x median)
FV: $195
```

### Reconciliation

| Method | Fair Value | Weight | Weighted |
|--------|-----------|--------|----------|
| OEY (7.5-8%) | $211 | 35% | $73.85 |
| DCF (conservative) | $195 | 45% | $87.75 |
| EV/EBIT (16.5x) | $195 | 20% | $39.00 |
| **Weighted Average** | | 100% | **$201** |

**R3 Resolution FV: $190** (applied additional conservatism for CEO selling, securities investigations, declining GM trend -- the R3 resolved thesis explicitly haircut to $190)

**I adopt $190 as the committee FV.** This is consistent with the valuation specialist's work (which arrived at $205 before the R3 haircut) and the R3 resolution. The R3 specifically corrected: FCF $1.4B -> $1.2B, revenue DECLINING FY2026, AI disruption confirmed NOW, wallet retention below 100%, QS 80 -> 78 (which I further downgrade to 71).

**Divergence between methods: 8.2%** ($211 highest vs $195 lowest) -- well within 30% threshold.

- [x] Method 1 (OEY): FV $211
- [x] Method 2 (DCF conservative): FV $195
- [x] Method 3 (EV/EBIT): FV $195
- [x] Divergence: 8.2% (acceptable)

---

## GATE 5: MARGIN OF SAFETY -- FAIL at current price

```
Tier: B (QS 71)
Price: $158.58 (2026-02-14)
FV (R3 resolved): $190
MoS vs Base: 16.5% ($190)
MoS vs Bear (valuation specialist): -10.9% ($143)
MoS vs Bear (thesis): 3.9% ($165)
```

### Razonamiento:

**Precedent analysis:**
- MMC (Tier B, WIDE moat): MoS 18.4% -- LOWEST accepted for Tier B, but with half-position sizing and exceptional moat quality
- ROP (Tier B, WIDE moat): MoS 22% at standing order $300
- VLTO (Tier B, NARROW-leaning-WIDE): MoS 20% at standing order $80
- ACGL (Tier B, WIDE moat): MoS 20% at standing order $88
- HRB (Tier B, pre-adversarial): MoS 42% -- but failed adversarial review and was SOLD

**IT at $158 offers 16.5% MoS -- BELOW the MMC floor of 18.4%.**

MMC's 18.4% was accepted because: (a) exceptional WIDE moat 21/25, (b) half-position sizing for Greensill binary, (c) growing recurring revenue, (d) no AI disruption risk. IT has: (a) WIDE moat 15/25 (lower), (b) standard sizing (not half-position), (c) DECLINING revenue, (d) active AI disruption. IT's risk profile is WORSE than MMC's in every dimension that matters.

**Furthermore, the bear case MoS is NEGATIVE at current price.**

All prior Tier A/B buys in our system had POSITIVE bear MoS:
- ADBE: Bear MoS positive
- NVO: Bear MoS ~15%+
- ROP at $300: Bear was ~$270-280, MoS positive
- MMC at $155: Bear was ~$135, MoS positive (13%)

IT at $158 with bear $143: MoS = -10.9%. This is UNPRECEDENTED for approved positions.

**I am deviating from the thesis's recommendation of entry at $140-150.** Even at $140, MoS vs base is 26% (acceptable for Tier B) but MoS vs bear is only 2% (borderline). The risk/reward is unfavorable because:
1. Bear case has severe downside ($80-100 per risk assessment, 30% probability)
2. Revenue is DECLINING (unprecedented for Gartner, raises structural question)
3. AI disruption is manifesting NOW in financials (management confirmed)
4. Securities fraud investigations add governance tail risk

**Recommended entry: $120-130** (MoS 32-37% vs base, 8-16% vs bear)
- At $130: MoS 31.6% vs $190 base, 9.1% vs $143 bear -- consistent with ROP precedent
- At $120: MoS 36.8% vs $190 base, 16.1% vs $143 bear -- strong Tier B entry

**Precedent deviation documented:** I require LOWER entry price than the thesis ($140-150) or the R3 resolution ($130-135) because:
1. QS is lower than thesis assumed (71 vs 78-80) -- Tier B not Tier A
2. Bear case is more severe than thesis modeled ($143 vs $165)
3. Revenue DECLINE is a novel situation in our system -- we have never bought a company guiding for revenue decline
4. Consistency with Tier B MoS precedents (18-22%) ONLY applies if bear MoS is positive

---

## GATE 6: MACRO CONTEXT -- PASS

- [x] World view reviewed (date: 2026-02-14)
- [x] Cycle: Mid-cycle US, labor market resilient, inflation moderating (CPI Jan 2.4%)
- [x] Fit enterprise-cycle: NEUTRAL
  - Enterprise buying cycles lengthened (headwind for Gartner subscriptions)
  - AI spending increases demand for advisory (tailwind)
  - USD weakness benefits FX translation
  - DOGE federal contract losses are US-specific and should fade
- [x] Megatrends: AI [MIXED -- threat to consulting, opportunity for advisory demand]

The macro environment is NEUTRAL for Gartner. No macro-driven urgency to buy or avoid.

---

## GATE 7: PORTFOLIO FIT -- PASS (if price reaches entry zone)

```
Price: $158.58 (checked 2026-02-14)
Proposed sizing: 4% (~EUR 400) -- standard Tier B

Constraint checker results:
- Position post-purchase: 4.0% -- Consistent with Tier B precedents (ROP 4%, VLTO 4%, ACGL 4%)
- Sector post-purchase: Technology 12.1% -- Reasonable. ADBE is the only other Technology position
- Geography post-purchase: US 18.5% -- Low. US is underpresented vs portfolio
- Cash post-purchase: EUR 5,352 (53.0%) -- Ample liquidity
- 50% drawdown impact: -2.0% portfolio -- Acceptable for Tier B conviction
- Correlation with existing: MEDIUM (ADBE is technology/SaaS, but Gartner is information services -- different business model but same SaaSpocalypse narrative risk)
```

**SaaSpocalypse cluster risk assessment:**
- Current portfolio SaaSpocalypse exposure: ADBE (~5.5% of portfolio)
- Pipeline with SaaSpocalypse exposure: ROP (standing order), BYIT.L (held), and potentially IT, MORN, VEEV, INTU, PAYC
- Adding IT would bring SaaSpocalypse exposure to ~9.5% (ADBE + IT). This is manageable for 2 positions but I flag that pipeline candidates (ROP, MORN, VEEV, INTU, PAYC) could push total exposure much higher if all are added.
- **Recommendation: Cap total SaaSpocalypse/per-seat narrative exposure at 15-20% of portfolio to avoid concentrated narrative bet.**

Precedent sizing: ROP at 4% (Tier B, WIDE moat, standing order) is the closest precedent.
Deviation: None. 4% at Tier B is consistent.

---

## GATE 8: SECTOR UNDERSTANDING -- PASS

- [x] Sector view exists: `world/sectors/business-services.md`
- [x] Sector view reviewed (date: 2026-02-13)
- [x] TAM and trends understood: IT advisory/research TAM $200-250B, growing 7-10%, driven by AI adoption + digital transformation
- [x] Disruption risks known: AI substitution of basic research, per-seat pricing erosion, SaaSpocalypse narrative
- [x] Sector position: NEUTRAL (quality subsectors preferred over value traps)
- [x] Gartner identified in sector view as R1 COMPLETE, high-priority candidate

**Sector context supports the thesis that information services selloff is partly indiscriminate.** VRSK (insurance data monopoly, harder moat) is also down 45%. WKL.AS down 66%. The sector-wide repricing suggests macro/narrative factors beyond company-specific fundamentals. However, Gartner's fundamentals ARE deteriorating more than VRSK's (revenue decline, FCF decline, AI disruption showing in financials).

---

## GATE 9: AUTOCRITICA -- PASS

### Assumptions not validated:
1. **Revenue recovery to 5-6% by 2027 is unproven.** Management promised "acceleration through 2026" but provided no quantitative targets. The Q1 2026 results (May 2026) are the critical test.
2. **AI disruption timeline of 5-10 years for core research may be optimistic.** Management already admitted AI is slowing growth NOW. The S-curve of disruption may be faster than modeled.
3. **FCF trajectory: Is $1.2B the new normal or a trough?** The thesis treats 2025-2026 as a trough, but FCF could continue declining if AI substitution accelerates.
4. **ROIC of 36% FY2025 is still exceptional but the DIRECTION reversed.** The accelerating ROIC narrative (27->52%) was a key bull thesis. At 52->36%, the story changes from "operating leverage" to "earnings pressure."

### Biases recognized:
- [x] **Popularity bias:** Gartner is a well-known company. The 70% selloff makes it psychologically attractive ("if it was worth $519 before, $158 must be cheap"). This is a classic anchor bias. The $519 price was likely a bubble (35-40x P/E for a mid-single-digit grower).
- [x] **Confirmation bias:** The franchise quality (ROIC, Magic Quadrant brand, market position) is genuinely impressive. This can lead to overfitting the "quality compounder" narrative to a company that is currently experiencing fundamental deterioration.
- [x] **Recency bias:** The selloff is dramatic (70%) and recent. This creates urgency ("must buy before it bounces"). But the Q1 2026 data is available in May -- patience costs nothing when cash is 57%.

### Kill conditions defined:
1. **KC#1: Wallet retention drops below 95%** for 2 consecutive quarters -- clients are churning, not just pausing
2. **KC#2: ROIC falls below WACC** for 2 consecutive quarters -- structural deterioration
3. **KC#3: Research segment revenue decline >5%** for 2 consecutive quarters -- AI displacement of core
4. **KC#4: CEO Gene Hall exits** without board-approved successor plan
5. **KC#5: AI-native competitor captures >10%** enterprise advisory market share
6. **KC#6: Per-seat pricing erosion >10%** from AI-driven headcount reduction at client firms
7. **KC#7: SEC formal investigation** (escalation beyond ambulance-chaser law firms)
8. **KC#8: FY2026 revenue below $6.3B** (decline exceeds -3%, structural not cyclical)

### What would make me change my mind:
- Q1 2026 CV growth accelerating to 4%+ ex-federal: Would confirm management's "acceleration" narrative and reduce bear case probability from 25-30% to 15%
- Insider buying at current levels (CEO or board members): Would signal informed confidence
- Wallet retention returning above 100% on GTS: Would disprove the AI erosion narrative
- AI product launches driving measurable new client wins: Would confirm AI as tailwind not headwind

---

## GATE 10: COUNTER-ANALYSIS & INDEPENDENT ASSESSMENTS

### Counter-analysis (devils_advocate.md):
- [x] Exists: YES
- [x] Verdict: **STRONG COUNTER (14/19)**
- [x] Challenges HIGH/CRITICAL: 8 of 18 (1 CRITICAL, 7 HIGH)

**For EACH HIGH/CRITICAL challenge:**

| # | Challenge | Thesis addresses? | Resolution |
|---|-----------|------------------|------------|
| 1 | AI disruption happening NOW | PARTIALLY -- thesis acknowledges for consulting but understates impact on core research growth | UNRESOLVED -- management confirmed AI slowing growth. Monitoring KC#3 and KC#1 |
| 2 | Consulting decline canary for research | NO -- thesis treats consulting as isolated | UNRESOLVED -- second-order pipeline effect not modeled. Risk documented. |
| 3 | OEY uses stale FCF ($1.4B vs $1.2B) | R3 CORRECTED -- R3 resolution uses $1.2B | RESOLVED by R3 |
| 4 | DCF assumes 5% growth; reality is DECLINE Y1 | R3 PARTIALLY CORRECTED -- R3 used $190 FV reflecting slower growth | PARTIALLY RESOLVED -- valuation specialist modeled decline but thesis still uses optimistic recovery |
| 5 | Bear case too generous | R3 PARTIALLY CORRECTED -- valuation specialist bear $143 vs thesis $165 | PARTIALLY RESOLVED -- I use $143 as bear, not $165 |
| 6 | Revenue DECLINE guided for 2026 | ACKNOWLEDGED in thesis | DOCUMENTED but unresolved -- unprecedented in our system |
| 7 | EPS engineering via buybacks | ACKNOWLEDGED but minimized | PARTIALLY RESOLVED -- documented as risk, monitoring KC#7 |
| 8 | Wallet retention below 100% | ACKNOWLEDGED | DOCUMENTED -- monitoring KC#1 |

**CRITICAL challenge resolution:**
- Challenge #1 (AI disruption happening NOW, rated CRITICAL): The thesis argues AI is partial and 5-10 year. The evidence shows it is affecting current growth. R3 adjusted FV from $245 to $190 partly for this reason. But the CRITICAL risk remains: if AI disruption accelerates beyond what the $190 FV models, the stock could reach $80-100 (risk assessment bear case). **I cannot fully resolve this before Q1 2026 data (May 2026).** This is the primary reason for WATCHLIST rather than BUY.

**Unresolved conflicts:** 4 of 8 HIGH/CRITICAL challenges remain partially or fully unresolved. Per the committee protocol: "If counter-analysis is STRONG COUNTER with desafios CRITICAL no resueltos, NO APROBAR hasta resolucion."

### Moat assessment (moat_assessment.md):
- [x] Exists: YES
- [x] Moat classification: WIDE (15/25) -- lower end
- [x] Coincides with thesis? YES -- thesis uses WIDE, moat assessment agrees but flags AI vulnerability
- [x] Key concern: 84% client retention vs VRSK's 92%. Wallet retention dropped below 100% on GTS. "Soft" switching costs (behavioral/cultural) vs VRSK's "hard" switching costs (regulatory/technical).

### Risk assessment (risk_assessment.md):
- [x] Exists: YES
- [x] Risk score: MEDIUM-HIGH (1 CRITICAL, 4 HIGH)
- [x] Risks NOT in thesis: EPS engineering via buybacks, securities fraud investigations, CEO selling pattern -- all added during R1
- [x] Kill conditions suggested: 6 kill conditions from risk assessment -- all incorporated into thesis
- [x] Risk assessment probability-weighted FV: $170-195 (below thesis's $245, consistent with R3 resolution of $190)

### Valuation report (valuation_report.md):
- [x] Exists: YES
- [x] FV divergence vs thesis: Valuation specialist $205 vs thesis $245 -- 16.3% divergence -- INVESTIGATED
  - Key driver: Valuation specialist uses FY2025 FCF ($1.2B) not FY2024 ($1.4B). This is correct.
  - R3 resolved at $190 (between DA's $160-185 and specialist's $205)
- [x] Sensitivity: HIGH -- TV 74.5% of EV, FV spread 82%. The DCF is unreliable as point estimate.
- [x] Bear case MoS: **NEGATIVE (-7.5% per valuation specialist, -10.9% at today's price)**

---

## FINAL VERDICT

### 10 GATES SUMMARY:

| Gate | Status | Key Issue |
|------|--------|-----------|
| 0. Sector View | PASS | business-services.md exists, updated 2026-02-13 |
| 1. Quality Score | CONDITIONAL PASS | QS 64 tool / 71 adjusted = Tier B (NOT Tier A as thesis claims) |
| 2. Business Understanding | PASS | Business model well understood, counter-thesis documented |
| 3. Projections | CONDITIONAL PASS | Revenue decline unprecedented; recovery projection unverified |
| 4. Valuation | CONDITIONAL PASS | FV $190 (R3 resolved), methods converge within 8% |
| 5. Margin of Safety | **FAIL at $158** | MoS 16.5% below MMC floor of 18.4%; bear MoS NEGATIVE |
| 6. Macro Context | PASS | Neutral environment, no urgency |
| 7. Portfolio Fit | PASS | 4% sizing, Technology 12.1%, US 18.5%, ample cash |
| 8. Sector | PASS | Sector view comprehensive, information services selloff context understood |
| 9. Autocritica | PASS | Assumptions, biases, kill conditions documented |
| 10. Counter-Analysis | **CONDITIONAL** | STRONG COUNTER 14/19; 4 of 8 HIGH/CRITICAL partially unresolved; CRITICAL AI risk cannot be resolved before Q1 data |

### VERDICT: WATCHLIST

```
WATCHLIST: IT (Gartner, Inc.)
Quality Score: 64 tool / 71 adjusted -- Tier B (NOT Tier A)
Current Price: $158.58
Fair Value: $190 (R3 resolved)
MoS at current: 16.5% (INSUFFICIENT for Tier B with this risk profile)

Entry Price Target: $120-130
  At $130: MoS 31.6% vs $190 base, 9.1% vs $143 bear
  At $120: MoS 36.8% vs $190 base, 16.1% vs $143 bear

Condition for Entry:
  PRICE: $120-130 range
  OR: Q1 2026 results (May 2026) show CV growth accelerating to 4%+ ex-federal
       + wallet retention returning above 100% on GTS
       + FCF guidance above $1.2B for FY2026
       (In which case, entry at $140-150 could be reconsidered with updated FV)

Sizing: 4% (~EUR 400) standard Tier B
ADD trigger: $110 (MoS 42% vs base, 23% vs bear -- exceptional entry)
```

### WHY NOT BUY AT CURRENT PRICE ($158):

1. **MoS 16.5% is below every Tier B BUY precedent in our system.** MMC at 18.4% was the floor, and MMC has a stronger moat, growing revenue, and no AI disruption risk.
2. **Bear case MoS is NEGATIVE (-10.9%).** Every prior BUY in our system had positive bear MoS. This would set a dangerous precedent.
3. **Revenue DECLINE is unprecedented** for a Gartner investment in our system. We have never bought a company guiding for revenue decline. This uncertainty warrants waiting for Q1 2026 evidence.
4. **STRONG COUNTER (14/19) with CRITICAL unresolved.** The committee protocol says "NO APROBAR hasta resolucion" for STRONG COUNTER with CRITICAL unresolved.
5. **Cash is 57%.** There is no urgency. Waiting for Q1 data (May 2026) costs nothing. If Gartner proves the recovery narrative, the stock will likely still be attractive at $140-150.
6. **QS is Tier B (71), not Tier A (80) as thesis claimed.** The entire thesis was built on Tier A assumptions. At Tier B, the entry discipline is stricter and the FV may need further revision.

### WHY NOT REJECT:

1. **The franchise is REAL.** #1 by 6x, ROIC 36% (still exceptional), WIDE moat 15/25, 82% recurring revenue, $1.2B FCF.
2. **The selloff IS disproportionate.** P/E 16.4x for a business with ROIC 36%, 68.4% gross margins, and $5.2B contract value. Even at reduced growth, this franchise generates real economic value.
3. **Multiple catalysts exist** -- CV growth re-acceleration, DOGE headwind rolling off, AI product launches, buybacks at depressed prices (8%/yr share count reduction).
4. **The sector-wide repricing creates opportunity.** The SaaSpocalypse has compressed multiples across all information services companies. When sentiment normalizes, the re-rating potential is significant.
5. **At $120-130, the risk/reward becomes asymmetric in our favor.** Bear case downside would be 8-16% vs upside of 46-58%.

### ACTIONS REQUIRED:

1. **DO NOT set standing order at $145 (thesis recommendation).** The MoS is insufficient for Tier B with NEGATIVE bear MoS.
2. **Set price alert at $130** -- if reached, re-evaluate for standing order placement
3. **Update quality universe entry price** from $200 (stale) to $130 (committee-adjusted)
4. **Monitor Q1 2026 results** (May 2026) -- if CV growth accelerates to 4%+ ex-federal and wallet retention returns above 100%, reconsider entry at $140-150 with updated thesis
5. **Update sector view** to reflect committee QS of 71 (not 80) and entry $120-130 (not $140-150)
6. **SaaSpocalypse cluster tracking**: Document that IT would be the 2nd per-seat narrative position (after ADBE) if purchased. Flag if total exposure approaches 15%.

---

## META-REFLECTION

### Dudas sobre esta decision

1. **Am I being too conservative?** The R3 resolution settled on $190 FV and entry $130-135. My entry of $120-130 is $5-15 below the R3. The difference is driven by my QS assessment (71 vs 78) and the Tier B reclassification. If the R3 QS of 78 is correct, my entry zone is too strict and we risk missing the opportunity.

2. **The ROIC trajectory reversal (52% -> 36%) may be more alarming than the raw number suggests.** A ROIC of 36% is still excellent (spread +27.4pp over WACC). But the DIRECTION matters for a "compounder" classification. If ROIC is declining, the compounding engine is weakening. This could be temporary (FY2025 was a tough year) or structural (AI eroding pricing power).

3. **Am I anchoring too much on the devil's advocate?** The DA scored 14/19 (STRONG COUNTER), which is the highest counter in our recent pipeline (vs 11/19 for VLTO, 13/19 for MMC, etc.). But the DA's $160-185 FV range was built on the most pessimistic interpretation of every data point. The truth is likely between the DA and the thesis.

4. **Revenue decline guidance could be sandbagging.** Management has a pattern of setting conservative guidance (they cut guidance twice in 2025 and then roughly met it). If Q1 2026 shows even modest positive growth, the stock could rerate quickly. Waiting for Q1 may mean buying 20-30% higher.

### Debilidades del analisis recibido

1. **FCF figure inconsistency across documents.** The thesis uses $1.4B (FY2024). The DA and valuation specialist correctly use $1.2B (FY2025). The R3 resolution notes $1.2B. But the thesis file still shows $1.4B in the headline OEY calculation. This should have been corrected in the thesis during R3.

2. **QS assessment was the biggest disagreement.** Thesis: 80 (Tier A). DA: 77 (Tier B). My assessment: 71 (Tier B). The 9-point spread between thesis and my assessment is material and drives the entire entry price difference. The root cause is the QS tool update (73->64) incorporating FY2025 data that the thesis did not have.

3. **The R3 resolution note says "QS 80->78 adj" but the tool now shows 64.** The R3 was based on the 73 tool score. Now that FY2025 data is incorporated, the base has shifted to 64. This invalidates the R3's QS assessment and should trigger a thesis update.

4. **The risk assessment's probability-weighted bear case ($80-100 at 30% probability) was not adequately incorporated into the thesis.** The thesis used $165 bear (25% prob). The valuation specialist used $143 bear (25% prob). The risk assessment's more severe bear should have been weighted in the scenarios.

5. **Insider buying/selling was incompletely analyzed.** The thesis mentions CEO sold $17M at $507, but the risk assessment notes Pagliuca bought $7.8M at $229 (Dec 2025). These are different signals that partially offset. A more nuanced insider analysis would help.

### Sugerencias de mejora

1. **QS tool should auto-flag when FY data updates change the score by >5 points.** The drop from 73 to 64 was only discovered because I re-ran the tool today. If the R3 resolution had been based on 64 (not 73), the FV and entry price would have been different.

2. **Standardize FCF base for valuation.** Thesis used trailing (FY2024), specialist used forward (FY2025). For companies guiding FCF decline, forward FCF should be mandatory. This should be a protocol in the valuation-methods skill.

3. **Bear case MoS should be a STANDARD metric in the committee template.** All prior buys had positive bear MoS. Making this explicit would have flagged IT earlier.

4. **SaaSpocalypse cluster tracker needed.** With ADBE, BYIT.L (held), ROP (standing order), and IT/MORN/VEEV/INTU/PAYC in pipeline, we are building concentrated exposure to a single narrative. A formal cluster risk limit should be established.

### Preguntas para Orchestrator

1. **QS tool now shows 64, not 73. Does this require a thesis rewrite before the committee decision can be considered final?** The thesis, R3 resolution, and all three independent assessments used 73 as the base. The base has shifted materially.

2. **Should we set an explicit SaaSpocalypse cluster exposure limit?** If all pipeline candidates are approved, we could have 6-8 positions (30-40% of portfolio) exposed to the same AI/per-seat disruption narrative.

3. **The thesis verdict was already WATCHLIST at $145 entry. My committee verdict is WATCHLIST at $120-130 entry. Should we update the thesis file to reflect the committee's lower entry, or keep the thesis as-is and document the committee override in the committee_decision.md file?**

4. **Q1 2026 earnings hard gate: Should we block any standing order for IT until after May 2026 Q1 results, similar to how RSG/CDNS have hard gates for Feb 17 earnings?**
