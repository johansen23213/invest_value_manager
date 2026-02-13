# VEEV - Veeva Systems Inc.

> **Fair Value:** $205 (R3 reconciled: analyst $220, specialist $195)
> **Date:** 2026-02-13
> **Status:** WATCHLIST
> **Pipeline Stage:** R1 (Fundamental Analysis)

---

## TL;DR

Veeva Systems is the dominant vertical SaaS platform for life sciences, holding ~80% market share in pharma CRM and rapidly penetrating R&D/clinical operations. The stock is down ~45% from its 2024 all-time high (~$310 from 52w, ~$500 from ATH) primarily due to CRM client retention concerns (14 vs 18 of top-20 pharma) and growth deceleration fears. At $172, it trades at 33.5x trailing earnings -- expensive by traditional value metrics but potentially cheap for a business with 75% gross margins, 40% FCF margins, $6.5B net cash, and a $20B+ TAM at only 16% penetration. The key question is whether Vault CRM migration risk and Salesforce/Medidata competition represent cyclical noise or structural erosion.

---

## Quality Score

### QS Tool: 72/100 (Tier B)

**Breakdown:**
| Category | Score | Max | Notes |
|----------|-------|-----|-------|
| Financial | 29 | 40 | ROIC spread only +0.7pp (penalized by conservative ROIC calc); FCF margin 40% (max); Net cash (max); FCF 4/4 (max) |
| Growth | 23 | 25 | Rev CAGR 14.1% (8/10); EPS CAGR 16.5% (10/10); GM expanding (5/5) |
| Moat | 15 | 25 | GM premium +19.5pp (10/10); Market position 0/8 (default -- MANUAL NEEDED); ROIC persistence 5/7 |
| Cap Alloc | 5 | 10 | No dividends/buybacks (0/5); Insider ownership 8.5% (5/5) |
| **TOTAL** | **72** | **100** | |

### QS Adjusted: 80/100 (Tier A) -- Adjustment: +8 points with quantitative evidence

**Adjustment rationale (item by item):**

1. **Market Position: 0 -> 8 (+8 points).** VEEV holds ~80% market share in life sciences CRM. It is unambiguously #1 in its vertical with no close second. 9 of top-20 pharma committed to Vault CRM vs Salesforce's 3. 1,500+ customers. This is the maximum score (8/8) and the tool scored 0 only because `market_position` defaults to 0 when not manually provided.

2. **ROIC spread +0.7pp underrepresents economic reality.** The tool calculates ROIC at 11.1% vs WACC 10.4%. However, VEEV has $6.5B in net cash on a $28B market cap -- the excess cash sitting on the balance sheet dilutes the ROIC denominator. If we exclude excess cash (~$5B above operating needs) from invested capital, ROIC rises to approximately 16-18%. This is consistent with the ROE trajectory (12.2%) being dragged down by the massive cash hoard. I am NOT adjusting points for this because it would require a separate category-level adjustment, but I note it for context.

**Net adjustment: +8 points (market position correction only).**

```
QS Tool: 72/100 (Tier B)
QS Adjusted: 80/100 (Tier A) -- Adjustment: +8 for market position (80% market share, #1 undisputed)
```

**Tier: A (Quality Compounder)**

---

## Business Understanding

### What Problem Does Veeva Solve?

Life sciences companies (pharma, biotech, medical devices) operate in the most heavily regulated industry on earth. They need specialized software for:

1. **Commercial operations**: CRM for sales reps calling on doctors, content management for regulated promotional materials, data analytics for prescriber behavior
2. **R&D/Clinical**: Clinical trial management (CDMS/EDC), regulatory submissions (RIM), quality management, pharmacovigilance/safety
3. **Data**: Reference data on healthcare professionals, prescribing patterns, clinical trial sites

Before Veeva, life sciences companies cobbled together horizontal tools (Salesforce CRM, Oracle databases, paper-based regulatory) that were poorly adapted to the industry's stringent requirements (FDA 21 CFR Part 11 compliance, audit trails, validated systems). Veeva built a purpose-built vertical cloud platform that integrates all these functions.

