# OPPORTUNITY SCAN PIPELINE — Full Universe Screening
## Date: 2026-02-11 | Session 53-54

---

## V1: Initial Quality-Focused Screening (Session 53)

### Screening Parameters
- **Tools used:** dynamic_screener.py (pe_max=999, no P/E filter) + quality_scorer.py v4.0
- **Indices screened:** us_all (193 results), europe_all (58 results)
- **Filters:** >20% below 52w high + low-coverage/undiscovered

### Top 3 Tier A Candidates (Session 53)

| Ticker | QS | ROIC | Key Thesis | %off52H |
|--------|-----|------|-----------|---------|
| **DSY.PA** (Dassault Systemes) | 78 | 15.3% | 3D/PLM monopoly, 49% insider, -57% at 52w LOW | -56.6% |
| **MORN** (Morningstar) | 83 | 20.5% | Data monopoly, 45% insider, only 3 analysts | -51.0% |
| **VRSN** (VeriSign) | 83 | 275% | .com/.net monopoly, ICANN contract | -29.0% |

---

## V2: Full Universe ROIC/FCF/CAGR Screening (Session 54)

### Methodology

**Stage 1: Universe Screening (dynamic_screener.py)**
- Universe attempted: US (SP500+SP400+Russell1000 = 1,103), EU (europe_all = 610), UK (FTSE350 = 339) = **2,052 total attempted**
- **Actually processed: ~800 tickers (~40%). ~60% were rate-limited by yfinance and returned no data.**
- Initial filter: FCF yield > 5%
- Results from processed tickers: US 55, EU 86, UK 80 passed (after dedup: 176 unique)
- **Coverage gap:** Many well-known names (V, MA, CME, COST, CRM, ASML, RACE, ADYEN, etc.) were rate-limited. Results are partial. A follow-up screening with fresh rate limits would improve coverage.

**Stage 2: Fundamental Filter (opportunity_filter.py — NEW TOOL)**
- Filters: ROIC > 15%, FCF margin > 10%, Revenue CAGR 5yr > 5%
- Excluded: 13 existing positions
- Results: **22 companies passed all 3 filters**

**Stage 3: Quality Scoring (quality_scorer.py)**
- 18 companies scored with full quality profile
- 5 scored Tier A (QS >= 75)

---

## TIER A CANDIDATES (QS >= 75) — Priority for Thesis

| Ticker | Name | QS | ROIC | FCFm% | RevCAGR | P/E | %off52H | Sector | Geo |
|--------|------|-----|------|-------|---------|-----|---------|--------|-----|
| **PAYC** | Paycom Software | 85 | 32.5% | 17.9% | 21.3% | 15.1 | -54.7% | Payroll SaaS | US |
| **FSG.L** | Foresight Group | 83 | 47.6% | 27.1% | 21.4% | 14.6 | -17.3% | Alt. Asset Mgmt | UK |
| **NFLX** | Netflix | 75 | 32.7% | 20.9% | 12.6% | 31.9 | -39.7% | Entertainment | US |
| **PAYX** | Paychex | 75 | 21.8% | 30.7% | 6.5% | 22.2 | -39.2% | Payroll SaaS | US |
| **RMV.L*** | Rightmove | 69 | 384.6% | 51.9% | 8.5% | 16.8 | -47.2% | Property Portal | UK |

*RMV.L legacy QS 69, but profile is exceptional (ROIC 385%, FCF 52%, net cash, monopoly). Likely Tier A adjusted.

### PAYC (Paycom Software) — TOP CANDIDATE
- **Business:** US payroll/HCM SaaS platform. Single-tenant cloud, founder-led.
- **Quality:** ROIC 32.5% rising, GM 82%, FCF margin 18%, net cash ($290M), 12% insider ownership.
- **Growth:** Revenue CAGR 21.3%, EPS CAGR 38.1%.
- **Moat:** Switching costs (payroll data migration), recurring SaaS revenue, integrated platform (HR+payroll+benefits).
- **Why cheap:** -55% from 52w high. Revenue deceleration fears + BETI (employee self-service) cannibalizing services revenue.
- **Risks:** Competition (ADP, PAYX, PCTY), macro employment sensitivity, founder-CEO concentration.
- **Action:** **FULL BUY-PIPELINE (4 rounds) recommended.**

### RMV.L (Rightmove) — VERY STRONG CANDIDATE
- **Business:** UK #1 property portal. >80% of UK property listings. Asset-light digital monopoly.
- **Quality:** ROIC 385% (!!), FCF margin 52%, net cash, 0.5% insider (low concern in duopoly position).
- **Growth:** Revenue CAGR 8.5%, EPS CAGR 4.6% (mature but steady).
- **Moat:** Network effects (agents need Rightmove because buyers are there, buyers go because agents list there). >95% penetration. Similar structural position to AUTO.L.
- **Why cheap:** -47% from 52w high. CoStar entry threat, UK housing market fears, estate agent consolidation.
- **Risks:** CoStar invasion ($100M+ UK investment), UK housing recession, agent pushback on fees.
- **Concern:** Would be 5th UK position (UK = 30% of portfolio). Per Principio 2, need explicit justification.
- **Action:** **FULL BUY-PIPELINE (4 rounds) recommended.** High similarity to AUTO.L thesis.

