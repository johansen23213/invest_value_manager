# Investment Committee Decision: IHP.L (IntegraFin Holdings PLC)

> Date: 2026-02-20
> Committee: investment-committee (opus)
> Decision Type: WATCHLIST + Standing Order Approval
> Pipeline: R1 (thesis) -> R2 (MODERATE COUNTER) -> R3 (resolution) -> R4 (this document)

---

## GATE 0: Sector View Exists -- PASS

Sector view verified: `world/sectors/uk-adviser-platforms.md` (created 2026-02-20).
Sector status: SELECTIVO. Revenue margin compression is dominant headwind. Proprietary tech platforms preferred.

---

## PASO 0.5: Precedentes Consultados

### Most Similar Precedents

**Precedent 1: MONY.L (BUY, 2026-02-04)**
- Tier A (QS 81), MoS 36%, sizing 4.1%, UK financial services platform
- Outcome: Still held, ON PROBATION (-12% P&L). Earnings Feb 23 make-or-break.
- Relevance: HIGHEST -- same geography (UK), same sector (financial services platform), same Tier. MONY.L was bought at 4.1% despite already having UK positions. However, at that time MONY.L was the 2nd UK position, not the 5th.
- Key difference: IHP.L would be 5th UK position (vs MONY.L was 2nd). This INCREASES the geographic concentration argument significantly.

**Precedent 2: MMC (Standing Order, 2026-02-14)**
- Tier B (QS 68), MoS 18.4%, sizing 2% HALF POSITION, standing order at $155
- Outcome: Pending (standing order not yet triggered)
- Relevance: HIGH -- establishes HALF POSITION (2%) sizing for situations with elevated binary risk. MMC used half-position for Greensill litigation; IHP.L would use small sizing for UK concentration risk.
- Deviation: MMC was half-position due to binary legal event. IHP.L 2% is for geographic concentration -- a different risk type but same sizing principle (limit exposure when incremental risk is elevated).

**Precedent 3: BYIT.L (BUY, 2026-02-06)**
- Tier A (QS 81), MoS 35%, sizing 3.5%, UK technology
- Outcome: Still held, ON PROBATION (-2% P&L). QS since downgraded to 68-72 (Tier B).
- Relevance: MODERATE -- another UK Tier A that was subsequently downgraded. Shows that UK fallen angels can lose their Tier A status post-adversarial.

**Deviation from precedents:**
- Tier A BUYs have all been 3-5% sizing. IHP.L at 2% is BELOW this range.
- Justification: 5th UK position creates genuine incremental geographic concentration. The 2% cap is DELIBERATE risk management, not lack of conviction in the business. If UK positions were reduced to 3 or fewer, sizing would naturally increase to 3-4%.
- The MMC half-position precedent (2%) provides the closest sizing analogy, though for a different risk type.

---

## 10-Gate Assessment

### Gate 1: Quality Score -- PASS

```
[X] Quality Score calculated: 78-80/100
    QS Tool: 78 (with FCF proxy for distorted financial services data)
    R1 QS: 80 (manual verification of FCF distortion)
    Difference: 2 points, within tolerance. No adjustment warranted.
[X] Tier: A (Quality Compounder)
[X] Tier D check: NOT Tier D -- proceed
[X] Quality Score verified with quality_scorer.py (run 2026-02-20)
```

**Notes on QS data quality:**
- FCF margin >200% is a data artifact (client money flows in yfinance for financial services). The tool correctly flags this and uses operating margin as proxy.
- ROIC trajectory shows wild swings (25% -> 69% -> 142% -> 49%) also due to financial services accounting. The ROE trajectory (25% -> 26% -> 25% -> 23%) is more reliable and stable.
- Financial Quality 38/40 (not 40/40 due to FCF proxy): still exceptional.
- Capital Allocation 10/10: 24.2% insider ownership is the highest in our portfolio and among the highest in FTSE250.

**Tier A qualification per Principio 9 (Quality Gravitation):** YES. IHP.L at QS 78-80 is genuinely Tier A. ROIC consistently >> WACC, proprietary technology moat, highest insider ownership in sector, near-zero value trap risk (0/10). This is the type of business the portfolio gravitates toward.

---

### Gate 2: Business Understanding -- PASS

