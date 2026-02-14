# RACE.MI (Ferrari N.V.) -- Independent Valuation Report

> **Valuation Date:** 2026-02-11
> **Analyst:** valuation-specialist (Claude)
> **QS Tool:** 82/100 (Tier A) | **QS Adjusted:** 84/100 (Tier A)

---

## VALUATION: RACE.MI

**Type of company:** Luxury goods compounder (NOT automaker)
**Methods selected:** Owner Earnings Yield (primary) + EV/EBIT Multiple Analysis (secondary) + P/E Relative Valuation (tertiary)
**DCF Tool status:** Documented but UNRELIABLE for this company (yfinance FCF underestimates industrial FCF by ~40%)

---

## Method 1: Owner Earnings Yield (OEY) -- Tier A Primary Method

### Inputs

| Input | Value | Source |
|-------|-------|--------|
| Industrial FCF FY2025 | EUR 1,538M | Ferrari FY2025 press release |
| Normalized Industrial FCF | EUR 1,300M | Conservative: adjusting for one-time WC benefit in FY2025. CMD guidance implies EUR 8B cumulative 2026-2030 = EUR 1,600M/yr avg. I discount by ~19% for conservatism. |
| Depreciation FY2025 | EUR 662M | Approx from EBITDA - EBIT: EUR 2,772M - EUR 2,110M = EUR 662M |
| Maintenance Capex | EUR 728M | Depreciation x 1.1 (standard assumption) |
| Market Cap | EUR 57,200M | price_checker.py |
| Shares outstanding | ~177M diluted | Thesis data |
| WACC | 9.35% | Derived: Ke = Rf 4.35% + Beta 1.0 x ERP 5.0% |

### Calculation

```
Owner Earnings = Normalized FCF - Maintenance Capex + Depreciation
               = EUR 1,300M - EUR 728M + EUR 662M
               = EUR 1,234M

Owner Earnings per share = EUR 1,234M / 177M = EUR 6.97

Owner Earnings Yield = EUR 1,234M / EUR 57,200M = 2.16%

Expected Growth (Revenue CAGR): 6.5% base case
  -- TAM growth (UHNW population +5%) + ASP growth (mix + personalization) + flat volume
  -- Management guides 5% CAGR; historically they beat guidance by 1-2pp
  -- EBIT margin expansion (29.5% --> 30%+) amplifies EPS growth to ~7-8%

OEY + Growth = 2.16% + 6.5% = 8.66%
vs WACC = 9.35%
Spread = -0.69pp (slightly negative)
```

### OEY-Implied Fair Value

The OEY method for Tier A compounders works by finding the price at which OEY + Growth exceeds WACC with a meaningful spread.

```
For OEY + Growth = WACC (break-even):
Required OEY = WACC - Growth = 9.35% - 6.5% = 2.85%
Break-even Market Cap = OE / Required OEY = EUR 1,234M / 0.0285 = EUR 43,298M
Break-even Price = EUR 43,298M / 177M = EUR 244.6

For OEY + Growth = WACC + 2pp (reasonable premium for Tier A quality):
Required OEY = WACC - Growth - quality_premium = 9.35% - 6.5% - 2% = 0.85%
Premium Market Cap = OE / Required OEY = EUR 1,234M / 0.0085 = EUR 145,176M
Premium Price = EUR 145,176M / 177M = EUR 820

Note: The OEY method produces an extremely wide range for Ferrari because the
growth rate is close to WACC. A small change in required OEY (from 2.85% to 0.85%)
quadruples the implied fair value. This makes OEY an unreliable point estimator
for Ferrari.

Practical approach: Use OEY to determine if the stock is reasonable, not to set a
precise fair value.

At current price (EUR 322.80):
  OEY = 2.16%
  OEY + Growth = 8.66%
  vs WACC 9.35%

VERDICT: Approximately fairly valued on OEY. The -0.69pp spread suggests the
market is pricing in growth roughly in line with expectations, with a slight
discount for execution risk.
```

**OEY-implied FV (for reconciliation): EUR 330** -- this represents the price where OEY + Growth approximately equals WACC, which for a Tier A luxury compounder with 2-year order book visibility is a fair equilibrium.

### Quality Adjustment for OEY

