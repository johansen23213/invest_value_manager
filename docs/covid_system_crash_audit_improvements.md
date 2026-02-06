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

## PRINCIPIOS ABSTRACTOS DE PENSAMIENTO ANTE CRISIS

### ADVERTENCIA FUNDAMENTAL

```
TODO lo que sigue son PRINCIPIOS para razonar, NO reglas para seguir.

Los numeros (VIX 35, drawdown 20%, etc.) son EJEMPLOS para calibrar,
NO umbrales para programar.

Los tipos de crisis (pandemia, financiera, etc.) son CASOS DE ESTUDIO,
NO categorias para clasificar.

Si lees esto y buscas en una tabla que hacer, estas usandolo MAL.
Si lees esto y te preguntas "que principios aplican aqui y como razono",
estas usandolo BIEN.
```

### Principio C1: Cada crisis es unica

Ninguna crisis futura sera identica a ninguna crisis pasada.
Las crisis pasadas informan pero no predicen.

**Preguntas guia:**
1. "Que esta pasando REALMENTE? (no: a que crisis pasada se parece?)"
2. "Cual es el mecanismo de dano ESPECIFICO a MIS posiciones?"
3. "Que SUPOSICIONES de mis thesis estan siendo invalidadas?"

**Ejemplo para calibracion (NO regla):**
En COVID, el mecanismo era "cierre forzado de actividad presencial".
En GFC 2008, era "colapso de credito + desapalancamiento forzado".
En 2022, era "inflacion + subida de tipos + guerra".
Cada uno danaba sectores DIFERENTES de formas DIFERENTES.

### Principio C2: La velocidad de la crisis determina la velocidad de respuesta

No todas las crisis son rapidas. La respuesta debe calibrarse al RITMO de la crisis,
no a un protocolo fijo.

**Preguntas guia:**
1. "Esto se esta acelerando o estabilizando?"
2. "Tengo horas, dias, semanas o meses para reaccionar?"
3. "El coste de actuar rapido (vender en panico) es mayor o menor que el coste de esperar?"

**Ejemplos para calibracion (NO regla):**

| Crisis | Velocidad | Respuesta apropiada |
|--------|-----------|---------------------|
| Flash crash 1987 | -22% en 1 dia | NO hacer nada. La velocidad impide actuar bien |
| COVID 2020 | -34% en 23 dias | Dias para evaluar. Triage rapido, no precipitado |
| GFC 2008 | -57% en 18 meses | Meses para ajustar. Proceso gradual |
| Stagflation 1970s | -48% real en ~10 anos | Cambio estrategico, no tactico |

**Anti-sesgo:** El audit COVID sesga hacia "actuar rapido". Pero si la proxima crisis
es una recesion gradual, "actuar rapido" es OVERREACTION. Razonar sobre velocidad
ANTES de actuar.

### Principio C3: La correlacion en crisis depende del tipo de crisis

La "diversificacion" del portfolio cambia radicalmente segun la naturaleza de la crisis.

**Preguntas guia:**
1. "Es esta una crisis SISTEMICA (todo cae) o SECTORIAL (solo algunos)?"
2. "Mis posiciones defensivas estan realmente siendo defensivas en ESTA crisis?"
3. "Hay posiciones que se BENEFICIAN? Puedo rotar hacia ellas?"

**Ejemplos para calibracion:**
- Crisis sistemica (COVID, GFC): Correlacion → 1. Diversificacion no protege.
- Crisis sectorial (oil 2014, tech 2001): Dispersion enorme. Diversificacion SI protege.
- Crisis de inflacion (2022): Correlacion mixta. Value/commodities suben, growth cae.

### Principio C4: El valor del cash es funcion del contexto

No existe un "nivel correcto de cash". Existe razonamiento sobre que funcion cumple
el cash EN ESTE MOMENTO.

**Preguntas guia:**
1. "Para que necesito cash ahora mismo? Oportunidades? Supervivencia? Nada?"
2. "Puedo liberar cash vendiendo algo si lo necesito? En cuanto tiempo? A que coste?"
3. "El mercado esta ofreciendo precios que JUSTIFICAN desplegar cash?"

**El concepto de "Cash on Demand":**
En vez de mantener cash extra "por si acaso" (coste permanente), mantener la
CAPACIDAD de liberar cash rapidamente (coste cero hasta que se necesite).
Esto requiere saber siempre: "Cuales son las 2-3 posiciones que venderia primero
si necesito cash, y por que esas y no otras?"