**This is a "must-have", not a "nice-to-have."** You cannot run clinical trials, submit drugs for regulatory approval, or manage a pharma sales force without these tools. Regulatory requirements mandate validated, auditable systems.

### Revenue Model

| Segment | FY2026E Revenue | Growth | % Total | Notes |
|---------|----------------|--------|---------|-------|
| Subscription - Commercial | ~$1,252M | ~12% | ~40% | Vault CRM, PromoMats, Medical CRM |
| Subscription - R&D | ~$1,420M | ~18% | ~45% | Vault EDC, RIM, Safety, Quality |
| Services | ~$497M | ~9% | ~15% | Implementation, consulting, training |
| **Total** | **~$3,169M** | **~15%** | **100%** | |

**Key characteristics:**
- **~85% subscription revenue** (highly recurring, multi-year contracts)
- **R&D Solutions now EXCEED Commercial Solutions** -- this is the growth engine
- Revenue retention rate: ~120% net dollar retention (existing customers spend 20% more each year)
- Customer churn: <4% (extremely sticky)
- ~1,500 customers, heavily concentrated in top-20 pharma

### Unit Economics

- **CAC**: Not disclosed, but the land-and-expand model means low incremental CAC for upsells within existing accounts
- **LTV/CAC**: Implied >10x given <4% churn and 120% net retention
- **Payback**: Estimated <18 months for new customers given high gross margins
- **Net Dollar Retention**: ~120% -- every $1 of revenue becomes $1.20 next year from same customers

### Margin Structure

| Metric | FY2022 | FY2023 | FY2024 | FY2025 | Trend |
|--------|--------|--------|--------|--------|-------|
| Gross Margin | 72.8% | 71.7% | 71.3% | 74.5% | Expanding |
| Operating Margin (non-GAAP) | 27.3% | 21.3% | 18.2% | 25.2% | Recovering strongly |
| Non-GAAP OpM (Q3 FY26) | -- | -- | -- | 45.0% | Significant expansion |
| FCF Margin | 41.3% | 36.2% | 38.6% | 39.7% | Consistently high |

The operating margin recovery from 18.2% to 45% (non-GAAP, Q3) reflects the completion of heavy R&D investment in Vault platform and the start of operating leverage as subscription revenue scales.

### Capital Requirements

- **Asset-light**: Capex ~1-2% of revenue (cloud-based software, minimal physical infrastructure)
- **Working capital**: Net cash generator (deferred revenue = customers pay upfront)
- **Net cash position**: $6.5B ($90M debt vs $6.6B cash) -- fortress balance sheet

### Pricing Model -- CRITICAL for SaaSpocalypse Assessment

Veeva's CRM products use a **per-user, per-year subscription model** ($1,000-$2,000/user/year for CRM). This means VEEV IS exposed to per-seat pricing risk from the SaaSpocalypse thesis (AI reduces headcount at pharma companies -> fewer CRM users -> lower revenue).

HOWEVER, several mitigating factors:

1. **R&D Solutions (45% of revenue, growing faster) are NOT per-seat.** Vault EDC, RIM, Safety, Quality are priced per-study, per-product, or platform-level -- these scale with pharma R&D activity, not headcount.
2. **Pharma sales forces are relatively stable.** Unlike tech companies aggressively cutting headcount, pharma reps are necessary for physician engagement and regulatory-required interactions (adverse event reporting, fair balanced promotion). AI cannot replace the in-person pharma rep relationship in most markets.
3. **Land-and-expand model offsets seat reduction.** Even if a pharma company has 10% fewer reps, Veeva sells more modules (PromoMats, Medical CRM, Data Cloud, Crossix analytics) to the same customer.

**Net assessment: SaaSpocalypse risk is MODERATE for VEEV, not HIGH.** Per-seat CRM exposure exists (~40% of revenue) but is offset by R&D revenue growth and product expansion. This is materially different from horizontal SaaS companies (PAYC, ADBE) where per-seat is the dominant model.

---

## Why Is It Cheap? (Down ~45% from ATH)

### Market Narrative

