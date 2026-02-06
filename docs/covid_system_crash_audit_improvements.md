# Plan de Mejoras Post-Audit COVID

> **Fecha:** 2026-02-06
> **Basado en:** docs/covid_system_crash_audit.md
> **Objetivo:** Que el sistema pase de C+ a A- ante el proximo crash

---

## Resumen: 8 Mejoras Priorizadas

| # | Mejora | Prioridad | Esfuerzo | Impacto en Crash |
|---|--------|-----------|----------|-----------------|
| 1 | Crisis Protocol Skill | CRITICA | Alto | Reduce drawdown -5pp, mejora recovery +15pp |
| 2 | Standing Order Circuit Breaker | CRITICA | Bajo | Evita -40% en ordenes ejecutadas en caida |
| 3 | Cash Reserve con Valor de Opcion | ALTA | Medio | Permite comprar en bottom (+15-20pp retorno) |
| 4 | Sector Vulnerability Matrix | ALTA | Medio | Triage instantaneo, vender vulnerable antes |
| 5 | Stress Testing Tool | MEDIA | Alto | Anticipa drawdown maximo, identifica debilidades |
| 6 | Tail Correlation Modeling | MEDIA | Medio | No sobreestimar diversificacion |
| 7 | Comunicacion de Crisis al Humano | ALTA | Bajo | Previene override emocional |
| 8 | Market Regime Detector | MEDIA | Alto | Automatiza deteccion de crisis |

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
  # Condicion global de mercado para TODOS los standing orders
  circuit_breaker:
    active: false  # Se activa automaticamente cuando:
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
      # NUEVO: Condiciones de validez
      valid_when:
        market_regime: "NORMAL or ESTRES"  # NO en CRISIS o PANICO
        vix_below: 35
      notes: "SUSPENDIDO automaticamente si circuit breaker activo"
```

### Protocolo de re-activacion

```
Cuando circuit breaker se desactiva (VIX <35, mercado estabiliza):

1. Revisar CADA standing order:
   - Sigue la tesis siendo valida post-crisis?
   - El trigger price sigue siendo correcto? (pueden haber cambiado fundamentales)
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

## MEJORA 3: Cash Reserve con Valor de Opcion (ALTA)

### Problema que resuelve
El Principio 4 actual incentiva desplegar cash. No contempla el VALOR DE OPCION del cash para tail events.

### Propuesta: Enriquecer Principio 4

**Adicion a learning/principles.md, Principio 4:**

```markdown
## Adicion: Valor de Opcion del Cash

El cash tiene DOS funciones:
1. COSTE: Drag de retorno en mercados normales (~3-5% anual)
2. OPCION: Capacidad de comprar quality en crashes (valor potencial: +50-100%)

Pregunta guia adicional:
"Si manana el mercado cae 30%, tengo suficiente cash para comprar al menos
2-3 quality compounders a precios generacionales?"

Razonamiento:
- Crashes >20% ocurren cada ~7-10 anos
- El retorno de comprar quality en crash supera ampliamente el drag de mantener cash
- No se trata de "timing the market" sino de "tener la opcion de actuar"
- El cash minimo razonable para tail events no tiene un numero fijo,
  pero deberia ser suficiente para al menos 2-3 posiciones nuevas
```

### No es una regla ("mantener siempre X% cash")

Es un principio: "Al razonar sobre cash, considerar no solo oportunidades actuales sino tambien el valor de opcion para eventos extremos."

En la practica, esto podria significar:
- En mercados caros con pocas oportunidades: cash alto es doblemente justificado
- En mercados baratos con muchas oportunidades: cash bajo es aceptable porque ya estas comprando quality barato
- En mercados normales: un buffer adicional razonado por valor de opcion

### Implementacion

1. Enriquecer Principio 4 en learning/principles.md
2. Documentar como precedente en decisions_log.yaml
3. constraint_checker.py puede mostrar "capacidad de compra en escenario -30%"

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
[Tabla similar: bancos, real estate vulnerables; staples, healthcare resilientes]

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

## MEJORA 5: Stress Testing Tool (MEDIA)

### Problema que resuelve
No sabemos cuanto cae nuestro portfolio en diferentes escenarios. Los calculos son ad-hoc.

