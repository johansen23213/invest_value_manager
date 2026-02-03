# Re-Evaluation Protocol v1.0

## Purpose
Systematic re-evaluation of existing positions when frameworks or methodologies change. Ensures consistency between new standards and legacy positions.

## When to Use
1. After major framework updates (v2.0, v3.0, etc.)
2. Post-earnings when thesis assumptions need validation
3. When macro context changes significantly
4. Scheduled quarterly reviews

## Pre-Requisites
BEFORE starting any re-evaluation:
1. **Read world/current_view.md** — Macro context informs all analysis
2. **Read the updated skills** — business-analysis-framework, projection-framework, valuation-methods
3. **Read existing thesis** — Understand original assumptions

## Re-Evaluation Process

### Step 1: Batch Prioritization
Prioritize positions by:
- Size (larger positions first)
- Catalyst proximity (earnings, events)
- Thesis staleness (older = higher priority)
- Original MoS (lower MoS = higher risk of reclassification)

### Step 2: Use Appropriate Agent
| Scenario | Agent |
|----------|-------|
| Framework change (like v2.0) | fundamental-analyst (full re-analysis) |
| Post-earnings validation | review-agent |
| Quick constraint check | position-calculator |
| Macro impact assessment | macro-analyst |

### Step 3: Per-Position Re-Evaluation
For each position, the agent must:

1. **Value Trap Checklist** (10 factors)
   - Count SI factors → if >3, flag as potential trap

2. **WACC Derivation**
   - Rf + Beta × ERP = Ke
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

5. **Status Determination**
   | New MoS | Status |
   |---------|--------|
   | >25% | UNDERVALUED → HOLD/ADD candidate |
   | 10-25% | FAIRLY VALUED → HOLD |
   | 0-10% | FAIRLY VALUED → HOLD, no add |
   | <0% | OVERVALUED → TRIM candidate |

### Step 4: Update Thesis
Agent MUST update thesis/active/{TICKER}/thesis.md with:
- v2.0 header with date
- New valuation multi-method
- Comparison table: Original vs v2.0
- Updated status and action triggers

### Step 5: Aggregate Results
After all positions re-evaluated:
1. Update state/system.yaml with results
2. Identify constraint violations
3. Generate TRIM/ADD recommendations
4. Update calendar with next review dates

## Output Format
```yaml
re_evaluation_results:
  date: YYYY-MM-DD
  framework_version: "2.0"
  positions_evaluated: N
  summary:
    undervalued: [TICKER1, TICKER2]
    fairly_valued: [TICKER3, TICKER4]
    overvalued: [TICKER5]
  actions_required:
    - ticker: TICKER5
      action: TRIM
      reason: "MoS -5%, overvalued per EV/EBIT"
    - ticker: TICKER1
      action: ADD_CANDIDATE
      reason: "MoS 30%, position 3.5% < 7% max"
```

## Anti-Patterns (DO NOT)
1. Re-evaluate manually when agents exist
2. Skip macro context check
3. Use only 1 valuation method
4. Skip thesis update after re-evaluation
5. Forget to update state/system.yaml

## Integration with Agents
- **review-agent**: Primary agent for re-evaluation, reads this skill
- **fundamental-analyst**: Full deep-dive when needed
- **rebalancer**: Takes re-evaluation output for position adjustments
