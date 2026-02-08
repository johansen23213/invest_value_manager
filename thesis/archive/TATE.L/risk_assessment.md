# Risk Assessment: TATE.L (Tate & Lyle PLC)

## Fecha: 2026-02-08

## Risk Score: HIGH

---

## Matriz de Riesgos

| # | Categoria | Riesgo | Probabilidad | Impacto | Score | Mitigante |
|---|-----------|--------|-------------|---------|-------|-----------|
| 1 | Valoracion | QS Tier C (45) misclassified as Tier B in thesis -- FV inflated | Alta | Alto | CRITICAL | Recalculate with correct tier |
| 2 | Financiero | ROIC spread NEGATIVE per tool (-0.5pp) vs thesis claim of +4.6pp | Alta | Alto | CRITICAL | Investigate data sources |
| 3 | Fundamental | Sucralose structural decline + Tyson phase-out + HHS regulatory pressure | Alta | Medio | HIGH | Allulose/stevia pipeline partially offsets |
| 4 | Valoracion | WACC 7.4% built on Beta 0.44 (unrealistically low) + arbitrary +175bp bump | Media | Alto | HIGH | Use higher beta or sector WACC |
| 5 | Financiero | GBP 952M net debt on GBP 1.7B market cap (56% debt/EV), post-acquisition | Media | Alto | HIGH | FCF GBP 190M, deleveraging on track |
| 6 | Fundamental | US tariffs increasing costs on US-China cross-border products | Alta | Medio | HIGH | Manufacturing footprint in both countries |
| 7 | Fundamental | North American demand weakness + double guidance downgrade | Media | Medio | MEDIUM | Potentially cyclical, not structural |
| 8 | Valoracion | Bear FV (400-420 GBp) only 2-7% above current price -- no downside protection | Alta | Medio | HIGH | |
| 9 | Financiero | GAAP P/E 56.2x (price_checker) vs thesis "adjusted" 8.8x -- massive gap | Media | Medio | MEDIUM | Acquisition accounting one-offs |
| 10 | Fundamental | Insider net selling in recent months | Media | Bajo | LOW | Glenn Fish departure is Huber rotation, not negative signal per se |
| 11 | Geopolitico | GBP currency risk -- 50% Americas revenue, UK listing | Media | Bajo | LOW | Natural cost hedge partially |
| 12 | Valoracion | Morgan Stanley UNDERWEIGHT, target 500p; Barclays downgraded to Equal Weight 430p | Media | Medio | MEDIUM | Analyst consensus still 473p |

---

## Top 3 Riesgos Criticos

### 1. Quality Score Misclassification: Tier C (45), NOT Tier B

- **Categoria:** Valoracion / Fundamental
- **Descripcion:** The thesis claims QS 5/10 = Tier B requiring 25% MoS. However, the quality_scorer.py tool calculates QS = 45/100 = Tier C. This is not a minor discrepancy -- it fundamentally changes the required MoS threshold and risk profile.
- **Evidencia:**
  - `quality_scorer.py --detailed` output: TOTAL SCORE 45/100, TIER C
  - Financial Quality: 5/40 points (extremely low)
  - ROIC Spread: 0 pts (-0.5pp -- NEGATIVE spread, meaning ROIC < WACC per tool calculation)
  - FCF Margin: 0 pts (2.5% -- very low)
  - FCF Consistency: 0 pts (2/5 years positive per yfinance data, though this may reflect acquisition distortions)
  - Leverage: 5 pts (2.3x -- elevated)
  - The thesis used a manual 10-point scoring system (5/10 = Tier B) that is incompatible with the standardized 100-point quality_scorer.py
