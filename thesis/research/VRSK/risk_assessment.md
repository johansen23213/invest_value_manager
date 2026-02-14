# Risk Assessment: VRSK (Verisk Analytics)

## Fecha: 2026-02-13

## Risk Score: MEDIUM

---

## Matriz de Riesgos

| # | Categoria | Riesgo | Probabilidad | Impacto | Score | Mitigante |
|---|-----------|--------|-------------|---------|-------|-----------|
| 1 | Fundamental | Single-vertical concentration (100% insurance) | Media | Alto | HIGH | Dominant position in that vertical; all top-100 P&C insurers are clients |
| 2 | Fundamental | P&C soft market cycle depresses NWP-linked revenue (~20-25% of rev) | Alta | Medio | HIGH | Subscription base (75%+ of revenue) is contractual and recurring |
| 3 | Fundamental | AI/SaaSpocalypse narrative compresses valuation further | Alta | Medio | HIGH | Verisk is DATA supplier not per-seat SaaS; BMO upgraded citing misprice |
| 4 | Legal/Regulatorio | Driver data privacy litigation (Hyundai/GM class actions) | Media | Medio | MEDIUM | GM FTC ban is precedent; Verisk's driver data is small part of business |
| 5 | Legal/Regulatorio | FTC antitrust scrutiny of data aggregation dominance | Media | Medio | MEDIUM | AccuLynx deal killed; signals FTC watching vertical expansion closely |
| 6 | Financiero | Negative shareholders' equity from aggressive buybacks; ROE 957% is meaningless | Media | Bajo | LOW | FCF $920M/yr easily covers obligations; debt is 1.9x EBITDA |
| 7 | Financiero | $4.9B debt + failed AccuLynx debt ($1.5B notes to be redeemed at 101%) | Baja | Medio | LOW | Redeeming the $1.5B; pro-forma leverage returns to ~1.9x |
| 8 | Fundamental | Moody's RMS + LexisNexis as credible competitors in cat modeling and claims | Media | Medio | MEDIUM | Verisk's 34.5B records + give-to-get model creates structural advantage |
| 9 | Valoracion | Revenue growth only ~5-6% organic; premium valuation requires acceleration | Media | Medio | MEDIUM | EPS growing 10-18% via margin expansion + buybacks, but top-line is modest |
| 10 | Geopolitico | Weather volatility dependency — quiet hurricane season cut 2025 guidance | Alta | Bajo | LOW | Transactional revenue is ~25%; subscription base is stable regardless |
| 11 | Management | Insider selling ($9.9M last year) vs minimal insider ownership (0.3%) | Media | Bajo | LOW | Director purchases offset narrative; compensation-driven selling typical |
| 12 | ESG/Regulatorio | State-level data privacy laws expanding (CCPA, Virginia, Colorado, etc.) | Media | Medio | MEDIUM | Verisk has compliance infrastructure; but regulatory creep raises costs |
| 13 | Valoracion | AccuLynx deal failure + litigation with AccuLynx | Media | Bajo | LOW | One-time cost (101% redemption premium); no ongoing drag |

---

## Top 3 Riesgos Criticos

### 1. Single-Vertical Concentration Risk (100% Insurance Post-Divestitures)

- **Categoria:** Fundamental
- **Descripcion:** After divesting Wood Mackenzie ($3.1B, 2023) and the financial services division, Verisk is now a pure-play insurance analytics company. 100% of revenue comes from the P&C insurance ecosystem. This is a deliberate strategic choice, but it creates existential concentration: any structural disruption to how P&C insurance uses data analytics hits 100% of Verisk's revenue, not a diversified portion.
- **Evidencia:**
  - Revenue breakdown is entirely Insurance segment (Underwriting + Claims)
  - The company explicitly markets itself as "returning to its roots" as an insurance-only company
  - No revenue diversification buffer if insurance spending patterns change
