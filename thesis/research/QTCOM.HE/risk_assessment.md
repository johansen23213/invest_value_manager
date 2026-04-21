# Risk Assessment: QTCOM.HE (Qt Group Oyj)

## Fecha: 2026-02-18

## Risk Score: HIGH

---

## Context

Qt Group Oyj is a Finnish developer tools company providing a cross-platform application framework (Qt) and embedded development tools (IAR Systems, acquired Q3 2025). The stock has collapsed from EUR 92.10 (52wH) to EUR 25.06, a decline of approximately 73%. FY2025 results publish **February 26, 2026** -- 8 days away.

No thesis exists yet for QTCOM.HE; this is an independent risk assessment for R1 of the buy-pipeline.

---

## Matriz de Riesgos

| # | Categoria | Riesgo | Probabilidad | Impacto | Score | Mitigante |
|---|-----------|--------|-------------|---------|-------|-----------|
| 1 | Fundamental | Revenue growth deceleration / customer purchasing behavior shift | Alta | Alto | CRITICAL | Long-term embedded market growth (~10% CAGR); IAR diversifies revenue |
| 2 | Fundamental | IAR Systems acquisition integration risk + dilution of margins | Media | Alto | HIGH | Management experienced; synergies in cross-selling; one-time costs isolatable |
| 3 | Fundamental | AI code generation disrupting developer tools market | Media | Medio | MEDIUM | Qt targets embedded/industrial (not web/mobile where AI coding strongest); C++ niche |
| 4 | Fundamental | Open-source fork risk / licensing controversy | Baja | Alto | MONITOR | KDE Foundation agreement provides fallback; community relations stabilized post-2021 |
| 5 | Fundamental | Customer concentration in automotive sector | Media | Medio | MEDIUM | Qt serves 70+ industries; automotive is significant but not majority |
| 6 | Fundamental | Competition from Flutter, Tauri, Electron in desktop/mobile | Media | Medio | MEDIUM | Qt dominates embedded/industrial niche; competitors focus mobile/web |
| 7 | Financiero | Small-cap volatility + Helsinki exchange liquidity risk | Alta | Medio | HIGH | Market cap EUR 636M; 29.5% insider ownership reduces free float further |
| 8 | Financiero | Profit margin compression (EBITA 10.5% Q3 vs 24.5% prior year) | Alta | Alto | CRITICAL | IAR one-time costs temporary; underlying margins recovering if deal sizes return |
| 9 | Financiero | FCF volatility (CV=1.7 per reverse DCF) | Media | Medio | MEDIUM | FCF trending positive (EUR 52M FY2024); subscription transition may smooth |
| 10 | Valoracion | Value trap -- cheap for structural reason | Media | Alto | HIGH | Stock at EUR 25 near 52wL; could be dead money if growth doesn't recover |
| 11 | Valoracion | Feb 26 earnings binary event | Alta | Alto | CRITICAL | Guidance already lowered twice; expectations may be reset low enough |
| 12 | Geopolitico | Finland/EU concentration; limited US market presence | Baja | Medio | LOW | EUR-denominated fits our portfolio; EU is stable jurisdiction |
| 13 | Regulatorio | EU CSRD compliance costs for small company | Baja | Bajo | LOW | Already reporting under SASB/CSRD since 2024 |
| 14 | ESG/Legal | Open-source community relations | Baja | Medio | LOW | Post-2021 tensions have moderated; KDE Foundation agreement in place |

### Scoring:
- Alta x Alto = CRITICAL
- Alta x Medio OR Media x Alto = HIGH
- Media x Medio = MEDIUM
- Baja x cualquiera OR cualquiera x Bajo = LOW

---

## Top 3 Riesgos Criticos

### 1. Revenue Growth Deceleration + Customer Purchasing Behavior Shift

