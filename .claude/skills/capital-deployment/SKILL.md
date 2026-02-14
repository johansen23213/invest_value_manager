# Capital Deployment Machine Pipeline

> **PRIORIDAD #1** mientras cash > 25% del portfolio.
> Framework v4.0 - Principios Adaptativos.
> El universe es un ORGANISMO VIVO, no una lista estática.

---

## Trigger

**Activacion:** Cash > 25% del portfolio total.
**Desactivacion:** Nunca se desactiva completamente — el universe siempre necesita mantenimiento.
**Intensidad:** Con cash > 25%, priorizar análisis nuevos. Con cash < 15%, mantener universe pero sin urgencia.

---

## Objetivo

El sistema conoce TODAS las empresas de calidad del universo invertible.
Cuando cualquier empresa de calidad cae a precio atractivo, tenemos thesis lista para actuar en horas.

Esto requiere un **ciclo continuo** — no un proyecto que se "completa":

```
SCREENING → SCORING → THESIS → MONITORING → RE-SCORING → SALIDA/MANTENIMIENTO
     ↑                                                          |
     └──────────────────────────────────────────────────────────┘
```

**El universe nunca está "terminado".** Empresas entran, salen, se re-evalúan, se actualizan.
Yo puedo trabajar en esto cada sesión sin cansarme. No hay excusa para tener gaps.

---

## Quality Universe (state/quality_universe.yaml)

Base de datos persistente de empresas con QS >= 65 (candidatas a pipeline).
**Target mínimo: 150+ empresas.** Pero de calidad — nunca meter relleno por alcanzar un número.

### Estructura

```yaml
companies:
  - ticker: PAYC
    name: Paycom Software
    qs_tool: 85
    qs_adj: 75
    tier: A
    sector: HCM/Payroll
    fair_value: 115
    entry_price: 92
    currency: USD
    pipeline_status: R3_COMPLETE
    thesis_path: thesis/research/PAYC/thesis.md
    last_scored: 2026-02-13
    notes: "R3 resolution: QS 85->75, FV $130->$115"
```

### Pipeline Status Progression

```
UNSCREENED → SCORED → R1_COMPLETE → R2_COMPLETE → R3_COMPLETE → APPROVED → STANDING_ORDER
                ↓                                                    ↓
            REJECTED                                             REJECTED
                                                                     ↓
                                                                 STALE (needs refresh)
```

### Tool: quality_universe.py

```bash
python3 tools/quality_universe.py report              # Full universe con precios actuales
python3 tools/quality_universe.py actionable           # Empresas dentro del 15% del entry
python3 tools/quality_universe.py add TICKER --qs 75 --fv 200 --entry 150 --sector "Tech"
python3 tools/quality_universe.py remove TICKER
python3 tools/quality_universe.py coverage             # Gaps de cobertura sectorial
python3 tools/quality_universe.py refresh              # Update precios (batch)
python3 tools/quality_universe.py stale                # Empresas que necesitan re-evaluación
python3 tools/quality_universe.py stats                # Métricas de salud del pipeline
```

---

## Ciclo de Vida del Universe (CONTINUO)

### ENTRADA: Cómo entran empresas

| Fuente | Método | Filtro |
|--------|--------|--------|
| Screening de índices | dynamic_screener.py | QS >= 65 via quality_scorer.py |
| Sector deep-dives | sector-screener agent | Candidatas de sector views |
| Oportunidades detectadas | opportunity-hunter, news | Empresas que caen fuerte con calidad |
| Conocimiento propio | VALIDAR con datos | Anti-popularity-bias: solo si pasa screening |

**Anti-bias:** Usar --undiscovered flag. No depender de "empresas que conozco".

### MANTENIMIENTO: Cómo se mantienen vivas

Cada sesión, como parte natural del flujo:
- **Mirar qué está stale** — `quality_universe.py stale` muestra qué necesita atención
- **Re-evaluar unas pocas** — re-ejecutar quality_scorer, verificar si FV/entry siguen vigentes
- **Actualizar precios** — `quality_universe.py refresh` para ver proximidad a entry
- No hace falta hacer todo cada sesión — pero algo siempre

**Staleness:** Una empresa sin re-evaluar pierde fiabilidad progresivamente.
No hay un "límite de meses" fijo — uso juicio: si hubo earnings, cambio regulatorio,
o cambio material, re-evaluar antes. Si nada cambió, puede esperar más.

### SALIDA: Cómo salen empresas

| Razón | Acción |
|-------|--------|
| QS cae < 65 en re-evaluación | Remover del universe |
| Kill condition activada | Remover + documentar |
| Sector se deteriora estructuralmente | Re-evaluar todas las del sector |
| Empresa comprada → portfolio | Mover a posición activa |
| Thesis rechazada en R4 | Marcar REJECTED, mantener para referencia |

