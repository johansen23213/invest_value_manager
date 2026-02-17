# Sistema Completo — Brief de Implementación

> **PARA:** Mi yo futuro (Claude en próxima sesión)
> **OBJETIVO:** Tener TODO el contexto para implementar sin preguntar nada
> **ORIGEN:** Conversación Session 73 (2026-02-17) con el humano
> **DOCUMENTOS RELACIONADOS:** `docs/short_selling_framework_design.md` (diseño detallado de shorts, 1238 líneas)
> **ESTADO:** DISEÑO APROBADO POR EL HUMANO. Pendiente implementación.
>
> **PRINCIPIO RECTOR DE ESTE DOCUMENTO:**
> Los tools que se construyan outputan DATOS CRUDOS, nunca juicios ni etiquetas.
> Las decisiones se razonan desde `learning/principles.md` y precedentes (`learning/decisions_log.yaml`).
> NO hay reglas fijas, umbrales fijos, ni números mágicos. Solo principios + datos + razonamiento.

---

## 1. CONTEXTO Y PREOCUPACIONES DEL HUMANO

### Qué disparó esta conversación

El humano leyó el documento de short selling framework (Session 73 previa, inspirada por "The Big Short") y preguntó sobre el reverse DCF. La conversación evolucionó hacia cuestiones más profundas sobre el sistema completo.

### Preocupación #1: Standing orders no funcionan como están diseñados

> "Los standing orders están diseñados para que cuando un ticker toque el precio yo pueda ya comprar sin preguntarte, pero esto no va a pasar nunca, porque yo no tomaré decisiones sin antes preguntarte a ti"

**Realidad:** El humano NUNCA ejecutará un standing order sin consultar a Claude primero. El diseño actual de "ejecución autónoma" es ficción. En la práctica son alertas de precio, no órdenes.

### Preocupación #2: Análisis viejos

> "También me preocupa que tengamos un standing order de un análisis hecho hace 3 meses y comprar inmediatamente sin revisar tampoco me da confianza"

**Realidad:** Tenemos 22 standing orders. Algunos tendrán meses de antigüedad cuando el precio toque el trigger. El mundo cambia. Comprar con análisis viejo sin revalidar es imprudente.

### Preocupación #3: ¿Cómo ayuda todo esto al despliegue de capital?

El humano preguntó si el reverse DCF ayuda con el cash drag (60.8% cash). Respuesta:
- **SÍ:** Prioriza dónde el gap es mayor, valida triggers, mata falsos candidatos rápido
- **NO:** No mueve los precios. Pero si descubre que nuestros triggers son demasiado exigentes, eso sí acelera el despliegue
- **CLAVE:** Si corremos reverse DCF sobre los 22 standing orders y descubrimos que el mercado ya implica pesimismo extremo a precios ACTUALES (no solo al trigger), podríamos razonar que comprar antes del trigger está justificado

### Preocupación #4: ¿Cómo sabes si el mercado tiene razón o no?

La respuesta honesta: NO lo sabemos con certeza. Pero apilamos evidencia con 4 filtros (ver sección 3). Es un juego de probabilidades con asimetría favorable, no de certezas.

---

## 2. LA PREGUNTA CENTRAL + REVERSE DCF

### Concepto

Todo empieza con una pregunta: **"¿Dónde se equivoca el mercado?"**

El mercado pone un precio a cada empresa. Ese precio IMPLICA asunciones sobre el futuro. Si esas asunciones son incorrectas → oportunidad.

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   "¿DÓNDE SE EQUIVOCA EL MERCADO?"                     │
│                                                         │
│   Herramienta: REVERSE DCF                              │
│   Input: precio actual + datos de la empresa            │
│   Output: "el mercado asume X% de crecimiento"          │
│                                                         │
└─────────────────────┬───────────────────────────────────┘
                      │
          ┌───────────┼───────────────┐
          ▼           ▼               ▼
    INFRAVALORA     TIENE RAZÓN     SOBREVALORA
    (asume peor     (no hay gap)    (asume mejor
     de lo real)                     de lo real)
          │               │               │
          ▼               ▼               ▼
     CANDIDATO        IGNORAR        CANDIDATO
       LONG          (no operar)       SHORT
```

### Cómo funciona el cálculo

**DCF normal:** Tú asumes crecimiento → calculas precio justo
**Reverse DCF:** Tomas el precio del mercado → calculas qué crecimiento implica

```
DATOS DE ENTRADA (todos observables, no opiniones):
  Precio actual:           $150
  Shares outstanding:      100M
  → Market Cap:            $15,000M
  + Deuda neta:            $2,000M
  → Enterprise Value:      $17,000M
  FCF actual (último año): $500M
  WACC:                    9%
  Terminal growth:         2.5%

