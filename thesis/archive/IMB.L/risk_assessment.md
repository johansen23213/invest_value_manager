# Risk Assessment: IMB.L (Imperial Brands PLC)

## Fecha: 2026-02-08

## Risk Score: HIGH

---

## CRITICAL FINDING: Quality Score Discrepancy

The thesis claims Quality Score 9.5/10 (Tier A). The quality_scorer.py tool calculates QS = 54 (Tier C). This is the LARGEST discrepancy in the portfolio: a 2-tier gap.

### Why the Tool Gives QS 54 (Tier C)

**Financial Quality: 15/40 pts (WEAK)**
- ROIC Spread: 4 pts (2.1pp above WACC) -- The thesis claims ROIC 25-30%, but the tool measures ROIC at ~20.7% (FY25). The spread over WACC of ~7.5% is approximately 13pp, not 2.1pp. The discrepancy likely arises from how the tool calculates ROIC (using total invested capital including goodwill and intangibles from acquisitions) vs the thesis using a narrower capital base. With GBP ~15B of goodwill/intangibles from historical acquisitions (Altadis, etc.), the capital base is inflated, dragging down ROIC as measured by the tool. This is actually informative: it means Imperial's returns on ALL capital ever deployed (including overpaid acquisitions) are mediocre.
- FCF Margin: 2 pts (9.8%) -- FCF of GBP 2.75B on revenue of GBP 32.2B = 8.5%. This is low because tobacco companies have enormous excise taxes flowing through revenue. On net revenue (~GBP 8.5B), FCF margin is ~32%. The tool uses gross revenue which penalizes tobacco's unusual revenue structure.
- Leverage: 5 pts (2.2x) -- Reasonable but not exceptional.
- FCF Consistency: 4 pts (4/5) -- One year of inconsistency.

**Growth Quality: 15/25 pts (MODERATE)**
- Revenue CAGR and EPS CAGR show N/A, likely due to reported revenue declining (-0.7% FY25). At constant currency, growth was +4.1%, but the tool uses reported figures.
- Gross Margin trend is expanding (positive).

**Moat Evidence: 14/25 pts (MODERATE)**
- GM Premium: -1.1pp vs sector -- The tool compares vs Consumer Defensive sector where peers like Unilever, P&G have similar or higher margins.
- ROIC Persistence and Market Position: moderate scores.

**Capital Allocation: 10/10 pts (EXCELLENT)**
- 10yr shareholder returns + 6.1% insider ownership.

### Which Score Is More Accurate?

**NEITHER is fully accurate, but the truth is closer to Tier B (55-74) than Tier A (75+).**

The thesis's manual 9.5/10 scoring has problems:
1. It gives full marks for ROE >15% (1/1) but ignores that ROE is inflated by massive debt and negative equity in some periods. ROE is not the same as ROIC.
2. It gives full marks for "Wide moat" (1/1) but the moat is based on addiction in a declining category -- this is a DEPLETING moat, not an expanding one.
3. It uses a simplistic 10-point checklist while the quality_scorer uses a 100-point framework with more granularity.

The tool's QS 54 is also imperfect:
1. Tobacco's revenue structure (excise taxes in gross revenue) artificially deflates FCF margin.
2. ROIC calculation includes goodwill from decades-old acquisitions, which is sunk cost.

**My assessment: QS ~60-65 (Tier B, Quality Value), NOT Tier A.**

This means the thesis's MoS requirement should be higher (~20-25% typical for Tier B) rather than the 15% it applies for Tier A. The current MoS of ~11% (price 3,341p vs blended FV 3,701p) is INSUFFICIENT for a Tier B company.

---

## Matriz de Riesgos

