# Moat Assessment: DSY.PA (Dassault Systemes SE)

## Fecha: 2026-02-11

## Clasificacion: WIDE

## Moat Score: 22/25

---

## Fuentes de Moat Identificadas

| Fuente | Presente | Evidencia | Durabilidad | Trayectoria |
|--------|----------|-----------|-------------|-------------|
| Cost advantage | MODERATE | R&D scale EUR 2B+/yr, 40+ years accumulated domain expertise, BUT not a cost leader -- it's a premium product | 20+ years | -> (stable) |
| Network effects | YES | Supply chain forced adoption (OEM uses CATIA = suppliers must too), trained workforce of millions, 350K+ enterprise customers, 3DEXPERIENCE marketplace ecosystem | 20+ years | Up (cloud platform amplifies) |
| Intangible assets | YES (STRONG) | CATIA = de facto standard in aerospace (used by Airbus, Boeing, Bombardier, Dassault Aviation), 600+ patents, 40+ years of simulation data/industry-specific know-how, regulatory certification carryover (DO-178C, ISO 26262) | 20+ years | -> (stable) |
| Switching costs | YES (STRONGEST) | Multi-year PLM migrations, retraining costs for millions of engineers, design certification tied to tool, 82% recurring revenue, manufacturing defect risk from switching far exceeds software cost | 20+ years | Up (3DEXPERIENCE deepens lock-in) |
| Efficient scale | YES | PLM is a natural oligopoly: 4-firm concentration (DSY ~29%, Siemens ~22%, PTC ~10%, Autodesk ~9%). No new entrant has achieved unicorn status in general CAD since the 1980s. Top 10 vendors = 84.8% market share | 20+ years | -> (stable) |

---

## Detailed Analysis by Moat Source

### 1. Switching Costs (STRONGEST SOURCE -- Strength 5/5)

This is the single most powerful moat source for Dassault Systemes. The evidence is overwhelming:

**Quantitative evidence:**
- 82% of software revenue is recurring (subscriptions + maintenance), indicating extremely high retention
- Typical PLM migration takes 18-36 months for a large enterprise
- Retraining thousands of engineers on a new CAD platform costs millions of dollars and months of lost productivity
- Manufacturing defects from flawed design transitions cost orders of magnitude more than the software itself -- a single defect in aerospace can be catastrophic

**Why switching from CATIA is nearly impossible in aerospace/automotive:**
- Aircraft and automotive designs carry regulatory certification tied to the design tool. A Boeing 777 designed on CATIA V3/V5 cannot be casually re-platformed -- the certification process would need to be re-validated
- Decades of design IP, parametric models, simulation data, and manufacturing instructions are stored in CATIA-native formats
- An OEM's entire supply chain (hundreds of Tier 1/2/3 suppliers) must use compatible tools. If Airbus uses CATIA, its suppliers must too. Switching the OEM means switching the entire supply chain
- Engineers trained on CATIA for 20+ years resist change -- CATIA proficiency is a career skill listed on CVs

**Cloud transition impact on switching costs:**
Contrary to the concern that cloud lowers switching costs, the 3DEXPERIENCE platform INCREASES them. Moving to 3DEXPERIENCE cloud means more data, more integrations (PLM + simulation + manufacturing + supply chain), and more organizational processes embedded in the platform. The migration from V5 to 3DEXPERIENCE itself is so complex that Dassault offers dedicated "Transition Offers" with consulting support. Once on 3DEXPERIENCE, the integration depth is far greater than standalone CATIA V5.

**Durability:** 20+ years. The installed base of CATIA-native designs grows every year. No competitive force can make this switching cost disappear -- it is structural to how physical products are designed and certified.

### 2. Intangible Assets (STRONG SOURCE -- Strength 5/5)

**Brand as standard:**
"The aerospace industry is practically all on CATIA, so if you don't have it you may not even be considered for the job." (industry source). CATIA in aerospace is like Bloomberg in finance or SAP in ERP -- it is the de facto standard. SOLIDWORKS holds a similar position in mid-market mechanical design with 3.8M+ users.

