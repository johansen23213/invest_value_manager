# Valuation Report: Moeve S.A. (antigua Cepsa)

> **Fecha:** 2026-02-07
> **Valoracion independiente multi-metodo**
> **Fair Value Estimado: EUR 4,000-5,500M equity (pre-descuento iliquidez)**
> **Risk-Adjusted Fair Value: EUR 2,000-2,800M equity**

---

## 1. Contexto para la Valoracion

### Challenges Especificos
- **No cotiza:** Sin precio de mercado para calcular MoS
- **FCF negativo:** DCF clasico no aplicable directamente
- **Cyclicality:** EBITDA fluctua +/-30% con refining margins
- **Transicion:** El valor depende materialmente de si EUR 8B capex genera retorno

### Metodos Seleccionados
1. **EV/EBITDA Comparables** (metodo primario - mas apropiado para refining)
2. **Sum of Parts** (captura diferencias de calidad por segmento)
3. **Transaction Multiples** (transaccion Carlyle 2019 como referencia)
4. **Normalized FCF** (proyectando FCF post-capex de transicion)

---

## 2. Metodo 1: EV/EBITDA Comparables

### Panel de Comparables (Feb 2026)

| Empresa | EV/EBITDA | ROIC | Net Debt/EBITDA | Nota |
|---------|-----------|------|-----------------|------|
| Repsol | 3.5x | ~7% | 1.2x | Mas diversificado, cotiza |
| Galp | 4.2x | ~9% | 0.8x | Mejor margin, cotiza |
| OMV | 3.2x | ~8% | 1.5x | Austria, mas quimicos |
| MOL | 3.8x | ~8% | 1.0x | Hungria, emergente premium |
| Neste | 8.0x | ~12% | 1.0x | Biofuels puro, premium |
| **Media (ex-Neste)** | **3.7x** | | | |
| **Media completa** | **4.5x** | | | |

### Descuento Apropiado vs Comparables
Moeve merece descuento por:
- No cotiza (-15% por iliquidez)
- ROIC inferior (3-6% vs media 7-9%)
- FCF negativo actual
- Riesgo de ejecucion transicion

**Multiple justo para Moeve: 2.8-3.5x EBITDA** (descuento ~20-25% vs media comparables)

### Calculo

| Escenario | Multiple | EBITDA Base | Enterprise Value | - Net Debt | Equity Value |
|-----------|----------|-------------|------------------|------------|-------------|
| Bear | 2.8x | EUR 1,500M* | EUR 4,200M | EUR 2,369M | **EUR 1,831M** |
| Base | 3.2x | EUR 1,852M | EUR 5,926M | EUR 2,369M | **EUR 3,557M** |
| Bull | 3.5x | EUR 2,000M** | EUR 7,000M | EUR 2,369M | **EUR 4,631M** |

*Bear: normalizado para refining margins debiles
**Bull: refining margins fuertes + crecimiento chemicals

---

## 3. Metodo 2: Sum of Parts

### Valoracion por Segmento

| Segmento | EBITDA 2024 | Multiple | EV Segmento | Razonamiento |
|----------|-------------|----------|-------------|-------------|
| **Energy** | EUR 1,453M | 3.0x | EUR 4,359M | Refining puro, ciclico, margenes bajos |
| **Chemicals** | EUR 253M | 5.0x | EUR 1,265M | LAB tiene mejor moat, menos ciclico |
| **Upstream** | EUR 298M | 2.0x | EUR 596M | En runoff, desinvirtiendo, bajo multiple |
| **Green pipeline** | -- | -- | EUR 500-1,000M | Optionality por hydrogen/biofuels |
| **Total EV** | | | **EUR 6,720-7,220M** | |
| - Net Debt | | | -EUR 2,369M | |
| **Equity Value** | | | **EUR 4,351-4,851M** | |

### Notas sobre Green Pipeline Value
- EUR 500M-1,000M es valor de opcion por los proyectos en desarrollo
- La planta de biofuels 2G en Huelva (EUR 1.2B inversion) podria valer EUR 500-800M si funciona
- El valle de hidrogeno verde tiene optionality pero es pre-revenue
- Descuento por probabilidad de exito: ~30-40% de capex como valor de opcion

---

## 4. Metodo 3: Transaction Multiples

### Transaccion Carlyle 2019
- Carlyle compro 38.41% de Cepsa
- Valoracion implicita: ~$12B EV (~EUR 11B al cambio de 2019)
- EBITDA 2019 estimado: ~EUR 2,000-2,200M
- **Multiple implicito: ~5.0-5.5x EBITDA**

### Analisis de la Transaccion
El multiple de 5.0-5.5x fue ALTO para refining:
- Carlyle posiblemente pago por: (a) potencial de IPO, (b) plan de transicion, (c) prima por control parcial
- La IPO se cancelo en 2018 y no se ha materializado
- EBITDA actual (EUR 1,852M) es similar al de 2019, pero el negocio ha cambiado (menos upstream, mas capex)
- **Implicacion: Carlyle posiblemente overpaid. Su inversion a ~EUR 4,200M por 38.4% implica que necesita equity value >EUR 11B para recuperar inversion. Actual: EUR 3,500-5,000M → Carlyle esta underwater.**

