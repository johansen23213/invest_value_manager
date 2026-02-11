# WKL.AS - Wolters Kluwer NV: Adversarial Thesis Review

**Review Date:** 2026-02-11
**Original Thesis Date:** 2026-02-07
**Framework Version:** 4.0

---

## 1. QUALITY SCORE VERIFICATION

### QS Tool Output (FUENTE PRINCIPAL)

```
TOTAL SCORE: 72/100 → TIER B
Category: Quality Value

Financial Quality:    27/40 pts
  ROIC Spread:       8 pts  (5.4pp)
  FCF Margin:       10 pts  (22.7%)
  Leverage:          5 pts  (2.2x)
  FCF Consistency:   4 pts  (4/5)

Growth Quality:       18/25 pts
  Revenue CAGR:      5 pts  (5.5%)
  EPS CAGR:          8 pts  (12.9%)
  GM Trend:          5 pts  (Expanding)

Moat Evidence:        22/25 pts
  GM Premium:       10 pts  (+44.9pp)
  Market Position:   5 pts  (Manual input needed)
  ROIC Persistence:  7 pts  (Estimated from current)

Capital Allocation:    5/10 pts
  Shareholder Ret:   5 pts  (10yr)
  Insider Own:       0 pts  (0.1%)
```

**QS Tool: 72/100 (Tier B)**

### Thesis Adjustment: 72 -> 75 (Tier B -> borderline Tier A)

The thesis adjusted QS from 72 to 75 based on a +3 point correction for Market Position (from 5 to 8 points), arguing the tool's "manual input needed" default of 5 understates WKL's #1-2 positions in tax/accounting, clinical decision support, and compliance.

### Adversarial Assessment of the Adjustment

**Is the +3 point Market Position adjustment valid?**

- WKL IS #1 in US professional tax software (~59% market share for CCH Axcess) -- VERIFIED
- WKL IS top-3 in clinical decision support (UpToDate) -- VERIFIED
- WKL IS #1-2 in banking compliance software (OneSumX, >90% of top US banks) -- CLAIMED but hard to verify independently

The adjustment from 5 to 8 points for market position is reasonable on the facts. However, the impact is exactly +3 points, which conveniently lifts QS from 72 to 75 -- the exact Tier A boundary. This should trigger skepticism per the adversarial review mandate.

**Additional concerns that could LOWER the QS:**

1. **Insider ownership 0.1% = 0 points.** This is not adjustable. It is a fact. The tool correctly scores this at 0/5. For a "quality compounder," management having virtually zero skin in the game is a genuine weakness. Dutch institutional culture explains it but does not remove the misalignment risk.

2. **FCF Consistency scored 4/5.** The tool detected one year of FCF miss in the last 5. This is correct -- 2022 FCF was EUR 1.22B vs 2021 EUR 1.29B, a decline. While still positive every year, the tool penalizes inconsistency. This is appropriate.

3. **ROIC Spread scored 8 points (5.4pp).** The thesis claims ROIC 18.1% vs WACC ~8.5% = spread of ~9.6pp. But the tool calculates 5.4pp spread. The discrepancy likely arises because the tool uses a different WACC calculation or a different ROIC definition. GuruFocus reports ROIC at 13.3% (annualized Q4 2024), which is materially lower than the thesis's 18.1%. The 18.1% appears to be the company's own adjusted ROIC figure (which excludes goodwill amortization and other items). **This is a significant discrepancy.**

**Adversarial QS Assessment:**

| Component | Tool | Thesis Adj | Adversarial | Reasoning |
|-----------|------|------------|-------------|-----------|
| Financial | 27 | 27 | 27 | ROIC debate exists but tool score stands |
| Growth | 18 | 18 | 18 | No change warranted |
| Moat | 22 | 25 (+3 Mkt Pos) | 25 | Market position adjustment is fair |
| Cap Alloc | 5 | 5 | 5 | 0.1% insider ownership is what it is |
| **TOTAL** | **72** | **75** | **75** | |

