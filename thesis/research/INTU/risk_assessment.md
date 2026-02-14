# Risk Assessment: INTU (Intuit Inc.)

## Fecha: 2026-02-12

## Risk Score: MEDIUM-HIGH

---

## Executive Summary

Intuit is a high-quality business (QS Tool 77, Tier A) with dominant market positions in tax preparation (TurboTax) and small business accounting (QuickBooks, ~62-80% market share). However, the company faces a convergence of risks that are material: AI disruption of its core tax business model, massive acquisition-related goodwill ($14B, ~38% of total assets), stock-based compensation consuming ~39% of FCF, and a stock that has already fallen 34% from highs yet remains at fair value by DCF (base case FV ~$384 vs price $400). The biggest risk is structural: AI agents could commoditize the tax preparation workflow that generates the bulk of Intuit's Consumer segment revenue.

---

## Quality Profile Summary (Tool Output)

| Metric | Value | Assessment |
|--------|-------|------------|
| QS Tool | 77/100 | Tier A |
| ROIC | 17.2% | Good, improving trajectory |
| ROIC-WACC Spread | +5.9pp | Positive but not exceptional for software |
| FCF Margin | 32.3% | Strong |
| Gross Margin | 79.6% | Strong, stable |
| Operating Margin | 26.2% | Improving trajectory |
| Revenue CAGR 3yr | 14.0% | Solid |
| EPS CAGR 3yr | 23.3% | Strong |
| Leverage | Net Cash per tool (but see financial risks below) |
| Insider Ownership | 2.3% | Low |
| SBC as % Revenue | ~10.1% | Elevated for software |
| SBC as % FCF | ~39% | MATERIAL - inflates reported FCF |

**NOTE on "Net Cash" classification:** The quality_scorer.py reports "Net Cash" but this appears to be a data gap. Per Intuit's FY2025 10-K, total debt is ~$6.0B and cash/investments ~$4.6B, implying net debt of ~$1.4B. The tool may be netting cash against current debt only. This is a meaningful discrepancy that must be clarified in the fundamental analysis.

---

## Matriz de Riesgos

| # | Categoria | Riesgo | Probabilidad | Impacto | Score | Timeline | Mitigante |
|---|-----------|--------|-------------|---------|-------|----------|-----------|
| 1 | Fundamental | AI agents commoditize tax prep | Media-Alta | Alto | **HIGH** | 2-5yr | Intuit investing heavily; $100M OpenAI deal |
| 2 | Fundamental | Growth deceleration (FY26 guide 12-13% vs 16% FY25) | Alta | Medio | **HIGH** | Now | Still double-digit; multiple already compressed |
| 3 | Financiero | SBC inflates FCF quality (~39% of FCF) | Alta | Medio | **HIGH** | Ongoing | Shares outstanding flat/declining via buybacks |
| 4 | Financiero | Goodwill $14B (~38% total assets, ~76% of est. equity) | Media | Alto | **HIGH** | 1-3yr | No impairment to date; acquisitions performing |
| 5 | Valoracion | At fair value after 34% drop; limited MoS | Alta | Medio | **HIGH** | Now | DCF base $384 vs $400; need ~$300 for 25% MoS |
| 6 | Regulatorio | Tax code simplification / IRS pre-filled returns | Baja | Muy Alto | MEDIUM | 3-10yr | IRS Direct File killed under Trump; strong lobbying |
| 7 | Legal | Data breach litigation + $141M settlement precedent | Media | Medio | MEDIUM | 1-3yr | Settlements manageable vs $6B+ FCF |
| 8 | Fundamental | Credit Karma revenue model under pressure (CFPB, rates) | Media | Medio | MEDIUM | 1-3yr | Integrated into TurboTax platform |
| 9 | Fundamental | QuickBooks SMB churn in recession | Media | Medio | MEDIUM | 1-2yr | 80%+ market share provides buffer |
| 10 | Governance | Insider selling (Scott Cook $50M Dec 2025) | Media | Bajo | LOW | Now | Founder is 73; may be estate planning |
| 11 | Fundamental | Mailchimp integration / Email marketing commoditization | Baja-Media | Medio | LOW-MEDIUM | 2-5yr | Growing but competitive market |
| 12 | Macro | Inflation sticky / Fed higher for longer compresses P/E | Media | Bajo-Medio | LOW-MEDIUM | 6-12m | Multiple already compressed from 40x to 27x |
| 13 | Geopolitico | Minimal exposure (US domestic business) | Baja | Bajo | LOW | N/A | 95%+ US revenue |