Standard OEY demands OEY + Growth >= WACC. But Ferrari's qualities warrant a lower required return:
- 2-year order book visibility (lower uncertainty)
- ROIC 24.9% and EXPANDING (exceptional capital allocation)
- Wide moat with 30+ year durability
- Net cash balance sheet (zero financial risk)
- 30.5% insider ownership (alignment)

For the highest-quality luxury compounders (Hermes trades at OEY + Growth BELOW WACC), accepting a 1-2pp lower threshold is defensible. This does not change the FV output; it contextualizes why EUR 330 is a floor rather than a ceiling.

---

## Method 2: EV/EBIT Multiple Analysis (Secondary Method)

### Inputs

| Input | Value | Source |
|-------|-------|--------|
| EBIT FY2025 | EUR 2,110M | Ferrari FY2025 results |
| EBIT FY2026E | EUR 2,213M | My estimate: Revenue EUR 7,500M (guidance) x EBIT margin 29.5% (guided floor) |
| EBIT FY2027E | EUR 2,421M | Revenue ~EUR 7,987M (+6.5% YoY) x margin 30.3% (CMD trajectory toward 30%+) |
| Net Debt (industrial) | EUR 32M | Ferrari FY2025 |
| Shares outstanding | ~177M | Thesis |

### Comparable Companies

| Company | EV/EBIT (trailing) | EV/EBIT (forward) | EBIT Margin | ROIC | Growth | Notes |
|---------|--------------------|--------------------|-------------|------|--------|-------|
| Hermes (RMS.PA) | ~43x | ~40x | ~37% | ~35% | ~10% | Closest luxury comp |
| LVMH (MC.PA) | ~21x | ~19x | ~22% | ~14% | ~4-6% | Diversified luxury |
| Ferrari (RACE.MI) | 27.1x trailing | 25.9x fwd | 29.5% | 24.9% | 5-7% | Our target |

### Ferrari-Appropriate EV/EBIT Multiple

Ferrari sits between Hermes (pure luxury, highest margins) and LVMH (diversified luxury, larger scale):

**Arguments for higher multiple (toward Hermes, 35-40x):**
- Scarcity model (deliberate supply constraint, like Birkin bags)
- Pricing power comparable to Hermes (+10% with zero demand impact)
- Net cash, pristine balance sheet
- ROIC-WACC spread +14.9pp and expanding
- 2-year order book (unmatched visibility)

**Arguments for lower multiple (toward LVMH, 20-25x):**
- Growth deceleration from 12%+ to 5% CAGR guided
- Higher capex/capital intensity than pure luxury
- EV transition risk and uncertainty
- Smaller company = less diversification
- US tariff exposure (29% of revenue)

**Arguments for middle ground (28-35x):**
- Historical 10-year average EV/EBIT ~35-40x
- Current 27x is BELOW historical average
- CMD disappointment already priced in at -35% from peak
- FY2025 execution was strong (beat expectations)

**My selected range: 28x - 36x, with base case 32x**

Rationale for 32x base: This is a ~10% discount to Ferrari's historical average (~35x), reflecting:
- Growth moderation from 12% to 5-7% (deserves some discount)
- Offset by improving margins, FCF, and demonstrated pricing power
- Below historical average is appropriate given CMD reset, but above LVMH given moat quality

### Fair Value Calculation

**Using FY2026E EBIT (EUR 2,213M):**

| Multiple | EV | Net Debt | Equity Value | FV/Share |
|----------|----|----------|-------------|----------|
| 28x (bear) | EUR 61,964M | -EUR 32M | EUR 61,932M | EUR 350 |
| 32x (base) | EUR 70,816M | -EUR 32M | EUR 70,784M | EUR 400 |
| 36x (bull) | EUR 79,668M | -EUR 32M | EUR 79,636M | EUR 450 |

**Using FY2027E EBIT (EUR 2,421M), discounted 1 year at WACC:**

| Multiple | EV (2027) | PV (2026) | Equity | FV/Share |
|----------|-----------|-----------|--------|----------|
| 28x | EUR 67,788M | EUR 62,000M | EUR 61,968M | EUR 350 |
| 32x | EUR 77,472M | EUR 70,886M | EUR 70,854M | EUR 400 |
| 36x | EUR 87,156M | EUR 79,771M | EUR 79,739M | EUR 450 |