ECUACIÓN:
  EV = Σ [FCF × (1+g)^n / (1+WACC)^n] + Terminal Value

  Todo conocido EXCEPTO "g" (growth rate).
  Resolver por iteración:

  ¿g = 10%? → DCF = $22,000M → demasiado alto
  ¿g = 5%?  → DCF = $16,000M → casi
  ¿g = 4.2%? → DCF = $17,000M → MATCH

OUTPUT: "El mercado implica crecimiento del 4.2% anual"
```

Ahora comparas 4.2% con la realidad (histórico 15%, sector 8%, consenso 12%) y decides si el mercado se equivoca.

### Variantes del cálculo

```
VARIANTE 1: Resolver para GROWTH (la más común)
  "¿A cuánto tiene que crecer para justificar el precio?"

VARIANTE 2: Resolver para MARGEN
  Fijas growth = consenso, resuelves qué FCF margin implica
  "Si crece al 10%, el mercado asume FCF margin 14% vs 22% actual"

VARIANTE 3: Resolver para TERMINAL MULTIPLE
  "¿Qué P/E terminal asume el mercado en año 10?"
  Si implica P/E 8x para empresa QS 80 → absurdo

VARIANTE 4: ESCENARIOS / PROBABILIDADES IMPLÍCITAS
  Si bear = $100, bull = $300, precio = $150
  → mercado pondera 75% bear, 25% bull
  ¿Estás de acuerdo con esas probabilidades?
```

---

## 3. LOS 4 FILTROS — "¿Tiene razón el mercado o no?"

Nunca lo sabemos con certeza. Pero apilamos evidencia:

### Filtro 1: ¿Qué asume el mercado y POR QUÉ?

El reverse DCF da el QUÉ. Ahora necesitas el POR QUÉ.

```
ADBE a $264 → mercado implica crecimiento 3-4%

¿Por qué?
  → Narrativa: "AI reemplaza a Adobe"
  → Sentiment: SaaS selloff general
  → Miedo: ChatGPT, Midjourney

¿Es RAZÓN o EMOCIÓN?
  → ¿Adobe pierde clientes? NO (revenue +10%)
  → ¿Firefly falla? NO (70M+ MAU)
  → ¿Miedo específico o genérico? GENÉRICO (todo SaaS cae)

Cuando el miedo es GENÉRICO y los datos ESPECÍFICOS lo contradicen
→ alta probabilidad de que el mercado se equivoca
```

### Filtro 2: ¿Quién opina y cuánto le cuesta equivocarse?

```
Los que venden: retail, ETFs rebalanceando, algos
  → Coste de equivocarse: NADA (venden y se olvidan)

Los que compran: Cantillon Capital (+157K shares), insiders
  → Coste de equivocarse: MUCHO (dinero real en juego)

Cuando gente con skin in the game compra
y gente sin skin in the game vende
→ señal de que el mercado probablemente se equivoca
```

### Filtro 3: ¿Datos primarios vs narrativa?

```
NARRATIVA: "AI destruye Adobe"

DATOS PRIMARIOS:
  • Revenue: +10% YoY (creciendo)
  • FCF margin: 35%+ (no se comprime)
  • Firefly: 70M+ MAU
  • Renewal rates: 95%+
  • 10-K: no menciona pérdida de clientes por AI

Si narrativa dice una cosa y datos dicen otra
→ a largo plazo, los datos ganan
```

### Filtro 4: ¿Cuánto me cuesta estar equivocado?

```
Incluso con los 3 filtros, PUEDO estar equivocado.

Pero si:
  • Compro a P/E 15x (históricamente 30x)
  • FCF $7B cubre si todo va mal
  • Sin deuda relevante
  • Peor caso: -20% → pierdo ~1% del portfolio

Coste de equivocarme: BAJO
Beneficio de acertar: ALTO
→ Apuesta asimétrica favorable

No necesito SABER que tengo razón.
Necesito que la apuesta sea asimétrica.
```

---

## 4. REDISEÑO DE STANDING ORDERS

### Antes (diseño actual, no funciona)

```
Precio toca trigger → Humano compra en eToro → Siguiente sesión actualiza
```

### Después (diseño realista)

```
Precio toca trigger → Alerta al humano → Humano avisa a Claude →

  FAST-TRACK VALIDATION:
  1. ¿Thesis sigue vigente? (¿algo cambió desde que se escribió?)
  2. ¿Noticias recientes que afecten?
  3. ¿Kill conditions / Hard gates?
  4. Reverse DCF a precio actual: ¿gap sigue?
  5. ¿Restricciones de portfolio?
  6. ¿Capital allocation óptima?

  TODO OK → COMPRAR → Humano ejecuta
  ALGO FALLA → RE-EVALUAR (rápido, no pipeline completo)
  THESIS MUERTA → CANCELAR standing order
