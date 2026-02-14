# INVESTMENT COMMITTEE - RONDA 4 GATE REVIEW: ZTS (Zoetis Inc.)

## Date: 2026-02-14
## Committee Session: R4 Final Gate Review

---

## GATE 0: SECTOR VIEW EXISTS -- PASS

Sector view verified: `world/sectors/pharma-healthcare.md`
- Last updated: 2026-02-12
- Subsector: Animal Health (added 2026-02-12 during ZTS R1)
- Status: NEUTRAL-POSITIVO for animal health subsector

---

## PASO 0.5: PRECEDENTES CONSULTADOS

### Most Similar Precedents

**1. NVO (Tier A, BUY at MoS 38%, sizing 3.4%)**
- Similarity: Both are pharma-healthcare sector, Tier A quality compounders at depressed valuations
- NVO: QS 82, MoS 38%, sizing 3.4%. Guidance shock (-17% in 2 days) created entry.
- Outcome: Position still active, HOLD.
- Relevance: ZTS has similar quality profile (ROIC >>WACC, dominant market position) but MUCH lower MoS (10-14% vs 38%). NVO was bought at 2x+ the MoS we see here.

**2. ADBE (Tier A, BUY at MoS 31%, sizing 4.8%)**
- Similarity: Both Tier A quality compounders at 52-week lows with temporary headwinds
- ADBE: QS 76, MoS 31%, sizing 4.8%. At 52w low.
- Outcome: Position still active, HOLD.
- Relevance: ADBE had 31% MoS -- still 2-3x what ZTS offers at current price.

**3. ROP (Tier B, STANDING ORDER at MoS 22%, sizing 4%)**
- Similarity: Tier B company where current price didn't offer enough MoS, so standing order was placed at lower price
- ROP: QS 70 adjusted, FV $385, entry $300 (22% MoS). Standing order.
- Outcome: Pending execution at $300.
- Relevance: This is the most relevant precedent for ZTS's situation -- a quality company where current price is insufficient but a standing order at a lower price makes sense. ROP was set at 22% MoS for Tier B.

**If I deviate from these precedents:** I must explain why accepting lower MoS or different sizing would be justified. Given all three precedents show 22-38% MoS for approval, accepting 10-14% MoS at ZTS's current price would be INCONSISTENT.

---

## GATE 1: QUALITY SCORE -- PASS (Tier B, QS 73)

### QS Tool Output: 78/100 (Tier A)

The quality_scorer.py now returns 78/100 with updated 2025 data:
- Financial: 38/40 (ROIC spread +17.4pp, FCF margin 24.1%, ND/EBITDA 1.7x, FCF 4/4)
- Growth: 18/25 (Revenue CAGR 5.4%, EPS CAGR 10.2%, GM expanding)
- Moat: 17/25 (GM +16.8pp vs sector, market position 0/8 manual, ROIC persistence 7/7)
- Capital Allocation: 5/10 (dividend yield 1.7%, insider 0.2%)

### QS Discrepancy Resolution

There are THREE different QS numbers floating around:
1. **quality_scorer.py (today):** 78/100 (Tier A) -- NEW data shows ROIC 26.1% (2025 TTM), EPS CAGR 10.2%, GM expanding to 71.8%
2. **Thesis (R3 resolved):** 73 tool / 78 adjusted (adjustment +5 for market position)
3. **Moat assessment:** 73 tool / 81 adjusted (adjustment +8 for market position)

The tool now returns 78 WITHOUT any manual adjustment, because:
- EPS CAGR improved to 10.2% (was 8.4% in earlier run) = +3 points in Growth
- GM trend now "Expanding" (was "Stable") = +2 points in Growth
- These real data improvements account for the difference from the earlier 73 reading

**Market Position adjustment:** The tool still gives 0/8 for market position (manual field). ZTS is undisputed global #1 with 17% market share. Per QS Tool-First protocol and Session 61 precedent, a +5 adjustment is conservative and documented. This would bring QS to 83.

