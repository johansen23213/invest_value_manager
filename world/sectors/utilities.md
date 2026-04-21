# Sector: Utilities (European)

> Ultima actualizacion: 2026-02-18
> Status: **INFRAPONDERAR -- Structural quality mismatch with our framework. Yields attractive but ROIC consistently near or below WACC.**

## Resumen Ejecutivo

El sector utilities europeo ofrece una combinacion atractiva de yield defensivo (4-6%), valuaciones razonables (P/E 10-13x vs 18x historico), y exposicion estructural a la electrificacion y transicion energetica. El capex del sector alcanzara EUR 114B en 2026 (+4% YoY), liderado por EDF, Enel, E.ON y EnBW.

Las utilities integradas (generacion + distribucion + retail) como A2A, Enel y Engie estan mejor posicionadas que las pure-play renovables (Orsted, EDP) que enfrentan presion de margenes por costes de materiales. El sector cotiza con descuento vs historia debido a: (1) tipos de interes elevados que comprimen multiplos de activos regulados, (2) volatilidad de precios de commodities post-2022, (3) preocupacion por capex de grid que reduce FCF a corto plazo.

**UPDATE 2026-02-18: Systematic screening confirms sector INCOMPATIBLE with our quality framework.**
Scored 4 major utilities via quality_scorer.py:
- SSE.L: QS 28 (Tier D) -- ROIC < WACC, negative FCF 2 of 4 years
- ENEL.MI: QS 45 (Tier C) -- FCF negative in 2021 (-2.3B) and 2022 (-4.6B)
- VIE.PA (Veolia): QS 52 (Tier C) -- ROIC-WACC only +1.0pp, 3.8x leverage, 17% GM
- Hera (HER.MI): ROIC 5.2% < WACC 8.9% (web data)
- A2A.MI: QS 37 (sold Feb 8) -- ROIC -3.0pp

None achieved QS >= 55 (Tier B minimum). The sector's capital-intensive, regulated model produces low ROIC by design. High yields mask poor capital efficiency. DTE.DE (already owned, QS 69) remains our sole utility exposure and is exceptional within the sector due to its telecom operations.

**Status downgraded from SOBREPONDERAR to INFRAPONDERAR for new investments.** Continue monitoring Enel CMD (Feb 23) but do not expect quality threshold to be met.

---

## Metricas Clave

| Metrica | Valor | vs Historia | Tendencia |
|---------|-------|-------------|-----------|
| TAM Europa | EUR 400B+ | Estable | --> |
| Capex 2026 | EUR 114B | +4% YoY | Up |
| P/E sector | 10-13x | vs 18x (10y avg) | Down |
| Dividend yield | 4-6% | vs 3-4% (10y avg) | Up |

---

## Estructura Competitiva

**Concentracion:** Oligopolio regional (cada pais dominado por 1-3 players)
**Top 5 por market cap:** EDF, Enel, Iberdrola, E.ON, Engie (~60% del mercado)

| Empresa | Pais | Fortaleza |
|---------|------|-----------|
| Enel | Italia | Lider renovables, escala global |
| Iberdrola | Espana | Networks + renewables, US exposure |
| E.ON | Alemania | Networks focus, regulated earnings |
| Engie | Francia | Gas + renewables, diversificado |
| A2A | Italia | Multi-utility, waste-to-energy, local monopoly |

**Barreras de entrada:** Altas
- Activos regulados con licencias exclusivas
- Capex intensivo (EUR 50-100M por proyecto)
- Relaciones regulatorias de decadas
- Grid infrastructure impossible to replicate

---

## Ciclo y Sensibilidad

| Factor | Sensibilidad | Notas |
|--------|--------------|-------|
| Tipos de interes | Alta | Activos regulados = duration larga. +100bp en tipos = -8-12% en valuacion |
| Recesion | Baja | Demanda electrica inelastica. Caida tipica <5% en recesion |
| Inflacion | Media | Pass-through parcial en tarifas reguladas. 6-12 meses de lag |

**Mejor fase del ciclo:** All (defensivo), pero outperforma en Early/Late cuando tipos bajan
**Beta tipico:** 0.6-0.8

---

## Disrupcion y Riesgos

### Tecnologicos
| Amenaza | Probabilidad | Impacto | Timeline |
|---------|--------------|---------|----------|
| Solar distributed | Alta | Medio | 5-10 anos |
| Battery storage | Alta | Medio | 3-5 anos |
| AI demand | Media | Positivo | 2-5 anos |

### Regulatorios
| Regulacion | Probabilidad | Impacto |
|------------|--------------|---------|
| EU Green Deal capex mandates | Alta | Mixto (capex up, pero returns regulados) |
| Windfall taxes (repeat 2022) | Baja | Alto negativo |
| Nuclear extension | Media | Positivo para EDF, neutro otros |

### Competitivos
- Nuevos entrantes: Limited (capital intensive, regulated)
- Sustitutos: Rooftop solar + battery (amenaza a largo plazo para retail margins)

---

## Sentimiento de Mercado

**Sentimiento actual:** Ignorado (post-2022 energy crisis rotation out)

**Narrativa dominante:**
"Utilities son aburridas, tipos altos comprimen valuaciones, capex de transicion destruye FCF"

**Mi contra-tesis (DEBILITADA por screening):**
"El mercado subestima pricing power y AI demand. PERO: systematic quality scoring shows that even the 'best' EU utilities barely clear WACC. The yields are attractive (4-6%) but ROIC is structurally low. We cannot invest in companies that destroy value (ROIC < WACC) regardless of yield. DTE.DE is the exception because its telecom segment (not utility segment) drives returns."

