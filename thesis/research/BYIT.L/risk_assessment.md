# Risk Assessment: BYIT.L (Bytes Technology Group plc)

## Fecha: 2026-02-11 (Updated)

## Risk Score: HIGH

---

## Executive Summary

This is an UPDATED independent risk assessment building on the 2026-02-09 version with fresh data and additional research. The core conclusion is UNCHANGED but STRENGTHENED: the risk profile is materially higher than the thesis acknowledges.

**Key findings:**
1. **Quality Score discrepancy:** Tool gives 68/100 (Tier B), NOT 81 (Tier A) as thesis claims. The adversarial-adjusted QS is 72 (still Tier B).
2. **Microsoft EA direct sales takeover:** LSP commissions projected to reach ZERO in 2026. This is structural disintermediation, not cyclical adjustment.
3. **Insider ownership materially overstated:** Thesis claims 9.6%; actual executive/board ownership is 0.4-0.5% (Simply Wall St, MarketBeat). The yfinance figure may include non-management blockholders from the Altron demerger era.
4. **Former CEO governance scandal:** Neil Murphy resigned Feb 2024 over 119 undisclosed share transactions on 66 trading days. NOT MENTIONED in thesis.
5. **Softcat competitive gap widening:** Softcat GII is GBP 3.6B vs Bytes' 2.1B. Softcat generated 43% of the top 250's growth. Market cap ratio 3:1.
6. **UK public sector spending under pressure:** Government planning GBP 1.2B consultancy spending cuts by 2026. Administration budgets facing real-term cuts.
7. **Current price 292p** (new 52-week low) -- stock continues to make new lows, suggesting the market has not found a floor.

**Thesis FV 455 GBp is overly optimistic. Risk-adjusted FV range: 330-380 GBp. MoS is 15-23%, not 35%.**

---

## QS Verification: Tool vs Thesis

### quality_scorer.py Output (2026-02-11)

| Metric | Tool Output | Thesis Claim |
|--------|-------------|-------------|
| **Legacy Score** | **68/100 (Tier B)** | **81/100 (Tier A)** |
| ROIC | N/A (data gap) | "4.9pp spread" |
| ROE trajectory | 69% -> 66% -> 60% -> 56% (DECLINING) | Not highlighted |
| FCF margin | 29.9% | "~30%" |
| Revenue CAGR | +14.2% | "+10.5%" |
| EPS CAGR | +18.4% | "+13.5%" |
| GM trend | Expanding (historical) | "Expanding" |
| Insider ownership | 9.6% (yfinance) | "9.6%" |
| Beta | 0.73 | "0.85" |

### Critical Discrepancies

**1. ROIC = N/A (zero points in tool)**
The tool cannot calculate ROIC because yfinance doesn't provide full balance sheet data for BYIT.L. The thesis assigned "4.9pp ROIC spread" manually but the tool gives 0/15 for this metric. This alone accounts for 13 points of difference.

**2. Insider ownership is DISPUTED**
yfinance reports 9.6%, which the tool uses. However:
- Simply Wall St (Sep 2025): "Insiders own 0.5% of shares, worth UK 5.1m"
- MarketBeat (Jan 2026): "Insiders own 0.4%, worth UK 4.4m"
- The 9.6% figure likely includes pre-IPO/Altron-related blockholders classified as "insiders" in some databases, not current executive management

The thesis scored 5/5 on insider ownership based on the 9.6% figure. If actual executive insider ownership is 0.4-0.5%, this score should be 1-2/5.

**3. ROE is DECLINING**
ROE trajectory: 69.1% (2022) -> 65.7% (2023) -> 59.8% (2024) -> 55.9% (2025). This is a consistent downward trend of ~4-5pp per year, yet the thesis does not flag this.

### Adversarial Quality Score