---

## 5. Metodo 4: Normalized FCF

### Proyeccion Post-Transicion (2030+)

Asumiendo que la transicion termina exitosamente en 2030:

| Item | 2024 (actual) | 2030E (exito) | 2030E (parcial) |
|------|---------------|---------------|-----------------|
| EBITDA | EUR 1,852M | EUR 2,500M | EUR 2,000M |
| Capex mant. | -EUR 600M | -EUR 700M | -EUR 700M |
| Capex transicion | -EUR 700M | EUR 0 | EUR 0 |
| **FCF** | **-EUR 170M** | **EUR 1,800M** | **EUR 1,300M** |
| FCF Yield (sobre EV) | Negativo | 22-25% | 16-18% |

Si Moeve genera EUR 1,300-1,800M de FCF en 2030, y asumimos:
- Discount rate: 10% (WACC + iliquidez premium)
- Terminal growth: 0% (mercado en declive)
- Descuento de 5 anos (2026-2030 FCF negativo/bajo)

**PV of 2030 FCF stream:** EUR 8,000-11,000M (perpetuity at 10%)
**Descontado 5 anos a 10%:** EUR 5,000-6,800M EV
**Menos Net Debt 2030E (EUR 3,000-4,000M):** EUR 1,000-3,800M equity

**ALTO RIESGO:** Este metodo depende totalmente de que la transicion funcione Y de que capex caiga post-2030.

---

## 6. Consolidacion de Fair Value

| Metodo | Bear | Base | Bull |
|--------|------|------|------|
| EV/EBITDA Comparables | EUR 1,831M | EUR 3,557M | EUR 4,631M |
| Sum of Parts | -- | EUR 4,351-4,851M | -- |
| Transaction (Carlyle) | -- | ~EUR 11B (overpaid) | -- |
| Normalized FCF (2030) | EUR 1,000M | EUR 2,400M | EUR 3,800M |

### Fair Value Pre-Descuento Iliquidez

**Ponderando por fiabilidad:**
- EV/EBITDA: 40% peso (mas fiable para refining)
- Sum of Parts: 35% peso (captura segmentos)
- Normalized FCF: 15% peso (altamente especulativo)
- Transaction: 10% peso (stale, posible overpayment)

| Escenario | Equity Value |
|-----------|-------------|
| Bear | EUR 2,000M |
| Base | EUR 4,000-4,500M |
| Bull | EUR 5,500M |

### Fair Value con Descuento por Iliquidez (-25-30%)

| Escenario | Equity Value Risk-Adjusted |
|-----------|--------------------------|
| Bear | EUR 1,400M |
| **Base** | **EUR 2,800-3,200M** |
| Bull | EUR 3,900M |

---

## 7. Implicaciones

### Para Equity (si alguna vez cotiza)
- **Fair Value base:** EUR 4,000-5,500M equity pre-iliquidez
- **Si IPO:** Descuento de ~10-15% vs intrinsic (nuevo listing, track record privado)
- **Range de IPO pricing:** EUR 3,400-4,700M equity

### Para Bonos (invertibles)
Los 3 bonds en Euronext Dublin SI son invertibles:
- **Bond 2028 (0.75% coupon):** Yield-to-maturity depende de precio de mercado
- **Bond 2026 (2.25%):** Vence pronto, bajo riesgo
- **Bond 2031 (4.125%):** El mas interesante. Rating BBB-/Baa3 (investment grade).

Con un equity cushion de EUR 3,000-5,000M por debajo de EUR 2,369M de deuda, los bonos parecen razonablemente seguros (debt/EV ~25-40%).

---

## 8. META-REFLECTION

### Dudas/Incertidumbres
1. El multiple exacto de comparables depende del momento del ciclo de refining. En pico de margenes, los multiples se comprimen (EBITDA sube, EV menos). Podria estar sobrevalorando en base de EBITDA 2024 (que fue buen ano).
2. La valoracion del green pipeline es altamente subjetiva. EUR 500-1,000M es placeholder basado en fraccion de capex invertido.

### Anomalias Detectadas
1. **Carlyle underwater:** La valoracion implica que Carlyle's 38.4% vale EUR 1,100-1,700M vs ~EUR 4,200M que pago. Esto explica la presion por merger Galp (crear valor/exit) y la fallida IPO.
2. **Net Debt/EBITDA subio de 1.4x a 1.7x** entre FY2024 y Q3 2025. Tendencia preocupante con FCF negativo.

### Preguntas para Orchestrator
1. Los bonos de Moeve merecerian un analisis de credito separado? BBB-/Baa3 con 4.125% coupon podria ser interesante vs nuestro portfolio de equity.
