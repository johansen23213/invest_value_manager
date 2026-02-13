# ACGL - Arch Capital Group Ltd.

> **Fair Value:** $120
> **Analysis Date:** 2026-02-12
> **Pipeline Stage:** R1 (Fundamental Analysis)
> **Analyst:** fundamental-analyst

## TL;DR

Arch Capital is the best-in-class specialty insurer/reinsurer with a 15%+ BVPS CAGR since 2001, ROE consistently 17-23%, net cash position, and a P/B of 1.53x against a justified P/B of 2.1-2.7x. The market prices ACGL at 8.6x P/E because it fears reinsurance cycle softening (-15% property cat rates at Jan 2026 renewals), but Arch's underwriting discipline moat means it will shed unprofitable volume rather than chase share -- exactly the behavior that produced book value compounding through every prior soft market. At $99.85 (EUR 84.06), ACGL offers 20% MoS to base case fair value of $120 per share.

---

## Quality Score

**QS Tool: 57/100 (Tier B)**

**QS Adjusted: 68/100 (Tier B)** -- Adjustment: +11 points for insurance-specific structural distortions

### Adjustment Documentation (Quantitative Evidence Required)

The quality_scorer.py tool has known structural biases that underscore insurance/financial companies:

| Factor | Tool Treatment | Reality | Adjustment |
|--------|---------------|---------|------------|
| **ROIC = 7.3% (2024)** | ROIC-WACC spread scored 0/15 (tool shows +nanpp due to NaN) | ROIC is MEANINGLESS for insurers. Float-funded invested assets inflate the denominator. **ROE is the correct metric**: 23.5% (2024), 34.4% (2023), 19.5% (FY2025 operating). ROE-WACC spread = +13-28pp. | +8 (from 0/15 to 8/15) |
| **GM Trend = 0/5** | Tool could not compute trend (data gap) | Insurance "gross margin" is effectively (1 - combined ratio). ACGL combined ratio: 82.8% FY2025, 85% FY2024, improving trend. Equivalent GM ~17% and EXPANDING. | +3 (from 0/5 to 3/5) |
| **Market Position = 0/8** | Tool defaults to 0 (manual required) | ACGL is top-3 global specialty reinsurer, #1 US mortgage insurer (with peers). Market cap $36B, among top 5 P&C globally by underwriting income. | +0 (conservative -- leave at 0, this requires deeper competitive analysis in R2) |

**Net adjustment: +11 points** (8 for ROIC structural distortion + 3 for GM trend data gap)

**Adjusted score: 57 + 11 = 68/100 (Tier B)**

Note: I am NOT adjusting market position upward despite strong evidence because the tool defaults to 0 and I want to be conservative. If market position were scored at 5/8, the adjusted QS would be 73 (borderline Tier A). This should be evaluated in R2 moat assessment.

---

## Business Understanding

### Business Model

Arch Capital Group is a Bermuda-domiciled specialty insurance, reinsurance, and mortgage insurance holding company operating through three platforms:

**1. Reinsurance (largest segment by profit)**
- Treaty and facultative reinsurance covering property catastrophe, property, liability, marine, aviation, trade credit, agriculture, accident & health, life, and political risk
- Clients are other insurance companies seeking to lay off risk
- Revenue model: annual/multi-year reinsurance premiums
- FY2025 underwriting income: $1.6B (record)

**2. Insurance (primary/specialty)**
- Specialty risk solutions across various industries
- Lines: specialty casualty, professional liability, property, programs, travel, accident & health
- Q4 2025 underlying ex-cat combined ratio: 90.8%
- Revenue model: annual premiums

**3. Mortgage Insurance**
- US private mortgage insurance (USMI) and international mortgage reinsurance
- FY2025 underwriting income: $1B (4th consecutive year above $1B)
- Q4 2025 combined ratio: 34% -- extraordinarily profitable
- Insurance in force relatively flat, persistency 81.8%
- Revenue model: monthly and single premiums on mortgage pools

### Revenue Split (FY2025 approximate)
- Total revenues: $18.8B (+12.9% YoY)
- Net premiums earned: majority from reinsurance and insurance
- Net investment income: $434M Q4 alone (growing with portfolio size and yield)
- Equity method income: $155M Q4 (Watford Holdings and other investments)

