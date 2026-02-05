# EXIT PROTOCOL - Framework v4.0

> **Proceso estructurado para decidir cuándo SALIR de una posición.**
> Más allá de kill conditions. Evalúa oportunidad-coste y mejor uso del capital.

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
4. **Cuando posición es "dead money"** (>12 meses sin progreso hacia FV)
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
    - Reducir posición 50%
    - Mover a "on probation" status
    - Re-evaluar en 90 días
- INVALIDADA → EXIT
```

### Gate 3: ¿MoS Actual?

```
Calcular MoS actual (precio actual vs Fair Value):

MoS = (Fair_Value - Precio_Actual) / Fair_Value × 100

RESULTADO:
- MoS < -20% (muy sobrevaluada):
    → TRIM al menos 50%
    → Considerar EXIT completo
    → Documentar razonamiento

- MoS entre -20% y 0% (sobrevaluada a fair):
    → HOLD pero NO ADD
    → Monitorear más frecuentemente
    → Preparar EXIT si sigue subiendo

- MoS > 0% (todavía hay upside):
    → No hay razón de vender por valoración
    → Continuar a Gate 4
```

### Gate 4: ¿Hay Mejor Oportunidad?

```
Comparar posición actual vs mejor candidato en watchlist.

CALCULAR OPPORTUNITY SCORE:

  OS = (MoS_candidato / MoS_actual) × (QS_candidato / QS_actual)

INTERPRETACIÓN:
- OS < 1.5   → Mantener posición actual
- OS 1.5-2.0 → Considerar rotación, depende del contexto
- OS > 2.0   → Rotación probablemente justificada
- OS > 2.5   → Rotación claramente justificada

EJEMPLO:
- Posición actual SHEL.L: MoS 5%, QS 36
- Candidato NVO: MoS 38%, QS 82
- OS = (38/5) × (82/36) = 7.6 × 2.28 = 17.3
- OS >> 2.0 → Rotación claramente justificada

NOTA: Considerar también correlación y diversificación.
Si el candidato aumenta concentración sectorial/geográfica,
el OS necesita ser mayor para justificar.
```

### Gate 5: ¿Dead Money?

```
Evaluar si la posición está "atrapada":

CRITERIOS para Dead Money:
1. >12 meses sin progreso hacia Fair Value
2. No hay catalizador identificado en próximos 6 meses
3. Hay alternativas con catalizadores claros

SI los 3 criterios se cumplen:
  → Considerar EXIT para liberar capital
  → Documentar razonamiento
  → El capital atrapado tiene coste de oportunidad

NOTA: "Dead money" no significa fracaso.
A veces el mercado tarda en reconocer valor.
Pero el capital tiene coste de oportunidad.
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

REGLA:
- Si fricción > 5% del valor → necesita OS > 2.5 para justificar
- Si fricción 2-5% → necesita OS > 2.0
- Si fricción < 2% → OS > 1.5 puede ser suficiente

EJEMPLO:
- Ganancia de 30% → impuesto ~7.5% (25% de 30%)
- Comisión 0.5%
- Spread 0.5%
- Fricción total = 8.5%
- Necesita OS muy alto (>3.0) para justificar rotación
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
    gate_3_mos_current: "X%"
    gate_4_opportunity_score: "X.X vs [candidato]"
    gate_5_dead_money: "NO / SÍ (tiempo atrapado)"
    gate_6_friction: "X%"

  recommendation: "HOLD / TRIM X% / EXIT"

  rationale: |
    Explicación del razonamiento que lleva a la recomendación.
    Referencias a principios y precedentes.

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
    gate_3_mos_current: "28%"
    gate_4_opportunity_score: "0.8 vs mejor candidato"
    gate_5_dead_money: "NO - comprada hace 1 día"
    gate_6_friction: "N/A - no vender"

  recommendation: "HOLD"
  rationale: |
    Tesis intacta, MoS positivo, no hay mejor oportunidad clara.
    No hay razón para vender.
```

### Ejemplo 2: TRIM (sobrevaluada)

```yaml
exit_analysis:
  ticker: XYZ
  date: 2026-XX-XX

  gates:
    gate_1_kill_condition: "NO"
    gate_2_thesis_valid: "INTACTA"
    gate_3_mos_current: "-15% (sobrevaluada)"
    gate_4_opportunity_score: "2.3 vs NVO"
    gate_5_dead_money: "NO"
    gate_6_friction: "3.2%"

  recommendation: "TRIM 50%"
  rationale: |
    Tesis intacta pero sobrevaluada (MoS negativo).
    Oportunidad mejor disponible (OS 2.3).
    Fricción moderada pero OS justifica.
    TRIM parcial mantiene exposición si sigue subiendo.
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

## Opportunity Score - Fórmula Detallada

```
OS = (MoS_nuevo / MoS_actual) × (QS_nuevo / QS_actual)

Donde:
- MoS = Margin of Safety (en %)
- QS = Quality Score (0-100)

AJUSTES:
- Si MoS_actual es negativo o cercano a 0, usar 5% como mínimo
- Si el candidato aumenta concentración sectorial >5%, reducir OS × 0.8
- Si el candidato aumenta exposición geográfica >5%, reducir OS × 0.9

EJEMPLO COMPLETO:
Posición actual SHEL.L:
  - Precio: 2800p
  - FV: 2940p
  - MoS: (2940-2800)/2940 = 4.8% ≈ 5%
  - QS: 36

Candidato NVO:
  - Precio: 48€
  - FV: 78€
  - MoS: (78-48)/78 = 38.5%
  - QS: 82

OS = (38.5/5) × (82/36) = 7.7 × 2.28 = 17.6

Interpretación: Rotación extremadamente justificada.
```

---

**Última actualización:** 2026-02-05
**Framework version:** 4.0