| Category | Tool Score | Thesis Score | My Adjusted Score | Reason |
|----------|-----------|-------------|-------------------|--------|
| Financial Quality | 25/40 | 28/40 | 24/40 | ROIC = 0 (data gap), declining ROE not captured |
| Growth Quality | 23/25 | 21/25 | 17/25 | Historical metrics miss H1 FY2026 deceleration (GP +0.4%, OP -7%) |
| Moat Evidence | 10/25 | 22/25 | 17/25 | Tool gives 0/8 market position, 0/7 ROIC persistence (data gaps). Moat partially dependent on Microsoft goodwill. |
| Capital Allocation | 10/10 | 10/10 | 7/10 | Insider ownership overstated; CEO governance scandal |
| **TOTAL** | **68** | **81** | **65-72** | **Tier B (Quality Value)** |

**My adjusted QS: 68-72 (Tier B)** -- consistent with the tool's 68 and the previous adversarial assessment of 72.

**The thesis QS of 81 (Tier A) is NOT supported by the tool output.** The 13-point gap between tool (68) and thesis (81) violates the QS Tool-First rule (Principle 5, Session 52), which requires documented evidence for any adjustment >5 points.

---

## Matriz de Riesgos

| # | Categoria | Riesgo | Probabilidad | Impacto | Score | Mitigante | Trajectory |
|---|-----------|--------|-------------|---------|-------|-----------|-----------|
| 1 | Fundamental | Microsoft EA direct sales takeover | Alta (70%) | Alto | **CRITICAL** | Services pivot, but 68% GII is Microsoft | WORSENING |
| 2 | Fundamental | Microsoft incentive compression structural | Alta (60%) | Alto | **CRITICAL** | "Settled into new structure" per mgmt | WORSENING |
| 3 | Fundamental | Softcat structurally winning market share | Media (40%) | Alto | **HIGH** | Public sector share retained | WORSENING |
| 4 | Financiero | Operating cost inflation vs flat GP | Alta (70%) | Medio | **HIGH** | Variable pay declining | STABLE |
| 5 | Regulatorio | UK public sector spending cuts 2026/27+ | Media (45%) | Alto | **HIGH** | NHS/cyber mandates provide floor | WORSENING |
| 6 | Fundamental | Services 40% growth unsustainable | Media (50%) | Alto | **HIGH** | Growing from low base | STABLE |
| 7 | Governance | Former CEO share dealing scandal legacy | Baja (15%) | Medio | **LOW** | FCA closed case | IMPROVING |
| 8 | Governance | Insider ownership overstated (0.5% actual vs 9.6% claimed) | Alta (90%) | Medio | **HIGH** | New CEO bought GBP 99K | STABLE |
| 9 | Valoracion | FV 455p inflated by ~20% | Alta (80%) | Alto | **CRITICAL** | Adversarial FV 330-380p | WORSENING |
| 10 | Fundamental | AI self-service reducing VAR complexity | Baja (20%) | Alto | **MEDIUM** | AI currently adds complexity | STABLE |
| 11 | Geopolitico | UK recession risk | Media-Baja (25%) | Medio | **LOW** | Defensive IT, counter-cyclical public sector | STABLE |
| 12 | Financiero | GBP/USD impact on Microsoft cost base | Media (35%) | Bajo | **LOW** | UK-focused business | STABLE |
| 13 | Fundamental | Key person risk: new CEO Sam Mudd untested | Media (30%) | Medio | **MEDIUM** | 20+ years experience in Bytes subsidiary | IMPROVING |
| 14 | Fundamental | Microsoft marketplace direct ISV-to-customer | Media (40%) | Medio | **MEDIUM** | Bytes building its own marketplace | WORSENING |
| 15 | Financiero | Analyst consensus deteriorating | Alta (80%) | Bajo | **LOW** | Berenberg, Jefferies both downgraded to Hold | WORSENING |

### Scoring:
- Alta x Alto = **CRITICAL**
- Alta x Medio OR Media x Alto = **HIGH**
- Media x Medio = **MEDIUM**
- Baja x cualquiera OR cualquiera x Bajo = **LOW**

---

## Top 3 Riesgos Criticos

### 1. Microsoft Enterprise Agreement Direct Sales Takeover -- CRITICAL

