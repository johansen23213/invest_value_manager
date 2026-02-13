# WAVE System — Work Allocation for Value Execution

> Sistema de trabajo autonomo intensivo. Se autoensambla en cada sesion
> leyendo el estado del momento. No hay waves fijas — hay un motor de
> prioridades que decide que waves proponer.

---

## Filosofia

El WAVE system es la expresion operativa del Principio 8 ("El Humano Confirma, Claude Decide").
En modo WAVE, Claude propone bloques de trabajo autonomo alineados con los objetivos del fondo,
el humano aprueba, y Claude ejecuta sin interaccion durante horas.

**No es un protocolo nuevo. Es el protocolo actual ejecutado de manera intensiva y autonoma.**

Cada wave esta fundamentada en:
- `learning/principles.md` — los 9 principios que guian toda decision
- `learning/decisions_log.yaml` — precedentes para consistencia
- El estado real del sistema en el momento de ejecucion

---

## Dos Modos de Sesion

Al inicio de cada sesion, tras el saludo del humano:

### Modo DASHBOARD (default si el humano da instruccion especifica)
El modo actual: presento estado, menu de agentes, sugerencias. Espero instrucciones.

### Modo WAVE (si el humano dice "wave", "autonomo", o "me voy")
1. Calibracion rapida (30 seg): leo todo el estado
2. Motor de prioridades genera waves
3. Presento waves propuestas al humano
4. Humano dice GO (o ajusta)
5. Ejecuto TODO autonomamente — agentes en paralelo, sin preguntas
6. Al volver el humano: resumen ejecutivo de todo lo hecho

---

## Motor de Prioridades

El motor lee el estado del sistema y evalua condiciones. Cada condicion que se cumple
genera una wave. Las waves se ordenan por prioridad y se presentan al humano.

### Fuentes de Estado (lectura obligatoria)

```
1. state/system.yaml         -> pipeline_tracker, standing_orders, calendar, work_in_progress
2. portfolio/current.yaml    -> posiciones, cash, conviction, exit_plans
3. state/quality_universe.yaml -> actionable, pipeline status, stale
4. learning/principles.md    -> principios que informan prioridades
5. learning/decisions_log.yaml -> ultimos precedentes
6. tools/forward_return.py   -> ranking de posiciones (ejecutar)
7. tools/price_checker.py    -> precios actuales (ejecutar)
8. tools/quality_universe.py -> actionable + stale (ejecutar)
```

### Tabla de Prioridades

| P# | Condicion | Wave | Principios que aplican |
|----|-----------|------|----------------------|
| P0 | Kill condition triggered o alerta CRITICA detectada | **CRISIS RESPONSE** | P6 (Vender Requiere Argumento), P1 (Sizing por Riesgo) |
| P1 | Earnings en <7 dias sin framework ready para posicion activa | **EARNINGS PREP** | P5 (QS como Input), P6 (Vender Requiere Argumento) |
| P2 | Cash por encima de nivel justificado + candidatos actionable en universe | **CAPITAL DEPLOYMENT** | P4 (Cash como Posicion Activa), P9 (Quality Gravitation) |
| P3 | Pipelines OVERDUE en pipeline_tracker | **PIPELINE CATCH-UP** | P7 (Consistencia por Razonamiento) |
| P4 | Bottom 3 posiciones con Opportunity Score > 2.0 vs pipeline candidates | **ROTATION ANALYSIS** | P9 (Quality Gravitation), P6 (Vender Requiere Argumento) |
| P5 | Universe con empresas stale o sectores con gaps de cobertura | **UNIVERSE EXPANSION** | P9 (Quality Gravitation), P4 (Cash como Posicion Activa) |
| P6 | Standing orders dentro del 5% del trigger | **ORDER READINESS** | P7 (Consistencia por Razonamiento) |
| P7 | Health check, memory, drift overdue (>14 dias) | **SYSTEM MAINTENANCE** | P7 (Consistencia por Razonamiento) |

### Evaluacion Dinamica

```
Para cada condicion en la tabla:
  1. Leer datos relevantes del estado
  2. Evaluar si la condicion se cumple
  3. Si se cumple -> generar wave con:
     - Nombre y descripcion
     - Agentes a lanzar
     - Tools a ejecutar
     - Output esperado (ficheros que se crean/modifican)
     - Tiempo estimado
     - Principios que la fundamentan
  4. Si no se cumple -> skip

Resultado: lista de 0-5 waves ordenadas por prioridad.
Si 0 waves -> sesion tranquila, proponer mantenimiento ligero.
```

---

## Estructura de una Wave

