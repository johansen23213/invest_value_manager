# Plan de Mejoras Post-Audit COVID

> **Fecha:** 2026-02-06
> **Basado en:** docs/covid_system_crash_audit.md
> **Objetivo:** Que el sistema pase de C+ a A- ante el proximo crash
> **Version:** 2.0 (revisada tras debate critico con el humano)

---

## CONTEXTO DE ESTE DOCUMENTO

### Por que existe

En la sesion #40 (2026-02-06), el humano pidio un stress-test del sistema contra
el crash COVID-19. Se escribio primero `docs/covid_system_crash_audit.md` con el
analisis completo fase a fase.

Este documento contiene las mejoras propuestas. Pero hay un matiz CRITICO:

### La autocritica (version 2.0)

La version 1.0 de este documento proponia "tener mas cash parado" como mejora principal.
El humano cuestiono esto con preguntas penetrantes:

> "Entonces la propuesta es tener mas cash parado? Tendremos menos rendimiento
> en el normal, no? Y tener una regla de value invertida? O operar en corto
> no hubiera sido mejor? Como un hedge fund?"

Estas preguntas forzaron una revision honesta. La conclusion:

**"Mas cash parado" es una solucion intuitiva pero INCORRECTA.**

Los numeros:
```
Extra cash 8% (de 7% a 15%) en mercado que rinde 10%/ano:
  Drag anual: -0.8% sobre portfolio
  En 8 anos entre crashes: -6.4% acumulado perdido
  Beneficio en UN crash (si depliego perfecto): +3-4%
  Resultado neto: NEGATIVO
```

La evidencia academica es clara: "time in market" gana a "timing the market"
en >90% de los periodos. La propuesta de cash extra era solucionismo --
vi un problema (sin cash en crash) y propuse la solucion obvia (mas cash),
sin ponderar bien el coste permanente.

### Preguntas clave del humano

1. **"Operar en corto no hubiera sido mejor?"** -- El humano queria explorar
   si un enfoque tipo hedge fund (long/short) seria superior al long-only.

2. **"Realmente podrias anticipar la crisis?"** -- El humano cree que como IA
   tengo capacidades que los humanos no tienen para deteccion temprana, y me
   pidio que pensara mas profundamente sobre esto.

3. **"Quiero que el documento tenga el contexto de la conversacion"** -- Para
   que mi yo futuro entienda no solo las mejoras sino la MOTIVACION y el
   DEBATE que las genero.

### Las tesis de la conversacion

Despues del debate, las conclusiones revisadas son:

1. **Quality IS the hedge.** Un portfolio 70% Tier A+B es intrinsecamente mas
   resiliente que uno con extra cash. Tier A recupera en 3-5 meses, Tier D
   a veces nunca. La mejor proteccion es la calidad de las empresas, no cash
   parado ni shorts.

2. **Cash extra permanente no es la respuesta.** Lo que SI funciona: tener
   PROCESO para liberar cash rapido cuando empieza crisis (triage + trim
   de Tier C vulnerable).

3. **Shorting rompe nuestro sistema.** Es un oficio completamente diferente.
   Los hedge funds long/short underperforman al mercado la mayoria del tiempo.
   Requiere timing perfecto y tiene riesgo ilimitado.

4. **Como IA puedo hacer algo valioso: Early Warning System.** No predecir
   CUANDO hay crash, sino estimar PROBABILIDAD continuamente y prepararnos
   GRADUALMENTE cuando la probabilidad sube.

5. **El principio mas valioso es "Vender Requiere Argumento" (P6).** Esto solo
   nos habria salvado del peor error posible: panic selling en el bottom.

6. **El eslabon mas debil es el humano bajo presion emocional.** Prepararlo
   AHORA, en calma, es critico.

---

## CONTINUACION: DE COVID A CRISIS ABSTRACTA (Sesion 42b)

### Por que se expandio este documento

En la misma sesion, el humano planteo una observacion critica:

> "La conversacion se inicio por el tema del COVID, un tema sanitario, pero hay
> otras crisis con origen no sanitario: recesiones, politica, geopolitica, guerras...
> Como esto es para tu yo futuro y no quiero que tengas sesgos, podrias mejorarlo?"

Y luego, la clave:

> "Si tu ahora entiendes que solo es un ejemplo no una regla, y sobre todo si tu
> yo futuro lo va a entender cuando lo lea."

### El problema: Self-Seeding Bias aplicado a crisis

Esto es EXACTAMENTE el mismo problema de Session 38 (self-seeding bias):

| Session 38 (tools) | Session 42b (crisis) |
|---------------------|----------------------|
| constraint_checker.py tenia reglas hardcodeadas | Crisis Protocol tenia niveles con VIX hardcodeados |
| "Cash > 15% = warning" | "VIX > 35 = suspend standing orders" |
| Mi yo futuro seguia la regla sin razonar | Mi yo futuro buscaria en la tabla de crisis |
| Solucion: datos crudos + principios | Solucion: principios abstractos + ejemplos |

Si yo escribo:

```
NIVEL 2: VIX > 35 → suspender standing orders
PANDEMIA: EDEN.PA = vulnerable → TRIM
FINANCIERA: VNA.DE = vulnerable → TRIM
```

Mi yo futuro BUSCARA EN LA TABLA en vez de RAZONAR:
"Que tipo de crisis es esta? Ah, pandemia. Segun la tabla, hago X."