- **Probabilidad:** Media -- P&C insurance is a $700B+ US market that is structurally growing, and data analytics spending within it is increasing. A structural disruption to the industry itself is unlikely in the medium term.
- **Impacto si materializa:** Alto -- If a regulatory change (e.g., banning third-party data in rate-setting) or technological disruption (e.g., insurers building proprietary models at scale) hit, it would affect 100% of Verisk's revenue. Estimated impact: 30-50% revenue decline over 3-5 years if the moat erodes meaningfully.
- **Mitigante:** Verisk serves all top-100 P&C insurers. The give-to-get data model creates a network effect that is extremely hard to replicate. ISO designation as statistical agent is quasi-regulatory. But the LACK of diversification means any black swan in insurance data regulation is catastrophic.
- **Kill condition?:** YES -- If US regulators prohibit third-party actuarial data aggregation, or if more than 2 of the top-10 P&C insurers announce they are building proprietary analytics to replace Verisk.

### 2. P&C Insurance Soft Market Cycle Depresses NWP-Linked Revenue

- **Categoria:** Fundamental / Macro
- **Descripcion:** Approximately 20-25% of Verisk's revenue is tied to net written premiums (NWP) through contracts linked to industry premium volumes. The P&C market is entering a correction phase after several hard-market years. Property rates are declining 10-30% in some segments. As premiums contract or flatten, Verisk's NWP-linked revenue declines proportionally. This is NOT a temporary blip -- soft markets typically last 3-5 years.
- **Evidencia:**
  - BMO Capital specifically flagged "slowing pricing growth in US P&C insurance" as feeding into 20-25% of Verisk's revenue
  - Deloitte 2026 outlook: "premium growth is expected to decline through 2026"
  - Insurance Insider US: "A deep soft market might be closer than you think"
  - Property rates dipping for first time since 2017
  - Already visible in Q3 2025: transactional revenue declined 8.8% YoY
- **Probabilidad:** Alta -- The soft market is already materializing. Property rates are declining, reinsurance capital is at record levels, and the 2025 hurricane season was abnormally quiet.
- **Impacto si materializa:** Medio -- This affects ~20-25% of revenue directly (NWP-linked contracts) and could create 2-4% headwind to overall revenue growth for multiple years. Combined with already modest 5-6% organic growth, this could reduce growth to 3-4% and compress the premium multiple.
- **Mitigante:** 75%+ of revenue is subscription-based with contractual pricing escalators. Verisk has been actively shifting mix toward subscription revenue. Even in the 2008-2011 soft market, Verisk's revenue grew continuously.
- **Kill condition?:** NO -- This is a cyclical headwind, not a structural break. But it should inform valuation (lower growth assumptions in soft market).

### 3. AI/SaaSpocalypse Narrative Compression + Actual Per-Seat Risk Assessment

- **Categoria:** Valoracion / Fundamental
- **Descripcion:** VRSK has fallen ~45% from its 52-week high of $323, caught in the broader SaaSpocalypse selloff that wiped ~$1T from software stocks. The market is treating all data/analytics companies as vulnerable to AI disruption. The critical question: Is Verisk actually at risk from AI, or is this a mispricing?
- **Evidencia:**
  - VRSK -45% from 52w high; broader SaaS sector -25-35%
  - Analyst downgrade: Rothschild cut to Sell, PT from $280 to $220
  - Consensus shifted to Hold (15 analysts)
  - BMO COUNTER-ARGUMENT: upgraded to Outperform, explicitly saying "AI fears misprice its moat"
  - Verisk is NOT per-seat SaaS. It sells DATA and MODELS, not software licenses per user
  - AI/LLMs need DATA as input -- Verisk's proprietary 34.5B records are the raw material LLMs would consume, not replace
  - However: GenAI could enable insurers to build their own models using alternative data, reducing dependency on Verisk's actuarial products over time
- **Probabilidad:** Alta (for continued narrative pressure in 2026) / Baja-Media (for actual fundamental disruption)
- **Impacto si materializa:**
  - Narrative only: Further 15-25% downside if SaaS selloff continues; but reverses when market differentiates data companies from per-seat SaaS
  - Actual disruption: If 2-3 large insurers successfully build AI-powered proprietary analytics, Verisk could lose 10-15% of revenue over 5-7 years. Estimated impact on fair value: -15-20%
- **Mitigante:**
  - Verisk is integrating AI INTO its products (Core Lines Reimagine, Synergy Studio 2026)
  - The give-to-get data network cannot be replicated by a single insurer's AI
  - CEO appointed to Federal Advisory Committee on Insurance -- deep regulatory relationships
  - Historical precedent: similar "technology will displace us" fears about Bloomberg Terminal proved wrong because proprietary data is the moat
