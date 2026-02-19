# ALFA.L - Alfa Financial Software Holdings PLC

> **Fair Value:** 235 GBp (R3 revised, was 265 GBp. DA -11.3%: CHP structural overhang + liquidity discount)
> **Entry Price:** 165 GBp (R3 revised, was 175-180 GBp)
> **Date:** 2026-02-19
> **Analyst:** fundamental-analyst (R1) + devil's-advocate (R2) + orchestrator (R3)
> **Status:** R3 COMPLETE -- WATCHLIST. HARD GATE Mar 12 FY2025 results.

---

## TL;DR

Alfa Financial Software is a niche vertical SaaS monopoly in asset finance software with extraordinary unit economics (ROIC 71%, FCF margin 21-30%, net cash). The company is at a 52-week low (~187p) with no apparent fundamental deterioration -- FY2025 prelim revenue +15% to GBP 126.5M beating consensus by GBP 2M. The disconnect between price and fundamentals appears driven by CHP Software (founder vehicle, 55% stake) periodic share disposals creating persistent overhang, plus low liquidity (GBP 600M market cap, <5 analysts historically). At 187p, the stock trades at 14.8x FY2025E EPS with 8 analysts unanimously rating BUY (targets 254-323p). This is a Tier A quality compounder trading at a Tier B valuation.

---

## Quality Score

### QS Tool: 80/100 (Tier A)

| Category | Score | Max | Notes |
|----------|-------|-----|-------|
| **Financial Quality** | **40/40** | 40 | Perfect: ROIC spread +66.9pp, FCF margin 21%, net cash, 4/4 FCF+ |
| **Growth Quality** | **16/25** | 25 | Revenue CAGR 9.7% (5pts), EPS CAGR 10.2% (8pts), GM stable (3pts) |
| **Moat Evidence** | **14/25** | 25 | GM premium +9.5pp (7pts), Market Position 0/8 (manual), ROIC persistence 7/7 |
| **Capital Allocation** | **10/10** | 10 | Insider ownership 56.7% (5pts), Dividend yield high (5pts) |

### QS Adjusted: 83/100 (Tier A)

**Adjustment: +3 points**

Reason: Market Position score is 0/8 because quality_scorer.py cannot assess market position automatically. ALFA is the #1 or #2 player in a niche market (asset finance software) with ~30+ customers that include Bank of America, Barclays, Mercedes-Benz Financial Services, Nordea. The company claims 3% penetration of a $3.4B TAM. However, this is a niche market with ~4-5 meaningful competitors (Solifi, Sofico, Odessa, LTi/Netsol). ALFA has the strongest position among Tier 1 lenders.

Applying market position assessment: #3-5 overall in broader asset finance software = +5 points, but discounted to +3 because the TAM is small and Siemens/Solifi is arguably ahead in certain segments. This is consistent with the serial acquirer market position precedent from decisions_log.yaml (max +3 for niche positions).

**QS Adjusted: 83/100 -- Tier A (Quality Compounder)**

---

## Business Understanding

### Model de Negocio

Alfa Financial Software develops and sells Alfa Systems, a single-product platform for the automotive and equipment finance industry. The platform manages the entire asset finance lifecycle: origination, contract management, servicing, collections, and end-of-term processing.

**Revenue segments (FY2025E: GBP 126.5M):**
- **Subscription** (~35-38%): Recurring SaaS fees. ARR GBP 41.6M (H1 2025), growing 16% YoY. NRR 112%. 41 subscription customers, 23 on Alfa Cloud.
- **Delivery** (~45-50%): Implementation, configuration, and customization services. Grows with new client wins and expansions. Revenue GBP 31M in H1 2025 (+10% YoY).
- **Software Engineering** (~15-17%): Custom development and enhancements. Lumpy, project-based. GBP 10.3M in H1 2025 (+72% but volatile).