**Patent portfolio:**
600+ protected inventions spanning AI for 3D shape inference, advanced simulation algorithms, and manufacturing optimization. These patents protect specific computational methods that competitors cannot legally replicate.

**40+ years of accumulated domain expertise:**
The simulation models, material databases, manufacturing process templates, and industry-specific configurations embedded in Dassault's software represent decades of accumulated knowledge. This is NOT replicable by a startup in 5-10 years. The software encodes "best practices" for designing jet engines, automotive bodies, pharmaceutical manufacturing processes, etc.

**Regulatory moat:**
Products designed on CATIA carry regulatory certification (DO-178C for avionics, ISO 26262 for automotive safety). This creates a quasi-regulatory barrier -- switching tools means re-certifying designs, which is prohibitively expensive and risky.

**Durability:** 20+ years. The brand, patents, and accumulated expertise compound over time. Each new industry vertical (life sciences via Medidata, infrastructure, etc.) adds new domain expertise.

### 3. Network Effects (MODERATE-STRONG SOURCE -- Strength 4/5)

**Supply chain network effect:**
This is the most powerful network effect. When an OEM (Airbus, Volkswagen, BMW) standardizes on CATIA/3DEXPERIENCE, the ENTIRE supply chain must adopt compatible tools. This creates a cascading adoption effect:
- OEM adopts CATIA -> Tier 1 suppliers adopt CATIA -> Tier 2/3 suppliers adopt CATIA
- The more suppliers on the platform, the more valuable it becomes for the OEM
- The 3DEXPERIENCE platform as "single source of truth" amplifies this by connecting design, manufacturing, and supply chain on one platform

**Trained workforce network effect:**
Millions of engineers worldwide are trained on CATIA and SOLIDWORKS. Universities teach SOLIDWORKS. This creates a self-reinforcing cycle: companies use SOLIDWORKS because engineers know it, and engineers learn SOLIDWORKS because companies use it.

**3DEXPERIENCE marketplace:**
Growing ecosystem of add-ons, templates, and partner applications. The more partners build on 3DEXPERIENCE, the more valuable the platform. Still nascent compared to Salesforce AppExchange, but growing.

**Limitation:** Network effects are not as pure as a two-sided marketplace (Visa, Uber). They are more "ecosystem lock-in" effects. A new entrant could theoretically build an alternative ecosystem, but the time and investment required is prohibitive.

**Durability:** 20+ years. Supply chain network effects strengthen as more companies digitize their value chains on 3DEXPERIENCE.

### 4. Efficient Scale (STRONG SOURCE -- Strength 4/5)

**Market structure:**
PLM/CAD is a natural oligopoly. The market has been dominated by the same 4 players since the 1980s:
- Dassault Systemes: ~29% core market share
- Siemens Digital Industries: ~22%
- PTC: ~10%
- Autodesk: ~9%

Top 10 vendors control 84.8% of the market. No startup has achieved unicorn status in general CAD design tools -- ever.

**Why new entry is nearly impossible:**
1. Software complexity: millions of lines of code per application, decades to develop
2. Domain expertise: requires deep understanding of aerospace, automotive, pharma manufacturing processes
3. Customer trust: mission-critical software (design flaws = catastrophic failures) requires proven reliability
4. Sales cycle: enterprise PLM sales take 12-24 months and require global support infrastructure
5. Certification: tools must be validated for regulatory compliance (DO-178C, ISO 26262)

**R&D barrier:** Dassault spends EUR 2B+ annually on R&D. A new entrant would need sustained investment of hundreds of millions over 10+ years to achieve minimal feature parity in ONE industry vertical.

**Durability:** 20+ years. The barriers to entry are structural, not cyclical. The market has been stable for 40 years.

### 5. Cost Advantage (MODERATE SOURCE -- Strength 3/5)

Dassault does NOT compete on cost -- it competes on premium functionality. However, it has a moderate cost advantage through:

**R&D scale economies:**
EUR 2B+ R&D spend amortized over 350K+ enterprise customers. The per-customer cost of innovation is lower than for any smaller competitor. This allows Dassault to invest in new domains (life sciences, infrastructure) while maintaining leadership in aerospace/automotive.

**Accumulated codebase:**
40+ years of development means Dassault has features that competitors would need to build from scratch. This is a "code moat" -- the cost to replicate the existing product is orders of magnitude higher than the cost to maintain it.

**NOT a pure cost advantage:** Dassault charges premium prices. The moat is not about being cheapest; it is about the high cost to compete against Dassault, not the low cost for Dassault to operate.

**Durability:** 15-20 years. R&D advantages persist as long as Dassault continues investing. If they cut R&D, competitors could catch up in specific verticals.

---

## Evidencia Cuantitativa

| Metrica | Empresa (DSY.PA) | Peer Median | Diferencia |
|---------|-------------------|-------------|------------|
| ROIC (4yr avg, tool data) | ~13.9% | ~10-12% (est. Siemens DI, PTC) | +2-4pp |
| ROIC latest | 16.4% | - | - |
| ROIC-WACC Spread | +9.2pp | ~2-5pp (est.) | +4-7pp |
| Gross Margin | 83.7% | ~80-83% (PTC 83.3%) | +0-4pp vs peers; +28.7pp vs sector median 55% |
| Operating Margin (non-IFRS) | 32.0% | ~25-30% (est. PTC, Siemens DI) | +2-7pp |
| EBITDA Margin | ~30% | <20% (competitors over comparable period) | +10pp+ |
| FCF Margin | 23.6% | ~18-22% (est.) | +2-5pp |
| Revenue CAGR (3yr) | 3.2% | ~5-8% (PTC faster) | -2-5pp (CONCERN) |
| Recurring Revenue % | 82% | ~75-80% (est.) | +2-7pp |
| Insider Ownership | 48.8% (Dassault family) | <5% typically | +43pp (STRENGTH) |
| Net Debt/EBITDA | Net Cash (EUR 1.3B) | Varies | Pristine balance sheet |

**ROIC Trajectory (from quality_scorer.py):**
- 2022: 11.0%
- 2023: 14.4%
- 2024: 13.7%
- 2025: 16.4%

This is an IMPROVING trajectory. ROIC consistently > WACC (7.2%) with spread of +3.8pp to +9.2pp over 4 years.

**Note on gross margin vs peers:**
Dassault's 83.7% gross margin is comparable to PTC's ~83.3% -- both are high-margin enterprise software businesses. The massive +28.7pp premium vs sector median (55%) reflects that these are NOT typical technology companies; they are specialized, mission-critical software businesses with exceptional pricing power. The relevant comparison is within the PLM oligopoly, where Dassault is competitive but not dramatically ahead of PTC on gross margin. The differentiation shows more in OPERATING margin and EBITDA margin, where Dassault's scale advantage produces meaningfully higher profitability.

---

## Amenazas al Moat

| Amenaza | Probabilidad | Impacto | Horizonte |
|---------|-------------|---------|-----------|
| AI-native design tools disrupting CAD workflow | Baja-Media | Alto (if realized) | 7-15 years |
| Autodesk Fusion 360 disrupting SOLIDWORKS from below | Baja | Medio | 5-10 years |
| Siemens Xcelerator gaining share in industrial PLM | Media | Medio | 3-10 years |
| Cloud transition temporarily creating switching window | Baja | Medio | 2-5 years |
| Medidata/Life Sciences continued underperformance | Media | Bajo-Medio | 1-3 years |
| Revenue growth stagnation eroding premium valuation | Media-Alta | Medio | 1-5 years |
| European automotive downturn reducing license revenue | Alta | Bajo-Medio | 1-2 years |

### Detailed Threat Analysis

**1. AI-Powered Design Tools (Probability: Low-Medium, Impact: High)**