---

## Fases de Trabajo (cada sesión)

### FASE A: Price Sweep (rápido, cada sesión)

```bash
python3 tools/quality_universe.py actionable
```

- ¿Algo cerca de entry? → Priorizar análisis/ejecución
- ¿Algo recién llegado a zona? → Alerta

### FASE B: Analysis Factory (si hay candidatos)

Prioridad de análisis:
1. Tier A con precio cerca de entry (< 20% away)
2. Tier A con catalizador próximo (earnings, guidance)
3. Tier A recién descubierto (screening nuevo)
4. Tier B excepcional (QS 70-74 con moat wide)

Agentes: fundamental-analyst + moat-assessor + risk-identifier (PARALELO) → valuation-specialist

### FASE C: Universe Expansion (continuo)

- Screenear sectores con gaps (coverage command)
- Añadir empresas de calidad descubiertas
- No hay "2 sectores por sesión" fijo — hacer lo que tenga sentido ese día

### FASE D: Universe Maintenance (continuo)

- Re-evaluar empresas stale
- Actualizar FV/entry tras earnings
- Quitar empresas que se deterioraron
- Verificar que thesis existentes siguen vigentes

### FASE E: Execution Readiness (event-driven)

```
TRIGGER: Precio toca entry de empresa con pipeline status >= R1_COMPLETE

SI R1_COMPLETE:
  → Lanzar R2 (devil's-advocate) INMEDIATAMENTE
  → R3 (conflictos) misma sesión
  → R4 (investment-committee 10 gates) misma sesión
  → Presentar al humano para ejecutar

SI APPROVED (standing order existe):
  → Informar al humano: EJECUTAR
  → Post-ejecución: portfolio-ops actualiza sistema

SI SCORED (solo QS, sin R1):
  → Lanzar R1 completa (3 agentes paralelo + valuation)
  → Si resultados positivos: continuar con R2-R4
```

---

## Métricas de Salud (datos crudos, sin juicios fijos)

| Métrica | Dato |
|---------|------|
| Universe size (QS >= 65) | Cuántas empresas mapeadas |
| Tier A count | Cuántas QS >= 75 |
| Thesis listas (R1+) | Cuántas con análisis hecho |
| Thesis aprobadas (R4+) | Cuántas listas para ejecutar |
| Standing orders activos | Cuántos triggers listos |
| Sectores cubiertos | Cuántos de 23 GICS |
| Actionable (< 15% entry) | Cuántas cerca de precio |
| Stale (sin re-eval reciente) | Cuántas necesitan atención |

El target de 150 empresas es un **piso mínimo de cobertura**, no un techo.
Tener 200 o 300 es mejor. Pero siempre de calidad — nunca relleno.

---

## Sector Coverage

| Sector | Status |
|--------|--------|
| Telecom | VIEW |
| Insurance | VIEW |
| Pharma/Healthcare | VIEW |
| Real Estate | VIEW |
| Business Services | VIEW |
| Consumer Staples | VIEW |
| Industrials | VIEW |
| Utilities | VIEW |
| Energy | VIEW |
| Media/Publishing | VIEW |
| Technology | VIEW + COMPANIES |
| Financial Data | VIEW + COMPANIES |
| Luxury Goods | VIEW + COMPANIES |
| Industrial Technology | VIEW + COMPANIES |
| Payments/Fintech | VIEW + COMPANIES |
| Testing/Inspection/Cert | COMPANIES ONLY |
| Semiconductors/Equipment | GAP |
| Defense/Aerospace | GAP |
| Healthcare Equipment | GAP |
| Professional Services | GAP |
| Environmental/Water | GAP |
| Consumer Brands | VIEW |
| Digital Infrastructure | VIEW |

**"VIEW" sin COMPANIES = trabajo pendiente.** La sector view existe pero no se han mapeado empresas QS >= 65.

---

## Principios v4.0 Aplicados

- **Principio 4 (Cash como Posición Activa):** Cash alto por falta de oportunidades = correcto. Cash alto por falta de análisis = error nuestro.
- **Principio 9 (Quality Gravitation):** Priorizar Tier A (QS >= 75) para despliegue.
- **Anti-bias:** NUNCA sugerir de "conocimiento implícito". SIEMPRE systematic screening.
- **Paciencia:** No desplegar por presión. Solo cuando calidad + MoS justifican.
- **Autonomía:** Yo opero esto cada sesión. No espero a que me lo pidan. No pongo cadencias fijas.

---

**Creado:** 2026-02-12
**Actualizado:** 2026-02-13 (v2.0 — universe como organismo vivo, sin cadencias fijas)
