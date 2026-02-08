# Risk Assessment: ALL (Allstate Corporation)

## Fecha: 2026-02-08

## Risk Score: MEDIUM-HIGH

### Executive Summary

Allstate's thesis paints an overly rosy picture of a turnaround story trading at a P/E discount to peers. The ACTUAL Quality Score is 56/100 (Tier B), not the "8/10 Tier A" the thesis claimed. While Q4 2025 earnings were exceptional (combined ratio 72.9%, net income $3.8B), several material risks were either absent from or minimized in the thesis:

1. **The Arity/data privacy litigation is completely absent from the thesis** -- Texas AG lawsuit with potential exposure across 45 million consumers and $7,500 per violation under TDPSA.
2. **Senate hearing on "systematic fraud" in claims handling was not mentioned** -- bipartisan congressional scrutiny with adjusters testifying about estimate manipulation, raising risk of federal legislation.
3. **California wildfire exposure of $1.1B (Jan 2025) not quantified** -- thesis mentioned generic "CAT losses" but didn't flag this specific exposure.
4. **The competitive dynamics are worse than stated** -- Allstate is voluntarily cutting premiums for 7.8M customers by avg 17%, which will compress margins in 2026 while Progressive has surged to 17% market share vs Allstate's 10.2%.
5. **CEO compensation controversy** -- $26.1M compensation while Congress accused the company of "running a racket" in claims handling creates governance and reputational risk.
6. **ROIC spread is essentially zero** (0.4pp per quality_scorer) -- thesis claimed ROE 37% >> WACC ~10%, but ROIC is a more relevant measure of value creation and the spread is negligible.

The thesis FV of $240 may be approximately correct post-Q4 earnings, but the risk profile is materially worse than documented. Risk-adjusted fair value: $205-215.

---

## Matriz de Riesgos

| # | Categoria | Riesgo | Probabilidad | Impacto | Score | Mitigante |
|---|-----------|--------|-------------|---------|-------|-----------|
| 1 | Legal/Regulatorio | Arity/Data Privacy litigation (TX AG + class actions) | Alta | Alto | CRITICAL | Settlement likely but costly; precedent-setting case |
| 2 | Fundamental | Competitive pricing pressure + voluntary rate cuts compressing margins | Alta | Alto | CRITICAL | PIF growth 3%, but at what margin cost? |
| 3 | Fundamental | Climate/CAT losses structural trend ($1.1B CA fires alone) | Media-Alta | Alto | HIGH | Reinsurance program, but trend worsening 5-7% annually |
| 4 | Legal/Regulatorio | Senate hearing / federal claims practice legislation | Media | Alto | HIGH | Industry-wide, not Allstate-specific only |
| 5 | Governance | CEO $26M comp + claims manipulation allegations | Media | Medio | MEDIUM | 10b5-1 selling plan, long tenure provides stability |
| 6 | Fundamental | Softening P&C market cycle (2026-2028) | Alta | Medio | HIGH | Discipline in underwriting, but cycle is structural |
| 7 | Regulatorio | State-level rate regulation limiting pricing flexibility | Media | Medio | MEDIUM | Multi-state diversification mitigates |
| 8 | Valoracion | Limited MoS after price appreciation ($207.55 vs $240 FV) | Media | Medio | MEDIUM | Q4 earnings beat supports FV |
| 9 | Governance | Insider selling pattern (CEO selling monthly) | Media | Bajo | LOW | Under 10b5-1 plan, pre-planned |
| 10 | Geopolitico | Tariffs on auto parts increasing claims costs | Baja | Medio | LOW | Pass-through to premiums with lag |

### Scoring Key:
- Alta x Alto = CRITICAL
- Alta x Medio OR Media x Alto = HIGH
- Media x Medio = MEDIUM
- Baja x cualquiera OR cualquiera x Bajo = LOW

---

## Top 3 Riesgos Criticos