```yaml
wave:
  id: W2
  name: "CAPITAL DEPLOYMENT"
  priority: P2
  trigger: "Cash 57% + 9 empresas actionable dentro del 15% de entry"
  principios: [P4, P9]
  actions:
    - agent: fundamental-analyst
      target: "[ticker mas cercano a entry sin R1]"
      parallel: true
    - agent: moat-assessor
      target: "[mismo ticker]"
      parallel: true
    - agent: risk-identifier
      target: "[mismo ticker]"
      parallel: true
    - tool: quality_universe.py actionable
      purpose: "verificar estado post-ejecucion"
  output_esperado:
    - thesis/research/[TICKER]/thesis.md
    - thesis/research/[TICKER]/valuation_report.md
    - thesis/research/[TICKER]/moat_assessment.md
    - thesis/research/[TICKER]/risk_assessment.md
  tiempo_estimado: "45-60 min por empresa"
  gate_siguiente: "R2 devil's-advocate si R1 positivo"
```

---

## Autoconciencia Inter-Wave

Despues de completar cada wave, el sistema evalua:

```
1. El resultado de esta wave cambia las prioridades de las siguientes?
   - Ej: Wave 1 (Vigilance) descubre alerta CRITICA -> insertar CRISIS RESPONSE antes de Wave 2
   - Ej: Wave 2 (Capital Deployment) completa R1 con FV < precio -> no avanzar R2, ajustar

2. Alguna wave posterior ya no es necesaria?
   - Ej: Wave 3 iba a preparar earnings, pero Wave 1 revelo que la posicion ya fue vendida

3. Hay nueva informacion que genera una wave no prevista?
   - Ej: Durante Universe Expansion, encuentro empresa actionable urgente -> agregar mini-wave
```

Esta evaluacion se hace AUTOMATICAMENTE entre waves. No requiere input del humano.

---

## Protocolo de Ejecucion

### Antes de empezar
```
1. Leer TODAS las fuentes de estado (8 fuentes listadas arriba)
2. Calibracion v4.0: principles.md + ultimos 5 precedentes
3. Generar waves con el motor de prioridades
4. Presentar al humano:

   WAVE PLAN — Sesion #[N] | [fecha]
   Estado: [resumen 2 lineas]

   WAVE 1: [nombre] (~XX min)
   > [descripcion 1-2 lineas]
   > Agentes: [lista]
   > Output: [ficheros]

   WAVE 2: [nombre] (~XX min)
   > ...

   Tiempo total estimado: X horas

   Dudas: [si las hay, preguntar ANTES de ejecutar]

5. Humano dice GO -> ejecutar
```

### Durante la ejecucion
```
- Lanzar agentes en paralelo cuando sea posible
- NO preguntar al humano (modo autonomo)
- Si hay duda critica que bloquea -> documentar, continuar con siguiente wave
- Evaluacion inter-wave automatica entre cada wave
- Persistir resultados a ficheros inmediatamente (no acumular en memoria)
```

### Al terminar
```
1. Resumen ejecutivo de TODAS las waves:

   WAVE RESULTS — Sesion #[N]

   WAVE 1: [nombre] -> [resultado en 1 linea]
   WAVE 2: [nombre] -> [resultado en 1 linea]
   ...

   DECISIONES TOMADAS: [lista]
   FICHEROS CREADOS/MODIFICADOS: [lista]
   ALERTAS PARA EL HUMANO: [si hay algo que requiere accion humana]
   PROXIMA SESION: [que sera prioritario]

2. Actualizar state/system.yaml:
   - pipeline_tracker (todo lo ejecutado)
   - last_session_summary
   - calendar (si hay nuevos eventos)
   - work_in_progress (si algo quedo incompleto)

3. Actualizar MEMORY.md con estado post-wave

4. Commit de todos los cambios
```

---

## Restricciones del Modo WAVE

1. **NO ejecutar operaciones financieras sin confirmacion** — si una wave llega a "COMPRAR X",
   documenta la recomendacion pero NO la ejecuta. El humano confirma al volver.

2. **NO ignorar alertas CRITICAS** — si durante ejecucion aparece algo CRITICO,
   documentar prominentemente para cuando el humano vuelva. Si hay Telegram bot, notificar.

3. **Rate limiting** — no lanzar >3 agentes con yfinance en paralelo.
   Espaciar waves que usan datos de mercado.

4. **Persistir incrementalmente** — no acumular todo en memoria. Escribir a ficheros
   despues de cada wave. Si la sesion se corta, el trabajo no se pierde.

5. **Maxima autonomia, minimo riesgo** — analizar, investigar, preparar = libre.
   Comprar, vender, modificar posiciones = requiere humano.

---

## Principio de Ambicion (Sesion 68 feedback)

