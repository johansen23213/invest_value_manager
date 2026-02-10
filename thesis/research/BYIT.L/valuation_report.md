# ADVERSARIAL VALUATION REPORT: BYIT.L (Bytes Technology Group plc)

**Date:** 2026-02-09
**Valuation Specialist:** Independent (adversarial mode)
**Current Price:** 306 GBp (source: price_checker.py)
**Thesis FV:** 455 GBp | **Thesis MoS:** 35% | **Thesis QS:** 81

---

## 1. Company Classification and Method Selection

**Type of enterprise:** Stable/Defensive Growth (asset-light IT services with high recurring revenue)
**Thesis classification:** Tier A Quality Compounder (QS 81)

**Methods selected:**
- **Primary:** Owner Earnings Yield (OEY) -- appropriate for Tier A compounder
- **Secondary:** DCF with multiple scenario analysis
- **Cross-check:** EV/EBIT peer comparison vs Softcat/Computacenter

---

## 2. Verification of Key Financial Inputs

### 2.1 FCF Verification (CRITICAL)

The thesis claims FCF ~GBP 48M based on "~30% FCF margin on ~GBP 160M GP."

**Actual data from yfinance (FY2025, ending Feb 2025):**

| Metric | yfinance | Thesis |
|--------|----------|--------|
| Free Cash Flow | GBP 64.9M | GBP 48M |
| Operating Cash Flow | GBP 75.0M | Not stated |
| Capital Expenditure | GBP 10.1M | Negligible |
| Net Income | GBP 54.8M (statutory) / GBP 74.6M (pre-tax) | 22.8p EPS |
| Gross Profit | GBP 163.3M | GBP 160M |
| Operating Income | GBP 66.4M | GBP 65M |
| EBIT | GBP 74.9M | Not stated |
| Depreciation & Amortization | GBP 2.6M | ~GBP 3M |

**FINDING 1: FCF is HIGHER than the thesis states.** The thesis used GBP 48M; actual FY2025 FCF was GBP 64.9M. However, there is a significant caveat: FY2025 included GBP 49.6M favorable working capital movement in payables (timing-related). Normalized FCF is closer to GBP 40-50M when adjusting for working capital volatility.

**FCF History (GBP millions):**

| Year | FCF | OCF | Capex | Net Income |
|------|-----|-----|-------|------------|
| FY2022 | 51.4 | 52.0 | -0.6 | 32.9 |
| FY2023 | 36.8 | 38.2 | -1.4 | 40.4 |
| FY2024 | 55.7 | 57.0 | -1.3 | 46.9 |
| FY2025 | 64.9 | 75.0 | -10.1 | 54.8 |
| **Average** | **52.2** | | | |

Note: FY2025 capex jumped to GBP 10.1M (vs ~GBP 1M historical) due to GBP 3.4M "marketplace" platform investment plus new office investments. This is above maintenance levels.

**My normalized FCF estimate:** GBP 48-52M (average of FY2022-FY2025, adjusting FY2025 down for working capital timing and higher capex).

**VERDICT:** The thesis FCF figure of GBP 48M is actually CONSERVATIVE relative to the FY2025 reported figure, but REASONABLE as a normalized estimate. I will use GBP 50M as my base.

### 2.2 EPS Verification

| Period | EPS | Source |
|--------|-----|--------|
| FY2025 | 22.8p (adjusted), 21p (trailing yfinance) | Thesis / yfinance |
| H1 FY2026 | 12.03p | H1 results |
| Forward EPS (yfinance) | 22.9p | yfinance |

**H1 FY2026 Analysis:**
- H1 EPS = 12.03p (down 5.1% YoY from ~12.7p)
- If H2 performs as well as H1: Full year EPS ~ 24p (H2 is typically stronger)
- Management guided "high single-digit operating profit growth" for full FY2026
- If OP grows 7-8% from FY2025's GBP 66.4M: FY2026 OP ~ GBP 71-72M
- Implied FY2026 EPS: ~24-25p

