# Allstate Corporation (ALL)

> Actualizado: 2026-02-08 (Adversarial Review v4.0)
> Status: HOLD ON PROBATION
> Confianza: LOW
> Quality Score: 56/100 (Tier B)

## TL;DR

Allstate is #2 US homeowners and #4 auto insurer. Q4 2025 earnings were exceptional ($14.31 EPS vs $9.85 consensus, combined ratio 72.9%), but this is PEAK CYCLE. Adversarial review found: QS 56 Tier B (thesis claimed "8/10 Tier A" -- WRONG), normalized ROE 15-18% (not 37%), Arity data privacy litigation completely absent from thesis, Senate claims fraud hearing absent, voluntary 17% rate cuts for 7.8M customers. Independent FV $234, risk-adjusted FV $214. MoS 3-11% -- thin for Tier B. HOLD ON PROBATION because position is tiny (3.5%, $400), freed capital marginal, no specific replacement. Q1 2026 earnings is the decision point.

---

## Adversarial Review Summary (2026-02-08)

### Quality Score Correction

| Component | Thesis Claimed | Actual Score | Gap |
|-----------|---------------|-------------|-----|
| Financial Quality | ~32/40 | 23/40 | -9 pts |
| Growth Quality | ~20/25 | 13/25 | -7 pts |
| Moat Evidence | ~20/25 | 14/25 | -6 pts |
| Capital Allocation | ~8/10 | 6/10 | -2 pts |
| **TOTAL** | **~80/100 (Tier A)** | **56/100 (Tier B)** | **-24 pts** |

Key issue: ROIC spread only 0.4pp (barely above WACC). ROE 37% is leverage-amplified and peak-cycle.

### Fair Value Revision

| Source | Fair Value | MoS at $207.55 |
|--------|-----------|----------------|
| Original Thesis | $240 | 13.5% |
| Independent Valuation (base) | $234 | 11.3% |
| Risk-adjusted | $214 | 3.1% |
| Bear case | $166 | -25.0% |

Methods: P/B vs ROE (60%, normalized ROE 16%, BV $108.45) + P/E normalized (40%, 10x on $23.30 EPS). Excellent convergence ($235 vs $233).

### Risks NOT in Original Thesis

1. **Arity/Data Privacy Litigation** (CRITICAL) -- TX AG first-ever TDPSA enforcement + class actions, 45M consumers, $7,500/violation theoretical exposure
2. **Senate hearing on "systematic fraud" in claims handling** (HIGH) -- bipartisan congressional scrutiny
3. **Voluntary 17% premium cuts for 7.8M customers** (HIGH) -- material margin compression 2026
4. **Morgan Stanley + TD Cowen downgrades Jan 2026** (MEDIUM)
5. **Progressive market share surge to 17% vs ALL 10.2%** (MEDIUM) -- gap accelerating
6. **California wildfire $1.1B exposure (Jan 2025)** not quantified in thesis

### Peak Cycle Evidence

- Combined ratio FY2025: 85.2% vs 10-year average ~97%. Not sustainable.
- ROE FY2025: ~38% vs 10-year median 11.5%, normalized 15-18%
- Consensus EPS drops 39% from $38 (2025) to $23 (2026)
- Management guiding mid-90s auto combined ratio for 2026
- P&C sector entering soft market (2025-2026 transition)

---

## EXIT Protocol Applied (2026-02-08)

```yaml
exit_analysis:
  ticker: ALL
  date: 2026-02-08

  gates:
    gate_1_kill_condition: "NO -- None of 5 kill conditions triggered"
    gate_2_thesis_valid: "DEBILITADA -- QS overstated, peak-cycle profitability, undocumented risks"
    gate_3_mos_current: "3-11% -- thin for Tier B. Precedent MoS for Tier B: 20-25% typical"
    gate_4_opportunity_score: "OS ~3.8 vs generic Tier A -- but freed capital ($340) is marginal"
    gate_5_dead_money: "NO -- up 6% in 12 days, fresh position"
    gate_6_friction: "~1-2% -- low but meaningful vs tiny position"

  recommendation: "HOLD ON PROBATION"

  rationale: |
    Thesis debilitated but not invalidated. Position tiny (3.5%, $400).
    Freed capital ($340) would add to already-large cash pile ($2,715).
    No specific Tier A alternative that needs this exact capital.
    Q1 2026 earnings will be decisive for cycle turn assessment.
    LIGHT.AS precedent (QS 56, SOLD) differs because there was a specific replacement.
    DTE.DE precedent (QS 48, HOLD) is more similar -- small position, no replacement.

  precedents_consulted:
    - "LIGHT.AS - QS 56, MoS 8.4%, SOLD for BYIT.L (specific replacement)"
    - "DTE.DE - QS 48, HOLD MEDIUM (no immediate replacement, similar situation)"
    - "SHEL.L - QS 36, SOLD for AUTO.L (specific replacement available)"
```

