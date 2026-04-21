# Simulacion Contrathesis: MONY.L (MoneySupermarket)

> **Tipo:** Ejercicio simulado — SIN cambios al sistema, portfolio ni state files
> **Fecha:** 2026-02-15
> **Proposito:** Aplicar el framework de contrathesis (Seccion 13 de short_selling_framework_design.md) a MONY.L como si la analizaramos desde cero. Comparar resultados con lo que nuestro proceso estandar encontro realmente.
> **Precio actual:** 147.10 GBp | **Nuestro coste medio:** 232 GBp (-37%)

---

## PASO 1: Que Cree el Consenso?

### 1.1 El Consenso Alcista (pre-crash, ~2025)

Antes del panico por AI, el consenso era:

- **Morgan Stanley (pre-downgrade):** Overweight, PT 275p. "Jugada defensiva UK con alto dividendo."
- **Berenberg:** BUY, PT 275p (mantenido incluso post-crash). "Negocio maduro, fuerte generacion de caja."
- **Sell-side general:** P/E 15-18x era "justo". Revenue creciendo low-single digits. Yield 7%+ atrae fondos de renta.
- **Narrativa:** "Aburrido pero fiable. Los consumidores UK comparan precios online, eso no va a cambiar."

**Lo que asumia el consenso alcista:**
- Los comparadores de precios estan estructuralmente arraigados en el comportamiento del consumidor UK
- La red de 5,000+ proveedores es un moat inexpugnable
- El crecimiento del 5-7% en revenue continuaria
- AI es un buzzword que no aplica a los comparadores
- El multiplo P/E se expandiria desde el rango 11-12x

### 1.2 El Consenso Bajista (post-Insurify, Feb 2026)

Tras el crash, el NUEVO consenso es:

- **Morgan Stanley (post-downgrade 21 ene):** Equalweight, PT 220p. "Creciente preocupacion sobre la posicion de MONY en un mundo de AI agentica."
- **Accion del mercado:** -25% desde maximo 52 semanas. P/E comprimido a 9.7x. En minimo de 13 anos.
- **Narrativa:** "Los agentes AI (ChatGPT/Insurify) desintermediaran los comparadores de precios. El modelo de negocio es obsoleto."
- **Medios:** Articulos "El Fin de los Comparadores" proliferando.

**Lo que asume el consenso bajista:**
- Los agentes AI pueden replicar lo que hacen los comparadores
- Los consumidores UK cambiaran rapidamente del habito PCW a agentes AI
- La red de proveedores de MONY puede ser replicada por OpenAI/Google
- El P/E 9.7x SIGUE siendo caro dada la disrupcion estructural
- MONY ira por el camino de las Paginas Amarillas, agencias de viaje, stockbrokers

### 1.3 La Posicion Neutral

**El mercado esta priciendo crecimiento 0-1% para siempre** (segun nuestro reverse DCF en thesis v1.0). Esto implica que el mercado cree que MONY es un negocio sin crecimiento, un cubo de hielo derritiendose con buen dividendo. No muerto aun, pero muriendo lentamente.

---

## PASO 2: De Que Depende Cada Creencia?

### 2.1 Cadena de Dependencias Alcista

```
"MONY es un quality compounder que vale 15-18x earnings"
  ↓ Depende de:
"Revenue crecera 5-7% anual"
  ↓ Depende de:
"Los consumidores UK seguiran comparando precios via web"
  ↓ Depende de:
"No existe mejor alternativa para comparar productos financieros"
  ↓ Depende de:
"Los agentes AI NO PUEDEN replicar la funcion de comparacion"
  ↓ Depende de:
"La integracion de proveedores, regulacion FCA, y complejidad
 de datos crean barreras que la AI no puede cruzar"
  ↓ ES ESTO CIERTO?

ESLABON FRAGIL IDENTIFICADO: La afirmacion "AI no puede replicar
la comparacion" esta ahora empiricamente desafiada. Insurify lo
hizo (EEUU, seguro de coche). La pregunta es CUANDO/SI llega a
UK y CUANTO penetra.
```

### 2.2 Cadena de Dependencias Bajista