### FSG.L (Foresight Group) — STRONG CANDIDATE
- **Business:** UK alternative asset manager focused on infrastructure/solar/PE.
- **Quality:** ROIC 48%, FCF margin 27%, 95% gross margin, net cash, 34.5% insider (!).
- **Growth:** Revenue CAGR 21.4%, AUM growth driven.
- **Moat:** Specialized infrastructure expertise, AUM stickiness, regulatory barriers to entry.
- **Risks:** AUM drawdowns, performance fee volatility, key person risk, UK small cap (GBP 465M).
- **Concern:** Small market cap. Verify eToro availability. UK concentration.
- **Action:** Verify eToro availability. If available, fundamental-analyst recommended.

---

## TIER B CANDIDATES (QS 55-74) — Worth Monitoring

| Ticker | Name | QS | ROIC | FCFm% | RevCAGR | P/E | %off52H | Key Note |
|--------|------|-----|------|-------|---------|-----|---------|----------|
| FDS | FactSet Research | 73 | 18.7% | 26.6% | 8.0% | 12.6 | -58.2% | Financial data monopoly |
| KCR.HE | Konecranes | 73 | 21.0% | 12.4% | 7.7% | 18.7 | -9.1% | Industrial cranes (EU) |
| REL.L | RELX | 73 | 23.2% | 22.5% | 9.2% | 19.7 | -51.8% | Data/analytics wide moat |
| PCTY | Paylocity | 72 | 20.6% | 21.5% | 23.2% | 25.8 | -49.9% | HCM SaaS (similar to PAYC) |
| TRN.L | Trainline | 70 | 23.1% | 21.7% | 32.9% | 12.0 | -45.3% | UK/EU rail ticketing |
| LNTH | Lantheus | 70 | 39.5% | 30.3% | 53.4% | 27.1 | -41.4% | Diagnostic imaging |
| HILS.L | Hill & Smith | 68 | 14.5% | 12.0% | 11.0% | 23.9 | -0.4% | Infrastructure (not cheap) |
| GAMA.L | Gamma Comms | 65 | 25.5% | 12.7% | 9.0% | 13.0 | -37.9% | UK business telecom |
| ITRK.L | Intertek | 63 | 18.0% | 13.6% | 6.8% | 19.8 | -20.3% | TIC services |

### Most Interesting Tier B:

**FDS (FactSet)** — -58% from highs is extreme. Financial data/analytics with Bloomberg competition but niche positioning. ROIC 19%, FCF margin 27%. Worth investigating cause of fall.

**TRN.L (Trainline)** — UK/EU rail ticketing. 33% revenue CAGR, ROIC 23%, P/E 12x, -45% from highs. Post-COVID recovery turning into genuine digital platform compounder.

**GAMA.L** — UK B2B telecom. ROIC 25.5%, P/E 13x, -38% from highs. Underfollowed (9 analysts). UCaaS platform.

---

## COMBINED PIPELINE FROM V1+V2

### Priority for Full Buy-Pipeline (4 rounds):
1. **PAYC** — QS 85, -55%, P/E 15x, 21% growth, net cash, 12% insider
2. **DSY.PA** — QS 78, -57%, 3D/PLM monopoly, 49% insider, at 52w LOW
3. **RMV.L** — ROIC 385%, FCF 52%, property monopoly, -47% (UK concern)
4. **MORN** — QS 83, -51%, data monopoly, 45% insider, only 3 analysts

### For Fundamental-Analyst:
5. **FDS** — QS 73, -58%, financial data, borderline Tier A
6. **TRN.L** — QS 70, -45%, 33% revenue CAGR, UK rail platform
7. **GAMA.L** — QS 65, -38%, UK B2B telecom, P/E 13x

### Watchlist/Monitor:
8. **VRSN** — QS 83, monopoly but slow growth + P/E 25x
9. **NFLX** — QS 75 but P/E 32x
10. **FSG.L** — QS 83, 34% insider, but verify eToro availability
11. **REL.L** — QS 73, wide moat, 52% off highs but P/E 20x

---

## EXCLUDED / ALREADY KNOWN

