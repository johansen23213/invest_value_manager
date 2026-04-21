# AON - Aon plc

> R1 Fundamental Analysis | Date: 2026-02-20
> Analyst: fundamental-analyst | Framework v4.0

---

## TL;DR

Aon is the #2 global insurance broker with an asset-light, commission-based model generating $3.2B FCF on $17.2B revenue. The stock is near its 52-week low ($324 vs $413 high, -21.5%) driven by: (1) an AI-related selloff in insurance broker stocks (Feb 9-10, AON -9.3%), and (2) margin dilution from the $13.4B NFP acquisition. The business model is fundamentally misunderstood by the AI narrative -- Aon operates in commercial/reinsurance broking where switching costs are enormous and AI chatbots are irrelevant. However, the DCF is highly sensitive (TV 74.5% of EV, FV spread 101%) and the reverse DCF shows the market is pricing 14.3% FCF growth -- above historical 2.1% FCF CAGR but in line with revenue growth trajectory post-NFP. This is NOT a screaming bargain -- it is a quality business at a reasonable price that requires patience for a proper entry.

---

## Quality Score

**QS Tool: 62/100 (Tier B)**

### QS Tool Breakdown
| Category | Score | Max | Notes |
|----------|-------|-----|-------|
| Financial Quality | 26 | 40 | ROIC spread +8.6pp (8/15), FCF margin 18.7% (8/10), Leverage 2.4x (5/10), FCF consistency 4/4 (5/5) |
| Growth Quality | 11 | 25 | Revenue CAGR +11.2% (8/10), EPS CAGR N/A (0/10), GM trend stable (3/5) |
| Moat Evidence | 17 | 25 | GM premium +17.7pp (10/10), Market position 0/8 (manual), ROIC persistence 7/7 |
| Capital Allocation | 8 | 10 | Shareholder returns 5/5, Insider ownership 2.8% (3/5) |
| **Total** | **62** | **100** | |

### QS Adjustment Reasoning

**Adjustment +8 points = QS Adjusted 70/100 (Tier B)**

1. **Market Position: +5 points** (0 -> 5/8)
   - Aon is #2 global insurance broker behind MMC, with $16.6B revenue
   - Top 4 brokers control ~97% of large broker revenue (MMC 40%, AON 25%, AJG 17%, WTW 15%)
   - In the PRECEDENT for MMC (decisions_log.yaml, Feb 2026), MMC received market position credit as #1. AON as #2 deserves 5/8 (consistent with #1-2 range receiving 8/8 in the QS rubric, but discounting because AON is solidly #2, not #1)

2. **Insurance Broker ROE adjustment: +3 points**
   - Per PRECEDENT (decisions_log.yaml: "Insurer QS adjustment protocol: ROIC->ROE +8, documented"), insurance companies should use ROE not ROIC
   - AON ROE: 39.5% (FY2025), 43.4% (FY2024) -- exceptionally high
   - However, AON's negative equity (common for brokers due to massive buybacks + goodwill write-downs) makes ROE meaningfully inflated. ROIC of 16.7% with +8.6pp spread is the more honest metric
   - Applying a conservative +3 (not the full +8 from insurer precedent) because: (a) ROIC is already positive and meaningful unlike pure insurers, (b) ROE is optically inflated by negative/near-zero equity, (c) the ROIC spread is genuine but not as understated as in pure underwriters

3. **Commission Business Flattery: -0 points**
   - Per PRECEDENT: "Commission businesses get -5 ROIC flattery adjustment"
   - However, AON's ROIC is already captured correctly by the tool at 16.7% with genuine invested capital. The commission business -5 precedent was for situations where ROIC was inflated by asset-light structure. Here, AON has $16B debt and $13.5B net debt -- it IS deploying significant capital. The ROIC spread of +8.6pp is genuine
   - Net adjustment: 0 (the commission flattery is already offset by the debt burden on ROIC)

**QS Adjusted: 70/100 (Tier B, upper end)**

Adjustment of +8 is within the max +20 without committee approval and is less than the +11 used for ACGL and +4 for MMC in precedent. Conservative and documented.

---

## Business Understanding

### Model de Negocio