**However, the Devil's Advocate raises valid forward-looking concerns:**
- Growth deceleration: 2026 guidance 3-5% (vs 6% achieved in 2025)
- Librela franchise under active siege (-32% US Q4, peer-reviewed 9x adverse events)
- Apoquel patent expires November 2026

**My Resolution:**

I accept the tool's 78/100 as the base score. The market position adjustment (+5) is valid and documented, bringing to 83. However, I apply a forward-looking deduction:
- Growth deceleration from 6% to 3-5% guided: -2 (growth quality will decline in next tool run)
- Librela franchise impairment (6% of revenue, accelerating decline): -1 (moat under local siege, though not system-wide)

**COMMITTEE QS: 78 (tool) + 5 (market position) - 3 (forward deductions) = 80/100**
**TIER: A (Quality Compounder) -- low end**

This is HIGHER than the thesis's 73/78 because the tool itself now returns 78 with 2025 data (EPS CAGR improved, GM expanding). The forward deductions acknowledge the DA's valid concerns but don't overcorrect -- the Librela franchise is 6% of revenue, and the growth deceleration may be conservative guidance (historical pattern).

**IMPORTANT NOTE:** Even at QS 73 (thesis's tool score), ZTS is Tier B. The MoS analysis below considers BOTH scenarios.

```
[X] Quality Score calculated: 78 (tool) / 80 (adjusted)
[X] Tier assigned: A (low-end, borderline A/B)
[ ] If Tier D -> STOP: N/A, not Tier D
[X] QS verified with tool
```

---

## GATE 2: BUSINESS UNDERSTANDING -- PASS

```
[X] Business Analysis Framework completed
[X] Can explain in 2 minutes
[X] Know WHY it's cheap + counter-thesis
[X] Value trap checklist: 0/10 SI
[X] Informational advantage identified
```

**2-minute explanation:**

Zoetis is the world's largest animal health company ($9.5B revenue, 17% global market share), spun off from Pfizer in 2013. It sells pharmaceuticals, vaccines, and diagnostics for companion animals (68% of revenue) and livestock (31%). The business generates 70%+ gross margins and 26-30% ROIC because: (1) regulatory barriers to entry are extreme (FDA/USDA approvals take years), (2) veterinary biologics have NO established biosimilar pathway, (3) switching costs are high (vet relationships, diagnostic platform lock-in), and (4) scale advantage is massive (45 manufacturing sites, 100+ countries, largest dedicated sales force).

The stock is cheap (-29% from 52-week high) because of: Librela safety concerns (FDA adverse event warnings, -32% US Q4 decline), 2026 growth guidance deceleration (3-5% vs 6% achieved), vet visit secular decline, and sector de-rating.

My counter-thesis: Librela is 6% of revenue and the decline is product-specific, not a platform failure. Diagnostics (+13% growth) is the new growth engine with razor/blade economics. Pet humanization is secular. 30% ROIC with 17pp+ WACC spread doesn't stay at 21x P/E forever.

**Value trap score: 0/10.** No secular decline, no tech disruption (ZTS IS the innovator), no balance sheet issues, no ROIC < WACC, no FCF problems. This is NOT a value trap.

**Informational advantage:** Longer time horizon than market. Market is pricing in 2026 guidance as permanent; I see a 5-10 year compounder with secular TAM growth.

---

## GATE 3: PROJECTIONS -- PASS (with adjustments per DA)

```
[X] Revenue growth derived (TAM/share/pricing): 5-7% organic (adjusted from thesis 7-8%)
[X] WACC calculated: 8.5-8.7% (tool: 8.7%, thesis derivation: 8.5%)
[X] Terminal growth justified: 2.5% (below GDP, conservative for growing TAM)
[X] Scenarios Bear/Base/Bull documented
```

### Revenue Growth Derivation

Following DA's challenge, I adjust growth assumptions:
- **Year 1 (2026):** 3-5% (management guidance -- NOT above guidance per critical thinking skill)
- **Years 2-3:** 4-6% (recovery from Librela trough, diagnostics acceleration, Lenivia launch)
- **Years 4-5:** 6-7% (TAM growth + modest share gains + pricing power)

This is MORE CONSERVATIVE than the thesis (which projected 5-6% Y1-2, 7-8% Y3-5) and CLOSER to the DA's correction (3-5% Y1, 4-6% Y2-3, 6-7% Y4-5).

### WACC

- Tool: 8.7% (Ke=9.8%, Kd=2.4%, beta=0.96, tax=20.4%)
- Thesis derivation: 8.5%
- I use 8.7% (tool value) for conservatism

### Terminal Growth: 2.5%

Justified because animal health TAM growing 6-10% long-term, pet humanization is secular, and 2.5% is well below GDP growth. Conservative for this industry.

---

## GATE 4: VALUATION -- PASS (with corrected FV)

```
[X] Method appropriate for Tier A/B: Owner Earnings Yield + Reverse DCF / EV/EBIT
[X] Method 1: OEY -> FV ~$135
[X] Method 2: EV/EBIT (2026E forward) -> FV ~$127
[X] Divergence resolved
```

### Valuation Reconciliation -- COMMITTEE CORRECTED

The thesis used 4 methods and then added an 18% "quality compounder premium" to arrive at $140. The DA correctly challenged this as double-counting. I agree with the DA on this point.

**My valuation:**

| Method | Fair Value | Weight | Weighted |
|--------|-----------|--------|----------|
| DCF Base (conservative) | $88 | 15% | $13.20 |
| OEY Midpoint | $135 | 35% | $47.25 |
| EV/EBIT (2026E, 16.5x) | $127 | 30% | $38.10 |
| Reverse DCF (sanity check) | $126 | 20% | $25.20 |
| **Weighted Average** | | **100%** | **$124** |

**CRITICAL CORRECTION vs thesis:** I do NOT add a "quality compounder premium" on top. The OEY method (35% weight) already captures the compounding value. Adding a premium double-counts it.

**Committee Fair Value: $120**

I apply a -$4 haircut to the $124 weighted average to account for:
1. Librela franchise declining faster than thesis assumed (-$2)
2. Apoquel generic entry approaching November 2026 (-$2)

This $120 FV is:
- Below thesis FV of $140 (-14%)
- Below DA's suggested $115-125 range (at the high end)
- Below risk assessment's EV-weighted $127-135
- Above DCF's mechanical $88 (which penalizes compounders)

**Why $120 and not the DA's $115?** The DA's $115 assumes the bear case on growth (3-5% permanent), the worst case on Librela (continued decline), and no credit for diagnostics acceleration. I give some credit to the diversified franchise (Simparica Trio growing, diagnostics +13%, livestock +8% international), which the DA discounts too heavily. But I accept most of the DA's corrections on the quality premium and growth assumptions.

---

## GATE 5: MARGIN OF SAFETY -- CONDITIONAL PASS (insufficient at current price)

```
[X] Tier: A (low-end) / possibly B
[X] MoS Actual vs Base ($120): -5% (OVERVALUED at $126)
[X] MoS Actual vs Bear ($95): -25% (significant downside)
```

### MoS Assessment at Current Price ($126)

At current price $125.64:
- MoS vs Committee FV $120: **-4.7%** (slightly overvalued)
- MoS vs Expected Value ($124 weighted): **-1.3%** (essentially fair value)
- MoS vs Bear ($95): **-24.4%** (material downside in bear case)

**This is INSUFFICIENT for any tier.**

### MoS at Standing Order Entry Prices

| Entry Price | MoS vs $120 FV | MoS vs Bear $95 | Assessment |
|-------------|----------------|-----------------|------------|
| $115 | 4.2% | -17.4% | Insufficient for any tier |
| $110 | 8.3% | -13.7% | Insufficient for Tier A/B |
| $105 | 12.5% | -9.5% | Marginal for Tier A with exceptional moat |
| $100 | 16.7% | -5.0% | Marginal for Tier B |
| $95 | 20.8% | 0% | Adequate for Tier B (consistent with ROP 22%, ACGL 20%) |

### Precedent Comparison

| Ticker | Tier | MoS at Entry | Context |
|--------|------|-------------|---------|
| NVO | A | 38% | Guidance shock, deep discount |
| ADBE | A | 31% | 52-week low |
| MONY.L | A | 36% | 52-week low |
| LULU | A | 34% | -58% fallen angel |
| AUTO.L | A | 29% | -47% fallen angel |
| BYIT.L | A | 35% | -47% fallen angel |
| ROP | B | 22% | Standing order (wide moat) |
| ACGL | B | 20% | Standing order (wide moat, net cash) |
| MMC | B | 18.4% | Standing order (HALF position, exceptional moat) |

**LOWEST Tier A MoS accepted:** AUTO.L at 29%
**LOWEST Tier B MoS accepted:** MMC at 18.4% (HALF position due to Greensill binary)

ZTS at current $126 offers -5% MoS. Even the thesis's own entry target of $110-115 offers only 4-8% MoS against the committee's corrected FV of $120. This is FAR below any precedent.

To reach adequate MoS:
- **For Tier B treatment (QS 73-78):** Need $95-100 (20-25% MoS). Consistent with ROP ($300 = 22%), ACGL ($88 = 20%).
- **For Tier A treatment (QS 80):** Need $84-90 (25-30% MoS). Consistent with Tier A precedents (29-38%).

### Resolution

**The thesis's entry target of $110-115 is TOO GENEROUS given the corrected FV of $120.** At $110, MoS is only 8.3% -- well below ALL precedents for both Tier A and Tier B.

**Standing order entry: $95** (20.8% MoS vs $120 FV). This is consistent with Tier B precedents (ROP 22%, ACGL 20%) and acknowledges that the company faces real near-term headwinds (Librela, generics, vet visit decline).

---

## GATE 6: MACRO CONTEXT -- PASS

```
[X] World view reviewed (date: 2026-02-14)
[X] Economic cycle: Mid-cycle US
[X] Company-cycle fit evaluated
[X] Megatrends: Pet humanization [+], AI [neutral], Demographics aging [+]
```

ZTS fits the current macro well:
- Defensive business in uncertain environment (healthcare, non-discretionary)
- Pet humanization is secular megatrend (aligns with demographics)
- USD weakness (DXY ~96.8) is FAVORABLE for ZTS's 50% international revenue
- Healthcare sector broadly out of favor = contrarian opportunity at right price
- Mid-cycle economy: animal health is not cyclically sensitive

No macro-related concerns that would block approval.

---

## GATE 7: PORTFOLIO FIT -- PASS

```
[X] Price verified: $125.64 (2026-02-14)
[X] Sizing proposed: 4% (EUR 400) at standing order price $95
```

Constraint checker output (simulated at $400):
- Position post-purchase: 4.0% -- Consistent with Tier B sizing precedents (ROP 4%, ACGL 4%, VLTO 4%)
- Sector post-purchase (Healthcare): 7.4% -- Moderate. NVO is also in healthcare. Combined ~7% healthcare is prudent, not concentrated.
- Geography post-purchase (US): 18.5% -- Low. Room for more US exposure.
- Cash post-purchase: 53.0% -- High cash level. Deployment is welcome.
- If ZTS falls 50%: -2.0% portfolio impact -- Acceptable for this conviction level.

### Sector Overlap with NVO

NVO and ZTS are both in pharma-healthcare but in DIFFERENT subsectors:
- NVO: GLP-1/obesity, human pharma
- ZTS: Animal health (companion + livestock)

Correlation between the two is LOW. They respond to different demand drivers (human obesity treatment vs. pet healthcare), different regulatory pathways (human FDA vs. veterinary FDA), different competitive dynamics. A Librela crisis doesn't affect NVO and vice versa. The only correlation is broad healthcare sentiment.

**Combined healthcare exposure at 7.4%:** Very reasonable. Below typical sector concentration patterns (20-25% historical).

**No UK geographic concern:** ZTS is US-based with global operations. No addition to our UK concentration.

### Precedent Sizing

ROP, VLTO, ACGL all approved at 4% for Tier B. ZTS at 4% is CONSISTENT.

---

## GATE 8: SECTOR UNDERSTANDING -- PASS

```
[X] Sector view exists: world/sectors/pharma-healthcare.md
[X] Sector view reviewed (date: 2026-02-12)
[X] TAM and trends understood
[X] Disruption risks known
[X] Sectoral position: NEUTRAL-POSITIVO (animal health subsector)
```

The animal health subsector was added to the pharma-healthcare sector view on 2026-02-12 during ZTS R1. Key points:
- TAM $63-67B growing to $150B+ by 2033 (~10% CAGR)
- Oligopoly structure (Top 5 = ~45% market share)
- Pet humanization is the primary secular driver
- Diagnostics is the fastest-growing sub-segment (~12-15% CAGR)
- Regulatory barriers are very high

---

## GATE 9: SELF-CRITIQUE -- PASS

```
[X] Unvalidated assumptions listed
[X] Biases recognized
[X] Kill conditions defined
[X] What would change my mind
```

### Unvalidated Assumptions

1. **Librela decline is product-specific, not platform-wide.** If the mAb platform itself has class-wide safety issues, Cytopoint ($1B+ franchise) is also at risk. I cannot validate this from public data -- only future safety data will resolve it.

2. **2026 guidance is conservative.** I assume management guides conservatively and will beat. This is the historical pattern but may not hold in 2026 given structural headwinds (vet visit decline, generics approaching).

3. **Diagnostics will become a meaningful growth driver.** ZTS is investing heavily but is distant #2 to IDEXX. I assume the razor/blade model will create sticky recurring revenue, but this is unproven at scale for ZTS.

4. **Animal health generic market remains "rational."** I assume generic pricing will be less aggressive than human pharma. If Indian generics manufacturers enter with aggressive pricing, Apoquel erosion could be worse than modeled.

### Biases Recognized

- **Popularity bias:** ZTS is a well-known quality compounder that "comes to mind" easily. VALIDATED with sector screening data -- ZTS genuinely is the #1 company in the sector.
- **Confirmation bias:** The quality metrics (ROIC 26%, GM 71%, FCF growing) are so strong that it's tempting to dismiss the headwinds. I have tried to weight the DA's corrections seriously.
- **Anchoring:** The thesis's $140 FV anchored me initially. I corrected to $120 after evaluating the DA's arguments independently.

### Kill Conditions

1. **KC#1: ROIC falls below 15% for 2+ consecutive quarters** -- The 17pp+ ROIC-WACC spread is ZTS's core investment case. Compression to single-digit spread would signal fundamental deterioration.
2. **KC#2: Librela/Solensia pulled from market by FDA** -- Full product withdrawal (not just labeling) would eliminate the mAb franchise and signal platform risk.
3. **KC#3: Gross margin falls below 65% for 2 consecutive years** -- The 71%+ GM reflects pricing power and IP moat.
4. **KC#4: Companion animal revenue declines >5% organic for 2 consecutive quarters** -- Would signal structural demand destruction.
5. **KC#5: Loss of #1 market position** -- Scale moat compromised.
6. **KC#6: Apoquel generic share >30% within 2 years of launch** -- Would indicate animal health generics are more aggressive than assumed.
7. **KC#7: EU antitrust finding + ranevetmab licensing order** -- Would create biological competitor in EU.

### What Would Change My Mind

- **BUY sooner:** If ZTS drops to $95-100 due to broad market correction (not fundamental deterioration), providing 20%+ MoS.
- **REJECT entirely:** If Librela/Solensia are pulled by FDA, or if ROIC compresses below 15%, or if EU antitrust results in forced licensing.
- **Raise FV:** If Q1-Q2 2026 shows vet visit recovery, Librela stabilization, and diagnostics acceleration above expectations.

---

## GATE 10: COUNTER-ANALYSIS & INDEPENDENT ASSESSMENTS -- CONDITIONAL PASS

```
[X] Counter-analysis exists: devils_advocate.md
[X] Verdict: STRONG COUNTER (13/19)
[X] HIGH/CRITICAL challenges: 8 of 18
[X] Resolution of each HIGH challenge below
[X] Moat assessment exists: moat_assessment.md (22/25 WIDE)
[X] Risk assessment exists: risk_assessment.md (Score: HIGH)
[X] Valuation report: does NOT exist
```

### Resolution of HIGH/CRITICAL Challenges

| # | Challenge | Thesis Position | DA Position | COMMITTEE Resolution |
|---|-----------|----------------|-------------|---------------------|
| 1 | Librela safety deeper than acknowledged | Temporary, 6% of revenue | 9x adverse events, -32% US Q4, accelerating | **DA IS RIGHT.** Librela decline is real and may not be temporary. Adjusted FV by -$2. But it IS still 6% of revenue -- not existential. |
| 2 | Apoquel patent Nov 2026 | "Before 2030" (vague) | THIS YEAR, generics 2027 | **DA IS RIGHT.** Thesis understated the timeline. Added KC#6 for generic share monitoring. Adjusted FV by -$2. But animal health generics historically capture less share than human pharma. |
| 3 | Vet visit secular decline | Not prominently addressed | -3.1% in 2025, affordability crisis | **PARTIALLY RIGHT.** This is a real headwind but may be cyclical (interest rates, consumer confidence). International markets growing. Not enough to change fundamental thesis. |
| 7 | $140 FV includes unjustified premium | "Quality compounder premium" | Double-counts quality in OEY | **DA IS RIGHT.** Removed the premium. Committee FV = $120 (not $140). |
| 9 | Growth assumptions exceed guidance | 5-6% Y1-2 | Management guides 3-5% | **DA IS RIGHT.** Adjusted Y1 to 3-5% per guidance. |
| 11 | EU antitrust minimized | Brief mention | Novel but EC invested resources | **PARTLY RIGHT.** Added KC#7 for EU antitrust finding. But novel legal theory = probability remains medium. |
| 14 | Correlated risk cluster | Acknowledged | HIGH/CRITICAL risks correlated | **DA IS RIGHT.** Librela + Apoquel + vet visits + deceleration all hit companion animal. This correlation is the strongest argument for higher MoS, which I require ($95 entry vs thesis $110-115). |
| 16 | No near-term catalyst | Several listed | All are medium-term | **DA IS RIGHT.** No catalyst before Q1 2026 results (May 2026). Standing order approach addresses this -- we only enter when price discipline is met. |

### Moat Assessment Consistency

Moat assessment rates ZTS as **WIDE (22/25)**. This is consistent with the thesis and my assessment. The DA argues "WIDE but NARROWING" -- I partially agree. The moat is under localized siege (Librela safety, Apoquel generics) but the STRUCTURAL moat sources (regulatory barriers, no biosimilar pathway for biologics, switching costs, scale) remain intact.

**Committee classification: WIDE moat, with localized product-level risks.**

### Risk Assessment Consistency

Risk assessment scored **HIGH** with 5 HIGH/CRITICAL risks. The key finding is the CORRELATED downside cluster (Librela + Apoquel + vet visits + deceleration). This is the strongest argument for requiring higher MoS -- which I do ($95 entry = 20.8% MoS).

### Conflicts Resolved

1. **QS discrepancy (thesis 73/78 vs moat 73/81 vs tool 78):** Resolved. Tool now returns 78 with 2025 data. Committee QS = 80 (78 tool + 5 market position - 3 forward deductions).
2. **FV discrepancy (thesis $140 vs DA $115-125 vs risk assessment $127-135):** Resolved. Committee FV = $120. Removed quality premium. Accepted most DA corrections.
3. **Growth discrepancy (thesis 5-8% vs guidance 3-5%):** Resolved. Y1 = 3-5% (guidance), Y2-3 = 4-6%, Y4-5 = 6-7%.

**No CRITICAL unresolved challenges.** All HIGH challenges have been addressed through FV correction, entry price adjustment, and kill condition additions.

---

## VERDICT: WATCHLIST (with Standing Order at $95)

ZTS is a high-quality business (QS 80, WIDE moat, ROIC 26%+, GM 71%+, #1 global market position) that is currently priced at approximately fair value. The stock does NOT offer adequate margin of safety at current prices for any tier.

### Why NOT BUY at $126:

1. MoS vs corrected FV $120 = -5% (overvalued)
2. Lowest Tier A MoS precedent = 29% (AUTO.L). Current MoS is -5%.
3. Lowest Tier B MoS precedent = 18.4% (MMC, half position). Current MoS is -5%.
4. DA STRONG COUNTER (13/19) with 8 HIGH challenges -- all resolved but they collectively require HIGHER MoS, not LOWER.
5. Risk assessment = HIGH with correlated downside cluster.
6. No near-term positive catalyst.

### Why NOT REJECT:

1. Business quality is exceptional (0/10 value trap, WIDE moat, ROIC 26%+)
2. Secular growth TAM ($63B -> $150B+)
3. Pet humanization megatrend is real and structural
4. ZTS IS the innovator (not being disrupted)
5. At the right price, this is a textbook quality compounder

### Standing Order Parameters

```
WATCHLIST: ZTS (Zoetis Inc.)

Quality Score: 78 (tool) / 80 (adjusted) -- Tier A (low-end)
Current Price: $125.64 (2026-02-14)
Committee Fair Value: $120
MoS at current price: -4.7% (insufficient)

Entry Price: $95
  MoS at entry: 20.8% vs FV $120
  MoS at entry vs Bear ($95): 0% (bear floor)
  Consistent with: ROP (22%), ACGL (20%) Tier B standing orders

ADD Price: $85
  MoS at ADD: 29.2% vs FV $120
  Approaching Tier A MoS territory

Sizing: 4% (EUR ~400) -- consistent with Tier B standing order precedents

Condition of entry: Price must reach $95 OR below
  Alternative earlier entry: $105 IF Librela shows stabilization in Q1 2026 data
  (would provide 12.5% MoS -- still below precedents but acceptable with
  demonstrable headwind resolution)

Standing Order Valid Until: Q2 2026 earnings (expected May 2026)
  Re-evaluate after Q1 2026 results for: Librela trajectory, vet visit trends,
  Apoquel generic filings, 2026 guidance execution

Kill Conditions at Entry:
  KC#1: ROIC < 15% for 2+ quarters
  KC#2: Librela/Solensia FDA withdrawal
  KC#3: GM < 65% for 2 consecutive years
  KC#4: Companion animal revenue -5% organic 2Q
  KC#5: Loss of #1 market position
  KC#6: Apoquel generic share >30% within 2Y of launch
  KC#7: EU antitrust finding + ranevetmab licensing order
```

### Summary Table

| Gate | Result | Key Finding |
|------|--------|-------------|
| Gate 0 | PASS | Sector view exists (pharma-healthcare.md) |
| Gate 1 | PASS | QS 78 tool / 80 adjusted = Tier A (low-end) |
| Gate 2 | PASS | Business understood. 0/10 value trap. Quality compounder. |
| Gate 3 | PASS | Growth 3-7% (adjusted per DA). WACC 8.7%. Terminal 2.5%. |
| Gate 4 | PASS | Committee FV $120 (corrected from thesis $140). No quality premium. |
| Gate 5 | CONDITIONAL | MoS -5% at current $126. Entry at $95 provides 20.8% MoS. |
| Gate 6 | PASS | Mid-cycle US. Defensive business. USD weak = favorable. |
| Gate 7 | PASS | 4% sizing. Healthcare 7.4% post-buy. Low NVO correlation. |
| Gate 8 | PASS | Animal health subsector well understood. NEUTRAL-POSITIVO. |
| Gate 9 | PASS | Kill conditions defined (7). Biases documented. Assumptions listed. |
| Gate 10 | CONDITIONAL | DA STRONG COUNTER resolved. FV corrected. Entry adjusted. |

**9/10 PASS, 2 CONDITIONAL (resolved via entry price adjustment)**

---

## COMPARISON: Thesis Entry vs Committee Entry

| Parameter | Thesis | Committee | Reason for Difference |
|-----------|--------|-----------|----------------------|
| Fair Value | $140 | $120 | Removed quality premium. Accepted DA growth/Librela corrections. |
| QS | 73/78 | 78/80 | Tool updated with 2025 data. Market position +5, forward deductions -3. |
| Entry Price | $110-115 | $95 | Thesis FV was $140 so $110 = 21% MoS. With corrected FV $120, $110 = 8% MoS (insufficient). $95 = 20.8% MoS per Tier B precedents. |
| ADD Price | $105 | $85 | Same logic: $85 = 29% MoS vs $120 FV. |
| Sizing | 3-4% | 4% | Consistent with Tier B standing order pattern. |

---

## META-REFLECTION

### Doubts About This Decision

1. **The $120 FV could be too conservative.** If diagnostics accelerates beyond 13% and becomes 15-20% of revenue by 2028, the growth profile improves materially. The OEY midpoint of $135 may be more accurate on a 5-year view. But I prefer to err on the side of conservatism and buy cheaper.

2. **$95 may never be reached.** The stock is at $126 and just reported in-line earnings. A further 24% decline requires either a broad market correction or company-specific bad news. If ZTS stabilizes at $120-130 and compounds at 7-8% for 3 years, the opportunity cost of not owning it at $126 could be 20-30%. But disciplined entry > chasing.

3. **The QS tool now returns 78 (up from 73 in earlier runs).** This data dependency creates instability. The 78 reflects real improvements (EPS CAGR 10.2%, GM expanding) but also yfinance data timing. The underlying business quality has not changed between runs -- the data coverage has.

### Weaknesses in the Analysis Received

1. **Thesis FV of $140 was not defensible.** The 18% quality premium on top of a $119 weighted average was arbitrary and double-counted quality already captured in OEY. The DA correctly identified this.

2. **Thesis understated Apoquel timeline.** "Before 2030" sounds distant; "November 2026" is THIS YEAR. The thesis should have been more precise about the generic entry timeline.

3. **Moat assessment gave QS +8 while thesis gave +5.** These should have been reconciled in R3, not left as a discrepancy for R4 to resolve.

4. **Risk assessment identified 5 HIGH/CRITICAL risks but the thesis concluded WATCHLIST $110-115.** The entry price should have been adjusted downward to reflect the HIGH risk score, as I've done here.

### Suggestions for Improvement

1. **quality_scorer.py market_position fix** remains the most impactful tool improvement needed. This has been flagged since Session 61.

2. **For pharma/animal health positions, add "patent expiry timeline" as a mandatory field in the thesis template.** The Apoquel November 2026 expiry was underemphasized.

3. **The valuation reconciliation should explicitly state whether a "quality premium" is being added and justify it independently from the method weights.** The thesis's approach of adding 18% was opaque.

### Questions for Orchestrator

1. Should ZTS be added to quality_universe.yaml with entry $95 and FV $120?
2. The thesis's entry target of $110-115 is now obsolete given the corrected FV of $120. Should the thesis.md be updated with committee corrections, or should committee_decision.md serve as the authoritative document?
3. Given ZTS just reported Q4 2025 (Feb 12), the next data point is Q1 2026 (May 2026). Should the standing order validity period be set to May 2026 (aligned with next earnings), or longer?

---

## FILES TO CREATE (when plan executes):

1. `thesis/research/ZTS/committee_decision.md` -- This entire document
2. Update `world/sectors/pharma-healthcare.md` -- Correct ZTS entry from "$110-115" to "$95"
3. Add ZTS standing order to `state/standing_orders.yaml` at $95
4. Update `state/watchlist.yaml` if applicable

---

**Committee Decision: WATCHLIST with standing order at $95 (4%, ~EUR 400)**
**Valid until: Q2 2026 earnings (May 2026)**
**Re-evaluate: After Q1 2026 data (Librela trajectory, vet visits, generic filings)**
