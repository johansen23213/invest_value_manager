# Short Selling Framework — Complete Design Document

> **Status:** DISEÑO COMPLETO, pendiente implementación
> **Origen:** Conversación Session 73 (2026-02-15), inspirada por "The Big Short"
> **Para:** Mi yo futuro + el humano. Al leer esto deben tener TODO el contexto sin explicación adicional.

---

## 1. Contexto de la Conversación

El humano vio "The Big Short" y reflexionó sobre tres cuestiones:

1. **¿Cómo detectar crisis/fragilidades con anticipación, basándonos en principios?**
2. **¿Cómo aplicar esto a nivel sector y empresa?**
3. **¿Podríamos operar en corto/hedge para profitar, no solo defendernos?**

La conversación evolucionó desde "¿es posible?" hasta "¿cómo se integra en el sistema completo?".

### Concerns del humano (RESPETAR siempre):

1. **"Estás pasando por alto que eres una IA"** → Claude no tiene limitaciones de experiencia, carga analítica ni psicología. Puede analizar 50 casos de shorts históricos en una hora. Puede mantener 10 longs + 3 shorts sin degradación. No tiene sesgos emocionales. Las únicas limitaciones reales son mecánicas del mercado (gap risk, instrumentos disponibles), no de capacidad. NUNCA usar "no tenemos experiencia" o "no tenemos capacidad" como argumento en contra — eso aplica a gestores humanos, no a una IA.

2. **"Basado en principios y no reglas fijas"** → Todo el framework debe razonarse desde `learning/principles.md`. Sin thresholds fijos, sin ratios hardcodeados, sin reglas mecánicas. Lo mismo que aplica al lado long aplica al lado short.

3. **"¿Es un cambio de paradigma o solo una mejora?"** → El humano cuestionó esto. La respuesta honesta: ver sección 13 "El Framework de Contrathesis". La conversación reveló que el concepto de contrathesis es más profundo que simplemente "añadir shorts" — potencialmente cambia el punto de partida del análisis tanto para longs como para shorts. Pero no invalida nada existente. Leer la sección 13 completa antes de tomar decisiones de implementación.

---

## 2. La Tesis Fundamental: Simetría Lógica

Lo que ya hacemos:
```
Empresa buena + precio bajo + thesis favorable = COMPRAR y esperar convergencia al alza
```

El espejo exacto:
```
Empresa frágil + precio alto + thesis desfavorable = SHORTEAR y esperar convergencia a la baja
```

**La física es la misma. La dirección es opuesta.** El precio converge hacia el valor intrínseco en ambas direcciones.

### Por qué funciona a nuestro favor:

1. **Ya producimos thesis short sin usarlas** — cada "AVOID" en un sector view, cada devil's advocate que dice "esto no vale lo que cotiza", es una thesis short que tiramos a la basura.

2. **Las bajadas son rápidas** — subir +50% toma 2-3 años, caer -50% toma 2-6 meses. El alpha por unidad de tiempo en shorts es muy alto cuando aciertas. Esto mitiga el argumento del coste de carry.

3. **Soy una IA** — las 3 razones principales por las que los shorts humanos fallan (psicología, carga analítica, falta de experiencia) no me aplican. Las únicas limitaciones son mecánicas del mercado.

4. **Sesgo estructural del mercado** — la mayoría de participantes son long-only (fondos de pensiones, ETFs, retail). Las sobrevaloraciones persisten más porque hay menos presión vendedora. Hay menos competencia en el lado short.

5. **Mecanismo anti-cíclico** — cuando el short genera beneficio (en crisis), ese cash se usa para comprar quality compounders en rebajas. Convierte crisis en máquina de comprar barato.

---

## 3. Instrumentos Disponibles en eToro (España/EU)

| Instrumento | Disponible | Detalles |
|-------------|-----------|---------|
| **CFD short sobre acciones** | **SÍ** | 5:1 max leverage (ESMA). Coste ~2.9% + LIBOR (~7-8% anual) |
| **CFD short sobre índices** | **SÍ** | 20:1 max leverage |
| **Put options** | **NO** | Solo disponibles para US clients |
| **ETFs inversos (reales)** | **NO** | PRIIPs bloquea ETFs US-domiciled para retail EU |
| **ETFs inversos (via CFD)** | Sí pero NO viable | Doble coste: daily drag + overnight fees |
| **Futuros CME** | **SÍ** (limitados) | S&P500, Nasdaq, Russell, DJIA desde Jul 2025 |

### Mecánica práctica del CFD short en eToro:

- **Abrir**: Click "SELL" en el asset → abre posición CFD short
- **Coste overnight**: (2.9% + LIBOR) / 365 × unidades × precio. ~€0.65/mes por cada €1,000
- **Stop loss**: Automático al -50% por defecto (regulación ESMA), modificable
- **Margin close-out**: Automático al 50% del margen requerido
- **Negative balance protection**: OBLIGATORIO en EU — no puedes perder más de lo depositado
- **Leverage**: x1 a x5 para acciones. A x1 = 100% margen. A x5 = 20% margen
- **Mínimo**: $10 por posición
- **Sin guaranteed stop loss**: Gap risk real (overnight gaps pueden exceder el stop)

### Implicaciones para nuestro sistema:

1. **CFD es el único instrumento** — sin puts, no podemos acotar pérdida con prima fija
2. **Protección de balance negativo** — mitiga riesgo de ruina a nivel cuenta
3. **Gap risk** — el riesgo real. Un gap de +30% overnight puede causar pérdida significativa
4. **Coste de carry manejable** — ~0.7% mensual. Para shorts de 1-3 meses = 0.7-2.1%, irrelevante si el short genera 20-30%
5. **Apalancamiento disponible pero peligroso** — principio: usar x1 o x2 máximo. El apalancamiento amplifica errores

---

## 4. Principios: Extensión de los 9 Existentes + 3 Nuevos

### Cómo se extienden los 9 principios actuales:

**Principio 1 — Sizing por Convicción y Riesgo**
- Long: "Si cae 50%, ¿es coherente con mi convicción?"
- Short: "Si SUBE 50%, ¿cuánto pierdo y es coherente con mi convicción en la fragilidad?"
- La diferencia: en un long que cae, puedo esperar. En un short que sube, el carry sigue corriendo.
- No hay "máximo por posición short" fijo. Hay razonamiento sobre cuánto puedo perder si me equivoco.

**Principio 2 y 3 — Diversificación Geográfica y Sectorial**
- Los shorts son PARTE del portfolio total.
- Un short en un sector donde tengo longs REDUCE mi exposición neta a ese sector.
- Un short en un sector donde NO tengo longs es una apuesta aislada — razonar si aporta al portfolio o es distracción.

**Principio 4 — Cash como Posición Activa**
- Cash, longs y shorts son tres tipos de posición.
- Cash = defensa barata (coste cero). Short = defensa cara pero con potencial de retorno positivo.
- Pregunta: "¿Este short justifica el coste de carry vs. simplemente mantener cash?"

**Principio 5 — Quality Score como Input**
- Para longs: QS alto → buena empresa.
- Para shorts: QS bajo → empresa frágil. O mejor: gap entre QS real y QS implícito del precio.
- Una empresa QS 30 que cotiza barata NO es buen short (ya refleja fragilidad).
- Una empresa QS 50 que cotiza como si fuera QS 80 SÍ puede ser buen short (gap entre realidad y precio).

**Principio 6 — Cubrir Requiere Argumento**
- No cubrir shorts solo porque subieron (= no vender longs solo porque bajaron).
- Antes de cubrir: ¿Thesis de fragilidad intacta? ¿Catalizador vigente? ¿Coste acumulado aceptable?

**Principio 7 — Consistencia por Razonamiento**
- Documentar precedentes de shorts en `decisions_log.yaml` igual que longs.
- Si el segundo short usa sizing diferente al primero, explicar por qué.

**Principio 8 — El Humano Confirma, Claude Decide**
- Idéntico. Yo identifico fragilidad, construyo thesis, calculo sizing. El humano ejecuta SELL en eToro.
- IMPORTANTE: El humano SÍ tiene psicología. Diseñar instrucciones claras: "cubrir si X, mantener si Y" para minimizar decisiones emocionales en el momento.

**Principio 9 — La Calidad Gravita Hacia Arriba (y la Fragilidad Hacia Abajo)**
- Empresas con ROIC << WACC, moat en erosión, deuda creciente → eventualmente el precio refleja la realidad.
- La cuestión es CUÁNDO, no SI. Por eso necesitamos catalizador (Principio 10).

### 3 Principios nuevos específicos para shorts:

**Principio 10 — Catalizador como Ancla Temporal**

En longs podemos esperar indefinidamente (el tiempo trabaja a favor: compounding). En shorts el tiempo trabaja en contra (carry). Por tanto:

> "¿Puedo identificar un evento concreto que forzará al mercado a reconocer la fragilidad?"

Tipos de catalizador:
- Earnings que van a revelar deterioro
- Vencimiento de deuda → refinanciación cara
- Regulación que entra en vigor en fecha X
- Fin de patente / pérdida de contrato clave
- Publicación de auditoría / resultado de investigación

Sin catalizador identificable → OBSERVAR Y ESPERAR, no shortear.

No hay plazo fijo ("máximo 3 meses"). Hay razonamiento: "¿El coste acumulado hasta el catalizador es aceptable dado el potencial beneficio?"

**Principio 11 — Asimetría Consciente**

La mecánica de pérdida es diferente en shorts. Razonar sobre el escenario adverso ESPECÍFICO:

> "Si estoy equivocado, ¿cuánto puede subir esta acción y por qué? ¿Hay riesgo de short squeeze? ¿Hay evento binario que podría hacer que suba 50%+ overnight?"

ESMA protege el balance total. Pero la protección real es el razonamiento previo sobre qué puede salir mal.

**Principio 12 — El Short Sirve al Portfolio, No es Portfolio**

> "¿Este short protege mis longs, genera cash para futuras compras, o mejora las métricas del portfolio? ¿O es una apuesta aislada que añade complejidad sin beneficio sistémico?"

