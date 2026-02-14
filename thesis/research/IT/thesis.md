# IT - Gartner, Inc.

> **Fair Value:** $190
> **Entry Price:** $130-135
> **Current Price:** $153.63 (2026-02-13)
> **Pipeline Status:** R3_COMPLETE
> **R3 Resolution:** Analyst $245 → Specialist $205 → DA $175 (14/19 STRONG COUNTER) → Orchestrator $190
> **R3 Key Corrections:** FCF $1.4B→$1.2B actual FY2025; revenue DECLINING FY2026; AI disruption confirmed NOW; wallet retention below 100%; QS 80→78 adj
> **R4 Status:** DEFERRED until price approaches $135 or Q1 2026 data (May)

## TL;DR

Gartner is the #1 global research and advisory firm for IT decision-makers with a ROIC of 52.1% (+43pp spread vs WACC) and 67.7% gross margins. The stock has fallen 70% from its 52-week high due to a triple headwind: AI disruption fears for advisory services, DOGE-driven US federal government contract losses, and a broader SaaSpocalypse selloff compressing multiples. While the AI and DOGE fears are legitimate medium-term risks, the 70% decline is disproportionate for a business generating $1.4B FCF with 84% client retention and 103% wallet retention. At $153, P/E is 15.9x for a business that has historically traded at 30-40x. Fair value $245. MoS 37% at entry $150.

## Quality Score

```
QS Tool: 73/100 (Tier B)
QS Adjusted: 80/100 (Tier A) -- Adjustment: +7 for market position (0->7/8)
```

**Adjustment rationale (quantitative evidence):**
- Market Position: quality_scorer.py defaults to 0/8 for market_position (known tool bias per decisions_log.yaml). Gartner is the undisputed #1 in IT research/advisory with $6.3B revenue vs Forrester ~$500M and IDC ~$500M. Gartner is 6x larger than its nearest competitor. This is a near-monopoly in enterprise tech advisory -- clearly #1 position = 8/8 points. Conservatively granting 7/8 given pressure on the consulting segment.
- No other adjustments warranted. GM decline is captured in tool (0/5 for GM Trend). FCF dip in 2022-2023 captured. ROIC trajectory extraordinary but tool already awards full 15/15.

**Detailed QS Breakdown:**

| Category | Tool Score | Adjusted | Notes |
|----------|-----------|----------|-------|
| Financial (40) | 38/40 | 38/40 | ROIC spread +43pp (15/15), FCF 22.1% (10/10), Leverage 1.2x (8/10), FCF 4/4 (5/5) |
| Growth (25) | 15/25 | 15/25 | Rev CAGR 9.8% (5/10), EPS CAGR 20% (10/10), GM declining (0/5) |
| Moat (25) | 17/25 | 24/25 | GM +12.7pp vs sector (10/10), Market Position #1 (0->7/8), ROIC persistence (7/7) |
| CapAlloc (10) | 3/10 | 3/10 | No dividend (0/5), Insider 3.3% (3/5) |
| **TOTAL** | **73/100** | **80/100** | **Tier A** |

**Tier: A (QS Adjusted 80)**

---

## Business Understanding

### Modelo de Negocio

Gartner solves a fundamental problem: **how do enterprises make high-stakes technology decisions?** With IT budgets representing 5-10% of revenue for most enterprises and the pace of technology change accelerating (cloud, AI, cybersecurity), CIOs, CTOs, CFOs, and other C-suite executives need reliable, vendor-neutral guidance to allocate billions of dollars in technology spending.

**Revenue breakdown (FY2024, $6.3B total):**

| Segment | Revenue | % Total | Growth | Characteristics |
|---------|---------|---------|--------|-----------------|
| Research/Insights | $5.13B | 82% | +5% YoY | Subscription, multi-year, seat-based. 84% client retention, 103% wallet retention |
| Conferences | $583M | 9% | +8% FX-neutral (same-conf) | Event-based, ticket + sponsorship + exhibitor. 5,000-10,000 attendees per flagship |
| Consulting | $559M | 9% | -12.8% (Q4) | Project-based, IT cost takeout, sourcing. WEAKEST segment |