---

## Top 3 Riesgos Criticos

### 1. AI Disruption of Tax Preparation Business Model

- **Categoria:** Fundamental / Structural
- **Descripcion:** Intuit's Consumer segment (TurboTax) generates ~$4.7B in revenue (25% of total). The core value proposition is simplifying tax filing. AI agents (ChatGPT, Claude, Gemini, specialized tax AI) are approaching the capability to file taxes end-to-end. Scale Venture Partners published research showing LLMs can "build TurboTax in a weekend." The question is not IF AI can do taxes, but WHEN it becomes reliable enough for consumers to trust it.
- **Evidencia:**
  - Intuit paid OpenAI $100M+ to embed ChatGPT in TurboTax -- this is DEFENSIVE spending, not offensive
  - Wells Fargo downgraded to Equal Weight citing "elevated expectations and difficult year-over-year comparisons"
  - TD Cowen cut target to $658 citing "investor hesitation around AI impacts and terminal values"
  - The stock fell 34% Nov 2025 - Feb 2026 with AI disruption as primary narrative
  - Washington Post reported TurboTax and H&R Block AI chatbots "giving bad tax advice" -- current AI is imprecise for tax, but improving rapidly
- **Probabilidad:** Media-Alta (40-60%) over 3-5 years. AI will be able to handle simple returns (W-2 only) within 2 years. Complex returns may take 5+ years.
- **Impacto si materializa:** 15-25% revenue at risk from Consumer segment. If TurboTax loses pricing power, margins compress. P/E de-rates from 27x to 15-18x (commodity software). Combined: -30% to -50% fair value impact.
- **Mitigante:** Intuit is aggressively investing in AI. The $100M OpenAI partnership is significant. Intuit's proprietary tax data (30M+ returns/year) is a moat. Regulatory requirements for tax filing precision create barriers. The hybrid "AI + Human Expert" model (600 expert office locations, 20 TurboTax stores) creates differentiation. But the question is whether this DELAYS disruption or PREVENTS it.
- **Kill condition?:** YES -- if TurboTax paying customer count declines >5% YoY for 2 consecutive quarters.

### 2. Stock-Based Compensation Masking True Cash Flow Quality

- **Categoria:** Financiero / Earnings Quality
- **Descripcion:** Intuit's SBC was $1.97B in FY2025 (10.1% of revenue, ~39% of reported FCF of ~$5.1B). This means that of every dollar of "free cash flow," ~39 cents is effectively employee compensation excluded from the calculation. True owner earnings are materially lower than headline FCF suggests. Additionally, SBC grew from $1.31B (FY2022) to $1.97B (FY2025), a 50% increase in 3 years.
- **Evidencia:**
  - SBC FY2025: $1.97B (10.1% of $19.4B revenue)
  - SBC FY2024: $1.94B (12% of $16.3B revenue -- higher % in prior years)
  - Reported FCF: $6.1B. FCF ex-SBC: ~$4.1B
  - P/FCF at $400: 18.3x on reported FCF, but 27.2x on FCF ex-SBC
  - Shares outstanding declined 0.53% YoY -- buybacks mostly offset dilution but don't create meaningful per-share value accretion
- **Probabilidad:** Alta (100% -- this is a known, ongoing issue)
- **Impacto si materializa:** If the market re-prices FCF quality (as it should for a mature compounder), intrinsic value drops 15-20%. DCF models using headline FCF overstate fair value.
- **Mitigante:** SBC is real compensation that retains talent. Buybacks offset dilution. Industry-standard for software companies. But at 10% of revenue, it is on the high end.
- **Kill condition?:** NO (structural feature, not binary event). But flag: if SBC exceeds 12% of revenue, talent retention costs are becoming unsustainable.

### 3. Goodwill Impairment Risk ($14B, ~76% of Estimated Equity)