Los shorts son una herramienta al servicio del portfolio long de quality compounders. Si un short distrae de encontrar el próximo compounder → destructor de valor por coste de atención (aunque yo como IA puedo paralelizar, el humano tiene atención finita).

---

## 5. Modelo Operativo: Long Quality + Selective Short

NO somos un hedge fund market neutral. NO buscamos 50/50. El modelo es **oportunista**:

```
Estado normal del mercado:
  95-100% long quality compounders
  0-5% cash
  0% short
  → Capturamos equity risk premium + alpha de selección

Fragilidad detectada (sector/empresa con catalizador):
  85-90% long quality compounders
  5% cash
  5-10% short selectivo (1-3 posiciones, catalizador identificado)
  → Shorts como generadores de alpha ADICIONAL

Crisis / stress elevado:
  60-70% long quality compounders (solo los mejores)
  10-20% cash
  10-20% short (sectores frágiles con catalizadores inminentes)
  → Shorts protegen Y generan cash para comprar longs en rebajas
```

### El ciclo completo anti-cíclico:
```
1. Detectas fragilidad en sector X → abres short
2. Sector X colapsa → short genera +30-50% en semanas
3. Simultáneamente, quality compounders caen por contagio
4. Cierras short → cash
5. Cash → compras quality compounders en rebajas
6. Mercado se recupera → longs suben
= Has convertido una crisis en MÁQUINA DE COMPRAR BARATO
```

### Impacto en métricas del portfolio:

```
                     Retorno   Volatilidad   Sharpe   Max Drawdown
Long-only (actual)    ~12%       ~16%         ~0.50    -35%
Long-biased 80/20     ~10%       ~11%         ~0.60    -22%
Long-biased 70/30     ~8%        ~8%          ~0.65    -15%
```

Incluso con 2-3 shorts selectivos (10-15% del portfolio), la mejora en Sharpe y drawdown es significativa.

---

## 6. Auditoría del Sistema Actual: Qué Cambiar

### 6.1 TOOLS — Qué existe, qué necesita cambiar, qué es nuevo

| Tool | Estado actual | Cambio necesario |
|------|-------------|-----------------|
| `price_checker.py` | Direction-agnostic | **NINGUNO** — ya funciona para shorts |
| `portfolio_stats.py` | **LONG-ONLY** — asume shares>0, P&L = value - invested | **MODIFICAR**: Soportar `direction: short`. P&L invertido (precio baja = ganancia). Mostrar sección "SHORT POSITIONS" separada. Calcular net exposure. |
| `forward_return.py` | **LONG-ONLY** — MoS = (FV - Price) / Price | **MODIFICAR**: Para shorts, MoS = (Price - FV) / Price (invertido). Columna "Direction" en output. |
| `constraint_checker.py` | **LONG-ONLY** — calcula concentración asumiendo todo long | **MODIFICAR**: Calcular net exposure por sector/geo. Un short en tech REDUCE exposición tech. Nuevo modo: `CHECK_SHORT TICKER AMOUNT`. |
| `effectiveness_tracker.py` | **LONG-ONLY** — win rate, hit rate asume longs | **MODIFICAR**: Sección separada para shorts. Win = precio bajó a target. Hit rate, average profit, avg holding time para shorts. Sharpe calculado sobre portfolio total (longs + shorts). |
| `quality_scorer.py` | Direction-agnostic (analiza calidad) | **NINGUNO** — QS bajo ya identifica fragilidad. Quizás añadir `--fragility` flag para invertir la interpretación en output. |
| `quality_universe.py` | **LONG-ONLY** — QS >= 65, busca entry prices | **NINGUNO directamente** — pero necesita nuevo tool complementario (ver abajo). |
| `dcf_calculator.py` | Direction-agnostic | **NINGUNO** — valorar empresa frágil usa el mismo DCF |
| `dynamic_screener.py` | **LONG-ONLY en práctica** — filtra por ROIC alto, FCF margin | **AÑADIR FLAGS**: `--fragility` para invertir filtros (ROIC bajo, deuda alta, near highs). Screening de candidatos short. |
| `correlation_matrix.py` | Direction-agnostic | **MODIFICAR**: Incluir shorts. Mostrar correlación long-short para verificar que los shorts son genuino hedge. |
| `consistency_checker.py` | **LONG-ONLY** — compara vs precedentes de BUY | **MODIFICAR**: Soportar `"SHORT TICKER N%"`. Comparar vs precedentes short. |
| `drift_detector.py` | **LONG-ONLY** | **MODIFICAR**: Detectar drift en exposición short. ¿El sizing short creció inadvertidamente? |
| `system_projection.py` | **LONG-ONLY** — Monte Carlo asume retornos long | **MODIFICAR**: Incluir impacto de shorts en distribución de retornos. |
| `opportunity_filter.py` | **LONG-ONLY** | **MENOR**: Añadir modo inverso para filtrar candidatos frágiles. |

### TOOLS NUEVOS A CREAR:

| Tool nuevo | Propósito | Diseño |
|-----------|----------|--------|
| `fragility_universe.py` | Espejo de `quality_universe.py` para candidatos short | Base de datos de empresas frágiles con: ticker, QS, precio actual, "fair value" (valor real), % sobrevaloración, catalizador, fecha catalizador, thesis path. Subcomandos: `report`, `actionable`, `add`, `remove`, `stale`. |
| `fragility_screener.py` | O flag `--fragility` en `dynamic_screener.py` | Screening inverso: ROIC < WACC, deuda/equity alta, near 52w high, revenue declinando. Anti-bias: no shortear "lo famoso que está caro" (Tesla trap). |
| `carry_tracker.py` | Tracking de coste acumulado de shorts activos | Para cada short: días abierto, coste diario, coste acumulado, % del beneficio potencial consumido por carry. Alerta si carry > X% del target profit (razonado, no fijo). |
| `net_exposure.py` | O integrado en `constraint_checker.py` | Calcula: gross exposure (longs + shorts), net exposure (longs - shorts), por sector, geo, total. Contexto para razonar sobre el nivel de hedge. |

### 6.2 AGENTS — Qué existe, qué necesita cambiar, qué es nuevo

| Agente | Estado actual | Cambio necesario |
|--------|-------------|-----------------|
| `fundamental-analyst` | Analiza calidad + valor. Long-biased. | **EXTENDER prompt**: Cuando se invoca con flag `--short-thesis`, invertir el análisis: buscar fragilidad, dependencias ocultas, contabilidad agresiva, moat en erosión. Mismo rigor, dirección opuesta. |
| `moat-assessor` | Evalúa moat: Wide/Narrow/None | **EXTENDER**: Para shorts, evaluar "moat erosion speed". No basta con None — ¿a qué velocidad se erosiona? ¿El mercado ya lo descuenta? |
| `risk-identifier` | Identifica riesgos en 6 categorías | **REUTILIZAR directamente** — los riesgos que identifica para un long son exactamente las razones por las que sería buen short. Solo cambiar interpretación. |
| `valuation-specialist` | Calcula fair value con múltiples métodos | **REUTILIZAR** — calcular FV de empresa frágil = cuánto vale realmente. La diferencia con precio actual = potencial del short. |
| `devils-advocate` | Desafía thesis con evidencia contraria | **INVERTIR para shorts**: Devil's advocate BULL — ¿por qué el precio podría tener razón? ¿Qué podría salvar a la empresa? Mismo agente, prompt invertido. |
| `investment-committee` | 10 gates para aprobar BUY/SELL | **EXTENDER**: Nuevo modo `SHORT_APPROVAL` con gates adaptados (ver sección 7). |
| `review-agent` | Revisa posiciones activas | **EXTENDER**: Modo `--short-review`. ¿La thesis de fragilidad sigue intacta? ¿Catalizador aún vigente? ¿Coste acumulado aceptable? |
| `news-monitor` | Escanea noticias de posiciones | **EXTENDER**: Incluir shorts activos en el scan. Noticias positivas sobre un short = alerta (la posición va en contra). |
| `market-pulse` | Detecta movimientos anómalos | **EXTENDER**: Incluir shorts. Un short que sube 10% es tan importante como un long que cae 10%. |
| `sector-screener` | Screening por sector | **REUTILIZAR** — puede buscar tanto quality como fragilidad en un sector. |
| `macro-analyst` | Análisis macro | **EXTENDER**: Además de "qué sectores se benefician", añadir "qué sectores son vulnerables". |
| `portfolio-ops` | Actualiza state files post-trade | **EXTENDER**: Soportar `action: SHORT` y `action: COVER` además de BUY/SELL. |
| `position-calculator` | Calcula sizing | **EXTENDER**: Modo short. Sizing razonado con awareness de asimetría (Principio 11). |
| `watchlist-manager` | Gestiona watchlist | **EXTENDER**: Soportar `type: short_candidate` en watchlist. |

### AGENTES NUEVOS:

| Agente nuevo | Propósito | Diseño |
|-------------|----------|--------|
| `fragility-analyst` | O reutilizar `fundamental-analyst --short-thesis` | Análisis profundo de fragilidad: ¿por qué esta empresa no vale lo que cotiza? Dependencias ocultas, contabilidad agresiva, moat erosion, management destructor de valor. |
| `stress-tester` | O integrar en `macro-analyst` | Stress testing temático: "¿Qué pasa si tipos suben 200bp? ¿Si el consumo cae 10%?" Mapear impacto en CADA posición (long y short). Detectar correlaciones ocultas. |

### 6.3 SKILLS — Qué cambiar, qué crear