### 1. Arity/Data Privacy Litigation -- ABSENT FROM THESIS

- **Categoria:** Legal/Regulatorio
- **Descripcion:** Texas Attorney General Ken Paxton filed the FIRST-EVER enforcement action under the Texas Data Privacy and Security Act (TDPSA) against Allstate and subsidiary Arity in January 2025. Allstate is accused of secretly collecting trillions of miles of location data from 45+ million Americans through SDKs embedded in third-party apps (Life360, GasBuddy, Routely, Fuel Rewards). This data was used to adjust insurance premiums and sold to other insurers. Multiple class action lawsuits are consolidated (In re Allstate & Arity Consumer Privacy Litigation). Allstate was given 30 days to cure violations in Nov 2024 and failed to comply.
- **Evidencia:**
  - Texas AG announcement Jan 13, 2025
  - Consolidated class action litigation (April 2025)
  - Potential fines: $7,500 per TDPSA violation, $10,000 for other violations
  - 45 million affected consumers = theoretical exposure in billions (though actual settlement will be far less)
  - Other state AGs likely to follow Texas precedent
- **Probabilidad:** Alta -- Litigation is active and growing. This is a precedent-setting case.
- **Impacto si materializa:** Moderate to Severe. Realistic settlement range: $200M-$1B depending on scope. But the bigger risk is operational: if Arity's data collection model is shut down or severely restricted, Allstate loses a competitive advantage in risk pricing. Additionally, multi-state regulatory copycat actions could multiply costs.
- **Estimated portfolio impact:** If $500M settlement + legal costs: ~$2/share after-tax. Manageable. If $1B+: ~$4/share. If Arity model is shut down: loss of pricing edge, structural damage to competitive position.
- **Mitigante:** Allstate has deep pockets ($10.2B net income in 2025). Settlement is affordable. But the Arity business model may need fundamental restructuring.
- **Kill condition?:** NO for settlement alone. YES if Arity model is permanently banned across multiple states (loss of data advantage = moat erosion).

### 2. Competitive Pricing Pressure + Voluntary Rate Cuts

- **Categoria:** Fundamental
- **Descripcion:** Allstate proactively reduced premiums for 7.8 million auto and homeowners customers by an average of 17% in 2025. While this is framed as "customer value," it represents material margin compression. Progressive has grown to 17% market share vs Allstate's 10.2%, and the gap is widening. The P&C market is entering a softening cycle after the 2020-2024 hard market. 42 auto insurers filed rate decreases in the past 12 months, with 17 new entrants in Florida alone since Jan 2024.
- **Evidencia:**
  - CEO Tom Wilson: "proactively reduced premiums for 7.8 million customers by average 17%"
  - Progressive: 17% market share, Allstate: 10.2% (Allstate is losing relative position)
  - Morgan Stanley downgraded ALL to Equalweight citing competitive auto market
  - TD Cowen downgraded from Buy to Hold in Jan 2026
  - Industry entering soft market cycle (Swiss Re, InsuranceJournal analysis)
- **Probabilidad:** Alta -- This is already happening, not speculative.
- **Impacto si materializa:** Combined ratio likely to rise from the Q4 2025 level of 72.9% toward 90-95% in 2026. Thesis assumed mid-90s as base case, which appears reasonable. But the Q4 72.9% is an outlier driven by benign catastrophe quarter ($209M CAT losses), not the new normal. If combined ratio normalizes to 92-95%, EPS drops from the $37.7 TTM to consensus ~$24. This is already in the thesis base case -- but the thesis treats $24 EPS as conservative when it may be the NEW OPTIMISTIC case if pricing competition intensifies beyond current expectations.
- **Estimated portfolio impact:** Each 1pp of combined ratio = ~$0.50-0.70 EPS impact. If combined ratio is 97% instead of 93%: EPS drops ~$2-3, FV drops to $210-220.
- **Mitigante:** Allstate's PIF grew 3% in 2025 despite rate cuts, suggesting some pricing power. Investment income ($3.1B+ annually) provides earnings floor.
- **Kill condition?:** YES if combined ratio exceeds 100% for 2+ consecutive quarters (underwriting loss sustained).

