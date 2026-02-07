# DTE.DE - Adversarial Valuation Report
> Date: 2026-02-07 | Adversarial Review Fase 1
> Analyst: Orchestrator (manual, agents hit rate limit)

---

## Current Data

| Metric | Value | Source |
|--------|-------|--------|
| Price | EUR 30.26 | price_checker.py |
| 52w High | EUR 35.91 | price_checker.py |
| 52w Low | EUR 26.00 | price_checker.py |
| P/E | 12.3x | price_checker.py |
| Dividend Yield | 3.0% | price_checker.py |
| Market Cap | EUR 150.7B | price_checker.py |
| Net Debt | EUR 139.12B | dcf_calculator.py |
| Quality Score | 48/100 (Tier C) | quality_scorer.py |

---

## Thesis FV Challenge

### Thesis Claims: EUR 36.50-38.50

**Method weights:** DCF 35% + EV/EBITDA 45% + SOTP 20%

### Issues Identified

**1. WACC Problems:**
- Thesis derived WACC as 3.9% (extremely low)
- Then manually overrode to 6.5% (arbitrary)
- Beta used: 0.29 → adjusted to 0.5 (another manual override)
- Neither the raw 3.9% nor the override 6.5% has proper justification

**2. Revenue Growth:**
- Thesis claims 4% revenue growth
- Actual 5Y revenue CAGR: 1.8% (quality_scorer.py)
- Q3 2025 organic growth: 3.3% (improving but still below thesis assumption)
- Guidance confirms improvement but historical track record is 1.8%

**3. SOTP Methodology:**
- Thesis counts 51.5% of TMUS market cap at par (EUR 78B)
- No holding company discount applied
- Standard holding company discount: 10-25%
- With 15% discount: TMUS contribution = EUR 66B (not EUR 78B)
- SOTP then = EUR 146B vs EUR 158B → EUR 29.30/share (not EUR 31.73)

---

## Independent Valuation

### Method 1: DCF (via dcf_calculator.py, default parameters)

| Scenario | FV | MoS vs EUR 30.26 |
|----------|-----|------------------|
| Bear (3%/10%/2%) | EUR 30.59 | +1.1% |
| Base (5%/9%/2.5%) | EUR 45.78 | +51.3% |
| Bull (7%/8%/3%) | EUR 67.31 | +122.4% |

**Caution:** Default parameters may be too generous. With DTE-specific inputs:
- Growth 3% (between historical 1.8% and guidance 3.3-4%): FV drops
- WACC 7-8% (more realistic for leveraged telecom): FV drops significantly

DCF is EXTREMELY sensitive to WACC for DTE because of the massive terminal value relative to near-term cash flows.

### Method 2: EV/EBITDA (Thesis Method, Verified)

Using thesis figures:
- EBITDA: ~EUR 50.4B (FY2025 guidance EUR 45.3B for EBITDA AL — need to reconcile)
- Net Debt: EUR 139.12B

| Multiple | EV | Equity Value | FV/share |
|----------|-----|-------------|---------|
| 5.5x (bear) | EUR 277B | EUR 138B | EUR 27.70 |
| 6.0x (conservative) | EUR 302B | EUR 163B | EUR 32.73 |
| 6.5x (base) | EUR 328B | EUR 189B | EUR 37.95 |
| 7.0x (bull) | EUR 353B | EUR 214B | EUR 42.97 |

**Note:** At current 4.85x multiple, DTE trades at a discount to EU telecom sector (5.5-6.5x). The question is whether this discount is justified.

### Method 3: Analyst Consensus

| Source | Target | Rating |
|--------|--------|--------|
| 18 analysts consensus | EUR 37.44 | Strong Buy |
| Range | EUR 33-42 | |

### Reconciliation

| Method | Bear FV | Base FV | Bull FV |
|--------|---------|---------|---------|
| DCF (defaults) | EUR 30.59 | EUR 45.78 | EUR 67.31 |
| EV/EBITDA | EUR 27.70 | EUR 32.73-37.95 | EUR 42.97 |
| Analyst consensus | EUR 33 | EUR 37.44 | EUR 42 |
| Thesis | EUR 28-30 | EUR 36.50-38.50 | EUR 45-50 |

**Risk-adjusted FV (my assessment):**

Given Tier C quality and the various risks identified:
- Weight EV/EBITDA more heavily (DCF too sensitive to WACC assumptions)
- Apply 10% discount to thesis for: ROIC uncertainty, leverage, growth overstated
- Conservative: EUR 30-33 (EV/EBITDA 5.5-6.0x)
- Base: EUR 33-36 (EV/EBITDA 6.0-6.5x with slight discount)
- Optimistic: EUR 37-40 (thesis range)

**Risk-Adjusted FV: EUR 33-35 (midpoint EUR 34)**

At EUR 30.26, MoS vs risk-adjusted EUR 34 = **~11%**

---

## Comparison: Thesis vs Adversarial

| Metric | Thesis | Adversarial | Delta |
|--------|--------|-------------|-------|
| Quality Tier | A | C | -2 tiers |
| FV Base | EUR 36.50-38.50 | EUR 33-35 | -9 to -12% |
| MoS (current) | 19-21% | ~11% | -8 to -10pp |
| WACC | 6.5% | 7-8% appropriate | +50-150bp |
| Growth | 4% | 1.8-3.3% | -0.7 to -2.2pp |
| Conviction | ALTA | MEDIUM | Lower |

---

## Earnings Feb 26 Decision Framework

| Scenario | Result | Action |
|----------|--------|--------|
| **BEAT + raised guidance** | Revenue >EUR 30B, EBITDA >EUR 45.5B | HOLD. Catalyst for re-rate toward EUR 33-35 |
| **INLINE** | Revenue ~EUR 29B, EBITDA ~EUR 45.3B | HOLD. Status quo, thin MoS |
| **MISS** | Revenue <EUR 28.5B, EBITDA <EUR 45B | EXIT ANALYSIS. Bear FV EUR 27-30, no margin |
| **Guidance cut** | FY2026 guidance disappoints | SELL trigger. Thesis dependent on growth improving |
| **Dividend cut** | Below EUR 1.00 | SELL immediately (kill condition per thesis) |

---

## META-REFLECTION

### Key Insight
DTE.DE is a "comfortable hold" that shouldn't be: it's Tier C with thin MoS (~11%), priced near fair value in bear scenarios, and the thesis overclaims quality. It survives because it's defensive and generates real FCF.

### Principle 9 Question
"Is DTE.DE the best use of this capital?" At 6.4% allocation and EUR 735 invested:
- Forward expected return: ~11% MoS + ~3% yield + ~2-3% growth = ~16-17% total
- This is mediocre for a Tier C position
- But it's not destroying value (unlike TEP.PA, LIGHT.AS, PFE exits)
- No immediate rotation candidate available

### Recommendation
HOLD MEDIUM conviction. Not urgent to exit but on the watch list for rotation if a better Tier A opportunity emerges. Earnings Feb 26 = decision point.
