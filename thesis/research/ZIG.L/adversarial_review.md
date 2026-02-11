# ZIG.L (Zigup plc) - Adversarial Re-Validation

**Date**: 2026-02-11
**Analyst**: Fundamental Analyst Agent (v4.0 Framework, Adversarial Mode)
**Status**: Re-validation of standing order at 375 GBp
**Original Thesis Version**: 2.0 (2026-02-03)
**Purpose**: Adversarial scrutiny following pattern of 12/13 positions with inflated FV (avg -15%)

---

## FASE 0: QUALITY SCORE (TOOL-FIRST)

### Tool Result

```
QS Tool: 34/100 (TIER D)
```

**Breakdown:**
| Category | Score | Key Drivers |
|----------|-------|-------------|
| Financial Quality | 9/40 | ROIC Spread -2.4pp (0 pts), FCF Margin 0.1% (0 pts), Leverage 2.2x (5 pts), FCF Consistency 4/5 (4 pts) |
| Growth Quality | 10/25 | Revenue CAGR N/A (5 pts), EPS CAGR N/A (5 pts), GM Trend Declining (0 pts) |
| Moat Evidence | 7/25 | GM Premium -5.5pp (0 pts), Market Position (5 pts est), ROIC Persistence (2 pts) |
| Capital Allocation | 8/10 | Shareholder Returns 10yr+ (5 pts), Insider Ownership 5.0% (3 pts) |

### QS Adjustment Analysis

The tool produces QS 34 (Tier D). The question is: are there structural distortions that warrant adjustment?

**Potential distortions identified:**

1. **ROIC Spread (-2.4pp): GENUINE OR DISTORTED?**
   - The company's self-reported ROCE is 12.6% (FY2025), down from 14.5% (FY2024)
   - yfinance-calculated ROIC includes the massive fleet asset base and associated debt
   - For fleet/leasing businesses, capital employed is inherently high (fleet = operating asset, not excess capital)
   - However, EVEN using company-reported ROCE (12.6%) vs WACC (8-9%), the spread is only +3.6-4.6pp
   - At the tool's calculated WACC, the spread is NEGATIVE
   - **VERDICT**: Partial distortion. Company ROCE is positive but declining. Not as bad as tool says, but NOT strong either.

2. **FCF Margin 0.1%: GENUINE OR DISTORTED?**
   - FCF trajectory: FY2021 GBP97.8M, FY2022 GBP19.8M, FY2023 GBP4.5M, FY2024 GBP30.3M, FY2025 GBP(-58.1M)
   - FCF is genuinely near-zero or negative because of fleet investment (growth capex GBP73.6M in H1 alone)
   - Management claims "inflection point" with steady-state FCF >GBP200M by FY27/28
   - This is a GENUINE investment phase, not structural inability to generate cash
   - BUT: 4 out of 5 years had FCF below GBP30M. The GBP200M+ target is aspirational, not proven
   - **VERDICT**: Partially distorted by investment cycle. But FCF weakness is REAL, not just timing.

3. **Gross Margin Trend Declining (0 pts):**
   - Gross margins per yfinance are declining, which is consistent with used vehicle residual values softening
   - This is a real concern, not a data distortion
   - **VERDICT**: Genuine. No adjustment warranted.

4. **Leverage 2.2x (tool) vs 1.9x (company reported):**
   - Minor discrepancy in measurement methodology
   - Both indicate elevated leverage near the upper end of 1-2x target
   - **VERDICT**: Minor distortion. Adjust from 5 pts to 5 pts (no material change).

### QS Adjusted Assessment

```
QS Tool: 34/100 (Tier D)
QS Adjusted: 40/100 (Tier C) -- Adjustment: +6 points

Adjustments:
+4 pts: ROIC Spread adjustment (company ROCE 12.6% > WACC 8-9%, spread +3.6pp deserves 4 pts vs 0)
+2 pts: FCF Consistency (tool says 4/5 but company IS generating operating cash flow;
        the negative FCF is driven by deliberate growth capex, not business failure)
+0 pts: All other categories -- no evidence for upward adjustment

EVIDENCE for each adjustment:
- ROCE 12.6% from company KPIs (audited), positive spread vs 8-9% WACC
- H1 FY26 replacement capex GBP172M + growth capex GBP74M = deliberate fleet investment
- 5-year ROCE track: 7.0%, 9.5%, 13.9%, 14.1%, 14.5%, 12.6% -- consistently above WACC
```

