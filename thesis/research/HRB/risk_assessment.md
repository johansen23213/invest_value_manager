# Risk Assessment: HRB (H&R Block)

## Fecha: 2026-02-09

## Risk Score: HIGH

---

## Matriz de Riesgos

| # | Categoria | Riesgo | Probabilidad | Impacto | Score | Mitigante |
|---|-----------|--------|-------------|---------|-------|-----------|
| 1 | Financiero | Capital destruction via buybacks at peak prices | Alta | Alto | CRITICAL | Share count decline offsets some EPS damage |
| 2 | Fundamental | FCF structural decline despite revenue growth | Media | Alto | HIGH | Low capex model provides floor |
| 3 | Tecnologico | AI disruption of simple tax prep (3-5yr horizon) | Media | Alto | HIGH | HRB investing in AI defensively |
| 4 | Financiero | Negative stockholders equity / leveraged balance sheet | Media | Medio | MEDIUM | Interest coverage 10x, predictable cash flow |
| 5 | Legal/Regulatorio | FTC consent order + privacy class action | Media | Medio | MEDIUM | FTC $7M fine is immaterial; privacy case structure limits exposure |
| 6 | Fundamental | DIY market share loss to TurboTax | Media | Medio | MEDIUM | Assisted segment more defensible |
| 7 | Gestion | New CEO (Curtis Campbell) - unproven as CEO | Media | Medio | MEDIUM | Strong industry background (Intuit, TaxAct, Capital One) |
| 8 | Fundamental | Financial products segment declining (-11% YoY) | Alta | Bajo | LOW | Only ~10% of revenue |
| 9 | Valoracion | Value trap risk - cheap for structural reasons | Media | Medio | MEDIUM | Not pure value trap per checklist |
| 10 | Fundamental | Franchise volume decline (-7.2% YoY) | Baja | Medio | LOW | Attributed to opportunistic buybacks, not organic decline |
| 11 | Regulatorio | IRS Direct File revival under future administration | Baja | Alto | MEDIUM | Discontinued for 2026; political winds currently favorable |
| 12 | Macro | US recession impact on discretionary tax spending | Baja | Medio | LOW | Tax filing is mandatory; recession may increase refund-seeking |
| 13 | Gestion | Insider selling - 5 sales, 0 purchases in 6 months | Media | Bajo | LOW | 10b5-1 plans, not panic selling |

---

## Top 3 Riesgos Criticos

### 1. Capital Destruction via Buybacks at Peak Prices (CRITICAL)

- **Categoria:** Financial / Capital Allocation
- **Descripcion:** H&R Block's management has systematically destroyed shareholder value through poorly-timed buybacks. The evidence is damning:
  - FY2025: Repurchased 6.5M shares at average $61.10/share, spending $400.1M
  - Q1 FY2026: Repurchased 7.9M shares at average $50.90/share, spending $400M
  - **Total: $800M spent at avg ~$55/share. Stock is now $32.88.** That is a 40% unrealized loss on $800M of buybacks.
  - This $800M in buybacks represents ~1.3 years of FCF, effectively vaporized.
  - Since 2016, the company has returned $5B to shareholders through buybacks and dividends, buying back 47% of shares outstanding -- but much of this was done at prices far above current levels.
  - The company has funded these buybacks partly with debt, driving stockholders' equity from positive $88.9M (June 2025) to negative $(823.1)M (December 2025) -- a swing of $912M in 6 months.

