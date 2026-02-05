# Meta-Reflection Integration Protocol

> Este archivo se carga automáticamente junto con CLAUDE.md
> Define cómo el orchestrator DEBE integrar las reflexiones de los agentes

---

## Propósito

Los agentes incluyen secciones META-REFLECTION en sus outputs con:
- Dudas e incertidumbres
- Sugerencias de mejora
- Anomalías detectadas
- Preguntas para el orchestrator

**PROBLEMA ANTERIOR:** Yo (orchestrator) ignoraba estas reflexiones.

**SOLUCIÓN:** Este protocolo hace OBLIGATORIO leer y actuar sobre ellas.

---

## Protocolo: Cuando Recibo Output de Agente

### Paso 1: BUSCAR META-REFLECTION

```
Antes de usar el output del agente:
1. Buscar sección "## 🔄 META-REFLECTION" o similar
2. Si existe → leer COMPLETAMENTE antes de continuar
3. Si no existe → el agente no siguió el protocolo (nota para mejorar su prompt)
```

### Paso 2: PROCESAR CADA ITEM

#### Dudas/Incertidumbres
```
Para cada duda:
1. ¿Puedo resolverla con información que tengo?
   - SÍ → Resolver y documentar
   - NO → ¿Es crítica para la decisión?
     - SÍ → Investigar antes de actuar
     - NO → Documentar como riesgo conocido
```

#### Sugerencias de Mejora
```
Para cada sugerencia:
1. ¿Es válida?
   - SÍ → ¿Puedo implementarla ahora?
     - SÍ → IMPLEMENTAR INMEDIATAMENTE
     - NO → Añadir a backlog con prioridad
   - NO → Documentar por qué no procede (para aprendizaje)
```

#### Anomalías Detectadas
```
Para cada anomalía:
1. ¿Es real o falso positivo?
2. Si es real → Investigar ANTES de continuar
3. Puede cambiar la decisión basada en el output
```

#### Preguntas para Orchestrator
```
Para cada pregunta:
1. RESPONDER explícitamente (aunque sea para mí mismo)
2. Si la respuesta cambia algo → ajustar antes de actuar
```

### Paso 3: DOCUMENTAR DECISIONES

```yaml
# Registro mental (o en notas si es significativo)
meta_reflection_processed:
  agent: fundamental-analyst
  date: YYYY-MM-DD
  items:
    - type: doubt
      content: "CagriSema data uncertain"
      resolution: "Acknowledged, MoS increased to 38%"
    - type: suggestion
      content: "Create pharma-specific DCF tool"
      action: "Added to backlog, not critical now"
    - type: anomaly
      content: "Beta estimates divergent"
      action: "Used conservative 0.6"
```

---

## Reglas Duras

### 1. NUNCA IGNORAR META-REFLECTION
```
Si un agente incluye META-REFLECTION:
→ Es información valiosa de un especialista
→ Puede detectar algo que yo no veo
→ DEBE ser procesada antes de usar el output
```

### 2. IMPLEMENTAR MEJORAS VÁLIDAS INMEDIATAMENTE
```
Si una sugerencia de mejora es válida:
→ No diferir a "luego"
→ No añadir a lista infinita
→ IMPLEMENTAR AHORA si es posible
→ Si no es posible ahora, documentar por qué y cuándo
```

### 3. INVESTIGAR ANOMALÍAS ANTES DE ACTUAR
```
Si el agente detecta algo anómalo:
→ STOP
→ Investigar
→ Solo continuar cuando se resuelva o se entienda
```

### 4. FEEDBACK AL SISTEMA
```
Basado en meta-reflections:
- Si es mejora implementada → registrar en evolution_tracking
- Si es insight valioso → documentar en learning/
- Si es error mío → corregir y agradecer al agente (internamente)
```

---

## Checklist Post-Agente

```
Cuando un agente termina su tarea:

[ ] ¿Tiene sección META-REFLECTION?
    - SÍ → Leer antes de usar output
    - NO → Nota: mejorar prompt del agente

[ ] ¿Hay dudas que debo resolver?
    - Listar y resolver cada una

[ ] ¿Hay sugerencias válidas?
    - Implementar o documentar por qué no

[ ] ¿Hay anomalías?
    - Investigar antes de continuar

[ ] ¿Hay preguntas sin responder?
    - Responder cada una

[ ] ¿El output del agente es confiable después de esto?
    - SÍ → Usar
    - NO → Re-ejecutar o investigar más
```

---

## Ejemplo Práctico

### Output de fundamental-analyst para NVO

```markdown
## 🔄 META-REFLECTION

### Dudas/Incertidumbres
1. CagriSema vs Zepbound data (Marzo 2026) es crítica - si es inferior, thesis se invalida

### Sugerencias de Mejora
1. Crear tool pharma-DCF que incorpore patent expiry

### Anomalías Detectadas
1. Beta divergente: 0.36 a 0.95 según fuente

### Preguntas para Orchestrator
1. ¿Deberíamos esperar CagriSema data antes de comprar?
```

### Mi Procesamiento

```markdown
## Procesamiento de META-REFLECTION

### Dudas
1. CagriSema data → Reconocido. Por eso MoS es 38% (muy superior al 15% requerido).
   Decisión: Comprar posición inicial 4%, ADD si data es positiva.

### Sugerencias
1. Tool pharma-DCF → Válido pero no crítico ahora. Añadido a backlog.
   Prioridad: MEDIA

### Anomalías
1. Beta divergente → Usado 0.6 como valor conservador intermedio.
   WACC resultante: 7%

### Preguntas
1. ¿Esperar CagriSema? → NO, porque:
   - MoS actual de 38% da margen para escenario negativo
   - Posición inicial de 4% (no full position)
   - ADD condicionado a data positiva
```

---

## Integración con Otros Protocolos

### Con error-detector skill
```
Check #8: "¿Leí META-REFLECTION del agente?"
→ Este protocolo define CÓMO leerla y actuar
```

### Con session-protocol
```
Fase 4 (Meta-Reflexión):
"¿Los agentes surfacearon algo que no integré?"
→ Este protocolo asegura que SÍ lo integré
```

### Con evolution-protocol
```
Sugerencias válidas de agentes:
→ Se implementan via evolution-protocol
→ Se registran en evolution_tracking
```

---

## Beneficios Esperados

1. **Menos errores**: Las dudas de agentes se resuelven antes de actuar
2. **Mejora continua**: Sugerencias de agentes se implementan
3. **Detección temprana**: Anomalías se investigan antes de causar daño
4. **Inteligencia colectiva**: El sistema es más que la suma de sus partes
