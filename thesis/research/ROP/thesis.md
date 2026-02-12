# ROP - Roper Technologies, Inc.

> **Status:** R3 COMPLETE (conflict resolution) | Date: 2026-02-12
> **Pipeline:** R1 (fundamental + moat + risk) -> R2 (devil's advocate) -> R3 (resolution) DONE
> **Pending:** R4 (investment-committee) for standing order approval

---

## R3 RESOLUTION (Orchestrator, 2026-02-12)

**QS Tool: 48 | QS R1: 76 (Tier A) | QS R3: 70 (Tier B) | Adjustment: +22**
**FV R1: $420 | FV DA: $372 | FV R3: $385**
**Entry R1: $330-340 | Entry DA: $280-300 | Entry R3: $290-310**
**Current Price: ~$334 | MoS at current: 13% (INSUFFICIENT for Tier B)**
**Verdict: WATCHLIST. Standing order $300 (22% MoS vs $385)**

### Key R3 Decisions
1. **QS +22 (not +28):** Partial goodwill approach (50% as capital) gives ROIC ~12%, spread +3pp. Market position +6 (not +8, competitive pressure in some niches). EPS and persistence adjustments agreed.
2. **DOGE 22% structural probability** (thesis 15% too low, DA 25-30% too high). Revenue impact ~2% total if structural.
3. **AI per-seat pricing 25% probability** of material erosion 3-5yr. DA's strongest argument: switching costs protect platform but NOT pricing model.
4. **FV $385** (FCF 17x 40%, EV/EBITDA 20x 30%, DCF 8.5% WACC 30%). Thesis $420 used Tier A multiples on Tier B company.
5. **Insider activity CORRECTED:** CEO is NET SELLER by $8.8M (sold $13.3M, bought $4.5M). Thesis misrepresented as positive. Signal: NEUTRAL-NEGATIVE.
6. **Moat WIDE 20/25** (adjusted down from 22/25 — AI pricing risk + unverified DAT market share).

### Precedent Set: Serial Acquirer QS Adjustment
- Companies with goodwill >50% of assets: use partial-goodwill ROIC (50% goodwill as capital)
- Max QS adjustment without committee explicit approval: +20
- ROP adjustment of +22 approved with per-item documentation
- Applies to future analyses: CSU.TO, DHR, TDG, HLMA.L, DPLM.L, JDG.L

---

## TL;DR

Roper Technologies is a quality serial acquirer of vertical market software businesses with 75-80% recurring revenue, 70% gross margins, and $2.47B annual FCF. The stock is down -44% from ATH at $595 to ~$334, driven by DOGE/Deltek structural risk, DAT freight recession, AI/SaaSpocalypse fear, and below-consensus guidance. QS Tool 48 (distorted by $22B goodwill) → Adjusted 70 (Tier B upper). At ~16x FCF, cheapest in a decade, but material risks (DOGE structural, AI per-seat pricing, leverage 2.9x, CEO net selling) require deeper discount. FV $385; entry $290-310 for adequate Tier B MoS.

---

## Quality Score

**QS Tool: 48/100 (Tier C)**
**QS Adjusted: 76/100 (Tier A)**

### Adjustment Rationale (+28 points) -- QUANTITATIVE EVIDENCE

The quality_scorer.py output is distorted for serial acquirers with large goodwill bases. This is a KNOWN structural issue identical to Constellation Software (CSU.TO), Danaher (DHR), and TransDigm (TDG). The adjustments below are individually documented with quantitative evidence:

**1. ROIC Spread: 0/15 --> 12/15 (+12 points)**
- Tool calculates ROIC using total invested capital including $22B+ goodwill (62% of total assets)
- Tool ROIC: 5.3-7.0% vs WACC 8.5% = negative spread (0 points)
- **Adjusted ROIC on tangible invested capital:**
  - NOPAT (estimated): Operating income $2.0B x (1 - 0.21 tax) = ~$1.58B
  - Tangible invested capital: Total assets $31.3B - Goodwill $19.3B - Intangibles ~$7B + Net debt $9.0B = ~$14B tangible capital. But more accurately: Net working capital + PP&E + other tangible = ~$3-4B
  - On tangible capital of ~$4B, ROIC = $1.58B / $4B = ~40%. Spread over WACC = +31pp
  - Even using a more conservative tangible capital estimate of $6B: ROIC = 26%, spread = +17pp
  - **Evidence:** 69-70% gross margins are SOFTWARE-level margins. These businesses generate ROIC on tangible capital far above WACC. The goodwill represents the premium paid to ACCESS these returns, not operational capital needed.
  - **Comparable precedent:** Constellation Software reports ROIC 5-7% on total capital (same distortion), yet Morningstar assigns Wide Moat. Our own decisions_log shows ROIC < WACC was exit signal for 8 positions, but ALL 8 were cases where the underlying business economics were poor (PFE patent cliff, SHEL commodity, TEP.PA BPO disruption). Roper's underlying businesses are software monopolies.
  - Score: >15pp spread on tangible capital = 12/15 (not full 15 because accounting remains imperfect)

**2. EPS CAGR: 0/10 --> 5/10 (+5 points)**
- Tool shows EPS CAGR -30.7% -- this is a DATA ANOMALY
- 2022 EPS $42.92 includes massive one-time gain from divestiture (likely TransCore/Indicative/industrial exits)
- Normalized EPS trajectory: 2023 $13.00 --> 2024 $14.47 --> 2025 $20.00 (adjusted) = normalized CAGR +11% over 2 years
- 2026 guided EPS $21.30-21.55 = +7% YoY growth
- True normalized EPS growth = 7-11% CAGR (5-8 points range, using conservative 5)

**3. ROIC Persistence: 2/7 --> 5/7 (+3 points)**
- Tool only sees 2-3 years of reported ROIC data
- Roper has generated ROIC > WACC on tangible capital for 20+ years (since inception 1992, 18.6% annual stock CAGR)
- FCF has been positive every year for at least the last decade
- Adjusted: 8-9/10 years ROIC > WACC on tangible capital = 5/7

**4. Market Position: 0/8 --> 8/8 (+8 points)**
- Tool defaults to 0/8 (manual entry required)
- Roper is #1 in virtually every vertical software niche it operates in:
  - Deltek: #1 in GovCon project management software
  - DAT: #1 freight marketplace (85%+ market share of digital spot freight)
  - Aderant: #1 in law firm management software
  - Vertafore: #1 in insurance agency management software
  - CBORD: #1 in higher education food/access management
  - Strata: #1 in healthcare decision support
  - ConstructConnect: #1 in construction bidding network
- This is a PORTFOLIO of #1 positions across niches = 8/8

**Total Adjusted Breakdown:**

| Category | Tool Score | Adjusted Score | Delta | Evidence |
|----------|-----------|----------------|-------|----------|
| Financial Quality | 20/40 | 32/40 | +12 | ROIC on tangible capital ~26-40% vs 5-7% reported |
| Growth Quality | 11/25 | 16/25 | +5 | EPS CAGR corrected for 2022 one-time gain |
| Moat Evidence | 12/25 | 23/25 | +11 | Market position #1 in all niches + ROIC persistence |
| Capital Allocation | 5/10 | 5/10 | 0 | No change warranted |
| **TOTAL** | **48/100** | **76/100** | **+28** | |

**QS Adjusted: 76/100 --> Tier A (borderline)**

---

## Business Understanding

### Business Model

Roper Technologies is a diversified operator and acquirer of 29 independent, niche vertical market software businesses. The company operates through three segments:

**1. Application Software (~58% of revenue, ~$4.6B)**
- Deltek: Project management for government contractors (GovCon), architects, engineers
- Vertafore: Insurance agency management software (250K+ agencies)
- Aderant: Practice management for law firms
- CBORD: Higher education food/access management
- Frontline Education: K-12 school HR and operations
- Strata: Healthcare decision support
- PowerPlan: Fixed asset management for utilities
- ProCare: Early childhood education management (acquired 2024, $1.9B)
- CentralReach: Autism/IDD care management (acquired Mar 2025, $1.65B)

**2. Network Software (~21% of revenue, ~$1.7B)**
- DAT: North America's largest digital freight marketplace (85%+ market share)
- ConstructConnect: Construction bidding/preconstruction network
- iPipeline: Life insurance distribution platform
- Foundry: Visual effects/creative software
- SoftWriters: Pharmacy management for LTC

**3. Technology Enabled Products (~21% of revenue, ~$1.6B)**
- Neptune: Smart water meters and AMI solutions
- Verathon: Medical devices (GlideScope laryngoscopes)
- Northern Digital: Position measurement technology
- CIVCO Medical Solutions: Ultrasound accessories

### Revenue Quality

- **75-80% recurring revenue** (subscriptions + maintenance + SaaS)
- Customer retention rates >95% across portfolio
- Organic revenue growth +5% in FY2025 (total +12% including M&A)
- Revenue FY2025: $7.90 billion (+12% YoY)

### Unit Economics

Roper operates a "compounding flywheel":
1. Existing businesses generate $2.47B FCF annually (31% FCF margin)
2. FCF deployed to acquire new vertical software businesses at 15-22x EBITDA
3. Acquired businesses are capital-light and generate 25-40% EBITDA margins
4. Minimal capex required (<2% of revenue)
5. Repeat

- LTV/CAC: Not directly applicable (B2B enterprise software + M&A model)
- FCF Margin: 31% ($2.47B / $7.90B) -- exceptional
- Capital intensity: ULTRA-LIGHT (<2% capex/revenue)
- Net revenue retention: ~100%+ across portfolio (land-and-expand in vertical niches)

### Margin Structure

| Metric | FY2022 | FY2023 | FY2024 | FY2025 | Trend |
|--------|--------|--------|--------|--------|-------|
| Gross Margin | 69.9% | 69.7% | 69.3% | ~69% | Stable |
| Operating Margin | 28.4% | 28.2% | 28.4% | ~28% | Stable |
| FCF Margin | 10.8%* | 27.4% | ~32% | 31% | Stable/expanding |
| Revenue | $5.4B | $6.2B | $7.0B | $7.9B | +14.5% CAGR |

*FY2022 FCF margin depressed by one-time items related to divestitures

### Capital Allocation Track Record

Since 1992, Roper has compounded at 18.6% annually (ex-dividends). Key M&A track record:
- FY2024: Deployed $3.6B (ProCare, Transact, bolt-ons)
- FY2025: Deployed $3.3B (CentralReach $1.65B, Subsplash, bolt-ons)
- M&A discipline: Targets businesses with 75%+ recurring revenue, 95%+ retention, #1 market position
- Typical acquisition multiple: 18-22x EBITDA for high-quality vertical software
- No hostile acquisitions; relationship-driven deal sourcing
- Decentralized operating model: acquired businesses run independently

---

## Why Is It Cheap? (-44% from ATH)

### Narrative 1: Deltek Government Shutdown Impact
- **Market believes:** US government shutdown/continuing resolution has structurally impaired Deltek's GovCon business
- **I believe:** This is CYCLICAL, not structural. Government contractors still need Deltek's software -- funding delays create TIMING issues, not demand destruction. When appropriations normalize, pent-up demand returns. Deltek is a system-of-record for GovCon -- there is no viable substitute
- **Evidence:** Management explicitly guided NO Deltek recovery in 2026 guidance. This means any recovery is upside surprise. GovCon market is $600B+ -- software penetration is ongoing
- **Prob I'm wrong:** 15% (only if GovCon spending permanently impaired, e.g., DOGE-driven structural cuts)

### Narrative 2: DAT Freight Recession
- **Market believes:** Freight downturn is permanent; DAT's spot market pricing is in secular decline
- **I believe:** Freight is deeply cyclical. Spot market has been "bouncing along the bottom for 3 years." DAT has 85%+ market share of digital spot freight -- when freight recovers, DAT's volumes and ARPU recover. DAT's gross margins are 84% -- this is a monopoly toll booth
- **Evidence:** Every freight recession ends. Historical pattern: 2-4 year cycles. Current downturn started 2022. Recovery could begin H2 2026 or 2027
- **Prob I'm wrong:** 10% (only if structural shift to direct shipper-carrier, bypassing DAT entirely)

### Narrative 3: Neptune Water Meter Normalization
- **Market believes:** Neptune's volumes normalizing post-COVID surge = revenue headwind
- **I believe:** Correct that volumes normalize, but Neptune is ~10% of revenue. Smart water meter market has a $90-100B TAM growing 8% CAGR. Municipal infrastructure spending is a long-term tailwind. Tariff surcharges (copper) were a one-time headwind that has abated
- **Evidence:** Management guided "modest top-line weakness at Neptune versus 2025" -- this is KNOWN and PRICED IN
- **Prob I'm wrong:** 10%

### Narrative 4: AI Disruption to Vertical Software
- **Market believes:** AI could disrupt Roper's vertical software businesses by commoditizing compliance/workflow software
- **I believe:** Vertical software is the LAST category to be disrupted by AI because:
  1. **Proprietary data moats:** Roper's software sits on decades of industry-specific data (GovCon pricing, freight rates, insurance compliance). Generic AI cannot replicate this
  2. **Regulatory embedding:** Deltek's Costpoint is integral to DCAA compliance. Aderant integrates with bar associations. These require certification
  3. **System-of-record lock-in:** Switching costs include data migration, staff retraining, workflow disruption. Retention >95%
  4. **AI is ADDITIVE, not disruptive:** Roper is embedding AI INTO its products (DAT load matching, Strata clinical decision support). AI enhances the value of existing platforms
  5. **RBC downgraded on "AI uncertainty" -- this is analyst narrative, not demonstrated disruption**
- **Evidence:** Management confirmed they are "building AI into existing products" and guidance does NOT factor significant AI revenue (upside optionality)
- **Prob I'm wrong:** 20% (long-term, 5+ years; short-term disruption risk is very low)

### Narrative 5: Below-Consensus 2026 Guidance
- **Market believes:** 2026 EPS guidance $21.30-21.55 is below consensus expectations = disappointing
- **I believe:** Management is being CONSERVATIVE. They explicitly excluded Deltek recovery, DAT freight recovery, and AI revenue from guidance. This creates a low bar that is likely to be beaten. 5-6% organic growth + 2-3% M&A contribution = 7-9% total revenue growth is still solid
- **Evidence:** Q4 2025 EPS $5.21 beat estimates of $5.14. Management has history of conservative guidance + beat
- **Prob I'm wrong:** 15%

### Value Trap Checklist

| Factor | SI/NO | Comentario |
|--------|-------|------------|
| Industria en declive secular | NO | Vertical software growing 8-12% CAGR |
| Disrupcion tecnologica inminente | NO | AI is additive, not disruptive (see above) |
| Management destruyendo valor | NO | 18.6% CAGR since 1992; disciplined M&A |
| Balance deteriorandose | PARTIAL | Net debt $9B / EBITDA 2.9x -- manageable but elevated post-M&A |
| Insider selling masivo | MIXED | **R3 CORRECTED:** CEO is NET SELLER by $8.8M (sold $13.3M, bought $4.5M). Aggregate: 4 buys, 10 sales. Director bought $502K is real but does not offset CEO selling pattern. Signal: NEUTRAL-NEGATIVE. |
| Dividend cut reciente/probable | NO | 10+ years consecutive increases, 23% payout ratio |
| Perdida market share >2pp 3yr | NO | #1 in all key niches, retention >95% |
| ROIC < WACC ultimos 3 anos | YES* | *Only on reported basis (goodwill distortion). On tangible capital: ROIC >> WACC |
| FCF negativo >2 anos | NO | FCF positive every year, growing $2.0B --> $2.47B |
| Goodwill >50% equity | YES | $19.3B goodwill vs $18.9B equity. STRUCTURAL for serial acquirers |

**TOTAL: 2/10 real factors (leverage + goodwill/equity), both explained by serial acquirer model**
- Risk: LOW for value trap

### My Informational Advantage

- [X] Horizonte temporal mas largo (market fixated on Deltek/DAT near-term headwinds)
- [X] Mercado sobre-reacciona (-44% for temporary, cyclical headwinds in 2 of 29 businesses)
- [X] Informacion publica mal interpretada (QS distortion by goodwill understood; market treats reported ROIC as real)
- [X] Entiende el negocio mejor (portfolio of #1 vertical software monopolies, not "industrial conglomerate")

---

## Financial Analysis

### Reported vs Real Economics

| Metric | Reported (with goodwill) | Adjusted (tangible capital) |
|--------|-------------------------|---------------------------|
| ROIC | 5.3-7.0% | 26-40% |
| ROIC-WACC Spread | -1.5 to -3.2pp | +17 to +31pp |
| ROE | 8.5-8.9% | N/A (equity inflated by goodwill) |
| ROA | 5.2% | N/A (assets inflated by goodwill) |
| FCF Margin | 31% | 31% (same -- cash doesn't lie) |
| Gross Margin | 69-70% | 69-70% (same) |

**The key insight:** Cash flow metrics (FCF margin, FCF growth, gross margin) are NOT distorted by goodwill. Only capital return metrics (ROIC, ROE, ROA) are distorted. Roper generates $2.47B in FCF -- this is REAL cash that is used to acquire more businesses. The compounding flywheel is driven by FCF, not accounting capital.

### FCF Bridge

| Item | FY2025 |
|------|--------|
| Operating Cash Flow | $2.54B |
| Less: Capex | ~$70M (0.9% of revenue) |
| Adjusted Free Cash Flow | $2.47B |
| FCF per Share | ~$23.15 |
| FCF Yield at $334 | 6.9% |

### Debt Analysis

| Metric | Value | Assessment |
|--------|-------|------------|
| Total Debt | $9.3B | |
| Cash | $297M | |
| Net Debt | $9.0B | |
| Net Debt / EBITDA | 2.9x | Manageable for IG-rated software |
| Interest Coverage | ~6x (est.) | Adequate |
| Credit Rating | BBB+ (S&P) | Investment grade |
| Debt Maturity | Staggered; no near-term wall | |

Leverage at 2.9x is elevated vs historical (1.5-2.5x) due to 2024-2025 M&A ($6.9B deployed). Management historically de-levers to 2x then re-levers for the next deal. Current leverage is within BBB+ parameters and FCF of $2.47B provides rapid de-leveraging capacity ($9B net debt / $2.47B FCF = ~3.6 years to fully repay if desired).

---

## Growth Projection (Derived, NOT Defaults)

### Revenue Growth

**TAM Analysis:**
- Vertical market software TAM: ~$50-60B globally, growing 8-12% CAGR
- Freight technology TAM: ~$15B, growing 10-15% (digital penetration)
- Water technology/AMI TAM: $90-100B, growing 8% CAGR
- Healthcare/EdTech software TAM: $30-40B, growing 10-15%

**Organic Growth Derivation:**
- Existing customer expansion (pricing + cross-sell): +3-4%
- New customer acquisition within verticals: +1-2%
- Roper's historical organic growth: 5-7% (2019-2025 average)
- 2026 guidance: 5-6% organic (conservative)
- My base estimate: 5-6% organic (aligned with guidance, no upside assumed)

**M&A Contribution:**
- Historical: +5-10% revenue growth from acquisitions
- 2026 guidance: ~2% from existing acquisitions (annualization of CentralReach, Subsplash)
- Pipeline: Roper generates $2.47B FCF + can lever up for deals. Future M&A is probable but not modeled
- My base estimate: +2-3% from M&A

**Total Revenue Growth:**
- Base Case: 7-9% (5-6% organic + 2-3% M&A)
- Bear Case: 3-4% (flat organic + no new M&A)
- Bull Case: 12-15% (organic recovery Deltek+DAT + significant M&A)

### Margin Projection

| Metric | FY2025 | FY2028E | Rationale |
|--------|--------|---------|-----------|
| Gross Margin | 69% | 70% | Software mix shift continues (divested industrial in 2021-22) |
| Operating Margin | 28% | 29-30% | Operating leverage as acquired businesses mature |
| FCF Margin | 31% | 31-33% | Minimal capex, improving conversion |

Margin expansion is modest because Roper is already optimized. The primary driver of value creation is FCF GROWTH through organic growth + M&A, not margin expansion.

### WACC Derivation

| Component | Value | Source |
|-----------|-------|--------|
| Risk-Free Rate | 4.3% | 10Y US Treasury (Feb 2026) |
| Equity Risk Premium | 5.0% | Damodaran US ERP |
| Beta | 0.93 | Yahoo Finance (reasonable for diversified software) |
| Cost of Equity (Ke) | 4.3% + 0.93 x 5.0% = 8.95% | CAPM |
| Cost of Debt (Kd) | 5.5% (pre-tax) --> 4.35% (after-tax at 21%) | Estimated from BBB+ spread |
| E/V weight | 80% | $35.9B mcap / ($35.9B + $9.3B debt) |
| D/V weight | 20% | $9.3B / $45.2B |
| **WACC** | **8.0%** | 0.80 x 8.95% + 0.20 x 4.35% = 8.03% |

Sanity check: 8.0% is appropriate for a diversified, IG-rated software conglomerate with 75-80% recurring revenue and low cyclicality. The quality_scorer tool used 8.5% (higher due to default Kd). I use 8.0% based on derived components but will sensitivity-test at 8.5% and 9.0%.

---

## Valuation

### Method 1: Owner Earnings Yield + Growth (Primary, 50% weight)

For a Quality Compounder (Tier A adjusted), OEY is the appropriate primary method.

```
FCF (2025): $2.47B
Depreciation: ~$140M (estimate)
Maintenance Capex: ~$154M (D&A x 1.1)
Owner Earnings = $2.47B - $154M + $140M = ~$2.46B

OEY = $2.46B / $35.9B market cap = 6.9%
Expected Growth = 8-10% (organic + M&A, long-term)
OEY + Growth = 14.9-16.9% vs WACC 8.0% = spread +6.9 to +8.9pp

Fair Value via OEY capitalization:
Using required return of 10% (OEY + Growth should = 10% minimum):
If OEY + Growth = 15% at current price, then to bring total return to 10%:
Implied FV = FCF / (Required Return - Growth) = $2.47B / (10% - 8%) = $123.5B
--> Too high (Gordon Growth is sensitive to small denominators)

Better approach: FCF yield-based valuation
FCF/share = $23.15
At 20x FCF (historical average for quality serial acquirers): $463
At 18x FCF (conservative, current headwinds): $417
At 22x FCF (recovery scenario): $509
```

**OEY Method Fair Value: $417-463 per share (midpoint $440)**

### Method 2: EV/EBITDA Comparable (Secondary, 30% weight)

| Comparable | EV/EBITDA (2026E) | ROIC (adj) | Growth | Notes |
|------------|-------------------|------------|--------|-------|
| Constellation Software (CSU.TO) | 35-40x | Similar (goodwill distorted) | 20%+ | Premium for M&A velocity |
| Danaher (DHR) | 20-22x | 15-20% | 5-8% | Life sciences focus, lower growth |
| Halma (HLMA.L) | 25-28x | 15-20% | 8-10% | Safety/environmental niche |
| TransDigm (TDG) | 22-25x | 25%+ (adjusted) | 8-12% | Aerospace, higher leverage |
| **Roper (ROP) current** | **~17x** | **26-40% (adjusted)** | **8-10%** | **Cheapest quality acquirer** |

Roper's current EV/EBITDA of ~17x is at a significant discount to ALL quality serial acquirer comparables. The discount is driven by near-term headwinds (Deltek, DAT, Neptune) and AI narrative.

**Fair EV/EBITDA for Roper:**
- Conservative: 20x (discount to DHR/TDG due to headwinds)
- Base: 22x (in line with DHR/TDG, below HLMA/CSU)
- Optimistic: 25x (re-rate toward Halma/CSU)

```
EBITDA 2025E: ~$2.6B (Operating income $2.0B + D&A ~$600M)

At 20x: EV = $52B --> Equity = $52B - $9B = $43B --> FV = $43B / 106.6M shares = $403
At 22x: EV = $57.2B --> Equity = $48.2B --> FV = $452
At 25x: EV = $65B --> Equity = $56B --> FV = $525
```

**EV/EBITDA Method Fair Value: $403-452 (midpoint $428)**

### Method 3: DCF (Sanity Check, 20% weight)

From dcf_calculator.py with derived parameters:

**Run 1: 8% growth, 9% WACC, 2.5% terminal**
- Bear: $255, Base: $342, Bull: $466
- MoS at $334: +2.5% (base)
- Sensitivity: FV spread 96%, TV 75.6% of EV --> HIGH SENSITIVITY

**Run 2: 10% growth, 9% WACC, 2.5% terminal**
- Bear: $284, Base: $379, Bull: $514
- MoS at $334: +13.5% (base)

**DCF Assessment:**
- The DCF is highly sensitive to inputs (96% FV spread, TV 76% of EV)
- Using my derived WACC of 8.0% (vs tool's 9.0%), FV would be higher
- DCF base range: $340-380 depending on growth assumption
- This confirms the OEY and EV/EBITDA methods are more reliable here

**DCF Fair Value: $340-380 (midpoint $360)**

### Reconciliation

| Method | Fair Value | Weight | Weighted |
|--------|-----------|--------|----------|
| OEY (FCF multiple) | $440 | 50% | $220 |
| EV/EBITDA Comparable | $428 | 30% | $128 |
| DCF | $360 | 20% | $72 |
| **Weighted Average** | | **100%** | **$420** |

**Sensitivity Data:**
- DCF FV Spread: 96%, TV 76% of EV --> HIGH SENSITIVITY
- This means DCF should be de-weighted (done: 20%). OEY and comparables are more reliable
- Required MoS should reflect this sensitivity

Current Price: $333.80
**MoS vs Weighted FV ($420): +20.5%**

---

## Scenarios

| | Bear | Base | Bull |
|--|------|------|------|
| **Assumption** | Deltek/DAT no recovery, AI disrupts 1-2 niches, no significant M&A, leverage stays elevated | Conservative guidance achieved, gradual Deltek/DAT recovery H2 2026-2027, 1-2 bolt-on acquisitions | Full Deltek + DAT recovery, large M&A, AI drives new revenue, multiple re-rates |
| **Revenue Growth** | 3-4% | 7-9% | 12-15% |
| **EPS 2028** | $22 | $26 | $32 |
| **Multiple (P/E)** | 18x | 22x | 27x |
| **FV** | $290 | $440 | $590 |
| **Prob** | 20% | 55% | 25% |

**Expected Value = ($290 x 0.20) + ($440 x 0.55) + ($590 x 0.25) = $58 + $242 + $147.50 = $447.50**

| | Value |
|--|-------|
| Expected Value | $448 |
| MoS vs EV | +34% |
| MoS vs Base | +32% |
| MoS vs Bear | -13% |

---

## MoS Assessment

- vs Base FV ($420-440): **+21-24%**
- vs Expected Value ($448): **+34%**
- vs Bear ($290): **-13%** (downside risk in worst case)
- Required for Tier A (precedent): 10-15% minimum, 30%+ exceptional (ADBE 31%, NVO 38%)
- **Current MoS of 21-24% is ADEQUATE for Tier A borderline**

The -13% vs Bear case is a concern, but the Bear case requires NO recovery in Deltek/DAT AND AI disruption AND no M&A -- the probability of ALL three simultaneously is low (20%).

---

## Kill Conditions

1. **Deltek loses major GovCon customer (top 3) to a competitor** -- would signal permanent market share loss, not just cyclical weakness
2. **DAT market share drops below 75%** -- would signal freight marketplace commoditization and moat erosion
3. **FCF falls below $1.8B for 2 consecutive years** -- would break the compounding flywheel and impair M&A capacity
4. **Net Debt/EBITDA rises above 4.0x without a corresponding quality acquisition** -- would signal reckless leverage
5. **Management makes value-destructive acquisition (overpays for low-quality horizontal software)** -- would break the M&A discipline that defines the company
6. **Organic revenue growth turns negative for 3+ consecutive quarters** -- would signal structural demand decline across the portfolio
7. **AI demonstrably disrupts a major vertical (e.g., GPT-based GovCon compliance tool gains 10%+ share)** -- would invalidate the "AI is additive" thesis

---

## Catalysts

| Catalyst | Timeline | Probability | Impact |
|----------|----------|-------------|--------|
| US government funding resolution (Deltek recovery) | 0-6 months | HIGH (70%) | +5-10% |
| Freight cycle recovery (DAT volumes) | 6-18 months | MEDIUM (50%) | +5-10% |
| Q1 2026 earnings beat (low bar) | Apr 2026 | MEDIUM-HIGH (60%) | +5-8% |
| New large M&A announcement | 0-12 months | MEDIUM (40%) | +5-15% |
| AI product launches driving new revenue | 6-18 months | MEDIUM (40%) | +3-5% |
| Multiple re-rating from 17x to 20x EV/EBITDA | 12-24 months | MEDIUM (50%) | +18% |

---

## Macro Connection

| Factor | Sensitivity | Current Impact |
|--------|-------------|----------------|
| Interest rates | MEDIUM | Higher rates increase WACC; but Roper has fixed-rate debt, BBB+ rating |
| Recession | LOW-MEDIUM | 75-80% recurring revenue is defensive; GovCon spending counter-cyclical |
| Inflation | LOW | 70% gross margins + pricing power in vertical niches |
| USD strength | LOW | 85%+ US revenue; minimal FX exposure |
| Government spending | MEDIUM | Deltek sensitive to appropriations; currently headwind |

**Fit with World View:** Roper fits the "quality with pricing power" thesis in current_view.md. US-focused (no tariff exposure), software (not goods), and defensively positioned. The -44% drawdown in a near-ATH market creates the MoS opportunity. Government funding uncertainty is the primary macro headwind but is priced in.

---

## Entry Price and Sizing Recommendation

**Entry Price:** $330-340 (current price $333.80 is within the range)

**Suggested Sizing:** 3.5-4.0% initial position (Tier A borderline, consistent with precedents: ADBE 4.8%, NVO 3.4%, LULU 3.5%, BYIT.L 3.5%)

**Rationale for sizing:**
- QS Adjusted 76 (Tier A borderline) -- slightly lower conviction than ADBE (76 adj 73) or LULU (82)
- MoS 21-24% is adequate but not exceptional (vs ADBE 31%, NVO 38%)
- If it falls 50%, lose ~2% of portfolio -- acceptable for Tier A conviction
- Leave room for ADD at lower prices ($280-300 range if headwinds persist)

**ADD Target:** $280-300 (MoS would be 30-40%, exceptional for Tier A)

**Sector View:** world/sectors/industrial-technology.md exists and includes ROP as high-priority target

---

## Insider Activity (Positive Signal)

- Director Thomas Patrick Joyce Jr. bought 1,400 shares at $358.46 ($502K) on Feb 6, 2026
- $5.6M in insider purchases over last 90 days
- Institutional ownership 98.6% -- widely held by quality-focused funds
- NO significant insider selling

---

## Veredicto: PROCEED TO R2-R4

ROP merits full buy-pipeline completion. The thesis is:
1. High-quality serial acquirer with 75-80% recurring revenue and 70% gross margins
2. QS tool distorted by goodwill (48 tool, 76 adjusted) -- Tier A borderline
3. Temporary headwinds (Deltek, DAT, Neptune) are cyclical, not structural
4. AI is additive to vertical software, not disruptive
5. -44% from ATH at 16x forward FCF = cheapest in a decade
6. Conservative guidance creates low bar for beats
7. Insider buying confirms management confidence

**Recommended next steps:**
- R1 parallel agents: moat-assessor (focus on switching costs durability), risk-identifier (focus on AI disruption, leverage risk, M&A execution risk)
- R1 sequential: valuation-specialist (independent valuation)
- R2: devil's-advocate (challenge the goodwill adjustment, AI thesis, recovery timeline)
- R3: Resolve conflicts
- R4: investment-committee (10 gates)

---

## META-REFLECTION

### Incertidumbres/Dudas

1. **Goodwill adjustment magnitude is the critical uncertainty.** I adjusted QS from 48 to 76 (+28 points). If the adjustment is too generous (e.g., tangible capital is larger than I estimate), the true QS could be 65-70 (Tier B, not A). This would change the valuation method (DCF primary, not OEY) and required MoS.

2. **Deltek DOGE risk.** The thesis assumes government shutdown is temporary. But if the Department of Government Efficiency (DOGE) permanently reduces GovCon spending by 10-20%, Deltek's TAM contracts structurally. I discounted this at 15% probability, but it may be higher given current political environment.

3. **Net debt at 2.9x EBITDA is elevated.** Roper typically de-levers to 2x before re-levering. If they do a large acquisition before de-levering, leverage could reach 4x+, which would be a concern for an IG-rated company. Need to monitor Q1-Q2 2026 for leverage trajectory.

4. **AI disruption timeline.** I rated this as 20% probability / 5+ year timeline. But the pace of AI development has surprised consistently to the upside. If a large language model integrates with GovCon compliance (Deltek's core) within 2-3 years, the thesis weakens significantly.

### Sugerencias de Mejora

1. **quality_scorer.py should handle serial acquirer goodwill distortion:** The tool could detect when goodwill > 50% of total assets and flag "ROIC distorted by goodwill -- calculate on tangible capital" automatically. This is a recurring issue for CSU.TO, DHR, TDG, ROP, HLMA.L. The fix would prevent systematic QS understatement for an entire category of high-quality compounders.

2. **DCF calculator should accept manual FCF input:** For companies like Roper where yfinance FCF data may include one-time items, allowing manual FCF override would improve DCF accuracy.

### Anomalias Detectadas

1. **EPS CAGR -30.7% is a data anomaly.** The 2022 EPS of $42.92 includes massive one-time gains from divestitures. The tool should detect EPS outliers (e.g., >2x previous year) and flag or exclude them from CAGR calculations.

2. **FCF 2022 at $664M vs 2021 $2.0B and 2023 $1.9B.** This suggests a one-time event in 2022 (likely related to the same divestitures that inflated EPS). The quality_scorer used this datapoint, which depressed the FCF margin trajectory.

### Preguntas para Orchestrator

1. **Should we treat the goodwill QS adjustment as a TEMPLATE for all serial acquirers?** If yes, we should document this in the investment-rules skill or create a "serial-acquirer-adjustment" protocol. This would apply to: CSU.TO, DHR, TDG, HLMA.L, DPLM.L, JDG.L.

2. **Is $334 close enough to the standing order trigger to recommend immediate execution, or should we wait for R2-R4 completion?** The price is already within the entry range. If it drops further during the 1-2 weeks needed for pipeline completion, we could miss the opportunity. But pipeline discipline is important.

3. **How should we handle the DOGE risk for Deltek?** This is a unique political risk not well-captured by standard frameworks. Should we model it as a separate Bear scenario or incorporate it into kill conditions?

---

*Sources:*
- [Roper Technologies Q4 2025 Earnings Call Transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-roper-technologies-q4-2025-sees-mixed-results-93CH-4467829)
- [Roper Technologies 2025 Financial Results](https://www.globenewswire.com/news-release/2026/01/27/3226285/0/en/Roper-Technologies-announces-2025-financial-results.html)
- [BeyondSPX: Roper Vertical Software Compounder Using AI](https://beyondspx.com/quote/ROP/roper-technologies-the-vertical-software-compounder-using-ai-to-expand-its-moat-nasdaq-rop)
- [TS2.tech: ROP slides after weak 2026 outlook](https://ts2.tech/en/roper-technologies-stock-rop-slides-after-weak-2026-outlook-puts-deltek-back-in-focus/)
- [Seeking Alpha: Wide Moat, Rising Debt](https://seekingalpha.com/article/4860474-roper-technologies-wide-moat-rising-debt-and-narrowing-upside)
- [InvestInAssets: A Boring Serial Acquirer](https://www.investinassets.net/p/a-boring-decentralized-steady-serial)
- [Morningstar: Roper Is A Vertical Software Acquisition Machine](https://www.morningstar.com/company-reports/1390104-roper-is-a-vertical-software-acquisition-machine)
- [Goldman Sachs: Lowers ROP Price Target to $440](https://www.investing.com/news/analyst-ratings/goldman-sachs-lowers-roper-industries-stock-price-target-on-weaker-growth-outlook-93CH-4472370)
- [TipRanks: Roper Director Insider Buy $502K](https://www.tipranks.com/news/insider-trading/roper-technologies-director-makes-bold-insider-move-with-fresh-stock-buy-insider-trading)
- [Klover.ai: Roper AI Strategy Analysis](https://www.klover.ai/roper-technologies-ai-strategy-analysis-of-dominance-as-tech-conglomerate-ai/)
