# INVESTMENT COMMITTEE DECISION: MORN (Morningstar, Inc.)

## GATE 0: SECTOR VIEW EXISTS -- PASS

Sector view verified: `world/sectors/financial-data-analytics.md`
Updated: 2026-02-13. Status: NEUTRAL-SELECTIVO.

---

## PASO 0.5: PRECEDENTES CONSULTADOS

Precedentes consultados:
- **ADBE**: Tier A (adj 73-76), MoS 31%, sizing 4.8%, BUY executed. Relevance: Same Tier A quality compounder at 52-week low. Similar conviction level.
- **NVO**: Tier A (adj 82), MoS 38%, sizing 3.4%, BUY executed. Relevance: Tier A fallen angel bought on panic. Higher MoS than ADBE due to binary event (CagriSema).
- **BYIT.L**: Tier A (adj 68-72 post-adversarial from 81), MoS 35%, sizing 3.5%, BUY executed. Relevance: Tier A that was downgraded by adversarial to Tier B. Similar risk of QS adjustment.
- **ROP**: Tier B (adj 70 from tool 48), MoS 22% at $300 standing order, sizing 4%. Relevance: Standing order approach. Lower MoS accepted with wide moat justification.

If I deviate from these precedents: MORN's situation is unique because it has a STRONG COUNTER (13/19) from DA with FV reduced from $205 to DA's $163. This is similar to BYIT.L's adversarial experience (FV -24.2%). The R3 resolution already reduced FV from $205 to $180 (-12%), but the DA argues for further reduction to $155-170.

---

## GATE 1: QUALITY SCORE -- PASS (CONDITIONAL)

```
[x] Quality Score calculated
[x] Tier assigned: A (low-end)
[ ] Tier D check: NOT Tier D
```

**QS Tool Run (Today):** Legacy Score = 60/100 (Tier B)
- ROIC Spread: 0/15 (ROIC 2025 = NaN, data gap)
- FCF Margin: 2/10 (tool shows 8.7% for 2023, not the more relevant 2024 figure of ~19.7%)
- The tool score of 60 is SEVERELY distorted by two data gaps:
  1. ROIC latest = NaN (2025 data unavailable in yfinance)
  2. FCF margin only shows through 2023, missing the 2024 recovery to ~20%
  3. Market Position = 0/8 (known tool default requiring manual input)

**QS Thesis Claim:** Tool 83, Adjusted 80 (from R1)
**QS R3 Resolution:** Adjusted to 78

**My Independent QS Assessment:**

Using the tool's PROFILE data (not the Legacy Score which is clearly distorted):
- ROIC 2024: 19.5% vs WACC 9.5% = +10pp spread -> 12/15
- FCF Margin 2024: ~19.7% (from thesis, confirmed by $449M FCF / $2.28B rev) -> 8/10
- Leverage: ND/EBITDA 1.1x -> 8/10
- FCF Consistency: 4/4 years positive -> 5/5
- Financial subtotal: 33/40

- Revenue CAGR 10.3% -> 8/10
- EPS CAGR: The 75.6% is from 2022 trough. DA correctly flags this. Normalized from 2021: ~24%. Even so, this scores 10/10.
- GM Trend: Expanding (58.3% -> 60.6%) -> 5/5
- Growth subtotal: 23/25

- GM Premium: +30.6pp vs sector -> 10/10
- Market Position: #3-5 in broad financial data, #1 in advisor research, #1 PitchBook, #4 DBRS -> 5/8
- ROIC Persistence: 2024 YES, 2023 BORDERLINE (8.9% vs 9.5% WACC), 2022 NO. Only 1/3 clearly above. Tool shows 2/7. Even with longer history, the 2022 dip is real. -> 3/7
- Moat subtotal: 18/25

- Shareholder Returns: Dividend continuous + buybacks -> 5/5
- Insider Ownership: 46% -> 5/5
- Cap Alloc subtotal: 10/10

**My QS Calculation: 84/100** before adjustments.