Aon is a pure-play insurance and reinsurance intermediary. It does NOT underwrite risk. It earns commissions and fees by placing its clients' insurance and reinsurance programs with carriers. This is a fundamentally different (and superior) business model to insurance underwriting:

**Problem Solved:** Large corporations, governments, and institutions face complex risk management challenges (property, casualty, cyber, employee benefits, retirement). They need expert intermediaries to structure programs, access multiple carriers, negotiate terms, and manage claims.

**Revenue Model:**
| Segment | FY2025 Revenue | Organic Growth | % of Total | Description |
|---------|---------------|----------------|------------|-------------|
| Commercial Risk Solutions | ~$7.5B est. | 6% | ~44% | Property, casualty, cyber, specialty insurance brokerage |
| Reinsurance Solutions | ~$3.5B est. | 8% | ~20% | Reinsurance placement for insurance companies |
| Health Solutions | ~$3.5B est. | 2% | ~20% | Employee benefits, health insurance advisory |
| Wealth Solutions | ~$2.7B est. | 2% (ex-NFP Wealth sale) | ~16% | Retirement, investments, delegation |

**Revenue Quality:**
- ~85%+ recurring (client retention typically >95%)
- Commission-based: grows with premium rates AND policy complexity
- Benefits from BOTH hard and soft insurance markets (hard = higher commissions; soft = more advisory demand)
- NFP acquisition (April 2024, $13.4B) added middle-market access

### Unit Economics
- **CAC:** Very low for existing relationships -- renewal is nearly automatic. New client acquisition via relationships, not advertising
- **LTV:** Multi-decade relationships. Top 100 clients average 20+ year tenure
- **LTV/CAC:** Exceptionally high (>10x estimated). Once a large corporation embeds Aon's advisory and data into its risk management, switching is extremely costly
- **FCF Margin:** 18.7% (FY2025). Lower than pre-NFP (~24%) due to integration costs. Guided to recover with double-digit FCF growth in 2026
- **Capital Intensity:** Asset-light. Capex ~1.4x depreciation. Primary capital deployment is M&A (NFP) and buybacks

### Structure de Margenes
| Metric | FY2022 | FY2023 | FY2024 | FY2025 | Trend |
|--------|--------|--------|--------|--------|-------|
| Gross Margin | 48.1% | 48.4% | 47.2% | 47.7% | Stable |
| Operating Margin | 29.4% | 29.3% | 26.9% | 27.4% | Recovering post-NFP |
| Adj. Operating Margin | ~32% | ~31.5% | ~31.5% | 32.4% | Expanding |
| FCF Margin | 24.2% | 23.8% | 17.9% | 18.7% | Recovering |
| SBC/Revenue | 3.2% | 3.3% | 3.0% | 2.5% | Declining (positive) |

**Key Observation:** Margins were temporarily compressed in FY2024 by NFP integration costs and transaction expenses. FY2025 shows clear recovery trajectory. Management guides 70-80bps adj. margin expansion in FY2026.

### Por Que Esta Barata

**The Market Narrative (2 overlapping narratives):**

1. **AI Disruption Fear (Feb 9-10, 2026):** OpenAI approved Tuio's ChatGPT-based home insurance quoting app. Anthropic's Claude Cowork plugins also targeted insurance brokerage/consulting. Insurance broker stocks crashed: WTW -12%, AJG -9.9%, AON -9.3%, MMC -7%. This narrative treats insurance broking like commodity SaaS -- something AI chatbots can replace.

2. **NFP Integration Hangover:** The $13.4B NFP acquisition (April 2024) temporarily depressed margins, increased leverage to 2.9x ND/EBITDA, and introduced integration risk. The market is pricing uncertainty about whether synergies ($350M annual by 2026) will materialize and whether the deal was worth diluting margins for.

**My Contra-Thesis:**

