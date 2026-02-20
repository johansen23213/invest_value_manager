# IHP.L - IntegraFin Holdings PLC

> R1 Fundamental Analysis | Date: 2026-02-20
> Analyst: fundamental-analyst (opus)
> Sector View: world/sectors/uk-adviser-platforms.md

## TL;DR

IntegraFin operates Transact, the UK's leading independent adviser investment platform with GBP 77.2bn FUA, proprietary technology, 97.8% gross margins, and 24.2% insider ownership. QS 80 (Tier A). The stock is 21% below its 52-week high at 315p, punished by revenue margin compression fears (22.4bps -> 21.9bps). My thesis: volume growth (FUA +14% YoY, net inflows +76%) outpaces margin compression (1bps/yr), and the market is anchoring on the margin decline while ignoring the operating leverage from costs guided to grow at only 3%/yr. FV range 380-420p. At 315p, MoS ~17-26%.

---

## Quality Score

**QS Tool: 80/100 (Tier A)**

Breakdown:
| Component | Score | Max |
|-----------|-------|-----|
| Financial Quality | 40 | 40 |
| Growth Quality | 13 | 25 |
| Moat Evidence | 17 | 25 |
| Capital Allocation | 10 | 10 |

**QS Adjusted: 80/100 (Tier A) -- No adjustment warranted.**

Rationale for no adjustment:
- Financial Quality 40/40 is DESERVED: ROIC 49%, ROIC-WACC spread +36.6pp, net cash (GBP 255M), FCF consistency 4/4 years, gross margin 97.8%
- Growth Quality 13/25 is FAIR: Revenue CAGR 5.5%, EPS CAGR 5.2% -- moderate growth accurately scored
- Moat Evidence 17/25 is UNDERSTATED but defensible: Market Position 0/8 (default) could justify +3 to +5 for #1 independent adviser platform in UK with 10% FUA market share and 20%+ net inflow share. However, keeping tool score to avoid inflation pattern
- Capital Allocation 10/10 is DESERVED: 24.2% insider ownership (exceptional), consistent dividends
- NET: The tool captures IHP.L accurately. No adjustment needed.

**NOTE on FCF data:** The quality_scorer.py shows FCF margins >100% which is a data artifact. For financial services platform companies, yfinance reports OCF inclusive of client money movements. The REAL operating FCF is better understood as: Underlying PBT GBP 75.4M + D&A (est. GBP 5-7M) - Maintenance Capex (est. GBP 3-5M) = Owner Earnings ~GBP 75-80M. This gives a real FCF margin of ~48-51% on GBP 157M revenue, which is still exceptional.

---

## Business Understanding

### What IntegraFin Does

IntegraFin Holdings is the parent of **Transact**, the UK's largest independent adviser investment platform built on proprietary technology. Founded in 1999, the platform enables financial advisers to manage client investment portfolios through a comprehensive technology stack offering:

1. **Investment wrappers**: ISAs, SIPPs, GIAs, bonds, offshore bonds
2. **Comprehensive investment range**: 3,000+ funds, ETFs, equities, fixed income, alternatives
3. **Financial planning tools**: Tax planning, reporting, portfolio analytics
4. **CURO (via Time4Advice subsidiary)**: CRM software for adviser practices

### How It Makes Money

**Revenue model: Basis points on FUA (Assets under administration)**

| Revenue Stream | FY25 | % of Total | Growth |
|---------------|------|-----------|--------|
| Annual charge income (bps on FUA) | GBP 138.1M | 88% | +10% |
| Wrapper charges (fixed fees) | GBP 12.5M | 8% | -2% |
| Other (T4A, interest) | GBP 6.2M | 4% | Mixed |
| **Total Revenue** | **GBP 156.8M** | **100%** | **+8%** |

**Revenue driver formula:**
```
Revenue = Average Daily FUA x Revenue Margin (bps) x 365/365
FY25: GBP 67.9bn x ~22.4bps = ~GBP 152M platform revenue
```

**This is a toll-road model**: Every pound that sits on the platform generates recurring revenue every day. The longer clients stay, the more revenue accumulates. Client retention: 95%.

### Unit Economics