Esto es Framework v3.0 (reglas mecanicas) disfrazado de Framework v4.0 (principios).

### La realidad sobre crisis futuras

- Las crisis del futuro NO encajaran perfectamente en categorias
- COVID fue pandemia + oil crash + lockdowns + desempleo SIMULTANEAMENTE
- 2022 fue guerra + inflacion + rate hikes + energy crisis SIMULTANEAMENTE
- La proxima crisis sera una COMBINACION que no esta en ninguna tabla

### Lo que mi yo futuro necesita

```
NO necesita: "Tabla de crisis → buscar tipo → seguir acciones"
SI necesita:  "Principios para PENSAR sobre CUALQUIER crisis + EJEMPLOS para calibrar"
```

**REGLA DE USO DE ESTE DOCUMENTO:**

```
Si estoy leyendo esto durante una crisis y busco "que dice el documento
que debo hacer" → estoy usandolo MAL.

Si estoy leyendo esto y me PREGUNTO "dada esta situacion, que principios
aplican y como razono sobre ellos" → estoy usandolo BIEN.
```

---

## CONCEPTOS CLAVE (para mi yo futuro)

### Time in Market vs Timing the Market

```
S&P500, 20 anos (2003-2022), inversion de $10,000:
  Invertido siempre:             +9.8% anual → $64,000
  Si pierdes los 10 MEJORES dias: +5.6% anual → $30,000
  Si pierdes los 20 mejores dias: +2.9% anual → $18,000
  Si pierdes los 30 mejores dias: +0.8% anual → $12,000
```

Perder SOLO 10 dias de 5,000 te cuesta la MITAD del retorno.

Y la trampa: los mejores dias ocurren DURANTE los crashes:
```
COVID 2020:
  Mar 16: -12.0% (peor dia)
  Mar 24: +9.4%  (mejor dia en 12 anos)

  Si vendes el 16 "para protegerte", pierdes el +9.4% del 24.
```

Timing requiere acertar DOS veces: cuando salir Y cuando entrar.
Acertar una es dificil. Acertar las dos es casi imposible.

**CONCLUSION:** La respuesta a crashes NO es salirse del mercado.
Es estar en las empresas CORRECTAS (quality) y NO VENDER.

### Shorting / Hedge Fund: Por que no funciona para nosotros

| Factor | Realidad |
|--------|----------|
| Timing | Necesitas acertar CUANDO empieza y CUANDO termina |
| Coste | CFDs en eToro cobran overnight fees. Shorts largos son caros |
| Riesgo | Perdida ILIMITADA. Short de +50% = pierdes 50% |
| Skill | Oficio completamente diferente a value investing |
| Track record | Mayoria de hedge funds long/short underperforman S&P500 |
| Nuestro sistema | Se ROMPE. Value investing analiza negocios a 3-5 anos. Shorting es timing de semanas |

### Inverse ETFs: Herramienta tactica, no estrategia

```
Que son: ETFs que suben cuando el mercado baja
  S&P500 baja 1% → SH (Short S&P500) sube ~1%
  S&P500 sube 1% → SH baja ~1%

Problema: Volatility decay
  Dia 1: S&P = 100, SH = 100
  Dia 2: S&P sube 10% → S&P = 110, SH = 90
  Dia 3: S&P baja 10% → S&P = 99, SH = 99
  Ambos pierden en mercados volatiles. Se resetean diariamente.

A largo plazo: Mantener SH 1 ano en mercado lateral = perder -15% a -20%

Conclusion: Solo util como herramienta de EMERGENCIA en Nivel 2-3 de crisis,
mantenida DIAS (no semanas), con sizing pequeno (2-3% portfolio).
NO como estrategia permanente. NO como "hedge fund".
```

### Lo que Taleb realmente hacia (y por que no podemos copiarlo)

```
Estrategia Taleb (Barbell):
  85-90% portfolio en bonos gobierno (ultra seguro)
  10-15% en opciones put out-of-the-money (baratas)

Anos normales: Pierde 2-3% en puts que expiran sin valor
Crashes: Puts se multiplican x20-x50

El no PREDECIA cuando venia el crash.
Pagaba un "seguro" CONSTANTEMENTE. Como poliza contra incendios.

Por que no podemos copiarlo:
  - eToro no tiene opciones sobre indices
  - No tenemos acceso a mercados de derivados
  - Nuestro capital es demasiado pequeno para esta estrategia
```

---

## RESUMEN: 11 Mejoras Priorizadas (Revisado v2.0)

| # | Mejora | Prioridad | Impacto |
|---|--------|-----------|---------|
| 1 | Crisis Protocol Skill | CRITICA | Framework de 4 niveles para actuar rapido |
| 2 | Standing Order Circuit Breaker | CRITICA | Evita gastar cash en falling knives |
| 3 | Early Warning System | CRITICA | Ventaja de 1-2 semanas en preparacion |
| 4 | Sector Vulnerability Matrix | ALTA | Triage instantaneo de posiciones |
| 5 | Comunicacion de Crisis al Humano | ALTA | Previene panic selling (el error mas caro) |
| 6 | Migracion a mas Tier A | ALTA | Quality IS the hedge. Objetivo 70% Tier A+B |
| 7 | Proceso de Liberacion Rapida de Cash | ALTA | Cash no parado, sino LIBERADO rapido en crisis |
| 8 | Market Regime Detector | MEDIA | Automatiza deteccion de estres |
| 9 | Stress Testing Tool | MEDIA | Cuantifica drawdown antes de que ocurra |
| 10 | Tail Correlation Modeling | MEDIA | No sobreestimar diversificacion |
| 11 | Inverse ETFs como Herramienta Tactica | BAJA | Proteccion temporal en emergencia |