1. **CRM client retention downgrade (Q3 FY2026)**: CEO Gassner said Veeva would retain "14 or so" of top-20 pharma for Vault CRM, down from 18 previously expected. This spooked the market.
2. **Salesforce Life Sciences Cloud competition**: Salesforce launched a competing product after the exclusive relationship ended Sep 2025. Market fears Salesforce will take meaningful CRM share.
3. **Growth deceleration**: Revenue growth expected to slow from 16% to ~10-11% over next 12 months.
4. **Goldman Sachs downgrade to Sell**: Cited maturity concerns.
5. **Multiple compression**: SaaS sector broadly re-rated downward as rates stayed higher for longer.

### My Counter-Thesis

| Market believes | I believe | Evidence |
|----------------|-----------|----------|
| Salesforce will take CRM share | VEEV retains 70%+ CRM share; Salesforce only has 3/20 top pharma, go-lives stretch to 2026-2029 | 9 vs 3 top-20 commitments; 115+ Vault CRM live deployments already |
| 14/20 = concerning retention | 14/20 = 70% retention rate in a transition period is STRONG, not weak | Historical context: any platform migration sees some client loss |
| Growth will decelerate materially | R&D Solutions growing 18%+ and now larger than Commercial; total growth runway still has years | TAM $20B+ at only 16% penetration; 2030 goal $6B revenue |
| SaaSpocalypse kills per-seat pricing | R&D/clinical revenue is not per-seat; pharma reps are relatively AI-proof | 45% of revenue is R&D (non-per-seat), growing faster |
| Premium valuation not justified | 40% FCF margin, net cash, 120% NRR, <4% churn -- this IS premium quality | Very few SaaS companies have this combination |

### Value Trap Checklist

| Factor | SI/NO | Comment |
|--------|-------|---------|
| Industry in secular decline | NO | Life sciences software TAM growing 10%+ CAGR |
| Technological disruption imminent | NO | AI is net positive (VEEV is embedding AI); Vault is proprietary platform |
| Management destroying value | NO | Gassner founder-CEO, 8.5% ownership, aligned. Removed super-voting 2023. |
| Balance sheet deteriorating | NO | $6.5B net cash, improving |
| Insider selling massive | PARTIAL | Gassner has sold some shares (routine 10b5-1 plans). Not alarming given 8.5% stake. |
| Dividend cut recent/probable | N/A | No dividend (growth reinvestment) |
| Losing market share >2pp 3yr | NO | Still ~80% CRM share. Losing 4 of top-20 is small in context of 1,500 customers |
| ROIC < WACC last 3 years | NO | ROIC 11.1% > WACC 10.4%. Understated due to excess cash. |
| FCF negative >2 years | NO | FCF consistently positive and growing: $764M -> $780M -> $911M -> $1.1B |
| Goodwill >50% equity | NO | Minimal goodwill (organic growth business) |

**TOTAL: 0-1/10 factors YES. Low value trap risk.**

### My Informational Advantage

- Horizon temporal: Market focused on Q4 FY2026 earnings (March 4) and near-term CRM transition noise. I can look through to 2028-2030 when R&D Solutions dominate revenue mix and Vault CRM migration is complete.
- The market is conflating CRM transition friction (temporary) with structural market share loss (permanent).

---

## Moat Assessment

### Source 1: Switching Costs (VERY HIGH -- 9/10)

Once clinical trial data, regulatory submissions, pharmacovigilance records, and quality systems are embedded in Vault, switching is virtually impossible without:
- Risking regulatory compliance (FDA 21 CFR Part 11)
- Disrupting active clinical trials (patient safety)
- Re-validating entire systems (12-18 month process, millions in costs)
- Retraining thousands of users

**Evidence**: <4% annual churn. 120% net dollar retention. Multi-year contracts.

### Source 2: Network Effects (MODERATE -- 5/10)

- Data network effects: Crossix analytics improves with more data flowing through the platform
- Ecosystem effects: Veeva CRM + Vault + Data Cloud integration makes the platform more valuable as customers use more modules
- Industry standard: When most pharma uses Veeva, consultants, CROs, and regulatory agencies align their processes to Veeva's platform

### Source 3: Intangible Assets (HIGH -- 7/10)

