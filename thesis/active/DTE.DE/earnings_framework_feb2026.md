# DTE.DE Earnings Framework -- Feb 26, 2026

> **Report**: FY2025 Full-Year Results
> **Date**: February 26, 2026, 10:00 CET
> **Framework Created**: 2026-02-12
> **Framework Version**: v4.0

---

## 1. Pre-Earnings Summary

| Field | Value |
|-------|-------|
| Current Price | EUR 30.37 (2026-02-12) |
| Fair Value (v3.1) | EUR 35.00 |
| Margin of Safety | 13.2% |
| Position Size | 20.62 shares, ~5.5% portfolio |
| Cost Basis | $699.56 (avg EUR 33.91) |
| P&L | ~-10.4% unrealized |
| Conviction | MEDIUM |
| Quality Score | **Tool: 61/100 (Tier B)** -- UPDATED from 48 (Tier C) |
| QS Adjusted | 61/100 (Tier B) -- No adjustment warranted |

### Quality Score Change (MATERIAL)

The quality_scorer.py now outputs QS 61 (Tier B), a significant improvement from the 48 (Tier C) recorded in the thesis as of 2026-02-10. Root cause of the change:

| Component | Previous (Feb 7) | Current (Feb 12) | Delta | Explanation |
|-----------|-------------------|-------------------|-------|-------------|
| ROIC-WACC spread | -0.7pp | +3.9pp | +4.6pp | FY2024 ROIC 8.7% vs WACC 4.8% |
| ROIC trajectory | Unclear | 4.1% -> 5.5% -> 5.4% -> 8.7% | Improving | FY2024 ROIC jump |
| Revenue CAGR | 1.8% | 2.4% | +0.6pp | Updated data window |
| GM Premium vs sector | -5.5pp | +11.1pp | +16.6pp | GM 61.1% vs sector 50% |
| Legacy score total | 48 | 61 | +13 | Financial +5, Moat +10 (GM) |

**Assessment**: The improvement is driven by FY2024 financials flowing into the tool (ROIC jumped to 8.7%, GM expanded to 61.1%). This is genuine operational improvement, not data error. The ROIC improvement reflects TMUS operating leverage and UScellular consolidation benefits. The GM premium reversal (from -5.5pp to +11.1pp) likely reflects updated sector medians or data window. This QS upgrade needs to be validated post-earnings with FY2025 data. If FY2025 confirms ROIC >7% and GM >60%, Tier B is the correct classification.

**NOTE**: Market Position score is 0/8 (default for tool). DTE is #1 in Germany and #1 in US via TMUS. A manual adjustment of +5-8 points for market position would be warranted if we adjust. However, per QS Tool-First rule, I record the tool output and note the gap. A reasonable adjusted QS would be 61 + 5 (market position) = 66 (still Tier B). I will NOT adjust until post-earnings confirmation.

### Key Thesis Points

1. **TMUS is 60% of EBITDA and the growth engine.** TMUS already reported Q4 2025 on Feb 11 -- BEAT on all key metrics. 2026 EBITDA guide $37-37.5B (+10% YoY).
2. **Consolidated FY2025 guidance**: EBITDA AL ~EUR 45.3B, FCF AL ~EUR 20.1B, EPS ~EUR 2.00, DPS EUR 1.00.
3. **FY2026 EPS target EUR 2.50** stated by management (but NOT yet formally guided).
4. **EUR 2B share buyback** program announced for 2026.
5. **Defensive characteristics**: Non-discretionary telecom, 90%+ recurring revenue, low churn (~1%).
6. **Risks**: High leverage (3.3x Net Debt/EBITDA), Tier C-to-B quality (still not a compounder), EUR/USD translation risk, EU operations low-growth.

---

## 2. Consensus Expectations

### Source: Deutsche Telekom IR Consensus (as of Feb 4, 2026, 21 analysts)

#### Group Level

| Metric | FY2025 Consensus | Company Guide | My Base | Q4 2025 Consensus |
|--------|-----------------|---------------|---------|-------------------|
| **Revenue** | EUR 118.7B | "Increasing" | EUR 119B | EUR 31.3B |
| **EBITDA AL (adj)** | EUR 44.1B | ~EUR 45.3B | EUR 45.0B | EUR 10.7B |
| **Net Income (adj)** | EUR 9.8B | -- | EUR 9.5B | EUR 2.2B |
| **EPS (adj)** | EUR 2.02 | ~EUR 2.00 | EUR 2.00 | EUR 0.44 |
| **FCF AL** | EUR 19.5B | ~EUR 20.1B | EUR 20.0B | EUR 3.4B |
| **DPS** | EUR 1.12 | EUR 1.00 floor | EUR 1.00-1.10 | -- |

