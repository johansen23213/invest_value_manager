# System Devil's Advocate

> Cadencia: Cada 4 semanas (alineado con macro-refresh pipeline)
> Trigger alternativo: Cuando el humano pregunta "¿qué está mal?"
> Ejecutor: devil's-advocate agent con prompt específico
> Output: state/system_challenge.md

---

## Propósito

El devil's-advocate agent cuestiona empresas individuales.
**Nadie cuestiona las asunciones del SISTEMA.**

Si las asunciones de base están sesgadas, todos los gates, tools y procesos
producen output sesgado: f(inputs_sesgados) = output_sesgado.

Este skill fuerza una revisión adversarial de las ASUNCIONES SISTÉMICAS,
no de empresas individuales.

---

## Las 5 Asunciones a Cuestionar

### 1. WORLD VIEW — "¿Mi visión del mundo es correcta?"

```
Leer world/current_view.md

Preguntas adversariales:
- ¿Qué asumo que es verdad y podría no serlo?
- ¿Qué narrativa estoy siguiendo sin cuestionar?
  (ej: "Europa está barata" → ¿merece descuento permanente?)
- ¿Qué evidencia me haría cambiar fundamentalmente de visión?
- ¿Cuándo fue la última vez que cambié de opinión sobre algo macro?
  Si >6 meses → sospechoso de confirmation bias

Herramienta: WebSearch para encontrar el MEJOR ARGUMENTO CONTRARIO
a cada posición del world view. No buscar confirmación — buscar refutación.
```

### 2. STRATEGY — "¿Quality compounder es la estrategia correcta?"

```
Preguntas adversariales:
- ¿Qué si "quality at reasonable price" está overcrowded?
  (Principio 9 dice gravitar hacia Tier A — ¿y si todo el mercado hace lo mismo?)
- ¿Qué ha hecho value vs quality en los últimos 12 meses?
  → WebSearch: "value vs quality factor performance 2025-2026"
- ¿Mi definición de "quality" (ROIC, FCF margin, moat) es la correcta?
  → ¿Hay empresas que compound sin ROIC alto? (asset-heavy compounders)
- Buffett no compraba a 25x P/E. ¿Estoy pagando de más por "quality"?

Herramienta: Ejecutar forward_return.py y comparar vs un portfolio
hipotético de deep value (P/E <8, yield >5%). Si deep value gana
consistentemente, cuestionar la estrategia.
```

### 3. SECTOR COVERAGE — "¿Qué estoy ignorando?"

```
Leer world/sectors/*.md — lista de sectores cubiertos.

Preguntas adversariales:
- ¿Qué sectores NO tengo sector view?
  → Glob("world/sectors/*.md") vs lista completa de GICS sectors
- ¿Por qué no? ¿Es razonado o es sesgo de familiaridad?
- ¿Asia? ¿Emerging Markets? ¿Commodities? ¿Energía no-oil?
  → Si la respuesta es "no los conozco bien" → ESO ES EL SESGO
- ¿Mi screening cubre suficiente? ¿Cuántos tickers he analizado vs universo?

Herramienta: dynamic_screener.py --index all --undiscovered
Si encuentro >20 empresas con QS >60 que nunca he mirado → coverage gap.
```

### 4. PORTFOLIO ASSUMPTIONS — "¿Mis posiciones realmente compound?"

```
Para CADA posición activa:

Preguntas adversariales:
- ¿ROIC ha mejorado o empeorado desde que compré?
  → quality_scorer.py TICKER --detailed (comparar vs thesis original)
- ¿El moat se ha ensanchado o estrechado?
- ¿Sigo teniendo ventaja informacional o el mercado ya ajustó?
- ¿Cuántas posiciones tengo por convicción vs por inercia?
  → Si conviction = LOW en >30% del portfolio → ¿por qué las tengo?

Herramienta: Batch quality_scorer.py para todas las posiciones.
Comparar QS actual vs QS en thesis. Si delta >5 puntos → investigar.
```

### 5. PROCESS — "¿El proceso produce buenos resultados?"

```
Preguntas adversariales:
- ¿Cuál es mi win rate REAL? (effectiveness_tracker.py)
- ¿Las mejoras que hago al sistema realmente mejoran resultados?
  → ¿Puedo medir antes/después de adversarial pipeline?
- ¿Estoy optimizando el proceso o el resultado?
  (Un proceso perfecto que pierde dinero es inútil)
- ¿Cuánto tiempo paso en mantenimiento vs en análisis que genera alpha?

Herramienta: effectiveness_tracker.py --summary
Si win rate <50% después de 20+ trades → el proceso necesita cambio fundamental.
```

---

## Protocolo de Ejecución

### Paso 1: Recopilar datos (30 min)
```
- Leer world/current_view.md
- Ejecutar forward_return.py
- Ejecutar effectiveness_tracker.py --summary
- Ejecutar quality_scorer.py para todas las posiciones (batch)
- Glob("world/sectors/*.md") para coverage
- WebSearch contrarian views a nuestro world view
```

### Paso 2: Lanzar devil's-advocate con prompt de sistema (30 min)
```
Task(subagent_type="devil's-advocate", prompt="""
SYSTEM CHALLENGE MODE — No estás cuestionando una empresa.
Estás cuestionando las ASUNCIONES DEL SISTEMA COMPLETO.

[Adjuntar datos del Paso 1]

Cuestiona las 5 áreas definidas en system-devils-advocate skill.
Para cada una:
1. ¿Cuál es la asunción?
2. ¿Qué evidencia la contradice?
3. ¿Cuál es el riesgo si la asunción es incorrecta?
4. ¿Qué cambiaría en el portfolio si fuera incorrecta?
5. Probabilidad de que la asunción sea incorrecta: [%]

Sé agresivo. No busques confirmar — busca REFUTAR.
""")
```

### Paso 3: Integrar (15 min)
```
Para cada asunción cuestionada:
- ¿Es válida la crítica? (SI/NO + por qué)
- Si SI → ¿Qué cambio hago? (inmediato)
- Si NO → ¿Por qué no? (documentar para no repetir la misma pregunta)

Output: state/system_challenge.md con fecha, hallazgos, acciones tomadas.
```

---

## Anti-Behavioral Guard

Para evitar que esto sea otro check que no se ejecuta:

1. **Integrado en pipeline system-health** (cada 14 días se recuerda,
   cada 4 semanas se ejecuta)
2. **El output (state/system_challenge.md) tiene fecha.**
   Si >35 días stale → health-check lo flagea como OVERDUE
3. **El humano puede trigger con "¿qué está mal?"**
   → Ejecutar inmediatamente, no diferir
4. **Mínimo output: 5 asunciones cuestionadas con evidencia.**
   Si el output es genérico ("todo bien") → re-ejecutar con más agresividad

---

## Cuándo NO ejecutar

- Si hay earnings esta semana (priorizar evaluación de posiciones)
- Si hay crisis de mercado activa (priorizar vigilancia)
- Si se acaba de ejecutar (<21 días)

---

## Primer Execution

La primera ejecución debería ocurrir en la próxima sesión que no tenga
earnings pendientes (post-Feb 26). Las 5 preguntas más urgentes HOY:

1. ¿"Europa barata" es real o es value trap regional?
2. ¿Quality compounder (25x P/E, ROIC 20%+) está overcrowded en 2026?
3. ¿Nuestro portfolio tiene 5 posiciones UK — es una concentración justificada?
4. ¿Las 5 posiciones en probation (ALL, VICI, GL, UHS, DTE.DE) son inercia?
5. ¿44% cash es prudencia o es parálisis de análisis?