- **Kill condition?:** PARTIAL -- If 3+ top-10 insurers announce AI-driven in-house analytics platforms replacing Verisk products, this should be added as kill condition. Current narrative selloff alone is NOT a kill condition.

---

## Additional Risk Detail

### 4. Driver Data Privacy Litigation

- **Categoria:** Legal/Regulatorio
- **Descripcion:** Class action lawsuits filed against Verisk (along with Hyundai, Kia, GM) for receiving and selling driver behavior data (mileage, speed, braking) to insurance companies without adequate consent. 1.7 million Hyundai vehicles' data was shared with Verisk. The FTC has already banned GM/OnStar from sharing such data for 5 years.
- **Probabilidad:** Media -- The litigation is active and the FTC precedent with GM is unfavorable. But Verisk's role was as data recipient, not collector.
- **Impacto:** Medio -- Financial exposure from settlements is likely manageable ($50-200M range for class actions). The larger risk is regulatory precedent: if FTC extends the GM ban to ALL data brokers receiving telematics data, Verisk loses a growth area (usage-based insurance analytics).
- **Mitigante:** Verisk won a dismissal of the ISO Claims data breach lawsuit (EDNY). Driver telematics is a small part of total revenue.

### 5. FTC Antitrust Scrutiny

- **Categoria:** Legal/Regulatorio
- **Descripcion:** The FTC issued a Second Request on the AccuLynx deal (only 3-4% of deals get this). Verisk terminated the deal after FTC failed to complete review. This signals regulatory sensitivity to Verisk's data dominance and vertical expansion.
- **Probabilidad:** Media -- Future M&A will face similar scrutiny. The FTC is explicitly concerned about "data aggregation" creating "information asymmetries."
- **Impacto:** Medio -- Limits Verisk's ability to grow via acquisition (its historical playbook). Forces reliance on organic growth, which is only 5-6%.
- **Mitigante:** Verisk can still make smaller bolt-on acquisitions. Organic growth in subscription revenue is solid. But the AccuLynx litigation adds a tail risk (AccuLynx disputes the termination validity).

### 6. Negative Shareholders' Equity / Balance Sheet Engineering

- **Categoria:** Financiero
- **Descripcion:** ROE of 957% is meaningless -- it reflects near-zero or negative equity from aggressive share buybacks ($250M+ per quarter). Total debt of $4.9B against a market cap of $25B. The $1.5B notes issued for AccuLynx (being redeemed at 101% premium, costing ~$15M extra) add to balance sheet complexity.
- **Probabilidad:** Media (of causing problems) -- In a rising rate environment, rolling over $4.9B in debt costs more.
- **Impacto:** Bajo -- FCF of $920M/yr provides 5.3x interest coverage (10.9x per tool). Net debt/EBITDA of 1.9x is comfortable. The negative equity is an accounting artifact, not a solvency issue.
- **Mitigante:** Strong FCF generation, investment-grade credit rating, no near-term maturities (after redeeming AccuLynx notes).

### 7. Weather/Catastrophe Revenue Volatility

- **Categoria:** Fundamental
- **Descripcion:** Verisk cut 2025 revenue guidance specifically because of a quiet hurricane season reducing demand for catastrophe risk models. Transactional revenue (cat modeling, event response) is inherently variable.
- **Probabilidad:** Alta -- Weather is unpredictable by definition. Quiet seasons will recur.
- **Impacto:** Bajo -- Affects transactional revenue (~25% of total). Subscription revenue is unaffected. Paradoxically, climate change INCREASES long-term demand for cat modeling.
- **Mitigante:** The company is shifting mix toward subscription revenue. A quiet year is followed by increased demand when catastrophes do occur.

### 8. Competition from Moody's RMS and LexisNexis

- **Categoria:** Fundamental / Competitivo
- **Descripcion:** Moody's acquired RMS and is investing heavily in cloud-native catastrophe modeling (Risk Modeler platform). LexisNexis Risk Solutions competes in claims analytics. These are well-capitalized competitors with credible data assets.
- **Probabilidad:** Media -- These competitors have existed for years without materially eroding Verisk's position. But Moody's post-acquisition investment is accelerating.
- **Impacto:** Medio -- If Moody's RMS achieves feature parity on cloud and offers bundled pricing with credit ratings, some cat modeling market share could shift. Estimated 5-10% revenue risk over 5 years.
- **Mitigante:** Verisk's Synergy Studio (2026 launch) is its cloud-native response. The ISO designation and give-to-get data model are not replicable by competitors. Most insurers use BOTH Verisk and RMS models for regulatory compliance.

