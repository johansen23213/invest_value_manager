# Moat Assessment: EEFT (Euronet Worldwide, Inc.)

## Fecha: 2026-02-18

## Clasificacion: NARROW

---

## Fuentes de Moat Identificadas

| Fuente | Presente | Evidencia | Durabilidad | Trayectoria |
|--------|----------|-----------|-------------|-------------|
| Cost advantage | PARTIAL | Scale in ATM operations & processing; ~57K ATMs, ~750K epay POS; lower unit cost at volume. But gross margin 40% is -15pp vs software/tech sector median (55%). Compared to WU (GM ~38%), margins are similar. Not a wide cost advantage over relevant peers. | 10-15 years | Stable |
| Network effects | YES | Dandelion cross-border network: 200 countries, 4B+ bank accounts, 3.1B wallet accounts, 639K cash locations. Ria agent network #2 globally. More endpoints = more value to banks/fintechs integrating. epay retail network: 363K retailer locations creates brand distribution density. | 15-20 years | Strengthening |
| Intangible assets | YES | Regulatory licenses for money transfer in ~200 countries (extremely costly/slow to replicate). DCC authorization on Visa/Mastercard ATM networks. Ria brand #2 in remittance. CoreCard issuing platform. But no patents or proprietary technology that cannot be replicated given time. | 15-20 years | Stable |
| Switching costs | MODERATE | ATM outsourcing: multi-year bank contracts with integration costs. epay: retailer POS terminal integration sticky once deployed. Money Transfer: agent network contracts but individual agents can multi-brand. Dandelion: single API integration for bank partners. However, end consumers face LOW switching costs -- any person can choose WU, Wise, Remitly at any time. | 10-15 years | Stable |
| Efficient scale | PARTIAL | ATM deployment in secondary European markets (Poland, Czech Republic, Greece) where density deters new entrants. But large markets (Germany, UK, France) are competitive. Remittance corridors: not efficient scale -- highly fragmented. | 10-15 years | Weakening slightly (digital entrants reducing scale barriers in remittance) |

---

## Evidencia Cuantitativa

### ROIC vs WACC

**CRITICAL NOTE ON ROIC**: The quality_scorer.py shows ROIC of 52.7% for 2024 which is a CALCULATION ARTIFACT. Euronet's balance sheet carries ~$1.7B of cash ($1.04B operating cash + $650M ATM cash), and the tool likely nets excess cash against invested capital, deflating the denominator. External sources (GuruFocus, AlphaSpread) show ROIC of 7-9% using different methodologies.

**My assessment using multiple approaches:**

| Method | 2021 | 2022 | 2023 | 2024 | 2025E |
|--------|------|------|------|------|-------|
| ROIC (tool, cash-adjusted) | 8.3% | 18.4% | 22.5% | 52.7% | N/A |
| ROE | 5.6% | 18.6% | 22.4% | 24.9% | ~24% |
| NOPAT/IC (gross capital) | ~6% | ~12% | ~14% | ~15% | ~16% |
| WACC (tool) | 6.2% | 6.2% | 6.2% | 6.2% | ~6-7% |

**Interpretation**: Using ROE (~25%) as a more reliable proxy (given the financial-services-like balance sheet with settlement cash), and estimating ROIC on gross capital at ~15%, the spread vs WACC is +8 to +18pp. This is GOOD but NOT exceptional. The 2021 ROE of 5.6% (COVID hangover) shows the cyclicality risk -- in a downturn, returns compress significantly.

**ROIC Persistence**: ROIC > WACC in at least 3 of last 4 years (2021 was break-even or slightly above depending on method). Not a full 10-year clean record due to COVID impact and earlier lower returns.

### Margins vs Peers

| Metric | EEFT | Western Union | Remitly | Sector Median (Tech) |
|--------|------|---------------|---------|----------------------|
| Gross Margin | 40.1% | ~38% | ~55% | 55% |
| Operating Margin | 12.6% | ~17% | ~0% (turning positive) | ~20% |
| FCF Margin | 15.4% | ~18% | ~5% | ~15% |

**Key observation**: EEFT's margins are below both tech peers and Western Union's operating margins. WU generates higher margins on lower revenue because it has a pure asset-light model. EEFT operates ATMs (capital-intensive) which drag blended margins. Remitly has higher gross margins but is still scaling to profitability.

**The correct peer comparison is against payment processors/financial infrastructure, NOT pure software:**