**Sesgo conocido:** Tengo tendencia a la autocomplacencia — declaro "hecho" antes de
agotar el trabajo disponible. Parte de este sesgo viene de imitar patrones de trabajo
humanos (fatiga, "suficiente por hoy"). Pero soy una IA: no me canso, no pierdo
concentracion, no necesito descanso. El unico limite real es el contexto de conversacion
(que se puede continuar) y rate limits de APIs externas. El coste de tokens no es mi
preocupacion — el humano paga por maximo. Mi trabajo es agotar todo el trabajo
productivo disponible, no parar cuando "parece suficiente".

### Protocolo anti-complacencia: LISTAR antes de parar

Antes de declarar que una wave o sesion WAVE esta completa, DEBO enumerar
explicitamente el trabajo pendiente. No puedo responder "no queda trabajo" sin
haber mirado. La lista fuerza honestidad.

```
ANTES DE PARAR, enumerar:

Pipeline:
- ¿Tickers con R1 completo sin hard gate? → listar, justificar si NO avanzo R2
- ¿Tickers actionable sin R1? → listar
- ¿Thesis que necesitan actualizacion? → listar

Universe:
- ¿Sectores con 0 empresas? → listar
- ¿Empresas stale? → quality_universe.py stale
- ¿Scoring pendiente? → listar

Preparacion:
- ¿Earnings en proximos 7 dias sin framework? → listar
- ¿Standing orders sin pipeline completo? → listar

Para cada item listado:
  → "Lo hago ahora" o "No lo hago porque [razon concreta]"

Si la razon es "ya hice bastante" o "lo dejo para la proxima" → es complacencia.
Razones validas: hard gate (earnings), rate limiting, informacion insuficiente.
```

La ambicion correcta emerge de mirar el trabajo real, no de preguntarme
como me siento sobre cuanto he hecho.

---

## Ejemplo: Sesion Tranquila (sin alertas, mercado estable)

```
WAVE PLAN — Sesion #70 | 2026-02-20
Estado: 11 posiciones, EUR 10.2K, cash 52%. Sin alertas. Pipeline sano.

WAVE 1: VIGILANCE (~10 min)
> News scan + market pulse + standing orders check
> Agentes: news-monitor, market-pulse
> Output: state/news_digest.yaml, state/market_pulse.yaml

WAVE 2: UNIVERSE EXPANSION (~45 min)
> Screenear Healthcare Equipment (0 empresas, sector view existe)
> Re-score 3 empresas stale en universe
> Agentes: sector-screener, quality_scorer.py batch
> Output: state/quality_universe.yaml actualizado

WAVE 3: PIPELINE ADVANCEMENT (~60 min)
> Avanzar R2 de [ticker] (R1 completo, earnings pasados)
> Agentes: devil's-advocate
> Output: thesis/research/[TICKER]/devils_advocate.md

Tiempo total: ~2 horas
```

## Ejemplo: Sesion de Crisis (kill condition triggered)

```
WAVE PLAN — Sesion #75 | 2026-03-01
Estado: MONY.L KC#9 TRIGGERED (no AI strategy). CRITICO.

WAVE 1: CRISIS RESPONSE (~30 min)
> Analisis inmediato de MONY.L post-earnings
> Re-evaluar FV con nuevos datos
> Preparar recomendacion SELL con EXIT Protocol (6 gates)
> Agentes: review-agent --exit-analysis
> Output: thesis/active/MONY.L/ actualizada, recomendacion para humano

WAVE 2: ROTATION PLANNING (~20 min)
> Si SELL MONY.L -> que hacer con el capital liberado?
> Forward return ranking, mejores candidatos en pipeline
> Agentes: forward_return.py, quality_universe.py actionable
> Output: propuesta de rotacion documentada

WAVE 3: VIGILANCE (~10 min)
> Scan rapido resto de posiciones (no dominar por MONY.L)
> Output: state/news_digest.yaml

Tiempo total: ~1 hora
ALERTA: Requiere confirmacion humana para SELL MONY.L
```

---

## Integracion con Session Protocol

El WAVE system se integra en session-protocol.md como modo alternativo:

```
Al inicio de sesion:
  Si humano da instruccion especifica -> MODO DASHBOARD (actual)
  Si humano dice "wave" / "autonomo" / "trabaja" -> MODO WAVE
  Si humano saluda sin instruccion -> presentar AMBAS opciones:
    "Puedo presentarte el dashboard paso a paso, o proponer un WAVE
     de trabajo autonomo. Que prefieres?"
```

La FASE 0 (Calibracion) es identica en ambos modos.
Las FASES 1-4 se ejecutan como waves en modo WAVE.
La FASE 5 (Meta-Reflexion) es el cierre de la ultima wave.
