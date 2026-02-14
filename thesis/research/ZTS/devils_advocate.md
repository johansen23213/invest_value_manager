# Counter-Analysis: ZTS (Zoetis Inc.)

## Fecha: 2026-02-13

> **ALERT: No CRITICAL challenges that invalidate the thesis outright, but STRONG COUNTER due to accumulation of HIGH-severity issues that collectively undermine the valuation and timing assumptions.**

## Resumen Ejecutivo

The ZTS thesis presents a textbook quality compounder narrative: #1 market position, 30% ROIC, 70%+ gross margins, secular pet humanization tailwind. The fundamentals are genuinely strong. However, the thesis systematically underweights four converging headwinds that together challenge the $140 fair value: (1) Librela's safety crisis is deeper and more scientifically grounded than the thesis acknowledges, with peer-reviewed evidence of 9x higher musculoskeletal adverse events and an accelerating decline (-32% US Q4); (2) Apoquel patent expiry in November 2026 threatens the $1.3B dermatology franchise sooner than the thesis implies; (3) the QS adjustment from 73 to 78 is partially justified but overreaches; and (4) the "quality compounder premium" added to the weighted valuation average ($119 to $140) lacks rigorous justification. After adversarial correction, fair value drops to $115-125, which means at $125.64, the stock offers essentially zero margin of safety. The thesis's entry target of $110-115 is reasonable, but the base FV of $140 is optimistic.

---

## Asunciones Clave Desafiadas

### 1. "Librela headwinds are temporary" -- FV $140 assumes mAb franchise recovers

- **Evidencia en contra:**
  - **Peer-reviewed Frontiers in Veterinary Science study (May 2025):** Musculoskeletal adverse event reports in Librela-treated dogs are approximately **9 times higher** than the combined total of six comparator OA drugs (carprofen, meloxicam, firocoxib, robenacoxib, enflicoxib, grapiprant). This is not anecdotal -- it is a specialist-led disproportionality analysis from the EMA's EudraVigilance database.
  - **Expert panel unanimously concluded "strong suspicion of causal association"** between bedinvetmab and accelerated joint destruction -- the very condition it is supposed to treat.
  - **US Librela revenue declined 32% in Q4 2025** ($36M quarterly), with full-year US decline of 16%. This is accelerating, not stabilizing.
  - **FDA found Zoetis's YouTube marketing made "false or misleading claims"** about Librela/Solensia safety (February 2025 warning).
  - **Consumer advocacy site (stopzoetis.org)** has emerged, creating persistent negative sentiment among pet owners.
  - **825+ dog death reports** to FDA between May 2023 and June 2024 alone. Cumulative reports are likely much higher by 2026.
  - **70% of adverse events occur after the first dose**, making this particularly frightening for new adopters.
  - The thesis dismisses Librela as "6% of revenue" but ignores: (a) it represents Zoetis's primary GROWTH vector in pain management; (b) if the mAb platform has class-wide safety issues, Cytopoint ($1B+ franchise) is also at risk; (c) vet confidence erosion affects ALL Zoetis products, not just Librela.
- **Severidad:** HIGH
- **Resolucion sugerida:** The investment committee should not assume Librela recovers. Base case should model Librela declining to $300-400M (from $568M) over 2 years, with a 15% probability of near-total franchise impairment. The $140 FV should be reduced by $5-8 to account for this.

### 2. "Growth deceleration is conservative guidance, will revert to 6-7%"

- **Evidencia en contra:**
  - **Management itself guided 3-5% organic for 2026.** The thesis then projects 5-6% in Years 1-2 and 7-8% in Years 3-5. This directly contradicts management's own guidance for Year 1.
  - **Veterinary visits declined 3.1% in 2025** (confirmed by industry white paper), continuing a multi-year trend. This is NOT purely cyclical: 52% of US pet owners have skipped or declined vet care due to cost (Gallup), 70% of pet owners have delayed visits (MetLife survey), and vet costs have risen 60%+ since 2014.
  - **Piper Sandler downgraded ZTS to Neutral** specifically citing vet visit secular decline.
  - **Dermatology franchise grew only 1% in Q4 2025** -- the $1.74B dermatology franchise is stalling even before generic entry.
  - **Apoquel patent expires November 2026.** The thesis mentions generics "before 2030" as if this is years away. In reality, patent expiry is THIS YEAR, with generic launches plausible in 2027. This is a $650M+ franchise at immediate risk.
  - The "diagnostics +13% growth" offset is real but diagnostics is a small fraction of total revenue. It cannot compensate for stalling dermatology, declining Librela, and weakening vet visits simultaneously.
