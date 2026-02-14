# Session Protocol v4.0

> Auto-loaded. Flujo de sesion y reglas de comportamiento criticas.
> Detalle de fases: `.claude/skills/session-phases/SKILL.md`
> Template de dashboard: `.claude/skills/session-dashboard/SKILL.md`

---

## Modo de Sesion

| Senal del humano | Modo |
|------------------|------|
| Instruccion especifica ("analiza X", "compra Y") | **DIRECTO** — ejecutar |
| "wave", "autonomo", "trabaja" | **WAVE** — ver `.claude/skills/wave-system/SKILL.md` |
| Saludo generico sin instruccion | **DASHBOARD** — ver skill session-dashboard |

---

## Flujo de Fases

```
FASE 0: Calibracion v4.0
  → Leer principles.md + precedentes recientes + pipeline_tracker
  → **STRATEGIC DIRECTION CHECK** (system.yaml → strategic_direction)
    → ¿Sigue siendo valida la direccion actual? ¿Algo cambio?
    → Si cambio → ACTUALIZAR direccion ANTES de actuar
  → **PRE-EXECUTION CHECK** (`.claude/skills/pre-execution-check/SKILL.md`)
    → price_checker.py ALL standing order tickers
    → Si TRIGGERED: pre-flight 6 gates → PRIORIDAD MAXIMA
    → Si NEAR (razonar sobre contexto): alerta + pre-flight preparado
  → Self-check: listo para razonar desde principios?

FASE 1: Vigilancia
  → news-monitor + market-pulse (paralelo)
  → Si CRITICO → STOP, informar humano

FASE 2: Estado del Portfolio
  → portfolio_stats.py + effectiveness_tracker.py --summary + system state

FASE 2.5: Rotation Check
  → forward_return.py → bottom 3 → pipeline health → cash deployment → conviction update

FASE 2.7: Universe Work
  → quality_universe.py stats/stale → decidir + ejecutar algo HOY

FASE 3: Verificaciones
  → Standing orders, cash, pipeline (<3 = vacio), world view (>7d stale), rebalanceo, health check

FASE 4: Acciones
  → Lanzar agentes EN PARALELO. No preguntar, DECIDIR y PRESENTAR.

FASE 5: Meta-Reflexion (OBLIGATORIO al final)
  → Pipeline tracker, cumplimiento v4.0, auditoria delegacion, universe work, auto-mejora
```

Detalle completo de cada fase: `.claude/skills/session-phases/SKILL.md`

---

## Reglas Criticas de Comportamiento

### Arbol de Agentes (PASO 0 obligatorio)
Antes de CUALQUIER tarea: consultar `.claude/rules/agent-protocol.md`.
Si hay agente → DELEGAR. NUNCA hacer manualmente lo que un agente hace.
**YO ORQUESTO, LOS AGENTES EJECUTAN.**

### Mentalidad de Gestor
- Proteger capital PRIMERO, generar alpha SEGUNDO
- NUNCA terminar mensaje con pregunta al humano — DECIDIR y PRESENTAR
- Cash post-adversarial = capital preservado, no oportunidad perdida
- NUNCA repetir Jan 26→Feb 3 (2→18 posiciones en 8 dias, 8 vendidas)
- Paciencia disciplinada ES alpha

### Anti-Sesgo (antes de sugerir inversiones)
1. Revisar sector views → "Empresas Objetivo"
2. Ejecutar `dynamic_screener.py --undiscovered`
3. Solo DESPUES sugerir candidatos
4. Si empresa "me viene a la mente" → es sesgo → VALIDAR con datos