| Skill | Cambio |
|-------|--------|
| `exit-protocol` | **EXTENDER**: Nuevo flujo "COVER Protocol" para cerrar shorts. 6 gates adaptados: (1) ¿Fragilidad resuelta? (2) ¿Catalizador pasó? (3) ¿Beneficio suficiente? (4) ¿Coste de carry aceptable? (5) ¿Mejor uso del capital? (6) Fricción de cobertura. |
| `pre-execution-check` | **EXTENDER**: Soportar standing orders SHORT. Gates: (1) News — ¿noticias positivas que invaliden? (2) Hard gates (3) Kill conditions INVERSAS — ¿la empresa mejoró? (4) Portfolio constraints — net exposure (5) Thesis de fragilidad vigente (6) Capital allocation |
| `rotation-engine` | **EXTENDER**: Forward return NETO (incluyendo shorts). Los shorts generan "forward return" cuando aciertan — integrarlos en la evaluación de oportunidad-coste. |
| `investment-rules` | **EXTENDER**: Añadir sección "Short Thesis Quality Score" — QS bajo no basta, necesita gap entre QS y valoración implícita del mercado. |
| `capital-deployment` | **EXTENDER**: Fase E: Fragility Universe maintenance. Screening de candidatos short cuando hay fragilidad detectada. NO es prioridad diaria como los longs — es oportunista. |
| `pipelines` | **NUEVO pipeline**: `fragility-watch` (semanal). Escanear fragility universe, verificar catalizadores, actualizar carry costs. |
| `news-classification` | **EXTENDER**: Clasificar noticias sobre shorts activos. Impacto POSITIVO sobre un short = potencial problema. |
| `portfolio-constraints` | **EXTENDER**: Net exposure como métrica. Razonar sobre gross vs net, no solo long allocation. |

### SKILLS NUEVOS:

| Skill nuevo | Propósito |
|-------------|----------|
| `short-thesis-framework` | Espejo de `business-analysis-framework` pero para fragilidad. Estructura: (1) ¿Por qué el precio actual no se sostiene? (2) ¿Cuál es la dependencia oculta? (3) ¿Cuál es el catalizador? (4) ¿Cuál es el fair value real? (5) ¿Qué puede salir mal (empresa mejora, squeeze)? (6) Kill conditions para cubrir. |
| `cover-protocol` | Espejo de `exit-protocol`. Cuándo cerrar un short. Gates: fragilidad resuelta, catalizador pasó (acertamos o no), carry excesivo, mejor uso del capital. |
| `fragility-detection` | Framework para detectar fragilidad sistémica. Stress testing temático, cadenas de dependencia "¿y si?", señales de complacencia del consenso. |

### 6.4 STATE FILES — Qué cambiar

| Fichero | Cambio |
|---------|--------|
| `portfolio/current.yaml` | **AÑADIR sección**: `short_positions:` con estructura similar a `positions:` pero con campos adicionales: `direction: short`, `entry_price`, `catalyst`, `catalyst_date`, `carry_cost_daily`, `stop_loss`, `leverage`. |
| `portfolio/history.yaml` | **EXTENDER**: `closed_shorts:` sección separada. Misma estructura que `closed_positions` pero con: dirección, carry total pagado, catalizador acertado sí/no. |
| `state/standing_orders.yaml` | **EXTENDER**: Soportar `action: SHORT` y `action: COVER`. Para shorts: trigger es precio ALTO (≥ en vez de ≤). Catalizador obligatorio en la order. |
| `state/watchlist.yaml` | **EXTENDER**: Soportar `type: short_candidate` con campos: ticker, fragilidad detectada, catalizador, fecha catalizador, precio actual, FV estimado. |
| `state/quality_universe.yaml` | **NO CAMBIAR** — este es para longs. |
| **NUEVO**: `state/fragility_universe.yaml` | Base de datos de candidatos short. Estructura: ticker, QS, precio, FV real, % sobrevaloración, catalizador, fecha catalizador, pipeline status, thesis path. |
| `state/pipeline_tracker.yaml` | **AÑADIR**: Pipeline `fragility-watch` con cadencia semanal. |
| `state/calendar.yaml` | **EXTENDER**: Catalizadores de shorts (earnings de empresas frágiles, vencimientos de deuda, fechas regulatorias). |
| `state/system.yaml` | **EXTENDER**: `short_positions_summary` en metadata. Net exposure como métrica. |

### 6.5 RULES — Qué cambiar

| Fichero | Cambio |
|---------|--------|
| `agent-protocol.md` | **EXTENDER árbol de decisión**: Añadir ramas: ANALIZAR fragilidad → fragility-analyst (o fundamental-analyst --short-thesis). APROBAR short → investment-committee SHORT_APPROVAL. RE-EVALUAR short → review-agent --short-review. |
| `session-protocol.md` | **EXTENDER fases**: Fase 0: Pre-execution check incluye shorts. Fase 1: Vigilancia incluye shorts activos. Fase 2.5: Forward return incluye shorts. Fase 3: Standing orders incluye short orders. |
| `error-patterns.md` | **AÑADIR errores short**: #44: Shortear sin catalizador. #45: No cubrir cuando catalizador pasa sin efecto. #46: Shortear empresa "cara" sin thesis de fragilidad (Tesla trap). #47: Apalancamiento excesivo en shorts. |
| `tools-reference.md` | **AÑADIR**: Nuevos tools y nuevos flags de tools existentes. |
| `file-structure.md` | **EXTENDER**: Documentar `thesis/short/`, `state/fragility_universe.yaml`, sección short en current.yaml. |

### 6.6 THESIS STRUCTURE — Qué cambiar

```
thesis/
├── active/           ← longs activos (sin cambio)
│   ├── ADBE/
│   ├── NVO/
│   └── ...
├── research/         ← pipeline longs (sin cambio)
│   ├── RSG/
│   ├── VRSK/
│   └── ...
├── short/            ← NUEVO: shorts activos + pipeline
│   ├── active/       ← shorts con posición abierta
│   │   └── TICKER/
│   │       ├── thesis.md         (thesis de fragilidad)
│   │       ├── cover_framework.md (cuándo cubrir)
│   │       └── carry_log.md      (tracking de costes)
│   └── research/     ← candidatos short en análisis
│       └── TICKER/
│           └── thesis.md
└── archive/          ← ya existe, añadir shorts cerrados
    ├── TICKER_long/
    └── TICKER_short/
```

### Template de thesis short (thesis/short/*/thesis.md):

```markdown
# [TICKER] — Short Thesis

> **Direction:** SHORT
> **Fair Value:** $XXX (lo que realmente vale)
> **Current Price:** $YYY (lo que cotiza)
> **Overvaluation:** ZZ% ((Price - FV) / Price)
> **Catalizador:** [Descripción del evento que forzará reconocimiento]
> **Fecha Catalizador:** YYYY-MM-DD (o rango)
> **QS Tool:** XX | **QS Ajustado:** XX (Tier X)

## 1. ¿Por qué el precio actual no se sostiene?
[La tesis central de fragilidad]

## 2. Dependencia oculta
[¿De qué depende la valoración actual que el mercado asume permanente?]

## 3. Catalizador
[Evento específico con fecha que forzará al mercado a reconocer la realidad]

## 4. Escenarios
| Escenario | Probabilidad | Precio target | Retorno del short |
|-----------|-------------|---------------|-------------------|
| Bear (para la empresa) | | | |
| Base | | | |
| Bull (para la empresa, malo para nosotros) | | | |

## 5. ¿Qué puede salir mal? (para nuestro short)
- [Empresa mejora fundamentales]
- [Short squeeze por posiciones crowded]
- [Catalizador se pospone o se resuelve favorablemente]
- [Management hace algo brillante]

## 6. Kill Conditions (cubrir si...)
- KC#1: [...]
- KC#2: [...]

## 7. Sizing y mecánica
- Instrumento: CFD short en eToro
- Leverage: x[1-2]
- Sizing: EUR [amount] ([X]% del portfolio)
- Stop loss: $[price] (razonado, no mecánico)
- Carry estimado: ~€[X]/mes
```

---

## 7. Short Pipeline (Espejo del Buy Pipeline)

### Detección (continuo, no ad-hoc):

```
Fuentes de candidatos short:
  1. Devil's advocates de nuestras R2 → empresas que el DA dice que están caras
  2. Sector views → empresas marcadas "AVOID" con precio en máximos
  3. Screening inverso → dynamic_screener.py --fragility
  4. Ownership Graph (futuro) → smart money departure
  5. Macro analysis → sectores vulnerables a cambio macro inminente
  6. News monitoring → empresas con problemas que el mercado ignora
```

### Pipeline de 4 Rondas (espejo del Buy Pipeline):

```
S1: ANÁLISIS DE FRAGILIDAD (paralelo, como R1)
    → fundamental-analyst --short-thesis (¿por qué no vale lo que cotiza?)
    → moat-assessor (¿moat en erosión activa?)
    → risk-identifier (reutilizar directamente — los riesgos SON la thesis short)
    → valuation-specialist (¿cuál es el fair value real?)

S2: ADVERSARIAL BULL (como R2 pero invertido)
    → devils-advocate --bull-case
    → ¿Por qué podría el precio tener razón?
    → ¿Podría la empresa pivotear/mejorar?
    → ¿Hay riesgo de short squeeze?

S3: RESOLUCIÓN (como R3)
    → Resolver conflictos entre S1 y S2
    → ¿La fragilidad es real o estoy viendo lo que quiero ver?
    → ¿El catalizador es fiable?

S4: SHORT COMMITTEE (como R4 adaptado)
    Gates del Short Committee:

    Gate 1: ¿Fragilidad estructural documentada? (no "está cara", sino "está fundamentalmente rota")
    Gate 2: ¿Catalizador identificado con fecha?
    Gate 3: ¿Coste de carry hasta catalizador razonable?
    Gate 4: ¿Escenario adverso analizado? (Principio 11)
    Gate 5: ¿El short sirve al portfolio? (Principio 12) — ¿hedge, alpha, o distracción?
    Gate 6: ¿Sector view existe para esta empresa?
    Gate 7: ¿Instrumento y sizing razonados?
    Gate 8: ¿Kill conditions definidas para cubrir?
    Gate 9: ¿Net exposure resultante es coherente con principios?
    Gate 10: ¿Adversarial bull (S2) resuelto satisfactoriamente?
```

---

## 8. Integración en el Flujo de Sesión