| # | Categoria | Riesgo | Probabilidad | Impacto | Score | Mitigante |
|---|-----------|--------|-------------|---------|-------|-----------|
| 1 | Regulatorio | UK Generational Smoking Ban | Alta | Alto | CRITICAL | Limited -- law already passing |
| 2 | Fundamental | Secular volume decline acceleration | Media | Alto | HIGH | Pricing power (but limits exist) |
| 3 | Valoracion | QS Discrepancy / Overvalued FV | Alta | Medio | HIGH | Recalculate with conservative FV |
| 4 | ESG | Institutional divestment pressure | Alta | Medio | HIGH | Already partly priced |
| 5 | Fundamental | NGP competitive irrelevance | Media | Alto | HIGH | Low capex, optionality |
| 6 | Regulatorio | Australia menthol ban + global regulation wave | Media | Medio | MEDIUM | Geographic diversification |
| 7 | Legal | US nicotine pouch lawsuits (Zone/TJP) | Media | Bajo | LOW | Small relative to company size |
| 8 | Financiero | Debt refinancing in higher-rate environment | Baja | Medio | LOW | Active management, BBB rating |
| 9 | Geopolitico | Currency headwinds (GBP strength vs revenue currencies) | Media | Medio | MEDIUM | Natural hedge, diversified |
| 10 | Valoracion | DDM sensitivity to growth assumptions | Alta | Alto | CRITICAL | Cross-check with other methods |

---

## Top 3 Riesgos Criticos

### 1. UK Generational Smoking Ban -- Structural Demand Destruction

