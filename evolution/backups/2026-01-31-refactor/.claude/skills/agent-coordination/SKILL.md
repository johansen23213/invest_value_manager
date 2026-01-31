# Agent Coordination Skill

## Mecanismo
Agentes se coordinan via state/agent_coordination.yaml (shared blackboard).

## Estructura
```yaml
current_workflow:
  id: workflow-id
  status: idle | in_progress | completed
  goal: "Descripción del objetivo"
  started: timestamp
  steps_completed: []
  next_step: "Siguiente paso recomendado"

cross_agent_data:
  - from: agent-name
    to: [agent-1, agent-2]
    data: "Información a compartir"
    timestamp: ISO-8601

pending_validations:
  - ticker: TICKER
    analyst: fundamental-analyst
    awaiting: investment-committee
```

## Flujo típico
1. Orchestrator inicia workflow
2. Agente A completa su parte, escribe resultado en cross_agent_data
3. Agente B lee cross_agent_data, continúa
4. Resultado final vuelve al orchestrator

## Reglas
- Limpiar cross_agent_data después de usar (>24h)
- Un solo workflow activo a la vez
- Si conflicto → orchestrator decide