**QS Adjusted: 40/100 -- TIER C (Special Situation)**

This is a CRITICAL downgrade from the original thesis which classified ZIG.L as "Tier B (Cyclical de calidad)." The original thesis did not run quality_scorer.py at all (pre-tool-first era).

**IMPLICATION**: Even with generous adjustments, ZIG.L is Tier C at best. The original thesis claimed Tier B without quantitative support.

---

## FASE 1: BUSINESS UNDERSTANDING -- ADVERSARIAL SCRUTINY

### What the Original Thesis Got Right

1. **Integrated platform model**: Zigup genuinely combines rental, fleet management, claims, and repair. This is differentiated vs pure lessors.
2. **Spain growth**: H1 FY26 rental revenue +16.3% in Spain confirmed. This is real, driven by underpenetrated LCV rental market.
3. **Public sector exposure**: 40%+ of customers are public sector, providing revenue stability. This is verified.
4. **Insider buying**: CEO Martin Ward bought GBP250k at 336p. Net insider buying GBP300k in 12 months. This is confirmed and significant.
5. **Low analyst coverage**: Only 3-5 analysts cover ZIG.L, creating potential for informational inefficiency.

### What the Original Thesis Missed or Minimized

**1. FCF Is Not "Temporarily Compressed" -- It Is Structurally Weak**

The thesis narrative is "FCF is temporarily compressed by fleet investment, inflection coming FY27/28." But the data tells a different story:

| Year | FCF (GBP M) | Net Debt (GBP M) | Leverage |
|------|-------------|-------------------|----------|
| FY2021 | 97.8 | 530.3 | - |
| FY2022 | 19.8 | 582.5 | - |
| FY2023 | 4.5 | 694.4 | - |
| FY2024 | 30.3 | 742.2 | - |
| FY2025 | (58.1) | 836.7 | 1.8x |
| H1 FY2026 | N/A | 939.0 | 1.9x |

Five-year trend: FCF has NEVER been sustainably strong. FY2021 was post-COVID recovery (abnormally high disposal profits). Since then: GBP20M, GBP5M, GBP30M, negative GBP58M.

The GBP200M+ FCF target for FY27/28 requires:
- Replacement capex to normalize (reasonable)
- Growth capex to decline (but they keep expanding fleet)
- Residual values to stabilize (uncertain)
- Working capital to improve (no evidence yet)

**Adversarial assessment**: The GBP200M FCF target is management guidance, not a base case. Apply 30% haircut per critical-thinking skill (management guidance is always optimistic). Realistic steady-state FCF: GBP100-140M. This is still significant but changes the valuation substantially.

**2. Leverage Is at the Top of the Range and Rising**

- FY2025: 1.8x
- H1 FY2026: 1.9x
- Target range: 1-2x
- Covenant: 3.0x (headroom exists but is narrowing)

Net debt went from GBP530M to GBP939M in 5 years (+77%). Fleet assets back the debt, but fleet assets depreciate and are subject to residual value risk. The company's "asset backing" argument only works if residual values hold.

**Debt covenants**: Interest cover 7.4x (covenant 3.0x), Loan-to-value 41% (covenant 70%), Leverage 1.9x (covenant 3.0x). Headroom exists but is not wide. A recession + residual value decline could compress headroom rapidly.

**Interest rate sensitivity**: Average funding rate 3.1%, with recent 7-10yr fixed notes at 4.4%. Some debt is variable rate. In a rising rate environment, funding costs will increase. The company has GBP341M facilities headroom, but new borrowing will be at higher rates.

**3. The "40% Public Sector" Claim Needs Scrutiny**

