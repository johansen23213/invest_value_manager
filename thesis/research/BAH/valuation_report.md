> **Fair Value:** $88

# Valuation Report: BAH (Booz Allen Hamilton)

## Date: 2026-02-13

---

## Company Classification

- **Type:** Government IT Services / Consulting (Stable-ish, but currently in CYCLICAL TROUGH with potential STRUCTURAL headwind)
- **Quality Tier:** B (QS Tool 73, Adjusted 68)
- **Moat:** NARROW (16/25 -- moat-assessor)
- **Risk Rating:** VERY HIGH (risk-identifier -- 2 CRITICAL, 3 HIGH, all correlated)
- **Methods Selected:** EV/EBIT Normalized (Primary, 60%) + P/E Relative (Secondary, 40%)
- **DCF used as:** Cross-check only (not primary -- see rationale below)

### Why NOT DCF as Primary Method

BAH's FCF is too volatile for DCF to be reliable as a primary valuation method:
- FY2022: $657M (7.9% margin)
- FY2023: $527M (5.7% margin)
- FY2024: $192M (1.8% margin -- anomalous)
- FY2025: $911M (7.6% margin)

The DCF sensitivity analysis confirms the problem: Terminal Value accounts for 72.2% of Enterprise Value, and the FV Spread is 95% ($56-140 depending on inputs). A method where a 1.5pp WACC change moves fair value by $30/share is not trustworthy as a primary source. EV/EBIT with observable peer multiples is more grounded for this type of business.

---

## Method 1: EV/EBIT Normalized (Primary -- 60% weight)

### EBIT Normalization

Government contractors have volatile margins due to contract mix, shutdowns, and restructuring charges. I normalize across 4 years of available data:

| Fiscal Year | Revenue | EBIT | Op Margin | Notes |
|-------------|---------|------|-----------|-------|
| FY2022 | $8.4B | ~$689M | 8.2% | Pre-growth ramp |
| FY2023 | $9.3B | ~$446M | 4.8% | Anomalous -- restructuring, FCA settlement |
| FY2024 | $10.7B | ~$1,017M | 9.5% | Growth year |
| FY2025 | $12.0B | ~$1,368M | 11.4% | Peak (pre-DOGE) |
| FY2026E | $11.3-11.4B | ~$1,190M | ~10.5% | DOGE-impacted guidance |

**Exclusion:** FY2023 EBIT ($446M) is anomalous due to restructuring charges and FCA settlement effects. Including it would distort the normalized figure.

**Approach:** Use FY2026E EBIT as the basis, not historical average. Reasoning: The fundamental analyst's thesis correctly notes that revenue is DECLINING, not growing. Historical average EBIT includes pre-DOGE peak revenue years that will not recur in the near term. FY2026E EBIT (~$1.19B based on adjusted EBITDA guidance of ~$1.24B minus ~$50M D&A) reflects the CURRENT earnings power under DOGE pressure.

**Normalized EBIT: $1.19B** (FY2026E, management guidance)

### Multiple Derivation

**Peer multiples (current):**

| Company | EV/EBIT | P/E | ROIC | Growth Profile | Notes |
|---------|---------|-----|------|----------------|-------|
| LDOS | ~14x | 16.4x | ~10% | Stable mid-single | Largest, diversified |
| SAIC | ~9x | 11.2x | N/A | Low-single | Smaller, less differentiated |
| CACI | ~18x | 25.0x | ~9% | Mid-teens growth | Premium for growth + intel focus |
| KBR | ~12x | 13.0x | N/A | Mid-single | International, engineering |
| **Peer median** | **~13x** | **13.0x** | | | |

**BAH vs peers -- multiple adjustment reasoning:**

Starting point: Peer median EV/EBIT = 13x

Adjustments:
- **Highest ROIC in sector (+18pp spread):** This is genuinely exceptional and warrants a premium. However, ROIC trajectory is volatile (8.4% in FY2023 to 23.6% in FY2025) and FORWARD ROIC will likely compress as civil revenue (higher margin) declines. +1x premium, tempered by forward compression risk.
- **Moat assessment: NARROW, actively eroding:** DOGE is breaking switching costs in the civil segment. Single-customer concentration (98%) is a structural fragility. The moat protects the defense oligopoly but not BAH specifically. -1x discount.
- **Revenue is DECLINING (not growing):** FY2026E revenue -5-6% YoY. Peers with growth command premiums; BAH is shrinking. SAIC at similar P/E (11.2x) also has flat/declining growth. -1x discount.
- **Elevated specific risks:** Treasury breach reputational contagion, CFO departure, 8.17% short interest rising, pattern of compliance failures (Snowden, FCA, Littlejohn). -0.5x discount.
- **AI business growing 30%+:** $800M in government AI revenue is a genuine differentiator and growth offset. +0.5x premium.