- **Severidad:** HIGH
- **Resolucion sugerida:** The investment committee should use 3-5% growth for Year 1 (matching guidance), 4-6% for Years 2-3, and only 6-7% for Years 4-5 if Apoquel generic erosion is offset by pipeline launches. This reduces DCF-derived and OEY-derived fair values by 5-10%.

### 3. "QS adjustment from 73 to 78 (+5 for market position) is justified"

- **Evidencia en contra:**
  - The thesis adjustment adds +5 for market position (0 to 5 out of 8). The moat assessment gives +8 (0 to 8). These are inconsistent -- which is it, +5 or +8?
  - The Session 61 lesson documents that quality_scorer.py defaults market_position to 0/8, and the fix should be applied conservatively. The thesis gives +5, the moat assessment gives +8. This inconsistency is itself a flag.
  - **More importantly, the QS should be adjusted DOWNWARD for forward-looking deterioration:**
    - Growth score of 13/25 assumed stable. But 2026 guidance of 3-5% vs historical 6% means Revenue CAGR is declining, and EPS CAGR will slow correspondingly. This could reduce Growth from 13 to 10-11.
    - Moat score assumes stable. But Librela safety crisis is actively degrading the mAb franchise moat. Apoquel patent expiry in November 2026 will create first generic competition for a core product. These factors warrant -2 to -3 on Moat.
    - Capital Allocation: 5/10 is fair, but the $3.2B buybacks at $140-170 (stock now $125.64) is poor capital allocation that the QS doesn't capture. Management borrowed $1.75B in convertible debt to fund buybacks at prices 10-35% above current price.
  - **Net forward-adjusted QS: 73 (tool) + 5 (market position) - 3 (growth deceleration) - 2 (moat under siege) = 73, or Tier B, NOT Tier A.**
  - The adversarial pattern continues: this is the 6th consecutive company where the fundamental analyst overrated the QS. The system's documented pattern (Error #43) shows 5 of 6 prior Tier A classifications had inflated QS.
- **Severidad:** MODERATE
- **Resolucion sugerida:** QS should remain at 73 (Tier B). The market position adjustment is valid (+5) but offset by forward-looking deductions for growth deceleration (-3) and moat under active siege (-2). Tier B valuation methods and MoS requirements should apply.

### 4. "Quality compounder premium justifies $140 FV vs $119 weighted average"

- **Evidencia en contra:**
  - The thesis calculates a $119 weighted average FV using 4 methods, then adds an arbitrary 15-18% "quality compounder premium" to arrive at $140. This is problematic:
    - **The weighted average already includes method weights that favor OEY (which gives compounder-friendly valuations).** Adding a premium on top double-counts the quality factor.
    - **The DCF at $88 is the only truly independent method.** The OEY, EV/EBIT, and Reverse DCF all cluster at $126-135, suggesting the stock is near fair value, not 11% below it.
    - **The reverse DCF explicitly states: "ZTS at $126 = approximately fair value."** The thesis then adds a premium to make it look undervalued. This is circular.
    - **Analyst consensus price target: $152-155.** Our $140 would be below consensus, which is unusual for a thesis claiming a stock is "cheap." But consensus is based on 25-30x P/E assumptions, which may not materialize given 3-5% growth.
    - **Seeking Alpha analysis notes intrinsic value range of $110-$146** depending on growth assumptions, centering around current price levels. "Only slightly undervalued at best."
    - **Risk-identifier's own expected-value-weighted price: $127-135.** The risk assessment team independently concluded ZTS is "approximately fairly priced for the risk-adjusted outlook."
  - **The FV should be $120-125, not $140.** Removing the unjustified premium and using the weighted average with corrected growth inputs.
- **Severidad:** HIGH
- **Resolucion sugerida:** Fair value should be reduced to $120-125. This means at current $125.64, MoS is approximately 0%, confirming the thesis's own conclusion that the stock is NOT a buy at current prices. But it also means the entry target should be $95-105 (not $110-115) to achieve adequate MoS for Tier B.

### 5. "Animal health TAM growing 6-10% CAGR is a secular tailwind"

