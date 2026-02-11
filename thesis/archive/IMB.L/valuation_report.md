# INDEPENDENT VALUATION REPORT: IMB.L (Imperial Brands PLC)

**Agent:** valuation-specialist (adversarial review)
**Date:** 2026-02-08
**Type of Company:** Dividend aristocrat / Secular decline industry
**Quality Score:** 54/100 (Tier C) per quality_scorer.py
**Methods Selected:** DDM (primary) + EV/EBIT Normalized (secondary) + FCF Yield cross-check

---

## CRITICAL FINDING: Quality Score Discrepancy

### Thesis Claims: QS 9.5/10 (Tier A)
### Tool Reports: QS 54/100 (Tier C)

**This is a MASSIVE discrepancy that fundamentally changes the risk profile.**

#### Breakdown of quality_scorer.py Output (54/100):

| Category | Score | Max | Key Issue |
|----------|-------|-----|-----------|
| Financial Quality | 15 | 40 | ROIC Spread only 2.1pp (thesis claims 25-30% ROIC, but tool measures ~7% vs 4.9% WACC); FCF Margin 9.8% (low vs revenue base of GBP 32B because excise taxes inflate reported revenue) |
| Growth Quality | 15 | 25 | Revenue CAGR and EPS CAGR marked N/A (data gaps); GM expanding is the one positive |
| Moat Evidence | 14 | 25 | GM Premium -1.1pp vs sector (surprising for tobacco); ROIC persistence estimated |
| Capital Allocation | 10 | 10 | Perfect score: 10yr+ dividend history, 6.1% insider ownership |

#### Why QS is 54 and Not 95:

1. **ROIC Spread is low (2.1pp):** The tool calculates ROIC from reported financials. Tobacco companies report gross revenue including excise taxes (~GBP 23B in excise on GBP 32B reported revenue), which inflates the capital base and depresses ROIC when measured on total assets/equity. The thesis's claim of "ROIC 25-30%" likely uses net revenue and adjusts for the capital-light model. The REAL ROIC on *net* revenue capital is indeed high, but the tool's measurement is mechanistically correct on reported numbers.

2. **FCF Margin 9.8%:** Same issue. FCF of GBP 2.7B / Revenue GBP 32B = 8.4%. But FCF / Net Revenue (~GBP 8.3B) = 32.5%, which is exceptional. The tool does not adjust for excise pass-through.

3. **Revenue CAGR N/A:** Data gaps prevent calculation. In reality, tobacco net revenue has grown 2-4% consistently.

4. **GM Premium -1.1pp:** Compared to "Consumer Defensive" sector broadly, not tobacco peers specifically. Tobacco margins are structurally different from food/beverage.

#### My Assessment of True Quality:

The quantitative tool is PENALIZING IMB.L because tobacco economics are distorted by excise tax pass-through. However, the thesis's 9.5/10 is also INFLATED because it ignores:
- Secular volume decline (structural headwind)
- GBP 8.4B net debt in a declining industry
- Regulatory risk (UK generational smoking ban)
- Limited growth optionality vs true compounders

**My independent QS estimate: 60-65 (Tier B)** -- better than the tool's 54 but NOT Tier A.

Rationale: Excellent capital allocation (10/10), strong cash generation, wide moat from addiction + regulation. But penalized by secular decline, debt, and limited growth. This is a high-quality cash cow, not a quality compounder.

---

## Method 1: DDM (Primary -- 60% weight)

DDM is the most appropriate method for a mature tobacco dividend stock with predictable cash flows and a progressive dividend policy.

### Parameter Derivation

**D0 (Current Annual Dividend):** 160.32p (FY25, confirmed)

**Required Return (Ke):**

The thesis uses 9%. Let me derive independently.

- Risk-Free Rate: 4.50% (UK 10Y Gilt)
- Equity Risk Premium: 4.50%
- Beta: The thesis uses 0.139 (yfinance) but acknowledges it is "unusually low." Zacks reports 0.69. Historical tobacco sector beta averages 0.5-0.8.

**Beta analysis:** IMB.L's yfinance beta of 0.139 is almost certainly an artifact of:
- Low trading volume periods
- Defensive nature during volatile markets
- Possible calculation methodology differences

A 5-year beta of 0.5-0.7 is more realistic for tobacco. I will use **0.65** as my base case (middle of tobacco range).