```
[X] Business Analysis Framework completed (R1 thesis.md)
[X] Can explain in 2 minutes:
    IntegraFin operates Transact, the UK's #1 independent adviser investment platform.
    Revenue comes from basis points charged on GBP 77bn FUA (assets under admin).
    It's a toll-road model: every pound on the platform generates daily revenue.
    95% client retention, proprietary technology (not outsourced FNZ), 97.8% gross margins.
    The bear case is revenue margin compression (25bps -> 22bps over 4 years).
    My thesis: volume growth (FUA +12-15%/yr) outpaces margin compression (~1bps/yr).
[X] Know WHY it's cheap + counter-thesis:
    - Cheap because: Revenue margin compression fears + BofA Underperform + analyst downgrades
    - Counter-thesis: Compression is decelerating per management + operating leverage (costs +3% vs revenue +8%)
    - BofA projects flat ROIC 22% -- but uses different capital basis than our tool (49% ROIC)
[X] Value trap checklist: 0/10 SI (ZERO risk factors)
[X] Informational edge: Horizon (market anchors on quarterly bps, I see 3-5yr operating leverage)
```

---

### Gate 3: Projections -- PASS

```
[X] Revenue growth derived from business logic:
    FUA Growth: Market returns (~6-8%) + Net inflows (~5-7%) = ~12-15% FUA growth
    Revenue margin compression: ~0.5-1.0 bps/yr (decelerating per management)
    Net revenue growth: ~8-10%
[X] WACC calculated:
    Ke = 4.0% (Rf) + 1.2 (adjusted beta) x 5.5% (ERP) = 10.6%
    Net cash position -> WACC = Ke = 10.6%
    Conservative WACC: 10.5%
    NOTE: Beta 1.47 from yfinance adjusted to 1.2 -- reasonable for stable platform business with 95% retention
[X] Terminal growth: 2.5% (below GDP, appropriate for mature platform)
[X] Scenarios documented:
    Bear: FV 310p (accelerated compression to 19bps + slower FUA growth)
    Base: FV 390p (R3 adjusted from 415p)
    Bull: FV 510p (FUA acceleration + margin stabilization)
```

---

### Gate 4: Multi-Method Valuation -- PASS

```
[X] Method appropriate for Tier A:
    - Primary: Owner Earnings Yield + P/E forward (Tier A method)
    - Secondary: EV/EBIT normalized
    - NOTE: Standard DCF REJECTED as unreliable for IHP.L (financial services FCF distortion)

[X] Method 1 (60%): P/E on FY26E EPS
    Multiple: 18-20x (R3 adjusted from R1's 20-22x)
    FY26E EPS: 19.9p
    FV: 358-398p, midpoint 378p

[X] Method 2 (40%): EV/EBIT normalized
    EBIT: ~GBP 78M normalized
    Multiple: 16-17x
    Surplus cash: GBP 34M (only distributable, not full GBP 255M)
    FV: 400-410p

[X] Weighted FV: 390p (60% x 378p + 40% x 400p)
    R1 FV was 415p; R3 adjusted to 390p (-6%) accepting DA challenges on multiple
    Divergence between methods: ~6% -- within acceptable range

[X] Sensitivity:
    If compression to 19bps by FY28: FV ~365p
    If costs +5% (not 3%): FV ~380p
    If FTSE -20%: temporary FV 209-250p (market sensitivity of bps-on-AUM model)
```

---

### Gate 5: Margin of Safety -- PASS (with nuance)

```
[X] Tier: A (QS 78-80)
[X] MoS at current 319p vs FV 390p: 18.2%
[X] MoS at entry 300p vs FV 390p: 23.1%
[X] MoS at entry 300p vs Bear 310p: 3.2%
```

**Reasoning (not mechanical):**

The standing order entry is 300p, not the current 319p. At 300p:

- MoS vs Base 23.1%: This EXCEEDS the typical Tier A range of 10-15% per precedents. It is below the exceptional entries we made in Feb 2026 (NVO 38%, MONY.L 36%, BYIT.L 35%) but those were at 52-week lows during a broad sell-off. IHP.L at 300p would be 14% above its 52-week low of 263p -- not a distressed entry.

- MoS vs Bear 3.2%: This is thin. The bear case (310p) is only 10p above entry. However, the bear case incorporates accelerated margin compression AND slower FUA growth simultaneously. The probability of BOTH occurring is lower than either individually.