### Diseno propuesto

**Tool:** `tools/stress_test.py`

```bash
python3 tools/stress_test.py --scenario covid       # Simula COVID crash en portfolio actual
python3 tools/stress_test.py --scenario gfc          # Simula 2008 GFC
python3 tools/stress_test.py --scenario uniform -20   # Caida uniforme del 20%
python3 tools/stress_test.py --scenario sector tech -30  # Tech cae 30%, resto -10%
python3 tools/stress_test.py --all                    # Todos los escenarios
```

**Output:**
```
STRESS TEST: COVID-19 Scenario
================================
Portfolio Pre-Stress:  €11,186
Portfolio Post-Stress: €7,830  (-30.0%)
Cash Available:        €790 (post-stress: 10.1% of portfolio)
Max Single Position Loss: TEP.PA -€362 (50% drop)
Tier A Recovery (est):  3-5 months
Tier B Recovery (est):  6-12 months
Tier C Recovery (est):  12-24 months

POSITIONS BY IMPACT:
  VULNERABLE:   EDEN.PA (-50%), VICI (-45%), SHEL.L (-40%)
  MODERATE:     VNA.DE (-30%), TEP.PA (-35%), A2A.MI (-25%)
  RESILIENT:    DTE.DE (-15%), PFE (-20%), IMB.L (-15%)
  BENEFICIARY:  ADBE (-10% then +30%), DOM.L (-5% then +20%)

CAPACITY TO BUY AT BOTTOM: €790 = 1.5 new positions (insuficiente)
RECOMMENDATION: Consider raising cash buffer by €800-1200
```

### Implementacion

1. Delegar a quant-tools-dev agent
2. Escenarios basados en datos historicos de sector drawdowns
3. Usar betas sectoriales para estimar caida por posicion
4. Ejecutar mensualmente o ante cambios de portfolio

---

## MEJORA 6: Tail Correlation Modeling (MEDIA)

### Problema que resuelve
correlation_matrix.py usa correlaciones normales (~0.11). En crashes, correlaciones van a ~0.9. No modelamos esto.

### Propuesta

**Enriquecer correlation_matrix.py** (o nuevo tool) para calcular:
1. Correlaciones normales (actual)
2. Correlaciones en periodos de estres historico (nuevo)
3. "Diversification benefit under stress" (nuevo)

```bash
python3 tools/correlation_matrix.py --stress     # Calcula correlaciones en periodos de crisis
python3 tools/correlation_matrix.py --compare     # Normal vs Stress side by side
```

**Ejemplo output:**
```
CORRELATION ANALYSIS
                    Normal    Stress(COVID)    Stress(GFC)
Avg Correlation:    0.11      0.78             0.82
Diversification:    60.9%     12.3%            9.1%
Effective Positions: 18.2     4.3              3.5
```

**Insight clave:** "En crisis, tu portfolio de 21 posiciones se comporta como si tuviera 4."

### Implementacion

1. Delegar a quant-tools-dev
2. Usar datos historicos de COVID (Feb-Mar 2020) y GFC (Sep-Nov 2008)
3. Calcular correlaciones usando solo periodos de estres

---

## MEJORA 7: Comunicacion de Crisis al Humano (ALTA)

### Problema que resuelve
En un crash de -30%, el humano esta bajo presion emocional extrema. Puede override las recomendaciones de Claude y vender en panico.

### Propuesta: Pre-briefing de Crisis

**Crear ahora, antes de que haya crisis, un documento que el humano pueda leer:**

**Archivo:** `docs/crisis_playbook_for_human.md`

**Contenido:**
1. "Que va a pasar cuando el mercado caiga 20-30%"
2. "Por que NO vamos a vender en panico"
3. "Que SI vamos a hacer (triage, liberar cash, comprar quality)"
4. "Que emociones vas a sentir y por que son normales"
5. "Si sientes urgencia de vender TODO, lee esta seccion primero"
6. "Historicamente, vender en panico es la peor decision posible"
7. "Nuestro plan especifico para cada fase del crash"

### Implementacion

1. Escribir docs/crisis_playbook_for_human.md
2. El humano lo lee AHORA, en calma, no durante el panico
3. Actualizar cada vez que cambia el portfolio significativamente
4. Referenciarlo en crisis-protocol skill

