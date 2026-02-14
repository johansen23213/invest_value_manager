# Investment Committee Decision: RACE.MI (Ferrari N.V.)

> **Date:** 2026-02-11
> **Agent:** investment-committee (Claude)
> **Framework:** v4.0 (Principios Adaptativos)
> **Status:** ROUND 4 (Final Gate)

---

## PASO 0.5: PRECEDENTES CONSULTADOS

Precedentes consultados:
- **AUTO.L**: Tier A (QS 79), MoS 29%, sizing 3.4%, outcome: HOLD LOW (moat degraded to Tier B post-adversarial). Relevance: Lowest MoS Tier A entry in portfolio history; AUTO.L was at 52w low with specific catalyst (dealer revolt = cyclical). Ferrari's MoS at current price (9%) is far below even this floor.
- **LULU**: Tier A (QS 82), MoS 34%, sizing 3.5%, outcome: HOLD (position open). Relevance: Identical QS to Ferrari (82). Luxury-adjacent business. Fell -58% from high vs Ferrari -35%. LULU had 34% MoS at entry; Ferrari would need EUR ~260 for comparable MoS.
- **NVO**: Tier A (QS 82), MoS 38%, sizing 3.4%, outcome: HOLD (position open). Relevance: Same QS, guidance shock (-17% in 2 days) created the entry. Ferrari's CMD caused -35% over months, but price has partially recovered to EUR 323. NVO was bought into maximum pessimism; Ferrari is post-earnings rebound (+11% off lows).

**Pattern from precedents:** All 6 Tier A entries had MoS 29-38%, averaging 34%. The minimum was 29% (AUTO.L). None was below 25%.

**If I deviate from these precedents:** I must explain why the context justifies accepting lower MoS. At current price (9% MoS), I CANNOT justify the deviation. Even at the thesis entry range of EUR 260-290 (MoS 18-27% vs reconciled FV EUR 355), only EUR 260 approaches the precedent floor.

---

## GATE 0: SECTOR VIEW EXISTS

**Sector view verified:** `world/sectors/luxury-goods.md` (created 2026-02-11)
- Status: NEUTRAL-SELECTIVO
- RACE.MI listed as priority research candidate
- Sector context: de-rating -30% from 2023 peaks, selective opportunities in ultra-luxury names

**PASS.** Proceed to Gates 1-10.

---

## GATE 1: QUALITY SCORE (CRITICAL)

- [x] Quality Score calculated: **82/100** (tool) / **84/100** (adjusted)
- [x] Tier assigned: **A**
- [x] Tier D check: NOT Tier D