- E[CAGR_3yr] at 300p: 12.8% (exceeds 12% Tier A threshold per framework). Includes dividend yield of 3.6%.

**Precedent comparison:**
- ADBE: 31% MoS, Tier A, 4.8% sizing
- MONY.L: 36% MoS, Tier A, 4.1% sizing
- NVO: 38% MoS, Tier A, 3.4% sizing
- IHP.L: 23.1% MoS at 300p entry, Tier A, 2% sizing

IHP.L MoS is LOWER than all previous Tier A BUYs. This is acknowledged and compensated by:
1. Smaller sizing (2% vs 3-5%) -- deliberate
2. Standing order (not market buy) -- provides price discipline
3. Market context: Feb 2026 entries were during broad-based sell-off creating exceptional MoS. IHP.L at 300p is a 5% pullback from current, not a crisis entry.

**Am I deviating from precedents?** YES -- lower MoS than historical Tier A BUYs. Justified because: (a) sizing is deliberately smaller (2%), (b) IHP.L's specific risk profile (0/10 value trap, net cash, 24% insider ownership, 95% retention) is among the lowest-risk in our Tier A universe, (c) the standing order at 300p provides additional discipline vs a market buy at 319p.

---

### Gate 6: Macro Context -- PASS

```
[X] World view reviewed (date: 2026-02-18)
[X] Economic cycle: Mid-cycle (US), UK weak but BoE cuts expected H1 2026
[X] Fit:
    - IHP.L is financial infrastructure, NOT consumer discretionary
    - Revenue depends on FUA levels (equity market sensitive) -- UK equity market near highs = SUPPORTIVE
    - BoE rate cuts expected H1 2026 = POSITIVE for UK equities and sentiment
    - UK consumer weakness is LESS relevant -- advisers serve wealth management clients, not mass-market
[X] Megatendencies:
    - Demographics aging: POSITIVE (more wealth needing advice, pension freedoms)
    - AI disruption: LOW risk (financial advice is relationship-driven; 5-10yr horizon at most)
    - Desglobalization: NEUTRAL (purely domestic UK business)
```

**UK macro risk for IHP.L specifically:**
The world view notes UK consumer weakness (disposable income growth 0.25%, 27% plan to spend less). However, IHP.L's clients are wealthy individuals using financial advisers -- not the mass-market consumer. Average portfolio on Transact is GBP 314K. This demographic is resilient to consumer downturns. The main UK macro risk to IHP.L is via equity market levels (FUA drops if FTSE drops), not consumer spending.

---

### Gate 7: Portfolio Fit -- CRITICAL GATE -- PASS WITH CONDITIONS

```
[X] Price verified: 319p (2026-02-20) via price_checker.py
[X] Sizing proposed: 2% (~EUR 200)
[X] constraint_checker.py executed: CHECK IHP.L 200
```

**Post-purchase portfolio state:**

| Metric | Current | After IHP.L | Assessment |
|--------|---------|-------------|------------|
| Position size | N/A | 2.0% | Smallest in portfolio. If falls 50%, impact = -1.0% |
| UK positions | 4 (14.6%) | 5 (16.5%) | 5 of 11 positions UK. 50% by count but only 16.5% by capital |
| Financial Services | 11.0% | 13.0% | MONY.L + GL + EDEN.PA + IHP.L. Different subsectors |
| Cash after | 60.5% | 58.6% | Minimal impact |
| Positions | 10 | 11 | Adequate diversification |

**UK Concentration -- Detailed Reasoning (Principio 2):**

This is the CRITICAL issue for this decision. Let me reason explicitly:

**Current UK positions:**
1. DOM.L (Consumer Cyclical, 4.0%, LOW conviction) -- pizza franchise, UK consumer exposure
2. BYIT.L (Technology, 3.6%, LOW conviction, PROBATION) -- IT resale, UK enterprise spending
3. MONY.L (Financial Services, 3.5%, LOW conviction, PROBATION) -- price comparison, UK consumer
4. AUTO.L (Communication Services, 3.5%, LOW conviction) -- auto classifieds, UK used car market

**IHP.L would add:**
5. IHP.L (Financial Services, 2.0%) -- adviser platform, UK wealth management