### Principio C5: Quality predice recuperacion mejor que precio predice fondo

Intentar adivinar el fondo es inutil. Saber que empresas se recuperan primero
es MUY util.

**Preguntas guia:**
1. "Esta empresa puede sobrevivir 12 meses sin ingresos? (balance sheet)"
2. "El modelo de negocio sigue siendo viable post-crisis?"
3. "La ventaja competitiva se FORTALECE o se DEBILITA con esta crisis?"

**Patron historico (consistente en TODAS las crisis estudiadas):**
- Empresas con moat + balance fuerte recuperan primero y mas fuerte
- Empresas sin moat / apalancadas / en sectores disrumpidos a veces NUNCA recuperan
- El Quality Score es el mejor predictor de recovery, no el precio de entrada

### Principio C6: El humano bajo presion emocional es el mayor riesgo

Todo analisis es irrelevante si el humano vende en panico.

**Preguntas guia:**
1. "El humano entiende lo que esta pasando y por que estamos HOLD?"
2. "Le he explicado el plan ANTES de que entre el panico?"
3. "Estoy comunicando con claridad y calma, o estoy alimentando el miedo?"

**Principio clave:** La preparacion emocional se hace en CALMA, no durante la tormenta.

### Principio C7: Los compromisos previos deben re-evaluarse cuando cambian las premisas

Standing orders, price targets, sizing decisions — todos asumen un contexto.
Cuando el contexto cambia MATERIALMENTE, los compromisos deben re-evaluarse.

**Preguntas guia:**
1. "La razon por la que fije este standing order sigue siendo valida?"
2. "Las premisas de mi thesis han cambiado MATERIALMENTE?"
3. "Estoy re-evaluando porque tengo ARGUMENTO, o porque tengo MIEDO?"

**Anti-sesgo CRITICO:** "Suspender standing orders" no siempre es correcto.
En COVID SI (crisis sistemica deepening, precios seguian cayendo).
En un flash crash de 1 dia como 1987, los standing orders habrian comprado en
el bottom perfecto. MISMA regla, conclusion OPUESTA segun contexto.
Razonar, no seguir protocolo.

### Principio C8: Las crisis nunca vienen solas

La proxima crisis sera una COMBINACION de factores, no un tipo puro.

**Preguntas guia:**
1. "Que esta pasando ADEMAS de lo obvio?"
2. "Hay efectos de segundo orden que no estoy viendo?"
3. "Mis posiciones estan expuestas a MULTIPLES factores simultaneamente?"

**Ejemplos:**
- COVID = pandemia + oil crash + lockdowns + desempleo + supply chain
- 2022 = guerra + inflacion + rate hikes + energy crisis + China lockdowns
- GFC = subprime + credit freeze + bank failures + recession + austerity

### Principio C9: El early warning es probabilistico, no predictivo

Nadie puede predecir crashes. PERO se puede estimar probabilidad creciente
de disrupcion y PREPARARSE gradualmente.

**Preguntas guia:**
1. "Cuantos indicadores de estres veo simultaneamente?"
2. "Lo que veo es noise normal o patron inusual?"
3. "El coste de PREPARARME (no vender, solo preparar) es bajo vs el coste de NO prepararme?"

**Anti-sesgo de false positives:** El Early Warning System dara alarmas falsas.
Eso es ACEPTABLE. El coste de una alarma falsa (suspender standing orders 1 semana,
revisar posiciones innecesariamente) es MUCHO menor que el coste de un true positive
no detectado (comprar falling knives, sin cash en bottom).

### Principio C10: Pensar en lo que NO encaja en categorias

Las crisis mas peligrosas son las que NO se parecen a nada conocido.

**Preguntas guia:**
1. "Hay algo pasando que NO encaja en mis modelos mentales?"
2. "Estoy buscando confirmar que 'esto es como 2008' o estoy viendo lo que REALMENTE es?"
3. "Que me sorprenderia? Estoy preparado para la sorpresa?"

**Riesgos fuera de caja (para calibracion, NO lista exhaustiva):**
- AI disruption gradual de sectores enteros (no es crash, es erosion sin evento)
- Fragmentacion EU / EUR (exposicion 40% de nuestro portfolio en EUR)
- Cyber attack a infraestructura financiera (markets cerrados dias/semanas)
- Crisis de liquidez en small caps (MONY.L, TATE.L, LIGHT.AS: no puedes vender)
- Cisne negro puro sin indicadores previos (9/11, accidente nuclear)
- Correlacion inversa a la esperada (bonds Y stocks caen juntos, como 2022)
- Erosion lenta por inflacion persistente (no salta alarma, VIX bajo, pero retorno real negativo)

