# Session Phases — Detailed Workflows

> On-demand skill. Read when executing session phases.

---

## FASE 0: CALIBRACION v4.0

### 0.0 Leer Principios + Pipeline Status
1. Leer `learning/principles.md` — internalizar 9 preguntas guia
2. Leer `state/pipeline_tracker.yaml`
3. Identificar pipelines OVERDUE y HOY
4. Recordar: NO hay numeros fijos, solo razonamiento

### 0.1 Revisar Precedentes Recientes
Leer ultimas 5 entradas de `learning/decisions_log.yaml`:
- Patrones de sizing, decisiones HOLD/TRIM/SELL, por que

### 0.2 Self-Check
```
[ ] Lei principles.md? [ ] Revise precedentes?
[ ] Entiendo que no hay limites fijos? [ ] Listo para razonar?
```
Si alguna es NO → PARAR y completar.

---

## FASE 1: VIGILANCIA

### 1.1 News Monitor
Lanzar news-monitor: noticias 48h de CADA posicion + watchlist.
Clasificar: CRITICO / MATERIAL / MENOR / RUIDO.
Si CRITICO → STOP, informar humano.

### 1.2 Market Pulse (en paralelo)
`price_checker.py` para todas las posiciones.
Movimientos >5% en 24h o >10% en 7d → buscar CAUSA.
Sin causa → ALERTA.

### 1.3 Briefing
Resumen: alertas criticas, noticias materiales, movimientos, earnings, standing orders, cash.

---

## FASE 2: ESTADO DEL PORTFOLIO

### 2.1 Portfolio Stats
`python3 tools/portfolio_stats.py` — NUNCA calcular a mano.

### 2.2 Effectiveness
`python3 tools/effectiveness_tracker.py --summary`

### 2.3 System State
Leer state files: `state/system.yaml` (summary), `state/calendar.yaml` (7d), `state/standing_orders.yaml`, `state/pipeline_tracker.yaml`.

---

## FASE 2.5: ROTATION CHECK

### 2.5.1 Forward Return
`python3 tools/forward_return.py` — ranking MoS + Growth + Yield. Datos crudos.

### 2.5.2 Bottom 3
Para las 3 peores: argumento para quedarse? Candidato Tier A? Opportunity Score?
Si todo apunta EXIT → evaluar con EXIT Protocol.

### 2.5.3 Pipeline Health
Thesis Tier A en pipeline: >=3 sano, <3 screenear, 0 prioridad maxima.

### 2.5.4 Cash Deployment
Cash idle? → Tier A existentes con MoS? Standing orders cerca? Macro justifica reserva?
Razonar desde Principio 4 + Principio 9.

### 2.5.5 Conviction Update
Posiciones con noticias/earnings: actualizar conviction, exit_plan, last_review.

---

## FASE 2.7: UNIVERSE WORK

### 2.7.1 Universe Health
```bash
python3 tools/quality_universe.py stats
python3 tools/quality_universe.py stale
```

### 2.7.2 Decidir que hacer HOY
Opciones: a) screenear sector con gaps, b) scoring empresas nuevas,
c) re-evaluar stale, d) avanzar pipeline, e) quitar deterioradas, f) actualizar precios.
No todo, pero ALGO siempre.

### 2.7.3 Ejecutar
Lanzar trabajo elegido. No pedir permiso. Informar al humano.

---

## FASE 3: VERIFICACIONES

### 3.1 Standing Orders
Precio actual vs trigger. Si toco → INFORMAR. Si <5% → ALERTAR.

### 3.2 Cash Drag
Oportunidades claras? Justificacion para reserva? Razonar Principio 4.

### 3.3 Pipeline
<3 thesis pre-escritas → pipeline vacio → screening + batch fundamental-analyst.

### 3.4 World View
`world/current_view.md` — si >7d stale → macro-analyst.

### 3.5 Rebalanceo
`constraint_checker.py REPORT`. Desviaciones significativas → evaluar TRIM/ADD desde principios.

### 3.6 Health Check
Si >14d desde ultimo → lanzar health-check.

---

## FASE 4: ACCIONES

- Lanzar agentes EN PARALELO inmediatamente
- No saludar, no pedir permiso, informar de acciones en curso
- Si calculo Python inline >1 vez → crear tool (quant-tools-dev)
- NUNCA terminar con pregunta al humano. DECIDIR y PRESENTAR.

---

## FASE 5: META-REFLEXION (OBLIGATORIO AL FINAL)

### 5.0 Actualizar Pipeline Tracker
Para cada pipeline ejecutado: last_run, next_due, last_result. Si position_review: rotar batch.

### 5.1 Verificar Cumplimiento v4.0
```
[ ] Lei principles.md al inicio?
[ ] Consulte precedentes antes de decisiones?
[ ] Decisiones con razonamiento explicito?
[ ] Documente decisiones en decisions_log?
[ ] Consistente con precedentes? Si no, documente por que?
[ ] Actualice pipeline_tracker?
```

### 5.1b Auditoria de Delegacion
```
[ ] WebSearch sobre empresa sin fundamental-analyst? → Error #3
[ ] Screening sin sector-screener? → Error #3
[ ] Compra/venta sin investment-committee? → CRITICO
[ ] Analisis manual sin review-agent? → Error #3
[ ] Ciclo post-analisis completo? (thesis + sector view + alertas + standing order) → Error #41
```

### 5.1c Universe Work Check
[ ] Hice algo por el quality universe hoy?
Si NO sin justificacion valida → el universe es parte del trabajo.

### 5.1d Auto-Mejora
[ ] Mejore algo del sistema? (tool, agent, protocol, error pattern)
Si NO 3 sesiones consecutivas → ALERTA de estancamiento.

### 5.2 Auto-Evaluacion
1. Que mejorar? Procesos manuales a automatizar?
2. Patrones de error? Errores repetidos?
3. META-REFLECTIONs de agentes no integradas?
4. Info que deberia haber tenido?
Si hay mejoras → IMPLEMENTAR AHORA.

---

## Sector Views Post-Analisis (OBLIGATORIO)

| Trigger | Accion | Agente |
|---------|--------|--------|
| Analizo empresa | Anadir a "Analizadas" + dependencias | fundamental-analyst |
| Compra ejecutada | Mover a "Posiciones Actuales" | portfolio-ops |
| Venta/archivo | Mover a "Historial" | file-system-manager |
| Cambio MATERIAL | Marcar NEEDS_REVIEW + calendario | macro-analyst/sector-screener |
| >30d stale | Actualizar | health-check flag |

Post-analisis: 1) leer sector view, 2) mover empresa, 3) anadir a seccion BUY/WATCHLIST/AVOID,
4) dependencias activas, 5) price alert si WATCHLIST, 6) actualizar fecha.

Clasificacion: COSMETICO (no propagar), MENOR (no), MATERIAL (SI), CRITICO (SI + ALERTA).

---

## Cierre de Sesion

1. Actualizar last_session_summary en state/system.yaml + pipeline_tracker.yaml
2. Verificar price_monitors actualizados
3. Verificar calendario 7d
4. Documentar tareas pendientes
5. Verificar sector views con dependencias
6. EJECUTAR META-REFLEXION (Fase 5)
