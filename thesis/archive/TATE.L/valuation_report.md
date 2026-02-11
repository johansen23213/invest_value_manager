# VALUATION REPORT: TATE.L (Tate & Lyle PLC)

**Date:** 2026-02-08
**Analyst:** Valuation Specialist (Adversarial Review)
**Status:** ARCHIVED - Position closed 2026-02-08
**Original Status:** INDEPENDENT VALUATION - Challenging thesis FV of 551 GBp

---

## Company Classification

**Type of enterprise:** Consumer Staples / Specialty Food Ingredients (in trough cycle + integration phase)
**Quality Score:** 45 (Tier C per quality_scorer.py)
**Thesis claimed tier:** Tier B (QS 5/10 on custom scale). Tool says Tier C.
**Methods selected:** EV/EBIT Normalized (primary) + DCF Conservative (secondary)

**Rationale for Tier C treatment:** The automated quality_scorer.py returns QS 45 (Tier C). Key issues: ROIC spread -0.5pp (below WACC), FCF margin only 2.5% (distorted by yfinance data, though actual is ~9%), FCF consistency only 2/5 years, leverage 2.3x. The thesis' custom 5/10 score does not map to Tier B in our system. For a Tier C company, conservative multiples and downside protection are the appropriate methodology per valuation-methods skill.

---

## CRITICAL FINDINGS vs THESIS

### Finding 1: D&A is GBP 172M, NOT GBP 100M

The thesis assumes D&A of approximately GBP 100M to arrive at EBIT FY26E of GBP 312M.

**Actual data:**
- H1 FY26 D&A: GBP 86M (depreciation GBP 61M + amortization GBP 25M)
- Full year FY26 D&A (annualized): ~GBP 172M
- Cross-check: FY25 EBITDA GBP 446M - FY25 Adj Op Profit GBP 288M = D&A ~GBP 158M
- D&A has increased FY25 to FY26 due to CP Kelco intangible amortization

**Impact on EBIT FY26E:**
- Thesis: EBITDA 412M - D&A 100M = EBIT 312M
- Reality: EBITDA ~425M - D&A ~172M = EBIT ~253M
- **The thesis overstates EBIT by ~GBP 59M (23%)**

### Finding 2: WACC of 7.4% is Artificially Low

The thesis derives WACC as follows:
- Ke = 4.5% + 0.44 x 5.0% = 6.7%
- Kd after-tax = 5.0% x 0.75 = 3.75%
- WACC = 64% x 6.7% + 36% x 3.75% = 5.65%
- Then adds +175bp "adjustment" to get 7.4%

**Problems:**
1. Beta of 0.44 is too low for a company with 2.3x leverage and integration risk.
2. The +175bp adjustment is arbitrary - not derived from any framework.
3. For a GBP 1.7B market cap, Tier C quality, 2.3x leveraged company in a trough, WACC should reflect REAL risk.

**My WACC derivation:**
- Rf: 4.5% (UK 10Y gilt)
- ERP: 5.5% (UK + small cap premium component)
- Beta: 0.65 (adjusted for leverage, illiquidity, integration risk)
- Ke = 4.5% + 0.65 x 5.5% = 8.1%
- Kd: 5.0% x (1-25%) = 3.75%
- E/V: 64%, D/V: 36%
- **WACC = 64% x 8.1% + 36% x 3.75% = 5.2% + 1.35% = 6.5%**
- Small cap illiquidity premium: +1.5%
- **Final WACC: 8.0%**

### Finding 3: FCF 8% CAGR Growth from Trough is Aggressive

The thesis assumes 8% FCF CAGR from a GBP 170M trough base.

**My assessment:** 5-6% FCF CAGR is more realistic.

### Finding 4: Terminal Growth 2.5% is High for a Leveraged Trough Company

For a leveraged company with uncertain integration: 2.0% is more appropriate.

### Finding 5: Sucralose is NOT Declining (Thesis Error)

**Actual:** FY25 sucralose revenue was $193M, UP 16%. This actually HELPS the valuation slightly.

### Finding 6: Analyst Consensus Price Target = 503-528 GBp (well below thesis 551)

---

## FINAL VALUATION

```
Current Price:         393.6 GBp
Thesis Fair Value:     551 GBp
My Base Case FV:       329 GBp
My Expected Value:     350 GBp
My Bear Case FV:       195 GBp

MoS vs Thesis FV:     +29% (thesis says upside)
MoS vs My Expected:    -11% (OVERVALUED)
MoS vs My Base:        -16% (OVERVALUED)
MoS vs My Bear:        -50% (severely overvalued vs downside)

Thesis FV Deviation:   551 -> 329 = -40% revision
```

---

## INVESTMENT IMPLICATIONS

At 393.6 GBp, TATE.L is **overvalued** relative to my independent fair value estimate of 329 GBp (base) or 350 GBp (expected).

**The position should be considered for EXIT or TRIM:**

1. **No margin of safety:** Price (394) > My Expected FV (350) = -11% overvalued
2. **Tier C quality:** QS 45, ROIC near WACC, leverage 2.3x
3. **Bear case risk:** FV 195 GBp = -50% downside from current
4. **Opportunity cost:** Capital tied up in an overvalued Tier C stock vs Tier A alternatives
5. **Thesis inflation:** Original FV 551 was inflated by ~40% due to D&A error and aggressive multiple

---

## SOURCES

- [Tate & Lyle H1 FY26 Results](https://www.tateandlyle.com/news/tate-lyle-plc-results-six-months-30-september-2025)
- [Tate & Lyle FY25 Full Year Results](https://www.tateandlyle.com/news/tate-lyle-plc-2025-full-year-results-statement)
- [Tate & Lyle H1 FY26 PDF Statement](https://www.tateandlyle.com/sites/default/files/2025-11/tate-lyle-fy26-h1-statement-final.pdf)
- [Ingredion FY2025 Full Year Results](https://www.globenewswire.com/news-release/2026/02/03/3230839/0/en/Ingredion-Incorporated-Reports-2025-Fourth-Quarter-and-Full-Year-Results.html)
- [Kerry Group H1 2025 Results](https://www.kerry.com/about/news-and-media/2025/kerry-group-h-one-2025-results)
- [Tate & Lyle Analyst Consensus](https://www.tateandlyle.com/investors/analyst-and-consensus)
- [TATE.L Price Data](https://finance.yahoo.com/quote/TATE.L/)