---

## MEJORA 8: Market Regime Detector (MEDIA)

### Problema que resuelve
Detectar automaticamente en que regimen de mercado estamos para activar el crisis protocol.

### Propuesta

**Enriquecer market-pulse agent** con deteccion de regimen:

```
Al inicio de cada sesion, market-pulse reporta:

MARKET REGIME: NORMAL | ESTRES | CRISIS | PANICO

Basado en (datos, no reglas fijas):
- VIX actual y tendencia
- Drawdown desde peak reciente
- Breadth del mercado (cuantos valores suben vs bajan)
- Spread credito (investment grade vs high yield)
- Volatilidad realizada vs implicita
```

**Integracion:**
- Si regimen >= ESTRES → crisis-protocol se activa automaticamente
- Si regimen >= CRISIS → circuit breaker de standing orders
- Reportar al orchestrator con datos crudos + clasificacion orientativa

### Implementacion

1. Agregar seccion de regime detection a market-pulse agent
2. Puede usar VIX como proxy principal (disponible via yfinance: ^VIX)
3. Reportar en state/market_pulse.yaml

---

## Roadmap de Implementacion

### Fase 1: Inmediata (esta sesion o proxima)

| # | Mejora | Tipo | Effort |
|---|--------|------|--------|
| 7 | Crisis playbook para humano | Documento | 1 hora |
| 2 | Standing order circuit breaker | Config system.yaml | 30 min |
| 3 | Enriquecer Principio 4 | Editar principles.md | 15 min |

### Fase 2: Corto plazo (proximas 2-3 sesiones)

| # | Mejora | Tipo | Effort |
|---|--------|------|--------|
| 1 | Crisis Protocol Skill | Skill nuevo | 2 horas |
| 4 | Sector Vulnerability Matrix | Documento nuevo | 1 hora |
| 8 | Market Regime en market-pulse | Editar agente | 1 hora |

### Fase 3: Medio plazo (proximas 4-6 sesiones)

| # | Mejora | Tipo | Effort |
|---|--------|------|--------|
| 5 | Stress Testing Tool | Tool Python nuevo | 3 horas |
| 6 | Tail Correlation Modeling | Tool Python mejorado | 2 horas |

---

## Impacto Esperado

### Sin mejoras (actual)
```
Proximo crash tipo COVID:
  Max drawdown: -36%
  Recovery time: 12 meses
  Retorno 12 meses: +4.5%
  Oportunidad perdida: ~€2,000 en quality no comprada en bottom
```

### Con mejoras implementadas
```
Proximo crash tipo COVID:
  Max drawdown: -28 a -30% (reducido por triage + cash)
  Recovery time: 6-8 meses
  Retorno 12 meses: +15 a +20%
  Capital desplegado en bottom: €1,500-2,000 en quality compounders
```

### Diferencia
```
Drawdown: -6 a -8pp mejor
Recovery: 4-6 meses mas rapido
Retorno 12m: +10 a +15pp mejor
En euros: ~€1,500-2,000 de diferencia en portfolio de €11K
```

---

## Meta-Reflexion

### Lo que este ejercicio revela sobre el sistema

1. **El sistema es bueno para mercados normales, fragil para tail events.** Esto es comun en sistemas de inversion, pero podemos mejorarlo.

2. **La mayor debilidad no es analitica, es operativa.** Sabemos que no debemos panic sell (Principio 6). Pero no tenemos el CASH para comprar en bottom, ni el PROCESO para actuar rapido.

3. **Framework v4.0 (principios > reglas) es MEJOR para crisis que v3.0.** Las reglas se rompen en crisis. Los principios se adaptan. Pero los principios solos no bastan; necesitan un framework operativo de crisis.

4. **El eslabon mas debil es el humano, no el sistema.** Prepararle emocionalmente AHORA es critico.

5. **Cash no es "dinero parado". Es una opcion de compra sobre el futuro.** Esta es quizas la leccion mas importante de todo el audit.

---

**Autor:** Claude (Orchestrator)
**Framework:** v4.0
**Fecha:** 2026-02-06
**Relacionado:** docs/covid_system_crash_audit.md
