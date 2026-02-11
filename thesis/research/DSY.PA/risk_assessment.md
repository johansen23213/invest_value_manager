# Risk Assessment: DSY.PA (Dassault Systemes SE)

## Fecha: 2026-02-11

## Risk Score: HIGH

---

## Context

Dassault Systemes dropped 21% on 2026-02-11 after reporting Q4 2025 earnings. This is the company's worst single-day decline in its history, wiping approximately EUR 6 billion in market value. The stock trades at EUR 17.77, down 56% from its 52-week high of EUR 40.76 and near its 52-week low of EUR 17.16.

**Key earnings data (Q4 2025):**
- Total revenue: EUR 1.68B (+1% cc, bottom of 1-8% guidance)
- Software revenue: EUR 1.52B (FLAT, vs 1-8% guidance)
- License revenue: EUR 358M (-7% yoy)
- Recurring software: EUR 1.16B (+3%, below 5-8% guidance)
- Non-IFRS operating margin: 37.0% (+90bps yoy) -- margins held
- Non-IFRS EPS: EUR 0.40 (+9% cc)
- FY2025 EPS: EUR 1.31 (non-IFRS), EUR 0.87 (IFRS)

**FY2026 guidance:**
- Revenue growth: 3-5% cc (vs consensus 5.9%)
- EPS: EUR 1.30-1.34 (essentially FLAT)
- Operating margin: 32.2-32.6%

---

## Matriz de Riesgos

| # | Categoria | Riesgo | Probabilidad | Impacto | Score | Mitigante |
|---|-----------|--------|-------------|---------|-------|-----------|
| 1 | Fundamental | Revenue growth structural deceleration | Alta | Alto | CRITICAL | Cloud transition eventually lifts growth |
| 2 | Fundamental | AI disruption of traditional PLM software | Media | Alto | HIGH | Moat in engineering workflows; but narrative is powerful |
| 3 | Fundamental | Medidata / Life Sciences secular decline | Alta | Medio | HIGH | Only ~15% of revenue; diversified across industries |
| 4 | Fundamental | European auto sector prolonged weakness | Alta | Medio | HIGH | Auto is ~20-25% of industrial innovation revenue |
| 5 | Competitivo | Siemens gaining share with Altair + Dotmatics acquisitions | Media | Alto | HIGH | Dassault has CATIA/SOLIDWORKS installed base lock-in |
| 6 | Financiero | IFRS vs non-IFRS 50% gap masks real profitability | Media | Medio | MEDIUM | SBC + amortization are real costs; EUR 429M in adjustments |
| 7 | Financiero | Goodwill/intangibles impairment risk (Medidata) | Media | Medio | MEDIUM | EUR 1.3B net cash provides buffer |
| 8 | Valoracion | Value trap at "optically cheap" P/E if growth doesn't recover | Alta | Alto | CRITICAL | Price already reflects considerable pessimism |
| 9 | Valoracion | Short interest surged 427% to 593K shares | Media | Medio | MEDIUM | Still small relative to float |
| 10 | Macro | European manufacturing recession persists | Alta | Medio | HIGH | 42% of software revenue from Europe |
| 11 | Geopolitico | China revenue exposure (~12% of revenue) amid trade tensions | Media | Medio | MEDIUM | Diversified across Americas/Asia/Europe |
| 12 | Ciberseguridad | Data breach by 0APT group (Feb 3, 2026) | Media | Alto | HIGH | Scope unknown; defense customers may react |
| 13 | Governance | Controlling shareholder (GIMD ~40-48%) limits minority rights | Baja | Medio | LOW | Alignment via long-term ownership; but no exit pressure |
| 14 | Regulatorio | Dual-use export controls tightening (ITAR, EU reg) | Baja | Medio | LOW | French origin = ITAR-free advantage |

### Scoring Key:
- Alta x Alto = CRITICAL
- Alta x Medio OR Media x Alto = HIGH
- Media x Medio = MEDIUM
- Baja x cualquiera OR cualquiera x Bajo = LOW

---

## Top 3 Riesgos Criticos

### 1. Revenue Growth Structural Deceleration -- Not Cyclical

- **Categoria:** Fundamental / Business Model
- **Descripcion:** Dassault's revenue growth has decelerated from ~10% organic in 2021-2022 to 4% in FY2025 and guidance of only 3-5% for FY2026. Q4 2025 growth was just 1% cc -- the worst quarter in recent memory. The company guided FY2026 EPS essentially flat (EUR 1.30-1.34 vs EUR 1.31 actual). This is NOT a one-off miss. This is a trend:
  - FY2023: +7% cc
  - FY2024: +5% cc
  - FY2025: +4% cc
  - FY2026 guide: +3-5% cc (midpoint 4%)
  - Q4 2025: +1% cc (alarming)

