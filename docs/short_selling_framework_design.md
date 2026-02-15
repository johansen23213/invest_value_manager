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

1. **"¿Por qué yo decido los fondos? ¿Por qué es fijo?"** → No hardcodear parámetros. Los fondos quality deben EMERGER del grafo, no ser elegidos subjetivamente. Esto aplica a TODO el sistema short: nada fijo, todo razonado desde principios.

2. **"Estás pasando por alto que eres una IA"** → Yo no tengo limitaciones de experiencia, carga analítica ni psicología. Puedo analizar 50 casos de shorts históricos en una hora. Puedo mantener 10 longs + 3 shorts sin cansarme. No tengo sesgos emocionales. Las únicas limitaciones reales son mecánicas del mercado (gap risk, instrumentos disponibles), no mías.

3. **"Basado en principios y no reglas fijas"** → Todo el framework debe razonarse desde `learning/principles.md`. Sin thresholds fijos, sin ratios hardcodeados, sin reglas mecánicas.

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

**Concepto:** Extensión simétrica del sistema long-only a long-biased con shorts selectivos oportunistas. No hedge fund, no market neutral. Shorts como herramienta táctica atada a catalizadores, que genera alpha adicional y mejora métricas del portfolio (Sharpe, drawdown).

**Fundamento:** Ya producimos thesis short (AVOIDs, DAs) sin monetizarlas. Las caídas son rápidas (alto alpha/tiempo). Como IA, no tenemos las 3 limitaciones principales del shorting humano (psicología, capacidad, experiencia).

**Instrumento:** CFD short en eToro. Sin puts disponibles en EU. Coste ~7-8% anual, manejable para posiciones de 1-3 meses.

**Principios:** Los 9 existentes se extienden naturalmente. 3 nuevos: Catalizador Obligatorio (P10), Asimetría Consciente (P11), Short Sirve al Portfolio (P12).

**Impacto en sistema:** 6 tools a modificar, 4 tools nuevos, 12+ agents a extender, 3 skills nuevos, 6+ state files a extender, 4 rules a actualizar. Es un proyecto significativo pero la mayoría son extensiones, no reescrituras.

**Guardrails:** No shortear sin fragilidad + catalizador. No apalancamiento alto. No shorts indefinidos. No copiar shorts famosos. No dejar que shorts dominen la atención.

**Primera operación:** Sizing mínimo (€100-200), 1 posición, documentar todo como precedente. Escalar solo con precedentes propios.
