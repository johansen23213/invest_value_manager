# Moat Assessment: QTCOM.HE (Qt Group Oyj)

## Fecha: 2026-02-18

## Clasificacion: NARROW

---

## Fuentes de Moat Identificadas

| Fuente | Presente | Evidencia | Durabilidad | Trayectoria |
|--------|----------|-----------|-------------|-------------|
| Switching costs | SI | Deep code integration in customer products (automotive HMI, medical devices, industrial). Rewriting Qt-based UI layer = months of engineering. Contract durations multi-year. Retention described as "no increase in churn" even during downturn (Q3 2025 call). | 15-20 years | -> (stable) |
| Intangible assets | SI | 30+ year framework history, de facto standard in embedded GUI. Safety certifications (automotive ISO 26262, medical IEC 62304). Brand recognition in 70+ industries. IAR acquisition adds embedded compiler IP. ~1M developer community (2017 estimate, likely larger now). | 15-20 years | -> (stable) |
| Cost advantage | PARTIAL | Dual-license model (LGPL/GPL open-source + commercial) creates unique distribution: developers learn for free, companies pay when shipping products. Very low Capex/Depreciation (0.1x). Net cash balance sheet. But gross margin 52.5% is BELOW sector median 55.0%. | 10-15 years | -> (stable) |
| Network effects | WEAK | Developer ecosystem creates mild indirect network effect: more Qt devs -> more Qt components/libraries -> more attractive for companies. But NOT a strong two-sided marketplace. No winner-take-all dynamics. Developers can learn multiple frameworks. | <10 years | -> (stable, weak) |
| Efficient scale | NO | Embedded GUI market is large (~$18B+ for embedded software broadly) and growing. Multiple viable competitors exist (LVGL, Crank Storyboard, Embedded Wizard, Flutter for embedded). No natural monopoly dynamics. | N/A | N/A |

---

## Evidencia Cuantitativa

### ROIC vs WACC (Primary Moat Indicator)

| Year | ROIC | WACC | Spread |
|------|------|------|--------|
| 2020 | 136.4% | ~13% | +123pp |
| 2021 | 72.0% | ~13% | +59pp |
| 2022 | 43.1% | ~13% | +30pp |
| 2023 | 34.8% | ~13% | +22pp |
| 2024 | 45.3% | 13.0% | +30.3pp |

**Assessment:** ROIC consistently and massively above WACC over 5 available years. The declining trend from 2020-2023 reflects normalization from a Covid-driven software spending boom, with 2024 showing recovery. Even at the trough (34.8% in 2023), ROIC was 2.7x WACC. This is strong moat evidence.

**Limitation:** Only 5 years of ROIC data available via yfinance. Pre-2020 data would strengthen the assessment. The company was listed in 2016 and was smaller/less profitable in early years.

### Margins vs Peers

| Metrica | Qt Group | Sector Median | Diferencia |
|---------|----------|---------------|------------|
| Gross Margin (2024) | 52.5% | 55.0% (Application Software) | -2.5pp |
| Operating Margin (2024) | 30.2% | N/A (varies widely) | Strong |
| FCF Margin (2024) | 25.1% | ~15-20% (typical SaaS) | +5-10pp |
| ROIC (5yr avg) | ~66% | ~15-20% (typical software) | +46-51pp |

**Note on Gross Margin:** The -2.5pp vs sector median is misleading. Qt's "sector" in yfinance includes pure SaaS companies with 70-80% gross margins. Qt has a consulting/services component that depresses gross margins. More relevant: Qt's gross margin expanded from 44.7% (2021) to 52.5% (2024) -- a +7.8pp improvement in 3 years, indicating the business is shifting toward higher-margin license/subscription revenue. The operating margin (30.2%) and FCF margin (25.1%) are excellent and better indicators of economic moat quality.

### Revenue & Growth Trajectory

| Year | Revenue (EUR M) | Growth | EPS | EPS Growth |
|------|-----------------|--------|-----|------------|
| 2021 | 121.1 | - | 0.91 | - |
| 2022 | 155.3 | 28.2% | 1.36 | +49% |
| 2023 | 180.7 | 16.4% | 1.40 | +3% |
| 2024 | 209.1 | 15.7% | 2.26 | +61% |
| 2025E | ~215-230 | 3-10% (guided) | ~1.5-2.0E | declining |

Revenue CAGR (3yr): 19.9%. EPS CAGR (3yr): 35.4%.
2025 is a clear deceleration year driven by customer cautiousness, deal postponements, and license count reductions.