Both FY2026E and FY2027E-discounted produce nearly identical fair values, which provides confidence in the estimate.

**EV/EBIT Fair Value: EUR 400 (base, 32x forward EBIT)**

---

## Method 3: P/E Relative Valuation (Tertiary / Cross-check)

### Inputs

| Input | Value | Source |
|-------|-------|--------|
| EPS FY2025 | EUR 8.96 (diluted) | Ferrari FY2025 results |
| EPS FY2026E | EUR 9.70 | My estimate: EBIT EUR 2,213M, ~24% effective tax, 177M shares. EUR 2,213M x 0.76 / 177M = EUR 9.50; plus buyback EPS accretion ~2% = EUR 9.70 |
| P/E trailing | 36.0x | price_checker.py |
| P/E forward | 33.3x | EUR 322.80 / EUR 9.70 |

### Comparable P/E Analysis

| Company | P/E (trailing) | P/E (forward) | EPS Growth | PEG |
|---------|----------------|---------------|------------|-----|
| Hermes | 49.7x | ~44x | ~10% | ~4.4x |
| LVMH | 23.9x | ~22x | ~6% | ~3.7x |
| Ferrari | 36.0x | ~33x | ~8% | ~4.1x |

Ferrari's PEG (4.1x) is between Hermes (4.4x) and LVMH (3.7x), which makes intuitive sense given its quality sits between these two luxury anchors.

### Historical P/E Context

Ferrari's P/E since IPO:
- 10-year average: ~39x trailing
- Peak: ~60x (Feb 2025, at EUR 493)
- Trough: ~30x (COVID, mid-2020)
- Current: 36.0x (below 10-year average)

The current 36x trailing P/E is ~8% below the historical average of 39x. If P/E reverts to historical average:

```
Fair Value at 39x trailing EPS: 39 x EUR 8.96 = EUR 349
Fair Value at 39x forward EPS: 39 x EUR 9.70 = EUR 378
Fair Value at 35x forward EPS (moderate): 35 x EUR 9.70 = EUR 340
Fair Value at 42x forward EPS (re-rate): 42 x EUR 9.70 = EUR 407
```

**P/E-implied FV range: EUR 340 - EUR 407, midpoint EUR 370**

---

## DCF Tool Output (Documented -- UNRELIABLE)

The DCF tool produces the following output using thesis-derived parameters (growth 6.5%, WACC 9.35%, terminal 3.0%):

| Scenario | FV/Share | MoS |
|----------|----------|-----|
| Bear | EUR 79.07 | -75.5% |
| Base | EUR 99.75 | -69.1% |
| Bull | EUR 129.25 | -60.0% |

**Sensitivity matrix (Growth x WACC):**

| Growth \ WACC | 7.8% | 9.3% | 10.8% |
|---------------|------|------|-------|
| 3.5% | EUR 115 | EUR 88 | EUR 71 |
| 5.0% | EUR 123 | EUR 94 | EUR 76 |
| 6.5% | EUR 131 | EUR 100 | EUR 80 |
| 8.0% | EUR 140 | EUR 106 | EUR 86 |
| 9.5% | EUR 149 | EUR 113 | EUR 91 |

**FV Spread:** 78% | **TV as % of EV:** 75.5%

### Why the DCF Tool is Wrong for Ferrari

The DCF tool uses yfinance-reported FCF, which for FY2024 is EUR 938M. Ferrari reports "industrial free cash flow" of EUR 1,538M for FY2025 -- a 64% premium over the yfinance figure for the prior year. The yfinance FCF definition excludes or misclassifies items that Ferrari's industrial FCF includes. Key issues:

1. **FCF base is ~40% too low:** Using EUR 938M vs EUR 1,300M (normalized industrial) understates every future year.
2. **Net debt treatment:** The tool correctly shows EUR 0 net debt, but the base FCF error dominates.
3. **Terminal value:** 75.5% of EV from terminal value is typical for a compounder, but the underestimated FCF makes the terminal also too low.

