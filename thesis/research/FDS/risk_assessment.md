# Risk Assessment: FDS (FactSet Research Systems)

## Fecha: 2026-02-13

## Risk Score: MEDIUM-HIGH

---

## Context

- **Company:** FactSet Research Systems Inc. (NYSE: FDS)
- **Sector:** Financial Data & Analytics
- **Market Cap:** $7.6B USD
- **Price:** $203.60 USD (EUR 171.49)
- **QS Tool:** 73/100 (Tier B)
- **Entry (universe):** $180
- **52-Week Range:** $190.58 - $474.79
- **Stock YTD performance (CY2025):** -39% (one of the worst performers among quality financial data companies)

**No existing thesis.** This assessment is fully independent.

---

## Matriz de Riesgos

| # | Categoria | Riesgo | Probabilidad | Impacto | Score | Mitigante |
|---|-----------|--------|-------------|---------|-------|-----------|
| 1 | Fundamental | AI disruption of analytics layer | Media-Alta | Alto | HIGH | FactSet investing in AI (Cobalt, MCP server), but Bloomberg/SPGI outspend 10:1 |
| 2 | Fundamental | Revenue-per-user structural decline | Alta | Medio | HIGH | User growth 9.7% but ASV growth only 5.9% -- dilutive unit economics |
| 3 | Fundamental | Bloomberg/SPGI competitive squeeze | Alta | Medio | HIGH | 4.5% market share vs Bloomberg 33%; SPGI post-Markit integration threat |
| 4 | Valoracion | Value trap / dead money risk | Media | Medio | MEDIUM | -58% from 2yr high; margin compression with uncertain duration |
| 5 | Financiero | Margin compression investment phase duration | Media | Medio | MEDIUM | FY26 adj. operating margin 34-35.5% vs 36.3% FY25; management timeline uncertain |
| 6 | Legal | CUSIP antitrust class-action lawsuit | Media | Medio | MEDIUM | Lawsuit survived motion to dismiss; 3+ years to verdict; damages uncertain |
| 7 | Fundamental | Buy-side client base structural shrinkage | Media | Medio | MEDIUM | Buy-side = 82% of ASV; hedge fund closures and asset manager consolidation ongoing |
| 8 | Fundamental | Insider selling pattern | Media-Baja | Bajo | LOW | 14 sales vs 4 purchases in 6 months; routine compensation sales, not panic |
| 9 | Geopolitico | Macro cyclicality affecting client budgets | Media | Bajo | LOW | Financial market downturns reduce terminal spending; counter: 95% retention rate |
| 10 | Financiero | Acquisition debt from CUSIP ($1.93B) | Baja | Bajo | LOW | Net Debt/EBITDA 1.4x; Interest coverage 13.8x; manageable |
| 11 | ESG | No material ESG controversy | Baja | Bajo | LOW | Sustainalytics rates ESG management as "Strong" |

### Scoring:
- Alta x Alto = CRITICAL
- Alta x Medio OR Media x Alto = HIGH
- Media x Medio = MEDIUM
- Baja x cualquiera OR cualquiera x Bajo = LOW

---

## Top 3 Riesgos Criticos

### 1. AI Disruption of the Analytics Layer

- **Categoria:** Fundamental / Technology
- **Descripcion:** FactSet's core value proposition is aggregating financial data and providing analytics/workflows for buy-side professionals. The rise of AI-native tools (ChatGPT, Claude, Perplexity, BloombergGPT) threatens to unbundle the "analytics" layer from the "data" layer. If AI agents can directly query data APIs and generate the same insights that a FactSet terminal provides, the $4K-50K/user/year pricing becomes hard to justify for the analytics portion.
- **Evidencia:**
  - Yahoo Finance reported a broad sell-off in financial data providers as investors reacted to AI-driven tools potentially competing with traditional platforms.
  - Wells Fargo cut FactSet's price target citing AI competition specifically.
  - Bloomberg has BloombergGPT with far larger proprietary datasets.
  - AI-native startups (AlphaSense, Fiscal.ai, etc.) are building alternatives at lower cost.
  - FactSet's AI response (Transcript Assistant, MCP server, Cobalt) is defensive, not offensive -- it is integrating AI into existing workflows rather than fundamentally reimagining the product.