**Key insight:** The business is transitioning from perpetual license to subscription SaaS. This depresses near-term revenue recognition but builds durability. 50% of customers now on Alfa Cloud. TCV (Total Contract Value) at GBP 227M provides multi-year revenue visibility.

### Problem Solved

Asset finance (auto leasing, equipment finance, wholesale finance) is a complex, heavily regulated industry. Finance companies need software that handles multi-jurisdictional compliance, complex product structures, and high transaction volumes. Alfa Systems is a "must-have" mission-critical platform -- a general ledger for asset finance. The software is deeply embedded in the operations of Tier 1 lenders. Replacing it requires 18-36 month implementation projects costing millions.

### Unit Economics

| Metric | Value | Interpretation |
|--------|-------|----------------|
| NRR | 112% | Customers spend 12% more each year (land-and-expand working) |
| Customers >GBP 1M revenue | 23 (of ~30-35 total) | High ARPU, concentrated but manageable |
| Top 5 concentration | 32% (down from 61% in 2019) | Diversifying rapidly |
| TCV | GBP 227M | ~1.8x annual revenue in contracted backlog |
| Next 12M TCV | GBP 90M | ~71% of FY2025 revenue already visible at H1 |
| Operating margin | 35% (H1 2025), 31% (FY2024) | Expanding as subscription mix grows |
| FCF margin | 21-30% (varies) | Historically 25-30%, FY2024 dipped to 21% on investment |
| SBC/Revenue | 1.0% (FY2024) | Negligible -- no SBC dilution issue |

### Structure de Margenes

| Metric | FY2021 | FY2022 | FY2023 | FY2024 | H1 2025 | Trend |
|--------|--------|--------|--------|--------|---------|-------|
| Gross Margin | 65.1% | 64.2% | 62.5% | 64.5% | ~65%* | Stable |
| Operating Margin | 29.7% | 31.7% | 29.5% | 31.2% | 34.6% | Expanding |
| FCF Margin | 30.5% | 26.7% | 28.2% | 20.7% | 35%* | Volatile |
| ROIC | 53.8% | 77.7% | 86.3% | 71.2% | N/A | Extraordinary |

*H1 2025 estimated from operating cash flow / revenue

### Capital Requirements

- **Asset-light**: Capex/Revenue historically <3% (though rising to ~6% with cloud infrastructure investment)
- **Net cash**: GBP 23.9M (H1 2025)
- **Working capital**: Receivables grew 54% vs revenue 8% in FY2024 -- **ANOMALY to investigate** (could be timing of large contract billing)
- **No debt dependency**: GBP 10M total debt, GBP 24M cash

---

## Por Que Esta Barata

### Narrativa del Mercado

The stock is at 187p, near its 52-week low of 181.8p, despite:
- FY2025 revenue +15% beating consensus
- Operating profit +17% beating consensus by GBP 3M
- NRR 112%, growing pipeline, 10 late-stage prospects

**Identified reasons for the discount:**

1. **CHP Software overhang (PRIMARY)**: Andrew Page (Executive Chair) controls ~55% via CHP Software. CHP has conducted multiple share sales: GBP 25M in May 2024, GBP 23M earlier. Each sale creates temporary selling pressure and signals "if the founder is selling, why should I buy?" -- but these are portfolio management/liquidity events by a controlling shareholder, not fundamental signals.

2. **Low liquidity / small cap**: GBP 600M market cap. Only ~8 analysts cover it (historically fewer). UK small/mid-cap has been deeply out of favor as capital flows to US mega-caps and AI plays. FTSE 250 underperformance drags everything.

3. **SaaSpocalypse contagion**: Broader software selloff ($800B in Feb 2026) dragged ALL software names, even niche vertical SaaS with no AI exposure risk. ALFA's per-seat pricing risk is MINIMAL -- its customers are not reducing headcount because of AI (asset finance operations require people for regulatory compliance and customer service).

