# SHORT THESIS FRAMEWORK - Framework v4.0

> **Espejo del business-analysis-framework para analisis de fragilidad.**
> Obligatorio ANTES de valorar un short candidate.
> **NOTA v4.0:** Framework de razonamiento. No thresholds fijos.

---

## Proposito

Asi como business-analysis-framework es obligatorio antes de valorar un LONG,
este framework es obligatorio antes de valorar un SHORT.

La diferencia fundamental:
- Long: busco CALIDAD que el mercado infravalora
- Short: busco FRAGILIDAD que el mercado sobrevalora

---

## Seccion 0: Quality Score

**Mismo proceso que para longs:**
```bash
python3 tools/quality_scorer.py TICKER --detailed
```

**Interpretacion para shorts:**
- QS alto que cotiza como aun MAS alto → posible short (pero peligroso — empresa de calidad)
- QS bajo que cotiza como alto → short mas seguro (fragilidad + sobrevaloracion)
- QS bajo que cotiza como bajo → NO es short (mercado ya refleja fragilidad)

**La clave no es el QS absoluto — es el GAP entre QS real y QS implicito del precio.**

---

## Seccion 1: Por Que el Precio No Se Sostiene

**Preguntas obligatorias:**
1. Que narrativa sostiene el precio actual?
2. Es esa narrativa verificable con datos? (Filtro 3 del contrathesis)
3. Que tiene que seguir siendo verdad para que el precio se mantenga?
4. Hay precedentes historicos de esta narrativa fallando?

**Herramientas:**
```bash
python3 tools/dcf_calculator.py --reverse TICKER
python3 tools/narrative_checker.py TICKER
```

**Output esperado:** Articulacion clara de POR QUE el precio es insostenible, con datos que lo soporten.

---

## Seccion 2: Dependencia Oculta

**El ejercicio:** Cadena de "de que depende?" hasta llegar a un dato primario.

Ejemplo:
- "La empresa vale $300" → depende de crecimiento 15% anual
- Crecimiento 15% depende de → expansion en mercado X
- Expansion en mercado X depende de → regulacion favorable
- Regulacion favorable depende de → gobierno actual
- Gobierno actual depende de → elecciones en 6 meses

**Cada eslabon de la cadena es un punto de fragilidad potencial.**

**Preguntas:**
1. Cual es la dependencia MAS fragil de la cadena?
2. Que probabilidad tiene de romperse?
3. Si se rompe, cuanto impacta al precio?
4. El mercado tiene priced-in esta fragilidad?

---

## Seccion 3: Catalizador (Principio 10)

**OBLIGATORIO. Sin catalizador = NO shortear.**

**Preguntas:**
1. Que evento concreto forzara al mercado a reconocer la fragilidad?
2. Cuando ocurrira? (fecha o rango de fechas)
3. Es un evento binario (si/no) o gradual?
4. Que coste de carry acumulo hasta ese evento?
5. Si el catalizador se retrasa 6 meses, sigue siendo rentable?

**Tipos de catalizadores validos:**
- Earnings que revelaran deterioro (fecha conocida)
- Decision regulatoria (fecha conocida o estimable)
- Vencimiento de contratos / renegociacion (fecha conocida)
- Competencia lanzando producto disruptivo (fecha estimable)
- Investigacion / litigacion resolviendose (fecha estimable)

**Catalizadores NO validos:**
- "Eventualmente el mercado se dara cuenta" (no tiene fecha)
- "Algun dia la burbuja explotara" (no es especifico)
- "La empresa es mala" (eso no es catalizador)

---

## Seccion 4: Escenario Adverso (Principio 11)

**Preguntas:**
1. Si estoy equivocado, cuanto puede subir? Por que?
2. Hay riesgo de squeeze? (short interest alto + float bajo)
3. Hay evento binario que pueda subir 50%+ overnight? (FDA, M&A, earnings blowout)
4. Cual es el ratio beneficio esperado / perdida maxima razonable?
5. Es el ratio coherente con precedentes en decisions_log.yaml?

**Tool de soporte:**
```bash
python3 tools/insider_tracker.py TICKER  # short interest, institucionales
```

---

## Seccion 5: Kill Conditions para Cubrir

**Definir ANTES de abrir el short:**
- KC#1: [Evento que invalida thesis completamente]
- KC#2: [Mejora fundamental que no esperaba]
- KC#3: [Stop loss por precio]
- KC#4: [Carry acumulado supera umbral razonable]

**Cada kill condition tiene accion automatica:** CUBRIR (parcial o total).

---

## Seccion 6: Sizing y Mecanica

**Razonar desde P1 (Sizing) + P11 (Asimetria) + precedentes.**

- Instrumento: CFD short en eToro
- Leverage: razonar (x1-x2 como precedente base, consultar decisions_log)
- Sizing en EUR y % del portfolio
- Stop loss definido (no "mental" — documentado)
- Carry estimado: EUR/mes y % anual
- Carry total hasta catalizador: EUR total

**Ejecutar ANTES de decidir sizing:**
```bash
python3 tools/constraint_checker.py CHECK_SHORT TICKER AMOUNT
```

---

## Pipeline Short (S1-S4)

Espejo del buy-pipeline de 4 rondas:

```
S1: fundamental-analyst (--short-thesis) + moat-assessor + risk-identifier (PARALELO)
    → valuation-specialist (fair value del short)
    OUTPUT OBLIGATORIO: thesis/short/research/TICKER/thesis.md + moat_assessment.md + risk_assessment.md
S2: devil's-advocate (BULL case — por que el precio podria tener razon?)
    OUTPUT OBLIGATORIO: thesis/short/research/TICKER/s2_bull_case.md
S3: Resolucion de conflictos (orchestrator)
    OUTPUT OBLIGATORIO: thesis/short/research/TICKER/s3_resolution.md
S4: investment-committee (modo SHORT_APPROVAL — gates adaptados)
    OUTPUT OBLIGATORIO: thesis/short/research/TICKER/s4_committee.md

REGLA (Error #52): Cada ronda DEBE crear su archivo. NUNCA solo notas en watchlist.yaml.
```

**Gates adicionales en S4 para shorts:**
- Gate SHORT-1: Catalizador documentado con fecha (P10)
- Gate SHORT-2: Escenario adverso documentado con ratio (P11)
- Gate SHORT-3: Mejora portfolio total documentada (P12)

---

## Anti-Sesgo Short

- **Error #46:** "Esta cara" NO es thesis. Necesita fragilidad estructural.
- **Error #44:** Sin catalizador → NO shortear.
- **Error #47:** Leverage razonado desde principios, no desde "quiero ganar mas".
- Si empresa "me viene a la mente" como short → SESGO → validar con datos (same as Error #7 for longs)

---

**Ultima actualizacion:** 2026-02-18
**Framework version:** 4.0
