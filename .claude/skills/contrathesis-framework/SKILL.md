# CONTRATHESIS FRAMEWORK - Framework v4.0

> **Framework unificado de 4 filtros + 6 preguntas para todo analisis (long y short).**
> Aplica ANTES de valoracion. Genera senales en AMBAS direcciones.
> **NOTA v4.0:** Tools = datos crudos. Este skill = framework de razonamiento.

---

## Proposito

Todo analisis — long o short — pasa por estos 4 filtros y 6 preguntas.
El framework NO decide la direccion. Genera la INFORMACION necesaria para que el analista razone.

---

## 4 Filtros

### Filtro 1: Que asume el precio y por que

**Tool:** `python3 tools/dcf_calculator.py --reverse TICKER`

**Preguntas:**
- Que tasa de crecimiento implica el precio actual?
- Es esa tasa coherente con el historico de la empresa?
- Es coherente con la dinamica del sector?
- La diferencia entre implicito e historico es por RAZON (datos macro reales, cambio estructural) o por EMOCION (miedo generico, hype)?

**Output del filtro:** Gap numerico entre expectativas implicitas vs razonables.

### Filtro 2: Quien opina y con que skin in the game

**Tool:** `python3 tools/insider_tracker.py TICKER`

**Preguntas:**
- Insiders estan comprando o vendiendo? (10b5-1 = ruido programado)
- Institucionales estan anadiendo o reduciendo?
- Cuanto le cuesta a esta persona estar equivocada?
- Ponderar por coste de equivocarse, NO por volumen de opiniones

**Output del filtro:** Quien tiene dinero real en juego y en que direccion.

### Filtro 3: Datos primarios confirman o contradicen la narrativa

**Tool:** `python3 tools/narrative_checker.py TICKER`

**Preguntas:**
- Si la narrativa dice "crecimiento acelerando", que dicen los deferred revenue?
- Si la narrativa dice "margen expandiendose", que dice el gross margin trend?
- Si la narrativa dice "investing for growth", R&D/revenue sube o baja?
- Receivables crecen mas rapido que revenue? (calidad de revenue)
- SBC/revenue subiendo? (dilucion oculta)

**Output del filtro:** Donde la narrativa diverge de los datos financieros.

### Filtro 4: Asimetria favorable

**NO requiere tool.** Razonamiento puro.

**Preguntas:**
- Cuanto pierdo si me equivoco vs cuanto gano si acierto?
- No necesito certeza. Necesito asimetria.
- Para longs: el downside esta limitado por activos tangibles, cashflow, etc?
- Para shorts: el upside adverso esta limitado por que? (valoracion, competencia, etc.)
- Ratio minimo razonable? Consultar precedentes en decisions_log.yaml.

**Output del filtro:** Ratio beneficio/riesgo y escenarios extremos.

---

## 6 Preguntas Complementarias

1. **Que cree el consenso?** (no solo analistas — el MERCADO, reflejado en precio)
2. **De que depende esa creencia?** (cadena de dependencias hasta dato primario verificable)
3. **Quien tiene incentivo a mantenerla?** (management, analistas sell-side, fondos con posicion)
4. **Donde podria estar equivocado el consenso?** (el punto de no-consenso)
5. **Puedo verificar con datos primarios?** (no opiniones — datos)
6. **En que marco temporal se resuelve?** (earnings, regulacion, competencia, catalizador)

---

## Matriz de Decision

| Consenso equivocado a la baja | → Senal LONG |
| Consenso equivocado al alza | → Senal SHORT |
| Consenso tiene razon | → NO OPERAR |
| No tengo informacion suficiente | → INVESTIGAR MAS |

**IMPORTANTE:** La senal NO es suficiente para operar. Pasa al pipeline correspondiente (buy-pipeline o short-pipeline) para validacion completa.

---

## Integracion con Otros Skills

- **business-analysis-framework:** Seccion 0.5 invoca este framework
- **short-thesis-framework:** Seccion 9 documenta los 4 filtros
- **pre-execution-check:** Gate 5 usa Filtro 1 (reverse DCF) para revalidar
- **investment-committee:** Evalua si los 4 filtros fueron completados

---

## Anti-Sesgo

- Los 3 tools (reverse DCF, insider, narrative) producen DATOS CRUDOS
- Este skill provee PREGUNTAS, no respuestas
- Si la conclusion "me parece obvia" sin completar los 4 filtros → es sesgo
- Filtro 2 (skin in the game) es especificamente anti-popularidad

---

**Ultima actualizacion:** 2026-02-18
**Framework version:** 4.0