### Balance Sheet

- Net cash: EUR 87M (pre-IAR acquisition)
- Total debt: EUR 7M
- Interest coverage: 252x
- Insider ownership: 29.5% (very high -- aligned incentives)
- Goodwill/Total Assets: 18.6% (declining trend, healthy)

**IAR Acquisition Impact (completed Jul 2025):** SEK 2.29B (~EUR 204M) acquisition will significantly change the balance sheet. The company will move from net cash to net debt. This is the biggest risk to the capital allocation quality.

---

## Detailed Source Analysis

### 1. Switching Costs (Score: 6/7) -- PRIMARY MOAT SOURCE

**Why it's strong:**
- Qt is deeply embedded in the source code of customer products. An automotive OEM using Qt for its infotainment system (Mercedes, BMW, Toyota) cannot rip it out without rewriting the entire UI layer -- a process taking 12-24+ months and costing millions.
- Embedded devices with safety certifications (automotive, medical) face even higher switching costs: re-certification of the entire software stack is required.
- Multi-year license agreements with large enterprise customers.
- Developer expertise is framework-specific: a team trained on Qt/QML would need retraining on any alternative.
- Q3 2025 earnings call explicitly stated "no increase in customer churn" despite downturn -- customers reduce seats but do not leave.

**Why not 7/7:**
- New projects can choose alternatives. The switching cost protects existing deployments, not future wins.
- The shift from 3-year to 1-year licenses (observed in Q3 2025) reduces contractual lock-in.
- Open-source availability means some customers can try to self-support and avoid commercial licensing (though this is difficult for embedded/safety-critical applications).

### 2. Intangible Assets (Score: 4/5) -- SECONDARY MOAT SOURCE

**Brand & Know-How:**
- Qt has been the dominant cross-platform C++ framework for 30+ years (since 1995).
- Used in "1 billion+ devices" globally across 70+ industries.
- The "Qt" brand is synonymous with cross-platform embedded UI in engineering circles.
- Safety certifications (ISO 26262, IEC 62304) are expensive and time-consuming to obtain -- this is a meaningful barrier to entry for smaller competitors.

**IAR Acquisition (2025):**
- IAR Systems adds embedded compiler technology supporting 15,000 devices from 70+ semiconductor partners.
- Extends Qt's intangible asset base into the broader MCU toolchain market.
- 40+ years of embedded toolchain expertise (IAR founded 1983).

**Why not 5/5:**
- No patents preventing competition. The framework is open-source (LGPL/GPL).
- Brand strength is limited to developer/engineering community -- not a consumer brand with pricing power.
- Certifications can be obtained by well-funded competitors given time.

### 3. Cost Advantage (Score: 2/4) -- WEAK/PARTIAL

**Dual-licensing distribution model:**
- Open-source (LGPL/GPL) acts as a massive customer acquisition funnel at zero CAC.
- Developers learn Qt for free, then companies pay when shipping commercial products.
- Very asset-light business: Capex/Depreciation = 0.1x.
- Operating leverage: margins have expanded significantly (operating margin from 23.8% to 30.2% over 3 years).

**Why only 2/4:**
- The open-source model is a double-edged sword: it also means competitors can fork the framework.
- Gross margin (52.5%) is not premium vs sector, though it's expanding.
- Smaller competitors (LVGL, Crank) can operate with even lighter cost structures.
- No structural cost advantage from scale -- Qt Group is a EUR 209M revenue company, not a scale player.

### 4. Network Effects (Score: 1/5) -- MINIMAL

- ~1M+ developer community creates some ecosystem stickiness (libraries, tutorials, forums, Stack Overflow answers).
- Qt marketplace exists but is not a significant revenue driver.
- No strong two-sided network effect. A new competitor with better technology could attract developers regardless of existing Qt ecosystem.
- Developer mindshare is NOT winner-take-all: developers commonly work with multiple frameworks.

### 5. Efficient Scale (Score: 0/4) -- NOT PRESENT

- Embedded software tools market is large ($18B+) and growing at 9.5% CAGR.
- Multiple competitors serve different segments: LVGL (free, MCU-focused), Crank (embedded HMI), Flutter (mobile-first, expanding to embedded), Electron (desktop).
- No natural monopoly characteristics.
- Market is large enough to support multiple players profitably.

---

## Moat Score: 13/25

