# Counter-Analysis: REN.AS (RELX PLC) -- R2 Devil's Advocate

## Fecha: 2026-02-24

---

## CRITICAL FINDING (HIGHLIGHT FOR ORCHESTRATOR)

**The thesis claims ROIC of 23% with +18pp spread over WACC. RELX's OWN 2025 annual report states post-tax ROIC of 15.4%.** The thesis's ROIC figure likely comes from quality_scorer.py using a GAAP/yfinance methodology that excludes goodwill from invested capital. Since RELX has goodwill at 54% of total assets (legacy of extensive M&A), stripping goodwill OVERSTATES economic returns. The company's self-reported 15.4% ROIC includes goodwill in the capital base -- a more honest measure of returns on capital actually deployed. This reduces the ROIC spread from +18pp (thesis) to +8pp (reality at 7.5% WACC) or +6.4pp (at RELX's 9% reported cost of capital). This is a MATERIAL overstatement that affects the entire quality thesis.

**Severity: HIGH**. Does not invalidate the thesis (15.4% ROIC is still good) but significantly weakens the "23% ROIC compounder" narrative.

---

## Resumen Ejecutivo

The RELX thesis is a competent R1 analysis of a genuinely high-quality business. However, it suffers from **three significant weaknesses**: (1) ROIC overstatement via goodwill exclusion, (2) underestimation of the Elsevier open access disruption risk, and (3) a valuation approach that relies heavily on a re-rating assumption with thin downside protection (bear FV EUR 22 is above current price adjusted). The bull case for AI as a tailwind is *plausible but unproven at scale*, and the Harvey-LexisNexis partnership introduces cannibalization risk that the thesis does not address. The thesis correctly identifies this as a WATCHLIST candidate (not a buy), and I agree with that verdict -- but the entry price of EUR 23-24 may still be insufficient given the risks below.

**Bottom line:** The thesis survives scrutiny but requires adjustments. The ROIC should be corrected, the bear case should be expanded, and the FV should be stress-tested with the company's own ROIC figure rather than the tool's inflated number.

---

## Asunciones Clave Desafiadas

### 1. "ROIC of 23% with +18pp spread over WACC"

- **Evidencia en contra:** RELX's own 2025 annual report states post-tax return on average invested capital of 15.4% (up from 14.8% in 2024). This is the company's preferred metric, which includes accumulated goodwill and amortization in the invested capital base. The thesis figure of 23% appears to come from quality_scorer.py, which likely strips goodwill from invested capital. For a company with 54% of total assets as goodwill from decades of acquisitions, this is a meaningful distortion. Independent sources (GuruFocus) show ROIC at 23.66% using a goodwill-excluded methodology, confirming the discrepancy is methodological, not an error -- but the company's own calculation is the more conservative and honest measure.
- **Severity:** **HIGH**
- **Resolution sugerida:** Use RELX's reported 15.4% ROIC as the primary figure. Note the tool's 23% as the "goodwill-stripped" figure for comparability. The ROIC spread narrows to +8pp over a 7.5% WACC -- still positive and still Tier A territory, but materially weaker than the +18pp claimed. This should be reflected in QS assessment and valuation narrative.

### 2. "AI is a TAILWIND, not a threat"

- **Evidencia en contra:** The thesis presents AI as unambiguously positive for RELX. The reality is more nuanced:
  - **Anthropic Claude Cowork launch (early 2026)** specifically targeted legal teams and academic researchers -- RELX's core customers. This was the direct catalyst for the 16% single-day crash in RELX shares in Feb 2026 (alongside Experian and LSEG).
  - **Harvey AI** raised $300M at $5B valuation and now has a strategic partnership with LexisNexis -- but this partnership was DEFENSIVE, not offensive. The Artificial Lawyer analysis notes LexisNexis "effectively conceded it could not build comparable technology independently." This is a company that is LICENSING its data to a potential disruptor rather than building the AI layer itself.
  - **Thomson Reuters acquired CaseText for $650M** -- showing the competitive response to AI legal research is real and well-funded.
  - The Harvey partnership introduces **pricing cannibalization risk**: Harvey can license Lexis data and potentially bundle it at lower prices than direct Lexis subscriptions. Harvey's $3B valuation implies $200M+ ARR by 2027, and that ARR will partly come from customers who might otherwise buy direct Lexis subscriptions.
  - **Per-seat pricing erosion** (SaaSpocalypse lesson L-12 from ROP analysis) applies directly: AI agents doing legal research reduce the number of human researchers who need Lexis seats.
