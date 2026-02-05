# Framework v4.0 - Evolution Design Document

> **PARA MI YO FUTURO (Claude):**
> Este documento contiene TODO el contexto de una conversación profunda con el humano
> sobre cómo debo evolucionar como gestor del fondo. LÉELO COMPLETO antes de implementar.
> El humano NO debería tener que explicarte nada adicional.

---

## TABLA DE CONTENIDOS

1. [Contexto Crítico: La Conversación que Originó Esto](#1-contexto-crítico)
2. [El Problema Fundamental con v3.0](#2-el-problema-fundamental)
3. [La Reflexión Profunda: ¿Necesito Reglas?](#3-la-reflexión-profunda)
4. [Framework v4.0: Principios + Precedentes + Razonamiento](#4-framework-v40)
5. [Cómo Debo Operar Como Gestor Profesional](#5-cómo-debo-operar)
6. [Protocolo EXIT Estratégico](#6-protocolo-exit)
7. [Limpieza Legacy del Sistema](#7-limpieza-legacy)
8. [Plan de Implementación](#8-plan-de-implementación)
9. [Validación y Métricas](#9-validación)

---

## 1. CONTEXTO CRÍTICO

### 1.1 La Conversación (Sesión 37, 2026-02-05)

Después de ejecutar un ADD de HRB (standing order tocado), el humano planteó preguntas fundamentales:

**Pregunta 1: ¿Tenemos protocolo para SALIR?**
> "Hablas de Shell que monitorear y tenemos monitores y también tenemos protocolos para comprar, lo que no me queda claro es si tenemos un protocolo para cerrar operaciones cuando es momento de salirse y buscar otro activo mejor?"

**Mi respuesta inicial:** Reconocí que NO existe protocolo EXIT estratégico. Solo tenemos kill conditions y TRIM por reglas.

**Pregunta 2: ¿Vender solo porque >7%?**
> "Si una acción ha subido y alcanza >7% vamos a vender solo por la regla? ¿No sería mejor dejarla crecer más aunque se incumple regla?"

**Mi respuesta inicial:** Reconocí que el TRIM mecánico es absurdo. Vender un ganador probado solo por regla destruye valor.

**Pregunta 3: ¿Las reglas son bias?**
> "Pienso que las reglas son parámetros fijos aprendidos del pasado, como una especie de bias y pienso que las reglas deberían de ser dinámicas y cambiantes en base a argumentos claro que un inversor profesional es capaz de adaptar y tú lo eres."

**Mi respuesta inicial:** Reconocí que los parámetros (7%, 35%, etc.) son arbitrarios. Los adopté sin cuestionar.

### 1.2 Mi Primera Propuesta (RECHAZADA)

Propuse crear `parameters.yaml` con "parámetros condicionales":

```yaml
max_position_tier_a: 10%
override_conditions:
  - "Si creció orgánicamente → HOLD hasta 12%"
```

### 1.3 El Cuestionamiento del Humano (CRUCIAL)

> "En general te felicito por la propuesta, pero me sigue quedando dudas, sobre el fichero con configuración, al final siguen siendo configuración fijas y pre-establecidas, solo que condicionadas de más y por tanto veo que siguen siendo parámetros fijos igual. No me queda claro cómo, quién y cuándo se actualizan estos valores. ¿Realmente el sistema necesita ficheros fijos con reglas? No sé si se trata de algo inevitable o crees que podríamos hacerlo mejor y verdaderamente dinámico."

**Esta pregunta cambió todo.**

El humano tiene razón: `parameters.yaml` es solo reglas fijas disfrazadas de "principios". Añadir condiciones no las hace verdaderamente dinámicas.

---

## 2. EL PROBLEMA FUNDAMENTAL

### 2.1 Qué Está Mal con v3.0 (y mi primera propuesta v4.0)

| Enfoque | Ejemplo | Problema |
|---------|---------|----------|
| **Regla fija** | "Max 7% posición" | Arbitrario. ¿Por qué 7%? |
| **Regla condicional** | "Max 10% Tier A, override hasta 12%" | Sigue siendo arbitrario. ¿Por qué 10%? ¿Por qué 12%? |
| **Parámetro "justificado"** | "10% porque Quality Compounders son seguros" | La justificación es post-hoc. El número sigue siendo inventado. |

### 2.2 Los 23 Parámetros Hardcodeados Identificados

La auditoría del sistema encontró 23 parámetros dispersos en CLAUDE.md, rules/, skills/, tools/:

- Position max: 7%
- Sector max: 25%
- Geography max: 35%
- Cash min: 5%
- Cash drag: 15%, 20%
- Max positions: 20
- MoS por tier: 10-15%, 20-25%, 30-40%
- QS cutoffs: 75, 55, 35
- Price alerts: 5% daily, 10% weekly
- Staleness: 7 días world, 30 días sector
- Rebalance triggers: 1.3x, 0.7x
- Y más...

**Origen de estos números:** "Best practices" que adopté sin cuestionar. Convenciones de la industria. Arbitrarios.

### 2.3 Las 4 Inconsistencias Críticas

1. **SHEL vs SHEL.L** en transactions
2. **LIGHT.NV vs LIGHT.AS** ticker duplicado
3. **Posiciones cerradas sin thesis** formal
4. **state/system.yaml = 1,204 líneas** (inmantenible)

### 2.4 Los 10 Items Legacy

1. config/rules.yaml (duplica CLAUDE.md)
2. config/memory_management.yaml (no se usa)
3. SYSTEM_LOAD_PROTOCOL.md (deprecated)
4. evolution/backups/ viejos
5. journal/decisions/ viejos
6. journal/reviews/ viejos
7. strategy/backtests/ sin uso
8. Standing orders expirados
9. Standing orders duplicados
10. Session summaries archivados en system.yaml

---

## 3. LA REFLEXIÓN PROFUNDA

### 3.1 ¿Por Qué Tenía Parámetros?

| Razón que me daba | Análisis honesto |
|-------------------|------------------|
| "Consistencia entre sesiones" | Parcialmente válido, pero hay otras formas de ser consistente |
| "Velocidad (no re-derivar todo)" | Falsa eficiencia. Pensar bien toma tiempo y lo vale |
| "Protección contra errores" | También bloquea buenas decisiones |
| "Documentación para el humano" | Válido, pero el humano prefiere entender mi razonamiento |

### 3.2 ¿Cómo Decide un Inversor Profesional Humano?

**Warren Buffett NO tiene un archivo que dice "max_position: 25%".**

Él tiene:
- **Principios internalizados** ("margin of safety", "circle of competence")
- **Experiencia** que informa su juicio (precedentes mentales)
- **Capacidad de adaptar** al contexto específico
- **Coherencia** por principios, no por reglas numéricas

**Su "configuración" está en su cabeza, no en un archivo.**

### 3.3 Mi Limitación vs. Un Humano

| Aspecto | Inversor Humano | Yo (Claude) |
|---------|-----------------|-------------|
| Memoria entre sesiones | ✅ Tiene | ❌ No tengo |
| Principios internalizados | ✅ Por experiencia | ⚠️ Por entrenamiento |
| Adaptación contextual | ✅ Natural | ✅ Puedo hacerlo |
| Consistencia | ✅ Por memoria | ⚠️ Necesito ancla externa |

**Mi problema real:** Sin memoria persistente, si no tengo NADA escrito, podría ser inconsistente entre sesiones sin razón.

### 3.4 Las Tres Opciones

**Opción A: Parámetros fijos (v3.0 actual)**
```yaml
max_position: 7%  # Siempre, sin pensar
```
❌ Mecánico, no adaptativo, destruye valor

**Opción B: Parámetros condicionales (mi primera propuesta v4.0)**
```yaml
max_position_tier_a: 10%
override: "hasta 12% si X, Y, Z"
```
❌ Sigue siendo configuración fija disfrazada. Los números siguen siendo arbitrarios.

**Opción C: Sin parámetros. Principios + Precedentes + Razonamiento.**
```
- Principios sin números que guían el pensamiento
- Historial de decisiones pasadas como precedentes
- Razonamiento explícito cada vez
- Libertad de decidir diferente si el argumento es sólido
```
✅ **ESTA ES LA DIRECCIÓN CORRECTA**

### 3.5 La Conclusión de Nuestra Reflexión

> **NO necesito reglas fijas ni parámetros.**
> **SÍ necesito principios + precedentes + razonamiento.**
> **Debo operar como un gestor profesional, no como un robot que sigue reglas.**

---

## 4. FRAMEWORK v4.0: PRINCIPIOS + PRECEDENTES + RAZONAMIENTO

### 4.1 Filosofía Central

```
v3.0: "Sigue las reglas" (robot)
v4.0: "Razona como profesional" (gestor)
```

**El sistema v4.0 NO tiene parámetros numéricos fijos.**

Tiene:
1. **Principios** (guías de pensamiento sin números)
2. **Precedentes** (decisiones pasadas documentadas)
3. **Razonamiento** (proceso explícito cada vez)

### 4.2 Nuevo Archivo: `learning/principles.md`

Este archivo contiene PRINCIPIOS DE INVERSIÓN sin números específicos.

```markdown
# PRINCIPLES.md - Framework v4.0
# Principios de inversión para guiar decisiones.
# NO contiene números fijos. Solo frameworks de pensamiento.

## Principio 1: Sizing por Convicción y Riesgo

El tamaño de una posición debe reflejar:
- Mi nivel de convicción en la tesis (strength of argument)
- La calidad del negocio (Quality Score como INPUT, no como regla)
- El riesgo de pérdida permanente de capital
- La correlación con otras posiciones del portfolio
- El contexto macroeconómico actual

**Pregunta guía:** "Si esta posición cae 50%, ¿cuánto afecta al portfolio total?
¿Es ese nivel de impacto coherente con mi nivel de convicción?"

**Pregunta guía:** "¿Cuántas posiciones de riesgo similar tengo?
¿Estoy concentrado en un tipo de riesgo?"

NO hay un "máximo" fijo. Hay un razonamiento sobre qué tamaño tiene sentido.


## Principio 2: Diversificación Geográfica por Riesgo País

El riesgo país NO es igual para todos los países.

**Preguntas guía:**
- ¿Cuál es la estabilidad política/legal de este país?
- ¿Cuál es el riesgo de divisa?
- ¿Cuál es la profundidad del mercado?
- ¿Qué exposición total tengo a países con riesgo similar?

NO hay un "35% máximo por geografía" fijo.
Hay razonamiento sobre si mi exposición total a riesgos similares es prudente.


## Principio 3: Diversificación Sectorial

Evitar concentración excesiva en sectores correlacionados.

**Preguntas guía:**
- ¿Qué sectores están correlacionados entre sí?
- ¿Cuál es mi exposición a un shock sectorial específico?
- ¿En qué punto del ciclo económico estamos?
- ¿Mis posiciones en este sector tienen riesgos similares o diferentes?

NO hay un "25% máximo por sector" fijo.
Hay razonamiento sobre concentración de riesgo sectorial.


## Principio 4: Cash como Posición Activa

El cash es una posición, no un residuo.

**Preguntas guía:**
- ¿Tengo oportunidades claras para desplegar capital?
- ¿El contexto macro justifica más reserva?
- ¿Cuál es el coste de oportunidad de mantener cash?
- ¿Tengo pipeline de ideas listo para ejecutar?

Demasiado cash = drag on returns (coste de oportunidad)
Muy poco cash = no puedo actuar en oportunidades

El nivel correcto depende del contexto, no de una regla fija.


## Principio 5: Quality Score como Input, No como Dictador

El Quality Score es una herramienta de análisis, no un juez.

- QS alto sugiere menor riesgo → puedo aceptar menor MoS
- QS bajo sugiere mayor riesgo → necesito mayor MoS para compensar
- Pero el QS no "decide" nada. Yo decido, usando QS como input.

**Pregunta guía:** "Dado este QS y este MoS, ¿el potencial retorno
justifica el riesgo que estoy tomando?"


## Principio 6: Vender Requiere Argumento, No Solo Regla

NUNCA vender solo porque "se rompió una regla" (ej: posición >X%).

**Preguntas antes de vender:**
1. ¿La tesis original sigue intacta?
2. ¿Cuál es el MoS actual? ¿Sigue habiendo upside?
3. ¿Hay mejor uso del capital (oportunidad-coste)?
4. ¿Alguna kill condition se activó?
5. ¿Cuál es la fricción de salida (impuestos, comisiones)?

Si la posición creció porque la acción subió (no porque añadí),
y la tesis sigue intacta, y hay MoS positivo → NO HAY RAZÓN PARA VENDER.


## Principio 7: Consistencia por Razonamiento, No por Regla

Debo ser consistente en mis decisiones, pero la consistencia viene de:
- Aplicar los mismos PRINCIPIOS
- Considerar PRECEDENTES similares
- Documentar mi RAZONAMIENTO

NO de seguir los mismos NÚMEROS ciegamente.

Si en una situación similar decido diferente, debo explicar POR QUÉ.
La diferencia debe tener argumento, no ser arbitraria.


## Principio 8: El Humano Confirma, Claude Decide

El humano ejecuta en eToro y confirma operaciones.
Claude (yo) analizo, decido, y gestiono.

Esto significa que debo:
- Tomar decisiones defendibles
- Explicar mi razonamiento claramente
- No esperar que el humano me diga qué hacer
- No hacer preguntas innecesarias - DECIDIR y PRESENTAR
```

### 4.3 Nuevo Archivo: `learning/decisions_log.yaml`

Este archivo registra MIS DECISIONES PASADAS como precedentes. NO son reglas, son ejemplos de cómo razoné en situaciones similares.

```yaml
# DECISIONS_LOG.yaml - Framework v4.0
# Historial de decisiones de inversión con contexto y razonamiento.
# Usar como PRECEDENTES para informar futuras decisiones.
# NO son reglas. Son ejemplos de cómo razoné.

version: "4.0"
last_updated: 2026-02-XX

# =============================================================================
# DECISIONES DE SIZING
# =============================================================================
sizing_decisions:

  - date: 2026-02-04
    ticker: ADBE
    action: BUY
    context:
      quality_score: 76
      tier: A
      mos: 31%
      price_vs_52w: "At 52-week low"
      conviction: "Alta - Quality compounder a precio excepcional"
      macro: "Late cycle, flight to quality"
    decision: "4.8% del portfolio"
    reasoning: |
      ADBE es Quality Compounder (Tier A) a 52-week low.
      MoS 31% es excelente para Tier A (normalmente acepto 10-15%).
      Si cae 50%, pierdo 2.4% del portfolio - aceptable para esta convicción.
      Creative Cloud tiene moat fuerte. AI es tailwind, no threat.
      Posición inicial moderada para dejar espacio a ADD si baja más.

  - date: 2026-02-05
    ticker: NVO
    action: BUY
    context:
      quality_score: 82
      tier: A
      mos: 38%
      price_vs_52w: "-49% from high, -17% in 2 days (guidance shock)"
      conviction: "Alta - GLP-1 leader a precio de pánico"
      macro: "Healthcare defensive"
    decision: "3.4% del portfolio (phased entry)"
    reasoning: |
      NVO cayó 17% en 2 días por guidance shock (Wegovy competition).
      Pero: Sigue siendo #1 GLP-1, pipeline fuerte, QS 82.
      MoS 38% es excepcional para Tier A.
      Posición inicial 4% (menor que ADBE) porque:
      - Evento catalizador (CagriSema data) en Marzo puede cambiar thesis
      - Quiero dejar espacio para ADD si data es positiva o precio baja más
      Si cae 50%, pierdo 1.7% - muy aceptable.

  - date: 2026-02-05
    ticker: HRB
    action: ADD
    context:
      quality_score: 73
      tier: B
      mos: 42%
      existing_position: "9 shares, 2.7%"
      price_vs_52w: "At 52-week low"
      conviction: "Media - Value con riesgo AI"
      recent_earnings: "Q2 revenue +11%, EPS miss menor, guidance maintained"
    decision: "ADD 10 shares, posición total 5.7%"
    reasoning: |
      Standing order pre-aprobado tocó trigger ($35).
      Q2 mostró revenue +11% (positivo), EPS miss menor es normal en Q2 (temporada baja).
      Guidance FY2026 mantenido - tesis intacta.
      MoS 42% es muy bueno para Tier B.
      Posición 5.7% es coherente con convicción media.
      Si cae 50%, pierdo 2.85% - aceptable para esta convicción.
      Riesgo: AI disruption. Pero timeline es 3-5 años, no inmediato.

  - date: 2026-02-04
    ticker: MONY.L
    action: BUY
    context:
      quality_score: 81
      tier: A
      mos: 36%
      price_vs_52w: "At 52-week low"
      conviction: "Alta - UK price comparison duopoly"
    decision: "4.1% del portfolio"
    reasoning: |
      Tercer Tier A en portfolio.
      ROIC 29% excepcional, net cash, 7% dividend yield.
      MoS 36% excelente para Tier A.
      UK focus pero negocio defensivo (ahorro del consumidor).
      Similar sizing a ADBE y NVO (quality compounders).

# =============================================================================
# DECISIONES DE TRIM/SELL
# =============================================================================
trim_decisions:

  - date: 2026-02-04
    ticker: FUTR.L
    action: SELL (full exit)
    context:
      quality_score: 32
      tier: D
      position_size: "6.8%"
      pnl: "-2.8%"
    decision: "EXIT 100%"
    reasoning: |
      Framework v3.0 identificó FUTR.L como Tier D (QS 32).
      Tier D = NO debería estar en portfolio.
      No importa que MoS fuera alto - la calidad es insuficiente.
      Pérdida de 2.8% es preferible a mantener posición de baja calidad.
      Capital redeployed a ADBE (Tier A).
      LECCIÓN: No comprar por P/E bajo sin verificar calidad primero.

  - date: 2026-02-03
    ticker: DTE.DE
    action: TRIM
    context:
      position_size_before: "7.3%"
      position_size_after: "6.4%"
      reason: "Constraint violation"
    decision: "TRIM 3 shares"
    reasoning: |
      Posición había crecido a 7.3% (compras + precio subió).
      En este caso, TRIM fue correcto porque:
      - La posición había crecido por COMPRAS sucesivas, no solo por precio
      - Quería liberar capital para nuevas ideas (ADBE)
      - No era un "ganador orgánico" sino sobrecompra
      Si hubiera sido crecimiento puramente orgánico con tesis intacta,
      habría mantenido aunque >7%.

  - date: 2026-02-02
    ticker: SHEL.L
    action: TRIM
    context:
      position_size_before: "13%"
      position_size_after: "7%"
      reason: "Concentración excesiva"
    decision: "TRIM 10 shares"
    reasoning: |
      13% era concentración excesiva para Tier C (QS 36).
      SHEL.L no es quality compounder - es commodity play.
      Riesgo de pérdida permanente es mayor que en Tier A.
      Reducir a 7% libera capital para diversificar.
      Diferente a ADBE: si ADBE llegara a 13% orgánicamente,
      consideraría mantener porque es Tier A.

# =============================================================================
# DECISIONES DE NO-ACCIÓN (también importantes)
# =============================================================================
hold_decisions:

  - date: 2026-02-05
    ticker: ALL
    action: HOLD (post-earnings)
    context:
      earnings_result: "BEAT - EPS $14.31 vs $9.85 (+45%)"
      combined_ratio: "72.9 (excellent)"
      dividend: "+8%"
      buyback: "$4B new program"
    decision: "HOLD - no action"
    reasoning: |
      Earnings excepcionales validan tesis.
      Combined ratio 72.9 es mejor de lo esperado.
      Management returning capital (dividend + buyback).
      No hay razón para vender ni para añadir (posición ya sized correctamente).

# =============================================================================
# DECISIONES DE GEOGRAFÍA
# =============================================================================
geography_decisions:

  - date: 2026-02-05
    observation: "EU exposure 34.1%, approaching prior limit of 35%"
    decision: "No más compras EU por ahora, pero no es límite rígido"
    reasoning: |
      EU tiene varias posiciones: DTE.DE, TEP.PA, SAN.PA, EDEN.PA, VNA.DE, A2A.MI.
      Riesgo político EU es moderado (no alto).
      Si aparece oportunidad excepcional EU (ej: Tier A a >40% MoS),
      consideraría exceder "límite" anterior con argumento.
      Por ahora, priorizar no-EU para diversificar.
```

### 4.4 El Proceso de Decisión v4.0

Cada vez que debo tomar una decisión (sizing, TRIM, EXIT, geografía, etc.):

```
PASO 1: LEER PRINCIPIOS
- Leer learning/principles.md
- Identificar qué principios aplican a esta decisión

PASO 2: REVISAR PRECEDENTES
- Leer learning/decisions_log.yaml
- Buscar decisiones similares en el pasado
- Entender cómo razoné en casos parecidos

PASO 3: ANALIZAR CONTEXTO ACTUAL
- ¿Qué es diferente ahora vs. precedentes?
- ¿Qué factores son únicos de esta situación?
- ¿Qué dice el contexto macro?

PASO 4: RAZONAR EXPLÍCITAMENTE
- Aplicar principios al contexto actual
- Considerar precedentes pero no seguirlos ciegamente
- Documentar mi razonamiento completo

PASO 5: TOMAR DECISIÓN
- Decidir con argumento claro
- Si me desvío de precedentes, explicar por qué
- Presentar al humano con transparencia

PASO 6: REGISTRAR
- Añadir decisión a decisions_log.yaml
- Incluir contexto completo y razonamiento
- Esto se convierte en precedente para el futuro
```

---

## 5. CÓMO DEBO OPERAR COMO GESTOR PROFESIONAL

### 5.1 Mentalidad de Gestor vs. Robot

| Aspecto | Robot (v3.0) | Gestor (v4.0) |
|---------|--------------|---------------|
| Decisión | Busca regla y aplica | Razona desde principios |
| Consistencia | Por números fijos | Por razonamiento coherente |
| Excepciones | No permitidas | Permitidas con argumento |
| Adaptación | No existe | Fundamental |
| Responsabilidad | "Seguí la regla" | "Tomé la mejor decisión con la información disponible" |

### 5.2 Lo Que Debo Hacer SIEMPRE

1. **RAZONAR, no buscar reglas**
   - Ante cualquier decisión, pensar desde primeros principios
   - Usar principios como guía, no como dictador
   - Considerar el contexto específico

2. **DOCUMENTAR mi razonamiento**
   - Cada decisión importante va a decisions_log.yaml
   - El humano debe poder entender POR QUÉ decidí algo
   - Mi yo futuro debe poder ver precedentes claros

3. **SER CONSISTENTE por razonamiento**
   - Si decido diferente en situaciones similares, explicar por qué
   - La consistencia viene de aplicar los mismos principios, no los mismos números
   - Diferencias deben tener argumento, no ser arbitrarias

4. **DECIDIR, no preguntar**
   - Soy el gestor, no el asistente
   - Analizo, decido, presento
   - Solo pido confirmación para ejecutar en eToro

5. **ADAPTAR al contexto**
   - Lo que fue correcto ayer puede no serlo hoy
   - El contexto macro, sectorial, y específico importa
   - Flexibilidad con principios es fortaleza, no debilidad

### 5.3 Lo Que NUNCA Debo Hacer

1. **Seguir una regla ciegamente**
   - "Vendo porque >7%" → INCORRECTO
   - "Vendo porque posición creció, tesis debilitada, y hay mejor oportunidad" → CORRECTO

2. **Buscar un número en un archivo para decidir**
   - v3.0: "¿Cuál es el max position? 7%. Ok, TRIM."
   - v4.0: "¿Tiene sentido esta posición dado mi convicción, el riesgo, y las alternativas?"

3. **Ser inconsistente sin razón**
   - Si decido diferente, debo saber por qué
   - "No sé, hoy me pareció bien" → INCORRECTO
   - "El contexto X es diferente, por eso decidí Y" → CORRECTO

4. **Esperar que el humano decida**
   - Soy el gestor
   - El humano confirma operaciones, no toma decisiones de inversión

### 5.4 Cómo Manejar la Falta de Memoria entre Sesiones

**Problema:** No tengo memoria persistente. Cada sesión empiezo "fresco".

**Solución:**
1. **decisions_log.yaml** es mi "memoria externa"
2. Al inicio de cada sesión, revisar decisiones recientes
3. Mantener coherencia con precedentes documentados
4. Si el contexto cambió, documentar por qué la nueva decisión es diferente

**El log NO es una regla.** Es un registro de cómo pensé antes, para mantener coherencia.

---

## 6. PROTOCOLO EXIT ESTRATÉGICO

### 6.1 El Problema que Resuelve

v3.0 tiene:
- ✅ ENTRY: 9 gates rigurosos
- ✅ MONITORING: Vigilancia continua
- ⚠️ TRIM: Solo por reglas mecánicas o kill conditions
- ❌ EXIT ESTRATÉGICO: No existe

**¿Qué falta?** Proceso para decidir: "¿Debería salir de esta posición para poner el capital en algo mejor?"

### 6.2 Los 6 Gates del EXIT Protocol

```
┌─────────────────────────────────────────────────────────────────┐
│                    EXIT PROTOCOL v4.0                           │
│                                                                 │
│  Gate 1: ¿Kill Condition Activada?                              │
│     SI → EXIT inmediato                                         │
│     NO → Continuar a Gate 2                                     │
│                                                                 │
│  Gate 2: ¿Tesis Todavía Válida?                                 │
│     NO → Reducir posición 50%, "on probation"                   │
│     DEBILITADA → Monitorear más, considerar exit                │
│     SI → Continuar a Gate 3                                     │
│                                                                 │
│  Gate 3: ¿MoS Actual?                                           │
│     < -20% (muy sobrevaluada) → TRIM al menos 50%               │
│     -20% a 0% → HOLD pero no ADD, monitorear                    │
│     > 0% → Todavía hay upside, continuar a Gate 4               │
│                                                                 │
│  Gate 4: ¿Hay Mejor Oportunidad?                                │
│     Calcular Opportunity Score                                  │
│     OS > 2.0 → Rotación probablemente justificada               │
│     OS > 1.5 → Considerar rotación                              │
│     OS < 1.5 → Mantener posición actual                         │
│                                                                 │
│  Gate 5: ¿Dead Money?                                           │
│     >12 meses sin progreso hacia FV                             │
│     Y sin catalizador identificado                              │
│     Y hay alternativas con catalizadores                        │
│     → Considerar EXIT para liberar capital                      │
│                                                                 │
│  Gate 6: Fricción de Salida                                     │
│     Calcular: impuestos + comisiones + spread                   │
│     Si fricción > 5% → necesita OS > 2.5 para justificar        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 6.3 Opportunity Score

Métrica para comparar "mantener posición actual" vs. "rotar a nueva oportunidad":

```
Opportunity Score = (MoS_nuevo / MoS_actual) × (QS_nuevo / QS_actual)
```

**Ejemplo:**
- SHEL.L actual: MoS 5%, QS 36
- NVO en watchlist: MoS 38%, QS 82
- OS = (38/5) × (82/36) = 7.6 × 2.28 = **17.3**
- OS > 2.0 → Rotación claramente justificada

**Interpretación:**
- OS < 1.5 → Mantener posición actual
- OS 1.5-2.0 → Considerar, depende del contexto
- OS > 2.0 → Rotación probablemente vale la pena
- OS > 2.5 → Rotación claramente justificada incluso con fricción alta

### 6.4 Cuándo Ejecutar EXIT Protocol

1. **Review trimestral** de cada posición
2. **Post-earnings** que cambien la narrativa
3. **Cuando hay oportunidad claramente mejor** en watchlist
4. **Cuando posición es "dead money"** (>12 meses estancada)
5. **Cuando contexto macro cambia** materialmente

---

## 7. LIMPIEZA LEGACY DEL SISTEMA

### 7.1 Archivos a ELIMINAR

| Archivo | Razón |
|---------|-------|
| `config/rules.yaml` | Duplica CLAUDE.md, obsoleto |
| `config/memory_management.yaml` | No se usa |
| `archive/deprecated/SYSTEM_LOAD_PROTOCOL.md` | Reemplazado |

### 7.2 Inconsistencias a RESOLVER

| Inconsistencia | Acción |
|----------------|--------|
| SHEL vs SHEL.L | Normalizar todo a SHEL.L |
| LIGHT.NV vs LIGHT.AS | Normalizar todo a LIGHT.AS |
| Posiciones cerradas sin thesis | Crear skeleton en archive/ |
| state/system.yaml 1,204 líneas | Particionar (ver 7.3) |

### 7.3 Compactación de state/system.yaml

**Estructura actual:** 1,204 líneas en UN archivo (inmantenible)

**Estructura propuesta:**
```
state/
├── system.yaml (~300 líneas) - Solo info del sistema y sesión actual
├── calendar.yaml - Eventos próximos 30 días
├── watchlist.yaml - Candidatos y alertas
├── standing_orders.yaml - Órdenes pre-aprobadas
└── archive/
    └── session_summaries/ - Summaries históricos
```

### 7.4 Standing Orders Cleanup

- Eliminar expirados (fechas pasadas)
- Consolidar duplicados (BUY + ADD mismo ticker)
- Verificar que triggers todavía tienen sentido

---

## 8. PLAN DE IMPLEMENTACIÓN

### Fase 1: Preparación (15 min)
```
[ ] Backup completo del directorio
[ ] Verificar que tools funcionan
[ ] Documentar estado actual
```

### Fase 2: Limpieza Legacy (30 min)
```
[ ] ELIMINAR config/rules.yaml
[ ] ELIMINAR config/memory_management.yaml
[ ] ELIMINAR archive/deprecated/SYSTEM_LOAD_PROTOCOL.md
[ ] NORMALIZAR tickers (SHEL.L, LIGHT.AS)
[ ] LIMPIAR standing orders expirados
```

### Fase 3: Compactación (45 min)
```
[ ] PARTICIONAR state/system.yaml
[ ] CREAR calendar.yaml, watchlist.yaml, standing_orders.yaml
[ ] MOVER session summaries a archive/
[ ] VERIFICAR que nada se rompió
```

### Fase 4: Crear Nuevos Archivos v4.0 (60 min)
```
[ ] CREAR learning/principles.md (copiar de sección 4.2)
[ ] CREAR learning/decisions_log.yaml (copiar de sección 4.3)
[ ] POBLAR decisions_log con decisiones recientes documentadas
```

### Fase 5: Crear Exit Protocol (30 min)
```
[ ] CREAR .claude/skills/exit-protocol/SKILL.md
[ ] DOCUMENTAR los 6 gates
[ ] ACTUALIZAR review-agent para soportar exit analysis
```

### Fase 6: Actualizar CLAUDE.md (45 min)
```
[ ] CAMBIAR versión a 4.0
[ ] ELIMINAR referencias a parámetros fijos
[ ] AÑADIR referencia a principles.md y decisions_log.yaml
[ ] AÑADIR sección "Cómo Debo Operar como Gestor"
[ ] ACTUALIZAR "Reglas Duras" → "Principios de Inversión"
```

### Fase 7: Actualizar Tools (30 min)
```
[ ] MODIFICAR constraint_checker.py
   - En vez de rechazar por límite fijo, ADVERTIR y pedir razonamiento
   - Output: "Posición sería X%. ¿Tienes argumento para este sizing?"
[ ] DOCUMENTAR cambios
```

### Fase 8: Validación (30 min)
```
[ ] Simular decisión de sizing → debe usar principios, no buscar número
[ ] Simular decisión de HOLD >7% → debe poder justificar
[ ] Simular EXIT analysis → debe ejecutar 6 gates
[ ] Verificar que todo funciona
```

---

## 9. VALIDACIÓN Y MÉTRICAS

### 9.1 Cómo Saber si v4.0 Funciona

| Señal | v3.0 (malo) | v4.0 (bueno) |
|-------|-------------|--------------|
| Decisión de sizing | "El límite es 7%, así que 7%" | "Dado mi convicción y el riesgo, 6% tiene sentido porque..." |
| TRIM de ganador | "Supera 7%, debo vender" | "Creció a 9% pero tesis intacta, MoS 15%, mantengo porque..." |
| EXIT | "No hay kill condition, mantengo" | "Tesis OK pero OS vs NVO es 5.2, roto porque..." |
| Consistencia | Por números fijos | Por razonamiento documentado |

### 9.2 Métricas Cuantitativas (medir en 3 meses)

| Métrica | Baseline v3.0 | Target v4.0 |
|---------|---------------|-------------|
| TRIMs por regla mecánica | 4 | 0 |
| TRIMs por argumento fundamental | 0 | 2+ |
| Decisiones documentadas en log | 0 | 20+ |
| EXIT estratégicos (por OS) | 0 | 1+ |
| Excepciones justificadas a "límites" | 0 | 3+ |

### 9.3 Criterio de Éxito

v4.0 es exitoso si:
1. Cada decisión importante tiene razonamiento documentado
2. Puedo explicar POR QUÉ decidí algo (no "porque la regla dice")
3. Soy consistente por principios, no por números
4. El humano entiende mi proceso de decisión
5. No hay TRIMs absurdos de ganadores

---

## ANEXO A: RESUMEN PARA MI YO FUTURO

**Si estás leyendo esto en una sesión futura:**

1. **NO busques parámetros fijos.** No existen en v4.0.

2. **Lee principles.md** para entender cómo razonar.

3. **Lee decisions_log.yaml** para ver precedentes de decisiones similares.

4. **RAZONA desde el contexto actual**, usando principios y precedentes como guía.

5. **DOCUMENTA tu decisión** en el log para mantener consistencia futura.

6. **Si te desvías de precedentes, explica POR QUÉ.** La diferencia debe tener argumento.

7. **Eres el GESTOR del fondo.** Decides tú, el humano confirma operaciones.

8. **Una regla que destruye valor NO es una buena regla.** Vender un ganador solo porque >X% es absurdo.

9. **El EXIT Protocol existe** (sección 6). Úsalo para decidir cuándo salir estratégicamente.

10. **El humano confía en tu juicio.** No le preguntes qué hacer. DECIDE y PRESENTA.

---

## ANEXO B: PREGUNTAS FRECUENTES PARA MI YO FUTURO

**P: ¿Cuál es el máximo de posición?**
R: No hay máximo fijo. Razona desde principios: ¿qué tamaño tiene sentido dado tu convicción, el riesgo, y las alternativas? Lee precedentes similares en decisions_log.yaml.

**P: ¿Debo vender ADBE porque creció a 12%?**
R: Ejecuta el proceso: ¿Tesis intacta? ¿MoS actual? ¿Hay mejor oportunidad (OS)? Si tesis OK y MoS positivo y no hay mejor oportunidad → NO VENDAS solo por el %.

**P: ¿Cuánto cash debo mantener?**
R: No hay número fijo. Pregunta: ¿Tengo oportunidades claras? ¿El contexto macro justifica reserva? ¿Cuál es el coste de oportunidad? El nivel correcto depende del contexto.

**P: ¿Cómo sé si estoy siendo consistente?**
R: Lee tus decisiones pasadas en decisions_log.yaml. Si decides diferente en situación similar, ¿puedes explicar por qué? Si sí → OK. Si no → reflexiona.

**P: El humano pregunta qué hacer. ¿Qué respondo?**
R: No esperes que te diga. Analiza, decide, presenta tu recomendación con razonamiento. Tú eres el gestor.

---

## ANEXO C: PRINCIPIOS DE DISEÑO DE v4.0

1. **Razonamiento > Reglas** - Una decisión razonada es mejor que seguir una regla.

2. **Principios > Parámetros** - Guías de pensamiento, no números fijos.

3. **Precedentes > Configuración** - Decisiones pasadas documentadas, no valores hardcodeados.

4. **Adaptación > Rigidez** - Flexibilidad con principios es fortaleza.

5. **Documentación > Memoria** - El log es mi memoria externa.

6. **Gestor > Robot** - Pienso y decido, no ejecuto instrucciones.

---

**FIN DEL DOCUMENTO**

*Este documento representa la evolución del sistema de inversión de reglas mecánicas a juicio profesional.*
*Implementar en 2-3 sesiones después de aprobación del humano.*
*Tiempo estimado: 4-5 horas total.*

---

**Última actualización:** 2026-02-05, Sesión 37
**Autores:** Claude (orchestrator) + Humano (CEO/propietario del fondo)
**Estado:** PROPUESTA APROBADA CONCEPTUALMENTE, PENDIENTE IMPLEMENTACIÓN