---

## Riesgos NO Mencionados en Thesis

No thesis exists yet for VRSK. This risk assessment is being produced in parallel with fundamental analysis. The following risks should be prominently featured in any thesis:

| Riesgo | Severidad | Likely to be Overlooked? | Comentario |
|--------|-----------|------------------------|------------|
| 100% insurance concentration post-divestitures | HIGH | YES -- Often framed as "focus" (positive) rather than "concentration" (risk) | The bull case celebrates pure-play; the risk case must acknowledge no diversification buffer |
| P&C soft market cycle hitting NWP-linked revenue | HIGH | YES -- Often ignored because "subscription revenue is 75%+" | 20-25% of revenue is premium-linked; soft markets last 3-5 years |
| FTC antitrust posture limiting M&A growth | MEDIUM | YES -- AccuLynx failure is treated as one-off, but it signals systemic FTC concern about data monopolies | Future deals will face same scrutiny; organic growth is only 5-6% |
| Driver data privacy litigation (Hyundai/GM) | MEDIUM | POSSIBLY -- Often buried in 10-K footnotes | FTC ban on GM is bad precedent; telematics data is growth area |
| Negative equity / balance sheet engineering | LOW | NO -- Obvious in financials | Not a real risk given FCF strength, but inflates ROE making quality look better than it is |
| AccuLynx counter-litigation | LOW | YES -- Verisk terminated but AccuLynx disputes validity | Could result in break-up fee obligation or protracted litigation |
| Revenue growth only 5-6% organic for "premium valuation" | MEDIUM | YES -- EPS growth of 10-18% masks this through buybacks and margin expansion | Premium valuation needs either growth acceleration or multiple compression |

---

## Kill Conditions Sugeridas

Based on risk assessment findings, the following kill conditions should be included in any VRSK thesis:

1. **KC#1: Regulatory prohibition on third-party actuarial data aggregation** -- If US federal or state regulators move to prohibit or materially restrict the use of third-party statistical data in insurance rate-setting, the ISO moat is structurally impaired. EXIT immediately.

2. **KC#2: Top-insurer defection** -- If 2+ of the top-10 P&C insurers announce plans to build proprietary analytics replacing Verisk products, the network effect is breaking. Initiate EXIT evaluation.

3. **KC#3: Organic revenue growth < 3% for 2 consecutive quarters** -- Would signal pricing power erosion beyond cyclical soft market effects. Distinguish from transactional weather volatility by tracking subscription growth specifically.

4. **KC#4: FTC enforcement action targeting Verisk's data aggregation practices directly** -- Beyond blocking acquisitions, if the FTC targets Verisk's core data collection/distribution model (similar to GM telematics ban), this is existential.

5. **KC#5: EBITDA margin decline below 50% for 2 consecutive quarters** -- Current margins are 55%+. Sustained compression below 50% would signal competitive pricing pressure or cost inflation that undermines the moat premium.

---

## Riesgo Agregado

- **Numero de riesgos HIGH+CRITICAL:** 3 (concentration, soft market, AI narrative)
- **Riesgos correlacionados?** YES -- Risks #1, #2, and #3 are correlated. Single-vertical concentration means the soft market cycle AND AI narrative both hit 100% of the business simultaneously. If the AI narrative proves partially correct AND the soft market deepens, the combined effect on revenue growth and valuation multiple is multiplicative, not additive.
- **Risk Score Final:** **MEDIUM**

**Rationale for MEDIUM (not HIGH):**
Despite 3 HIGH-rated risks, the mitigants are substantial:
- Verisk's moat (ISO designation, 34.5B records, give-to-get network, all top-100 insurers as clients) is among the strongest in data analytics
- FCF generation of $920M/yr with 32% FCF margin provides financial resilience
- The AI risk is primarily NARRATIVE (stock price) not FUNDAMENTAL (business model) -- Verisk is a data SUPPLIER to AI, not a per-seat SaaS company
- Historical precedent: Verisk grew revenue continuously through the 2008-2011 soft market
- Insider ownership is low (0.3%) but this is typical for large-cap companies; director purchases provide some confidence signal