### 3. Climate/Catastrophe Losses Structural Trend

- **Categoria:** Fundamental
- **Descripcion:** 2025 was the 6th consecutive year with insured catastrophe losses exceeding $100B globally. The LA wildfires (Jan 2025) alone cost Allstate $1.1B. While Allstate exited new California homeowners policies in 2022, it still has legacy exposure. The structural trend is 5-7% annual increase in catastrophe losses (Munich Re data). Allstate's modeled 1-in-100 year aggregate probable maximum loss is $3.0B net of reinsurance. A single bad hurricane season could wipe out an entire quarter of earnings.
- **Evidencia:**
  - Q1 2025 catastrophe losses: $2.2B pre-tax (Allstate)
  - California wildfires Jan 2025: $1.1B Allstate-specific (CNN reporting)
  - Q4 2025 CAT losses: only $209M (unusually benign)
  - LA wildfires total industry: $35-45B insured losses
  - Munich Re: insured losses trend +5-7% annually
  - Senate hearing: adjusters testify Allstate alters damage estimates downward
- **Probabilidad:** Media-Alta -- A bad catastrophe year is not "if" but "when." The 72.9% Q4 combined ratio benefited from unusually low CAT losses.
- **Impacto si materializa:** Q1 2025 already showed $2.2B CAT losses in a single quarter. A severe hurricane or repeated convective storms could push annual CAT losses to $4-6B. At that level, even with reinsurance, earnings would be materially impaired.
- **Estimated portfolio impact:** In a severe CAT scenario, EPS could drop to $15-18 for a year. At 10x P/E: stock at $150-180, representing 13-28% downside from current price.
- **Mitigante:** Reinsurance program covers tail risk. Allstate pulled back from highest-risk California market. Can reprice post-events.
- **Kill condition?:** YES if CAT losses structurally exceed $2B/quarter for 2+ consecutive quarters AND reinsurance costs spiral, indicating the business model cannot price for climate risk.

---

## Riesgos NO Mencionados en Thesis

| Riesgo | Severidad | Mencionado en thesis? | Comentario |
|--------|-----------|----------------------|------------|
| **Arity/Data Privacy Litigation** | HIGH | NO | Completely absent. This is the most serious omission. |
| **Senate hearing on claims fraud** | HIGH | NO | Bipartisan congressional scrutiny with adjusters testifying about systematic estimate manipulation. |
| **California wildfire $1.1B exposure (Jan 2025)** | MEDIUM | NO (generic CAT mentioned) | Thesis mentioned CAT losses generically but not the $1.1B specific exposure. |
| **Quality Score overstatement** | HIGH | Minimized | Thesis claimed "8/10 Tier A" but actual QS = 56 (Tier B). ROIC spread only 0.4pp. |
| **CEO compensation controversy ($26.1M)** | MEDIUM | Partially (noted "Red flag") | Thesis noted it but didn't flag the Senate hearing context where it became politically toxic. |
| **Morgan Stanley + TD Cowen downgrades** | MEDIUM | NO | Both downgraded in Jan 2026, signaling thesis "played out." |
| **Voluntary 17% premium cut for 7.8M customers** | HIGH | NO | This is the Q4 2025 announcement and represents material margin compression going forward. |
| **Progressive market share surge to 17% vs ALL 10.2%** | MEDIUM | Partially | Thesis noted competition but didn't quantify the market share gap acceleration. |
| **Exclusive agent class action (966 class members, trial June 2026)** | LOW | NO | Immaterial financially but adds legal overhang. |

---

## Quality Score Discrepancy -- CRITICAL FINDING

The thesis claimed ALL is "8/10 Tier A." The ACTUAL Quality Score from quality_scorer.py is:

| Component | Thesis Implied | Actual Score | Gap |
|-----------|---------------|-------------|-----|
| Financial Quality | ~32/40 | 23/40 | -9 pts |
| Growth Quality | ~20/25 | 13/25 | -7 pts |
| Moat Evidence | ~20/25 | 14/25 | -6 pts |
| Capital Allocation | ~8/10 | 6/10 | -2 pts |
| **TOTAL** | **~80/100 (Tier A)** | **56/100 (Tier B)** | **-24 pts** |

**Key discrepancies:**
- ROIC Spread: Only 0.4pp (barely above WACC). Thesis emphasized ROE 37% but ROE is inflated by leverage. ROIC tells the real value creation story and it is essentially breakeven.
- FCF Margin: N/A due to insurance accounting, but the scorer could not confirm strong FCF generation.
- Revenue CAGR and EPS CAGR: Moderate, not exceptional growth.
- Gross Margin Premium vs sector: Only +1.3pp, not a wide moat signal.

This is a Tier B company (Quality Value), not Tier A (Quality Compounder). The investment thesis is not invalidated by this, but the risk profile is higher than represented, and the required MoS should be higher for a Tier B than for a Tier A.

---

## Fair Value Reassessment

### Thesis FV: $240 (P/E 10x on $24 EPS)

### Post-Q4 2025 Earnings Update:
- Q4 2025 EPS: $14.31 (massive beat, $4.45 above consensus)
- Full Year 2025 EPS: ~$37.7 (well above $24 consensus for 2026)
- 2025 was an OUTLIER year -- combined ratio 72.9% Q4, ~83% full year
- 2026 consensus EPS: ~$24 (normalization expected)

### Risk-Adjusted Fair Value:
The thesis FV of $240 assumed P/E 10x on $24 EPS. This remains a reasonable base case given that:
- Q4 2025 confirmed execution capability
- Investment income is strong
- PIF growing 3%

However, applying a risk discount for:
1. Arity litigation overhang: -3% (~$7)
2. Softening market / margin compression risk: -5% (~$12)
3. Quality tier correction (Tier B not Tier A): -3% (~$7)

**Risk-adjusted FV: $214** (vs thesis $240, -11% discount)

**Current price: $207.55**
**Risk-adjusted MoS: 3.1%** (barely any margin of safety)

At current price, the risk-reward is mediocre: ~3% upside to risk-adjusted FV, with material downside in a bad catastrophe year or if the Arity litigation results in a large settlement.

---

## Kill Conditions Sugeridas

These should be added to the thesis:

1. **Combined ratio > 100% for 2 consecutive quarters** -- indicates the underwriting model is broken and the turnaround has reversed.
2. **Arity business model permanently banned by regulatory action across multiple states** -- loss of data-driven pricing advantage would erode the narrow moat further.
3. **Federal claims practice legislation passes** -- if Congress legislates claims handling requirements based on the Senate hearing, compliance costs would structurally increase.
4. **CEO departure without clear succession plan** -- Wilson has been CEO since 2007. No visible succession plan. A sudden departure could disrupt the turnaround.
5. **Market share drops below 9% in auto** -- currently 10.2%, a sustained decline would signal pricing discipline is not working.

---

## Riesgo Agregado

- Numero de riesgos HIGH+CRITICAL: 4 (Arity litigation, competitive pricing, CAT losses, Senate/regulatory)
- Riesgos correlacionados? YES:
  - Climate risk + regulatory risk are correlated: more catastrophes -> more political pressure -> more rate regulation -> compressed margins
  - Senate hearing + Arity litigation: both increase regulatory scrutiny and legal costs simultaneously
  - Competitive pressure + rate cuts: both compress margins in same direction
- Risk Score Final: **MEDIUM-HIGH**