4. **EQT dropout hangover (2023)**: EQT offered 208p in June 2023, then withdrew. Shares fell 25%. The "failed bid" stigma lingers.

5. **Software Engineering revenue uncertainty**: SE segment is lumpy (H1 2025 +72%, Q4 +11%, expected to decline in 2026). Management explicitly guides lower SE revenue ahead.

### Mi Contra-Tesis

| Market believes | I believe | My evidence |
|-----------------|-----------|-------------|
| CHP selling = negative signal | CHP selling = liquidity event, not conviction loss | CHP still holds 55%, CEO is minority CHP shareholder, both "fully committed." Insider ownership 56.7% is among the highest in our universe. |
| Small cap UK = dead money | Small cap UK vertical SaaS monopoly = mispriced | NRR 112%, revenue +15%, OP +17% -- the business is accelerating. The market is not pricing this. |
| Software sector under AI threat | Alfa Systems immune to AI seat-count risk | Asset finance is compliance-heavy, regulation-driven. AI reduces manual processes but INCREASES demand for sophisticated compliance software. Per-seat model is NOT ALFA's pricing model (subscription based on contract portfolio). |
| EQT withdrawal = flawed business | EQT withdrawal = price disagreement, not quality issue | EQT offered 208p. The business has grown revenue 35%+ since then (GBP 93M to GBP 127M). |

### Value Trap Checklist

| Factor | SI/NO | Comment |
|--------|-------|---------|
| Industria en declive secular | NO | Asset finance growing, digital transformation accelerating |
| Disrupcion tecnologica inminente | NO | Niche vertical SaaS with deep regulatory moats |
| Management destruyendo valor | NO | 56.7% insider ownership, disciplined capital allocation |
| Balance deteriorandose | NO | Net cash GBP 24M, no debt concerns |
| Insider selling masivo | PARTIAL | CHP share disposals BUT still 55% ownership |
| Dividend cut reciente/probable | NO | Paying ordinary + special dividends |
| Perdida market share | NO | NRR 112%, new client wins accelerating |
| ROIC < WACC ultimos 3 anos | NO | ROIC 53-86% vs WACC 4.3% -- extraordinary |
| FCF negativo >2 anos | NO | 4/4 years FCF positive |
| Goodwill >50% equity | NO | Goodwill ~29% of total assets |

**Value Trap Score: 0.5/10** (only partial mark for CHP disposals)

### Ventaja Informacional

- **Horizon temporal mas largo**: Market focuses on CHP selling; I focus on 112% NRR and accelerating subscription revenue
- **Market over-reacciona**: Small cap UK + SaaSpocalypse = double discount unrelated to fundamentals
- **Vertical SaaS monopoly underappreciated**: The market prices ALFA like a generic UK mid-cap software company, not like the vertical SaaS monopoly it is

---

## Projections

### Revenue Projection

**TAM Analysis:**
- Asset finance software TAM: $4.6B (2025), growing at ~10% CAGR to ~$7.4B by 2030
- ALFA's current revenue ~$160M (GBP 127M) = ~3.5% of TAM
- Market share trend: Growing (new client wins, NRR 112%)

**Revenue Growth Derivation:**
- TAM growth: +10% CAGR
- Market share: Stable to slightly gaining (+0.2pp/year through new wins)
- Pricing: Subscription model embeds ~3-5% annual escalators
- Mix shift: Subscription growing faster than delivery, SE declining
- FY2025 actual: +15% (includes SE catch-up)
- Normalized forward growth: 10-12% (subscription +15%, delivery +5-8%, SE -5-10%)

| Metric | FY2024A | FY2025E | FY2026E | FY2027E | FY2028E |
|--------|---------|---------|---------|---------|---------|
| Revenue (GBP M) | 110 | 127 | 140 | 154 | 168 |
| Growth | 8% | 15% | 10% | 10% | 9% |
| Op Margin | 31.2% | 31.6% | 32.5% | 33.5% | 34.0% |
| Op Profit (GBP M) | 34.3 | 40.0 | 45.5 | 51.6 | 57.1 |
| FCF (GBP M) | 22.8 | 32* | 36 | 42 | 47 |
| FCF Margin | 20.7% | 25%* | 26% | 27% | 28% |