**Are these correlated?**
- DOM.L: UK consumer discretionary spending on pizza. LOW correlation with IHP.L.
- BYIT.L: UK enterprise IT budgets. LOW correlation with IHP.L.
- MONY.L: UK household insurance/finance comparison. MODERATE correlation (both financial services, but different customers -- MONY serves mass-market consumers, IHP serves financial advisers managing wealthy clients).
- AUTO.L: UK used car transactions. LOW correlation with IHP.L.

The COMMON risk factor is GBP. A 10% GBP depreciation would reduce all 5 UK positions by ~10% in EUR terms. At combined 16.5% UK allocation post-IHP.L, a -10% GBP move = -1.65% portfolio impact. This is manageable.

The COMMON economic risk is a UK recession. But IHP.L's revenue is driven by FUA levels (equity markets), not consumer spending. In a UK recession, equity markets typically drop 15-25%, which would reduce IHP.L FUA and revenue. However, the platform still earns bps on remaining FUA -- it doesn't go to zero. And the cost base is largely fixed, so operating leverage works in reverse temporarily.

**Why no non-UK alternative?**
- Australian adviser platforms (Netwealth NWL.AX, Hub24 HUB.AX): Not tradable on eToro
- AJ Bell (AJB.L): UK-listed anyway, and at 28x P/E vs IHP.L at 19.9x
- US wealth platforms (Schwab, Fidelity): Different business model (vertically integrated, not B2B adviser platform)
- No direct non-UK comparable exists. The question is: deploy EUR 200 to IHP.L or keep as cash?

**My reasoning:**
- 2% sizing (smallest possible) limits incremental UK risk
- IHP.L is in a DIFFERENT subsector from all 4 existing UK positions
- UK allocation would be 16.5% by capital (not 50% -- the count metric overstates the concentration)
- Several existing UK positions (MONY.L, BYIT.L) are on PROBATION and may be rotated out, naturally reducing UK concentration
- The marginal GBP risk of EUR 200 is ~EUR 20 in a -10% GBP scenario -- negligible

**VERDICT on UK concentration:** ACCEPTABLE at 2% sizing. The business quality (QS 78-80, ROIC 49%, 0/10 value trap, 24% insider ownership) justifies the position despite geographic concentration. The 2% cap provides adequate protection.

**Precedent sizing comparison:**
- MMC: 2% (half position for Greensill binary risk)
- All other Tier A: 3-5%
- IHP.L at 2% is consistent with the principle of smaller sizing when incremental risk is elevated.

---

### Gate 8: Sector Understanding -- PASS

```
[X] Sector view exists: world/sectors/uk-adviser-platforms.md
[X] Sector view reviewed (date: 2026-02-20 -- same day, fresh)
[X] TAM and trends understood:
    - UK adviser platform TAM: GBP 700-800bn FUA, growing 8-12%/yr
    - Revenue margin compression ~1-2bps/yr structural (industry-wide)
    - Proprietary tech platforms (Transact, AJ Bell) preferred over FNZ-based (Quilter, Abrdn)
[X] Disruption risks known:
    - Revenue margin compression: Alta probability, Medium impact (ongoing)
    - AI replacing advisers: Low-Medium probability, 5-10yr horizon
    - Consolidation (M&A): Medium probability
[X] Sector position: SELECTIVO (not overweight/underweight -- first position in this sector)
```

**Sector view consistency check:**
The sector view rates competition risk at "Media" and margin compression probability at "Alta." The R2 devil's advocate flagged that the thesis dismisses competition risk more aggressively than the sector view supports. R3 resolved this by adjusting FV down to 390p (incorporating more conservative multiple). The committee accepts this resolution.

---

### Gate 9: Self-Critique -- PASS