**BUT WAIT -- Challenge on guidance credibility:**
The H1 FY2026 showed OP DECLINING 7.0% (GBP 33.1M vs GBP 35.6M). For full-year OP to grow "high single digit," H2 must deliver ~GBP 38-39M of OP (vs ~GBP 30M in H2 FY2025). This implies H2 OP growth of ~27-30%. This is a very steep H2 ramp.

**Is this realistic?** The thesis notes management "maintained guidance" of double-digit GP growth. If services growth continues at 40%+ and Microsoft incentive headwinds normalize (management says they have "settled into the new structure"), H2 should improve. Additionally, the GBP 25M share buyback reduces shares, boosting EPS. Microsoft commercial price increases (8-33% across products, effective July 2026) would also boost GII and potentially GP in FY2027.

**My estimate for FY2026 EPS:** 22-24p (assuming modest H2 recovery, not full guidance achievement)
**My estimate for FY2027 EPS:** 24-27p (incentive normalization + Microsoft price increases + services growth)

### 2.3 Growth Rate Challenge

The thesis uses 8% GP growth as the base case. Let me challenge this:

**Historical GP growth:**

| Period | GP | Growth |
|--------|-----|--------|
| FY2022 | GBP 107.4M | -- |
| FY2023 | GBP 129.6M | +20.7% |
| FY2024 | GBP 145.8M | +12.5% |
| FY2025 | GBP 163.3M | +12.0% |
| H1 FY2026 | GBP 82.4M | +0.4% |

3-year GP CAGR (FY2022-FY2025): **15.0%**

The H1 FY2026 deceleration to +0.4% is dramatic. The question is whether this is a one-off trough or the start of a structural slowdown.

**Arguments for 8% being achievable:**
- H1 was the trough of Microsoft incentive transition
- Services growing 40%+ should accelerate GP
- Microsoft price increases July 2026 boost FY2027
- Consolidation of smaller VARs due to higher Microsoft thresholds
- Management guides double-digit GP growth for full FY2026

**Arguments for 8% being too optimistic:**
- H1 showed FLAT GP growth -- 8% for the full year requires ~16% H2 GP growth
- Microsoft incentive changes may not be one-off -- they restructure every 2-3 years
- Public sector growth decelerated materially (1.6%)
- GP/GII margin compressed 0.6pp -- may not recover
- OP growth of "high single digit" is weaker than historical double-digit

**My independent growth estimate:**

| Scenario | GP Growth | OP Growth | Reasoning |
|----------|-----------|-----------|-----------|
| Bear | 3% | 0% | Incentive headwinds persist, services growth slows to 20%, public sector flat |
| Base | 6% | 5% | Partial normalization, services 25-30%, modest public sector recovery |
| Bull | 10% | 9% | Full normalization, AI services boom, Microsoft price hikes flow through |

**FINDING 2: The thesis 8% GP growth base case is in my BULL territory, not base.** I use 6% as base, reflecting the real uncertainty from the H1 deceleration. The market has reason to be cautious.

### 2.4 WACC Challenge

The thesis derives WACC as follows:
- Rf = 4.2% (UK 10Y Gilt)
- Beta = 0.85
- ERP = 5.0%
- Ke = 4.2% + 0.85 * 5.0% = 8.45%
- Rounded up to 9.0% for Microsoft concentration risk

**My challenge:**
1. Beta of 0.85 seems low for a stock that fell 47% when the index was relatively flat. Empirical beta may be higher. The 52-week price range (291-563 GBp) shows extreme volatility.
2. The company has significant concentration risk in Microsoft (estimated 60-70% of GP derives directly or indirectly from Microsoft ecosystem).
3. UK mid-cap premium: smaller companies deserve higher discount rate.
4. Company-specific risk: management transition (new CEO Sam Mudd), incentive structure uncertainty.

**My WACC estimate:** 9.5% (thesis says 9.0%, but I add 0.5pp for the above risks)

Conservative cross-check: For a GBP 700M UK mid-cap with single-vendor concentration and declining margins, 9.5% is reasonable. Softcat (GBP 2.3B, better ROIC, more diversified revenue) would warrant ~8.5-9.0%.

---

## 3. Method 1: Owner Earnings Yield (Primary, 60% weight)

### 3.1 Calculation