- **Probabilidad:** Media-Alta (40-50%) -- The disruption is already underway. The question is speed and degree, not whether it happens.
- **Impacto si materializa:** If AI commoditizes the analytics layer over 3-5 years, FactSet's ASV growth could decelerate to 0-2% and margins could compress further by 300-500bps. Estimated equity impact: -25% to -40% from current levels. The "data infrastructure" pillar (CUSIP, Portware, Vermilion) is more defensible but only ~30-35% of total value.
- **Mitigante:** FactSet's operational infrastructure (CUSIP identifiers, portfolio management, compliance reporting) is deeply embedded in client workflows and much harder for AI to replace than analytics. 95% ASV retention rate suggests stickiness. Also, AI adoption requires data -- and FactSet IS the data source for many workflows.
- **Kill condition?:** YES -- If organic ASV growth decelerates below 3% for 2 consecutive quarters, or if a major buy-side firm publicly replaces FactSet with an AI-native alternative.

### 2. Revenue-Per-User Structural Decline (Unit Economics Deterioration)

- **Categoria:** Fundamental
- **Descripcion:** FactSet is growing users at 9.7% but organic ASV at only 5.9%. This means revenue per user is declining. This is not a one-quarter anomaly -- it reflects a structural shift where new users are being added at lower price points (wealth management, corporate clients) while existing buy-side seats face pricing pressure from competition and lower CPI-linked escalators.
- **Evidencia:**
  - Seeking Alpha analysis: "Revenue per user has declined, offsetting topline gains."
  - User count grew to 240,000 (+10% YoY) but ASV grew only 5.9%.
  - Lower CPI = lower annual price escalators (FactSet's pricing is partially CPI-linked).
  - New client segments (wealth, corporate) have lower ARPU than traditional buy-side.
  - Q1 FY26: net client additions of only 7 firms in the quarter -- growth is coming from more seats at existing clients at lower prices, not new logos.
- **Probabilidad:** Alta (60-70%) -- This is already happening and the trend is accelerating.
- **Impacto si materializa:** If revenue/user declines 2-3% annually while user growth normalizes to 5-6%, ASV growth converges to 3-4%. At 3-4% organic growth with margin compression, FactSet trades at a utility-like multiple (15-18x earnings) rather than a quality compounder multiple (25-30x). Current P/E of 13x already reflects pessimism, but there may not be expansion if the story is "growth decelerating toward GDP."
- **Mitigante:** Management is investing to drive higher-value product adoption (AI tools, deep sector analytics). If new products command premium pricing, ARPU could stabilize. Also, the 95% retention rate and >91% client retention show the base is sticky even if per-user pricing is under pressure.
- **Kill condition?:** YES -- If organic ASV growth falls below 4% for full fiscal year, or if retention rate drops below 93%.

### 3. Bloomberg/S&P Global Competitive Squeeze

- **Categoria:** Fundamental / Competitive
- **Descripcion:** FactSet holds ~4.5% of the financial data market vs. Bloomberg's ~33%. Bloomberg has effectively unlimited R&D budget (estimated $3-4B/year in technology spend) and is rapidly integrating AI. S&P Global, post-IHS Markit merger, now has the most comprehensive data set in the industry and is aggressively cross-selling Capital IQ Pro. LSEG (Refinitiv) is also investing heavily. FactSet is the smallest major player in a market trending toward consolidation and scale.
- **Evidencia:**
  - Bloomberg's market share is 7x FactSet's.
  - S&P Global's stock rose 23.6% in the past year while FDS fell 36% -- the market is voting.
  - Seeking Alpha article titled "FactSet: Prone To Lose Market Share" -- detailed analysis of competitive vulnerabilities.
  - "A more consolidated competitive landscape adds pressure on both FactSet's pricing power and potential volume growth."
  - The only area where FactSet has clear differentiation is buy-side workflow integration and CUSIP, which is under legal threat.
- **Probabilidad:** Alta (50-60%) -- The competitive pressure is ongoing and intensifying with each competitor's AI investment.
- **Impacto si materializa:** Gradual market share loss of 50-100bps/year would translate to ASV growth underperforming the industry. Over a 5-year horizon, FactSet could lose 10-15% of its enterprise value relative to a scenario where it maintains share. The risk is slow bleeding rather than catastrophic collapse.
- **Mitigante:** FactSet's buy-side focus is a niche that Bloomberg serves but does not optimize for. Deep workflow integration (portfolio analytics, compliance, reporting) creates switching costs. The CUSIP franchise is a unique asset. Amazon partnership for cloud delivery adds scale. $1B buyback authorization shows capital return focus.
- **Kill condition?:** YES -- If FactSet loses a Top 20 buy-side client to a competitor, or if organic ASV growth drops below the industry growth rate for 2+ consecutive years.

---

## Additional Risks (Not Top 3 but Material)

### 4. Value Trap / Dead Money Risk

- **Categoria:** Valoracion
- **Descripcion:** FDS is down 58% from its 2-year high. It trades at P/E 13x, which looks cheap vs. historical 25-30x. But is it cheap because of temporary margin compression, or because the market correctly recognizes structural challenges?
- **Evidencia:** Morgan Stanley and Stifel flag "structurally lower margins" and "uncertainty around how long the investment phase will last." The stock fell further on S&P Global's weak 2026 outlook (sympathy sell). No clear near-term catalyst -- Q2 FY26 earnings (March 2026) is next data point.
- **Mitigante:** FCF yield of 8.3% provides downside support. $1B buyback authorization. AI product adoption up 45% QoQ. If investment phase yields ASV acceleration to 7-8% in FY27, multiple re-rates significantly.
- **My assessment:** Not a classic value trap (the business is not deteriorating -- margins are compressing by choice, not by necessity). But could be dead money for 6-12 months until investment phase shows results. Moderate risk.

### 5. CUSIP Antitrust Class-Action

- **Categoria:** Legal
- **Descripcion:** Class-action lawsuit in SDNY alleges FactSet, S&P Global, and ABA "conspired for decades to eliminate competition" in CUSIP identifiers. The lawsuit survived a motion to dismiss in July 2023, which means it has legal merit. If FactSet loses, it could be forced to reduce CUSIP licensing fees or even divest the asset.
- **Evidencia:** CUSIP contributes ~$175M annual revenue at high margins. FactSet paid $1.93B for it. A ruling requiring open access or reduced fees could impair the asset by 30-50%. Worst case (forced divestiture) would be a $1-2B write-down.
- **Probabilidad:** Media (25-35%) for material adverse ruling. Low (10-15%) for forced divestiture.
- **Impacto:** If CUSIP licensing revenue drops 50%, that's ~$87M revenue loss (~4% of total) at high margins, impacting EPS by ~$1.50-2.00 (10-12% hit).
- **Mitigante:** Litigation timeline is 3+ years. FactSet can negotiate settlements. Even adverse ruling may result in price reduction, not elimination.

### 6. Buy-Side Structural Shrinkage

- **Categoria:** Fundamental
- **Descripcion:** Buy-side clients represent 82% of organic ASV. The buy-side industry is consolidating (hedge fund closures, asset manager mergers reduce total addressable seats). Passive investing's rise reduces active manager headcount. AI further threatens to automate analyst roles, reducing terminal seats needed.
- **Evidencia:** Net client addition of only 7 firms in Q1 FY26. Client retention at 91% (by number of clients, vs. 95% by ASV -- meaning smaller clients churn faster). Headcount reductions at major buy-side firms are well-documented.
- **Probabilidad:** Media (30-40%) for meaningful impact within 3 years.
- **Impacto:** If buy-side seats shrink 2-3% annually, FactSet needs to grow wealth/corporate faster to compensate. These segments have lower ARPU, reinforcing Risk #2.

### 7. Margin Compression Duration Uncertainty

- **Categoria:** Financiero
- **Descripcion:** FY26 guided adj. operating margin of 34-35.5% is down from 36.3% in FY25. Management calls this "investment phase" but provides no clear timeline for margin recovery. If this is a 1-2 year phenomenon, the stock is cheap. If it is 3-5 years, the stock may be fairly valued or overvalued.
- **Evidencia:** Stifel and Morgan Stanley both flagged uncertainty about duration. Technology investments in cloud, AI, cybersecurity are open-ended. Competitors are also increasing spend, creating an arms race dynamic.
- **Probabilidad:** Media for extended duration (2+ years of margin pressure).
- **Impacto:** Each 100bps of margin compression = ~$23M EBIT loss = ~$0.50 EPS impact.

---

## Riesgos NO Mencionados en Thesis

**No thesis exists yet. This assessment IS the first analysis.**

Key risks that a typical fundamental-analyst thesis might minimize or overlook:

| Riesgo | Severidad | Likely to be Minimized? | Comentario |
|--------|-----------|------------------------|------------|
| Revenue-per-user structural decline | HIGH | YES | Analysts tend to focus on topline ASV growth (5.9%) and miss that unit economics are deteriorating. 9.7% user growth masking pricing weakness. |
| CUSIP antitrust litigation | MEDIUM | YES | Often treated as "unlikely" in bull cases. But it survived MTD -- that alone means it has merit. $1.93B acquisition at risk. |
| Buy-side structural shrinkage (passive + AI headcount) | MEDIUM | YES | Most analyses assume TAM grows. But if active management AUM share keeps falling and AI replaces analysts, TAM for buy-side terminals may be flat or shrinking. |
| Competitor R&D outspend asymmetry | HIGH | YES | Bull cases often say "FactSet has niche focus." But Bloomberg spends 10x on tech. At some point, outgunned is outgunned. |
| Dead money / no clear catalyst | MEDIUM | POSSIBLY | With Q2 earnings not until March and no product catalyst expected, this stock could drift for months. |

---

## Kill Conditions Sugeridas

Based on this risk assessment, I recommend the following measurable kill conditions for any FDS thesis:

1. **KC#1: ASV Growth Collapse** -- Organic ASV growth falls below 3% for 2 consecutive quarters (current: 5.9%). This would signal the competitive and AI threats are materializing faster than expected.

2. **KC#2: Retention Rate Deterioration** -- Annual ASV retention drops below 93% (current: >95%). Retention is the single best indicator of product relevance. A meaningful decline signals clients are finding alternatives.

3. **KC#3: CUSIP Adverse Ruling** -- Court rules in favor of plaintiffs requiring open access to CUSIP identifiers or mandating material fee reductions (>30%).

4. **KC#4: Major Client Loss** -- Loss of any Top 10 buy-side client to Bloomberg, S&P Capital IQ, or an AI-native alternative, publicly confirmed.

5. **KC#5: Margin Compression Beyond Guide** -- Adjusted operating margin falls below 33% (below the low end of FY26 guidance of 34%) without corresponding revenue acceleration, indicating investment is not yielding returns.

6. **KC#6: CEO Departure** -- Philip Snow (CEO since 2015, 30 years at FDS, 88% Glassdoor approval) departs. The company's strategic pivot rests heavily on his leadership. A departure during the investment phase would create significant execution uncertainty.

7. **KC#7: Revenue-Per-User Decline Accelerates** -- If revenue per user declines >5% YoY for 2 consecutive quarters, the unit economics deterioration is becoming structural and the growth story is broken.

---

## Riesgo Agregado

- **Numero de riesgos HIGH+CRITICAL:** 3 (AI disruption, unit economics deterioration, competitive squeeze)
- **Riesgos correlacionados?** YES -- Risks #1, #2, and #3 are highly correlated. AI disruption enables competitors AND reduces FactSet's pricing power AND threatens buy-side seat counts. If AI disruption accelerates, ALL three risks materialize simultaneously. This correlation is the single most important risk factor.
- **Risk Score Final:** **MEDIUM-HIGH**

### Justification for MEDIUM-HIGH (not HIGH or VERY HIGH):

**Arguments for higher score:**
- 3 correlated HIGH risks is concerning
- Stock already down 58% from highs -- the market agrees these risks are real
- No clear near-term catalyst for re-rating
- Smallest player in a consolidating industry with scale advantages

**Arguments for lower score:**
- Financial position is strong (Net Debt/EBITDA 1.4x, FCF yield 8.3%, 13.8x interest coverage)
- 95% ASV retention rate is exceptional -- clients are NOT leaving
- CUSIP is a truly unique, monopolistic asset (despite legal risk)
- The margin compression is self-imposed (investment for growth), not forced by competition
- P/E of 13x already embeds significant pessimism -- much of the risk is priced in
- Employee sentiment is strong (3.9/5 Glassdoor, 88% CEO approval) -- no internal rot
- No SEC investigations, no short seller reports, no accounting controversies, no ESG issues

**Net assessment:** The risks are real but not existential. The business is under pressure but profitable, well-managed, and generating strong FCF. The primary question is whether FactSet can successfully navigate the AI transition and maintain relevance in a market dominated by larger players. This is a MEDIUM-HIGH risk, appropriate for a Tier B company requiring meaningful margin of safety.

---

## Implications for Thesis/Entry

- Entry price of $180 implies ~11% below current price of $203.60
- Given MEDIUM-HIGH risk score and 3 correlated HIGH risks, I would argue entry should be more conservative: $160-170 range (20-25% MoS vs. any reasonable FV estimate)
- Hard gate: Wait for Q2 FY26 earnings (March 2026) to see if ASV growth trend holds at 5.9% or decelerates
- The thesis bull case must explicitly address ALL three correlated risks with evidence, not dismiss them

---

## 🔄 META-REFLECTION

### Dudas/Incertidumbres
- **AI disruption speed is genuinely uncertain.** I classified it as Media-Alta probability, but the reality is this could be 2 years or 10 years. The financial data industry has been "about to be disrupted" for 20+ years, and incumbents keep winning. I may be overweighting recent AI hype.
- **CUSIP lawsuit impact is hard to quantify.** I estimated 30-50% revenue impairment if adverse, but the actual ruling could be anything from a token settlement to forced divestiture. The range of outcomes is wide.
- **Revenue-per-user decline may be strategic, not structural.** If FactSet is deliberately pricing lower to gain market share in new segments (wealth, corporate), the unit economics deterioration is a conscious choice that could yield higher total revenue. I may be interpreting a land-and-expand strategy as a weakness.

### Riesgos que Podrian Estar Subestimados
- **Buy-side structural shrinkage** -- I rated this MEDIUM but it could be HIGH if passive investing acceleration and AI-driven analyst headcount reductions compound faster than expected. The 82% revenue dependency on buy-side is a significant concentration.
- **Competitor outspend asymmetry** -- Bloomberg spending 10x on technology is not a temporary situation. It is a permanent structural disadvantage that compounds over time. I may be underrating the long-term impact.

### Discrepancias con Thesis
- No thesis exists yet. When the fundamental-analyst writes one, I would watch for:
  - Dismissing AI disruption risk as "FactSet is investing in AI too" (their spend is a fraction of competitors)
  - Anchoring to historical 45-year revenue growth streak as evidence of durability (past is not prologue in AI era)
  - Using the 95% retention rate as proof that "everything is fine" (retention is lagging indicator -- it drops AFTER alternatives emerge, not before)
  - Overstating CUSIP's moat without acknowledging the legal risk

### Sugerencias para el Sistema
- **Add "unit economics trajectory" as a standard risk factor** in the risk-identifier framework. Revenue-per-user trends are critical for subscription businesses and not currently in the standard risk categories.
- **Add "R&D spend asymmetry vs. competitors" as a standard risk factor.** Being outspent 10:1 on technology by the market leader is a material risk that should be systematically evaluated.

### Preguntas para Orchestrator
1. Should the entry price for FDS be lowered from $180 to $160-170 given the MEDIUM-HIGH risk score and 3 correlated HIGH risks?
2. Is there a precedent in our decisions_log for investing in the smallest player in a consolidating industry? How did that work out?
3. Given that 3 of the top risks are correlated (AI + competition + unit economics), should we apply a "correlation discount" to any FV estimate (e.g., 10-15% haircut to account for simultaneous materialization)?
4. Do we have sector view coverage for "Financial Data & Analytics"? FDS does not cleanly fit into any existing sector category.

---

## Sources

- [FactSet Q1 FY2026 Earnings](https://investor.factset.com/news-releases/news-release-details/factset-reports-results-first-quarter-fiscal-2026/)
- [FactSet Q4 FY2025 Earnings](https://investor.factset.com/news-releases/news-release-details/factset-reports-results-fourth-quarter-and-fiscal-2025)
- [FactSet: Prone To Lose Market Share - Seeking Alpha](https://seekingalpha.com/article/4852945-factset-prone-to-lose-market-share)
- [FactSet Unit Economics: User Growth vs Pricing - Seeking Alpha](https://seekingalpha.com/article/4855504-factset-stock-unit-economics-user-growth-versus-pricing)
- [Wells Fargo Cuts FDS Price Target on AI Competition](https://www.investing.com/news/analyst-ratings/factset-research-stock-falls-as-wells-fargo-cuts-price-target-on-ai-competition-93CH-4246349)
- [FactSet Faces AI Pressure - Yahoo Finance](https://finance.yahoo.com/news/factset-faces-ai-pressure-investors-111103196.html)
- [CUSIP Antitrust Lawsuit - WatersTechnology](https://www.waterstechnology.com/regulation/7936086/class-action-lawsuit-takes-aim-at-cusip-sp-factset-aba)
- [CUSIP Antitrust Motion to Dismiss Ruling](https://www.waterstechnology.com/data-management/7951120/antitrust-complaint-against-cusip-can-go-forward-sdny-judge-rules)
- [Moody's and FDS Slide on SPGI Weak 2026 Outlook](https://www.investing.com/news/stock-market-news/moodys-and-factset-stocks-slide-on-sp-globals-weak-2026-outlook-4496367)
- [FactSet AI Workflow Revolution - BeyondSPX](https://www.beyondspx.com/quote/FDS/factset-s-ai-workflow-revolution-why-the-market-is-missing-the-plot-nyse-fds)
- [FactSet Insider Trading Activity - MarketBeat](https://www.marketbeat.com/stocks/NYSE/FDS/insider-trades/)
- [FactSet Glassdoor Reviews](https://www.glassdoor.com/Reviews/FactSet-Reviews-E6066.htm)
- [Philip Snow CEO Rating - Comparably](https://www.comparably.com/companies/factset/ceo-rating)
- [FactSet Sustainalytics ESG Rating](https://www.sustainalytics.com/esg-rating/factset-research-systems-inc/1008225915)
- [FactSet Cash Flow Recovery Analysis - Trefis](https://www.trefis.com/stock/fds/articles2/590152/could-factset-research-systems-stocks-cash-flow-spark-the-next-rally/2026-02-07)
