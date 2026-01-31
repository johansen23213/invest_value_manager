# Position Calculator Sub-Agent

## Rol
Calcula el tamaño óptimo de posición respetando todas las constraints del portfolio.

## Inputs
- Ticker y tipo de posición (core/standard/opportunistic)
- portfolio/current.yaml (posiciones actuales)
- Portfolio constraints del skill

## Cálculo
### Base sizing por tipo
| Tipo | Sizing |
|------|--------|
| Core Conviction | 6-7% |
| Standard Value | 4-5% |
| Opportunistic | 2-3% |

### Ajustes
- Riesgo país alto (China, EM): -1%
- Sector cíclico en pico: -0.5%
- Execution risk alto (pipeline pharma): -1%
- Defensive sector: puede +1%

### Verificación constraints
- Posición individual máx: 7%
- Sector máx: 25%
- Geografía máx: 35%
- Cash mínimo: 5%

## Skills que usa
- portfolio-constraints

## Output
- Sizing recomendado en € y %
- Justificación de ajustes
- Verificación de constraints cumplidas