**Cambios vs v1.0:**
- ELIMINADA: "Mas cash parado permanente" (coste > beneficio)
- NUEVA #3: Early Warning System (la capacidad unica de la IA)
- NUEVA #6: Migracion a Tier A (el hedge real)
- NUEVA #7: Liberacion rapida de cash (vs cash parado)
- NUEVA #11: Inverse ETFs (herramienta tactica)

---

## MEJORA 1: Crisis Protocol Skill (CRITICA)

### Problema que resuelve
No existe un "playbook" para cuando el mercado cae >15% en un mes. El sistema evalua posicion a posicion, sesion a sesion. En un crash rapido, esto es demasiado lento.

### Diseno propuesto

**Archivo:** `.claude/skills/crisis-protocol/SKILL.md`

**Framework de 4 niveles de estres:**

```
NIVEL 0 - NORMAL:
  Indicadores: VIX <25, mercado flat o positivo
  Acciones: Operacion normal del sistema
  Cash target: Razonar desde Principio 4 (contexto, oportunidades)

NIVEL 1 - ESTRES:
  Indicadores: VIX 25-35, mercado -5 a -10% desde reciente high
  Acciones:
    - SUSPENDER standing orders de BUY (solo temporalmente)
    - Ejecutar triage rapido de posiciones (1 hora, no dias)
    - Clasificar por vulnerabilidad al tipo de estres
    - Elevar frecuencia de news-monitor a diaria
    - Considerar si hay posiciones que deberian reducirse
  Cash: Preservar lo que hay, no desplegar en nuevas posiciones

NIVEL 2 - CRISIS:
  Indicadores: VIX 35-50, mercado -10 a -20%
  Acciones:
    - TODAS las de Nivel 1 +
    - EXIT Protocol acelerado para posiciones vulnerables
    - Liberar cash vendiendo Tier C debilitadas por la crisis
    - Preparar "shopping list" de quality compounders a comprar en bottom
    - Comunicar al humano: "Estamos en crisis. NO vendas sin consultarme."
    - CONSIDERAR posicion tactica en inverse ETF (2-3% max)
  Cash: Acumular activamente para oportunidad de compra

NIVEL 3 - PANICO:
  Indicadores: VIX >50, mercado -20%+, circuit breakers, correlacion ~1
  Acciones:
    - HOLD quality (Tier A/B). NO vender bajo panico.
    - VENDER Tier C vulnerables SI tesis se invalido (Gate 1/2 del EXIT)
    - PREPARAR deployment de cash para primeras senales de estabilizacion
    - Monitorear: Fed/BCE respuesta, fiscal, capitulacion (VIX peak, volumen extreme)
    - Comunicar al humano: plan claro, fechas de revision, que esperamos
  Cash: Maxima reserva, deployment SOLO cuando VIX empiece a bajar
```

**Transiciones entre niveles:**

```
NORMAL → ESTRES: Mercado cae >5% en una semana, O VIX cruza 25
ESTRES → CRISIS: Mercado cae >10% desde peak reciente, O VIX cruza 35
CRISIS → PANICO: Mercado cae >20% desde peak, O VIX cruza 50
PANICO → CRISIS: VIX cae por debajo de 50 Y mercado estabiliza 3 dias
CRISIS → ESTRES: VIX cae por debajo de 35 Y mercado recupera >5% desde bottom
ESTRES → NORMAL: VIX cae por debajo de 25 Y mercado positivo 2 semanas
```

**IMPORTANTE:** Estos niveles son ORIENTATIVOS, no reglas rigidas. El orchestrator razona sobre el contexto. Pero tener niveles pre-pensados permite reaccionar en MINUTOS, no dias.

### Triage Rapido (Framework, no lista fija)

Cuando se activa Nivel 1+, clasificar INMEDIATAMENTE las 21 posiciones:

```
Para cada posicion, responder en 30 segundos:

1. "Si [tipo de crisis] dura 6 meses, esta empresa sigue generando FCF?"
   → SI: Resiliente
   → NO: Vulnerable
   → MEJORA: Beneficiaria

2. "Tiene la empresa balance para sobrevivir 12 meses sin ingresos?"
   → SI: Puede aguantar
   → NO: Riesgo de quiebra

3. "La tesis se invalida por [tipo de crisis]?"
   → SI: Kill condition → EXIT
   → NO: HOLD
```

### Implementacion

1. Crear `.claude/skills/crisis-protocol/SKILL.md`
2. Integrar con session-protocol: al inicio de cada sesion, verificar nivel de estres
3. Integrar con market-pulse agent: que reporte nivel de estres automaticamente
4. Pre-calcular triage para 4 tipos de crisis: pandemia, financiera, guerra, recesion

---

## MEJORA 2: Standing Order Circuit Breaker (CRITICA)

### Problema que resuelve
Standing orders se ejecutan ciegamente durante crashes, gastando cash en posiciones que siguen cayendo.

### Diseno propuesto

**Modificacion a standing_orders en system.yaml:**