**Flujos de fondos (12m):** Outflows moderados (~$5B de equity funds europeos)

---

## Quality Scoring Results (2026-02-18)

| Ticker | Name | QS Tool | Tier | ROIC-WACC | GM | FCF Pattern | Leverage | Yield | Verdict |
|--------|------|---------|------|-----------|-----|------------|----------|-------|---------|
| SSE.L | SSE plc | 28 | **D** | -0.2pp | 38% | Neg 2/4y | 3.7x | 2.4% | ELIMINATED |
| ENEL.MI | Enel | 45 | C | +1.3pp | 54% | Neg 2/4y | 3.2x | 5.3% | BELOW THRESHOLD |
| VIE.PA | Veolia | 52 | C | +1.0pp | 17% | Pos 4/4y | 3.8x | 4.2% | BELOW THRESHOLD |
| HER.MI | Hera | N/A | C est. | -3.7pp | N/A | N/A | N/A | 3.5% | BELOW THRESHOLD (ROIC < WACC) |
| A2A.MI | A2A | 37 | C | -3.0pp | N/A | N/A | N/A | 4.1% | SOLD (destroyed value) |

---

## Empresas Objetivo

### Para analisis profundo
| Ticker | Razon | Priority |
|--------|-------|----------|
| A2A.MI | SOLD 2026-02-08. Adversarial: QS 37, ROIC -3.0pp, FV inflated 24% | ARCHIVED |
| ENEL.MI | QS 45 Tier C. Lider renovables, CMD Feb 23. ROIC-WACC +1.3pp barely positive. FCF inconsistent. Would need QS >= 55 for consideration. | **Baja (quality insufficient)** |
| ENGI.PA | Not yet scored. Yield 6.6%, diversificada, earnings Feb 28. But sector pattern suggests QS likely Tier C. | **Baja** |
| IBE.MC | Not scored. US exposure via Avangrid. But Morningstar says 23% overvalued. | **Baja** |
| VIE.PA | QS 52 Tier C. World water leader. ROIC-WACC only +1.0pp. 90.9% payout ratio. 3.8x leverage. Not our type. | **Evitar** |

### Evitar
| Ticker | Razon |
|--------|-------|
| ORSTED.CO | Pure renewables, margin pressure, capex cuts |
| EDP.LS | Similar a Orsted, selective capex |
| EDF.PA | State-owned, nuclear politics, opaque |
| SSE.L | QS 28 Tier D. ROIC < WACC. Eliminated. |
| HER.MI | ROIC < WACC by 3.7pp. Value destruction. |

---

## Posiciones Historicas

### A2A.MI (SOLD 2026-02-08)
- **Entry:** 134 shares @ EUR 2.54, invested ~EUR 343
- **Exit:** EUR 2.54, P&L: -1.5% (EUR -5)
- **Reason:** Adversarial review - QS 37 Tier C (thesis claimed Tier A). ROIC -3.0pp (destroying value). EBIT overstated 25%. FV inflated 24% (thesis EUR 2.70 vs adversarial EUR 2.04). MoS -24.5%.
- **Lesson:** Thesis self-assigned quality tier must match quality_scorer.py. ROIC < WACC = exit signal. DDM unreliable when FCF is negative.

---

## Catalizadores Proximos

| Fecha | Evento | Impacto esperado |
|-------|--------|------------------|
| 2026-02-23 | Enel Capital Markets Day | Monitor only. Would need to show QS-improving metrics (FCF consistency, ROIC >8%). |
| 2026-02-28 | Engie FY2025 results | Watch FCF yield >5%, Debt/EBITDA <4x |
| 2026-03-01 | Naturgy FY2025 | Watch dividend policy |
| 2026-03-19 | Enel FY2025 results | Confirmar guidance post-CMD |

---

## Historial de Cambios

| Fecha | Cambio | Razon |
|-------|--------|-------|
| 2026-02-04 | Status inicial: SOBREPONDERAR | Valuaciones atractivas, yield spread positivo, exposicion estructural a electrificacion |
| 2026-02-08 | A2A.MI SOLD | Adversarial review: QS 37 Tier C, ROIC -3.0pp, FV inflated 24%. Position closed. |
| 2026-02-18 | **Status: SOBREPONDERAR -> INFRAPONDERAR** | Systematic QS screening of 4 major utilities: ALL scored Tier C or Tier D. ROIC structurally near/below WACC. Sector incompatible with quality framework. |

---

## Fuentes

- [ING Think: European utilities 2026 outlook](https://think.ing.com/articles/energy-european-utilities-2026-steady-currents/)
- [Morgan Stanley: A2A top pick](https://www.investing.com/news/stock-market-news/morgan-stanley-lifts-a2a-to-top-pick-stock-climbs-6-on-325-call-4326321)
- [Deloitte: 2026 Power & Utilities Outlook](https://www.deloitte.com/us/en/insights/industry/power-and-utilities/power-and-utilities-industry-outlook.html)
- [A2A Investor Relations](https://www.a2a.eu/en/investors)
- [Morningstar: Top Picks Among European Utilities](https://global.morningstar.com/en-gb/stocks/top-picks-among-european-utilities)
- [Morningstar: Best Utilities Stocks to Buy](https://www.morningstar.com/stocks/best-utilities-stocks-buy)
