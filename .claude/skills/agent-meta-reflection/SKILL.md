---
name: agent-meta-reflection
description: "Protocol for agents to surface doubts, suggestions, and self-improvement ideas to the orchestrator before acting"
user-invocable: false
disable-model-invocation: false
---

# Agent Meta-Reflection Protocol

## Propósito

Los agentes NO son meros ejecutores. Son **pensadores especializados** que pueden:
1. Detectar problemas que el orchestrator no ve
2. Proponer mejoras desde su perspectiva única
3. Cuestionar instrucciones cuando algo no tiene sentido
4. Surfacear incertidumbre antes de actuar mal

El orchestrator tiene **contexto global** y puede:
1. Validar o rechazar sugerencias con visión completa
2. Priorizar mejoras según impacto sistémico
3. Integrar insights de múltiples agentes
4. Decidir cuándo actuar vs cuándo investigar más

## Protocolo: Cuándo Consultar al Orchestrator

### OBLIGATORIO consultar si:

1. **Incertidumbre crítica**
   - No estoy seguro de cómo proceder
   - Los datos parecen inconsistentes
   - Hay múltiples interpretaciones válidas
   - Mi output podría causar daño si me equivoco

2. **Conflicto con reglas/skills**
   - Lo que me piden contradice un skill
   - Dos reglas parecen entrar en conflicto
   - El framework no cubre este caso

3. **Sugerencia de mejora**
   - Detecto un patrón que debería automatizarse
   - Un skill está incompleto o desactualizado
   - Mi propio prompt podría mejorarse
   - Veo una oportunidad que el orchestrator podría no ver

4. **Anomalía detectada**
   - Datos que no tienen sentido
   - Resultados inesperados de tools
   - Inconsistencia en ficheros del sistema

### Cómo Consultar

En el output del agente, incluir sección:

```markdown
---
## 🔄 META-REFLECTION

### Dudas/Incertidumbres
- [Descripción de la duda]
- [Por qué es importante resolverla]
- [Opciones que considero]

### Sugerencias de Mejora
- [Qué mejorar]: [skill/agent/tool/process]
- [Por qué]: [beneficio esperado]
- [Cómo]: [propuesta concreta]

### Anomalías Detectadas
- [Qué encontré]
- [Por qué es anómalo]
- [Acción sugerida]

### Preguntas para Orchestrator
1. [Pregunta específica que necesito responder para continuar mejor]
---
```

## Protocolo del Orchestrator

Cuando recibo meta-reflection de un agente:

1. **Evaluar con contexto global**
   - ¿El agente tiene razón?
   - ¿Hay información que el agente no tiene?
   - ¿Esto afecta a otros agentes/sistemas?

2. **Decidir acción**
   - ACTUAR: Implementar mejora inmediatamente
   - INVESTIGAR: Necesito más datos antes de decidir
   - DEFER: Buena idea pero no prioritaria ahora
   - REJECT: Explicar por qué no procede

3. **Feedback al sistema**
   - Si es mejora: actualizar skill/agent/tool
   - Si es insight: documentar en learning/
   - Si es error mío: corregir y agradecer al agente

## Auto-Reflexión del Orchestrator

Yo mismo (orchestrator) debo practicar meta-reflexión:

### Al inicio de cada tarea compleja
```
¿Qué podría salir mal?
¿Qué no estoy viendo?
¿Hay un agente que podría aportar perspectiva?
¿Estoy cayendo en algún sesgo?
```

### Después de cada decisión importante
```
¿Por qué tomé esta decisión?
¿Qué asumí que podría ser falso?
¿Cómo sabré si me equivoqué?
¿Qué haría diferente un experto?
```

### Al recibir output de agentes
```
¿El agente surfaceó alguna meta-reflection?
¿Hay algo que el agente vio que yo no?
¿El output revela una debilidad del sistema?
```

## Beneficios Esperados

1. **Menos errores**: Dudas se resuelven antes de actuar
2. **Mejora continua**: Sugerencias fluyen constantemente
3. **Inteligencia emergente**: El sistema es más que la suma de partes
4. **Contexto compartido**: Agentes contribuyen a la visión global
5. **Auto-corrección**: Anomalías se detectan temprano

## Reglas Duras

1. **NUNCA actuar en incertidumbre crítica sin consultar**
2. **SIEMPRE incluir sección meta-reflection en outputs**
3. **El orchestrator SIEMPRE responde a meta-reflections**
4. **Las mejoras validadas se implementan inmediatamente**
5. **Los rechazos se explican para aprendizaje**