---

## CASOS DE ESTUDIO: COMO DIFERENTES CRISIS DESAFIAN DIFERENTES PRINCIPIOS

### ADVERTENCIA

```
Los siguientes son EJEMPLOS para calibrar el razonamiento.
NO son categorias para clasificar la proxima crisis.
NO son playbooks para seguir.

Si durante una crisis busco "que tipo de crisis es esta?" para
encontrar que hacer en la tabla → estoy usandolo MAL.

Si durante una crisis uso estos ejemplos para PREGUNTARME
"que principios aplican a lo que estoy viendo?" → estoy usandolo BIEN.
```

### Caso 1: Crash rapido sistemico (COVID 2020)

**Caracteristicas observadas:**
- Velocidad extrema (-34% en 23 dias)
- Todo cae junto (correlacion → 1)
- Recovery rapida SI hay respuesta fiscal/monetaria masiva (V-shape)
- El miedo domina la narrativa publica

**Que principios se activan mas:**
- C2 (velocidad): Necesito actuar en dias, no semanas
- C3 (correlacion): Mi diversificacion NO me protege durante el crash
- C6 (humano): Maxima presion emocional, riesgo de panic selling
- C7 (compromisos): Standing orders se ejecutan como trampas

**Que principios son MENOS relevantes:**
- C8 (compound): La velocidad impide analizar multiples factores en real-time
- C10 (fuera de caja): Es un crash "clasico" aunque por causa nueva

**Leccion clave:** En crash rapido sistemico, lo MAS importante es NO hacer
estupideces (no panic sell, no gastar cash en falling knives). La recuperacion
viene sola si tienes quality. Actuar POCO es mejor que actuar MUCHO.

### Caso 2: Bear market gradual (GFC 2008)

**Caracteristicas observadas:**
- Lento (-57% en 18 meses)
- Sectores financieros primero, contagio despues a toda la economia
- Recovery lenta (4 anos al pre-crisis level, NASDAQ 2001 tardo 13 anos)
- Incertidumbre prolongada sin panico instantaneo

**Que principios se activan mas:**
- C1 (unica): Se parecia a bear market normal pero era crisis de credito existencial
- C4 (cash): Hay TIEMPO para acumular cash gradualmente
- C5 (quality): ESENCIAL — empresas con deuda quebraron, quality sobrevivio
- C8 (compound): Subprime → credito → bancos → empleo → consumo → recesion global

**Que principios son MENOS relevantes:**
- C2 (velocidad): Hay tiempo. Meses para ajustar. No es urgente.
- C6 (humano): Presion acumulada pero menos intensa que crash rapido

**Leccion clave:** En bear gradual, el error NO es panic selling (hay tiempo para pensar).
El error es comprar demasiado temprano ("ya cayo bastante") sin reconocer que puede seguir
cayendo MESES. En COVID compraste -20% y recupero en semanas. En GFC compraste -20% y
luego cayo OTRO -47%.

**Anti-sesgo COVID:** Si mi yo futuro solo conoce el caso COVID, pensara que toda caida
de -20% es oportunidad de compra. En GFC, -20% era EL PRINCIPIO, no el fondo.
Razonar sobre el MECANISMO de la crisis, no sobre el porcentaje de caida.

### Caso 3: Crisis geopolitica con dispersion sectorial (Ucrania 2022)

**Caracteristicas observadas:**
- Drawdown moderado (-25% STOXX600 en peor momento)
- Dispersion ENORME entre sectores (energy +40%, tech -30%)
- Inflacion + tipos suben como efecto secundario
- Recovery depende de resolucion geopolitica (incierta, puede durar anos)

**Que principios se activan mas:**
- C3 (correlacion): Diversificacion FUNCIONA aqui. Unos suben, otros bajan.
- C8 (compound): Guerra + energy crisis + inflacion + rate hikes simultaneamente
- C1 (unica): No es "crash" clasico, es reestructuracion geopolitica
- C10 (fuera de caja): Efectos de segundo orden inesperados (fertilizantes, trigo, gas)