| Metric | EEFT | NCR Atleos (ATMs) | Fiserv | WU |
|--------|------|--------------------|--------|----|
| Gross Margin | 40.1% | ~30% | ~40% | ~38% |
| Op Margin | 12.6% | ~8% | ~25% | ~17% |

Against ATM/payment infrastructure peers, EEFT's margins are above average, suggesting moderate moat contribution from scale.

### Market Position by Segment

| Segment | Revenue (2025) | Position | Growth | Margin Trend |
|---------|---------------|----------|--------|-------------|
| EFT Processing | $1,284M | Largest independent ATM deployer in Europe, ~57K ATMs | +11% YoY (+7% CC) | Expanding |
| epay | $1,188M | Top 3 global prepaid/branded content distributor | +3% YoY (+1% CC) | Stable |
| Money Transfer | $1,782M | #2 globally (Ria, behind WU); xe.com for FX | +6% YoY (+4% CC) | Expanding |

---

## Segment-Level Moat Analysis

### EFT Processing (30% of revenue)

**Moat sources**: Scale + switching costs + efficient scale in secondary markets.

- Operates ~57K ATMs across Europe, India, and other markets. This is the largest independent network in Europe.
- Banks outsource to Euronet via multi-year contracts (switching costs: integration of settlement, compliance, cash management).
- DCC (Dynamic Currency Conversion) is a high-margin revenue stream from tourist transactions -- controversial but lucrative. EU regulation (2020) required transparency but did not ban DCC.
- Merchant acquiring growing fast: 32% EBITDA growth in 2025; market share in Greece grew from 18% to 24% in 3.5 years.
- **Threat**: Cash usage declining (52% of Euro-area POS transactions in 2024, down from 79% in 2016). However, ATMs per country also declining, meaning survivors gain share. Cash will not go to zero -- ATMs are essential infrastructure for cash access, which governments are legislating to protect.
- **Counter-threat**: Euronet is pivoting ATM infrastructure into merchant acquiring and payments, reducing pure-play ATM dependency. Transaction volumes grew +36% YoY in 2025 (vs +3% ATM count growth), suggesting higher utilization and more non-ATM transactions.

**Moat rating**: Moderate. Multi-year contracts and scale create barriers, but secular cash decline is a structural headwind partially offset by pivot to merchant acquiring.

### epay (28% of revenue)

**Moat sources**: Distribution network + retailer integration switching costs.

- ~363K retailer locations, ~749K POS terminals, 59 countries.
- Distributes prepaid content (gaming, streaming, mobile top-up) for 1,000+ brands. Acts as middleman between content providers and physical retail.
- Switching costs for retailers: integrated POS terminal, training, reconciliation systems.
- Digital branded payments growing (Revolut expansion to 20 countries).
- **Threat**: App stores (Apple, Google) disintermediate physical distribution of digital content. Why buy a gift card at a store when you can buy in-app? Mobile top-up declining as prepaid shifts to postpaid/data plans.
- Gaming gift cards provide partial offset -- many gamers are young and prefer physical/retail purchasing.
- Revenue growth only +3% YoY (1% CC) in 2025 -- suggests structural headwind is real.
- POS terminals DECLINED 4% YoY -- network is shrinking at the edges.

**Moat rating**: Weak to moderate. The distribution network is real but the secular trend is clearly against physical distribution of digital content. This segment's moat is eroding.

### Money Transfer (42% of revenue)

**Moat sources**: Network effects (agent network) + regulatory licenses + Dandelion platform.

- Ria: #2 globally with ~639K cash locations across ~200 countries.
- Dandelion: "largest real-time cross-border payments network" -- 4B+ bank accounts, 3.1B wallet accounts, 126 mobile wallets.
- Regulatory licenses in ~200 countries -- takes years and significant investment to replicate.
- Digital channels growing 31% transaction growth, 33% revenue growth (Q4 2025). Digital new customer acquisitions +33%.
- Xe.com provides FX services and digital-first corridor access.
- **Threat**: Digital-native competitors (Wise: $33B send volume/Q; Remitly: $14.5B/Q) growing faster in digital corridors. Western Union declining but still #1 in cash-to-cash.
- **Key question**: Can Ria transition to digital fast enough while maintaining physical agent network?
- US-originated transfers DECLINED 2% in Q4 2025 due to immigration policy uncertainty.
- $20.4M restructuring charge in 2025 for "digital acceleration" -- signals urgency.

**Moat rating**: Moderate to strong. The combination of physical agent network (essential for cash-centric emerging markets) + Dandelion digital infrastructure creates a hybrid model that pure-digital players cannot easily replicate. But the moat is being tested by digital disruption and immigration policy risk.