The 4 high/critical risks, with 2 pairs being correlated, elevate the overall risk profile above what the thesis documented. The thesis represented this as a straightforward value play. The reality is more nuanced: Allstate faces legal, regulatory, competitive, and climate headwinds simultaneously. The stock is not expensive, but the margin of safety at current price ($207.55 vs $214 risk-adjusted FV) is insufficient for the risk level.

---

## META-REFLECTION

### Dudas/Incertidumbres

1. **Arity litigation quantum is highly uncertain.** The $7,500 per violation x 45M consumers = $337B theoretical maximum is obviously absurd and will never materialize. Realistic settlement could range from $100M to $2B. I used $500M as central estimate but have low confidence in this number.

2. **Combined ratio normalization trajectory is unclear.** Q4 2025 was 72.9% (benign CAT quarter). Full year 2025 was much better. The thesis assumed mid-90s for 2026. Allstate is voluntarily cutting rates 17%, which should push combined ratio higher. But by how much? I lack precision on the earnings impact of the 17% rate cut across 7.8M policies.

3. **The "ROE 37% vs ROIC 0.4pp spread" discrepancy needs more analysis.** Insurance companies use leverage structurally (float). ROE may be a more appropriate measure for insurers than ROIC. The quality_scorer may be penalizing ALL unfairly on ROIC spread because the tool was not designed for financial companies. However, this uncertainty cuts both ways -- if the ROE is leverage-driven, it may not be as durable as it appears.

### Riesgos que Podrian Estar Subestimados

1. **The Arity litigation risk.** This is the first-ever enforcement under TDPSA. If it becomes a template for other state AGs, Allstate could face 10-20 separate state actions. This is potentially a multi-billion-dollar overhang that could take years to resolve and fundamentally alter the Arity business model.

2. **Federal claims legislation.** The Senate hearing was bipartisan (Hawley, a Republican, led it). If both parties want to legislate insurance claims practices, the probability is higher than I've estimated. The insurance industry has historically avoided federal regulation, but the political dynamics are shifting.

### Discrepancias con Thesis

1. **Quality Score:** Thesis said "8/10 Tier A" -- actual is 56/100 Tier B. This is a MAJOR discrepancy.
2. **Risk section:** Thesis identified 3 risks. I identified 10, including 4 that are HIGH or CRITICAL.
3. **Fair Value:** Thesis $240 vs my risk-adjusted $214. The thesis did not discount for litigation or competitive risk.
4. **Combined ratio narrative:** Thesis framed mid-90s as conservative. It may actually be optimistic given the 17% voluntary rate cuts.
5. **Insider selling:** Thesis noted it as "MIXTO" but the pattern is CEO selling monthly under 10b5-1, which while pre-planned, is a continuous outflow.

### Sugerencias para el Sistema

1. **quality_scorer.py needs an insurance-specific mode.** The current tool penalizes financial companies on ROIC spread because insurance float creates leverage that inflates ROE vs ROIC. A mode that uses ROE for financial companies (banks, insurers) would be more accurate.

2. **Litigation risk scanner.** A systematic process to search for active litigation for every position would have caught the Arity case. Currently, the thesis author only searches for what they know to look for.

3. **The thesis QS "8/10" was NOT from quality_scorer.py.** The thesis used an informal quality assessment, not the actual tool. This is a process failure: EVERY thesis should run quality_scorer.py and use THAT number, not an informal estimate.

### Preguntas para Orchestrator

1. Given the risk-adjusted FV of $214 and current price of $207.55, the MoS is only 3.1%. For a Tier B company with 4 HIGH/CRITICAL risks, is this sufficient? My recommendation would be HOLD (not ADD) with a tight watch on Q1 2026 combined ratio and Arity litigation developments.

2. Should the conviction on ALL be downgraded from the current level? The thesis was written before Q4 earnings (which were strong) but also before the full scope of Arity litigation was understood.

3. The CEO has been in charge since 2007 (19 years). At what point does key-person risk become material? There is no visible succession plan in public filings.

---

## Sources