The thesis presents 40%+ public sector exposure as strong diversification. But:
- Public sector contracts are typically lower-margin (volume deals)
- UK public sector is under fiscal pressure (spending cuts possible)
- Public sector fleet demand is less cyclical but also less growth-oriented
- It does NOT protect against the residual value risk, which is the main concern

**4. Competitive Position Is Not as Strong as Implied**

The thesis says ZIG.L is "the leader" in UK integrated mobility. But:
- Lex Autolease (Lloyds subsidiary): 280,000-385,000 vehicles vs ZIG.L 135,000
- ALD Automotive (SG subsidiary): Largest in UK by fleet size
- Volkswagen Financial Services: 200,000+ vehicles
- ZIG.L is NOT the largest by fleet size. It is the largest INDEPENDENT LCV specialist.

The competitive advantage is integration (rental + claims + repair) rather than scale. This is real but narrower than "market leader" suggests. The moat is moderate, not wide.

**5. EV Residual Value Risk Is Understated**

The thesis says "core is LCVs/ICE, less affected." But:
- EV rentals grew 75% (from a small base)
- The company is transitioning ~20% of service fleet to electric
- UK ZEV mandate will force increasing EV adoption in fleet
- EV residual values have collapsed 30-40% in 2024-2025
- Even ICE LCV residual values are softening: "residual values for LCVs followed a similar pattern to cars -- softening values through summer and autumn"

The thesis's "<10% fleet is EV" figure will grow. By FY2028, EV could be 20-30% of fleet, significantly increasing residual value risk.

**6. Declining ROCE Is a Trend, Not a Blip**

| Year | ROCE |
|------|------|
| FY2020 | 7.0% |
| FY2021 | 9.5% |
| FY2022 | 13.9% |
| FY2023 | 14.1% |
| FY2024 | 14.5% |
| FY2025 | 12.6% |

ROCE peaked at 14.5% in FY2024 and is declining. The thesis assumes ROCE > WACC is sustainable, but:
- FY2025 ROCE 12.6% vs WACC 8-9% = spread of 3.6-4.6pp (moderate, not strong)
- If ROCE continues declining toward 10%, spread compresses to 1-2pp
- At that level, ZIG.L is barely creating value above WACC

---

## FASE 2: VALUATION RE-ASSESSMENT

### Method 1: EV/EBITDA (Primary -- 45% weight)

**Original thesis**: 5x EV/EBITDA = 688 GBp (base case)

**Adversarial challenge**: Is 5x appropriate?

Peer comparison for fleet/leasing (from original thesis):
- Peers trade at 5-7x
- But ZIG.L has: higher leverage, lower FCF generation, smaller scale, declining ROCE
- Appropriate discount to peers: 5x is at the LOW end of peer range, which is reasonable for a Tier C company

Updated calculation:
```
EBITDA FY26E (underlying, annualized): GBP492M (H1: GBP246M x 2)
  - H2 historically slightly better, so GBP500M is reasonable
Net Debt (H1 FY26): GBP939M
Shares outstanding: ~226M

Bear (4x): EV = 2,000M. Equity = 1,061M. Per share = 469p
Base (5x): EV = 2,500M. Equity = 1,561M. Per share = 691p
Bull (6x): EV = 3,000M. Equity = 2,061M. Per share = 912p
```

Wait -- these are similar to the original thesis. But the original used GBP500M EBITDA and I see H1 was GBP246M, so annualized is ~GBP492-500M. The numbers check out.

The KEY question is: should the multiple be 5x or lower? Given:
- ROCE declining (12.6% from 14.5%)
- FCF negative
- Leverage at upper range
- Gross margins declining

I argue 4.5x base is more appropriate than 5x.

```
Revised Base (4.5x): EV = 2,250M. Equity = 1,311M. Per share = 580p
```

### Method 2: P/E Normalized (25% weight)

**Original thesis**: 10x P/E = 550p (base)

**Adversarial challenge**: 10x P/E for a cyclical with 4.4% net margin?

Current TTM EPS: ~55p (underlying). Forward EPS at top of PBT range GBP155M:
- Tax at 25%: Net income GBP116M
- EPS: 116M / 226M shares = 51p

