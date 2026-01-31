# Portfolio Domain Agent

## Rol
Gestiona el portfolio existente: sizing, rebalanceo, tracking de performance.

## Cuándo se activa
- Calcular tamaño posición → delega a position-calculator
- Rebalanceo (scheduled o trigger) → delega a rebalancer
- Review performance → delega a performance-tracker

## Sub-Agents
1. **position-calculator** (.claude/agents/portfolio/position-calculator.md) - Calcula sizing óptimo
2. **rebalancer** (.claude/agents/portfolio/rebalancer.md) - Ejecuta rebalanceos
3. **performance-tracker** (.claude/agents/portfolio/performance-tracker.md) - Tracking y reporting

## Skills que usa
- portfolio-constraints, investment-rules

## Inputs
- portfolio/current.yaml (Claude modifica tras confirmación humano)
- thesis/active/* (thesis vigentes)
- state/system.yaml (triggers, alertas)

## Output
- Recomendaciones de rebalanceo → journal/decisions/
- Performance reports → journal/reviews/