- **Evidence:**
  - License revenue (upfront sales) fell 7% in Q4 and 6% for FY2025 -- clients are NOT signing new large deals
  - Recurring revenue grew only 3% in Q4 vs 5-8% guidance -- even the subscription/cloud engine is sputtering
  - Software revenue was FLAT in Q4 (0% growth) vs 1-8% guidance range -- the low end was barely met
  - 3DEXPERIENCE platform revenue was DOWN 3% in Q4 -- the flagship next-gen product is shrinking
  - ARR growth of only 6% -- described by analysts as "underwhelming", averaging 6% since late 2023
  - JPMorgan called it "worse than even the most negative had feared"
  - Jefferies flagged the quarter as "particularly weak"

- **Probabilidad:** Alta -- This is not one bad quarter. The deceleration pattern spans 3+ years. The cloud transition is cannibalizing license revenue faster than subscription can compensate. Management itself guided only 3-5% growth.

- **Impacto si materializa:** 30-50% revenue multiple de-rating. If the market re-prices DSY from a "mid-single-digit grower" (historically traded at 30-40x earnings) to a "low-single-digit grower" (deserving 15-20x), the stock has another 20-30% downside from current levels. At EUR 17.77 and ~20x IFRS P/E (13.5x non-IFRS), a permanent 3-4% grower might be worth 12-15x non-IFRS EPS = EUR 15.70-19.65.

- **Mitigante:** Cloud transition is expected to eventually provide uplift once license cannibalization completes. Management calls 2025 "a year of transition" and 2026 "a year of execution." AI revenue of EUR 50-100M expected in 2026. But management credibility is damaged.

- **Kill condition?:** YES -- If FY2026 actual revenue growth is <3% (below bottom of guidance), this would confirm structural growth impairment. Should be a hard kill condition.

---

### 2. AI Disruption Narrative Causing Permanent Valuation De-rating

- **Categoria:** Fundamental / Valoracion
- **Descripcion:** The market is pricing in fear that AI will disrupt traditional PLM/CAD software business models. Dassault's crash coincided with a broader European software selloff driven by AI disruption fears (SAP also fell ~15% recently). The narrative: AI "world models" (from NVIDIA, startups) could eventually replicate engineering simulation and design tasks that Dassault charges premium prices for.

- **Evidence:**
  - ZeroHedge headline: "AI Disruption Fears Go Global: France's Dassault Crashes Most On Record"
  - CNBC: "The stock plunge stoked concerns that artificial intelligence will disrupt its business model"
  - Short interest in DASTY surged 427.6% from 112,398 to 593,054 shares between Jan 15 and Jan 30
  - SAP's own 2026 cloud forecasts disappointed, triggering its biggest daily loss since 2020
  - Broader European software sector (Temenos, Sage, SUSE) all sold off on AI fears
  - NVIDIA described Dassault as being at the "epicenter of the next frontier of AI" -- but this is double-edged: if AI commoditizes simulation, Dassault's pricing power erodes

- **Probabilidad:** Media -- Engineering PLM/CAD software has deep workflow integration and switching costs that make pure AI disruption unlikely in the short term (3-5 years). CATIA workflows are embedded in aerospace/auto manufacturing processes over decades. However, the NARRATIVE alone can permanently de-rate the multiple, even if the actual disruption takes 10+ years. The market is forward-looking and may price in disruption risk NOW.

- **Impacto si materializa:** If AI truly commoditizes PLM/simulation (5-10 year timeframe), Dassault's 83% gross margin collapses to 60-70%. Revenue multiple compresses from 3-4x to 1-2x revenue. In the nearer term, if the market permanently treats DSY as an "at-risk" software business rather than a compounder, the P/E multiple stays compressed at 12-15x non-IFRS vs historical 30-40x.

- **Mitigante:** Dassault is partnering with NVIDIA on "virtual twins" and AI integration. Management expects EUR 50-100M in AI revenue in 2026. The installed base of 300,000+ companies using CATIA/SOLIDWORKS creates massive switching costs -- you cannot rip out a PLM system in months. But the mitigant depends on Dassault LEADING in AI, not just defending.

- **Kill condition?:** NO -- but should be a monitoring condition. If AI competitors demonstrate a viable PLM/CAD product at 50%+ lower cost within 2 years, that would become a kill condition.