- **Revenue per client**: GBP 157M / 246,191 = GBP 637/yr
- **Average portfolio size**: GBP 77.2bn / 246,191 = GBP 313,600/client
- **Cost to serve per client** (approx): GBP 91M underlying costs / 246,191 = GBP 370/yr
- **Profit per client**: ~GBP 267/yr
- **LTV/CAC**: Not directly calculable but client retention 95% implies ~20-year average lifetime. LTV = GBP 267 x 20 = GBP 5,340. CAC is low because advisers bring clients (no direct consumer marketing). LTV/CAC ratio is likely >10x.
- **Capital intensity**: Asset-light. Capex/Depreciation 1.5x (FY25), up from historical <1x due to tech investment. Still very light.

### Margin Structure

| Metric | FY22 | FY23 | FY24 | FY25 | Trend |
|--------|------|------|------|------|-------|
| Gross Margin | 98.4% | 97.1% | 97.9% | 97.8% | Stable (near 98%) |
| Operating Margin | 19.9% | 51.0% | 68.3% | 66.3% | Expanding (FY22 outlier) |
| Underlying PBT Margin | N/A | N/A | 48.7% | 48.1% | Stable ~48% |
| Revenue Margin (bps) | ~25 | ~24 | 23.5 | 22.4 | Compressing ~1bps/yr |

**KEY INSIGHT**: The operating margin from yfinance is misleading (fluctuates wildly due to financial services accounting). The underlying PBT margin of ~48% is the real operating margin. This is exceptional for a platform business and indicates strong operating leverage.

### Competitive Position

Transact is the **#1 independent adviser platform in the UK** by:
- **Net inflow market share**: 20%+ (punches above weight vs 10% FUA share)
- **Customer satisfaction**: #1 in Investment Trends NPS survey 2025
- **Proprietary technology**: One of only 3 major platforms (with HL and AJ Bell) running proprietary tech (vs Quilter/Abrdn on outsourced FNZ infrastructure)
- **Adviser loyalty**: 95% client retention, 7 consecutive quarters of GBP 2bn+ gross inflows
- **FUA**: GBP 77.2bn (Q1 FY26), up 17% YoY

### Why Proprietary Technology Matters

Platforms using outsourced tech (FNZ) pay license fees, have less control over product development, and face switching costs if they want to move. Transact's proprietary tech means:
1. Higher gross margins (no FNZ license fees)
2. Faster product development (direct control)
3. Better customization for advisers
4. A true technology moat (competitors cannot easily replicate 25 years of built functionality)

---

## Why Is It Cheap?

### Current Price: 315p (21% below 52wH of 398p)

### Market Narrative (Bear Case)

1. **Revenue margin compression** (MAIN CONCERN): Platform revenue margin fell from 25bps (FY21) to 22.4bps (FY25) and most recently 21.9bps (Sep 2025). The fear: this is structural and accelerating. If margins compress another 3-4bps to 18bps, earnings growth stalls even with FUA growth.

2. **Analyst downgrades**: Multiple downgrades in late 2025:
   - Panmure Liberum: downgraded to Hold (limited earnings upgrade potential)
   - BofA Securities: initiated with Underperform (margin pressure + competition)
   - Shore Capital: downgraded to Hold after share price rise

3. **T4A (Time4Advice) impairment**: GBP 7.5M goodwill write-down on the CURO subsidiary. Signal of failed diversification?

4. **Pricing cuts**: IntegraFin has proactively reduced pricing on larger portfolios (tiered structure). Market reads this as competitive weakness.

5. **UK market uncertainty**: BoE rates, UK consumer weakness, regulatory risk (SIPP/ISA changes)

### My Contra-Thesis

| Market Believes | I Believe | Evidence |
|----------------|-----------|----------|
| Revenue margin compression will kill earnings | Volume growth outpaces margin compression | FUA +14% YoY, net inflows +76%. Revenue grew +8% despite margin falling 1.1bps |
| Pricing cuts signal weakness | Pricing cuts are OFFENSIVE (to win market share from FNZ platforms) | Net inflow share 20%+ vs 10% FUA share. Winning disproportionately |
| T4A impairment signals failed diversification | T4A is <4% of revenue. Core platform is what matters | GBP 7.5M write-down on a GBP 1.0B market cap company is noise |
| Competition will erode moat | Proprietary tech + 25yr of functionality + adviser switching costs = durable moat | HL going private (less competitive). Quilter/Abrdn on inferior outsourced tech |
| Limited earnings growth | Operating leverage: costs guided +3%/yr vs revenue +8%+ | PBT margin should EXPAND from 48% to 50%+ over FY26-FY27 |