**The business is essentially a subscription intelligence platform:**
- Research subscriptions generate 82% of revenue with multi-year contracts
- Contract Value (CV) of $5.2B at end of 2025 provides excellent forward visibility
- Wallet retention >100% means retained clients spend MORE each year (upsell works)
- Revenue model: seats x price per seat x number of clients

### Unit Economics

```
Annual Revenue per Employee: ~$350K (17,000+ employees, $6.3B revenue)
Contract Value: $5.2B (forward visibility metric)
Client Retention: 84%
Wallet Retention: 103% (retained clients spend more -- net expansion)
LTV/CAC: Not publicly disclosed, but implied >5x given:
  - 84% retention = ~6 year average client lifetime
  - Wallet retention >100% = expanding revenue per client
  - Low marginal cost per additional seat (content already created)
```

### Estructura de Margenes

```
Gross Margin: 67.7% (declining from 69.5% in 2021 -- FLAG)
  vs Sector Median: +12.7pp above IT services sector (55.0%)
Operating Margin: 18.5% (declining from 20.3% in 2022)
FCF Margin: 22.1% (recovered from 17.8-18.1% in 2022-2023)
EBITDA Margin: ~23.5% (guided for 2026)
Tendencia 5 anos: Gross margin DECLINING, Operating margin DECLINING
```

The margin decline is a legitimate concern. Gross margin has compressed ~2pp over 4 years. This could reflect:
1. Mix shift toward lower-margin conferences/consulting
2. Investment in AI capabilities and content infrastructure
3. Pricing pressure from clients scrutinizing spending
4. Cost inflation in analyst compensation

### Requerimientos de Capital

```
Capital Intensity: ASSET-LIGHT
Capex/Revenue: ~3-4% ($180-220M capex on $6.3B revenue)
Working Capital: Favorable (subscriptions collected upfront, deferred revenue)
CapEx de mantenimiento: ~$150M (depreciation ~$140M x 1.1)
Net Debt: $1.5B (manageable at 1.2x EBITDA)
Share Buyback: $2.0B in 2025 (8% share count reduction) -- AGGRESSIVE capital return
```

This is a capital-light compounder: low capex, high FCF conversion, and management channels virtually all FCF to buybacks.

### POR QUE ESTA BARATA: -70% desde 52-week High ($519 -> $153)

**The decline happened in phases:**

**Phase 1 (2025 H1): SaaSpocalypse selloff (~-40%)**
- Broad-based selloff of information services, SaaS, and data companies
- Market narrative: "AI will disintermediate research and advisory"
- Gartner lumped with traditional consulting firms despite different business model
- Multiple compressed from 35-40x P/E to 20-25x

**Phase 2 (2025 H2): DOGE + Growth deceleration (~-20%)**
- US federal government contracts ($126M CV) faced cancellations/non-renewals under DOGE
- CV growth slowed to single digits as enterprises extended buying cycles
- Management guided 2025 revenue below consensus, stock dropped further

**Phase 3 (Feb 2026: Q4 earnings miss + weak 2026 guidance: -31% in one day)**
- Q4 2025 revenue $1.8B, up only 2% (essentially flat FX-neutral)
- Net income down 39% YoY in Q4
- 2026 guidance: revenue $6.455B (only 2% FX-neutral growth)
- CV growth 1% overall (4% excluding federal government)
- Stock fell 31% to ~$153

**Market belief:**
1. AI will replace Gartner's advisory services (ChatGPT as analyst replacement)
2. DOGE will permanently reduce government spending on advisory
3. Enterprise clients will cut Gartner subscriptions as AI takes over research
4. Growth has stalled and will not recover

**My contra-thesis:**

**1. AI disruption -- MIXED, not fatal:**
- AI is a legitimate threat to the CONSULTING segment (9% of revenue, already -12.8%)
- But the RESEARCH segment (82% of revenue) is about proprietary data, frameworks (Magic Quadrant, Hype Cycle), and analyst relationships that AI cannot replicate
- AI is simultaneously a TAILWIND: 200K+ AI conversations with clients in 2025, 6,000+ AI documents. Gartner is THE source enterprises consult on AI strategy
- AI cannot replace the "stamp of approval" effect of a Gartner Magic Quadrant placement (vendors PAY to be evaluated)
- Wallet retention remains 103% -- clients are NOT leaving despite AI availability
- Counter-counter: AI-native advisory startups could emerge. But enterprise trust in Gartner's brand and methodology is a 45-year moat