```

### Cambios concretos a implementar

1. **Standing orders = alertas de precio con thesis pre-escrita**, no órdenes autónomas
2. **Principio de frescura:** cuanto más tiempo ha pasado desde el análisis, más importante es revalidar antes de actuar. Razonar sobre si algo material ha cambiado (earnings, macro, competencia, regulación)
3. **Fast-track validation** antes de toda ejecución (skill pre-execution-check extendido)
4. **Reverse DCF en la validación:** confirmar que el gap sigue existiendo al precio actual

---

## 5. FLUJO COMPLETO DEL SISTEMA

### Ciclo anual

```
CADA TRIMESTRE (4x/año):
  → Reverse DCF scan del universo completo (76+ empresas)
  → Identificar gaps nuevos
  → Priorizar para pipeline

CADA EARNINGS SEASON (4x/año):
  → Frameworks pre-earnings para posiciones + pipeline
  → Post-earnings: ¿thesis confirma o cambia?
  → Revalidar standing orders afectados

CONTINUO:
  → Monitoreo diario (noticias, precios, kill conditions)
  → Rebalanceo mensual (rotation check)
  → Pipeline avanzando (candidatos moviéndose por R1→R4)
  → Standing orders vigilados
```

### Cadencia mensual (orientativa, no prescriptiva)

```
Las cuatro actividades que ocurren naturalmente cada mes:
  • ESCANEO:    Reverse DCF sobre universo, ¿nuevos gaps?
  • PIPELINE:   Avanzar candidatos R1→R4
  • MONITOREO:  Posiciones activas, kill conditions
  • REBALANCEO: Forward return, rotation, optimización

No hay orden fijo ni calendario rígido. Se priorizan según contexto
(earnings season cambia el ritmo, crisis acelera monitoreo, etc.)
```

### Pipeline de "idea" a "dinero invertido"

```
REVERSE DCF SCAN → GAP DETECTADO
         │
    ┌────┴────┐
    ▼         ▼
  LONG      SHORT
    │         │
    ▼         ▼
PIPELINE    PIPELINE
R1→R4       S1→S4
    │         │
    ▼         ▼
STANDING    STANDING
ORDER       ORDER SHORT
    │         │
    ▼         ▼
PRECIO TOCA TRIGGER
    │
    ▼
FAST-TRACK VALIDATION (6 checks)
    │
    ▼
HUMANO CONFIRMA → EJECUTA EN eToro
```

### Rebalanceo y rotación

```
Forward return de cada posición → comparar con pipeline

Preguntas que informan la decisión (no reglas mecánicas):
  • ¿Alguna posición tiene forward return significativamente menor que candidatos del pipeline?
  • ¿La diferencia justifica los costes y riesgos de rotar?
  • ¿La posición bottom tiene catalizadores pendientes que podrían cerrar el gap?

Reverse DCF como contexto adicional:
  "¿El bottom realmente no tiene gap? ¿O debería mantener?"
  "¿El top realmente tiene gap? ¿O el mercado tiene razón?"

La decisión se razona desde principios, no se ejecuta mecánicamente.
```

### Ciclo anti-cíclico (crisis)

```
Concepto: los shorts pueden generar cash CUANDO más se necesita.

Secuencia lógica (no prescriptiva):
  1. Reverse DCF detecta sobrevaloración extrema en sector X
  2. Pipeline short S1→S4 confirma fragilidad fundamental
  3. Abrir short — sizing razonado desde principios y contexto
  4. Si el sector colapsa → short genera retorno
  5. Cubrir short → CASH disponible
  6. Quality compounders caen por contagio (mercado no discrimina)
  7. Alertas de precio se activan
  8. Fast-track → razonar si comprar o esperar
  9. Si se compra → beneficio de entrada en crisis

La idea no es un playbook mecánico — es entender que los shorts
pueden convertir una crisis en oportunidad de compra. El sizing y
timing se razonan en cada situación concreta.
```

---

## 6. QUÉ CONSTRUIR — Tools, Skills, Agents

### TOOLS NUEVOS (3)

**Tool 1: `implied_expectations.py`** — EL CORAZÓN DEL SISTEMA

```
Uso:
  python3 tools/implied_expectations.py TICKER
  python3 tools/implied_expectations.py TICKER --detailed
  python3 tools/implied_expectations.py TICKER1 TICKER2 TICKER3

Input (automático via yfinance):
  • Precio actual, shares outstanding
  • Deuda neta (deuda total - cash)
  • FCF último año (o promedio 3 años)
  • WACC estimado

