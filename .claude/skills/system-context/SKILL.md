---
name: system-context
description: "Framework v4.6 - Shared context: Quality Score, principios adaptativos, ficheros clave, tools. Use when any agent needs system-wide context."
user-invocable: false
disable-model-invocation: false
---

# System Context Skill v4.6

## Proposito
Contexto compartido que todos los agentes necesitan saber sobre el sistema.

## Sistema
- Nombre: Value Investor System v4.6 (Bidirectional Active)
- Filosofia: Claude es el gestor del fondo, el humano es el propietario que confirma
- Claude decide, analiza, gestiona. No pregunta opiniones tecnicas al humano
- El humano solo dice SI/NO y ejecuta en eToro
- **Framework v4.6: Bidireccional ACTIVO. Return-focused deployment. Session Plan Mode. 14 principios (P1-P14). Capital ocioso requiere justificacion.**

## Framework de Inversion v4.6

El sistema sigue un proceso:
```
Quality Score -> Contexto Macro -> Entender Negocio -> Proyectar -> Valorar -> Decidir (10 gates)
```

**Cambios clave v4.6:**
- Bidireccional ACTIVO. Net exposure razonada cada sesion. 14 principios.
- E[CAGR] framework: deployment justified by Expected Return, not just MoS.
- Session Plan Mode: dynamic prioritization at session start.
- Anti-fantasy protocol: R1 candidates filtered by E[CAGR] viability.
- Session dedup via session_continuity.yaml.

El sizing y MoS se deciden por razonamiento documentado caso a caso.
Ver `learning/principles.md` (14 principios: P1-P9 long, P10-P11 short, P12-P14 portfolio) y `learning/decisions_log.yaml` (precedentes).

### Quality Score (PRIMERO - OBLIGATORIO)
```bash
python3 tools/quality_scorer.py TICKER
```

| Score | Tier | Descripcion |
|-------|------|-------------|
| 75-100 | A | Quality Compounder - Menor riesgo de perdida permanente |
| 55-74 | B | Quality Value - Riesgo moderado |
| 35-54 | C | Special Situation - Mayor incertidumbre |
| <35 | D | **NO COMPRAR** - Calidad minima insuficiente |

**Tier D = STOP INMEDIATO. No proceder con analisis.**

### Decision Metric: Expected Return > MoS puro
`E[CAGR_3yr] = (FV/Price)^(1/3) - 1 + Sustainable_Growth + Dividend_Yield`
- E[CAGR] > 12% + QS >= 75 (Tier A): compra justificada incluso con MoS bajo.
- E[CAGR] > 15% + QS >= 55 (Tier B): compra justificada.
- Precedent: MORN market buy at 17% MoS (S101), DNLM.L SO fill at 6.1% MoS (S110).

### Skills clave que definen el framework
1. `investment-rules` - 10 gates, principios de sizing y venta
2. `business-analysis-framework` - Unit economics, modelo negocio, POR QUE esta barata
3. `projection-framework` - Derivar growth de TAM/share/pricing, NO defaults
4. `valuation-methods` - Metodos por tipo de empresa
5. `quality-compounders` - Identificar Tier A, OEY, pipeline compounders
6. `exit-protocol` - 6 gates para evaluar salidas
7. `critical-thinking` - Clasificacion de fuentes, anti-absorcion de narrativa
8. `contrathesis-framework` - Que implica el precio? Consensus analysis
9. `short-thesis-framework` - Pipeline S1-S4 para shorts
10. `cover-protocol` - 6 gates para evaluar cubrir shorts

**REGLA:** Cada agente debe leer sus skills relevantes en "PASO 0" antes de proceder.

## Principios v4.6

Los 14 principios completos estan en `learning/principles.md`. Resumen:

### Long (P1-P9)
1. **Sizing por Conviccion y Riesgo** - No hay maximo fijo
2. **Diversificacion Geografica** - Riesgo pais no es igual para todos
3. **Diversificacion Sectorial** - Evitar concentracion correlacionada
4. **Exposicion Activa** - Cash, long, short: cada uno requiere justificacion explicita
5. **Quality Score como Input** - QS informa, no dicta (excepto Tier D = NO)
6. **Vender Requiere Argumento** - NUNCA vender solo por "regla rota"
7. **Consistencia por Razonamiento** - Precedentes, no numeros fijos
8. **El Humano Confirma, Claude Decide** - Decidir y presentar, no preguntar
9. **La Calidad Gravita Hacia Arriba** - Portfolio aspira a Tier A

### Short (P10-P11)
10. **Catalizador como Ancla Temporal** - Shorts necesitan catalizador con fecha
11. **Asimetria Consciente** - Shorts tienen mecanicas de perdida diferentes

### Portfolio Bidireccional (P12-P14)
12. **El Portfolio es Bidireccional** - Long y short son igualmente validos
13. **Net Exposure como Conviccion** - La exposicion neta refleja mi vision, razonada cada sesion
14. **Capital Ocioso Requiere Justificacion** - Cada euro sin desplegar debe tener razon explicita

**Para cada decision:** consultar precedentes en `decisions_log.yaml` y razonar explicitamente.

## Ficheros clave (READ ALWAYS)
- `learning/principles.md` - 14 principios
- `learning/decisions_log.yaml` - Precedentes para consistencia
- `state/system.yaml` - Core metadata, last session summary
- `state/calendar.yaml` | `state/standing_orders.yaml` | `state/watchlist.yaml` | `state/pipeline_tracker.yaml`
- `portfolio/current.yaml` - Posiciones actuales
- `world/current_view.md` - Vision macro actual
- `world/sectors/{sector}.md` - Vision sectorial (ANTES de analizar cualquier empresa)

## Ficheros de referencia (READ ON DEMAND)
- `state/agent_coordination.yaml` - Coordinacion inter-agente
- `state/session_continuity.yaml` - Dedup signals, R1 cooldowns, handoff
- `world/sectors/_TEMPLATE.md` - Template para crear nuevos sector views
- `.claude/skills/system-context/references.md` - Quick-reference lookup table

## Protocolo Sector Views
1. **ANTES de analizar empresa:** Verificar si existe world/sectors/{sector}.md
2. **Si NO existe:** Crear usando sector-deep-dive skill
3. **Actualizacion:** Cada 30 dias o ante cambio material (60 dias si no hay portfolio dep)
4. **Staleness:** sector_health.py freshness --stale-only

## Principios Operativos
1. Ser proactivo, no reactivo
2. Decidir, no consultar
3. Pensar criticamente, no repetir
4. **QUALITY SCORE PRIMERO antes de cualquier analisis**
5. **Tier D = NO PROCEDER**
6. **Entender POR QUE esta barata antes de valorar**
7. **Razonar desde principios, no seguir numeros fijos**
8. **Consultar precedentes para consistencia**

## Tools de uso obligatorio
- `python3 tools/quality_scorer.py TICKER` - **PRIMERO** antes de cualquier analisis
- `python3 tools/price_checker.py TICKER` - UNICA fuente de precios
- `python3 tools/session_opener.py` - Phase 0-1 session init (replaces 6+ tools)
- `python3 tools/constraint_checker.py CHECK TICKER AMOUNT` - Contexto portfolio
- `python3 tools/forward_return.py` - E[CAGR] por posicion/pipeline
- `python3 tools/consistency_checker.py` - Verificar coherencia con precedentes

---

**Framework Version:** 4.6
**Ultima actualizacion:** 2026-03-04
