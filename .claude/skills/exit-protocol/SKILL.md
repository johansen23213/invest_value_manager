# EXIT PROTOCOL - Framework v4.0

> **Proceso estructurado para decidir cuándo SALIR de una posición.**
> Más allá de kill conditions. Evalúa oportunidad-coste y mejor uso del capital.
> **NOTA v4.0:** Este protocolo provee FRAMEWORK de razonamiento, no thresholds fijos.

---

## Propósito

v3.0 tenía:
- ENTRY: 9 gates rigurosos
- MONITORING: Vigilancia continua
- TRIM: Solo por reglas mecánicas o kill conditions
- **EXIT estratégico: NO EXISTÍA**

v4.0 añade este protocolo para responder:
> "¿Debería salir de esta posición para poner el capital en algo mejor?"

---

## Cuándo Ejecutar Este Protocolo

1. **Review trimestral** de cada posición
2. **Post-earnings** que cambien la narrativa
3. **Cuando hay oportunidad claramente mejor** en watchlist
4. **Cuando posición parece "dead money"** (sin progreso significativo)
5. **Cuando contexto macro cambia** materialmente
6. **Cuando el orchestrator lo solicite** para posición específica

---

## Los 6 Gates del EXIT Protocol

```
┌─────────────────────────────────────────────────────────────────┐
│                    EXIT PROTOCOL v4.0                           │
│                                                                 │
│  GATE 1 → GATE 2 → GATE 3 → GATE 4 → GATE 5 → GATE 6           │
│   Kill     Tesis    MoS     Mejor    Dead    Fricción          │
│  Condition Válida  Actual  Oport.   Money                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Gate 1: ¿Kill Condition Activada?

```
Verificar kill conditions documentadas en thesis.

SI alguna kill condition se activa:
  → EXIT inmediato
  → No necesita más análisis
  → Documentar en decisions_log

EJEMPLOS de kill conditions:
- Management fraud/misalignment
- Pérdida permanente de ventaja competitiva
- Deterioro estructural del negocio
- Regulación que destruye el modelo
```

### Gate 2: ¿Tesis Todavía Válida?

```
Verificar la tesis original vs. realidad actual:

[ ] ¿El negocio sigue siendo el mismo?
[ ] ¿Las ventajas competitivas persisten?
[ ] ¿El management sigue alineado?
[ ] ¿Los fundamentales mejoran o empeoran?

RESULTADO:
- INTACTA → Continuar a Gate 3
- DEBILITADA (pero no kill condition) →
    - Considerar reducir exposición (cuánto depende del contexto)
    - Mover a "on probation" status
    - Definir timeline para re-evaluación
- INVALIDADA → EXIT
```

### Gate 3: ¿MoS Actual?

```
Calcular MoS actual (precio actual vs Fair Value):

MoS = (Fair_Value - Precio_Actual) / Fair_Value × 100

PREGUNTAS GUÍA (no thresholds fijos):

1. ¿El MoS actual justifica mantener la posición?
   - MoS muy negativo sugiere sobrevaluación
   - Pero: ¿la tesis sigue intacta? ¿Hay catalizadores?

2. ¿Qué hice en precedentes similares?
   - Consultar decisions_log.yaml
   - ¿Por qué este caso sería diferente?

3. ¿Cuál es el coste de oportunidad?
   - Si hay MoS negativo pero no hay mejor alternativa → HOLD puede ser correcto
   - Si hay alternativas con MoS positivo → evaluar en Gate 4

RESULTADO:
- MoS claramente negativo + mejor alternativa clara → Continuar a Gate 4
- MoS negativo pero tesis fuerte + sin alternativas → HOLD, monitorear
- MoS positivo → No hay urgencia de salir por valoración
```

### Gate 4: ¿Hay Mejor Oportunidad? (Opportunity Score)

```
Comparar posición actual vs mejor candidato en watchlist.

CALCULAR OPPORTUNITY SCORE:

  OS = (MoS_candidato / MoS_actual) × (QS_candidato / QS_actual)