- **Categoria:** Fundamental
- **Descripcion:** Qt Group issued TWO profit warnings in 2025. Initial 2025 guidance was 10-20% revenue growth with 30-40% EBITA margins. This was slashed to 3-10% revenue growth and 20-30% EBITA margins. Q3 2025 net sales declined 3.4% YoY (EUR 40.7M). Jan-Sep 2025 revenue was down 1.0% YoY. The cause: customers are reducing license counts, shifting from multi-year to one-year deals, and postponing larger deals worth several million euros. This is NOT a one-quarter blip -- it has persisted for 4+ quarters.
- **Evidencia:**
  - Q1 2025: Revenue growth slowed to 4.8%, margins contracted (Source: Investing.com Q1 2025 slides)
  - Q3 2025: Revenue -3.4% YoY; EBITA collapsed to EUR 4.3M (-58.5% YoY); EBITA margin 10.5% vs 24.5% prior year (Source: Q3 2025 earnings call transcript)
  - Two formal profit warnings issued (April 23 and October 2025) (Source: Qt.io stock releases)
  - CEO Juha Varelius: "Market softness in embedded, automotive, and consumer electronics segments expected to persist through Q4; no significant improvement expected"
- **Probabilidad:** Alta -- trend has persisted 4+ quarters with management acknowledging no near-term recovery
- **Impacto si materializa:** If revenue stagnates for 2+ years at current levels (~EUR 160-180M organic), margins compress to 15-20% EBITA, and the stock could trade at EUR 15-18 (30-40% further downside from current levels). At current P/E 15.2x on depressed earnings, there is no margin of safety if earnings don't recover.
- **Mitigante:** Embedded software market is growing structurally (~10% CAGR per management); IAR acquisition adds EUR 40-50M annual revenue; subscription model transition should reduce deal-size volatility over time. Management "expressed confidence in long-term growth prospects."
- **Kill condition?:** YES -- If FY2025 results (Feb 26) show Q4 revenue also declining YoY AND 2026 guidance below 5% organic growth, this suggests structural demand impairment rather than cyclical softness.

### 2. Profit Margin Compression -- Structural or Temporary?

- **Categoria:** Financiero
- **Descripcion:** Q3 2025 EBITA margin collapsed to 10.5% from 24.5% the prior year and 30.2% operating margin in FY2024. The company blames IAR integration one-time costs (EUR 6-7M impact on FY2025 EBITA) plus the revenue shortfall. However, the magnitude of margin compression raises the question: is the high-margin era (25-30% EBITA) over, or just temporarily depressed?
- **Evidencia:**
  - FY2024 operating margin: 30.2% (Source: narrative_checker.py data)
  - Q3 2025 EBITA margin: 10.5% (Source: Investing.com Q3 2025 earnings transcript)
  - IAR one-time costs: ~EUR 6-7M (Source: Qt.io profit warning)
  - EBIT fell 72.6% YoY to EUR 2.3M in Q3 2025
  - Net profit Q3: EUR 1.4M vs EUR 7.7M prior year
- **Probabilidad:** Alta for near-term (FY2025-H1 2026); Media for structural
- **Impacto si materializa:** If margins settle at 15-20% EBITA structurally (vs 25-30% historically), fair value drops significantly. At EUR 180M revenue x 17% EBITA margin = EUR 30.6M EBITA. At 15x EBITA multiple = EUR 459M EV = ~EUR 18/share (28% downside).
- **Mitigante:** FY2024 showed expanding margins (gross margin 44.7% -> 52.5% over 2021-2024; operating margin 23.8% -> 30.2%). The core business margin profile appears intact -- the compression is largely driven by (a) IAR one-time costs and (b) revenue shortfall creating operating deleverage. If revenue recovers, margins should recover.
- **Kill condition?:** YES -- If FY2026 organic EBITA margins (excluding IAR one-time costs) remain below 22%, this suggests structural margin impairment.

### 3. IAR Systems Acquisition -- Integration Execution + Timing Risk

