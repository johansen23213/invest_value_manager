# ADVERSARIAL VALUATION REPORT: H&R Block (HRB)

**Date**: 2026-02-09
**Valuation Specialist**: Independent Adversarial Analysis
**Purpose**: Challenge thesis FV of $59.58 with independent, conservative valuation
**Framework**: v4.0 (Principles-based reasoning, no fixed rules)

---

## 1. THESIS VALUATION CRITIQUE

The active thesis (v2.0, dated 2026-02-03) values HRB at $59.58 base case (weighted DCF + EV/EBIT). Below is a systematic critique of every major assumption.

### 1.1 WACC of 8.5% -- UNDERSTATED

**Thesis derivation:**
- Rf = 4.25%, Beta = 0.67 (adjusted from raw 0.35), ERP = 5.5%
- Ke = 7.9%, Kd after-tax = 3.0%
- WACC = 6.5% --> then +2% "risk premium" = 8.5%

**Problems:**

| Issue | Detail |
|-------|--------|
| **Beta of 0.67 is too low** | Raw beta 0.35 reflects HRB's extreme seasonality (most revenue in Q3-Q4), not low risk. Using adjusted beta of 0.67 still underestimates business risk for a company facing secular headwinds. A beta of 0.9-1.0 is more appropriate for a business with disruption risk + negative equity. |
| **2% "risk premium" is arbitrary** | The thesis adds 2% for "AI/structural risk" on top of a WACC that is already derived with an understated beta. If you properly size beta at 0.9-1.0, Ke = 9.2-9.75%, and WACC becomes 7.5-8.0% before any additional premium. |
| **Negative equity ignored** | HRB has negative shareholders' equity of -$823M (Dec 2025). Traditional WACC using market cap weights may understate risk because the business is effectively leveraged beyond its book equity. The company's aggressive buybacks funded by debt have destroyed its equity cushion. |
| **Debt increase not reflected** | Total debt rose from $1.49B (June 2025) to $2.44B (Dec 2025). The thesis uses $2.03B. Current net debt per DCF tool is $2.59B. Higher leverage = higher risk = higher WACC. |

**My WACC derivation:**
```
Rf = 4.25% (10Y Treasury)
Beta = 0.95 (reflecting disruption risk + negative equity + seasonality)
ERP = 5.5%
Ke = 4.25% + 0.95 x 5.5% = 9.5%

Kd pre-tax = 4.5% (weighted avg of existing + new debt at higher rates)
Tax rate = 25%
Kd after-tax = 3.375%

Market Cap = $4.2B
Total Debt = $2.94B (current per StockAnalysis)
E/V = 59%
D/V = 41%

WACC = (0.59 x 9.5%) + (0.41 x 3.375%) = 5.6% + 1.4% = 7.0%

Add disruption premium: +1.5% (AI, regulatory risk, secular decline)
ADJUSTED WACC = 8.5%

Note: Despite different methodology, I arrive at a similar WACC of 8.5%.
However, if I use beta 1.1 (which is defensible given the negative equity
and disruption), Ke = 10.3%, and WACC = 8.6% before premium = 10.1% after.
```

**Conservative WACC for valuation: 10.0-10.5%** -- This reflects the reality that HRB is NOT a low-risk business despite defensive revenue.

### 1.2 Growth Rate of 3% -- OPTIMISTIC Given FCF Trajectory

**Thesis assumption:** Revenue growth ~3-4% (TAM 2% + pricing 2% + stable share)