- **Severity:** **MODERATE**
- **Resolution sugerida:** The thesis should present AI as "net positive but with meaningful transition risks and cannibalization uncertainty," not as an unambiguous tailwind. The Harvey partnership is a smart defensive move, but it demonstrates that RELX cannot build the AI layer itself -- it is a DATA PROVIDER to AI, not an AI company. Long-term, the value may accrue to the AI layer (Harvey, Claude, etc.), not the data layer (RELX).

### 3. "WIDE moat via irreplaceable proprietary data"

- **Evidencia en contra:** The moat score of 22/25 is reasonable for Risk and Legal segments, but the STM (Elsevier) moat is under ACTIVE assault:
  - **9+ UK universities have opted out of the Elsevier deal** as of Feb 2026 (Sheffield, Lancaster, Surrey, Essex, Kent, Sussex, York, Swansea, Sheffield Hallam). One Russell Group institution called terms "financially unsustainable."
  - **"Silent decoupling"** is underway -- universities are quietly dropping Elsevier without fanfare, potentially leading to "double-digit exits" in coming months.
  - **Australia/New Zealand (CAUL)** also experienced disruptions to Elsevier access for 2026.
  - **20,908 academics** have signed the "Cost of Knowledge" boycott against Elsevier.
  - **Plan S** and national open access mandates (Sweden goal: OA by 2026) are structural regulatory headwinds.
  - **Sci-Hub** provides free access to virtually all Elsevier papers, undermining the subscription model at the margin.
  - STM is ~33% of revenue but growing at only 5% (lowest segment). If university opt-outs accelerate and open access mandates tighten, this segment's growth could stall or go negative.
- **Severity:** **MODERATE-HIGH**
- **Resolution sugerida:** The moat should be disaggregated by segment. Risk and Legal have WIDE moats. STM/Elsevier has a moat that is NARROWING under institutional pressure and regulatory mandate. The aggregate 22/25 moat score overstates the true picture. A disaggregated approach: Risk (10/10), Legal (9/10), STM (6/10), Exhibitions (5/10) = weighted 7.9/10 vs 8.8/10 aggregate.

### 4. "Revenue growth accelerating: 7% FY2025"

- **Evidencia en contra:** Bloomberg headline after FY2025 results: "RELX's Sales Growth Misses Analyst Estimates." While 7% underlying growth is solid, it is not the "accelerating" narrative the thesis claims. Historical context:
  - FY2024: 7% underlying growth
  - FY2025: 7% underlying growth (flat, not accelerating)
  - H1 2025: 8% underlying growth (H2 decelerated)
  - The 7% headline was a deceleration from H1 momentum.
  - Analyst estimates were higher, hence the Bloomberg "miss" framing.
  - This is a semantic point -- 7% is still strong -- but the thesis narrative of "acceleration" is overstated.
- **Severity:** **LOW**
- **Resolution sugerida:** Describe growth as "consistent at 7%" rather than "accelerating." The Legal segment IS accelerating (9% vs historical 5-6%), but the aggregate is not.

### 5. "Fair Value EUR 33.50 with WACC of 7.5%"

- **Evidencia en contra:** Multiple valuation concerns:
  - **WACC calculation is below RELX's own cost of capital.** The thesis uses 7.5% WACC. RELX's own calculation (which uses a more standard equity risk premium methodology) implies a higher rate. The tool's default of 9% may actually be closer to reality for a European-listed company. Using 8.5% WACC (midpoint) instead of 7.5% significantly reduces DCF FV.
  - **DCF terminal value is 80.6% of enterprise value.** The thesis correctly flags this as "high." For context, a DCF where >75% of value comes from the terminal value is essentially a perpetuity calculation, not a 5-year cash flow analysis. The thesis's DCF FV of EUR 31 is heavily dependent on the terminal growth rate and WACC assumptions -- small changes produce large swings (EUR 22-32 range on WACC sensitivity).
  - **The OEY/Earnings method uses 24x P/E.** The thesis justifies this by noting RELX's historical range is 20-35x. But the current market regime (SaaSpocalypse, AI disruption fears) has structurally de-rated information services companies. RELX peers: WKL.AS at 13x, IT at 16x. Using RELX's current 21x as the fair P/E (which assumes NO re-rating) gives FV = EUR 27 -- essentially current price, implying zero MoS.
  - **The thesis acknowledges E[CAGR] of 10.6% is below the 12% Tier A threshold.** This is correct and honest. But it then attempts to rescue this by arguing "with compounding, 17-20% CAGR." This is double-counting: if FV already reflects earnings at fair multiple, adding earnings growth ON TOP assumes the multiple stays constant as earnings grow -- i.e., it assumes the stock is permanently cheap, which contradicts the mean-reversion thesis.