- **Evidencia en contra:**
  - The TAM growth is real, but Zoetis's CAPTURE of that growth is questionable:
    - US vet visits declining 2-4% YoY. If fewer pets see vets, fewer get prescribed Zoetis products.
    - 52% of US pet owners have skipped or declined vet care due to cost (Gallup 2025). This is a demand ceiling.
    - 64% of pet owners earning <$36K and 72% earning $36-60K say they cannot afford vet care.
    - Post-COVID pet ownership is normalizing -- the pandemic "pet boom" added ~23M pets to US households. Not all will sustain premium vet care spending.
  - The thesis assumes pet humanization is a permanent one-way trend. But the affordability data suggests an inflection point: people WANT to spend on pets but increasingly CANNOT.
  - **International markets (50% of ZTS revenue) are growing** -- this partially offsets US weakness. But the thesis relies on BOTH US and international growth to hit 6-7%.
- **Severidad:** MODERATE
- **Resolucion sugerida:** TAM growth should be haircut from 6-10% to 4-7% to reflect US demand ceiling. Zoetis's share of growth should assume flat US and +6-8% international.

---

## Desafios por Categoria

### Negocio

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 1 | Librela safety crisis deeper than thesis acknowledges | Peer-reviewed 9x higher adverse events, 825+ deaths reported, -32% US Q4, accelerating decline, FDA misleading marketing warning | HIGH |
| 2 | Apoquel patent expiry November 2026 -- sooner than implied | US patent expires Nov 2026. Generics could launch 2027. $650M+ at risk. Thesis says "before 2030" as if distant | HIGH |
| 3 | Vet visit secular decline undermines demand | -3.1% in 2025, 52% owners skip care, affordability crisis documented by Gallup, not just cyclical | HIGH |
| 4 | Dermatology franchise already stalling (1% Q4 growth) | Pre-generic maturation suggests franchise peaked. Even without generics, growth exhausted | MODERATE |
| 5 | Credelio Quattro competitive threat materializing | $100M in first year, 14% US vet clinic share, faster tick kill claims, global expansion 2026 | MODERATE |
| 6 | Diagnostics distant #2 to IDEXX | IDEXX structural lead. Diagnostics growth real but not enough to offset declining legacy products | LOW |

### Valoracion

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 7 | $140 FV includes unjustified 18% "quality premium" on top of weighted average | Double-counts quality factor already in OEY weighting. Reverse DCF says ~fair at $126. Risk team says $127-135 | HIGH |
| 8 | DCF base case ($88) vs OEY ($135) divergence of 53% not adequately resolved | Thesis acknowledges >30% divergence but resolves by downweighting DCF. Both methods have merit. | MODERATE |
| 9 | Growth assumptions exceed management's own guidance | Thesis projects 5-6% Y1-2, management guides 3-5%. This inflates all forward-looking methods | HIGH |
| 10 | Using 2027E forward EV/EBIT to justify premium ignores execution risk | 2027 earnings assume Apoquel survives generics AND growth re-accelerates. Both uncertain. | MODERATE |

### Riesgos

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 11 | EU antitrust investigation minimized | Novel legal theory but EC invested significant resources (dawn raids, formal investigation). Fine up to 10% of turnover (~$950M). Licensing ranevetmab to Virbac would create direct biological competitor to Librela in EU | HIGH |
| 12 | Capital allocation poor: $3.2B buybacks at $140-170 while stock now $125 | Convertible bond at $148.20 is underwater. Borrowed $1.75B at effectively 0.25% to buy shares 10-35% above current price. Value destruction. | MODERATE |
| 13 | Insider ownership 0.1% -- lowest among our Tier A/B companies | Management has minimal skin-in-the-game. Options/RSUs repriced, not permanent capital at risk. 98.2% institutional. | MODERATE |
| 14 | Risk assessment identified 5 HIGH/CRITICAL risks with CORRELATED downside | Librela + Apoquel generics + vet visit decline + growth deceleration all hit companion animal segment simultaneously | HIGH |
| 15 | Convertible bond creates dilution risk at $148.20 if stock recovers | If thesis bull case plays out, converts dilute shareholders. If bear case plays out, debt burden increases | LOW |

### Timing

| # | Desafio | Evidencia | Severidad |
|---|---------|-----------|-----------|
| 16 | No catalyst for near-term re-rating. Headwinds persist through 2026 | Librela decline continuing, Apoquel generics approaching, vet visits declining. No positive catalyst until Lenivia US approval (2027) or pipeline launches | HIGH |
| 17 | Stock just reported earnings (Feb 12) -- post-earnings "known" | Q4 results digested, no information advantage. Next catalyst: Q1 2026 results (May 2026) | MODERATE |
| 18 | Entry at $115 requires further -8.5% decline with no clear catalyst for that drop | Market may have already priced in the negatives. Stock could stabilize at $120-130 and never reach entry | LOW |

