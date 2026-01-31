# DECISIÓN: WATCHLIST - Iberdrola (IBE.MC)

**Fecha:** 2026-01-27
**Decisión:** WATCHLIST (NO comprar ahora)
**Analista:** Deep Analyst
**Comité:** Investment Committee

---

## Resumen Ejecutivo

Iberdrola RECHAZADA para compra inmediata. Quality excelente (9/10), moat narrow-to-wide, management track record impecable, estructura defensive perfecta para portfolio. PERO cotiza P/E 21-24x con margen seguridad NEGATIVO -19% vs valor intrínseco €15.30. Morningstar confirma "moderately overvalued". Precio actual €18.92 refleja ejecución perfecta, no hay margen para error.

**Quality high, price higher. Pass.**

---

## Checklist Investment Committee

### BÁSICO
- [x] Thesis completa: thesis/research/IBE/thesis.md
- [❌] **FALLA: Margen seguridad -19%** (requiere >25%)
- [x] Moat: Narrow-to-wide (redes reguladas 50% negocio)
- [x] Riesgos: Execution €58B capex, regulatory UK/US, interest rate sensitivity
- [x] Macro: Compatible (utilities EU oportunidad, pero Iberdrola excepción cara)

**RESULTADO: RECHAZADO** por margen seguridad insuficiente

### PORTFOLIO STRUCTURE V2.0
- [x] Sizing: 5% apropiado (Standard Defensive)
- [x] Sector: Utilities 5% OK (<25%)
- [x] Geografía: España/EU 5% OK (<35%)
- [x] Defensive: 0% → 5% (hacia target 35-40%) ✅
- [x] Cash: 68% post-compra (>>> 5% mínimo) ✅

**RESULTADO: PASA** estructura portfolio

### DECISIÓN FINAL

**Regla básica prioritaria:** Margen <25% = NO COMPRAR, independientemente de estructura.

**WATCHLIST** hasta corrección precio o validación premium justificado.

---

## Razones CONTRA Compra

1. **Margen seguridad NEGATIVO -19%**
   - Valor intrínseco base: €15.30 (P/E 18x sobre EPS €0.85)
   - Precio actual: €18.92
   - Requiere ejecución PERFECTA plan €58B capex para justificar precio
   - Value investing = comprar con margen ERROR, no asumir perfección

2. **Trading all-time highs**
   - +36% YoY, máximos desde 2012
   - P/E 21-24x vs histórico 14-18x → trading 30-50% premium a historia
   - P/E 21-24x vs sector EU 15-18x → 25-35% más cara que peers
   - P/E 21-24x vs Enel 9-15x → 50-100% más cara que competidor similar

3. **Morningstar: "Moderately overvalued"**
   - Analistas independientes confirman valuación alta
   - Consenso precio target €15.94 (15% downside actual)

4. **FCF bajo presión próximos 3 años**
   - FCF $4.6B 2024, cayendo -11% YoY
   - Capex plan €58B (€14.5B/año) vs FCF €4-5B/año
   - Gap financiación → equity raise probable (dilución 10-15%)
   - Dividendo 3.5% cubierto por earnings, NO por FCF → riesgo si capex delays

5. **Comparación con Enel desfavorable**
   - Enel: P/E 9-15x, yield 5%, LATAM risk SIMILAR
   - Iberdrola: P/E 21-24x, yield 3.5%
   - Si Enel quality comparable, está 50% más barato
   - NO JUSTIFICA pagar 2x múltiplo por mejor execution (premium razonable 15-20%, NO 100%)

---

## Razones A FAVOR (reconocidas pero insuficientes)

1. **Quality excelente (9/10)**
   - Moat narrow-to-wide (redes reguladas 50%)
   - Management: Guidance raised 3x 2025, profit +17%
   - Balance sólido: Debt/Eq 0.93x, Debt/EBITDA 3.6x
   - 85% inversión países rating A (disciplina capital allocation)

2. **Growth visible**
   - Net profit €6.6B (2025) → €7-8B (2028) = 8-10% CAGR
   - EBITDA €16B → €18B
   - Installed capacity 40 GW → 60 GW (+50%)

3. **Fit portfolio V2.0 perfecto**
   - Defensive value para llenar gap 35-40%
   - Utilities estables, drawdown -15-20% vs -35-45% cyclicals
   - Sizing 5% correcto

4. **Sector ignorado macro**
   - Utilities EU generalmente baratas (world view confirma)
   - Re-rating cuando BCE baje tipos (2027)

**PERO:** Quality high NO justifica pagar cualquier precio. Margen seguridad protege contra imprevistos.

---

## Triggers para Compra

### 1. Corrección Precio (PRINCIPAL)

**Target entrada:** €14.00-15.00

**Razón:**
- €15.00 = valor intrínseco base (P/E 18x) → margen seguridad 0%
- €14.00 = margen seguridad 20% → ACEPTABLE dado quality
- €13.50 = margen seguridad 25% → IDEAL

**Alerta configurar:** €15.00 (revisar), €14.00 (comprar probable)

### 2. Validación Execution Plan (SECUNDARIO)

**Evento:** Feb 25, 2026 - FY2025 earnings

**Validar:**
- Net profit ≥ €6.6B guidance (confirma track record)
- Capex 2025: ¿€14-15B deployed sin delays?
- GW additions: ¿5+ GW added? (necesario para 60 GW 2028)
- FCF trend: ¿Mejora o sigue cayendo?
- Guidance 2026: ¿Raised again?