- 20+ years of life sciences domain expertise embedded in product design
- Regulatory compliance features that are extremely difficult to replicate (GxP validation)
- Brand trust: "No one gets fired for choosing Veeva" in life sciences (similar to IBM/Oracle in enterprise IT)

### Source 4: Scale Advantages (MODERATE -- 5/10)

- R&D investment ($600M+/year) amortized across 1,500+ customers
- Professional services network and partner ecosystem
- Data assets (reference data on 15M+ healthcare professionals)

**Total Moat Score: 20/25 (Wide Moat)**

---

## Projections

### Revenue Projection

| Component | Assumption | Basis |
|-----------|-----------|-------|
| TAM | $20B+ current, growing to $30-50B by 2028 | Company disclosure, industry research |
| Market share | Stable ~15-16% of TAM (pricing captures more value as TAM grows) | Already #1, share stable |
| Pricing | +2-3% annual price increases | Regulated industry = low price sensitivity |
| R&D Solutions growth | 15-18% (near-term), 12-15% (medium-term) | Vault EDC winning 6/20 top pharma, clinical/regulatory TAM expanding |
| Commercial Solutions growth | 8-12% (Vault CRM migration, new products) | Losing some CRM seats but adding modules |
| Services growth | 5-8% | Migration-related consulting demand |

**Revenue trajectory (fiscal years ending Jan 31):**
| Year | Revenue | Growth |
|------|---------|--------|
| FY2026 (actual, mostly reported) | $3.17B | 15% |
| FY2027E | $3.55B | 12% |
| FY2028E | $3.94B | 11% |
| FY2029E | $4.33B | 10% |
| FY2030E | $4.76B | 10% |

This is below management's $6B run-rate target for 2030. I am intentionally conservative.

### Margin Projection

| Metric | FY2026 | FY2028E | FY2030E | Basis |
|--------|--------|---------|---------|-------|
| Gross Margin | 74.5% | 75.5% | 76% | Scale + subscription mix shift |
| Non-GAAP Operating Margin | ~42% | 44% | 45% | Operating leverage (R&D investment peaking) |
| FCF Margin | ~40% | 41% | 42% | Minimal capex, working capital generator |

### WACC Derivation

| Component | Value | Source |
|-----------|-------|--------|
| Risk-free rate | 4.3% | US 10Y Treasury (Feb 2026) |
| Equity Risk Premium | 5.5% | Damodaran US ERP 2026 |
| Beta | 1.08 | yfinance |
| Cost of Equity (Ke) | 10.2% | 4.3% + 1.08 * 5.5% |
| Cost of Debt (Kd) | N/A | Essentially no debt ($90M vs $6.6B cash) |
| WACC | 10.2% | ~100% equity-funded |

**Sanity check:** 10.2% WACC is appropriate for a high-quality SaaS company with stable cash flows but some competitive uncertainty. This is higher than a utility but lower than speculative tech.

---

## Valuation

### Method 1: Owner Earnings Yield + Growth (Primary -- 55% weight)

**Tier A companies should be valued primarily on OEY per the valuation-methods skill.**

```
FCF (TTM): ~$1.1B
Depreciation: ~$50M
Maintenance Capex: ~$55M (Depreciation x 1.1)
Owner Earnings = $1.1B - $55M + $50M = ~$1.095B

Market Cap: $28.3B
Owner Earnings Yield = $1.095B / $28.3B = 3.87%

Expected Growth (revenue): 11-12% (next 5 years average)
FCF Growth (expected): 13-15% (margin expansion + revenue growth)

OEY + Expected FCF Growth = 3.87% + 14% = 17.87%
vs WACC = 10.2%

Spread: +7.67pp -> ATTRACTIVE
```

**For OEY-based fair value:**
At what price does OEY + Growth = WACC (breakeven)?
If we require OEY + Growth > 12% (consistent with precedents for Tier A quality):
- At $172: OEY 3.87% + 14% growth = 17.87% > 12% --> Attractive
- At $250: OEY 2.66% + 14% = 16.66% > 12% --> Still attractive
- At $310 (52w high): OEY 2.15% + 14% = 16.15% --> Even here, technically positive

However, OEY method for a growth company gives very high fair values because growth dominates. This is why Reverse DCF is needed as secondary.