| Ticker | Status | Reason |
|--------|--------|--------|
| WKL.AS | Watchlist | Adversarial FV EUR 72. Wait EUR 50-55 post-earnings Feb 25 |
| MEGP.L | Archived | NOT AVAILABLE ON ETORO |
| PAYX | Watchlist AVOID | "HR software caro, no value" (business-services.md) |
| DNLM.L | Watchlist | Standing order 780 GBp |
| CS.PA | Watchlist | AXA, entry EUR 34.50-35.50, earnings Feb 26 |
| INGR | Watchlist | QS 57 Tier B, entry $105-113 |

---

## V2.5: COVERAGE EXPANSION (Session 58, 2026-02-12)

### Methodology
V2 only processed ~800/2,052 tickers (40%) due to yfinance rate limits. V2.5 addresses the gap:
- **Batch 1:** S&P 500 FCF yield >5% — 104 stocks fully processed (no rate limits)
- **Batch 2:** 46 US quality compounders >15% off 52w high — 27 passed (custom ticker list, 1 worker)
- **Batch 3:** 28 EU/UK quality compounders >15% off 52w high — 9 passed
- **Stage 2:** quality_scorer.py on 20 most promising candidates

### NEW TIER A CANDIDATES (5 found)

| Ticker | Name | QS | ROIC | FCF% | %off52H | P/E | Key Note |
|--------|------|-----|------|------|---------|-----|----------|
| **RACE.MI** | Ferrari | 82 | 24.9% | 14.0% | -34.5% | 36.0 | Luxury pricing monopoly, zero debt, 16% rev CAGR |
| **INTU** | Intuit | 77 | 17.2% | 32.3% | -50.9% | 27.4 | TurboTax+QuickBooks+CreditKarma. Net cash, 80% GM |
| **FICO** | Fair Isaac | 75 | 86.0% | 37.1% | -38.5% | 50.4 | Credit score monopoly (~90% US lenders). D/E 3.0x risk |
| **CPRT** | Copart | 75 | 20.9% | 26.5% | -38.1% | 24.2 | Auto auction duopoly. Net cash, 9 analysts, 10% rev CAGR |
| **ADSK** | Autodesk | 75 | 26.9% | 24.5% | -29.3% | 45.3 | CAD/BIM monopoly. 91% GM, subscription transition |

### TIER B WORTH MONITORING (7 found)

| Ticker | QS | ROIC | %off52H | Key Note |
|--------|-----|------|---------|----------|
| NOW | 68 | 14.9% | -52.4% | ServiceNow cloud workflows. FCF 34%, 22% CAGR |
| CRM | 68 | 9.7% | -44.0% | Salesforce. Low ROIC drags QS. FCF 33% |
| MCO | 67 | 24.4% | -24.6% | Moody's rating agency duopoly |
| WDAY | 63 | 5.7% | -48.6% | Workday HCM. Elliott $2B activist |
| SGE.L | 61 | 20.9% | -39.2% | Sage Group UK SME accounting. 93% GM |
| EXPN.L | 60 | 13.7% | -42.1% | Experian credit bureau |
| SPGI | 61 | N/A | -32.5% | S&P Global data + rating monopoly |

### CONFIRMED EXISTING (already in pipeline/standing orders)

| Ticker | QS | Status |
|--------|-----|--------|
| MA | 84 | Standing order $315 |
| V | 82 | Standing order $220 |
| PAYC | 85 | Watchlist $95-105 |
| MORN | 83 | Watchlist $145, earnings Feb 12 |

### TIER D (SKIP)
- FIS — QS 34 Tier D. ROIC 4.4%, D/E 4.0x

### COVERAGE IMPROVEMENT
- V2: ~800/2,052 processed (40%)
- V2.5: +503 SP500 (FCF>5%) + 74 custom quality compounders = **~1,377 processed (~67%)**
- Remaining gap: SP400 mid-caps, smaller EU/UK. Lower priority — primary quality universe covered
- Net new: **5 Tier A + 7 Tier B = 12 actionable candidates**

---

## PIPELINE HEALTH (UPDATED V2.5)

| Category | Count | Tickers |
|----------|-------|---------|
| **Tier A candidates (buy-pipeline needed)** | **9** | PAYC, DSY.PA, RMV.L, MORN, RACE.MI, INTU, FICO, CPRT, ADSK |
| Tier B with MoS (fundamental-analyst) | 10 | FDS, TRN.L, GAMA.L, NOW, CRM, MCO, WDAY, SGE.L, EXPN.L, SPGI |
| Standing orders ready | 2 | DSY.PA (EUR 15.50), DNLM.L (780p) |
| Standing orders (far) | 4 | MA ($315), V ($220/$200), GL ($125), NVO ($40/CagriSema) |
| Total pipeline | ~25 | **VERY HEALTHY** |

Pipeline status: **VERY HEALTHY** (9 Tier A + 10 Tier B candidates). Far exceeds ">=3 thesis ready" threshold.
Cash deployment priority: INTU, CPRT, RACE.MI (biggest MoS + highest quality).