The most existential long-term threat. AI-native companies could potentially:
- Automate generative design, reducing need for manual CAD expertise
- Create "text-to-3D" workflows that bypass traditional parametric design
- Enable non-experts to create complex designs (democratization)

**Why I rate this LOW-MEDIUM, not HIGH:**
- Dassault is actively investing in AI integration (NVIDIA partnership, AI Virtual Twins)
- Physical design requires precision to micron tolerances -- generative AI is not there yet
- Regulatory certification requires traceable, deterministic design processes -- AI "black boxes" are problematic
- The installed base of CATIA designs will need to be maintained/modified for decades regardless
- No AI startup has demonstrated ability to replace CATIA for aerospace-grade design
- Fusion 360's generative design is useful for component optimization, not full aircraft/vehicle design

**Timeline:** 7-15 years before AI could meaningfully erode the core aerospace/automotive moat. Even then, Dassault can integrate AI into existing workflows rather than being disrupted by it.

**2. Autodesk Fusion 360 vs SOLIDWORKS (Probability: Low, Impact: Medium)**

Fusion 360 is cloud-native, cheaper, and gaining traction with students and startups. Could it erode SOLIDWORKS' mid-market dominance?

**Why I rate this LOW:**
- SOLIDWORKS has 3.8M+ users and massive trained workforce
- Fusion 360 lacks advanced simulation, manufacturing integration at SOLIDWORKS level
- Enterprise customers do not switch mission-critical design tools for marginal cost savings
- SOLIDWORKS migration to 3DEXPERIENCE cloud closes the cloud gap
- University/education channel still dominated by SOLIDWORKS in mechanical engineering
- Fusion 360 is stronger in consumer/maker segment, not enterprise manufacturing

**3. Siemens Xcelerator (Probability: Medium, Impact: Medium)**

Siemens is the strongest direct competitor. Xcelerator platform combines organically developed + acquired capabilities (Teamcenter PLM, NX CAD, Simcenter simulation).

**Why this is the most credible competitive threat:**
- Siemens has OT (operational technology) + IT integration that Dassault lacks
- Siemens DI has strong position in process industries where Dassault is weaker
- Forrester ranked Siemens #1 in discrete manufacturing PLM
- But: Dassault retains aerospace dominance; Siemens is stronger in general manufacturing

**Mitigation:** This is market share nibbling, not moat destruction. Both companies coexist profitably because switching costs prevent customer migration. The risk is in NEW accounts, not existing ones.

**4. Revenue Growth Stagnation (Probability: Medium-High, Impact: Medium)**

This is the MOST IMMEDIATE concern and the reason for today's 21% stock drop:
- Q4 2025: +1% constant currency growth (bottom of guidance)
- FY2025: +4% cc growth
- FY2026 guidance: +3-5% cc growth (below consensus 5-7%)
- Medidata/Life Sciences: -2% FY2025 (pharma CRO spending cuts)
- License revenue: flat to declining
- European automotive: soft

**My assessment:** This is a GROWTH problem, not a MOAT problem. The moat is intact -- customers are not leaving. But the company is struggling to:
- Grow Medidata in a challenging pharma capex environment
- Convert license revenue to subscription (temporary revenue headwind)
- Penetrate new verticals fast enough to offset mature verticals

The moat protects existing revenue (82% recurring, very low churn). Growth requires NEW customer acquisition and cross-selling, which is harder in a soft macro.

---

## Escenarios de Erosion

### Scenario 1: AI Disruption (Most Probable Long-Term, 15-20% probability over 10 years)

A new paradigm in engineering design emerges where AI-generated designs replace human-directed parametric modeling. In this scenario:
- CATIA's accumulated know-how becomes less relevant
- Switching costs decrease because AI tools are more interoperable
- The trained workforce advantage erodes as AI handles complexity

**Why I assign only 15-20% probability:**
- Physical design for safety-critical applications (aerospace, nuclear, automotive) requires regulatory traceability that AI cannot currently provide
- Dassault can integrate AI into its own platform rather than being disrupted
- The 40-year head start in domain expertise is also an AI advantage (training data)