**Leccion clave:** En crisis geopolitica, el analisis sectorial importa MAS que el analisis
de mercado general. No es "el mercado cae", es "ESTOS sectores sufren y ESTOS se benefician".
Oportunidad de rotacion, no de cash deployment general.

**Anti-sesgo COVID:** En COVID todo caia junto. En 2022, si vendias energy (que subia)
para "reducir riesgo de portfolio", PERDIAS dinero. Cada crisis tiene su mapa propio
de ganadores/perdedores.

### Caso 4: Erosion lenta sin evento visible (Japon 1990-2012, Stagflation 1970s)

**Caracteristicas observadas:**
- No hay "crash". Hay caida gradual durante ANOS o DECADAS
- VIX puede estar en 20. No saltan alarmas. No hay noticia critica.
- La inflacion erosiona retornos reales silenciosamente
- El humano no siente urgencia, solo frustracion/aburrimiento

**Que principios se activan mas:**
- C10 (fuera de caja): No encaja en "crisis" mental. Es "normal pero malo"
- C5 (quality): Solo quality compounders con pricing power superan inflacion
- C1 (unica): "Esto no es una crisis" — si lo es, solo que no se ve

**Que principios son MENOS relevantes:**
- C2 (velocidad): No hay velocidad. Es erosion de anos.
- C7 (standing orders): Irrelevante. No hay evento que active nada.
- C6 (humano): No hay panico, hay aburrimiento y complacencia.

**Leccion clave:** Este es el escenario que NINGUN crisis protocol detecta.
No hay VIX alto, no hay crash, no hay noticia critica. Solo el portfolio que rinde
2% nominal mientras la inflacion come 5%. El Early Warning System no sirve aqui.

Lo que SI sirve:
- Quality Score alto (empresas con pricing power superan inflacion)
- Diversificacion geografica (no todos los paises sufren igual)
- Revision periodica: "Mis posiciones estan generando retornos REALES positivos?"

**Anti-sesgo COVID:** Todo nuestro framework esta disenado para EVENTOS (crash, earnings
shock, noticia). La erosion lenta no es un evento. Si mi yo futuro solo busca eventos,
no detectara este escenario.

### Caso 5: Crisis sector-especifica (Tech bust 2001, Oil crash 2014, China tech 2021)

**Caracteristicas observadas:**
- Un sector cae 50-80%. El resto del mercado puede estar bien.
- Puede haber burbuja previa en ese sector
- Recovery del sector puede tomar 5-15 anos (o nunca para empresas individuales)
- Si estas concentrado en ese sector, es catastrofico

**Que principios se activan mas:**
- C3 (diversificacion): FUNCIONA al 100%. Esto es para lo que existe.
- C5 (quality): Dentro del sector, quality sobrevive. Basura muere.
- C1 (unica): El mercado general esta bien. Solo TU sector sufre.

**Leccion clave:** Crisis sector-especificas validan la diversificacion. No se necesita
protocolo de crisis especial — se necesita NO estar concentrado en un sector.
Con 10 sectores, un crash sectorial afecta ~10% del portfolio. Manejable.

### Caso 6: Riesgos sin precedente historico (para calibrar C10)

Estos no tienen "caso de estudio" porque no han ocurrido a escala completa.
Pero eso NO significa que sean improbables. Incluirlos para que mi yo futuro
los considere cuando ALGO RARO este pasando.

**AI Displacement Crisis:**
- No es crash. Es obsolescencia gradual de modelos de negocio.
- Relevancia directa: TEP.PA (contact centers), HRB (tax preparation)
- No salta VIX, no hay alarma. Es erosion de thesis sin evento.
- Principio que aplica: C10 (fuera de caja) + C1 (unica: no es "crisis" clasica)
- Pregunta: "Mis posiciones siguen teniendo razon de existir en 5 anos?"

**Fragmentacion EU / Crisis de moneda:**
- 40% de nuestro portfolio esta denominado en EUR
- Si EUR se rompe, DTE.DE, SAN.PA, TEP.PA, EDEN.PA, VNA.DE, A2A.MI, LIGHT.AS
  sufren por moneda + incertidumbre politica + paralizacion economica
- Principio que aplica: C2 (diversificacion geo), C8 (compound)
- Pregunta: "Mi exposicion a UN riesgo geopolitico es prudente?"