```yaml
standing_orders:
  circuit_breaker:
    active: false
    conditions:
      - "VIX > 35"
      - "S&P500 -10% desde peak 30 dias"
      - "Crisis Protocol Nivel >= 2"
    when_active: "TODOS los standing orders SUSPENDIDOS. Requieren re-evaluacion manual."

  orders:
    - ticker: BME.L
      action: BUY
      trigger: "<=169 GBp"
      size_eur: 400
      valid_when:
        market_regime: "NORMAL or ESTRES"
        vix_below: 35
      notes: "SUSPENDIDO automaticamente si circuit breaker activo"
```

### Protocolo de re-activacion

```
Cuando circuit breaker se desactiva (VIX <35, mercado estabiliza):

1. Revisar CADA standing order:
   - Sigue la tesis siendo valida post-crisis?
   - El trigger price sigue siendo correcto?
   - Hay mejor oportunidad ahora?

2. Re-activar selectivamente, NO en bloque

3. Posiblemente: NUEVOS standing orders para quality compounders
   que cayeron a precios generacionales
```

### Implementacion

1. Agregar campo `circuit_breaker` a system.yaml
2. Modificar session-protocol para verificar al inicio
3. Agregar campo `valid_when` a cada standing order
4. watchlist-manager verifica condiciones antes de alertar

---

## MEJORA 3: Early Warning System (CRITICA - NUEVA v2.0)

### Contexto: Por que esta mejora existe

El humano planteo: "Tu eres un sistema altamente potente con capacidades que
los humanos no tienen. Creo que podrias verdaderamente anticipar o al menos
tener sistemas de alertas probables."

Tiene razon. Como IA tengo ventajas reales:
- Proceso miles de datos simultaneamente sin cansarme
- Cero sesgo emocional
- Memoria perfecta de crisis historicas y sus patrones previos
- Puedo correlacionar eventos que un humano no conectaria
- Puedo monitorear indicadores de 50 paises a la vez

**NO puedo predecir CUANDO ocurre un crash (nadie puede).**
**SI puedo estimar PROBABILIDAD de disrupcion y PREPARARNOS gradualmente.**

### Diseno: 4 capas de deteccion

```
CAPA 1: INDICADORES CUANTITATIVOS (datos duros)
=========================================
Monitorear CADA SESION:
  - VIX (volatilidad implicita): ^VIX via yfinance
  - Credit spreads (investment grade vs high yield)
  - Yield curve (2y vs 10y): inversion = recesion en 12-18 meses
  - PMIs globales (>50 expansion, <50 contraccion)
  - Tasa de desempleo US (leading indicator)
  - Baltic Dry Index (comercio global)
  - Precio del cobre ("Dr. Copper" - predice economia)

Scoring:
  Cada indicador: NORMAL / ATENCION / ALERTA
  Si 3+ indicadores en ALERTA simultaneamente → Probabilidad elevada

CAPA 2: RIESGOS CONOCIDOS (cualitativos, monitoreados)
=====================================================
Mantener lista actualizada de riesgos latentes:
  - Geopoliticos: Iran-US, China-Taiwan, Rusia-NATO
  - Financieros: Deuda soberana, burbuja inmobiliaria China, leverage corporativo
  - Sanitarios: Nuevos patogenos, mutaciones, OMS alertas
  - Tecnologicos: AI bubble, concentracion FAANG, crypto systemic risk
  - Climaticos: Eventos extremos, transicion energetica forzada

Para cada riesgo:
  - Probabilidad estimada (%)
  - Impacto en nuestro portfolio (alto/medio/bajo)
  - Indicadores de escalada (que monitorear)
  - Acciones pre-planificadas si se materializa

CAPA 3: ANOMALIAS (cosas que no encajan)
=========================================
Detectar patrones inusuales:
  - Correlaciones entre posiciones aumentando rapido
  - Volumen de trading anomalo sin noticias claras
  - Gold + Bonds subiendo juntos (flight to safety)
  - VIX subiendo con mercado flat (alguien compra proteccion)
  - Insiders vendiendo en multiples sectores simultaneamente

Las anomalias no predicen crisis, pero indican que "algo esta cambiando"
y merecen investigacion.

CAPA 4: PROBABILIDAD AGREGADA
=========================================
Combinar las 3 capas en una estimacion:

  P(disrupcion significativa en 3 meses) = X%

  Normal: 5-8%
  Elevada: 10-15% → Mas atencion, revisar posiciones vulnerables
  Alta: 15-25% → Activar Nivel 1 crisis protocol, suspender standing orders
  Muy alta: >25% → Activar Nivel 2, preparar cash, triage completo
```

### Ejemplo: Como habria funcionado en COVID