- **Evidencia:** FY2025 10-K, Q1 FY2026 earnings release, Q2 FY2026 balance sheet
- **Probabilidad:** Alta (this has ALREADY happened; the question is whether it continues)
- **Impacto si materializa:** The damage is done on past buybacks. Going forward, ~$700M remaining on the $1.5B authorization. If management continues buying at current prices ($33) and the stock goes to $20, that is another round of capital destruction. But if the stock recovers, current-price buybacks would be accretive. The uncertainty is HIGH.
- **Quantified impact:** $800M at $55 avg vs $33 current = ~$320M of value destroyed. That is approximately $2.50/share of capital permanently lost.
- **Thesis assessment:** The thesis mentions management "bought back $400M at $61, now at $39" as a partial value trap factor. But it UNDERSTATES the magnitude: it was actually $800M total at average ~$55, and the stock is now $33, not $39. The thesis scored management quality as "0.5" (MIXED) -- I would score it lower.
- **Mitigante:** Share count has declined from ~188M (2016) to ~126M (current), a 33% reduction. If the business stabilizes and stock recovers, the compounding effect of fewer shares is powerful. But this requires FCF to stop declining.
- **Kill condition?** YES -- if management continues aggressive buybacks while FCF declines and stock drops further, this becomes a spiral. Suggested kill condition: "Management spends >$200M on buybacks while FCF is declining AND stock is below $40."

### 2. FCF Structural Decline Despite Revenue Growth (HIGH)

- **Categoria:** Fundamental / Financial
- **Descripcion:** FCF has declined 20% over 3 fiscal years while revenue grew:
  - FY2023: FCF ~$752M (estimated from thesis)
  - FY2024: FCF $657M (OCF $721M - Capex $64M)
  - FY2025: FCF $599M (OCF $681M - Capex $82M)
  - **Decline: $752M to $599M = -20.3% over 3 years**
  - Revenue grew from ~$3.6B to $3.8B (+5.6%) over the same period.
  - This means FCF margin compressed from ~21% to ~16%.
  - The thesis assumes FCF "stabilizes at $500-550M" in the base case. But the TREND is still downward. Nothing in the Q2 FY2026 results suggests reversal.

- **Evidencia:** FY2023-FY2025 cash flow statements; FY2026 guidance of EBITDA $1.015-1.035B (roughly flat vs FY2025 EBITDA ~$1.0B)
- **Probabilidad:** Media-Alta -- the decline has been consistent for 3 years. The question is whether it stabilizes or continues.
- **Impacto si materializa (continued decline to $400M):**
  - At P/FCF of 7x on $400M FCF = $2.8B market cap = ~$22/share (vs $32.88 now = -33% downside)
  - This is significantly worse than the thesis "Bear case" of $46.53
  - The thesis bear case assumes FCF declines to $400M but applies a 9.5x multiple -- I think that multiple would compress further if FCF is actively declining.

- **Root cause analysis:** The thesis attributes the decline to "one-time investments (tech, marketing)" and says "company can cut if needed." But:
  - Capex rose from $64M to $82M (+28%)
  - SG&A has been rising to fund digital transformation
  - These investments may be NECESSARY to compete, not discretionary
  - If they cut, they may accelerate competitive decline

- **Mitigante:** The business has natural FCF floor due to low capex requirements and high margin on assisted returns. Even in a severe scenario, FCF below $350M seems unlikely.
- **Kill condition?** Already in thesis: "FCF drops below $400M." I would tighten to $450M given the trend.

### 3. AI Disruption of Tax Preparation (HIGH, 3-5yr horizon)

