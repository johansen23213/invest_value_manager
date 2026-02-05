# Framework v4.0 - Evolution Design Document (ÍNDICE)

> **PARA MI YO FUTURO (Claude):**
> Este documento es el ÍNDICE de la evolución v4.0.
> Contiene DOS propuestas que evolucionaron durante la conversación.
> LEE ESTE ÍNDICE PRIMERO para entender el contexto completo.

---

## ESTRUCTURA DE DOCUMENTOS

```
docs/
├── evolution_framework_4.0.md              ← ESTE DOCUMENTO (índice)
├── evolution_framework_4.0_v1_parameters.md ← Propuesta 1: Parámetros Condicionales
└── evolution_framework_4.0_v2_principles.md ← Propuesta 2: Principios + Precedentes (RECOMENDADA)
```

---

## RESUMEN EJECUTIVO

### La Conversación (Sesión 37, 2026-02-05)

El humano cuestionó fundamentalmente cómo opera el sistema:

1. **¿Tenemos protocolo EXIT?** → No, solo kill conditions
2. **¿Vendemos solo porque >7%?** → Sí, y eso es absurdo
3. **¿Las reglas son bias?** → Sí, son parámetros arbitrarios
4. **¿El sistema necesita reglas fijas?** → Pregunta filosófica profunda

### Evolución del Pensamiento

```
PROBLEMA IDENTIFICADO:
v3.0 tiene 23 parámetros hardcodeados arbitrarios (7%, 35%, 25%, etc.)
que aplico mecánicamente sin cuestionar.

PROPUESTA 1 (v1_parameters.md):
"Parámetros Condicionales" - Centralizar parámetros en parameters.yaml
con justificaciones y condiciones de override.

CUESTIONAMIENTO DEL HUMANO:
"Siguen siendo parámetros fijos... ¿realmente necesitas ficheros con reglas?"

REFLEXIÓN PROFUNDA:
Buffett no tiene max_position.yaml. Tiene principios internalizados
y experiencia (precedentes). Yo no tengo memoria entre sesiones,
pero puedo tener principios + precedentes documentados.

PROPUESTA 2 (v2_principles.md):
"Principios + Precedentes + Razonamiento" - SIN números fijos.
Guías de pensamiento + historial de decisiones + razonamiento cada vez.
```

---

## QUÉ DOCUMENTO LEER

### Si quieres implementar v4.0:
**Lee `evolution_framework_4.0_v2_principles.md`** - Es la propuesta final recomendada.

### Si quieres entender la auditoría detallada del sistema:
**Lee `evolution_framework_4.0_v1_parameters.md`** - Contiene:
- Auditoría completa de 23 parámetros con ubicaciones exactas
- Las 4 inconsistencias críticas detalladas
- Los 10 items legacy específicos
- Plan de implementación por fases muy detallado (9 fases)
- Checklist de validación exhaustivo
- Estructura de parameters.yaml completa (aunque no la usaremos)

### Para contexto completo:
Lee AMBOS documentos en orden (v1 primero, v2 después) para entender la evolución del pensamiento.

---

## COMPARACIÓN DE PROPUESTAS

| Aspecto | Propuesta 1 (v1_parameters) | Propuesta 2 (v2_principles) |
|---------|-----------------------------|-----------------------------|
| **Archivo central** | `learning/parameters.yaml` | `learning/principles.md` + `learning/decisions_log.yaml` |
| **Contiene números?** | SÍ (10%, 7%, 5% por tier) | NO (solo preguntas guía) |
| **Cómo decide sizing** | Lee parámetro, aplica override si aplica | Razona desde principios, consulta precedentes |
| **Consistencia por** | Números fijos | Razonamiento coherente |
| **Flexibilidad** | Limitada (condiciones predefinidas) | Total (con argumento) |
| **Problema** | Sigue siendo configuración fija | Requiere más pensamiento |

---

## CONTENIDO DE CADA DOCUMENTO

### v1_parameters.md (1,200+ líneas)

1. **Resumen Ejecutivo** - Qué es v4.0
2. **Contexto y Motivación** - La conversación completa
3. **Diagnóstico v3.0** - Problemas identificados
   - 23 parámetros hardcodeados CON UBICACIONES
   - 4 inconsistencias críticas
   - 10 items legacy
4. **Framework v4.0 Diseño** - Los 5 pilares
5. **Parámetros Dinámicos** - Especificación completa de parameters.yaml
   - Position sizing por tier
   - Geography por categoría
   - Sector limits
   - Cash management
   - Quality Score (sin cambios de v3.0)
   - Monitoring thresholds