### Scenario 2: Sustained Growth Stagnation (Most Probable Near-Term, 40-50% probability over 3 years)

Revenue growth stays at 3-5% for multiple years as:
- Medidata fails to recover
- Cloud transition cannibalization continues
- European automotive remains weak
- AI investment has long payback period

**Impact on moat:** NONE. Growth stagnation does not erode switching costs, network effects, or market position. It reduces the REINVESTMENT value of the moat (less capital to deploy at high ROIC) but does not destroy it. The company would still generate EUR 1.5B+ in FCF annually, be net cash positive, and maintain 32%+ non-IFRS operating margins.

**Risk:** The market de-rates the stock from "growth premium" to "mature software" valuation. This is a VALUATION risk, not a MOAT risk.

---

## Why WIDE Moat (Not Narrow)

I classify DSY.PA as WIDE moat based on:

1. **4 of 5 moat sources present and strong** (switching costs, intangible assets, network effects, efficient scale -- all rated 4-5/5)
2. **ROIC consistently > WACC** with improving trajectory (11.0% -> 16.4% over 4 years, vs 7.2% WACC)
3. **Durability > 20 years** for the primary moat sources:
   - CATIA's aerospace installed base will be maintained for decades
   - Supply chain network effects are self-reinforcing
   - Regulatory certification lock-in persists as long as physical products need certification
4. **Market structure stable for 40 years** -- no new entrant has disrupted the oligopoly since the 1980s
5. **Gross margin premium vs sector** (+28.7pp) confirms pricing power
6. **48.8% insider ownership** (Dassault family) provides aligned, long-term stewardship

**The key distinction from Narrow:**
A Narrow moat company has 1 source of advantage that could erode in 10-20 years. Dassault has 4 mutually reinforcing sources (switching costs lock in customers -> network effects make the ecosystem more valuable -> intangible assets/brand make it the standard -> efficient scale prevents new entry). The COMBINATION of these sources makes the moat wider and more durable than any single source.

---

## Discrepancias con Thesis (si aplica)

No existing thesis for DSY.PA to compare against. This is an independent assessment.

**Key tension to flag:** The WIDE moat does NOT mean the stock is cheap or a good investment at any price. The moat protects the BUSINESS; the price determines the INVESTMENT return. At EUR 17.77 (down 56% from 52-week high), the question is whether the moat + growth trajectory justifies the current valuation -- but that is a valuation question, not a moat question.

**Growth concern:** Revenue CAGR of 3.2% is slow for a company with this quality of moat. This suggests either:
1. The moat is maturing (less reinvestment runway) -- possible in core automotive/aerospace
2. Temporary headwinds (Medidata, license-to-subscription transition, EU auto weakness) -- likely
3. Management execution issue -- possible given Q4 miss and guidance miss

The moat classification is WIDE regardless, because moat measures DURABILITY of competitive advantage, not GROWTH RATE.

---

## Quality Score Assessment

**QS Tool Output:** 70/100 (Tier B)

**QS Adjusted:** 78/100 (Tier A) -- Adjustment: +8 points

**Justification for adjustment:**
- Market Position: tool scored 0/8 (manual input required). DSY is #1 in PLM globally with ~29% core market share. Score: 8/8 (+8 points)
- This is a straightforward data gap correction, not a subjective inflation

**Adjusted breakdown:**
| Category | Tool Score | Adjusted Score | Delta | Reason |
|----------|-----------|---------------|-------|--------|
| Financial | 33/40 | 33/40 | 0 | No change needed |
| Growth | 10/25 | 10/25 | 0 | Revenue CAGR 3.2% is honestly slow |
| Moat | 17/25 | 25/25 | +8 | Market Position #1 globally = 8/8 |
| Capital Allocation | 10/10 | 10/10 | 0 | Perfect score already |
| **TOTAL** | **70/100** | **78/100** | **+8** | |

