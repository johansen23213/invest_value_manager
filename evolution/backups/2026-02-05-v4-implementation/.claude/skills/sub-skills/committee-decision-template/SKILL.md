---
name: committee-decision-template
description: Template for documenting investment committee decisions for traceability
user-invocable: false
---

# Committee Decision Template

## Uso
El investment-committee agent DEBE crear un archivo con este formato después de cada decisión.

## Ubicación
`thesis/[research|active]/[TICKER]/committee_decision.md`

---

## TEMPLATE

```markdown
# Investment Committee Decision: [TICKER]

> Fecha: YYYY-MM-DD
> Precio al momento: [precio] [moneda]
> Decisión: [APROBAR BUY / WATCHLIST / REJECT]

---

## Resumen Ejecutivo

**Empresa:** [nombre completo]
**Sector:** [sector]
**Geografía:** [país/región]
**Tier:** [A / B / C]
**Fair Value:** [precio] ([método principal])
**MoS actual:** [X]%

---

## Validación de 8 Gates

| Gate | Status | Nota |
|------|--------|------|
| 1. Business Understanding | PASS/FAIL | [1 línea] |
| 2. Proyección Fundamentada | PASS/FAIL | Growth X%, WACC Y% |
| 3. Valoración Multi-Método | PASS/FAIL | [métodos usados] |
| 4. Margen de Seguridad | PASS/FAIL | MoS X% vs Y% req |
| 5. Contexto Macro | PASS/FAIL | [ciclo, fit] |
| 6. Portfolio Fit | PASS/FAIL | [constraints OK/violación] |
| 7. Autocrítica | PASS/FAIL | [sesgos identificados] |
| 8. Sector Understanding | PASS/FAIL | [sector view exists/date] |

**Gates pasados:** X/8
**Gates fallidos:** [lista si aplica]

---

## Valoración

| Método | Fair Value | Peso |
|--------|-----------|------|
| [método 1] | | X% |
| [método 2] | | X% |
| **Weighted** | **[FV]** | 100% |

| Escenario | Fair Value | Probabilidad | MoS |
|-----------|-----------|--------------|-----|
| Bear | | 25% | |
| Base | | 50% | |
| Bull | | 25% | |
| **Expected** | | 100% | |

---

## Riesgos y Kill Conditions

### Riesgos Principales
1. [riesgo 1] - Prob: X%, Impacto: [alto/medio/bajo]
2. [riesgo 2]
3. [riesgo 3]

### Kill Conditions (vender inmediatamente si ocurre)
1. [ ] [condición 1]
2. [ ] [condición 2]
3. [ ] [condición 3]

---

## Decisión

### Si APROBAR BUY:
```
Acción: COMPRAR
Ticker: [TICKER]
Sizing: €[X] ([Y]% del portfolio)
Shares aproximadas: [N]
Precio máximo de entrada: [precio]
```

### Si WATCHLIST:
```
Acción: WATCHLIST
Ticker: [TICKER]
Precio target de entrada: [precio] (MoS sería X%)
Condición de entrada: [qué debe pasar]
Standing order: [SI/NO]
```

### Si REJECT:
```
Acción: REJECT
Ticker: [TICKER]
Razón principal: [1-2 líneas]
Clasificación: [value trap / MoS insuficiente / no entiendo / macro / sector]
Revisitar: [NO / SI si precio cae a X / SI si condición]
```

---

## Post-Decisión (si APROBAR)

- [ ] Mover thesis a active/
- [ ] Actualizar portfolio/current.yaml
- [ ] Configurar price alert
- [ ] Actualizar watchlist en system.yaml
- [ ] Documentar next review date

---

## Firmas

**Investment Committee:** Claude (Orchestrator)
**Fecha:** YYYY-MM-DD
**Versión Framework:** v2.1 (8 gates)
```