```
Normalized FCF: GBP 50M (my estimate, conservatively below FY2025 actual of GBP 64.9M)
Depreciation: GBP 2.6M
Maintenance Capex: ~GBP 3M (D&A x 1.1, asset-light)

Owner Earnings = FCF (already net of capex) = GBP 50M
(For asset-light businesses, FCF ~ Owner Earnings)

Market Cap at 306p: GBP 724M (236.3M shares x 306p)

OEY = GBP 50M / GBP 724M = 6.9%
Expected Growth (my base, 6%): 6.0%
OEY + Growth = 6.9% + 6.0% = 12.9%

vs WACC = 9.5%
Spread = +3.4pp
```

**Comparison with thesis:**
- Thesis: OEY 6.4% + Growth 8.0% = 14.4%, spread +5.4pp
- Mine: OEY 6.9% + Growth 6.0% = 12.9%, spread +3.4pp
- The difference is mainly in the growth assumption (I use 6%, thesis uses 8%)

### 3.2 OEY-Implied Fair Value

At what price does OEY + Growth = required return?

**For 12% total return target (typical for Tier A):**
- Required OEY = 12% - 6% growth = 6.0%
- Market Cap = GBP 50M / 6.0% = GBP 833M
- Per share = GBP 833M / 236.3M = **353p**

**For WACC (9.5%) as minimum acceptable return:**
- Required OEY = 9.5% - 6% = 3.5%
- Market Cap = GBP 50M / 3.5% = GBP 1,429M
- Per share = 1,429M / 236.3M = **605p** (theoretical max, too generous)

**For 10.5% return (midpoint):**
- Required OEY = 10.5% - 6% = 4.5%
- Market Cap = GBP 50M / 4.5% = GBP 1,111M
- Per share = 1,111M / 236.3M = **470p**

**I use 12% as the target return for the OEY method, giving OEY Fair Value: 353p**