- **Categoria:** Financiero / Balance Sheet
- **Descripcion:** Intuit carries $14.0B in goodwill on $36.9B total assets (~38% of total assets). Against estimated total equity of ~$18-19B, goodwill represents roughly 74-78% of equity. This goodwill came primarily from Credit Karma ($8.1B acquisition, 2020) and Mailchimp ($12B acquisition, 2021). If either business underperforms, impairment risk is material.
- **Evidencia:**
  - Goodwill: $13.98B (FY2025)
  - Total assets: $36.96B
  - Credit Karma acquisition: $8.1B (Feb 2021) -- paid during peak fintech valuations
  - Mailchimp acquisition: $12B (Nov 2021) -- paid near peak SaaS valuations
  - Credit Karma's lead-gen model depends on interest rates (mortgage/lending activity)
  - Email marketing (Mailchimp's core) is increasingly commoditized
  - No impairment charges to date, but both acquisitions were made at peak valuations
- **Probabilidad:** Media (25-35%). Unlikely near-term if revenue growth continues, but if any segment meaningfully underperforms expectations, impairment testing could trigger.
- **Impacto si materializa:** A $3-5B impairment would wipe out 1-2 quarters of earnings on a GAAP basis. While non-cash, it signals capital misallocation and could trigger a 10-15% stock decline. If Credit Karma is written down, it invalidates the platform ecosystem thesis.
- **Mitigante:** Both acquisitions are generating revenue. Mailchimp integrated into SMB platform. Credit Karma integrated into TurboTax. No current signs of impairment.
- **Kill condition?:** YES -- if Intuit takes a goodwill impairment charge >$2B, it signals the acquisition strategy has destroyed value.

---

## Additional Material Risks

### 4. Valuation: Still Not Cheap After 34% Decline

- **Descripcion:** INTU has fallen from $813 (52w high) to $400 (-51%). Despite this, DCF base case FV is ~$384, meaning MoS is approximately -4% (slightly overvalued). Even the bear case ($305) is only -24% below current price. The stock traded at 40x+ P/E pre-crash; at 27x P/E now, it is cheaper but not deeply discounted.
- **The problem:** For a Tier A compounder, we typically seek 15-25% MoS. At $400, there is no margin of safety. The stock needs to fall to ~$300-320 range for attractive entry. Earnings on Feb 26 could be a catalyst either way.
- **Risk:** If Q2 FY2026 earnings (Feb 26) disappoint, stock could fall to $350-370. If they beat, the window for entry closes.

### 5. Growth Deceleration: FY26 Guide 12-13% vs FY25 Actual 16%

- **Descripcion:** Revenue growth is decelerating: FY25 +16%, FY26 guided 12-13%. Q1 FY26 grew 18%, but this was slower than Q4 FY25 (+20%). The market is pricing this deceleration, but the question is whether 12-13% is the new normal or a temporary floor.
- **Risk:** If growth decelerates further to single-digit (8-10%), the stock re-rates from "growth compounder" to "mature software" at 15-20x P/E, implying fair value of $300-360.

### 6. Tax Code / Regulatory Tail Risk

- **Descripcion:** If a future administration simplifies the tax code (pre-filled returns, flat tax), TurboTax's raison d'etre diminishes. The IRS Direct File program was killed by Trump, but a future Democratic administration could revive it.
- **Probabilidad:** Baja under current administration (Trump killed Direct File). Medium under future admin.
- **Impact:** Would eliminate or severely compress Consumer segment (~$4.7B revenue). Existential for that segment.
- **Mitigante:** Intuit spent $3.8M lobbying in 2023 (record). Strong political connections. Tax code complexity is structural (Congress benefits from it).

---

## Riesgos NO Mencionados en Thesis (Independent Findings)

Note: No thesis exists yet for INTU. These are risks I would flag for the fundamental-analyst to address:

| Riesgo | Severidad | Likely Thesis Gap? | Comentario |
|--------|-----------|-------------------|------------|
| SBC at 39% of FCF -- FCF quality issue | HIGH | YES -- analysts often cite headline FCF without adjusting | $1.97B SBC on $5.1B FCF materially distorts valuation |
| Goodwill at 76% of equity from peak-valued acquisitions | HIGH | YES -- often glossed over as "acquisitions performing" | $14B goodwill from Credit Karma ($8.1B) + Mailchimp ($12B) at 2021 peak |
| Insider selling: Scott Cook sold $50M in Dec 2025 | MEDIUM | PROBABLY | Founder selling $50M while stock is at lows is noteworthy |
| Data breach litigation pattern | MEDIUM | POSSIBLY | $141M settlement + ongoing class actions from 2024 breach |
| Credit Karma revenue sensitivity to interest rates | MEDIUM | POSSIBLY | Mortgage/lending lead-gen revenue declines in high-rate environment |
| OpenAI $100M+ deal = DEFENSIVE spend, not moat reinforcement | MEDIUM | YES | Often positioned as AI leadership; in reality it is paying the disruptor to delay disruption |
| Tax seasonality concentration risk | LOW-MEDIUM | POSSIBLY | Q3 fiscal (Jan-Apr) = ~45% of annual revenue |
| QuickBooks Desktop end-of-life forced migration risk | LOW-MEDIUM | POSSIBLY | Forced cloud migration could create churn window for Xero/FreshBooks |

---

## Kill Conditions Sugeridas

Based on my independent risk assessment, the following kill conditions should be included in any INTU thesis:

1. **TurboTax paid customer count declines >5% YoY for 2 consecutive quarters** -- signals AI disruption is materializing
2. **Goodwill impairment charge >$2B** -- signals acquisition strategy has destroyed value
3. **Revenue growth decelerates to <8% for 2 consecutive quarters** -- below compounder threshold, re-rate to mature software
4. **SBC exceeds 12% of revenue** -- talent retention costs becoming unsustainable, diluting shareholders
5. **ROIC falls below WACC (currently 17.2% vs 11.3%)** -- business no longer creating value above cost of capital
6. **IRS Direct File program reinstated and expanded to 50 states** -- structural threat to Consumer segment
7. **Credit Karma segment revenue declines >10% YoY** -- signals acquisition has failed to deliver

---

## Bear Case: What Makes This a -50% Stock?

### Scenario: "The AI Reckoning" (Price target: $200)

**Trigger sequence:**
1. **2026-2027:** AI tax agents (OpenAI, Google, startups) begin handling simple W-2 returns for free or $5-10. TurboTax Free + Simple tier collapses.
2. **2027:** TurboTax paid customers decline 8-10% as AI handles increasingly complex returns. Intuit responds by cutting prices, compressing margins.
3. **2027-2028:** QuickBooks faces competition from AI-native accounting tools (ChatGPT for Business, Xero AI) that are 80% as good at 50% of the price.
4. **2028:** New administration revives IRS Direct File. Political will exists because AI makes it feasible.
5. **Impact:** Revenue growth goes flat (0-3%). Operating margins compress from 26% to 20% as Intuit increases AI spending and cuts prices. P/E compresses from 27x to 14x. Stock falls to $200-250 range.

**Structural impairment:** If AI commoditizes tax filing, Intuit's moat in Consumer is permanently impaired. QuickBooks' moat (switching costs, data lock-in) is stronger, but if SMBs can use AI agents to manage books, the pricing power diminishes.

**Probability of this bear case:** 15-25% over 5 years. The most likely outcome is that AI partially disrupts but Intuit adapts. However, the TAIL RISK is real.

### What the market might know that we don't:

The 34% decline from $813 to $400 suggests the market is already pricing in significant AI disruption risk. Smart money is rotating out of software companies with "AI-targetable" workflows. The question is: has the market OVER-corrected (opportunity) or is it still in denial about the pace of disruption (further downside)?

---

## Riesgo Agregado

- Numero de riesgos HIGH+CRITICAL: **5** (AI disruption, SBC quality, goodwill, valuation, growth deceleration)
- Riesgos correlacionados: **YES**
  - AI disruption + growth deceleration + valuation compression are correlated: if AI disrupts, growth slows, and multiple compresses simultaneously
  - Goodwill impairment is triggered by business underperformance, which correlates with AI disruption
  - This correlation means the risks are NOT independent -- a single catalyst (AI advancement) could trigger multiple risks simultaneously

- **Risk Score Final: MEDIUM-HIGH**

**Reasoning:** The business is high quality (QS 77, Tier A) with dominant market positions and strong financials. However, five HIGH-rated risks, with significant correlation among them, elevate aggregate risk above MEDIUM. The primary concern is that Intuit is at the center of an AI disruption zone (tax prep, bookkeeping, email marketing -- all highly automatable workflows) while simultaneously being at fair value with no margin of safety. The combination of "disruption risk + no MoS" is dangerous.

---

## 🔄 META-REFLECTION

### Dudas/Incertidumbres
- **SBC treatment in quality_scorer.py:** The tool shows "Net Cash" for INTU, but 10-K shows $6B debt vs $4.6B cash. This needs reconciliation before any valuation work proceeds. The tool may be looking at different line items.
- **Credit Karma revenue decomposition:** I could not find a clean breakdown of Credit Karma's contribution to total revenue. The fundamental-analyst needs to extract this from segment reporting.
- **Mailchimp growth trajectory:** Similarly, Mailchimp's standalone performance within the SMB segment is opaque. Is it growing or stagnating post-acquisition?
- **AI impact timing:** My biggest uncertainty is WHEN AI disrupts tax prep. The technology is advancing faster than I expected. If it takes 5+ years, Intuit has time to adapt. If 2-3 years, the stock is materially overvalued even at $400.

### Riesgos que Podrian Estar Subestimados
- **SBC quality of earnings:** I rated this HIGH, but it might be CRITICAL. At 39% of FCF, the market may be valuing INTU on inflated cash flow metrics. When/if the market reprices FCF quality, the multiple compression could be severe.
- **Correlated risk cascade:** The correlation between AI disruption, growth deceleration, goodwill impairment, and multiple compression means the downside scenario is fatter-tailed than my individual probability estimates suggest. A correlated unwind could be -50%+ from here.

### Riesgos que el Mercado No Esta Pricing (Potentially)
- **The OpenAI deal as DEFENSIVE, not offensive.** The market may be interpreting the $100M OpenAI partnership as "Intuit is an AI leader." I interpret it as "Intuit is paying the disruptor to not disrupt them yet." This is a subtle but critical distinction.
- **SBC quality.** Most analysts cite headline FCF ($6.1B) without adjusting for $1.97B SBC. FCF ex-SBC is $4.1B, implying a P/FCF(adj) of 27x, not 18x.

### Discrepancias Potenciales con Thesis
- If a fundamental-analyst writes this up, they will likely focus on the strong brand, dominant market share, and AI integration. My role is to counterbalance: the brand and market share exist BECAUSE the tax code is complex and software is the only way to navigate it. If AI makes tax filing trivial, the moat evaporates.
- The analyst may anchor on 14% revenue CAGR. I note this is decelerating, and the mix is shifting (Credit Karma + Mailchimp growing faster than core TurboTax, which masks organic deceleration).

### Sugerencias para el Sistema
1. **quality_scorer.py debt/cash detection:** Investigate why INTU shows "Net Cash" when 10-K clearly shows $6B total debt. This could be affecting other companies too.
2. **SBC-adjusted FCF metric:** Consider adding "FCF ex-SBC" as a standard metric in quality_scorer.py. For software companies, SBC is a material non-cash adjustment that affects valuation.
3. **AI disruption risk framework:** We should develop a standardized framework for assessing AI disruption risk across our portfolio and pipeline. Several positions (ADBE, MONY.L, BYIT.L, and now potentially INTU) face this risk.

### Preguntas para Orchestrator
1. **Entry price target:** Given MEDIUM-HIGH risk, what MoS should we require for INTU? My suggestion: 25%+ (Tier A with elevated risk), implying entry at ~$290-300. This is consistent with DCF bear case ($305).
2. **Timing vs Feb 26 earnings:** Should we wait for Q2 FY26 results (Feb 26) before completing the full buy-pipeline? The earnings could clarify AI impact on tax season revenue.
3. **SBC adjustment policy:** Should we adopt a policy of always adjusting FCF for SBC when valuing software companies? This would lower FVs across the board but provide more conservative, realistic estimates.
4. **AI disruption as sector-wide screen:** Should we add "AI disruption vulnerability" as a screening criterion for all software/fintech companies in our pipeline?

---

## Sources

### Revenue & Stock Performance
- [Motley Fool: Intuit Stock Down 24% in 2026](https://www.fool.com/investing/2026/01/30/intuit-stock-is-down-24-already-in-2026-time-to-bu/)
- [Trefis: Why Intuit Stock Crashed -30%](https://www.trefis.com/stock/intu/articles2/589573/why-intuit-stock-crashed-30/2026-02-04)
- [TIKR: Intuit Stock Drops 6% After Downgrades](https://www.tikr.com/blog/intuit-stock-drops-6-after-sharp-downgrades-are-we-looking-at-a-difficult-2026)
- [EBC: Why Intuit Stock Is Dropping Ahead of Feb 26 Earnings](https://www.ebc.com/forex/why-intuit-intu-stock-is-dropping-ahead-of-feb-26-earnings)

### AI Disruption
- [TechBuzz: Intuit Pays OpenAI $100M+ for ChatGPT Integration](https://www.techbuzz.ai/articles/intuit-pays-openai-100m-to-embed-chatgpt-in-turbotax)
- [Scale VP: Building TurboTax in a Weekend with LLMs](https://www.scalevp.com/insights/turbotax-llms-ai/)
- [Yahoo Finance: AI Pressure Tests Intuit's Moat](https://finance.yahoo.com/news/ai-pressure-tests-intuit-moat-021114925.html)
- [MIT Sloan: TurboTax Meets Turbo Innovation](https://sloanreview.mit.edu/article/turbotax-meets-turbo-innovation-ai-at-intuit/)
- [Washington Post: AI Tax Chatbots Giving Bad Advice](https://www.washingtonpost.com/technology/2024/03/04/ai-taxes-turbotax-hrblock-chatbot/)

### IRS Direct File
- [Kiplinger: Free Tax Filing Option Disappeared for 2026](https://www.kiplinger.com/taxes/a-free-tax-filing-option-just-disappeared)
- [Nextgov: Direct File Won't Happen in 2026](https://www.nextgov.com/digital-government/2025/11/direct-file-wont-happen-2026-irs-tells-states/409309/)
- [CBPP: Trump Plan to End Direct File Is a Mistake](https://www.cbpp.org/blog/trump-plan-to-end-free-direct-file-program-and-rely-on-for-profit-tax-preparers-is-a-mistake)
- [Legis1: Intuit Spends $900K Lobbying on Tax Policy](https://legis1.com/news/intuit-tax-policy-lobbying/)

### Legal/Regulatory
- [ClassAction.org: Intuit Litigation](https://www.classaction.org/news/category/intuit-inc)
- [ForThePeople: TurboTax Accused of Ignoring Fraud](https://www.forthepeople.com/blog/turbotax-accused-ignoring-fraud-boost-profits/)
- [TopClassActions: Intuit $141M Settlement](https://topclassactions.com/lawsuit-settlements/lawsuit-news/intuit-agrees-to-141m-settlement-over-allegations-it-improperly-charged-certain-consumers-for-turbotax/)
- [Lexology: Intuit Data Breach Lawsuit](https://www.lexology.com/library/detail.aspx?g=6b1f9232-4e8b-458d-8c19-776908d80d8c)

### Insider Activity
- [MarketScreener: Intuit Insider Sold Shares Worth $50M](https://www.marketscreener.com/news/intuit-insider-sold-shares-worth-50-367-047-according-to-a-recent-sec-filing-ce7e59d9da88f626)
- [MarketBeat: Intuit Insider Trading Activity](https://www.marketbeat.com/stocks/NASDAQ/INTU/insider-trades/)

### Analyst Ratings
- [Investing.com: BMO Lowers INTU Target to $624](https://www.investing.com/news/analyst-ratings/bmo-capital-lowers-intuit-stock-price-target-to-624-on-tax-survey-results-93CH-4496105)
- [Investing.com: TD Cowen Lowers Target to $658](https://www.investing.com/news/analyst-ratings/intuit-stock-price-target-lowered-to-658-by-td-cowen-on-ai-concerns-93CH-4494482)
- [Seeking Alpha: Wells Fargo Downgrades Intuit](https://seekingalpha.com/news/4537707-figma-gets-an-upgrade-intuit-sees-rating-cut-as-wells-fargo-highlights-2026-outlook-for-software-stocks)

### Financial Data
- [MacroTrends: Intuit SBC](https://macrotrends.net/stocks/charts/INTU/intuit/stock-based-compensation)
- [QuickBooks Market Share](https://www.acecloudhosting.com/blog/quickbooks-market-share/)
- [Intuit IR: FY2025 Results](https://investors.intuit.com/news-events/press-releases/detail/1266/intuit-reports-strong-fourth-quarter-and-full-year-fiscal-2025-results-sets-fiscal-2026-guidance-with-double-digit-revenue-growth-and-continued-operating-margin-expansion)
- [StockAnalysis: INTU Balance Sheet](https://stockanalysis.com/stocks/intu/financials/balance-sheet/)