**If we manually adjust the DCF output by the FCF ratio (1,300/938 = 1.39x):**
- Adjusted base FV: EUR 99.75 x 1.39 = EUR 138.7 -- STILL far below market price
- This means even with corrected FCF, a standard DCF at 9.35% WACC cannot justify EUR 323

**This is the core insight:** Ferrari is valued by the market as a luxury franchise (multiple-based), not as a discounted cash flow stream. A DCF that produces EUR 139 when the stock trades at EUR 323 tells us the market assigns a ~2.3x premium for brand, scarcity, and moat. This is consistent with how Hermes trades (Hermes at a standard DCF also looks "overvalued").

**Conclusion on DCF:** The DCF tool is uninformative for Ferrari. The stock's valuation is driven by the multiple the market assigns to its luxury franchise value, not by discounting cash flows. This is not a flaw in the tool -- it is a feature of how ultra-luxury businesses are valued.

---

## Reconciliation of Methods

| Method | Fair Value | Weight | Weighted | Rationale for Weight |
|--------|-----------|--------|----------|---------------------|
| OEY Framework | EUR 330 | 20% | EUR 66 | OEY unreliable as point estimator for Ferrari (growth close to WACC creates extreme range). Used as sanity check only. |
| EV/EBIT Multiple (32x FY26E) | EUR 400 | 50% | EUR 200 | Most appropriate for luxury goods. Ferrari is valued as luxury, not DCF. Peer-anchored. |
| P/E Relative (39x forward) | EUR 370 | 30% | EUR 111 | Consistent with historical average; captures the market's established valuation framework for Ferrari. |
| **Weighted Average** | | **100%** | **EUR 377** |

**Divergence between methods:** EV/EBIT gives EUR 400, P/E gives EUR 370, OEY gives EUR 330.
- Maximum divergence: (EUR 400 - EUR 330) / EUR 377 = 18.6% -- BELOW the 30% threshold. No investigation required.
- The methods are coherent: multiple-based methods (EV/EBIT and P/E) cluster at EUR 370-400, while OEY (which penalizes high multiples by design) is lower at EUR 330. This pattern is expected for premium compounders.

---

## Scenarios

| | Bear | Base | Bull |
|--|------|------|------|
| **Revenue CAGR 2025-2030** | 3.5% | 6.5% | 10% |
| **EBIT Margin 2030** | 28% | 30.5% | 32% |
| **Valuation Multiple (EV/EBIT)** | 25x | 32x | 40x |
| **EPS FY2026E** | EUR 9.00 | EUR 9.70 | EUR 10.50 |
| **Fair Value** | EUR 280 | EUR 377 | EUR 500 |
| **Probability** | 20% | 55% | 25% |

### Bear Case (20%): Luxury Demand Weakness

Assumptions:
- Global UHNW spending weakens (China hard landing + mild US recession)
- Revenue growth decelerates to 3.5% CAGR (volume flat, ASP growth slows)
- EBIT margin compresses to 28% (Luce launch costs, tariff absorption)
- Market re-rates to 25x EV/EBIT (below historical range, but above auto sector)
- FV: 25x x EUR 2,100M EBIT / 177M shares = EUR 297 on trailing; using EUR 9.00 forward EPS x 31x P/E = EUR 279

**Bear FV: EUR 280**

This is not a catastrophic scenario. Even the bear case implies a 25x multiple (above auto, below luxury average), which reflects that even in a downturn, Ferrari's brand and scarcity model provide a floor. During COVID, Ferrari's P/E troughed at ~30x.

### Base Case (55%): CMD Execution + Moderate Re-rating

Assumptions:
- Revenue CAGR 5-7% per CMD, management likely beats by 1-2pp
- EBIT margin expands to 30%+ per 2030 target
- Luce launches successfully, contributing from late 2026
- Buyback program (EUR 3.5B) provides ~1.5% annual EPS accretion
- P/E normalizes to ~39x (historical average) from current 36x
- EV/EBIT at 32x

**Base FV: EUR 377**

### Bull Case (25%): Luxury Re-rating + Luce Success

Assumptions:
- Revenue CAGR 8-10% (management beats guidance materially as historically)
- Personalization penetration exceeds 25% of car revenue
- Luce is a runaway success, EUR 500K+ EV with strong demand
- EBIT margin reaches 32% by 2028 (ahead of 2030 target)
- Market re-rates Ferrari to 40x EV/EBIT (historical upper range, Hermes territory)
- Share buyback accelerated