However, I would UPGRADE to HIGH if:
- Q4 2025 earnings (Feb 18) show subscription revenue growth decelerating below 7%
- The soft market produces NWP declines exceeding 5% industry-wide
- Any FTC enforcement action directly targeting Verisk's data practices

---

## Earnings Catalyst: Q4 2025 Results on February 18, 2026

**Key metrics to monitor:**
- Subscription revenue growth (must stay >7% to justify premium)
- Transactional revenue trend (already declining; how much further?)
- 2026 guidance range (consensus expects $3.15-3.20B; any cut is negative)
- EBITDA margin trajectory (55%+ is the standard)
- Share buyback authorization and pace
- Any commentary on FTC/AccuLynx litigation
- AI product adoption metrics (Core Lines Reimagine, Synergy Studio timeline)

---

## 🔄 META-REFLECTION

### Dudas/Incertidumbres
- **AI disruption probability is genuinely uncertain.** I classified actual AI disruption as Baja-Media, but I acknowledge I could be wrong. The insurance industry is conservative and slow-moving, which protects Verisk today. But LLM capabilities are accelerating faster than expected. If a well-funded InsurTech demonstrates comparable actuarial accuracy using alternative data + LLMs, the moat erosion could be faster than my 5-7 year estimate.
- **NWP-linked revenue percentage.** BMO cites 20-25%, but Verisk does not explicitly disclose this breakdown in its public filings. The actual figure could be higher, which would make soft market risk more severe.
- **AccuLynx litigation outcome.** AccuLynx disputes the termination validity. If a court rules Verisk improperly terminated, the financial exposure (break-up fee, damages) could be material. I have insufficient data to estimate this.

### Riesgos que Podrian Estar Subestimados
- **FTC antitrust risk** -- I rated this MEDIUM, but the trend in US antitrust enforcement is toward more aggressive action against data aggregators. The AccuLynx Second Request was a warning shot. If the FTC broadens its focus to Verisk's CORE data aggregation (not just acquisitions), the impact would be existential, not medium.
- **Soft market duration** -- I assumed 3-5 years based on historical cycles. But with record reinsurance capital entering the market and catastrophe losses declining, this could be longer. A 7-year soft market would meaningfully reduce Verisk's long-term revenue CAGR.

### Discrepancias con Thesis
- No thesis exists yet. When the thesis is written, I recommend the analyst explicitly address:
  1. Why 100% insurance concentration is acceptable (not just "it's a focused pure-play")
  2. What happens to valuation if organic revenue growth stays at 5-6% in a soft market
  3. The AI disruption question with SPECIFIC evidence, not just "the moat is strong"
  4. The negative equity issue and why ROE of 957% should be ignored in quality assessment

### Sugerencias para el Sistema
- **quality_scorer.py ROE distortion**: VRSK shows ROE 957% due to negative equity from buybacks. The tool should flag when ROE exceeds 100% and note it may be an artifact of buyback-driven negative equity rather than genuine return on capital. ROIC (38.3%) is the correct metric here.
- **Soft market cycle tracking**: Consider adding a P&C insurance cycle indicator to world/current_view.md. This affects VRSK, and potentially other insurance-related positions (ALL, GL) and pipeline candidates (ACGL).
- **SaaSpocalypse cluster risk**: VRSK is being added to the same narrative bucket as ADBE, BYIT.L, PAYC, etc. The system should track which positions are exposed to the SaaSpocalypse narrative separately from actual per-seat pricing risk. VRSK is in the narrative bucket but NOT in the actual per-seat risk bucket.

### Preguntas para Orchestrator
1. Should the Q4 2025 earnings on Feb 18 be treated as a gate before proceeding to R2/R3/R4? The data will materially inform the soft market risk assessment.
2. Given VRSK at $179 vs 52-week high of $323, is the -45% decline sufficient to create margin of safety even with the risks identified? My risk assessment says MEDIUM risk, which typically corresponds to 20-25% MoS requirement.
3. The FTC antitrust risk deserves deeper investigation. Should we launch a separate legal/regulatory deep-dive specifically on Verisk's data practices and regulatory exposure?
4. How does VRSK fit in the portfolio context? We have no insurance data/analytics exposure currently. ALL and GL are insurance companies (different risk profile). VRSK would add a new type of insurance exposure.