```
"MONY es un modelo de negocio moribundo, P/E justo es 6-8x"
  ↓ Depende de:
"Los agentes AI reemplazaran los comparadores para consumidores UK"
  ↓ Depende de:
"Los agentes AI pueden obtener autorizacion FCA para intermediar seguros"
  ↓ Depende de:
"La FCA adapta su framework para permitir comparacion de productos
 financieros mediada por AI"
  ↓ Depende de:
"La cultura regulatoria UK cambia de 'proteccion al consumidor via
 comparacion estandarizada' a 'proteccion al consumidor via AI'"
  ↓ ES ESTO CIERTO?

ESLABON FRAGIL IDENTIFICADO: Cambio regulatorio UK. La FCA tiene
un framework especifico de "customer duty" que OBLIGA a presentacion
clara y comparable de productos. Los comparadores fueron literalmente
disenados para esto. Las conversaciones con ChatGPT son lo opuesto
a comparacion estandarizada. Aprobacion FCA para seguros mediados
por AI NO es inminente.
```

Tambien depende de:
```
"Los consumidores QUIEREN usar AI para comparar seguros"
  ↓ Depende de:
"Los consumidores confian en AI con datos financieros sensibles"
  ↓ Depende de:
"Los consumidores ven la AI como fiable para decisiones financieras
 con consecuencias reales"
  ↓ ES ESTO CIERTO?

ESLABON FRAGIL IDENTIFICADO: Confianza. El 96.7% de consumidores UK
ya usan PCWs para seguros. La inercia de comportamiento es enorme.
Cambiar de un sitio web de confianza a un chatbot de AI para algo tan
consecuente como un seguro requiere una transferencia masiva de
confianza que no ha ocurrido.
```

### 2.3 Resumen: Ambos Lados Tienen Dependencias Fragiles

| Consenso | Dependencia Fragil Clave | Probabilidad de Romperse |
|----------|-------------------------|-------------------------|
| **Alcista** | "AI no puede replicar la comparacion" | MEDIA — prueba de concepto existe (Insurify) |
| **Bajista** | "FCA permitira seguros mediados por AI" + "consumidores confiaran en AI" | BAJA-MEDIA — barreras regulatorias y de comportamiento son reales |

**Insight clave:** La cadena bajista tiene MAS eslabones fragiles y MAS barreras que superar que la alcista. Pero la cadena alcista tiene UN eslabon critico ("AI no puede replicar") que fue agrietado por Insurify.

---

## PASO 3: Quien Tiene Incentivo en Mantener Cada Narrativa?

### 3.1 Quien se beneficia de la narrativa ALCISTA?

| Actor | Incentivo | Fuerza |
|-------|-----------|--------|
| **Management de MONY** | Bonos vinculados al precio, seguridad laboral | ALTA |
| **Berenberg** (broker, rating BUY) | Relacion bancaria, comisiones de brokerage | MEDIA |
| **Fondos de renta** | Tienen MONY por el 8.2% yield, necesitan narrativa para mantener posicion | ALTA |
| **Empleados MONY** (10.4% insider ownership) | Riqueza atada a las acciones | MEDIA |
| **Lobby de comparadores UK** | Supervivencia del sector | MEDIA |

### 3.2 Quien se beneficia de la narrativa BAJISTA?

| Actor | Incentivo | Fuerza |
|-------|-----------|--------|
| **Empresas AI (OpenAI, Google)** | Narrativa de "AI disrumpe todo" impulsa inversion/adopcion | ALTA |
| **Vendedores en corto** | Beneficios de la caida de precio | MEDIA |
| **Medios tech** | "AI mata industria X" genera clicks | ALTA |
| **Insurify** | Su producto recibe publicidad gratuita por la cobertura del crash de MONY | ALTA |
| **PCWs competidores** (si pivotan a AI-first) | Ganancia de cuota si la narrativa debilita a MONY | BAJA |

### 3.3 Analisis del Desequilibrio de Incentivos