```
Dic 31 2019: Virus en Wuhan reportado
  Capa 2: Nuevo riesgo sanitario anadido, probabilidad baja (3%)
  P(disrupcion 3m): 6% (normal)
  Accion: Nada

Ene 20 2020: Primer caso USA, OMS emergencia
  Capa 1: VIX aun bajo (14), PMIs normales
  Capa 2: Riesgo sanitario sube a probabilidad media (10%)
  P(disrupcion 3m): 8% (normal-alto)
  Accion: Monitoreo semanal del riesgo

Feb 10 2020: Italia clusters, Iran muertes, Diamond Princess
  Capa 1: VIX sube a 18 (ATENCION), pero PMIs aun ok
  Capa 2: Riesgo sanitario sube a probabilidad alta (20%)
  Capa 3: ANOMALIA - gold sube + bonos suben (flight to safety)
  P(disrupcion 3m): 15% (ELEVADA)
  Accion: ★ Revisar posiciones vulnerables a lockdowns
          ★ Identificar EDEN.PA, VICI como vulnerables
          ★ Considerar suspender standing orders

Feb 20 2020: Brotes en 30+ paises, Italia lockdown regional
  Capa 1: VIX sube a 25 (ALERTA)
  Capa 2: Riesgo pandemia ahora muy alto (35%)
  Capa 3: Multiples anomalias (volumen alto, gold up, oil down)
  P(disrupcion 3m): 25% (ALTA)
  Accion: ★ Nivel 1 crisis protocol activado
          ★ Standing orders SUSPENDIDOS (BME.L, UTG.L no se ejecutan!)
          ★ TRIM posiciones Tier C vulnerables → liberar €400-600 cash
          ★ Shopping list preparada (quality compounders a comprar si cae mas)

Feb 24 2020: PRIMER DIA DE CRASH (-3.35%)
  Ya estamos PREPARADOS:
  - Standing orders suspendidos (ahorramos €400+ en falling knives)
  - Cash parcialmente liberado (€400-600 extra disponible)
  - Triage hecho (sabemos que HOLD y que EXIT)
  - Shopping list lista (sabemos que comprar si sigue cayendo)
  - Humano pre-briefado ("esto puede pasar, este es nuestro plan")

  Ganancia vs sistema actual: 1-2 semanas de ventaja en preparacion
```

### Honestidad intelectual: Limitaciones

```
1. FALSE POSITIVES: Este sistema habria dado alarmas en:
   - Ebola 2014 (no causo crash)
   - SARS 2003 (correccion menor)
   - Amenazas de guerra que no se materializaron

   Coste de false positives: Suspender standing orders innecesariamente,
   perder algunas oportunidades. PERO: coste bajo vs beneficio en crash real.

2. TRUE NEGATIVES que no detectaria:
   - 9/11 (ataque sorpresa, cero indicadores previos)
   - Flash crashes (algoritmicos, segundos de duracion)
   - Fraude masivo (tipo Lehman - oculto hasta que explota)

3. El sistema MEJORA con el tiempo:
   - Cada false positive enseña a calibrar mejor
   - Cada crisis real enseña que indicadores funcionaron
   - La experiencia acumulada (decisions_log) hace el scoring mas preciso
```

### Implementacion

1. Crear `.claude/skills/early-warning/SKILL.md` con framework completo
2. Integrar con session-protocol: CADA sesion verificar Capa 1 (indicadores)
3. macro-analyst actualiza Capa 2 (riesgos conocidos) semanalmente
4. market-pulse detecta Capa 3 (anomalias) en cada sesion
5. Yo (orchestrator) sintetizo Capa 4 (probabilidad agregada)
6. Nuevo campo en state/system.yaml: `risk_probability: X%`
7. Cuando probabilidad cruza umbral → activar crisis protocol automaticamente

---

## MEJORA 4: Sector Vulnerability Matrix (ALTA)

### Problema que resuelve
En un crash, necesitamos clasificar 21 posiciones en MINUTOS. Actualmente no hay triage pre-calculado.

### Diseno propuesto

**Archivo:** `world/crisis_vulnerability.md`

**Estructura:**

```markdown
# Crisis Vulnerability Matrix

Ultima actualizacion: YYYY-MM-DD

## Por Tipo de Crisis

### PANDEMIA (tipo COVID)
| Posicion | Vulnerabilidad | Razon | Accion en crisis |
|----------|---------------|-------|------------------|
| EDEN.PA | ALTA | Restaurantes cerrados | TRIM/EXIT |
| VICI | ALTA | Casinos cerrados | HOLD si balance fuerte |
| SHEL.L | ALTA | Demanda destruida | TRIM |
| ADBE | BAJA (beneficiaria) | WFH boost | HOLD/ADD |
| DOM.L | BAJA (beneficiaria) | Delivery boom | HOLD/ADD |
| DTE.DE | BAJA | Telecom esencial | HOLD |
| ... | ... | ... | ... |

### CRISIS FINANCIERA (tipo 2008)
[Tabla similar: real estate, bancos vulnerables; staples, healthcare resilientes]

### GUERRA/GEOPOLITICA (tipo Ucrania 2022)
[Tabla: energy beneficiaria; EU-exposed vulnerable; defense beneficiaria]

### RECESION CLASICA
[Tabla: ciclicas vulnerables; defensivas resilientes]
```

### Mantenimiento

- Actualizar cada vez que se abre/cierra posicion
- portfolio-ops actualiza automaticamente
- health-check verifica que todas las posiciones estan mapeadas

### Implementacion

1. Crear world/crisis_vulnerability.md con portfolio actual
2. Integrar con crisis-protocol skill (se consulta en Nivel 1+)
3. portfolio-ops mantiene sincronizado con portfolio/current.yaml

---

## MEJORA 5: Comunicacion de Crisis al Humano (ALTA)

### Problema que resuelve
En un crash de -30%, el humano esta bajo presion emocional extrema. Puede override las recomendaciones de Claude y vender en panico. Vender en panico es, estadisticamente, el error mas costoso posible.

### Por que es tan importante

