# Session Dashboard — Quick Status View

> On-demand skill. Version corta para cuando el humano pide "estado" sin iniciar sesion completa.
> Para sesion completa: usar `.claude/skills/session-planner/SKILL.md` (auto-activa en modo SESSION PLAN).

---

## Cuando Usar

- El humano dice "estado", "como vamos", "resumen rapido"
- NO inicia sesion de trabajo — solo quiere ver numeros
- Si quiere trabajar → session-planner se activa automaticamente

---

## Template

```
Sesion #[N] | [fecha]
Portfolio: EUR [X] invested | [N] posiciones | Cash [Y]%
P&L: [+/-X.X]%
Tier A: [N] | Probation: [tickers o ninguno]
Market Regime: [Opportunity/Fair-Value/Defensive]

PROXIMOS EVENTOS (7d):
- [fecha] [ticker] [evento]
- ...

ALERTAS:
- [SOs near trigger, pipelines OVERDUE, positions on probation]
- Si no hay alertas: "Sin alertas."
```

## Que Ejecutar

1. `python3 tools/portfolio_stats.py` — P&L y allocation
2. Leer `state/calendar.yaml` — proximos 7d
3. Leer `state/standing_orders.yaml` — SOs near trigger

## NO Hacer

- NO lanzar agentes
- NO ejecutar tools pesados (forward_return, r1_prioritizer)
- NO generar plan de trabajo — para eso esta session-planner
- Solo presentar estado y esperar instruccion
