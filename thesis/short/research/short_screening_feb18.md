# Short Candidate Discovery - Fragility Screening
# Date: 2026-02-18
# Purpose: Expand short pipeline beyond LYV (S4 approved) and CVNA (S2 complete)
# Methodology: Programmatic screening + activist short report analysis + structural fragility research
# Anti-bias: Focused on structural fragility + catalyst, NOT "expensive" alone (Error #44, #46)

---

## SCREENING METHODOLOGY

### Sources Used
1. **Programmatic**: `dynamic_screener.py --index sp500 --pe-min 40` (78 stocks found)
2. **Programmatic**: `dynamic_screener.py --index europe_all --pe-min 50` (23 stocks found)
3. **Activist Short Reports (Feb 2026)**:
   - Spruce Point Capital: REZI (Jan 27, 2026)
   - Wolfpack Research: IONQ (Feb 4, 2026)
   - Culper Research: NXE (Feb 6, 2026)
   - Grizzly Research: EOS (Feb 6, 2026)
   - Culper Research + CapitalWatch: APP (ongoing since 2025, new Jan 2026 report)
4. **SEC Enforcement**: Morgan Lewis roundup Jan/Dec 2025
5. **Market data**: price_checker.py for current prices

### Anti-Bias Checks
- [x] Avoided "popular" shorts (TSLA, RIVN, LCID, GME, AMC)
- [x] Searched multiple geographies (US + EU)
- [x] Used programmatic screening, not just memory
- [x] Verified structural fragility, not just "expensive"
- [x] Identified catalyst with date for each candidate
- [x] Checked for companies NOT already in our pipeline

### Already In Pipeline (EXCLUDED)
- LYV: S4 APPROVED CONDITIONAL (DOJ trial Mar 2)
- CVNA: S2 COMPLETE (Q4 earnings reported Feb 18, awaiting S3)
- BA: Previously screened (NEEDS_S1, secondary priority)
- PLTR: Previously screened (NEEDS_S1, tertiary priority)

---

## NEW SHORT CANDIDATES - RANKED BY CONVICTION

### RANK 1: APP (AppLovin Corporation) - RECOMMEND S1

**Summary**: Ad-tech company under SEC investigation for data-collection practices, facing multiple
securities class action lawsuits, and targeted by three independent short sellers (Culper Research,
Fuzzy Panda Research, CapitalWatch) alleging ad fraud, undisclosed China operations, and money
laundering connections.

| Metric | Value |
|--------|-------|
| Price | $402.95 (EUR 339.84) |
| Market Cap | $136.3B (EUR ~115B) |
| P/E (trailing) | 40.1x |
| P/E (forward) | 27.3x |
| % off 52w High | -46.1% |
| Short Interest | 4.44% of float (13.05M shares) |
| D/E | 1.66 |

**Structural Fragility (NOT just "expensive")**:
1. SEC investigation (Oct 2025) into data-collection practices and platform agreement violations
2. Three independent short seller reports alleging ad fraud:
   - Culper Research (Feb 2025): "backdoor installations," artificial inflation of metrics
   - Fuzzy Panda Research (Feb 2025): corroborated fraud allegations
   - Culper Research (Jun 2025): undisclosed agency agreements with Chinese AdTech companies
     despite management claiming "we don't operate inside China" on earnings call (May 2025)
   - CapitalWatch (Jan 2026): alleged "asset sale haven for cross-border black money"
3. Multiple securities class action lawsuits filed (Rosen Law, Hagens Berman, Labaton Keller)
   - Class period: May 2023 - March 2025
   - Lead plaintiff motion deadline: May 5, 2025 (PASSED - case proceeding)
4. State attorneys general investigations (multiple states)
5. $13.7B in shareholder value wiped out on Feb 26, 2025 alone
6. Q4 2025 beat expectations (EPS $3.24 vs $2.96, rev $1.66B vs $1.61B) but stock STILL fell 3.3%
   in after-hours -- market not rewarding beats, indicating overhang from investigations

**Catalyst + Date**:
- **PRIMARY**: SEC investigation resolution/enforcement action (timeline: H1-H2 2026)
- **SECONDARY**: Class action lawsuit proceedings (discovery phase 2026)
- **TERTIARY**: Next earnings May 13, 2026 -- if fraud allegations have substance, will show in
  revenue quality metrics
