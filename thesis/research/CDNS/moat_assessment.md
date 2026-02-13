# Moat Assessment: CDNS (Cadence Design Systems)

## Date: 2026-02-13

## Classification: WIDE

Cadence possesses one of the widest and most durable moats in the entire technology sector, driven by the convergence of extreme switching costs, duopoly market structure, foundry certification barriers, and IP/know-how accumulation. At least 3 independent moat sources are present and expected to endure 20+ years. AI is reinforcing rather than eroding these advantages.

---

## Sources of Moat Identified

| Source | Present | Evidence | Durability | Trajectory |
|--------|---------|----------|------------|------------|
| Cost advantage | NO | Not a material moat source. CDNS competes on capability, not cost. | N/A | N/A |
| Network effects | PARTIAL | Foundry-EDA-IP ecosystem creates indirect network effects; PDK standards and foundry certifications create self-reinforcing loops. However, this is weaker than classic platform network effects. | 15-20 years | Stable (-->) |
| Intangible assets | YES | Thousands of patents, decades of process know-how, foundry certifications (TSMC, Samsung, Intel), AI optimization IP from 1,000+ tapeouts. | 25+ years | Strengthening (up) |
| Switching costs | YES | Near-100% customer retention. Multi-year qualified design flows. Engineer retraining cost. Time-to-market risk of switching. Customer lifetimes exceed 20 years. | 25+ years | Strengthening (up) |
| Efficient scale | YES | Duopoly with SNPS controlling ~70% of market. No new entrant in 30+ years. Foundry certification acts as gatekeeper. TAM insufficient to support a 4th major player at leading-edge nodes. | 20+ years | Stable (-->) |

**Total sources present:** 3 strong + 1 partial = 3.5 of 5
**Overall moat strength:** 9/10

---

## Detailed Moat Source Analysis

### 1. Switching Costs -- EXTREME (Primary Moat Source)

**Evidence:**

This is the single most powerful moat source for CDNS and the foundation of the entire duopoly.

- **Customer retention rate:** Near 100%. The industry maxim is: "Customers stop using Cadence when they go out of business, not when they switch vendors."
- **Design flow qualification:** Chip design flows take 2-3 years to qualify with foundries. These flows are built around specific EDA vendor toolchains. Switching means re-qualifying the entire flow.
- **Engineer training lock-in:** Chip design engineers train for years (often decades) on a specific vendor's tools. Tool proficiency is a career skill. Universities teach on CDNS/SNPS tools, creating vendor lock-in before engineers enter the workforce.
- **Multi-year contracts:** Typical EDA agreements span 3-5 years with automatic renewal. CDNS's $7.0B backlog (1.3x TTM revenue) represents locked-in future revenue.
- **Revenue characteristics:** 80-85% recurring (subscription + maintenance), with near-100% net retention.
- **Cost of switching:** EDA software costs are approximately half the total cost of designing a chip. The cost of failure during a tool migration (delayed tape-out, manufacturing defects) can run into hundreds of millions of dollars.
- **Empirical evidence:** No major semiconductor company has wholesale switched EDA vendors in the last 20+ years. The pattern is adding incremental tools from a second vendor, not replacing the primary vendor.

**Quantitative support:**
- Backlog: $7.0B (record)
- cRPO: $3.5B
- Revenue visibility: Among the best in all of software
- Multi-year contract renewals with embedded price escalators

**Durability: 25+ years.** Switching costs are structural -- they are embedded in the physics of chip design complexity. As chips become more complex (AI driving trillion-transistor designs by 2030), the switching costs INCREASE, not decrease. More verification steps, more IP blocks, more foundry-specific optimizations all deepen the lock-in.

**Trajectory: Strengthening.** AI chip complexity is driving more verification cycles, more IP integration, and more foundry-specific customization. Each layer of complexity adds another layer of switching cost.

---

### 2. Efficient Scale / Duopoly Structure -- EXTREME (Secondary Moat Source)