La narrativa bajista esta impulsada por actores con VOCES MUY ALTAS (empresas AI, medios tech) pero poco skin in the game especifico de UK. Insurify es solo EEUU. OpenAI no ha anunciado comparacion de seguros UK. Los AI Overviews de Google afectan trafico SEO pero no reemplazan la comparacion en si.

La narrativa alcista esta defendida por actores con INTERES FINANCIERO DIRECTO en MONY pero VOCES CALLADAS (management, holders institucionales, fondos de renta no escriben titulares).

**Implicacion:** La narrativa esta actualmente sesgada hacia lo bajista porque los actores mas ruidosos se benefician del caso bajista. Pero los actores con mayor conocimiento directo (management, CEO que compro a 170.6p, Berenberg que mantiene BUY) son alcistas.

Esto no significa que los alcistas tengan razon — los insiders pueden equivocarse. Pero el ANALISIS DE INCENTIVOS sugiere que la narrativa bajista puede estar amplificada mas alla de su justificacion fundamental.

---

## PASO 4: Donde Podria Estar Equivocado el Consenso?

### 4.1 Donde el consenso ALCISTA se equivoca

1. **"AI no puede replicar la comparacion"** — Ya lo ha hecho (Insurify, EEUU). La pregunta es CUANDO, no SI. Pretender que no puede pasar es negacion.

2. **"Revenue crecera 5-7%"** — El crecimiento REAL ha sido ~1-2% (hallazgo adversarial). El sell-side usaba estimaciones de crecimiento obsoletas. El segmento de seguros (-2% H1 2025) es la mayoria del revenue.

3. **"El P/E se expandira a 15-18x"** — Por que? Que catalizador? Si el overhang de AI persiste, no hay driver de re-rating. El mercado tiene razon en asignar un descuento por riesgo de disrupcion tecnologica. La pregunta es CUANTO descuento.

4. **"La red de proveedores es moat inexpugnable"** — Tardo decadas en construirse, si. Pero solo necesita UNA gran plataforma AI para replicarla via APIs directas con aseguradoras. Si Google decide entrar en comparacion de seguros UK via sus relaciones existentes, el moat podria erosionarse mas rapido de lo asumido.

5. **"MONY usa AI para 60% de contactos con clientes = AI es oportunidad"** — Esto confunde AI OPERATIVA INTERNA (ahorro de costes, chatbots) con AI COMPETITIVA EXTERNA (destruccion de demanda). Usar AI internamente no protege contra competidores AI. Es como decir "Kodak usa digital internamente" cuando la amenaza eran las camaras digitales reemplazando al film.

### 4.2 Donde el consenso BAJISTA se equivoca

1. **"AI reemplazara comparadores inminentemente"** — Insurify es solo EEUU, solo coches, no puede formalizar polizas, requiere suscripcion ChatGPT Plus. Es prueba de concepto, no competidor. La distancia de "cotizaciones de seguro de coche US en ChatGPT" a "comparacion multi-producto UK reemplazando el 96.7% de uso de PCWs" es ENORME.

2. **"MONY es como las Paginas Amarillas"** — Las Paginas Amarillas tenian cero efectos de red, cero ventaja de datos, cero switching costs. MONY tiene 5,000+ proveedores integrados con feeds de datos a medida, motores de pricing personalizados, frameworks de comparacion regulados por FCA. La analogia es perezosa.

3. **"P/E 9.7x sigue siendo caro"** — Para una empresa generando ROIC 31.8%, FCF margin 23%, net cash, 8.2% yield, creciendo incluso al 1-2%? A 9.7x earnings, solo el yield proporciona 10%+ de retorno antes de cualquier crecimiento. El mercado esta priciendo MONY para declive, no estancamiento.

4. **"El crash del 11% demuestra que el mercado sabe algo"** — El crash fue provocado por un producto americano (Insurify) que tiene cero operaciones en UK. Esto es contagio por narrativa, no por fundamentales. RBC y Berenberg notaron la sobre-reaccion. Cuando el trigger es una historia (no un fallo de resultados), la correccion del mercado suele ser excesiva.

5. **"El trafico bajando significa que el modelo esta muriendo"** — El trafico de Nov 2025 fue -8.82% MoM. Pero la variacion mensual de trafico para negocios estacionales es ruidosa. Los patrones de renovacion de seguros son ciclicos. Necesitamos datos YoY de multiples trimestres, no un dato mensual.

