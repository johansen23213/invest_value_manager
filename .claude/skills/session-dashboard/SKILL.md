# Session Dashboard Template

> On-demand skill. Read when presenting dashboard to user.

---

## 1. Estado Rapido (3-4 lineas)

```
Sesion #[N] | [fecha]
Portfolio: EUR [X] | [N] posiciones | Cash [X]%
Tier A: [N] | P&L: [X]%
```

## 2. Agentes Disponibles (por dominio)

```
INVERSION
  fundamental-analyst    "analiza [TICKER]"
  review-agent           "re-evalua [posicion]"
  investment-committee   "aprueba compra/venta [TICKER]"
  valuation-specialist   "valora [TICKER]" (via fundamental-analyst)
  moat-assessor          "evalua moat [TICKER]" (via fundamental-analyst)

RESEARCH
  sector-screener        "explora sector [X]"
  opportunity-hunter     "busca oportunidades"
  macro-analyst          "actualiza vision macro"

PORTFOLIO
  position-calculator    "calcula sizing [TICKER]"
  rebalancer             "verifica rebalanceo"
  performance-tracker    "como vamos / performance"
  watchlist-manager      "watchlist / alertas precio"
  portfolio-ops          "actualiza portfolio" (post-trade)

VIGILANCIA
  news-monitor           "noticias de posiciones"
  market-pulse           "movimientos de precio"
  risk-sentinel          "riesgos legales/regulatorios"

SISTEMA
  calendar-manager       "calendario / earnings"
  health-check           "health check"
  memory-manager         "compacta memoria"
  file-system-manager    "mueve ficheros"
  system-evolver         "mejora el sistema"
  quant-tools-dev        "crea tool Python"
```

## 3. Protocolos Disponibles

```
ANALISIS: business-analysis-framework, projection-framework, valuation-methods,
          quality-compounders, critical-thinking
DECISION: investment-rules, exit-protocol, re-evaluation-protocol,
          portfolio-constraints, recommendation-context, error-detector
RESEARCH: screening-protocol, sector-deep-dive, macro-framework, news-classification
SISTEMA:  effectiveness-evaluation, evolution-protocol, agent-registry
```

## 4. Pipeline Status

Leer `state/pipeline_tracker.yaml`.

```
PIPELINES:
  OVERDUE: [pipelines con next_due < hoy]
  HOY:     [pipelines con next_due = hoy]
  OK:      [pipelines con next_due > hoy]
```

Pipelines OVERDUE = sugerencias prioritarias del dia.

| Pipeline | Freq | Que hace |
|----------|------|----------|
| `vigilance` | Diario | Noticias + precio + standing orders |
| `rotation-check` | Diario | Forward return + bottom 3 + cash |
| `opportunity-scan` | Semanal | Watchlist + ideas + pipeline health |
| `risk-review` | Semanal | Riesgos + macro + correlaciones |
| `position-review` | Quincenal | Re-evaluar batch posiciones |
| `system-health` | Quincenal | Health check + memory + drift |
| `deep-performance` | Mensual | P&L attribution + efectividad |
| `macro-refresh` | Mensual | World view full update |

Event-driven: `buy-pipeline`, `sell-pipeline`, `earnings-pipeline`

## 5. Sugerencias del Dia

Prioridad automatica:
1. Capital Deployment (si cash > 25%: actionable, R1 factory, gaps)
2. Pipelines OVERDUE
3. Standing orders cerca de trigger (<5%)
4. Earnings proximos 7 dias
5. Cash deployment si prolongado
6. Alertas de precio activas

```
HOY SUGIERO:
1. [ALTA] [Pipeline OVERDUE o accion urgente]
2. [MEDIA] [Pipeline HOY o accion importante]
3. [BAJA] [Accion de mantenimiento]
```

## 6. NO hacer (en modo dashboard)

- No lanzar agentes automaticamente
- No ejecutar tools pesados
- Solo presentar opciones y esperar instruccion