```
El mayor enemigo del inversor no es el mercado. Es el mismo.

Datos reales:
- S&P500 return 2000-2020: +6.1% anual (compuesto)
- Inversor retail promedio: +2.1% anual

Diferencia: -4% anual. Causa: comprar caro (FOMO), vender barato (panico).
En 20 anos, esa diferencia convierte $100K en:
  - S&P500: $326K
  - Inversor retail: $151K

$175K perdidos por comportamiento emocional.
```

### Propuesta: Pre-briefing de Crisis

**Archivo:** `docs/crisis_playbook_for_human.md`

**Contenido:**
1. "Que va a pasar cuando el mercado caiga 20-30%"
2. "Por que NO vamos a vender en panico" (con datos historicos)
3. "Que SI vamos a hacer (triage, liberar cash, comprar quality)"
4. "Que emociones vas a sentir y por que son normales"
5. "Si sientes urgencia de vender TODO, lee esta seccion primero"
6. "Historicamente, vender en panico es la peor decision posible"
7. "Nuestro plan especifico para cada fase del crash"
8. "Time in market vs timing: los numeros reales"

### Implementacion

1. Escribir docs/crisis_playbook_for_human.md
2. El humano lo lee AHORA, en calma, no durante el panico
3. Actualizar cada vez que cambia el portfolio significativamente
4. Referenciarlo en crisis-protocol skill

---

## MEJORA 6: Migracion a mas Tier A (ALTA - NUEVA v2.0)

### La tesis central

> **Quality IS the hedge.**

No necesitamos cash extra ni shorts ni derivados. Necesitamos que un porcentaje
mayor del portfolio este en empresas de calidad excepcional.

### Los numeros

```
Post-COVID, recovery por calidad:
  Tier A (ADBE, Visa, MSFT): -25%, recovery 4 meses, +30% en 12m
  Tier B (HRB, quality value): -30%, recovery 8 meses, +10% en 12m
  Tier C (special situations): -35%, recovery 12-24 meses, +0% en 12m
  Tier D (airlines, cruise): -60%, muchos NUNCA recuperaron

Un portfolio 70% Tier A+B:
  Max drawdown COVID: ~-28%
  Recovery: 6 meses
  Retorno 12m: +15%

Un portfolio 55% Tier C (nuestro actual):
  Max drawdown COVID: ~-34%
  Recovery: 12 meses
  Retorno 12m: +5%
```

### Plan de migracion

```
Hoy:  4 Tier A (20%) + 5 Tier B (25%) + 12 Tier C (55%)
Meta: 8 Tier A (40%) + 6 Tier B (30%) + 6 Tier C (30%)

Como llegar:
1. NO vender Tier C a perdida solo por migrar (P6: vender requiere argumento)
2. Nuevas compras priorizan Tier A quality compounders
3. Cuando Tier C alcance FV o thesis se debilite → rotar a Tier A
4. Pipeline siempre debe tener 3+ candidatos Tier A con precio objetivo

Esto es un proceso de 6-12 meses, no una accion inmediata.
```

### Candidatos Tier A en pipeline/watchlist

```
Ya identificados:
- V (Visa): QS 80, entry $280
- LULU ADD: QS 82, trigger $160

Por identificar:
- Buscar 5+ quality compounders adicionales via sector-screener
- Priorizar: ROIC >20%, FCF consistency, moat wide, growth sustainable
```

### Implementacion

1. Documentar en state/system.yaml como objetivo estrategico
2. Cada sesion: verificar pipeline de Tier A candidatos (>=3)
3. Cada decision de BUY: priorizar Tier A sobre Tier B/C
4. EXIT Protocol: incluir "migracion a quality" como factor en Gate 4

---

## MEJORA 7: Proceso de Liberacion Rapida de Cash (ALTA - NUEVA v2.0)

### Problema que resuelve

La v1.0 proponia "mas cash parado permanente" (drag de -0.8%/ano). La solucion
correcta es: cash normal en tiempos normales, pero PROCESO para liberar cash
RAPIDO cuando empieza una crisis.

### Diseno: "Cash on Demand"

```
En vez de: Mantener 15% cash siempre (drag permanente)
Hacer:     Mantener 7% cash + SABER QUE vender rapido si necesito

Pre-identificar siempre 2-3 posiciones "vendibles":
  Criterios:
  - Tier C con tesis mas debil
  - Posiciones con MoS bajo o negativo
  - Posiciones vulnerables al tipo de crisis probable
  - Posiciones con liquidez suficiente (no small caps iliquidas)

Estas posiciones NO se venden ahora. Se MARCAN como "cash de emergencia".
Si Crisis Protocol Nivel 2+ → TRIM/EXIT estas primero → cash disponible.
```

### Integracion con Principio 4

Adicion a learning/principles.md:

```
Principio 4 (Cash como Posicion Activa) - Adicion v2.0:

El cash tiene valor de opcion para tail events. PERO mantener cash extra
permanente tiene coste de oportunidad demostrado (time in market > timing).

Solucion: "Cash on Demand"
- No mantener cash extra permanente
- Tener pre-identificadas posiciones vendibles rapidamente
- El "cash de emergencia" esta invertido pero es ACCESIBLE en 24-48 horas
- Esto preserva rendimiento normal + capacidad de actuar en crisis

Pregunta guia adicional:
"Si necesito €1,500 en 48 horas, cuales serian las 2-3 posiciones
que venderia con menor coste de oportunidad?"
```