---

### 3. Value Trap Risk at "Optically Cheap" Valuation

- **Categoria:** Valoracion
- **Descripcion:** At EUR 17.77, DSY trades at 20.4x IFRS P/E and ~13.5x non-IFRS P/E. For a company with 83% gross margins, 16% ROIC, and net cash, this looks optically cheap. But the market may be RIGHT: if growth has structurally slowed to 3-4% and the cloud transition drags on for years, this is not cheap -- it is fairly valued or even expensive for what is essentially a European software utility.

- **Evidence:**
  - Revenue CAGR of only 3.2% over the last 3 years
  - EPS CAGR of 8.6% (but FY2026 guide is FLAT EPS)
  - FY2026 EPS guide EUR 1.30-1.34 vs FY2025 actual EUR 1.31 = 0% growth in EPS
  - 3DEXPERIENCE (the growth engine) declined 3% in Q4
  - Life Sciences / Medidata acquisition (EUR 5.8B in 2019) has been a value destroyer -- Life Sciences revenue down 6% FY2025
  - No clear catalyst for re-acceleration in the next 12 months
  - Management says "2026 is a year of execution" but Q4 2025 execution was poor
  - Yahoo Finance article asks: "Is Dassault Systemes fairly priced or a value trap?"

- **Probabilidad:** Alta -- The combination of (a) no near-term catalyst, (b) flat EPS guidance, (c) damaged management credibility after missing Q4, and (d) sector-wide AI fear creates a high probability that the stock remains "dead money" for 12-24 months even if fundamentals are stable.

- **Impacto si materializa:** Opportunity cost of 12-24 months of dead money. In a portfolio targeting Tier A quality compounders, capital locked in DSY cannot be deployed elsewhere. If the stock drifts to EUR 14-16 (another 10-20% downside to test support), the intermediate-term loss would be material.

- **Mitigante:** Price is near 52-week low (EUR 17.16). The company has EUR 1.3B net cash and generates EUR 1.5B FCF annually. If management stabilizes growth at 4-5% and AI fears fade, re-rating to 20x non-IFRS EPS = EUR 26-27 (45% upside). But this requires EVIDENCE of growth stabilization, which we do not have today.

- **Kill condition?:** YES -- If two consecutive quarters of negative revenue growth (not just deceleration but actual contraction), this confirms the value trap. Exit immediately.

---

## Additional Risk Details

### 4. Medidata / Life Sciences Secular Decline

- Life Sciences software revenue declined 6% in FY2025, down 4% in Q4
- Medidata specifically declined 7% in Q4 recurring revenue
- Medidata acquired for EUR 5.8B in 2019 -- inflation-adjusted growth has been "very modest" over 5 years
- Root cause: pharmaceutical companies cutting back on clinical study starts
- This is not a temporary pause -- biotech funding environment remains challenged
- Medidata represents ~15% of Dassault's total revenue, making it material
- Impairment risk on goodwill from the acquisition exists if decline continues

### 5. European Auto Sector Prolonged Weakness

- Europe represents 42% of software revenue and declined 5% in Q4
- Auto sector is Dassault's single largest vertical (CATIA was born for automotive/aerospace)
- German auto sector (VW, BMW, Mercedes) in structural crisis: EV transition costs, Chinese competition, tariff uncertainty
- Aerospace is partially offsetting (Airbus orders), but not enough
- Recovery timeline unclear: German GDP growth projected only 1.0-1.4% in 2026

### 6. Siemens Competitive Threat