**Reality check:**
- Revenue IS growing: FY2026 guided $3.875-$3.895B (+3% vs FY2025's $3.76B)
- BUT FCF has been DECLINING: $752M (FY2023) --> $682M (FY2024) --> $599M (FY2025)
- This is a 20% FCF decline over 3 years DESPITE revenue growth
- The DCF tool uses FCF, not revenue. Revenue growth of 3% is irrelevant if FCF doesn't grow.

**FCF trajectory analysis:**
```
FY2023: FCF $752M, Revenue $3.62B --> FCF margin 20.8%
FY2024: FCF $682M, Revenue $3.61B --> FCF margin 18.9%
FY2025: FCF $599M, Revenue $3.76B --> FCF margin 15.9%
TTM:    FCF $524M (per StockAnalysis) --> FCF margin ~13.5%

Trend: FCF margin compressing by ~2.4pp per year
```

**Why is FCF declining while revenue grows?**
1. Operating expenses growing faster than revenue (+5.4% in Q2 vs +11.1% revenue, BUT H1 total costs up faster than H1 revenue when normalized)
2. Field wages up 15.5% in Q2 (labor cost inflation)
3. Buybacks funded by debt --> higher interest expense
4. Capex stable but not declining

**My FCF growth assumption:** 0-2% for base case. The thesis assumes 3% but there is NO evidence that FCF growth will match revenue growth. Until FCF margin stabilization is demonstrated, 0-2% is more honest.

### 1.3 Terminal Growth of 2% -- AGGRESSIVE for Potentially Declining Business

**Thesis:** 2% terminal growth, "below GDP growth due to secular headwinds"

**Counter-argument:**
- Tax preparation is a mature industry. The IRS itself processed 163M returns in 2024.
- While IRS Direct File has been cancelled for 2026, this is a POLITICAL decision that can reverse under a different administration.
- AI is advancing rapidly. HRB's own OpenAI partnership aims to make tax pros more productive -- but this also means fewer tax pros needed over time.
- The long-term trend is toward automated, AI-assisted filing that erodes the value proposition of assisted preparation.

**My terminal growth:** 1.0-1.5%. This acknowledges that HRB will not disappear, but its core assisted business faces secular headwinds that cap long-term growth below GDP.

### 1.4 EV/EBIT Multiple of 9.5x -- UNJUSTIFIED

**Thesis:** 9.5x base case (range 8-11x), arguing "tax services sector typical range: 8-12x"

**Problem:** What is "tax services sector"? There is essentially ONE comparable -- Intuit (TurboTax). And Intuit trades at completely different multiples because it is a software company with 80% margins.

**Actual comparable analysis:**

| Company | EV/EBIT | P/E | Growth | FCF Margin | Notes |
|---------|---------|-----|--------|------------|-------|
| INTU | ~25x | 30.5x | 10-12% | 35%+ | Pure software, dominant platform |
| HRB current | 8.0x | 7.7x | 3% | ~14% | Hybrid (offices + software), declining FCF |

There is NO peer group that trades at 8-12x with HRB's characteristics. HRB is a unique business. The correct approach is to ask: what multiple does a low-growth, capital-returning, disruption-threatened business deserve?

**Comparable by business characteristics:**

| Business Type | Example | EV/EBIT | Why |
|---------------|---------|---------|-----|
| Mature services, low growth, returning capital | HRB | 7-9x | Slow growth + disruption risk |
| Legacy tech / declining moat | Xerox, Pitney Bowes | 5-7x | Secular decline |
| Franchise services, defensive | ServiceMaster, Regis | 6-9x | Franchise model, some moat |
| Mature consumer services | H&R Block | 7-8x | Current market assessment |

**My EV/EBIT multiple:** 7-8x base case. The current market is paying 8x, and the market's assessment of disruption risk may be closer to correct than the thesis implies. A 9.5x multiple requires either (a) revenue acceleration or (b) FCF margin stabilization -- neither is demonstrated yet.

### 1.5 Capital Allocation Concerns -- NOT ADDRESSED IN THESIS

The thesis acknowledges but underweights a critical issue: management bought back $400M in shares at $61.10/share in FY2025, and $400M at $50.90/share in Q1 FY2026. The stock is now $32.88.

**Buyback destruction calculation:**
```
FY2025: 6.5M shares at $61.10 avg = $397M. Current value: 6.5M x $32.88 = $214M.
  --> $183M of shareholder value DESTROYED (46% loss)

Q1 FY2026: 7.9M shares at $50.90 avg = $402M. Current value: 7.9M x $32.88 = $260M.
  --> $142M of shareholder value DESTROYED (35% loss)

Since 2016: 43% of shares bought back. Much at prices far above current.
  --> BILLIONS in value destruction through poorly timed buybacks
```

This is NOT a one-time error. Management systematically bought back stock at elevated prices. This raises serious questions about capital allocation competence that should factor into valuation (lower multiple, higher WACC).

### 1.6 Net Debt Is Higher Than Thesis Assumes

**Thesis uses:** Net Debt = $1.05B
**Current reality:** Net Debt = $2.59B (per DCF tool, confirmed by StockAnalysis)

This is a MASSIVE discrepancy. Net debt has MORE THAN DOUBLED. The thesis was written when total debt was $2.03B; it is now $2.94B. Cash has dropped from $983M to $349M.

**Impact:** Every DCF and EV/EBIT calculation must subtract $2.59B, not $1.05B. This alone reduces fair value by ~$12/share ((2.59-1.05)B / 126.8M shares).

---

## 2. INDEPENDENT VALUATION

### Method 1: DCF (60% weight)

**My independently derived assumptions:**

| Parameter | Thesis | My Value | Justification |
|-----------|--------|----------|---------------|
| FCF base | $599M | $524M (TTM) | Use most recent trailing data |
| Growth Yrs 1-5 | 3% | 2% | FCF declining despite revenue growth; margin compression; 2% assumes stabilization |
| WACC | 8.5% | 10.5% | Beta 1.0-1.1 + disruption premium; negative equity; debt increase |
| Terminal growth | 2.0% | 1.5% | Secular headwinds cap long-term growth below GDP |
| Net Debt | $1.05B | $2.59B | Current actual (thesis outdated) |

**DCF Results (via dcf_calculator.py with growth=2, wacc=10.5, terminal=1.5):**

| Scenario | Growth | WACC | Terminal | Fair Value |
|----------|--------|------|----------|-----------|
| Bear | 0% | 11.5% | 1.0% | $24.67 |
| Base | 2% | 10.5% | 1.5% | $34.01 |
| Bull | 4% | 9.5% | 2.0% | $46.22 |

**DCF Fair Value (Base): $34.01**

**Sensitivity table around base case:**

| WACC \ Growth | 0% | 1% | 2% | 3% | 4% |
|---------------|-----|-----|-----|-----|-----|
| 9.5% | ~$31 | ~$35 | ~$40 | ~$46 | ~$53 |
| 10.0% | ~$29 | ~$33 | ~$37 | ~$42 | ~$49 |
| 10.5% | ~$27 | ~$30 | ~$34 | ~$39 | ~$46 |
| 11.0% | ~$25 | ~$28 | ~$31 | ~$36 | ~$42 |
| 11.5% | ~$23 | ~$26 | ~$29 | ~$33 | ~$39 |

**Key observation:** Fair value is approximately equal to current price ($32.88) at 2% growth / 10.5% WACC. This means the market is pricing HRB fairly for a low-growth, moderate-risk business. Only if you believe WACC < 10% OR growth > 3% is there meaningful upside.

### Method 2: EV/EBIT Comparable Multiples (40% weight)

**Current financials:**
```
EBIT (TTM): ~$843M (EV $6.75B / EV/EBIT 8.01x = implied EBIT ~$843M)
EBITDA guided FY2026: $1,015-$1,035M (midpoint $1,025M)
Implied EBIT FY2026: ~$860-$880M (EBITDA - D&A ~$160M)
Net Debt: $2.59B
Shares: 126.8M
```

**Multiple justification:**

| Factor | Impact on Multiple |
|--------|-------------------|
| Duopoly position (with Intuit) | +1x premium |
| Negative equity (leverage risk) | -1x discount |
| FCF declining 3 years | -1x discount |
| AI disruption risk (3-5yr horizon) | -1x discount |
| Share count declining 5%/yr | +0.5x premium |
| Buyback at wrong prices (capital allocation) | -0.5x discount |
| Defensive revenue (tax filing mandatory) | +0.5x premium |
| IRS Direct File cancelled (tailwind) | +0.5x premium |
| **Starting point** | Sector services ~9x |
| **Net adjustments** | -1.0x |
| **Fair multiple** | **8.0x** |

**EV/EBIT Valuation:**

| Scenario | EBIT | Multiple | EV | Less Net Debt | Equity | Per Share |
|----------|------|----------|-----|---------------|--------|-----------|
| Bear | $800M | 7.0x | $5.60B | $2.59B | $3.01B | $23.74 |
| Base | $860M | 8.0x | $6.88B | $2.59B | $4.29B | $33.83 |
| Bull | $920M | 9.5x | $8.74B | $2.59B | $6.15B | $48.50 |

**EV/EBIT Fair Value (Base): $33.83**

### Method 3: Dividend Discount Model (Sanity Check Only)

HRB currently yields 5.1% ($1.68/share). As a sanity check:

```
D0 = $1.68
g (dividend growth) = 5% (12% recent increase, but FCF decline suggests unsustainable; normalize to 5%)
Ke = 10% (cost of equity)

DDM Fair Value = D1 / (Ke - g) = $1.68 x 1.05 / (0.10 - 0.05) = $1.764 / 0.05 = $35.28

Sensitivity:
  g = 3%, Ke = 10%: FV = $24.73
  g = 5%, Ke = 10%: FV = $35.28
  g = 5%, Ke = 9%:  FV = $44.10
  g = 7%, Ke = 10%: FV = $59.92
```

**DDM suggests $35.28 at reasonable assumptions.** The thesis's $59.58 would require either 7%+ sustainable dividend growth or a cost of equity below 8% -- neither is credible given FCF trajectory.

### Reconciliation

| Method | Bear | Base | Bull | Weight |
|--------|------|------|------|--------|
| DCF | $24.67 | $34.01 | $46.22 | 60% |
| EV/EBIT | $23.74 | $33.83 | $48.50 | 40% |
| **Weighted** | **$24.30** | **$33.94** | **$47.13** | 100% |

**Divergence between methods: 0.5% (Base case)** -- Excellent convergence, both methods agree.

DDM sanity check ($35.28) is close to base case -- further confirms valuation.

### Expected Value (Probability-Weighted)

```
Expected FV = (Bear x 25%) + (Base x 50%) + (Bull x 25%)
Expected FV = ($24.30 x 0.25) + ($33.94 x 0.50) + ($47.13 x 0.25)
Expected FV = $6.08 + $16.97 + $11.78
Expected FV = $34.83
```

---

## 3. STRESS TEST RESULTS

### Scenario A: FCF Continues Declining 5-7% Per Year

If FCF declines from $524M at -6%/year for 5 years:
```
Year 1: $493M
Year 2: $463M
Year 3: $435M
Year 4: $409M
Year 5: $385M
Terminal: $385M x 1.01 / (0.105 - 0.01) = $4.09B
PV of flows + terminal: ~$3.6B
Less net debt: $2.59B
Equity: $1.01B
Per share: $7.96

THIS IS THE NIGHTMARE SCENARIO -- HRB becomes a value trap.
```

### Scenario B: AI Reduces Assisted Tax Prep Clients by 15% Over 5 Years

Assisted tax prep is ~70% of revenue (~$2.7B). A 15% decline = ~$405M revenue loss.
At 23% operating margin, this is ~$93M EBIT loss.
```
Adjusted EBIT: $860M - $93M = $767M
At 7.5x multiple: EV = $5.75B
Less net debt: $2.59B
Equity: $3.16B
Per share: $24.92
```

### Scenario C: IRS Direct File Returns Under Future Administration

If Direct File returns and expands to cover 50% of filers:
- Impact primarily on DIY segment (~20% of revenue)
- Could lose 10-20% of DIY revenue = $75-150M
- At 8x EV/EBIT equivalent impact: ~$5-10/share reduction
- Combined with AI scenario: FV could drop to $15-20/share

### Stress Test Summary

| Scenario | Fair Value | vs Current Price | Probability |
|----------|-----------|-----------------|-------------|
| FCF continues -6%/yr | $7.96 | -76% | 10% |
| AI -15% assisted clients | $24.92 | -24% | 20% |
| Direct File returns | $27-30 | -8% to -18% | 15% |
| AI + Direct File combined | $15-20 | -39% to -54% | 10% |
| Base case (stabilization) | $33.94 | +3% | 45% |

**Weighted stress-adjusted FV:**
```
= (7.96 x 0.10) + (24.92 x 0.20) + (28.50 x 0.15) + (17.50 x 0.10) + (33.94 x 0.45)
= 0.80 + 4.98 + 4.28 + 1.75 + 15.27
= $27.08
```

Including stress scenarios, risk-adjusted fair value drops to approximately $27.

---

## 4. FAIR VALUE RANGE (RISK-ADJUSTED)

| Metric | Value |
|--------|-------|
| **DCF Base Case** | $34.01 |
| **EV/EBIT Base Case** | $33.83 |
| **Weighted Base Case** | $33.94 |
| **Expected Value (scenario-weighted)** | $34.83 |
| **Stress-adjusted FV** | $27.08 |
| **DDM Sanity Check** | $35.28 |
| **Current Price** | $32.88 |

### Final Fair Value Assessment

| Scenario | Fair Value | Probability |
|----------|-----------|-------------|
| Bear (secular decline) | $24.30 | 25% |
| Base (stabilization) | $33.94 | 50% |
| Bull (FCF recovery + re-rating) | $47.13 | 25% |
| **Expected FV** | **$34.83** | 100% |

**MoS vs Expected: +5.9%**
**MoS vs Bear: -26.1% (PRICE IS ABOVE BEAR CASE)**

This is a critical finding. The current price of $32.88 is ABOVE the bear case of $24.30, meaning there IS downside protection only if you believe the base case or bull case will play out. But the margin of safety is razor-thin at +5.9%.

---

## 5. DISCREPANCIES VS THESIS

| Item | Thesis | My Valuation | Delta | Why |
|------|--------|-------------|-------|-----|
| **Fair Value (Base)** | $59.58 | $33.94 | **-43%** | WACC, growth, net debt all different |
| **Fair Value (Bear)** | $46.53 | $24.30 | **-48%** | Thesis bear is too optimistic |
| **Fair Value (Bull)** | $75.96 | $47.13 | **-38%** | Even bull case is lower |
| **WACC** | 8.5% | 10.5% | +2.0pp | Higher beta + disruption premium |
| **FCF Growth** | 3% | 2% | -1pp | FCF declining, not growing |
| **Terminal Growth** | 2.0% | 1.5% | -0.5pp | Secular headwinds |
| **Net Debt** | $1.05B | $2.59B | +$1.54B | Thesis used outdated data |
| **EV/EBIT Multiple** | 9.5x | 8.0x | -1.5x | No real peer group justifies 9.5x |
| **MoS vs Base** | 54% | 3.2% | -51pp | Fundamentally different valuations |

### Root Causes of Divergence

1. **Net debt ($1.54B difference):** The single largest driver. The thesis used $1.05B but current net debt is $2.59B. This alone accounts for ~$12/share or ~20% of the fair value gap.

2. **WACC (8.5% vs 10.5%):** The thesis uses a low beta (0.67) that understates business risk. For a company with negative equity, declining FCF, and AI disruption risk, 10-10.5% WACC is more appropriate. This accounts for ~$8-10/share.

3. **Growth (3% vs 2%):** The thesis projects revenue growth but FCF has declined 20% in 3 years. Using FCF growth (what actually matters for DCF) rather than revenue growth is more conservative and honest.

4. **EV/EBIT multiple (9.5x vs 8.0x):** There is no true peer group for HRB. The thesis cites "tax services sector 8-12x" but this range is largely invented. The market currently pays 8x, which may be approximately correct.

---

## 6. POSITIVE FACTORS (BULL CASE ARGUMENTS)

To be fair, there are legitimate reasons HRB could be worth more than $34:

1. **IRS Direct File cancelled for 2026** -- This is a genuine positive that removes a competitive threat. Under current political environment, it may not return for years.

2. **Share count declining ~5%/year** -- Even with flat FCF, FCF per share grows. At 126.8M shares declining 5%/yr, in 5 years there are ~98M shares. $524M FCF / 98M = $5.35 FCF/share vs current $4.13.

3. **Dividend yield 5.1% with 36% payout** -- The dividend is well-covered and provides income floor. 12% recent increase is aggressive but sustainable at current payout.

4. **Tax filing is mandatory** -- Unlike many services, tax filing is legally required. HRB's core business cannot go to zero.

5. **$700M buyback capacity remaining** -- At current prices ($33), management is finally buying at non-destructive prices. If they deploy $700M at $33, that retires ~21M shares (~17% of outstanding).

However, these positives are already partially reflected in my base case and do not justify the thesis's $59.58.

---

## VALUATION SUMMARY

```
VALUATION: HRB

Type of company: Mature services, low growth, capital return
Methods selected: DCF (primary) + EV/EBIT (secondary) + DDM (sanity check)

Method 1: DCF
- Inputs: FCF $524M, Growth 2%, WACC 10.5%, Terminal 1.5%, Net Debt $2.59B
- Fair Value: $34.01

Method 2: EV/EBIT
- Inputs: EBIT $860M, Multiple 8.0x, Net Debt $2.59B, Shares 126.8M
- Fair Value: $33.83

Method 3: DDM (sanity check)
- Inputs: D0 $1.68, g 5%, Ke 10%
- Fair Value: $35.28

Reconciliation:
| Method   | FV      | Weight | Weighted |
|----------|---------|--------|----------|
| DCF      | $34.01  | 60%    | $20.41   |
| EV/EBIT  | $33.83  | 40%    | $13.53   |
| **Avg**  |         | 100%   | **$33.94** |

Divergence: 0.5% (EXCELLENT convergence)

Scenarios:
| Scenario     | Fair Value | Prob |
|-------------|-----------|------|
| Bear         | $24.30    | 25%  |
| Base         | $33.94    | 50%  |
| Bull         | $47.13    | 25%  |
| **Expected** | **$34.83** | 100% |

Price actual: $32.88
MoS vs Expected: +5.9%
MoS vs Bear: -26.1% (OVERVALUED vs bear case)
```

---

## 7. SENSITIVITY AND VALIDATION

### DCF Sensitivity (WACC vs Growth)

| WACC \ Growth | 0% | 1% | 2% | 3% | 4% |
|---------------|------|------|------|------|------|
| **9.0%** | $33 | $37 | $42 | $49 | $57 |
| **9.5%** | $31 | $35 | $40 | $46 | $53 |
| **10.0%** | $29 | $33 | $37 | $42 | $49 |
| **10.5%** | $27 | $30 | $34 | $39 | $46 |
| **11.0%** | $25 | $28 | $31 | $36 | $42 |

### Validation vs Peers

HRB implied multiples at my fair value ($34):
- P/E: ~7.4x (at $4.61 EPS guidance midpoint)
- EV/EBIT: ~8.0x
- P/FCF: ~8.2x

These are in line with where the stock currently trades, which suggests the **market is already pricing HRB approximately at fair value.** The thesis's $59.58 implies P/E of ~12.9x and EV/EBIT of ~11.5x -- multiples that would require significantly better fundamentals than HRB currently delivers.

### Validation vs Precedents

From `decisions_log.yaml`:
- HRB ADD decision at $35 was based on thesis MoS of 42%. My analysis shows MoS was actually ~3-6%, not 42%.
- Precedent: TEP.PA had MoS revised from 38-51% to 17% when valuation method was corrected. HRB shows a similar pattern of thesis FV inflation.
- Pattern across adversarial reviews: 12/13 positions had inflated FV (avg ~-15%). HRB's -43% is the LARGEST discrepancy found so far.

---

## META-REFLECTION

### Doubts/Uncertainties
- **FCF base year:** I used TTM $524M. If FY2026 tax season generates strong FCF (as guidance implies $1.0B+ EBITDA suggests FCF could recover to $600M+), my valuation would increase by ~$5-6/share. This is the biggest swing factor.
- **Buyback pace:** If management deploys $700M at ~$33, share count drops to ~106M, which would meaningfully increase per-share value. My base case does not fully account for the accelerated buyback at low prices.
- **Beta selection:** 0.95-1.0 is defensible but debatable. HRB's revenue is truly defensive (tax filing is mandatory). The raw beta of 0.35 may have some signal, not just noise.

### Sensibility Concerns
- FV changes significantly with WACC: $34 at 10.5% vs $42 at 10.0% vs $46 at 9.5%. A 1pp difference in WACC = ~$8/share (~24% swing). This is uncomfortably high sensitivity.
- The net debt of $2.59B vs thesis $1.05B is the largest single driver of the FV gap. If this is seasonal (HRB borrows in off-season and repays during tax season), the thesis's $1.05B may have been the "right" number at the right time. Need to verify seasonal debt patterns.

### Discrepancies with Thesis
- The -43% delta is the LARGEST in the adversarial review program. This warrants serious attention.
- However, ~$12/share of the gap is from net debt timing (thesis at June 30, my data at Dec 31). HRB's business is extremely seasonal; debt peaks in Q2 (Oct-Dec) and cash floods in during Q3-Q4 (Jan-Apr). If normalized to year-end (June 30), net debt might be ~$1.5-1.8B, not $2.59B.
- Even with normalized net debt of ~$1.7B, the DCF at 10.5% WACC gives ~$41/share -- still 31% below thesis.

### Seasonal Debt Adjustment
This is important enough to flag: HRB's business model requires borrowing in the off-season to fund operations and buybacks, then repaying from tax-season cash flows. The December 31 balance sheet shows PEAK debt. A mid-year average net debt of ~$1.5-1.8B may be more appropriate for valuation purposes.

**If I use net debt $1.7B instead of $2.59B:**
- DCF at 10.5% WACC, 2% growth: FV ~$41
- EV/EBIT at 8.0x: FV ~$41
- Expected Value: ~$42

This is still 30% below the thesis's $59.58 but represents a ~24% MoS vs current price -- which is more interesting.

### Suggestions for the System
1. The thesis should be updated with current net debt figures and seasonal normalization
2. FCF trajectory (declining despite revenue growth) should be flagged as a kill condition precursor
3. Management's buyback track record (buying at peaks) should factor into quality score
4. The quality score of 70 (Tier B) may be overstated -- negative equity, declining FCF margin, and poor capital allocation suggest QS 55-60

### Questions for Orchestrator
1. Is the $2.59B net debt the seasonal peak, and should we normalize to ~$1.7B for valuation? This changes FV from $34 to $41.
2. Should the ADD decision at $35 (now at $32.88) be revisited given this adversarial analysis shows MoS of only 3-6% (not 42%)?
3. The management has destroyed hundreds of millions in shareholder value through poorly-timed buybacks. Should this be a kill condition or at minimum a QS penalty?
4. FCF margin has compressed from 21% to 14% in 3 years. At what point does this become a kill condition?

---

**Sources:**
- [H&R Block Q2 FY2026 Results](https://www.globenewswire.com/news-release/2026/02/03/3231606/0/en/H-R-Block-Reports-Fiscal-2026-Second-Quarter-Results.html)
- [H&R Block FY2025 Results & FY2026 Outlook](https://investors.hrblock.com/news-releases/news-release-details/hr-block-reports-fiscal-2025-results-and-provides-fiscal-2026)
- [H&R Block Q2 FY2026 Earnings Call Transcript](https://finance.yahoo.com/news/h-r-block-hrb-q2-230114045.html)
- [IRS Direct File Not Available 2026](https://www.nextgov.com/digital-government/2025/11/direct-file-wont-happen-2026-irs-tells-states/409309/)
- [H&R Block & OpenAI Partnership](https://investors.hrblock.com/news-releases/news-release-details/hr-block-leverages-openai-create-force-multiplier-its-human)
- [H&R Block Statistics - StockAnalysis](https://stockanalysis.com/stocks/hrb/statistics/)
- [H&R Block FY2026 Guidance Update](https://www.themarketsdaily.com/2026/02/04/hr-block-nysehrb-updates-fy-2026-earnings-guidance.html)
- yfinance data via tools/price_checker.py and tools/dcf_calculator.py