---

## Amenazas al Moat

| Amenaza | Probabilidad | Impacto | Horizonte |
|---------|-------------|---------|-----------|
| Secular decline of cash (ATMs become less relevant) | Alta | Medio | 5-15 years (gradual, not sudden) |
| Digital remittance disruption (Wise, Remitly take share) | Alta | Medio-Alto | 3-10 years |
| App store disintermediation of epay physical distribution | Media-Alta | Medio | 5-10 years |
| US immigration policy tightening (reduces remittance volumes) | Media | Medio | 1-3 years |
| DCC regulatory restriction (EU bans or caps DCC fees) | Media | Medio | 3-5 years |
| Loss of major bank ATM outsourcing contract | Baja-Media | Bajo | Ongoing |
| Apple Card / CoreCard client losses (JPMorgan transition by 2027) | Media | Bajo-Medio | 1-2 years |
| Stablecoin/crypto remittance replacing traditional corridors | Baja | Alto (if materializes) | 5-10 years |

---

## Escenarios de Erosion

### 1. Most Probable: Gradual Margin Compression from Digital Disruption (60% probability over 10 years)
- Cash usage continues declining 2-3pp annually in Europe. ATM network shrinks but survivors gain share.
- Digital remittance players (Wise, Remitly) capture increasing share of high-margin digital corridors, forcing Ria to match pricing.
- epay's physical distribution becomes increasingly niche as app stores dominate digital content delivery.
- **Impact**: Revenue growth slows to 3-5%, margins compress 100-200bp, ROIC declines toward WACC over 10+ years.
- **Mitigation**: Euronet's pivot to merchant acquiring, Dandelion platform, and digital channels partially offsets, but unlikely to fully replace legacy high-margin streams.

### 2. Tail Risk: Regulatory Crackdown on DCC + Immigration Shock (15% probability)
- EU bans or severely caps DCC markups, eliminating a high-margin EFT revenue stream.
- Simultaneously, US immigration policy dramatically restricts remittance-sending populations.
- **Impact**: Could reduce operating income 20-30% over 2-3 years.
- **Probability**: Low individually but correlated (both driven by populist/nationalist policy trends).

---

## Short Interest Signal

Short interest is 14.0% of float with 8.7 days to cover -- elevated. This has been INCREASING (up 3.9% month-over-month). This signals meaningful skepticism about the business trajectory, possibly driven by:
- Q4 EPS miss (stock dipped to ~$70 from ~$75)
- Immigration policy uncertainty
- Secular cash decline narrative
- Slow epay growth

This does NOT invalidate the moat but indicates market participants see vulnerability.

---

## ROIC Sustainability Assessment

The +46.5pp ROIC-WACC spread reported by the tool is **NOT reliable** for this company due to balance sheet structure (high settlement/ATM cash distorts invested capital calculation).

**Realistic assessment**: ROE of 20-25% vs cost of equity ~9% provides a REAL spread of +11 to +16pp. This is GOOD and above average, but:
- 2021 showed ROE of only 5.6% (COVID), demonstrating cyclicality
- The business has structural headwinds (cash decline, digital disruption) that could compress returns
- Growth requires capital (ATMs, merchant acquiring expansion, CoreCard integration)

**Conclusion on ROIC sustainability**: Returns are likely to remain above cost of capital for the next 10-15 years but the MAGNITUDE of the spread is likely to narrow as legacy high-margin streams (DCC, physical prepaid, cash-based remittance) face secular erosion.

---

## Discrepancias con Thesis (si aplica)

No fundamental-analyst thesis exists yet for EEFT (directory was empty). This is a first assessment. Key discrepancy flagged for the orchestrator:

1. **The QS of 73 may be slightly INFLATED due to the ROIC calculation issue.** The tool gives 15/15 on ROIC spread based on the 52.7% ROIC figure, which is an artifact. Using a more conservative 15% ROIC, the spread would be ~9pp, still scoring well (12/15 or 15/15 depending on threshold) but the narrative of "exceptional ROIC" should be challenged.

2. **The 0/10 score on Market Position and 0/10 on GM Premium in the legacy QS reflects the tool's inability to assess multi-segment businesses against their correct peer group.** EEFT's relevant peers are payment processors and remittance companies, not pure software firms. Against correct peers, GM is at or above median. Market position is #1 (independent ATMs in Europe) and #2 (global remittance). Adjusting these manually could add +10 to +15 points, potentially pushing QS to 83-88 (Tier A). BUT this requires careful justification.

---

## Moat Classification Rationale