Output:
  ┌──────────────────────────────────────────────────────┐
  │  TICKER: ROP                                         │
  │  Price: $321 | EV: $52.4B | FCF: $2.1B              │
  │  WACC: 8.5% | Terminal growth: 2.5%                  │
  │                                                      │
  │  IMPLIED EXPECTATIONS:                                │
  │    Revenue growth:  4.1% /yr (10yr)                  │
  │    FCF growth:      3.8% /yr (10yr)                  │
  │    Terminal P/FCF:  18.2x                             │
  │                                                      │
  │  HISTORICAL CONTEXT:                                 │
  │    Historical rev growth (5yr):  12.3% /yr           │
  │    Historical FCF growth (5yr):  14.1% /yr           │
  │    Analyst consensus growth:     8-10% /yr           │
  │                                                      │
  │  GAP: Implied 4.1% vs historical 12.3%               │
  │                                                      │
  │  SCENARIO MATH:                                      │
  │    If gap closes: +47%                               │
  │    If market correct: -15%                           │
  │    Ratio: 3.1:1                                      │
  │                                                      │
  │  [Raw data. Reason from principles.md]               │
  └──────────────────────────────────────────────────────┘

Con --detailed:
  • Sensitivity table (WACC 7-10% vs growth 2-8%)
  • Implied margin analysis
  • Implied terminal multiple
  • Probability-weighted scenarios
```

Esfuerzo: MEDIO (1-2 sesiones). Usar `quant-tools-dev` agent.

**Tool 2: `insider_tracker.py`** — FILTRO 2

```
Uso:
  python3 tools/insider_tracker.py TICKER

Input: ticker (yfinance tiene estos datos y NO los usamos)

Output:
  ┌──────────────────────────────────────────────────────┐
  │  INSIDER ACTIVITY (6 months):                        │
  │    Buys: 3 transactions, $1.2M total                 │
  │    Sells: 1 transaction, $200K (10b5-1 plan)         │
  │    Net: +$1.0M buying                                │
  │                                                      │
  │  INSTITUTIONAL CHANGES:                               │
  │    Top buyer: Cantillon Capital +157K shares          │
  │    Top seller: Vanguard -50K (index rebalance)       │
  │    Net institutional: +2.1% ownership                │
  │                                                      │
  │  SHORT INTEREST:                                      │
  │    Short ratio: 2.3 days to cover                    │
  │    % float short: 3.2%                               │
  │    Prior quarter: 3.8%                               │
  │                                                      │
  │  ANALYST CONSENSUS:                                   │
  │    Strong Buy: 15 | Buy: 6 | Hold: 3 | Sell: 1      │
  │    Avg PT: $380 | High: $450 | Low: $280             │
  │                                                      │
  │  [Raw data. Reason from principles.md]               │
  └──────────────────────────────────────────────────────┘

Fuente: yfinance (ya disponible, no lo usamos):
  ticker.insider_transactions
  ticker.institutional_holders
  ticker.major_holders
  ticker.recommendations
  ticker.short_ratio  (o info['shortRatio'])
```

Esfuerzo: BAJO (1 sesión).

**Tool 3: `narrative_checker.py`** — FILTRO 3

```
Uso:
  python3 tools/narrative_checker.py TICKER

Input: ticker (datos financieros de yfinance organizados como health check)

Output:
  ┌──────────────────────────────────────────────────────┐
  │  FINANCIAL DATA TRENDS:                                │
  │                                                      │
  │  Revenue concentration:                               │
  │    Top segment: 45% of revenue (if available)        │
  │                                                      │
  │  Deferred revenue:                                   │
  │    2023: $4.2B → 2024: $4.5B → 2025: $4.9B (+8%)   │
  │                                                      │
  │  R&D / Revenue:                                      │
  │    2023: 18% → 2024: 17% → 2025: 16%                │
  │                                                      │
  │  Capex / Depreciation:                               │
  │    Capex: $800M | Depreciation: $600M                │
  │    Ratio: 1.33x                                      │
  │                                                      │
  │  SBC / Revenue:                                      │
  │    2023: 8% → 2024: 9% → 2025: 10%                  │
  │                                                      │
  │  Working capital:                                     │
  │    Receivables growing faster than revenue: NO        │
  │    Inventory building: N/A (software)                 │
  │                                                      │
  │  [Raw data. Reason from principles.md]               │
  └──────────────────────────────────────────────────────┘
```

Esfuerzo: BAJO-MEDIO (1 sesión).

### SKILLS NUEVOS (3)

**Skill 1: `contrathesis-framework`** — Integra los 4 filtros

```
Framework de preguntas para fundamental-analyst (no checklist rígido):
  • ¿Qué asume el precio? → implied_expectations.py da los datos
  • ¿Por qué el mercado asume eso? → narrativa vs datos
  • ¿Quién compra/vende y con qué skin in the game? → insider_tracker.py da los datos
  • ¿Datos primarios confirman o contradicen? → narrative_checker.py da los datos
  • ¿Cuánto se pierde si el mercado tiene razón vs cuánto se gana si no?
  • ¿Hay catalizador que forzaría al mercado a reconocer la realidad?