**Critical Observation**: There is a GAP between company guidance and consensus:
- Company guides EBITDA ~EUR 45.3B vs consensus EUR 44.1B. This suggests the company has been guiding UP (3 raises during 2025) and analysts may be conservative, or the consensus compilation uses a stale cut-off (Jan 21 deadline). The actual result will likely be EUR 45.0-45.5B.
- Company guides FCF ~EUR 20.1B vs consensus EUR 19.5B. Same dynamic.
- DPS consensus EUR 1.12 vs company stated EUR 1.00. Analysts expect MORE than the company announced, which could lead to a small beat if DTE announces EUR 1.10-1.15.

#### FY2026 Consensus (Key for forward guidance)

| Metric | FY2026 Consensus | Company Stated | My Base (v3.1) |
|--------|-----------------|----------------|-----------------|
| **Revenue** | EUR 121.8-122.3B | -- | EUR 127B |
| **EBITDA AL (adj)** | EUR 46.5B | -- | EUR 48.5B |
| **EPS (adj)** | EUR 2.20 | ~EUR 2.50 | EUR 2.50 |
| **FCF AL** | EUR 20.1B | -- | EUR 21B |
| **DPS** | EUR 1.25 | 40-60% payout | EUR 1.10-1.25 |

**Critical Gap on EPS**: Company has stated FY2026 EPS target of ~EUR 2.50. Consensus shows EUR 2.20. This is a significant gap. If DTE formally guides EUR 2.50 on Feb 26, this would be a 14% EPS beat vs consensus -- a strong catalyst for re-rating.

**Critical Gap on EBITDA**: My v3.1 thesis uses EUR 48.5B (reflecting TMUS 2026 guide $37-37.5B). Consensus is EUR 46.5B. My estimate may be optimistic OR may correctly incorporate the TMUS Capital Markets Day data that analysts have not yet fully updated (Jan 21 cut-off was BEFORE the Feb 11 TMUS results).

### Segment Expectations

| Segment | FY2025E EBITDA | Key Driver | Risk |
|---------|----------------|------------|------|
| **T-Mobile US** | ~EUR 28.5B (at $1.08 FX) | Already reported: FY25 $33.9B. 2026 guide $37-37.5B | EPS depressed by severance. FX translation |
| **Germany** | ~EUR 10.5-11B | EBITDA growth >2% Q4. Fiber + mobile ARPU | Competition from 1&1. Energy costs |
| **Europe** | ~EUR 4.5-4.8B | 7th consecutive year of EBITDA growth | Weak consumer in Southern Europe |
| **Systems Solutions** | ~EUR 0.4B | Order entry +10.8% FY24, cloud & security | Automotive sector weakness |

### TMUS Results Already Known (Feb 11 -- COMPLETED)

| Metric | FY2025 Actual | 2026 Guide | 2027 Guide |
|--------|--------------|------------|------------|
| Postpaid Net Adds | 7.8M (beat 7.2-7.4M guide) | Acct adds 900K-1M | -- |
| Service Revenue | $71.3B (+7.7%) | ~$77B (+8%) | $80.5-81.5B (+5%) |
| Core Adj EBITDA | $33.9B (+6.8%) | $37.0-37.5B (+10%) | -- |
| Adj Free Cash Flow | $18.0B (+5.7%) | $18.0-18.7B | -- |
| Q4 EPS | $1.88 (-27%, severance) | -- | -- |

**TMUS was the main event. It already beat.** The Feb 26 DTE earnings are primarily about:
1. Confirmation of consolidated FY2025 at/above raised guidance
2. FY2026 formal guidance (especially EPS EUR 2.50 confirmation)
3. Dividend announcement (EUR 1.00 floor, upside EUR 1.10-1.15)
4. EU operations update (Germany fiber rollout, Europe margin trends)
5. Any strategic announcements (M&A, further TMUS ownership changes)

---

## 3. Scenario Analysis

### BULL Case (25% probability)