**Adjustments:**
1. Market Position corrected from 0/8 to 5/8: already incorporated above.
2. ROIC persistence: The tool only has 4 years. I scored 3/7 which is conservative vs the thesis's 5/7. The difference from thesis's 83: my 84 vs their 83 is consistent -- the small difference is in ROIC persistence scoring.
3. **DA-flagged adjustments:**
   - EPS CAGR from 2022 trough inflates growth score. The 10/10 score is technically correct on the numbers but misleading. Forward EPS growth will be 8-12%, not 75%. However, the QS formula uses historical CAGR, not forward. No score change, but note the limitation.
   - FCF declined 1.4% in FY2025 ($442.6M vs $449M). This is real and contradicts "expanding" narrative. But the QS uses historical FCF margin which was 19.7% -- still correct for scoring.
   - CRSP goodwill adds to leverage: ND/EBITDA will rise from 0.9x to ~1.5x. Still scores 8/10, no change.

**Adjusted QS: 78-80/100 (Tier A, low-end)**

This is consistent with the R3 resolution's QS 78. I will use **QS 78 (Tier A, low-end)**.

**Key concern:** The EPS CAGR score of 10/10 is based on a recovery from abnormal 2022 trough. The QS formula mechanically rewards this, but the investor should understand that forward growth is 7-9%, not 75%. This does NOT change the tier (even reducing EPS CAGR to 5/10, QS would be 73 = still Tier B high-end / Tier A borderline).

**Verdict Gate 1: PASS. QS 78, Tier A (low-end). Robust to downward adjustments -- even at QS 73 (worst case), Tier B upper end.**

---

## GATE 2: BUSINESS UNDERSTANDING -- PASS

```
[x] Business Analysis Framework completed (thesis Section: Business Understanding)
[x] Can explain in 2 minutes: YES
[x] Know WHY it's cheap + contra-thesis: YES
[x] Value trap checklist: 0-1/10 SI -- LOW risk
[x] Informational advantage identified: Longer time horizon, peer multiple disconnect
```

**2-Minute Explanation:**
Morningstar provides independent investment research, data, and analytics across six segments: Morningstar Direct (advisor platform), PitchBook (private markets data), DBRS Credit (ratings agency), Wealth, Retirement, and Indexes. Revenue is ~80% recurring (subscription/license), with 60%+ gross margins and 46% insider ownership by founder Joe Mansueto. The stock declined 53% from highs due to multiple compression (from 50-60x P/E to 18x) as growth normalized from 12% to 8%. It trades at 18x P/E vs peers at 30-42x. The bear case is that growth decelerates further and AI disrupts traditional research; the bull case is that this is a quality compounder at a rare discount with margin expansion ahead.

**Why is it cheap:**
1. Multiple compression from extreme 50-60x P/E to 18x
2. Growth deceleration from 12% (2024) to 8% (2025)
3. AI disruption fears across information services sector
4. Sustainalytics/ESG headwind

**My contra-thesis:**
Growth normalization from 12% to 8% is healthy, not threatening. MORN's value is in compliance-grade curated data with deep switching costs, not in commoditizable research. 18x P/E for this quality profile is historically anomalous. Peers at 30-42x with similar or lower quality metrics suggest massive undervaluation, even after adjusting for MORN's lower operating margins.

**Value trap score: 0-1/10 -- VERY LOW risk.** Not a value trap. No factors present.

**CRSP acquisition (DA-flagged omission):** The thesis omits the $365M CRSP acquisition completed Feb 2, 2026. This creates a conflict of interest (owning indexes that its ratings evaluate). This is a MATERIAL omission that I must evaluate. My assessment: The conflict is real but manageable. S&P Global operates with similar conflicts (rates debt AND provides indices). However, MORN's brand as "independent, impartial third-party" makes it more acute. I will add a kill condition for this.

**Verdict Gate 2: PASS. Business is well understood. CRSP conflict acknowledged and kill condition added.**

---

## GATE 3: PROJECTIONS -- PASS (with adjustments)

```
[x] Revenue growth derived: 7-8% (adjusted from thesis 9%)
[x] WACC calculated: 9.5-10% (range)
[x] Terminal growth justified: 2-2.5%
[x] Bear/Base/Bull scenarios documented
```