**Net adjustment:** +1x - 1x - 1x - 0.5x + 0.5x = **-1x from peer median**

**Fair multiple for BAH: 12x EV/EBIT**

Sanity check: 12x EV/EBIT is between SAIC (9x, lower quality) and LDOS (14x, larger/diversified). For a company with BAH's margins but declining revenue and elevated risk, 12x is reasonable. It is below BAH's own historical median (~15x) which is appropriate given DOGE represents a different operating environment than the past decade.

### Calculation

```
EBIT (normalized, FY2026E): $1.19B
Multiple: 12x
Enterprise Value: $1.19B x 12 = $14.28B
Net Debt: $3.25B (total debt $4.1B - cash $882M)
Equity Value: $14.28B - $3.25B = $11.03B
Shares Outstanding: 120.5M (approximate)
Fair Value per Share: $91.53

Rounding: $92/share
```

**Sensitivity to multiple selection:**

| EV/EBIT Multiple | Enterprise Value | Equity Value | FV/Share |
|-------------------|-----------------|-------------|----------|
| 10x (bear) | $11.90B | $8.65B | $72 |
| 11x | $13.09B | $9.84B | $82 |
| **12x (base)** | **$14.28B** | **$11.03B** | **$92** |
| 13x (peer median) | $15.47B | $12.22B | $101 |
| 14x (LDOS level) | $16.66B | $13.41B | $111 |
| 15x (BAH historical) | $17.85B | $14.60B | $121 |

---

## Method 2: P/E Relative with Growth Adjustment (Secondary -- 40% weight)

### Earnings Basis

- **FY2026E adjusted EPS: $5.95-6.15** (management guidance, midpoint $6.05)
- **FY2027E EPS (base case, +3% revenue growth, margin stable):** ~$6.30-6.50
- **Normalized EPS (FY2026-FY2027 avg):** ~$6.20

I use FY2026E EPS ($6.05) as the primary basis rather than forward estimates, because:
1. FY2027 guidance does not yet exist
2. The civil segment trajectory is highly uncertain
3. Using current-year guidance is more conservative and defensible

### P/E Multiple Derivation

**Peer P/E multiples:**

| Company | P/E | Growth | Quality Notes |
|---------|-----|--------|---------------|
| LDOS | 16.4x | Stable mid-single | Diversified, larger |
| SAIC | 11.2x | Flat/declining | Smaller, lower margins |
| CACI | 25.0x | Mid-teens | Intelligence premium, no dividend |
| KBR | 13.0x | Mid-single | International, mixed |
| **Median** | **14.7x** | | |

**BAH historical P/E range:** 12-25x (since 2010 IPO). Current 11.9x is the lowest EVER.

**Fair P/E reasoning:**

BAH's ROIC (23.6%), gross margins (54.8%), and AI growth (30%+) would normally justify a P/E above the peer median. However:

1. Revenue is declining 5-6% (peers generally flat to growing)
2. DOGE represents a regime change, not a normal cyclical dip
3. Civil segment (35% of earnings) has structural headwinds
4. Risk assessment is VERY HIGH with correlated risks
5. CFO departed, management credibility questionable (May-Oct guidance miss)

Fair P/E: **13-14x** on FY2026E EPS

This is below the peer median (14.7x) and at the low end of BAH's historical range, reflecting the DOGE headwinds and elevated risk. It is above SAIC (11.2x) because BAH has superior ROIC and AI positioning.

### Calculation

```
FY2026E EPS: $6.05 (midpoint of guidance)
P/E Multiple: 13.5x (midpoint of 13-14x range)
Fair Value: $6.05 x 13.5 = $81.68

Rounded: $82/share
```

**Sensitivity:**

| P/E Multiple | On FY2026E EPS ($6.05) | On Normalized EPS ($6.20) |
|-------------|----------------------|--------------------------|
| 11x (SAIC level) | $67 | $68 |
| 12x | $73 | $74 |
| **13x** | **$79** | **$81** |
| **14x** | **$85** | **$87** |
| 15x | $91 | $93 |
| 16x (LDOS level) | $97 | $99 |

---

## Reconciliation