**What happens**:
- FY2025 EBITDA AL EUR 45.5B+ (beat raised guidance)
- FY2026 formal guidance: EBITDA EUR 48-49B, EPS EUR 2.50+
- Dividend raised to EUR 1.10-1.15 (above EUR 1.00 floor)
- Buyback program EUR 2B confirmed or increased
- Germany fiber: >8M homes passed, ARPU growth +2-3%
- Europe: margin expansion continues for 8th year
- Potential announcement: increased TMUS ownership or special distribution

**Implied FV**: EUR 37-40
- EV/EBITDA 6.5-7.0x on EUR 48.5B+ = EUR 37-43
- P/E 15-16x on EUR 2.50 = EUR 37.50-40.00

**Action**: HOLD. Do NOT chase. If price rallies to EUR 34-35 (near FV), activate TRIM standing order (7 shares at >EUR 34). The thesis is Tier B (now), not a compounder. Take profit near fair value.

**Reasoning**: DTE is a defensive income position, not a growth compounder. Even in the bull case, forward return from EUR 34-35 would be mostly yield-based (~4.5%). Better uses of capital likely exist in pipeline (PAYC at QS 85, MORN at QS 83).

### BASE Case (50% probability)

**What happens**:
- FY2025 EBITDA AL EUR 45.0-45.3B (in-line with raised guidance)
- FY2026 guidance: EBITDA EUR 47-48B, EPS EUR 2.40-2.50
- Dividend EUR 1.00-1.05 (meeting floor, small upside)
- Buyback EUR 2B confirmed
- Germany stable, Europe stable
- No surprises

**Implied FV**: EUR 34-36
- EV/EBITDA 6.5x on EUR 47.5B = EUR 34.55
- P/E 14x on EUR 2.50 = EUR 35.00

**Action**: HOLD at MEDIUM conviction. MoS ~13-15% at current EUR 30.37. Total expected return ~18-19% (MoS convergence + 3.3% div yield + ~2-3% EPS growth). Competitive with portfolio average. No urgency to add or trim.

**Reasoning**: Base case validates the v3.1 thesis. The position earns its place as a defensive anchor with reasonable forward return. Monitor for rotation opportunity if a Tier A candidate at significant MoS emerges. Principio 9 (Quality Gravitation): QS 61 Tier B is not the lowest quality in the portfolio (VICI 54, UHS 51 are Tier C), but DTE should be monitored for eventual rotation to higher quality.

### BEAR Case (25% probability)

**What happens**:
- FY2025 EBITDA AL below EUR 45.0B (miss vs raised guidance)
- FY2026 EPS guidance below EUR 2.30 (significant miss vs EUR 2.50 target)
- Germany EBITDA flat or declining (competition from 1&1, fiber cost overruns)
- Europe margin compression (Southern European weakness)
- EUR/USD headwind reduces TMUS contribution in EUR terms
- Dividend meets floor EUR 1.00 but no increase

**Implied FV**: EUR 29-31
- EV/EBITDA 5.5-6.0x on EUR 46B = EUR 28-33
- P/E 12x on EUR 2.30 = EUR 27.60

**Action**: If FY2026 EPS guidance <EUR 2.30 -- **TRIM 50%** (sell 10 shares). This is a meaningful deterioration from stated EUR 2.50 target and signals TMUS translation issues or EU weakness. At EUR 30.37 and bear FV EUR 29-31, there would be essentially zero MoS remaining.

If FY2026 EPS guidance EUR 2.30-2.40 -- HOLD but downgrade conviction to LOW and set tighter EXIT trigger. The thesis weakens but does not break.

**Reasoning**: The bear case does not trigger a kill condition (dividend intact, no credit rating issue), but it eliminates the MoS and makes DTE dead money. At zero MoS with Tier B quality, the Opportunity Score vs pipeline candidates (PAYC QS 85 at 25%+ MoS) would justify rotation. Principio 6 (Sell requires argument): Argument = zero MoS + better alternative. Consistent with precedent SHEL.L exit (MoS -3.5% + AUTO.L available).

---

## 4. Kill Conditions (Immediate SELL Triggers)

These trigger immediate full exit regardless of scenario:

| # | Kill Condition | Threshold | Rationale |
|---|---------------|-----------|-----------|
| 1 | **Dividend cut** | DPS announced <EUR 1.00 | Violates raised dividend commitment; signals cash flow stress |
| 2 | **FY2026 EPS guidance <EUR 2.00** | Below FY2025 level | Implies regression, not growth; entire thesis premised on earnings growth |
| 3 | **Credit rating downgrade below BBB** | Any agency | Would signal unsustainable leverage; refinancing risk materializes |
| 4 | **TMUS controlling stake lost** | DTE ownership <50% | Fundamental thesis change; DTE loses consolidation of crown jewel |
| 5 | **Debt/EBITDA >3.5x for 2+ quarters** | Reported metric | Leverage approaching unsustainable levels |
| 6 | **Guidance withdrawal** | No FY2026 guidance provided | Extreme uncertainty signal |

---

## 5. Key Questions to Answer from the Report

### Priority 1 -- Thesis Validation

1. **FY2026 EPS guidance**: Is EUR 2.50 formally confirmed? This is the single most important data point. Consensus is EUR 2.20 -- formal confirmation of EUR 2.50 would be a strong catalyst.
2. **FY2026 EBITDA AL guidance**: What range? My model uses EUR 48.5B. If guided >EUR 47B, thesis intact. If <EUR 46B, thesis weakens.
3. **Dividend**: EUR 1.00 confirmed or increased? Upside to EUR 1.10-1.15 would be positive.
4. **Buyback**: EUR 2B 2026 program confirmed? Timeline and execution plans?

### Priority 2 -- Segment Performance

5. **Germany Q4 EBITDA**: Growth >2% as expected? Fiber rollout progress (homes passed, take-up rates)?
6. **Europe Q4**: Margin expansion continuing? Any country-specific weakness?
7. **Systems Solutions**: Revenue and margin trajectory? Cloud/security pipeline?
8. **TMUS consolidation FX impact**: What EUR/USD rate was used? How does current ~1.19 compare to budget rate?

### Priority 3 -- Strategic and Risk

9. **TMUS ownership**: Any plans to increase stake above 51.5%? Sprint merger integration complete?
10. **Net debt trajectory**: Path to Debt/EBITDA 2.75x target?
11. **Net neutrality/regulatory**: Any commentary on EU Digital Networks Act or Bundesnetzagentur investigation?
12. **German fiscal stimulus**: Benefit from EUR 500B infrastructure fund for fiber/5G?
13. **CEO Hottges**: Any strategic shifts or updated medium-term targets?

---

## 6. Post-Earnings Decision Matrix

| Metric | BULL Threshold | BASE Range | BEAR Threshold | KILL |
|--------|---------------|------------|----------------|------|
| FY2025 EBITDA AL | >EUR 45.5B | EUR 44.8-45.5B | <EUR 44.5B | -- |
| FY2025 FCF AL | >EUR 20.5B | EUR 19.5-20.5B | <EUR 19.0B | -- |
| FY2025 EPS | >EUR 2.10 | EUR 1.95-2.10 | <EUR 1.90 | -- |
| FY2025 DPS | >EUR 1.05 | EUR 1.00 | <EUR 1.00 | **SELL** |
| FY2026 EBITDA guide | >EUR 48B | EUR 46.5-48B | <EUR 46B | -- |
| FY2026 EPS guide | >EUR 2.50 | EUR 2.30-2.50 | <EUR 2.30 | <EUR 2.00 = **SELL** |
| Germany EBITDA Q4 | >+3% YoY | +1-3% YoY | Flat/negative | -- |
| Net Debt/EBITDA | <2.7x | 2.7-3.0x | >3.0x | >3.5x = **SELL** |

### Action Summary by Combined Scenario

| Combined Result | Action | Sizing | Conviction |
|----------------|--------|--------|------------|
| **BULL** (EBITDA beat + EPS EUR 2.50+ guide + div increase) | HOLD, activate TRIM >EUR 34 | Maintain ~5.5% | MEDIUM-HIGH |
| **BASE** (In-line + EPS EUR 2.40-2.50 guide) | HOLD | Maintain ~5.5% | MEDIUM |
| **SOFT BEAR** (Slight miss + EPS EUR 2.30-2.40) | HOLD, tighten monitoring | Maintain | LOW-MEDIUM |
| **HARD BEAR** (Miss + EPS <EUR 2.30) | TRIM 50% | Reduce to ~2.5-3% | LOW |
| **KILL** (Div cut OR EPS guide <EUR 2.00 OR rating cut) | SELL 100% | Exit | N/A |

---

## 7. Thesis Update Needed Post-Earnings

Regardless of outcome, the thesis must be updated to reflect:

1. **QS change**: Tool now shows 61 (Tier B), up from 48 (Tier C). If FY2025 data confirms, this is a material re-classification. Tier B changes the MoS benchmark, rotation priority, and conviction framework.
2. **FY2025 actual numbers** replacing estimates
3. **FY2026 formal guidance** vs my assumptions
4. **Standing orders review**: TRIM >EUR 34 (still valid?), ADD <EUR 28 (still relevant?)
5. **Rotation assessment**: With 44% cash and 6 pipeline candidates (PAYC, MORN, DSY.PA, DNLM.L, RACE.MI, INTU), evaluate whether DTE capital is better deployed elsewhere (Principio 9)

---

## 8. Precedents Consulted

| Precedent | Situation | Decision | Relevance |
|-----------|-----------|----------|-----------|
| DTE.DE TRIM (Feb 3) | Overaccumulated to 7.3% | TRIM to 6.4% | Sizing discipline for Tier C. Now potentially Tier B -- reconsider sizing |
| SHEL.L HOLD then EXIT | Thin MoS, then alternative appeared | HOLD -> SELL when AUTO.L ready | If DTE has zero MoS post-bear + pipeline ready, same logic applies |
| ALL HOLD (Feb 5) | Earnings BEAT, combined ratio excellent | HOLD, thesis strengthened | If DTE beats, same response: HOLD, no chase |
| TEP.PA HOLD then EXIT | Earnings review, thesis debilitating | HOLD -> SELL when BYIT.L ready | Dead money pattern -- if DTE stalls, eventually rotate |
| ROIC < WACC pattern | 8/8 positions with this were sold | EXIT | DTE ROIC was -0.7pp. NOW +3.9pp per tool. If confirmed, this EXIT signal is removed. Very positive development. |

**Key insight from precedents**: The ROIC-WACC spread improvement from -0.7pp to +3.9pp is the most significant change. Every position with ROIC < WACC was eventually sold (8/8). If DTE's ROIC has genuinely crossed above WACC, this removes what was arguably the strongest bear argument and potential kill condition. FY2025 earnings will confirm or deny this.

---

## 9. FX Sensitivity (EUR/USD)

TMUS reports in USD. DTE consolidates in EUR. Current EUR/USD ~1.19.

| EUR/USD Rate | TMUS EBITDA in EUR (at $37B guide) | Impact on Group EBITDA |
|--------------|----------------------------------|-----------------------|
| 1.08 (budget) | EUR 34.3B | Base assumption |
| 1.12 | EUR 33.0B | -EUR 1.3B vs budget |
| 1.19 (current) | EUR 31.1B | -EUR 3.2B vs budget |
| 1.25 | EUR 29.6B | -EUR 4.7B vs budget |

**This is critical**: If DTE used $1.08 as its budget rate (which it historically does), the current EUR 1.19 represents a ~10% headwind on TMUS translation. This means:
- My EUR 48.5B EBITDA estimate for FY2026 may be overstated by EUR 2-3B on FX alone
- But: DTE typically guides at constant FX and then reports both constant FX and actual. The market watches constant FX for underlying performance.
- Watch for: What FX rate DTE uses in FY2026 guidance. If they guide at "current rates" (1.19), the EUR EBITDA number will be lower than at historical rates.

---

---

## META-REFLECTION

### Changes Detected Since Last Review (Feb 10-11)

- **Quality Score material change**: Tool now shows QS 61 Tier B vs 48 Tier C. The ROIC-WACC spread improved from -0.7pp to +3.9pp. This is driven by FY2024 data (ROIC jumped to 8.7%). This is the single most important development -- it potentially removes the "ROIC < WACC" bear signal that drove 8 previous exits.
- **TMUS Q4 results**: Already incorporated in v3.1. FV upgraded EUR 34 -> 35. Beat on all key metrics. 2026 EBITDA +10% guide.
- **Price**: EUR 30.37, roughly stable since thesis update. MoS ~13%.
- **Consensus vs company**: Significant gap on FY2026 EPS (consensus EUR 2.20 vs company EUR 2.50). This is a potential positive catalyst if formally guided.

### Incertidumbres