**vs Thesis OEY FV of 470p:** My estimate is 25% lower. The divergence comes from:
1. Lower growth assumption (6% vs 8%) -- accounts for ~60% of the gap
2. Higher return requirement (12% vs thesis's implicit ~12% but using 8% growth)

**FINDING 3: At the thesis growth rate of 8%, OEY FV would be GBP 50M / (12% - 8%) = GBP 1.25B = 529p. But this is aggressive. At my 6% growth, OEY FV = 353p. The truth is likely between 353p and 470p depending on growth realization.**

To be fair, I will present both scenarios:
- OEY FV at 6% growth = 353p
- OEY FV at 8% growth = 416p (using GBP 50M / (12%-8%) * 0.8 to account for growth uncertainty)

**My OEY Fair Value: 380p** (blended, weighting base 60% and optimistic 40%)

---

## 4. Method 2: DCF with Multiple Scenarios (Secondary, 40% weight)

### 4.1 DCF Tool Results Summary

| Scenario | Growth | WACC | Terminal | Fair Value | MoS vs 306p |
|----------|--------|------|----------|-----------|-------------|
| Ultra-Bear | 2% | 11% | 1.5% | **317p** | +3.6% |
| Bear | 4% | 10% | 2.0% | **398p** | +30.2% |
| Moderate | 6% | 9.5% | 2.5% | **484p** | +58.2% |
| Base (thesis) | 8% | 9.0% | 2.5% | **565p** | +84.5% |
| Default scenarios (5%/9%) Bear | 5% | 10% | 2.0% | **401p** | +30.9% |
| Default scenarios (5%/9%) Base | 5% | 9% | 2.5% | **500p** | +63.2% |
| Default scenarios (5%/9%) Bull | 5% | 8% | 3.0% | **640p** | +108.9% |

### 4.2 DCF Sensitivity Table (WACC vs Growth)

| | WACC 8.5% | WACC 9.0% | WACC 9.5% | WACC 10.0% | WACC 10.5% |
|--|-----------|-----------|-----------|------------|------------|
| Growth 3% | ~380p | ~350p | ~325p | ~305p | ~285p |
| Growth 4% | ~435p | ~400p | ~370p | ~340p | ~315p |
| Growth 5% | ~500p | ~455p | ~420p | ~390p | ~360p |
| Growth 6% | ~575p | ~525p | ~484p | ~445p | ~410p |
| Growth 7% | ~665p | ~600p | ~550p | ~505p | ~465p |
| Growth 8% | ~775p | ~700p | ~635p | ~575p | ~525p |

(Values estimated by interpolation between DCF tool results)

### 4.3 My DCF Fair Value Selection

Using my derived parameters (growth 6%, WACC 9.5%, terminal 2.5%):
**DCF Base Case: 484p** (from dcf_calculator.py direct output)

However, I need to apply judgment:

1. The DCF tool uses the most recent FCF (GBP 64.9M) which includes working capital timing benefit. If I normalize to GBP 50M, the DCF result should be scaled down: 484p * (50/64.9) = **373p**

2. The terminal value represents 73.3% of enterprise value at these parameters -- this is high and makes the DCF sensitive to terminal assumptions.

**My adjusted DCF scenarios:**

| Scenario | Growth | WACC | Terminal | Normalized FCF | FV |
|----------|--------|------|----------|----------------|-----|
| Bear | 3% | 10.5% | 1.5% | GBP 45M | **~240p** |
| Base | 6% | 9.5% | 2.0% | GBP 50M | **~345p** |
| Bull | 8% | 9.0% | 2.5% | GBP 55M | **~480p** |

**DCF Fair Value (base): ~345p**

Note: The discrepancy between the tool's 484p and my 345p comes from:
1. Normalizing FCF down from 64.9M to 50M (-23% reduction in base)
2. Using lower terminal growth (2.0% vs 2.5%)
3. Using higher WACC (9.5%)

---

## 5. Cross-Check: EV/EBIT Peer Comparison

### 5.1 Peer Multiples (Live Data)

| Company | Price | MCap (GBP B) | EV (GBP B) | EBIT (GBP M) | EV/EBIT | Trailing P/E | Fwd P/E | ROE |
|---------|-------|-------------|------------|-------------|---------|-------------|---------|-----|
| **SCT.L** (Softcat) | 1,171p | 2.3B | ~2.15B | ~180M (FY25) | **~12x** | 17.7x | 15.1x | 41.8% |
| **CCC.L** (Computacenter) | -- | 3.2B | ~3.0B | ~252M | **~12x** | 20.7x | 15.8x | 17.7% |
| **BYIT.L** (current) | 306p | 0.72B | ~0.68B | ~66M (FY25) | **~10.3x** | 14.6x | 13.4x | 68.9% |

**CRITICAL FINDING 4: Softcat's P/E has RE-RATED DOWN significantly.**

The thesis claimed Softcat traded at "~25x P/E." Current data shows:
- Softcat trailing P/E: **17.7x** (NOT 25x)
- Softcat forward P/E: **15.1x**
- Softcat EV/EBIT: ~12x

The thesis valuation gap argument ("Softcat at 25x vs BYIT at 14x is excessive") is MATERIALLY WRONG. The actual gap is:
- Trailing P/E: Softcat 17.7x vs BYIT 14.6x -- only a 21% premium, NOT 79%
- Forward P/E: Softcat 15.1x vs BYIT 13.4x -- only a 13% premium

**This fundamentally undermines the thesis's comparables argument.** Softcat has also been de-rated, suggesting the market's concerns about UK VARs are sector-wide, not BYIT-specific.

### 5.2 What EV/EBIT Multiple Should BYIT Deserve?

Given the peer re-rating:

| Multiple Basis | Value | Reasoning |
|----------------|-------|-----------|
| Sector median (Softcat/CCC) | 12x | Where peers now trade |
| Discount for smaller size/concentration | -1x to -2x | Microsoft dependence, GBP 700M vs GBP 2-3B peers |
| Premium for higher FCF margin/ROE | +1x | 30% FCF margin, 69% ROE vs peer average |
| Net adjustment | 0 to -1x | Roughly offset |
| **My range** | **11-13x** | Around sector median |

**EV/EBIT Fair Value at different multiples:**

| Multiple | EV (GBP M) | + Net Cash | Equity Value | Per Share |
|----------|-----------|------------|-------------|-----------|
| 10x | 660M | +40M | 700M | 296p |
| 11x | 726M | +40M | 766M | 324p |
| 12x | 792M | +40M | 832M | 352p |
| 13x | 858M | +40M | 898M | 380p |
| 14x | 924M | +40M | 964M | 408p |
| 15x | 990M | +40M | 1,030M | 436p |

Using GBP 66M EBIT (FY2025 actual).

**At sector-median 12x, BYIT fair value = 352p.**
**At 13x (slight premium for FCF quality), fair value = 380p.**

For comparison, the thesis used 15x and 17x, getting 409p and 461p -- but those multiples are NOT justified now that Softcat itself trades at only ~12x.

### 5.3 Forward EV/EBIT Analysis

If FY2026 EBIT recovers to GBP 71M (my base, +7.5%):

| Multiple | FV |
|----------|-----|
| 11x | 349p |
| 12x | 381p |
| 13x | 413p |

**Forward EV/EBIT Fair Value (12-13x on FY2026E): 380-413p**

---

## 6. Bear Case Deep Dive

### 6.1 What if Microsoft Incentive Compression Continues 2+ Years?

Microsoft restructures partner programs every 2-3 years. The current FY26 changes are the most significant in recent history. If this is a permanent structural shift:

- GP/GII margin could decline from 6.7% to 5.5-6.0% over 2-3 years
- This would reduce GP by ~10-15% relative to GII growth
- OP margin (OP/GP) could compress from 40.7% to 35-38% as investment continues
- Normalized OP: GBP 55-60M (vs FY2025's GBP 66M)
- At 10x EV/EBIT: FV = 250-265p
- At 11x EV/EBIT: FV = 275-290p

**Bear floor under sustained margin compression: ~260-280p**

### 6.2 What if Services Growth Slows from 40% to 15%?

Services currently ~30% of GP and growing 40%+. If it slows to 15%:
- Services GP growth contribution: ~4.5% of total GP (vs ~12% currently)
- Total GP growth: 3-5% (not enough to offset software margin loss)
- OP growth: 0-3%
- EPS growth: 2-5% (share buyback helps)
- Forward P/E at 12x on 23p EPS = 276p

This scenario is not catastrophic because services at 15% growth still contributes positively.

### 6.3 Absolute Floor Valuation

**Liquidation / stressed scenario:**
- Net cash: GBP 40M (now GBP 42.9M per yfinance, minus buyback spend)
- Recurring revenue base: ~80% of GP = GBP 130M+ of mostly contracted annual revenue
- Even at severe margin compression, FCF stays positive (no debt, low capex)
- At 8x normalized EBIT of GBP 55M + GBP 30M cash = GBP 470M = **~200p**

**Hard floor: ~200p** (would imply business generating GBP 40-50M FCF forever with zero growth)

### 6.4 My Bear Case Fair Value

Weighted bear case considering probability:
- Incentive compression continues 2 years (40% probability in bear): 265p
- Services slow to 15% growth (35% probability in bear): 276p
- Full recovery stalls, status quo (25%): 310p

**Bear Case FV: ~275p**

---

## 7. Reconciliation of Methods

### 7.1 Method Summary

| Method | Fair Value | Weight | Weighted |
|--------|-----------|--------|----------|
| OEY (6% growth, 12% return) | 380p | 60% | 228p |
| DCF (6%/9.5%/2.0%, normalized FCF) | 345p | 40% | 138p |
| **Weighted Average** | | **100%** | **366p** |

**Cross-checks:**
- EV/EBIT peer comparison (12-13x FY2025 EBIT): 352-380p -- VALIDATES
- Forward EV/EBIT (12-13x FY2026E EBIT): 380-413p -- VALIDATES upper end
- Analyst consensus target: 461-491p -- HIGHER than my estimate (not unusual for analyst consensus)

**Divergence between methods: 10%** (380p vs 345p) -- well within acceptable range.

### 7.2 Comparison with Thesis

| Metric | Thesis | My Estimate | Delta |
|--------|--------|-------------|-------|
| OEY FV | 470p | 380p | **-19%** |
| DCF FV | 432p | 345p | **-20%** |
| Weighted FV | 455p | 366p | **-20%** |
| Bear Case | 350p | 275p | **-21%** |
| Bull Case | 580p | 460p | **-21%** |
| Growth assumption | 8% | 6% | -2pp |
| WACC | 9.0% | 9.5% | +0.5pp |
| FCF used | GBP 48M | GBP 50M | +4% |

**FINDING 5: My independent valuation is approximately 20% below the thesis across all scenarios and methods.** The delta is remarkably consistent, driven primarily by:

1. **Lower growth assumption (6% vs 8%):** -2pp accounts for ~60% of the FV gap
2. **Higher WACC (9.5% vs 9.0%):** +0.5pp accounts for ~20% of the gap
3. **Peer re-rating downward:** Softcat at 17.7x P/E (not 25x) invalidates the "massive discount" argument and accounts for ~20% of the gap

---

## 8. Scenario Analysis

### 8.1 Three Scenarios

| Scenario | Prob | FV (GBp) | Key Assumptions |
|----------|------|----------|-----------------|
| **Bear** | 25% | 275p | Incentive compression persists, services growth slows to 15%, GP growth 3%, OP flat, P/E 12x on GBP 22p EPS |
| **Base** | 50% | 366p | Partial normalization, services 25-30% growth, GP growth 6%, OP growth 5%, EV/EBIT 12-13x |
| **Bull** | 25% | 460p | Full normalization + AI services boom + Microsoft price increases, GP growth 10%, OP growth 9%, EV/EBIT 14x |

### 8.2 Expected Value Calculation

```
EV = (275 x 0.25) + (366 x 0.50) + (460 x 0.25)
EV = 68.75 + 183.0 + 115.0
EV = 367p
```

### 8.3 Margin of Safety Analysis

```
Current Price: 306p

MoS vs Expected Value: (367 - 306) / 367 = 16.6%
MoS vs Base Case: (366 - 306) / 366 = 16.4%
MoS vs Bear Case: (275 - 306) / 275 = -11.3%  <-- UNDERWATER in bear case
```

### 8.4 Comparison with Thesis MoS

| Metric | Thesis | My Estimate |
|--------|--------|-------------|
| MoS vs Expected | 35.7% | **16.6%** |
| MoS vs Base | 34.9% | **16.4%** |
| MoS vs Bear | 15.4% | **-11.3%** |

**FINDING 6: The actual MoS is approximately HALF of what the thesis claims.** More critically, in my bear case the stock is 11% OVERVALUED, meaning there is no downside protection if things go wrong.

---

## 9. Sensitivity Table (DCF)

Varying WACC and growth around base case (normalized FCF = GBP 50M):

| | **Growth 4%** | **Growth 5%** | **Growth 6%** | **Growth 7%** | **Growth 8%** |
|--|:---:|:---:|:---:|:---:|:---:|
| **WACC 8.5%** | ~335p | ~385p | ~443p | ~510p | ~595p |
| **WACC 9.0%** | ~310p | ~350p | ~400p | ~460p | ~535p |
| **WACC 9.5%** | ~285p | ~320p | ~365p | ~415p | ~480p |
| **WACC 10.0%** | ~265p | ~295p | ~335p | ~380p | ~440p |
| **WACC 10.5%** | ~245p | ~275p | ~310p | ~350p | ~400p |

**Key observation:** At my base WACC of 9.5%, the stock is only fairly valued (306p) at growth of ~5%. This means the market is pricing in about 5% FCF growth -- which is actually reasonable given the H1 deceleration.

---

## 10. Validation

### 10.1 Implied Multiples at My FV

At my fair value of 366p:

| Metric | Value |
|--------|-------|
| Market Cap implied | GBP 865M |
| P/E on FY2025 EPS (22.8p) | 16.0x |
| P/E on FY2026E EPS (23p) | 15.9x |
| EV/EBIT on FY2025 (GBP 66M) | 12.5x |
| FCF yield on normalized GBP 50M | 5.8% |

**These multiples are reasonable:** 16x P/E for a quality UK mid-cap with 6% growth is in line with peers (Softcat 17.7x, CCC 20.7x). Not cheap, not expensive.

### 10.2 Implied Multiples at Thesis FV (455p)

| Metric | Value |
|--------|-------|
| Market Cap implied | GBP 1,076M |
| P/E on FY2025 EPS (22.8p) | 20.0x |
| P/E on FY2026E EPS (23p) | 19.8x |
| EV/EBIT on FY2025 (GBP 66M) | 15.7x |

**This would imply BYIT deserves a PREMIUM to Softcat** (17.7x P/E), which is hard to justify given:
- Softcat has higher ROIC (36% vs BYIT's ~25%)
- Softcat has larger scale (3.3x market cap)
- Softcat has lower Microsoft concentration risk
- Softcat has stronger historic OP growth trajectory

### 10.3 Validation vs Precedents

From decisions_log.yaml, Tier A purchases:

| Ticker | QS | MoS at Purchase | Thesis FV Accuracy (if known) |
|--------|-----|-----------------|-------------------------------|
| ADBE | 76 | 31% | Pending |
| NVO | 82 | 38% | Pending |
| MONY.L | 81 | 36% (adversarial revised to -27% delta) | Pending |
| AUTO.L | 79 | 29% | Pending |
| LULU | 82 | 34% | Pending |

From the adversarial review (Session 51), 12/13 positions had inflated FV with average -15% delta. My finding of -20% for BYIT is consistent with this pattern but slightly worse.

### 10.4 Director Purchase Context

The thesis notes a director bought shares at 402p. This is a positive signal but:
- 402p is ABOVE my fair value of 366p
- Director purchases can be wrong (insiders are not infallible valuation specialists)
- The purchase may have been governance-driven (show confidence)
- At 402p, the director would have been buying at my bull case range, which requires 8%+ growth

---

## 11. Key Findings Summary

| # | Finding | Impact |
|---|---------|--------|
| 1 | FCF of GBP 48M (thesis) is conservative; actual FY2025 was GBP 64.9M but includes working capital timing | Neutral -- normalized ~GBP 50M is fair |
| 2 | Growth assumption of 8% is optimistic given H1 flat GP; 6% is more realistic base | **FV -10 to -15%** |
| 3 | OEY fair value is 380p vs thesis 470p | **FV -19%** |
| 4 | Softcat P/E has re-rated from 25x to 17.7x, undermining the "massive discount" argument | **FV -10 to -15%** |
| 5 | Weighted FV is 366p vs thesis 455p, a consistent -20% across all methods | **FV -20% total** |
| 6 | MoS is 16.6% (not 35%), and bear case shows -11% downside | **Risk materially higher than thesis suggests** |

---

## 12. Risk-Adjusted Fair Value

Applying the adversarial findings:

| Metric | Thesis | Adversarial | Delta |
|--------|--------|-------------|-------|
| **Fair Value** | 455p | **366p** | **-20%** |
| **Bear Case** | 350p | **275p** | **-21%** |
| **Bull Case** | 580p | **460p** | **-21%** |
| **Expected Value** | 460p | **367p** | **-20%** |
| **MoS vs EV** | 35.7% | **16.6%** | -19pp |
| **MoS vs Bear** | 15.4% | **-11.3%** | -27pp |

**Verdict on current price (306p):**

At 306p vs adversarial FV of 366p, there IS upside (~20%), but:
- The MoS of 16.6% is borderline for a Tier A compounder (precedent range: 29-38%)
- The bear case of 275p means 10% downside if things go wrong
- The risk/reward is not as compelling as the thesis suggests

At the thesis's ADD trigger of 260p, my adversarial analysis would show:
- MoS vs 366p FV = 29% -- in line with Tier A precedents
- MoS vs 275p bear = 5.5% -- minimal but positive downside protection
- This would be a more appropriate entry point

---

## 13. Meta-Reflection

### Dudas/Incertidumbres

1. **FCF normalization is subjective.** FY2025 FCF of GBP 64.9M included a GBP 49.6M payables swing. Is GBP 50M too conservative? FY2022 was GBP 51.4M when the business was smaller. Perhaps GBP 52-55M is fairer, which would raise my FV by ~5%.

2. **H2 FY2026 is the key unknown.** If management achieves their "high single-digit OP growth" guidance, it would validate the thesis's growth assumption and raise my estimates. H2 results (expected May 12, 2026) are the most important data point.

3. **Microsoft commercial price increases (July 2026)** are a material positive catalyst not fully captured in my analysis. 8-33% price increases across M365 products should boost GII and potentially GP in FY2027. This could push GP growth back above 8% from FY2027 onward.

4. **The GBP 25M share buyback** will reduce shares by ~3-4% at current prices, boosting EPS. This is a real value creator not reflected in the DCF tool's share count assumption.

5. **Softcat's re-rating concerns me.** If even the highest-quality UK VAR is being de-rated from 25x to 18x, this may signal a structural re-rating of the entire UK VAR sector. The market may see something about Microsoft's long-term partner strategy that I'm not capturing.

### Sensibilidad Preocupante

- If growth is 5% (not 6%), FV drops to ~330p (MoS only 7.8%)
- If growth is 4% and WACC is 10%, FV drops to ~295p (BELOW current price)
- Terminal value is 65-75% of EV in all DCF scenarios -- excessive dependence on far-future assumptions

### Discrepancias con Thesis

1. **Growth rate:** Thesis 8% vs my 6% -- the H1 data does not support 8% as BASE case. It could be bull case.
2. **Softcat valuation gap:** Thesis claims "massive discount vs Softcat at 25x." Actual Softcat is 17.7x trailing. The gap is real but much smaller (21% premium, not 79%).
3. **MoS:** Thesis claims 35%; my calculation shows 16.6%. This is a material overstatement that affects position sizing and conviction calibration.
4. **Bear case:** Thesis bear of 350p has no downside to current 306p (15% MoS). My bear of 275p shows 10% downside. The risk profile is worse than presented.

### Sugerencias para el Sistema

1. **Always verify peer multiples at time of valuation, not from thesis.** Softcat's re-rating from 25x to 18x happened during the analysis period and the thesis did not capture it.
2. **When a company guides "high single-digit" growth but H1 shows negative growth, the base case should not be AT guidance but BELOW it.** Management guidance has inherent optimism.
3. **Share buybacks should be explicitly modeled** in the valuation (reduce share count in out-years of DCF).

### Preguntas para Orchestrator

1. Given my adversarial FV of 366p (MoS 16.6%), is 306p still a compelling entry? Or should we lower the ADD trigger to 260p and await H2 results?
2. The Softcat re-rating changes the relative value argument. Should we verify whether AUTO.L and MONY.L (other UK positions) have also seen comparable re-ratings?
3. H2 FY2026 results (May 12, 2026) are the key inflection point. Should we set a standing order for ADD at 260p but also prepare a sell scenario if H2 disappoints?
4. The adversarial review pattern (Sessiones 50-51) found 12/13 positions had ~15% inflated FV. BYIT at -20% is consistent. Should we systematically re-derive fair values for ALL positions using adversarial parameters?

---

**Sources:**
- [Bytes Technology H1 FY2026 Interim Results](https://www.bytesplc.com/media/s3qkpjfi/btg-interim-results-31aug25-rnsfinal-sc-tel.pdf)
- [Bytes Technology FY2026 Guidance Analysis](https://www.asktraders.com/analysis/bytes-technology-group-navigates-market-headwinds-maintains-fy26-guidance/)
- [Softcat FY2025 Full Year Results](https://www.softcat.com/4717/6111/2589/Softcat_plc_Prelims_FY2025.pdf)
- [Microsoft FY26 CSP Program Changes](https://cspcontrolcenter.com/microsoft-csp-2026-program-changes/)
- [Microsoft Commercial Price Increases July 2026 (Bytes UK)](https://www.bytes.co.uk/info/news/microsoft-commercial-price-increases-effective-july-2026-uk-focused-report)
- [Bytes Technology Analyst Consensus - MarketScreener](https://www.marketscreener.com/quote/stock/BYTES-TECHNOLOGY-GROUP-PL-116485507/consensus/)
- [DirectorsTalk BYIT Stock Analysis](https://www.directorstalkinterviews.com/bytes-technology-group-plc-byit-l-stock-analysis-unveiling-a-43-62-potential-upside/4121228720)
- [Microsoft FY26 Partner Incentives Update](https://connect.tdsynnex.be/blog/media-library/microsoft-fy26-incentives-update/)
