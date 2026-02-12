# Capital Deployment Machine Pipeline

> **PRIORIDAD #1** mientras cash > 25% del portfolio.
> Mas importante que vigilance, rotation-check, o cualquier otro pipeline.
> Framework v4.0 - Principios Adaptativos.

---

## Trigger

**Activacion:** Cash > 25% del portfolio total.
**Desactivacion:** Cash < 15% O pipeline tiene 15+ thesis listas.
**Frecuencia:** CADA SESION (diario, primera prioridad).

---

## Objetivo

Transformar cash idle en posiciones de Quality Compounders (Tier A, QS >= 75).
El sistema debe ser una MAQUINA que:
1. Conoce TODAS las empresas de calidad del universo invertible
2. Monitoriza TODAS para detectar oportunidades de precio
3. Tiene thesis pre-escritas para actuar en horas, no dias
4. Nunca pierde una oportunidad porque "no habiamos analizado esa empresa"

---

## Quality Universe (state/quality_universe.yaml)

Base de datos persistente de empresas con QS >= 65 (candidatas a pipeline).

### Estructura

```yaml
companies:
  - ticker: PAYC
    name: Paycom Software
    qs_tool: 85
    qs_adj: 85
    tier: A
    sector: HCM/Payroll
    fair_value: 200  # USD
    entry_price: 100  # USD
    currency: USD
    pipeline_status: R1_COMPLETE  # UNSCREENED | SCORED | R1_COMPLETE | R2_COMPLETE | APPROVED | REJECTED
    thesis_path: thesis/research/PAYC/thesis.md
    last_scored: 2026-02-11
    notes: "Zero debt, 91% retention, EBITDA 43%"
```

### Pipeline Status Progression

```
UNSCREENED → SCORED → R1_COMPLETE → R2_COMPLETE → R3_COMPLETE → APPROVED → STANDING_ORDER
                ↓                                                    ↓
            REJECTED                                             REJECTED
```

### Tool: quality_universe.py

```bash
python3 tools/quality_universe.py report              # Full universe con precios actuales
python3 tools/quality_universe.py actionable           # Empresas dentro del 15% del entry
python3 tools/quality_universe.py add TICKER --qs 75 --fv 200 --entry 150 --sector "Tech"
python3 tools/quality_universe.py remove TICKER
python3 tools/quality_universe.py coverage             # Gaps de cobertura sectorial
python3 tools/quality_universe.py refresh              # Update precios (batch)
```

---

## Fases del Pipeline

### FASE A: Universe Building (one-time, refresh mensual)

**Objetivo:** Mapear TODAS las empresas QS >= 65 del universo invertible.
**Target:** 150-300 empresas en quality_universe.yaml.

| Paso | Accion | Herramienta | Cadencia |
|------|--------|-------------|----------|
| A1 | Screen indices US (sp500+sp400+russell1000) | dynamic_screener.py | Mensual |
| A2 | Screen indices EU (stoxx600+europe_all) | dynamic_screener.py | Mensual |
| A3 | Screen indices UK (ftse100+ftse250) | dynamic_screener.py | Mensual |
| A4 | Screen Nordic (omx_stockholm+nordic) | dynamic_screener.py | Mensual |
| A5 | quality_scorer.py en batches de 5-8 | quality_scorer.py | Por batch |
| A6 | Almacenar en quality_universe.yaml | quality_universe.py add | Tras scoring |

**Anti-bias:** Usar --undiscovered flag. No depender de "empresas que conozco".
**Rate limit:** Max 5-8 tickers por batch de quality_scorer. Espaciar 30s entre batches.

### FASE B: Price Sweep (cada sesion)

**Objetivo:** Detectar CUALQUIER empresa QS >= 70 que entre en zona de compra.

| Paso | Accion | Herramienta |
|------|--------|-------------|
| B1 | Refresh precios del quality universe | quality_universe.py refresh |
| B2 | Filtrar: distancia a entry < 15% | quality_universe.py actionable |
| B3 | Cross-reference con thesis existentes | Orchestrator |
| B4 | ALERTA si Tier A en zona de entry | Orchestrator → humano |

**Criterio "actionable":** Precio actual dentro del 15% del entry price.
**Criterio "execute":** Precio actual <= entry price + thesis aprobada + standing order.

### FASE C: Analysis Factory (cada sesion, paralelo)

**Objetivo:** Mantener 15-20 thesis listas para ejecucion rapida.
**Meta:** Producir 2-3 R1 por sesion.

| Paso | Accion | Agentes | Cadencia |
|------|--------|---------|----------|
| C1 | Priorizar candidatos por QS x proximidad x catalizador | Orchestrator | Cada sesion |
| C2 | Lanzar 2-3 R1 en paralelo | fundamental-analyst + moat-assessor + risk-identifier | Cada sesion |
| C3 | Valuation post-R1 | valuation-specialist | Secuencial tras C2 |
| C4 | Almacenar en quality_universe con status R1_COMPLETE | quality_universe.py | Tras C3 |

**Prioridad de analisis:**
1. Tier A con precio cerca de entry (< 20% away)
2. Tier A con catalizador proximo (earnings, guidance)
3. Tier A recien descubierto (screening nuevo)
4. Tier B excepcional (QS 70-74 con moat wide)

### FASE D: Sector Coverage (sistematico)