### Unit Economics (Insurance-Specific)

For insurers, the key "unit economic" is the **combined ratio** -- the cost of claims + expenses per dollar of premium collected.

| Metric | ACGL FY2025 | ACGL FY2024 | Industry Avg |
|--------|-------------|-------------|-------------|
| Combined Ratio (consolidated) | 82.8% | 85.0% | ~98-99% |
| Reinsurance CR | ~75-80% (est.) | ~80% | ~95% |
| Insurance CR | ~90-91% | ~91% | ~97% |
| Mortgage CR | ~34% | ~35% | ~50-60% |

**Underwriting profit = premiums - claims - expenses.** ACGL produces 15-20% underwriting margins when the industry as a whole barely breaks even. This is the core of the moat.

### Float and Investment Income

The insurance model generates "float" -- premiums collected upfront, claims paid later. ACGL invests this float, generating:
- Net investment income: growing as portfolio grows and yields remain elevated
- FY2025 investment portfolio: ~$30B+ at ~4% yield = ~$1.2B+/year investment income
- This is essentially free money -- the cost of float is negative when combined ratio <100%

### Capital Intensity
- **Asset-heavy** by nature (investment portfolio backing reserves), but capital-EFFICIENT
- No physical capex -- "capex" is capital allocated to underwriting risk
- Book value IS the business
- FCF is enormous ($6.6B in 2024) because insurance premiums are cash upfront, claims are paid later

### Structure of Margins
- Operating margin: ~25-30% (net income / revenues)
- Net margin: ~20-25%
- FCF margin: ~35% (but distorted for insurers -- cash flow includes premium collection which inflates the number)
- The correct profitability metric is ROE: 17-23% consistently

---

## Por Que Esta Barata

### Narrativa del Mercado

The market is pricing ACGL at 8.6x P/E and 1.53x P/B because:

1. **[X] Reinsurance cycle softening** -- Property cat rates down -14.7% at Jan 2026 renewals (largest decline since 2014). Market fears margin compression across the reinsurance book.

2. **[X] Insurance sector generally "out of favor"** -- After 2-year outperformance (2023-2025), insurance stocks have underperformed in late 2025. ACGL -6.8% vs Dow +7.1% over 52 weeks.

3. **[X] Revenue miss in Q4 2025** -- ACGL beat on EPS but missed on revenue in Q4. Insurance segment GPW grew only 2%, NPW declined 4% due to business mix/timing. Market sees deceleration.

4. **[X] CEO transition** -- Marc Grandisson (founder/CEO since 2018, at company since 2001) retired October 2024. Nicolas Papadopoulo took over. Market discounts leadership change risk.

5. **[ ] Climate/catastrophe risk** -- LA wildfires ($40B insured losses), 6th year >$100B insured losses. Market prices in cat tail risk.

### Mi Contra-Tesis

**Market cree:** Reinsurance softening will compress margins and earnings will decline.

**Yo creo:** ACGL has navigated every underwriting cycle since 2001. Their "house playbook" -- shedding volume when pricing is inadequate -- is precisely what produces BVPS compounding. The company GREW book value through the 2017-2019 soft market. The current cycle is softening FROM record profitability (82.8% CR vs 95%+ industry). Even with -15% rate declines, ACGL's disciplined pricing means their CR might go from 83% to 87% -- still vastly profitable.

**Evidence:**
- BVPS CAGR >15% since 2001 (through multiple soft markets)
- Management explicitly stated: "house playbook remains as valid and effective as ever"
- Q4 2025 insurance NPW declined 4% = they are already shedding unprofitable volume
- Reinsurance segment produced RECORD $1.6B underwriting income in FY2025
- 2026 described by executives as potentially "fifth-best year ever" for cat reinsurance even after expected rate cuts

**Probability I am wrong:** 20% -- the risk is that softening is deeper/longer than expected, combined with a major cat event, causing double hit to underwriting income.

**Market cree:** CEO transition creates uncertainty.

**Yo creo:** Papadopoulo is a 15-year Arch veteran who ran the reinsurance segment. The underwriting culture is institutional, not one-man. Grandisson retains 2.2M shares (~$220M) showing confidence. The transition has been smooth -- Q4 2025 was excellent under new leadership.