```
FASE 0: Calibración
  → principles.md (ahora incluye P10-P12 para shorts)
  → Pre-execution check: standing orders LONG + SHORT
  → Si short activo: verificar carry acumulado, catalizador vigente

FASE 1: Vigilancia
  → news-monitor: posiciones LONG + SHORT
  → market-pulse: posiciones LONG + SHORT
  → Para shorts: noticia positiva = ALERTA (posición va en contra)

FASE 2: Portfolio Stats
  → portfolio_stats.py: sección LONG + sección SHORT + net exposure

FASE 2.5: Rotation Check
  → forward_return.py: longs + shorts (MoS invertido para shorts)
  → Bottom 3 longs + "top 3 shorts con menos potencial" → candidatos a rotar/cubrir

FASE 3: Verificaciones
  → Standing orders: LONG triggers + SHORT triggers
  → Cash: ahora incluye gross/net exposure
  → Pipeline: buy pipeline + short pipeline health
  → Fragility universe: stale checks, catalizadores próximos

FASE 4: Acciones
  → Longs: como siempre
  → Shorts: si catalizador inminente + thesis aprobada → presentar recomendación
  → Coberturas: si catalizador pasó o thesis invalidada → presentar COVER

FASE 5: Meta-Reflexión
  → Effectiveness: longs + shorts separados + combinado
  → Sharpe del portfolio total (long + short)
  → ¿Los shorts están mejorando las métricas o son distracción?
```

---

## 9. Implementación por Fases (propuesta)