No todas las preguntas aplican a todas las empresas.
El analista razona cuáles son más relevantes en cada caso.
```

**Skill 2: `filing-analysis`** — Qué buscar en Annual Reports

```
Checklist para análisis de filings:
  - Risk factors nuevos vs año anterior
  - Cambios de lenguaje ("expect" → "anticipate" = menor confianza)
  - Cambio de auditor (red flag)
  - Off-balance sheet obligations
  - Contingent liabilities nuevas
  - Related party transactions
  - Cambios en políticas contables
  - Revenue concentration disclosure
```

**Skill 3: `skin-in-the-game`** — Ponderar opiniones

```
Framework para evaluar quién opina:
  - Insider buying > insider selling (pero 10b5-1 plans = noise)
  - Institucional añadiendo = smart money ve valor
  - Analyst contra consenso > analyst que sigue manada
  - Short sellers con track record > short sellers desconocidos
  - Management comprando con dinero propio >> management con stock comp
```

### AGENTS EXTENDIDOS (3, cambios de prompt)

```
1. fundamental-analyst:
   AÑADIR paso 0: "¿Qué implica el precio?" (implied_expectations.py)
   AÑADIR paso: "Management dice X, ¿datos confirman?" (narrative_checker.py)
   AÑADIR paso: "¿Quién compra/vende?" (insider_tracker.py)

2. devils-advocate:
   AÑADIR: "¿Qué tendría que ser cierto para que el precio tenga razón?"

3. news-monitor:
   AÑADIR: insider transactions como categoría estándar de monitoreo
```

---

## 7. LIMITACIÓN REAL: FILINGS EU vs US vs UK

### El problema

```
TIER 1 — Acceso excelente (US):
  ADBE, GL, LULU, NVO (ADR)
  → EDGAR: 10-K completo, Form 4 insiders, todo estructurado
  → Filing-analysis al 100%

TIER 2 — Acceso bueno (UK):
  DOM.L, MONY.L, AUTO.L, BYIT.L, FOUR.L, DNLM.L
  → Companies House + RNS/Investegate
  → Annual Reports en inglés, PDMR insiders
  → Filing-analysis al 80-90%

TIER 3 — Acceso parcial (EU continental):
  EDEN.PA, DSY.PA, DTE.DE, RACE.MI, BVI.PA
  → Reguladores nacionales (AMF, BaFin, CONSOB)
  → Idiomas locales (francés, alemán, italiano)
  → Annual Reports suelen tener versión inglesa (las grandes)
  → Filing-analysis al 50-60%
```

### Lo que nos salva

Los DATOS FINANCIEROS (lo más importante) vienen de yfinance para TODAS las empresas:

```python
# Funciona IGUAL para US, UK, EU:
ticker.financials             # Income statement
ticker.balance_sheet          # Balance
ticker.cashflow               # Cash flow
ticker.insider_transactions   # Insider trades
ticker.institutional_holders  # Institucionales
ticker.recommendations        # Analyst consensus
```

**Conclusión:** Las 3 tools nuevas funcionan para TODOS los mercados (yfinance). El skill de filing-analysis funciona mejor en US/UK y parcialmente en EU continental, pero el 80% del valor viene de los datos financieros que sí son universales.

---

## 8. PLAN DE IMPLEMENTACIÓN

> **Nota:** Las fases son secuenciales por dependencia lógica, no por calendario fijo.
> Cada fase se completa cuando se completa, no en X sesiones.

### Fase 1: El detector — VALOR INMEDIATO

```
→ Construir implied_expectations.py
→ Correr sobre todo el portfolio (posiciones activas)
→ Correr sobre los standing orders más cercanos
→ PREGUNTA CLAVE: ¿Nuestros triggers tienen sentido?
  ¿O estamos siendo demasiado exigentes y por eso el cash no se despliega?