- **Categoria:** Regulatorio
- **Descripcion:** The UK Tobacco & Vapes Bill has passed the House of Commons (415-47 vote, November 2025) and is progressing through the House of Lords. It will prohibit tobacco sales to anyone born on or after January 1, 2009, meaning the legal smoking age rises by one year every year indefinitely. This effectively legislates the extinction of tobacco sales in the UK over 30-50 years. The bill also includes licensing requirements, advertising restrictions, and vape regulation.
- **Evidencia:** Parliamentary votes show overwhelming support. Both Labour government and Conservative opposition back it. The bill passed second reading by 368 votes. Similar laws inspired by New Zealand's model (which was repealed, but UK is proceeding). Australia has simultaneously implemented menthol bans, health warnings on individual sticks, and standardized packaging from 2025.
- **Probabilidad:** Alta -- The bill is near-certain to become law in 2026.
- **Impacto si materializa:**
  - UK represents ~8-10% of Imperial's tobacco revenue (it's a "priority market")
  - Short-term: minimal impact (ban affects those born after 2009, who aren't yet 18)
  - Medium-term (5-10 years): accelerated volume decline in UK as addressable market shrinks
  - Long-term (15-30 years): UK tobacco revenue goes to zero
  - Contagion risk: other countries copy the UK model. If EU follows, this becomes catastrophic.
  - Estimated impact: 5-15% reduction in terminal value, depending on contagion.
- **Mitigante:** Impact is very slow (decades). Short-term, no revenue impact. But it establishes a REGULATORY PRECEDENT that other countries could follow. The thesis does NOT adequately address this contagion risk.
- **Kill condition?:** NO for now (impact is 15+ years out), but should be monitored as potential kill condition if EU or other major markets adopt similar legislation.

### 2. DDM Valuation Fragility -- 4.5% Perpetual Growth in a Declining Industry

- **Categoria:** Valoracion
- **Descripcion:** The thesis uses a DDM (Gordon Growth Model) as primary valuation (60% weight) with dividend growth of 4.5% in PERPETUITY and a required return of only 9%. This produces FV of 3,723p. The problem: 4.5% perpetual dividend growth assumes pricing power FOREVER offsetting volume decline FOREVER. In a generational ban environment, this assumption breaks down within 20-30 years. A DDM is a perpetuity model -- small changes in g or r cause massive FV swings.
- **Evidencia:**
  - DDM sensitivity: g=3% (instead of 4.5%) gives FV=2,752p (-26% from base). This is BELOW current price of 3,341p.
  - DDM sensitivity: r=10% (instead of 9%) with g=4.5% gives FV=3,046p, also below current price.
  - The thesis acknowledges "MoS vs Bear DDM (worst case): -11% (would be underwater in bear case)" but still proceeds.
  - WACC of 7.5% used in DCF is arguably too low. The thesis's own theoretical WACC of 4.7% is absurd (based on beta of 0.139). The 7.5% "conservative buffer" may still be too low -- tobacco sector WACC is typically 8-10% given regulatory risk premium.
  - Using beta 0.139 in ANY calculation is unreliable. Tobacco betas are typically 0.5-0.8.
- **Probabilidad:** Alta -- The model is structurally fragile by construction.
- **Impacto si materializa:**
  - If true FV is closer to bear DDM (2,752p), the stock is OVERVALUED by 21% from current price of 3,341p.
  - If I use g=3.5%, r=9.5%: FV = 160.32 * 1.035 / (0.095 - 0.035) = 165.9 / 0.06 = 2,766p. Still overvalued.
  - A conservative blended FV using more realistic parameters: ~2,900-3,100p, giving MoS of -8% to +7%. This is NOT adequate for a Tier B company.
- **Mitigante:** High FCF yield (10.3%) provides return even if capital appreciation is limited. The stock can deliver 10%+ returns through dividends + buybacks alone, even without price appreciation.
- **Kill condition?:** NO, but the FV should be revised downward. Current FV of 3,701p is inflated by approximately 15-25%.

### 3. ESG-Driven Institutional Divestment -- Structural Demand Compression for the Stock

- **Categoria:** ESG
- **Descripcion:** ESG exclusion lists continue to grow. Major pension funds (Norway GPFG, UK NEST, CalPERS, AP Pension, Scottish Widows) have divested from tobacco. This is not a one-time event but an accelerating structural trend. As ESG mandates become standard across institutional asset management, the pool of potential buyers for tobacco stocks shrinks permanently.
- **Evidencia:**
  - Norway's GPFG excluded all 17 tobacco producers
  - UK's NEST (largest auto-enrolment provider) exiting GBP 40M of tobacco investments
  - CalPERS (California state pension, $500B+) extended tobacco divestment
  - AP Pension (Denmark) cut tobacco from EUR 15B portfolio
  - Imperial's P/E of 13.4x (current) vs consumer staples peers at 20-25x reflects this ESG discount
  - The ESG exclusion trend is ACCELERATING, not stabilizing
- **Probabilidad:** Alta -- This is already happening and accelerating.
- **Impacto si materializa:**
  - Permanent P/E compression: the stock may NEVER re-rate to sector average P/E
  - Reduced liquidity as institutional holders exit
  - Higher cost of equity (fewer willing buyers demand higher returns)
  - The thesis's DDM implicitly assumes the market will eventually give tobacco a fair P/E. ESG exclusion ensures it won't.
  - Estimated impact: 15-25% permanent valuation discount vs non-ESG-excluded peers
- **Mitigante:** The discount is partly priced in already. Buybacks reduce share count, supporting EPS growth. Retail and hedge fund investors can still hold. But the shrinking buyer pool is a STRUCTURAL headwind to any re-rating.
- **Kill condition?:** NO, but it means total return will be driven almost entirely by income (dividends + buybacks), NOT by multiple expansion. The thesis's FV assumes some re-rating which may never happen.

---

## Riesgos NO Mencionados en Thesis

| Riesgo | Severidad | Mencionado en thesis? | Comentario |
|--------|-----------|----------------------|------------|
| QS discrepancy (54 vs 9.5/10) | HIGH | NO | Largest gap in portfolio. Thesis uses flawed manual scoring. |
| UK Generational Ban contagion risk | HIGH | Minimizado | Thesis mentions "generational smoking bans (NZ model) could spread" in autocritica but dismisses it |
| DDM perpetuity growth fragility | HIGH | Minimizado | Thesis shows bear DDM is underwater but proceeds anyway |
| US nicotine pouch lawsuits (Zone trademark + TJP breach of contract) | MEDIUM | NO | Two active US lawsuits could impair NGP growth strategy |
| Australia menthol ban + stick regulations (April 2025) | MEDIUM | NO | Australia is an Imperial "priority market" -- menthol ban, packaging standardization, individual stick health warnings |
| Beta unreliability (0.139) | MEDIUM | Minimizado | Thesis acknowledges but still uses WACC derived from it |
| Accelerating institutional ESG divestment | HIGH | Mentioned but impact underestimated | Thesis says "already priced in" but trend is accelerating |
| FY25 reported revenue declined (-0.7%) | MEDIUM | NO | Thesis claims revenue growing, but FY25 reported revenue actually declined |
| NGP is only 4% of net revenue (not 7% as thesis claims) | LOW | Misleading | Thesis says NGP is 7% of revenue but FY24 data shows 4% of net revenue |
| Debt maturities: EUR 650M + USD 400M + GBP 188M in 2026 | LOW | NO | ~GBP 1.1B maturing in 2026, refinancing in higher rate environment |

---

## Additional Risk Analysis

### Fundamental Risk: NGP Competitive Irrelevance

Imperial's NGP business is a distant third behind PMI and BAT:
- PMI: NGP = 38.8% of revenue (IQOS dominant in heated tobacco)
- BAT: NGP = 13.3% of revenue (Vuse dominant in vaping)
- Imperial: NGP = ~4% of net revenue (niche player in all three categories)

Imperial's "asset-light" NGP approach means lower investment but also lower market share. The Zone nicotine pouch brand faces TWO US lawsuits (trademark infringement by 2ONE Labs + breach of contract by TJP Labs). The Pulze heated tobacco device is in only 8 markets vs IQOS in 70+. If the tobacco-to-NGP transition accelerates, Imperial risks being the Blackberry of tobacco -- competent in the legacy business but irrelevant in the new one.

**Probability:** Media (30-40%)
**Impact:** Alto -- If NGP becomes the primary nicotine delivery mechanism within 15 years, Imperial's current 4% NGP share could mean secular revenue decline of 5-10%/year instead of the current 2-3%.

### Financial Risk: Revenue Reality vs Thesis Narrative

The thesis states revenue is growing at +3-4%. Reality check:
- FY25 reported revenue: GBP 32.17B (-0.7% YoY)
- FY25 constant currency tobacco + NGP net revenue: +4.1%
- FY25 tobacco volumes: 186.9B sticks (-1.7%)
- Price/mix: +5.4%

The thesis is technically correct that net revenue grew at constant currency, but the REPORTED revenue declined. Currency headwinds are real and persistent for a UK-listed company with global revenue. The thesis uses constant currency figures which flatter the picture.

### Valuation Risk: Revised Fair Value Estimate

Using more conservative but defensible parameters:

**DDM (Conservative):**
- Dividend: 160.32p
- Growth: 3.5% (below company guidance of 4.5%, reflecting long-term volume decline acceleration + regulatory headwinds)
- Required return: 9.5% (adding 50bp risk premium for ESG + regulatory risk vs thesis's 9%)
- FV = 160.32 * 1.035 / (0.095 - 0.035) = 165.93 / 0.06 = 2,766p

**FCF Yield (Conservative):**
- FCF per share: 316p
- Target yield: 9% (conservative for tobacco)
- FV = 316 / 0.09 = 3,511p

**Blended Conservative FV:**
- DDM 60%: 2,766 * 0.6 = 1,660p
- FCF Yield 40%: 3,511 * 0.4 = 1,404p
- Total: 3,064p

At current price of 3,341p, this gives **MoS of -8.3%** (negative -- the stock is OVERVALUED under conservative assumptions).

Even using the thesis's own bear DDM of 2,752p at 60% weight + FCF yield at 3,515p at 40%:
- Blended = 2,752 * 0.6 + 3,515 * 0.4 = 1,651 + 1,406 = 3,057p
- MoS = -8.5%

**The stock has appreciated from 3,082p (thesis entry) to 3,341p (+8.4%). Much of the original MoS has been consumed by price appreciation.**

---

## Kill Conditions Sugeridas

Based on my findings, these kill conditions should be added to the thesis:

1. **EU or another G7 country adopts generational smoking ban** -- If the UK model spreads to EU (Germany, France, Spain are Imperial priority markets), the terminal value thesis collapses. SELL on announcement.
2. **Dividend growth falls below 2%** -- At g=2% and r=9%, DDM FV = 160.32 * 1.02 / 0.07 = 2,335p. At that point the stock is deeply overvalued.
3. **NGP net revenue growth turns negative for 2 consecutive quarters** -- This would indicate the NGP hedge is failing.
4. **Tobacco volume decline accelerates beyond -5%/year** -- If volume decline accelerates beyond pricing power's ability to compensate, the revenue equation breaks.
5. **Debt/EBITDA exceeds 3.5x** -- With declining volumes and regulatory headwinds, leverage above this level becomes dangerous.

---

## Riesgo Agregado

- Numero de riesgos HIGH+CRITICAL: 5
- Riesgos correlacionados? SI -- Regulatory risk (UK ban), ESG divestment, and volume decline are all correlated. A regulatory wave would simultaneously accelerate volume decline AND institutional selling.
- Risk Score Final: **HIGH**

The thesis is built on the assumption that pricing power will FOREVER exceed volume decline. This assumption has been correct for 50 years. But the regulatory environment is changing (generational bans, menthol bans, individual stick warnings, packaging standardization) in ways that could eventually break this equation. The thesis fails to adequately address: (a) the quality score discrepancy, (b) the DDM valuation fragility, (c) the UK generational ban contagion risk, and (d) the accelerating ESG exclusion headwind.

**The most concerning finding is that at current price (3,341p), the MoS under conservative assumptions is NEGATIVE. The stock has run up 8.4% since entry and is now closer to fair value than the thesis suggests.**

---

## 🔄 META-REFLECTION

### Dudas/Incertidumbres
- The quality_scorer's ROIC spread of 2.1pp seems too low even accounting for goodwill. Imperial's ROIC of 20.7% (FY25) minus WACC of 7.5% = 13.2pp spread. The tool may be using a different WACC or ROIC calculation. This needs investigation -- if the tool is wrong, QS could be 60-65 rather than 54.
- I am uncertain whether the beta of 0.139 reflects genuine low volatility of tobacco stocks or is a data artifact. Using a more standard tobacco beta of 0.6 would increase WACC significantly and further reduce the DDM fair value.
- The "asset-light" NGP strategy could be viewed either positively (low capex, optionality) or negatively (underinvestment, competitive irrelevance). I lean negative but cannot be certain.

### Riesgos que Podrian Estar Subestimados
- The UK generational ban contagion risk. If the EU follows (which is plausible given EU public health orientation), this moves from CRITICAL but slow (15-30 years) to CRITICAL and faster (5-10 years). I classify this as CRITICAL but the probability of EU contagion is hard to estimate -- I put it at 20-30% within 10 years, but this is a guess.
- The ESG divestment acceleration. I classified the probability as "Alta" but the IMPACT may be higher than "Medio" if it leads to genuine liquidity problems for tobacco stocks over the next decade.

### Discrepancias con Thesis
1. **QS: Thesis says 9.5/10 (Tier A), tool says 54 (Tier C), I estimate ~60-65 (Tier B).** The thesis uses a simplistic 10-point checklist that gives full marks to ROE (which is inflated by leverage/negative equity) and moat (which is a depleting asset). This is the most material discrepancy.
2. **MoS: Thesis says 20%, I calculate -8% to +7% under conservative assumptions.** The thesis uses a DDM with aggressive perpetuity growth.
3. **NGP revenue: Thesis says 7% of revenue, actual FY24 data shows 4% of net revenue.** The thesis may be using a different revenue base.
4. **Revenue growth: Thesis says +3-4%, reported FY25 revenue was -0.7%.** Constant currency vs reported is a meaningful difference.
5. **Value Trap Score: Thesis says 1/10. I would give 3-4/10.** Secular decline + ESG exclusion + regulatory wave = more than just "one factor."

### Sugerencias para el Sistema
1. The quality_scorer.py tool should be investigated for how it handles tobacco companies' unusual revenue structure (excise taxes in gross revenue). This may be systematically underrating tobacco companies on FCF margin.
2. DDM-based fair values should ALWAYS include sensitivity tables showing at what g and r the stock becomes overvalued. The thesis includes this but dismisses the bear case.
3. For industries in secular decline, the DDM perpetuity growth rate should be NEGATIVE or zero, not +4.5%. A more appropriate model would be a two-stage DDM: 4.5% growth for 10 years, then 0% or negative growth terminal.

### Preguntas para Orchestrator
1. Given the QS discrepancy (54 vs thesis 9.5/10), should the MoS requirement be revised upward? At Tier B, we typically want 20-25% MoS, and at current price the MoS is approximately 0-7% (my conservative estimate). This suggests the position may be approaching a TRIM or EXIT.
2. Should we recalculate the fair value using a two-stage DDM (growth phase + terminal decline) instead of the perpetuity DDM? This would more accurately reflect the reality of a declining industry.
3. The stock is up 8.4% since entry. Given the negative MoS under conservative assumptions, should we consider taking profits while the position is in the green?
4. Imperial is the ONLY tobacco position in the portfolio. Is this intentional diversification or an oversight? If the thesis is weaker than believed, does it warrant its current 5% allocation?
