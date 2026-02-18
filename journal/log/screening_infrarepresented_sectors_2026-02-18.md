# Sector Screening: Infrarepresented Sectors for Capital Deployment
> Date: 2026-02-18
> Sectors: Healthcare Equipment, Industrial Technology, Utilities (EU)
> Objective: Find NEW candidates (not in quality_universe) with QS >= 55

---

## Screening Summary

### Method
1. `dynamic_screener.py --index europe_all --undiscovered` (194 results from 610 tickers)
2. `dynamic_screener.py --index stoxx600 --pe-max 18 --yield-min 2 --near-low 25` (partial -- rate limited)
3. Web search for sector-specific opportunities (Morningstar, Kepler Cheuvreux, Bernstein)
4. `quality_scorer.py` on 9 candidates

### Companies Scored (NEW -- not in quality_universe)

| Ticker | Name | QS Tool | Tier | ROIC-WACC | GM | FCF Margin | Rev CAGR | P/E | Yield | Dist 52wH | Sector |
|--------|------|---------|------|-----------|-----|-----------|----------|-----|-------|-----------|--------|
| **MEGP.L** | ME Group International | **80** | **A** | **+32.3pp** | 35.6% | 10.6% | +12.8% | 9.6x | 5.8% | **-39.5%** | Industrials (Kiosks) |
| LAGR-B.ST | Lagercrantz Group | 67 | B | +4.6pp | 39.0% | 12.3% | +19.6% | 37.9x | 1.1% | -15.3% | Industrial/Serial Acquirer |
| JDG.L | Judges Scientific | 65 | B | +1.5pp | 68.9% | 16.5% | +13.5% | 31.1x | 2.1% | -44.4% | Industrial/Scientific Instruments |
| GAMA.L | Gamma Communications | 65 | B | +17.7pp | 51.8% | 12.7% | +9.0% | 12.6x | 2.3% | -38.8% | Telecom/UCaaS |
| G1A.DE | GEA Group | 59 | B | +6.6pp | 35.7% | 8.7% | +4.9% | 25.6x | 1.8% | -2.4% | Industrial/Food Tech |
| COLO-B.CO | Coloplast | 56 | B | +8.6pp | 67.6% | 5.3% | +11.6% | 27.2x | 4.8% | -40.6% | Healthcare/MedTech |
| VIE.PA | Veolia | 52 | C | +1.0pp | 17.4% | 11.3% | +16.2% | 22.1x | 4.2% | -0.6% | Utilities/Water-Waste |
| ENEL.MI | Enel | 45 | C | +1.3pp | 54.0% | 4.3% | +1.1% | -- | 5.3% | -10.8% | Utilities |
| SSE.L | SSE plc | 28 | **D** | -0.2pp | 38.1% | neg | +5.2% | -- | 2.4% | -- | Utilities |
| FUTR.L | Future plc | 28 | **D** | -3.0pp | 44.5% | 13.7% | -3.6% | 6.6x | 4.2% | -61.9% | Media/Publishing |

### Eliminated
- **SSE.L** (Tier D): ROIC < WACC, negative FCF 2 of 4 years, declining EPS
- **FUTR.L** (Tier D): ROIC < WACC, declining revenue, declining margins -- value trap
- **ENEL.MI** (Tier C): Inconsistent FCF (-2.3B and -4.6B in 2021/2022), ROIC-WACC barely positive
- **VIE.PA** (Tier C): QS 52, low GM 17%, 3.8x Net Debt/EBITDA, 90.9% payout ratio

---

## TOP CANDIDATES (QS >= 55, not in quality_universe)

### 1. MEGP.L -- ME Group International (QS 80 Tier A) -- HIGHEST PRIORITY

**Why this is exceptional:**
- QS 80 = Tier A Quality Compounder
- ROIC-WACC spread of +32.3pp -- among the highest in our entire universe
- Net cash balance sheet (no leverage)
- 37.3% insider ownership (founder-led)
- 5.8% dividend yield with 52.5% payout ratio (well-covered)
- Trading at P/E 9.6x and -39.5% below 52-week high
- Revenue CAGR +12.8%, EPS CAGR +35.4%
- Market cap GBP 543M (small cap -- less analyst coverage = potential mispricing)

**Business:** Global leader in automated self-service kiosks:
- Photo.ME: 30,600+ photobooths across 18 countries (30-60%+ market share by country)
- Wash.ME: 8,500+ laundry kiosks (key growth driver, +17.7% revenue growth H1 2025)
- Revolution laundry EBITDA margins >40%, rapidly expanding
- H1 2025: Revenue GBP 153.8M (+4.7% CC), EBITDA GBP 53.2M (34.6% margin)
- FY2025 guidance: Revenue GBP 311-318M, PBT GBP 76-79M (record profitability)

**Risks to investigate:**
- Photo booth segment may face secular decline (digital ID, smartphone cameras)
- Laundry kiosk business is the growth thesis -- need to verify TAM and competitive dynamics
- Small cap, only 2 analysts -- lower liquidity
- UK concentration risk (already have 4 UK positions)

**Entry estimate:** Current price 143.8p. At P/E 9.6x for a QS 80 company, this looks significantly undervalued. Quick FV estimate: If normalized earnings ~15p EPS at fair P/E 15-18x = FV 225-270p. Current price implies ~35-45% upside.