*FY2025 FCF estimated from 90-100% cash conversion guidance

### WACC Derivation

| Component | Value | Source |
|-----------|-------|--------|
| Risk-Free Rate (UK 10Y Gilt) | 4.5% | Current market |
| Equity Risk Premium | 5.0% | Standard UK |
| Beta | 0.60 | Low beta, defensive SaaS. Tool reports -0.04 which is nonsensical; using industry beta for small-cap UK software |
| Ke | 7.5% | 4.5% + 0.60 * 5.0% |
| Kd after-tax | 5.6% | ~7.4% * (1 - 24.9%) |
| D/V | ~2% | Net cash, minimal debt |
| E/V | ~98% | |
| **WACC** | **7.5%** | (98% * 7.5%) + (2% * 5.6%) |

**Note:** Tool reports 4.3% WACC which uses a negative beta -- this is distorted by small-cap illiquidity, not real business risk. I use 7.5% (conservative for a UK small-cap SaaS).

### Terminal Growth

2.5% -- consistent with UK GDP growth. Asset finance is a mature, slow-growth industry. The software layer grows faster (digital transformation), but terminal value should reflect steady-state.

---

## Valuation

### Method 1: Owner Earnings Yield (Primary -- 60% weight, Tier A method)

```
FCF (FY2025E): GBP 32M
Maintenance Capex ~ Depreciation * 1.1: GBP 3.5M * 1.1 = GBP 3.9M
Owner Earnings = FCF - Maint Capex = GBP 32M - GBP 3.9M = GBP 28.1M

Market Cap at 187p: GBP 554M
Owner Earnings Yield = 28.1 / 554 = 5.1%

Expected Growth (normalized): 10%
OEY + Growth = 5.1% + 10% = 15.1%
vs WACC 7.5% = spread +7.6pp --> ATTRACTIVE

Forward OE (FY2027E): GBP 38M (FCF 42M - maint capex 4M)
Apply 15x Owner Earnings (justified by ROIC 70%+, NRR 112%, net cash):
FV = 38M * 15 / 296M shares = GBP 1.93 = 193p

Apply 18x Owner Earnings (premium for monopoly SaaS with 56.7% insider ownership):
FV = 38M * 18 / 296M shares = GBP 2.31 = 231p

Apply 20x Owner Earnings (reflecting Tier A quality):
FV = 38M * 20 / 296M shares = GBP 2.57 = 257p
```

**OEY Method Fair Value: 257p** (using 20x forward Owner Earnings, justified by ROIC 70%+, Tier A quality, monopoly position, 56.7% insider ownership)

### Method 2: EV/EBIT Normalized (Secondary -- 40% weight)

```
EBIT FY2025E: GBP 40M (operating profit)
EBIT FY2026E: GBP 45.5M

Comparable multiples:
- UK vertical SaaS (Bytes, Softcat): 15-20x EV/EBIT
- Vertical SaaS globally (Tyler, Veeva): 25-35x EV/EBIT
- Discount for UK small-cap, low liquidity: -3x to -5x
- Premium for monopoly position, 70%+ ROIC: +2x to +3x

Applying 16x FY2026E EBIT (conservative, reflecting UK small-cap discount):
EV = 45.5M * 16 = GBP 728M
Net cash: GBP 24M
Equity = GBP 752M
FV = 752M / 296M shares = 254p

Applying 18x FY2026E EBIT (reflecting quality premium):
EV = 45.5M * 18 = GBP 819M
Equity = GBP 843M
FV = 843M / 296M shares = 285p
```

**EV/EBIT Method Fair Value: 270p** (using 17x forward EBIT, midpoint of conservative and quality-adjusted range)