### Value Trap Checklist

| Factor | SI/NO | Comentario |
|--------|-------|------------|
| Industria en declive secular | NO | Wealth management growing structurally |
| Disrupcion tecnologica inminente | NO | They ARE the technology platform |
| Management destruyendo valor | NO | Cost discipline, 24.2% insider alignment |
| Balance deteriorandose | NO | Net cash GBP 255M, improving |
| Insider selling masivo | NO | BUYING (multiple purchases in Jan-Feb 2026) |
| Dividend cut reciente/probable | NO | +9% YoY, 65% payout |
| Perdida market share >2pp 3yr | NO | GAINING share (20%+ of net inflows) |
| ROIC < WACC ultimos 3 anos | NO | ROIC 49% >> WACC 12.5% |
| FCF negativo >2 anos | NO | Consistently positive |
| Goodwill >50% equity | NO | Negligible goodwill (0%) |

**Value Trap Score: 0/10 -- ZERO risk factors**

### My Informational Edge

- **Horizon**: Market anchored on short-term margin compression (quarterly bps). I see 3-5yr operating leverage story (costs +3% vs revenue +8%+)
- **Math**: The market is treating margin compression as linear. In reality, it DECELERATES as the client book seasons (existing clients already through tiering). Management guided slower compression in FY26
- **Comparable**: AJ Bell trades at 28x P/E with similar dynamics but LESS insider ownership (4.7% vs 24.2%) and LESS market share of inflows

---

## Moat Assessment

### Moat Type: NARROW-leaning-WIDE

| Moat Source | Score | Evidence |
|-------------|-------|----------|
| Switching costs | 9/10 | Moving GBP 300K+ portfolio across platforms = weeks of paperwork, tax events, lost time. Advisers reluctant to disrupt client relationships |
| Network effects | 3/10 | Limited. More advisers attract more fund choices but network effects are moderate |
| Technology/IP | 8/10 | 25 years of proprietary platform development. Cannot be replicated quickly |
| Brand/reputation | 6/10 | #1 NPS in adviser surveys. Strong but not consumer-facing |
| Scale advantages | 5/10 | GBP 77bn FUA enables technology investment spread across more clients |
| **Total** | **20/25** | **NARROW-leaning-WIDE** |

### Moat Durability

- **STRENGTHS**: Switching costs are the primary moat and they are INCREASING (more wrappers, more complex portfolios = harder to move). Proprietary tech creates a second layer.
- **RISKS**: Revenue margin compression is a slow moat erosion (charging less per unit of AUM). However, this is an industry-wide phenomenon, not IHP-specific. The question is whether IHP can maintain RELATIVE advantage, and the answer is YES based on proprietary tech and cost discipline.

---

## Projections

### Revenue Projection

```
Revenue = Average Daily FUA x Revenue Margin (bps)

FUA Growth drivers:
- Market returns (FTSE All-Share/Global): ~6-8% long-term
- Net inflows: ~5-7% of opening FUA (based on GBP 4.4bn on GBP 64bn)
- Gross = ~12-15% FUA growth before margin compression

Revenue margin:
- Current: 21.9bps (Sep 2025)
- Compression rate: ~0.5-1.0bps/yr (decelerating per management)
- Projection: ~20-21bps by FY28

Revenue growth = FUA growth (~12%) - margin compression (~4%) = ~8% revenue growth
```

| Year | Avg Daily FUA (bn) | Rev Margin (bps) | Revenue (M) | Growth |
|------|-------------------|------------------|-------------|--------|
| FY25A | 67.9 | 22.4 | 156.8 | +8% |
| FY26E | 78.0 | 21.5 | 172 | +10% |
| FY27E | 88.0 | 21.0 | 190 | +10% |
| FY28E | 98.0 | 20.5 | 206 | +8% |
| FY29E | 108.0 | 20.2 | 224 | +9% |
| FY30E | 118.0 | 20.0 | 242 | +8% |