**Adversarial verdict on QS: 72-75, Tier B (borderline Tier A)**

I accept the Market Position adjustment as factually warranted. However, the 0.1% insider ownership and the ROIC discrepancy (company-reported 18.1% vs GuruFocus 13.3%) mean this is a MARGINAL Tier A at best. The thesis should NOT claim this as a confident Tier A company. It is borderline, and should be valued and sized as Tier B with Tier A characteristics.

---

## 2. VERIFICATION OF KEY CLAIMS

### Claim 1: "Only 8-10% of revenue at risk from AI"

**Thesis states:** Legal & Regulatory division is 16% of revenue, 10-13% of EBIT. Only the "legal research" portion is vulnerable. Total revenue at risk: 8-10%.

**Verification:**

The 16% revenue figure for Legal & Regulatory is confirmed by 9M 2025 data (division revenues consistent with stated proportion). The 10-13% EBIT figure is corroborated by Morningstar and multiple analyst reports.

**Adversarial challenge:** The thesis's 8-10% estimate assumes only the "research" portion of legal is at risk, and that tax, health, compliance, and ESG are immune. This may be optimistic for two reasons:

1. **Claude's legal plugin is just the beginning.** Anthropic launched with legal, but the same "model + wrapper + workflow" strategy could extend to tax prep, compliance, and health. The thesis assumes these segments are insulated by switching costs and regulatory barriers, but these same barriers were assumed for legal before Feb 3. What stops Anthropic or OpenAI from building a "Claude Tax Plugin" or "Claude Compliance Plugin" in 12-24 months?

2. **The 20-30% estimate for Legal & Regulatory division is itself uncertain.** The thesis states 20-30% of the Legal & Regulatory division's revenue is at risk. But the Claude plugin targets contract review, legal briefings, and templated responses -- tasks that are central to in-house legal teams. This could be closer to 40-50% of the division over 3-5 years if AI adoption accelerates.

**Adversarial estimate:** Revenue at risk is likely 10-15% (not 8-10%), and could be 15-20% if AI capabilities expand beyond legal into other professional domains. The thesis is moderately optimistic.

### Claim 2: "H1 2025 showed 6% organic growth"

**Verification:** H1 2025 organic growth was 5% (not 6%). The 9-month figure was 6% organic. The thesis conflates these. The H1 report shows 5% organic on EUR 3,052M revenue. Momentum improved in Q3, bringing the 9M figure to 6%.

**Correction needed:** H1 was 5% organic, 9M was 6% organic. Full-year guidance reaffirmed at "broadly in line with prior year" (which was 6% organic in FY2024).

### Claim 3: "84% recurring revenue"

**Verification:** The 9M 2025 trading update confirms 84% recurring revenue. However, the FY2024 annual report states 82% recurring revenue. The difference is that the 9M 2025 figure benefits from the continued shift to cloud (non-recurring declining faster). The 84% figure appears to be the most current and is not misleading.

**Minor correction:** FY2024 was 82%, 9M 2025 was 84%. The thesis uses the 9M 2025 figure throughout, which is acceptable but should note the trajectory.

### Claim 4: "ROIC really 18.1%"

**Verification:** This is the company's adjusted ROIC figure, which excludes certain items including amortization of acquired intangible assets. GuruFocus calculates ROIC at 13.3% (Q4 2024 annualized) using standard methodology including goodwill.

The ROIC discrepancy matters because:
- Company-adjusted: 18.1% (excludes goodwill amortization) -> spread vs WACC = ~9.6pp
- Standard (GuruFocus): 13.3% -> spread vs WACC = ~4.8pp
- The QS tool uses 5.4pp spread, consistent with the standard calculation

**Adversarial assessment:** Both figures show ROIC > WACC, which is the critical threshold. But the thesis's presentation of "18.1% ROIC" without noting that this is an adjusted figure is misleading. The standard ROIC of ~13% is more appropriate for cross-company comparison and QS scoring. For an information services company with large acquired databases (goodwill), this is still a healthy spread, but NOT the wide-moat compounder spread the thesis implies.