- **Categoria:** Fundamental
- **Descripcion:** Microsoft is systematically reclaiming Enterprise Agreement renewals from Licensing Solution Providers (LSPs). Commission payouts to LSPs globally: $2.5B (2023) -> $1.67B (2024) -> $583M (2025) -> projected $0 (2026). Microsoft reportedly reclaimed roughly one-third of large EA renewals in 2024, and expects to reclaim nearly all by January 2026.
- **Evidencia:**
  - [US Cloud: "Microsoft Licensing Solution Providers Lose EA Revenue"](https://www.uscloud.com/blog/microsoft-licensing-solution-providers-lsp-lose-enterprise-agreement-ea-revenue/): "All large Microsoft Enterprise Agreement accounts will be lost to Microsoft Sales Direct by January 1, 2026"
  - [US Cloud: "65% of Partners Won't Survive"](https://www.uscloud.com/blog/microsoft-lsp-changes-2024/): "Partners projected to lose 65% of EA commission revenue"
  - 68% of Bytes' GII stems from Microsoft products (company disclosure)
  - ~50% of Bytes' gross profit derives from Microsoft sales
  - Microsoft FY26 CSP revenue threshold raised from ~$300K to $1M TTM
- **Probabilidad:** Alta (70%) -- This is already happening, not speculative. The trajectory is clear.
- **Impacto si materializa:** If EA commissions go to zero, Bytes loses a meaningful portion of its GP from EA renewals. Conservative estimate: 15-25% of gross profit at risk. At 25% GP loss, operating profit could decline 40%+, implying stock price of 180-220 GBp (-25-38% from current).
- **Mitigante:** Bytes is primarily a CSP partner, not purely an LSP. CSP involves ongoing management and billing that Microsoft cannot easily replicate. The distinction between EA (going direct) and CSP (still through partners) matters. Services growth of 40%+ partially offsets. BUT: the thesis treats ALL Microsoft changes as one "cyclical adjustment" when the EA direct model is qualitatively different.
- **Kill condition?:** **YES** -- "If Microsoft extends direct sales model from large EAs to mid-market accounts, EXIT." The thesis does not have this specific kill condition.

**CRITICAL NOTE:** The thesis says "Microsoft restructures partner programs every 2-3 years. Partners adapt." This is true for INCENTIVE RATE changes. It is NOT true for STRUCTURAL DISINTERMEDIATION of an entire channel (EA -> direct). These are qualitatively different phenomena that the thesis conflates.

---

### 2. Valuation Inflation: Thesis FV 455p is ~20% Too High -- CRITICAL

- **Categoria:** Valoracion
- **Descripcion:** The thesis FV of 455p uses pre-compression earnings, optimistic 8% growth, and stale Softcat comparables. Multiple independent analyses converge on 330-380p FV range.
- **Evidencia:**
  - Counter-analysis (Feb 9): Adversarial FV 330p, MoS 7%
  - Valuation report (Feb 9): Independent FV 366p, MoS 16.6%
  - This risk assessment (Feb 9): Risk-adjusted FV 370p, MoS 17%
  - Softcat P/E has compressed from "~25x" (thesis) to 17.2x (today at 1138p). The "massive valuation gap" thesis claim is materially wrong.
  - Berenberg TP: 390p (cut from 660p). Jefferies TP: 400p (cut from 447p).
  - At 292p today vs adversarial FV 330-380p, actual MoS is 11-23%, NOT 35%.
- **Probabilidad:** Alta (80%) -- Three independent analyses converge on similar range.
- **Impacto si materializa:** Position was sized based on 35% MoS for "Tier A quality." If MoS is actually 11-23% for "Tier B quality," the risk/reward profile is fundamentally different.
- **Mitigante:** The stock has fallen further to 292p since the thesis (296p entry), partially improving the MoS. But the improvement is marginal (3-4pp).
- **Kill condition?:** No, but the thesis FV should be IMMEDIATELY revised downward to 330-400p range.

---

### 3. Softcat Structurally Winning the UK VAR Market -- HIGH

- **Categoria:** Fundamental (Competitive)
- **Descripcion:** Softcat is pulling away from Bytes in absolute scale, growth rate, and market recognition. The gap is widening, not narrowing.
- **Evidencia:**
  - Softcat GII: GBP 3.617B (FY2025), +26.8% growth. Bytes GII: GBP 2.1B, +15.2% growth. Softcat is 72% larger and growing faster.
  - Softcat GP grew +18.3% vs Bytes GP +12% in FY2025 (and Bytes H1 FY2026 was +0.4%).
  - [IT Channel Oxygen: Oxygen 250 2026](https://itchanneloxygen.com/uks-top-resellers-and-msps-revealed-in-oxygen-250-2026/): "Softcat generated 43% of the top 250's growth"
  - Softcat market cap GBP 2.2B vs Bytes GBP 0.7B. Ratio has widened from ~4x to ~3.2x as both declined, but Softcat retains premium.
  - Softcat ROIC: ~36% vs Bytes: ~25% (per thesis). Softcat has 20 consecutive years of growth.
  - Softcat made its first acquisition (Oakland Group, GBP 8M) -- entering AI/data consulting. Bytes has not acquired.
  - Softcat P/E: 17.2x. Bytes P/E: 13.9x. The 3.3x gap may be fully justified by scale, quality, and growth differential.
- **Probabilidad:** Media (40%) -- Softcat is definitively winning on growth. Whether this translates to market share gain at Bytes' expense is less clear (market is growing).
- **Impacto si materializa:** If Softcat continues to grow 2x faster, the "duopoly" narrative weakens. Microsoft's higher thresholds ($1M CSP, $30M indirect provider) favor the larger player. Bytes could become #3 or #4 over 5-10 years.
- **Mitigante:** Bytes leads in public sector (GBP 824M vs Softcat GBP 628M). Different customer focus may limit head-to-head competition. Market is growing, so both can win.
- **Kill condition?:** Not immediately, but monitor: if Bytes loses #1 UK public sector VAR position, the competitive moat narrative weakens substantially.

---

## Additional Material Risks

### 4. Former CEO Governance Scandal -- NOT IN THESIS

- **Detail:** Neil Murphy resigned as CEO on February 27, 2024, after the FCA sent a voluntary request for information about undisclosed share transactions.
- **Scale:** 119 unauthorized transactions on 66 trading days between January 2021 and November 2023. An additional 15 transactions on behalf of his wife.
- **Outcome:** FCA closed the case with no sanctions. Internal investigation found no evidence of broader misconduct.
- **Residual risk:** New CEO Sam Mudd appointed from within (previously MD of Phoenix subsidiary). Average board tenure is only 2.6 years -- relatively short, indicating recent churn.
- **Impact on thesis:** The thesis does NOT mention this at all. It is a governance red flag that should be disclosed, even if resolved.
- **Source:** [IT Channel Oxygen: Former Bytes CEO FCA Closes Enquiry](https://itchanneloxygen.com/former-bytes-ceo-neil-murphy-thankful-as-fca-closes-enquiry/)

### 5. Insider Ownership Materially Overstated -- FACTUAL ERROR IN THESIS

- **Thesis claims:** 9.6% insider ownership
- **Actual data:**
  - Simply Wall St (Sep 2025): 0.5% (GBP 5.1M)
  - MarketBeat (Jan 2026): 0.4% (GBP 4.4M)
  - yfinance: 9.56% -- likely includes non-executive blockholders or pre-Altron demerger entities
- **Why it matters:** The thesis scored 10/10 on Capital Allocation partly based on "9.6% insider ownership." With actual insider ownership at 0.4-0.5%, the alignment signal is dramatically weaker.
- **New CEO Sam Mudd bought only GBP 99K worth of shares** (~0.014% of company). This is a token amount for a CEO of a GBP 700M company.
- **Source:** [Simply Wall St: BYIT Insider Trading](https://simplywall.st/stocks/gb/software/lse-byit/bytes-technology-group-shares/ownership)

### 6. UK Public Sector IT Spending Under Pressure

- **UK government planning GBP 1.2B consultancy spending cuts by 2026** ([GOV.UK](https://www.gov.uk/government/news/new-controls-across-government-to-curb-consultancy-spend-and-save-over-12-billion-by-2026))
- G-Cloud 15 framework introducing mandatory lowest-price criteria, compressing margins for suppliers
- 65% of Bytes' GII comes from public sector (per H1 earnings call -- higher than the thesis's "~50%" claim)
- However, UK government awarded GBP 573M in AI-related contracts in 2025, suggesting digital transformation spending continues
- Net risk: MODERATE-HIGH. Public sector floor exists from cybersecurity mandates, but discretionary IT admin spending faces real-term cuts.

### 7. Microsoft FY27 Incentive Changes (July 2026) -- Unknown

- Microsoft changes partner programs ANNUALLY in July (FY start).
- FY26 changes were the most severe in recent memory.
- FY27 changes are unknown. If they bring FURTHER compression, the thesis assumption of "normalization" fails.
- This creates binary risk around the July 2026 announcement.
- Probability of further compression: 30-40%. Probability of improvement: 20-30%. Status quo: 30-40%.

---

## Riesgos NO Mencionados en Thesis

| Riesgo | Severidad | Mencionado in thesis? | Comentario |
|--------|-----------|----------------------|------------|
| Microsoft EA direct sales takeover (LSP commissions -> $0) | **CRITICAL** | NO -- Thesis mentions "incentive restructuring" but NOT the EA direct model | Qualitatively different from incentive changes |
| Insider ownership is 0.4-0.5%, not 9.6% | **HIGH** | NO -- Uses yfinance 9.6% uncritically | Factual error. Tool-First rule violated. |
| Former CEO Neil Murphy: 119 undisclosed trades, FCA investigation | **MEDIUM** | NO | Governance red flag not disclosed |
| UK NI increase (+2% payroll from April 2025) | **HIGH** | NO | Not quantified for 1,266 headcount |
| Berenberg: "disruption unlikely limited to H1" | **MEDIUM** | NO | Most recent analyst qualitative view ignored |
| Public sector = 65% of GII (not ~50% as thesis claims) | **MEDIUM** | Minimized | Higher concentration than acknowledged |
| Softcat GII 72% larger and growing faster | **MEDIUM** | Partially | Thesis claims "comparable" but Softcat is pulling away |
| Microsoft marketplace direct ISV-to-customer sales | **MEDIUM** | NO | Alternative channel reduces VAR role |
| QS Tool = 68 (Tier B), not 81 (Tier A) | **HIGH** | NO -- Tool not consulted | Violates QS Tool-First rule |

---

## Kill Conditions Sugeridas

### Existing Kill Conditions Assessment

| # | Kill Condition (from thesis) | Adequate? | My View |
|---|---------------------------|-----------|---------|
| 1 | Microsoft structurally disintermediates VARs | **TOO NARROW** | Already happening via EA direct. Should trigger for EA segment NOW. |
| 2 | FCF negative 2+ years | **TOO GENEROUS** | OP can decline 40% while FCF stays positive. Need tighter trigger. |
| 3 | Services growth <10% | **ADEQUATE** | Correct metric. Watch H2 results. |
| 4 | Public sector framework loss | **ADEQUATE** | G-Cloud 15 qualification is key. |
| 5 | QS falls below 75 | **ALREADY TRIGGERED** | Tool gives 68. Adversarial gives 65-72. |

### Kill Conditions That Should Be ADDED

1. **Microsoft EA direct sales expansion to mid-market** -- If Microsoft extends direct sales below the "large EA" threshold to mid-market accounts, Bytes' last safe harbor in EA business disappears. EXIT.
2. **Operating efficiency ratio below 35%** -- Currently 40.2% and declining. Below 35% = structural cost problem beyond recovery.
3. **Two consecutive periods of GP decline** -- H1 FY2026 showed GP +0.4%. If H2 also flat or negative, the "compounder" thesis fails.
4. **Softcat EV/EBIT premium falls below 10% vs BYIT** -- If even the market stops differentiating the two, it suggests the premium for "quality VAR" is gone.

---

## Riesgo Agregado

- **Numero de riesgos HIGH+CRITICAL: 6** (EA takeover, incentive structural, valuation inflation, insider ownership, cost inflation, public sector cuts)
- **Riesgos correlacionados: YES**
  - Risks #1 + #2 + #3 are all manifestations of Microsoft's strategic decision to capture more value from its ecosystem. These compound rather than diversify.
  - Risks #4 + #5 (cost inflation + public sector cuts) are UK macro-driven and correlated during fiscal tightening periods.
- **The correlation factor is critical:** A single adverse Microsoft decision simultaneously worsens vendor dependency, margin compression, and EA revenue loss. This is NOT 6 independent risks -- it is effectively 3 correlated clusters.

**Risk Score Final: HIGH**

Rationale:
1. 6 HIGH/CRITICAL risks, 3 of which share a common root cause (Microsoft strategy)
2. QS Tool gives 68 (Tier B), contradicting thesis claim of 81 (Tier A)
3. Insider ownership factual error undermines capital allocation quality assessment
4. Adversarial FV convergence at 330-380p = MoS of 11-23% (not 35%)
5. Former CEO governance scandal not disclosed in thesis
6. Stock continues to make new lows (292p, new 52-week low Feb 4)
7. Both Berenberg and Jefferies downgraded to Hold
8. Softcat competitive gap is widening, not narrowing

**However, mitigating factors prevent VERY HIGH rating:**
- Net cash (GBP 42M) -- no debt risk
- 30% FCF margin is genuine quality
- Business is NOT dying -- GII still growing 9.1%
- Services growth 40%+ is real, albeit from low base
- Small position size (3.5%, ~EUR 377) limits portfolio damage
- Not a value trap (0/10) -- revenue growing, FCF positive, dividends increasing

---

## Scenario Analysis: Price Impact

| Scenario | Probability | FV (GBp) | vs 292p | Key Driver |
|----------|------------|----------|---------|-----------|
| **Catastrophic** (Microsoft takes all EA + mid-market direct) | 10% | 180-220p | -25 to -38% | Existential threat to margins |
| **Bear** (Incentive compression persists, services slows to 15%) | 25% | 275p | -6% | Current trajectory continues |
| **Base** (Partial normalization, services 25-30%, GP growth 6%) | 40% | 345-370p | +18 to +27% | Moderate recovery |
| **Bull** (Full normalization, AI boom, Microsoft price hikes) | 20% | 430-460p | +47 to +57% | Thesis scenario |
| **Ultra-bull** (Pre-transition multiple re-rating) | 5% | 520+p | +78%+ | Unlikely given structural changes |

**Expected Value: (0.10 x 200) + (0.25 x 275) + (0.40 x 360) + (0.20 x 445) + (0.05 x 520) = 20 + 69 + 144 + 89 + 26 = 348p**

**MoS vs EV at 292p: (348 - 292) / 348 = 16.1%**

---

## Comparison: Risk Metrics vs Other Portfolio Positions

| Position | QS Tool | QS Adjusted | # CRITICAL risks | # HIGH risks | MoS (adversarial) | Verdict |
|----------|---------|-------------|-----------------|-------------|-------------------|---------|
| AUTO.L | 79 | 68-72 | 1 | 3 | ~20% | HOLD on probation |
| MONY.L | 81 | 75-78 | 0 | 2 | ~25% | HOLD medium |
| BYIT.L | **68** | **65-72** | **3** | **3** | **11-23%** | **HOLD probation LOW** |
| LULU | 82 | 66-72 | 1 | 3 | ~20% | HOLD on probation |

BYIT.L has the MOST CRITICAL risks (3) and the LOWEST adversarial MoS of the UK positions. It also has the lowest QS Tool score.

---

## 🔄 META-REFLECTION

### Dudas/Incertidumbres
- **Microsoft EA vs CSP revenue split for Bytes specifically:** I cannot determine what percentage of Bytes' Microsoft GP comes from EA commissions vs CSP margin. If the majority is CSP (which is NOT being taken direct), the EA risk is less severe than my assessment. The thesis and H1 results do not provide this breakdown. This is the single most important data gap.
- **yfinance 9.6% insider ownership:** I could not fully resolve whether this includes current management or legacy Altron-era entities. The Altron demerger in Dec 2020 distributed ~40% of shares to Altron shareholders, some of whom may still be classified as "insiders" in databases. The thesis should have verified this with the annual report.
- **Berenberg vs management on H2 outlook:** Berenberg says "disruption not limited to H1." Management says "settled into new structure" and guides double-digit GP growth for full year. These directly contradict. I leaned toward Berenberg (bearish) but management has better visibility into their own pipeline.
- **G-Cloud 15 qualification:** If Bytes fails to qualify for G-Cloud 15 (September 2026), the public sector revenue base is at severe risk. I found no evidence this is at risk, but it should be monitored.

### Riesgos que Podrian Estar Subestimados
- **Microsoft EA direct sales is potentially existential** -- I rated it CRITICAL but within a range. If Microsoft extends direct sales to ALL account sizes (not just large), the impact is not 15-25% of GP but potentially 30-40%. The trajectory data (commissions $2.5B -> $0) is alarming.
- **UK public sector spending cuts** -- I scored MEDIUM-HIGH but the GBP 1.2B consultancy cut and G-Cloud 15 lowest-price requirement could make this worse. If public sector becomes a "race to the bottom" on price, the VAR margin evaporates.
- **Softcat acquisition strategy** -- Softcat made its first acquisition ever (Oakland Group). If Softcat begins acquiring capabilities that Bytes doesn't have, the competitive gap accelerates.

### Discrepancias con Thesis
1. **QS: 68 (tool) vs 81 (thesis)** -- 13-point gap. The thesis manually scored ROIC spread, market position, and ROIC persistence that the tool couldn't calculate, but even with those additions, the adversarial-adjusted QS is 65-72, not 81.
2. **Insider ownership: 0.4-0.5% (independent) vs 9.6% (thesis)** -- Factual error with material impact on Capital Allocation scoring.
3. **Microsoft changes: "cyclical" (thesis) vs "structural" (evidence)** -- The EA direct sales model is qualitatively different from past incentive adjustments.
4. **FV: 455p (thesis) vs 330-380p (adversarial consensus)** -- 20% inflation.
5. **Former CEO scandal: not mentioned in thesis** -- Material governance event omitted.
6. **Softcat P/E: "~25x" (thesis) vs 17.2x (actual)** -- The comparables argument is materially wrong.

### Sugerencias para el Sistema
1. **QS Tool-First enforcement:** The thesis should NEVER claim a QS higher than the tool's output without documented, quantitative justification. The 13-point gap here is the largest in the portfolio and should have been caught.
2. **Insider ownership cross-verification:** For UK companies with complex ownership history (demergers, dual-listed), yfinance insider ownership data should be cross-referenced with at least one additional source before scoring.
3. **Vendor dependency threshold:** Any company with >50% revenue from a single vendor should automatically trigger a mandatory deep-dive on that vendor's channel strategy evolution. The thesis treated Microsoft dependency too casually.
4. **Governance history check:** A basic "former CEO" search should be standard for any company analyzed. The Neil Murphy scandal is easily discoverable.

### Preguntas para Orchestrator
1. Given that QS Tool = 68 (Tier B), should the thesis be immediately reclassified from Tier A to Tier B? This changes MoS expectations from 10-15% to 20-25%.
2. Should the thesis FV be immediately revised to 330-400p range? At 292p, this still shows MoS of 11-27%, which may be adequate for Tier B but was purchased on Tier A assumptions.
3. The stock is at 292p (new 52-week low). If it continues to decline, the ADD trigger of 260p approaches. Should the full adversarial buy-pipeline be required before any ADD, given the HIGH risk score?
4. H2 FY2026 results (expected May 2026) are the key data point. Should we set a calendar event to re-evaluate with EXIT review if H2 OP also declines?
5. Three independent analyses (counter-analysis, risk assessment, valuation report) all converge on FV 20% below thesis. This pattern is consistent with the portfolio-wide finding from Sessions 50-51 (12/13 positions had inflated FV avg -15%). Should we systematically revise all thesis FVs?

---

**Assessment by:** Risk Identifier Agent (Independent)
**Date:** 2026-02-11
**Confidence:** Medium-High (key uncertainty: EA vs CSP revenue split for Bytes specifically)
**Previous version:** 2026-02-09 (core conclusions unchanged, strengthened by additional evidence)

---

## Sources

### Microsoft Channel Strategy
- [US Cloud: Microsoft LSPs Lose EA Revenue](https://www.uscloud.com/blog/microsoft-licensing-solution-providers-lsp-lose-enterprise-agreement-ea-revenue/)
- [US Cloud: Microsoft LSP Changes 2024 - 65% Won't Survive](https://www.uscloud.com/blog/microsoft-lsp-changes-2024/)
- [Microsoft FY26 CSP Program Changes](https://cspcontrolcenter.com/microsoft-csp-2026-program-changes/)
- [Microsoft FY26 Incentives Update (TDSYNNEX)](https://connect.tdsynnex.be/blog/media-library/microsoft-fy26-incentives-update/)
- [Microsoft New FY26 Incentive Guidelines (Community Hub)](https://techcommunity.microsoft.com/discussions/cloudservicesproviderspartners/new-fy26-incentive-guidelines/4413668)
- [Crayon: FY26 Microsoft CSP Incentives](https://www.crayon.com/us/resources/blogs/unpacking-the-latest-fy26-microsoft-csp-incentives/)
- [Microsoft FY26 Partner Benefits](https://partner.microsoft.com/en-us/blog/article/new-benefits-designations-specializations)

### Bytes Technology Group
- [GuruFocus: BYIT H1 FY2026 Earnings Call Highlights](https://www.gurufocus.com/news/3144722/bytes-technology-group-plc-byity-half-year-2026-earnings-call-highlights-strong-revenue-growth-amid-profitability-challenges)
- [Investing.com: Bytes Shares Tumble on Microsoft Changes](https://www.investing.com/news/earnings/bytes-technology-group-shares-tumble-as-profit-falls-amid-microsoft-changes-93CH-4284969)
- [MarketBeat: BYIT New 12-Month Low](https://www.marketbeat.com/instant-alerts/bytes-technology-group-lonbyit-reaches-new-12-month-low-heres-why-2026-02-04/)
- [IT Channel Oxygen: Neil Murphy FCA Closes Enquiry](https://itchanneloxygen.com/former-bytes-ceo-neil-murphy-thankful-as-fca-closes-enquiry/)
- [IT Channel Oxygen: Bytes Shares Slump as CEO Resigns](https://itchanneloxygen.com/bytes-shares-slump-as-ceo-neil-murphy-resigns/)

### Competitive & Market
- [IT Channel Oxygen: Bytes and Softcat Dominate Public Sector VAR Market](https://itchanneloxygen.com/bytes-and-softcat-dominate-3-7bn-public-sector-var-market/)
- [IT Channel Oxygen: UK Top Resellers Oxygen 250 2026](https://itchanneloxygen.com/uks-top-resellers-and-msps-revealed-in-oxygen-250-2026/)
- [IT Channel Oxygen: Softcat GBP 8M Acquisition](https://itchanneloxygen.com/softcat-spends-8m-on-first-acquisition-in-32-year-history/)
- [Computer Weekly: Softcat Delivers Again FY25](https://www.computerweekly.com/microscope/news/366633373/Softcat-delivers-again-in-FY-25)

### Analyst Actions
- [Berenberg Downgrades BYIT](https://www.investing.com/news/analyst-ratings/berenberg-downgrades-bytes-technology-group-stock-on-weak-growth-outlook-93CH-4122179)
- [Jefferies Downgrades BYIT to Hold](https://www.defenseworld.net/2026/01/16/jefferies-financial-group-downgrades-bytes-technology-group-lonbyit-to-hold.html)

### UK Public Sector
- [GOV.UK: GBP 1.2B Consultancy Spending Cuts by 2026](https://www.gov.uk/government/news/new-controls-across-government-to-curb-consultancy-spend-and-save-over-12-billion-by-2026)
- [UK Government G-Cloud 15 Framework](https://www.computerweekly.com/feature/UK-governments-G-Cloud-15-framework-Everything-you-need-to-know)
- [The Register: G-Cloud Inflated to GBP 14B](https://www.theregister.com/2025/10/28/uk_g_cloud_15/)

### Insider Activity
- [Simply Wall St: BYIT Ownership Structure](https://simplywall.st/stocks/gb/software/lse-byit/bytes-technology-group-shares/ownership)
- [MarketBeat: BYIT Insider Trades 2025](https://www.marketbeat.com/stocks/LON/BYIT/insider-trades/)
- [Yahoo Finance: Favourable Signals for Bytes](https://finance.yahoo.com/news/favourable-signals-bytes-technology-group-070721295.html)