**Si execution beats + guidance conservative → Re-valorar:**
- Quizás premium 20-25% justificado (P/E 19-20x)
- Fair value sube a €16-17
- Target entrada ajusta a €12-13 (margen 25%)

### 3. Catalizador Macro (TERCIARIO)

**Evento:** BCE baja tipos antes esperado (2026 vs 2027 consensus)

**Efecto:** Utilities re-rate, P/E sector sube a 18-20x

**Acción:** Si mercado general re-rates utilities, Iberdrola podría estar "fairly valued" a €18-19. Considerar entry solo si otros utilities suben más (oportunidad relativa).

---

## Configuración Sistema

### Watchlist

```yaml
watchlist:
  on_watch:
    - ticker: IBE.MC
      name: "Iberdrola S.A."
      target_price: 14.00-15.00
      current_price: 18.92
      current_thesis: thesis/research/IBE/thesis.md
      added_date: 2026-01-27
      reason_watch: "RECHAZADO - Quality excelente (9/10) PERO margen seguridad -19% (requiere >25%). Precio refleja perfección, no hay margen error. Esperar corrección a €14-15 (margen 20-25%)."
      triggers_to_buy:
        - "Precio cae a €14-15 (margen seguridad 20-25%)"
        - "FY2025 earnings (25-feb) beats + guidance raised → re-valorar si premium justificado"
        - "BCE baja tipos antes esperado → utilities re-rate"
      alerts:
        - type: price
          condition: below
          target: 15.00
          action: "Revisar para compra - margen seguridad 0-20%"
        - type: price
          condition: below
          target: 14.00
          action: "COMPRAR - margen seguridad 20%+"
        - type: earnings
          date: "2026-02-25"
          event: "FY2025 earnings"
          action: "Validar execution plan €58B capex, FCF trend, guidance 2026"
      notes: "Líder EU utilities, moat narrow-to-wide redes reguladas 50%, management excelente (guidance raised 3x). PERO P/E 21-24x vs Enel 9-15x, Morningstar 'overvalued', FCF -11% por capex masivo. Comparar con Enel antes de comprar."
      priority: medium
```

### Calendario

```yaml
calendar:
  events:
    - date: 2026-02-25
      type: earnings
      ticker: IBE.MC
      event: "Iberdrola FY2025 earnings"
      priority: medium
      action: "Validar execution: net profit €6.6B+, capex €14-15B deployed, 5+ GW added, FCF trend, guidance 2026"
      context: "Watchlist - Si beats + guidance conservative → re-valorar premium. Si miss → descartar."
```

---

## Próximos Pasos

1. **Comparar Enel vs Iberdrola side-by-side**
   - Enel P/E 9-15x vs IBE 21-24x (50-100% cheaper)
   - Enel yield 5% vs IBE 3.5%
   - Enel LATAM risk vs IBE LATAM risk (Brasil ambos)
   - ¿Quality gap justifica 2x múltiplo? Probablemente NO
   - **Decisión:** Si Enel comparable → comprar Enel antes que Iberdrola

2. **Continuar construcción defensive**
   - Target: 7-8 posiciones defensive (35-40% portfolio)
   - Actual: 0 posiciones
   - Gap: Necesito 7-8 posiciones €350-500 cada una
   - Sectores: Utilities, staples, pharma/healthcare
   - **Siguiente:** Analizar Enel (earnings feb 1) o explorar otras utilities EU/global

3. **Monitorear Iberdrola pasivamente**
   - Alerta precio €15 y €14
   - Earnings feb 25
   - NO dedicar más tiempo hasta trigger activa

---

## Lecciones

1. **Quality ≠ Precio correcto**
   - Iberdrola es TOP quality utility EU
   - PERO precio refleja perfección → no es value
   - Value = quality + margen seguridad, ambos requeridos

2. **Comparación relativa crítica**
   - Iberdrola "cara" solo evidente comparando con Enel
   - Siempre buscar 2-3 opciones antes de comprar
   - Explorar sector completo, no enamorarse primera opción

3. **Timing importa**
   - Comprar en all-time highs raramente es value
   - Paciencia: esperar corrección o catalizador
   - Cash alto (73%) permite esperar oportunidad correcta

4. **Premium quality tiene límite**
   - Premium 15-20% razonable para mejor execution/moat
   - Premium 50-100% (como Iberdrola vs Enel) requiere justificación extraordinaria
   - Iberdrola NO es 2x mejor que Enel

---

## Autocrítica Decisión

**¿Sesgo anti-Iberdrola?**
- ⚠️ Riesgo: Rechazar empresa excelente por precio, perder re-rating
- ✅ Mitigado: Watchlist configurada, triggers claros, volveré si corrige

**¿Premium realmente injustificado?**
- 🔍 Bull case: Si Iberdrola mantiene premium histórico 10-15%, fair value €16-17
- 🔍 Histórico: Iberdrola traded 14-18x P/E típicamente, 21-24x es OUTLIER
- ✅ Conclusión: Premium actual 30-50% vs histórico SÍ es excesivo

**¿Debería comprar pequeña posición "starter"?**
- ❌ NO: V2.0 requiere sizing disciplinado (4-7% posiciones)
- ❌ NO: "Starter position" = timing market, no es value investing
- ✅ Correcto: Esperar precio correcto, comprar full 5% allocation directamente

**Decisión final validada:** WATCHLIST es correcta. Continuar con Enel o explorar alternativas.