```
[X] Unvalidated assumptions:
    1. Revenue margin compression will decelerate from ~1bps/yr to ~0.5bps/yr (management guidance only -- no independent verification)
    2. Cost growth at 3%/yr is achievable (FY25 was +9%, step down is ambitious)
    3. FUA growth will sustain ~12%/yr (partially market-dependent, Q1 FY26 net inflows decelerated from +76% to +11%)
    4. Adjusted beta of 1.2 is more appropriate than yfinance's 1.47

[X] Biases recognized:
    [X] Popularity bias: IHP.L came from systematic screening (quality_universe.py), NOT from mind-recall. MITIGATED.
    [X] Confirmation bias: The R2 devil's advocate challenged the thesis and found it MODERATE COUNTER. 8 challenges MODERATE or above. FV was adjusted down 6%. MITIGATED through adversarial pipeline.
    [X] Recency bias: Recent UK position additions (4 positions in Jan-Feb) create a UK concentration pattern. Am I unconsciously drawn to UK stocks? Checking: UK positions came from FTSE250 screening which naturally produces more UK candidates. This is screening availability bias (documented in principles.md P2 note). PARTIALLY MITIGATED by small sizing.
    [X] UK screening bias: FTSE250 produces more "fallen angel" candidates -- this is documented in decisions_log.yaml lesson from Session 53. The committee acknowledges this bias and notes that IHP.L was flagged through quality_universe.py systematic scoring, not ad-hoc browsing.

[X] Kill conditions defined (7 total):
    KC#1: Revenue margin compression below 20bps AND FUA growth <8% (both required)
    KC#2: Net outflows 2+ consecutive quarters
    KC#3: Insider selling >5% within 12 months
    KC#4: Major regulatory change to ISA/SIPP economics
    KC#5: Management abandons cost discipline (costs >6%/yr)
    KC#6: AI disruption reduces adviser numbers materially (5-10yr monitor)
    KC#7: UK equity market drawdown >25% sustained 6+ months

[X] What would change my mind:
    - H1 FY26 results showing PBT margin NOT expanding (costs growing faster than guided)
    - Revenue margin compression accelerating to 2+bps/yr (not decelerating)
    - Net outflows in any quarter (would signal adviser disengagement)
    - Insiders selling after recent buying spree
```

---

### Gate 10: Counter-Analysis & Independent Assessments -- PASS

```
[X] counter_analysis.md (r2_devils_advocate.md): EXISTS
[X] Verdict: MODERATE COUNTER (17 challenges, 1 HIGH, 8 MODERATE+)
[X] No moat_assessment.md or risk_assessment.md (R1 only produced thesis.md -- noted)

HIGH challenge:
    UK geographic concentration (5th UK position)
    -> RESOLVED: 2% sizing cap + committee approval (this document)

MODERATE+ challenges (8 total):
    1. Revenue margin compression may accelerate -> ACCEPTED, FV adjusted 415->390p
    2. P/E 20-22x too generous -> ACCEPTED, adjusted to 18-20x
    3. BofA 286p Underperform -> ENGAGED, incorporated via lower multiple
    4. FUA market sensitivity (bear market) -> ACKNOWLEDGED, KC#7 added
    5. AJ Bell comp misleading -> ACCEPTED, removed as primary comp
    6. Net inflow deceleration +76%->+11% -> NOTED, already in projections
    7. Costs +3%/yr ambitious -> PARTIALLY ACCEPTED, FV sensitivity is only 5-10p
    8. FV sensitivity to 19bps compression -> INCORPORATED in bear case 310p

[X] No CRITICAL unresolved challenges
[X] Counter-analysis conclusion: Thesis SURVIVES with calibration (FV 415->390p, Bear 340->310p)
```

**BofA Underperform (286p) -- explicit engagement:**
BofA projects flat ROIC of ~22% through FY28 and flows below consensus. Their 286p target implies 14-16x forward P/E. I disagree with BofA's ROIC basis -- they appear to include all regulatory capital, which is required but does not represent invested capital in the traditional sense. Our tool shows ROIC 49% on a standard basis. The ROE trend (25% -> 26% -> 25% -> 23%) is more informative -- stable and well above cost of equity. However, BofA's concern about margin compression is valid and has been incorporated via the FV adjustment to 390p. The 286p target represents an extreme bear scenario that I assign ~15% probability.

---

## VEREDICTO

### APPROVED -- WATCHLIST with Standing Order

**RECOMMENDATION: Add IHP.L to WATCHLIST. Create STANDING ORDER at 300p for EUR 200 (2% portfolio).**

