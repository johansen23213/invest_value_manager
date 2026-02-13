# UHS - Adversarial Valuation Report
> Date: 2026-02-07 | Adversarial Review Fase 1
> Analyst: Orchestrator (manual, agents hit rate limit)

---

## Current Data

| Metric | Value | Source |
|--------|-------|--------|
| Price | $218.56 | price_checker.py |
| 52w High | $246.33 | price_checker.py |
| 52w Low | $152.33 | price_checker.py |
| P/E | 10.4x | price_checker.py |
| Market Cap | $13.9B | price_checker.py |
| Net Debt | $5.0B | dcf_calculator.py |
| Quality Score | 51/100 (Tier C) | quality_scorer.py |
| ROIC Spread | +1.2pp | quality_scorer.py |

---

## Thesis FV Challenge

### Thesis Claims: $283.74 (blended DCF 50% + EV/EBITDA 50%)

### Issues Identified

**1. DCF Weight Too High:**
- FCF coefficient of variation = 2.3 (tool flagged as "highly volatile")
- DCF gives $313.58 (base) but EV/EBITDA gives only $253.89
- This $60 gap suggests DCF is unreliable for UHS
- Thesis gives DCF 50% weight — should be lower given volatility

**2. EV/EBITDA Bear Case:**
- At 6.5x multiple: FV = $207.70 → only 2.8% upside from thesis price ($201.86)
- At current price $218.56: EV/EBITDA bear FV $207.70 is **5% BELOW current price**
- This means downside protection is essentially zero in bear case

**3. FV vs Consensus:**
- Thesis FV: $283.74
- Analyst consensus: $250.41 (20 analysts)
- DCF tool base: $266.55
- Thesis is the most optimistic of all sources

---

## Independent Valuation

### Method 1: DCF (via dcf_calculator.py, default parameters)

| Scenario | FV | MoS vs $218.56 |
|----------|-----|-----------------|
| Bear (3%/10%/2%) | $193.42 | **-11.5%** |
| Base (5%/9%/2.5%) | $266.55 | +22.0% |
| Bull (7%/8%/3%) | $370.19 | +69.4% |

**WARNING:** Bear case is $193.42 = 11.5% BELOW current price. No downside protection.

Given FCF volatility (CV 2.3), I weight DCF at only 30% (not 50% as thesis).

### Method 2: EV/EBITDA (Updated with Q3 2025 data)

Q3 2025 annualized EBITDA: ~$3.0B (based on Q3 revenue $4.5B at ~11% op margin + D&A)

| Multiple | EV | Equity | FV/share | MoS |
|----------|-----|--------|---------|-----|
| 6.5x (bear) | $19.5B | $14.5B | $208 | -4.8% |
| 7.5x (base) | $22.5B | $17.5B | $251 | +14.9% |
| 8.0x (bull) | $24.0B | $19.0B | $273 | +24.9% |

**Multiple justification:**
- Sector median: 7.5x
- HCA (premium peer): 8-9x
- UHS discount for: smaller scale, marginal ROIC, DOJ oversight, dual-class
- Fair multiple: 7.0-7.5x

### Method 3: P/E Cross-Check

| Scenario | EPS | P/E | FV |
|----------|-----|-----|-----|
| FY2025E ($21.80 consensus) | $21.80 | 12x (historical median) | $261.60 |
| FY2026E ($23.52 consensus) | $23.52 | 11x (applying slight discount) | $258.72 |
| Bear (FY2025 at 10x) | $21.80 | 10x | $218.00 |

**Note:** Current P/E 10.4x on TTM earnings. Forward P/E ~10x on FY2025E. For a company with 1.2pp ROIC spread, 10x P/E may be approximately fair.

### Reconciliation

| Method | Weight | Bear FV | Base FV | Bull FV |
|--------|--------|---------|---------|---------|
| DCF | 30% | $193 | $267 | $370 |
| EV/EBITDA | 50% | $208 | $251 | $273 |
| P/E cross-check | 20% | $218 | $260 | N/A |
| **Weighted** | **100%** | **$205** | **$256** | **$300** |

### Risk-Adjusted FV

Applying 5% discount for: DOJ oversight, ROIC uncertainty, governance

**Risk-Adjusted Base FV: ~$243**

At $218.56, MoS vs $243 = **~10%**
At $218.56, MoS vs bear $205 = **-6.6% (negative!)**

---

## Comparison: Thesis vs Adversarial

| Metric | Thesis | Adversarial | Delta |
|--------|--------|-------------|-------|
| Base FV | $283.74 | $243 | **-14.4%** |
| Bear FV | $217.36 | $205 | -5.7% |
| MoS (at current price) | ~23% | ~10% | -13pp |
| DCF weight | 50% | 30% | -20pp |
| EV/EBITDA weight | 50% | 50% | same |
| Conviction | HOLD | HOLD LOW | Lower |

---

## Earnings Feb 26 Decision Framework

| Scenario | Result | Action |
|----------|--------|--------|
| **Q4 BEAT + strong 2026 guidance** | EPS >$5.70, FY2026 guidance >$24 | HOLD. Confirms Q3 inflection, ROIC improving |
| **Q4 INLINE** | EPS ~$5.50, FY2026 guidance ~$23.50 | HOLD. Status quo, thin MoS |
| **Q4 MISS** | EPS <$5.00 or guidance <$22 | EXIT ANALYSIS. Would push bear FV below $200 |
| **Labor cost warning** | Margin guidance down | TRIM or SELL. ROIC likely < WACC |
| **Behavioral health slowdown** | BH revenue growth <5% | HOLD cautiously. Secular thesis weakened |

---

## Sensitivity Analysis

| WACC | FV (DCF base) | MoS |
|------|-------------|-----|
| 7.5% | $303 | +38.6% |
| 8.0% | $284 | +29.9% |
| 8.5% (thesis) | $267 | +22.0% |
| 9.0% (default) | $252 | +15.3% |
| 9.5% | $238 | +8.9% |
| 10.0% | $226 | +3.4% |

At WACC 10% (appropriate for a cyclical healthcare services company with marginal ROIC), DCF FV = $226, MoS = only 3.4%.

---

## META-REFLECTION

### Key Insight
UHS thesis FV of $283 was ~14% inflated, similar to MONY.L (-27%) and EDEN.PA (-24.5%) findings. The pattern is consistent: thesis FVs are systematically optimistic.

### The Core Question
UHS is a Tier C position with ROIC barely > WACC, ~10% MoS after adversarial adjustment, and DOJ oversight not factored into the thesis. Is this position earning its place?

Arguments FOR holding:
- P&L is positive (+8.5%, $34 gain)
- Operational execution is excellent (Q3 beat, guidance raised)
- No kill conditions
- Earnings Feb 26 could provide catalyst

Arguments AGAINST holding:
- QS 51, Tier C — portfolio gravitating to Tier A
- ROIC spread 1.2pp — marginal
- Risk-adjusted MoS only ~10%
- Capital could compound faster in a Tier A position

### Verdict
HOLD through earnings Feb 26. The Q4 results will determine direction. If Q4 confirms Q3 inflection (margins expanding, ROIC improving), the investment case strengthens. If Q4 disappoints, the thin MoS doesn't justify holding a Tier C position.