| Method | Fair Value | Weight | Weighted |
|--------|-----------|--------|----------|
| EV/EBIT (12x normalized) | $92 | 60% | $55.20 |
| P/E (13.5x FY2026E) | $82 | 40% | $32.80 |
| **Weighted Average** | | **100%** | **$88.00** |

**Divergence between methods:** ($92 - $82) / $87 avg = **11.5%** -- ACCEPTABLE (below 30% threshold). The divergence is explained by the fact that EV/EBIT captures the full enterprise value including debt capacity, while P/E is penalized by interest expense on $4.1B debt. Both point to the same conclusion: fair value is in the $82-92 range.

**Why $88 and not $95 (thesis FV):**

The thesis used 13x EV/EBIT and 14x P/E as base cases, arriving at $96 weighted. My analysis agrees on the EV/EBIT multiple (12-13x) but I weight the lower end because:
1. The risk assessment is VERY HIGH (not just HIGH)
2. All 5 major risks are correlated (single-customer dependency amplifies everything)
3. The moat assessment is NARROW, not WIDE
4. Civil decline appears structural, not cyclical (moat-assessor gives 50% probability)
5. The compliance failure pattern (Snowden -> FCA -> Littlejohn) suggests governance risk premium

I set final FV at **$88** (slightly below the mechanical $88.00 to keep a round number that reflects the downward bias of my qualitative concerns).

---

## DCF Cross-Check

### Base Case DCF: 3% growth, 9% WACC, 2% terminal

| Scenario | FV/Share | MoS vs $80 |
|----------|---------|------------|
| Bear | $65.32 | -18.4% |
| Base | $87.92 | +9.8% |
| Bull | $119.30 | +49.0% |

### Conservative DCF: 0% growth, 10% WACC, 1.5% terminal

| Scenario | FV/Share | MoS vs $80 |
|----------|---------|------------|
| Bear | $42.70 | -46.7% |
| Base | $57.66 | -28.0% |
| Bull | $77.46 | -3.3% |

### Optimistic DCF: 5% growth, 9% WACC, 2.5% terminal

| Scenario | FV/Share | MoS vs $80 |
|----------|---------|------------|
| Bear | $78.47 | -2.0% |
| Base | $105.63 | +31.9% |
| Bull | $144.13 | +80.0% |

### DCF Sensitivity Matrix (3% base growth, 9% base WACC)

| Growth \ WACC | 7.5% | 9.0% | 10.5% |
|---------------|------|------|-------|
| 0.0% | $101.2 | $73.9 | $56.3 |
| 1.5% | $110.0 | $80.7 | $61.8 |
| **3.0%** | $119.4 | **$87.9** | $67.5 |
| 4.5% | $129.3 | $95.5 | $73.6 |
| 6.0% | $139.8 | $103.5 | $80.0 |

**Key observations from DCF:**
- Terminal Value as % of EV: **72.2%** -- high, characteristic of asset-light services businesses
- FV Spread: **95%** ($56-140) -- extremely sensitive to inputs, confirming DCF should NOT be the primary method
- At 9% WACC and 3% growth (my base case parameters), DCF produces $87.92 -- consistent with my weighted FV of $88
- At 10.5% WACC (reflecting VERY HIGH risk), even 3% growth only produces $67.50
- The current price of $80.09 implies ~1.5% growth at 9% WACC, or ~6% growth at 10.5% WACC

**DCF cross-check verdict:** Consistent with the $88 FV from EV/EBIT + P/E methods. DCF range spans $65-120, with my $88 sitting in the lower half -- appropriate given VERY HIGH risk rating.

---

## Scenarios

| | Bear (30%) | Base (45%) | Bull (25%) |
|--|-----------|-----------|-----------|
| **Narrative** | DOGE expands to defense advisory, civil permanently shrinks 30%+, additional agency cancellations (domino from Treasury breach), margins compress | Civil bottoms FY2027 at ~60-70% of peak, defense grows 5-7%, AI business $1B+, margins hold 10-11%, gradual recovery | DOGE reversed/scaled back, $1.5T defense budget realized in full, AI boom accelerates, civil partially recovers, P/E re-rates |
| **Revenue (FY2028E)** | $9.8-10.2B | $11.5-12.0B | $13.0-14.0B |
| **FY2028E EBIT** | $880M-920M (9% margin) | $1.2-1.3B (10.5-11% margin) | $1.5-1.7B (12% margin) |
| **EV/EBIT Multiple** | 9-10x | 12-13x | 15-16x |
| **Fair Value** | **$55-60** | **$88** | **$130-140** |
| **MoS from $80.09** | **-25% to -31%** | **+10%** | **+62% to +75%** |