| Parameter | Value |
|-----------|-------|
| Ticker | IHP.L (IntegraFin Holdings PLC / Transact) |
| Quality Score | 78-80/100 (Tier A) |
| Fair Value | 390p (R3 post-adversarial, weighted P/E + EV/EBIT) |
| Bear Case FV | 310p |
| Entry Price (SO) | 300p |
| MoS at Entry | 23.1% vs Base, 3.2% vs Bear |
| E[CAGR_3yr] at Entry | 12.8% (above 12% Tier A threshold) |
| Sizing | 2% (~EUR 200) |
| Category | Quality Compounder (Tier A) |
| Standing Order Category | ACTIVE (5% from current price, reasonable fill probability) |
| Dividend Yield | 3.6% |

**Main Risk:** Revenue margin compression accelerating beyond management guidance, reducing operating leverage thesis.

**Kill Conditions:** 7 defined (KC#1-KC#7, see Gate 9).

**Conditions beyond kill conditions:**
1. PREFERRED (not required): Validate operating leverage thesis with H1 FY26 results (~June 2026) before execution. If SO triggers before H1 results, the 2% sizing provides adequate cushion.
2. REQUIRED: If UK positions increase beyond 5 (via other additions), IHP.L SO should be PAUSED until UK concentration is reviewed.
3. MONITORING: Revenue margin data points each quarterly update. If compression accelerates to >1.5bps in any single period, downgrade to WATCHLIST WITHOUT SO.

**Why APPROVED despite lower MoS than historical Tier A BUYs:**
- Smallest possible sizing (2%) limits downside to -1% in a 50% drop scenario
- Standing order provides price discipline (not a market buy)
- Business quality is exceptional (0/10 value trap, 24% insider ownership, ROIC 49%, net cash)
- E[CAGR] 12.8% exceeds Tier A deployment threshold
- No non-UK comparable available at this quality level
- Multiple UK positions on PROBATION may be rotated out, naturally reducing concentration

**Confirm standing order at 300p for EUR 200 in eToro?**

---

## META-REFLECTION

### Doubts About This Decision
- The MoS at entry (23.1%) is below all previous Tier A BUYs (31-38%). While compensated by small sizing, this is a pattern I should watch: am I accepting lower MoS over time? The framework says E[CAGR] > 12% justifies Tier A deployment, but the trend is concerning if it continues.
- Revenue margin compression is the single most uncertain variable. Management guidance is the ONLY source for the "deceleration" claim. If I'm wrong about deceleration, the FV drops to 370p and MoS at 300p shrinks to ~19% -- still acceptable but less comfortable.
- IHP.L's sensitivity to UK equity markets is real. A -20% FTSE move temporarily crushes FV to 209-250p. The SO at 300p would then be a 17-30% overvaluation. However, this is TEMPORARY (markets recover), and the 2% sizing limits damage to -1% of portfolio in worst case.

### Weaknesses of the Analysis Received
- R1 thesis did not separate FUA growth into market appreciation (43%) vs organic inflows (57%). This matters because market appreciation reverses in a bear market. R2 correctly flagged this.
- R1 initially cited +76% net inflow growth without noting Q1 FY26 deceleration to +11%. This was cherry-picking the best number. R2 caught it.
- The DCF tool produced meaningless results (FV >1,400p) due to financial services FCF distortion. The thesis correctly rejected DCF but this highlights a gap in our tooling for financial services companies.
- No separate moat_assessment.md or risk_assessment.md were produced in R1. These would have added independent perspective. For future financial services R1 analyses, recommend requiring these documents.

### Suggestions for Improvement
- **quality_scorer.py**: Already flags FCF distortion (implemented Session 99). No further change needed.
- **Valuation framework**: For bps-on-AUM businesses, the standard bear case should ALWAYS include a market downturn scenario (FUA -20%), not just "slower growth." This is a structural feature of the business model. Suggest adding to valuation-methods skill.
- **UK concentration tracking**: The constraint_checker.py reports UK at 14.6% (by capital) but the position count is 4/10 (40%). Both metrics matter. Consider adding position-count-by-geography to the tool output for better visibility.

### Questions for Orchestrator
- None. All questions have been resolved through the R1-R2-R3 pipeline and this R4 analysis. The decision is APPROVED.

---

*Committee Decision Version: 1.0*
*Framework: v4.6*
*Gates Passed: 10/10*
*Verdict: APPROVED -- Standing Order 300p, EUR 200 (2%)*