- **Categoria:** Fundamental
- **Descripcion:** Qt Group completed the acquisition of IAR Systems Group in Q3 2025 during a period of organic revenue decline and market uncertainty. The acquisition adds complexity (new products, R&D teams, SaaS licensing transition for IAR), one-time costs (EUR 6-7M), and management distraction at a time when the core business needs attention. IAR's SaaS transformation plan won't be presented until Q1 2026 -- meaning investors are buying integration risk without visibility on the payoff.
- **Evidencia:**
  - Acquisition completed Q3 2025 at 94.49% of IAR shares (Source: Qt.io stock release)
  - One-time transaction costs: EUR 6-7M negative impact on FY2025 EBITA (Source: profit warning)
  - IAR expected to contribute EUR 8-10M to FY2025 net sales (Source: Investing.com)
  - SaaS transformation plan for IAR to be presented Q1 2026 (Source: management statement)
  - Q3 2025 was the worst quarter in years -- coinciding with acquisition close
- **Probabilidad:** Media -- acquisitions in embedded tools have reasonable synergy logic (Embedded Workbench + Qt UI framework); but execution during downturn is risky
- **Impacto si materializa:** If integration fails or SaaS conversion stalls, Qt has (a) paid acquisition premium for a declining-margin business, (b) diluted its own margin profile, (c) distracted management from core business recovery. Worst case: EUR 5-10/share value destruction.
- **Mitigante:** IAR's Embedded Workbench is a defensible product selected at start of dev projects (switching costs); combined platform creates comprehensive embedded offering; management has M&A experience (though this is their largest deal). Acquisition was all-cash (no equity dilution).
- **Kill condition?:** PARTIAL -- Monitor IAR revenue trajectory in FY2026. If IAR revenue declines post-acquisition while margins don't recover, reconsider thesis.

---

## Additional Risks (Ranked by Severity)

### 4. Small-Cap Liquidity + Volatility Risk (HIGH)

- **Categoria:** Financiero / Valoracion
- **Descripcion:** Market cap EUR 636M with 29.5% insider ownership = effective free float ~EUR 450M. Helsinki exchange small-caps are notably illiquid. Institutional holders are primarily passive index funds (Vanguard, iShares) with tiny positions (0.3-1.0% of shares outstanding). The stock declined 73% from 52wH to 52wL -- extreme volatility for a profitable business.
- **Probabilidad:** Alta (inherent structural feature)
- **Impacto:** Medio -- can amplify both upside and downside; may prevent timely exit
- **Mitigante:** eToro may have limited coverage of Helsinki small-caps; need to verify tradability. Our position sizing at ~EUR 400-600 is tiny relative to even this small float.

### 5. Value Trap / Dead Money Risk (HIGH)

- **Categoria:** Valoracion
- **Descripcion:** The reverse DCF implies the market is pricing in -6.6% FCF decline per year -- extreme pessimism given historical 52% FCF CAGR and 20% revenue CAGR. However, the market MAY be correct that the high-growth era is over and Qt is now a low-single-digit grower with margin compression. At P/E 15.2x on depressed earnings, the stock is not obviously cheap if growth doesn't recover.
- **Evidencia:**
  - Reverse DCF implied growth: -6.6%/yr (Source: dcf_calculator.py)
  - Historical revenue CAGR: 19.9%; FCF CAGR: 51.7% (Source: dcf_calculator.py)
  - Analyst consensus: Mean target EUR 35.50 (range EUR 29-42), +41.7% from current (Source: insider_tracker.py). Only 4 analysts cover the stock.
  - Stock near 52-week low of EUR 24.24 (currently EUR 25.06)
- **Probabilidad:** Media -- depends entirely on Feb 26 earnings and 2026 guidance
- **Impacto:** Alto -- if growth doesn't recover, stock could languish at EUR 20-30 for years

### 6. AI Code Generation Disrupting Developer Tools (MEDIUM)