- **Probabilidad:** Alta -- this is not a forecast, it is a measurable fact from the standardized tool
- **Impacto si materializa:** A Tier C company with QS 45 should require significantly more MoS than 25%. Under Tier C guidance from precedents, MoS of 30-40% is more appropriate. At current price 393.6 GBp, the thesis claims 31% MoS to a 550 GBp FV. If the FV is actually lower (see Risk #4 on WACC) and MoS requirement higher, the position may not meet the bar.
- **Mitigante:** The 100-point tool may penalize TATE.L unfairly on FCF consistency due to acquisition-related one-offs. The company's adjusted FCF has been positive for 5+ years. However, ROIC spread of -0.5pp is concerning.
- **Kill condition?:** NO, but a SIGNIFICANT downgrade to thesis conviction. Should be reclassified as Tier C throughout.

### 2. ROIC Spread Negative (-0.5pp) vs Thesis Claim of +4.6pp

- **Categoria:** Financiero / Fundamental
- **Descripcion:** The thesis claims ROIC ~12% vs WACC 7.4% = +4.6pp positive spread. The quality_scorer.py calculates ROIC spread at -0.5pp. A separate source (GuruFocus) shows ROIC 12.74% vs WACC 6.21% = +6.53pp. There is a major discrepancy depending on how ROIC is measured post-acquisition.
- **Evidencia:**
  - quality_scorer.py: ROIC spread -0.5pp (0/5 points)
  - GuruFocus (July 2025): ROIC 12.74%, WACC 6.21%
  - Alpha Spread: ROCE 9.8%, below 3-year median 10.6%
  - The discrepancy likely stems from how the CP Kelco acquisition (GBP 952M goodwill + intangibles) inflates the invested capital base. Post-acquisition, ROIC on total capital (including goodwill) may be significantly lower than pre-acquisition ROIC
  - Amortization of acquired intangibles: GBP 19M in H1 FY26 (GBP 38M annualized), which reduces NOPAT
- **Probabilidad:** Alta that post-acquisition ROIC is materially lower than thesis claims
- **Impacto si materializa:** If ROIC is at or below WACC, the company is NOT creating value. This destroys the fundamental investment case. A "specialty ingredients compounder" that does not earn above its cost of capital is just a leveraged mediocre business.
- **Estimated impact:** If ROIC ~ WACC, the terminal value multiple should be much lower (justified P/B ~ 1.0x). This could reduce FV by 20-30%.
- **Mitigante:** The ROIC may improve as synergies are realized and acquisition costs amortize. Run-rate synergies of $50M by FY27 would add ~GBP 40M to EBITDA, potentially restoring ROIC above WACC.
- **Kill condition?:** YES, if confirmed as structural. Kill condition #7 in thesis says "ROIC falls below WACC for 2 consecutive years = SELL." This needs close monitoring.

### 3. Sucralose Structural Decline + Regulatory Headwind

- **Categoria:** Fundamental / Regulatorio
- **Descripcion:** Sucralose is ~15% of revenue (GBP ~200M based on FY25 $193M sucralose revenue). The WHO advised against non-sugar sweeteners in 2023. Tyson Foods is phasing out sucralose from all branded US products by end 2025. The US HHS under the Trump administration identified sucralose as contributing to chronic disease. A March 2025 Nature Metabolism study showed sucralose increases hypothalamic blood flow and hunger responses. Morgan Stanley downgraded TATE.L specifically citing sucralose risks.
- **Evidencia:**
  - WHO May 2023: advised against non-sugar sweeteners for weight loss
  - Tyson Foods September 2025: phasing out sucralose from ALL branded products (Tyson, Jimmy Dean, Hillshire Farm, etc.)
  - US HHS: identified sucralose as contributing to chronic disease
  - Nature Metabolism March 2025: sucralose increases hunger vs sucrose
  - Morgan Stanley downgrade to UNDERWEIGHT citing "higher risks to medium-term goals, particularly following Tyson's decision to phase out sucralose"
  - US Right to Know petitioned FTC to investigate deceptive Splenda/sucralose advertising by Tate & Lyle and Coca-Cola
- **Probabilidad:** Alta for continued decline; Media for outright regulatory ban
- **Impacto si materializa:**
  - Gradual decline (5-7%/yr as thesis assumes): Loss of ~GBP 10-15M revenue/yr, manageable
  - Accelerated decline (15-20%/yr, multiple major CPG customers phase out): Loss of GBP 30-40M revenue/yr, material. Sucralose EBITDA ~GBP 60M, so loss of ~GBP 12-20M EBITDA
  - Regulatory ban/restriction: Worst case, GBP 200M revenue at risk, ~GBP 60M EBITDA. This would reduce FV by ~25-30%
- **Mitigante:** Tate & Lyle has allulose (DOLCIA PRIMA) and stevia (TASTEVA) growing at 20%+ CAGR. These can partially replace sucralose revenue. But "partially" is the key word -- the substitution takes years.
- **Kill condition?:** The thesis has Kill Condition #4: "Sucralose revenue decline >20% YoY for two consecutive periods = REVIEW." I would suggest this is too lenient. A single >20% decline should trigger review given the regulatory direction.

---

## Riesgos NO Mencionados en Thesis

| Riesgo | Severidad | Mencionado en thesis? | Comentario |
|--------|-----------|----------------------|------------|
| QS is Tier C (45), not Tier B | HIGH | NO -- thesis uses incompatible 10-point scale | Entire MoS framework built on wrong tier |
| ROIC spread potentially negative post-acquisition | HIGH | Minimizado -- thesis claims +4.6pp without post-acquisition adjustment | quality_scorer shows -0.5pp |
| Tariff impact is REAL and SPECIFIC (US-China cross-border) | HIGH | Minimizado -- thesis says "Not directly exposed to Trump tariffs" | Pre-close statement explicitly cites tariff costs |
| GAAP P/E 56.2x vs adjusted 8.8x gap | MEDIUM | NO | Huge gap suggests heavy "adjustments" -- need to understand what is excluded |
| Tyson Foods specific phase-out of sucralose | HIGH | NO -- thesis mentions "sucralose health concerns" generically | Major CPG customer specifically eliminating sucralose |
| HHS identifying sucralose as chronic disease contributor | HIGH | NO | US regulatory posture actively hostile to sucralose |
| FTC petition to investigate deceptive Splenda advertising | MEDIUM | NO | Regulatory/reputational risk |
| Goodwill impairment risk from CP Kelco | MEDIUM | Minimizado -- thesis mentions "elevated" but does not quantify | Post-acquisition goodwill + intangibles are very large vs equity |
| Bear FV only 2-7% above current price | HIGH | Minimizado -- thesis shows 5.5% MoS vs bear but does not flag this as dangerous | Essentially NO downside protection in bear case |
| Morgan Stanley UNDERWEIGHT rating with sucralose-specific concern | MEDIUM | NO | Major investment bank bearish on the stock |
| Capex GBP 120M (FY26) vs thesis GBP ~100M D&A assumption | LOW | NO | May slightly affect FCF projections |
| Intangible amortization GBP 38M/yr reducing GAAP earnings | MEDIUM | NO | Explains the GAAP vs adjusted EPS gap |

---

## Riesgo Agregado

- Numero de riesgos HIGH+CRITICAL: **7** (2 CRITICAL + 5 HIGH)
- Riesgos correlacionados: **SI**
  - Risks #1, #2, #4, #8, #13 are all valuation-related and COMPOUND each other: wrong tier classification + questionable ROIC + aggressive WACC + no bear case protection = FV likely significantly inflated
  - Risks #3, #6 are both demand-side and compound: sucralose decline + tariff costs both reduce revenue and margins simultaneously
- Risk Score Final: **HIGH**

The thesis FV of 550 GBp is likely inflated by 15-20%. My independent risk-adjusted estimate is ~450-460 GBp, giving only 13-15% MoS from current price. For a Tier C company with 2.3x leverage, this is INSUFFICIENT.

---

## Sources

- [Tate & Lyle H1 FY26 Results](https://www.tateandlyle.com/news/tate-lyle-plc-results-six-months-30-september-2025)
- [Tate & Lyle Pre-close Statement](https://www.tateandlyle.com/news/pre-close-statement)
- [Tate & Lyle Integration Update](https://www.tateandlyle.com/news/integration-update-and-pre-close-statement)
- [ESM Magazine: Tate & Lyle Cuts Outlook](https://www.esmmagazine.com/a-brands/tate-lyle-cuts-annual-profit-outlook-as-demand-slows-297093)
- [Morningstar: TATE Shares Tumble](https://global.morningstar.com/en-gb/stocks/tate-lyle-shares-tumble-demand-softness-drives-sharp-downgrade-full-year-guidance)
- [TradingView: Tate & Lyle Tariff Impact](https://www.tradingview.com/news/reuters.com,2025:newsml_L4N3RU0IG:0-uk-s-tate-lyle-flags-weaker-sales-growth-as-tariffs-hit-food-ingredients-maker/)
- [MarketScreener: Tate & Lyle Tariff Revenue](https://www.marketscreener.com/quote/stock/TATE-LYLE-PLC-4000590/news/Tate-Lyle-flags-weaker-2026-revenue-growth-on-US-tariff-uncertainty-50034438/)
- [Proactive Investors: Morgan Stanley Sucralose Downgrade](https://www.proactiveinvestors.com/companies/news/1078894/tate-lyle-gets-sour-taste-from-investment-bank-downgrade-on-sucralose-risks-1078894.html)
- [TipRanks: Barclays Downgrade](https://www.tipranks.com/news/the-fly/tate-lyle-downgraded-to-equal-weight-from-overweight-at-barclays-thefly)
- [Investing.com: BofA Target Cut](https://www.investing.com/news/analyst-ratings/tate--lyle-stock-price-target-lowered-to-gbp630-at-bofa-securities-93CH-4268002)
- [Berenberg Target Cut](https://www.investing.com/news/analyst-ratings/berenberg-lowers-tate--lyle-stock-price-target-on-weak-demand-outlook-93CH-4284742)
- [InsiderScreener: TATE Insider Trading](https://www.insiderscreener.com/en/company/tate-lyle-plc)
- [InsiderTrades: Insider Buying](https://www.insidertrades.com/alerts/lon-tate-insider-buying-and-selling-2025-03-01/)
- [USRTK: Sucralose Health Risks](https://usrtk.org/sweeteners/sucralose-emerging-science-reveals-health-risks/)
- [PMC: Sucralose Metabolic Controversies](https://pmc.ncbi.nlm.nih.gov/articles/PMC10971371/)
- [Tyson Foods: Ingredient Phase-out](https://www.tysonfoods.com/news/news-releases/2025/9/tyson-foods-plans-to-stop-using-high-fructose-corn-syrup)
- [Tate & Lyle Debt Offering](https://www.foodmanufacture.co.uk/Article/2025/01/27/tate-lyle-to-raise-588m-through-debt-offering/)
- [GuruFocus: TATE WACC](https://www.gurufocus.com/term/wacc/TATYF)
- [Alpha Spread: TATE ROCE](https://www.alphaspread.com/security/f/tly/profitability/ratio/return-on-capital-employed)
- [FoodNavigator: Allulose Growth](https://www.foodnavigator-usa.com/Article/2022/04/13/Tate-Lyle-expands-allulose-production-amid-exponential-growth-for-sweetener-with-temporal-profile-almost-identical-to-sucrose/)
- [Tate & Lyle: Board Changes](https://www.tateandlyle.com/news/board-changes-4)