| Source | Score | Max |
|--------|-------|-----|
| Switching Costs | 6 | 7 |
| Intangible Assets | 4 | 5 |
| Cost Advantage | 2 | 4 |
| Network Effects | 1 | 5 |
| Efficient Scale | 0 | 4 |
| **Total** | **13** | **25** |

---

## Amenazas al Moat

| Amenaza | Probabilidad | Impacto | Horizonte |
|---------|-------------|---------|-----------|
| AI code generation reduces developer tool value | Media | Medio-Alto | 3-7 years |
| LVGL gains traction in low-end embedded (free, open-source, growing fast) | Media | Medio | 5-10 years |
| Flutter/web technologies expand into embedded space | Media-Baja | Medio | 5-10 years |
| Open-source fork gains critical mass (community bypasses commercial licensing) | Baja | Alto | >10 years |
| Automotive sector prolonged downturn (EV transition disruption) | Media | Medio | 2-5 years |
| IAR acquisition integration risk / overpayment | Media | Medio | 1-3 years |
| Customer shift from multi-year to 1-year licenses (lower visibility) | Alta | Bajo-Medio | Already happening |
| Per-seat revenue pressure from developer layoffs (AI-driven) | Media-Alta | Medio | 2-5 years |

### Detailed Threat Analysis

**AI Code Generation (Most Important Long-term Threat):**
- AI coding tools (GitHub Copilot, Cursor, etc.) are already reducing developer headcount at large companies.
- Qt's revenue model is partially per-developer-seat. Fewer developers = fewer licenses needed.
- Q3 2025 management explicitly acknowledged "fewer developers due to downsizing" as a driver of reduced license counts.
- HOWEVER: Qt's moat is NOT in writing code -- it's in the runtime/rendering engine and safety-certified framework. AI can help write Qt code but cannot replace the Qt framework itself.
- Qt is also responding: launched AI Assistant with fine-tuned LLMs for QML code generation.
- **Assessment:** Per-seat revenue at risk (Medium), but the framework itself is not disrupted by AI. The threat is to the pricing model, not the product.

**LVGL (Most Important Near-term Competitive Threat):**
- LVGL is fully free/open-source (MIT license), lightweight (64KB flash, 8KB RAM), and growing rapidly.
- Targets the same embedded GUI space but at the low end (MCUs, resource-constrained devices).
- Does NOT compete head-to-head with Qt in complex embedded (automotive infotainment, medical devices).
- But could erode Qt's bottom-of-market new customer pipeline.
- **Assessment:** Threat to the bottom of the market, but Qt's safety certifications and enterprise features protect the high-value segment.

**Open-Source Fork Risk:**
- Qt's core framework is available under LGPL/GPL.
- A well-funded fork (like MariaDB from MySQL) could theoretically undermine commercial licensing.
- In practice: Qt has maintained commercial value for 25+ years despite open-source availability because embedded/safety-critical customers NEED commercial support, indemnification, and certified releases.
- **Assessment:** Low probability. The open-source model has been stable for decades.

---

## Escenarios de Erosion

