---
name: portfolio-constraints
description: Portfolio sizing limits, rebalancing triggers. Max position 7%, sector 25%, geography 35%, cash min 5%.
user-invocable: false
disable-model-invocation: false
---

# Portfolio Constraints Skill

## Estructura target
| Categoría | Peso | Posiciones |
|-----------|------|-----------|
| Defensive Value | 35-40% | 7-8 |
| Cyclical Value | 45-50% | 9-11 |
| Opportunistic | 0-5% | 0-3 |
| Cash | 10-15% | - |
| **Total** | **100%** | **16-20** |

## Sizing por tipo
| Tipo | Sizing | Máx posiciones |
|------|--------|---------------|
| Core Conviction | 6-7% | 6-7 |
| Standard Value | 4-5% | bulk |
| Opportunistic | 2-3% | 3 |

## Ajustes sizing
- Riesgo país alto: -1%
- Sector cíclico en pico: -0.5%
- Execution risk alto: -1%
- Defensive sector: puede +1%

## Límites absolutos
- Posición individual máx: 7%
- Sector máx: 25%
- Geografía máx: 35%
- Cash mínimo absoluto: 5%
- Cash target: 12%
- Mínimo sectores: 5
- Mínimo geografías: 4

## Rebalanceo triggers
- Posición >target × 1.3 → TRIM
- Posición <target × 0.7 + thesis intacta → ADD
- Sector >27% → REBALANCEAR inmediato
- Geografía >37% → REBALANCEAR
- Cash <5% → STOP buying
