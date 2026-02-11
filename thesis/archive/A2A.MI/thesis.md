# ARCHIVED: 2026-02-08
# Exit reason: Adversarial review - QS 37 Tier C (thesis claimed Tier A), ROIC -3.0pp, FV inflated 24%
# P&L: -1.5% (EUR -5)
# Adversarial FV: EUR 2.04 vs thesis EUR 2.70
# See portfolio/history.yaml for full exit record

# Original thesis content below.

# A2A S.p.A. (A2A.MI) - Investment Thesis v2.0

**Date:** 2026-02-03
**Analyst:** Claude (Fundamental Analyst + Review Agent)
**Status:** ARCHIVED (was ACTIVE)
**Framework Version:** 2.0 (post-revaluation)
**Tier:** A (Defensive Utility) - requires 15% MoS minimum
**ADVERSARIAL CORRECTION:** quality_scorer.py shows QS=37 (Tier C), NOT Tier A

---

## 1. Executive Summary

A2A S.p.A. is Italy's second-largest multi-utility by revenue, operating across energy generation/distribution, waste management, district heating, and water services. Headquartered in Brescia, Lombardy, the company benefits from regulated concessions, regional density, and a vertically integrated circular economy model. Municipal ownership by Milan and Brescia (25% each) provides governance stability.

**Recommendation:** HOLD at current price EUR 2.53 (validated 2026-02-03)

**Key Metrics (updated 2026-02-03):**
| Metric | Value | Source |
|--------|-------|--------|
| Price | EUR 2.53 | price_checker.py (yfinance) |
| Market Cap | EUR 7.9B | price_checker.py |
| Trailing P/E | 9.7x | price_checker.py |
| Forward P/E | ~10-11x | H1 2025 guidance extrapolation |
| Dividend Yield | 4.0% (EUR 0.10/share) | price_checker.py |
| 52-Week High/Low | EUR 2.744 / EUR 1.894 | price_checker.py |
| Beta | 0.94 | Yahoo Finance |
| Net Debt/EBITDA | 2.3x | H1 2025 report |

---

## Adversarial Review Summary (2026-02-08)

| Metric | Thesis v2.0 | Adversarial | Delta |
|--------|-------------|-------------|-------|
| QS / Tier | 6.5/10 self-assessed "Tier A" | 37/100 Tier C | CRITICAL ERROR |
| Fair Value Base | EUR 2.70 | EUR 2.04 | -24.4% |
| Fair Value Bear | EUR 2.20 | EUR 1.55 | -29.5% |
| EBIT used | EUR 1,500M | EUR 1,250M | -16.7% |
| ROIC spread | "PARCIAL" | -3.0pp (destroying value) | CRITICAL |
| MoS at exit | 6.3% | -24.5% (OVERVALUED) | CRITICAL |

Key issues found by adversarial review:
1. Thesis self-assigned Tier A, actual QS = 37 (Tier C)
2. EBIT overstated by 25% (EUR 1,500M vs actual ~EUR 1,200M)
3. ROIC below WACC = value destruction
4. AGCM antitrust investigation not in thesis
5. Net debt +24% in FY2024 not mentioned
6. 3% annual margin compression not mentioned
7. DDM unreliable with negative FCF (dividends funded by borrowing)

See: risk_assessment.md and valuation_report.md for full adversarial analysis.

---

[Original thesis sections 2-13 omitted for brevity - see risk_assessment.md and valuation_report.md for the adversarial corrections]