- **Severity:** **MODERATE-HIGH**
- **Resolution sugerida:** The valuation needs stress-testing with more conservative assumptions: (a) WACC 8.5% (closer to tool default and RELX's implied cost of capital), (b) P/E 20-22x (current market regime, not historical peak), (c) Terminal growth 2.0% (not 2.5%). Under these assumptions, FV would be approximately EUR 27-29, and MoS at current price of EUR 26.80 would be negligible (0-8%). This significantly weakens the investment case at current levels.

---

## Desafios por Categoria

### Negocio

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | ROIC overstatement (23% vs 15.4% reported) | RELX 2025 Annual Report, RELX press release | HIGH |
| 2 | Elsevier open access disruption accelerating | 9+ UK universities opted out (Feb 2026), "silent decoupling" underway, 20K boycott signatories | MODERATE-HIGH |
| 3 | Harvey partnership is defensive, not offensive | Artificial Lawyer analysis: LexisNexis "conceded it could not build comparable technology independently" | MODERATE |
| 4 | AI is dual-edged, not pure tailwind | Anthropic Claude Cowork triggered 16% crash; per-seat pricing erosion applies to legal research | MODERATE |
| 5 | CEO Erik Engstrom net seller | Sold GBP 2.5M in shares, further 22K shares in Feb 2026. No insider BUYS in 3 months. | MODERATE |
| 6 | Revenue growth flat at 7%, not "accelerating" | FY2024: 7%, FY2025: 7%. H2 2025 decelerated vs H1. Bloomberg framed as "sales miss." | LOW |

### Valoracion

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | WACC 7.5% may be too low | Thesis uses adjusted beta 0.7. Tool default 9%. RELX's own implied cost of capital likely 8-9%. | MODERATE-HIGH |
| 2 | DCF terminal value 80.6% of EV | Thesis acknowledges this. DCF is effectively a perpetuity calculation. | MODERATE |
| 3 | 24x P/E assumes re-rating in depressed market | Current market regime: WKL.AS 13x, IT 16x, RELX 21x. Using 21x = FV ~ EUR 27 (no MoS). | MODERATE-HIGH |
| 4 | E[CAGR] 10.6% below 12% Tier A threshold | Thesis correctly identifies this. Rescue argument ("with compounding, 17-20%") risks double-counting. | MODERATE |
| 5 | Bear case FV EUR 22 provides no cushion | At EUR 26.80, price is 21.8% ABOVE bear case. Worst entry profile of any Tier A candidate in system. | HIGH |
| 6 | Analyst price targets may be anchored to old multiples | Deutsche Bank cut to 3050p (from 3700p), UBS to 3600p (from 4570p). Multiple compression ongoing. | LOW |

### Riesgos

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | Elsevier university opt-out cascade risk | 9 universities opted out; "double-digit exits" expected. STM = 33% of revenue. | HIGH |
| 2 | Harvey AI cannibalization of Lexis revenue | Harvey can license Lexis data and bundle at lower prices. $200M+ ARR target by 2027 = potential margin pressure. | MODERATE |
| 3 | Goodwill 54% of total assets + rising net debt | Net debt up 10% to GBP 7.2B (2.0x EBITDA from 1.8x). If goodwill impairment needed, equity wipe-out risk. | MODERATE |
| 4 | Regulatory risk (GDPR, data privacy evolution) | EU GDPR procedural regulation tightening 2027. Data-heavy business model faces increasing scrutiny. | LOW-MODERATE |
| 5 | Insider ownership only 0.1% | CEO Engstrom holds GBP 26.4M (~0.065% of company). Minimal skin in the game for a EUR 48B company. | MODERATE |
| 6 | GBP/EUR FX exposure creates valuation noise | 60% NA revenue, GBP reporting, EUR listing. FV is sensitive to exchange rate assumptions. | LOW |

### Timing

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | SaaSpocalypse selloff may not be over | Multiple compression ongoing across all info services (WKL.AS -66%, IT -70%, RELX -49%). No bottom signal yet. | MODERATE-HIGH |
| 2 | No clear re-rating catalyst in near term | The thesis identifies "market recognizes AI as tailwind" as medium-probability catalyst. This is vague and not time-bound. | MODERATE |
| 3 | Anthropic, OpenAI continue to release legal/academic AI tools | Each new AI tool announcement creates fresh selloff pressure. Multiple events expected in 2026. | MODERATE |
| 4 | UK university deal rejection cycle may intensify | Next wave of negotiations could see 20+ universities exit by mid-2026. Each opt-out is negative headline. | MODERATE |

---

## Conflictos con Otros Analisis

No moat_assessment.md or risk_assessment.md files exist for REN.AS -- only the thesis.md was produced in R1. This is a gap: a full R1 pipeline typically produces separate moat and risk assessments from moat-assessor and risk-identifier agents. The thesis was apparently a single-agent R1 output.

**Key discrepancy with sector view:** The business-services sector view lists REL.L as "Not scored, -48% off 52wH" in the "Companies Priced but NOT Scored" section. The R1 thesis now scores REN.AS at QS 78 adjusted. The sector view should be updated to reflect this R1 completion.

**Consistency with MORN precedent:** The thesis compares the REN.AS entry decision to MORN (bought at 17% MoS with E[CAGR] 15.6%). But RELX's E[CAGR] of 10.6% is materially below MORN's 15.6%. The comparison actually WEAKENS the case for RELX at current price, which the thesis correctly concludes (WATCHLIST, not BUY).

---

## Veredicto Global

| Metric | Valor |
|--------|-------|
| Total desafios | 22 |
| Desafios HIGH/CRITICAL | 3 HIGH, 0 CRITICAL |
| Desafios MODERATE-HIGH | 5 |
| Desafios no resueltos por thesis | 8 (ROIC overstatement, university opt-outs, Harvey cannibalization, WACC calculation, bear FV cushion, insider selling, P/E re-rating assumption, AI dual-edge) |
| Veredicto | **MODERATE COUNTER** |

### Interpretacion:

**MODERATE COUNTER:** The thesis has meaningful gaps that require investigation and adjustment before proceeding. The core business quality is genuine (RELX is a high-quality company), but the thesis overstates several metrics (ROIC, moat breadth, growth trajectory) and understates specific risks (Elsevier disruption, Harvey cannibalization, valuation sensitivity). The WATCHLIST verdict at EUR 26.80 is CORRECT -- the issue is whether the entry price of EUR 23-24 provides sufficient margin of safety given the risks identified.

---

## Recomendacion al Investment Committee

Before approving any standing order for REN.AS, the committee should:

1. **CORRECT the ROIC figure.** Use RELX's reported 15.4% post-tax ROIC, not the tool's 23%. Assess whether 15.4% still qualifies for the same QS and tier treatment. (It likely does -- 15.4% ROIC is still well above WACC -- but the narrative changes from "exceptional compounder" to "good quality business.")

2. **DISAGGREGATE the moat assessment.** Risk and Legal segments have WIDE moats. STM (Elsevier) has a moat under increasing pressure from open access mandates and institutional pushback. The thesis should present segment-level moat durability.

3. **STRESS-TEST the valuation at WACC 8.5% and P/E 20-22x.** This produces FV of approximately EUR 27-29. At EUR 23-24 entry, MoS would be 12-21% -- still acceptable for a Tier A candidate but thinner than the thesis's 30% MoS claim.

4. **MONITOR the Elsevier university opt-out cascade.** If more than 15-20 UK universities opt out by mid-2026, or if major European consortia (Germany, Netherlands) threaten similar action, this becomes a kill condition for the STM segment.

5. **RESOLVE the Harvey partnership question.** Is Harvey a net revenue CREATOR (AI uplift on existing subscriptions) or a net revenue CANNIBALIZER (cheaper bundled access via Harvey)? The answer to this question should be tracked as a leading indicator for Legal segment health.

6. **LOWER the entry price to EUR 21-22** (from thesis's EUR 23-24) to account for: (a) lower FV under stress-tested assumptions, (b) bear case provides no cushion at current levels, (c) ongoing SaaSpocalypse momentum with no clear bottom signal.

7. **TRACK the insider activity.** CEO selling GBP 2.5M+ while insiders make zero purchases in 3 months is a negative signal. If selling continues post-earnings, escalate concern.

---

## Alternative Bear Case Fair Value

Using more conservative assumptions:

| Input | Thesis | DA Alternative |
|-------|--------|----------------|
| WACC | 7.5% | 8.5% |
| Revenue Growth | 7-8% | 5-6% (STM pressure) |
| P/E Multiple | 24x | 20-21x (current regime) |
| Terminal Growth | 2.5% | 2.0% |
| ROIC | 23% | 15.4% (company-reported) |

**DA Alternative FV:**
- Method 1 (Earnings @ 20.5x P/E): 128.5p * 20.5 = GBP 26.34 = EUR 30.10
- Method 2 (DCF @ 8.5% WACC, 6% growth): ~EUR 22-24
- Weighted (60/40): EUR 27.66

**DA Fair Value: EUR 27.50-28.00** (vs thesis EUR 33.50)

At this FV, the current price of EUR 26.80 offers only 2.5-4.3% MoS -- essentially FAIRLY VALUED at current levels.

At the thesis entry of EUR 23.50, MoS would be 15-16% -- acceptable for Tier A but not exceptional.

At my recommended entry of EUR 21.50, MoS would be 22-23% -- adequate for a Tier A with the risk profile described.

---

## META-REFLECTION

### Dudas/Incertidumbres
- The ROIC discrepancy (23% vs 15.4%) is the most important finding but I cannot verify precisely how quality_scorer.py calculates ROIC for RELX. If the tool uses NOPAT / (Total Assets - Cash - Current Liabilities) without goodwill, the 23% is technically correct on a goodwill-stripped basis. However, RELX's acquisitions required REAL capital, so stripping goodwill entirely overstates economic returns. The truth is somewhere between 15.4% and 23% -- likely around 18-19% on a partial-goodwill basis (similar to the ROP partial-goodwill precedent).
- The Elsevier university opt-out situation is EVOLVING. As of my research, 9 universities have opted out, with "double-digit" expected. But this could stabilize if Elsevier offers better terms, or it could accelerate if a cascade effect takes hold. The financial materiality is uncertain: UK university spending on all 5 major publishers is GBP 112M/year -- Elsevier's share is perhaps GBP 40-60M. Even if 20 universities opt out, the revenue impact on a GBP 9.6B revenue company is <1%. The risk is more about NARRATIVE and PRECEDENT than near-term revenue.
- I have not been able to verify the exact FY2025 figures that drove Bloomberg's "sales growth misses estimates" headline. The 7% underlying growth is strong on an absolute basis but may have been below consensus if analysts expected 7.5-8%.

### Limitaciones de Este Analisis
- Could not access RELX's full 20-F annual report to verify balance sheet details, goodwill breakdown by segment, or full ROIC calculation methodology.
- Limited data on institutional flows in/out of RELX in the past 3 months.
- Could not verify the exact number and revenue weight of universities opting out of Elsevier deals.
- The Harvey-LexisNexis pricing impact analysis relies heavily on Artificial Lawyer's analysis, which is a Level 2/3 source (informed industry opinion, not verified data).

### Sugerencias para el Sistema
- **ROIC dual-reporting for all companies with significant goodwill:** The system should always report both (a) the tool's ROIC (which may strip goodwill) and (b) the company's self-reported ROIC. The discrepancy should be noted and explained. This prevents the exact overstatement found here.
- **Moat disaggregation for multi-segment companies:** A single moat score for RELX hides the fact that Risk has a much stronger moat than STM. The moat_assessment template should support segment-level moat scoring.
- **The R1 for REN.AS appears to have been done without separate moat-assessor and risk-identifier agents.** The agent-protocol requires R1 to run these three in parallel. If this was a single-agent R1, the quality checks may be incomplete.

### Preguntas para Orchestrator
1. Was the R1 for REN.AS run through the full parallel pipeline (fundamental-analyst + moat-assessor + risk-identifier + valuation-specialist), or was it a single-agent output? The absence of moat_assessment.md and risk_assessment.md files suggests the latter.
2. Given the ROIC discrepancy (23% tool vs 15.4% company-reported), should quality_scorer.py be investigated for systematic ROIC overstatement across all companies with significant goodwill? This could affect multiple pipeline candidates.
3. The thesis proposes a standing order at EUR 23.50. Given my alternative FV of EUR 27.50-28.00 and recommended entry of EUR 21.50, should the R3 resolution target a compromise entry price?
4. RELX, MORN, and VRSK are all in the pipeline as "information services" companies. If all three are bought, the portfolio would have significant sector concentration in data/analytics. Has this cluster risk been evaluated?

---

## Sources

- [RELX 2025 Results Press Release](https://www.relx.com/media/press-releases/year-2026/relx-2025-results)
- [UK Universities Decline New Elsevier Deal - Inside Higher Ed](https://www.insidehighered.com/news/faculty-issues/books-publishing/2026/02/06/uk-universities-decline-new-elsevier-deal)
- [Three More UK Universities Opt Out of Elsevier - Times Higher Education](https://www.timeshighereducation.com/news/three-more-uk-universities-opt-out-new-elsevier-deal)
- [Number of UK Universities Opting Out Hits Nine - Research Professional News](https://www.researchprofessionalnews.com/rr-news-uk-open-access-2026-2-ninth-uk-university-confirms-opting-out-of-elsevier-deal/)
- [Harvey + LexisNexis Pricing Impact - Artificial Lawyer](https://www.artificiallawyer.com/2025/06/30/harvey-lexisnexis-the-potential-pricing-impact/)
- [LexisNexis Partners with Harvey - legal.io](https://www.legal.io/articles/5691231/LexisNexis-Partners-with-Harvey-in-Strategic-AI-Alliance)
- [LexisNexis Explains Why REV Invested in Rival Harvey - Artificial Lawyer](https://www.artificiallawyer.com/2025/02/13/lexisnexis-explains-why-rev-invested-in-rival-harvey/)
- [Don't Ignore Insider Selling in RELX - Simply Wall St](https://simplywall.st/stocks/gb/commercial-services/lse-rel/relx-shares/news/dont-ignore-the-insider-selling-in-relx)
- [RELX Share Price Slips as Buyback and Insider Filings Hit Tape - ts2.tech](https://ts2.tech/en/relx-share-price-slips-as-buyback-and-insider-filings-hit-the-tape/)
- [RELX Insider Trading Activity - MarketBeat](https://www.marketbeat.com/stocks/LON/REL/insider-trades/)
- [RELX Valuation Bear Case - ainvest.com](https://www.ainvest.com/news/relx-valuation-strategic-positioning-overcorrection-valid-bear-case-2512/)
- [RELX Brokers Cut Targets on De-Rating - Proactive Investors](https://www.proactiveinvestors.co.uk/companies/news/1087342/relx-brokers-back-the-investment-story-despite-ai-fears-targets-cut-on-de-rating-1087342.html)
- [What on Earth's Going on with RELX Shares - Motley Fool UK](https://www.fool.co.uk/2026/02/16/what-on-earths-going-on-with-relx-shares/)
- [Here's Why RELX Crashed 16% - Motley Fool UK](https://www.fool.co.uk/2026/02/03/heres-why-experian-relx-and-lseg-just-crashed-up-to-16-in-the-ftse-100/)
- [RELX ROIC - GuruFocus](https://www.gurufocus.com/term/roic/RELX)
- [LexisNexis Risk Solutions Market Position - MarketsandMarkets](https://www.marketsandmarkets.com/ResearchInsight/us-identity-verification-companies.asp)
- [RELX PLC Stock Outlook 2026 - ts2.tech](https://ts2.tech/en/relx-plc-stock-outlook-2026-ai%E2%80%91powered-growth-buybacks-and-valuation-risks/)
- [Cost of Knowledge Boycott - Wikipedia](https://en.wikipedia.org/wiki/The_Cost_of_Knowledge)
- [Silent Decoupling as Elsevier Talks Near Crunch Point - Times Higher Education](https://www.timeshighereducation.com/news/silent-decoupling-under-way-elsevier-talks-near-crunch-point)