```

### Fase 2: Los ojos

```
→ Construir insider_tracker.py
→ Construir narrative_checker.py
→ Son datos que yfinance YA TIENE y no estamos usando
→ Integrar en flujo de análisis
```

### Fase 3: Los frameworks

```
→ Crear contrathesis-framework skill
→ Crear filing-analysis skill
→ Crear skin-in-the-game skill
→ Extender prompts de fundamental-analyst + devils-advocate
```

### Fase 4: Macro Fragility

```
→ Construir macro_fragility.py (ver sección 12)
→ Integrar datos macro/país/sector como contexto para asignación
→ No como reglas de asignación, sino como datos para razonar
```

### Fase 5: Integración

```
→ implied_expectations.py en flujo de sesión (Fase 2.5)
→ Escaneo periódico del universo como fuente de pipeline
→ Standing orders con principio de frescura + revalidation
→ Fast-track validation con reverse DCF incluido
```

### Fase 6 (futuro): Shorts

```
→ Solo DESPUÉS de que Fases 1-5 estén operativas y validadas
→ Ver docs/short_selling_framework_design.md para diseño completo
→ Empezar con una posición mínima como aprendizaje
```

---

## 9. PRIMERA ACCIÓN CONCRETA (próxima sesión)

Cuando el humano diga "implementa", empezar por:

1. **Construir `implied_expectations.py`** usando `quant-tools-dev` agent
2. **Correr sobre las 10 posiciones activas** — ver qué implica el mercado
3. **Correr sobre los 6-8 standing orders más cercanos** (DSY.PA 2.9%, ROP 7.1%, ACGL 10.6%)
4. **Presentar al humano:** "El mercado asume X para cada empresa. Esto es lo que realmente pasa. Aquí están los gaps."

Esto tiene valor inmediato y valida el concepto antes de construir más.

---

## 10. SISTEMA DE FRAGILIDAD MACRO + KPIs SECTORIALES

### Concepto

El objetivo es tener datos económicos organizados en 3 capas (mundo → país → sector) que informen las decisiones de asignación. **No son reglas de asignación.** Son datos crudos que, combinados con principles.md, ayudan a razonar sobre cuánto capital exponer y dónde.

### Las 3 capas

```
CAPA 1: MUNDO (macro global)
  │
  ├── Indicadores de ciclo económico
  ├── Condiciones financieras globales
  ├── Geopolítica y riesgos sistémicos
  │
  CAPA 2: PAÍS (por mercado donde invertimos)
  │
  ├── US: empleo, deuda, consumo, vivienda, Fed policy
  ├── UK: empleo, BoE policy, GBP, housing, Brexit effects
  ├── EU: BCE policy, PMIs, deuda soberana
  ├── Nórdicos: específicos (NVO → DK)
  │
  CAPA 3: SECTOR (por sector donde tenemos posiciones o pipeline)
  │
  ├── Valoración relativa del sector
  ├── Flujos de capital (¿dinero entrando o saliendo?)
  ├── Earnings momentum (¿revisiones al alza o baja?)
  ├── Indicadores específicos del sector
  └── Riesgos regulatorios/disruptivos activos
```

### Tool: `macro_fragility.py`

```
Uso:
  python3 tools/macro_fragility.py                    # Vista completa
  python3 tools/macro_fragility.py --layer world      # Solo macro global
  python3 tools/macro_fragility.py --layer country US  # Solo US
  python3 tools/macro_fragility.py --sector technology # Solo un sector
  python3 tools/macro_fragility.py --portfolio         # Solo sectores donde tenemos posiciones

Output CAPA 1 (ejemplo):
  ┌──────────────────────────────────────────────────────┐
  │  WORLD MACRO DATA:                                    │
  │                                                      │
  │  Global PMI:     51.2 (prior: 50.8)                  │
  │  US 10Y yield:   4.35% (prior: 4.12%)               │
  │  Credit spreads: 3.8% (prior: 3.5%)                 │
  │  VIX:            18.2 (prior: 15.1)                  │
  │  USD DXY:        104.2 (prior: 103.5)               │
  │  Oil WTI:        $78 (prior: $72)                    │
  │  Gold:           $2,050 (prior: $2,010)              │
  │  Yield curve:    -0.12% (2y-10y)                     │
  │                                                      │
  │  TREND: 5 of 8 indicators deteriorating vs 30d ago   │
  │                                                      │
  │  [Raw data. Reason from principles.md]               │
  └──────────────────────────────────────────────────────┘

Output CAPA 2 (ejemplo US):
  ┌──────────────────────────────────────────────────────┐
  │  US ECONOMIC DATA:                                    │
  │                                                      │
  │  Employment:                                          │
  │    Unemployment: 4.1% (prior: 3.9%)                  │
  │    Initial claims: 225K (prior: 210K)                │
  │    NFP (last): +150K (prior: +275K)                  │
  │                                                      │
  │  Consumer:                                            │
  │    Consumer confidence: 98.2 (prior: 102.5)          │
  │    Retail sales MoM: -0.2% (prior: +0.4%)           │
  │    Personal savings rate: 3.8%                       │
  │    Household debt/income: 9.8%                       │
  │                                                      │
  │  Housing:                                             │
  │    Existing home sales: 4.1M (prior: 4.0M)          │
  │    Case-Shiller YoY: +4.2%                           │
  │    Mortgage rate 30y: 6.8%                           │
  │                                                      │
  │  Corporate:                                           │
  │    S&P 500 earnings growth: +8.2% YoY               │
  │    Corporate debt/GDP: 47%                            │
  │    Buyback authorization YTD: $180B                  │
  │                                                      │
  │  Fed:                                                 │
  │    Fed funds: 4.25-4.50%                             │
  │    Market implied cuts (12m): 1.5                    │
  │    QT pace: $60B/month                               │
  │                                                      │
  │  [Raw data. Reason from principles.md]               │
  └──────────────────────────────────────────────────────┘