- **Categoria:** Fundamental
- **Descripcion:** 65% of developers now use AI coding tools weekly (Stack Overflow 2025). AI coding tools are commoditizing simple coding tasks. The question is whether Qt's cross-platform UI framework and embedded tooling face disruption from AI that can generate equivalent code directly.
- **Assessment:** Qt's core value proposition (cross-platform UI for embedded/industrial/automotive with C++ performance) is NOT the same as "write me a web app." AI code generators are strongest at web/mobile development (JavaScript, Python) and weakest at embedded systems, real-time OS integration, and hardware-level C++ -- exactly where Qt lives. The disruption risk is REAL but distant for Qt's specific niche.
- **Probabilidad:** Media (long-term, 3-5 years)
- **Impacto:** Medio -- gradual erosion more likely than sudden disruption
- **Mitigante:** Qt's moat is in the runtime/framework layer, not in coding convenience. AI helps developers write Qt code faster, which could INCREASE Qt adoption.

### 7. Competition from Flutter/React Native/Tauri (MEDIUM)

- **Categoria:** Fundamental
- **Descripcion:** Flutter (46% cross-platform market share) and React Native (35%) dominate mobile/web. Tauri (lightweight Rust-based) is growing 35% YoY and challenging Electron for desktop. Qt is increasingly positioned as a niche player in embedded/industrial.
- **Assessment:** Qt and Flutter/React Native serve different primary markets. Flutter/RN dominate mobile apps; Qt dominates embedded HMI/industrial. Tauri threatens Electron (not Qt) for desktop. However, if Qt's embedded market doesn't recover, the niche positioning becomes a liability.
- **Probabilidad:** Media
- **Impacto:** Medio
- **Mitigante:** Qt has 30 years of embedded expertise; 1.5M developer base; products used by 70+ industries.

### 8. Open-Source Fork Risk (MONITOR)

- **Categoria:** Fundamental / Regulatorio
- **Descripcion:** Qt changed LTS licensing in 2020 to commercial-only, causing community backlash. KDE and other open-source projects depend on Qt. A fork (like happened with OpenOffice -> LibreOffice) could undermine Qt's commercial moat.
- **Assessment:** The 2020-2021 controversy has largely settled. KDE Foundation has contractual protections ensuring Qt remains available under open-source license. A fork would be costly and fragmenting for the community. But the RISK of aggressive monetization strategies pushing users to fork persists latently.
- **Probabilidad:** Baja
- **Impacto:** Alto (a successful fork would destroy the dual-licensing business model)
- **Mitigante:** KDE Foundation agreement; community relations have improved; the commercial/open-source balance has stabilized.

### 9. Automotive Sector Cyclical Exposure (MEDIUM)

- **Categoria:** Fundamental / Geopolitico
- **Descripcion:** Qt has significant automotive exposure (dashboard HMI, infotainment). The auto sector is under pressure from trade tensions, EV transition uncertainty, and Chinese competition. Management explicitly cited automotive weakness in profit warning.
- **Probabilidad:** Alta (auto sector IS weak)
- **Impacto:** Medio -- automotive is one of several verticals, not the majority
- **Mitigante:** Software-defined vehicle trend is structural tailwind; Qt serves the UI layer regardless of powertrain type.

---

## Riesgos NO Mencionados en Thesis

No thesis exists yet for QTCOM.HE. These are risks that any future thesis MUST address:

| Riesgo | Severidad | Mencionado en thesis? | Comentario |
|--------|-----------|----------------------|------------|
| Two profit warnings in 2025 | HIGH | N/A (no thesis) | Core business revenue declining while management promised growth |
| IAR integration during downturn | HIGH | N/A | Worst timing for largest-ever acquisition |
| EBITA margin collapse to 10.5% | HIGH | N/A | Even excluding one-time costs, organic margins compressed |
| Feb 26 earnings binary event | HIGH | N/A | FY2025 results + 2026 guidance in 8 days |
| Helsinki small-cap liquidity | MEDIUM | N/A | Limited institutional coverage; 4 analysts only |
| Customer shift from multi-year to 1-year deals | HIGH | N/A | Reduces revenue visibility and predictability |
| Subscription model transition risk for IAR | MEDIUM | N/A | SaaS transformation plan not yet disclosed |
| AI code generation medium-term threat | MEDIUM | N/A | Not immediate but requires monitoring |
| 73% stock decline may reflect structural problems | HIGH | N/A | Market may know something the thesis doesn't |