### Q4 2025 Earnings
- [Allstate Doubles Q4 Net Income While Auto Underwriting Income Triples](https://www.insurancejournal.com/news/national/2026/02/05/856975.htm)
- [Allstate Reports $10.2 Billion Net Income for 2025](https://collisionweek.com/2026/02/05/allstate-reports-10-2-billion-net-income-2025/)
- [Allstate Q4 Earnings Call Highlights](https://www.dailypolitical.com/2026/02/07/allstate-q4-earnings-call-highlights.html)
- [Allstate Q4 2025 Earnings Call Transcript - Seeking Alpha](https://seekingalpha.com/article/4866513-the-allstate-corporation-all-q4-2025-earnings-call-transcript)

### Arity/Data Privacy Litigation
- [Texas AG Sues Allstate and Arity](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-allstate-and-arity-unlawfully-collecting-using-and-selling-over-45)
- [Allstate Data Collection Class Action](https://www.classaction.org/allstate-app-data-collection-privacy-lawsuits)
- [In re Allstate & Arity Consumer Privacy Litigation](https://www.bfalaw.com/cases/in-re-allstate-arity-consumer-privacy-litigation)

### Senate Hearing / Claims Practices
- [Allstate, State Farm Blasted at Senate Hearing - S&P Global](https://www.spglobal.com/market-intelligence/en/news-insights/articles/2025/5/allstate-state-farm-blasted-at-senate-hearing-over-claims-practices-88993421)
- [Senator Hawley Exposes Insurance Fraud](https://www.hawley.senate.gov/hawley-chairs-hearing-that-exposes-insurance-fraud-by-major-corporations/)
- [Systematic Fraud Alleged in Claims Practices](https://insurancenewsnet.com/innarticle/systematic-fraud-alleged-in-property-casualty-claims-practices)

### Competition & Market
- [Morgan Stanley Downgrades Allstate](https://www.investing.com/news/analyst-ratings/morgan-stanley-downgrades-allstate-stock-to-equalweight-amid-competitive-auto-market-93CH-4409870)
- [Auto Insurance Market Share - ValuePenguin](https://www.valuepenguin.com/largest-auto-insurance-companies)
- [Auto Insurance Pricing Trends 2026](https://www.autoinsurance.com/research/auto-insurance-pricing-trends/)

### Catastrophe / Climate
- [Allstate Expects $1.1B Loss from California Fires - CNN](https://www.cnn.com/2025/02/06/business/allstate-california-fire-losses/index.html)
- [Munich Re Natural Disaster Figures 2025](https://www.munichre.com/en/company/media-relations/media-information-and-corporate-news/media-information/2026/natural-disaster-figures-2025.html)
- [Allstate Catastrophe Reinsurance Program](https://www.allstateinvestors.com/static-files/e642c6b7-9caa-44fd-a52c-1eb4815e4313)

### Insider Selling
- [Allstate CEO Wilson Sells $3.3M in Stock](https://www.investing.com/news/insider-trading-news/allstate-ceo-wilson-sells-33m-in-stock-93CH-4486599)
- [Allstate Insider Transactions - Yahoo Finance](https://finance.yahoo.com/quote/ALL/insider-transactions/)

### Analyst Ratings
- [Allstate Analyst Ratings - StockAnalysis](https://stockanalysis.com/stocks/all/ratings/)
- [Benzinga: 10 Analyst Ratings on Allstate](https://www.benzinga.com/insights/analyst-ratings/26/02/50426227/deep-dive-into-allstate-stock-analyst-perspectives-10-ratings)

### CEO Compensation
- [Senate Grills Allstate CEO Over $26M Compensation](https://www.sill.com/latest-news/posts/senate-grills-allstate-ceo-over-26m-executive-compensation/)
- [Hawley Blasts Allstate CEO - Yahoo Finance](https://finance.yahoo.com/news/josh-hawley-blasts-allstate-ceo-214700596.html)
