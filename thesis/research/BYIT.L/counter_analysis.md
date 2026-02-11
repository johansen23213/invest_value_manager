# Counter-Analysis: BYIT.L (Bytes Technology Group plc)

## Fecha: 2026-02-09

## PROCESS FINDING: NO ADVERSARIAL PIPELINE WAS RUN

**This position was purchased on 2026-02-07 at ~296 GBp WITHOUT the full adversarial pipeline.**

Evidence: The directory `thesis/active/BYIT.L/` contains ONLY `thesis.md`. There is no:
- `moat_assessment.md` (independent moat assessment)
- `risk_assessment.md` (independent risk identification)
- `valuation_report.md` (independent valuation)
- `counter_analysis.md` (devil's advocate review)
- `committee_decision.md` (formal committee approval with 10 gates)

The buy-pipeline requires 4 rounds with independent agents. This position bypassed all of that. The thesis was written by the fundamental-analyst alone, with no independent challenge before purchase.

**This is the FIRST finding and it colors everything that follows.**

---

## Resumen Ejecutivo

The thesis has moderate-to-serious vulnerabilities. The investment story is reasonable but the analysis contains a critical factual error (insider ownership overstated by ~7x), underestimates the structural nature of Microsoft's channel compression, and was purchased at what may be the beginning -- not the end -- of margin deterioration. The 35% MoS claimed in the thesis shrinks to 3-16% under bear assumptions. The position is small (3.5%) and the business is genuinely high-quality, which limits downside -- but the thesis should have been stress-tested before capital was deployed.

---

## Asunciones Clave Desafiadas

### 1. "QS 81 = Tier A Quality Compounder"

- **Thesis claim:** QS 81, Tier A. ROIC spread +4.9pp acknowledged as low but dismissed because "asset-light business distorts ROIC calculation."
- **Evidencia en contra:**
  - The ROIC spread of 4.9pp is the LOWEST of any Tier A position in the portfolio. For comparison: AUTO.L has ROIC spread +38pp, MONY.L has ROIC spread +20pp, LULU has 25%+ ROIC. BYIT's 4.9pp is closer to Tier B territory.
  - The thesis dismisses this by saying "FCF margin 30% is more relevant." But FCF margin of 30% is measured on gross profit (GBP 160M), not revenue (GBP 2.1B GII). On a GII basis, FCF margin is ~2.3%. The 30% figure flatters the business by using a selective denominator.
  - The QS tool awards 10/10 for Capital Allocation partly based on "9.6% insider ownership." Independent research shows actual insider ownership is 0.5-1.5% (see Challenge #10). This would reduce Capital Allocation score from 10 to 6, dropping QS from 81 to 77. Still Tier A, but barely.
  - The FCF consistency score is 4/5 (not perfect) -- one year of negative/low FCF breaks the pattern.
  - H1 FY2026 showed operating profit DECLINING 7%. This is not compounder behavior.
- **Severidad:** MODERATE
- **Resolution:** QS is likely 75-77 (still Tier A) but at the very bottom of the tier. The "quality compounder" label is aggressive for a company whose operating profit is declining. Monitor closely -- if H2 FY2026 also shows OP decline, the compounding thesis breaks.

### 2. "Microsoft incentive changes are cyclical, not structural"

- **Thesis claim:** Microsoft restructures partner programs every 2-3 years. Partners adapt. 25% probability thesis is wrong.
- **Evidencia en contra:**
  - Microsoft is taking ALL large Enterprise Agreement renewals DIRECT by January 2026. This is not a cyclical adjustment -- it is a permanent structural shift in Microsoft's go-to-market model.
  - Microsoft paid LSPs ~$2.5B in commissions in 2023. Projected: $583M in 2025. ZERO in 2026. This is a 100% loss of EA commission revenue for licensing solution providers.
  - The thesis focuses on CSP incentive changes (revenue thresholds from $300K to $1M) but MISSES the larger EA disintermediation story entirely. EA renewals going direct is a much bigger structural headwind than CSP threshold changes.
  - Berenberg explicitly stated the disruption "is unlikely to be limited to the first half of 2026" and downgraded to Hold with target cut from 660p to 390p.
  - Microsoft's push to CSP and Marketplace as primary channels REDUCES the value partners add in the software resale layer. Partners' value increasingly depends on services -- but services is only 30% of GP today.
  - The Growth Accelerator incentive rewards partners who grow customer revenue, but Microsoft is simultaneously reducing the MARGIN available on that growth. Growing revenue at shrinking margins is a treadmill, not a moat.
- **Severidad:** HIGH
- **Resolution:** The thesis significantly underestimates the structural nature of Microsoft's channel evolution. The 25% "probability wrong" should be 40-50%. This is the most important risk to the thesis. Committee should assess whether the services growth (30% of GP growing 40%) can realistically offset the structural decline in software margin contribution (70% of GP with declining margins).

### 3. "Services growth 40%+ offsets margin compression"

- **Thesis claim:** Services at 30% of GP growing 40%+ fills the gap. Thesis says this adds ~GBP 14.4M GP.
- **Evidencia en contra:**
  - Services is currently ~30% of GP = ~GBP 48M. Growing at 40% = +GBP 19.2M incremental GP.
  - Software is ~70% of GP = ~GBP 112M. If software GP declines even 5% (which H1 data suggests is happening), that is -GBP 5.6M.
  - Net effect: +GBP 13.6M. This WORKS mathematically for now.
  - BUT: 40% services growth is unsustainable. The company itself targets services reaching 20% of GP in 5 years (from ~15% of GP currently on a revenue basis). If they are targeting 20% in 5 years, the growth rate must decelerate substantially.
  - The company admitted the corporate sales restructuring "took longer than expected" to stabilize. Services growth depends on having the right specialized teams in place.
  - If services growth decelerates to 20% (still strong) and software margins continue to compress, the offset FAILS. The net GP growth would be low single digits, not the 8% the thesis assumes.
- **Severidad:** MODERATE
- **Resolution:** The offset works today but is fragile. The thesis assumes 40% services growth is the new normal rather than a catch-up effect from a low base. The more realistic medium-term scenario is services growth of 15-25% and software margin stability (not recovery). This points to 4-6% GP growth, not 8%.

### 4. "FV 455 GBp = 35% MoS" (Valuation is overly optimistic)

- **Thesis claim:** Weighted FV of 455p using OEY (470p, 60%) and DCF (432p, 40%).
- **Evidencia en contra:**
  - The OEY method calculates Owner Earnings at GBP 44.7M. But this uses TTM FCF from FY2025 -- before the margin compression hit. H1 FY2026 shows OP down 7%. Normalizing for the new margin structure, OE is more like GBP 38-42M.
  - The thesis uses 8% GP growth for the OEY method. With my adjusted growth estimate (4-6%), the OEY target return changes materially.
  - The DCF uses growth 8%, WACC 9%, terminal 2.5%. A more adversarial set of parameters (growth 4%, WACC 10.5%, terminal 2%) gives a base case FV of ~330p and bear case of ~280p.
  - Analyst consensus: Berenberg target 390p, Jefferies 400p. Consensus average ~461p. But the two most recent analyst actions (Berenberg, Jefferies) were DOWNGRADES. The 461p consensus includes stale, pre-profit-warning estimates.
  - My independent DCF scenarios:
    - Bear (growth 3%, WACC 11%, terminal 1.5%): Bear case 278p, Base 330p
    - Moderate Bear (growth 4%, WACC 11%, terminal 2%): Bear case 298p, Base 356p
  - At current price 307p, MoS vs my bear base case (330p) is only 7.5%. MoS vs my bear-bear case (298p) is NEGATIVE.
  - Softcat comparison: SCT.L trades at 17.7x P/E (down from 25x) -- meaning Softcat ALSO re-rated lower. The thesis claimed "Softcat at 25x vs BYIT at 14x is excessive gap" but Softcat is now at 17.7x, narrowing the gap substantially. The remaining gap (17.7x vs 14.6x) may be justified by Softcat's larger scale, better ROIC (36% vs 25%), and greater diversification.
- **Severidad:** HIGH
- **Resolution:** Fair value range is more realistically 330-400p, not 455p. At 307p, MoS is 7-23%, not 35%. The thesis FV is inflated by ~15-30%.

### 5. "-47% from highs is overreaction"

- **Thesis claim:** The market is over-punishing BYIT for what is a temporary margin trough.
- **Evidencia en contra:**
  - The stock was at 563p at its 52-week high. At that level, it traded at ~27x earnings. For a company growing GP at 10-12%, 27x was arguably already generous.
  - The current 14.6x P/E reflects 4-8% GP growth with margin compression. If growth normalizes to 8%, the stock deserves perhaps 17-19x (in line with Softcat's current 17.7x, adjusted for smaller scale). At 19x on current EPS of ~21p, that is ~400p. At 17x, that is ~357p.
  - The "overreaction" narrative implies a return to 25x+ multiples. But the market environment has changed: higher interest rates, Softcat itself has de-rated from 25x to 17.7x, and Microsoft's structural channel changes mean the business model's quality has been permanently slightly impaired.
  - The stock has continued to decline AFTER the thesis was written, hitting 291p on Feb 4 2026 (new 52-week low). The market may know something the thesis does not.
- **Severidad:** MODERATE
- **Resolution:** Some of the -47% is overreaction, but not all. A fair multiple is 16-19x, not 25x. The thesis implicitly assumes re-rating back to 20-22x (the 455p FV on ~21-23p EPS implies 20-22x). This may be optimistic given the structural headwinds.

---

## Desafios por Categoria

### Negocio

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | ROIC spread 4.9pp is lowest of any Tier A | AUTO.L 38pp, MONY.L 20pp, LULU 25%+. BYIT barely qualifies. | MODERATE |
| 2 | Microsoft EA going direct = permanent revenue loss for LSPs | Microsoft paid $2.5B to LSPs in 2023, projected ZERO in 2026. 100% commission loss on EA channel. | HIGH |
| 3 | Corporate sales restructuring taking longer than expected | Company admitted in AGM update and H1 results. Berenberg says not limited to H1. | MODERATE |
| 4 | 40% services growth unsustainable | Company targets services at 20% of GP in 5 years. Current growth rate must decelerate materially. | MODERATE |
| 5 | CEO governance scandal (Neil Murphy, 119 unauthorized trades) | Former CEO resigned Feb 2024 over unauthorized share trading. FCA investigation (closed without sanctions). Thesis does NOT mention this at all. | MODERATE |
| 6 | New CEO Sam Mudd untested at public company CEO level | Previously MD of Phoenix Software (subsidiary). No track record as listed company CEO. Thesis incorrectly names CEO as "Sam Sheridan." | LOW |

### Valoracion

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 7 | FV 455p uses pre-compression earnings and optimistic growth | H1 OP down 7%. Using 4-6% growth vs 8%, FV range drops to 330-400p. | HIGH |
| 8 | Softcat gap has narrowed substantially | SCT.L now 17.7x (was 25x). Gap to BYIT's 14.6x is 3.1x, not 11x as thesis implied. | MODERATE |
| 9 | DCF terminal growth 2.5% aggressive for UK mid-cap IT reseller | UK GDP ~1.5-2%. IT grows faster than GDP but 2.5% terminal for a RESELLER (not a software creator) is generous. | LOW |

### Riesgos

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 10 | Insider ownership materially overstated | Thesis claims 9.6%. Independent research shows 0.5-1.5%. yfinance reports 9.56% which may include non-management blockholders. True executive/board insider ownership is very low. New CEO Sam Mudd bought only GBP 99K worth. | HIGH |
| 11 | Profit warning at AGM (July 2025) not adequately weighted | Stock fell 27% in one day. Thesis acknowledges H1 was weak but treats it as the trough. Berenberg says it is NOT. | MODERATE |
| 12 | UK public sector spending cuts are structural | IFS: unprotected spending (including IT administration) falls 1.3%/year real terms. Administration cuts of GBP 2B by 2028-29. Public sector is ~50% of BYIT revenue. | MODERATE |
| 13 | Share buyback GBP 25M may be value-destructive | Launched at ~390p. If fair value is 330-400p, buying back at top of range destroys value. Buyback signals management may not know intrinsic value. | LOW |
| 14 | No adversarial pipeline was run before purchase | Missing: moat_assessment, risk_assessment, valuation_report, counter_analysis, committee_decision. All bypassed. | HIGH |

### Timing

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 15 | Purchased at 296p but stock has since hit 291p (new 52w low) | Price has not stabilized. The market is still finding the floor. | LOW |
| 16 | Full year FY2026 results due ~May 2026 | If H2 disappoints (Berenberg thinks it will), another leg down is possible. The thesis assumes H2 recovery that may not materialize. | MODERATE |
| 17 | Microsoft FY27 incentive changes unknown | Microsoft changes partner programs annually (July). FY27 changes (July 2026) could bring further compression. No visibility. | MODERATE |

---

## Conflictos con Otros Analisis

**No independent analyses exist.** There is no moat_assessment.md, risk_assessment.md, or valuation_report.md to compare against. This is itself a process failure.

Key findings that independent agents would likely have caught:
1. The insider ownership error (9.6% vs <1.5%)
2. The Neil Murphy CEO scandal (not mentioned in thesis at all)
3. The Microsoft EA direct sales structural shift (thesis focuses only on CSP incentive changes)
4. The Berenberg downgrade reasoning (disruption not limited to H1)

---

## Scoring Each Bull Claim

| # | Bull Claim | Counter Strength (1-3) | Reasoning |
|---|-----------|----------------------|-----------|
| 1 | QS 81 Tier A Quality Compounder | 2 | ROIC spread lowest of any Tier A. OP declining. But FCF margin and net cash are genuinely good. Borderline Tier A. |
| 2 | Microsoft incentive changes cyclical, not structural | 3 | EA going 100% direct is PERMANENT. CSP thresholds eliminate sub-scale partners permanently. Not a cycle. |
| 3 | Services growth 40%+ offsets margin compression | 2 | Works today but 40% is unsustainable. Company targets 20% of GP in 5 years, implying deceleration. Offset becomes insufficient at 20% services growth. |
| 4 | FV 455 GBp = 35% MoS | 3 | Uses pre-compression earnings and 8% growth. Realistic FV 330-400p. MoS is 7-23%, not 35%. |
| 5 | -47% from highs is overreaction | 2 | Partially. But repricing from 27x to 14-18x is rational given structural headwinds. Full recovery to 25x unlikely. |
| 6 | AI is opportunity not threat | 1 | Fair point. AI does increase complexity. But this is speculative and the revenue impact is years away. Neutral. |
| 7 | 80%+ recurring revenue gives visibility | 2 | Recurring at SHRINKING margins. Visibility into declining profitability is not the same as visibility into growth. |
| 8 | Softcat at 25x vs BYIT at 14x excessive gap | 2 | Softcat now at 17.7x, not 25x. Gap narrowed. Remaining gap may be justified by Softcat's scale and better ROIC. |
| 9 | Public sector will recover | 2 | IFS says administration spending cut 1.3%/year real terms. National Cyber Strategy provides floor but no recovery. |
| 10 | 9.6% insider ownership = aligned | 3 | Factually incorrect. Actual executive/board insider ownership is 0.5-1.5%. Former CEO forced out over unauthorized trading. New CEO invested only GBP 99K. |

**Total Score: 22/30 = 17.6/24 equivalent**

---

## Devil's Advocate Bear Valuation

### Method 1: Conservative EV/EBIT

- EBIT (H1 annualized, reflecting new margin structure): ~GBP 62M (using thesis figure; but if H2 is also weak per Berenberg, could be GBP 58-60M)
- Multiple: 12x (discount to Softcat's ~15x EV/EBIT, premium to Computacenter's ~12x, but appropriate given margin uncertainty)
- EV = 12 x 60M = GBP 720M
- Plus net cash: +GBP 40M
- Equity = GBP 760M
- Per share = 760M / 237M = **321p**

### Method 2: Adversarial DCF

- Growth: 4% (GP growth, not the 8% thesis assumes)
- WACC: 10.5% (thesis uses 9%; add 1.5pp for execution risk + Microsoft structural risk)
- Terminal: 2.0%
- Bear-Base from DCF tool: **~330p**

### Method 3: P/E Multiple on Depressed Earnings

- FY2026E EPS: ~21p (flat to slightly down from FY2025's 22.8p due to margin compression)
- Fair multiple: 15-17x (peer range: Softcat 17.7x, Computacenter 20.7x; BYIT deserves discount for smaller scale and margin headwinds)
- FV range: 315-357p
- Midpoint: **336p**

### Weighted Adversarial Fair Value

| Method | FV | Weight |
|--------|-----|--------|
| Conservative EV/EBIT | 321p | 30% |
| Adversarial DCF | 330p | 40% |
| P/E Multiple | 336p | 30% |
| **Weighted** | **330p** | **100%** |

At current price 307p, adversarial MoS = (330 - 307) / 330 = **7.0%**

This is dramatically below the thesis claim of 35% MoS.

---

## Case for SELL (1 Paragraph)

Bytes Technology is a decent business bought on a flawed thesis. The "35% MoS" claimed rests on inflated fair value (455p) derived from pre-compression earnings and optimistic 8% growth that neither Berenberg nor Jefferies believes. The 9.6% insider ownership that helped justify the Tier A quality score is factually wrong -- actual insider ownership is under 1.5%, the former CEO was fired for unauthorized trading, and the new CEO has invested a negligible GBP 99K. Microsoft's structural shift to direct EA sales is not "cyclical" -- it is permanent, and the thesis completely misses this larger threat. At a realistic FV of 330p, MoS is 7%, not 35%. With FY2026 results approaching in May and Berenberg warning that disruption extends beyond H1, the risk/reward is asymmetric to the downside. Every euro in this position could instead be in MONY.L (QS 81, genuine ROIC spread, net cash, 7% yield) or AUTO.L (QS 79, monopoly, 50% FCF margin). The position was bought without any adversarial scrutiny and the analysis has not survived it.

---

## Veredicto Global

| Metric | Valor |
|--------|-------|
| Desafios totales | 17 |
| Desafios HIGH/CRITICAL | 5 of 17 (29%) |
| Desafios no resueltos por thesis | 8 of 17 |
| Factual errors in thesis | 2 (insider ownership, CEO name) |
| Process failures | 1 (no adversarial pipeline) |
| Thesis FV vs Adversarial FV | 455p vs 330p (-27.5%) |
| Thesis MoS vs Adversarial MoS | 35% vs 7% |
| Bull claim score | 22/30 = 17.6/24 |
| **Veredicto** | **STRONG COUNTER** |

### Interpretacion:

**STRONG COUNTER** -- The thesis has serious problems:

1. **Factual error:** Insider ownership overstated by ~7x. CEO name wrong (Sheridan vs Mudd).
2. **Material omission:** Neil Murphy CEO scandal not mentioned. Microsoft EA direct sales structural shift not mentioned.
3. **Valuation inflation:** FV overstated by ~27%. MoS shrinks from 35% to 7% under adversarial assumptions.
4. **Process failure:** No independent agents reviewed this before purchase.
5. **Multiple sell-side downgrades:** Berenberg (Buy to Hold, TP 660p to 390p), Jefferies (Hold, TP 447p to 400p). Consensus is HOLD, not BUY.

**However, mitigating factors exist:**
- Position is small (3.5%, ~EUR 377). Absolute risk is limited.
- The business IS genuinely decent (net cash, 30% FCF margin, UK #1/2 VAR).
- Even adversarial FV (330p) is above current price (307p), so the stock is not OVERVALUED.
- The 0/10 value trap score in the thesis is probably correct -- this is not a value trap, just an overpaid entry.

---

## Recomendacion al Investment Committee

1. **DO NOT ADD at current levels.** The ADD trigger of 260p in the thesis is too high given the adversarial FV of 330p. A more appropriate ADD trigger would be 250p (MoS ~24% vs adversarial FV).

2. **HOLD on PROBATION with LOW conviction.** The position is small and the business is real. But the thesis needs to be rewritten with correct facts and stress-tested assumptions. Set a deadline: if FY2026 full-year results (May 2026) show continued OP decline, EXIT.

3. **Require full adversarial pipeline before any ADD.** If the stock reaches 250p and we consider adding, run the full 4-round buy-pipeline first.

4. **Correct the thesis facts immediately:**
   - Insider ownership: 0.5-1.5%, not 9.6%
   - CEO: Sam Mudd, not Sam Sheridan
   - Add Neil Murphy governance scandal history
   - Add Microsoft EA direct sales structural shift
   - Revise FV to 330-400p range
   - Revise MoS to 7-23%

5. **Key catalyst to monitor:** FY2026 Full Year Results (~May 2026). If H2 OP growth does not materialize and full-year OP declines >5%, the quality compounder thesis is invalidated. EXIT at that point.

---

## 🔄 META-REFLECTION

### Dudas/Incertidumbres
- The yfinance "9.6% insider ownership" figure vs Simply Wall St's "0.5-1.5%" represents a genuine data discrepancy I could not fully resolve. yfinance may be including non-executive blockholders (possibly Altron-related entities from the company's South African heritage) that are classified as "insiders" in some databases but are not management insiders in the meaningful sense. This should be resolved by reading the company's annual report directly.
- I could not access the Bytes Technology H1 FY2026 earnings call transcript or Berenberg's full research note due to access restrictions. My analysis of their views is based on secondary reporting.
- The Microsoft EA direct sales shift is well-documented for the US market. I am less certain about its specific impact on UK public sector (which was noted as "unaffected" in one source). If UK public sector EA revenue is exempt, the impact on Bytes is reduced since public sector is ~50% of their business.

### Limitaciones de Este Analisis
- Could not read the actual H1 FY2026 earnings call transcript (paywall)
- Could not access Berenberg's full research note
- Limited visibility into Bytes' specific customer-level data and Microsoft incentive economics
- The quality scorer tool's insider ownership data may be stale or definitionally inconsistent

### Sugerencias para el Sistema
1. **Quality scorer should flag when insider ownership data may be unreliable** -- the tool awarded 5/5 for insider ownership based on yfinance data without cross-referencing. For UK-listed companies with complex ownership structures, this can be misleading.
2. **The adversarial pipeline MUST be enforced before any purchase.** This position demonstrates exactly why -- multiple material issues were missed that independent agents would have caught.
3. **Thesis should be required to name the CEO correctly and include governance history.** A basic fact check would have caught both the CEO name error and the Neil Murphy scandal.

### Preguntas para Orchestrator
1. Should the thesis FV be immediately revised downward to 330-400p to reflect adversarial findings, or should we wait for FY2026 results?
2. Given that this is a STRONG COUNTER with 5 HIGH challenges, does the committee want to consider EXIT given the small position size (EUR 377) and low conviction?
3. The quality_scorer.py tool pulls insider ownership from yfinance. Should we add a cross-reference check or manual override for this metric?

---

**Sources:**

- [Jefferies Downgrades BYIT to Hold (Jan 2026)](https://www.marketbeat.com/instant-alerts/jefferies-financial-group-downgrades-bytes-technology-group-lonbyit-to-hold-2026-01-15/)
- [Berenberg Downgrades BYIT on Weak Growth Outlook](https://www.investing.com/news/analyst-ratings/berenberg-downgrades-bytes-technology-group-stock-on-weak-growth-outlook-93CH-4122179)
- [BYIT Shares Plunge 25% on Weaker Outlook](https://www.investing.com/news/stock-market-news/bytes-technology-shares-plunge-25-on-weaker-outlook-and-sales-shift-4120560)
- [BYIT H1 FY2026 Earnings Call Highlights - GuruFocus](https://www.gurufocus.com/news/3144722/bytes-technology-group-plc-byity-half-year-2026-earnings-call-highlights-strong-revenue-growth-amid-profitability-challenges)
- [Microsoft LSPs Lose EA Revenue - US Cloud](https://www.uscloud.com/blog/microsoft-licensing-solution-providers-lsp-lose-enterprise-agreement-ea-revenue/)
- [Microsoft LSP Changes 2024: 65% of Partners Won't Survive](https://www.uscloud.com/blog/microsoft-lsp-changes-2024/)
- [UK's Top Resellers in Oxygen 250 2026](https://itchanneloxygen.com/uks-top-resellers-and-msps-revealed-in-oxygen-250-2026/)
- [Bytes and Softcat Dominate Public Sector VAR Market](https://itchanneloxygen.com/bytes-and-softcat-dominate-3-7bn-public-sector-var-market/)
- [IFS: Planned Cuts to Administration Budgets](https://ifs.org.uk/articles/how-could-planned-cuts-administration-budgets-affect-public-sector-productivity)
- [Former Bytes CEO Neil Murphy - FCA Closes Enquiry](https://itchanneloxygen.com/former-bytes-ceo-neil-murphy-thankful-as-fca-closes-enquiry/)
- [Bytes CEO Neil Murphy Resigns Over Unauthorized Trades](https://itchanneloxygen.com/bytes-shares-slump-as-ceo-neil-murphy-resigns/)
- [Bytes Investigation Clears Former CEO of Misconduct](https://www.marketscreener.com/quote/stock/BYTES-TECHNOLOGY-GROUP-PL-116485507/news/Bytes-Technology-probe-clears-former-CEO-of-misconduct-in-share-trade-46750322/)
- [Bytes Launches GBP 25M Share Buyback Programme](https://www.tipranks.com/news/company-announcements/bytes-technology-group-launches-25-million-share-repurchase-programme)
- [Softcat vs Bytes vs Computacenter - Proactive Investors](https://www.proactiveinvestors.com/companies/news/1027149/bytes-computacenter-softcat-which-is-the-uk-s-top-value-added-reseller-1027149.html)
- [Microsoft CSP 2026 Program Changes](https://cspcontrolcenter.com/microsoft-csp-2026-program-changes/)
- [Microsoft Enterprise Agreement Explained 2026](https://samexpert.com/what-is-a-microsoft-enterprise-agreement/)
- [Institute for Government: Impact of Budget on Public Services](https://www.instituteforgovernment.org.uk/publication/impact-labour-first-budget-public-services)