### Cost Projection

Management guided costs to grow at ~3%/yr in FY26-FY27. This creates significant operating leverage.

| Year | Underlying Costs (M) | Growth | PBT (M) | PBT Margin |
|------|---------------------|--------|---------|------------|
| FY25A | 91.0 | +9% | 75.4 | 48.1% |
| FY26E | 93.7 | +3% | 88.3 | 51.3% |
| FY27E | 96.5 | +3% | 103.5 | 54.5% |
| FY28E | 100.8 | +4.5% | 115.2 | 55.9% |
| FY29E | 105.8 | +5% | 128.2 | 57.2% |
| FY30E | 111.1 | +5% | 140.9 | 58.2% |

### EPS Projection

Assuming 332M shares outstanding, 25% tax rate:

| Year | PBT (M) | Tax | Net Income (M) | EPS (p) | Growth |
|------|---------|-----|----------------|---------|--------|
| FY25A | 75.4 | 25% | 56.5 | 17.4 | +7% |
| FY26E | 88.3 | 25% | 66.2 | 19.9 | +14% |
| FY27E | 103.5 | 25% | 77.6 | 23.4 | +18% |
| FY28E | 115.2 | 25% | 86.4 | 26.0 | +11% |
| FY29E | 128.2 | 25% | 96.2 | 29.0 | +11% |
| FY30E | 140.9 | 25% | 105.7 | 31.8 | +10% |

### WACC Derivation

```
Risk-Free Rate: 4.0% (UK 10Y gilt)
Equity Risk Premium: 5.5% (UK)
Beta: 1.47 (yfinance -- seems HIGH for a platform business, likely reflects small cap volatility)
Adjusted Beta: 1.2 (more appropriate for stable platform business)
Ke = 4.0% + 1.2 x 5.5% = 10.6%

Debt: GBP 13M (negligible)
Cash: GBP 268M
Net cash position -- WACC = Ke = 10.6%

Conservative WACC: 10.5%
```

---

## Valuation

### Method 1 (Primary, 60%): Owner Earnings Yield + Growth

**Tier A method per framework.**

```
Owner Earnings = Underlying PBT GBP 75.4M + D&A ~GBP 6M - Maintenance Capex ~GBP 4M
Owner Earnings = ~GBP 77.4M

Market Cap at 315p: GBP 1,046M (315p x 332M shares)
Enterprise Value: GBP 1,046M - GBP 255M net cash = GBP 791M

Owner Earnings Yield = GBP 77.4M / GBP 1,046M = 7.4%

Expected Sustainable Growth = ~8-10% (FUA growth 12% - margin compression 3%)
Dividend Yield = 3.6%

Total Return Framework:
OEY (7.4%) + Growth (8%) = 15.4%  vs WACC 10.5% = +4.9pp spread
OEY (7.4%) + Growth (8%) + Dividend Reinvested (3.6%) = ~19% total return potential

Reasonable P/E for this profile:
- Growth: ~9% EPS CAGR
- Quality: ROIC 49%, net cash, 97.8% gross margin
- Visibility: 95% retention, recurring revenue
- Comparable: AJ Bell at 28x P/E

Fair Value P/E: 20-22x forward earnings
FY26E EPS: 19.9p
FV Range: 19.9p x 20-22x = 398-438p
Midpoint: 418p
```

### Method 2 (Secondary, 40%): EV/EBIT Normalized

```
Underlying EBIT (FY25): ~GBP 75.4M (PBT proxy, minimal interest expense given net cash)
Normalized EBIT (average FY24-FY26E): ~GBP 78M

Sector comparables:
- AJ Bell: EV/EBIT ~22x
- Hargreaves Lansdown: taken private at ~20x
- Quilter: EV/EBIT ~15x (inferior model, FNZ-based)

Appropriate multiple for IHP.L:
- Proprietary tech (like AJ Bell): +2x vs Quilter
- Highest insider ownership in sector: +1x
- Lower growth than AJ Bell: -2x
- Revenue margin headwind: -1x
Base multiple: 16-18x

EV = GBP 78M x 16-18x = GBP 1,248-1,404M
Equity = EV + Net Cash (GBP 255M) = GBP 1,503-1,659M
FV/share = GBP 1,503-1,659M / 332M shares = 453-500p
Midpoint: 476p

NOTE: This seems high vs Method 1. The key driver is the large net cash position (GBP 255M = 77p/share).
Without net cash: EV-derived equity / shares = 376-423p (more consistent with Method 1).
```