**Probability I am wrong:** 10% -- Papadopoulo could change capital allocation strategy, but early evidence is positive (Q4 CR 80.6%, $798M buyback).

### Value Trap Checklist

| Factor | SI/NO | Comentario |
|--------|-------|------------|
| Industria en declive secular | NO | Insurance grows with GDP, climate increases TAM |
| Disrupcion tecnologica inminente | NO | AI helps incumbents (claims processing, underwriting) |
| Management destruyendo valor | NO | $1.9B buybacks in 2025 at 1.5x P/B, accretive |
| Balance deteriorandose | NO | Net cash $953M, improving |
| Insider selling masivo | PARTIAL | Grandisson sold $45M since 2021, but retains $220M+ |
| Dividend cut reciente/probable | NO | Never paid regular dividend (special $5 in Dec 2024) |
| Perdida market share >2pp 3yr | NO | Growing selectively, shedding unprofitable business |
| ROIC < WACC ultimos 3 anos | N/A | ROIC meaningless for insurers; ROE 17-23% >> 6.6% Ke |
| FCF negativo >2 anos | NO | FCF: $3.4B, $3.8B, $5.7B, $6.6B (growing) |
| Goodwill >50% equity | NO | Goodwill minimal for insurer model |

**TOTAL: 0.5/10 (very low value trap risk)**

### Mi Ventaja Informacional
- [X] Horizonte temporal mas largo -- market discounts cycle fear, we buy quality through cycles
- [X] Entiendo el negocio mejor -- P/B vs ROE framework reveals clear undervaluation
- [X] Mercado sobre-reacciona -- ACGL -6.8% while producing record results is overreaction to cycle fears
- [X] Informacion publica mal interpretada -- P/E 8.6x looks "distressed" but is normal for insurer with high float leverage; P/B is the correct metric

---

## Growth Projections

### TAM Analysis
- Global P&C insurance TAM: $2.5T, growing 2-3% real per year
- Global reinsurance TAM: ~$400B, growing 3-5% (climate risk expanding TAM)
- US mortgage insurance TAM: ~$40B premiums, tied to housing origination (~$2T/year)
- ACGL addressable: $500B+ across three segments
- ACGL current premiums: ~$18B (~3-4% of addressable)

### Book Value Growth Projection (PRIMARY metric for insurers)

| Component | Historical | Base Case | Bear Case | Bull Case |
|-----------|-----------|-----------|-----------|-----------|
| Underwriting ROE contribution | ~10-14% | ~10-12% | 6-8% | 14-16% |
| Investment income ROE contribution | ~5-7% | 5-6% | 4-5% | 6-7% |
| Share buybacks (accretion) | 5-6% | 4-5% | 2-3% | 5-6% |
| **Total BVPS growth** | **15-22%** | **12-15%** | **8-10%** | **16-20%** |

**Derivation:**
- **Underwriting:** Even with softening, 85-88% combined ratio generates 12-15% return on allocated capital. Bear case: major cat year + deep softening pushes CR to 92-95%.
- **Investment income:** $30B+ portfolio at ~4% yield. Rates staying elevated per Fed trajectory. Minimal risk here.
- **Buybacks:** $1.9B in 2025 (5.6% of shares). At current P/B (~1.5x), buybacks are highly accretive. Management said they'll be "pretty active."
- **Reinvestment:** Surplus capital deployed into expanding specialty lines where pricing is still attractive.

### Premium Growth Projection

| | FY2025 | FY2026E | FY2027E | FY2028E |
|--|--------|---------|---------|---------|
| Total Revenue | $18.8B | $18.0-19.5B | $19-21B | $20-23B |
| Revenue Growth | +12.9% | -4% to +4% | +5-8% | +5-8% |

Revenue may dip slightly in 2026 as ACGL deliberately sheds unprofitable reinsurance volume. This is POSITIVE for book value (preserving capital > growing revenue). Revenue re-accelerates as cycle turns.

### WACC Derivation (for reference, though P/B is primary valuation)