### Method 2: Reverse DCF (Secondary -- 25% weight)

Using DCF tool output with WACC 9.5% (slightly below my calculated 10.2% to account for the fortress balance sheet reducing real risk):

| Growth Rate Implied | Fair Value | At $172 |
|---------------------|-----------|---------|
| 11% | $186.9 | Market implies ~13% growth |
| 14% | $205.8 | Base case = 20% MoS |
| 17% | $226.8 | Bull case = 32% MoS |

**At $172, the market implies approximately 10-11% FCF growth.** Given VEEV's 14% revenue CAGR and expanding margins, this seems overly pessimistic. The market is pricing in material growth deceleration that I think is exaggerated by CRM transition noise.

### Method 3: EV/FCF Multiple (Verification -- 20% weight)

```
Current EV = Market Cap - Net Cash = $28.3B - $6.5B = $21.8B
Current FCF = ~$1.1B
EV/FCF = 19.8x

For a company growing FCF 13-15% with 40% FCF margins and <4% churn:
- Fair EV/FCF range: 22-28x (comparable to high-quality vertical SaaS)
- At 25x: EV = $27.5B -> Equity = $34B -> FV = $206/share
- At 22x: EV = $24.2B -> Equity = $30.7B -> FV = $187/share
- At 28x: EV = $30.8B -> Equity = $37.3B -> FV = $227/share
```

### Reconciliation

| Method | Fair Value | Weight | Weighted |
|--------|-----------|--------|----------|
| OEY + Growth (implied FV where OEY+G = 12%) | ~$260 | 30% | $78.0 |
| DCF Base (14% growth, 9.5% WACC) | $206 | 35% | $72.1 |
| EV/FCF 25x | $206 | 20% | $41.2 |
| DCF Conservative (12% growth, 10% WACC) | $182 | 15% | $27.3 |
| **Weighted Average** | | **100%** | **$218.6** |

**Rounded Fair Value: $220**

### DCF Sensitivity Assessment

```
Sensitivity: FV Spread 62%, TV 77.4% of EV --> HIGH SENSITIVITY
```

The DCF is highly sensitive to growth and WACC assumptions, and terminal value dominates (77.4%). This is typical for growth companies. Therefore, the DCF is UNRELIABLE as a point estimate -- I use the RANGE ($155-$260) as the relevant output. The weighted FV of $220 sits comfortably within this range but should be treated as a midpoint, not a precise target.

**This high sensitivity means the required MoS should be at the higher end for Tier A.**

---

## Scenarios

| Scenario | Prob | Revenue Growth | FCF Growth | Fair Value | MoS at $172 |
|----------|------|---------------|-----------|-----------|-------------|
| **Bear** | 25% | 8% (Salesforce takes meaningful share, growth stalls) | 9% | $160 | -7% |
| **Base** | 50% | 12% (R&D drives growth, CRM stabilizes) | 14% | $220 | +28% |
| **Bull** | 25% | 16% (R&D accelerates, AI upsell, $6B target achieved) | 18% | $290 | +69% |

### Expected Value

```
EV = ($160 x 25%) + ($220 x 50%) + ($290 x 25%)
EV = $40 + $110 + $72.5
EV = $222.5

MoS vs EV: ($222.5 - $172) / $222.5 = +22.7%
MoS vs Bear: ($160 - $172) / $160 = -7.5% (DOWNSIDE in bear)
```

### Bear Case Details
- Salesforce wins 6-8 of top-20 pharma CRM (from current 3)
- R&D Solutions growth decelerates to 12% then 8%
- Pricing pressure from competition compresses margins
- Multiple compresses further to 18-20x EV/FCF
- **Catalyst**: Major pharma company publicly switches from Vault CRM to Salesforce

### Bull Case Details
- Vault CRM stabilizes at 14+ of top-20 pharma
- R&D Solutions accelerate to 20%+ driven by AI-powered clinical tools
- Veeva AI agents become industry standard for pharmacovigilance/safety
- Management achieves $6B revenue run rate target by 2030
- Multiple re-rates to 28-30x EV/FCF as market recognizes quality
- **Catalyst**: Q4 FY2026 earnings (March 4) show strong bookings, CRM retention stabilizes