### Why NARROW and not WIDE:

1. **Only 1 segment has a durable strong moat source (Money Transfer via regulatory licenses + Dandelion network).** EFT Processing has moderate switching costs but faces secular headwind. epay moat is eroding.

2. **ROIC persistence is not clean for 10+ years.** 2021 was weak (COVID), and pre-COVID years show variable returns depending on methodology. A Wide moat requires consistent ROIC > WACC for 10+ years.

3. **Multiple active threats** with Medium-High probability are testing the moat simultaneously (digital disruption in remittance, cash decline in ATMs, app store disintermediation in epay). A Wide moat would show resilience to all these. EEFT is ADAPTING (merchant acquiring, Dandelion, digital channels) but adaptation =/= proven resilience.

4. **Trayectoria mixta**: Money Transfer moat strengthening (Dandelion, digital growth 30%+). EFT moat stable-to-strengthening (merchant acquiring). epay moat weakening. Net: roughly stable with risk of deterioration.

### Why NARROW and not NONE:

1. **Regulatory licenses in 200 countries** for money transfer are genuinely difficult to replicate. Even well-funded fintech players take years to get licensing in new markets.

2. **Dandelion network** has real network effects -- 4B+ bank accounts, 3.1B wallet accounts. Banks like Citi are integrating, which adds value for all participants.

3. **Physical agent network** of 639K locations cannot be replicated by digital-only players. In cash-centric economies (Latin America, South Asia, Africa), physical presence is essential and provides a moat that will persist for at least 10-15 years.

4. **ROIC is above WACC** by a meaningful margin in normal years (ROE 20-25% vs CoE 9%).

5. **Founder-led**: CEO Michael Brown is founder with 6.2% ownership, aligned incentives.

---

## 🔄 META-REFLECTION

### Dudas/Incertidumbres
- **ROIC calculation is unreliable**: The quality_scorer.py produces a 52.7% ROIC for 2024 which is clearly a calculation artifact for a company with $1.7B of settlement/ATM cash on the balance sheet. External sources show 7-15% ROIC depending on methodology. The QS of 73 may be distorted by this. A ROIC correction could change the score by +/- 5 points. This needs to be flagged prominently in the thesis.
- **Dandelion's competitive position**: I could not find direct competitor network comparison data for Dandelion vs Visa Direct vs Mastercard Send vs SWIFT GPI. Management claims "largest real-time cross-border network" but this needs verification. If Visa Direct/Mastercard Send are comparable or superior, the Dandelion moat is weaker than presented.
- **epay segment direction**: POS terminals declining 4% YoY is a concerning signal. Revenue only +1% CC. I could not determine what percentage of epay revenue comes from mobile top-up (declining) vs gaming gift cards (growing) vs other. This breakdown matters for assessing the erosion rate.
- **DCC revenue contribution**: DCC is described as "high margin" but the exact revenue/profit contribution is not disclosed. If DCC represents >15% of EFT profits, regulatory risk is material.

### Sugerencias de Mejora
- **quality_scorer.py**: Should handle companies with large settlement/ATM cash balances by excluding this cash from the invested capital calculation, or at minimum flagging it as a distortion. Payment processors and financial infrastructure companies commonly have this issue. Consider a --payment-processor flag similar to the proposed --insurer flag.
- **Moat assessment template**: The current template does not explicitly handle MULTI-SEGMENT businesses where each segment has a DIFFERENT moat profile. EEFT has Wide-ish moat in Money Transfer, Narrow in EFT, and Weakening in epay. The final classification is a weighted judgment call that should be more structured.

### Preguntas para Orchestrator
1. Should the fundamental-analyst adjust the QS to reflect the ROIC calculation issue? If so, should the adjustment be UP (adding manual market position + GM premium points) or DOWN (correcting the inflated ROIC component)?
2. The 14% short interest is notable -- should we treat this as a signal that the market has already identified the moat erosion thesis, or simply as a contrarian indicator?
3. For the thesis, which segment should carry the most weight in the moat assessment -- the largest by revenue (Money Transfer at 42%) or the one with the strongest/weakest moat?

---

**Assessment by**: moat-assessor agent (R1 buy-pipeline)
**Source classification**: Financial data from quality_scorer.py + narrative_checker.py = Level 1 (primary data via yfinance). Web research = Level 2 (secondary analysis from FXCIntel, GlobeNewsWire press releases, ECB studies) and Level 3 (opinion from Seeking Alpha, analyst notes). Market position claims from company IR = Level 2, treated with appropriate skepticism.