```
Risk-Free Rate: 4.4% (US 10Y)
ERP: 5.0%
Beta: 0.38 (yfinance) -- LOW beta, defensive
Ke = 4.4% + 0.38 * 5.0% = 6.3%

ACGL has no meaningful debt cost (net cash).
Effectively, WACC = Ke = ~6.3-6.6%

ROE - Ke = 17.1% - 6.6% = +10.5pp spread (EXCELLENT)
```

---

## Valuation

### Insurance-Specific Framework: P/B vs ROE is PRIMARY

For insurers, book value IS equity value. The correct valuation is:

**Justified P/B = (ROE - g) / (Ke - g)**

### Method 1: P/B vs ROE (60% weight)

**Inputs:**
- Sustainable ROE: 15-17% (conservative; FY2025 operating ROE 17.1%, 5-year avg ~19.5%)
- Cost of equity (Ke): 6.6% (derived above, beta 0.38)
- Sustainable growth (g): 3% (terminal book value growth from reinvested earnings)

**Calculation:**

| Scenario | ROE | Ke | g | Justified P/B | BVPS | FV/share |
|----------|-----|-----|---|---------------|------|----------|
| **Bear** | 12% (deep softening + cat year) | 7.5% | 2.5% | 1.90x | $65 | $124 |
| **Base** | 15% (normalized cycle) | 6.6% | 3.0% | 3.33x | $65 | $117* |
| **Bull** | 18% (hard market returns) | 6.0% | 3.0% | 5.00x | $65 | $173* |

*Note: The Gordon Growth formula produces very high justified P/B because ACGL's ROE >> Ke. This is mathematically correct but practically, P/B multiples are capped by market willingness to pay. Let me reality-check with historical P/B:

**Historical P/B for ACGL:**
- 5-year median: 1.64x
- Current: ~1.53x ($99.85 / $65.11 BVPS)
- Historical range: 1.2x - 2.5x

The formula says justified P/B is 3.33x in the base case, but the market has NEVER paid that for ACGL because:
1. Insurance earnings are cyclical
2. Cat risk creates permanent capital loss potential
3. Market applies a structural discount to insurance book value

**Practical fair P/B approach:**

Given ROE 17% vs Ke 6.6%, ACGL deserves a PREMIUM P/B vs the sector (sector avg ~1.0-1.3x P/B for 10-12% ROE). A fair premium for an insurer with:
- ROE 17% vs sector 10-12%
- Net cash vs typical leverage
- 15%+ BVPS CAGR since 2001
- Three diversified platforms

**Fair P/B range: 1.7x (conservative) to 2.0x (justified)**

| Scenario | Fair P/B | BVPS Dec 2025 | FV/share |
|----------|----------|---------------|----------|
| Bear | 1.3x | $65.11 | $85 |
| Base | 1.85x | $65.11 | $120 |
| Bull | 2.2x | $65.11 | $143 |

**Using P/B method: Fair Value = $120 (base case)**

### Method 2: Earnings Power Value / P/E Relative (40% weight)

**Normalized EPS derivation:**
- FY2025 operating EPS: $9.84
- FY2024 EPS: $11.47 (higher due to lower cat losses)
- FY2023 EPS: $11.94
- 3-year average: $11.08
- Normalized mid-cycle EPS estimate: $10.50 (conservative, below average)

**Fair P/E for ACGL:**
- Sector P/E: 13.6x (US insurance)
- ACGL historical average P/E: ~10-12x
- Premium deserved: ACGL has superior ROE, underwriting discipline, and growth
- Fair P/E: 11-12x on normalized earnings (modest premium to history)

| Scenario | Normalized EPS | Fair P/E | FV/share |
|----------|---------------|----------|----------|
| Bear | $8.00 (soft market + cat) | 9x | $72 |
| Base | $10.50 | 12x | $126 |
| Bull | $13.00 (hard market) | 13x | $169 |

**Using P/E method: Fair Value = $126 (base case)**

### Reconciliation

| Method | Fair Value | Weight | Weighted |
|--------|-----------|--------|----------|
| P/B vs ROE | $120 | 60% | $72.00 |
| P/E Relative | $126 | 40% | $50.40 |
| **Weighted Avg** | | **100%** | **$122** |

Rounding to $120 for conservatism (below weighted average).