---

## PASO 5: Puedo Verificar con Datos Primarios?

### 5.1 Lo que SI puedo verificar

| Afirmacion | Metodo de Verificacion | Resultado |
|-----------|----------------------|----------|
| ROIC 31.8% >> WACC 9.2% | quality_scorer.py | **CONFIRMADO** — Financial quality 40/40 |
| FCF margin 23.1% | yfinance + datos thesis | **CONFIRMADO** — GBP 102m FCF sobre GBP 439m revenue |
| Posicion de net cash | Balance sheet | **CONFIRMADO** — 0.3x net debt/EBITDA |
| CEO compro a 170.6p 5 Feb | Disclosure regulatorio (PDMR) | **CONFIRMADO** — filing publico |
| Revenue seguros -2% H1 2025 | Filings de la compania | **CONFIRMADO** |
| Insurify es solo EEUU | Web de Insurify / filings regulatorios | **CONFIRMADO** — licencia en 50 estados US + DC |
| Reglas customer duty de FCA | FCA.org.uk | **CONFIRMADO** — Consumer Duty en vigor Jul 2023 |
| Crecimiento revenue 1-2% vs 5-7% reclamado | Filings de compania | **CONFIRMADO** — FY2024 +2% real |
| Margen bruto bajando | Filings de compania | **CONFIRMADO** — 70.4%(2021) → 66.2%(2024) |
| 96.7% consumidores UK usan PCWs | Informes del sector | **RECLAMADO** en thesis pero calidad de la fuente DESCONOCIDA |

### 5.2 Lo que NO puedo verificar (y que importa)

| Desconocido | Por Que Importa | Cuando Lo Sabremos |
|-------------|----------------|-------------------|
| Rendimiento segmento seguros H2 2025 | Kill condition clave | Resultados 23 Feb |
| Detalles estrategia AI del management | Trigger KC#9 | Earnings call 23 Feb |
| Tendencia actual trafico organico (Dic-Feb) | Valida/refuta afirmacion bajista | 23 Feb o Similarweb |
| Postura FCA sobre seguros mediados por AI | Determina durabilidad del moat regulatorio | Desconocido — FCA se mueve lento |
| Pipeline de MONY para integracion AI | Caso alcista depende de adaptacion | Earnings call 23 Feb |

### 5.3 Datos Primarios vs Datos Derivados

La mayor parte del caso alcista descansa en datos PRIMARIOS (ROIC, FCF, net cash, compra insider) — hechos verificables.
La mayor parte del caso bajista descansa en PROYECCIONES (AI disrumpira, trafico bajara, P/E se comprimira) — narrativas.

**Pero:** El caso bajista tiene un dato primario que importa: Insurify existe. Es real. Funciona (en EEUU). La cuestion es puramente sobre la velocidad de traduccion geografica/regulatoria.

---

## PASO 6: En Que Marco Temporal Se Resuelve?

### 6.1 Resolucion Corto Plazo (23 Feb 2026 — 8 dias)

