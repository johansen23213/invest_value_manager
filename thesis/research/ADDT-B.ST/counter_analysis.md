# Counter-Analysis: ADDT-B.ST (Addtech AB ser. B)

## Fecha: 2026-02-19

## Resumen Ejecutivo

The R1 thesis correctly identifies Addtech as a high-quality serial acquirer and appropriately concludes WATCHLIST at SEK 200 given the extreme overvaluation at SEK 322. The thesis survives scrutiny on its business quality assessment but has three significant weaknesses: (1) the QS adjustment from 70 to 79 is partially unjustified and inflates the Tier from B to A, (2) the organic growth weakness is underweighted as a structural risk, and (3) the Fair Value of SEK 250 is generous given that it requires a SEK 40 upward "rounding" from the weighted average of SEK 210. The good news: the WATCHLIST verdict is correct, and the entry price of SEK 200 provides adequate protection. The bear case conviction is **6.5/10** -- moderate-strong. The thesis is directionally right but the FV and QS are flattering.

---

## Asunciones Clave Desafiadas

### 1. QS Adjustment of +9 Points (70 to 79, Tier B to Tier A)

- **The assumption:** Addtech deserves a +4 ROIC adjustment (partial-goodwill) and a +5 market position correction, elevating it from QS 70 (Tier B) to QS 79 (Tier A).

- **Evidence against:**
  - **The ROIC adjustment (+4) is defensible but modest.** Goodwill at 29.9% of assets is below the ROP 50% threshold. The standard ROIC of 17.9% is already STRONG and positive vs WACC. This is not the same situation as ROP where ROIC appeared negative without adjustment. The adjustment reveals a better picture (22.9% vs 17.9%) but does not correct a misleading one. Proportionally correct per protocol.
  - **The market position adjustment (+5) is subjective and problematic.** The thesis claims Addtech is "#2-3 Nordic serial acquirer" and assigns 5/8 for market position. But Addtech is not a market position holder in the traditional sense -- it holds positions in 150+ micro-niches. No single subsidiary has a dominant market position in a measurable addressable market. The "serial acquirer ranking" is not a market position -- it is a business model ranking. A 5/8 score implies "#3-5" market position, but in WHAT market? Industrial distribution in Europe is a >EUR 50B fragmented market where Addtech has ~1.5-2% share. That is not #3-5. The adjustment conflates "quality of the acquisition machine" with "market position" which is a different concept.
  - **The Tier jump from B to A has material consequences.** It changes the MoS requirement (from ~20-25% for Tier B to ~15-20% for Tier A per precedents). It also signals "quality compounder" when the organic growth is only 2%. A business that cannot grow organically above 2% is NOT a compounder in the traditional sense -- it is a financial engineering vehicle.
  - **The moat assessor proposed +11 (not +9), including +2 for insider ownership.** The orchestrator already rejected the additional +2 for insider ownership. But the moat assessor's reasoning was that dual-class voting control (31.6%) should override the 2.0% capital stake. This is a reasonable argument, but the quality_scorer.py measures CAPITAL at risk, not voting control. Voting control protects against hostile takeovers but does not align economic incentives the same way as capital ownership. The Borjesson/Hedelius families have only 4.6% of CAPITAL invested -- their downside from poor decisions is limited.