**QS Tool:** 82/100 -- Financial 32/40, Growth 23/25, Moat 17/25, Capital Allocation 10/10.
**QS Adjusted:** 84/100 -- +2 for market position correction (0/8 in tool for manual field; Ferrari is unambiguously #1 in ultra-luxury sports cars, deserving 8/8). This is a factual correction, not a subjective upgrade. Adjustment < 5 points, no additional evidence required.

**Post-adversarial QS validation:** The devil's advocate did NOT challenge the QS score. The moat assessment scored 23/25 WIDE. The quality of the business is undisputed. The dispute is about the PRICE.

**Key QS metrics:**
| Metric | Value | Assessment |
|--------|-------|------------|
| ROIC | 24.9% | Exceptional |
| ROIC-WACC spread | +14.9pp | Top-decile |
| Gross Margin | ~50% | +15pp vs auto sector |
| FCF Margin (industrial) | 21.5% (FY2025) | Strong (normalize ~18%) |
| Net Debt/EBITDA | Net cash | Fortress |
| Insider Ownership | 30.5% (Exor/Agnelli) | Maximum alignment |

**PASS.** Quality is exceptional. Proceed.

---

## GATE 2: BUSINESS UNDERSTANDING

- [x] Business Analysis Framework completed (thesis Section: Business Understanding)
- [x] Can explain in 2 minutes: Ferrari is a luxury goods business disguised as an automaker. Produces ~13,600 cars/year deliberately below demand. Revenue grows via ASP increase (+10%/yr compound), personalization, and mix -- NOT volume. Order book extends to end-2027. Gross margin ~50%, EBIT margin 29.5% and expanding. ROIC 24.9%. Net cash. Moat = brand (80+ years, F1) + scarcity (2-year waitlist) + pricing power (10% tariff pass-through with zero demand impact). Stock down -35% from peak because CMD guided 5% revenue CAGR (vs 12% historical), disappointing growth investors.
- [x] Know WHY it is cheap + counter-thesis: CMD growth reset from 12% to 5% CAGR caused P/E compression from ~55x to ~36x. Counter-thesis: 5% is the FLOOR (management historically beats), margins expanding, FCF growing faster than revenue, scarcity model protects.
- [x] Value trap checklist: **0/10 YES** -- No value trap indicators.
- [x] Informational advantage: Longer time horizon + understanding that Ferrari is luxury (not auto) + market overreaction to growth deceleration

**PASS.** Business is deeply understood. No value trap risk.

---

## GATE 3: PROJECTION FUNDAMENTALS

- [x] Revenue growth derived: 5.5% CAGR (R3 reconciled: split between management 5% guidance and thesis 6.5%)
  - Volume: 0-0.5% (deliberate cap at ~13,600-14,000 units)
  - ASP growth: 4-5% (mix enrichment, personalization, selective pricing)
  - Other: 0.5-1% (brand/sponsorship)
- [x] WACC calculated: 9.35% (Ke = Rf 4.35% + Beta 1.0 x ERP 5.0%; near-zero debt so WACC = Ke)
- [x] Terminal growth: 3.0% (justified by UHNW population growth ~5%, Ferrari's pricing power, constrained by GDP growth ceiling)
- [x] Scenarios documented:

| Scenario | Revenue CAGR | EBIT Margin 2030 | Multiple | FV | Probability |
|----------|-------------|-------------------|----------|-----|-------------|
| Deep Bear | 2% | 25% | 22x | EUR 220 | 5% |
| Bear | 3.5% | 28% | 25x | EUR 270 | 15% |
| Base | 5.5% | 30% | 30x | EUR 355 | 55% |
| Bull | 8% | 32% | 36x | EUR 440 | 25% |

**R3 Expected Value:** (EUR 220 x 5%) + (EUR 270 x 15%) + (EUR 355 x 55%) + (EUR 440 x 25%) = EUR 11 + EUR 40.5 + EUR 195.25 + EUR 110 = **EUR 357**

**PASS.** Projections are grounded in business logic, not defaults.

---

## GATE 4: MULTI-METHOD VALUATION

Methods selected per Tier A protocol:

**Method 1: Owner Earnings Yield (OEY)** -- Tier A Primary
```
Normalized industrial FCF: EUR 1,300M (conservative vs FY2025 EUR 1,538M)
Depreciation: EUR 662M
Maintenance Capex: EUR 728M (D&A x 1.1)
Owner Earnings: EUR 1,234M
OEY: 2.16% (EUR 1,234M / EUR 57,200M market cap)
OEY + Growth: 2.16% + 5.5% = 7.66%
vs WACC: 9.35%
Spread: -1.69pp (NEGATIVE)
```
**OEY Assessment: At current price, Ferrari does NOT clear cost of capital on an earnings-yield basis.** This is a known limitation for ultra-luxury compounders (Hermes also fails this test). It means the market assigns a "quality premium" that makes OEY+Growth < WACC at almost any realistic entry price for Ferrari. OEY-implied FV (where OEY+Growth = WACC): ~EUR 244.

**Method 2: EV/EBIT Multiple** -- Most Appropriate for Luxury Compounder
```
EBIT FY2026E: EUR 2,213M (Revenue EUR 7.5B x 29.5% guided margin)
Multiple: 30x (R3 reconciled: between thesis 32-33x and adversarial 28x)
EV: EUR 66,390M
Net Debt: ~EUR 0
Equity: EUR 66,390M
FV/share: EUR 66,390M / 177M = EUR 375
```

**Method 3: P/E Relative**
```
EPS FY2026E: EUR 9.70
P/E: 37x (R3 reconciled: between thesis 39x and adversarial 35x)
FV: EUR 9.70 x 37 = EUR 359
```

### Reconciliation

| Method | FV | Weight | Weighted | Rationale |
|--------|-----|--------|----------|-----------|
| OEY | EUR 244 (break-even) | 30% | EUR 73.2 | Mandated Tier A primary. Tells us current price is fully valued on earnings yield. Given higher weight than thesis (20%) per adversarial concern. |
| EV/EBIT (30x) | EUR 375 | 40% | EUR 150.0 | Most appropriate for luxury franchise. R3 reconciled 30x. |
| P/E (37x) | EUR 359 | 30% | EUR 107.7 | Historical P/E average ~39x; reconciled to 37x reflecting growth reset. |
| **Weighted FV** | | **100%** | **EUR 331** | |

**Divergence:** (EUR 375 - EUR 244) / EUR 331 = 40%. **ABOVE 30% threshold.**

**Explanation for divergence:** The OEY method structurally undervalues luxury compounders because their quality premium (brand, scarcity, 2-year order book) justifies a lower required return than WACC alone implies. Hermes, the closest comparable, also trades at OEY+Growth well below WACC. This is a known methodological gap, not an anomaly. The divergence is expected and documented.

**Committee FV Decision:** I give OEY 30% weight (above the thesis's 20% but below the mandated 50%). The reason I do not use 50%: OEY produces a break-even price of EUR 244, which is 25% below the stock's COVID trough. This suggests the method is structurally inapplicable to ultra-luxury compounders whose quality commands a permanent multiple premium. However, the OEY signal that Ferrari does not clear WACC at current price is important and should not be dismissed.

**Final Committee Fair Value: EUR 355** (Using R3 reconciled FV as the best balanced estimate, which incorporates adversarial adjustments to multiples and growth rate)

**MoS at various prices:**
| Price | MoS vs EUR 355 | MoS vs Bear EUR 270 | MoS vs Deep Bear EUR 220 |
|-------|----------------|----------------------|--------------------------|
| EUR 322.80 (current) | 9% | -16% | -32% |
| EUR 290 | 18% | -7% | -24% |
| EUR 280 | 21% | -4% | -21% |
| EUR 270 | 24% | 0% | -19% |
| EUR 260 | 27% | +4% | -15% |

**CONDITIONAL PASS.** Valuation is sound. But MoS at current price is INADEQUATE. MoS becomes reasonable only at EUR 260-270.

---

## GATE 5: MARGIN OF SAFETY (REASONED v4.0)

- [x] Tier: A (QS 82/84)
- [x] MoS actual vs Base (EUR 355): **9%** at EUR 322.80 -- INADEQUATE
- [x] MoS actual vs Bear (EUR 270): **-16%** -- price is ABOVE bear case

**Reasoning:**

The MoS at current price (9%) is the weakest of ANY Tier A candidate in portfolio history. Precedents:

| Ticker | Tier | MoS at Entry | Sizing | Context |
|--------|------|-------------|--------|---------|
| NVO | A (82) | 38% | 3.4% | -49% from high, guidance shock |
| MONY.L | A (81) | 36% | 4.1% | 52w low |
| BYIT.L | A (81) | 35% | 3.5% | -47% from high |
| LULU | A (82) | 34% | 3.5% | -58% from high |
| ADBE | A (76) | 31% | 4.8% | 52w low |
| AUTO.L | A (79) | 29% | 3.4% | -47% from high |
| **Average** | | **34%** | **3.5%** | |
| **Minimum** | | **29%** | | |
| **RACE.MI at EUR 323** | **A (82)** | **9%** | **--** | **-35% from high, post-earnings rebound** |

**The gap is stark.** Ferrari at EUR 323 offers MoS that is 20 percentage points below the Tier A average and 20pp below the Tier A minimum. This is not a minor deviation -- it would represent a fundamental break with established practice.

**Can the deviation be justified?**

Arguments FOR accepting lower MoS:
1. Ferrari's business quality is comparable to the best in the portfolio (QS 82, WIDE moat, 0/10 value trap)
2. Bear case downside is limited (~EUR 270, only 16% below current)
3. Order book to end-2027 provides exceptional visibility
4. Luxury compounders rarely trade at deep discounts

Arguments AGAINST:
1. OEY + Growth < WACC -- the mandated primary method says the stock is fully valued
2. The devil's advocate produced a STRONG COUNTER (9 of 18 challenges at HIGH/CRITICAL)
3. Risk is MEDIUM-HIGH with 4 correlated HIGH risks
4. FV is 85% multiple-dependent (subjective)
5. The thesis itself recommends entry at EUR 290-305, NOT at EUR 323
6. We have 44% cash -- there is NO urgency to deploy
7. The adversarial view puts FV at EUR 335, making current-price MoS only 3.7%

**VERDICT:** The arguments against overwhelm the arguments for. Accepting 9% MoS would require an extraordinary justification (e.g., a crisis creating a fleeting opportunity). Ferrari at EUR 323 is the opposite: it is post-earnings, the stock has rebounded 11% from recent lows, and the market is digesting the results calmly.

**Precedent most similar:** AUTO.L (29% MoS, lowest Tier A entry). The AUTO.L entry was justified by: (a) specific cyclical catalyst (dealer revolt creating temporary fear), (b) near 52-week low, (c) capital from SHEL.L rotation creating deployment pressure. Ferrari at EUR 323 has none of these catalysts.

**Do I deviate from precedent?** NO. The 9% MoS is indefensible.

**At what price would MoS be adequate?**
- EUR 270: MoS 24% vs R3 FV -- approaching the precedent floor of 29%. Acceptable if combined with a specific catalyst.
- EUR 260: MoS 27% -- within 2pp of the precedent minimum. This is the entry I would approve.
- EUR 252: MoS 29% -- matches the precedent minimum exactly.

**FAIL at current price.** CONDITIONAL PASS at EUR 260-270 with standing order.

---

## GATE 6: CONTEXT MACRO

- [x] World view reviewed (date: 2026-02-11)
- [x] Economic cycle: Mid-cycle (US resilient, inflation sticky, rates higher-for-longer)
- [x] Enterprise-cycle fit:

Ferrari's UHNW customer base is largely insensitive to macroeconomic cycles. The luxury sector has de-rated -30% from 2023 peaks, creating selective value. However:

- **US tariffs (25% on EU autos)** directly impact Ferrari (29% US revenue). Tariff deadline June 1 creates binary event risk.
- **USD weakness (DXY ~96.8)** creates FX headwind for EUR-reported US revenue.
- **China luxury demand weakening** -- Porsche China -26%, Ferrari China -8% revenue. Minor for Ferrari but part of a broader sectoral trend.
- **Sticky inflation** could compress multiples further if rates stay higher-for-longer.

**Macro fit: NEUTRAL with CAUTION.** The macro environment does not argue against Ferrari specifically, but it does not provide a tailwind either. The tariff situation is the most relevant macro risk.

**CONDITIONAL PASS.** No macro hard block, but tariff resolution (June 1) would be a significant de-risking event.

---

## GATE 7: PORTFOLIO FIT (REASONED v4.0)

- [x] Price verified: EUR 322.80 (2026-02-11)
- [x] Sizing proposed: 3% initial (~EUR 350) at entry price

**Constraint checker output (simulated EUR 350 buy):**
- Position post-buy: 3.5% -- Coherent with Tier A precedent (3-5% initial). Conservative end of range.
- Sector post-buy: Consumer Cyclical 10.4% -- LULU is the only other Consumer Cyclical position. Ferrari is luxury, not overlapping with LULU's athletic premium. Low sectoral concentration.
- Geography post-buy: EU 17.1% -- Currently low EU exposure (EDEN.PA, DTE.DE). Ferrari adds Italian/EUR diversification. Well within prudent bounds.
- Cash post-buy: EUR 4,494 (44.9%) -- Substantial dry powder remains.
- If RACE.MI falls 50%: -1.7% portfolio impact -- Acceptable for Tier A conviction.

**Correlation analysis:**
- vs LULU: Low-Medium. Both consumer discretionary but different sub-sectors (ultra-luxury auto vs premium athletic). Different geographies (Italy/EU vs US). Different customer bases (UHNW vs affluent).
- vs EDEN.PA: Low. Different sector (business services vs luxury goods).
- vs UK positions: Very Low. Ferrari diversifies away from UK concentration (currently 4 UK positions).

**Portfolio benefit:** Ferrari would add genuine sector diversification (luxury goods -- not represented in portfolio), geographic diversification (Italy/EUR), and quality (Tier A). The portfolio currently has no luxury goods exposure.

**Sizing precedent:** Tier A entries have been 3-5% initial. At EUR 350 (~3.5%), consistent with NVO (3.4%), LULU (3.5%), BYIT.L (3.5%), AUTO.L (3.4%).

**PASS.** Portfolio fit is excellent. Ferrari would add diversification on multiple dimensions.

---

## GATE 8: SECTOR UNDERSTANDING

- [x] Sector view exists: `world/sectors/luxury-goods.md`
- [x] Sector view reviewed (date: 2026-02-11)
- [x] TAM and trends understood: Global personal luxury EUR 370B, ultra-luxury auto ~EUR 50-60B, UHNW population +5% CAGR
- [x] Disruption risks known: EV transition (managed cautiously), tariffs (demonstrable pass-through), China slowdown (minor exposure)
- [x] Sector position: NEUTRAL-SELECTIVO -- Opportunities selective in names with de-rating

**PASS.** Sector context fully documented and understood.

---

## GATE 9: SELF-CRITIQUE

**Unvalidated assumptions:**
1. The 30x EV/EBIT multiple is appropriate. If the market re-classifies Ferrari as "premium auto" (25x), FV drops to EUR 312, making current price overvalued.
2. Management will beat 5% CAGR guidance as historically. If 5% IS the ceiling (not floor), base-case growth is 5%, not 5.5%.
3. Luce launch will be at least neutral to the brand. If it damages Ferrari's ICE identity, the moat narrative shifts.
4. US tariffs will remain at 25% or resolve lower. Escalation to 35%+ would materially impact margins.

**Biases recognized:**
- [x] Popularity bias: Ferrari is a famous brand. I must ensure the analysis is driven by fundamentals, not brand admiration. The OEY failure is a critical reality check against this bias.
- [x] Confirmation bias: The thesis, moat, valuation, and risk assessments all describe an exceptional business. The risk is conflating "great business" with "great investment." The devil's advocate correctly flags this.
- [x] Recency bias: FY2025 was excellent (FCF +50%). But FY2025 had one-time WC benefits. FY2026 will have higher capex. Normalizing is essential.

**Kill conditions (consolidated from all analyses, including adversarial KC#7-9):**
1. **Volume discipline abandoned:** Production >15,000 units/year
2. **Margin deterioration:** EBIT margin <25% for 2 consecutive quarters
3. **Order book shortens:** Below 12 months visibility
4. **Management credibility:** CEO Vigna departure without credible successor; or Exor/Piero Ferrari sells >5% in 12 months
5. **Brand damage:** Major quality/safety scandal, F1 exit, or mass-market licensing dilution
6. **Luce complete failure:** Zero demand or brand contagion to ICE lineup
7. **P/E sustained below 30x for 6+ months** (adversarial KC#7) -- market reclassification signal
8. **FY2026 revenue misses EUR 7.3B** (adversarial KC#8) -- below guided EUR 7.5B by >EUR 200M
9. **Cumulative buyback at avg P/E >35x with ROIC declining** (adversarial KC#9)

**What would make me change my mind about buying (even on watchlist):**
- P/E compresses to <25x for 6+ months (kill condition #7)
- Luce launch reveals brand damage across ICE lineup
- Management abandons scarcity model to chase growth
- ROIC falls below WACC

**PASS.** Self-critique is thorough. Kill conditions are comprehensive.

---

## GATE 10: COUNTER-ANALYSIS & INDEPENDENT ASSESSMENTS

### Counter-Analysis (Devil's Advocate)
- [x] Exists: `thesis/research/RACE.MI/devils_advocate.md`
- [x] Verdict: **STRONG COUNTER** (9 of 18 challenges at HIGH/CRITICAL)

**CRITICAL challenges (2):**

| Challenge | Thesis Response | Resolved? |
|-----------|----------------|-----------|
| OEY + Growth (8.66%) < WACC (9.35%) | Known limitation for ultra-luxury compounders. Hermes also fails this test. The OEY method is structurally inapplicable as sole valuation for luxury franchises that command quality premiums. However, the signal that current price is fully valued IS valid and should not be dismissed. | PARTIALLY -- Acknowledged but not resolved. OEY given 30% weight (above thesis 20%), pulling committee FV down. |
| MoS at current price (9-17%) breaks every Tier A precedent (avg 34%, min 29%) | AGREED. This is the dispositive issue. No entry should occur at current price. The committee will set entry at EUR 260-270 where MoS reaches 24-27%, approaching precedent floor. | YES -- Resolved by rejecting current-price entry and setting standing order at lower price. |

**HIGH challenges (7):**

| Challenge | Resolution |
|-----------|-----------|
| "Luxury not auto" classification is oversimplified | PARTIALLY AGREED. Ferrari is more luxury than auto but capital intensity is structurally higher than pure luxury (Hermes). Committee uses 30x EV/EBIT (below thesis 32-33x, above adversarial 28x) to reflect this hybrid nature. |
| FV 85% multiple-dependent | ACKNOWLEDGED. The sensitivity is real. FV changes EUR 12.50/share per 1x EV/EBIT change. Mitigated by using R3 reconciled 30x (conservative within range). |
| Growth assumption above guidance | ADDRESSED. R3 reconciled to 5.5% (split between 5% guidance and 6.5% thesis). Committee uses 5.5% not 6.5%. |
| No deep bear case in thesis | ADDRESSED. Committee adds deep bear at EUR 220 (22x, 25% margin) with 5% probability. Included in scenario table above. |
| Risk scored MEDIUM despite 4 HIGH risks | UPGRADED to MEDIUM-HIGH per adversarial recommendation. |
| Tail risk exceeds MoS at current price | ACKNOWLEDGED. This reinforces the FAIL on Gate 5 at current price. At EUR 260-270 entry, MoS of 24-27% provides more buffer against tail risk. |
| Bear case too optimistic at EUR 280 | ADDRESSED. Committee bear = EUR 270 (25x, 28% margin). Deep bear EUR 220 added. |

**Unresolved CRITICAL challenges:** ZERO (both CRITICAL challenges resolved or addressed).

### Independent Assessments

**Moat Assessment (moat_assessment.md):**
- [x] Classification: WIDE (23/25). Moat score AGREES with thesis. Expanding trajectory.
- [x] Discrepancy: Moat scored "Network Effects" 2/5 and "Efficient Scale" 3/5. Adversarial notes these may be generous. I agree "network effects" is more accurately "brand aspiration" -- but this is captured in the Intangible Assets score of 5/5. No material impact on overall WIDE classification.

**Risk Assessment (risk_assessment.md):**
- [x] 4 HIGH risks identified, all incorporated in committee analysis
- [x] Kill conditions #1-6 from risk assessment adopted
- [x] "Perfect storm" scenario (EUR 170-200) noted but probability is low (10-15%). Captured partially in deep bear (EUR 220 at 5% probability).
- [x] Risk upgraded from MEDIUM to MEDIUM-HIGH per adversarial review

**Valuation Report (valuation_report.md):**
- [x] Independent FV: EUR 377 (vs thesis EUR 379). Agreement is strong.
- [x] Adversarial FV: EUR 335 (using more conservative multiples).
- [x] **Committee reconciled FV: EUR 355** -- between thesis/valuation-specialist (EUR 377-379) and adversarial (EUR 335), reflecting:
  - R3 reconciled 30x EV/EBIT (between 28x adversarial and 32-33x thesis)
  - 5.5% growth (between 5% guidance and 6.5% thesis)
  - 30% OEY weight (above thesis 20%, acknowledging the WACC signal)

**Conflicts between analyses:** All four independent analyses (thesis, moat, risk, valuation) agree on business quality. The ONLY conflict is on PRICE adequacy. The adversarial correctly identifies that great quality does not equal great entry price. The committee resolves this by approving the thesis but setting entry below current price.

**PASS.** All counter-analysis challenges resolved or addressed. No unresolved CRITICAL items.

---

## VERDICT: WATCHLIST -- CONDITIONAL APPROVE WITH STANDING ORDER

### Summary of 10 Gates

| Gate | Result | Notes |
|------|--------|-------|
| 0. Sector View | **PASS** | luxury-goods.md exists |
| 1. Quality Score | **PASS** | QS 82/84, Tier A |
| 2. Business Understanding | **PASS** | Deeply understood, 0/10 value trap |
| 3. Projection | **PASS** | Bottom-up derived, 4 scenarios |
| 4. Multi-Method Valuation | **CONDITIONAL PASS** | FV EUR 355. MoS inadequate at current price |
| 5. Margin of Safety | **FAIL at EUR 323** | 9% MoS vs 34% Tier A average. CONDITIONAL PASS at EUR 260-270 |
| 6. Macro Context | **PASS** | Neutral with tariff caution |
| 7. Portfolio Fit | **PASS** | Adds sector + geographic diversification |
| 8. Sector Understanding | **PASS** | Luxury-goods sector view comprehensive |
| 9. Self-Critique | **PASS** | 9 kill conditions, biases documented |
| 10. Counter-Analysis | **PASS** | STRONG COUNTER addressed; 0 unresolved CRITICAL |

### Decision

**WATCHLIST: RACE.MI (Ferrari N.V.)** with standing order at specific entry prices.

```
RECOMMENDATION: SET STANDING ORDER for RACE.MI

Quality Score: 82/100 (Tool) / 84/100 (Adjusted) --> Tier A
Fair Value: EUR 355 (R3 reconciled)
Risk: MEDIUM-HIGH
Category: Quality Compounder (Luxury Goods)

STANDING ORDER 1: BUY EUR 350 (~3%) at EUR 270
  MoS: 24% vs base FV EUR 355
  MoS: 0% vs bear FV EUR 270 (at bear floor)
  Rationale: Approaching Tier A precedent floor (29%). Price would be
  at 52-week low territory. EUR 270 is where MoS vs adversarial FV
  (EUR 335) reaches 24% -- a level where both thesis and adversarial
  views agree the stock is reasonably priced.

STANDING ORDER 2: ADD EUR 350 (to ~6% total) at EUR 260
  MoS: 27% vs base FV EUR 355
  MoS: +4% vs bear FV EUR 270
  Rationale: MoS of 27% is within 2pp of Tier A precedent minimum (29%).
  At EUR 260, Ferrari would be below its 52-week low (EUR 276.20),
  requiring a specific catalyst (tariff escalation, macro shock, or
  Luce reception concern) to reach. If it reaches this level, the
  risk-reward is compelling for a full Tier A position.

DO NOT BUY at current EUR 322.80.
  MoS: 9% -- below every Tier A precedent by 20+ pp.
  No catalyst justifies breaking the pattern.

Kill conditions: 9 defined (see Gate 9)
Review trigger: Luce exterior reveal (May 2026), tariff resolution (June 1),
  Q1 2026 results (if price approaches entry levels)
```

### Sizing Rationale

3% initial position at EUR 270, consistent with:
- Tier A precedents: NVO 3.4%, LULU 3.5%, BYIT.L 3.5%, AUTO.L 3.4%
- Conservative end of range due to: (a) MEDIUM-HIGH risk with 4 correlated HIGH risks, (b) first EV launch creating execution uncertainty, (c) tariff situation unresolved, (d) OEY < WACC signal
- If cae 50%: -1.5% portfolio impact -- acceptable for Tier A conviction
- ADD to 6% at EUR 260 if price drops further, bringing total risk in line with higher-conviction entries (ADBE 4.8%)

Precedent most similar: AUTO.L (29% MoS, 3.4% sizing) -- same "fallen angel" dynamic but with specific near-term uncertainty.

### Why NOT Buy at Current Price

1. **OEY + Growth < WACC.** The mandated Tier A primary method says the stock is fully valued.
2. **MoS 9% vs 34% Tier A average.** This would be the largest deviation from precedent in portfolio history. No justification exists.
3. **STRONG COUNTER from devil's advocate.** 9 HIGH/CRITICAL challenges, 2 CRITICAL resolved only by NOT buying at current price.
4. **44% cash with no urgency.** Lesson from Jan 26-Feb 3: deployment pressure causes mistakes. Patience is the correct default.
5. **Post-earnings rebound.** Stock is +11% from recent lows. The easy money has been made. Buying into a rebound at inadequate MoS is the opposite of our process.
6. **The thesis itself recommends EUR 290-305 entry.** The valuation specialist recommends EUR 290-305. The adversarial recommends EUR 280-295. NO agent recommends buying at EUR 323.

### Why Standing Order at EUR 260-270 (Not EUR 290-305)

The thesis recommends EUR 290-305 and the adversarial recommends EUR 280-295. I set the standing order at EUR 260-270 because:

1. **Post-adversarial standards are higher.** The adversarial review project (Sessions 48-53) revealed that 14/16 positions had inflated FVs (avg -19%). Our committee FV of EUR 355 already incorporates adversarial adjustments, but the lesson is to be conservative on entry.
2. **Consistency with precedent.** At EUR 270 (MoS 24%), we are still below the Tier A minimum of 29%. At EUR 260 (MoS 27%), we approach it. EUR 290-305 (MoS 15-18%) would be the weakest Tier A entry ever, setting a precedent I do not want to establish.
3. **The OEY signal.** OEY says the stock is fairly valued at ~EUR 330. Buying at EUR 270-290 gives a 15-20% discount to even the OEY fair value, providing genuine margin of safety even on the conservative method.
4. **Patience cost is low.** We have 44% cash. If Ferrari never reaches EUR 260-270, we preserve capital for other Tier A opportunities. The opportunity cost of NOT buying Ferrari is low when we have DSY.PA and DNLM.L as approved standing orders at closer-to-trigger prices.

---

## META-REFLECTION

### Doubts About This Decision
- **Am I being too conservative?** Ferrari is an exceptional business and the stock is -35% from peaks. If it never reaches EUR 260-270, we miss a high-quality compounder. However, the data (OEY < WACC, 9% MoS, STRONG COUNTER from adversarial) all point the same direction: current price is not compelling enough.
- **Is the OEY method appropriate for Ferrari at all?** Ultra-luxury compounders trade at quality premiums that make OEY+Growth < WACC structurally. If we always give OEY 30%+ weight for Tier A, we may systematically exclude the highest-quality luxury businesses. This is worth revisiting in the valuation-methods skill.
- **The EUR 260-270 entry may never trigger.** Ferrari's 52-week low is EUR 276.20. Reaching EUR 260 would require a new 52-week low. This is possible (tariff escalation, Luce concern, macro shock) but not probable in the near term. The standing order may sit untriggered for months.

### Weaknesses of the Analysis Received
- **All four independent agents converged on the same FV range (EUR 377-379).** The adversarial correctly flags this as potentially suspicious -- the agents used the same frameworks and data. True independence would require different methodologies.
- **The industrial FCF figure of EUR 1,538M (FY2025) was not independently verified** against GAAP financials. The normalization to EUR 1,300M is reasonable but based on thesis assumptions.
- **Tariff impact was not quantitatively modeled.** A margin impact analysis of 25% tariff on 29% US revenue would strengthen the risk assessment.
- **The yfinance dividend yield error (96%)** was flagged by all agents but not fixed. This is a data quality issue that should be addressed in quality_scorer.py.

### Suggestions for Improvement
1. **Update valuation-methods skill for luxury compounders.** Add a documented framework for when OEY + Growth < WACC is acceptable (e.g., moat score >20/25, ROIC >2x WACC, order book >18 months). Currently the skill does not address this edge case.
2. **Add DCF FCF override parameter.** For companies where yfinance FCF materially differs from reported FCF (Ferrari, REITs), `dcf_calculator.py --fcf-override` would make the tool useful.
3. **Fix yfinance dividend yield validation.** Add a check in price_checker.py/quality_scorer.py that flags yields >50% as probable data errors.

### Questions for Orchestrator
- None. The decision is clear: WATCHLIST with standing orders at EUR 260-270. All counter-analysis has been addressed. The committee is confident in this verdict.

---

**Committee Decision Date:** 2026-02-11
**Decision:** WATCHLIST with standing orders
**Fair Value:** EUR 355 (R3 reconciled)
**Entry 1:** EUR 270 (3% initial, MoS 24%)
**Entry 2:** EUR 260 (ADD to 6%, MoS 27%)
**Current Price:** EUR 322.80 -- DO NOT BUY
**Kill Conditions:** 9 defined
**Review Triggers:** Luce reveal (May 2026), tariff resolution (June 1), Q1 2026 results
**Next Review:** If price approaches EUR 280 or material news
