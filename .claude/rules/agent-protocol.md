# Agent Protocol

> Auto-loaded. Arbol de decision + reglas criticas de agentes.
> Registro completo: `.claude/skills/agent-registry/SKILL.md`

---

## REGLA: TODOS opus. NUNCA haiku/sonnet.

---

## Arbol de Decision (OBLIGATORIO antes de cualquier tarea)

```
Que necesito?
├─ ANALIZAR empresa nueva LONG (buy-pipeline 4 rondas)
│  R1: fundamental-analyst + moat-assessor + risk-identifier (PARALELO) → valuation-specialist
│  R2: devil's-advocate
│  R3: Resolucion conflictos (si necesario)
│  R4: investment-committee (10 gates)
├─ ANALIZAR fragilidad SHORT (short-pipeline 4 rondas)
│  S1: fundamental-analyst (--short-thesis) + moat-assessor + risk-identifier (PARALELO) → valuation-specialist
│  S2: devil's-advocate (BULL case — por que precio podria tener razon?)
│  S3: Resolucion conflictos (si necesario)
│  S4: investment-committee (modo SHORT_APPROVAL — 10+3 gates)
├─ DESAFIAR thesis → devil's-advocate
├─ RE-EVALUAR posicion long → review-agent
├─ RE-EVALUAR posicion short → review-agent (--short-review)
├─ APROBAR compra/venta → investment-committee (OBLIGATORIO)
├─ APROBAR short/cover → investment-committee modo SHORT_APPROVAL (OBLIGATORIO)
├─ CUBRIR short → cover-protocol skill → investment-committee
├─ BUSCAR en sector → sector-screener
├─ ACTUALIZAR macro → macro-analyst
├─ SIZING → position-calculator
├─ WATCHLIST → watchlist-manager
├─ PORTFOLIO post-trade → portfolio-ops (soporta BUY/SELL/SHORT/COVER)
├─ PERFORMANCE → performance-tracker
├─ REBALANCEO → rebalancer
├─ CALENDARIO → calendar-manager
├─ HEALTH CHECK → health-check
├─ MOVER ficheros → file-system-manager
├─ MEJORAR sistema → system-evolver
└─ CREAR tool Python → quant-tools-dev
```

---

## Instrucciones v4.0 para Agentes de Decision

Al invocar fundamental-analyst, review-agent, investment-committee, incluir:

```
CONTEXTO v4.0:
- Leer learning/principles.md + learning/decisions_log.yaml
- NO limites fijos — razonar desde principios
- Razonamiento explicito. Si se desvia de precedentes, explicar por que.
- Tools = DATOS CRUDOS, no interpretar como warnings/violations
- Indicar si empresa califica Tier A (Principio 9: Quality Gravitation)
```

---

## Verificacion Post-Agente

```
[ ] Output tiene estructura esperada?
[ ] Refleja frameworks de los skills?
[ ] Datos consistentes (FV matches inputs)?
[ ] No hay errores obvios?
[ ] Actualizo ficheros que debia? (releer y verificar)
```

Si falla → re-ejecutar con instruccion mas especifica o corregir + documentar.

---

## Propagacion de Cambios

Cuando hay cambio sistemico:
```
[ ] Que agentes leen/escriben esto? → Actualizar
[ ] Que skills definen el framework? → Actualizar
[ ] file-system-rules conoce ubicacion? [ ] health-check debe verificar?
[ ] CLAUDE.md documenta? [ ] agent-registry actualizado?
```