### DCF Tool Analysis

The DCF tool reports base case FV of 140p, which uses 9% WACC and 5% growth. This is too pessimistic because:
1. WACC 9% is too high for a net-cash company with defensive revenue (I derive 7.5%)
2. Growth 5% is below normalized 10% (FY2025 actual was +15%)
3. The tool uses trailing FCF which was depressed in FY2024 (GBP 22.8M vs FY2025E GBP 32M)

**Sensitivity assessment:** FV Spread 74%, TV 74.5% of EV = HIGH SENSITIVITY. DCF is unreliable as a point estimate. Using as range validation only (with corrected parameters, the range shifts materially upward).

At my derived parameters (7.5% WACC, 10% growth, 2.5% terminal):
From the sensitivity table at 8% growth / 7.5% WACC = 205p. At 6.5% growth / 7.5% WACC = 193p. These are CONSERVATIVE vs my 10% growth expectation.

### Reverse DCF Gap Analysis

The reverse DCF implies the market expects 12.2% FCF growth to justify 187p -- BUT this uses 9% WACC. With my 7.5% WACC, the implied growth is lower (~8-9%), which is BELOW my expectation of 10%. This suggests the stock is slightly undervalued even at current price.

### Reconciliation

| Method | Fair Value | Weight | Weighted |
|--------|-----------|--------|----------|
| OEY (20x FY2027 OE) | 257p | 60% | 154p |
| EV/EBIT (17x FY2026E) | 270p | 40% | 108p |
| **Weighted Average** | | **100%** | **262p** |

Applying a small quality premium of +1% (Tier A with 83 QS, monopoly SaaS) and rounding:

**Fair Value: 265p**

---

## Scenarios

### Bear Case (25% probability)

**Assumptions:**
- Revenue growth decelerates to 5% (TAM slows, no new wins)
- Operating margin stagnates at 31% (investment costs persist)
- CHP executes another large share sale, overhang persists
- SE revenue declines 20%
- WACC 8.5% (risk premium increase)

**Fair Value Bear: 180p**

### Base Case (50% probability)

**Assumptions:**
- Revenue growth 10% (subscription +15%, delivery +5%, SE flat)
- Operating margin expands to 33% by FY2027
- 2-3 new client wins per year
- NRR stable at 110%+
- WACC 7.5%

**Fair Value Base: 265p**

### Bull Case (25% probability)

**Assumptions:**
- Revenue growth 13% (accelerating new wins, Originations/Fleet/Commercial expansion)
- Operating margin reaches 36% (subscription mix >50%)
- M&A interest revives (EQT-type PE bid at premium)
- WACC 7.0%

**Fair Value Bull: 360p**

### Expected Value

```
EV = (180 * 25%) + (265 * 50%) + (360 * 25%)
EV = 45 + 132.5 + 90
EV = 267.5p

Current price: 187p
MoS vs EV: 30.1%
MoS vs Bear: 3.7% (tight -- bear case is close to current price)
```

---

## MoS Assessment

| Metric | Value |
|--------|-------|
| MoS vs Base FV (265p) | **29.4%** |
| MoS vs EV (267.5p) | **30.1%** |
| MoS vs Bear (180p) | **3.7%** |
| Typical Tier A MoS (precedents) | 10-15% minimum, 30%+ exceptional |
| Current MoS adequacy | **GOOD** -- 29.4% is in the range of our best Tier A entries (NVO 38%, MONY.L 36%, LULU 34%, ADBE 31%) |

**Assessment:** The 29% MoS is strong for a Tier A compounder. The tight bear case (180p, only 3.7% MoS) reflects the asset-light nature of the business -- in a bear scenario, the stock doesn't crash because there's no leverage and FCF remains positive. This is a FEATURE, not a bug. However, it means limited downside protection if the thesis is wrong.

---

## Insider & Institutional Analysis