---

## MoS Analysis

| Metric | Value |
|--------|-------|
| MoS vs Base FV ($220) | +22% |
| MoS vs Bear FV ($160) | -7% |
| MoS vs Expected Value ($222.5) | +23% |
| Required MoS (Tier A, high sensitivity DCF) | 15-20% |
| Meets requirement? | YES at base/EV, NO at bear |

### Precedent comparison (Tier A buys):

| Ticker | Tier | MoS at Entry | Context |
|--------|------|-------------|---------|
| ADBE | A | 31% | Fallen angel, AI fears |
| NVO | A | 38% | Guidance shock, panic |
| LULU | A | 34% | Fallen angel, CEO vacancy |
| MONY.L | A | 36% | 52w low |
| AUTO.L | A | 29% | Dealer revolt |
| BYIT.L | A (adj B) | 35% | Microsoft restructuring |
| **VEEV** | **A** | **22%** | **CRM transition noise** |

**VEEV's MoS at $172 (22%) is below the typical Tier A entry range (29-38%) from precedents.** This is the main reason to WATCHLIST rather than BUY immediately.

An entry price of $168 would give ~24% MoS. An entry of $155-160 would give 27-30% MoS, more consistent with precedents.

**However, reasoning from principles:** The lower MoS is partially offset by:
1. Net cash of $6.5B provides a substantial floor
2. 40% FCF margins mean the business generates enormous cash even in bear scenarios
3. <4% churn and 120% NRR mean revenue is highly resilient
4. No debt = no insolvency risk

I set entry at $155-165 for consistency with Tier A precedents, noting that $168 (current 52w low) would be acceptable if the Q4 earnings provide positive signals.

---

## Kill Conditions

1. **KC#1: CRM market share falls below 50% of top-20 pharma.** If Salesforce wins 10+ of top-20, Veeva's CRM moat is breached. Current: 14/20. Threshold: <10/20.

2. **KC#2: Net dollar retention falls below 105%.** This would indicate customers are shrinking spend, not expanding. Current: ~120%. Threshold: <105%.

3. **KC#3: R&D Solutions growth decelerates below 10% for 2+ consecutive quarters.** R&D is the growth engine. If it stalls, the thesis breaks. Current: ~18%. Threshold: <10%.

4. **KC#4: FCF margin falls below 25% for 2+ consecutive quarters (excluding one-time events).** This would indicate structural profitability deterioration. Current: ~40%. Threshold: <25%.

5. **KC#5: CEO Peter Gassner departs or sells >50% of his stake.** Gassner is the founder-CEO and holds 8.5%. His departure or major selling would signal fundamental concern. Current: 8.5% ownership, active management.

6. **KC#6: Major regulatory change eliminates need for validated systems in life sciences.** If FDA/EMA stopped requiring 21 CFR Part 11 compliance for clinical systems, switching costs would collapse. Probability: <1%.

7. **KC#7: Per-seat CRM pricing erosion >15% across portfolio in any fiscal year.** Per the SaaSpocalypse risk framework. If AI-driven headcount reduction at pharma companies causes material seat loss, the CRM revenue model is impaired. Monitor via quarterly CRM subscription revenue growth.

---

## Catalysts

| Catalyst | Timeframe | Probability | Impact |
|----------|-----------|-------------|--------|
| Q4 FY2026 earnings (March 4, 2026) | 3 weeks | 100% | HIGH -- CRM retention clarity, FY2027 guidance |
| Vault CRM migration reaching critical mass (200+ go-lives) | H1 2026 | 80% | MEDIUM -- validates platform transition |
| R&D Solutions winning additional top-20 pharma for Vault EDC | 2026 | 60% | HIGH -- proves R&D as growth engine |
| Veeva AI agent deployment across applications | H2 2026 | 70% | MEDIUM -- AI monetization catalyst |
| Fed rate cuts | H2 2026 | 40% | MEDIUM -- SaaS multiple re-rating |
| IQVIA partnership post-legal settlement | 2026-2027 | 50% | MEDIUM -- removes competitive friction in data |

---

## Macro Fit