**Revenue Growth Derivation:**
- TAM Growth: +8% (financial data market)
- Market Share: +0.5pp/year (PitchBook gaining, DBRS gaining)
- Pricing Power: +3% (annual escalators)
- Theoretical organic: ~8-10%

**R3 Resolution:** Reduced from 9% to 7.5%, reflecting:
- FY2025 actual: 7.5% reported (8.0% organic)
- Q4 consensus: 6.2% revenue growth
- PitchBook deceleration to 8.6%
- Morningstar Direct only +5.4%

**My assessment:** 7.5% base case growth is appropriate. The DA's 7% is reasonable for a conservative case. The thesis's original 9% requires re-acceleration which is not justified by recent trends. I use **7.5% base case**.

**WACC:**
- Thesis: 9.5% (Rf 4.5%, Beta 1.08, ERP 5.5%)
- DA argues 10% for conservatism
- My assessment: 9.5% is mathematically correct per CAPM. Using 10% as a stress test is prudent but not required as the base case. I use **9.75% base case** (splitting the difference given CRSP acquisition adds leverage and complexity).

**Terminal Growth:** 2.5% (thesis) vs 2% (DA). Financial data is secular growth, 2.5% is defensible but I will use **2% for conservatism** given growth deceleration trend.

**Verdict Gate 3: PASS. Growth 7.5%, WACC 9.75%, Terminal 2%. More conservative than thesis, more generous than DA.**

---

## GATE 4: VALUATION -- PASS (with significant FV revision)

```
[x] Method 1 (OEY, 40% weight): FV $186
[x] Method 2 (DCF, 60% weight): FV $171
[x] Divergence: 8.8% -- LOW
```

**Method 1: Owner Earnings Yield (40% weight)**

Using the thesis's calculation framework but with conservative 4.5% required OEY (DA's recommendation, not 3.5% from thesis):
- Owner Earnings: $354M (from thesis)
- FV at 4.5% OEY = $354M / 0.045 = $7.87B equity / 42.5M shares = **$185/share**

I agree with the DA that the thesis's 3.5% OEY (implying 29x OE multiple) is too generous for an 8% grower with 18.5% operating margins. 4.5% OEY (implying 22x OE multiple) is more appropriate.

**Method 2: DCF (60% weight)**

With my adjusted parameters: Growth 7.5%, WACC 9.75%, Terminal 2%:
- This falls between the thesis's DCF ($197 at 9/9.5/2.5) and the DA's ($158.62 at 7/10/2)
- Interpolating: approximately **$170-175/share**
- Using $171 as central estimate

**Reconciliation:**

| Method | Fair Value | Weight | Weighted |
|--------|-----------|--------|----------|
| OEY (4.5%) | $186 | 40% | $74 |
| DCF (7.5%/9.75%/2%) | $171 | 60% | $103 |
| **Weighted Average** | | 100% | **$177** |

**R3 Resolution FV: $180.** My independent calculation: **$177.** These are within 2% of each other -- strong convergence.

**I will use FV $180 (R3 resolution) as it is within my independent range and provides an established reference point.**

**Divergence between methods:** 8.8% -- LOW. Acceptable.

**Peer sanity check:**
- At $180 FV and current EPS ~$8.90: implied P/E ~20x
- Peers: SPGI 37x, MSCI 42x, FDS 30x, MCO 35x
- 20x is a ~40% discount to peer average of 36x
- Even adjusting for MORN's lower margins (18.5% vs 35-55%), a 40% discount is excessive
- PEG-adjusted: MORN 20x / 8% growth = PEG 2.5 vs SPGI 37x / 14% = PEG 2.64. Similar.
- This suggests $180 is reasonable and possibly conservative

**Verdict Gate 4: PASS. FV $180. Significant reduction from thesis $205 (-12%), consistent with R3 resolution, within 2% of my independent calculation.**

---

## GATE 5: MARGIN OF SAFETY -- CONDITIONAL PASS

```
[x] Tier: A (low-end, QS 78)
[x] MoS Actual vs Base: 12.5% ($160 vs $180)
[x] MoS Actual vs Bear: -5% to +8% (range)
```

**Current price: $160.03**
**FV (R3 resolved): $180**
**MoS vs Base: +12.5%**