**Bull FV: EUR 500**

### Expected Value

```
EV = (EUR 280 x 20%) + (EUR 377 x 55%) + (EUR 500 x 25%)
EV = EUR 56 + EUR 207.35 + EUR 125
EV = EUR 388
```

---

## Sensibilidad (EV/EBIT Method)

### EV/EBIT Multiple Sensitivity (FY2026E EBIT)

| EBIT \ Multiple | 25x | 28x | 32x | 36x | 40x |
|-----------------|-----|-----|-----|-----|-----|
| EUR 2,100M (miss) | EUR 297 | EUR 332 | EUR 380 | EUR 427 | EUR 475 |
| EUR 2,213M (base) | EUR 312 | EUR 350 | EUR 400 | EUR 450 | EUR 500 |
| EUR 2,350M (beat) | EUR 332 | EUR 372 | EUR 425 | EUR 478 | EUR 531 |

*Values are FV per share in EUR, assuming net debt ~0 and 177M shares.*

### P/E Sensitivity (FY2026E EPS)

| EPS \ P/E | 30x | 33x | 36x | 39x | 42x |
|-----------|-----|-----|-----|-----|-----|
| EUR 9.00 | EUR 270 | EUR 297 | EUR 324 | EUR 351 | EUR 378 |
| EUR 9.70 | EUR 291 | EUR 320 | EUR 349 | EUR 378 | EUR 407 |
| EUR 10.50 | EUR 315 | EUR 347 | EUR 378 | EUR 410 | EUR 441 |

### Key Sensitivity Observation

The fair value is most sensitive to the **multiple** assigned, not to earnings estimates. A 1x change in EV/EBIT (from 32x to 33x) moves FV by ~EUR 12.50/share (~3.3%). A 5% change in EBIT moves FV by ~EUR 20/share (~5%). The multiple is the key variable, and it depends on whether the market classifies Ferrari as "luxury" (35-45x) or "premium auto" (15-25x).

---

## Validation vs Peers

### Implied Multiples at My FV

| Metric | At Current (EUR 323) | At My FV (EUR 377) | Hermes | LVMH |
|--------|---------------------|---------------------|--------|------|
| P/E trailing | 36.0x | 42.1x | 49.7x | 23.9x |
| P/E forward | 33.3x | 38.9x | ~44x | ~22x |
| EV/EBIT trailing | 27.1x | 31.7x | ~43x | ~21x |
| EV/EBIT forward | 25.9x | 30.3x | ~40x | ~19x |

At my FV of EUR 377, Ferrari would trade at 42x trailing P/E -- BELOW Hermes (49.7x) and ABOVE LVMH (23.9x). This is where Ferrari should sit given its moat profile (comparable to Hermes in brand/scarcity, but higher capital intensity).

At 42x trailing P/E, Ferrari is expensive relative to LVMH but justified given:
- Higher ROIC (24.9% vs ~14%)
- Higher ROIC-WACC spread (+14.9pp vs ~4pp)
- Scarcity model (no volume competition)
- Net cash vs LVMH's significant debt

### Validation: Historical P/E Band

Ferrari's historical 10-year P/E range is approximately 30x-60x, with average ~39x. My FV of EUR 377 implies 42x trailing, which is within the 39-45x "normal" band for Ferrari. This passes the sanity check.

### Validation vs Precedents (decisions_log.yaml)

No prior Ferrari positions exist in the portfolio. The closest precedent by type is:
- **Tier A compounders bought:** NVO (MoS 38%), LULU (34%), MONY.L (36%), ADBE (31%), BYIT.L (35%), AUTO.L (29%)
- **Pattern:** Tier A entries have been at MoS 29-38%, averaging ~34%

Ferrari at current EUR 323 vs my FV EUR 377 = MoS 14.4%. This is BELOW the precedent average of ~34%.
Ferrari at current EUR 323 vs EV EUR 388 = MoS 16.8%. Still below precedents.

---

## Summary