- **Categoria:** Technology / Disruption
- **Descripcion:** The thesis dismisses AI disruption for complex returns but underestimates the medium-term risk:
  - **Current state (2026):** AI chatbots (TurboTax, HRB's own) are wrong ~50% of the time on tax questions. NOT yet a threat.
  - **Near-term (2027-2028):** AI accuracy will improve. Intuit's proprietary LLM trained by tax professionals is already more accurate than generic models. Intuit has $2.5B+ R&D budget vs HRB's limited tech spend.
  - **Medium-term (2029-2030):** For the 60% of HRB customers with "simple-to-moderate" returns (W-2 + standard deductions + a few itemized), AI-assisted DIY could become good enough. This is NOT just about the IRS Direct File -- it is about TurboTax AI making professional assistance feel unnecessary.
  - **Intuit's competitive advantage:** $123.5B market cap vs HRB's $4.2B. Intuit can outspend HRB on AI by 10-20x. TurboTax maintains 60% DIY market share. HRB is already losing DIY share.

- **Evidencia:** Scale Venture Partners analysis ("Building TurboTax in a weekend"); 88% of tax professionals believe AI will be central within 5 years; Intuit's "Intuit Assist" AI platform; Washington Post findings that AI chatbots give wrong tax advice ~50% of the time
- **Probabilidad:** Media (for material impact within 3 years), increasing to Alta over 5+ years
- **Impacto si materializa:**
  - ~20% of HRB revenue is DIY -- this is most vulnerable. Loss of 30-50% of DIY = -6-10% revenue impact
  - ~70% of revenue is Assisted -- but the "simple" portion (~40% of assisted, or ~28% of total revenue) is vulnerable over 5 years. Loss of 30% of simple-assisted = -8.4% revenue impact
  - Total at-risk revenue: 14-18% over 5 years
- **What thesis says:** "AI disruption is gradual (3-5+ years), not sudden." I agree it is gradual but disagree that it is not material. A 15% revenue decline over 5 years with rising costs to compete would crush FCF.
- **Mitigante:** HRB partnered with OpenAI defensively. Complex filers (business, multi-state, audit support) are genuinely hard to automate. HRB's physical office network is a moat for elderly/tech-averse customers.
- **Kill condition?** Not currently in thesis. Suggested: "TurboTax AI achieves >90% accuracy on moderate-complexity returns AND HRB DIY market share drops below 10%."

---

## Additional Risks Detail

### 4. Negative Stockholders' Equity / Leveraged Balance Sheet (MEDIUM)

- **Current state:** Stockholders' equity swung from +$88.9M (June 2025) to -$823.1M (December 2025). This is primarily due to $412.6M in share repurchases in H1 FY2026 plus the seasonal operating loss.
- **Total debt:** $2.44B long-term debt (as of Q2 FY2026)
- **Cash:** $349.2M (down from $983.3M at fiscal year-end -- seasonal pattern)
- **Net debt:** ~$2.1B
- **Net Debt/EBITDA:** ~2.0x (using guided EBITDA $1.025B)
- **Interest coverage:** 10x (EBIT $781M / Interest $78M)
- **Risk:** While interest coverage is strong now, negative equity creates covenant risk. The company has extended its CLOC maturity to 2030, which is positive. But if FCF continues declining AND the company keeps doing debt-funded buybacks, leverage could rise to uncomfortable levels (3x+ Net Debt/EBITDA).
- **Thesis assessment:** Thesis says "debt is manageable at 2x EBITDA." TRUE today, but the thesis does not discuss the TRAJECTORY -- debt rising while FCF declines.
- **Mitigante:** Seasonal cash flow pattern. Tax season generates majority of annual cash. Credit facility extended to 2030.

### 5. FTC Consent Order + Privacy Litigation (MEDIUM)

- **FTC consent order (Jan 2025):** $7M fine + operational requirements:
  - Must allow automated downgrades (no forced call to customer service)
  - Must stop deleting customer data when downgrading
  - Must disclose actual eligibility rates for "free" products
  - This limits HRB's ability to use friction-based revenue tactics
- **Privacy class action (RICO):** HRB, Meta, Google accused of sharing tax data via Facebook Pixel without consent. TaxAct settled similar case for $14.95M. However, HRB's Terms of Service forbid class actions -- exposure is through individual arbitration (up to $10,000 per person). If 100,000 people pursue arbitration, that is $1B potential exposure. But in practice, arbitration uptake is typically <1% of affected users.
- **Quantified impact:** FTC fine is immaterial ($7M on $3.8B revenue). Privacy litigation could cost $50-200M in a reasonable scenario. More importantly, the reputational damage of being caught sharing tax data with Facebook could drive customer attrition.
- **Thesis assessment:** NOT mentioned in thesis at all. This is a material omission.

### 6. New CEO Risk (MEDIUM)

- **Curtis Campbell** took over as CEO on January 1, 2026.
- Background: Previously President of Global Consumer Tax and CPO at HRB. Prior roles at TaxAct, Capital One, and Intuit.
- **Base salary:** $995K. Total comp structure unclear.
- **Risk:** New CEOs often make strategic pivots. Campbell's Intuit background could mean either (a) digital-first transformation that is positive, or (b) expensive investments that further pressure FCF.
- **The thesis mentions "CEO leaving" as a reason the stock is cheap but does not analyze Campbell specifically.** This is a gap.
- **Mitigante:** Campbell has deep tax industry experience and was internally groomed for the role. This is not an outside disruptive hire.

### 7. Value Trap Assessment (MEDIUM)

The thesis's own value trap checklist shows 2-3 PARTIAL factors:
- Industry in secular decline: PARTIAL
- Technology disruption imminent: PARTIAL
- Management destroying value: PARTIAL (I would upgrade this to YES based on buyback evidence)

Three partial-to-yes factors out of 10 is borderline. The thesis concludes "PROCEED WITH CAUTION but not reject." I agree with caution but note that the combination of declining FCF + debt-funded buybacks at peak + secular headwinds is the classic value trap pattern.

The stock has declined from $64.62 (52-week high) to $32.88 -- a 49% decline. When a stock halves, it is worth asking: does the market know something the thesis does not?

---

## Riesgos NO Mencionados en Thesis

| Riesgo | Severidad | Mencionado en thesis? | Comentario |
|--------|-----------|----------------------|------------|
| FTC consent order + deceptive practices | MEDIUM | NO | $7M fine + operational restrictions on upselling tactics |
| Privacy class action (RICO, Meta/Google data sharing) | MEDIUM | NO | Potential $50-200M exposure + reputational damage |
| Negative stockholders' equity trajectory | MEDIUM | Minimizado | Thesis mentions debt but not the -$823M equity or the trajectory |
| Insider selling (5 sales, 0 purchases, 6 months) | LOW | NO | Not alarming individually but pattern is negative |
| Franchise volume decline (-7.2%) | LOW | NO | Attributed to buybacks but still worth monitoring |
| Wave acquisition integration risk | LOW | NO | Wave revenue growing but contribution still small |
| $800M in buybacks at $55 avg (not $400M at $61) | HIGH | Minimizado | Thesis understates magnitude -- says "$400M at $61" when actual recent buybacks total $800M at ~$55 avg |
| Intuit's 30x R&D spending advantage in AI | HIGH | Parcialmente | Thesis mentions AI defensively but not the competitive spending gap |
| Financial products segment declining 11% | LOW | NO | Small segment but shows erosion at the edges |
| Adjusted EPS miss in Q2 FY2026 despite revenue beat | MEDIUM | NO | Revenue up 11% but EPS worse than expected -- cost pressure signal |

---

## Kill Condition Assessment

The thesis defines 5 kill conditions. Current status:

| # | Kill Condition | Status | Assessment |
|---|---------------|--------|------------|
| 1 | FCF drops below $400M | NOT TRIGGERED | FY2025 FCF $599M. But trend: $752M -> $657M -> $599M. At current decline rate (~$75M/yr), could hit $400M by FY2028. 2 years away. |
| 2 | Dividend cut | NOT TRIGGERED | Dividend increased 17% in FY2024. 211 consecutive quarterly dividends. Current yield 5.1%. Annual cost ~$210M vs $599M FCF = payout ratio ~35%. Safe for now. |
| 3 | ROIC < WACC for 2+ years | NOT TRIGGERED | ROIC ~16.3% vs WACC 8.5% = spread +7.8pp. Comfortable. |
| 4 | New CEO shifts away from core tax prep | NOT TRIGGERED | Campbell is a tax industry veteran. No indication of strategic pivot. |
| 5 | IRS Direct File expands to complex returns | RISK REDUCED | IRS Direct File has been DISCONTINUED for 2026 filing season. Low adoption (0.5% of returns) and high per-return costs. This kill condition is less likely under current political environment. |

**Assessment:** No kill conditions are currently triggered. Kill condition #1 (FCF < $400M) is the closest to triggering given the 3-year decline trend, but is still ~2 years away at current trajectory.

---

## Suggested Additional Kill Conditions

Based on my findings, I recommend adding:

1. **Management continues debt-funded buybacks while FCF is declining AND stock is below prior buyback prices.** This is the classic "management looting the balance sheet" pattern.
2. **Net Debt/EBITDA exceeds 3.0x.** Currently 2.0x but rising. At 3x+, refinancing risk becomes material given the company's secular headwinds.
3. **Privacy litigation settlement/verdict exceeds $200M.** Would consume ~1/3 of annual FCF.
4. **Assisted tax return volumes decline >5% YoY for 2 consecutive years.** This would signal structural decline of the core business, not just pricing power masking volume weakness.

---

## Riesgo Agregado

- **Numero de riesgos HIGH+CRITICAL:** 3 (Capital destruction, FCF decline, AI disruption)
- **Riesgos correlacionados?** YES:
  - FCF decline + debt-funded buybacks are directly correlated -- declining FCF means more debt needed for buybacks, which increases leverage, which increases risk.
  - AI disruption + FCF decline are correlated -- if AI erodes volumes, FCF will decline faster.
  - FTC/privacy issues + customer acquisition costs are correlated -- regulatory restrictions on upselling tactics could increase CAC and reduce conversion.
- **Risk Score Final: HIGH**

**Rationale for HIGH (not VERY HIGH):** Despite 1 CRITICAL and 2 HIGH risks, several mitigating factors prevent a VERY HIGH rating:
1. The business is genuinely necessary (tax filing is mandatory)
2. Interest coverage is strong at 10x
3. IRS Direct File has been discontinued (tail risk removed)
4. New CEO has strong industry credentials
5. The stock has already declined 49% from highs, potentially pricing in many of these risks
6. FCF, while declining, remains solidly positive at ~$600M

**However,** the thesis fair value of $59.58 appears aggressive given these risks. The DCF assumptions (3% growth, 8.5% WACC) may be too optimistic for a business with declining FCF and secular headwinds. A risk-adjusted fair value closer to $40-45 seems more defensible, which would reduce the MoS from the claimed 54% to approximately 15-25%.

---

## Comparison: Thesis FV vs Risk-Adjusted FV

| Scenario | Thesis FV | Risk-Adjusted FV | Delta | Rationale |
|----------|-----------|-------------------|-------|-----------|
| Bear | $46.53 | $35-38 | -20-25% | FCF decline to $400M with 7-8x multiple (not 9.5x) |
| Base | $59.58 | $42-47 | -20-30% | FCF stabilizes at $500M with 8-9x multiple (not 9.5x) |
| Bull | $75.96 | $55-62 | -18-27% | FCF recovers to $600M with 10x multiple (not 11x) |

**Key adjustment rationale:**
1. FCF base case should be $500M (not $550M implied by thesis growth rates)
2. EV/EBIT multiple should be lower given FTC regulatory overhang + privacy risk + AI disruption narrative
3. WACC of 8.5% may be too low -- the 2% "risk premium" added to the base 6.5% should be 3% given the evidence of FCF decline, resulting in 9.5% WACC
4. Terminal growth of 2.0% may be too high for a business losing DIY share and facing AI disruption -- 1.0-1.5% seems more appropriate

---

## META-REFLECTION

### Dudas/Incertidumbres
- I lack detailed data on HRB's debt maturity schedule beyond the CLOC (extended to 2030). The $349.9M "current portion of long-term debt" as of FY2025 suggests near-term maturities that could require refinancing at higher rates. I could not confirm specific bond maturities.
- The privacy class action exposure is genuinely hard to quantify. The Terms of Service forbidding class actions should limit exposure, but the RICO theory could potentially pierce that limitation. I am uncertain about the legal outcome.
- Whether FCF decline is structural or cyclical is the central uncertainty. Three years of decline is concerning, but the company's investment phase (tech, AI, Wave integration) could genuinely be causing temporary margin pressure. I do not have enough conviction to call it definitively structural.

### Riesgos que Podrian Estar Subestimados
- **Capital allocation risk is the most underestimated risk.** The thesis treats buybacks as accretive (and they are on a per-share basis), but $800M spent at $55 when the stock is $33 is objectively terrible capital allocation. This calls into question management's judgment. If they misjudged the stock's value by 40%, what else are they misjudging?
- **Intuit's AI spending advantage** could be more decisive than I estimated. If Intuit achieves AI-powered accuracy that makes moderate-complexity returns automatable, HRB loses its core competitive advantage (human expertise for complex situations) faster than my 5-year timeline.

### Discrepancias con Thesis
1. **Buyback magnitude:** Thesis says "$400M at $61" -- actual recent total is $800M at ~$55 average. The thesis understates the capital destruction by 50%.
2. **Quality Score:** Tool gives QS 70 (Tier B), thesis gives 5/10 manually. These are different scales. The tool's 70 seems generous given declining FCF and negative equity.
3. **Bear case too optimistic:** Thesis bear case is $46.53 (+20% MoS from $38.72 at time of writing). Current price $32.88 is BELOW the thesis's implied worst case. The market disagrees with even the bear case.
4. **FTC/privacy litigation completely absent** from thesis risk analysis.
5. **IRS Direct File:** Thesis treats this as a risk. In fact, it has been DISCONTINUED for 2026 -- this is a positive development not reflected in the thesis.

### Sugerencias para el Sistema
1. For any company with aggressive buyback programs, the risk assessment should include a "Buyback Efficiency Audit" -- comparing average purchase price vs current price vs fair value estimates.
2. FTC/regulatory searches should be MANDATORY for all US consumer-facing companies in the buy pipeline.
3. The thesis valuation section should include a "Market Implied Expectations" analysis -- what growth/margins does the CURRENT stock price imply? If the market is pricing in worse outcomes than our bear case, we should investigate why.

### Preguntas para Orchestrator
1. Given that the current price ($32.88) is BELOW the thesis bear case ($46.53), should the thesis bear case be revised downward? The market is pricing in a scenario worse than our worst case.
2. The thesis was written at $38.72 and the stock has fallen 15% since. Should we update the thesis fair value with current data before the committee reviews?
3. Should the buyback capital destruction ($800M at $55 avg, now $33) change our conviction level from HOLD to something lower? The management quality assessment may need revision.
4. With IRS Direct File discontinued, should we remove kill condition #5 and replace it with one of the new kill conditions I suggested?

---

**Sources:**
- [H&R Block FY2025 Results](https://investors.hrblock.com/news-releases/news-release-details/hr-block-reports-fiscal-2025-results-and-provides-fiscal-2026)
- [H&R Block Q1 FY2026 Results](https://investors.hrblock.com/news-releases/news-release-details/hr-block-reports-fiscal-2026-first-quarter-results-and-reaffirms)
- [H&R Block Q2 FY2026 Results](https://investors.hrblock.com/news-releases/news-release-details/hr-block-reports-fiscal-2026-second-quarter-results)
- [FTC Finalizes Order vs H&R Block](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-order-hr-block-requiring-them-pay-7-million-overhaul-advertising-customer-service)
- [IRS Direct File Discontinued for 2026](https://federalnewsnetwork.com/it-modernization/2025/11/irs-direct-file-will-not-be-available-in-2026-agency-tells-states/)
- [H&R Block Privacy Class Action](https://www.classaction.org/hr-block-privacy-facebook)
- [H&R Block CEO Succession](https://investors.hrblock.com/news-releases/news-release-details/hr-block-inc-announces-leadership-succession-plan)
- [H&R Block Insider Activity (Nasdaq)](https://www.nasdaq.com/market-activity/stocks/hrb/insider-activity)
- [Tax Policy Center: Will AI Prepare Tax Returns?](https://taxpolicycenter.org/taxvox/will-artificial-intelligence-be-able-prepare-our-tax-returns)
- [Intuit TurboTax AI (MIT Sloan)](https://sloanreview.mit.edu/article/turbotax-meets-turbo-innovation-ai-at-intuit/)
- [H&R Block $1.5B Buyback Analysis (Kavout)](https://www.kavout.com/market-lens/hr-blocks-1-5-billion-buyback-what-it-means-for-shareholders-and-market-sentiment)
- [H&R Block Negative Equity Analysis (Accountable Finance)](https://accountable.finance/stock/HRB)