**Divergence between methods: 5% -- EXCELLENT convergence.**

---

## Escenarios

| | Bear (25%) | Base (50%) | Bull (25%) |
|--|------------|------------|------------|
| Assumption | Deep soft market + major cat year. CR rises to 95%. ROE drops to 10-12%. BVPS flat. | Normal cycle transition. CR 86-90%. ROE 14-16%. BVPS grows 10-12%. | Hard market returns on cat event. CR 80-84%. ROE 18-20%. BVPS grows 18%+. |
| Fair Value | $85 | $120 | $155 |
| MoS vs current $99.85 | -15% (overvalued in bear) | +20% | +55% |

### Expected Value

EV = ($85 x 0.25) + ($120 x 0.50) + ($155 x 0.25)
EV = $21.25 + $60.00 + $38.75
**EV = $120.00**

### MoS Calculation

- **vs Base: +20%** ($99.85 vs $120)
- **vs Bear: -15%** ($99.85 vs $85)
- **vs EV: +20%** ($99.85 vs $120)

---

## MoS Assessment

- vs Base: 20%
- vs Bear: -15%
- Precedents for Tier B: 20-25% typical MoS
- Current MoS of 20% is at the LOW END of Tier B precedents

**Reasoning:** The 20% MoS is adequate but not exceptional for Tier B because:
1. ACGL has best-in-class underwriting discipline (reduces downside risk vs typical Tier B)
2. Net cash position provides safety cushion
3. The bear case ($85) is still above tangible book value -- limited permanent capital loss risk
4. BUT cycle softening is REAL and duration uncertain
5. Comparable precedent: GL at $125 had similar MoS range, also insurance

**Verdict: MoS is ADEQUATE at current price. An entry at $90-95 (25-28% MoS) would be COMPELLING.**

---

## Entry Price Reasoning

| Entry Level | Price | MoS | Reasoning |
|-------------|-------|-----|-----------|
| Full position | $90-95 | 21-25% | Compelling for Tier B with ACGL's quality |
| Initial position | $95-100 | 17-20% | Acceptable for R1, wait for confirmation |
| Standing order | $88-92 | 23-27% | Ideal entry for standing order |

**Recommended standing order: $92 (23% MoS, well within comfort zone for Tier B insurer with superior quality)**

---

## Kill Conditions

1. **Combined ratio exceeds 100% for 2 consecutive years** -- would indicate underwriting discipline breakdown, the core moat
2. **ROE falls below 10% for 2 consecutive years** -- would mean the compounding engine is broken; historical ROE never dropped this low except in anomalous catastrophe years
3. **Management abandons underwriting discipline** -- pursuing premium growth over profitability; evidence would be rising GPW while CR deteriorates
4. **Major adverse reserve development** -- prior year reserves insufficient, retroactive hit to book value >10%
5. **Mortgage insurance book impairment** -- US housing market crash causing large MI losses (2008-style); ACGL has strengthened underwriting standards since then but monitor delinquency trends
6. **Share buybacks at elevated P/B (>2.5x)** while underwriting margins deteriorate -- would signal poor capital allocation under new CEO
7. **Book value per share DECLINES for 2 consecutive years** (excluding major cat years) -- the fundamental compounding metric must be positive

---

## Catalizadores

| Catalyst | Timeframe | Probability | Impact |
|----------|-----------|-------------|--------|
| Q1 2026 earnings confirm disciplined cycle management | 0-3 months | High | +10-15% re-rating |
| Cat event causes industry losses, re-hardens market | 0-18 months | Medium | +20-30% (ACGL benefits from hard market) |
| Buyback accretion continues at 5%+ pace | 0-12 months | High | Steady 5% BVPS accretion |
| US housing recovery boosts MI segment | 6-24 months | Medium | +5-10% from MI volume |
| Cycle turns, market recognizes ACGL premium | 12-36 months | Medium | Multiple re-rating to 1.8-2.0x P/B |

---

## Macro Connection