1. **AI Threat is Massively Overblown for Commercial Broking (LEVEL 3 OPINION -- not data):**
   - The Tuio app and ChatGPT plugins target PERSONAL lines (auto, home) -- a business that AON essentially does NOT do. AON's revenue comes from commercial risk, reinsurance, health, and wealth advisory for LARGE corporations
   - Placing a $500M property/casualty program for a Fortune 500 company requires: (a) actuarial analysis, (b) relationships with 30+ carriers, (c) regulatory knowledge across jurisdictions, (d) claims advocacy, (e) contract negotiation. A chatbot cannot do this. Period.
   - Wolfe Research and BMO Capital explicitly defended insurance brokers: "The ChatGPT apps target personal lines... the major public brokers derive most of their revenue from commercial lines -- a far more complex business that requires human expertise"
   - **My Evidence:** AON's Q4 2025 organic growth was 5% DURING the period when AI fears were building. Clients did not leave. Revenue accelerated in Reinsurance (8% organic). The market reaction is sentiment, not fundamentals.

2. **NFP Integration is Actually Working:**
   - Producer retention HIGHER than pre-deal levels
   - $80M revenue synergies achieved in 2025 (on track for $175M by 2026)
   - $1.9B debt paid down in FY2025. Leverage reduced to 2.9x (target was 2.8-3.0x)
   - NFP Wealth divested to Madison Dearborn for $2.7B (smart capital recycling)
   - Deal expected to be EPS accretive from 2027
   - **My Evidence:** FCF grew 14% YoY to $3.2B despite integration costs. Adj. operating margin expanded 90bps to 32.4%. These are not the metrics of a botched acquisition.

### Value Trap Checklist
| Factor | SI/NO | Comentario |
|--------|-------|------------|
| Industria en declive secular | NO | Insurance broking TAM growing 9.4% CAGR globally |
| Disrupcion tecnologica inminente | NO | AI targets personal lines, not commercial broking |
| Management destruyendo valor | NO | NFP synergies ahead of schedule, smart divestitures |
| Balance deteriorandose | NO | $1.9B debt paid down in 2025, leverage on target |
| Insider selling masivo | NO | Net purchasers: 155.6K net shares purchased recently |
| Dividend cut reciente/probable | NO | Payout ratio 17%, dividend aristocrat 12+ years |
| Perdida market share >2pp 3yr | NO | Stable #2 position, NFP expanded middle-market access |
| ROIC < WACC ultimos 3 anos | NO | ROIC 16.7%, spread +8.6pp over WACC |
| FCF negativo >2 anos | NO | 4/4 years positive, $3.2B FY2025 |
| Goodwill >50% equity | WARN | Goodwill 31.1% of total assets (elevated post-NFP, but typical for broker M&A model) |

**TOTAL: 0/10 factors SI, 1 WARNING** -- Very low value trap risk.