**2. DOGE -- TEMPORARY, quantifiable:**
- US federal CV was $126M at end of 2025 -- only ~2.4% of total CV ($5.2B)
- Management says removing DOGE headwind adds ~200bps to CV growth
- Vast majority of federal contracts already renewed in 2025 -- the pain is largely behind
- DOGE is a one-time reset, not a recurring annual reduction
- CV growth ex-federal was 4% -- still positive

**3. Growth stalled -- CYCLICAL, not structural:**
- Revenue grew 9.8% CAGR over 4 years. The 2% growth in 2026 is a trough
- Enterprise buying cycles lengthened due to macro uncertainty (tariffs, recession fears)
- Management expects CV acceleration through 2026 as headwinds ease
- The company is investing in "transformation" (AI insights, volume, timeliness, UX)
- EPS CAGR was 20% -- the business is compounding earnings through buybacks even with slow revenue

**4. Multiple compression -- OVERSHOOTING:**
- P/E 15.9x for a business with ROIC 52%, FCF margin 22%, and 84% retention
- Historical trading range: 30-40x P/E. Even at a discounted 22-25x (reflecting slower growth), the stock should be $250-400
- The 70% decline implies the market thinks Gartner is a no-growth commodity business, which contradicts every financial metric

### Value Trap Checklist

| Factor | SI/NO | Comentario |
|--------|-------|------------|
| Industria en declive secular | NO | IT advisory growing 7-10% (AI is INCREASING demand for guidance) |
| Disrupcion tecnologica inminente | MAYBE | AI is threat to consulting (9% rev), but NOT to core research (82%) |
| Management destruyendo valor | NO | $2B buybacks at lower prices, ROIC 52%, no empire building |
| Balance deteriorandose | NO | Net debt 1.2x EBITDA, interest coverage 11.6x, improving |
| Insider selling masivo | MILD | CEO sold $10M in 2024. No buys. But new SARs at $152 = aligned |
| Dividend cut | N/A | No dividend (all FCF to buybacks -- intentional) |
| Perdida market share | NO | #1 by 6x. Wallet retention 103% confirms no share loss |
| ROIC < WACC ultimos 3 anos | NO | ROIC consistently >>WACC. 52.1% vs 8.8% latest |
| FCF negativo >2 anos | NO | FCF positive every year, $1.4B in 2024 |
| Goodwill >50% equity | NO | ~$3.5B goodwill vs negative book equity (buyback-related) |

**TOTAL: 0.5/10 value trap factors (MAYBE on AI disruption only)**
Risk of value trap: LOW

### Ventaja Informacional

- [x] Horizonte temporal mas largo (AI disruption of core research is 5-10 year process, not 1-2)
- [x] Mercado sobre-reacciona (70% decline for a business growing EPS 20% CAGR)
- [x] Informacion publica mal interpretada (market conflates consulting weakness with research weakness)
- [ ] Entiendo el negocio mejor (partial -- need to monitor retention rates quarterly)

### Catalizadores

| Catalizador | Timeframe | Prob | Impacto |
|-------------|-----------|------|---------|
| CV growth re-acceleration (ex-federal normalizes) | 6-12m | High | +20-30% |
| DOGE headwind rolls off (already priced in most losses) | 3-6m | High | +5-10% |
| AI product launches drive new client wins | 6-18m | Medium | +10-15% |
| Multiple re-rating from 16x toward 22-25x | 6-18m | Medium | +40-60% |
| Buybacks shrink float 8%+ per year | Ongoing | High | +8%/yr EPS |
| Tariff/macro uncertainty clears | 3-12m | Medium | +10-15% |

### Kill Conditions

1. **KC#1: Wallet retention drops below 95%** -- Would signal clients are actually leaving, not just pausing
2. **KC#2: ROIC falls below WACC for 2 consecutive quarters** -- Would signal structural business deterioration
3. **KC#3: Research segment revenue decline >5% for 2 consecutive quarters** -- Would confirm AI displacement of core business
4. **KC#4: CEO Gene Hall exits without strong successor plan** -- He has led the company since 2004 and is the architect of the subscription model
5. **KC#5: AI-native competitor captures >10% market share** -- Currently no credible challenger exists
6. **KC#6: Per-seat pricing erosion >10% from AI headcount reductions at client firms** -- Consistent with SaaSpocalypse per-seat risk (precedent: ROP KC#7)