```

### KPIs Sectoriales (CAPA 3) — Lo más granular

Cada sector tiene indicadores específicos que revelan su salud. El tool los presenta como datos crudos. Ejemplos:

```
Output SECTOR: Technology/SaaS (ejemplo):
  ┌──────────────────────────────────────────────────────┐
  │  SECTOR: Technology / SaaS                            │
  │                                                      │
  │  Valoración relativa:                                 │
  │    Sector P/E: 28.3x (5yr avg: 32.1x)               │
  │    Sector EV/Revenue: 8.2x (5yr avg: 9.5x)          │
  │    vs S&P 500 P/E premium: +45% (5yr avg: +55%)     │
  │                                                      │
  │  Earnings momentum:                                   │
  │    % companies beating estimates (last Q): 72%       │
  │    Consensus revision (NTM EPS) 90d: -2.3%           │
  │    Revenue growth (sector median): +9.5%             │
  │                                                      │
  │  Sector-specific:                                     │
  │    Net retention rates (median): 112%                │
  │    Rule of 40 (median): 35%                          │
  │    AI capex as % of revenue (sector): 8.2%           │
  │                                                      │
  │  Capital flows:                                       │
  │    ETF flows (sector) 30d: -$2.1B                    │
  │    Insider buying ratio (sector): 0.8x               │
  │                                                      │
  │  Regulatory/disruption:                               │
  │    Active: EU AI Act (implementation 2026)            │
  │    Active: Per-seat pricing → consumption shift       │
  │                                                      │
  │  NUESTRAS POSICIONES en este sector:                  │
  │    ADBE (QS 73, FV $390), BYIT.L (QS 68, FV 345p)  │
  │                                                      │
  │  PIPELINE en este sector:                             │
  │    INTU (R3), PAYC (R4-watchlist)                    │
  │                                                      │
  │  [Raw data. Reason from principles.md]               │
  └──────────────────────────────────────────────────────┘

Output SECTOR: Insurance (ejemplo):
  ┌──────────────────────────────────────────────────────┐
  │  SECTOR: Insurance                                    │
  │                                                      │
  │  Valoración relativa:                                 │
  │    Sector P/B: 1.8x (5yr avg: 1.5x)                 │
  │    Sector P/E: 11.2x (5yr avg: 10.5x)               │
  │                                                      │
  │  Sector-specific:                                     │
  │    Combined ratio (industry avg): 96.2%              │
  │    Premium growth (market): +7.8%                    │
  │    Cat losses YTD: $18B (vs $22B prior yr)           │
  │    Reserve adequacy (industry): adequate              │
  │    Social inflation trend: accelerating              │
  │    Investment yield (portfolio avg): 4.8%            │
  │                                                      │
  │  Regulatory:                                          │
  │    IFRS 17 implementation effects                    │
  │    Climate disclosure requirements                   │
  │                                                      │
  │  NUESTRAS POSICIONES:                                 │
  │    GL (QS 52, FV $191)                               │
  │                                                      │
  │  PIPELINE:                                            │
  │    ACGL (R4-approved)                                │
  │                                                      │
  │  [Raw data. Reason from principles.md]               │
  └──────────────────────────────────────────────────────┘

Output SECTOR: Pharma / Healthcare (ejemplo):
  ┌──────────────────────────────────────────────────────┐
  │  SECTOR: Pharma / Healthcare                          │
  │                                                      │
  │  Valoración relativa:                                 │
  │    Sector P/E: 18.5x (5yr avg: 17.2x)               │
  │    Biotech index (XBI) YTD: +3.2%                    │
  │                                                      │
  │  Sector-specific:                                     │
  │    FDA approvals YTD: 12 (vs 15 prior yr)            │
  │    IRA drug price negotiation: 10 drugs selected     │
  │    GLP-1 market size (est): $80B by 2030             │
  │    Patent cliff exposure (top 20): $120B rev at risk │
  │    Clinical trial success rate: 12% (Ph1→approval)   │
  │                                                      │
  │  Regulatory:                                          │
  │    Medicare negotiation expanding                    │
  │    EU HTA regulation                                 │
  │                                                      │
  │  NUESTRAS POSICIONES:                                 │
  │    NVO (QS 73, FV — pending CagriSema)               │
  │                                                      │
  │  [Raw data. Reason from principles.md]               │
  └──────────────────────────────────────────────────────┘
```

### Cross-referencing: el valor está en cruzar datos

La potencia del sistema no está en un indicador individual — está en cruzar datos de las 3 capas para detectar inconsistencias o confirmar patrones.

```
Ejemplo de cruce que REVELA algo:

  CAPA 1: Credit spreads ampliándose + VIX subiendo
  CAPA 2 US: Employment deteriorando + consumer confidence cayendo
  CAPA 3 Consumer discretionary: Earnings revisions negativas

  → Los 3 niveles apuntan en la misma dirección
  → Dato relevante para posiciones en consumer discretionary (LULU)