6. **Protocolo EXIT** - 6 gates + Opportunity Score
7. **Limpieza Legacy** - Plan detallado
8. **Cambios en Agentes/Skills** - Qué modificar
9. **Estructura de Ficheros** - Nueva organización
10. **Plan de Implementación** - 9 fases con tareas específicas
11. **Checklist de Validación** - 50+ checks
12. **Métricas de Éxito** - Cuantitativas y cualitativas
13. **Anexos** - Conversación original, principios de diseño, glosario

### v2_principles.md (900+ líneas)

1. **Contexto Crítico** - La conversación Y el cuestionamiento posterior
2. **El Problema Fundamental** - Por qué v1 también falla
3. **La Reflexión Profunda** - ¿Cómo decide Buffett? ¿Necesito reglas?
4. **Framework v4.0** - Principios + Precedentes + Razonamiento
   - principles.md (8 principios SIN números)
   - decisions_log.yaml (precedentes con contexto)
   - Proceso de decisión de 6 pasos
5. **Cómo Operar como Gestor** - Mentalidad gestor vs robot
6. **Protocolo EXIT** - 6 gates (mismo que v1)
7. **Limpieza Legacy** - Plan (mismo que v1)
8. **Plan de Implementación** - 8 fases
9. **Validación y Métricas**
10. **Anexos** - FAQ para mi yo futuro, principios de diseño

---

## DECISIÓN: ¿CUÁL IMPLEMENTAR?

**RECOMENDACIÓN: Implementar Propuesta 2 (v2_principles.md)**

Razones:
1. El humano cuestionó v1 y tiene razón
2. Los números de v1 siguen siendo arbitrarios
3. v2 es más cercano a cómo opera un profesional
4. v2 permite verdadera adaptación

**PERO usar v1 como referencia para:**
- La auditoría detallada (23 parámetros, ubicaciones)
- El plan de limpieza legacy (es más detallado)
- Los checklists de validación

---

## IMPLEMENTACIÓN RECOMENDADA

### Fase 1: Limpieza Legacy (usar detalles de v1)
- Eliminar archivos legacy (lista en v1 sección 7)
- Resolver inconsistencias de tickers
- Compactar state/system.yaml

### Fase 2: Crear Nuevos Archivos (de v2)
- `learning/principles.md` - Copiar de v2 sección 4.2
- `learning/decisions_log.yaml` - Copiar de v2 sección 4.3

### Fase 3: Crear Exit Protocol (común a ambos)
- `.claude/skills/exit-protocol/SKILL.md`
- 6 gates + Opportunity Score

### Fase 4: Actualizar CLAUDE.md (enfoque v2)
- Eliminar referencias a parámetros fijos
- Añadir referencia a principles.md y decisions_log.yaml
- Cambiar "Reglas Duras" → "Principios de Inversión"

### Fase 5: Actualizar Tools (híbrido)
- constraint_checker.py → ADVERTIR, no rechazar
- Output: "Posición sería X%. Documenta tu razonamiento."

### Fase 6: Validación
- Simular decisiones con nuevo proceso
- Verificar que todo funciona

---

## CONTEXTO COMPLETO DE LA CONVERSACIÓN

### Pregunta 1 del humano:
> "¿Tenemos protocolo para cerrar operaciones cuando es momento de salirse?"

### Pregunta 2:
> "Si una acción ha subido y alcanza >7% vamos a vender solo por la regla?"

### Pregunta 3:
> "Las reglas son parámetros fijos aprendidos del pasado, como una especie de bias"

### Pregunta 4 (después de ver v1):
> "Siguen siendo configuración fijas... ¿realmente el sistema necesita ficheros con reglas?"

### Mi respuesta final:
> "Tienes razón. Buffett no tiene max_position.yaml. Tiene principios + experiencia.
> Yo no tengo memoria entre sesiones, pero puedo tener:
> - Principios (sin números) que guían el pensamiento
> - Precedentes (decisiones pasadas documentadas)
> - Razonamiento explícito cada vez"

---

## PARA MI YO FUTURO

1. **Lee este índice PRIMERO**
2. **Lee v2_principles.md** para la propuesta a implementar
3. **Consulta v1_parameters.md** para detalles de auditoría y limpieza
4. **Implementa siguiendo la sección "Implementación Recomendada" de este documento**
5. **El humano aprobó conceptualmente v2** - Solo falta implementar

---

## ESTADO

- **Fecha:** 2026-02-05, Sesión 37
- **Estado:** PROPUESTA APROBADA CONCEPTUALMENTE, PENDIENTE IMPLEMENTACIÓN
- **Documentos:** 3 (índice + 2 propuestas)
- **Tiempo estimado implementación:** 4-5 horas

---

**FIN DEL ÍNDICE**