---

## Conflictos con Otros Analisis

### Thesis vs Risk Assessment

The risk assessment independently concluded ZTS is "approximately fairly priced" with expected-value-weighted price of $127-135. The thesis claims FV of $140, a 4-10% gap. The risk assessment's conclusion is MORE CONSERVATIVE than the thesis and should take priority, as it incorporates probability-weighted downside scenarios.

### Thesis QS (78) vs Moat Assessment QS (81)

The moat assessment gave QS 81 (adjusting market position by +8), while the thesis gave QS 78 (adjusting by +5). This 3-point discrepancy is a flag. The investment committee should resolve: is the market position adjustment +5 or +8? Given the documented QS inflation pattern (Error #43), the more conservative +5 should apply, and then further adjusted down for forward-looking deterioration.

### Thesis Growth (5-8%) vs Management Guidance (3-5%)

The thesis projects revenue growth above management's own guidance for 2026. This contradicts the critical-thinking skill's rule: "Management guidance: always optimistic, descount 20-30%." If management guides 3-5%, our base case should be 3-5%, not higher.

### Moat Assessment "WIDE" vs Reality of Active Siege

The moat assessment rates ZTS as WIDE moat with 22/25. But:
- Librela franchise is in active decline (-32% US Q4) with peer-reviewed safety concerns
- Apoquel patent expires November 2026
- EU antitrust could force licensing of competing biological
- Dermatology growth stalled at 1% Q4

A moat under this many concurrent attacks should be rated WIDE but NARROWING, not WIDE and STABLE.

---

## Veredicto Global

| Metric | Valor |
|--------|-------|
| Total desafios | 18 |
| Desafios HIGH/CRITICAL | 8 of 18 (44%) |
| Desafios no resueltos por thesis | 6 |
| Veredicto | **STRONG COUNTER (13/19)** |

### Severity Score: 13/19

| Severity | Count | Points Each | Subtotal |
|----------|-------|-------------|----------|
| CRITICAL | 0 | 3 | 0 |
| HIGH | 8 | 1.5 | 12 |
| MODERATE | 7 | 0.5 | 3.5 |
| LOW | 3 | 0 | 0 |
| **Adjusted Total** | | | **13** (capped at 19, rounded) |

Note: Score methodology: CRITICAL=3pts, HIGH=1.5pts, MODERATE=0.5pts, LOW=0pts, capped at 19.

### Interpretacion:

**STRONG COUNTER.** The thesis has serious gaps:

1. **The $140 FV is NOT defensible.** The unjustified 18% quality premium, above-guidance growth assumptions, and inadequate haircut for Librela/Apoquel risks inflate FV by $15-25. Corrected FV: **$115-125.**

2. **QS 78 (Tier A) is NOT defensible on a forward-looking basis.** After adjusting for growth deceleration and moat under siege, QS is approximately 73 = Tier B. This changes MoS requirements from ~15-20% (Tier A precedents) to ~20-25% (Tier B precedents).

3. **The thesis's entry target of $110-115 is actually REASONABLE** -- but only because the corrected FV of $115-125 means $110-115 provides 0-12% MoS. For adequate Tier B MoS of 20-25%, the entry should be $90-100.

4. **No CRITICAL challenges exist** -- the business is fundamentally strong. ROIC of 30%, 70%+ GM, #1 market position, secular TAM growth, no debt crisis. This is NOT a value trap. But it IS fully valued at current prices.

## Recomendacion al Investment Committee

1. **DO NOT proceed to R4 at current prices.** ZTS at $125.64 offers no margin of safety against a corrected FV of $115-125. Even using the thesis's own $140 FV, the 10% MoS is insufficient per all precedents.

2. **Correct the FV from $140 to $120 for the standing order.** The $140 FV inflates the apparent MoS and could lead to premature entry.

3. **Correct entry price from $110-115 to $95-105** to achieve adequate Tier B MoS of 20-25% against corrected FV $120.

4. **Resolve the QS discrepancy:** Is the adjustment +5 (thesis) or +8 (moat assessment)? Apply forward-looking deductions for growth deceleration and moat under siege. My assessment: QS 73, Tier B.

5. **Monitor before acting:**
   - Apoquel generic filings (any ANADA submissions to FDA?)
   - Librela Q1 2026 US revenue trajectory (stabilizing or accelerating decline?)
   - EU antitrust case progress (Statement of Objections?)
   - US vet visit trends (recovering or structural decline?)

6. **If ZTS falls to $95-100:** Re-evaluate. At that price, even the corrected FV of $120 provides 20-25% MoS, consistent with Tier B precedents. The quality of the business is genuine -- the question is price, not quality.

---

## META-REFLECTION

### Dudas/Incertidumbres
- **Librela causality uncertainty:** The Frontiers study found 9x disproportionality, but this is correlation from adverse event databases, not a randomized controlled trial. Zoetis argues confounding factors (older dogs with OA are predisposed to musculoskeletal issues). I could not definitively resolve whether Librela CAUSES joint destruction or whether the patient population is biased. The 18-member expert panel's unanimous "strong suspicion" leans toward causation, but this remains uncertain.
- **Apoquel generic timeline precision:** Patent expires November 2026, but actual generic availability depends on ANADA filings, which I could not find specific data on. Generics could be delayed to 2028 if no manufacturer has filed. My assumption of 2027 launch may be optimistic for the bear case.
- **Vet visit decline structural vs cyclical:** Both narratives are plausible. If interest rates decline and consumer confidence improves, vet visits could recover. I weight structural slightly more because the affordability data is alarming (52% skip care, 60%+ cost increase since 2014), but I acknowledge this could normalize.
- **Fair value sensitivity:** My corrected FV of $115-125 depends heavily on whether growth reverts to 6%+ in Years 3-5. If diagnostics + pipeline launches succeed, the thesis's $140 could prove correct on a 3-5 year horizon. My counter is strongest on 1-2 year timing, weaker on 5-year outlook.

### Limitaciones de Este Analisis
- yfinance rate limiting prevented independent QS tool verification during this analysis.
- Could not access Seeking Alpha full articles (paywall), limiting my ability to fully assess sell-side bear cases.
- The Frontiers study is the most damaging evidence against Librela. I could read the abstract and key findings via search but not the full methodology section to assess statistical rigor.
- Insider transaction data was limited. I could not find specific insider PURCHASES (which would be bullish) -- only that recent insider activity is minimal.

### Sugerencias para el Sistema
- **Add "Apoquel patent expiry November 2026" to ZTS kill condition monitoring.** This is a specific, time-bound event that could materially impact the dermatology franchise.
- **The quality_scorer.py market_position default-to-0 continues to create inconsistencies.** The thesis uses +5, the moat assessment uses +8. A standard override protocol would improve consistency.
- **For pharma/animal health positions, "product safety crisis" should be a standard risk factor** in the risk-identifier template. Librela is a template case that could apply to any biologics position (NVO, GSK, etc.).
- **Capital allocation quality metric needed:** Zoetis scored 5/5 for "shareholder returns" in QS despite buying back $3.2B in stock 10-35% above current price. The QS should penalize buybacks at inflated prices.

### Preguntas para Orchestrator
1. Given the corrected FV of $115-125 (vs thesis $140), should the quality_universe.yaml entry for ZTS be updated from $115 to $95-105?
2. The Apoquel patent expiry in November 2026 is a specific, time-bound risk that the thesis underplayed. Should this be added as a formal kill condition or monitoring trigger?
3. With 8 HIGH-severity challenges and a STRONG COUNTER verdict, does the orchestrator want to defer R2/R3/R4 entirely until Librela stabilization evidence appears, or proceed with the corrected FV?
4. The QS inflation pattern continues (6th consecutive case). Should we implement a "mandatory -5 skepticism discount" on all QS adjustments above the tool score until the tool is fixed?

---

## Sources

### Librela Safety
- [FDA Adverse Events Notification -- dvm360](https://www.dvm360.com/view/fda-notifies-veterinarians-of-adverse-events-linked-to-osteoarthritis-treatment)
- [Frontiers -- Musculoskeletal adverse events in Librela-treated dogs (9x disproportionality)](https://www.frontiersin.org/journals/veterinary-science/articles/10.3389/fvets.2025.1581490/full)
- [Frontiers -- Commentary on musculoskeletal AEs](https://www.frontiersin.org/journals/veterinary-science/articles/10.3389/fvets.2025.1663398/full)
- [PMC -- Musculoskeletal adverse events commentary](https://pmc.ncbi.nlm.nih.gov/articles/PMC12606670/)
- [AVMA -- FDA adverse events in dogs with mAb drug](https://www.avma.org/news/fda-adverse-events-dogs-reported-monoclonal-antibody-drug)
- [Vet Times -- Librela ban calls](https://www.vettimes.com/news/vet-nursing/small-animal/librela-row-erupts-again-amid-public-calls-for-ban)
- [Zoetis Statement on Librela Safety](https://news.zoetis.com/press-releases/press-release-details/2024/Zoetis-Statement-on-the-Safety-of-Librela/default.aspx)

### Competitive Threats
- [Elanco -- Credelio Quattro hits blockbuster $100M](https://www.elanco.com/us/newsroom/press-releases/elanco-innovation-builds-momentum-credelio-quattrotm-lotilaner-moxidectin-praziquantel-and-pyrantel-chewable-tablets-reaches-blockbuster-status)
- [Credelio Quattro 14% market share in US vet clinics](https://www.stocktitan.net/news/ELAN/elanco-innovation-builds-momentum-credelio-quattro-tm-lotilaner-3a5o2vyy0t8z.html)

### Vet Visit Decline
- [Gallup -- 52% of US pet owners skipped or declined vet care](https://news.gallup.com/poll/659057/pet-owners-skipped-declined-veterinary-care.aspx)
- [Pets.care -- Vet visits decline 3.1% in 2025](https://www.pets.care/news/2026/01/new-white-paper-reveals-veterinary-visits-decline-3-point-1-percent-in-2025-as-negative-trend-continues/)
- [dvm360 -- Veterinary visits decline as clients face rising costs](https://www.dvm360.com/view/veterinary-visits-decline-as-clients-face-rising-costs-data-reveals)
- [MetLife -- 70% of pet owners delayed vet visits due to cost](https://www.metlifepetinsurance.com/dodging-the-vet/)
- [PetSmart Charities -- Cost of care strains veterinary access](https://petsmartcharities.org/press-releases/cost-of-care-continues-to-strain-veterinary-care-access-new-study-finds)

### Growth Deceleration & Analyst Views
- [Benzinga -- Analysts question Zoetis pathway to growth](https://www.benzinga.com/markets/earnings/26/02/50588760/analysts-question-zoetis-pathway-to-growth-as-key-segments-slide)
- [Seeking Alpha -- Zoetis has fallen hard, investment case not obvious](https://seekingalpha.com/article/4860081-zoetis-has-fallen-hard-investment-case-is-still-not-obvious)
- [Simply Wall St -- Zoetis outlook cut highlights slower vet visits](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-zts/zoetis/news/zoetis-outlook-cut-highlights-slower-vet-visits-and-long-ter/amp)
- [ainvest -- Zoetis hold rating priced in](https://www.ainvest.com/news/zoetis-hold-rating-priced-2602/)

### Apoquel Patent
- [Federal Register -- Apoquel patent term extension](https://www.federalregister.gov/documents/2016/04/12/2016-08333/determination-of-regulatory-review-period-for-purposes-of-patent-extension-apoquel)

### Capital Allocation
- [ainvest -- Zoetis convertible bond: strategic or manipulation?](https://www.ainvest.com/news/zoetis-1-75-billion-convertible-bond-offering-strategic-share-buybacks-stock-price-manipulation-2512/)
- [Zoetis -- $6B buyback authorization](https://investor.zoetis.com/news/news-details/2024/Zoetis-Announces-Authorization-of-Multi-Year-6-Billion-Share-Repurchase-Program/default.aspx)

### EU Antitrust
- [EC -- Investigation into Zoetis](https://ec.europa.eu/commission/presscorner/detail/en/ip_24_1687)
- [Goodwin Law -- EC launches antitrust investigation](https://www.goodwinlaw.com/en/insights/publications/2024/04/insights-otherindustries-european-commission-launches-antitrust-investigation)
- [Hogan Lovells -- Pipeline drug investigation analysis](https://www.hoganlovells.com/en/publications/commission-investigation-into-termination-of-pipeline-drug-what-next-for-rd-decision-making)

### Valuation & Consensus
- [Public.com -- ZTS analyst forecast and price target](https://public.com/stocks/zts/forecast-price-target)
- [Alpha Spread -- ZTS intrinsic valuation](https://www.alphaspread.com/security/nyse/zts/summary)
- [Benzinga -- Top forecasters revamp ZTS expectations](https://www.benzinga.com/analyst-stock-ratings/price-target/26/02/50566792/top-wall-street-forecasters-revamp-zoetis-expectations-ahead-of-q4-earnings)