---

## Kill Conditions Sugeridas

Based on my findings, the following kill conditions should be part of any thesis:

1. **KC#1: Revenue stagnation** -- If FY2025 organic revenue (ex-IAR) declines YoY AND 2026 organic guidance is below 5%, the growth thesis is broken.
2. **KC#2: Margin structural impairment** -- If FY2026 organic EBITA margin (excluding IAR one-time costs) remains below 22%, the high-margin developer tools model is impaired.
3. **KC#3: IAR integration failure** -- If IAR revenue declines post-acquisition or SaaS conversion timeline extends beyond 2027, acquisition value is questionable.
4. **KC#4: Customer deal size continued decline** -- If average deal size continues shrinking through H1 2026, the "cyclical softness" narrative becomes structural.
5. **KC#5: Open-source fork** -- If KDE or major projects announce a Qt fork initiative, the dual-licensing moat is under direct attack.
6. **KC#6: Insider selling** -- If insiders (currently 29.5% ownership) begin material selling post-earnings, it signals loss of confidence.

---

## Riesgo Agregado

- **Numero de riesgos HIGH+CRITICAL:** 5 (revenue deceleration CRITICAL, margin compression CRITICAL, Feb 26 binary event CRITICAL, IAR integration HIGH, value trap HIGH)
- **Riesgos correlacionados?** SI -- Revenue deceleration, margin compression, and value trap risk are ALL correlated. If revenue doesn't recover, margins stay compressed, and the stock remains a value trap. The IAR acquisition amplifies all three (higher costs during lower revenue).
- **Risk Score Final: HIGH**

The score is HIGH rather than VERY HIGH because:
1. The balance sheet is clean (net cash EUR 87M, interest coverage 252x)
2. The core business has strong fundamentals when demand normalizes (43% ROIC, expanding gross margins over 4 years)
3. Insider ownership at 29.5% aligns management with shareholders
4. The embedded software market has structural tailwinds (IoT, SDV, Industry 4.0)

But the near-term risks are severe: two profit warnings, margin collapse, largest acquisition during worst quarter, and FY2025 earnings in 8 days. **The Feb 26 report will be make-or-break for any investment thesis.**

---

## Quantitative Data Summary (Tool Outputs)

### Quality Score
- **QS Tool: 80/100 (Tier A)** -- BUT this is based on FY2024 data, BEFORE the 2025 deterioration
- ROIC: 43.3% (FY2024), WACC: 13.0%, spread +30.3pp
- Gross margin trajectory: 44.7% -> 48.7% -> 50.5% -> 52.5% (expanding)
- FCF margin: 12.4% -> -3.3% -> 21.7% -> 25.1% (volatile but improving)
- Net cash position: EUR 87M (debt only EUR 7M)
- **WARNING:** QS 80 reflects the GOOD years. Q3 2025 margins (10.5% EBITA) would produce a materially lower QS if annualized.

### Valuation Context
- Price: EUR 25.06 | 52wH: EUR 92.10 | 52wL: EUR 24.24
- P/E: 15.2x (on FY2024 EPS EUR 2.26 -- but FY2025 EPS will be MUCH lower)
- Market cap: EUR 636M | EV: ~EUR 549M (net cash)
- Reverse DCF implied growth: -6.6%/yr (extreme pessimism vs 20% historical revenue CAGR)
- Analyst targets: EUR 29-42 (mean EUR 35.50, +41.7%) -- only 4 analysts cover

### Insider/Institutional Data
- Insider ownership: 29.5% (high -- positive signal)
- Institutional: 43.2% (mostly passive ETFs: Vanguard, iShares, DFA)
- Recent insider activity: Net buyers in past 3 months (per Simply Wall St)
- CFO Jouni Lintunen had a share disposal in March 2025 (size unknown)
- Short interest data: Not available for Helsinki exchange