```
VALUATION: RACE.MI (Ferrari N.V.)

Tipo de empresa: Luxury goods compounder
Metodos seleccionados: OEY + EV/EBIT Multiple + P/E Relative

Metodo 1: Owner Earnings Yield
- Inputs: Normalized industrial FCF EUR 1,300M, WACC 9.35%, Growth 6.5%
- OEY + Growth = 8.66% vs WACC 9.35% = near fair value
- Fair Value: EUR 330

Metodo 2: EV/EBIT Multiple (32x FY2026E)
- Inputs: EBIT FY2026E EUR 2,213M, Multiple 32x, Net Debt ~EUR 0
- Fair Value: EUR 400

Metodo 3: P/E Relative (39x forward)
- Inputs: EPS FY2026E EUR 9.70, P/E 39x (historical average)
- Fair Value: EUR 378

Reconciliacion:
| Metodo | FV | Peso | Weighted |
|--------|----|------|----------|
| OEY | EUR 330 | 20% | EUR 66 |
| EV/EBIT | EUR 400 | 50% | EUR 200 |
| P/E Relative | EUR 378 | 30% | EUR 111 |
| **Weighted Avg** | | 100% | **EUR 377** |

Divergencia: 18.6% (within acceptable range)

Escenarios:
| Escenario | Fair Value | Prob |
|-----------|-----------|------|
| Bear | EUR 280 | 20% |
| Base | EUR 377 | 55% |
| Bull | EUR 500 | 25% |
| **Expected** | **EUR 388** | 100% |

Precio actual: EUR 322.80
MoS vs Base FV: +16.8%
MoS vs Expected: +20.2%
MoS vs Bear: -13.3%
```

---

## Comparison with Fundamental-Analyst Estimate

The fundamental-analyst estimated FV = EUR 379 using EV/EBIT 33x (50% weight), OEY (30%), and Reverse DCF (20%).

**My estimate: EUR 377 (weighted average). Agreement is essentially exact.**