### Claim 5: "63% decline from all-time high"

**Verification:** Price checker shows 52-week high EUR 181.30, current price EUR 65.72 = -63.7% decline. This is confirmed. However, the 52-week LOW is EUR 65.14, meaning the current price of EUR 65.72 is within 1% of the 52-week low. The stock continues to make new lows even after the thesis was written on Feb 7 (it was EUR 67.70 then, now EUR 65.72 -- a further -2.9% decline in 4 days).

---

## 3. WHAT HAS HAPPENED SINCE THE THESIS WAS WRITTEN (Feb 7)

### Price Movement

- **Thesis date (Feb 7):** EUR 67.70
- **Current (Feb 11):** EUR 65.72
- **Change:** -2.9% (further decline)
- **52-week low:** EUR 65.14 (set recently)
- **The stock is AT or near its 52-week low and still falling.**

### FY2025 Results NOT Yet Published

The thesis identified this as a key catalyst: "2025 Full-Year Results are imminent (expected late February 2026)." The results are scheduled for **February 25, 2026** -- still 14 days away. This is critical: the stock could move significantly in either direction on these results.

### Share Buyback Update

Wolters Kluwer repurchased 177,617 shares for EUR 13.5M at an average price of EUR 76.20 during Jan 29 - Feb 4. The EUR 200M buyback program runs through Feb 23, 2026. The average buyback price of EUR 76.20 is 16% above the current market price, meaning the company was buying at higher prices. The buyback provides some floor support but is small relative to market cap (~1.3% annualized).

### BofA Upgrade

BofA Securities upgraded WKL from Neutral to Buy with a EUR 165 target on Feb 2 (the day BEFORE the Claude crash). This is notable because:
- The upgrade was based on WKL's defensiveness in an uncertain macro environment
- The EUR 165 target was set BEFORE the 13% crash
- Post-crash, there has been no visible downgrade, but the target may be stale

### No New Material Developments

No additional AI developments, regulatory changes, or company-specific news since the thesis date. The stock drift from EUR 67.70 to EUR 65.72 appears to be continued post-crash selling pressure / sector rotation, not new information.

---

## 4. CHALLENGE: SPECIFIC WEAKNESSES

### 4.1 The QS 72->75 Adjustment is Suspicious

As detailed in Section 1, the +3 point adjustment lands EXACTLY on the Tier A boundary. This is the exact pattern identified in the adversarial review sessions (48-52): theses inflate QS to reach a higher tier. The original fundamental-analyst should have flagged this coincidence.

**Verdict:** The adjustment is factually defensible (market position is strong), but the convenient landing point on 75 warrants treating this as Tier B for all valuation and sizing purposes. The "borderline Tier A" label is acceptable for qualitative description only.

### 4.2 Insider Ownership 0.1% is a REAL Concern

The thesis acknowledges this (0.1% insider ownership, scoring 0/5 on Cap Alloc) but dismisses it as "common for Dutch companies." This is a pattern seen in the adversarial reviews: acknowledging a weakness then minimizing it.

**Why it matters for a compounder:** Quality compounders are defined by management that allocates capital wisely over decades. With 0.1% ownership, the executive board and supervisory board collectively own ~EUR 13M in stock. For executives earning EUR 3-5M/year in compensation, this is 3-4 years of salary. This is NOT aligned for a company worth EUR 15B. Compare to BYIT.L (9.6% insider ownership), ADBE (executives actively buying), or AUTO.L (management with meaningful ownership).

**Impact:** This does not disqualify WKL as an investment, but it means management has limited downside exposure if they make poor AI strategy decisions. In a period where AI disruption is the central question, having management with no financial skin in the game is a genuine risk factor.

### 4.3 The HRB Comparison is Both Flattering and Concerning