### Narrative Checker Highlights
- Revenue growth decelerating: 28.2% -> 16.4% -> 15.7% (FY2022-2024)
- Receivables growth (13.5%) tracking below revenue growth (15.7%) -- POSITIVE (no revenue quality concern)
- Goodwill declining: 24.4% -> 21.5% -> 18.6% of total assets (POSITIVE -- before IAR acquisition adds goodwill)
- SBC data unreliable (N/A or negative readings -- likely data quality issue for Finnish small-cap)
- Capex/Depreciation at 0.1x -- very asset-light model

---

## 🔄 META-REFLECTION

### Dudas/Incertidumbres
- **Q4 2025 and FY2025 full-year numbers are NOT yet available** (publish Feb 26). My assessment is based on Q1-Q3 2025 data. The Q4 number could change the picture materially in either direction.
- **IAR Systems financials pre-acquisition** -- I could not access detailed IAR standalone financials to assess what Qt actually bought. The EUR 8-10M revenue contribution in FY2025 seems small for an acquisition that triggered EUR 6-7M in one-time costs.
- **Customer concentration data is NOT disclosed** -- Qt says "70+ industries" but doesn't break down revenue by sector. Automotive exposure could be 20% or 40% -- I cannot quantify.
- **Short interest data unavailable** for Helsinki exchange small-caps. I cannot assess short squeeze risk or bearish positioning.
- **The P/E of 15.2x is misleading** -- it uses FY2024 EPS. FY2025 EPS will be materially lower given Q1-Q3 performance. The true forward P/E on FY2025E earnings is likely 25-40x, which changes the valuation picture dramatically.

### Riesgos que Podrian Estar Subestimados
- **Revenue stagnation risk (currently CRITICAL but may be worse):** Two profit warnings suggest management was consistently over-optimistic about demand recovery. If this pattern continues in 2026 guidance, the "cyclical" narrative may be wrong -- it could be structural.
- **AI disruption (currently MEDIUM):** I classified this as medium because Qt targets embedded (not web). But "vibe coding" and AI-native development practices are advancing fast. If AI reduces the need for UI frameworks altogether by generating native code directly, Qt's entire value proposition weakens. This is a 3-5 year risk that I may be underweighting.
- **Free float liquidity (currently HIGH):** With 29.5% insider ownership and 43.2% institutional (mostly passive), the actively traded float may be as low as EUR 150-200M. At current volumes, exiting even a EUR 500 position could take days in a panic scenario.

### Discrepancias con Thesis
- No thesis exists yet. My key warning for the fundamental-analyst: the QS of 80 (Tier A) based on FY2024 data is STALE. The 2025 operational deterioration has not been captured. Any thesis must use a forward-looking adjusted QS that reflects the 2025 margin collapse.

### Sugerencias para el Sistema
- **Helsinki small-cap data gaps:** Our tools (insider_tracker.py, quality_scorer.py) have limited data for Finnish small-caps. Short interest, SBC data, and insider transaction details were all unavailable or unreliable. Consider flagging Nordic small-caps as having "data quality risk" in future assessments.
- **Binary earnings event proximity:** QTCOM.HE reports Feb 26 -- just 8 days away. Any buy decision should WAIT for this report unless the thesis has explicit pre-earnings entry justification with a framework (bear/base/bull scenarios).

### Preguntas para Orchestrator
1. Is QTCOM.HE even tradeable on eToro? Helsinki small-caps may not be available. This should be verified before any further pipeline work.
2. Given FY2025 results publish Feb 26, should the fundamental-analyst WAIT for those results before completing the thesis, or proceed with current (incomplete) data?
3. The QS of 80 is based on FY2024 data that is now stale. Should the fundamental-analyst be explicitly instructed to calculate a forward-looking adjusted QS based on 2025 estimated earnings?
4. The 73% stock decline from 52wH is extreme for a company with net cash and positive FCF. Should the devil's-advocate specifically challenge whether the market is correct to price in terminal decline?

---

## Sources