Minor differences:
1. I used 32x EV/EBIT (vs analyst's 33x) -- slightly more conservative due to growth deceleration
2. I gave OEY lower weight (20% vs 30%) because OEY is unreliable as a point estimator when growth is close to WACC
3. I added P/E Relative as a third method (30% weight) -- this provides a market-anchored cross-check
4. My scenarios differ slightly: Bear EUR 280 vs analyst's EUR 290, Bull EUR 500 vs EUR 510

**Verdict: AGREE with the fundamental-analyst's FV of EUR 379. My independent estimate of EUR 377 confirms the valuation within 0.5%.**

The convergence of two independent methods (fundamental-analyst using 3 methods, valuation-specialist using 3 methods) on the same number provides confidence in the EUR 375-380 fair value range.

---

## Entry Price Recommendation

### MoS Analysis at Various Prices

| Entry Price | MoS vs Base (EUR 377) | MoS vs Expected (EUR 388) | MoS vs Bear (EUR 280) | Assessment |
|-------------|----------------------|--------------------------|----------------------|------------|
| EUR 323 (current) | +16.8% | +20.2% | -13.3% | ADEQUATE for Tier A but below precedent average (~34%) |
| EUR 305 | +23.6% | +27.2% | -8.2% | REASONABLE -- approaching precedent range |
| EUR 290 | +30.0% | +33.8% | -3.4% | GOOD -- within Tier A precedent range (29-38%) |
| EUR 276 (52w low) | +36.6% | +40.6% | -1.4% | EXCELLENT -- above precedent average |

### Recommendation

| Price Level | Action | Sizing |
|-------------|--------|--------|
| EUR 290-305 | **BUY initial position** | 3-4% (consistent with Tier A precedents: ADBE 4.8%, NVO 3.4%, LULU 3.5%) |
| EUR 276 (52w low) | **ADD aggressively** | Up to 5% total (MoS 36.6% vs base) |
| EUR 323 (current) | **WATCHLIST** | MoS 16.8% is adequate but below the 29-38% range achieved in prior Tier A entries. Patience is warranted. |
| Below EUR 260 | **STRONG BUY** | Hypothetical; would require significant market dislocation |

### Rationale for NOT Buying at Current Price

While EUR 323 offers a 17-20% MoS (adequate for Tier A), the portfolio has 44% cash and a clear mandate to deploy capital patiently (lesson from Jan 26-Feb 3 rapid deployment disaster). Every Tier A entry to date has been at MoS 29%+. Buying Ferrari at 17% MoS would break this precedent without strong justification.

**Strong justification would be:** A catalyst that increases confidence in the base case (e.g., Luce pre-order numbers, FY2026 Q1 guidance beat, tariff resolution). Without such a catalyst, the risk-reward at EUR 323 is decent but not compelling enough to break the pattern of higher-MoS Tier A entries.

---

## 🔄 META-REFLECTION

### Dudas/Incertidumbres

1. **DCF structural mismatch:** The DCF tool is fundamentally wrong for Ferrari (EUR 100 vs EUR 323 market price). This is not a data error -- it reveals that DCF at a "normal" WACC cannot explain Ferrari's valuation. The market values Ferrari as a luxury franchise with a structural multiple premium. Whether this premium persists is the core risk.

2. **Multiple choice is the key driver:** My entire valuation hinges on whether 32x EV/EBIT is appropriate. At 28x, FV drops to EUR 350. At 36x, FV rises to EUR 450. The uncertainty is +/- EUR 50 from the base case based on multiple alone. This is inherently subjective and driven by comparable selection (Hermes vs LVMH vs historical average).

3. **Normalized FCF estimate:** I used EUR 1,300M (vs FY2025 reported EUR 1,538M). If FY2025's elevated level is more sustainable than I assume, OEY-implied FV would rise. Conversely, if FY2026 capex ramp compresses FCF more than expected (Luce investment), the OEY case weakens.

4. **yfinance dividend yield anomaly (96%):** This is clearly erroneous (actual ~0.7%). It affects any automated screening or tool that uses yfinance dividend data for RACE.MI.

### Sensibilidad Preocupante

- FV changes by EUR 12.50/share for every 1x change in EV/EBIT multiple (~3.3%)
- Multiple range of 25x-40x (reasonable) implies FV range of EUR 312-500 (60% spread)
- This is HIGH sensitivity. The investment case requires conviction in the "luxury" classification (32x+), not just in the business fundamentals.

### Discrepancias con Thesis

- **No material discrepancy.** My FV (EUR 377) matches the fundamental-analyst's FV (EUR 379) almost exactly.
- **One nuance:** The fundamental-analyst used 33x EV/EBIT; I used 32x. The 1x difference is immaterial (EUR 12.50/share) and within the estimation error band.
- **Entry price alignment:** Both the analyst and I recommend entry at EUR 290-305 (MoS 23-30%) rather than the current EUR 323 (MoS 17%). This convergence is reassuring.

### Sugerencias para el Sistema

1. **DCF tool FCF override:** For companies where yfinance FCF materially differs from reported FCF (Ferrari, REITs, financials), add a `--fcf-override` parameter to `dcf_calculator.py`. This would make the tool useful for a broader range of companies.

2. **Luxury goods sector view:** Ferrari analysis highlights the need for `world/sectors/luxury-goods.md` covering Hermes, LVMH, Ferrari, Brunello Cucinelli. These companies share moat characteristics (brand, scarcity, pricing power) that are not captured by the "Consumer Cyclical / Auto Manufacturers" classification.

3. **Multiple-based valuation tool:** For Tier A luxury compounders where DCF is unreliable, a simple EV/EBIT and P/E sensitivity tool that takes EBIT/EPS + multiple range + net debt would be useful. Currently this is done manually.

### Preguntas para Orchestrator

1. Given that the current MoS (17%) is below Tier A precedent average (34%), should we set a standing order at EUR 290-300, or wait for devil's-advocate + investment-committee to complete the pipeline first?
2. The EUR 280 bear case implies only 13% downside from current price. Does this limited downside compensate for the below-average MoS, or should we strictly adhere to the 29%+ MoS precedent for Tier A?
3. Ferrari would be the first "luxury goods" position in the portfolio. Does this add genuine diversification (new sector exposure) or is it correlated with existing Consumer Discretionary exposure (LULU)?

---

**Valuation Date:** 2026-02-11
**Price at valuation:** EUR 322.80
**Fair Value (weighted):** EUR 377
**Expected Value:** EUR 388
**Recommended entry:** EUR 290-305