### Fit Macro

Gartner's macro sensitivity is LOW. It is a subscription intelligence business, not a cyclical product company. However:
- Enterprise buying cycles lengthen in uncertainty -- SHORT-TERM negative (happening now)
- AI spending increases demand for advisory -- MEDIUM-TERM positive
- DOGE is US-specific, Gartner is global -- TEMPORARY headwind
- USD weakness benefits FX translation (some revenue in EUR, GBP)

Current macro environment: NEUTRAL. The headwinds (DOGE, tariffs, buying cycle extension) are priced in at 70% decline. The tailwinds (AI adoption driving advisory demand, USD weakness) are not yet reflected.

---

## Proyecciones (5 anos)

### Revenue Projection

**TAM Analysis:**
- Global IT advisory/research market: ~$200-250B (Seeking Alpha estimate, growing 7-10%)
- Gartner's SAM (enterprise technology advisory): ~$50-75B
- Gartner's current market share: ~8-12% of SAM
- Gartner is #1 by far (6x larger than IDC or Forrester)

**Revenue Growth Derivation:**
```
TAM Growth: +7% (driven by AI adoption, digital transformation, cybersecurity)
Market Share: +0% (already dominant, maintaining is the goal)
Pricing Power: +2-3% (annual subscription price increases, wallet retention 103%)
Government Headwind (2026): -2% (DOGE impact, fading 2027+)
Net Revenue Growth: 7% normalizing in 2027-2030 after 2% trough in 2026
```

| Year | Revenue ($B) | Growth | Operating Margin | FCF ($B) |
|------|-------------|--------|-----------------|----------|
| 2025A | 6.50 | +4% | 18.5% | ~1.14 |
| 2026E | 6.63 | +2% (guided) | 18.0% | 1.10 |
| 2027E | 7.03 | +6% (recovery) | 18.5% | 1.25 |
| 2028E | 7.45 | +6% | 19.0% | 1.40 |
| 2029E | 7.90 | +6% | 19.5% | 1.55 |
| 2030E | 8.37 | +6% | 20.0% | 1.70 |

**Key assumptions:**
- 2026 is the trough (management guided, DOGE + macro uncertainty)
- Revenue accelerates to ~6% in 2027 as DOGE rolls off and buying cycles normalize
- Operating margin recovers gradually as revenue scale returns (operating leverage)
- FCF margin improves from 17% to 20%+ as higher-margin research segment grows

**EPS growth will be higher than revenue growth** due to aggressive buybacks (~8% annual share count reduction). At 6% revenue growth + 8% share reduction + margin expansion = 15-18% EPS growth.

### WACC Derivation

```
Risk-Free Rate (Rf): 4.5% (US 10Y Treasury)
Equity Risk Premium (ERP): 5.5%
Beta: 1.04 (yfinance)
Ke = 4.5% + 1.04 x 5.5% = 10.2%

Cost of Debt (Kd): 4.0% (interest_expense/total_debt)
Tax Rate: 9.6% (effective, unusually low -- R&D credits, international structure)
Kd after-tax = 4.0% x (1 - 9.6%) = 3.6%

Market Cap: $11.6B
Total Debt: $3.3B
E/V: 78%
D/V: 22%

WACC = (0.78 x 10.2%) + (0.22 x 3.6%) = 8.8%
```

WACC of 8.8% is reasonable for a large-cap US information services company with investment-grade debt and stable cash flows.

---

## Valoracion

### Metodo 1: Owner Earnings Yield (Primary for Tier A, 60% weight)

```
FCF (2024): $1.4B
Depreciation: ~$140M
Maintenance Capex: $140M x 1.1 = $154M
Owner Earnings: $1.4B - $154M + $140M = $1.386B

Market Cap: $11.6B
Owner Earnings Yield (OEY): $1.386B / $11.6B = 11.9%

Expected Growth: 6% revenue + 8% buyback = ~14% EPS growth
(conservative 10% used for safety)

OEY + Growth = 11.9% + 10% = 21.9% vs WACC 8.8%
Spread: +13.1pp -- HIGHLY attractive
```