**Evidence:**

The EDA market is a textbook case of efficient scale resulting in a natural duopoly.

- **Market concentration:** CDNS (~30-36%) + SNPS (~31-38%) = ~65-74% combined. Siemens EDA (Mentor Graphics) is a distant #3 at ~13%. The remaining ~15-20% is fragmented among niche players.
- **No new entrant in 30+ years:** Despite the EDA market growing to $15-16B, no new broad-platform EDA company has emerged since the consolidation of the 1990s. Every significant startup has been acquired (typically for $100-500M) rather than achieving independent scale.
- **Foundry certification as gatekeeper:** TSMC, Samsung, and Intel maintain "EDA Alliance" programs that certify specific tools for each process node. Getting certified requires years of collaboration and significant engineering investment. Even Siemens (the #3 player) does not have complete certification coverage for TSMC's 3nm process. A startup has essentially zero chance of getting certified at leading edge.
- **R&D intensity barrier:** CDNS spends ~$1.5B annually on R&D (~30% of revenue). A new entrant would need to match this spend across multiple product categories simultaneously to offer a competitive suite.
- **IP litigation moat:** The EDA industry has a long history of patent litigation between incumbents. New entrants face "IP lawsuits and enticing acquisition offers" as described by industry observers. The cost of defending IP claims is prohibitive for startups.

**Quantitative support:**
- Top 3 market share: ~87% (HHI > 3,000 -- extremely concentrated)
- New entrants in last 30 years that survived independently: ZERO
- R&D spending: CDNS $1.5B, SNPS $2.1B (post-Ansys). Combined duopoly R&D outspend exceeds any conceivable challenger.

**Durability: 20+ years.** The duopoly structure has been stable for 3 decades and the barriers are increasing as chip complexity rises. The TAM ($15-16B) is large enough to support two dominant players profitably but not large enough to incentivize a 4th player to invest the $5-10B needed to build a competitive suite.

**Trajectory: Stable.** Siemens EDA is the only credible challenger, and it has been at ~13% for years without gaining meaningful share. Its recent IP alliance with Samsung targets a niche (foundry IP) rather than the core EDA flow. The SNPS acquisition of Ansys (2025) may slightly strengthen SNPS but does not change the duopoly dynamic.

---

### 3. Intangible Assets (IP, Know-How, Foundry Certifications) -- VERY HIGH

**Evidence:**

- **Patents:** Thousands of active patents covering design algorithms, verification methodologies, simulation techniques, and AI/ML-assisted design. These create specific barriers in every sub-category of EDA.
- **Foundry certifications:** CDNS tools are certified for leading-edge process nodes at TSMC (N3, N2), Samsung (3nm, 2nm), and Intel (18A, 18A-P). These certifications are co-developed over years with the foundries and represent a massive accumulated knowledge base.
- **AI/ML IP from 1,000+ tapeouts:** CDNS's Cerebrus AI engine has been used in over 1,000 tapeouts, generating proprietary training data that improves tool performance. This creates a data network effect where more usage = better AI = more usage.
- **ChipStack AI Super Agent (Feb 2026):** World's first agentic AI workflow for chip design and verification, with up to 10x productivity improvements. In early deployment at NVIDIA and Altera. This represents a new generation of moat -- AI-driven design tools that create additional stickiness.
- **Process Design Kit (PDK) influence:** CDNS's OpenAccess standard and PDK formats are deeply embedded in the industry. Si2, the standards body, uses Cadence-originated formats (OpenAccess, CPF), giving CDNS structural influence over industry standards.
- **IP licensing portfolio:** Tensilica DSP cores, interface IP (USB, PCIe, DDR, MIPI), and other design IP blocks are deeply embedded in thousands of chip designs. This creates additional vendor lock-in beyond the EDA tools themselves.

**Quantitative support:**
- Foundry certifications: 3 of 3 major leading-edge foundries (TSMC, Samsung, Intel)
- AI tapeouts: 1,000+
- IP revenue growing 25-28% (faster than core EDA), indicating increasing design-in dependency
- R&D spending: $1.5B/year sustaining and extending IP portfolio

**Durability: 25+ years.** Patent portfolios refresh continuously. Foundry certifications deepen with each new process node. AI training data accumulates. Know-how compounds over time. Unlike pharma patents with fixed expiry dates, EDA patents are continuously filed and existing ones are reinforced by trade secrets and process know-how.

**Trajectory: Strengthening.** The ChipStack AI acquisition and deployment adds a new layer of intangible assets. AI-assisted chip design is becoming a new battleground where CDNS's data advantage (1,000+ tapeouts) creates a virtuous cycle.

---

### 4. Network Effects -- PARTIAL / INDIRECT

**Evidence:**

CDNS does not benefit from classic platform network effects (more users = more value to all users). However, there are meaningful indirect network effects:

- **Foundry-EDA-Designer triangle:** Foundries (TSMC, Samsung, Intel) certify EDA tools. Designers choose foundry-certified tools. More designers using CDNS tools = more foundry investment in CDNS certifications = more designers choosing CDNS. This is a 3-sided indirect network effect.
- **IP ecosystem:** More chip designers using CDNS tools = more IP blocks available in CDNS format = more designers choosing CDNS for IP compatibility. The IP licensing segment (20% of revenue, growing 25-28%) is evidence of this effect.
- **PDK standards:** CDNS-originated formats (OpenAccess) being industry standard creates a soft network effect where third-party tools and IP providers build for CDNS compatibility first.
- **Engineering talent pool:** Universities teach on CDNS tools. Graduates enter the workforce with CDNS proficiency. Companies hire these graduates and standardize on CDNS. This is a labor-market network effect.

**Limitations:**
- CDNS tools do not become intrinsically better with more users in the way a social network does.
- Customers often use BOTH CDNS and SNPS tools for different parts of the design flow, which limits winner-take-all dynamics.
- The network effects are indirect and slow-acting, reinforcing the duopoly structure rather than driving market share gains.

**Quantitative support:**
- IP segment growing 25-28% (faster than core EDA), indicating ecosystem pull
- University partnerships: hundreds of universities globally use CDNS tools for teaching
- Market share has been stable (not growing dramatically), consistent with indirect rather than direct network effects

**Durability: 15-20 years.** The indirect network effects are durable because they are embedded in institutional structures (foundry alliances, university programs, IP ecosystems). However, they do not create the exponential returns-to-scale of true platform network effects.

**Trajectory: Stable.** The ecosystem is mature and self-reinforcing but not accelerating. AI may create a new data network effect (more usage = better AI), but this is nascent.

---

## Quantitative Evidence

| Metric | CDNS | Peer Median (Software) | Difference |
|--------|------|------------------------|------------|
| ROIC (4yr avg 2021-2024) | 29.4% | ~15% | +14.4pp |
| ROIC (latest 2024) | 22.4% | ~15% | +7.4pp |
| WACC | 9.8% | ~9-10% | Similar |
| ROIC-WACC Spread (4yr avg) | +19.6pp | ~5-6pp | +14pp |
| ROIC-WACC Spread (latest) | +12.6pp | ~5-6pp | +7pp |
| Gross Margin | 86.0% | 55% (sector) | +31.0pp |
| Gross Margin (vs SNPS) | 86.0% | 78%* | +8.0pp |
| FCF Margin (GAAP) | 24.1% | ~15% | +9.1pp |
| Revenue CAGR 3yr | 15.8% | ~10% | +5.8pp |
| Customer Retention | ~100% | ~90-95% | +5-10pp |

*SNPS gross margin distorted by Ansys acquisition in 2025.

### ROIC Persistence

| Year | ROIC | > WACC? |
|------|------|---------|
| 2021 | 30.6% | YES (+20.8pp) |
| 2022 | 29.8% | YES (+20.0pp) |
| 2023 | 34.9% | YES (+25.1pp) |
| 2024 | 22.4% | YES (+12.6pp) |

Tool only provides 4 years of data. Based on financial databases (GuruFocus, Roic.ai), CDNS has maintained ROIC > WACC for at least 7-10 consecutive years. The 2024 decline is attributable to BETA CAE acquisition inflating the invested capital denominator (goodwill increased from $1.5B to $2.4B), not to operational deterioration.

**Assessment:** ROIC consistently and substantially exceeds WACC, with the spread averaging ~19pp over 2021-2024. This is textbook evidence of a wide moat. Even the "compressed" 2024 spread of +12.6pp remains exceptional.

---

## Threats to the Moat

| Threat | Probability | Impact | Horizon | Assessment |
|--------|------------|--------|---------|------------|
| **Open-source EDA (OpenROAD)** | Very Low (5%) | Low | >10 years | OpenROAD has enabled 600+ tapeouts at 180nm-12nm nodes, but remains limited to academic/educational use for commercial designs. The critical gap is foundry certification at leading-edge nodes (3nm, 2nm). Efabless, the most prominent open-source EDA commercializer, shut down in March 2025 due to funding. The threat is negligible for advanced chips and minimal for legacy nodes. |
| **Siemens EDA gaining share** | Low (15%) | Low-Medium | 5-10 years | Siemens has been stuck at ~13% for years. Its recent IP alliance with Samsung targets foundry IP, not core EDA flow displacement. Even with AI-enabled EDA suites, Siemens lacks the foundry certification breadth of CDNS/SNPS at leading nodes. |
| **AI reducing chip complexity** | Extremely Low (2%) | Very High | >15 years | Current trajectory is the opposite -- AI is INCREASING chip complexity (trillion-transistor chips by 2030, multi-die chiplets, 3D stacking). AI-generated chip designs still require the same verification and manufacturing preparation tools. This threat would require a fundamental paradigm shift in computing architecture. |
| **AI democratizing chip design** | Low (10%) | Medium | 5-10 years | AI tools like ChipStack automate parts of the design flow, but they are built ON TOP of existing EDA platforms, not as replacements. CDNS is the one building these AI tools, reinforcing rather than undermining the moat. A new entrant using AI would still need foundry certification. |
| **SNPS Ansys integration strengthening competitor** | Medium (30%) | Low-Medium | 2-5 years | SNPS's $35B Ansys acquisition creates a broader simulation platform that competes with CDNS's System Design & Analysis segment. However, this primarily expands SNPS's TAM rather than eroding CDNS's existing EDA moat. CDNS's own BETA CAE acquisition and Clarity/Celsius products address the same multi-physics opportunity. |
| **China revenue loss from export controls** | Medium-High (50%) | Medium | 1-3 years | 15-20% of CDNS revenue is from China. Export controls have already restricted leading-edge tool sales. This reduces the addressable market but does not erode the moat -- it is a geopolitical revenue risk, not a competitive risk. Non-China chip design activity is accelerating as a partial offset. |
| **Customer concentration** | Low-Medium (20%) | Medium | Ongoing | CDNS does not disclose customer concentration, but the top 10 semiconductor companies likely represent 40-60% of revenue. Loss of a major customer is extremely unlikely given switching costs, but regulatory action (e.g., banning sales to a specific company/country) could impact revenue. |
| **SBC dilution eroding shareholder value** | Medium (40%) | Low-Medium | Ongoing | SBC growing from 7% to 8.6% of revenue. Buybacks roughly offset but net share reduction is only 1.8% over 3 years. If SBC reaches 12%+, it becomes value-destructive. This is a capital allocation concern, not a moat concern. |

---

## Scenarios of Erosion

### 1. Most Probable Erosion Scenario: Geopolitical Fragmentation (Probability: 30%, Horizon: 3-7 years)

US-China tech decoupling intensifies beyond export controls. China develops domestic EDA tools (e.g., Empyrean, X-EPIC) specifically for domestic chip designs, creating a parallel EDA ecosystem. CDNS loses 15-20% of addressable market permanently. This does not destroy the core moat (switching costs, duopoly) but reduces the TAM and therefore the long-term growth ceiling. Chinese EDA tools remain limited to trailing-edge nodes (14nm+) for the foreseeable future, so the moat at leading edge is preserved.

**Impact on CDNS:** Revenue reduction of 10-15% from China, offset by 5-8% from accelerating non-China chip design. Net impact: modest growth deceleration, not moat erosion.

### 2. Tail-Risk Erosion Scenario: Paradigm Shift in Computing Architecture (Probability: 5%, Horizon: 15-25 years)

A fundamental shift away from silicon-based transistor architecture (e.g., quantum computing, photonic computing, biological computing) could eventually make traditional EDA tools obsolete. This would not happen overnight -- the installed base of silicon chip designs will persist for decades. CDNS would likely pivot to new architectures (they already have multi-physics simulation capabilities via BETA CAE and Clarity). The analog: ASML's EUV dominance would also be threatened, but no one considers this a near-term risk.

**Impact on CDNS:** Existential in the very long term (25+ years), but the transition would be gradual enough for CDNS to adapt. Not a valid reason to discount the moat today.

### 3. Moderate-Probability Scenario: SBC-Driven Value Destruction (Probability: 30%, Horizon: 5-10 years)

SBC continues growing faster than revenue (23% CAGR vs 16% revenue CAGR), reaching 12-15% of revenue by 2030. Buybacks fail to offset dilution, and shares outstanding begin increasing. Real shareholder returns (SBC-adjusted) significantly underperform headline growth. This does not erode the competitive moat but erodes the economic value flowing to shareholders.

**Impact on CDNS:** The moat remains intact, but the investment return is diminished. This is a capital allocation issue, not a moat issue. Kill condition: SBC > 12% of revenue.

---

## Discrepancies with Thesis

The existing R1 thesis (thesis/research/CDNS/thesis.md) rates the moat as "WIDE -- among the widest in technology" with switching costs, duopoly structure, IP/know-how, network effects, and customer captivity.

**My assessment AGREES with the thesis classification of WIDE moat.**

However, I note the following nuances where my independent assessment differs slightly from the thesis framing:

1. **Network effects strength:** The thesis rates network effects at 7/10. I rate them as PARTIAL (weaker than the thesis implies). True network effects would mean CDNS tools become intrinsically better with more users. What CDNS has is more accurately described as ecosystem lock-in through foundry certifications and IP format standards. This is extremely powerful but is better categorized under switching costs and efficient scale than under network effects per se.

2. **Foundry certification as the critical barrier:** The thesis does not sufficiently emphasize that FOUNDRY CERTIFICATION (TSMC EDA Alliance, Samsung, Intel) is the most critical barrier to entry. This is more important than the software complexity itself. As one industry analyst notes: "Users describe existing tools as slow, difficult to use, segfaulting constantly -- yet dominance persists." The moat is not the software quality; it is the certification infrastructure.

3. **Gross margin decline deserves more attention:** The thesis attributes the 89.7% to 86.0% GM decline to "mix shift" (more hardware/IP revenue). This is correct but incomplete. The GM decline ALSO reflects the changing nature of CDNS's revenue -- as System Design & Analysis (lower margin) grows faster than core EDA (higher margin), the blended GM will structurally decline toward 82-85% even without competitive degradation. This does not erode the moat but does impact profitability metrics.

4. **SBC as moat-adjacent risk:** SBC at 8.6% of revenue (and growing) is not a moat issue per se, but if talent retention costs continue escalating (requiring more SBC to retain engineers), it signals increased competitive pressure for talent even within the duopoly. Worth monitoring.

---

## AI as Moat Reinforcer (Independent Analysis)

AI's impact on CDNS's moat deserves special treatment because it is the most important secular trend in the industry.

**Thesis: AI REINFORCES the moat, it does not erode it.**

Evidence:

1. **AI increases chip complexity, which increases EDA tool demand.** The industry is targeting trillion-transistor chips by 2030. More transistors = more design time = more verification cycles = more EDA revenue. This is the most direct and powerful tailwind.

2. **AI-assisted design tools (ChipStack) deepen switching costs.** CDNS's ChipStack AI Super Agent (Feb 2026) creates AI-powered workflows that generate proprietary training data within the customer's design flow. Customers who adopt ChipStack become even more locked in because the AI improves with their specific design data.

3. **AI creates a data network effect within CDNS.** With 1,000+ tapeouts using Cerebrus AI, CDNS has accumulated proprietary training data that competitors cannot replicate. This is a new moat source that did not exist 5 years ago and is growing in importance.

4. **AI does NOT replace chip designers.** ChipStack automates routine tasks (code generation, regression testing, debugging) but still requires human engineers for architecture decisions, custom IP design, and complex verification. AI augments the engineer, increasing productivity per seat -- which means CDNS can charge more per license, not fewer licenses.

5. **AI-native EDA startups face the same certification barrier.** Even if a startup builds superior AI-powered EDA tools, it cannot get TSMC/Samsung/Intel certification without years of collaboration. The AI advantage accrues to the certified incumbents (CDNS, SNPS), not to challengers.

**Key risk:** If AI eventually enables a fundamentally different chip design methodology that bypasses traditional EDA flows (e.g., fully AI-generated chip designs from natural language specifications), the moat could be disrupted. This is a 15-25 year risk, not a near-term concern.

---

## Summary

| Dimension | Assessment |
|-----------|------------|
| **Moat Classification** | **WIDE** |
| **Primary Sources** | Switching Costs (extreme), Efficient Scale/Duopoly (extreme), Intangible Assets/IP (very high) |
| **Secondary Sources** | Indirect Network Effects (partial/moderate) |
| **ROIC-WACC Spread** | +12.6pp (2024), +19.6pp average (2021-2024) |
| **ROIC Persistence** | 4/4 years above WACC (tool data); 7-10 years per external databases |
| **Gross Margin vs Peers** | +31pp vs sector median, +8pp vs SNPS |
| **Overall Durability** | 20-25+ years |
| **Trajectory** | Strengthening (AI reinforcing switching costs and IP barriers) |
| **Most Probable Threat** | Geopolitical fragmentation reducing China TAM (revenue risk, not moat risk) |
| **Classification Confidence** | Very High (9/10) |

This is among the 5-10 widest moats in the entire technology sector, comparable to ASML (EUV monopoly), MSFT (OS/cloud ecosystem), and Visa/Mastercard (payment network effects). The duopoly structure provides extraordinary stability, and AI is a secular tailwind that deepens rather than threatens the competitive advantages.

---

## 🔄 META-REFLECTION

### Doubts/Uncertainties
- **Gross margin trajectory:** I am confident the 89.7% to 86.0% decline is mix shift, not competitive erosion. However, if GM drops below 82% within 3 years, this assumption would need revisiting. The mix shift explanation has a logical floor around 82-84% (where hardware/IP revenue stabilizes as a percentage), but I cannot quantify this precisely.
- **Network effects classification:** I deliberately rated these weaker than the thesis (PARTIAL vs the thesis's 7/10). The distinction between "ecosystem lock-in" and "network effects" is subtle. Some investors would argue the foundry certification triangle IS a network effect. I chose the more conservative interpretation.
- **ROIC decline in 2024:** The ROIC drop from 35% (2023) to 22% (2024) is clearly acquisition-driven, but I only have 4 years of tool data. Longer-term ROIC history (7-10 years) from external databases consistently shows CDNS above WACC, but I have not verified this independently year-by-year.
- **Customer concentration:** CDNS does not disclose customer concentration. My estimate of top-10 clients at 40-60% of revenue is based on industry knowledge of who designs chips, not on disclosed data. This could be higher (more concentrated) or lower.

### Discrepancies with Thesis
- **Network effects:** Thesis rates 7/10, I rate PARTIAL. The difference is classification taxonomy, not substance. The thesis and I agree the ecosystem is extremely sticky; we disagree on whether to call it "network effects."
- **Foundry certification emphasis:** My assessment places MORE weight on foundry certification as the critical barrier than the thesis does. I view this as the most underappreciated aspect of the moat.
- **No material disagreement on WIDE classification.** I agree fully that this is a Wide moat.

### Suggestions for the System
- Consider adding "Foundry/Platform Certification" as a sub-category under Efficient Scale or Switching Costs in the moat framework. This is distinct from both and is the most critical barrier for EDA, semiconductor equipment, and similar technology oligopolies.
- The quality_scorer.py market_position default of 0 caused a misleading QS of 74 for what is clearly a top-2 market position globally. Suggest adding a warning in the tool output: "Market Position: 0/8 (NOT SCORED -- manual assessment required)."

### Questions for Orchestrator
1. The thesis has a HARD GATE on Q4 2025 earnings (Feb 17). Should the moat assessment be revisited post-earnings, or is the moat assessment sufficiently independent of quarterly results to stand regardless?
2. Given the Wide moat classification, does this change the entry price consideration? The thesis sets $260 (40x FY2026E). Wide moat quality compounders with this durability might justify a tighter MoS.

---

## Sources

- [Cadence & Synopsys: The Duopoly That Never Loses a Client](https://arvy.ch/en/cadence-and-synopsys-the-duopoly-that-never-loses-a-client/)
- [Why Is It So Hard for Startups to Compete with Cadence?](https://www.zach.be/p/why-is-it-so-hard-for-startups-to)
- [Cadence Unleashes ChipStack AI Super Agent](https://www.cadence.com/en_US/home/company/newsroom/press-releases/pr/2026/cadence-unleashes-chipstack-ai-super-agent-pioneering-a-new.html)
- [Cadence ChipStack Coverage -- Tom's Hardware](https://www.tomshardware.com/tech-industry/semiconductors/cadence-embeds-ai-across-its-eda-portfolio)
- [Cadence ChipStack Coverage -- EE Times](https://www.eetimes.com/cadence-unveils-chipstack-ai-agent-for-agentic-chip-design-and-verification/)
- [EDA Market Size and Forecast -- Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/electronic-design-automation-eda-tools-market)
- [Electronic Design Automation Software Market -- Precedence Research](https://www.precedenceresearch.com/electronic-design-automation-software-market)
- [Siemens Eyes Samsung's IP Weak Spot -- DigiTimes](https://www.digitimes.com/news/a20250716PD242/ip-siemens-synopsys-cadence-samsung.html)
- [Synopsys AI Strategy Analysis -- Klover.ai](https://www.klover.ai/synopsys-ai-strategy-analysis-of-dominance-in-tools-services-for-semiconductor-design-manufacturing/)
- [OpenROAD Project -- UCSD](https://theopenroadproject.org/)
- [Cadence 2024 10-K](https://www.cadence.com/content/dam/cadence-www/global/en_US/documents/company/investors/form-10-k-2024.pdf)
- [Cadence Q3 2025 Results](https://investor.cadence.com/news/news-details/2025/Cadence-Reports-Third-Quarter-2025-Financial-Results/default.aspx)
- [Cadence Expands IP for Intel 18A](https://www.cadence.com/en_US/home/company/newsroom/press-releases/pr/2025/cadence-expands-design-ip-portfolio-optimized-for-intel-18a-and.html)
- [CDNS ROIC Data -- GuruFocus](https://www.gurufocus.com/term/roic/CDNS)