1. **QS improvement durability**: The QS jump from 48 to 61 is large. It could be driven by data window changes (FY2024 ROIC 8.7% is one data point, not a trend). Need to see if FY2025 ROIC >7% to confirm sustainability.
2. **FX impact on FY2026 guidance**: EUR/USD at 1.19 is significantly above the typical 1.08 budget rate. FY2026 EBITDA in EUR could be EUR 2-3B lower than my estimate on FX alone. The market may react negatively to a "miss" that is purely FX-driven.
3. **EPS EUR 2.50 confirmation**: Management stated this but has not formally guided it. If they guide EUR 2.30-2.40 citing FX, the market may treat it as a disappointment even if underlying USD earnings are strong.
4. **Consensus staleness**: The consensus was compiled with a Jan 21 cut-off -- BEFORE TMUS Q4 results (Feb 11). Analysts have not updated. The "real" consensus for FY2026 EBITDA is likely higher than EUR 46.5B. This means the bar for a "beat" may be higher than the published consensus suggests.

### Suggestions

1. **Post-earnings**: Run quality_scorer.py again once FY2025 data flows in. If QS confirms >55 (Tier B), update thesis tier classification from C to B. This changes sizing rationale, MoS framework, and rotation priority.
2. **FX scenario planning**: Build explicit constant-FX vs actual-FX comparison into the post-earnings review. DTE is essentially a USD-earning company reporting in EUR.
3. **Standing order review**: The ADD <EUR 28 trigger seems appropriate for bear case. The TRIM >EUR 34 trigger should be maintained. Both are consistent with the scenario analysis.
4. **Rotation consideration**: Even at QS 61 Tier B, DTE's forward return of ~19% is competitive but not exceptional. With PAYC (QS 85, Tier A), MORN (QS 83, Tier A), and DSY.PA (approved) in the pipeline, DTE could be a rotation candidate if the bull case plays out and the stock approaches EUR 34-35 with thin MoS remaining.

### Alerts for Orchestrator

1. **QS TIER CHANGE DETECTED**: DTE.DE moved from QS 48 (Tier C) to QS 61 (Tier B) in the quality_scorer.py output. This is a material change that should be confirmed post-earnings and then propagated to the thesis, portfolio stats, and decisions_log.yaml.
2. **FX RISK**: EUR/USD at 1.19 vs typical 1.08 budget rate creates translation headwind of ~10% on TMUS contribution. If DTE guides FY2026 at current FX rates, the absolute EUR numbers will appear lower than expected. The market may misinterpret this. Watch for DTE's language on "constant currency" vs "reported" guidance.
3. **CONSENSUS STALE**: Jan 21 cut-off means published consensus does NOT include TMUS Q4 beat or 2026 guidance. The "real" bar is likely 3-5% above published consensus numbers.

---

## Sources

- [Deutsche Telekom Consensus Estimates](https://www.telekom.com/en/investor-relations/publications/consensus)
- [Deutsche Telekom Outlook & Financial Strategy](https://www.telekom.com/en/investor-relations/company/outlook-financial-strategy)
- [Deutsche Telekom Q3 2025 Results](https://www.telekom.com/en/media/media-information/archive/third-quarter-report-2025-1098968)
- [Deutsche Telekom Financial Results 2025](https://www.telekom.com/en/investor-relations/publications/financial-results/financial-results-2025)
- [T-Mobile US Q4 2025 Earnings and Capital Markets Day](https://www.t-mobile.com/news/business/t-mobile-q4-2025-earnings)
- [T-Mobile US 2026 Guidance (BusinessWire)](https://www.businesswire.com/news/home/20260210151033/en/)
- [T-Mobile Q4 2025 Earnings Transcript (Motley Fool)](https://www.fool.com/earnings/call-transcripts/2026/02/11/t-mobile-us-tmus-q4-2025-earnings-transcript/)
- [MarketScreener DTE Forecasts](https://www.marketscreener.com/quote/stock/DEUTSCHE-TELEKOM-AG-444661/finances/)
- [Capital.com DTE Stock Forecast](https://capital.com/en-int/market-updates/deutsche-telekom-stock-forecast-10-02-2026)
- [Digital Networks Act Overview](https://radiobruxelleslibera.com/2026/01/18/whats-new-for-telcos-and-ott-in-the-incoming-digital-network-act/)
- [EU Net Neutrality / Epicenter.works](https://epicenter.works/en/content/the-eu-commission-is-gutting-net-neutrality)
- quality_scorer.py (2026-02-12): 61/100 Tier B
- price_checker.py (2026-02-12): EUR 30.37, TMUS $209.54