- DOGE/government contract review could expose any government-related ad spend irregularities

**Estimated QS Range**: 35-45 (Tier C). Strong revenue growth but sustainability questionable if
ad fraud allegations have merit. High SBC, questionable accounting transparency around AXON 2.0
AI claims.

**Squeeze Risk**: MODERATE. Short interest at 4.44% is manageable. Not a meme stock. Institutional
ownership dominant. However, stock has proven volatile (745 -> 200 -> 402 in 12 months).

**Why This Is NOT Just "Expensive"**:
APP at 40x P/E is not absurdly expensive on face value. The short thesis is NOT valuation-based.
It is fraud/regulatory-based: SEC probe, class actions, three independent short sellers alleging
ad fraud and undisclosed China operations. If allegations are even partially substantiated,
revenue recognition and growth narrative collapse. This is structural fragility per Error #46.

**Recommended Next Step**: S1 ANALYSIS. High conviction candidate with clear catalysts.

---

### RANK 2: IONQ (IonQ, Inc.) - RECOMMEND WATCH / POSSIBLE S1

**Summary**: Largest publicly traded quantum computing company. Wolfpack Research (Feb 4, 2026)
alleges 86% of revenue depended on now-cancelled government "backdoor earmarks," creating a
$54.6M revenue "black hole." Trades at 141x sales while burning $408M EBITDA annually.

| Metric | Value |
|--------|-------|
| Price | $33.47 (EUR 28.23) |
| Market Cap | $12.0B (EUR ~10.1B) |
| P/E (trailing) | N/A (unprofitable) |
| P/S | ~57x forward (vs industry avg 4.9x) |
| % off 52w High | -60.5% |
| Short Interest | ~21% of float (VERY HIGH - pre-report) |
| Revenue (FY2025E) | $106-110M |

**Structural Fragility**:
1. Wolfpack Research (Feb 4, 2026): alleges 86% of 2022-2024 booked revenue came from government
   "backdoor earmarks" inserted by friendly lawmakers into Pentagon budget
2. Those earmarks were CANCELLED after Republicans took Congress in 2025
3. Only $12M of $54.5M Air Force contract was actually funded (rest was "total possible future awards")
4. Company acquiring non-quantum businesses (Capella, Vector Atomics, ID Quantique) to backfill
   lost Pentagon revenue -- growth is INORGANIC and non-core
5. Management ~$400M in stock sales raise insider trading investigation concerns
6. Legal probe: Ademi LLP announced securities fraud investigation (Feb 6, 2026)
7. Fundamental problem: quantum computing is genuinely pre-commercial, $12B valuation on $110M
   revenue is extreme even for "next big thing" narrative

**Catalyst + Date**:
- **PRIMARY**: Q4 FY2025 earnings on February 25, 2026 (7 DAYS AWAY) -- first results after
  Wolfpack report. Revenue quality will be scrutinized. If organic revenue disappoints, stock drops.
- **SECONDARY**: Securities fraud investigation proceedings (H1 2026)
- **TERTIARY**: Government contract renewal cycles throughout 2026

**Estimated QS Range**: 10-20 (Tier D). Pre-profit, massive cash burn, revenue quality questioned,
insider selling pattern. Would be Tier D = NO COMPRAR for long side.

**Squeeze Risk**: HIGH. 21% short interest is very elevated. Any positive quantum computing news
(government AI/quantum initiative, partnership announcement) could trigger violent squeeze.
Float is relatively small. This is the key risk.

**Why This Is NOT Just "Expensive"**:
Not about valuation per se. Revenue was allegedly dependent on earmarks that are now cancelled.
If 86% figure is even directionally correct, the revenue base is a mirage. Company response was
generic denial. Securities fraud investigation launched. This is a legitimate structural fragility.

**Recommended Next Step**: WATCH earnings Feb 25. HIGH squeeze risk (21% SI) makes this dangerous
despite strong thesis. If earnings confirm revenue deterioration post-earmark cancellation,
consider S1 with very small position size (P11 asymmetry). eToro availability for CFD short
needs verification.

---

### RANK 3: REZI (Resideo Technologies) - RECOMMEND WATCH

