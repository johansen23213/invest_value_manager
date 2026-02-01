---
name: dcf-template
description: Discounted Cash Flow valuation template with sensitivity analysis
user-invocable: false
disable-model-invocation: false
---

# DCF Template Sub-Skill

## Tool automatizado
**SIEMPRE usar `python3 tools/dcf_calculator.py TICKER --scenarios` en lugar de cálculos manuales.**
El tool implementa todo lo descrito abajo automáticamente. Este skill es referencia teórica.

## Inputs requeridos
- FCF actual (último año fiscal)
- Growth rate años 1-5 (conservador: guidance -20-30%)
- Growth rate años 6-10 (fade to terminal)
- Terminal growth rate (≤ GDP, 2-3%)
- WACC (mínimo 8% empresas establecidas)
- Shares outstanding

## Cálculo
1. Proyectar FCF años 1-10
2. Calcular terminal value: FCF₁₀ × (1+g) / (WACC - g)
3. Descontar todos los flujos a valor presente
4. Sumar PV flujos + PV terminal value
5. Dividir por shares outstanding = fair value per share

## Sensibilidad
Calcular fair value con:
- WACC: base ±1%
- Growth: base ±2%
- Terminal: base ±0.5%

## Conservadurismo
- Usar FCF (no earnings) siempre que posible
- Growth rates < analyst consensus
- Terminal growth ≤ inflation target (2%)
- WACC reflejar riesgo real, no teórico