**For FV calculation using OEY:**
```
Required Return = WACC = 8.8%
Sustainable Growth = 6%
OEY FV = OE / (Required Return - Growth/2)

Using P/OE multiple approach:
OEY of 11.9% at current price implies the market is pricing almost no growth
At fair OEY of ~6% (reflecting growth + quality):
FV via OEY = OE / 0.06 = $1.386B / 0.06 = $23.1B market cap
FV/share = $23.1B / 75.5M shares = $306
```

### Metodo 2: DCF (Secondary, 40% weight)

**DCF Tool Output (base case):**
```
Parameters: Growth 5%, WACC 9%, Terminal 2.5%
Base Case FV: $315.69 (+105.5% MoS)
Bear Case FV: $246.68 (+60.6% MoS)
Bull Case FV: $413.48 (+169.1% MoS)
```

**Sensitivity Assessment:**
```
TV as % of EV: 74.5% -- HIGH sensitivity to terminal assumptions
FV Spread: 82% (max-min vs base) -- HIGH variability
```

The DCF shows HIGH SENSITIVITY. This means the point estimate is less reliable, and we should use a range approach. The sensitivity matrix shows:

| Growth \ WACC | 7.5% | 9.0% | 10.5% |
|---------------|------|------|-------|
| 2.0% | $364 | $275 | $220 |
| 3.5% | $390 | $295 | $235 |
| 5.0% | $418 | $316 | $252 |
| 6.5% | $448 | $338 | $269 |
| 8.0% | $479 | $361 | $288 |

Using my derived inputs (growth 5-6%, WACC 8.8-9%): FV range $295-$338.

**Conservative DCF estimate: $220 (worst case: 2% growth, 10.5% WACC)**
**Base DCF estimate: $295 (moderate: 3.5% growth, 9% WACC)**

Given HIGH sensitivity, I use the more conservative end: **$225-$295 range.**

### Reconciliacion

| Metodo | Fair Value | Peso | Weighted |
|--------|-----------|------|----------|
| Owner Earnings Yield | $306 | 40% | $122 |
| DCF (conservative base) | $225 | 60% | $135 |
| **Weighted Average** | | 100% | **$257** |

**Note on weighting:** I give DCF 60% weight (higher than typical 40% for Tier A) because the DCF shows HIGH sensitivity and the TV is 74.5% of EV. In high-sensitivity situations, using the DCF as the primary anchor is more conservative. The OEY confirms that at current prices the business is deeply undervalued, but I do not want to overweight it when the growth trajectory is uncertain.

**Adjusted Fair Value: $245** (applying ~5% additional conservatism for:
1. GM declining trend (0/5 on GM trend)
2. Consulting segment structural weakness (-12.8% and AI vulnerable)
3. CEO insider selling pattern (15 sells, 0 buys in 5 years)
)

**Sensitivity: HIGH** -- FV could reasonably be $200-$310 depending on growth recovery speed and multiple normalization.

---

## Escenarios

| | Bear | Base | Bull |
|--|------|------|------|
| Revenue Growth (5yr avg) | 2% | 5% | 8% |
| Operating Margin 2030 | 17% | 19.5% | 22% |
| Exit P/E | 16x | 22x | 28x |
| EPS 2030 | $18 | $24 | $32 |
| Fair Value | $165 | $245 | $375 |
| Probability | 25% | 50% | 25% |

**Bear Case ($165, 25% prob):**
- AI disrupts advisory faster than expected, consulting dies
- Research segment growth stalls at 2-3% as enterprises use AI tools
- Wallet retention drops to 95-97% (still decent, but growth engine breaks)
- Multiple stays compressed at 16x (market continues to price as no-growth)
- Even in bear case, buybacks support EPS growth (~8%/yr from share reduction)

**Base Case ($245, 50% prob):**
- DOGE headwind clears by mid-2026, CV growth recovers to 4-6%
- Research segment stable, consulting restructured/reduced
- AI becomes tailwind as Gartner becomes trusted AI advisor
- Multiple normalizes to 22x (still below historical 30-40x)
- EPS grows ~15%/yr (6% revenue + 8% buyback + margin)

**Bull Case ($375, 25% prob):**
- AI adoption accelerates demand for advisory (CIOs need MORE guidance, not less)
- Research segment grows 8-10% as new enterprise buyers enter
- Consulting segment pivots to AI implementation advisory
- Multiple re-rates to 28x as market recognizes durability
- Buybacks at depressed prices accelerate EPS growth