INTERPRETACIÓN CUALITATIVA (no thresholds rígidos):

- OS cercano a 1: No hay mejora significativa
- OS moderadamente mayor que 1: Mejora marginal, considerar costes de rotación
- OS significativamente mayor que 1: Rotación probablemente justificada
- OS muy alto: Rotación claramente justificada

PREGUNTAS GUÍA:
1. ¿La mejora en OS justifica la fricción de rotación?
2. ¿Hay precedentes de rotaciones similares? ¿Cómo resultaron?
3. ¿La rotación aumenta concentración de riesgo?

AJUSTES CUALITATIVOS:
- Si el candidato aumenta concentración sectorial significativamente → más exigente
- Si el candidato diversifica el portfolio → menos exigente
- Considerar correlación con otras posiciones

DOCUMENTAR: El razonamiento específico, no solo el número.
```

### Gate 5: ¿Dead Money?

```
Evaluar si la posición está "atrapada":

PREGUNTAS GUÍA (no criterios rígidos):

1. ¿Cuánto tiempo lleva sin progreso hacia Fair Value?
   - Más tiempo no es automáticamente malo
   - Value investing requiere paciencia
   - Pero el capital tiene coste de oportunidad

2. ¿Hay catalizadores identificables en el horizonte?
   - Earnings, nuevo producto, cambio regulatorio, etc.
   - Si no hay catalizador visible, ¿por qué cambiaría la situación?

3. ¿Hay alternativas con catalizadores claros?
   - Si hay mejor uso del capital, considerar rotación
   - Si no hay, paciencia puede ser correcta

NOTA: "Dead money" no significa fracaso.
A veces el mercado tarda en reconocer valor.
El juicio es sobre coste de oportunidad, no sobre la tesis.
```

### Gate 6: Fricción de Salida

```
ANTES de ejecutar EXIT, calcular costes:

COMPONENTES DE FRICCIÓN:
- Impuestos sobre ganancias (si aplica)
- Comisiones de venta
- Spread bid-ask (especialmente en small caps)
- Impacto en diversificación del portfolio

CÁLCULO:
Fricción_Total = Impuestos + Comisiones + Spread

RAZONAMIENTO:
- A mayor fricción, el Opportunity Score necesita ser mayor
- No hay fórmula fija - depende del contexto
- Documentar el razonamiento explícito

PREGUNTAS:
1. ¿El beneficio esperado de la rotación supera claramente la fricción?
2. ¿Qué hice en casos similares con fricción comparable?
3. ¿Hay forma de reducir fricción? (timing, sizing parcial)
```

---

## Output del Protocolo

Después de ejecutar los 6 gates, documentar:

```yaml
exit_analysis:
  ticker: XXX
  date: YYYY-MM-DD

  gates:
    gate_1_kill_condition: "NO / SÍ (cuál)"
    gate_2_thesis_valid: "INTACTA / DEBILITADA / INVALIDADA"
    gate_3_mos_current: "X% - [razonamiento sobre si justifica acción]"
    gate_4_opportunity_score: "X.X vs [candidato] - [razonamiento]"
    gate_5_dead_money: "NO / SÍ - [razonamiento sobre tiempo y catalizadores]"
    gate_6_friction: "X% - [razonamiento sobre si OS lo justifica]"

  recommendation: "HOLD / TRIM / EXIT"

  rationale: |
    Explicación del razonamiento que lleva a la recomendación.
    Referencias a principios y precedentes.
    Por qué este caso es similar o diferente a precedentes.

  precedents_consulted:
    - "[ticker] - [situación similar] - [decisión tomada] - [resultado]"

  alternative_considered: "La otra opción considerada"
  why_not_alternative: |
    Por qué no se eligió la alternativa.