---

## El Negocio

**Modelo:** Property & Casualty insurance (auto + hogar principalmente)

**Revenue Breakdown (2024):**
- Property-Liability Insurance: Core business (auto + hogar)
- Auto Insurance: Fuente principal, #4 US con 10.2% market share
- Homeowners Insurance: #2 US con 8.9% market share
- Protection Services: $2.0B revenue anual, 160M policies
- Investment Income: $3.1B (2024, +24.8% YoY)

**Escala:**
- FY2025 Net Income: $10.2B (exceptional)
- FY2025 EPS: $38.06 (peak cycle)
- Market cap: ~$54B (P/E 5.5x TTM)
- Book Value/share: $108.45 (Q4 2025)

**Competidores:**
1. State Farm (leader, private)
2. Progressive (#3 auto, 17% market share, gaining aggressively)
3. GEICO (Berkshire, pricing bajo)
4. Liberty Mutual, USAA, others

---

## Moat

**Rating: NARROW (unchanged)**

**Strengths:**
- Brand Recognition: "You're In Good Hands" + AM Best A+ rating
- Scale: #2 homeowners, #4 auto, $57B revenue base
- Distribution: Multi-channel (agents + direct)
- Data: Arity subsidiary for telematics (BUT under litigation)

**Weaknesses:**
- Pricing Power LIMITED: P&C insurance is commodity-like
- Switching Costs LOW: Online comparison trivial
- Progressive gaining share faster (17% vs 10.2%)
- Arity competitive advantage at risk from litigation

---

## Financials (Updated Q4 2025)

| Metric | FY2025 | FY2024 | FY2023 | Notes |
|--------|--------|--------|--------|-------|
| Net Income | $10.2B | $4.6B | -$0.3B | Peak cycle 2025 |
| EPS (diluted) | $38.06 | $30.84 | N/A | -39% expected 2026 |
| Combined Ratio | 85.2% | 94.3% | 104.5% | Exceptional 2025 |
| ROE | ~38% | ~23% | ~-1% | Normalized: 15-18% |
| Book Value/share | $108.45 | ~$80 | ~$72 | Grew 35% in FY2025 |
| Investment Income | $3.1B+ | $3.1B | - | Stable with rates |
| Dividend | $4.32/yr | $4.00/yr | - | 33yr streak, +8% raise |
| Buyback program | $4B new | - | - | Capital returns strong |

**Critical note:** FY2025 earnings are NOT repeatable. Management guided mid-90s auto CR for 2026. Consensus EPS FY2026: $23.30 (range $19.85-$28.67).

---

## Valoracion (Adversarial -- 2026-02-08)

### Method 1: P/B vs ROE (60% weight)

```
Normalized ROE: 16% (range 13-20%, vs thesis 22%, vs peak 38%)
Ke: 9.0% (Rf 4.3% + Beta 0.85 * ERP 5.5%)
g: 3%
P/B Justified: (16% - 3%) / (9% - 3%) = 2.17x
BV/share: $108.45
FV = 2.17 * $108.45 = $235
```

### Method 2: P/E Normalized (40% weight)

```
Normalized EPS: $23.30 (FY2026 consensus)
P/E Justified: 10x (conservative vs sector 10-13x)
FV = 10 * $23.30 = $233
```

### Reconciliation

| Method | Bear | Base | Bull | Weight |
|--------|------|------|------|--------|
| P/B vs ROE | $170 | $235 | $347 | 60% |
| P/E Normalized | $160 | $233 | $312 | 40% |
| **Weighted** | **$166** | **$234** | **$333** | **100%** |

Divergence: 0.9% (excellent convergence)

### Margin of Safety

| vs Benchmark | FV | MoS |
|-------------|-----|------|
| Base Weighted | $234 | 11.3% |
| Risk-adjusted | $214 | 3.1% |
| Bear case | $166 | -25.0% |
| Expected (prob-weighted) | $242 | 14.2% |

---

## Riesgos (Adversarial Assessment -- 10 risks identified)

### CRITICAL (2)
1. **Arity/Data Privacy Litigation** -- TX AG + class actions, 45M consumers. Settlement range $200M-$1B. If Arity model banned = moat erosion.
2. **Competitive Pricing + Voluntary Rate Cuts** -- 7.8M customers avg 17% rate cut. Progressive at 17% share vs ALL 10.2%. Soft market approaching.

### HIGH (2)
3. **Climate/CAT Losses Structural Trend** -- $1.1B CA fires (Jan 2025). 6th year >$100B global insured losses. +5-7% annual trend.
4. **Senate hearing / federal claims legislation** -- Bipartisan scrutiny, adjusters testifying about estimate manipulation.

### MEDIUM (3)
5. **CEO $26M compensation + claims controversy** -- Governance/reputational risk.
6. **Softening P&C market cycle (2026-2028)** -- Combined ratio normalizing upward.
7. **State-level rate regulation** -- Limits pricing flexibility.

### LOW (3)
8. **Limited MoS after price appreciation** -- Near 52-week high.
9. **Insider selling pattern** -- CEO monthly under 10b5-1 plan.
10. **Tariffs on auto parts** -- Pass-through to premiums with lag.

---

## Kill Conditions (Updated)

1. Combined ratio > 100% for 2 consecutive quarters
2. Arity business model permanently banned across multiple states
3. Federal claims practice legislation passes
4. CEO departure without succession plan
5. Market share drops below 9% in auto

**Model Disruption Kill Conditions (added 2026-02-11):**
6. **Autonomous vehicles eliminate personal auto insurance TAM >10%** — If AVs (Waymo, Tesla FSD, Cruise) achieve Level 4+ deployment at scale AND shift liability to manufacturers/fleet operators, personal auto insurance premiums decline structurally. ALL gets ~80% of premiums from auto. Even a 10% TAM reduction = $4-5B premium loss. Monitor: AV deployment rates, state-by-state liability law changes, L4 regulatory approvals.
7. **Embedded insurance at point-of-sale disintermediates carriers** — If Tesla, Apple Car, or auto dealers bundle insurance at purchase with captive carriers (Tesla Insurance model expanding), ALL loses customer acquisition channel. The moat is brand + agent network; if insurance is bundled and invisible, brand doesn't matter. Monitor: Tesla Insurance state expansion, OEM embedded insurance programs, ALL agent count trends.

---

## Position Parameters

```
Conviction: LOW
Fair Value: $234 (independent base)
Risk-Adjusted FV: $214
Price: $207.55
MoS vs Base: 11.3%
MoS vs Risk-Adjusted: 3.1%
Position Size: 3.5% ($400 invested)

Exit Plan:
  - SELL if Q1 2026 combined ratio > 97%
  - SELL if Arity settlement > $1B or model permanently restricted
  - SELL if Tier A alternative identified that specifically needs capital
  - ADD trigger: $180 or below (MoS > 23%, appropriate for Tier B)

Next Review: Q1 2026 earnings (~May 2026)
```

---

## Fuentes

### Q4 2025 Earnings
- [Allstate Q4 Insurance Journal](https://www.insurancejournal.com/news/national/2026/02/05/856975.htm)
- [Allstate $10.2B Net Income](https://collisionweek.com/2026/02/05/allstate-reports-10-2-billion-net-income-2025/)
- [Allstate Q4 Earnings Call](https://seekingalpha.com/article/4866513-the-allstate-corporation-all-q4-2025-earnings-call-transcript)

### Arity/Data Privacy
- [Texas AG Sues Allstate and Arity](https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-allstate-and-arity-unlawfully-collecting-using-and-selling-over-45)
- [Class Action Consolidated](https://www.bfalaw.com/cases/in-re-allstate-arity-consumer-privacy-litigation)

### Senate Hearing / Claims
- [Allstate Blasted at Senate Hearing](https://www.spglobal.com/market-intelligence/en/news-insights/articles/2025/5/allstate-state-farm-blasted-at-senate-hearing-over-claims-practices-88993421)
- [Systematic Fraud Alleged](https://insurancenewsnet.com/innarticle/systematic-fraud-alleged-in-property-casualty-claims-practices)

### Competition
- [Morgan Stanley Downgrades ALL](https://www.investing.com/news/analyst-ratings/morgan-stanley-downgrades-allstate-stock-to-equalweight-amid-competitive-auto-market-93CH-4409870)

### Valuation Data
- [Allstate ROE Historical](https://www.macrotrends.net/stocks/charts/ALL/allstate/roe)
- [Allstate BV/share GuruFocus](https://www.gurufocus.com/term/book-value-per-share/ALL)
- [Allstate Combined Ratio GuruFocus](https://www.gurufocus.com/term/combined-ratio_pct/ALL)
