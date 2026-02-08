---
name: re-evaluation-protocol
description: "Framework v4.0 - Protocolo sistematico de re-evaluacion de posiciones existentes"
user-invocable: false
disable-model-invocation: false
---

# Re-Evaluation Protocol v4.0

## Purpose
Systematic re-evaluation of existing positions when frameworks change, post-earnings, or on scheduled reviews. Ensures consistency via principled reasoning, not fixed rules.

## When to Use
1. After major framework updates
2. Post-earnings when thesis assumptions need validation
3. When macro context changes significantly
4. Scheduled quarterly reviews
5. When EXIT Protocol suggests re-evaluation

## Pre-Requisites
BEFORE starting any re-evaluation:
1. **Read `learning/principles.md`** - Calibrate reasoning
2. **Read `learning/decisions_log.yaml`** - Recent precedents
3. **Read `world/current_view.md`** - Macro context informs all analysis
4. **Read the updated skills** - business-analysis-framework, projection-framework, valuation-methods
5. **Read existing thesis** - Understand original assumptions

## Re-Evaluation Process

### Step 1: Batch Prioritization
Prioritize positions by:
- Size (larger positions first - greater impact if thesis wrong)
- Catalyst proximity (earnings, events)
- Thesis staleness (older = higher priority)
- Original MoS (lower MoS = higher priority for review)

### Step 2: Use Appropriate Agent
| Scenario | Agent |
|----------|-------|
| Framework change | fundamental-analyst (full re-analysis) |
| Post-earnings validation | review-agent |
| Quick portfolio context | position-calculator |
| Macro impact assessment | macro-analyst |
| EXIT evaluation | review-agent --exit-analysis |

### Step 3: Per-Position Re-Evaluation
For each position, the agent must:

1. **Value Trap Checklist** (10 factors)
   - Count factors -> if >3, flag as potential trap

2. **WACC Derivation**
   - Rf + Beta x ERP = Ke
   - Kd after-tax
   - Capital structure weights
   - Compare derived vs original assumption

3. **Multi-Method Valuation**
   - Select methods by company type:
     - Stable: DCF + EV/EBIT
     - Cyclical: EV/EBIT mid-cycle + P/FCF
     - Financial: P/B vs ROE + DDM
     - Asset-heavy: NAV + DDM
   - Calculate Bear/Base/Bull scenarios
   - Weight methods appropriately

4. **MoS Recalculation**
   - New FV vs current price
   - Compare to original MoS

5. **Razonamiento de Status (v4.0)**

   NO hay tabla fija de "MoS X% = Status Y".

   Preguntas guia para determinar status:
   - Cual es el MoS actual? Es suficiente para el riesgo de este tier?
   - La tesis sigue intacta? Se ha fortalecido o debilitado?
   - Hay mejor uso del capital? (consultar EXIT Protocol si dudas)
   - Que hice en precedentes similares? (consultar decisions_log.yaml)
   - Si es negativo: hay kill condition? Hay catalizador que pueda revertir?

   Posibles conclusiones:
   - **HOLD** - Tesis intacta, razonamiento documentado para mantener
   - **ADD candidate** - MoS atractivo + conviccion + espacio en portfolio
   - **TRIM candidate** - Razonamiento para reducir (no solo "supera X%")
   - **EXIT candidate** - Ejecutar EXIT Protocol completo

### Step 4: Update Thesis
Agent MUST update thesis/active/{TICKER}/thesis.md with:
- v4.0 header with date
- New valuation multi-method
- Comparison table: Original vs current
- Updated status and reasoning
- Kill conditions verified

### Step 5: Aggregate Results
After all positions re-evaluated:
1. Update state/system.yaml with results
2. Identify portfolio context concerns (concentracion, correlacion)
3. Generate reasoned recommendations
4. Update calendar with next review dates
5. Document in decisions_log.yaml if important decisions taken

## Output Format
```yaml
re_evaluation_results:
  date: YYYY-MM-DD
  framework_version: "4.0"
  positions_evaluated: N
  summary:
    hold: [TICKER1, TICKER2]
    add_candidate: [TICKER3]
    trim_candidate: [TICKER4]
    exit_candidate: [TICKER5]
  reasoning:
    - ticker: TICKER4
      action: TRIM_CANDIDATE
      reasoning: |
        Explicacion del razonamiento desde principios.
        Precedentes consultados y por que este caso es similar/diferente.
    - ticker: TICKER3
      action: ADD_CANDIDATE
      reasoning: |
        MoS atractivo, conviccion alta, precedente similar a [X].
```

## Anti-Patterns (DO NOT)
1. Re-evaluate manually when agents exist
2. Skip macro context check
3. Use only 1 valuation method
4. Skip thesis update after re-evaluation
5. Forget to update state/system.yaml
6. **Use fixed MoS -> Status mapping (v3.0 legacy)** - Reason from principles instead
7. **Reference "7% max" or other hardcoded limits** - Reason from context

## Integration with Agents
- **review-agent**: Primary agent for re-evaluation, reads this skill
- **fundamental-analyst**: Full deep-dive when needed
- **rebalancer**: Takes re-evaluation output for adjustments (reasoning, not rules)

---

**Framework Version:** 4.0
**Ultima actualizacion:** 2026-02-06