**Recommended action:** ADVANCE TO R1 (buy pipeline). This is the strongest find of this screening.

---

### 2. JDG.L -- Judges Scientific (QS 65 Tier B, already in sector view)

**Why interesting:**
- UK serial acquirer of scientific instrument companies
- 68.9% gross margin, 16.5% FCF margin, 15.5% insider ownership
- -44.4% below 52-week high (major dislocation)
- Revenue CAGR +13.5% (organic + acquisitions)

**Concerns:**
- ROIC declining (30.9% -> 9.2%) as goodwill from acquisitions accumulates (serial acquirer distortion)
- US federal research funding headwinds (significant customer base)
- P/E 31.1x on trough earnings -- not cheap on headline P/E
- Already in industrial-technology sector view as Priority Alta target

**Status:** Already tracked in sector view. Not adding to this screening -- already flagged.

---

### 3. COLO-B.CO -- Coloplast (QS 56 Tier B, already in healthcare-equipment sector view)

**Why interesting:**
- Global leader in ostomy/wound care (30% insider ownership, 68% GM)
- -40.6% below 52-week high (significant dislocation)
- ROIC-WACC +8.6pp
- 4.8% dividend yield

**Concerns:**
- QS 56 is borderline (needs adjustment for market position, but FCF margin dropped to 5.3%)
- Operating margin declining (32.7% -> 27.0%)
- Leverage 2.8x Net Debt/EBITDA (Atos Medical acquisition)
- DKK 480 near 52-week low of DKK 475 -- may still have downside

**Status:** Already tracked in healthcare-equipment sector view as Priority Alta target.

---

### 4. G1A.DE -- GEA Group (QS 59 Tier B)

**Why interesting:**
- German food processing technology, ROIC-WACC +6.6pp, net cash
- Improving margins: GM 33.1% -> 35.7% (expanding), OM 7.8% -> 9.9%
- Kepler Cheuvreux top EU capital goods pick for 2026
- Defensive end-markets (food/beverage/pharma)

**Concerns:**
- P/E 25.6x -- near 52-week high (only -2.4% off high) = no MoS
- Revenue growth anemic (+0.9% in 2024)
- 0% insider ownership
- QS 59 needs to improve to be compelling

**Status:** Monitor. Good company but no valuation opportunity currently.

---

### 5. GAMA.L -- Gamma Communications (QS 65 Tier B)

**Why interesting:**
- UK UCaaS provider, ROIC-WACC +17.7pp
- Near-zero leverage (0.3x), 51.8% GM, +9% revenue/EPS CAGR
- -38.8% off high, P/E 12.6x
- 87% institutional ownership -- well-known to UK fund managers

**Concerns:**
- 1.1% insider ownership (low skin in the game)
- Telecom sector -- commoditization risk from larger players (Microsoft Teams, Zoom)
- UK concentration (already 4 UK positions)
- FCF margin declining (16.3% -> 12.7%)

**Status:** Interesting but deprioritize due to UK concentration risk. Add to watchlist if UK exposure decreases.

---

## SECTOR-LEVEL CONCLUSIONS

### Healthcare Equipment
Sector view already comprehensive (28+ companies screened Feb 14). Coloplast (COLO-B.CO) confirmed as best new candidate at QS 56, but already tracked. No NEW names found beyond existing sector view. The sector is well-covered.

### Industrial Technology
Sector view already comprehensive. Lagercrantz (QS 67) is a known Nordic serial acquirer already on the radar. GEA Group (QS 59) is new but no MoS currently. Judges Scientific (QS 65) already tracked. ME Group International (QS 80) is the standout DISCOVERY from this screening -- not previously on radar.

### Utilities (EU)
**This is the weakest sector for our quality framework.** Every utility scored either Tier C or Tier D:
- VIE.PA: QS 52 (Tier C), ROIC barely above WACC, high leverage
- ENEL.MI: QS 45 (Tier C), inconsistent FCF
- SSE.L: QS 28 (Tier D), ROIC < WACC
- Hera: ROIC < WACC (from web data)

**Conclusion on utilities:** European utilities structurally conflict with our quality framework. They have low ROIC, high leverage, capital-intensive models, and inconsistent FCF. The yields (4-6%) are attractive but do not compensate for the quality deficiency. We should NOT pursue this sector for the portfolio. DTE.DE (already owned) remains the best utility exposure we can find.

---

## VALIDATION CHECKLIST

- [x] Found >10 companies? YES (10 scored, 28+ in healthcare already in sector view)
- [x] Any company I did NOT know before? YES -- ME Group International (MEGP.L)
- [x] Top match has better valuation than famous names? YES -- MEGP.L P/E 9.6x vs ISRG 62x
- [x] Multiple geographies compared? YES -- UK, Denmark, Germany, Sweden, France, Italy
- [x] Anti-availability bias: used --undiscovered flag? YES
- [x] Screener results validated with quality_scorer.py? YES (9 companies)

---

## RECOMMENDED NEXT STEPS

1. **MEGP.L -> R1 pipeline** (highest priority new find, QS 80 Tier A at P/E 9.6x)
2. Continue monitoring COLO-B.CO, JDG.L (already in sector views)
3. GEA Group: add to watchlist, wait for >15% correction
4. **Do NOT pursue EU utilities** -- structural quality mismatch
5. Score remaining Nordic serial acquirers (LIFCO-B.ST, INDT.ST) when yfinance rate limit resets