### Probability Weighting

**NOTE:** I assign 30% to Bear (not the standard 25%) because:
1. DOGE risk is ALREADY materializing, not hypothetical
2. All 5 major risks are correlated (amplification effect)
3. Risk assessment is VERY HIGH
4. Short interest rising 22% suggests institutional conviction on further downside

I reduce Bull to 25% (from standard 25%) because:
1. DOGE reversal requires political change that is not imminent
2. Civil recovery assumption is optimistic given structural shift
3. P/E re-rating requires sentiment change that depends on catalysts that are uncertain

| Scenario | Fair Value | Probability | Weighted |
|----------|-----------|-------------|----------|
| Bear | $58 (midpoint) | 30% | $17.40 |
| Base | $88 | 45% | $39.60 |
| Bull | $135 (midpoint) | 25% | $33.75 |
| **Expected Value** | | **100%** | **$90.75** |

---

## Summary

| Metric | Value |
|--------|-------|
| **Current Price** | **$80.09** |
| **Fair Value (weighted methods)** | **$88** |
| **Expected Value (probability-weighted scenarios)** | **$91** |
| **MoS vs Base FV** | **+10%** |
| **MoS vs Expected Value** | **+14%** |
| **MoS vs Bear Case** | **-28% to -37%** (significant downside risk) |

### Validation vs Peers

| Metric | BAH (at FV $88) | LDOS | SAIC | CACI |
|--------|-----------------|------|------|------|
| Implied P/E (on FY26E EPS) | 14.5x | 16.4x | 11.2x | 25.0x |
| Implied EV/EBIT | ~13x | ~14x | ~9x | ~18x |
| Div Yield (at FV) | 2.7% | 1.4% | 1.8% | 0.0% |

The implied multiples at $88 FV are reasonable: above SAIC (lower quality), below LDOS (larger, more diversified), and well below CACI (growth premium). No red flags.

### Validation vs Precedents

From `decisions_log.yaml`:
- ROP standing order at $300 = 22% MoS for Tier B with HIGH risk. BAH at $88 FV with current price $80 = only 10% MoS. This is INSUFFICIENT for a Tier B company with VERY HIGH risk.
- HRB was bought at 42% MoS (Tier B) and lost 13.25% -- lesson learned that high MoS alone does not protect against structural deterioration.
- Pattern: For Tier B with elevated risk, we have typically required 20-25%+ MoS. BAH at $80 has only 10% MoS vs $88 FV.

---

## Entry Recommendation

**At current price of $80.09, MoS is only 10% vs $88 FV -- INSUFFICIENT for Tier B with VERY HIGH risk.**

The risk assessment documents 2 CRITICAL + 3 HIGH risks, all correlated through single-customer dependency. The bear case ($55-60) has 30% probability. At $80, the risk/reward asymmetry is unfavorable:
- Upside to FV: +10% ($88)
- Downside to bear: -28 to -37% ($50-58)
- Expected value-weighted return: +14%

Per precedent (ROP at 22% MoS for Tier B HIGH risk), BAH with VERY HIGH risk needs at minimum 25% MoS = entry at **$66** (25% below $88 FV).

However, given that the risk-identifier explicitly recommends $60-65 entry to provide genuine margin of safety for VERY HIGH risk, and given the MoS vs Bear analysis:

| Entry Price | MoS vs $88 FV | MoS vs Bear ($58) | Assessment |
|-------------|---------------|-------------------|------------|
| $80 (current) | 10% | -28% | INSUFFICIENT |
| $75 | 15% | -23% | Still insufficient for VERY HIGH risk |
| $70 | 20% | -17% | Borderline -- thesis suggested this |
| **$66** | **25%** | **-12%** | Minimum adequate for Tier B VERY HIGH risk |
| $60 | 32% | -3% | Risk-identifier recommendation |

**Recommended entry: $66** (25% MoS -- consistent with ROP precedent adjusted for VERY HIGH vs HIGH risk)

**Alternative entry: $70** (20% MoS -- if Q4 FY2026 earnings confirm civil bottoming AND no additional agency cancellations)

---

## DCF Sensitivity Table

| Growth \ WACC | 7.5% | 8.0% | 9.0% | 10.0% | 10.5% |
|---------------|------|------|------|-------|-------|
| 0.0% | $101 | - | $74 | - | $56 |
| 1.0% | $106 | - | $77 | - | $59 |
| 2.0% | $112 | - | $81 | - | $62 |
| **3.0%** | $119 | - | **$88** | - | $68 |
| 4.0% | $127 | - | $92 | - | $71 |
| 5.0% | $136 | - | $98 | - | $75 |

