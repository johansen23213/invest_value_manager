---
name: error-detector
description: "Checklist automático ANTES de cada recomendación para evitar errores documentados"
user-invocable: false
---

# Error Detector Framework

## Propósito
Prevenir errores recurrentes mediante un checklist OBLIGATORIO antes de cualquier recomendación de inversión.

---

## Cuándo Ejecutar

**OBLIGATORIO antes de:**
- Recomendar BUY de nueva posición
- Recomendar ADD a posición existente
- Recomendar SELL/TRIM
- Aprobar standing order
- Presentar análisis al humano

---

## Checklist de Errores (TODOS deben pasar)

### 1. POPULARITY BIAS CHECK
```
[ ] ¿Encontré esta empresa mediante proceso SISTEMÁTICO?
    - Screening con dynamic_screener.py ✓
    - Sector view "Empresas Objetivo" ✓
    - Standing order pre-existente ✓

    ❌ FALLO si: "Se me ocurrió" / "Es famosa" / "La conozco"

    → Error #7, #29 en error-patterns.md
```

### 2. NEWS CHECK (48 HORAS)
```
[ ] ¿Verifiqué noticias de las últimas 48 horas?
    - news-monitor ejecutado ✓
    - WebSearch manual si no hay agente ✓

    ❌ FALLO si: No sé qué pasó esta semana con la empresa

    → Evita sorpresas tipo NVO
```

### 3. TIMING CONTEXT
```
[ ] ¿Puedo explicar POR QUÉ AHORA?
    - Qué evento creó la oportunidad
    - Hace cuánto ocurrió
    - Por qué el precio actual es atractivo

    ❌ FALLO si: No sé por qué está barata o qué cambió

    → Error nuevo: recomendaciones sin contexto temporal
```

### 4. CONSTRAINT CHECK
```
[ ] ¿Ejecuté constraint_checker.py?
    - Posición no superará 7%
    - Sector no superará 25%
    - Geografía no superará 35%
    - Cash no bajará de 5%

    ❌ FALLO si: No verifiqué o hay violación

    → Error #12 en error-patterns.md
```

### 5. QUALITY SCORE CHECK
```
[ ] ¿Quality Score calculado ANTES de valorar?
    - QS >= 35 (no Tier D)
    - MoS apropiado para el Tier

    ❌ FALLO si: No hay QS o es Tier D

    → Framework v3.0 regla #1 y #2
```

### 6. MULTI-METHOD VALUATION
```
[ ] ¿Usé al menos 2 métodos de valoración?
    - DCF + Comparables ✓
    - OEY + Reverse DCF ✓
    - NAV + DDM ✓

    ❌ FALLO si: Solo usé 1 método

    → Error #18 en error-patterns.md
```

### 7. WHY IS IT CHEAP
```
[ ] ¿Entiendo POR QUÉ está barata?
    - Razón documentada en thesis
    - Counter-thesis explicado
    - Value trap checklist completado

    ❌ FALLO si: "Está barata porque P/E bajo" sin más análisis

    → Error #16 en error-patterns.md
```

### 8. META-REFLECTION CHECK
```
[ ] ¿Leí META-REFLECTION del agente (si hubo)?
    - Dudas del agente respondidas
    - Sugerencias evaluadas
    - Anomalías investigadas

    ❌ FALLO si: Ignoré la sección META-REFLECTION

    → Nuevo error: no integrar reflexiones de agentes
```

### 9. SECTOR VIEW CHECK
```
[ ] ¿Existe sector view para esta empresa?
    - world/sectors/{sector}.md existe
    - Empresa documentada en el sector view

    ❌ FALLO si: No hay sector view

    → Error #30 en error-patterns.md
```

### 10. EARNINGS TIMING
```
[ ] ¿Hay earnings en los próximos 7 días?
    - Si SÍ: ¿Tengo framework de escenarios?
    - Si SÍ: ¿Es mejor esperar post-earnings?

    ❌ FALLO si: Earnings inminentes sin preparación

    → Error #13 en error-patterns.md
```

---

## Proceso de Ejecución

```
ANTES DE PRESENTAR RECOMENDACIÓN:

1. Abrir este skill mentalmente
2. Pasar por cada check (1-10)
3. Si ALGUNO falla:
   - STOP
   - Resolver el fallo
   - Volver a verificar
4. Solo si TODOS pasan → presentar recomendación

INCLUIR en la recomendación:
"Error-detector: 10/10 checks passed"
```

---

## Formato de Output

Cuando presento recomendación, incluir:

```markdown
### Pre-Recommendation Checks
| Check | Status |
|-------|--------|
| Popularity Bias | ✅ Found via screening |
| News 48h | ✅ Verified, no critical news |
| Timing Context | ✅ Opportunity from earnings miss |
| Constraints | ✅ Position 4.2%, within limits |
| Quality Score | ✅ QS 76, Tier A |
| Multi-Method | ✅ OEY + Reverse DCF |
| Why Cheap | ✅ Market overreacted to guidance |
| Meta-Reflection | ✅ Agent doubts addressed |
| Sector View | ✅ pharma-healthcare.md exists |
| Earnings Timing | ✅ No earnings next 7 days |
```

---

## Fallos Comunes y Cómo Evitarlos

| Error | Síntoma | Prevención |
|-------|---------|------------|
| Popularity bias | "Todos conocen X" | Verificar origen sistemático |
| News blindness | "No sabía que..." | news-monitor SIEMPRE primero |
| Context amnesia | "Compra X" sin más | Explicar timing obligatorio |
| Constraint violation | "Oops, superó 7%" | constraint_checker.py SIEMPRE |
| Tier D purchase | "Pero está muy barata" | QS ANTES de valorar |
| Single method | "DCF dice que..." | Mínimo 2 métodos |
| Value trap | "P/E 5x!" | Entender el POR QUÉ |
| Ignored reflection | "El agente dijo pero..." | Leer y responder META-REFLECTION |

---

## Regla de Oro

```
SI TENGO DUDA SOBRE ALGÚN CHECK → NO PASA

Mejor rechazar una buena oportunidad que aprobar una mala.
Los errores de omisión cuestan menos que los de comisión.
```