**Objetivo:** Sector view para TODOS los sectores GICS relevantes.
**Meta:** 2 sectores nuevos por sesion hasta cobertura 100%.

| Sector | Status | Sector View |
|--------|--------|-------------|
| Telecom | CUBIERTO | telecom.md |
| Insurance | CUBIERTO | insurance.md |
| Pharma/Healthcare | CUBIERTO | pharma-healthcare.md |
| Real Estate | CUBIERTO | real-estate.md |
| Business Services | CUBIERTO | business-services.md |
| Consumer Staples | CUBIERTO | consumer-staples.md |
| Industrials | CUBIERTO | industrials.md |
| Utilities | CUBIERTO | utilities.md |
| Energy | PARCIAL | energy.md (WARNING) |
| Media/Publishing | CUBIERTO | media-publishing.md |
| Technology | CUBIERTO | technology.md |
| Financial Data | CUBIERTO | financial-data-analytics.md |
| Luxury Goods | CUBIERTO | luxury-goods.md |
| Industrial Technology | PENDIENTE | Screening en curso |
| Testing/Inspection/Cert | PENDIENTE | Screening en curso |
| Semiconductors/Equipment | PENDIENTE | - |
| Defense/Aerospace | PENDIENTE | - |
| Healthcare Equipment | PENDIENTE | - |
| Professional Services | PENDIENTE | - |
| Payments/Fintech | PENDIENTE | - |
| Environmental/Water | PENDIENTE | - |
| Consumer Brands | PENDIENTE | - |
| Digital Infrastructure | PENDIENTE | - |

**Agente:** sector-screener (SIEMPRE, nunca manual).

### FASE E: Execution Readiness (event-driven)

**Objetivo:** De senal de precio a recomendacion en HORAS, no dias.

```
TRIGGER: Precio toca entry de empresa con pipeline status >= R1_COMPLETE

SI R1_COMPLETE:
  → Lanzar R2 (devil's-advocate) INMEDIATAMENTE
  → R3 (conflictos) misma sesion
  → R4 (investment-committee 10 gates) misma sesion
  → Presentar al humano para ejecutar
  → Sizing via position-calculator

SI APPROVED (standing order existe):
  → Informar al humano: EJECUTAR
  → Post-ejecucion: portfolio-ops actualiza sistema

SI SCORED (solo QS, sin R1):
  → Lanzar R1 completa (3 agentes paralelo + valuation)
  → Si resultados positivos: continuar con R2-R4
  → Target: thesis completa en 1-2 sesiones
```

---

## Metricas de Salud del Pipeline

| Metrica | Target | Alerta |
|---------|--------|--------|
| Thesis listas (R1+) | >= 15 | < 10 = pipeline debil |
| Thesis aprobadas (R4+) | >= 8 | < 5 = execution pipeline debil |
| Standing orders activos | >= 10 | < 6 = pocos triggers |
| Sectores cubiertos | >= 18 | < 15 = gaps de cobertura |
| Universe size (QS > 65) | >= 150 | < 50 = universe incompleto |
| Actionable (< 15% entry) | >= 5 | 0 = mercado caro, paciencia |

---

## Integracion con Otros Pipelines

```
INICIO DE SESION (mientras cash > 25%):

1. CAPITAL-DEPLOYMENT:
   a. quality_universe.py actionable → algo cerca de entry?
   b. Si hay actionable → priorizar analisis/ejecucion
   c. Si no hay → FASE C (2-3 R1 nuevas) + FASE D (sector nuevo)

2. VIGILANCE (en paralelo):
   a. news-monitor + market-pulse
   b. Si noticia CRITICA afecta pipeline → ajustar

3. ROTATION-CHECK:
   a. forward_return.py → bottom 3 candidates for rotation
   b. Cross-reference con pipeline: hay Tier A de reemplazo?

4. Resto de pipelines segun cadencia
```

---

## Principios v4.0 Aplicados

- **Principio 4 (Cash como Posicion Activa):** 44% cash es suboptimo. Este pipeline lo soluciona.
- **Principio 9 (Quality Gravitation):** Solo desplegar en Tier A (QS >= 75).
- **Principio 7 (Consistencia):** Precedentes de sizing: 3-5% Tier A (ADBE 4.8%, NVO 3.4%).
- **Anti-bias:** NUNCA sugerir de "conocimiento implicito". SIEMPRE systematic screening.
- **Paciencia:** No desplegar por presion. Solo cuando calidad + MoS justifican.

---

## Razonamiento sobre Cash Level

NO hay un "target" fijo de cash. Hay razonamiento:

```
Cash 44% AHORA es aceptable porque:
- Post-adversarial: vendimos 8 posiciones para preservar capital (correcto)
- Pipeline tiene 6 candidatos pero todos sobre entry (paciencia)
- Mercado no ofrece calidad con descuento suficiente (paciencia = alpha)

Cash 44% DEJA de ser aceptable cuando:
- Pipeline tiene < 10 thesis listas (no es problema de mercado, es problema NUESTRO)
- Llevamos > 3 meses sin desplegar nada (coste oportunidad real)
- No estamos haciendo screening activo (inaccion injustificada)
```

**La diferencia:** Cash alto por falta de oportunidades = correcto. Cash alto por falta de analisis = error nuestro.

---

**Creado:** 2026-02-12
**Framework:** v4.0