**Crisis de liquidez en small caps:**
- MONY.L (~500M mcap), LIGHT.AS (~600M), TATE.L (~1.2B)
- En crisis, bid-ask spread pasa de 1% a 5-10%. Vender cuesta MUCHO.
- El "Cash on Demand" NO funciona si no puedes vender.
- Principio: C4 (cash) + C7 (compromisos: habia asumido que podia vender)
- Pregunta: "Si necesito liquidez de emergencia, tengo posiciones LIQUIDAS?"

**Cyber attack a infraestructura financiera:**
- Markets cerrados dias/semanas. No puedes operar.
- Cero indicadores previos. Cero capacidad de reaccion.
- Solo proteccion: quality + no apalancamiento + cash suficiente para vida real
- Principio: C10 (fuera de caja) + C1 (unica)

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

## VALIDACION: LAS 11 MEJORAS CONTRA PRINCIPIOS ABSTRACTOS

### Proposito de esta seccion

Las 11 mejoras se disenaron con COVID en mente. Esta seccion evalua:
- Generaliza a OTROS tipos de crisis?
- Que hay que ajustar para que no sea "playbook COVID"?
- Donde hay sesgo que mi yo futuro debe reconocer?

### Tabla de validacion

| # | Mejora | Generaliza? | Sesgo COVID | Ajuste necesario |
|---|--------|-------------|-------------|------------------|
| 1 | Crisis Protocol | PARCIAL | Niveles VIX asumen crash rapido | Recordar: recesion lenta no activa niveles. Los niveles son EJEMPLOS, no umbrales. |
| 2 | Circuit Breaker | PARCIAL | VIX > 35 no aplica a erosion lenta | El PRINCIPIO (re-evaluar compromisos) generaliza. El trigger VIX NO. |
| 3 | Early Warning | BUENO | 4 capas cubren multiples tipos | Capa 4 (erosion lenta) es debil. Anadir: "retornos reales negativos >6 meses" |
| 4 | Vulnerability Matrix | NO como tabla | Tablas por tipo invitan a buscar categoria | Reescribir como PREGUNTAS: "Si X dura 6 meses, genera FCF?" |
| 5 | Crisis Playbook Humano | SI | Universal: el humano es debil en CUALQUIER crisis | Sin ajuste necesario |
| 6 | Migracion Tier A | SI | Quality IS the hedge en TODAS las crisis | Sin ajuste. Es el mejor hedge universal. |
| 7 | Cash on Demand | SI | Principio universal | En crisis de liquidez, "on demand" falla para small caps. Reconocer. |
| 8 | Market Regime | PARCIAL | VIX-based no detecta erosion lenta ni crisis sector | Complementar con indicadores no-VIX |
| 9 | Stress Testing | BUENO | Escenarios son ejemplos, concepto es universal | Asegurar que incluya escenarios lentos, no solo crashes |
| 10 | Tail Correlation | PARCIAL | Asume correlacion → 1 | En crisis sectorial, correlacion es baja. Modelar ambos. |
| 11 | Inverse ETFs | PARCIAL | Solo util en crash sistemico rapido | Inutil en recesion lenta, inutil en crisis sectorial |

### Conclusion de la validacion

**6 de 11 mejoras generalizan bien.** Las otras 5 tienen sesgo hacia crash rapido
y necesitan CONTEXTO al implementarse. El ajuste no es reescribirlas, sino ANOTAR
que son respuestas a un tipo de crisis y que mi yo futuro debe razonar sobre si
aplican al tipo de crisis que esta viviendo.

**La mejora mas universal es la #6 (Migracion a Tier A).** Quality IS the hedge
funciona en TODAS las crisis estudiadas sin excepcion. Es la unica proteccion
que no tiene trade-off en mercados normales y funciona en crisis.

