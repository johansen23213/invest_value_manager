# Investment Committee Decision: Moeve S.A. (antigua Cepsa)

> **Fecha:** 2026-02-07
> **Decision: NO INVERTIBLE (empresa no cotizada) + AVOID incluso si cotizara**
> **Unanimidad: SI**

---

## Gate 0: Sector View Exists?

- **Sector:** Energy (refining/integrated oil)
- **Sector view:** `world/sectors/energy.md` existe (SHEL.L era posicion previa)
- **Status:** PASS (nota: sector view es para energy general, no refining-especifico)

---

## Gate 1: Quality Score >= 35 (Tier D Filter)

- **QS Manual:** 45/100 (Tier C)
- **Status:** PASS (supera umbral Tier D)
- **Nota:** QS 45 es bajo. Financial Quality 16/40 es particularmente debil (ROIC < WACC, FCF negativo).

---

## Gate 2: Business Understanding

- **Modelo de negocio comprendido:** SI
  - Refining (78% EBITDA): Compra crudo, refina, vende productos petroliferos
  - Chemicals (14%): LAB, fenol, acetona para industria
  - Upstream (8%): Produccion en declive, desinvertido 70%
  - Transicion: Hydrogen, biofuels, biometano, EV charging (pre-revenue)
- **Unit economics:** Margenes ultra-bajos tipicos de refining (EBITDA 7.4%, Net 0.4%)
- **Status:** PASS

---

## Gate 3: Moat Assessment

- **Moat:** NARROW (debilitandose)
- **Durabilidad:** 8-12 anos
- **ROIC premium:** NEGATIVO (3-6% vs WACC 8-9%)
- **Status:** PASS con reservas. Un moat sin ROIC premium no protege capital.

---

## Gate 4: Risk Assessment

- **Risk Score:** HIGH (2 criticos + 6 importantes)
- **Riesgos criticos:**
  1. FCF negativo prolongado por EUR 8B capex transicion
  2. Iliquidez total (no cotiza)
- **Status:** FAIL PARCIAL. Riesgo HIGH es aceptable SOLO con MoS muy alto (>40%). No aplicable por no cotizar.

---

## Gate 5: Valuation & MoS

- **Fair Value base:** EUR 4,000-5,500M equity
- **Risk-adjusted:** EUR 2,000-2,800M equity
- **Precio actual:** N/A (no cotiza)
- **MoS:** NO CALCULABLE (sin precio de mercado)
- **Status:** N/A (no cotiza, no hay MoS)

---

## Gate 6: Macro Alignment

- **Contexto macro:** Tipos elevados pero bajando, refining margins ciclicos
- **Sector alignment:** Energia en transicion, regulacion ESG creciente
- **Espana:** Riesgo regulatorio (windfall tax), pero entorno macro estable
- **Status:** NEUTRAL. No hay desalineacion macro especifica.

---

## Gate 7: Portfolio Fit

- **Correlacion con portfolio:** Tendriamos exposicion a energia (ya vendimos SHEL.L)
- **Sector concentration:** Energia es 0% del portfolio actual
- **Geo concentration:** Espana no tiene exposicion actual
- **Status:** PASS hipotetico (no correlacionada con portfolio actual)

---

## Gate 8: Sector Understanding

- **Sector view existe:** SI (energy.md)
- **Posicion en sector:** #2 refiner Espana, transicionando
- **Competencia entendida:** SI (Repsol, Galp, OMV, MOL, Neste)
- **Status:** PASS

---

## Gate 9: Counter-Analysis

- **Devil's Advocate:** STRONG COUNTER (7/10 puntos criticos/altos)
- **Puntos criticos no resueltos:**
  1. Transicion de EUR 8B sin precedentes de exito industrial
  2. ROIC < WACC (destruye valor economico)
  3. Net income contable = break-even (EUR 92M sobre EUR 25B revenue)
  4. Carlyle trapped capital crea incentivos perversos
- **Conflictos con thesis:** La thesis reconoce estos problemas pero los califica como "especulativos". El devil's advocate los demuestra como ESTRUCTURALES.
- **Status:** FAIL. Counter-analysis es mas convincente que thesis positiva.

---

## Gate 10: Quality Gravitation (Principio 9)

- **QS de Moeve:** 45 (Tier C)
- **Portfolio actual avg Tier A:** 6 posiciones Tier A (QS >75)
- **Direccion:** CONTRARIA a la direccion estrategica del portfolio
- **Pregunta:** "Si tuvieramos EUR 500 libres, ¿Moeve QS 45 o ADD a ADBE QS 76 / NVO QS 82?"
- **Respuesta:** Claramente las Tier A existentes son mejor uso del capital
- **Status:** FAIL. Invertir en Moeve iria contra Principio 9.

---

## Decision Final

### RESULTADO: NO INVERTIBLE / AVOID

**Razones primarias:**

1. **No cotiza en bolsa** — no hay forma fisica de invertir en equity
2. **QS 45 (Tier C)** en un portfolio que gravita hacia Tier A
3. **ROIC < WACC** — destruye valor economico
4. **FCF negativo** — no retorna capital a accionistas
5. **Counter-analysis STRONG** — los argumentos en contra son mas solidos que los a favor
6. **Principio 9** — cada euro en Moeve es un euro no invertido en un compounder

**Gates fallidos:** Gate 4 (FAIL parcial), Gate 9 (FAIL), Gate 10 (FAIL)

### Nota sobre Bonos

Los bonos de Moeve (especialmente EUR 750M al 4.125% vencimiento 2031, rating BBB-/Baa3) podrian ser invertibles como instrumento de renta fija. Sin embargo, esto queda fuera del scope de nuestro portfolio (equity value investing). El analisis de credito seria un ejercicio separado.

### Nota sobre IPO Futura

Si Moeve eventualmente sale a bolsa, RE-EVALUAR SOLO SI:
1. QS mejora a >55 (Tier B minimo)
2. FCF se vuelve positivo
3. ROIC > WACC demostrado
4. Transicion energetica muestra resultados cuantificables
5. Precio ofrece MoS >30% vs fair value adversarial

---

## Votos

| Evaluador | Voto | Razonamiento |
|-----------|------|-------------|
| Fundamental Analyst | AVOID | QS 45, FCF negativo, ROIC < WACC |
| Moat Assessor | AVOID | Narrow moat debilitandose, no genera retornos |
| Risk Identifier | AVOID | HIGH risk score, 2 criticos |
| Valuation Specialist | N/A | No hay precio de mercado |
| Devil's Advocate | STRONG AVOID | 7/10 puntos criticos, narrative-reality gap enorme |
| **Committee** | **AVOID (unanime)** | **No invertible + no cumple estandares de calidad** |

---

## META-REFLECTION

### Proceso
- Este fue un analisis completo ejecutado manualmente (agentes no disponibles por rate limit)
- La profundidad es adecuada para la decision (AVOID) pero inferior a un analisis con agentes independientes
- Los 6 ficheros del pipeline se generaron: thesis, moat, risk, valuation, counter-analysis, committee

### Lecciones
1. El pipeline de analisis funciona para empresas no cotizadas con adaptaciones (QS manual, sin yfinance)
2. La data de empresas privadas es mas limitada (no PDFs accesibles, no balance sheet completo)
3. Para empresas no cotizadas, el gate de iliquidez deberia ser Gate 1 (filtrar antes de invertir esfuerzo)

### Sugerencia para Sistema
- Considerar anadir un "Gate -1: Invertibilidad" al pipeline que filtre empresas no cotizadas ANTES de gastar recursos en analisis completo (a menos que sea un ejercicio deliberado como este caso).