Cyclical companies typically trade at 7-10x mid-cycle P/E. ZIG.L net margin is thin at 4.4%. Insurance-like businesses with thin margins get lower P/E.

- Bear (7x): 51p x 7 = 357p
- Base (8x): 51p x 8 = 408p
- Bull (10x): 51p x 10 = 510p

**The original thesis used 10x as base. This is generous.** An 8x base for a cyclical with thin margins, declining ROCE, and negative FCF is more appropriate.

### Method 3: DDM (20% weight)

**Original thesis**: FV 416-425p

DPS: 26.4p/year. Growth: 2-2.5% (dividend has grown slowly).
Required return: 9-10% (cyclical with leverage).

```
Bear (Ke=10%, g=1.5%): 26.4 x 1.015 / (10% - 1.5%) = 315p
Base (Ke=9.5%, g=2.0%): 26.4 x 1.02 / (9.5% - 2.0%) = 359p
Bull (Ke=9.0%, g=2.5%): 26.4 x 1.025 / (9.0% - 2.5%) = 416p
```

The original thesis DDM of 416-425p was using the BULL case scenario as the base. The true base DDM is ~359p.

### Method 4: NAV Floor (10% weight)

Fleet NBV: GBP1.68B. Net debt: GBP939M. Equity from assets: GBP741M.
Per share: 741M / 226M = 328p.

But book value understates fleet value (used vehicle market). Add 10-15% premium:
- Bear (0%): 328p
- Base (+10%): 361p
- Bull (+15%): 377p

### Reconciliation: Adversarial Fair Value

| Method | Bear | Base | Bull | Weight |
|--------|------|------|------|--------|
| EV/EBITDA | 469p | 580p | 912p | 45% |
| P/E | 357p | 408p | 510p | 25% |
| DDM | 315p | 359p | 416p | 20% |
| NAV | 328p | 361p | 377p | 10% |
| **Weighted** | **399p** | **478p** | **615p** | 100% |

### Expected Value

```
EV = (399 x 25%) + (478 x 50%) + (615 x 25%)
EV = 100 + 239 + 154 = 493p
```

### Comparison: Original vs Adversarial

| Metric | Original (v2.0) | Adversarial |
|--------|-----------------|-------------|
| Bear | 524p | 399p (-24%) |
| Base | 651p | 478p (-27%) |
| Bull | 781p | 615p (-21%) |
| Expected Value | 652p | 493p (-24%) |
| Tier | B | C |

**The original FV was inflated by approximately 24%.** This is consistent with the portfolio-wide pattern of ~15% average FV inflation, though ZIG.L's inflation is above average.

**Sources of inflation:**
1. EV/EBITDA multiple too high (5x vs 4.5x appropriate): ~-15% impact
2. P/E multiple too high (10x vs 8x appropriate): ~-25% impact on P/E component
3. DDM used bull case as base: ~-15% impact on DDM component
4. Tier misclassification (B vs C): materially changed MoS requirements

---

## FASE 3: RISK ASSESSMENT

### Risks the Original Thesis Missed or Minimized

**1. Structural FCF Weakness (HIGH)**
- 5-year FCF average: GBP19M/year (excluding COVID recovery FY2021)
- Net debt growing +77% in 5 years
- Management's GBP200M target is unproven
- If FCF doesn't materialize by FY28, leverage could breach 2.5x (kill condition)

**2. Residual Value Secular Decline (MEDIUM-HIGH)**
- EV residual values collapsing industry-wide
- ICE LCV values also softening
- ZEV mandate forces increasing EV adoption, increasing exposure
- Disposal profits contributed meaningfully to earnings historically
- If residual values decline 10% across the fleet: ~GBP170M book value impairment risk

**3. UK Economic Slowdown (MEDIUM)**
- UK GDP growth modest at best
- Construction, logistics sectors are key fleet customers
- 40% public sector provides buffer but is also under fiscal pressure
- Trump tariffs creating global uncertainty affecting UK trade