**Summary**: Home automation/security hardware company targeted by Spruce Point Capital (Jan 27, 2026)
with "Strong Sell" opinion alleging 25-50% downside ($17.64-$26.45). Concerns about accounting
practices around acquisitions and aggressive customer life assumptions.

| Metric | Value |
|--------|-------|
| Price | $36.64 (EUR 30.90) |
| Market Cap | $5.5B (EUR ~4.6B) |
| P/E (trailing) | ~13x (normalized) or N/A (GAAP negative) |
| Leverage | 5.5x (up from 3.3x at spin-off 2018) |
| % off 52w High | -19.1% |

**Structural Fragility**:
1. Spruce Point Capital (Jan 27, 2026): "Strong Sell" with 25-50% downside
2. 4 CFOs and 4 Chief Accounting Officers since going public (red flag for financial reporting)
3. Problematic ERP system complicating financial reporting across 13+ acquisitions
4. First Alert (2022) and Snap One (2024) acquisitions described as "particularly troubled"
5. Customer life assumption increased from 10 to 12 years in Snap transaction (vs 7-8 competitive norm)
6. Spruce Point estimates pre-tax income inflated 8-12% from aggressive assumptions
7. Leverage risen to 5.5x (dangerous for hardware distributor)
8. Trades at 1.3x 2026E revenue (2x the long-term median of 0.6x)
9. CEO transition underway (leadership instability)

**Catalyst + Date**:
- **PRIMARY**: Post-earnings reporting scrutiny (next earnings date TBD, likely late Feb/early Mar)
- **SECONDARY**: Spruce Point report creating sustained selling pressure
- **TERTIARY**: Debt covenants at 5.5x leverage could trigger if EBITDA disappoints

**Estimated QS Range**: 25-35 (Tier D). CFO/CAO rotation, aggressive accounting, high leverage,
troubled acquisitions. Low quality business.

**Squeeze Risk**: LOW. Not a meme stock. Small market cap ($5.5B). Institutional ownership dominant.

**Why This Is NOT Just "Expensive"**:
At 13x P/E this is NOT expensive. The thesis is about ACCOUNTING QUALITY: aggressive customer
life assumptions inflating earnings, serial CFO rotation, problematic ERP, and high leverage.
If Spruce Point's 8-12% pre-tax income inflation estimate is correct, real P/E is higher and
the debt burden is more dangerous than it appears.

**Recommended Next Step**: WATCH. Smaller market cap makes it potentially less liquid for CFD
short on eToro. Need to verify eToro availability. Interesting as a forensic accounting play
but lower conviction than APP.

---

### RANK 4: PLTR (Palantir Technologies) - MAINTAIN NEEDS_S1 (from prior screen)

Already in previous screening file. Updated assessment:

**NEW DATA (Feb 2026)**:
- Q4 2025 earnings BLEW OUT: Revenue $1.41B (+70% YoY), US commercial +137%
- FY2026 guidance: $7.18-7.20B (consensus was $6.22B) -- CRUSHED expectations
- Stock rallied 11% post-earnings despite 215x P/E
- Government revenue: $570M Q4 (+66% YoY), NOT declining from DOGE cuts yet
- Commercial TCV bookings: $2.6B (+161% YoY)

**REVISED ASSESSMENT**: The short thesis on PLTR has WEAKENED materially. Government revenue
is accelerating, not declining. The "DOGE will cut Palantir" narrative was wrong -- Palantir
appears to be BENEFITING from government AI modernization. At 215x P/E the stock is still
extremely expensive, but the fundamental trajectory is moving in the WRONG direction for shorts.

**Recommendation**: DEPRIORITIZE. Move from NEEDS_S1 to MONITOR. The earnings blowout makes
this a dangerous short -- the narrative is confirmed by data (for now). Only reconsider if
government revenue decelerates in Q1-Q2 2026 or AI spending sentiment reverses.

---

### RANK 5: SMCI (Super Micro Computer) - SKIP

Considered but REJECTED as short candidate.

**Reasons for SKIP**:
- Stock already at $29.66, down from $66+ (55% decline from highs)
- Regained Nasdaq compliance (Jan 2026)
- BDO gave adverse opinion on internal controls but no restatement
- Market has largely priced in the accounting concerns
- DOJ/SEC investigations are ongoing but stock reflects this
- At 21.6x P/E and massive AI infrastructure tailwind, the risk/reward for shorts is poor
- Shorting after a 55% decline with AI spending tailwind = fighting the trend