### Qt Group Financial Data & Earnings
- [Qt Group: Profit Warning October 2025](https://www.qt.io/stock/inside-information-profit-warning-qt-group-lowers-its-outlook-for-2025-1760683200000-3671125)
- [Qt Group: Profit Warning April 2025](https://www.qt.io/stock/inside-information-profit-warning-qt-group-lowers-its-net-sales-outlook-for-2025-operating-profit-margin-outlook-unchanged-1745407500000-3576788)
- [Investing.com: Q3 2025 Earnings Call Transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-qt-groups-q3-2025-reveals-sales-decline-stock-dips-93CH-4320993)
- [Investing.com: Q3 2025 Slides Summary](https://www.investing.com/news/company-news/qt-group-q3-2025-slides-sales-decline-amid-market-challenges-iar-acquisition-completed-93CH-4321097)
- [Investing.com: Q1 2025 Slides](https://www.investing.com/news/company-news/qt-group-q1-2025-slides-growth-slows-to-48-profit-margins-contract-93CH-4000495)
- [Simply Wall St: QTCOM Analysis](https://simplywall.st/stocks/fi/software/hel-qtcom/qt-group-oyj-shares)
- [TradingView: FY2025 Results Date Feb 26](https://www.tradingview.com/news/modular_finance:6402a89b6be4b:0-publishing-qt-group-s-financial-statements-bulletin-on-february-26-2026/)

### IAR Systems Acquisition
- [Qt Group: IAR Acquisition Offer](https://www.qt.io/stock/inside-information-qts-recommended-public-cash-offer-for-iar-systems-group-1751607060000-3623512)
- [Qt Group: IAR Acquisition Completed](https://www.qt.io/stock/qt-completes-the-recommended-public-cash-offer-to-the-shareholders-of-iar-systems-group-1760351460000-3668995)
- [ainvest.com: Qt Group's Bid for IAR Systems](https://www.ainvest.com/news/qt-group-bid-iar-systems-premium-play-embedded-software-synergies-2507/)
- [MarketScreener: Qt Group Profit Warning Following IAR](https://www.marketscreener.com/news/qt-group-issues-profit-warning-for-2025-following-iar-systems-acquisition-ce7d5adcd081fe22)

### Open-Source Licensing
- [The Register: Qt LTS Goes Commercial-Only (2021)](https://www.theregister.com/2021/01/05/qt_lts_goes_commercial_only/)
- [Slashdot: Open Source Advocates Hope They Don't Have to Fork Qt](https://news.slashdot.org/story/20/04/12/1940232/open-source-advocates-hope-they-dont-have-to-fork-qt)
- [ifrOSS: Qt, KDE and Licensing](https://www.ifross.org/artikel/qt-kde-and-corona-maybe-ensuring-continued-development-and-availability-under-free-and-open-)

### Competition & AI Disruption
- [MIT Technology Review: Rise of AI Coding](https://www.technologyreview.com/2025/12/15/1128352/rise-of-ai-coding-developers-2026/)
- [MIT Technology Review: Generative Coding Breakthrough 2026](https://www.technologyreview.com/2026/01/12/1130027/generative-coding-ai-software-2026-breakthrough-technology/)
- [SomcoSoftware: Flutter vs React Native vs Qt](https://somcosoftware.com/en/blog/flutter-vs-react-native-vs-qt)
- [SoftwareLogic: Qt vs Electron vs Tauri 2025](https://softwarelogic.co/en/blog/migration-secrets-choosing-qt-electron-or-tauri-for-desktop-apps-2025)

### Analyst Coverage
- [StocksGuide: Qt Group Stock Forecast 2026](https://stocksguide.com/en/forecast/Qt-Group-FI4000198031)
- [Inderes: Qt Group](https://www.inderes.fi/en/companies/Qt-Group)

### Insider & Market Data
- [Yahoo Finance: Qt Group Insider Transactions](https://finance.yahoo.com/quote/2QT.F/insider-transactions/)
- [Yahoo Finance: European Undervalued Small Caps With Insider Action Jan 2026](https://finance.yahoo.com/news/european-undervalued-small-caps-insider-053938968.html)