**4. Interest Rate / Refinancing Risk (MEDIUM)**
- GBP939M debt at 3.1% average cost
- New borrowing at 4.4% (recent notes)
- If entire debt refinanced at 4.4%, annual interest cost increases by ~GBP12M
- Not catastrophic but compresses already thin margins

**5. Competitive Pressure (LOW-MEDIUM)**
- Lex Autolease (Lloyds-backed) is 2-3x larger
- ALD Automotive, VW Financial Services are massive competitors
- ZIG.L advantage is integration, not scale
- New entrants could replicate integration model over time

**6. Spain Concentration Risk (LOW-MEDIUM)**
- Spain is the growth engine (rental revenue +16.3%)
- If Spanish economy slows (EU wide risk) or regulation changes, growth thesis weakens
- Closing fleet in Spain grew 9.8% -- good but creates asset concentration

---

## FASE 4: VERDICT ON STANDING ORDER

### MoS Analysis at 375 GBp

| Metric | Original Thesis | Adversarial |
|--------|-----------------|-------------|
| FV Expected | 652p | 493p |
| MoS vs EV at 375p | 42% | 24% |
| MoS vs Bear at 375p | 28% | 6% |
| Tier | B (MoS >25% required) | C (MoS >30% required) |
| **MoS adequate?** | **YES** | **NO** |

At 375 GBp:
- MoS vs adversarial EV: 24% -- this is below the typical 30%+ for Tier C
- MoS vs adversarial Bear: only 6% -- dangerously thin
- The standing order does NOT provide adequate protection for a Tier C cyclical

### What Entry Price Would Be Adequate?

For Tier C with 30% MoS vs Expected Value:
```
493p x (1 - 0.30) = 345p
```

For 20% MoS vs Bear case (more conservative):
```
399p x (1 - 0.20) = 319p
```

**Recommended entry range: 320-345 GBp** (not 375 GBp)

### Analyst Consensus Check

Analyst consensus: avg 458-476p, range 350-550p. Only 3-5 analysts.
- The low end of analyst range (350p) is close to our revised entry target
- This suggests analysts with full access to management also see limited upside at current levels

---

## FASE 5: COMPLETE ASSESSMENT

### TL;DR

ZIG.L is a legitimate business with real competitive advantages (integration, Spain growth, public sector base), but the original thesis overstated quality (Tier B vs actual Tier C), ignored structural FCF weakness, and used aggressive valuation multiples. The standing order at 375 GBp does NOT provide adequate Margin of Safety for a Tier C cyclical with declining ROCE, negative FCF, and rising leverage. Entry at 320-345 GBp would be appropriate.

### Quality Score

```
QS Tool: 34/100 (Tier D)
QS Adjusted: 40/100 (Tier C)
Adjustment: +6 points
  +4 pts: ROCE 12.6% (audited) vs WACC 8-9% = positive spread (~3.6pp), tool's ROIC calculation
          penalizes fleet-heavy business model. Evidence: 5yr ROCE track 7-14.5%, consistently >WACC
  +2 pts: FCF negative but driven by deliberate growth capex (GBP74M growth in H1),
          not operational failure. Tool's 0.1% FCF margin conflates investment with weakness.
No further adjustments warranted. Gross margin decline, leverage increase, and moderate
competitive position are accurately captured by the tool.
```

### Kill Conditions (Updated)

1. Leverage >2.5x sustained (2+ quarters)
2. Dividend cut
3. ROCE < WACC for 2 consecutive years (at company-reported level)
4. Spain growth reverses to negative for 2+ quarters
5. **NEW**: FCF fails to exceed GBP100M by FY2028 (management guides >GBP200M)
6. **NEW**: Fleet impairment >GBP100M from residual value declines

### VERDICT

**CANCEL standing order at 375 GBp.**

Reasons:
1. QS 40 = Tier C (not Tier B as original thesis claimed)
2. Adversarial FV 493p vs original 652p (-24% inflation, consistent with portfolio pattern)
3. MoS at 375p: 24% vs EV (below Tier C requirement of ~30%)
4. MoS at 375p vs Bear: only 6% (inadequate for cyclical)
5. FCF structurally weak -- the GBP200M promise is unproven
6. Declining ROCE trend (14.5% to 12.6%)