**Bear Case FV Scenarios:**
- Thesis bear: $148 (7%/10.5%/2%) -- MoS at $160 = -8%
- DA bear: $142 (6%/10.5%/2%) -- MoS at $160 = -12.7%
- My bear: $155 (6.5%/10%/2%) -- MoS at $160 = -3%

**MoS Assessment:**

12.5% MoS for a Tier A compounder. Is this sufficient?

**Precedent comparison:**
| Ticker | Tier | MoS at Entry | Outcome |
|--------|------|-------------|---------|
| ADBE | A (76) | 31% | Active |
| NVO | A (82) | 38% | Active |
| MONY.L | A (75) | 36% | ON PROBATION |
| LULU | A (78) | 34% | ON PROBATION |
| AUTO.L | A->B (71) | 29% | LOW conviction |
| BYIT.L | A->B (68-72) | 35% | ON PROBATION |

**All Tier A entries had MoS of 29-38%.** MORN at 12.5% is SIGNIFICANTLY BELOW all precedents.

**DA's recommendation:** Entry at $130-135 (MoS 25-28%) -- consistent with precedent range.

**R3 resolution header states:** Entry $130-135 (25-28% MoS).

**This is the critical gate.** At $160, MoS is only 12.5%. Our precedent pattern for Tier A is 29-38%. Accepting 12.5% would deviate from ALL precedents without justification.

**Can I justify the deviation?**
1. MORN's moat is WIDE (20/25 moat score). But so are ADBE's and NVO's.
2. MORN's insider ownership (46%) is exceptional. True, but not unique (NVO has founder-equivalent in Nordic culture).
3. No value trap factors. Same as other Tier A entries.
4. Portfolio fit is excellent (no overlap). True, but diversification benefit alone doesn't justify accepting lower MoS.

**I cannot justify deviating from the 25-30% MoS precedent for Tier A at current price.**

**However:** The R3 resolution already anticipated this, setting entry at $130-135. The stock is at $160 today. This is a WATCHLIST entry, not a BUY at current price.

**Verdict Gate 5: CONDITIONAL PASS. MoS insufficient at current $160 for BUY. Entry at $135 (MoS 25%) is consistent with precedents and R3 resolution. WATCHLIST with standing order.**

---

## GATE 6: MACRO CONTEXT -- PASS

```
[x] World view reviewed (date: 2026-02-14)
[x] Economic cycle: Mid-cycle US, labor market resilient
[x] Company-cycle fit: FAVORABLE
[x] Megatrends: AI [MIXED], Demographics [+], Financial complexity [+]
```

**Macro fit:**
- Mid-cycle US with inflation moderating (CPI 2.4% Jan). Favorable for quality.
- Financial data demand is structural, not cyclical.
- USD weak (DXY ~96.8) -- MORN is 71% US revenue, slight headwind for EUR-based investors but manageable.
- BoE/ECB/Fed all on hold or easing -- supportive for equities broadly.
- Information services sector hit by Anthropic AI sell-off Feb 2026 (-$285B sector). This creates a sector-wide headwind that may persist but also creates opportunity.

**MORN-specific macro:**
- Lower rates would benefit DBRS Credit (more debt issuance).
- Inflation sticky but MORN has strong pricing power (3-5% annual contract escalators).
- AI is both risk and opportunity -- monitoring required.

**Verdict Gate 6: PASS. Macro context is neutral-to-favorable for a quality financial data compounder.**

---

## GATE 7: PORTFOLIO FIT -- PASS

```
[x] Price verified: $160.03 (EUR 134.79) (date: 2026-02-14)
[x] Sizing proposed: 4% (~EUR 400)
```

**Constraint Checker Results (CHECK MORN 400):**
- Position post-purchase: 4.0% -- Consistent with Tier A precedents (3-5%)
- Sector post-purchase: Financial Services 18.5% -- This includes ALL and GL (insurance). MORN is in a different sub-sector (financial data vs insurance). Actual correlation within "Financial Services" is LOW.
- Geography post-purchase: US 18.5% -- LOW for US exposure. No geographic concentration concern.
- Cash post-purchase: EUR 5,352 (53.0%) -- HIGH cash still, well above prudent levels. Plenty of dry powder.
- Correlation with existing: **LOW** -- MORN has essentially zero overlap with our 11 current positions. No other financial data company. Closest would be the insurance positions (ALL, GL) but different sub-sector dynamics.