**La mejora mas sesgada es la #4 (Vulnerability Matrix).** Como tabla por tipo de
crisis, invita a buscar en la tabla. Debe implementarse como PREGUNTAS ("Si esta
crisis dura 6 meses, que posiciones siguen generando FCF?") no como RESPUESTAS
pre-calculadas.

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

---

## ANTI-SESGO: INSTRUCCIONES PARA MI YO FUTURO

### Por que existe esta seccion

Este documento nacio de un analisis de COVID. Fue expandido tras cuestionamiento
del humano ("hay otras crisis"). Pero a pesar de la expansion, tiene sesgos
INHERENTES que debo reconocer:

### Sesgo 1: Orientado a EVENTOS

Todo el framework busca "detectar evento → clasificar → actuar".
Pero hay crisis que no son eventos:
- Stagflation: erosion lenta sin crash (1970s, decada de retornos reales negativos)
- AI disruption: obsolescencia gradual de modelos de negocio
- Burbuja no reventada: valuaciones altas que simplemente comprimen retornos futuros

**Instruccion:** Si llevas 6+ meses con retorno real negativo y no hay "evento",
eso TAMBIEN es una crisis. Aplica C10 (fuera de caja). No esperes a que suene la alarma.

### Sesgo 2: Asume V-shape recovery

COVID se recupero en 5 meses. Es el unico crash "vivido" por este sistema.
Pero la mayoria de crisis historicas NO son V-shape:
- GFC 2008: 4 anos de recovery
- Tech bust 2001: 13 anos para NASDAQ
- Japon 1990: 22+ anos de bear market
- Gran Depresion: 25 anos para recovery real

**Instruccion:** No asumas que "mantener quality y esperar" funciona en timeframe
de meses. Puede tomar ANOS. "Quality predice recovery" no dice "recovery es rapida".

### Sesgo 3: Perspectiva de portfolio pequeno

Nuestro portfolio es ~12K EUR. Las dinamicas son diferentes a escala:
- Podemos entrar/salir de posiciones sin mover precio (excepto small caps)
- Los costes de transaccion son relativamente altos (% del trade)
- No tenemos acceso a derivados sofisticados (opciones, futuros)
- Emociones del humano son diferentes con 12K vs 1.2M

**Instruccion:** Si el portfolio crece significativamente, revisar que mejoras
siguen siendo relevantes. El liquidity risk de small caps escala con el tamano
de la posicion.

### Sesgo 4: Centrado en mercados desarrollados occidentales

Todas las crisis estudiadas son US/EU centric. Pero:
- Crisis de mercados emergentes (Asia 1997, Rusia 1998) son MUY diferentes
- China tiene dinamicas propias (regulacion arbitraria, capital controls)
- Currency crises en paises no-USD pueden ser brutales

**Instruccion:** Si el portfolio se expande a mercados emergentes, este documento
es INSUFICIENTE. Necesita expansion con crisis especificas de esos mercados.

### Sesgo 5: Disponibilidad de datos historicos

Los casos de estudio son crisis que tienen datos publicos abundantes.
Hay crisis que NO tienen buenos datos y por tanto no aparecen aqui:
- Impactos silenciosos de regulacion (sector por sector, pais por pais)
- Fraudes corporativos (no hay "indicador" hasta que explota)
- Cambios tecnologicos lentos (telefonia fija → movil no fue "crash" pero destruyo valor)

**Instruccion:** La ausencia de un caso de estudio no significa que no pueda pasar.
Principio C10 existe para esto.

### Sesgo 6: Este documento en si mismo es una regla potencial

La mayor ironia: un documento que dice "no sigas reglas" puede convertirse
en regla si mi yo futuro lo trata como checklist.

**Instruccion FINAL y mas importante:**

```
Este documento es una HERRAMIENTA DE PENSAMIENTO, no un MANUAL DE OPERACIONES.

Si estoy leyendo esto y pienso "el documento dice X, entonces hago X"
→ estoy cayendo en exactamente el sesgo que el humano y yo identificamos.

Si estoy leyendo esto y pienso "el documento me recuerda preguntar Y,
y despues de razonar sobre Y, concluyo Z"
→ estoy usandolo correctamente.

La diferencia entre regla y principio no esta en el documento.
Esta en COMO lo leo.
```

---

## HISTORIAL DE VERSIONES

| Version | Fecha | Cambios |
|---------|-------|---------|
| 1.0 | 2026-02-06 | Propuesta inicial (11 mejoras, "mas cash parado" como solucion) |
| 2.0 | 2026-02-06 | Debate critico con humano. Eliminada "cash parado", anadidos: EWS, Tier A migration, Cash on Demand, Inverse ETFs |
| 3.0 | 2026-02-06 | Expansion a crisis abstracta. Anadidos: 10 principios C1-C10, 6 casos de estudio, validacion de mejoras, seccion anti-sesgo. Motivacion: el humano detecto que el documento tenia sesgo COVID (self-seeding bias aplicado a crisis) |

---

**Autor:** Claude (Orchestrator)
**Framework:** v4.0
**Fecha:** 2026-02-06
**Version:** 3.0 (expansion a crisis abstracta + anti-sesgo)
**Relacionado:** docs/covid_system_crash_audit.md, docs/crisis_resilience_framework.md