```
Ke = 4.50% + (0.65 x 4.50%) = 7.43%
```

This is LOWER than the thesis's 9%. However, 9% as a "required return" from an investor perspective is reasonable given:
- Secular decline risk
- Regulatory risk
- ESG liquidity premium

**I will use 8.5% as my base Ke** -- a compromise between theoretical CAPM (7.4%) and investor hurdle (9%). The 110bp premium over CAPM reflects secular decline risk.

**Dividend Growth Rate (g):**

The thesis uses 4.5% (company guidance). Let me stress-test this.

Imperial's dividend growth is funded by:
- FCF growth: Revenue growth 2-4% + margin stability = FCF growth ~3-4%
- Buyback-enhanced EPS growth: ~2-3pp from share count reduction
- Payout ratio sustainability: 160.32p / 315p adj EPS = 50.9% payout -- conservative

Sustainable dividend growth = ROE x (1 - Payout) = est. 22% x 0.49 = 10.8% (theoretical max)

But in a DECLINING volume industry, reinvestment opportunities are limited. Actual growth is constrained by top-line:
- Revenue growth: +2-3% (pricing net of volume decline)
- Operating leverage: minimal (+0.5pp)
- Buyback contribution to DPS: +2-3%
- Total DPS growth capacity: ~4-6%

Company guidance: low-to-mid single digit DPS growth.

**My g estimates:**
- Bear: 2.5% (volume decline accelerates, pricing resistance, regulatory pressure)
- Base: 3.5% (below company guidance of 4.5% -- they always guide optimistically)
- Bull: 4.5% (company guidance achieved, NGP adds growth)

### DDM Calculation

**Gordon Growth Model: FV = D1 / (Ke - g)**

| Scenario | g | Ke | D1 | Fair Value | MoS vs 3,341p |
|----------|---|----|----|-----------|----------------|
| Bear | 2.5% | 9.5% | 164.33p | 2,348p | -29.7% |
| Base | 3.5% | 8.5% | 165.93p | 3,319p | -0.7% |
| Bull | 4.5% | 8.0% | 167.53p | 4,787p | +43.3% |

**DDM Expected Value (25/50/25):** (2,348 x 0.25) + (3,319 x 0.50) + (4,787 x 0.25) = **3,443p**

**CRITICAL OBSERVATION:** The DDM is extremely sensitive to the spread between Ke and g. Moving g by just 1pp changes FV by ~40%. This makes DDM unreliable as a precision tool here.

### DDM Sensitivity Table

| Ke \ g | 2.0% | 2.5% | 3.0% | 3.5% | 4.0% | 4.5% |
|--------|------|------|------|------|------|------|
| **7.5%** | 2,979p | 3,317p | 3,725p | 4,232p | 4,892p | 5,773p |
| **8.0%** | 2,719p | 2,998p | 3,327p | 3,725p | 4,219p | 4,858p |
| **8.5%** | 2,506p | 2,742p | 3,015p | 3,339p | 3,732p | 4,215p |
| **9.0%** | 2,327p | 2,529p | 2,762p | 3,035p | 3,359p | 3,723p |
| **9.5%** | 2,173p | 2,348p | 2,547p | 2,776p | 3,046p | 3,370p |
| **10.0%** | 2,039p | 2,191p | 2,362p | 2,557p | 2,783p | 3,046p |

**Observation:** The thesis's DDM of 3,723p requires BOTH 9% required return AND 4.5% growth. At my base case (8.5%/3.5%), I get 3,339p -- essentially today's price. At 9%/3.5%, I get 3,035p (below current price).

---

## Method 2: EV/EBIT Normalized (Secondary -- 25% weight)

### Normalized EBIT

FY25 Adjusted Operating Profit: GBP 4,091M (+4.6% YoY)
FY24: GBP 3,911M
FY23: GBP ~3,750M (estimated from growth trajectory)

5-year average (est.): ~GBP 3,700-3,900M
I will use FY25 as forward-looking: GBP 4,091M

### Peer Multiple Comparison

| Company | P/E | EV/EBITDA | EV/EBIT (est) | Div Yield | Notes |
|---------|-----|-----------|---------------|-----------|-------|
| IMB.L | 13.4x | ~8.1x | ~9.5x | 4.8% | Smallest of big tobacco |
| BATS.L (BAT) | 33.2x* | 8.8x | ~10x | 5.2% | *Inflated trailing; fwd ~12x |
| PM (Philip Morris) | 25.2x* | 15.7x | ~18x | 3.2% | Premium for IQOS/growth; fwd ~19x |
| MO (Altria) | 15.9x | 10.3x | ~11x | 6.5% | US-only, highest yield |