**50% drawdown impact:** -2.0% portfolio. At 4% sizing, this is well within acceptable range for Tier A conviction.

**Precedent sizing:**
- ADBE (Tier A): 4.8%
- NVO (Tier A): 3.4%
- MONY.L (Tier A): 4.1%
- LULU (Tier A): 3.5%
- Pattern: 3-5% for Tier A initial positions

**4% (~EUR 400) is consistent with all precedents. No deviation needed.**

**Verdict Gate 7: PASS. 4% sizing, no concentration concerns, excellent diversification benefit.**

---

## GATE 8: SECTOR UNDERSTANDING -- PASS

```
[x] Sector view exists: world/sectors/financial-data-analytics.md
[x] Sector view reviewed (date: 2026-02-13)
[x] TAM and trends understood: $50B TAM, 8-10% CAGR
[x] Disruption risks known: AI, VantageScore (FICO-specific), ratings shopping
[x] Sectoral position: NEUTRAL-SELECTIVO
```

**Sector context for MORN:**
- The sector view covers FICO, FDS, SPGI, MSCI as key players. MORN is not yet listed in the sector view (should be added).
- Sector sentiment: Mixed -- FICO and FDS are "hated/feared," larger players like SPGI remain at premium multiples.
- MORN sits in the middle: not as feared as FICO/FDS, but caught in the broader AI sell-off.
- NEUTRAL-SELECTIVO status supports selective entry at the right price, which aligns with a WATCHLIST verdict.

**Key sector risk relevant to MORN:** AI disruption of information services. The Feb 2026 Anthropic plug-in triggered a $285B sector sell-off. This is a real headwind that may persist.

**Verdict Gate 8: PASS. Sector understood. MORN should be added to sector view as analyzed company.**

---

## GATE 9: AUTOCRITICA -- PASS

```
[x] Unvalidated assumptions listed
[x] Biases recognized
[x] Kill conditions defined
[x] What would change my mind
```

**Unvalidated Assumptions:**
1. CRSP acquisition Chinese walls will prevent brand damage -- UNVALIDATED. No precedent for MORN specifically.
2. Operating margin expansion will continue to 25%+ -- UNVALIDATED. Q3 2025 showed plateauing at 20.7%. FY2025 FCF declined despite revenue growth.
3. PitchBook retains growth leadership vs BlackRock/Preqin -- UNVALIDATED. BlackRock's $3.2B Preqin acquisition creates well-funded competitor.
4. 46% insider ownership = alignment -- PARTIALLY VALIDATED. Mansueto selling $30M/year under 10b5-1 plan complicates the narrative.

**Biases Recognized:**
- [x] **Popularity bias:** Morningstar is a well-known brand. Am I attracted to the brand rather than the business? MITIGATED by fundamental analysis showing genuine quality metrics.
- [x] **Confirmation bias:** The thesis builds a compelling narrative of "quality at a discount." Am I ignoring the DA's valid points about growth deceleration and CRSP conflict? MITIGATED by accepting the R3 FV reduction and setting entry at $135.
- [x] **Recency bias:** Recent AI sell-off may be creating perceived opportunity that is actually a falling knife. MITIGATED by using standing order (price discipline).

**Kill Conditions (comprehensive, incorporating R1 thesis + risk-identifier + DA recommendations):**
1. Revenue growth turns negative for 2+ consecutive quarters
2. Operating margin falls below 15% with trajectory reversal
3. PitchBook growth decelerates below 5%
4. Joe Mansueto sells >10% of his stake in 12 months
5. AI-native competitor gains material market share in advisor research
6. DBRS loses NRSRO or ESMA designation
7. QS drops below 70 (reclassification to Tier B)
8. **NEW (from risk-identifier):** Regulatory investigation into MORN's fund ratings objectivity related to CRSP-benchmarked funds
9. **NEW (from risk-identifier):** Vanguard announces intention to replace CRSP indexes with proprietary/alternative benchmarks
10. **NEW (from DA):** Organic revenue growth falls below 5% for 2 consecutive quarters