- **Severity:** MODERATE
- **Resolution suggested:** Accept the +4 ROIC adjustment (protocol-compliant). Reduce the market position adjustment from +5 to +3 (reflecting #3-5 in Nordic serial acquirer space, but acknowledging it is not a traditional market position). This gives QS 77 -- still Tier A but at the lower boundary, more accurately reflecting the business. Alternatively, keep QS 70 as Tier B (upper) and apply Tier B MoS requirements (20-25%), which the thesis already does.

### 2. Organic Growth of 2% is Primarily Cyclical (60% Probability per Thesis)

- **The assumption:** The thesis assigns 60% probability to cyclical explanation, 30% structural, 10% mix effect. It expects organic growth recovery above 5% as a catalyst.

- **Evidence against:**
  - **The 2% organic growth has persisted for 5+ quarters** (since at least Q2 FY2024/25 through Q3 FY2025/26). Five quarters is no longer "a temporary dip" -- it is a trend.
  - **The problem is broad-based, not localized.** Medical, sawmill, defense, and automation ALL showed weak development in Q3 FY2025/26. Energy and special vehicles were bright spots, but they cannot carry the whole portfolio.
  - **European industrial recovery is NOT materializing.** Eurozone Manufacturing PMI was 49.5 in January 2026 -- still in contraction territory for 22+ consecutive months. German manufacturing PMI is the worst in the group. The "H2 2026 recovery" thesis has been deferred multiple times over the past 18 months.
  - **Addtech's target of 7.5% organic growth has NEVER been achieved recently.** The company's own stated growth model assumes 7.5% organic + 7.5% acquired = 15% total. Actual organic growth: FY2023/24 ~3%, FY2024/25 2%, Q3 FY2025/26 1%. The trajectory is DECLINING, not stabilizing.
  - **Peers show the same pattern.** Indutrade reported ~2% organic growth. Lagercrantz ~3%. This is not Addtech-specific -- it is structural to the Nordic industrial distribution model. These businesses distribute into mature European industrial markets growing at GDP rates (1-2%).
  - **The margin expansion (11% to 15.6% EBITA) may be masking organic weakness.** When organic volumes are flat, margins can temporarily expand through cost discipline and mix shift. But this is a one-time lever, not a permanent growth driver. As the In Practise research noted: "Having played the margin expansion ace already, it will be harder for these blue chips to deliver outsize earnings growth over the next decade."

- **Severity:** HIGH
- **Resolution suggested:** Reweight the cyclical/structural probability split to 40% cyclical / 50% structural / 10% mix. At 50% structural probability, the base case FV should reflect permanently lower organic growth (1-3%), not a recovery to 5%+. This lowers the growth input in the OEY method from 10% to 8%, which drops the OEY-derived FV from SEK 194 to approximately SEK 150-160.

### 3. Fair Value of SEK 250 (vs Weighted Average of SEK 210)

- **The assumption:** The thesis calculates a weighted average FV of SEK 210 from two methods (EV/EBITA SEK 220 at 60% + OEY SEK 194 at 40%), then ROUNDS UP to SEK 250 to account for "quality premium, margin expansion trajectory, structural tailwinds, and conservative EBITA multiple."

- **Evidence against:**
  - **The SEK 40 upward adjustment (19% premium to the weighted calculation) is not quantitatively justified.** The thesis lists four qualitative reasons but does not show how each translates to a specific SEK amount. This is exactly the kind of "narrative premium" that Error #49 (anchoring to consensus) warns against. The consensus mean PT is SEK 378 -- the thesis started at SEK 210, then rounded toward consensus.
  - **The "conservative EBITA multiple (20x vs sector 25-32x)" argument is circular.** The thesis uses 20x as conservative, gets SEK 220, then says the 20x was too conservative and rounds up to SEK 250 (effectively implying 23x EBITA). If 23x was the right multiple, it should be used explicitly, not backdoored through a quality premium.
  - **Every upward adjustment for quality is already embedded in the QS.** The QS of 79 (Tier A) already reflects the quality of the business. Adding a further quality premium to the FV double-counts the quality factor.
  - **The OEY method at SEK 194 is more appropriate for the current growth reality.** With organic growth at 2% and total growth at 5-9%, the 10% growth assumption in the OEY method is already generous. The weighted average of SEK 210 is closer to fair than SEK 250.

- **Severity:** HIGH
- **Resolution suggested:** Use the weighted average of SEK 210 as the FV without rounding adjustment. Or if a quality premium is applied, limit it to +10% (SEK 231). Entry price at 20% MoS from SEK 210 = SEK 168. From SEK 231 = SEK 185. Both are below the thesis entry of SEK 200 but more defensible.

### 4. Acquisition Pipeline Sustainability at Reasonable Multiples

- **The assumption:** The thesis assumes Addtech can sustain 12 acquisitions/year at 6-8x EBIT indefinitely, providing 5-7% acquired growth.

- **Evidence against:**
  - **The Nordic serial acquirer playbook is now widely replicated.** Storskogen (before its collapse), Roko (newly IPO'd), Boreo, Teqnion, and international players like Halma and Diploma ALL compete for the same pool of Nordic family-owned niche businesses. The universe of targets is FINITE.
  - **Storskogen's collapse is a cautionary tale.** Storskogen grew from SEK 1.7B to SEK 34B revenue via 200+ acquisitions, then collapsed when net debt/operating cash flow hit 9x. The lesson: rapid serial acquisition can mask deteriorating deal quality. Addtech is far more disciplined, but the competitive dynamics that drove Storskogen's collapse (too many buyers chasing finite targets) affect all players.
  - **Acquisition multiples are reportedly rising.** Industry commentary suggests multiples have crept from 5-7x EBIT to 8-12x for quality targets. Addtech management states 6-8x, but this is self-reported and may exclude earn-outs. The Q2 FY2025/26 report shows SEK 456M consideration for 3 acquisitions contributing SEK 225M goodwill -- goodwill at 49% of consideration is at the high end of the range, consistent with rising multiples.
  - **Geographic expansion into UK/Germany has different dynamics.** These are more competitive M&A markets with higher multiples than the Nordics. Expanding the target universe means accepting worse economics per deal.
  - **Scale limits.** At SEK 22B revenue and 150+ subsidiaries, Addtech needs larger deals to move the needle. But larger deals carry higher execution risk and higher multiples. The SEK 133M average deal adds only 0.6% to revenue -- maintaining 7% acquired growth requires 12+ deals per year, forever.

- **Severity:** MODERATE
- **Resolution suggested:** Model a scenario where acquisition ROIC degrades from 15%+ to 10-12% over 5 years as multiples rise. This reduces the value-creation spread from M&A and should compress the fair multiple from 20x to 17-18x EBITA. Incorporate this into the bear case more prominently.

### 5. CEO Insider Selling Pattern

- **The assumption:** The thesis notes the CEO sold 11% of his holding but classifies it as a MEDIUM risk, partially offset by board member purchases.

- **Evidence against:**
  - **The CEO sold SEK 9.8M at SEK 349 then bought back SEK 2.0M at SEK 332.** This is a net sale of SEK 7.8M. The pattern looks like TRADING, not diversification. A CEO who believed in long-term compounding would not sell at SEK 349 and rebuy at SEK 332 -- they would hold.
  - **The CEO's total holding is only 2.0% of capital.** After selling 11% of that, he holds ~1.8%. This is very low alignment for a SEK 87B company. Compare to Lifco where the Stahl family holds ~30%, or Lagercrantz with ~15% foundation ownership.
  - **Board member Fredrik Borjesson's December 2025 purchase (SEK 26.7M) offsets numerically but is a different signal.** Borjesson is a founding family member exercising stewardship. The CEO is the OPERATOR -- his signal matters differently. A founding family maintaining their multi-generational stake is not the same as the CEO increasing conviction.
  - **The thesis notes this but does not adequately weight it.** In our system, the GL insider selling case (Session 76) established that exercise-and-sell vs open-market selling matters. The CEO's open-market sale at SEK 349 followed by a smaller open-market rebuy is NET SELLING -- not exercise-and-sell.

- **Severity:** MODERATE
- **Resolution suggested:** Weight the CEO selling pattern as a moderately negative signal for conviction. Do not elevate to HIGH because the net insider activity (last 90 days) is positive. But document that the CEO's personal alignment is LOW and declining.

---

## Desafios por Categoria

### Negocio

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | Organic growth of 2% is structural, not cyclical | 5+ quarters of weakness, Eurozone PMI <50 for 22 months, peers show same pattern, management's 7.5% target never achieved recently | HIGH |
| 2 | "Margin expansion ace" already played -- 11% to 15.6% EBITA | In Practise research: harder to deliver outsize growth after margin expansion. One-time lever, not permanent | MODERATE |
| 3 | The moat is the acquisition machine, not the underlying businesses | Remove M&A overlay and organic growth is 1-2% -- GDP-level. Individual subsidiaries are mature niche distributors | MODERATE |
| 4 | Peer comparison shows Addtech is NOT best-in-class on margins | Lifco EBITA 24.2% vs Addtech 15.6%. Addtech is #2-3, not #1 | LOW |

### Valoracion

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | FV SEK 250 is a 19% premium to the calculated weighted average (SEK 210) | Four qualitative justifications without quantification. Double-counts quality already in QS | HIGH |
| 2 | 42x P/E implies 22.4% annual FCF growth -- impossible to sustain | Current total growth 5-9%, organic 2%. Gap of 13-17pp between implied and actual | HIGH |
| 3 | Reverse DCF shows market prices perfection | Even at bull case 12% growth, OEY FV is SEK 280 -- below current price. Market needs 22%+ | HIGH |
| 4 | EV/EBITA of 20x used in thesis is "conservative" but peers trade at 25-40x -- creates false sense of discount | Thesis uses 20x, rounds up to effective 23x. Actual question: what is the CORRECT multiple for a business with 2% organic growth? | MODERATE |
| 5 | Nordic serial acquirer multiples cluster: Lifco 40x, Lagercrantz 38x, Indutrade 32x, Addtech 42x | Addtech trades at the HIGHEST P/E of the peer group despite having the lowest organic growth | MODERATE |

### Riesgos

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | Goodwill accumulation trajectory: 25.8% to 29.9% of assets in 3 years | At this pace, crosses 50% threshold in ~7 years. Impairment never tested in severe recession. IFRS impairment losses for goodwill are NEVER reversible | HIGH |
| 2 | Acquisition multiple inflation from PE competition | Nordic M&A market is "heating up" per White & Case. EQT plans to double European investments. More capital chasing same targets | MODERATE |
| 3 | Storskogen/Teqnion precedent shows serial acquirer model can fail catastrophically | Storskogen: 200+ acquisitions, net debt/OCF 9x, collapsed. Teqnion: CFO instability, goodwill-heavy allocation, acquisition write-off | MODERATE |
| 4 | Covenant risk in stress scenario not quantified | Thesis identifies covenants but does not know threshold levels. Goodwill impairment + earnings decline could approach limits simultaneously | LOW |

### Timing

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | No catalyst for a decline to SEK 200 entry price (-38%) | Stock would need to fall 38% from current levels. Even the 52-week low is SEK 254. Without a specific catalyst, waiting could be indefinite | MODERATE |
| 2 | The stock is only -12% from 52-week high -- minimal distress | Compare to portfolio precedents: ADBE -30%, LULU -58%, NVO -49%, BYIT.L -47%. Addtech has NOT experienced the kind of drawdown that creates opportunity | MODERATE |
| 3 | Q4 FY2025/26 results (May 2026) could be catalyst if organic growth deteriorates further | Automation segment facing "challenging market situation" per Q3 call. If organic growth turns negative, multiple compression follows | LOW |

---

## Conflictos con Otros Analisis

### Moat Assessment vs Thesis

- **Moat assessor classified: NARROW (borderline Wide)** with 18/25 score
- **Thesis effectively treats it as Wide** by applying Tier A treatment and quality premium to FV
- **Resolution:** The NARROW classification should temper the FV premium. A Narrow moat business dependent on M&A execution should not receive the same quality premium as a Wide moat compounder (like ADBE or AUTO.L) that grows organically.

### Moat Assessor QS Suggestion vs Thesis QS

- **Moat assessor proposed QS 81 (+11 adjustment)** including +2 for insider ownership
- **Thesis settled on QS 79 (+9 adjustment)** correctly rejecting the insider ownership uplift
- **My view: QS 73-77** -- the market position adjustment should be +3 not +5
- **Consequence:** At QS 73, Addtech is Tier B (upper). At QS 77, it is borderline Tier A. The difference matters for MoS requirements.

### Risk Assessment vs Thesis

- **Risk assessment classified: HIGH** (1 CRITICAL, 3 HIGH)
- **Thesis acknowledges but the WATCHLIST verdict inherently accepts the risk assessment**
- **No conflict** -- both agree current price is too high

---

## Veredicto Global

| Metric | Valor |
|--------|-------|
| Desafios HIGH/CRITICAL | **5** of 16 total |
| Desafios no resueltos por thesis | **3** (FV rounding, organic growth structural probability, QS adjustment) |
| Veredicto | **MODERATE COUNTER** |

### Interpretacion

**MODERATE COUNTER:** The thesis has meaningful gaps that require adjustment, but the overall direction is correct. The WATCHLIST verdict is appropriate. The bear case is:

1. The FV should be SEK 210-230, not SEK 250. Entry price should be SEK 170-185, not SEK 200.
2. The QS should be 73-77 (Tier B upper / Tier A lower boundary), not a confident 79.
3. The organic growth risk is underweighted -- structural at 50%+ probability, not 30%.
4. The stock may never reach the entry price without a specific catalyst, making this a perpetual watchlist item.

**Bear Case Conviction: 6.5/10** -- The thesis is not wrong, it is generous. The quality is real but the FV is flattering. The entry price of SEK 200 provides adequate protection but the probability of reaching it is low without a market correction or an organic growth shock.

---

## Recomendacion al Investment Committee

1. **Reduce FV from SEK 250 to SEK 220-230.** The SEK 40 rounding premium above the weighted average is not quantitatively justified. A maximum 10% quality premium on the weighted SEK 210 = SEK 231.

2. **Reduce entry price from SEK 200 to SEK 175-185.** At QS 73-77, the MoS requirement is 20-25% (Tier B precedent). 20% MoS on SEK 230 = SEK 184. 25% MoS = SEK 173.

3. **Do NOT create a standing order.** The stock is 38%+ above entry. There is no near-term catalyst for a decline of that magnitude. Add to quality_universe as monitoring item, set price alert at SEK 250 for deeper re-analysis.

4. **Classify QS as 73-77 (Tier B upper, borderline Tier A).** The market position adjustment should be +3 not +5 given the lack of a traditional measurable market position.

5. **Monitor organic growth as the KEY variable.** If organic growth recovers to 4%+ for 2+ consecutive quarters, upgrade to confident Tier A and raise FV. If organic growth turns negative, this becomes a clear AVOID at any price above SEK 180.

6. **Investigate before proceeding to R3:**
   - What is the EXACT goodwill figure from the FY2024/25 annual report? (The thesis uses estimates.)
   - What is the 5-year organic growth average? (Only recent quarters are cited.)
   - What are the actual acquisition multiples paid in the last 3 years? (Management claims 6-8x but no independent verification.)

---

## META-REFLECTION

### Dudas/Incertidumbres
- I could not find specific bear case research on Addtech from short sellers or bearish analysts. Most coverage is bullish, reflecting the "quality compounding" narrative. This could mean: (a) the bear case is genuinely weak, or (b) the stock is under-scrutinized because it is a mid-cap Swedish stock with limited international coverage. I lean toward (b), which means my independent bear case may be the first rigorous one assembled.
- The distinction between "cyclical organic weakness" and "structural organic weakness" is the most important unresolved question. I weighted it toward structural based on the duration (5+ quarters) and peer comparison, but I acknowledge that a European industrial recovery could quickly change this picture. The Eurozone PMI approaching 50 suggests the bottom may be near.
- The goodwill figure is estimated (~SEK 5.5B based on yfinance) rather than independently verified from the annual report. If actual goodwill is higher (e.g., SEK 7B), the impairment risk and QS adjustment both change.

### Limitaciones de Este Analisis
- No access to Addtech's full annual report PDF (corruption issues noted by fundamental-analyst). The exact goodwill breakdown, individual CGU analysis, and earn-out details would strengthen the impairment risk assessment.
- Acquisition multiple data is from industry commentary, not from Addtech's own deal disclosures. The company does not publish individual deal multiples.
- I could not assess the quality distribution of the 150+ subsidiaries -- are the best 20 carrying the worst 130? This is unknowable from outside but would materially affect the structural vs cyclical organic growth debate.
- Swedish Finansinspektionen insider filing data would provide more granular insider activity analysis. The current tools missed the CEO sale initially.

### Sugerencias para el Sistema
- **The market position adjustment for serial acquirers needs a protocol.** The current QS framework does not handle conglomerates of 150+ niche businesses well. A "serial acquirer" override should exist that scores based on acquisition machine quality metrics (deal pace, ROIC on acquisitions, success rate) rather than trying to force-fit traditional market position scoring.
- **The FV rounding/quality premium should be capped at 10% above weighted calculation** to prevent narrative drift. If the analyst believes the multiple is too conservative, they should use a higher multiple directly, not backfill it through rounding.
- **A "catalyst probability" assessment should be added for WATCHLIST verdicts.** Addtech at SEK 200 is a great buy -- but what is the probability of getting there within 12 months? If <15%, the watchlist entry provides little practical value vs. monitoring the quality_universe.

### Preguntas para Orchestrator
1. Should the FV rounding protocol be established as a system rule? The +19% premium from weighted average to stated FV is the largest such rounding I have seen in the system.
2. Is the QS market position adjustment of +5 for serial acquirers justified by protocol, or should a lower adjustment (+3) be the standard for businesses without traditional measurable market positions?
3. Should the organic growth trajectory be classified as a kill condition? Currently, KC#1 triggers only on "negative organic growth for 2+ years." Should there be an intermediate warning at "organic growth below 3% for 4+ quarters"?
4. Given the stock needs to fall 38% to reach entry, should we classify this as "monitoring only" rather than "active watchlist" to avoid anchoring bias toward a price that may never arrive?

---

**Sources:**
- [Addtech Q3 2025/26 Slides - Investing.com](https://www.investing.com/news/company-news/addtech-q3-202526-slides-margin-expansion-drives-9-ebita-growth-despite-modest-sales-93CH-4486854)
- [Addtech Q3 2025 Earnings Call Transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-addtech-q3-2025-sees-eps-rise-stock-gains-93CH-4486821)
- [The Swedish Serial Acquirer Dilemma - Edelweiss Capital](https://edelweisscapital.substack.com/p/the-swedish-serial-acquirer-dilemma)
- [Rollups From Hell: Storskogen](https://rollupeurope.com/p/rollups-from-hell-vol-1-storskogen-the-arsonist-in-sweden-s-holy-holdco-forest)
- [Lifco Stock: Quiet Compounder Or Hidden Value Trap?](https://www.ad-hoc-news.de/boerse/news/ueberblick/lifco-stock-quiet-compounder-or-hidden-value-trap-a-deep-dive-into-the/68571044)
- [Northern Dealmaking Heats Up - White & Case](https://mergers.whitecase.com/highlights/northern-dealmaking-heats-up-nordic-ma-and-pe-activity-on-the-rise-in-2025)
- [Addtech CEO Niklas Stenberg Sells Shares - MarketScreener](https://www.marketscreener.com/quote/stock/ADDTECH-AB-15223809/news/Addtech-CEO-Niklas-Stenberg-sells-shares-for-just-under-SEK-10-million-50025002/)
- [Euro Area Manufacturing PMI - Trading Economics](https://tradingeconomics.com/euro-area/manufacturing-pmi)
- [Judges Scientific Unfavorable Conditions - MarketScreener](https://www.marketscreener.com/quote/stock/JUDGES-SCIENTIFIC-PLC-4004055/news/Judges-Scientific-suffers-from-unfavorable-conditions-in-some-of-its-markets-49435360/)
- [Roko IPO & Swedish Serial Acquirers - In Practise](https://inpractise.com/articles/roko-ipo-and-swedish-serial-acquirers)
- [Addtech Year-End Report 2024/2025](https://yearend2425.reports.addtech.com/)
- [Addtech Owners Page](https://www.addtech.com/investors-and-media/the-share/owners)
- [Addtech Insider Trading Activity - InsiderScreener](https://www.insiderscreener.com/en/company/addtech-ab)