```

---

## Ejemplos de Uso

### Ejemplo 1: HOLD (tesis intacta, MoS positivo)

```yaml
exit_analysis:
  ticker: ADBE
  date: 2026-02-05

  gates:
    gate_1_kill_condition: "NO"
    gate_2_thesis_valid: "INTACTA - Creative Cloud sigue dominando"
    gate_3_mos_current: "28% - significativo upside, no hay urgencia de salir"
    gate_4_opportunity_score: "0.8 vs mejor candidato - no hay mejora"
    gate_5_dead_money: "NO - comprada hace 1 día"
    gate_6_friction: "N/A - no vender"

  recommendation: "HOLD"
  rationale: |
    Tesis intacta, MoS positivo, no hay mejor oportunidad clara.
    No hay razón para vender.
```

### Ejemplo 2: EXIT por Oportunidad Claramente Mejor

```yaml
exit_analysis:
  ticker: SHEL.L
  date: 2026-02-05

  gates:
    gate_1_kill_condition: "NO"
    gate_2_thesis_valid: "INTACTA pero débil - Q4 miss, FCF cayendo"
    gate_3_mos_current: "5% - casi fair value, poco upside"
    gate_4_opportunity_score: "17.6 vs NVO - diferencia extrema"
    gate_5_dead_money: "Parcialmente - 3 semanas sin progreso"
    gate_6_friction: "~2% - bajo vs beneficio potencial"

  recommendation: "EXIT para rotar a NVO"
  rationale: |
    El OS de 17.6 indica oportunidad dramáticamente mejor.
    Tesis SHEL.L debilitada post-earnings.
    Fricción de 2% es insignificante vs MoS de 38% en NVO.

  precedents_consulted:
    - "No hay precedente directo de rotación tan clara"
    - "Primer caso de aplicar EXIT Protocol formalmente"
```

### Ejemplo 3: EXIT (kill condition)

```yaml
exit_analysis:
  ticker: ABC
  date: 2026-XX-XX

  gates:
    gate_1_kill_condition: "SÍ - Management fraud revelado"
    gate_2_thesis_valid: "N/A - kill condition activa"
    gate_3_mos_current: "N/A"
    gate_4_opportunity_score: "N/A"
    gate_5_dead_money: "N/A"
    gate_6_friction: "N/A - EXIT obligatorio"

  recommendation: "EXIT 100% INMEDIATO"
  rationale: |
    Kill condition activada. No hay análisis adicional necesario.
    EXIT aunque haya pérdida - mejor pérdida pequeña ahora que grande después.
```

---

## Integración con Sistema

- **Quién ejecuta:** review-agent (con flag --exit-analysis) o orchestrator directamente
- **Output:** Documentar en thesis/active/{ticker}/exit_analysis.md
- **Si recomendación es EXIT:** Pasa a investment-committee para aprobación
- **Después de EXIT:** Mover thesis a archive/, registrar en decisions_log

---

## Opportunity Score - Fórmula

```
OS = (MoS_nuevo / MoS_actual) × (QS_nuevo / QS_actual)

Donde:
- MoS = Margin of Safety (en %)
- QS = Quality Score (0-100)

MANEJO DE CASOS ESPECIALES:
- Si MoS_actual es negativo o cercano a 0:
  → El denominador pequeño amplifica OS
  → Esto es CORRECTO: indica que hay poco que perder
  → Pero razonar cualitativamente, no solo confiar en el número

EJEMPLO:
Posición actual SHEL.L:
  - MoS: 5%, QS: 36
Candidato NVO:
  - MoS: 38%, QS: 82

OS = (38/5) × (82/36) = 7.6 × 2.28 = 17.3

Este OS muy alto indica diferencia extrema.
Pero SIEMPRE documentar el razonamiento, no solo el número.
```

---

## Principio Central

**El EXIT Protocol es un FRAMEWORK de razonamiento, no una calculadora automática.**

Los números (OS, MoS, fricción) son INPUTS para razonar.
La decisión viene del RAZONAMIENTO documentado.
Consultar `learning/decisions_log.yaml` para precedentes.
Documentar por qué este caso es similar o diferente.

---

**Última actualización:** 2026-02-05
**Framework version:** 4.0