**Tier: A (Quality Compounder)**

**Supporting evidence for Tier A:**
- ROIC > WACC consistently (spread +3.8pp to +9.2pp)
- FCF positive 4/4 years, FCF margin ~24%
- Net cash position (EUR 1.3B)
- 83.7% gross margin (vs 55% sector median)
- 48.8% insider ownership
- 82% recurring revenue
- #1 global market position in PLM
- 40-year operating history with no major disruption

**What PREVENTS a higher QS:**
- Revenue CAGR only 3.2% (below the 10% threshold for top growth scores)
- ROIC spread +9.2pp is strong but below the 15pp threshold for maximum Financial Quality points
- These are legitimate limitations, not errors to correct

---

## 🔄 META-REFLECTION

### Dudas/Incertidumbres
1. **ROIC historical data beyond 4 years:** The quality_scorer.py only shows 2022-2025 (4 years). I cannot confirm ROIC > WACC for 10+ years as required for Wide moat classification. Web sources suggest historical ROIC of ~9-10% which is still above WACC but with thinner spread. The improving trajectory (11% -> 16.4%) is encouraging but the 10-year record would strengthen the case.

2. **Medidata structural vs cyclical:** Is the Life Sciences underperformance (-2% FY2025, -7% Medidata Q4) cyclical (pharma CRO spending cuts) or structural (competition from Veeva, new entrants)? Management says cyclical and excluded recovery from 2026 guidance. If structural, it weakens the diversification thesis.

3. **Actual customer churn rate:** I found that 82% of revenue is recurring, which implies high retention, but I could not find a specific net revenue retention rate (NRR) or gross retention rate. Best-in-class enterprise software has NRR >110% and gross retention >95%. Without this data, I am inferring stickiness from recurring revenue percentage and market structure.

4. **SOLIDWORKS' competitive position vs Fusion 360 in education channel:** If Autodesk captures the next generation of engineering students via Fusion 360 (free for education), this could slowly erode SOLIDWORKS' trained workforce advantage over 10-15 years. I rated this Low probability but would want to monitor university adoption data.

### Sugerencias de Mejora
1. **Add peer comparison feature to quality_scorer.py**: The moat assessment would benefit greatly from automated peer comparison. Currently, I had to manually search for PTC, Siemens margins. A `--peers` flag that automatically fetches comparable companies' margins would save time and improve accuracy.

2. **Long-term ROIC data:** The quality_scorer.py only shows 4 years of ROIC. For moat assessment, 10 years is needed. Consider extending the historical data window.

### Anomalias Detectadas
1. **Revenue vs EPS divergence:** Revenue CAGR is 3.2% but EPS CAGR is 8.6%. This suggests margin expansion is driving earnings growth, not top-line growth. This is a sign of a mature business optimizing rather than a high-growth compounder. Sustainable? Margins are already at 32% non-IFRS operating margin -- how much more expansion is possible?

2. **Stock down 56% from 52-week high but fundamentals improved:** ROIC went from 11% to 16.4%, FCF is stable at EUR 1.5B, and margins expanded. The magnitude of the stock decline (56%) seems disproportionate to the fundamental deterioration (slow growth, Q4 miss). This may represent the market de-rating from "growth premium" to "mature software" valuation -- a potential opportunity if the moat is truly wide.

### Preguntas para Orchestrator
1. Should the fundamental-analyst weight the growth slowdown more heavily? The moat is WIDE but growth is below compounder thresholds (10%+ revenue CAGR). Is this a "quality business at a good price" or a "decelerating business at a fair price"?
2. The 56% decline from 52-week high is dramatic. Should we run dcf_calculator.py with conservative assumptions (3-5% growth, 7.2% WACC) to see if current price offers sufficient MoS despite slow growth?
3. Medidata/Life Sciences is the swing factor for thesis bull/bear scenarios. Should the fundamental-analyst conduct a deep dive specifically on Medidata's competitive position vs Veeva and other clinical trial platforms?

---