### Reconciliation

The EV/EBIT method gives a higher FV because it explicitly adds back the GBP 255M net cash. However, much of this cash is regulatory capital buffer (only GBP 33.7M is true surplus). Adjusting:

```
Method 2 Adjusted:
EV = GBP 78M x 17x = GBP 1,326M
Equity = GBP 1,326M + Surplus Cash GBP 34M = GBP 1,360M
FV/share = 410p
```

### Weighted Fair Value

| Method | FV | Weight | Weighted |
|--------|-----|--------|----------|
| OEY + P/E (20-22x FY26E) | 418p | 60% | 251p |
| EV/EBIT (17x, surplus cash only) | 410p | 40% | 164p |
| **Weighted Average** | | **100%** | **415p** |

### Sensitivity Assessment

The standard DCF tool is UNRELIABLE for IHP.L (Financial Services FCF data distortion, FCF margin >200%, TV 74.5% of EV). The DCF output showing FV >1,400p is REJECTED as meaningless for this business type.

My valuation relies on P/E multiples and EV/EBIT -- more appropriate for a platform business with recurring revenue.

**Key sensitivity:**
- If revenue margin compresses faster (to 19bps by FY28): FV drops to ~370p
- If FUA growth slows to 8% (market only, no flow growth): FV drops to ~360p
- If costs grow at 5% (not 3%): FV drops to ~385p

**Sensitivity: MODERATE** (main risk is revenue margin compression speed)

### Current Price vs Fair Value

```
Price: 315p
FV: 415p
MoS: (415-315)/415 = 24.1%
```

---

## Scenarios

| | Bear | Base | Bull |
|--|------|------|------|
| Assumption | Revenue margin compression accelerates (19bps by FY28). FUA growth slows. Costs miss target. | FUA +12%/yr, margin compression decelerates per guidance, costs +3%/yr | FUA +15%/yr (market rally + strong flows). Margin stabilizes. M&A optionality |
| FY28E EPS | 20p | 26p | 33p |
| FV Multiple | 17x | 21x | 24x |
| **FV** | **340p** | **415p (weighted)** | **510p** |
| **Probability** | **25%** | **50%** | **25%** |

```
Expected Value = (340 x 25%) + (415 x 50%) + (510 x 25%) = 85 + 207.5 + 127.5 = 420p

MoS vs EV: (420-315)/420 = 25.0%
MoS vs Base: (415-315)/415 = 24.1%
MoS vs Bear: (340-315)/340 = 7.4%
```

### Expected Return Calculation

```
E[CAGR_3yr] = (FV/Price)^(1/3) - 1 + Sustainable_Growth + Dividend_Yield
E[CAGR_3yr] = (415/315)^(1/3) - 1 + ~0% (already in FV via P/E method) + 3.6%
E[CAGR_3yr] = 9.6% + 3.6% = 13.2%

Alternative (just price appreciation to FV):
E[CAGR_3yr] = (415/315)^(1/3) - 1 = 9.6%
Plus dividend: 13.2%
```

E[CAGR] of 13.2% exceeds 12% threshold for Tier A deployment per framework.

---

## MoS Summary

| Metric | Value |
|--------|-------|
| MoS vs Base FV (415p) | 24.1% |
| MoS vs Expected Value (420p) | 25.0% |
| MoS vs Bear (340p) | 7.4% |
| Required (Tier A precedents) | ~10-15% |
| **Meets Tier A MoS?** | **YES -- 24% exceeds typical Tier A range** |

---

## Kill Conditions

1. **Revenue margin compression accelerates below 20bps AND FUA growth decelerates below 8%** (both must occur -- either alone is manageable)
2. **Net outflows for 2+ consecutive quarters** (would signal adviser disengagement from Transact)
3. **Insider selling >5% of holdings within 12 months** (currently buying -- reversal would be very bearish)
4. **Major regulatory change materially reducing adviser platform economics** (e.g., ISA/SIPP tax benefit removal)
5. **Management abandons cost discipline** (costs growing >6%/yr vs guided 3%)
6. **AI disruption of financial advice reduces number of advisers materially** (5-10yr risk, monitor quarterly)