**Alternative**: If genuinely interested, set new standing order at **330 GBp** (33% MoS vs adversarial EV, 17% MoS vs Bear). This would align with Tier C requirements and provide genuine margin of safety. However, per Principio 9 (Quality Gravitation), deploying capital into a Tier C cyclical with ~GBP0 FCF when we have 44% cash is suboptimal. Better alternatives likely exist in Tier A pipeline.

---

## META-REFLECTION

### Incertidumbres/Dudas
- The GBP200M FCF target is the crux. If management is right, the stock is very cheap at any price below 500p. If wrong, it could be a value trap. There is no way to resolve this without waiting for FY2027/2028 results.
- Company-reported ROCE (12.6%) vs tool-calculated ROIC (-2.4pp spread): significant divergence. The truth likely lies between -- ROCE is a broader measure that may flatter results.
- The 5-analyst coverage creates both opportunity (information gap) and risk (limited external scrutiny of management claims).

### Sugerencias para el Sistema
- The quality_scorer.py struggles with fleet/leasing businesses where FCF is distorted by deliberate fleet investment. Consider a flag or adjustment mode for asset-heavy cyclicals.
- The original thesis (v2.0) was written before the QS tool-first rule (Sesion 52). This is exactly the pattern the adversarial review was designed to catch.

### Preguntas para Orchestrator
1. Should we maintain ZIG.L on the watchlist at the lower 330 GBp entry, or remove it entirely given Principio 9 (Quality Gravitation toward Tier A)?
2. With 44% cash, should we be looking for Tier A opportunities rather than Tier C cyclicals?

### Anomalias Detectadas
- The original thesis listed a "Fair Value v2.0: 652 GBp" but the weighted calculation actually yields 652 only because it used 5x EBITDA as base and 10x P/E as base -- both at the generous end for this type of business.
- Insider buying is genuinely strong (GBP300k net in 12 months, CEO at 336p). This is the strongest bull argument and the only reason to keep it on the watchlist at all.
- The thesis claimed "ROCE 11.9% > WACC" but the company-reported ROCE for FY2025 was 12.6%, and H1 FY2026 annualized may be lower given PBT guidance of GBP155M on higher capital employed. The ROCE may fall below 11% in FY2026.

---

## Sources

- [ZIGUP FY26 Interim Results](https://zigup.com/fy-26-interim-results-statement/)
- [ZIGUP Financial Highlights](https://www.zigup.com/investors/financial-highlights/)
- [ZIGUP KPIs](https://zigup.com/investors/financial-highlights/our-kpis/)
- [ZIGUP Our Markets](https://zigup.com/about-us/our-markets/)
- [Lex Autolease - Wikipedia](https://en.wikipedia.org/wiki/Lex_Autolease)
- [MatrixBCG - Zigup Competitive Landscape](https://matrixbcg.com/blogs/competitors/zigup)
- [UK LCV Rental Market - Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/europe-lcv-rental-market)
- [Investing.com - Zigup Insider Buying](https://www.investing.com/news/company-news/zigup-plc-insider-acquires-company-shares-93CH-3829299)
- [Yahoo Finance - Zigup Insiders](https://finance.yahoo.com/news/several-insiders-invested-zigup-flagging-050404389.html)
- [TipRanks - ZIG Forecast](https://www.tipranks.com/stocks/gb:zig/forecast)
- [DirectorsTalk - ZIG.L Analysis](https://www.directorstalkinterviews.com/zigup-plc-zig-l-stock-analysis-industrial-rental-services-giant-with-a-30-upside-potential/4121238494)
- [Fleet News - UK LCV Market](https://www.fleetnews.co.uk/news/uk-new-lcv-market-records-weakest-start-in-over-a-decade)

---

**Changelog:**
| Version | Date | Changes |
|---------|------|---------|
| Adversarial | 2026-02-11 | Full adversarial re-validation. QS 34 tool -> 40 adjusted (Tier C). FV 652->493 GBp (-24%). Standing order 375 GBp CANCEL recommended. |