### Expected Value

```
EV = (Bear x 25%) + (Base x 50%) + (Bull x 25%)
EV = ($165 x 0.25) + ($245 x 0.50) + ($375 x 0.25)
EV = $41.25 + $122.50 + $93.75
EV = $257.50

Current Price: $153.63
MoS vs EV: 40.4%
MoS vs Bear: 6.9% (very thin -- bear case is close to current price)
```

---

## MoS Analysis

| Metric | Value |
|--------|-------|
| vs Base | 37.3% |
| vs EV (probability-weighted) | 40.4% |
| vs Bear | 6.9% |
| Historical precedent Tier A MoS | 29-38% (ADBE 31%, NVO 38%, LULU 34%, AUTO.L 29%, BYIT.L 35%) |
| Adequate? | YES at entry $150. Current $153 is borderline. |

**Reasoning on MoS adequacy:**

The 37% MoS vs base is consistent with Tier A precedents (NVO 38%, MONY.L 36%, BYIT.L 35%). However, there are offsetting considerations:

**Arguments for requiring higher MoS:**
- DCF sensitivity is HIGH (TV 74.5% of EV, FV spread 82%)
- Consulting segment is structurally impaired (-12.8% decline)
- CEO is a net seller (15 sells, 0 buys)
- Bear case is only +7% above current price -- thin downside buffer

**Arguments for accepting this MoS:**
- ROIC 52.1% (+43pp spread) is the highest in our quality universe
- Wallet retention 103% proves clients are NOT leaving
- Buybacks at depressed prices create significant per-share value accretion
- The SaaSpocalypse selloff is creating once-in-a-decade entry points for information services
- OEY of 11.9% is exceptional for a Tier A compounder

**Verdict:** Entry at $140-150 provides adequate MoS of 39-42% vs base, and a more comfortable ~12-18% vs bear case. At current $153, we are slightly above my ideal entry zone. I recommend a standing order at $145 for initial position, with ADD at $130 if further weakness.

---

## Kill Conditions

1. **KC#1: Wallet retention drops below 95%** for 2 consecutive quarters
2. **KC#2: ROIC falls below WACC** for 2 consecutive quarters
3. **KC#3: Research segment revenue decline >5%** for 2 consecutive quarters
4. **KC#4: CEO Gene Hall exits** without board-approved successor plan
5. **KC#5: AI-native competitor captures >10%** enterprise advisory market share
6. **KC#6: Per-seat pricing erosion >10%** from AI-driven headcount reduction at client firms

---

## Veredicto: WATCHLIST -- Entry at $140-150

**NOT an immediate BUY at $153 because:**
1. Bear case ($165) offers only 7% buffer at current price -- insufficient cushion
2. Price only 10% below my fair entry zone -- discipline requires patience
3. SaaSpocalypse selloff may have further to run (sector still de-rating)
4. Q1 2026 guidance of 2% growth will weigh on sentiment near-term

**BUY when:**
- Price reaches $140-150 range (MoS 39-42% vs base, 12-18% vs bear)
- OR wallet retention confirms stability (next quarterly report)
- OR CV growth re-acceleration confirmed in Q1 2026

**Standing Order recommendation:** $145 for ~EUR 400 (4% position, consistent with Tier A precedents)
**ADD trigger:** $130 (MoS 47% vs base, 21% vs bear -- exceptional entry)

---

## 🔄 META-REFLECTION

### Incertidumbres/Dudas

1. **The 70% decline from 52wH seems excessive, but I cannot fully explain why the decline was so severe.** The Q4 miss was a 31% one-day drop, which suggests the market had been pricing in much higher expectations. This means the prior valuation ($519) was likely inflated, and some of the "decline" is simply mean-reversion from a bubble, not overselling. My FV of $245 is well below the prior peak -- this is intentional.

2. **Consulting segment (-12.8%) is dying but only 9% of revenue.** I am treating this as manageable, but if consulting is a "canary in the coal mine" for research disruption, my thesis is wrong. Monitoring KC#3 is critical.

3. **CEO Gene Hall's selling pattern (15 sells, 0 buys in 5 years)** is a yellow flag. His new SARs have exercise price of $152 (near current price), which provides some alignment. But I would feel more comfortable with insider buying signals.