### 1. Most Probable: Gradual Per-Seat Pricing Pressure (60% probability, 5-10 year horizon)
AI-driven developer productivity reduces headcount at Qt's enterprise customers by 20-40% over the next decade. Qt's per-seat licensing model means proportional revenue pressure. Qt must transition to per-device or platform-based pricing to offset. If they execute this transition (which they've already begun with distribution licensing), the moat survives. If they fail, margins compress from 30% to 15-20%.

### 2. Tail Risk: Automotive Paradigm Shift (15% probability, 5-10 year horizon)
If automotive OEMs standardize on a different UI framework (Android Automotive, Flutter Embedded, or a new framework), Qt loses its highest-value segment. Currently unlikely given certification requirements and entrenched positions, but a generational platform shift (like Android displacing Symbian in mobile) is not impossible.

### 3. Acquisition Destruction (20% probability, 1-3 year horizon)
IAR Systems acquisition at EUR 204M (66.4% premium) was expensive. If integration fails, Qt burns cash, takes goodwill impairments, and management attention is diverted from the core business during a downturn. This would not destroy the moat but would damage the financial profile significantly.

---

## Clasificacion Justification: NARROW (not Wide)

**Why NARROW, not WIDE:**
1. Only 2 strong moat sources (switching costs + intangible assets), but both have a 15-20 year durability horizon, not clearly >20 years.
2. ROIC history is excellent but only 5 years of data available -- the moat-framework requires 10+ years for Wide classification. The company was smaller and less profitable pre-2020.
3. The per-seat pricing model is under structural pressure from AI-driven developer reduction -- a clear threat to the business model if not to the product itself.
4. Gross margin is NOT premium vs sector (actually -2.5pp below median), though operating margin is strong.
5. The company is small (EUR 636M market cap, EUR 209M revenue) -- scale advantages are limited.
6. Open-source nature of the core framework means the IP is not truly proprietary. The moat comes from the ECOSYSTEM (certifications, support, tooling), not from the code itself.

**Why not NONE:**
1. ROIC consistently 2.5-10x WACC over all available years.
2. Genuine switching costs for embedded deployments (code rewrite + re-certification).
3. 30+ year track record, safety certifications, 1B+ devices deployed.
4. Customer retention remains strong even during significant downturn (Q3 2025).
5. Expanding margins (gross margin +7.8pp in 3 years, operating margin +6.4pp).

**Assessment:** Qt Group has a real but bounded competitive advantage. The switching costs and certification moat protect existing revenue streams effectively, but the company faces structural headwinds from AI-driven developer reduction and growing open-source competition at the low end. The NARROW classification reflects high confidence in a 10-15 year moat with meaningful but manageable threats beyond that.

---

## Discrepancias con Thesis (si aplica)

No existing thesis to compare against -- this is the first R1 analysis for QTCOM.HE.

---

## 🔄 META-REFLECTION

### Dudas/Incertidumbres
- **Pre-2020 ROIC data missing:** Only 5 years of ROIC available via yfinance. The company was listed in 2016 and was likely less profitable in early years (transition from Nokia era). This creates uncertainty about whether the high ROIC is structural or cyclical (post-Covid software boom). The ROIC declining trend (136% in 2020 to 35% in 2023 then recovering to 45% in 2024) is concerning -- the 2020 figure was clearly an anomaly.
- **Net Retention Rate unknown:** Qt Group does not publicly report NRR. The Q3 2025 call said "no increase in customer churn" which is qualitative, not quantitative. Without NRR data, the switching cost assessment relies on indirect evidence.
- **IAR acquisition impact unclear:** The EUR 204M acquisition will transform the balance sheet (from net cash to net debt) and change the financial profile materially. The 2024 data used in this assessment is PRE-acquisition. Post-IAR financials will look different -- potentially lower ROIC due to goodwill/intangible amortization.
- **Developer community size data is stale:** The "1 million developers" figure dates from 2017. The actual current community size is unknown.
- **Peer comparison is imprecise:** Qt's closest peers (Crank, LVGL) are private or open-source projects without public financials. The sector median comparison (Application Software) includes many dissimilar companies.

### Sugerencias de Mejora
- **Fetch Q3 2025 report directly** (PDF) for segment breakdown and customer metrics -- the earnings call transcript confirms valuable data exists but was not fully extractable.
- **Check Qt Group's 2024 Annual Report** for NRR, customer count, and distribution licensing metrics.
- **Consider creating an "embedded software" peer set** rather than using generic "Application Software" sector median. Relevant peers: Crank (private), IAR Systems (now acquired), Wind River (owned by Aptiv), Green Hills Software (private).

### Anomalias Detectadas
- **Stock at 52-week low:** Price EUR 25.06 vs 52-week high EUR 92.10. This is a 73% decline from peak. The reverse DCF implies -6.6% annual FCF decline -- extremely pessimistic given 20% revenue CAGR history.
- **P/E 15.2x for a 20% revenue grower with 30% operating margins:** This is remarkably cheap for the quality profile. The market is pricing this as if growth is permanently impaired.
- **Insider ownership 29.5% with no selling:** High insider alignment during a massive price decline is a positive signal.
- **Quality Score 80/100 (Tier A) vs 73% price decline:** This divergence warrants investigation -- is the market seeing something the QS model doesn't, or is this a genuine mispricing?

### Preguntas para Orchestrator
1. Should the IAR acquisition be modeled as a QS adjustment downward (balance sheet deterioration, integration risk) or is the pre-acquisition QS of 80 appropriate for the standalone Qt business?
2. The stock is at 52-week lows with the next earnings on Feb 26 -- should we wait for Q4 2025 results before completing the full buy-pipeline, or is this a hard gate?
3. Given the 73% price decline and QS 80 (Tier A), this appears to be a potential quality compounder at a distressed valuation. Does the orchestrator want to fast-track this through the full R1 pipeline (fundamental-analyst + risk-identifier running in parallel)?