The thesis compares WKL favorably to HRB (both face AI in tax/professional services, both had ~40% MoS). However, HRB was just SOLD from the portfolio on Feb 9 after adversarial review revealed:
- Intuit's physical + AI two-front assault (600 Expert Offices + $100M OpenAI)
- FCF structural decline (-23% over 3 years)
- Moat breach from a competitor embedding AI into physical presence

**The concerning parallel:** WKL faces the same dynamic -- AI companies (Anthropic, OpenAI) building "model + wrapper + workflow" that competes directly with incumbent workflow tools. The thesis argues WKL's moat is stronger (switching costs, regulatory barriers), which is true for now. But HRB's moat was also considered strong 6 months ago.

**The key difference:** WKL has 84% recurring revenue and is actively integrating AI into its products (CCH Axcess Expert AI, UpToDate Expert AI). HRB was declining in FCF. WKL's fundamentals are genuinely stronger.

**Verdict:** The HRB comparison should serve as a WARNING, not a validation. It demonstrates that "AI won't disrupt us" theses can fail faster than expected. But WKL's stronger fundamentals and active AI integration make it genuinely different from HRB.

### 4.4 The Morningstar Fair Value Claim is Confusing

The thesis claims Morningstar's EUR 585 FV would be ~EUR 83.50 "adjusted for a 7:1 stock split." However, there is NO evidence of a stock split. Research shows Wolters Kluwer had ~237.5M shares outstanding at end of 2024, declining to ~225.5M by Jan 2026 through buybacks. No stock split occurred.

The EUR 585 figure from Morningstar likely refers to the pre-split price history or a different share class. Morningstar's current website shows WKL at a Wide Moat rating, but the specific fair value needs verification. This claim should be removed or corrected -- it adds confusion rather than clarity.

### 4.5 The "Near-Zero Bear Case MoS" is Inadequate for a Falling Knife

The thesis calculates bear case FV at EUR 68.88, which at the thesis price of EUR 67.70 showed +1.7% MoS. However:

- Current price is EUR 65.72, meaning the bear case FV is now +4.8% above the current price (DCF tool confirms EUR 68.88)
- But this is a stock making new 52-week lows weekly
- The bear case assumes 4% growth and 9.5% WACC -- but what if AI disruption is worse? What if growth goes to 2-3% organic? What if WACC should be 10%+ given terminal AI uncertainty?

**A more aggressive bear case:** Growth 2%, WACC 10%, Terminal 1.5% -- this could yield FV of ~EUR 50-55, implying significant downside risk.

The thesis's bear case is not actually bearish enough for a company facing existential questions about AI disruption of its core business model.

---

## 5. VALUATION VERIFICATION

### DCF Cross-Check (Tool Output)

| Scenario | Thesis FV | Tool FV (Feb 11) | Difference | Notes |
|----------|-----------|-------------------|------------|-------|
| Bear (4%, 9.5%, 2%) | EUR 68.88 | EUR 68.88 | 0% | Matches exactly |
| Base (6%, 8.5%, 2.5%) | EUR 98.96 | EUR 98.96 | 0% | Matches exactly |
| Bull (8%, 8%, 2.5%) | N/A | N/A | N/A | Not re-run |
| Default scenarios | N/A | EUR 85.22 | N/A | Tool's own base: EUR 85.22 |

The DCF tool confirms the thesis's numbers. The FV calculations are arithmetically correct.

### Updated MoS at Current Price (EUR 65.72)

| Metric | Thesis (Feb 7, EUR 67.70) | Current (Feb 11, EUR 65.72) |
|--------|---------------------------|------------------------------|
| MoS vs Base DCF | +46.2% | +50.6% |
| MoS vs Weighted FV (EUR 94.28) | +39.3% | +43.5% |
| MoS vs Bear DCF | +1.7% | +4.8% |
| MoS vs EV/EBIT (EUR 87.26) | +28.9% | +32.8% |

The MoS has improved slightly due to the further price decline. However, this also means the stock has NOT found a floor, which is concerning.

### EV/EBIT Cross-Check

The thesis uses 15x EV/EBIT on EUR 1,600M adjusted operating profit = EUR 24B EV. After net debt (EUR 4.31B), equity = EUR 19.69B / 225.6M shares = EUR 87.26.