**Los resultados resolveran:**
- Rendimiento segmento seguros H2 2025 (KC#1, KC#2)
- Estrategia AI del management (KC#9)
- Trayectoria crecimiento revenue FY2025
- Decision de dividendo
- Guidance futuro

**Si positivo:** Narrativa bajista se debilita, P/E podria recuperar a 11-13x = 180-210p (+22-43%)
**Si negativo:** Narrativa bajista se refuerza, caida adicional posible a 120-130p (-18%)

### 6.2 Resolucion Medio Plazo (6-18 meses)

**Se resolvera:**
- Si algun producto de comparacion de seguros AI se lanza en UK
- Direccion regulatoria de FCA sobre productos financieros mediados por AI
- Si las inversiones AI de MONY producen resultados visibles
- Cambios de comportamiento del consumidor UK (si los hay)

### 6.3 Resolucion Largo Plazo (3-5 anos)

**Se resolvera:**
- Si el modelo "comparison website" sobrevive como categoria
- Si MONY pivotea exitosamente a "motor de comparacion potenciado por AI"
- El destino final de PCWs vs agentes AI

### 6.4 Marco Temporal vs Valoracion de Posicion

Nuestra posicion es PEQUENA (3.2% del portfolio) y nuestro proximo dato es INMINENTE (8 dias). El riesgo temporal es BAJO — no necesitamos esperar anos para obtener informacion critica. Los resultados del 23 Feb validan o invalidan la decision de mantener.

---

## SENAL DE DIRECCION DE LA CONTRATHESIS

### Aplicando el Framework: Que direccion sugiere el analisis?

```
Paso 1: Consenso es BAJISTA (P/E 9.7x, minimo 13 anos, panico AI)
Paso 2: Cadena bajista tiene MAS eslabones fragiles (aprobacion FCA,
        transferencia confianza consumidor, diferencias mercado UK)
Paso 3: Narrativa bajista amplificada por actores ruidosos sin skin
        in the game en UK
Paso 4: Consenso bajista equivocado en inmediatez, en analogia Paginas
        Amarillas, en "MONY cara a 9.7x con 31.8% ROIC"
Paso 5: Datos primarios del caso alcista mas fuertes; caso bajista
        depende de proyecciones
Paso 6: Resolucion inminente (8 dias, resultados)

PERO:
Paso 2: Dependencia alcista tambien agrietada ("AI no puede replicar"
        — si puede)
Paso 4: Consenso alcista equivocado en crecimiento revenue (1-2% no
        5-7%), equivocado en "AI es oportunidad" (confunde AI interna
        con externa)
Paso 5: Margen bruto bajando 4 anos consecutivos — dato PRIMARIO

DIRECCION: LONG (contrario al consenso bajista)
CONVICCION: BAJA-MEDIA
```

**La contrathesis dice:** El mercado esta excesivamente bajista sobre MONY.L. La narrativa de disrupcion AI esta amplificada por actores con incentivo a amplificarla, mientras que los datos fundamentales (ROIC, FCF, net cash, compra insider) siguen fuertes. El caso bajista requiere que multiples dependencias fragiles (aprobacion FCA, cambio comportamiento consumidor, traduccion tecnologica) se rompan simultaneamente. Sin embargo, la amenaza DIRECCIONAL es real (Insurify prueba el concepto), asi que la conviccion no puede ser ALTA.

**Senal de Direccion: LONG CAUTELOSO — mantener hasta catalizador (resultados), con salida pre-definida si el catalizador falla.**

---

## COMPARACION: Que Encontro Nuestro Proceso Estandar vs Contrathesis?

### Cronologia de Nuestro Analisis Real

| Fecha | Version | Proceso | FV | Veredicto |
|-------|---------|---------|-----|-----------|
| 4 Feb | v1.0 | R1 estandar (fundamental-analyst) | 277 GBp | **BUY al 4%** |
| 7 Feb | v2.0 | Review adversarial (devil's-advocate) | 201 GBp (-27%) | **HOLD, conviccion BAJA** |
| 12 Feb | v3.0 | Re-eval disrupcion AI (review-agent) | 190 GBp (-5.5%) | **HOLD EN PROBATION** |

### Lo Que el Proceso Estandar Acerto

1. **v2.0 adversarial identifico correctamente la sobreestimacion de crecimiento** (1-2% real vs 5-7% asumido en v1.0). Exactamente lo que Paso 2 (cadena de dependencias) y Paso 4 (donde se equivoca el consenso) habrian encontrado.

2. **v3.0 distinguio correctamente la estructura del mercado UK del US** (barreras FCA, 96.7% penetracion PCW). Mapea a Paso 2 (fragilidad cadena bajista).

3. **v3.0 identifico correctamente la compra del CEO como senal alcista.** Mapea a Paso 3 (analisis de incentivos).

4. **v2.0 + v3.0 ajustaron correctamente kill conditions y crearon arbol de decisiones post-resultados.** Mapea a Paso 6 (resolucion temporal).

### Lo Que el Proceso Estandar FALLO (que la contrathesis habria pillado)

#### 1. El FV inicial de 277 GBp se baso en asunciones del consenso alcista, no en contrathesis

La thesis v1.0 empezo desde "es buena empresa?" → SI → "esta barata?" → SI → COMPRAR. Adopto la tasa de crecimiento del CONSENSO ALCISTA (5-7%) sin preguntar primero "que implica el precio actual?"

**Si hubieramos hecho reverse DCF primero:**
- Precio 169p implicaba ~0-1% crecimiento
- Crecimiento historico era ~2% (no 5-7%)
- El argumento "el consenso es demasiado bajista" habria sido mas debil
- FV habria estado mas cerca de 200-210 GBp desde el dia uno, no 277 GBp

**La caida 277→201→190 GBp a traves de tres versiones se habria evitado.** El framework de contrathesis habria empezado con expectativas implicitas, aterrizando cerca del FV adversarial inmediatamente.

#### 2. La contra-tesis "AI es oportunidad, no amenaza" fue acritica

v1.0 afirmo: "MONY usa AI para 60% de contactos con clientes = AI es oportunidad." Esto confundio AI OPERATIVA INTERNA con AI COMPETITIVA EXTERNA (analogia Kodak del Paso 4). El Paso 4 ("donde podria equivocarse el consenso?") aplicado a NUESTRA PROPIA thesis habria flaggeado inmediatamente: "Espera — usar AI internamente no protege contra competidores AI. Son cosas diferentes."

El adversarial review (v2.0) pillo esto pero DESPUES de haber comprado. El framework de contrathesis lo habria pillado ANTES de la decision de compra.

#### 3. El analisis de incentivos no existio en ninguna de las tres versiones

Ninguno de nuestros analisis pregunto: "Quien se beneficia de la narrativa AI-mata-PCWs?" o "Quien se beneficia de la narrativa PCW-es-resiliente?" El Paso 3 del framework de contrathesis revela que la narrativa bajista esta amplificada por empresas AI y medios tech sin skin in the game en UK. Es una senal util para calibrar la pregunta "que tan malo es esto realmente?"

#### 4. La caida del margen bruto se noto pero no se encadeno a su dependencia

v1.0 noto GM bajando (70.4% → 66.2%) pero lo puntuo como "0 puntos" en QS y siguio adelante. El Paso 2 habria preguntado:

```
"Margen bruto bajando 4 anos"
  ↓ Por que?
"Mayor competencia / presion de precios de proveedores"
  ↓ Que significa esto?
"Los proveedores tienen poder de negociacion sobre MONY"
  ↓ Que implica?
"El moat de efecto de red es mas debil de lo afirmado —
 los proveedores pueden presionar a MONY porque existen
 alternativas"
  ↓ Implicacion para la thesis?
"La evaluacion del moat (NARROW) podria ser generosa. Si
 los proveedores pueden apretar margenes, el moat
 proporciona menos poder de pricing de lo asumido."
```

Esto habria sido un argumento MAS FUERTE para menor puntuacion de moat que la etiqueta generica "narrow moat".

#### 5. El dato del 96.7% de penetracion PCW se uso sin critica

v3.0 cito "96.7% de consumidores UK usan PCWs para seguros" como evidencia de comportamiento arraigado. Pero el Paso 5 flaggea: **calidad de la fuente DESCONOCIDA.** Es auto-reportado por la industria PCW? Es actual? Mide "alguna vez usado" o "siempre usa"? La distincion importa enormemente. Nos apoyamos en este dato como pilar clave del caso alcista sin verificar su procedencia.

### Lo Que el Proceso Estandar Encontro que la Contrathesis TAMBIEN Habria Encontrado

- Sobreestimacion crecimiento revenue (v2.0 = Paso 2/Paso 4)
- Barreras regulatorias UK (v3.0 = Paso 2 cadena bajista)
- Senal compra insider (v3.0 = Paso 3)
- ROIC >> WACC como diferenciador clave (todas versiones = Paso 5)
- Resultados como resolucion cercana (todas versiones = Paso 6)

**El solapamiento es sustancial** — el proceso adversarial (v2.0, v3.0) acabo cubriendo ~60-70% de lo que el framework de contrathesis habria producido. Pero necesito TRES iteraciones para llegar ahi, y le falto el analisis de incentivos, el punto de partida de expectativas implicitas, y la conflacion AI interna/externa.

---

## EL CONTRAFACTUAL: Que Habria Cambiado?

### Si hubieramos aplicado el framework de contrathesis ANTES de comprar el 4 de Feb:

1. **Expectativas implicitas (reverse DCF)** habria mostrado que el mercado pricea 0-1% crecimiento. Nuestra asuncion de "5-7%" habria sido inmediatamente cuestionada. Habriamos usado 1-2% (la tasa real) como caso base desde el dia uno.

2. **FV habria sido ~190-210 GBp desde el inicio**, no 277 GBp. El MoS a 169p habria sido 11-19% (vs el 35-40% que calculamos). Esto es borderline para Tier A.

3. **Probablemente IGUAL HABRIAMOS COMPRADO** — 11-19% MoS para una empresa Tier A borderline con 31.8% ROIC esta dentro del rango de precedentes. Pero habriamos entrado con **EXPECTATIVAS MAS REALISTAS y MAYOR ALERTA** al riesgo AI.

4. **NO habriamos necesitado tres revisiones de thesis** (277→201→190). El overhead emocional e intelectual de revisar repetidamente a la baja es significativo. Empezar realista es mejor que empezar optimista y corregir.

5. **Podriamos haber dimensionado MAS PEQUENO** — sabiendo que el MoS era 11-19% (no 35-40%), podriamos haber empezado al 2-3% en vez de 4%. Esto habria reducido nuestra perdida actual de ~EUR 130 a ~EUR 65-100.

6. **La conflacion "AI es oportunidad" se habria pillado antes de comprar.** Este era el punto mas debil de la thesis v1.0 y paso sin cuestionar hasta v2.0 (3 dias despues de comprar).

### Evaluacion Neta

| Dimension | Proceso Estandar | Con Contrathesis | Delta |
|-----------|-----------------|-----------------|-------|
| FV inicial | 277 GBp | ~200 GBp | -28% (mas preciso) |
| MoS inicial | 35-40% | 11-19% | Mas realista |
| Decision compra | BUY 4% | BUY 2-3% (probable) | Menor perdida |
| Revisiones necesarias | 3 (v1.0→v2.0→v3.0) | 1 (quiza v1.5 post-Insurify) | Menos overhead |
| Evaluacion riesgo AI | "Oportunidad" (incorrecto) | "Amenaza a monitorizar" (correcto) | Mejor desde inicio |
| Veredicto actual | HOLD EN PROBATION | HOLD EN PROBATION | Mismo destino final |
| Preparacion resultados | Mismo framework | Mismo framework | Sin diferencia |

**El framework de contrathesis no habria cambiado el VEREDICTO FINAL** (HOLD hasta resultados, luego decidir). Pero nos habria llevado ahi MAS RAPIDO, con MENOS capital en riesgo, y con EXPECTATIVAS MAS PRECISAS desde el inicio.

El mayor valor anadido esta en la ENTRADA: evitar la compresion de Fair Value 277→190 GBp que forzó tres re-evaluaciones. Esta es la promesa central de la contrathesis: empezar desde lo que el PRECIO te dice, no desde lo que tu QUIERES que sea el valor.

---

## META-REFLEXION SOBRE LA SIMULACION

### Lo Que Este Ejercicio Revela Sobre Nuestro Sistema

1. **El adversarial review (R2/devil's advocate) esta haciendo ~60-70% de lo que el framework de contrathesis hace**, pero DESPUES de la decision de compra, no antes. Mover el analisis de contrathesis a ANTES de la decision de compra (como parte de R1) seria mas efectivo.

2. **El paso de reverse DCF es la aportacion individual de mayor valor.** Empezar desde "que asume el precio?" previene el sesgo de anclaje de construir un DCF desde nuestras propias asunciones y luego comparar con el precio. Nuestro FV v1.0 de 277 GBp fue exactamente este anclaje — construimos desde nuestras asunciones y obtuvimos un numero optimista.

3. **El analisis de incentivos es genuinamente novedoso** — ninguno de nuestros agentes pregunta actualmente "quien se beneficia de la narrativa actual?" Es un paso barato y rapido que anade senal util para calibrar movimientos de precio impulsados por narrativa (como el panico Insurify).

4. **La "conflacion Kodak" (AI interna vs AI externa) es un error sistematico** que el analisis de cadena de dependencias del framework de contrathesis pilla naturalmente. Cuando seguimos la cadena "MONY usa AI → por tanto AI es oportunidad," la cadena se rompe cuando preguntamos "espera, de QUE AI estamos hablando?"

5. **El framework de contrathesis NO reemplaza el pipeline existente.** Mejora el PUNTO DE ENTRADA (Paso 0 antes de R1) y fortalece el adversarial review existente (R2). Las 4 rondas, los agentes, los skills — todo sigue siendo necesario.

### Que Necesitaria Cambiar para Implementar Esto

Basado puramente en esta simulacion (no prescribiendo, solo observando):

1. **Anadir "Expectativas Implicitas" como Paso 0 de R1**: Antes de que el fundamental-analyst construya un caso alcista, calcular que asume el precio actual. Esto ancla el analisis a la realidad del mercado.

2. **Anadir "Analisis de Incentivos" al prompt del devil's advocate**: "Quien se beneficia del consenso actual? Quien se beneficia de tu thesis bajista? Estas siendo influido por actores con motivos ulteriores?"

3. **Anadir "Cadena de Dependencias" explicitamente al template de thesis**: No solo "riesgos" (que ya listamos) sino la cadena completa de conclusion → asuncion → dependencia → dato primario. Obliga al analista a trazar cada afirmacion hasta su raiz.

4. **Tool: `implied_expectations.py`** — Dado precio + FCF + historial de crecimiento, outputear que tasa de crecimiento implica el precio. Datos puros, sin juicio.

Estos 4 cambios son independientes de la decision de short selling. Mejoran el sistema long-only independientemente.

### Lo Que Este Ejercicio NO Demuestra

1. Que el framework de contrathesis habria prevenido la perdida — probablemente igualmente habriamos comprado, solo mas pequeno.
2. Que el proceso estandar esta roto — eventualmente llego a la misma conclusion via 3 iteraciones.
3. Que el framework de contrathesis previene todos los errores — es una lente, no una bola de cristal.
4. Que debamos implementar esto inmediatamente — es una simulacion, una empresa. Mas casos validarian.

---

## APENDICE: Scorecard de Calidad de Senal

Como de bien funciona cada paso del framework de contrathesis para MONY.L?

| Paso | Calidad | Comentario |
|------|---------|-----------|
| 1. Identificacion consenso | ALTA | Cambio alcista→bajista claramente identificable |
| 2. Cadenas de dependencias | ALTA | Ambos lados tienen cadenas claras y trazables |
| 3. Analisis de incentivos | ALTA | Desequilibrio claro (bajistas ruidosos, alcistas callados) |
| 4. Donde se equivoca el consenso | MEDIA | Ambos lados parcialmente equivocados, matizado |
| 5. Verificacion datos primarios | MEDIA-ALTA | Mayoria de afirmaciones verificables, algunas incognitas |
| 6. Marco temporal | ALTA | Catalizador inminente (resultados 23 Feb) |

**En conjunto: MONY.L es un CANDIDATO EXCELENTE para analisis contrathesis** porque:
- Cambio claro de consenso (alcista→bajista) proporciona dos contrathesis a testear
- Un evento concreto (Insurify) desencadeno el cambio, haciendo las cadenas de dependencias tangibles
- Un catalizador inminente (resultados) proporciona fecha para resolucion
- Ambos lados tienen afirmaciones verificables y falsificables

Un peor candidato seria una empresa cotizando "en consenso" sin tension narrativa — el framework de contrathesis es mas poderoso cuando hay un gap claro entre precio y valor para investigar.

---

*Simulacion completada: 2026-02-15*
*Este documento es solo para aprendizaje. No se han hecho cambios al sistema, portfolio ni state files.*