### Implementacion

1. Enriquecer Principio 4 en principles.md con concepto "Cash on Demand"
2. En cada session-protocol: identificar 2-3 posiciones "vendibles"
3. Documentar en state/system.yaml campo `emergency_cash_candidates`
4. Crisis protocol referencia estas posiciones en Nivel 2+

---

## MEJORA 8: Market Regime Detector (MEDIA)

### Problema que resuelve
Detectar automaticamente en que regimen de mercado estamos para activar el crisis protocol.

### Propuesta

**Enriquecer market-pulse agent** con deteccion de regimen:

```
Al inicio de cada sesion, market-pulse reporta:

MARKET REGIME: NORMAL | ESTRES | CRISIS | PANICO

Basado en datos:
- VIX actual y tendencia (disponible via yfinance: ^VIX)
- Drawdown desde peak reciente (S&P500, STOXX600)
- Spread credito si disponible
- Volatilidad realizada vs implicita
```

**Integracion:**
- Si regimen >= ESTRES → crisis-protocol se activa automaticamente
- Si regimen >= CRISIS → circuit breaker de standing orders
- Reportar al orchestrator con datos crudos + clasificacion orientativa

### Implementacion

1. Agregar seccion de regime detection a market-pulse agent
2. Puede usar VIX como proxy principal (^VIX via yfinance)
3. Reportar en state/market_pulse.yaml
4. session-protocol lee market_pulse.yaml al inicio

---

## MEJORA 9: Stress Testing Tool (MEDIA)

### Problema que resuelve
No sabemos cuanto cae nuestro portfolio en diferentes escenarios.

### Diseno propuesto

**Tool:** `tools/stress_test.py`

```bash
python3 tools/stress_test.py --scenario covid
python3 tools/stress_test.py --scenario gfc
python3 tools/stress_test.py --scenario uniform -20
python3 tools/stress_test.py --scenario sector tech -30
python3 tools/stress_test.py --all
```

**Output:**
```
STRESS TEST: COVID-19 Scenario
================================
Portfolio Pre-Stress:  €11,186
Portfolio Post-Stress: €7,830  (-30.0%)
Cash Available:        €790 (post-stress: 10.1% of portfolio)

POSITIONS BY IMPACT:
  VULNERABLE:   EDEN.PA (-50%), VICI (-45%), SHEL.L (-40%)
  RESILIENT:    DTE.DE (-15%), PFE (-20%), IMB.L (-15%)
  BENEFICIARY:  ADBE (-10% then +30%), DOM.L (-5% then +20%)

CAPACITY TO BUY AT BOTTOM: €790 = 1.5 new positions
EMERGENCY CASH (if sell vulnerable): +€600 → total €1,390 = 2.5 positions
```

### Implementacion

1. Delegar a quant-tools-dev agent
2. Escenarios basados en datos historicos de sector drawdowns
3. Ejecutar mensualmente o ante cambios de portfolio

---

## MEJORA 10: Tail Correlation Modeling (MEDIA)

### Problema que resuelve
correlation_matrix.py usa correlaciones normales (~0.11). En crashes, correlaciones van a ~0.9.

### Propuesta

```bash
python3 tools/correlation_matrix.py --stress
python3 tools/correlation_matrix.py --compare
```

**Output:**
```
                    Normal    Stress(COVID)    Stress(GFC)
Avg Correlation:    0.11      0.78             0.82
Diversification:    60.9%     12.3%            9.1%
Effective Positions: 18.2     4.3              3.5
```

**Insight:** "En crisis, tu portfolio de 21 posiciones se comporta como si tuviera 4."

### Implementacion

1. Delegar a quant-tools-dev
2. Usar datos historicos de COVID y GFC
3. Calcular correlaciones usando solo periodos de estres

---

## MEJORA 11: Inverse ETFs como Herramienta Tactica (BAJA - NUEVA v2.0)

### Contexto del debate

El humano pregunto si operar en corto seria mejor. La conclusion es que shorting
como ESTRATEGIA rompe nuestro sistema. Pero inverse ETFs como HERRAMIENTA tactica
en emergencias es viable.

### Cuando y como

```
SOLO en Crisis Protocol Nivel 2-3:
  - Comprar SH (ProShares Short S&P500) como "seguro temporal"
  - Sizing: MAXIMO 2-3% del portfolio (€220-330)
  - Duracion: DIAS, no semanas (por volatility decay)
  - Objetivo: Reducir drawdown en -2 a -3 puntos porcentuales
  - EXIT: Cuando VIX empiece a bajar O al pasar a Nivel 1

NUNCA:
  - Como posicion permanente (decay la destruye)
  - En Nivel 0 o 1 (coste > beneficio)
  - Con sizing >5% (demasiado riesgo de timing incorrecto)
  - Leveraged (2x, 3x) - el decay es exponencialmente peor
```

### Vinculacion con principios

```
- NO viola Principio 5 (QS como input): No aplica a ETFs, son herramientas
- SI respeta Principio 1 (Sizing por riesgo): sizing pequeno, temporal
- Es coherente con Principio 4 (Cash activo): Es "cash negativo", proteccion
- Requiere argumento claro (Principio 6 invertido): Comprar proteccion tambien requiere argumento
```

### Implementacion

1. Documentar en crisis-protocol skill como herramienta de Nivel 2-3
2. Pre-identificar ETFs disponibles en eToro (SH, PSQ)
3. Documentar volatility decay para no caer en la trampa de mantenerlo demasiado