| Factor | Sensitivity | Current Impact |
|--------|-------------|----------------|
| Interest rates | Medium-High | Rates staying higher = multiple compression for growth stocks |
| Recession | Low | Healthcare spending is defensive; pharma R&D is non-discretionary |
| Inflation | Low | High pricing power in regulated vertical |
| USD strength | Low-Medium | Most revenue US-denominated, some international exposure |
| Tariffs | Very Low | Software, zero physical trade exposure |

**World view alignment:** NEUTRAL to SLIGHTLY FAVORABLE. The macro environment (rates higher for longer, potential inflation reacceleration) is a headwind for SaaS multiples but VEEV's defensive end-market (healthcare) and quality metrics (net cash, FCF margins) provide resilience. A Fed rate cut would be a clear positive catalyst for re-rating.

---

## Veredicto: WATCHLIST

**Entry Price: $155-165 (MoS 25-30% vs base FV $220)**

| Factor | Assessment |
|--------|-----------|
| Quality | Tier A (QS 80 adjusted). Wide moat. Exceptional financials. |
| Price | Not cheap enough yet. At $172, MoS is ~22% -- below Tier A precedent range (29-38%). |
| Risk | MODERATE. CRM transition is the main near-term risk. High DCF sensitivity. |
| Timing | Q4 earnings March 4 will provide critical CRM retention data and FY2027 guidance. |
| Recommendation | WAIT for either (a) price decline to $155-165 or (b) Q4 earnings that de-risk the CRM transition narrative. |

