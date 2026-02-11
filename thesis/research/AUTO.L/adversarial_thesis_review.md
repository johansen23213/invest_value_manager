# Adversarial Position Review: AUTO.L (AutoTrader Group plc)

> Date: 2026-02-11
> Reviewer: Claude (review-agent, adversarial mode)
> Position: 65 shares @ 485.80 GBp | Current: 471.00 GBp | P&L: -3.1%
> Context: Adversarial review of existing Tier A position (claimed QS 79)

---

## QS Tool vs Thesis

### Quality Scorer Tool Output

| Category | Tool Score | Thesis Claim | Delta |
|----------|-----------|--------------|-------|
| **Financial Quality** | 40/40 | 39/40 | +1 (FCF 5/5 vs thesis 4/5) |
| **Growth Quality** | 11/25 | 13/25 | -2 (EPS data gap) |
| **Moat Evidence** | 7/25 | 22/25 | **-15 (major discrepancy)** |
| **Capital Allocation** | 5/10 | 5/10 | 0 |
| **TOTAL** | **63/100 (Tier B)** | **79/100 (Tier A)** | **-16 points** |

### Critical Discrepancy: Moat Evidence (7 vs 22)

The thesis claims 22/25 for moat, including:
- GM Premium: 10 pts (79% GM vs 50% sector = +29pp)
- Market Position: 8 pts (manually adjusted from tool's 5 to 8, citing "#1 by 10x margin")
- ROIC Persistence: 7 pts (based on 10+ years)

The tool scores only 7/25 because:
- **GM Premium: 0 pts** -- The tool compares against Communication Services sector median (50%). In the most recent year (2025), yfinance returns `nan` for gross margin, causing the tool to fail the comparison. This is a data gap issue, not a real quality deficit.
- **Market Position: 0 pts** -- The tool defaults to 0 (fixed in recent session, previously defaulted to 5). Manual assessment of #1 position is valid.
- **ROIC Persistence: 7 pts** -- Correctly scored.

### Adversarial QS Assessment

The tool's 63 score is **mechanically understated** due to two known biases (documented in decisions_log Session 52):
1. `market_position` default = 0 (no manual override in automated run)
2. `nan` gross margin in 2025 causes GM premium to fail

**Fair adversarial adjustment:**
- GM Premium: AUTO.L has 72-84% gross margin consistently. Vs 50% sector = +22-34pp premium. Score: 10/10 (justified).
- Market Position: 75% of all UK automotive classified minutes, 10x nearest competitor. Score: 8/8 (justified).
- Growth: EPS CAGR cannot be computed (nan in 2025). Revenue CAGR 11.6% is strong but only covers 3 years of data (FY2022-2025). With longer horizon, growth is closer to 7-8%. Thesis claim of 5+5 for Rev+EPS is reasonable but not verifiable for EPS. Score: 8-11/25 (conservative estimate).

**QS Adversarial Adjusted: 70-73/100 (Tier B, high end)**

This is BELOW the thesis claim of 79 (Tier A) by 6-9 points. The thesis inflated QS primarily through generous growth scoring that cannot be verified (EPS nan) and by rounding up moat assessment. AUTO.L is a strong Tier B company, not a clear Tier A.

| Score | Source | Tier |
|-------|--------|------|
| 63 | Tool (raw, with data gaps) | B |
| 70-73 | Adversarial adjusted | **B (high-end)** |
| 79 | Thesis claim | A (inflated) |

---

## What Has Changed Since Thesis (Feb 6, 2026)

### 1. Share Price Decline Continues
- Entry: 485.80 GBp (Feb 6)
- Current: 471.00 GBp (Feb 11)
- New 52-week low: 468.60 GBp (touched)
- Change since entry: -3.1%

### 2. Deal Builder Situation - More Detail Emerged
The thesis stated "165 cancellations out of ~13,500 = 1.2% noise." Updated data from trade press:
- **59 dealers fully cancelled** (not 165 as thesis stated -- 165 was the threat, 59 executed)
- **70+ dealers downgraded packages** (confirmed)
- **180+ dealers reduced advertising spend** (per internal dealer group polls, higher than the 70 in official figures)
- **3,000+ dealers joined Facebook protest group** (still active)
- April 2026 pricing event announced: **5.5% increase** (vs 8% last year -- a DECELERATION in pricing power)
- Jefferies downgraded to HOLD with target cut from 895p to 650p
- Berenberg cut target from 830p to 665p, ARPR growth forecast CUT from 7.5% to 5.2% for FY27

### 3. Analyst Consensus Deteriorating
- Jefferies: HOLD, 650p target (was BUY 895p)
- Berenberg: HOLD, 665p target (was 830p)
- Consensus average target: 710-770p (range across sources)
- 8 BUY, 7 HOLD, 1 SELL per recent data
- Consensus is shifting from BUY to HOLD

### 4. UK Used Car Market -- Positive
- 2025 used car sales: 7.8M units (+2.2% YoY) -- 3 consecutive years of growth
- 2026 forecast: +3% to ~8M units
- AutoTrader platform visits: 86.3M in January 2026 (strong)
- Used EV sales surging (+45.7%)
- BUT: supply headwinds loom -- 5-6 year old cars drop 25-30% in 2026

### 5. Competitor Dynamics
- Motors.co.uk acquired Cazoo assets (Jun 2024) and relaunching as competitor
- Motors.co.uk: 4M monthly visits vs AutoTrader's ~80M+ (still 20x smaller)
- Facebook Marketplace: 38M UK users, becoming largest US used car platform but UK share unclear
- No credible competitor has achieved >10% of classified minutes

### 6. Share Buyback Active
- Multiple buyback tranches in February 2026:
  - Feb 2: 430k shares @ 536p
  - Feb 3: 460k shares @ 517p
  - Feb 4: 462k shares @ 502p
  - Feb 9: 800k shares @ 479p
- Management buying back at current levels signals confidence

### 7. AI Disruption -- Slow but Real
- BCG: "AI agents will reshape automotive" but focused on dealership operations, not disintermediation
- AI search (ChatGPT, Google AI Overviews) reducing some classified browsing
- BUT: AutoTrader itself investing in AI (Co-Driver product launched April 2025)
- Timeline: 3-5+ years before AI fundamentally changes car buying behavior

---

## Thesis Assumptions Stress-Test

### Assumption 1: "Deal Builder backlash is cyclical, not structural"

**Thesis position:** Dealers complain every year. 165 cancellations out of 13,500 = noise. Same happened with Rightmove.

**Adversarial challenge:**
- The actual cancellations (59) were lower than thesis stated (165), BUT:
- The 5.5% April price increase (vs 8% last year) is the REAL signal
- Berenberg cut ARPR growth forecast from 7.5% to 5.2% -- this is MATERIAL
- If Deal Builder forces AutoTrader to moderate pricing, the growth trajectory changes permanently
- The Rightmove analogy is only partially valid: property agents have no alternative. Car dealers have Facebook Marketplace, Motors.co.uk, direct OEM sales
- "Proportionate and productive" response (Jefferies) does not mean resolved -- it means damage control

**Verdict: Thesis PARTIALLY valid.** The backlash was less severe than feared (59 vs 165 cancellations). But the PRICING POWER IMPACT is the real story. 5.5% vs 8% pricing = ARPR growth decelerating. This may not be cyclical but a new normal of constrained pricing power.

**Risk probability revision: 15% -> 25%** that pricing power is structurally constrained.

### Assumption 2: "75% market share is sustainable"

**Thesis position:** Network effects are unbreakable. Where would dealers go?

**Adversarial challenge:**
- Core classifieds market share is probably safe for now
- BUT three emerging threats:
  1. **Facebook Marketplace** -- 38M UK users, dominant in US for used cars. If it captures private seller market fully, AutoTrader's growth TAM shrinks
  2. **OEM direct-to-consumer** -- Tesla model, now BYD expanding. If 10-20% of new car sales go direct, dealer count structurally declines
  3. **AI search** -- If consumers use ChatGPT/Perplexity to search for cars instead of browsing AutoTrader, the "classified minutes" metric becomes irrelevant

- The 75% share is a BACKWARD-looking metric. The question is what share will look like in 5 years.
- Motors.co.uk/Cazoo relaunch is still tiny (4M vs 80M+ visits) but the gap is narrowing at the margin

**Verdict: Market share LIKELY holds 3-5 years.** But the moat is LESS wide than thesis implies. Facebook Marketplace for private sellers and AI search are slow-burning threats that reduce the lifetime of the pricing power monopoly. The thesis does not adequately price this degradation.

### Assumption 3: "ARPR 5% growth is sustainable indefinitely"

**Thesis position:** GBP 90-100/month pricing + GBP 70-80/month product value = 5-6% ARPR growth forever.

**Adversarial challenge:**
- H1 2026 ARPR growth: 5% (GBP 2,994/month, +GBP 142)
- April 2026 pricing: only 5.5% (down from 8%)
- Berenberg now forecasts only 5.2% ARPR growth for FY27 (was 7.5%)
- If dealer backlash constrains pricing to 4-5% permanently, the growth story weakens
- At some point, ARPR hits a ceiling where dealers' ROI on AutoTrader spending becomes marginal
- Current ARPR GBP 36k/year per forecourt -- for a mid-size dealer with 50 cars, that is GBP 720/car/year. If cars sell for GBP 15k avg, that is 4.8% of revenue per car going to AutoTrader. At what point do dealers say "enough"?

**Verdict: 5% growth is REASONABLE for next 2-3 years but NOT indefinite.** The pricing event deceleration (8% -> 5.5%) suggests the peak pricing power regime is ending. A 3-4% ARPR growth rate in the medium term (FY28+) is more realistic than 5-6%.

### Assumption 4: "P/E 15x is cheap for this business"

**Thesis position:** Rightmove at 17x, Scout24 at 16x. AUTO.L at 14-15x is a discount.

**Adversarial challenge:**
- Current P/E: 14.3x (per price_checker)
- Rightmove EV/EBITDA: ~14x, Scout24: ~16x -- but BOTH are facing similar AI/disintermediation concerns
- All three UK classifieds platforms (RMV, AUTO, MONY) lost ~40% of market value in 6 months
- This is NOT just AUTO.L-specific -- it is a SECTOR derating driven by AI anxiety
- If the derating reflects genuine long-term risk, rerating to 17-20x would require demonstrating AI resilience
- 14-15x for a 5% grower with some pricing power uncertainty is FAIR, not cheap
- Bear case: if growth decelerates to 3-4%, a 12-14x P/E is APPROPRIATE (mid-teens would be expensive)

**Verdict: P/E 14-15x is FAIR to slightly cheap, not dramatically undervalued.** The thesis assumed rerating to historical multiples, but the market may be correctly pricing in lower growth and AI risk. The discount to peers (Rightmove, Scout24) is smaller than thesis implied and may be justified by Deal Builder uncertainty.

### Assumption 5: "OEY 720p assumes 8% growth -- is that justified?"

**Thesis position:** OEY + Growth = 7.4% + 8% = 15.4% vs 8.5% WACC. Implied FV 720p.

**Adversarial challenge:**
- 8% growth was based on EPS CAGR (~8%) and revenue growth trajectory
- Revenue CAGR: tool shows 11.6% over 3 years, but this includes COVID recovery bounce
- Normalized revenue growth: ~5-7% (H1 2026: +5%)
- EPS growth benefits from buybacks (+2-3pp on top of revenue growth)
- Realistic organic growth + buyback = 5% + 2% = 7% at best
- IF ARPR growth decelerates to 4% and dealer count is flat, revenue growth = 4-5%
- EPS growth then = 6-7% (with buybacks)
- At 7% growth: OEY FV = ~680-700p (close to thesis)
- At 5% growth: OEY FV = ~600-620p (materially lower)

**Verdict: 8% growth is OPTIMISTIC. 6-7% is more realistic.** The OEY method at 720p overstates by roughly 50-100p depending on growth assumption.

---

## Revised Fair Value

### Method 1: Owner Earnings Yield (60% weight)

```
FCF (TTM): GBP 301M
Depreciation: ~GBP 15M
Maintenance Capex: ~GBP 17M (D&A x 1.1)
Owner Earnings: GBP 299M
Market Cap at 471p: ~GBP 3.95B
OEY: 7.6%

Conservative growth assumption: 6% (5% organic + buyback, down from 8%)
OEY + Growth = 7.6% + 6% = 13.6%
WACC = 8.6% (tool-derived)
Spread = 5.0pp (still positive, still attractive)

Implied FV from OEY at 6% growth: ~620-640p
Implied FV from OEY at 5% growth: ~580-600p
Implied FV from OEY at 7% growth: ~680-700p
```

Using 6% growth (adversarial base case): **OEY FV = 630p**

### Method 2: EV/EBIT Peers (40% weight)

```
Operating Profit (TTM): ~GBP 373M
EV/EBIT:
  - AUTO.L current: ~11x (cheap for the quality)
  - Rightmove: ~14x EV/EBITDA
  - Scout24: ~16x EV/EBITDA

Applying 13x EV/EBIT (discount to RMV due to Deal Builder uncertainty):
  EV = 373M x 13 = GBP 4.85B
  Equity = 4.85B - 0.04B = GBP 4.81B
  FV/share = 4.81B / 838M shares = ~574p

Applying 14x EV/EBIT (in line with Rightmove):
  EV = 373M x 14 = GBP 5.22B
  FV/share = ~620p
```

Using 13-14x range: **EV/EBIT FV = 574-620p, midpoint 597p**

### Method 3: DCF Cross-Check

```
DCF with 5% growth, 8.5% WACC, 2.5% terminal:
  Bear: 532p | Base: 679p | Bull: 891p

DCF with 3% growth, 9% WACC, 2% terminal (stress):
  Bear: 434p | Base: 541p | Bull: 690p

DCF with 7% growth, 8.5% WACC (thesis assumptions):
  Bear: 580p | Base: 739p | Bull: 971p
```

DCF sensitivity confirms FV is highly growth-dependent. At the adversarial 5-6% growth, DCF base case is 600-680p.

### Reconciliation

| Method | FV (Thesis) | FV (Adversarial) | Delta |
|--------|-------------|-------------------|-------|
| OEY (60%) | 720p | 630p | -12.5% |
| EV/EBIT Peers (40%) | 640p | 597p | -6.7% |
| **Weighted Average** | **688p** | **617p** | **-10.3%** |

**Adversarial Fair Value: 617p** (vs thesis 688p, vs current price 471p)

**MoS at current price: 23.7%** (vs thesis claim of 29%)

### Scenario Table (Revised)

| Scenario | Prob | FV | MoS at 471p |
|----------|------|----|-------------|
| Bear (3% growth, pricing power hit) | 25% | 490p | 3.9% |
| Base (6% growth, moderate Deal Builder impact) | 50% | 617p | 23.7% |
| Bull (7%+ growth, Deal Builder resolves, rerates) | 25% | 740p | 36.4% |
| **Expected Value** | 100% | **616p** | **23.5%** |

---

## Kill Conditions Check

| Kill Condition | Status | Evidence |
|----------------|--------|----------|
| 1. Dealer count decline >5% | **OK** -- dealer count UP 1% in H1 2026 (13,986 -> 14,080) | No issue yet |
| 2. ARPR growth turns negative | **OK** -- ARPR +5% in H1 2026 | Positive but decelerating |
| 3. Competitor >20% share | **OK** -- Motors.co.uk ~5% at best, others much smaller | No near-term threat |
| 4. FCF margin <35% | **OK** -- FCF margin 50% | Rock solid |
| 5. Large M&A >GBP 1B | **OK** -- no M&A activity | No issue |
| 6. OEM direct >20% UK sales | **OK** -- still <5% | Long-term risk only |
| 7. AI buying agents disintermediate | **OK** -- still nascent, 3-5 year horizon | Monitoring |

**No kill conditions triggered or approaching.**

---

## EXIT Protocol Application (6 Gates)

**Gate 1: Kill Condition?** NO -- all 7 kill conditions OK.

**Gate 2: Thesis Valid?** PARTIALLY WEAKENED -- Deal Builder pricing event deceleration (8% -> 5.5%) is new information that weakens the pricing power thesis moderately. The core monopoly thesis remains intact. Overall: INTACTA but with LOWER GROWTH TRAJECTORY than thesis assumed.

**Gate 3: MoS Current?** Adversarial MoS = 23.7% at revised FV of 617p. This is positive and reasonable for a high-end Tier B / borderline Tier A position. No urgency to exit on valuation grounds.

**Gate 4: Opportunity Score?** No specific candidate identified that would justify rotation. Cash at 44% is the alternative but cash drag (4.5pp/yr estimated) is less attractive than 23.7% MoS + 6% growth = ~30% total expected return over 2-3 years.

**Gate 5: Dead Money?** NO -- position held 5 days. Too early to evaluate. First real catalyst: April 2026 pricing event implementation. Second: FY2026 full year results (May 2026).

**Gate 6: Friction?** Minimal (liquid stock, small loss, no tax impact).

---

## Verdict: HOLD -- Medium Conviction

### Reasoning

AUTO.L is NOT the Tier A compounder the thesis claimed. The QS tool scores 63, adversarial adjusted is 70-73 (Tier B, high-end). The original thesis inflated QS by claiming 79 through generous moat scoring.

However, the business quality is genuinely strong:
- Financial Quality: 40/40 (perfect -- ROIC +42pp spread, FCF margin 50%, near net cash)
- The monopoly position is real (75% classified minutes, 10x nearest competitor)
- FCF consistency is excellent (4/4 years positive)
- Share buyback program active at current depressed prices

The ADVERSARIAL Fair Value of 617p provides 23.7% MoS at current price of 471p. This is:
- Less than thesis claimed (29% MoS) but still meaningful
- Reasonable for a high-quality Tier B position (precedent: MoS 20-25% for Tier B is acceptable per decisions_log)
- Supported by DCF cross-check (base 541-679p depending on growth)

The key risk is ARPR growth deceleration. If April 2026 pricing event (5.5%) plus product generates only 5% ARPR growth (vs historical 7-8%), the valuation compresses further. But even at 5% growth, DCF bear case is 532p -- still 13% above current price.

### Why Not SELL?

1. No kill conditions triggered
2. Financial quality is exceptional (40/40)
3. Monopoly position is real and intact near-term
4. MoS of 23.7% provides buffer even with adversarial FV
5. Catalysts ahead: April pricing event, FY2026 results (May 2026)
6. Precedent: we held MONY.L at similar conviction after adversarial review (Tier A claim -> actual Tier B)
7. The 44% cash position means we don't need to sell to raise capital
8. Buyback at current levels = management alignment

### Why Not ADD?

1. QS downgrade from Tier A to Tier B changes the risk profile
2. The pricing power deceleration is new and unresolved
3. April 2026 pricing event is the next test -- wait for data
4. UK concentration already at 4 positions (MONY.L, AUTO.L, BYIT.L, DOM.L)
5. Standing order at 450p should be CANCELLED -- was based on Tier A thesis with FV 688p

### Actions Required

1. **Revise thesis FV:** 688p -> 617p
2. **Revise QS:** 79 (Tier A) -> 71 (Tier B, high-end) [QS Tool 63, Adjusted 71]
3. **Cancel ADD standing order at 450p** -- original MoS calculation was based on inflated FV
4. **Monitor:** April 2026 pricing event implementation and dealer reaction
5. **Monitor:** FY2026 full year results (May 2026) for ARPR, dealer count, operating profit
6. **Re-evaluate after May 2026 results** -- if ARPR growth >5% and dealer count stable, thesis strengthens; if ARPR growth <4%, consider TRIM

### Conviction: MEDIUM (was HIGH)

The downgrade from HIGH to MEDIUM reflects:
- QS downgrade from Tier A to Tier B
- Pricing power deceleration evidence (8% -> 5.5%)
- But offset by: strong financials, real monopoly, reasonable MoS

---

## Value Trap Checklist (10 factors)

| Factor | Check | Detail |
|--------|-------|--------|
| Industria en declive secular | NO | UK car market growing |
| Disrupcion tecnologica | MAYBE | AI search is slow threat |
| Management destruyendo valor | NO | Buybacks at depressed prices |
| Balance deteriorandose | NO | Net cash |
| Insider selling masivo | NO | No evidence |
| Dividend cut probable | NO | Payout 32%, well covered |
| Perdida market share >2pp | NO | Still 75%+ |
| ROIC < WACC | NO | ROIC-WACC spread +42pp |
| FCF negativo >2 anos | NO | FCF GBP 301M, 50% margin |
| Goodwill >50% equity | POSSIBLE | Legacy acquisitions, but immaterial for asset-light |

**Score: 0-1/10 -- Very low value trap risk.** This is genuinely a high-quality business.

---

## Comparison with Other Adversarial Reviews

| Position | QS Thesis | QS Adversarial | FV Delta | Verdict |
|----------|-----------|----------------|----------|---------|
| NVO | 82 | 68-70 | -12-14 | Pattern: inflation |
| LULU | 82 | 66-72 | -22.6% | HOLD |
| BYIT.L | 81 | 68-72 | Moat siege | Deferred |
| MONY.L | 81 | ~65-70 | -27% | HOLD LOW |
| **AUTO.L** | **79** | **70-73** | **-10.3%** | **HOLD MEDIUM** |

AUTO.L's FV delta (-10.3%) is the SMALLEST among all adversarial reviews. The business quality is genuinely high -- the inflation was mainly in QS classification (Tier A vs Tier B), not in the underlying valuation. The financial metrics (40/40 financial quality, 50% FCF margin, ROIC +42pp) are among the best in the portfolio.

---

## META-REFLECTION

### Changes Detected Since Last Review
- Deal Builder pricing event deceleration (8% -> 5.5%) is the most material new information
- Jefferies and Berenberg downgrades with target cuts confirm market concern
- Share price touched new 52-week low (468.6p) since purchase
- UK used car market data is positive (supports volume thesis)

### Incertidumbres
- April 2026 pricing event implementation is the key unknown -- will 5.5% hold or will dealers force further concessions?
- ARPR growth trajectory FY27+ is genuinely uncertain (Berenberg cut from 7.5% to 5.2%)
- Facebook Marketplace's UK car market share is not measurable -- could be larger than we think for private sellers
- The AI disintermediation timeline is hard to forecast -- could be 3 years or 10 years
- EPS data gap in quality_scorer.py (nan for 2025) makes growth scoring unreliable

### Sugerencias
- Create a "UK digital platforms" sector view covering AUTO.L, MONY.L, RMV.L -- these are correlated businesses with similar risks (AI disintermediation, UK consumer)
- Fix quality_scorer.py nan handling -- when a metric is nan, flag it rather than scoring 0
- Track ARPR growth at each reporting date as a leading indicator
- AUTO.L thesis should be updated to reference the April pricing event as the KEY near-term catalyst

### Alertas para Orchestrator
- **CANCEL the ADD standing order at 450p** -- this was based on FV 688p (now 617p). At 450p with adversarial FV 617p, MoS would be 27% which is reasonable for Tier B but no longer Tier A entry. If we keep the standing order, it should be at a price that provides 25%+ MoS vs adversarial FV -- roughly 460p or below. Consider adjusting to 430p.
- **UK concentration alert**: AUTO.L is 4th UK position. Principles.md now notes "before adding ANY new UK position, document why non-UK comparable is inferior." This applies if we consider ADD.
- **QS Tier downgrade**: Original purchase was justified as "Tier A Quality Compounder." Adversarial review shows Tier B. The sizing at 3.4% was appropriate for Tier A and is also appropriate for high-conviction Tier B, so no action needed on sizing. But future ADD decisions should use Tier B framework.

---

## Sources

### Deal Builder Controversy
- [Motor Trade News: Autotrader outlines changes to Deal Builder](https://www.motortradenews.com/dealer-insights/autotrader-outlines-changes-to-deal-builder-following-backlash/)
- [Car Dealer Magazine: Auto Trader launches Customer Advisory Groups](https://cardealermagazine.co.uk/auto-trader-looks-to-quell-deal-builder-backlash-as-it-officially-launches-customer-advisory-groups/320561)
- [Car Dealer Magazine: Auto Trader defends pricing](https://cardealermagazine.co.uk/auto-trader-defends-its-pricing-as-bosses-deny-deal-builder-is-responsible-for-falling-share-value/320741)
- [AM-online: Autotrader responds to Deal Builder criticism](https://www.am-online.com/news/autotrader-responds-to-deal-builder-criticism-after-facing-threat-of-mass-cancellations)
- [AM-online: Reservation Request added to Deal Builder](https://www.am-online.com/news/autotrader-to-add-reservation-request-to-deal-builder-after-retailer-backlash)

### Analyst Ratings
- [Jefferies downgrade to Hold, target 650p](https://www.trustfinance.com/blog/jefferies-downgrades-autotrader-to-hold-amid-price-risks)
- [Berenberg target cut to 665p](https://www.sharecast.com/news/broker-recommendations/berenberg-slashes-auto-trader-target-price-on-deal-builder-issues--21484699.html)
- [MarketBeat: AUTO forecast and price target](https://www.marketbeat.com/stocks/LON/AUTO/forecast/)
- [TipRanks: AUTO forecast](https://www.tipranks.com/stocks/gb:auto/forecast)

### UK Used Car Market
- [AutoTrader: Used car market enters 2026 with positive momentum](https://plc.autotrader.co.uk/news-views/press-releases/used-car-market-enters-2026-with-positive-momentum-as-2025-sales-finish-2-ahead-of-previous-year/)
- [AM-online: UK used car market up 2.2% in 2025](https://www.am-online.com/news/used-ev-sales-surge-as-uk-used-car-market-grows-again)
- [Marsh Finance: UK Car Market 2026](https://www.marshfinance.com/blog/navigating-the-uk-car-market-in-2026)

### H1 2026 Results
- [DirectorsTalk: AUTO H1 2026 results](https://www.directorstalkinterviews.com/auto-trader-reports-5-revenue-growth-and-expands-ai-powered-tools-in-h1-2026/4121224614)
- [ts2.tech: AUTO share price and 2026 outlook](https://ts2.tech/en/auto-trader-group-plc-lonauto-share-price-near-52%E2%80%91week-low-despite-strong-results-2026-stock-outlook-and-analyst-forecasts/)

### Competitors
- [Plan Insurance: Cazoo relaunch by Motors](https://www.planinsurance.co.uk/blog/cazoo-relaunch-challenge-auto-trader/)
- [SQ Magazine: Facebook Marketplace Statistics 2026](https://sqmagazine.co.uk/facebook-marketplace-statistics/)

### AI Disruption
- [Digital Dealer: AI Search in 2026](https://digitaldealer.com/news/whats-next-for-ai-search-in-2026-a-dealers-guide-to-whats-coming-and-what-to-do-about-it/168942/)
- [BCG: Will AI Become the Best Car Sales Advisor?](https://www.bcg.com/publications/2025/will-ai-become-best-car-sales-advisor)

### Share Buyback
- [TipRanks: Autotrader repurchases 430,000 shares](https://www.tipranks.com/news/company-announcements/autotrader-repurchases-430000-shares-updates-voting-rights-total)
- [TipRanks: Autotrader buys back 461,692 shares](https://www.tipranks.com/news/company-announcements/autotrader-buys-back-461692-shares-trimming-free-float-voting-rights)