---

## Catalizadores

| Catalyst | Timeline | Probability | Impact |
|----------|----------|-------------|--------|
| FY26 H1 results (operating leverage visible) | ~Jun 2026 | High (70%) | +10-15% if PBT margin expands toward 50%+ |
| BoE rate cut cycle | H1 2026 | Medium (50%) | +5-10% (sentiment boost for UK equities) |
| Equity market rally (FUA growth accelerates) | Ongoing | Medium | Direct revenue driver |
| Adviser consolidation (Transact wins switching advisers) | 1-3yr | Medium | Structural net inflow boost |
| Revenue margin compression decelerates visibly | FY26-27 | Medium (50%) | Re-rating catalyst as market sees stability |

---

## Macro Connection

| Factor | Sensitivity | Current Impact |
|--------|-------------|----------------|
| UK equity markets | HIGH | FTSE near highs = FUA growth supportive |
| Interest rates | MEDIUM | BoE at 3.75%, cuts coming = positive for sentiment |
| UK consumer | LOW-MEDIUM | Advice demand structural, not discretionary |
| GBP/EUR | MEDIUM | GBP strength benefits our EUR-denominated portfolio |
| Regulation | LOW | FCA Consumer Duty benefits quality platforms like Transact |

**Fit with World View**: UK economy weak BUT BoE cuts expected H1 2026 (positive for UK equities and sentiment). IHP.L is not consumer-discretionary -- it is financial infrastructure. Advisers need platforms regardless of consumer confidence. Macro is NEUTRAL-POSITIVE for this thesis.

---

## Insider Activity (Skin in the Game)

**EXTREMELY POSITIVE:**
- 24.2% insider ownership (exceptional for FTSE250 company)
- Multiple insider PURCHASES in Jan-Feb 2026 (Marshall, Scott, Dunbar)
- No insider selling detected
- Institutional ownership 51.7%
- Analyst consensus: BUY (8 buy/hold vs 1 sell), mean target 411p (+30%)

---

## Portfolio Context Notes

- Adding IHP.L would be 5th UK position (after MONY.L, DOM.L, AUTO.L, BYIT.L)
- UK concentration risk documented per P2 -- however, IHP.L is FINANCIAL SERVICES, not consumer discretionary or digital platforms. Different risk profile from existing UK positions
- Correlation with MONY.L: Both are UK financial services platforms. However, MONY.L is price comparison (consumer-facing), IHP.L is adviser platform (B2B). Revenue drivers are different (MONY = consumer searches, IHP = FUA levels + adviser activity)
- UK geographic allocation concern noted -- document why no non-UK alternative is superior

### Why IHP.L vs Non-UK Alternative?

- No direct non-UK comparable exists at Tier A with this quality profile
- The closest global comparables (Australian platform companies like Netwealth, Hub24) are not tradable on eToro
- AJ Bell (UK) trades at 28x P/E (vs IHP.L at 19.7x) with less insider ownership
- The UK adviser platform market is structurally distinct -- US wealth platforms (Schwab, Fidelity) are different business models

---

## Veredicto: WATCHLIST with Standing Order Recommendation

**At 315p, IHP.L offers 24% MoS vs FV 415p with E[CAGR] 13.2% -- above the 12% Tier A threshold.**

However, I recommend WATCHLIST (not immediate BUY) for these reasons:

1. **Earnings proximity**: FY26 H1 results expected ~June 2026. The operating leverage thesis needs validation -- if H1 shows PBT margin expanding toward 50%+, conviction increases materially
2. **Revenue margin data point**: Next quarterly update will show whether compression is truly decelerating as management guided
3. **UK concentration**: With 4 UK positions already, adding a 5th requires higher conviction threshold. MoS of 24% is good but not exceptional for Tier A precedents (NVO had 38%, BYIT.L 35%)
4. **Price trend**: Stock was 398p in Dec 2025, now 315p (21% decline). May still be finding a floor