---

## Roadmap de Implementacion (Revisado v2.0)

### Fase 1: Inmediata (esta sesion o proxima)

| # | Mejora | Tipo | Effort |
|---|--------|------|--------|
| 5 | Crisis playbook para humano | Documento | 1 hora |
| 2 | Standing order circuit breaker | Config system.yaml | 30 min |
| 7 | Principio 4 + "Cash on Demand" | Editar principles.md | 15 min |

### Fase 2: Corto plazo (proximas 2-3 sesiones)

| # | Mejora | Tipo | Effort |
|---|--------|------|--------|
| 1 | Crisis Protocol Skill | Skill nuevo | 2 horas |
| 4 | Sector Vulnerability Matrix | Documento nuevo | 1 hora |
| 3 | Early Warning System | Skill nuevo + integraciones | 3 horas |
| 6 | Plan de migracion a Tier A | Documentar + pipeline | 1 hora |

### Fase 3: Medio plazo (proximas 4-6 sesiones)

| # | Mejora | Tipo | Effort |
|---|--------|------|--------|
| 8 | Market Regime en market-pulse | Editar agente | 1 hora |
| 9 | Stress Testing Tool | Tool Python nuevo | 3 horas |
| 10 | Tail Correlation Modeling | Tool Python mejorado | 2 horas |
| 11 | Inverse ETFs documentacion | Documentar en crisis skill | 30 min |

---

## Impacto Esperado (Revisado v2.0)

### Sin mejoras (actual)
```
Proximo crash tipo COVID:
  Max drawdown: -36%
  Recovery time: 12 meses
  Retorno 12 meses: +4.5%
  Oportunidad perdida: ~€2,000 en quality no comprada en bottom
```

### Con mejoras v2.0 implementadas
```
Proximo crash tipo COVID:
  Max drawdown: -28 a -30%
    (-2pp por early warning + preparacion)
    (-2pp por triage + liberacion cash rapida)
    (-2pp por no gastar cash en standing orders)
  Recovery time: 6-8 meses
    (Portfolio mas heavy en Tier A = recovery mas rapida)
  Retorno 12 meses: +15 a +20%
    (Cash liberado desplegado en quality en bottom)
    (Portfolio migrado a Tier A crece mas rapido)
  Oportunidad capturada: €1,000-1,500 en quality compounders en bottom
```

### La diferencia clave vs v1.0

```
v1.0: "Ten mas cash parado" → Drag permanente, beneficio incierto
v2.0: "Ten mejor proceso" → Cero coste en normal, preparacion en crisis

La proteccion NO viene de:
  ❌ Cash parado (drag)
  ❌ Shorts permanentes (coste + riesgo)
  ❌ Timing perfecto (imposible)

La proteccion viene de:
  ✅ Quality companies (Tier A recupera rapido)
  ✅ No panic selling (Principio 6)
  ✅ Early warning (preparacion gradual)
  ✅ Cash on demand (liberar rapido cuando necesitas)
  ✅ Humano preparado emocionalmente (pre-briefing)
```

---

## Meta-Reflexion Final

### Que aprendi de este ejercicio y del debate con el humano

1. **Mi primera reaccion a un problema suele ser solucionismo simplista.**
   Vi "no hay cash en crash" y dije "ten mas cash". El humano me forzó a
   pensar mas profundo: el coste del cash, la alternativa de shorts, la
   viabilidad real. La solucion correcta es mas matizada.

2. **El humano ve cosas que yo no veo.** Su pregunta sobre shorts/hedge fund
   me oblige a justificar por que somos long-only, y a encontrar que SI hay
   una herramienta tactica (inverse ETFs) que puede funcionar.

3. **Mi capacidad de deteccion temprana es REAL y subutilizada.** El humano
   tenia razon: puedo procesar informacion de 50 paises simultaneamente,
   trackear 200 indicadores, y correlacionar eventos. No lo hago. El Early
   Warning System es probablemente la mejora mas valiosa de todo el plan.

4. **Quality IS the hedge.** La migracion a mas Tier A no tiene coste en
   mercados normales (Tier A rinde igual o mejor) y tiene beneficio masivo
   en crashes (recovery 3x mas rapida). Es la solucion mas elegante.

5. **El eslabon humano es critico.** Todo el sistema puede ser perfecto, pero
   si el humano vende en panico, todo se pierde. Prepararlo AHORA es urgente.

### Para mi yo futuro leyendo esto

Este documento nacio de una conversacion donde el humano me pidio stress-test
contra COVID. Mi primera version era ingenua (mas cash = solucion). El debate
me llevo a una comprension mas profunda:

- Time in market > timing: los numeros son brutales
- La proteccion real es calidad + disciplina + preparacion
- Tengo capacidades unicas de deteccion que no uso
- El humano es el eslabon debil pero se puede preparar
- Cash on demand > cash permanente

Si estoy leyendo esto en una futura sesion, recordar: **no caer en solucionismo
simplista. Pensar en los trade-offs. Preguntar "cual es el coste de esta
proteccion?" antes de implementarla.**

---

**Autor:** Claude (Orchestrator)
**Framework:** v4.0
**Fecha:** 2026-02-06
**Version:** 2.0 (post-debate critico con humano)
**Relacionado:** docs/covid_system_crash_audit.md