---

## CANDIDATES NOT PURSUED (with reasons)

| Candidate | Reason for Skip |
|-----------|----------------|
| TSLA | Popular short = availability bias (Error #7). No structural fragility that market hasn't seen. |
| RIVN/LCID | EV bubble already deflated. Not in S&P 500. Well-shorted. |
| CSGP | Better as LONG if activists succeed (from prior screen). |
| WDAY | -49% and 13x forward P/E = potentially a VALUE BUY not a short. |
| NOW | -49% and 21x forward P/E = value territory. |
| NXE (Culper target) | Uranium mining, pre-revenue. Not available on eToro. Too small. |
| EOS (Grizzly target) | Australian defense, tiny market cap. Not available on eToro. |

---

## SUMMARY TABLE - ALL CANDIDATES

| Rank | Ticker | Thesis Type | Fragility Score (1-10) | Catalyst | Date | Next Step |
|------|--------|-------------|----------------------|----------|------|-----------|
| 1 | APP | Fraud/Regulatory | 8/10 | SEC investigation + class actions | H1-H2 2026 | **S1 ANALYSIS** |
| 2 | IONQ | Revenue mirage | 7/10 | Q4 earnings + securities investigation | Feb 25, 2026 | WATCH (squeeze risk) |
| 3 | REZI | Accounting quality | 6/10 | Spruce Point report + earnings | Mar 2026 | WATCH |
| 4 | PLTR | Valuation extreme | 4/10 (WEAKENED) | DOGE cuts / sentiment shift | Rolling 2026 | DEPRIORITIZE |
| -- | SMCI | Accounting (resolved) | 3/10 | DOJ/SEC investigation | 2026-2027 | SKIP |

---

## PIPELINE STATUS AFTER THIS SCREENING

| Stage | Ticker | Status | Priority |
|-------|--------|--------|----------|
| S4 APPROVED | LYV | Standing order EUR 100. Entry Feb 20-28. | EXECUTE |
| S2 COMPLETE | CVNA | Awaiting Q4 data for S3. | HIGH |
| NEEDS S1 | APP | **NEW** - strongest new candidate. | HIGH |
| NEEDS S1 | BA | From prior screen. Monthly delivery data monitoring. | MEDIUM |
| WATCH | IONQ | **NEW** - strong thesis but 21% SI squeeze risk. | MEDIUM |
| WATCH | REZI | **NEW** - forensic accounting play, smaller cap. | LOW |
| DEPRIORITIZED | PLTR | Q4 blowout weakened thesis. Monitor only. | LOW |
| DEPRIORITIZED | ENR.DE | Stock -42% from screening price. | SKIP |
| REMOVED | VTY.L | Removed S76. | CLOSED |
| REMOVED | RAND.AS | Deprioritized S76. | CLOSED |

---

## META-REFLECTION

### Biases Checked
- Did NOT start with "famous shorts" (TSLA, GME) -- used programmatic screening first
- Discovered APP, IONQ, REZI through activist short report research, not popularity
- Checked European market (found few compelling shorts -- mostly cyclical semis in trough)
- Applied Error #44 strictly: every candidate has dated catalyst
- Applied Error #46 strictly: every thesis has structural fragility beyond "expensive"

### Key Strategic Observation
The current market shows a BIFURCATION:
- Software/SaaS companies are already heavily discounted (-40-50% from highs) -- these are
  potential LONGS, not shorts
- Ad-tech/quantum/speculative growth companies still carry fraud/structural risk
- The best short candidates are NOT the "most expensive" -- they are the ones where
  REVENUE QUALITY is questionable (APP fraud allegations, IONQ earmark dependence, CVNA
  related-party transactions)

### Limitation
- Could not verify eToro CFD availability for all candidates programmatically
- European screening yielded few candidates (mostly cyclical troughs, not structural fragility)
- Hindenburg Research disbanded Jan 2025, removing a major source of short intelligence

---

**Screening completed: 2026-02-18**
**Analyst: Claude (sector-screener)**
**Next action: Submit APP for S1 short pipeline analysis**