**Standing Order Recommendation:**
- **Entry: 300p** (MoS 27.7% vs FV 415p)
- **Sizing: 3-4% (EUR 300-400)**
- **Condition: Validate operating leverage thesis with H1 FY26 results before execution OR if price reaches 300p before H1 results**

This is 5% below current price of 315p -- achievable on any moderate market pullback. At 300p, the thesis is compelling enough to add despite UK concentration concerns.

---

## 🔄 META-REFLECTION

### Incertidumbres/Dudas
- The FCF data from yfinance is clearly distorted for IHP.L (FCF margins >200%). This made the standard DCF tool UNRELIABLE. I had to derive owner earnings manually from Underlying PBT. This is a structural limitation for financial services companies in our tooling.
- Revenue margin compression: I project deceleration per management guidance, but I have no independent evidence beyond management's word. If compression continues at 1bps/yr (not decelerating), FV drops to ~380p and MoS shrinks to ~17%.
- The beta of 1.47 from yfinance seems too high for a stable platform business with 95% retention. I adjusted to 1.2 for WACC calculation. If the real beta is closer to 1.0 (which I believe), the WACC would be lower and FV higher.

### Sugerencias para el Sistema
- **quality_scorer.py** should flag when FCF margin >100% as likely data distortion for financial services companies, and suggest using operating profit as FCF proxy
- **dcf_calculator.py** produces meaningless results for financial services companies (FV >1,400p for a 315p stock). Should auto-detect and warn more prominently, or use a different model for financials
- A **platform valuation model** (revenue margin x FUA growth approach) would be more appropriate for companies like IHP.L, AJB.L, HL.L than standard DCF

### Preguntas para Orchestrator
1. Given we already have 4 UK positions (MONY.L, DOM.L, AUTO.L, BYIT.L), should I apply a higher MoS threshold for IHP.L? Current 24% is good but not exceptional.
2. IHP.L and MONY.L are both UK financial services platforms. Is there meaningful correlation risk beyond geographic?
3. Should we fast-track to R2 (devil's advocate) given proximity to universe entry, or wait for H1 results validation?

### Anomalias Detectadas
- yfinance reports IHP.L FCF margin of 207.6% which is clearly wrong for the actual business (real underlying FCF margin is ~48-51%). All DCF-based analysis should be treated with extreme caution.
- ROIC trajectory shows wild swings (25% -> 69% -> 142% -> 49%) which also reflects data quality issues in yfinance for financial services companies.
- The EV/EBIT of 7.5x (from reverse DCF tool) seems very low for a Tier A quality compounder. This suggests the market is pricing IHP.L as if it were a slow-growth or declining business, which contradicts the +76% net inflow growth.

---

Sources:
- [IntegraFin Holdings plc](https://www.integrafin.co.uk/)
- [IntegraFin FY25 Annual Results (Dec 2025)](https://www.integrafin.co.uk/media/1zapl3v5/fy25-year-end-results-announcement-rns.pdf)
- [IntegraFin H2 Earnings Call Highlights](https://www.dailypolitical.com/2025/12/22/integrafin-h2-earnings-call-highlights.html)
- [IntegraFin Q1 FY26 Strong Start](https://www.sharecast.com/news/news-and-announcements/integrafin-reports-strong-start-to-2026-financial-year--21492436.html)
- [IntegraFin FY25 Results - Investing.com](https://www.investing.com/news/stock-market-news/integrafin-holdings-reports-solid-fy25-results-with-focus-on-margin-expansion-93CH-4411866)
- [IntegraFin FY25 Results Analysis](https://joshthompson.co.uk/investing/integrafin-reports-strong-fy25-earnings-growth-record-net-inflows/)
- [IntegraFin eToro Page](https://www.etoro.com/markets/ihp.l)
- [Yahoo Finance IHP.L](https://finance.yahoo.com/quote/IHP.L/)
- [IntegraFin Wikipedia](https://en.wikipedia.org/wiki/IntegraFin)
- [Proactive Investors - IntegraFin Downgrades](https://www.proactiveinvestors.com/companies/news/1074831/integrafin-downgraded-on-valuation-grounds-and-limited-upgrade-earnings-potential-1074831.html)