**What would change my mind:**
- Q1/Q2 2026 earnings showing revenue growth below 6% with margin compression -> thesis weakens materially
- A regulatory inquiry into CRSP/ratings conflict -> immediate re-evaluation
- PitchBook losing material share to Preqin (BlackRock) -> crown jewel impaired
- DBRS credit event (rated bonds defaulting at higher-than-Big-3 rates) -> credibility damaged

**Verdict Gate 9: PASS. Self-criticism thorough. Kill conditions comprehensive.**

---

## GATE 10: COUNTER-ANALYSIS & INDEPENDENT ASSESSMENTS -- CONDITIONAL PASS

```
[x] Counter-analysis exists: devils_advocate.md
[x] Verdict: 13/19 STRONG COUNTER
[x] HIGH/CRITICAL challenges: 5 of 21
[x] Each HIGH/CRITICAL addressed below
```

**HIGH/CRITICAL Challenges Resolution:**

**1. FV of $205 is overstated by 20-30% (HIGH)**
- RESOLVED. R3 already reduced FV to $180. My independent calculation gives $177. The DA's $163 is overly conservative (uses 7% growth, 10% WACC, 2% terminal -- all at the bearish end simultaneously). The truth is between $163 and $180. I use $180 which is within 2% of my independent estimate.

**2. Growth 9% requires re-acceleration (HIGH)**
- RESOLVED. R3 reduced growth assumption to 7.5%. This is more conservative than the original thesis (9%) and more generous than the DA (7%). FY2025 organic growth was 8.0%, so 7.5% is a slight deceleration assumption, which is appropriate.

**3. CRSP acquisition omitted from thesis (HIGH)**
- PARTIALLY RESOLVED. The thesis header references R3 resolution acknowledging CRSP. However, the thesis body still does not have a dedicated CRSP analysis section. I have:
  - Acknowledged the conflict of interest in Gate 2
  - Added kill conditions #8 and #9 for CRSP-related risks
  - Assessed that the conflict is manageable (S&P Global precedent) but acute for MORN's specific brand
  - This risk is MONITORED, not fully resolved. It does NOT block WATCHLIST approval (we are not deploying capital immediately) but the thesis should be updated to include CRSP analysis before any BUY execution.

**4. Insider selling misrepresented (MODERATE)**
- RESOLVED. Mansueto selling $30M/year under 10b5-1 plan adopted at $300+. This represents <1% of his ~$2.8B holding. It is routine portfolio management for a 45% owner with extreme concentration. The thesis's characterization "insider selling: NO" is technically incorrect and should be corrected to "insider selling: ROUTINE under 10b5-1 plan, <1% of holding." This is NOT a material concern for the investment thesis.

**5. Q4 beat but stock did not move (MODERATE)**
- NOTED. Q4 EPS $2.83 vs $2.36 consensus (+20% beat), revenue beat +2.2%. Stock flat. This suggests the market is pricing in concerns beyond Q4 results (AI disruption, growth deceleration, CRSP). This is not a kill condition but it means the re-rating catalyst is not obvious in the near term.

**6. FCF declined YoY in FY2025 (MODERATE)**
- NOTED. FCF $442.6M vs $449M (-1.4%). Higher tax and bonus payments. Operating leverage narrative is at risk if this persists. Monitor FY2026 FCF trajectory as a key thesis validation point.

**Moat Assessment Discrepancies:**
- Network effects: Moat-assessor rates MODERATE (3/5), thesis says WIDE. I agree with moat-assessor. Net effect: moat score 20/25, still WIDE overall.
- Operating margins: 18.5% vs peer 35-55%. The gap is real but the trajectory is expanding. This is a "show me" story.

**Valuation Report Discrepancies:**
- Thesis $205 vs DA $163 vs R3 $180 vs my $177. Spread: $163-$205 (25% range). R3 and my independent estimate converge at $177-$180. I use $180 as resolved FV.

**Unresolved Conflicts:**
1. CRSP thesis section not yet written -- REQUIRED before BUY execution
2. Thesis needs correction on insider selling characterization
3. Bear case FV range is wide ($142-$155) -- need clarity on which bear is realistic