| Factor | Sensitivity | Impact for ACGL |
|--------|-------------|----------------|
| Interest rates | POSITIVE | Higher rates = higher investment income. Fed on hold at 3.5-3.75% is excellent for ACGL's $30B+ investment portfolio |
| Recession | Low-Medium | Insurance premiums are inelastic short-term. Claims may increase but reserves well-established |
| Inflation | Medium | Loss cost inflation pressures combined ratio, BUT ACGL has pricing power to offset via rate increases |
| USD strength | Low | ACGL is US-domiciled, mostly US revenue. No significant FX risk for our EUR-based portfolio |
| Climate change | HIGH (but manageable) | Cat losses trend higher, but ACGL's disciplined underwriting and retrocession management limits downside. Climate EXPANDS TAM long-term |

**Fit with World View:** NEUTRAL-FAVORABLE
- Mid-cycle US economy supports premium volumes
- Elevated rates boost investment income
- Inflation pressures offset by pricing power
- Not correlated with our existing portfolio (no insurance exposure beyond ALL and GL)
- US geographic exposure is DIVERSIFYING for our portfolio (currently EU-heavy)

---

## Portfolio Context

- Current insurance sector allocation: ~6-7% (ALL + GL)
- Adding ACGL would increase to ~10-11% (within sector view recommendation of max ~10%)
- US exposure would increase (FAVORABLE -- currently underweight US)
- ACGL has LOW correlation to our existing positions (specialty reinsurer vs ALL P&C personal, GL life/health)
- ACGL is higher quality than both ALL (QS 56) and GL (QS 52) -- represents quality UPGRADE within insurance allocation
- If capital constrained, ACGL could REPLACE ALL or GL via rotation (Principio 9: Quality Gravitation)

---

## Autocritica and Critical Thinking

### Assumptions
1. Sustainable ROE of 15-17% may be optimistic if soft market is deep and prolonged
2. P/B valuation depends on sustained high ROE -- if ROE normalizes to 12%, fair P/B drops to ~1.3x ($85)
3. Mortgage segment assumed stable but US housing is rate-sensitive
4. New CEO Papadopoulo assumed to maintain discipline -- limited track record as CEO

### Sesgos Detectados
1. **Recency bias** -- FY2025 was exceptional (22.6% BVPS growth). I may be anchoring to recent results rather than full-cycle averages
2. **Quality bias** -- ACGL's reputation as best-in-class may cause me to overweight moat durability
3. **Screening context** -- ACGL came from preliminary screening data suggesting P/E 8.6x is "distressed" -- it may simply be appropriate for this point in the cycle

### Evidence Ignored
1. Revenue MISSED in Q4 2025 -- insurance NPW declined 4%
2. Reinsurance pricing down -15% at Jan 2026 -- this is the steepest decline since 2014
3. Some analysts (KBW) expect property cat rates to decline approaching -20%
4. CEO transition from a founder-type leader is always higher risk than acknowledged

### Validation
- Book value per share: CONFIRMED at $65.11 via multiple sources
- Combined ratio: CONFIRMED at 82.8% FY2025, 80.6% Q4 2025
- Buyback: CONFIRMED $1.9B in 2025, $349M additional in early 2026
- ROE: CONFIRMED 17.1% operating, 22.6% total return on equity (includes unrealized gains)
- Share count: CONFIRMED ~372M outstanding

---

## Veredicto: WATCHLIST -- Standing Order at $92

ACGL is a high-quality specialty insurer at a reasonable (but not exceptional) valuation. The 20% MoS at current price is adequate for Tier B, but given cycle uncertainty and the bear case showing -15% downside, a standing order at $92 (23% MoS) provides better risk/reward discipline. The business quality is among the best I have analyzed in insurance -- superior to both ALL and GL in our current portfolio.

**Next steps for pipeline:**
- R2: moat-assessor (quantify underwriting discipline moat, competitive positioning vs RNR, AXIS, Everest)
- R2: risk-identifier (quantify cat exposure, reserve adequacy, cycle duration risk)
- R2: valuation-specialist (independent P/B vs ROE validation)
- R3: devil's-advocate (challenge cycle resilience assumption, test bear case)
- R4: investment-committee (if price approaches $92-95)

---

## META-REFLECTION