### Mi Ventaja Informacional
- [x] Horizonte temporal mas largo (AI fear will fade as commercial clients don't leave)
- [x] Mercado sobre-reacciona (AI chatbot for home insurance =/= threat to commercial reinsurance placement)
- [x] Informacion publica mal interpretada (NFP margin compression is temporary, already recovering)

### Catalizadores
| Catalizador | Timeframe | Prob | Impacto |
|-------------|-----------|------|---------|
| FY2026 margin recovery (70-80bps guided) | 2026 Q1-Q4 | Alta (70%) | +10-15% re-rating |
| NFP EPS accretion inflection (2027) | Early 2027 | Media-Alta (65%) | +10% |
| AI disruption fear fades (commercial broking unaffected) | 3-6 months | Alta (75%) | +5-10% re-rating |
| Debt paydown continues, leverage <2.5x | 2026-2027 | Alta (80%) | Multiple expansion |
| Interest rate benefit on fiduciary float | 2026 | Alta (75%) | FCF boost |
| $7B available capital deployment (M&A + buybacks) | 2026-2027 | Alta (80%) | EPS growth acceleration |

### Kill Conditions
1. **Organic revenue growth turns negative for 2+ quarters** (signals client attrition or structural disruption)
2. **NFP synergies fail to materialize** ($175M target by 2026 missed by >40%)
3. **Leverage exceeds 4x ND/EBITDA** (balance sheet risk)
4. **AI demonstrably disrupts commercial insurance placement** (evidence of AI-driven client defection in Fortune 500 accounts)
5. **Adjusted operating margin declines YoY for 3+ quarters** (signals permanent margin compression, not temporary)
6. **FCF margin fails to recover above 20% by FY2027**

### Fit Macro
Insurance broking is mid-cycle resilient. Benefits from: (a) elevated interest rates (fiduciary float income), (b) hard-to-soft market transition (more advisory demand), (c) rising risk complexity (cyber, climate). Neutral-to-favorable in current macro environment.

---

## Valoracion

### DCF Sensitivity Assessment

**DCF tool output:**
- Base FV: $200.90 (MoS -38.1% -- OVERVALUED at current price)
- FV Spread: 101% | TV as % of EV: 74.5%

**ASSESSMENT: HIGH SENSITIVITY.** The DCF is unreliable as a point estimate due to TV >70% and FV spread >100%. This means small changes in growth/WACC assumptions swing FV dramatically. I will use the DCF as a RANGE, not a point.

### Reverse DCF Analysis

**Implied FCF growth at current price: 14.3%/yr for 5 years**
- Historical FCF CAGR: 2.1% (depressed by NFP integration)
- Revenue CAGR 3yr: 11.2% (inflated by NFP inorganic)
- Organic revenue growth: 6% consistently
- FCF margin expected to recover from 18.7% to 22-24%

**My Assessment:** The market is pricing in ~14% FCF growth. Is this achievable?
- Organic revenue growth: 5-7% (management guides mid-single-digit or higher)
- Margin expansion: 70-80bps/yr guided = ~2-3% FCF boost from margins
- Buybacks: ~3-4% share count reduction per year (historically consistent)
- Total EPS/FCF per share growth: 5-7% organic + 2-3% margins + 3-4% buybacks = 10-14%
- **Conclusion:** 14% is the OPTIMISTIC end of achievable. Not unreasonable but leaves NO margin of safety.

### Method 1: Owner Earnings Yield (Primary for Tier B broker, 50% weight)

```
FCF (FY2025): $3.22B
Depreciation: ~$800M (estimated)
Maintenance Capex: ~$880M (D&A x 1.1)
Owner Earnings = FCF - Maint Capex + Depreciation = $3.22B - $0.88B + $0.80B = $3.14B

Market Cap: $69.7B
Owner Earnings Yield = $3.14B / $69.7B = 4.5%

Expected Sustainable Growth: 6-8% (organic 6% + margin expansion)
OEY + Growth = 4.5% + 7% = 11.5% vs WACC 8.0% = spread +3.5pp

For context: MMC at $182.70 has similar OEY + Growth characteristics but at a slightly higher multiple.
```

**OEY-implied Fair Value:** Using a 5% OEY target (reasonable for Tier B quality broker):
FV = OE / Target OEY = $3.14B / 5% = $62.8B market cap / ~214M shares = **$293/share**

Using a 4% OEY target (premium for quality compounder characteristics):
FV = $3.14B / 4% = $78.5B / 214M = **$367/share**

**OEY Range: $293 - $367. Midpoint: $330.**

### Method 2: P/E vs Growth (Earnings Power Value, 30% weight)

Aon's normalized earning power:
- FY2025 adj. EPS: $17.07
- FY2026E EPS growth: ~10-12% (organic + margin + buyback)
- FY2026E adj. EPS: ~$18.80-$19.10
- Forward P/E at current price: $324 / $18.95 = 17.1x

Historical P/E range (5yr): 18-28x
Current sector P/E (brokers): 22-25x
Reasonable forward P/E for #2 broker with 6% organic growth + margin expansion: 20-22x

**P/E-implied Fair Value:**
- Conservative (20x FY2026E): 20 x $18.95 = **$379**
- Mid (21x): 21 x $18.95 = **$398**
- Generous (22x): 22 x $18.95 = **$417**

**P/E Range: $379 - $417. Midpoint: $398.**

### Method 3: EV/EBIT Normalized (20% weight)

- FY2025 EBIT (adj.): $17.2B x 32.4% = $5.57B
- Normalized EBIT (3yr avg margin 28.9% applied to current revenue): $17.2B x 28.9% = $4.97B
- Forward EBIT (FY2026E, 33.1% margin): $18.1B x 33.1% = $5.99B

Appropriate EV/EBIT multiple:
- Current EV/EBIT: 14.9x (per reverse DCF data)
- Sector median (brokers): 16-20x
- Quality premium for #2 global broker: 17-19x

**EV/EBIT-implied Fair Value:**
- Using forward EBIT $5.99B at 17x: EV = $101.8B - $13.5B net debt = $88.3B / 214M shares = **$413**
- Using normalized EBIT $4.97B at 18x: EV = $89.5B - $13.5B = $76.0B / 214M = **$355**

**EV/EBIT Range: $355 - $413. Midpoint: $384.**

### Reconciliation

| Metodo | Fair Value | Peso | Weighted |
|--------|-----------|------|----------|
| Owner Earnings Yield | $330 | 50% | $165 |
| P/E vs Growth | $398 | 30% | $119 |
| EV/EBIT Normalized | $384 | 20% | $77 |
| **Weighted Average** | | 100% | **$361** |

**Weighted Fair Value: $361**

Note: Higher weight on OEY because it's the most conservative and least dependent on multiple assumptions. The P/E and EV/EBIT methods converge around $380-400, which is consistent with analyst consensus mean target of $398.

**WARNING (Error #49):** My weighted FV ($361) is close to but below the consensus PT ($398). This is because my OEY method pulls the weighted average down. The P/E method alone gives $398 -- identical to consensus. I am NOT anchoring to consensus; the convergence reflects that Aon IS widely covered and the market is not wildly mispricing it. My edge is in the ENTRY PRICE, not in having a dramatically different FV.

**Sensitivity: FV Spread 101%, TV 74.5% of EV = HIGH SENSITIVITY.** Given this, the FV range is wide. Using the DCF range as a floor/ceiling check: DCF bull $277, DCF base $201. My methods give $330-398. The DCF uses a very mechanical WACC=9% with default growth that doesn't capture the NFP synergy trajectory. My OEY + P/E methods are more appropriate for an asset-light broker.

---

## Escenarios

| | Bear | Base | Bull |
|--|------|------|------|
| **Assumption** | AI disruption proves real for commercial broking; NFP synergies miss; organic growth slows to 3% | NFP integration succeeds; 6% organic growth continues; margins expand per guidance | NFP accelerates growth to 8%+; AI becomes tailwind (analytics); rate environment stays elevated |
| **FV** | $280 | $361 | $430 |
| **Prob** | 20% | 55% | 25% |

### Expected Value
EV = ($280 x 20%) + ($361 x 55%) + ($430 x 25%)
EV = $56 + $198.55 + $107.50 = **$362**

### MoS Analysis
- **Current price:** $324.30
- **MoS vs Base FV ($361):** 10.2%
- **MoS vs EV ($362):** 10.4%
- **MoS vs Bear ($280):** -15.8% (OVERVALUED vs bear case)

---

## MoS Assessment

| Metric | Value |
|--------|-------|
| vs Base | 10.2% |
| vs Bear | -15.8% |
| Required (Tier B, WIDE moat) | ~18-20% (per precedents: MMC 18.4%, ACGL 20%, VLTO 20%, ROP 22%) |
| Meets Required? | **NO -- at current price** |

**At current $324, the MoS is insufficient for Tier B.** The precedent floor for Tier B with WIDE moat is ~18-20% (MMC at 18.4% was the lowest accepted, and that was a HALF POSITION due to Greensill binary risk). AON at 10.2% does not meet this standard.

---

## Entry Price and Standing Order Recommendation

**Recommended Entry: $300** (MoS 16.9% vs Base FV $361)

Reasoning:
- $300 = 16.9% MoS vs FV $361. This is BELOW the typical Tier B floor (18-20%), but I would accept it because:
  - AON has WIDE moat (#2 global position, 95%+ client retention)
  - 0/10 value trap factors
  - Insiders are net buyers (155.6K net shares)
  - Short interest is minimal (1.0%)
  - FCF recovery trajectory is clear
  - At $300, forward P/E = ~15.8x (very attractive for quality broker)
- $300 is 7.5% below current price ($324). Given the stock is near 52wL ($304.59), there IS a reasonable chance it gets there (currently 6.4% above 52wL)

**Alternative: Aggressive entry at $310** (MoS 14.1%)
- Requires higher conviction. Would only consider if: (a) next earnings confirm 70-80bps margin expansion, (b) NFP synergies on track, (c) AI fears fully fade

**E[CAGR_3yr] at $300:**
- Capital appreciation: ($361/$300)^(1/3) - 1 = 6.4%
- Sustainable growth (organic + margin): ~7%
- Dividend yield: ~0.8%
- **E[CAGR_3yr] at $300 = ~14.2%**

**E[CAGR_3yr] at current $324:**
- Capital appreciation: ($361/$324)^(1/3) - 1 = 3.7%
- Sustainable growth: ~7%
- Dividend yield: ~0.7%
- **E[CAGR_3yr] at $324 = ~11.4%**

At current price, E[CAGR] of 11.4% is BELOW the 12% threshold for Tier B (per principles: "E[CAGR] > 15% and QS >= 55: compra justificada"). This confirms that the current price does NOT justify a buy.

At $300, E[CAGR] of 14.2% is close to but below 15%. This is borderline and would depend on whether we treat AON as a high-end Tier B (near-compounder quality) that could justify a lower threshold.

---

## Insider & Market Signals

**Insiders:** NET BUYERS. 155.6K shares purchased vs 8.8K sold (17.7:1 buy/sell ratio). This is a STRONG positive signal. Multiple C-suite members received stock awards in Feb 2026 and are holding.

**Institutions:** 88.9% institutional ownership. Top holders are passive (Vanguard 9.4%, BlackRock 7.6%). Capital World Investors at 5.7% is a notable active holder.

**Short Interest:** 1.0% of float, 1.8 days to cover. Minimal. No squeeze risk but also no bearish conviction from shorts.

**Analyst Consensus:** 13 Buy/Strong Buy vs 7 Hold vs 2 Sell. Mean target $398, range $326-$443. Goldman upgraded to BUY with $408 target.

---

## Comparison to MMC (Peer Check)

| Metric | AON | MMC |
|--------|-----|-----|
| Market Position | #2 | #1 |
| Market Cap | $69.7B | $89.8B |
| P/E (TTM) | 19.0x | 21.9x |
| Organic Growth | 6% | 4% |
| Adj. Op Margin | 32.4% | 28-29% est. |
| FCF | $3.2B | $3.5B est. |
| Leverage | 2.9x | ~2.5x |
| ROE | 39.5% | 27% |
| QS Adj. | 70 | 68 |
| Our FV | $361 | $220 (from thesis) |
| Entry Target | $300 | $155 |
| Current MoS | 10.2% | ~8.3% |

AON trades at a DISCOUNT to MMC despite: higher organic growth (6% vs 4%), higher margins (32.4% vs 28-29%), and higher ROE. The discount is justified by: higher leverage (2.9x vs 2.5x), integration risk (NFP), and smaller scale. Both are attractive at the right price. AON's entry would be at $300 vs MMC's at $155.

---

## Veredicto: WATCHLIST

**Rationale:**
1. Quality is genuine: QS 70 (Tier B upper), WIDE moat, 0/10 value trap, insiders buying
2. Business is misunderstood: AI fear is overblown for commercial broking
3. BUT: MoS at current $324 is only 10.2% -- insufficient for Tier B
4. E[CAGR] at current price is 11.4% -- below 15% threshold for Tier B
5. The stock could reach $300 (only 7.5% decline from current) given it's near 52wL

**Recommended Action:**
- Add to watchlist at **entry $300** (MoS 16.9%, E[CAGR] ~14.2%)
- Add to price monitors
- If R2 (devil's advocate) validates thesis, proceed to R3/R4 for standing order approval
- Monitor Q1 2026 earnings (April) for NFP synergy confirmation and margin expansion

---

## META-REFLECTION

### Incertidumbres/Dudas
- **EPS CAGR data gap:** quality_scorer.py returned 0/10 for EPS CAGR because the FY2025 EPS data point was NaN. This is likely a yfinance data issue for the most recent period. The actual FY2025 adj. EPS is $17.07, up 9% YoY. This gap artificially depresses the QS by ~5-8 points. I chose not to adjust for this because my +8 adjustment is already conservative and documented.

- **Dividend yield anomaly:** price_checker.py shows 92.0% yield for AON, which is clearly erroneous (actual yield is ~0.7%, payout ratio 17%). This is a yfinance data quality issue. I used the actual dividend data ($2.46/share annual) for my analysis.

- **DCF reliability:** The DCF tool gives FV of $201 (base), which is 44% below current price. This is because the default WACC=9% and mechanical growth assumptions don't capture the broker business model well. DCF is not the right primary method for an asset-light broker with high ROIC persistence. OEY + P/E are more appropriate.

- **NFP integration risk is the genuine uncertainty.** Management says it's going well, but $13.4B is a massive acquisition and integration typically takes 3-5 years. If synergies disappoint, margins won't recover as expected.

### Sugerencias para el Sistema
- **quality_scorer.py:** Should handle NaN EPS data points more gracefully -- perhaps interpolate from adj. EPS when available, or flag for manual review rather than scoring 0
- **price_checker.py yield data:** The 92% yield anomaly should trigger an automatic sanity check (yield >20% = likely data error)
- **Insurance broker template:** Consider creating a sub-template for insurance brokers within the insurance sector view, as the economics are fundamentally different from underwriters

### Preguntas para Orchestrator
1. Should AON be added to the insurance sector view as an "Analizadas" entry alongside ACGL and MMC?
2. Given we already have MMC at entry $155 in the pipeline, does it make sense to also track AON? They're correlated (both insurance brokers, similar macro drivers). Would owning both create excessive sector concentration?
3. The AI-disruption-of-brokers narrative may create a broader opportunity across all 4 major brokers. Should we do a comparative ranking (AON vs MMC vs AJG vs WTW)?

### Anomalias Detectadas
- **Dividend yield 92% in yfinance** -- clearly wrong. Actual payout ratio is 17%, annual dividend ~$2.46/share on $324 stock price = 0.76% yield
- **EPS CAGR showing NaN for FY2025** despite Aon reporting $17.07 adj. EPS. This is a data gap in yfinance
- **ROIC trajectory dip:** FY2024 ROIC dropped to 13.4% from 26.3% (FY2023), then recovered to 16.7% (FY2025). The FY2024 dip is entirely due to NFP acquisition inflating invested capital. This is temporary, not structural.
- **OCF/Net Income ratio dropped to 0.9x in FY2025** (from 1.3x in FY2023). This needs monitoring -- could indicate working capital absorption from NFP integration, or aggressive revenue recognition. At 0.9x it's still acceptable but the trend is negative.

---

## Sources

- [Aon Q4 2025 Earnings Call Transcript](https://www.fool.com/earnings/call-transcripts/2026/01/30/aon-aon-q4-2025-earnings-call-transcript/)
- [Aon Reports FY2025 Results -- Insurance Journal](https://www.insurancejournal.com/news/international/2026/01/30/856337.htm)
- [Aon Q4 2025 Earnings Beat -- Nasdaq](https://www.nasdaq.com/articles/aon-q4-earnings-top-estimates-new-business-growth-strong-retention)
- [Aon generates $3.2B cash, pays down $1.9B debt](https://www.stocktitan.net/news/AON/aon-reports-fourth-quarter-and-full-year-2025-js11wyu456oe.html)
- [Insurance Broker Stocks Sink as AI App Sparks Disruption Fears -- Bloomberg](https://www.bloomberg.com/news/articles/2026-02-09/insurance-broker-stocks-sink-as-ai-app-sparks-disruption-fears)
- [Insurance Broker Stocks Tumble -- Yahoo Finance](https://finance.yahoo.com/news/insurance-broker-stocks-tumble-openai-204925570.html)
- [Aon NFP Acquisition Strategic Analysis](https://www.ainvest.com/news/aon-nfp-acquisition-strategic-play-dominate-middle-market-risk-volatile-world-2506/)
- [Aon Sells NFP Wealth to Madison Dearborn](https://401kspecialistmag.com/aon-sells-back-nfp-wealth-side-to-madison-dearborn/)
- [Goldman Sachs Upgrades AON to Buy](https://www.investing.com/news/analyst-ratings/wells-fargo-lowers-aon-stock-price-target-to-443-on-guidance-review-93CH-4478287)
- [BMO Capital Defends Insurance Brokers](https://www.investing.com/news/analyst-ratings/bmo-capital-defends-insurance-broker-stocks-amid-aidriven-selloff-93CH-4497041)
- [Simply Wall St: AON Potentially Undervalued 38%](https://simplywall.st/stocks/us/insurance/nyse-aon/aon/news/how-investors-may-respond-to-aon-aon-q4-earnings-beat-and-ex)