(Values interpolated from DCF tool output where available, estimated for intermediate points)

At the base WACC of 9% and base growth of 3%, DCF produces $88 -- consistent with EV/EBIT and P/E methods.

If one uses the WACC from quality_scorer (5.6%, based on beta 0.35 -- clearly too low for current risk), DCF would produce absurdly high FV ($150+). This demonstrates why beta needs to be manually adjusted for regime changes, and why I use 9% WACC (reflecting beta ~0.80 and an additional premium for DOGE execution risk).

---

## META-REFLECTION

### Dudas/Incertidumbres

- **EBIT normalization is the key judgment call.** I used FY2026E EBIT ($1.19B) rather than a 4-year average. If I used the 4-year average including FY2023 anomaly, normalized EBIT would be ~$880M, and FV at 12x would drop to $64/share. If I exclude FY2023 and average FY2022/2024/2025, normalized EBIT is ~$1.02B, giving FV of $79. The choice of normalization period materially changes the valuation. I chose FY2026E guidance because it reflects the CURRENT earnings power, which is what a buyer is purchasing.

- **The fair multiple (12x EV/EBIT) is a judgment call.** If BAH deserves peer median (13x), FV rises to $101. If DOGE risk warrants SAIC-level multiple (9x), FV drops to $63. The 12x I chose is defensible but not uniquely correct.

- **Civil segment permanence is the pivotal uncertainty.** If civil recovers to 80% of peak (cyclical interpretation), FV is materially higher. If civil permanently shrinks to 60% of peak (structural interpretation), FV is lower. I split the difference in the base case but the moat-assessor assigns 50% probability to the structural scenario -- which is concerning.

- **Compliance pattern risk is hard to quantify.** Snowden (2013), FCA settlement (2023), Littlejohn/Treasury (2026) -- three major compliance failures in 10 years. Is this bad luck or systemic? I applied a -0.5x multiple discount but this may be insufficient if another incident occurs.

### Sensibilidad Preocupante

- Changing the EV/EBIT multiple by 1x (from 12x to 13x or 11x) changes FV by $10/share (~11%). This is within normal valuation uncertainty but given the VERY HIGH risk rating, erring on the conservative side (12x) is appropriate.
- The DCF is extremely sensitive: WACC +/- 1.5pp changes FV by $20-30/share. This confirms DCF should not be the primary method for BAH.
- The probability weighting in scenarios matters: if Bear is 35% (not 30%) and Bull is 20% (not 25%), Expected Value drops from $91 to $86.

### Discrepancias con Thesis

- **Thesis FV: $95 vs. my FV: $88** -- a 7% difference. The divergence comes from: (1) I use 12x EV/EBIT vs thesis 13x, reflecting the moat-assessor's NARROW classification and risk-identifier's VERY HIGH rating which the thesis had not yet incorporated when it set 13x; (2) I weight bear scenario at 30% vs thesis 25%, because the DOGE risk is ALREADY MATERIALIZING, not hypothetical. The thesis entry of $70 (26% below $95) is close to my recommended $66 (25% below $88).

- **Risk assessment recommends $60-65 entry** while thesis recommends $70 and I recommend $66. The risk-identifier's bear case ($55-65 FV range) is more pessimistic than mine ($55-60), which would justify an even lower entry. However, at $60 entry the stock would need to fall another 25% from current price ($80) -- possible but may not be achievable unless DOGE significantly expands into defense.

### Sugerencias para el Sistema

- For government contractors with >90% single-customer revenue, the valuation framework should apply an automatic multiple discount (e.g., -1 to -2x from peer median) to reflect concentration risk. This is not a standard adjustment in our comparables-method skill.
- The DCF tool's sensitivity matrix should include a flag when Terminal Value exceeds 70% of Enterprise Value -- this is a signal that DCF should be used as cross-check only, not primary method.

### Preguntas para Orchestrator

1. The thesis sets entry at $70, I recommend $66. Should the quality_universe entry price be revised from $70 to $66, or is the thesis entry of $70 acceptable given it was already conservative vs the $95 FV?
2. Given that BAH at $80 has only 10% MoS and VERY HIGH risk, should this even remain on the watchlist or is the risk/reward profile insufficient to justify tracking?
3. The compliance failure pattern (3 major incidents in 10 years) suggests a governance discount that I quantified at -0.5x EV/EBIT. Should this be larger? The decisions_log shows we have not encountered this pattern before -- it could be a precedent worth documenting.

---