**Adversarial challenge:** The 15x multiple is derived as: 14x base + 1x ROIC + 1x margins + 1x recurring - 2x AI = 15x. But peers Thomson Reuters and RELX now trade at ~14-15x EV/EBIT post-crash. WKL at 15x assumes it deserves the SAME multiple as peers, even though WKL is smaller and arguably more exposed to AI disruption in specific segments. A more conservative 13x multiple would give:

EV = EUR 1,600M x 13x = EUR 20,800M
Equity = EUR 20,800M - EUR 4,310M = EUR 16,490M
FV = EUR 16,490M / 225.6M = EUR 73.10

This gives a FV range of EUR 73-87 from the EV/EBIT method, depending on multiple selection.

### Adversarial Fair Value

Combining the DCF and EV/EBIT methods with more conservative assumptions:

| Method | FV (Thesis) | FV (Adversarial) | Change |
|--------|------------|-------------------|--------|
| DCF Base | EUR 98.96 | EUR 85.22 (tool default) | -14% |
| EV/EBIT | EUR 87.26 | EUR 73.10 (13x) | -16% |
| Weighted (60/40) | EUR 94.28 | EUR 80.37 | -15% |

**Adversarial Weighted FV: EUR 80 (range EUR 73-85)**

At current price EUR 65.72, this gives MoS of +22% (vs thesis's +39%). This is still positive and adequate for Tier B, but significantly lower than the thesis claims.

---

## 6. WHAT THE THESIS GETS RIGHT

To be fair, the thesis has several strong elements:

1. **The AI-segment analysis is fundamentally correct.** The market IS conflating legal research (vulnerable) with tax compliance (not vulnerable) and clinical decision support (not vulnerable). This is the core of the investment thesis and it holds up under scrutiny.

2. **The recurring revenue model is genuinely defensive.** 84% recurring, <1% of customer costs, extreme switching costs -- these are real barriers. AI cannot replicate the workflow + compliance + data integration overnight.

3. **The company IS actively integrating AI.** CCH Axcess Expert AI and UpToDate Expert AI launched in 2025. Over 50 health systems deploying UpToDate Expert AI enterprise-wide. This is a company that is embracing AI, not ignoring it.

4. **Fundamentals through 9M 2025 are strong.** 6% organic growth, 15% cloud growth, guidance reaffirmed, margins expanding. There is NO evidence of AI disruption in the actual numbers yet.

5. **The WATCHLIST verdict is prudent.** Waiting for FY2025 results (Feb 25) before buying is smart. The thesis correctly identifies the catalyst and the risk of catching a falling knife.

---

## 7. OVERALL ADVERSARIAL VERDICT

### What Changed

| Item | Thesis | Adversarial | Impact |
|------|--------|-------------|--------|
| QS | 75 (Tier A borderline) | 72-75 (Tier B, treat as B) | Minor -- sizing/MoS expectations |
| Revenue at risk from AI | 8-10% | 10-15% | Moderate -- widens bear case |
| H1 2025 organic growth | "6%" | 5% (9M was 6%) | Minor factual correction |
| Recurring revenue | 84% | 84% (FY2024 was 82%) | Confirmed |
| ROIC | 18.1% | 13.3% standard / 18.1% adjusted | Significant -- affects spread |
| Weighted FV | EUR 94.28 | EUR 80 (range 73-85) | Significant -- MoS drops from 39% to 22% |
| Bear case FV | EUR 68.88 | EUR 50-55 (severe bear) | The thesis bear is not bearish enough |
| Morningstar split claim | "7:1 split" | No split occurred | Factual error in thesis |

### Verdict: WATCHLIST MAINTAINED, but with Revised Parameters

The core thesis is sound: WKL is a high-quality business with defensible moats being sold off on AI fear that affects only 10-15% of its revenue. However, the original thesis is too optimistic in three specific areas:

1. **Fair value is closer to EUR 80 than EUR 94** (15% lower)
2. **The QS should be treated as Tier B** (72, not borderline Tier A at 75)
3. **The bear case should be more severe** (EUR 50-55 in true disaster, not EUR 69)

### Revised Standing Order Recommendation

| Parameter | Thesis | Adversarial Revised |
|-----------|--------|---------------------|
| Entry price | EUR 65.00 | EUR 55-58 |
| MoS at entry | 31% (vs adversarial FV EUR 80) | 28-31% |
| ADD trigger | EUR 55.00 | EUR 48-50 |
| Sizing | 3.3-3.6% | 3.0-3.5% |
| Tier for sizing | Tier A/B | Tier B |

**Rationale:** The FY2025 results on Feb 25 are the critical catalyst. If results show continued 6%+ organic growth with healthy cloud metrics, a buy at EUR 55-58 provides adequate MoS for a Tier B business. If results show deceleration below 5% organic, the thesis weakens materially and the entry price should be lowered further.

### Key Dates

- **Feb 25, 2026:** FY2025 Full-Year Results -- THE catalyst
- **Feb 23, 2026:** EUR 200M buyback program ends -- removes floor support
- **Late March 2026:** Annual report publication

---

## 8. KILL CONDITIONS (Verified and Enhanced)

Original kill conditions are reasonable. Adding:

7. **AI companies launch tax/compliance plugins** -- If Anthropic or OpenAI announce plugins for tax prep, clinical decision support, or regulatory compliance (not just legal), this would validate the market's fear that AI disruption extends beyond the 16% legal division.
8. **ROIC falls below WACC** -- Per the portfolio's established pattern (8/8 positions with ROIC < WACC were sold), if standard ROIC drops below WACC, this becomes an automatic sell signal.

---

## META-REFLECTION

### Incertidumbres/Dudas

1. **The ROIC discrepancy (18.1% company-adjusted vs 13.3% standard) is material.** The thesis uses the company figure without qualification. For QS scoring, the tool uses a figure closer to the standard calculation (5.4pp spread). This needs resolution -- the analyst should explicitly state which ROIC methodology is used and why.

2. **The stock is still falling.** It was EUR 67.70 on Feb 7, EUR 65.72 today, and the 52-week low is EUR 65.14. A stock making persistent new lows despite an allegedly irrational selloff could mean the selloff is NOT irrational. The market may know something about AI disruption speed that I don't.

3. **No sector view exists for professional information services.** The thesis itself flags this (error #30/#42 pattern). WKL is classified under "Industrials" by yfinance and "Technology" in our sector views, but it belongs to neither. A dedicated sector view covering WKL, RELX, Thomson Reuters, and Verisk would provide better competitive context.

### Sugerencias para el Sistema

1. **Create a `professional-information-services` sector view** BEFORE any purchase of WKL. This is a hard gate (error pattern #30/#42).

2. **The quality_scorer.py could benefit from a `--sector-override` parameter.** WKL classified as "Industrials" inflates its gross margin premium (+44.9pp) because it is compared to actual industrials, not information services peers. A manual sector override would produce more meaningful comparisons.

3. **Track AI plugin launches systematically.** Multiple portfolio holdings face AI disruption risk (ADBE, AUTO.L, WKL). A systematic tracker of AI product launches by major AI companies (Anthropic, OpenAI, Google) and their impact on incumbent business models would be valuable.

### Anomalias Detectadas

1. **Price continuing to fall post-thesis is unusual.** Most of our adversarial reviews catch thesis inflation in established positions. Here, the thesis was written 4 days ago and the stock is already lower. This could indicate: (a) broader market weakness, (b) continued AI sector rotation, or (c) informed selling ahead of FY2025 results.

2. **The EUR 200M buyback ending Feb 23 (2 days before earnings) is suspiciously timed.** The company will stop buying back shares just before announcing results. If results are bad, there will be no buyback support. If results are good, the stock should rise on its own. This timing suggests management is cautious about what the results will show.

3. **BofA upgraded to Buy with EUR 165 target on Feb 2, ONE DAY before the 13% crash.** This is a poor timing signal from an analyst, and the EUR 165 target is now 151% above the current price. Either the analyst is spectacularly right (long term) or the target is stale. No revision has been published.

### Preguntas para Orchestrator

1. Should we wait for FY2025 results (Feb 25) before setting any standing order? The thesis recommends waiting, and the adversarial review agrees. But the stock could bounce before results if AI fears fade.

2. Is 22% MoS (vs adversarial FV EUR 80) sufficient for a Tier B position with AI disruption risk? Precedent MoS for Tier B: HRB 42% (sold at 0%), EDEN.PA 35% initial. WKL at 22% MoS is at the lower end of precedents.

3. The missing professional-information-services sector view is a hard blocker per error patterns #30/#42. Should we create it now or wait until a BUY decision is closer?

---

**Adversarial Review Conclusion:**

The WKL thesis is **DIRECTIONALLY CORRECT** -- this is a high-quality business being sold off on AI fear that primarily affects 10-15% of its revenue. However, the thesis is **QUANTITATIVELY OPTIMISTIC** by ~15% on fair value and borderline on quality tier classification. The WATCHLIST verdict is correct. The entry price should be lowered from EUR 65 to EUR 55-58, and the FY2025 results on Feb 25 should be the decision gate.

**Revised WATCHLIST parameters: Entry EUR 55-58 post-earnings confirmation, Tier B sizing (3-3.5%), FV EUR 80 (range 73-85), kill conditions enhanced with AI plugin expansion and ROIC < WACC triggers.**

---

Sources:
- [Wolters Kluwer 2025 Nine-Month Trading Update](https://www.wolterskluwer.com/en/news/wolters-kluwer-2025-nine-month-trading-update)
- [Wolters Kluwer 2025 Half-Year Report](https://www.wolterskluwer.com/en/news/wolters-kluwer-2025-half-year-report)
- [Wolters Kluwer 2024 Full-Year Report](https://www.wolterskluwer.com/en/news/wolters-kluwer-2024-full-year-report)
- [Morningstar: Thomson Reuters, RELX, and Wolters Stocks Crushed After Anthropic Debuts Claude Legal Plug-In](https://www.morningstar.com/stocks/reuters-relx-wolters-stocks-crushed-after-anthropic-debuts-claude-legal-plug-in)
- [Artificial Lawyer: Claude Crash Impact is Irrational](https://www.artificiallawyer.com/2026/02/04/claude-crash-impact-on-thomson-reuters-lexisnexis-is-irrational/)
- [StockTitan: Wolters Kluwer Reaffirms 2025 Outlook; Organic Growth 6%](https://www.stocktitan.net/news/WTKWY/wolters-kluwer-2025-nine-month-trading-9opqem01s5m6.html)
- [StockTitan: WKL Share Buyback Jan 29 - Feb 4](https://www.stocktitan.net/news/WTKWY/share-buyback-transaction-details-january-29-february-4-vs1hkve2wm3y.html)
- [Investing.com: Wolters Kluwer Upgraded to Buy at BofA](https://www.investing.com/news/analyst-ratings/wolters-kluwer-stock-rating-upgraded-to-buy-at-bofa-93CH-3975752)
- [LawNext: Anthropic's Legal Plugin May Be Opening Salvo](https://www.lawnext.com/2026/02/anthropics-legal-plugin-for-claude-cowork-may-be-the-opening-salvo-in-a-competition-between-foundation-models-and-legal-tech-incumbents.html)
- [Winbuzzer: Anthropic's Legal AI Triggers $285B Software Market Selloff](https://winbuzzer.com/2026/02/05/anthropic-legal-ai-triggers-285b-market-selloff-xcxwbn/)
- [GURUFOCUS: Wolters Kluwer ROIC](https://www.gurufocus.com/term/ROIC/WTKWY/Return%2Bon%2BInvested%2BCapital/Wolters+Kluwer+NV)