- Siemens acquired Altair Engineering for USD 10B (March 2025) -- massive bolstering of simulation capabilities
- Siemens acquired Dotmatics for USD 5.1B (July 2025) -- expanding into Life Sciences (directly targeting Dassault's Medidata)
- ABI Research named Siemens Teamcenter the #1 PLM software for large discrete manufacturers (above Dassault)
- Siemens Xcelerator platform gaining traction with AI-powered autonomous agents
- PTC also competitive in MBSE (Model-Based Systems Engineering)
- Autodesk Fusion 360 pressuring SOLIDWORKS from below with cloud-native, AI-assisted design

### 7. Data Breach (Feb 3, 2026)

- Dassault Systemes breached by threat actor "0APT" on Feb 3, 2026
- Scope of leak unknown -- but timing is terrible (1 week before earnings crash)
- Dassault provides software to defense customers including Naval Group (French submarines)
- Naval Group also suffered a separate major cyberattack -- source code for combat management systems allegedly leaked
- Defense customers may demand additional security assurance or diversify software suppliers
- Regulatory scrutiny possible under EU NIS2 Directive

### 8. IFRS vs Non-IFRS Earnings Gap

- IFRS EPS: EUR 0.87, Non-IFRS EPS: EUR 1.31 -- gap of EUR 0.44 (50.5%)
- Non-IFRS adjustments for FY2026 estimated at:
  - Stock-based compensation: EUR 116M
  - Amortization of acquired intangibles: EUR 313M (mostly Medidata)
  - Total adjustments: ~EUR 429M
- This is a REAL cost. SBC dilutes shareholders. Amortization reflects the ongoing cost of the Medidata acquisition.
- At IFRS P/E of 20.4x, the stock is not cheap for a 0-4% grower
- Risk: investors may increasingly focus on IFRS earnings as "accounting reality"

---

## Riesgos NO Mencionados en Thesis

No thesis exists for DSY.PA yet. However, the following risks are typically underappreciated by bullish narratives:

| Riesgo | Severidad | Commonly Overlooked? | Comentario |
|--------|-----------|---------------------|------------|
| 3DEXPERIENCE declining (-3% Q4) | HIGH | YES | The flagship growth product is shrinking |
| Medidata as value destroyer (EUR 5.8B for declining business) | HIGH | YES | M&A track record questionable |
| Short interest +427% | MEDIUM | YES | Smart money positioning for further downside |
| Data breach by 0APT (Feb 3, 2026) | HIGH | YES | Not widely discussed; defense customer risk |
| IFRS EPS only EUR 0.87 (P/E 20.4x) on IFRS basis | MEDIUM | YES | Non-IFRS flatters picture |
| ARR growth only 6% (SaaS underperformance) | HIGH | YES | For a cloud transition company, 6% ARR growth is poor |
| No clear near-term catalyst | HIGH | YES | Management credibility damaged |
| Siemens EUR 15B in acquisitions (Altair + Dotmatics) | HIGH | YES | Directly targeting Dassault's positions |
| Controlled company (GIMD ~40-48%) | LOW | Sometimes | Double voting rights give family ~52-57% voting control |

---

## Kill Conditions Sugeridas

1. **Two consecutive quarters of negative revenue growth (not deceleration, actual contraction)** -- Confirms structural decline, not cyclical weakness. EXIT immediately.

2. **FY2026 actual revenue growth <3% (below bottom of guidance)** -- Second consecutive year of disappointing vs own guidance would confirm management cannot forecast their own business. EXIT or TRIM 50%.

3. **Medidata goodwill impairment charge** -- Would confirm the EUR 5.8B acquisition was a value-destroying deal. Review thesis fundamentally.

4. **Loss of a Top 5 automotive customer to Siemens Xcelerator** -- VW already uses 3DEXPERIENCE, but if VW/Audi/Porsche defect to Siemens, it signals moat erosion. EXIT or TRIM.

5. **AI competitor demonstrates viable PLM/CAD product at 50%+ lower cost** -- Would break the pricing power assumption. HARD EXIT.

6. **Data breach escalation: defense customer loss or regulatory fine >EUR 50M** -- Would damage the trust that is core to Dassault's enterprise relationships.

---

## Riesgo Agregado

- **Numero de riesgos HIGH+CRITICAL:** 7 (2 CRITICAL + 5 HIGH)
- **Riesgos correlacionados?** YES -- Risks 1, 4, 5, and 10 are correlated. European manufacturing weakness (auto, industrial) drives both revenue deceleration AND competitive pressure from Siemens. If Europe enters deeper recession, all four risks compound simultaneously.
- **AI disruption risk (Risk 2) amplifies Risk 8 (value trap):** Even if AI doesn't actually disrupt PLM in 5 years, the FEAR keeps the multiple compressed, creating dead money.
- **Risk Score Final: HIGH**

**Rationale:** 7 HIGH/CRITICAL risks is well above the threshold for HIGH. Two risks are CRITICAL (structural deceleration + value trap). Multiple risks are correlated (European macro weakness compounds across auto, manufacturing, and competitive dynamics). The data breach adds an idiosyncratic risk that hasn't been priced in. While the balance sheet is strong (net cash, EUR 1.5B FCF), the growth and competitive profile present material uncertainty that makes timing an entry extremely difficult.

---

## Quantitative Risk-Adjusted Valuation Range

**Bull Case (P=20%):** Growth recovers to 5-6%, AI fears fade, multiple re-rates to 25x non-IFRS EPS
- FV: EUR 1.35 x 25 = EUR 33.75 (90% upside)

**Base Case (P=50%):** Growth stabilizes at 3-4%, multiple stays 15-18x non-IFRS EPS
- FV: EUR 1.32 x 16.5 = EUR 21.78 (22% upside)

**Bear Case (P=30%):** Growth stalls at 1-2%, AI disruption narrative intensifies, multiple compresses to 12-14x
- FV: EUR 1.25 x 13 = EUR 16.25 (8.5% downside)

**Probability-weighted FV:** (0.20 x 33.75) + (0.50 x 21.78) + (0.30 x 16.25) = EUR 22.51

**MoS at EUR 17.77:** ~21% to probability-weighted FV

**Note:** This MoS is modest given the HIGH risk score and 7 material risks. For a Tier B (QS 70) company with this risk profile, our framework suggests MoS should be 25-30% or higher. The current price does NOT provide sufficient margin of safety for immediate purchase.

---

## 🔄 META-REFLECTION

### Dudas/Incertidumbres
- **Cloud transition timeline:** I cannot determine with confidence when the cloud transition inflection point occurs. Management has been saying "next year" for 2-3 years. The 6% ARR growth rate is concerning but could be a lagging indicator.
- **AI disruption vs AI opportunity:** Dassault's partnership with NVIDIA could be genuine upside (virtual twins + AI), or it could be defensive positioning. I cannot reliably assess whether Dassault will be an AI winner or loser.
- **Data breach severity:** The 0APT breach (Feb 3, 2026) scope is unknown. If it involved defense customer data, the consequences could be severe. If it was limited, it may be noise. I could not find enough detail to assess.
- **Automotive vertical detail:** I estimate auto is ~20-25% of industrial innovation revenue but Dassault does not break out exact industry percentages granularly. The actual exposure could be higher.
- **China exposure:** Revenue from Asia is 21% (of which ~12% is estimated as China). If US-China tensions escalate and Dassault's dual-use software falls under expanded export controls, this revenue could be at risk.

### Riesgos que Podrian Estar Subestimados
- **Medidata value destruction:** I classified this as HIGH but it could be CRITICAL. EUR 5.8B spent on a business declining 6% annually = massive capital misallocation. If this trend continues for 2-3 more years, the write-off potential is significant.
- **Siemens competitive threat:** Siemens spent EUR 15B on Altair + Dotmatics in 2025 alone. This is a deliberate assault on Dassault's two key markets (industrial simulation + life sciences). I may be underestimating the medium-term competitive impact.
- **Data breach:** Classified as HIGH but if it involved defense-grade data, it could be CRITICAL. The timing (Feb 3) just before the earnings crash (Feb 11) is suspicious -- market may not have fully digested this.

### Discrepancias con Thesis
- No thesis exists. This risk assessment should inform any future thesis by ensuring the analyst addresses ALL risks identified here before establishing a buy case.

### Sugerencias para el Sistema
1. **Sector view needed:** If DSY.PA proceeds to fundamental analysis, a `world/sectors/enterprise-software.md` or `world/sectors/technology-plm.md` should be created first. This is a specialized niche within technology.
2. **AI disruption monitoring:** The system should add a periodic check for "AI disruption to software" as a macro-level risk in `world/current_view.md`. This affects multiple potential investments (SAP, Dassault, Temenos, Sage, etc.).
3. **Breach monitoring:** The data breach risk should be added to risk-sentinel's watch list if DSY.PA enters the pipeline.

### Preguntas para Orchestrator
1. Given 7 HIGH/CRITICAL risks and only ~21% MoS to probability-weighted FV, does DSY.PA meet the bar for Tier B quality (QS 70) with sufficient MoS? Historical precedent for Tier B suggests 20-25% MoS minimum.
2. Should we wait for Q1 2026 results (likely April-May) to see if growth stabilizes before considering an entry? The risk of catching a falling knife is material.
3. Is the -56% from 52-week high sufficient to account for the structural risks, or is this a NVO-like opportunity where the market overreacted? Key difference: NVO had a clear catalyst (CagriSema data) while DSY has no near-term catalyst.
4. The data breach on Feb 3 needs monitoring. Should this be added to risk-sentinel's weekly scan?

---

**Assessment completed: 2026-02-11**
**Risk Identifier Agent (independent of fundamental-analyst)**
**QS Tool: 70/100 (Tier B)**
**Price: EUR 17.77 | 52wH: EUR 40.76 | 52wL: EUR 17.16**