| Metric | Value | Interpretation |
|--------|-------|----------------|
| Insider Ownership | 56.7% | EXCEPTIONAL -- CHP Software (Andrew Page) holds ~55%. CEO Denton is minority CHP shareholder. |
| Institutional Ownership | 37.9% | BlackRock is a holder. Limited institutional coverage. |
| Analyst Consensus | Strong Buy (8/8 Buy) | UNANIMOUS. Targets: 254-323p, mean 289p |
| Short Interest | N/A | Not reported (UK small-cap) |
| Recent Insider Transactions | Company buyback program (small amounts Jan 2026, Dec 2025, etc.) | No insider SELLING by named directors. CHP disposals are controlled vehicle sales. |

**Assessment:** The 56.7% insider ownership is the highest in our entire universe. The founder has >50% of his net worth in the company. This is the strongest skin-in-the-game signal possible. CHP periodic sales are liquidity events, not conviction signals.

---

## Kill Conditions

1. **NRR drops below 100%** -- Would signal customer churn/contraction, breaking the land-and-expand thesis
2. **CHP stake drops below 40%** -- Would signal potential full exit by founder, removes governance anchor
3. **New client wins stop for 2+ consecutive years** -- Would signal market saturation or competitive loss
4. **Operating margin drops below 25% for 2 consecutive years** -- Would signal pricing pressure or cost inflation
5. **Major client loss** (any of top 5) -- Given 32% concentration in top 5, losing one would be material
6. **Receivables/Revenue ratio keeps rising** -- FY2024 showed 54% receivables growth vs 8% revenue. If this continues in FY2025, could signal revenue quality issues
7. **Per-seat/per-contract pricing erosion >10%** (KC#7 equivalent) -- If customers renegotiate lower rates using AI/automation as justification
8. **UK regulatory change disadvantaging small-cap software** -- Unlikely but monitor

---

## Catalizadores

| Catalyst | Timeframe | Probability | Impact |
|----------|-----------|-------------|--------|
| FY2025 full results (Mar 12, 2026) | 3 weeks | HIGH | Confirms GBP 127M rev, GBP 40M OP. May include 2026 guidance |
| New major client win announcement | 0-12m | MEDIUM | Each win adds GBP 3-5M+ TCV, validates pipeline |
| M&A approach (PE or strategic) | 0-24m | LOW-MEDIUM | EQT offered 208p in 2023; with rev +35% since, 280-300p+ possible |
| Subscription revenue >50% of total | 12-24m | HIGH | Re-rating catalyst as market recognizes SaaS quality |
| BoE rate cuts | H1-H2 2026 | HIGH | Positive for UK small-cap multiples broadly |
| Originations / Fleet / Commercial Finance expansion | 12-36m | MEDIUM | Expands TAM from $3.4B core to potentially $10B+ |

---

## Macro Fit

- **Interest rates**: LOW sensitivity. Asset finance volumes are less rate-sensitive than mortgage (equipment finance is capex-driven). BoE cuts would help multiples.
- **Recession**: LOW-MEDIUM sensitivity. Auto/equipment finance slows in recession, but contract renewals and subscription revenue provide floor.
- **UK economy**: MEDIUM. UK weakness affects sentiment and multiples, but ALFA's revenue is ~60-65% non-UK (US, Europe, Asia-Pacific).
- **Currency**: Positive. GBP weakness benefits ALFA (reports in GBP, significant USD/EUR revenue).
- **SaaSpocalypse**: NOT APPLICABLE. Alfa Systems is mission-critical compliance software for regulated financial institutions. Zero AI per-seat risk.

**Fit with world view:** NEUTRAL-POSITIVE. Macro is supportive (rate cuts coming, geopolitical deescalation). UK small-cap discount creates entry opportunity. Cash deployment in quality at discount is aligned with strategic direction.

---

## Portfolio Context (IMPORTANT)

### UK Concentration Risk

Current portfolio has 4 UK positions: AUTO.L, MONY.L, BYIT.L, DOM.L (~30% of invested capital).

Adding ALFA.L would create a 5th UK position. Per Principio 2 and the decisions_log.yaml lesson from Session 53:

> "Before adding ANY new UK position, document why non-UK comparable is inferior."

**Justification for UK:** Alfa Financial Software has NO non-UK comparable. It is a unique vertical SaaS monopoly in asset finance. The closest competitors (Solifi/Sofico/Odessa) are private. There is no publicly traded alternative that offers this specific vertical SaaS exposure with this quality profile. The UK listing is incidental -- 60%+ of revenue is generated outside the UK.

However, the UK geographic concentration is a REAL portfolio constraint. At R4, this must be weighed against available non-UK opportunities in the pipeline.

### Small-Cap Liquidity Risk

GBP 600M market cap. Low daily volumes. Wide bid-ask spreads possible. Our typical position size (EUR 400, ~GBP 350) represents ~0.06% of market cap -- negligible. But exit in a stress scenario could be slower than for large-caps.

---

## Veredicto: WATCHLIST

**Rationale:** ALFA.L is a Tier A quality compounder (QS 83) at a compelling valuation (29% MoS vs 265p FV). The business is accelerating (FY2025 +15% revenue, +17% OP) while the stock sits at 52-week lows. This is the type of disconnect we look for.

**However, three factors warrant WATCHLIST rather than immediate BUY recommendation:**

1. **FY2025 full results on Mar 12, 2026**: The Q4 trading update is preliminary/unaudited. Full results will confirm FCF, working capital (the receivables anomaly), and may include 2026 guidance. This is 3 weeks away.

2. **UK concentration**: 5th UK position requires careful portfolio consideration. At R4, investment-committee must weigh this.

3. **Entry timing**: At 187p, the stock may continue drifting lower given low liquidity and SaaSpocalypse overhang. A standing order at 175-180p (MoS ~32-34%) would provide better risk/reward and alignment with Tier A precedents.

**Recommended next steps:**
- Proceed to R2 (devil's-advocate)
- Set price alert at 180p
- Wait for FY2025 full results (Mar 12) as HARD GATE before R4
- Entry target: 175-180p (MoS 32-34%)
- Sizing: 3-4% (EUR 300-400), consistent with Tier A precedents

---

## Sensitivity Assessment

| Metric | Value | Rating |
|--------|-------|--------|
| FV Spread (DCF) | 74% | HIGH |
| Terminal Value % of EV | 74.5% | HIGH |
| DCF Reliability | LOW (distorted by beta/WACC issues) | Use OEY + EV/EBIT as primary |
| Analyst target range | 254-323p (narrow) | Moderate consensus certainty |
| Key variables | Revenue growth + operating margin expansion | Both have positive trajectory |

---

## META-REFLECTION

### Incertidumbres/Dudas

- **Receivables anomaly**: FY2024 receivables grew 54% vs revenue 8%. This could be normal timing (large contract billed late in year) or could signal revenue quality issues. FY2025 full results will clarify. If receivables continue growing disproportionately, this is a RED FLAG.

- **CHP overhang quantification**: How much more does CHP need to sell? If CHP is on a path to full exit (from 55% to, say, 30%), that's years of selling pressure at ~GBP 25M/year. But if CHP is near its target holding, the overhang dissipates. No public information on CHP's target.

- **Beta/WACC uncertainty**: The quality_scorer reports beta of -0.04, which is clearly distorted by small-cap illiquidity. I used 0.60 as a reasonable estimate for a defensive SaaS, but this is an assumption. The WACC range of 7-9% creates significant FV sensitivity.

- **Dividend yield anomaly**: Yahoo Finance reports 75% dividend yield, which is clearly incorrect (likely includes the special dividend in a distorted way). The actual ordinary dividend yield is closer to 2-3%, plus special dividends. The payout ratio of 14.1% confirms this is sustainable.

- **Limited public data**: As a UK small-cap, there's less public financial data available than for US companies. Some metrics (detailed segment breakdown, customer-level data) are only available in annual reports.

### Sugerencias para el Sistema

- **Sector view needed**: ALFA.L doesn't fit cleanly into technology.md (which is general software) or financial-data-analytics.md (which is data/scoring). A "vertical-saas.md" or "financial-software.md" sector view would be more appropriate for companies like ALFA.L. For now, technology.md is the closest match.

- **quality_scorer.py beta handling**: The tool reported -0.04 beta, leading to a 4.3% WACC. For UK small-caps with low trading volume, the tool should flag when beta is negative or <0.2 as "potentially distorted by illiquidity -- manual review recommended."

- **Dividend yield parsing**: The 75% yield displayed is clearly wrong (special dividend distortion). The tools should flag anomalous yields >20% for investigation.

### Preguntas para Orchestrator

1. Given UK concentration (4 positions already), should ALFA.L be deprioritized vs non-UK pipeline candidates at similar quality/MoS?
2. The FY2025 full results on Mar 12 are 3 weeks away -- is it worth running R2 now or better to wait for the results?
3. The receivables anomaly (54% growth vs 8% revenue growth) -- should this be flagged as a potential kill condition or just a monitoring item?

### Anomalias Detectadas

- **Beta -0.04**: Negative beta is anomalous for any equity. This is a data quality issue from yfinance, likely caused by low trading volumes distorting the regression.
- **Dividend yield 75%**: Clearly distorted. Actual ordinary yield is ~2-3%.
- **Capex/Depreciation ratio 3.3x (FY2024)**: Rising from 0.6x in 2021. This is significant -- the company is investing heavily relative to its depreciation base. Likely cloud infrastructure buildout. Not negative per se (growth capex), but should be monitored.
- **FCF margin declining** from 30.5% (2021) to 20.7% (2024): Partly investment-driven, partly receivables timing. The H1 2025 cash conversion of 88% (vs 95% prior year) suggests this may be normalizing but bears watching.

---

## Sources

- [Alfa Financial Software H1 2025 Results](https://www.investegate.co.uk/announcement/rns/alfa-financial-software-holdings--alfa/2025-half-year-report/9087867)
- [Alfa Financial Software Q4 2025 Trading Update](https://www.investegate.co.uk/company/ALFA)
- [Alfa Financial Software Investor Relations](https://www.alfasystems.com/en-eu/investors/our-business)
- [Alfa Financial Software Company Profile - Quartr](https://quartr.com/companies/alfa-financial-software-holdings-plc_14275)
- [EQT Drops Buyout Offer - MarketScreener](https://www.marketscreener.com/quote/stock/ALFA-FINANCIAL-SOFTWARE-H-35043565/news/UK-s-Alfa-Financial-tumbles-as-EQT-drops-buyout-pursuit-44290712/)
- [CHP Software Stake Sale - Morningstar](https://www.morningstar.co.uk/uk/news/AN_1717086831059810400/alfa-financial-majority-owner-chp-software-to-sell-gbp25-million-stake.aspx)
- [Asset Finance Software Market - Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/asset-finance-software-market)
- [Alfa Financial Software - Wikipedia](https://en.wikipedia.org/wiki/Alfa_Financial_Software)
- [Alfa Financial Analyst Consensus - DirectorsTalk](https://www.directorstalkinterviews.com/alfa-financial-software-holdings-alfa-l-analyst-consensus-points-to-a-potential-60-upside/4121240126)
- [TipRanks: Alfa Financial Beats FY25 Forecasts](https://www.tipranks.com/news/company-announcements/alfa-financial-software-beats-fy25-forecasts-on-strong-q4-and-growing-pipeline)

---

**R1 Status:** COMPLETE
**Next:** R2 (devil's-advocate) recommended. HARD GATE: FY2025 full results Mar 12, 2026.