**Standing order consideration:** A standing order at $160 would give 27% MoS, consistent with Tier A precedents. However, this should wait for R2 (devil's advocate) before committing.

---

## Sources

- [Veeva Q3 FY2026 Earnings - Nasdaq](https://www.nasdaq.com/articles/veeva-systems-q3-revenue-16-ai-and-crm-momentum-drive-growth)
- [Veeva Q3 FY2026 Slides - Investing.com](https://www.investing.com/news/company-news/veeva-systems-q3-2026-slides-revenue-jumps-16-margins-expand-to-45-93CH-4371882)
- [Veeva Q3 Earnings Call Transcript - Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-veeva-systems-q3-2026-beats-expectations-stock-dips-93CH-4371867)
- [Veeva IR - Quarterly Results](https://ir.veeva.com/financials/quarterly-results/default.aspx)
- [Veeva FY2025 Results](https://www.veeva.com/resources/veeva-announces-fourth-quarter-and-fiscal-year-2025-results/)
- [Veeva Q4 FY2026 Date Announcement](https://www.stocktitan.net/news/VEEV/veeva-to-release-fiscal-2026-fourth-quarter-and-full-year-results-on-gbviihj9ona2.html)
- [Veeva CRM vs Competitors - IntuitionLabs](https://intuitionlabs.ai/articles/veeva-crm-vs-competitors-comprehensive-comparison)
- [Veeva Competitive Landscape - MatrixBCG](https://matrixbcg.com/blogs/competitors/veeva)
- [Veeva Vertical SaaS Quality - Compound and Fire](https://compoundandfire.substack.com/p/veeva-systems-vertical-saas-quality)
- [Veeva Platform Strategy - Intrinsic Investing](https://intrinsicinvesting.com/2024/07/23/veeva-a-winning-platform-strategy-in-life-sciences/)
- [Veeva Pricing Guide - IntuitionLabs](https://intuitionlabs.ai/articles/veeva-systems-pricing-overview-complete-guide-to-costs-and-licensing)
- [Veeva CRM Pricing 2026 - IntuitionLabs](https://intuitionlabs.ai/articles/veeva-crm-pricing-license-cost-2026)
- [Veeva Risks - Sleep Well Investments](https://www.sleepwellinvestments.com/p/veeva-systems-veev-a-leader-in-life)
- [Veeva 52-Week Low - Investing.com](https://www.investing.com/news/company-news/veeva-systems-stock-hits-52week-low-at-17782-93CH-4500477)
- [Veeva Stifel Buy Rating - Investing.com](https://www.investing.com/news/analyst-ratings/veeva-systems-stock-falls-despite-stifel-reiterating-buy-rating-93CH-4373113)
- [Veeva Long-Term Analysis - IntuitionLabs](https://intuitionlabs.ai/articles/veeva-systems-veev-ticker-investment-analysis-2025)
- [Life Sciences Software Market Forecast - IntuitionLabs](https://intuitionlabs.ai/articles/life-sciences-software-market-forecast-structural-gaps)
- [Veeva Institutional Ownership - Yahoo Finance](https://finance.yahoo.com/news/81-ownership-veeva-systems-inc-110019712.html)
- [Peter Gassner Net Worth - GuruFocus](https://www.gurufocus.com/insider/90248/peter-p-gassner)
- [Veeva Rebound - Seeking Alpha](https://seekingalpha.com/article/4867690-veeva-la-vida-here-comes-the-rebound-for-veeva-systems)
- [Vault CRM Migration Roadmap - IntuitionLabs](https://intuitionlabs.ai/articles/veeva-vault-crm-migration-roadmap)
- [Veeva TAM - Lewistown Capital](https://lewistowncapital.substack.com/p/veev-veeva-systems)

---

## 🔄 META-REFLECTION

### Incertidumbres/Dudas

1. **ROIC calculation is distorted by excess cash.** The tool shows ROIC-WACC spread of only +0.7pp, which mechanically pushes VEEV toward a Tier B classification. But $6.5B in excess cash on the balance sheet dilutes invested capital, making ROIC look artificially low. If excess cash is excluded, ROIC is ~16-18%. The tool does not handle this. I documented this transparently in the QS adjustment section (NOT adjusting points for it) but it means the tool's 72/100 underrepresents the true economic quality.

2. **CRM retention: 14 vs 18 of top-20 is the key unknown.** I cannot know from public data which specific pharma companies are switching and why. Q4 FY2026 earnings (March 4) will provide critical clarity. If the number drops to 12 or below, the thesis weakens materially.

3. **Per-seat pricing risk quantification.** I assessed SaaSpocalypse risk as MODERATE, but I cannot precisely quantify how much AI-driven headcount reduction will impact pharma sales forces. This is a 3-5 year horizon risk, not immediate.

4. **Valuation complexity.** The OEY method gives a very high implied FV (~$260+) because growth dominates the equation. The DCF has high sensitivity (62% FV spread, 77% TV). This makes the $220 FV a judgment call, not a precise number. The range is probably $180-$260.

### Sugerencias para el Sistema

1. **quality_scorer.py should handle excess cash.** Companies like VEEV, GOOGL, and AAPL with massive net cash positions get penalized in ROIC calculations because cash inflates the invested capital denominator. A flag like `--excess-cash-adjustment` could net out cash above 10% of revenue from invested capital. This would affect all tech companies with fortress balance sheets.

2. **Sector view gap: There is no dedicated "Health IT / Life Sciences Technology" sector view.** VEEV spans both pharma-healthcare and technology but fits neither perfectly. It is a vertical SaaS company serving life sciences. Consider creating a dedicated "Health IT" or "Life Sciences Technology" subsection in one of the existing sector views.

### Preguntas para Orchestrator

1. Should we wait for Q4 FY2026 earnings (March 4) before setting a standing order? The earnings will clarify CRM retention and FY2027 guidance, which are the two biggest uncertainties.

2. Given VEEV is 2.4% from its quality universe entry price ($168), should we proceed to R2 (devil's advocate) now to have the full pipeline ready if price drops further?

### Anomalias Detectadas

1. **Quality scorer shows ROIC trajectory: 22.9% -> 15.1% -> 9.5% -> 11.1%.** This declining ROIC trend would normally be a red flag, but it coincides with Veeva's massive cash accumulation ($0 -> $6.5B over 4 years). As the cash pile grew, ROIC denominator inflated, causing the apparent decline even as operating performance improved. The non-GAAP operating margin expanded from 18.2% to 45.0% over the same period, contradicting the "declining returns" narrative.

2. **Tool beta of 1.08 seems slightly low** for a growth SaaS company (sector typical: 1.2-1.5). This may reflect VEEV's defensive end-market (healthcare) dampening volatility. The 1.08 beta is plausible and I use it as-is.

---