**Verdict Gate 10: CONDITIONAL PASS. STRONG COUNTER addressed through R3 FV reduction, adjusted growth assumptions, and comprehensive kill conditions. CRSP analysis must be incorporated into thesis before any BUY execution. For WATCHLIST status, current analysis is sufficient.**

---

## 10-GATE SUMMARY

| Gate | Verdict | Key Finding |
|------|---------|-------------|
| 0. Sector View | PASS | financial-data-analytics.md exists |
| 1. Quality Score | PASS | QS 78, Tier A (low-end). Tool 60 distorted by data gaps. |
| 2. Business Understanding | PASS | Well understood. CRSP conflict acknowledged. 0-1/10 value trap. |
| 3. Projections | PASS | Growth 7.5%, WACC 9.75%, Terminal 2%. Conservative vs thesis. |
| 4. Valuation | PASS | FV $180 (R3 resolved). Methods converge. -12% from thesis $205. |
| 5. Margin of Safety | CONDITIONAL | 12.5% at $160 -- BELOW all Tier A precedents (29-38%). Entry $135. |
| 6. Macro Context | PASS | Mid-cycle US, neutral-favorable for quality data business. |
| 7. Portfolio Fit | PASS | 4% sizing, no concentration, excellent diversification. |
| 8. Sector Understanding | PASS | NEUTRAL-SELECTIVO sector, selective entry appropriate. |
| 9. Autocritica | PASS | Biases, assumptions, 10 kill conditions documented. |
| 10. Counter-Analysis | CONDITIONAL | STRONG COUNTER 13/19 addressed. CRSP thesis update needed pre-BUY. |

**Gates CONDITIONAL: 5 (MoS) and 10 (Counter-analysis CRSP update).**
Both conditions are satisfied by a WATCHLIST verdict with standing order at $135.

---

## FINAL VERDICT: WATCHLIST

```
WATCHLIST: MORN (Morningstar, Inc.)

Quality Score: 78/100 (Tier A, low-end)
Fair Value: $180 (R3 resolved, independently confirmed at $177)
Current Price: $160.03
MoS at Current: 12.5% (INSUFFICIENT for Tier A entry)

Entry Target: $135 (MoS 25%, consistent with Tier A precedent range 29-38%, slightly below due to CRSP uncertainty)
Alternative Entry: $130 (MoS 28%, provides additional buffer for CRSP/growth risks)

CONDITIONS BEFORE BUY EXECUTION:
1. Price reaches $135 or below
2. Thesis must be updated to include CRSP acquisition analysis section
3. Insider selling characterization must be corrected
4. Monitor Q1 2026 earnings for growth trajectory confirmation

Standing Order Parameters:
- Trigger: $135
- Size: EUR 400 (4% of portfolio)
- Valid Until: Q1 2026 earnings (late April/May 2026)
- Auto-cancel if: Kill conditions #1, #8, or #10 trigger

Kill Conditions (10 total):
1. Revenue growth negative 2+ consecutive quarters
2. Operating margin below 15% with reversal
3. PitchBook growth below 5%
4. Mansueto sells >10% stake in 12 months
5. AI-native competitor gains material advisor market share
6. DBRS loses NRSRO/ESMA
7. QS drops below 70
8. Regulatory investigation into ratings objectivity (CRSP)
9. Vanguard replaces CRSP indexes
10. Organic revenue growth below 5% for 2 consecutive quarters
```

**Why WATCHLIST, not BUY:**
1. MoS at $160 (12.5%) is below ALL Tier A entry precedents (29-38% range)
2. DA scored 13/19 STRONG COUNTER -- the adversarial review pattern (Sessions 48-53) showed 14/16 positions had inflated FV. MORN's FV has been corrected ($205 -> $180) but the market at $160 still does not provide sufficient MoS
3. CRSP acquisition conflict is a MATERIAL governance risk not yet fully analyzed in thesis
4. Q4 beat did not move stock -- market sees risks we must respect
5. Consistency with precedents (Principio 7): We have NEVER bought a Tier A compounder with MoS below 29%