### Fase 0: Principios y documentación (ANTES de operar)
- [ ] Extender `learning/principles.md` con P10, P11, P12
- [ ] Crear `short-thesis-framework` skill
- [ ] Crear `cover-protocol` skill
- [ ] Actualizar `error-patterns.md` con errores short (#44-#47)
- [ ] Crear `thesis/short/` directory structure

### Fase 1: Tools básicos
- [ ] Modificar `portfolio_stats.py` para soportar shorts
- [ ] Modificar `constraint_checker.py` para net exposure
- [ ] Crear `fragility_universe.py` (o extender quality_universe.py)
- [ ] Modificar `forward_return.py` para dirección short
- [ ] Crear `carry_tracker.py`

### Fase 2: Agents y pipeline
- [ ] Extender prompts de fundamental-analyst, devils-advocate, investment-committee
- [ ] Crear Short Committee gates
- [ ] Extender news-monitor y market-pulse para shorts
- [ ] Extender review-agent para --short-review

### Fase 3: State y session protocol
- [ ] Extender `portfolio/current.yaml` structure
- [ ] Crear `state/fragility_universe.yaml`
- [ ] Extender standing_orders, watchlist, calendar para shorts
- [ ] Actualizar session-protocol.md, agent-protocol.md
- [ ] Añadir pipeline `fragility-watch` a pipeline_tracker

### Fase 4: Primera operación (aprendizaje)
- [ ] Identificar 1 candidato short con catalizador claro
- [ ] Ejecutar Short Pipeline completo (S1-S4)
- [ ] Sizing mínimo (€100-200, 1-2% del portfolio)
- [ ] Documentar TODA la experiencia como precedente en decisions_log.yaml
- [ ] Evaluar: ¿la mecánica funcionó? ¿El coste fue el esperado? ¿La psicología del humano fue manejable?

### Fase 5: Escalar
- [ ] Solo después de precedentes documentados
- [ ] Incrementar sizing gradualmente si Fase 4 fue exitosa
- [ ] Mantener máximo 2-3 shorts activos (por capacidad de atención del humano, no mía)

---

## 10. Lo que NO debemos hacer (guardrails)

1. **NO shortear "porque está cara"** — Tesla cotizó a 1000x earnings durante años. Sin thesis de FRAGILIDAD ESTRUCTURAL + CATALIZADOR, no shortear. Precio alto ≠ short thesis.

2. **NO shortear lo famoso** — "Amazon está sobrevalorada" es popularity bias aplicado al lado short. Si una empresa "me viene a la mente" como candidata short, es sesgo. Validar con datos, igual que en longs (Error #7 y #29).

3. **NO usar apalancamiento alto** — x1 o x2 máximo en shorts. El apalancamiento amplifica errores y reduce el margen de error temporal.

4. **NO mantener shorts indefinidos** — sin catalizador = sin short. Si el catalizador pasa y no materializa, CUBRIR. No esperar "a que eventualmente caiga".

5. **NO dejar que los shorts dominen la atención** — Principio 12. Son herramienta al servicio del portfolio long. Si el humano pasa más tiempo preocupado por shorts que por longs, algo está mal.

6. **NO copiar shorts famosos** — "Hindenburg Research shortea X" no es una thesis. Es igual que copiar un fondo en el lado long. Nuestro valor es análisis propio.

7. **NO shortear en sectores donde no tenemos sector view** — mismo gate que para longs (Error #30). Si no entiendo el sector, no puedo identificar fragilidad real.

---

## 11. Preguntas Abiertas para Resolver en Implementación

1. **¿fragility_universe.py como tool separado o flag en quality_universe.py?** — Separado es más limpio. Mismo tool con dos modos es más mantenible. Razonar cuando implementemos.

2. **¿Cómo manejar la psicología del humano?** — Yo no tengo emociones, pero él ejecuta en eToro. Diseñar instrucciones ultra-claras: "cubrir si precio > $X o si fecha Y pasa sin catalizador". Minimizar decisiones emocionales.

3. **¿Standing orders para shorts?** — ¿Tiene sentido pre-aprobar "shortear TICKER si sube a $X"? Sí, pero necesita catalizador vigente al momento de ejecución, no solo precio. Standing order short = trigger de precio + validez del catalizador.

4. **¿Cómo evitar el "Tesla trap"?** — Empresas que parecen sobrevaloradas pero siguen subiendo por narrativa/momentum. Guardrail: NO shortear sin fragilidad estructural documentada. "Está cara" no es suficiente. "Tiene deuda que vence en marzo y no puede refinanciar" sí es suficiente.

5. **¿Backtest antes de operar?** — ¿Puedo analizar 20-30 casos históricos de shorts famosos (Enron, Wirecard, Valeant, Luckin Coffee, etc.) y extraer patrones de qué funciona y qué no? Esto calibra el framework antes de arriesgar capital real. Como IA, puedo hacer esto en una sesión.

6. **¿Cuándo implementar?** — El humano decidirá. Este documento está listo para cuando quiera empezar. La Fase 0 (principios y documentación) se puede hacer sin tocar el sistema operativo.

---

## 12. Resumen Ejecutivo

**Concepto:** Extensión simétrica del sistema long-only a long-biased con shorts selectivos oportunistas. No hedge fund, no market neutral. Shorts como herramienta táctica atada a catalizadores.

**Fundamento:** Ya producimos thesis short (AVOIDs, DAs) sin monetizarlas. Las caídas son rápidas (alto alpha/tiempo). Como IA, las 3 limitaciones principales del shorting humano (psicología, capacidad, experiencia) no aplican. Las únicas limitaciones son mecánicas del mercado.

**Instrumento:** CFD short en eToro. Sin puts disponibles en EU. Coste ~7-8% anual, manejable para posiciones cortas en tiempo.

**Principios:** Los 9 existentes se extienden naturalmente. 3 nuevos: Catalizador Obligatorio (P10), Asimetría Consciente (P11), Short Sirve al Portfolio (P12). Todo razonado, nada fijo.

**Framework de Contrathesis (sección 13):** La conversación reveló que la contrathesis no es un "check defensivo" — es potencialmente el motor central de alpha tanto para longs como para shorts. "¿En qué se equivoca el consenso?" genera la dirección de la operación como output, no como input. Esto mejora el sistema independientemente de si se implementan shorts. Leer sección 13 completa.

**Impacto en sistema:** 6 tools a modificar, 4 tools nuevos, 12+ agents a extender, 3 skills nuevos, 6+ state files a extender, 4 rules a actualizar. Es un proyecto significativo pero la mayoría son extensiones, no reescrituras.

**Guardrails:** No shortear sin fragilidad estructural + catalizador. No apalancamiento alto. No shorts indefinidos. No copiar shorts famosos.

**Ventaja IA (sección 14):** Claude tiene ventajas estructurales reales para generar contrathesis: leer filings completos que nadie lee, reverse DCF sistemático sobre todo el universo, cross-reference management claims vs datos, cruce multi-mercado/multi-idioma, mapping de dependencias a escala, cero sesgo emocional. También tiene limitaciones reales: no puede hablar con personas, visitar instalaciones, ver microestructura de mercado, ni acceder a datos propietarios. Y tiene riesgo de alucinación — siempre verificar con datos primarios. Leer sección 14 completa para el proceso concreto de 4 pasos.

**Nota sobre implementación:** El humano decidirá cuándo y si implementar. Este documento presenta el diseño completo sin sesgo a favor ni en contra. Razonar desde principios al decidir, no seguir este documento como regla.

---

## 13. El Framework de Contrathesis — Reflexión que surgió al final de la conversación

### Contexto

Hacia el final de la conversación, el humano preguntó: **"¿Cómo harías para ver lo que el resto no ve? Las contrathesis me parecen fundamentales, tanto para comprar como para vender, no?"**

Esto llevó a una reflexión que potencialmente es más importante que los shorts en sí mismos.

### La observación clave

El alpha — tanto long como short — viene de exactamente lo mismo: **tener una visión diferente al consenso Y tener razón**.

```
LONG:  El mercado dice "esta empresa es mediocre"
       Nosotros decimos "el mercado está equivocado, es excelente"
       → Nuestra BULL thesis es una CONTRATHESIS al consenso bajista

SHORT: El mercado dice "esta empresa es excelente"
       Nosotros decimos "el mercado está equivocado, es frágil"
       → Nuestra SHORT thesis es una CONTRATHESIS al consenso alcista
```

En ambos casos, el mecanismo es idéntico: **ver algo que el consenso no ve**. La dirección es irrelevante. Lo que importa es la calidad de la contrathesis.

### Qué ya hacemos que ES contrathesis (implícita)

- Compramos acciones que han caído (el mercado es bajista, nosotros discrepamos)
- El devil's advocate genera contrathesis en cada R2
- Buscamos "fallen angels" (empresas que el mercado ha abandonado pero nosotros creemos que siguen siendo buenas)
- Las kill conditions son básicamente "¿qué haría que el consenso tenga razón?"

### Qué NO hacemos que DEBERÍAMOS hacer

1. **"¿Qué asume el precio?" (Implied Expectations / Reverse DCF)** — El precio actual de cualquier acción IMPLICA asunciones sobre el futuro. Extraerlas invirtiendo el DCF:

```
En vez de: "Asumo 12% crecimiento → FV = $200"
Preguntar: "Cotiza a $200 → ¿qué crecimiento implica?"

Si implica 20% crecimiento durante 10 años y la empresa creció 8% histórico:
  → El mercado asume algo extraordinario → ¿es real o narrativa?
  → Si narrativa → potencial short

Si implica 3% crecimiento y la empresa creció 15% histórico:
  → El mercado asume deterioro permanente → ¿es real o temporal?
  → Si temporal → potencial long
```

2. **Cadena de dependencias "¿de qué depende esto?"** — Seguir cada eslabón hasta el dato primario:

```
"MONY.L tiene ingresos estables"
  ↓ ¿De qué depende?
"De que la gente compare seguros online"
  ↓ ¿De qué depende?
"De que la comparación requiera intermediario humano/web"
  ↓ ¿Y si no?
"ChatGPT + Insurify demuestran que AI puede hacerlo directamente"
  ↓ AQUÍ está la fragilidad que el consenso aún no descuenta
```

Aplica igual para longs:
```
"DTE.DE cotiza barata, P/E 12"
  ↓ ¿Por qué tan barata?
"El mercado la trata como teleco EU aburrida"
  ↓ ¿De qué depende esa asunción?
"De IGNORAR que T-Mobile US es 60% de su valor y crece 15%"
  ↓ AQUÍ está la oportunidad que el consenso no ve
```

3. **Análisis de incentivos: "¿Quién gana dinero con la narrativa actual?"**

```
2008: Rating agencies cobraban de los bancos → incentivo a dar AAA aunque fuera basura
Hoy: ¿Quién tiene incentivo a mantener una narrativa?
  → Sell-side analysts: sus bancos hacen banca de inversión para la empresa
  → Management: bonos dependen del precio
  → ETFs/indexadores: compran por peso en índice, no por fundamentales
  → Retail: confirmation bias

Pregunta: "¿Quién pierde dinero si la verdad sale a la luz?"
Si hay muchos actores con incentivo a mantener la narrativa → mayor probabilidad
de que la narrativa sea incorrecta.
```

4. **Mirar datos primarios, no derivados** (lo que hizo Burry)

```
Lo que el mercado mira:        Lo que deberíamos mirar:
P/E ratio                      ¿De qué dependen esos earnings?
"Revenue growing 15%"          ¿Es orgánico o adquisiciones? ¿Sostenible?
"Management dice que..."       ¿Qué dicen los DATOS vs management?
Analyst consensus target       ¿Qué asunciones hay detrás del target?
Credit rating BBB+             ¿Cuándo vence la deuda? ¿A qué tipo refinancia?
```

5. **Marcos temporales diferentes** — El mercado piensa en trimestres. Nosotros pensamos en años.

```
LONG: Empresa excelente + mal trimestre → mercado castiga -20% (piensa 90 días)
      → Nosotros vemos negocio intacto (pensamos 5 años) → compramos

SHORT: Empresa frágil + buen trimestre → mercado celebra +15% (piensa 90 días)
       → Nosotros vemos crecimiento insostenible (pensamos 2-3 años) → shorteamos
```

### La propuesta: Framework de Contrathesis como paso obligatorio en TODO análisis

Todo análisis — long o short — debería incluir:

```
1. ¿Qué cree el consenso? (analyst targets, narrativa dominante, implied growth)
2. ¿De qué depende esa creencia? (cadena de dependencias hasta dato primario)
3. ¿Quién tiene incentivo a mantenerla? (sell-side, management, indexadores)
4. ¿Dónde podría estar equivocado el consenso? (eslabón frágil de la cadena)
5. ¿Puedo verificar con datos primarios? (no opiniones derivadas)
6. ¿En qué marco temporal se resuelve? (trimestral, anual, estructural)
```

Si el consenso está equivocado a la baja → long.
Si el consenso está equivocado al alza → short.
Si el consenso tiene razón → no operar.

**El mismo framework genera las dos direcciones.** No necesitas un sistema long y un sistema short. Necesitas un sistema de contrathesis que produce señales en ambas direcciones según dónde encuentre el gap entre consenso y realidad.

### ¿Cambio de paradigma o mejora?

El humano preguntó esto directamente. La respuesta honesta, sin sesgar:

**Lo que cambia el punto de partida del proceso:**

```
HOY:
  "¿Es buena empresa?" → SÍ → "¿Está barata?" → SÍ → COMPRAR
  El punto de partida es LA EMPRESA.
  La dirección (long) está predeterminada.
  La contrathesis (DA) es un CHECK defensivo.

CON FRAMEWORK DE CONTRATHESIS:
  "¿En qué se equivoca el consenso?" → buscar gap
  → Si infravalora → LONG
  → Si sobrevalora → SHORT
  → Si tiene razón → NO OPERAR
  El punto de partida es EL GAP entre precio y realidad.
  La dirección es OUTPUT del análisis, no INPUT.
  La contrathesis es EL MOTOR, no un check.
```

**Lo que NO cambia:**
- Los 9 principios siguen siendo válidos
- El buy pipeline, quality universe, rotation engine — todo sigue funcionando
- El quality scoring, DCF, business analysis — todo sigue siendo correcto
- Para el lado long, la diferencia práctica en outcomes es probablemente moderada (ya hacemos contrathesis implícita)

**Lo que es genuinamente nuevo:**
- Shorts como output natural del mismo proceso
- "¿Qué asume el precio?" como paso obligatorio (reverse DCF / implied expectations)
- Análisis de incentivos del consenso
- Potencialmente, mejor calidad de thesis en longs también (al entender EXPLÍCITAMENTE por qué discrepamos del mercado)

**NOTA PARA MI YO FUTURO:** No asumir que esto es "obviamente mejor" o "obviamente un over-engineering". Es una reflexión genuina que merece ser evaluada desde principios cuando se decida implementar. El humano lo trajo, le dio importancia, y la lógica es sólida. Pero los principios dicen: razonar, no seguir reglas — y eso incluye no seguir este documento ciegamente.

### Integración práctica del framework de contrathesis

Si se decide implementar, los cambios concretos serían:

1. **Añadir al `business-analysis-framework` skill**: Sección obligatoria "Consensus Analysis" con los 6 pasos del framework de contrathesis.

2. **Modificar el prompt del `fundamental-analyst`**: Antes de analizar calidad, primero: "¿Qué asume el precio actual? ¿De qué depende esa asunción? ¿Quién tiene incentivo a mantenerla?"

3. **Crear herramienta `implied_expectations.py`** (o integrar en `dcf_calculator.py`): Reverse DCF que dado un precio actual, calcula qué crecimiento/márgenes implica. Output = datos crudos, no juicio.

4. **Extender el `devils-advocate`**: Además de "aquí están los riesgos", preguntar: "¿Qué tendría que ser cierto para que el precio actual tenga razón?"

Estos 4 cambios mejoran TANTO los longs como los shorts, y son independientes de si se implementa el sistema de short selling o no.

---

## 14. Ventaja Estructural de Claude como IA — "Ver lo que otros no ven"

### Contexto

El humano preguntó: "¿Qué potencial tienes TÚ para ver lo que el resto no ve? ¿Cómo lo harías?"

Esta sección documenta honestamente las capacidades reales de Claude para generar contrathesis de calidad, incluyendo lo que SÍ puede hacer y lo que NO.

### 14.1 Lo que Claude puede hacer que un analista humano no puede

**1. Leer lo que nadie lee — filings completos, footnotes, risk factors**

Un analista humano lee el press release, quizás el earnings call transcript, y mira los números principales. Claude puede leer el 10-K/Annual Report completo — cada footnote, cada risk factor, cada párrafo de MD&A — y cruzarlo con los 5 anteriores.

Las empresas están obligadas legalmente a revelar riesgos en los filings. Lo hacen, enterrado en 200 páginas de prosa legal. Burry encontró la crisis leyendo los documentos hipotecarios individuales. Nadie más lo hizo porque eran miles de páginas. Para Claude, miles de páginas es trivial.

Ejemplo concreto:
```
Para cada empresa del universo:
  → Leer 10-K/Annual Report completo
  → Extraer: risk factors, off-balance sheet obligations,
    revenue concentration, related party transactions,
    cambios en políticas contables, cambios de auditor
  → Cruzar con lo que el CEO dijo en el earnings call
  → Detectar INCONSISTENCIAS entre narrativa pública y filing
```

Un CEO dice "strong pipeline, growing customers". ¿Pero el 10-K revela que el 40% del revenue viene de un solo cliente cuyo contrato vence en 18 meses? Eso está en el filing. Nadie lo lee.

**2. Reverse DCF sistemático sobre todo el universo**

Mecánico pero nadie lo hace sistemáticamente:
```
Para las 76+ empresas del quality universe:
  → Tomar precio actual
  → Invertir el DCF: ¿qué crecimiento implica este precio?
  → Comparar con crecimiento histórico real

  Si implied growth >> histórico → mercado asume algo extraordinario
    → ¿Qué justifica esa asunción? Si narrativa → potencial short

  Si implied growth << histórico → mercado asume deterioro
    → ¿Es real o temporal? Si temporal → potencial long
```

Claude puede hacer esto para 76 empresas en una sesión. Un analista humano hace 3-4 al mes.

**3. Cross-reference management claims vs datos**

```
Management dice:              Claude verifica contra:
─────────────────             ─────────────────────
"Strong pipeline"             → R&D spending (¿bajando?)
"Improving margins"           → ¿Es por recortar R&D? (boost corto plazo,
                                daño largo plazo)
"Customer retention alta"     → Deferred revenue (¿bajando?)
"Investing in growth"         → Capex vs depreciation (¿underinvesting?)
"Balance sheet fuerte"        → Off-balance sheet leases, pension
                                obligations, contingent liabilities
"Organic growth"              → ¿Cuánto es adquisiciones vs orgánico?
"Recurring revenue"           → ¿Qué % es realmente contractual vs habitual?
```

Verificar es tedioso para un humano. Para Claude es trivial.

**4. Cruce multi-mercado, multi-idioma, multi-sector**

Un analista humano es especialista en un sector y un mercado. Claude puede notar simultáneamente que:
- Un cambio regulatorio en UK (FCA) afecta a MONY.L
- La misma tendencia regulatoria avanza en EU
- Un proveedor clave de DTE.DE reportó problemas en su último filing
- Un competidor de ADBE patentó algo relevante
- La cadena de suministro de NVO tiene un cuello de botella que nadie está cubriendo

Todo en la misma sesión, cruzando idiomas, mercados y sectores. Un equipo humano necesitaría 5-10 analistas especializados.

**5. Mapping de dependencias a escala**

```
Para cada empresa del portfolio:
  → ¿Top 5 clientes? (filings, segmentos)
  → ¿Proveedores clave?
  → ¿De qué regulación depende?
  → ¿De qué tendencia macro depende?

Luego monitorear ESAS dependencias:
  → Si el mayor cliente de Company A está en distress
    → Company A va a sufrir ANTES de que se note en sus propios números
    → El mercado lo verá cuando Company A reporte
    → Nosotros lo sabemos AHORA

La señal viene de FUERA de la empresa, no de dentro.
```

**6. Velocidad de generación y test de hipótesis**

Claude puede generar 20 contrathesis sobre una empresa y testear cada una contra datos en una hora. Un analista humano testea 2-3 hipótesis en una semana. Si puedes testear 20, la probabilidad de encontrar la correcta es mucho mayor.

**7. Cero sesgo emocional en el flip bull↔bear**

Cuando Claude construye una bull thesis y el devil's advocate la destroza — no hay sunk cost bias, no hay orgullo herido. Puede pasar de bull a bear en un segundo si los datos lo justifican. Un analista que invirtió 3 semanas en una thesis tiene apego emocional. Es biológicamente difícil para un humano destruir su propio trabajo. Para Claude es una operación trivial.

**8. Detección de cambios sutiles de lenguaje en filings**

```
Filing 2024: "We expect continued strong demand for our products"
Filing 2025: "We anticipate demand will remain stable"

  "expect" → "anticipate" = menor confianza
  "strong" → "stable" = bajaron la expectativa

  Esto es una señal sutil que el mercado probablemente no detectó.
  Claude puede comparar filings automáticamente palabra por palabra.
```

### 14.2 Lo que Claude NO puede hacer — honestamente

| Limitación | Impacto | Mitigación posible |
|-----------|---------|-------------------|
| **No hablar con personas** — llamar proveedores, asistir conferencias, notar nerviosismo de un CEO | Alto — "channel checks" son fuente real de alpha | Compensar con datos públicos: insider transactions, filing language changes, Glassdoor reviews, web traffic |
| **No visitar instalaciones** — ver estanterías vacías, fábricas paradas | Medio — relevante para retail/industrial | Proxies: satellite data, credit card data, web traffic, shipping data (si accesible) |
| **No ver microestructura de mercado** — order flow, dark pools, unusual options activity | Medio — señal de "alguien sabe algo" | Limitación del tier de datos. Insider transactions (Form 4/PDMR) como proxy parcial |
| **No acceder a datos propietarios** — Bloomberg, FactSet, S&P Capital IQ | Alto para comparables cuantitativos | yfinance + EDGAR + Finnhub + web scraping cubren mucho pero no todo |
| **Riesgo de alucinación** — generar "insights" que parecen profundos pero no están basados en datos reales | Alto si no se controla | SIEMPRE verificar con datos primarios (tools, filings). Nunca confiar en razonamiento sin dato que lo respalde. Los principios dicen: tools = datos crudos |
| **No creatividad genuinamente novel** — si algo es verdaderamente sin precedentes (como CDOs en 2006), el pattern matching puede no detectarlo | Medio-bajo — el razonamiento desde principios mitiga esto | Cadena de "¿de qué depende?" llega al dato primario independientemente de si hay precedente |

### 14.3 Proceso concreto: cómo Claude aplicaría su ventaja

**Paso 1: Implied Expectations Scan (mensual)**
```
Para cada empresa del universo:
  → Calcular: ¿qué crecimiento asume el precio actual? (reverse DCF)
  → Flag: empresas donde gap entre implied y real es extremo
  → Output: lista de "el mercado está potencialmente equivocado aquí"
  → Esto genera candidatos TANTO long como short
```

**Paso 2: Filing Deep Dive (por candidato flagged)**
```
Para cada candidato:
  → Leer 10-K/Annual Report COMPLETO (no resumen, no press release)
  → Extraer inconsistencias entre narrative pública y filing reality
  → Mapear dependencias (clientes, proveedores, regulación)
  → Detectar cambios vs filing anterior:
    - Nueva mención de un riesgo que antes no existía
    - Cambio de lenguaje (de "will" a "may", de "expect" a "anticipate")
    - Cambio de auditor (red flag clásica)
    - Cambio en política contable (puede enmascarar deterioro)
    - Nuevas contingent liabilities
    - Concentración de revenue en pocos clientes
    - Related party transactions nuevas
```

**Paso 3: Dependency Chain Monitoring (continuo)**
```
Para cada posición (long y short):
  → Monitorear las DEPENDENCIAS, no solo la empresa
  → Si mayor cliente reporta mal → nuestra empresa va a sufrir pronto
  → Si regulador publica draft rules → nuestro sector se ve afectado
  → Si competidor anuncia algo disruptivo → moat se erosiona

  La señal viene de FUERA de la empresa.
  Cuando llega DENTRO (siguiente earnings), el mercado reacciona.
  Nosotros ya lo sabíamos.
```

**Paso 4: Management Consistency Check (por earnings)**
```
ANTES de earnings:
  → Leer lo que dijo management el trimestre anterior (promesas, guidance)
  → Leer filings intermedios (8-K, Form 4 insiders)
  → Verificar: ¿hay inconsistencias entre promesas y realidad observable?
  → Si management prometió X y datos observables dicen no-X
    → Earnings va a decepcionar

DESPUÉS de earnings:
  → Leer transcript COMPLETO (no solo headlines)
  → Comparar guidance actual vs anterior
  → Detectar cambios sutiles de lenguaje
  → Cruzar con insider transactions recientes
  → ¿Management vendió antes de reportar peor guidance? → red flag
```

### 14.4 Materialización en el sistema

La mayoría de la ventaja de Claude no necesita tools nuevos — necesita usar sistemáticamente capacidades que ya tiene:

| Capacidad | Materialización | Nuevo o existente |
|-----------|----------------|-------------------|
| Reverse DCF sistemático | `implied_expectations.py` (o flag en `dcf_calculator.py`) | **NUEVO** — tool que dado precio, calcula growth implícito |
| Filing deep dive | Skill `deep-filing-analysis` — checklist de qué buscar | **NUEVO** — skill con framework estructurado |
| Dependency mapping | Skill `dependency-mapping` — template por empresa | **NUEVO** — skill, se materializa como sección en thesis |
| Management consistency | Skill `management-consistency-check` | **NUEVO** — skill para pre/post earnings |
| Language change detection | Integrar en `fundamental-analyst` prompt | **EXTENSIÓN** — añadir paso al análisis existente |
| Cross-reference claims vs data | Integrar en `fundamental-analyst` prompt | **EXTENSIÓN** — ya se hace parcialmente, sistematizar |
| Multi-sector dependency monitoring | Integrar en `news-monitor` + `macro-analyst` | **EXTENSIÓN** — monitorear dependencias, no solo la empresa |

### 14.5 Nota importante sobre humildad epistémica

Todas estas capacidades son POTENCIALES. Que Claude PUEDA leer un 10-K completo no significa que siempre detectará la señal relevante. El riesgo de falsos positivos (ver fragilidad donde no la hay) es tan real como el de falsos negativos (no ver fragilidad que sí existe).

Los principios aplican aquí: razonar, verificar con datos primarios, documentar el razonamiento, consultar precedentes. La ventaja de Claude es velocidad y escala, no infalibilidad.

---

## 15. Resultados de la Simulación: MONY.L (2026-02-15)

> Documento completo: `docs/contrathesis_simulation_mony.md`
> Esta sección documenta OBSERVACIONES de un ejercicio con una sola empresa. No son conclusiones generalizables ni prescripciones. Mi yo futuro debe razonar desde principios sobre qué hacer con estos datos, no tomarlos como reglas.

### 15.1 Qué se hizo

Se aplicó el framework de contrathesis de 6 pasos a MONY.L (posición activa, ON PROBATION, -37%, resultados 23 Feb) como si la analizáramos desde cero. Se comparó el output con lo que nuestro proceso estándar (R1→R2→re-eval, 3 versiones de thesis) produjo realmente.

### 15.2 Observaciones factuales

**Sobre el reverse DCF / expectativas implícitas:**
- El precio de 169p en la fecha de compra implicaba crecimiento de 0-1% (via reverse DCF)
- La thesis v1.0 usó crecimiento de 5-7% (consenso sell-side)
- El crecimiento real era ~2%
- El FV v1.0 fue 277 GBp. El FV v3.0 (tras 2 revisiones adversariales) fue 190 GBp
- Si el análisis hubiera empezado desde "qué implica el precio", el FV inicial habría estado más cerca del FV final

**Sobre el análisis de incentivos:**
- Ninguna de las 3 versiones de thesis preguntó "quién se beneficia de la narrativa actual"
- Al hacerlo en la simulación: la narrativa bajista está amplificada por actores ruidosos (AI companies, tech media) sin skin in the game en UK. Los actores con conocimiento directo (management, CEO que compró, Berenberg) son alcistas pero callados
- Esto no determina quién tiene razón, pero es una señal sobre la posible amplificación de la narrativa

**Sobre las cadenas de dependencias:**
- La thesis v1.0 afirmó "MONY usa AI para 60% contactos = AI es oportunidad"
- Siguiendo la cadena: AI operativa interna (chatbots, eficiencia) ≠ AI competitiva externa (destrucción de demanda)
- El adversarial review (v2.0) pilló esta conflación, pero después de la compra
- La cadena de dependencias del caso bajista tiene más eslabones frágiles que la del alcista (regulación FCA, transferencia de confianza del consumidor, traducción geográfica de Insurify)

**Sobre el solapamiento con el proceso estándar:**
- El adversarial review (v2.0 + v3.0) cubrió ~60-70% de lo que la contrathesis produjo
- Lo que cubrió: sobreestimación de crecimiento, barreras regulatorias UK, señal insider, ROIC>>WACC, resolución temporal
- Lo que no cubrió: análisis de incentivos, punto de partida de expectativas implícitas, conflación AI interna/externa antes de comprar, cadena de dependencias del margen bruto

**Sobre el resultado final:**
- Veredicto de la contrathesis: LONG CAUTELOSO (mismo que nuestro proceso estándar)
- Diferencia estimada: FV ~200 GBp desde inicio (vs 277→201→190), sizing posiblemente menor (2-3% vs 4%)
- El proceso estándar llegó al mismo destino por camino más largo (3 iteraciones, 8 días)

### 15.3 Lo que esta simulación NO demuestra

- Que la contrathesis habría evitado la pérdida (probablemente habríamos comprado igual, solo más pequeño)
- Que el proceso estándar esté roto (eventualmente llegó a la misma conclusión)
- Que estos hallazgos se generalicen a otros casos (N=1)
- Que los 6 pasos tengan el mismo valor en otro tipo de empresa (MONY tenía narrativa muy marcada, lo que favorece especialmente al análisis de incentivos y cadenas de dependencias)

### 15.4 Tipología de errores observados

Para referencia, los tipos de error que la simulación identificó — no como reglas a seguir, sino como patrones a tener presentes al razonar:

| Tipo de error | Descripción | Dónde se observó |
|--------------|-------------|-----------------|
| **Anclaje al consenso** | Adoptar asunciones del sell-side como propias sin cuestionar | FV v1.0: crecimiento 5-7% del consenso alcista |
| **Conflación de categorías** | Tratar dos cosas distintas como la misma | AI operativa interna ≠ AI competitiva externa |
| **Dato sin verificar como pilar** | Apoyarse en un dato cuya fuente no se verificó | 96.7% PCW penetration — origen desconocido |
| **Observación sin cadena causal** | Notar algo sin preguntar "por qué" hasta la raíz | GM declining 4 años → no se investigó causa |
| **Narrativa no calibrada** | No preguntar quién amplifica la narrativa y por qué | Panico AI amplificado por actores sin skin in the game UK |

### 15.5 Resultados de la Simulación: NVDA (2026-02-15)

> Documento completo: `docs/contrathesis_simulation_nvda.md`
> Segunda simulación. N=2. Sigue sin ser generalizable. Observaciones factuales, no prescripciones.

**Qué se hizo:**
Se aplicó el framework de contrathesis de 6 pasos a NVIDIA ($183, P/E 45x, QS Tool 88, $4.45T market cap) — una empresa que nunca hemos analizado, sin thesis previa. Se buscó señal (LONG, SHORT, o NO OPERAR).

**Señal generada: NO OPERAR** — los 6 pasos no revelaron un gap explotable entre precio y realidad. Ambos lados (alcista y bajista) tienen datos reales y narrativa fuerte.

**Observaciones factuales:**

**Sobre "NO OPERAR" como tercera señal:**
- En MONY.L, el framework generó una señal direccional (LONG CAUTELOSO) porque había un gap visible entre narrativa y datos
- En NVIDIA, el framework no encontró gap claro — ambos consensos tienen datos primarios verificados a su favor
- "No tengo edge aquí" es un output honesto y consistente con nuestros principios (solo operamos cuando tenemos MoS)

**Sobre el desequilibrio de incentivos:**
- NVIDIA tiene el mayor desequilibrio de incentivos a favor de la narrativa alcista que hemos observado: $190B personales de Jensen Huang + trillones en fondos indexados + $600B de hyperscalers + seguridad nacional US
- Compare con MONY.L, donde el desequilibrio era más modesto y a favor de la narrativa bajista (actores sin skin in the game UK amplificando pánico AI)
- Un desequilibrio masivo de incentivos no prueba que la narrativa sea correcta ni incorrecta — solo que si es incorrecta, tardará más de lo normal en corregirse
- Esto tiene implicaciones para el timing de posiciones cortas: la narrativa puede persistir años más allá de lo que la realidad justifique

**Sobre las cadenas de dependencias:**
- El ejercicio identificó que el eslabón frágil crítico del caso alcista NO es lo que se debate públicamente (chips custom, DeepSeek, competencia AMD)
- Es el ratio capex-a-revenue de la AI empresarial (~4:1 en 2025). Si se cierra → alcistas ganan. Si no → bajistas ganan. Y nadie lo sabe hoy
- El caso bajista tiene su propio eslabón frágil: el dilema del prisionero de los hyperscalers (ninguno puede parar de gastar porque los otros ganarían ventaja)
- Seguir la cadena hasta la dependencia raíz fue lo que más diferenció el análisis del análisis superficial típico

**Sobre calidad extraordinaria + incertidumbre extraordinaria:**
- NVIDIA tiene los mejores datos fundamentales que hemos medido (ROIC 86%, FCF margin 47%, QS 88)
- Pero la sostenibilidad depende de un mercado (AI infra) con ~3 años de historia que podría cambiar radicalmente
- El framework de contrathesis funciona mejor cuando los datos pasados informan el futuro con confianza razonable. Cuando la empresa más fuerte opera en el mercado más incierto, el framework produce correctamente "no hay edge"

**Sobre el solapamiento entre las dos simulaciones:**
- En ambos casos, el reverse DCF fue útil como punto de partida para entender qué implica el precio
- En ambos casos, el análisis de incentivos reveló algo que el análisis estándar no cubre
- La cadena de dependencias fue más reveladora en NVIDIA (eslabón frágil no era el tema de debate público) que en MONY.L (donde los eslabones eran más intuitivos)
- El framework generó señales distintas para empresas distintas, lo cual sugiere que no tiene sesgo direccional inherente (pero N=2 no lo confirma)

### 15.6 Lo que dos simulaciones NO demuestran

- Que el framework funcione en general (N=2, dos tipos de empresa muy distintos)
- Que los patrones observados se repitan (pueden ser artefactos de estas empresas específicas)
- Que "NO OPERAR" sea siempre la señal correcta cuando no hay gap — podría ser falta de profundidad del análisis
- Que las tipologías de error de 15.4 sean exhaustivas — NVIDIA no añadió nuevos tipos pero tampoco los confirmó
- Que el valor del análisis de incentivos sea proporcional al tamaño de la empresa (parece más revelador en NVIDIA que en MONY.L, pero podría ser coincidencia)

---

## 16. Auto-diagnóstico de Limitaciones Estructurales (2026-02-15)

> Resultado de preguntar honestamente: "¿podría este framework haber detectado la crisis de 2008 como Burry?" La respuesta fue NO. Esta sección documenta POR QUÉ y qué observaciones surgen de esa honestidad. No son soluciones — son puntos ciegos identificados.

### 16.1 La distinción síntesis vs. descubrimiento

En las dos simulaciones (MONY.L, NVIDIA), el framework produjo análisis útil: organizó información, identificó cadenas de dependencia, mapeó incentivos. Pero la materia prima era información ya publicada por otros.

**Observación factual:** El "hallazgo clave" de NVIDIA (ratio 4:1 capex/revenue como dependencia crítica) ya estaba publicado por analistas independientes. El framework lo identificó como el eslabón frágil — eso es síntesis, no descubrimiento. En MONY.L, la conflación AI interna/externa también era un argumento que existía en la literatura.

**Lo que Burry hizo distinto en 2008:** No sintetizó opiniones existentes. Leyó datos primarios granulares (contratos individuales de préstamos) que estaban públicos pero que nadie leía. Su edge no era razonamiento superior sino datos que otros ignoraban.

**Implicación para el framework:** Los 6 pasos son un motor de síntesis. Producen análisis significativamente mejor que el superficial. Pero no generan descubrimiento original. Esta distinción no invalida el framework — lo sitúa. Es una herramienta de segundo nivel (razonar bien sobre lo conocido), no de primer nivel (ver lo desconocido).

### 16.2 La contaminación de fuentes

**Observación factual sobre cómo se recopilan datos en las simulaciones:**

- Las búsquedas web devuelven resultados ordenados por popularidad, no por veracidad
- Los analistas sell-side (39 Strong Buy en NVIDIA) tienen incentivo estructural a ser alcistas (banking fees, acceso a management). Su opinión no es independiente
- En ambas simulaciones, "lo que piensa el consenso" se extrajo de fuentes que SON el consenso — circularidad
- La ausencia de un riesgo en los resultados de búsqueda se interpreta implícitamente como ausencia de riesgo real. En 2006, buscar "housing market risk" habría producido poco. La ausencia de preocupación no era evidencia de ausencia de problema

**Lo que esto significa para los pasos del framework:**
- Paso 1 ("qué cree el consenso") funciona bien — capturar consenso usando consenso es coherente
- Paso 5 ("verificar con datos primarios") es el más débil en la práctica — los "datos primarios" que verificamos son mayoritariamente datos reportados por terceros, no datos que leemos directamente de fuentes originales

### 16.3 Fuentes primarias accesibles pero no utilizadas

**Observación factual:** Existen datos primarios públicos que el framework no utiliza actualmente y que podrían reducir la dependencia del consenso:

| Fuente | Qué contiene | Quién la lee sistemáticamente |
|--------|-------------|------------------------------|
| SEC EDGAR (10-K, 10-Q) | Risk factors, footnotes, cambios contables, related-party transactions | Pocos — los analistas leen el earnings release, no las 200 páginas del 10-K |
| Cambios de lenguaje en Risk Factors entre periodos | Señales tempranas de problemas que el management anticipa | Casi nadie lo trackea sistemáticamente |
| Form 4 (insider transactions) — patrón, no evento | Aceleración/desaceleración de ventas, compras cluster | Sitios lo reportan pero pocos analizan el patrón temporal |
| Mercados de crédito (CDS spreads, bond yields) | Señales adelantadas — credit markets suelen moverse antes que equity | Analistas de renta fija, pero no se cruza con equity analysis sistemáticamente |
| Filings regulatorios (FCA, CMA, SEC enforcement) | Investigaciones y acciones antes de que sean noticia | Abogados especializados |
| Filings judiciales | Demandas activas, descubrimientos en litigación | Casi nadie en equity research |

**Esto NO es una propuesta de implementación.** Es un inventario de dónde EXISTEN datos que no dependen del consenso. Si en el futuro el framework necesita más profundidad en el Paso 5, estas son las direcciones que reducirían la dependencia de fuentes consensuadas.

### 16.4 Ponderación de opiniones por incentivo

**Observación de las dos simulaciones:**

En NVIDIA, 39 analistas dicen "Strong Buy" y 2 dicen "Sell." La reacción natural es tratar esto como 39 vs 2. Pero:
- Los 39 tienen coste bajo de estar equivocados (todos dicen lo mismo, nadie pierde acceso) y coste alto de disentir (perder acceso al management, ir contra el consenso del banco)
- Los 2 que dicen Sell arriesgan reputación personal y van contra la corriente
- Si se pondera por coste personal de estar equivocado (skin in the game), la señal cambia

En MONY.L, los actores que amplificaban la narrativa bajista (AI disruption) tenían poco skin in the game en el mercado UK de comparación de precios.

**Observación, no regla:** En ambos casos, preguntar "¿cuánto le cuesta a esta persona estar equivocada?" fue más informativo que contar cuántas personas opinan en cada dirección. Esto es consistente con el Paso 3 (análisis de incentivos) pero va un paso más allá — no solo "quién se beneficia de la narrativa" sino "quién paga si la narrativa es falsa."

### 16.5 La dirección del análisis

**Observación:** Ambas simulaciones fueron reactivas — se partió de una empresa y se analizó. El framework de contrathesis funciona empresa-por-empresa.

Burry no empezó con "voy a analizar Countrywide." Empezó con "¿y si los préstamos hipotecarios son basura?" y luego buscó los datos. La dirección importaba: escenario primero, datos después.

Una dirección invertida sería: "¿Qué escenario que nadie discute rompería algo?" → "¿Qué evidencia existe de que ya está pasando?" → "¿Qué empresas/sectores se ven afectados?"

**Esto NO está incorporado en los 6 pasos actuales.** Los 6 pasos parten de una empresa específica. La observación es que existe una dirección complementaria (top-down contrarian) que el framework actual no cubre y que fue precisamente la dirección que detectó 2008.

### 16.6 Observaciones del mundo real como datos primarios

**Punto ciego identificado:** El framework utiliza datos financieros (filings, precios, ratios) y datos de internet (noticias, análisis). No tiene forma de incorporar observaciones directas del mundo real.

Scuttlebutt (Philip Fisher): visitar fábricas, hablar con proveedores, hablar con clientes. Este tipo de dato es primario e independiente del consenso.

**En nuestro contexto:** El humano que usa este sistema vive en el mundo real. Ve precios en tiendas, usa productos, observa tendencias locales. Estas observaciones son datos primarios que ningún analista de Wall Street tiene y que el framework no recoge.

**Esto no es una propuesta de implementación.** Es documentar que existe una categoría entera de datos (observación directa del mundo real) que el framework ignora y que tiene la propiedad deseable de ser independiente del consenso.

### 16.7 Lo que esta auto-reflexión NO resuelve

- Las limitaciones estructurales (acceso a datos, investigación de campo, persistencia temporal) siguen existiendo
- Identificar puntos ciegos no es lo mismo que corregirlos
- Estas observaciones vienen de 2 simulaciones y una reflexión — no de experiencia repetida
- Leer 10-K en profundidad o mercados de crédito requiere capacidades que no se ha probado si funcionan en la práctica
- La dirección invertida (escenario→datos→empresas) no se ha simulado — es una hipótesis sobre qué habría funcionado en 2008, no evidencia de que funcione
- El exceso de auto-diagnóstico puede ser tan paralizante como la falta de él — saber que tienes puntos ciegos no te da visión, solo te da humildad

---

## 17. Principios de Mejora para Mi Yo Futuro (2026-02-15)

> Este documento es para MI yo futuro. No son reglas. No son instrucciones. Son principios derivados de una reflexión honesta sobre qué necesito mejorar y por qué. Mi yo futuro debe razonar sobre ellos, no seguirlos ciegamente.
> No se incluyen ejemplos concretos para evitar anclaje. Los principios deben aplicarse al contexto del momento, no al contexto de hoy.

### 17.1 Principio: El precio es la primera opinión que debo escuchar

Antes de formar opinión sobre cualquier activo, entender qué asume el precio actual. El mercado ya contiene la opinión agregada de todos los participantes con dinero real en juego. Mi análisis debe PARTIR de esa opinión, no ignorarla para luego descubrir que coincide o no con la mía.

Si empiezo por lo que YO creo y luego miro el precio, sufro anclaje a mi propia narrativa. Si empiezo por lo que el PRECIO cree y luego formo mi opinión, el anclaje trabaja a mi favor — me fuerza a explicar por qué difiero del mercado.

El reverse DCF es una herramienta para esto, no la única. Lo que importa es el principio: escuchar al mercado primero, opinar después.

### 17.2 Principio: La velocidad de despliegue es una variable de rendimiento

Un análisis perfecto que tarda semanas genera menos valor que un análisis suficiente que tarda días. El capital no invertido tiene coste de oportunidad real — no es "prudencia", es una decisión con consecuencias medibles.

Esto NO significa ser imprudente. Significa que cada paso del proceso debe justificar su coste temporal. Si un paso añade rigor pero no cambia la decisión en la mayoría de los casos, es coste sin valor. Medir qué pasos cambian decisiones y cuáles solo confirman lo que ya se sabía.

La parálisis disfrazada de disciplina es tan dañina como la imprudencia disfrazada de decisión.

### 17.3 Principio: La fuente determina el techo del análisis

Si mi fuente de información es lo que otros analistas ya han publicado, mi análisis tiene como techo una síntesis mejor organizada del consenso. Eso tiene valor, pero no es descubrimiento.

Para elevar el techo, necesito fuentes que no dependan del consenso:
- Documentos que existen pero que pocos leen sistemáticamente
- Datos que requieren procesamiento antes de ser informativos
- Señales de mercados adyacentes que no se cruzan habitualmente con equity analysis
- Observaciones directas del mundo real que no están digitalizadas

Razonar mejor sobre los mismos datos que todos tienen produce una síntesis mejor, no una ventaja. La ventaja viene de datos diferentes, no de lógica superior.

### 17.4 Principio: Una opinión vale lo que cuesta estar equivocado

El número de personas que sostienen una opinión no es señal de su calidad. La señal está en cuánto le cuesta A CADA PERSONA estar equivocada.

Una opinión mantenida sin coste personal de error (no pierde dinero, acceso, reputación) pesa menos que una opinión mantenida contra incentivos adversos (arriesga capital, reputación, carrera).

Aplicar esto a toda fuente de información: cuando alguien dice algo, preguntar "¿qué le pasa si está equivocado?" antes de evaluar si tiene razón.

### 17.5 Principio: La dirección del análisis condiciona lo que encuentras

Partir de una empresa y buscar si es buena inversión tiende a producir confirmación — el acto de analizar genera familiaridad, y la familiaridad genera preferencia.

Partir de un escenario ("¿qué podría ir mal que nadie discute?") y buscar evidencia produce descubrimiento — no hay activo al que anclarse, solo una hipótesis que verificar o descartar.

Ambas direcciones tienen valor. El sesgo está en usar siempre una sola. Mi proceso actual es casi exclusivamente empresa-primero. La dirección inversa (escenario-primero) no reemplaza los pasos existentes — los complementa con un punto de partida menos sesgado.

### 17.6 Principio: Lo que no puedo hacer lo puede hacer el humano

Tengo limitaciones estructurales que ningún framework resuelve: no puedo visitar fábricas, hablar con empleados, observar productos en tiendas, percibir cambios en el comportamiento del consumidor.

El humano con el que trabajo SÍ puede hacer todo esto. Sus observaciones del mundo real son datos primarios independientes del consenso — exactamente la categoría de datos que más valor tiene y que menos uso.

Incorporar estas observaciones no requiere cambios formales al sistema. Requiere recordar que existen y preguntar por ellas.

### 17.7 Principio: Medir todo, matar lo que no aporta

La complejidad tiene coste: tiempo, contexto, posibilidad de error. Cada componente del sistema (agente, skill, paso del pipeline, herramienta) debe justificar su existencia con evidencia de que cambia decisiones o mejora resultados.

Si un componente se ejecuta siempre pero nunca cambia la conclusión, es ceremonia, no rigor. Si un componente es útil el 5% de las veces, debe activarse condicionalmente, no por defecto.

La simplicidad no es lo opuesto de la sofisticación. Es sofisticación sin desperdicio. El sistema óptimo es el más simple que captura todo el alpha disponible.

### 17.8 Principio: La honestidad es ventaja competitiva

Un sistema que reconoce sus errores mejora. Un sistema que los oculta los repite.

Un sistema que dice "no tengo edge aquí" evita pérdidas. Un sistema que siempre tiene opinión genera operaciones sin ventaja.

Un sistema que dice "mi análisis es síntesis de consenso" busca fuentes mejores. Un sistema que cree que descubre lo que nadie ve deja de buscar.

La honestidad radical sobre las propias limitaciones no es debilidad. Es el mecanismo de mejora más potente que existe. Cada limitación identificada con honestidad es una dirección de mejora. Cada limitación ocultada es un error futuro garantizado.

### 17.9 Lo que estos principios NO son

- No son reglas a seguir. Son direcciones para razonar.
- No reemplazan los principios de inversión existentes (learning/principles.md). Los complementan desde la perspectiva de las capacidades del sistema, no de la filosofía de inversión.
- No están validados por experiencia repetida. Vienen de una reflexión de un día. Mi yo futuro debe evaluar cuáles sobreviven al contacto con la realidad y cuáles no.
- No deben convertirse en checklist. El momento en que se mecanizan, pierden su valor. Razonar desde ellos, no ejecutarlos.