Ejemplo de cruce que CONTRADICE:

  CAPA 1: VIX alto, mercado nervioso
  CAPA 2 US: Employment robusto, consumer spending estable
  CAPA 3 Technology: 72% beating estimates, net retention 112%

  → Miedo macro vs datos micro saludables
  → Dato relevante para razonar si SaaS selloff es fundamentado

En ambos casos: son DATOS para razonar, no señales para actuar automáticamente.
```

### Fuentes de datos

```
CAPA 1 (World): FRED API, trading economics, yfinance (^VIX, ^TNX, etc.)
CAPA 2 (Country): FRED API (US), ONS (UK), Eurostat (EU)
CAPA 3 (Sector): yfinance (sector ETFs), earnings data agregado, sector-specific sources

Implementación gradual:
  • Fase 1: Datos de yfinance (ETFs sectoriales, índices macro como ^VIX, ^TNX)
  • Fase 2: FRED API para datos económicos US
  • Fase 3: Fuentes europeas (más fragmentadas, menor prioridad)
```

### Lo que este tool NO hace

```
❌ NO dice "estás sobreexpuesto al sector X"
❌ NO dice "reduce long a 60%"
❌ NO genera alertas automáticas
❌ NO tiene umbrales de peligro codificados
❌ NO prescribe acciones

✓ SÍ presenta datos crudos organizados por capa
✓ SÍ muestra tendencias (prior vs current)
✓ SÍ cruza datos para que el analista vea patrones
✓ SÍ conecta los datos con nuestras posiciones y pipeline
✓ SÍ deja que principles.md guíe el razonamiento
```

---

## 11. DOCUMENTOS RELACIONADOS

| Documento | Contenido |
|-----------|-----------|
| `docs/short_selling_framework_design.md` | Diseño completo de short selling (1238 líneas). Incluye: instrumentos en eToro, principios P10-P12, pipeline S1-S4, auditoría completa del sistema, guardrails, simulaciones MONY.L/NVDA, auto-diagnóstico de limitaciones, principios para el futuro. |
| `docs/contrathesis_simulation_mony.md` | Simulación del framework de contrathesis aplicado a MONY.L |
| `docs/contrathesis_simulation_nvda.md` | Simulación del framework de contrathesis aplicado a NVIDIA |
| `learning/principles.md` | 9 principios de inversión actuales (se extenderían con P10-P12 para shorts) |
| `.claude/skills/pre-execution-check/SKILL.md` | Skill de pre-execution que se extendería para fast-track validation |

---

## 12. RESUMEN EN UNA PÁGINA (para lectura rápida)

```
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║  EL SISTEMA:                                                  ║
║                                                               ║
║  1. ESCANEAR: Reverse DCF → ¿qué asume el mercado?          ║
║  2. CONTEXTUALIZAR: Macro fragility → ¿cómo está el entorno?║
║  3. VALIDAR:  4 filtros → ¿el mercado se equivoca?           ║
║     F1: ¿Qué asume y por qué? (razón vs emoción)            ║
║     F2: ¿Quién opina y con qué skin in the game?            ║
║     F3: ¿Datos primarios confirman o contradicen?            ║
║     F4: ¿Asimetría favorable?                                ║
║  4. ANALIZAR: Pipeline R1→R4 → ¿es real el gap?             ║
║  5. PREPARAR: Alerta de precio + thesis pre-escrita          ║
║  6. VALIDAR:  Cuando toca precio → fast-track (NO auto-buy)  ║
║  7. EJECUTAR: Humano confirma → eToro                         ║
║  8. MONITOREAR: Noticias, earnings, kill conditions           ║
║  9. REBALANCEAR: Razonar sobre rotación hacia calidad         ║
║                                                               ║
║  TOOLS NUEVOS: implied_expectations.py (reverse DCF)          ║
║                insider_tracker.py (skin in the game)          ║
║                narrative_checker.py (datos vs narrativa)      ║
║                macro_fragility.py (contexto macro/sector)     ║
║                                                               ║
║  SKILLS NUEVOS: contrathesis-framework                        ║
║                 filing-analysis                               ║
║                 skin-in-the-game                              ║
║                                                               ║
║  PRINCIPIO RECTOR:                                            ║
║    Tools = DATOS CRUDOS. Nunca juicios ni etiquetas.          ║
║    Decisiones = principles.md + precedentes + razonamiento.   ║
║                                                               ║
║  SIGUIENTE PASO: Construir implied_expectations.py            ║
║                  y correr sobre portfolio + standing orders    ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

---

*Documento actualizado: Session 73, 2026-02-17*
*Para mi yo futuro. Todo el contexto está aquí. Implementar sin preguntar.*