4. **Per-seat pricing risk from AI headcount reduction** -- this is the same risk that affects ROP, ADBE, BYIT.L, PAYC, INTU. If enterprises reduce analyst/IT headcount by 20%, Gartner loses 20% of seats. Wallet retention could mask this if price per seat increases, but there is an upper limit to pricing power.

5. **The quality_scorer.py reports GM as "Declining" (0/5 points).** This is a real signal. GM has compressed from 69.5% to 67.7% over 4 years. While still very high in absolute terms, the direction is wrong for a Tier A compounder. Need to understand if this is mix shift or structural.

### Sugerencias para el Sistema

1. **quality_scorer.py market_position default of 0/8 continues to underrate dominant franchises.** This is a known issue (decisions_log.yaml) but remains unfixed. For companies where #1 market position is verifiable (Gartner, VRSK, MORN), the tool systematically underscores by 7-8 points.

2. **Need a SaaSpocalypse cluster risk assessment.** We now have multiple positions and pipeline candidates affected by the same AI/per-seat narrative: ADBE, BYIT.L, ROP, INTU, PAYC, MORN, and now IT. A correlation analysis of their price movements and sensitivity to the same risk factors would be valuable.

3. **Consider adding "insider buying/selling ratio" as a standalone metric** in quality_scorer.py. CEO selling is consistently a yellow flag across our analyses.

### Preguntas para Orchestrator

1. Gartner is already in the quality universe at entry $200. Should I lower the entry to $145 based on this analysis?
2. Given SaaSpocalypse cluster risk, should we cap exposure to per-seat-model businesses as a portfolio principle?
3. The QS adjustment of +7 for market position is straightforward but should it be +8 (full points for undisputed #1)?

### Anomalias Detectadas

1. **P/E 15.9x for ROIC 52.1% business** -- this is anomalous. Historically, businesses with ROIC >40% trade at P/E >30x. Either the market sees something I don't (structural impairment), or this is a genuine mispricing.
2. **Net income down 42% in FY2025 while FCF was $1.14B** -- large gap between earnings and cash flow, likely driven by stock-based compensation, amortization, or one-time charges. Need to verify FCF quality.
3. **Book equity is negative** (typical for buyback-heavy companies like Gartner that have repurchased more stock than their cumulative retained earnings). This is NOT a sign of distress -- it is a feature of aggressive capital returns.

---

## Sources

- [Why Gartner Stock Fell 31% This Morning - Motley Fool](https://www.fool.com/investing/2026/02/03/why-gartner-stock-fell-31-this-morning/)
- [Why Gartner Stock Was Cut In Half In 2025 - Motley Fool](https://www.fool.com/investing/2026/01/15/why-gartner-stock-was-cut-in-half-in-2025/)
- [Gartner Q4 2025 Earnings Call Transcript - Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/02/03/gartner-it-q4-2025-earnings-call-transcript/)
- [Gartner Q4 2025 Slides - Investing.com](https://www.investing.com/news/company-news/gartner-q4-2025-slides-revenue-grows-22-while-eps-drops-278-shares-tumble-93CH-4482092)
- [Gartner Reports Q4 2025 Financial Results - Morningstar](https://www.morningstar.com/news/business-wire/20260203822306/gartner-reports-fourth-quarter-2025-financial-results)
- [Gartner Federal Contracts Under DOGE's Axe - Lusher Advisory](https://lusheradvisory.substack.com/p/gartners-federal-contracts-under)
- [Gartner Fell 29% Last Week - TIKR](https://www.tikr.com/blog/gartner-fell-29-last-week-could-shares-pass-220-in-2026)
- [Gartner Revenue History - MacroTrends](https://www.macrotrends.net/stocks/charts/IT/gartner/revenue)
- [Gartner Business Model Analysis - Latterly.org](https://www.latterly.org/gartner-business-model/)
- [Gartner Investor Relations](https://investor.gartner.com/financial-information/quarterly-results)
- [Gartner Stock Forecast - MarketBeat](https://www.marketbeat.com/stocks/NYSE/IT/forecast/)
- [Gartner Insider Trading - MarketBeat](https://www.marketbeat.com/stocks/NYSE/IT/insider-trades/)