### Incertidumbres/Dudas
- The quality_scorer.py ROIC calculation is structurally broken for ALL insurance/financial companies. The tool shows ROIC 7.3% and ROIC-WACC spread as NaN, when ROE is 17-23%. This affects not just ACGL but also ALL, GL, and any future insurer we analyze. The +11 adjustment I applied is conservative but somewhat subjective.
- I cannot determine with certainty whether the current P/B of 1.53x is "cheap" or "appropriate." ACGL's 5-year median P/B is only 1.64x, so 1.53x is only a 7% discount to median. The high justified P/B from the Gordon Growth model (3.33x) suggests massive undervaluation, but the market has never paid that.
- Mortgage insurance segment is a "black box" -- the 34% combined ratio seems too good to be sustainable but has been stable for 4+ years. If US housing cracks, this is the hidden risk.

### Sugerencias de Mejora
- **quality_scorer.py needs an --insurer flag** that uses ROE instead of ROIC, combined ratio instead of gross margin, and P/B-appropriate leverage metrics. This would fix structural underscoring for ALL insurance companies in our universe. Priority: HIGH -- affects pipeline decisions.
- **valuation-methods skill should include a dedicated P/B vs ROE section** for financials with worked examples and historical calibration tables. Current P/B section is minimal.
- **insurance.md sector view should be updated** with ACGL as pipeline candidate and Jan 2026 renewal pricing data.

### Anomalias Detectadas
- ACGL's beta is 0.38 -- extremely low for a company that is -6.8% over 52 weeks while the Dow is +7.1%. The low beta makes WACC/Ke very low (6.3-6.6%) which makes the justified P/B very high. This might overstate fair value. A beta of 0.6-0.8 (more typical for insurers) would give Ke of 7.4-8.4% and justified P/B of 1.7-2.3x -- still above current but less extreme.
- FCF of $6.6B in 2024 for a $36B market cap company implies FCF yield of 18%. This is ANOMALOUS for any quality company. But for insurers, FCF includes premium cash flows that are matched by growing reserves -- it overstates "free" cash available. Do not use FCF-based valuation for ACGL.

### Preguntas para Orchestrator
1. Should we prioritize ACGL R2 given it overlaps with our existing insurance allocation (ALL, GL)? Or is the quality upgrade argument sufficient?
2. The quality_scorer.py --insurer flag would benefit the entire system -- should we prioritize this over other backlog items?
3. Given 44% cash and ACGL at $99.85, is a standing order at $92 too conservative? Current price already offers 20% MoS.

---

## Sources

- [Arch Capital Q4 2025 Results](https://www.stocktitan.net/news/ACGL/arch-capital-group-ltd-reports-2025-fourth-quarter-xyveznrieped.html)
- [Arch Capital Q4 2025 Earnings Transcript - Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/02/10/arch-capital-acgl-q4-2025-earnings-transcript/)
- [Arch Capital Q4 2025 Earnings Highlights - GuruFocus](https://www.gurufocus.com/news/8603402/arch-capital-group-ltd-acgl-q4-2025-earnings-call-highlights-strong-income-growth-and-strategic-capital-management)
- [ACGL Book Value Per Share - GuruFocus](https://www.gurufocus.com/term/book-value-per-share/ACGL)
- [Reinsurance Prices Sharper Softening - Artemis](https://www.artemis.bm/news/reinsurance-prices-show-sharper-softening-than-anticipated-at-jan-renewals-moodys-ratings/)
- [Property Cat Reinsurance Down 14.7% - Howden Re](https://www.artemis.bm/news/property-cat-reinsurance-down-14-7-retrocession-down-16-5-at-jan-2026-renewals-howden-re/)
- [KBW Property Cat Rate Decline 15-20%](https://beinsure.com/news/drop-cat-reinsurance-rates-renewals/)
- [Arch Capital Measured Underwriting - Seeking Alpha](https://seekingalpha.com/article/4867947-arch-capitals-measured-underwriting-is-underappreciated)
- [Marc Grandisson Insider Activity - TipRanks](https://www.tipranks.com/experts/insiders/marc-grandisson)
- [Insurance Market 2026 Outlook - AmWINS](https://www.amwins.com/resources-and-insights/market-insights/article/state-of-the-market-2026-outlook)
- [Arch Capital Group - Wikipedia](https://en.wikipedia.org/wiki/Arch_Capital_Group)