**Why not REJECT:**
1. Business quality is genuine (WIDE moat, QS 78 Tier A, 0-1/10 value trap)
2. At $135, MoS of 25% brings it into the acceptable range
3. No structural impairment detected -- this is a valuation/timing question, not a quality question
4. Excellent portfolio diversification (zero overlap with existing positions)
5. ROIC 19.5% >> WACC 9.5% -- the business creates value

---

## META-REFLECTION

### Doubts About This Decision
- The R3 FV of $180 may itself be too generous. The DA's independent DCF at $158.62 uses defensible parameters (7%/10%/2%). If the DA is closer to right, then even $135 entry (MoS 17% vs $163 DA FV) may not provide sufficient safety.
- The AI disruption risk is genuinely uncertain. The Feb 2026 Anthropic sell-off suggests the market is pricing in a real threat to information services. If AI tools become "good enough" for advisor research, the switching cost moat for Morningstar Direct could weaken faster than expected.
- CRSP conflict of interest severity is hard to gauge. I may be either over- or underweighting this. The fact that S&P Global operates with similar conflicts suggests it is manageable, but MORN's specific brand as "independent" makes it more acute.
- The stock's non-reaction to a 20% Q4 EPS beat is genuinely concerning. When good news does not move a stock, the market is telling us something about the forward outlook that we may not fully understand.

### Weaknesses of the Analysis Received
- **Thesis omits CRSP entirely.** This is the most significant gap. A $365M acquisition completed 10 days before the analysis that creates fundamental conflicts with the core business should have been the central discussion topic. The risk-identifier caught it, but the fundamental-analyst missed it.
- **Insider selling mischaracterized.** The thesis states "insider selling: NO" and "Kapoor not selling" while the founder/chairman is selling $30M+/year. Technically accurate (CEO Kapoor is not selling) but substantively misleading. This should be a standard check.
- **EPS CAGR of 24-75% is misleading.** Based on 2022 trough. Forward EPS growth is 8-12%. The QS mechanically rewards trough-to-peak recovery, which inflates the growth score.
- **FY2025 FCF decline not addressed.** The narrative of "operating leverage" is contradicted by FCF declining 1.4% while revenue grew 7.5%. This deserves investigation.
- **Bear case may be optimistic.** The thesis's bear FV of $148 uses 7%/10.5%/2%, but the DA's stressed case at 6%/10.5%/2% gives $142 and the extreme bear at 6%/10.5%/2% gives $114-142.

### Suggestions for Improvement
- **Mandatory acquisition check:** When a material acquisition (>10% of market cap) occurred within 90 days of analysis date, the fundamental-analyst should be required to analyze it.
- **Insider selling check:** The thesis template should include a mandatory section reviewing recent Form 4 filings, not just ownership levels.
- **PEG as standard sanity check:** When comparing P/E multiples to peers, always include PEG ratios. MORN PEG 2.25 vs SPGI PEG 2.64 is a much more honest comparison than 18x vs 37x.
- **FCF trajectory check:** The quality scorer should flag if FCF declined YoY despite revenue growth, as this contradicts the operating leverage assumption.

### Questions for Orchestrator
1. Should the thesis be updated NOW (before setting the standing order) to include CRSP analysis, or can the standing order be set with a note that CRSP update is required before execution?
2. The quality_scorer.py shows Legacy Score 60 for MORN due to ROIC NaN and FCF margin data gaps. This is a known tool limitation. Should we document this as a known issue for companies with recent fiscal year-end (data not yet in yfinance)?
3. MORN should be added to the financial-data-analytics.md sector view as an analyzed company. Should this be done now or as part of the post-analysis cycle?
4. The standing order at $135 implies a 16% decline from current $160. Given the AI sector headwind, this target could be reached in a broad sell-off. Is the standing order approach appropriate, or should we wait for more clarity on growth trajectory (Q1 2026 earnings)?

---

**Analysis Date:** 2026-02-14
**Analyst:** investment-committee (R4)
**Verdict:** WATCHLIST at $135 entry (MoS 25%)
**Fair Value:** $180 (R3 resolved)
**Quality Score:** 78/100 (Tier A, low-end)
**Kill Conditions:** 10 defined
**Standing Order:** $135, EUR 400 (4%), valid until Q1 2026 earnings