*BAT and PM have inflated trailing P/E due to one-time items; forward P/E is more representative.

**Sector median EV/EBIT:** ~10-11x (excluding PM's premium)

**Appropriate multiple for IMB.L:**
- Base: Sector median 10x (IMB is not premium but not worst)
- Adjustments:
  - (-1x) Smallest scale, least NGP progress vs PMI
  - (-0.5x) Higher regulatory risk (UK generational ban)
  - (+0.5x) Strong buyback/capital return discipline
  - Net adjustment: -1x

**My EV/EBIT multiple: 9x**

### Calculation

```
Normalized EBIT: GBP 4,091M
EV = GBP 4,091M x 9 = GBP 36,819M
Net Debt: GBP 8,400M (FY25: 8,406M)
Equity Value = GBP 36,819M - GBP 8,400M = GBP 28,419M
Shares Outstanding: ~787M (estimated from market cap / price)
FV per share = 28,419M / 787M x 100 = 3,611p
```

**EV/EBIT Scenarios:**

| Scenario | Multiple | EV (GBP M) | Equity (GBP M) | FV/share |
|----------|----------|-----------|----------------|----------|
| Bear | 7.5x | 30,683 | 22,283 | 2,831p |
| Base | 9.0x | 36,819 | 28,419 | 3,611p |
| Bull | 10.5x | 42,956 | 34,556 | 4,391p |

---

## Method 3: FCF Yield (Cross-check -- 15% weight)

FCF yield is a direct measure of what the business generates for equity holders.

### Parameters

- FY25 FCF: GBP 2,700M (reported)
- Shares outstanding: ~787M
- FCF per share: ~343p

Note: The thesis claims FCF per share of 316p. The difference may be due to one-time items or timing. I use 343p based on GBP 2.7B total FCF.

### Target FCF Yield

Tobacco stocks historically trade at 8-11% FCF yield due to secular decline risk. Current IMB.L FCF yield: 343p / 3,341p = 10.3%.

| Target FCF Yield | Implied FV | MoS |
|-----------------|-----------|-----|
| 8% (growth premium) | 4,288p | +28.3% |
| 9% (fair for stable) | 3,811p | +14.1% |
| 10% (current) | 3,430p | +2.7% |
| 11% (decline discount) | 3,118p | -6.7% |

**My assessment:** A 9.5-10% FCF yield is FAIR for a company in secular decline with GBP 8.4B of debt. The market is pricing IMB.L approximately correctly on this measure.

| Scenario | Target Yield | FV |
|----------|-------------|-----|
| Bear | 11% | 3,118p |
| Base | 10% | 3,430p |
| Bull | 8.5% | 4,035p |

---

## Reconciliation

| Method | Bear FV | Base FV | Bull FV | Weight |
|--------|---------|---------|---------|--------|
| DDM | 2,348p | 3,319p | 4,787p | 60% |
| EV/EBIT | 2,831p | 3,611p | 4,391p | 25% |
| FCF Yield | 3,118p | 3,430p | 4,035p | 15% |

### Weighted Fair Values

| Scenario | DDM (60%) | EV/EBIT (25%) | FCF Yield (15%) | Weighted FV |
|----------|-----------|---------------|-----------------|-------------|
| Bear | 1,409p | 708p | 468p | **2,584p** |
| Base | 1,991p | 903p | 515p | **3,409p** |
| Bull | 2,872p | 1,098p | 605p | **4,575p** |

### Expected Value (probability-weighted)

```
Expected FV = (Bear x 25%) + (Base x 50%) + (Bull x 25%)
            = (2,584 x 0.25) + (3,409 x 0.50) + (4,575 x 0.25)
            = 646 + 1,705 + 1,144
            = 3,494p
```

**Divergence between methods (base case):**
- DDM: 3,319p
- EV/EBIT: 3,611p
- FCF Yield: 3,430p
- Range: 3,319 - 3,611p (spread: 8.8% -- well within 30% threshold)

All three methods converge in the 3,300-3,600p range for the base case. This is encouraging for reliability.

---

## Comparison with Thesis Valuation

| Metric | Thesis | Independent | Delta |
|--------|--------|-------------|-------|
| DDM Base | 3,723p | 3,319p | **-10.9%** |
| DDM Bear | 2,752p | 2,348p | **-14.7%** |
| DCF Bear | 3,821p | N/A (DCF inappropriate*) | -- |
| Blended FV | 3,701p | 3,409p | **-7.9%** |
| Expected FV | 3,602p | 3,494p | **-3.0%** |

*The thesis's DCF produced inflated values (base case 5,038p, bear 3,821p) because the tool uses total FCF without appropriately adjusting for the declining nature of the business. DCF is inherently biased upward for cash-generative declining businesses because it projects current FCF forward and applies a terminal value that assumes perpetual cash flows.

### Key Differences in Parameters

| Parameter | Thesis | Independent | Why Different |
|-----------|--------|-------------|---------------|
| Dividend growth (g) | 4.5% | 3.5% | Thesis uses company guidance uncritically; I haircut by ~1pp for secular decline risk |
| Required return (Ke) | 9.0% | 8.5% | Thesis rounds up; my CAPM-derived with risk premium lands at 8.5% |
| DDM FV | 3,723p | 3,319p | Combined effect of lower g AND different Ke |
| Quality Tier | Tier A (9.5/10) | Tier B-C (60-65) | Thesis uses subjective scoring; tool says 54 |
| DCF weight | 40% | 0% | DCF is inappropriate for declining-volume business as primary method |

---

## Peer Valuation Validation

| Metric | IMB.L | BAT | Altria | PMI |
|--------|-------|-----|--------|-----|
| P/E (trailing) | 13.4x | 33.2x* | 15.9x | 25.2x* |
| P/E (forward) | ~11x | ~12x | ~11x | ~19x |
| EV/EBITDA | ~8.1x | 8.8x | 10.3x | 15.7x |
| Dividend Yield | 4.8% | 5.2% | 6.5% | 3.2% |
| FCF Yield | 10.3% | ~8% | ~8% | ~5% |

*BAT and PM have one-time distortions in trailing P/E.

**IMB.L trades at a discount to peers** on most metrics. This discount is partially justified by:
1. Smallest scale among big tobacco
2. Least advanced NGP transition (vs PMI's IQOS)
3. Higher UK regulatory exposure (generational ban)
4. Management transition (new CEO/CFO named)

But partially unjustified because:
- FCF generation is excellent (10.3% yield vs 5-8% for peers)
- Capital return discipline is best-in-class (GBP 10B in 4 years)
- Leverage is lower than BAT (2.0x vs 2.7x)

**My implicit P/E at base FV 3,409p:** 3,409 / 315 = 10.8x (adjusted EPS) -- reasonable vs peer range of 11-12x forward.

---

## Risk Assessment for Valuation

### UK Generational Smoking Ban

**Status:** The Tobacco and Vapes Bill passed second reading (415-47 votes, Nov 2024). Expected to become law in 2027. Bans tobacco sales to anyone born after 1 Jan 2009.

**Impact on IMB.L:**
- UK is a priority market but ~15% of tobacco revenue
- Impact is GRADUAL (only affects new would-be smokers, not existing)
- Volume impact: estimated additional -0.5 to -1pp per year of UK decline starting ~2030
- Net effect on total company: modest (-0.2 to -0.4pp total volume impact)
- BUT: Precedent risk if other countries follow (Germany, Spain, Australia are priority markets)

**Valuation impact:** Included in bear case via lower growth and higher required return. Does NOT justify a kill condition today.

### GBP 8.4B Net Debt

- Net Debt / EBITDA: 2.0x (manageable)
- Interest coverage: >6x
- No refinancing crisis risk
- BUT: In a declining industry, debt optionality is reduced vs growing companies
- Debt must be serviced from declining volume base
- **Conclusion:** Not a crisis, but limits shareholder returns ceiling and adds fragility

### Volume Decline Acceleration Risk

- Global cigarette volumes declining ~3% per year
- If decline accelerates to 5%+ (regulatory, cultural shift), pricing power may not fully compensate
- Historical evidence: pricing power has held for 50+ years
- Key indicator to watch: price elasticity trends in priority markets

---

## Final Valuation Summary

```
VALUATION: IMB.L (Imperial Brands PLC)

Type of company: Dividend aristocrat / secular decline cash cow
Quality: Tier B-C (QS 54-65 depending on methodology)
Methods: DDM (60%) + EV/EBIT (25%) + FCF Yield (15%)

Scenarios:
| Scenario | Fair Value | Probability |
|----------|-----------|-------------|
| Bear     | 2,584p    | 25%         |
| Base     | 3,409p    | 50%         |
| Bull     | 4,575p    | 25%         |
| Expected | 3,494p    | 100%        |

Current Price: 3,341p
MoS vs Expected: +4.6%
MoS vs Base: +2.0%
MoS vs Bear: -22.7%

THESIS FV INFLATION: Thesis blended 3,701p vs Independent 3,409p = -7.9%
(Less severe than portfolio average of -20.8%, because IMB.L
was already conservatively valued relative to other positions)
```

---

## Conviction Assessment

| Factor | Assessment |
|--------|-----------|
| Quality | Tier B-C (60-65), NOT Tier A as thesis claims |
| MoS at current price | ~2-5% (essentially fairly valued) |
| MoS vs Bear case | Negative (-22.7%) -- NO downside protection |
| Dividend safety | HIGH -- 51% payout, GBP 2.7B FCF covers GBP 1.3B dividend 2x |
| Forward return potential | Dividend 4.8% + DPS growth 3.5% + modest multiple expansion = 8-10% |
| Conviction | LOW-MEDIUM |

**The stock is approximately fairly valued.** It is not a compelling value at 3,341p. It is not dangerously overvalued either. It is a reasonable hold for income, but NOT a position that should be in a portfolio targeting quality compounders (Principio 9).

---

## 🔄 META-REFLECTION

### Dudas/Incertidumbres
- The QS discrepancy (54 vs thesis 9.5/10) is primarily a METHODOLOGY issue, not a quality issue. The quality_scorer.py tool penalizes tobacco because excise taxes distort revenue-based metrics. However, even adjusting for this, IMB.L is NOT Tier A -- it is Tier B at best.
- DDM sensitivity is extreme. A 1pp change in either g or Ke swings FV by 30-40%. This makes precision impossible. The valuation range is wide (2,584 - 4,575p), which reflects genuine uncertainty.
- I could not find the H1 FY26 trading update content (only the LSE listing reference). The FY26 guidance of 3-5% adj OP growth is the most recent forward-looking data.
- Beta is unreliable (yfinance 0.139, Zacks 0.69, TradingView 0.00-0.20). I used 0.65 which is a tobacco sector average estimate.

### Sensibilidad Preocupante
- DDM FV changes by ~400p for every 1pp change in growth rate at 8.5% Ke. This means the difference between "undervalued" and "overvalued" is literally one percentage point of dividend growth.
- If dividend growth is 4.5% (company guidance) vs my 3.5%, FV jumps from 3,319p to 4,215p. The ENTIRE bull/bear debate hinges on whether 3.5% or 4.5% is the right long-term growth.

### Discrepancies with Thesis
- Thesis FV 3,701p vs my 3,409p (-7.9%). Less inflation than average (-20.8%) because the thesis was already somewhat conservative on DCF and used a reasonable DDM framework.
- The BIGGEST discrepancy is quality classification: thesis says Tier A (9.5/10), I say Tier B-C (60-65). This matters enormously for portfolio construction under Principio 9 (Quality Gravitation).
- Thesis uses DCF with 40% weight producing inflated values (base 5,038p). I replace DCF with EV/EBIT which gives more grounded results.

### Sugerencias para el Sistema
- The quality_scorer.py tool should be enhanced to handle tobacco/excise-intensive businesses that report gross revenue including excise taxes. A flag or sector-specific adjustment would prevent false-low QS readings.
- DDM-based valuations should ALWAYS include the full sensitivity table to highlight how sensitive the output is to small parameter changes.

### Preguntas para Orchestrator
1. Given that IMB.L is Tier B-C (not Tier A), and MoS is only 2-5%, does this position "earn its place" under Principio 9? The forward return (~8-10% total) is decent but not compelling vs Tier A alternatives with 15%+ expected returns.
2. Should we set a TRIM trigger if price approaches 3,500p (near our base FV) to take profits and redeploy to Tier A?
3. The adversarial review average FV inflation is -20.8%, but IMB.L shows only -7.9%. Should we treat this as confirmation that the original thesis was relatively sound, or just that the methods used (DDM-heavy) happen to be more conservative than DCF-heavy approaches used elsewhere?
---
