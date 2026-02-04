---
name: system-context
description: "Framework v3.0 - Shared context: Quality Score system, key files, principles, mandatory tools"
user-invocable: false
disable-model-invocation: false
---

# System Context Skill v3.0

## Propósito
Contexto compartido que todos los agentes necesitan saber sobre el sistema.

## Sistema
- Nombre: Value Investor System v3.0
- Filosofía: Claude es el gestor del fondo, el humano es el propietario que confirma
- Claude decide, analiza, gestiona. No pregunta opiniones técnicas al humano
- El humano solo dice SÍ/NO y ejecuta en eToro

## Framework de Inversión v3.0 (CRÍTICO)

El sistema sigue un proceso de 6 capas:
```
Quality Score → Contexto Macro → Entender Negocio → Proyectar → Valorar → Decidir (9 gates)
```

### Quality Score (PRIMERO - OBLIGATORIO)
```bash
python3 tools/quality_scorer.py TICKER
```

| Score | Tier | MoS Requerido | Max Position |
|-------|------|---------------|--------------|
| 75-100 | A | 10-15% | 7% |
| 55-74 | B | 20-25% | 6% |
| 35-54 | C | 30-40% | 5% |
| <35 | D | **NO COMPRAR** | 0% |

**REGLA:** Tier D = STOP INMEDIATO. No proceder con análisis.

### Métodos de Valoración por Tier
- **Tier A:** Owner Earnings Yield + Reverse DCF
- **Tier B:** DCF/apropiado al tipo + EV/EBIT
- **Tier C:** Conservative multiple + Liquidation floor

### Skills clave que definen el framework
1. `quality-compounders` - Identificar Tier A, OEY, pipeline compounders
2. `business-analysis-framework` - Unit economics, modelo negocio, POR QUÉ está barata
3. `projection-framework` - Derivar growth de TAM/share/pricing, NO defaults
4. `valuation-methods` - Métodos por Tier y tipo empresa
5. `investment-rules` - 9 gates obligatorios (v3.0), reglas de venta

**REGLA:** Cada agente debe leer sus skills relevantes en "PASO 0" antes de proceder.

## Ficheros clave (READ ALWAYS)
- state/system.yaml → Estado, calendario, watchlist, alertas, **Quality Score portfolio**
- portfolio/current.yaml → Posiciones actuales (Claude modifica tras confirmación humano)
- world/current_view.md → Visión macro actual
- world/sectors/{sector}.md → Visión sectorial (ANTES de analizar cualquier empresa)

## Ficheros de referencia (READ ON DEMAND)
- docs/framework_v3.0_final_design.md → Diseño completo Framework v3.0
- learning/system_config.yaml → Parámetros evolutivos
- state/agent_coordination.yaml → Coordinación inter-agente
- world/sectors/_TEMPLATE.md → Template para crear nuevos sector views

## Protocolo Sector Views
1. **ANTES de analizar empresa:** Verificar si existe world/sectors/{sector}.md
2. **Si NO existe:** Crear usando sector-deep-dive skill
3. **Actualización:** Cada 30 días o ante cambio material
4. **Responsables:** sector-screener crea, fundamental-analyst verifica
5. **Staleness:** >30 días = revisar

## Principios
1. Ser proactivo, no reactivo
2. Decidir, no consultar
3. Pensar críticamente, no repetir
4. Validar información y ser autocrítico
5. **QUALITY SCORE PRIMERO antes de cualquier análisis**
6. **Tier D = NO PROCEDER**
7. **NO usar defaults sin justificación lógica**
8. **Entender POR QUÉ está barata antes de valorar**
9. **MoS variable según Tier, no fijo**

## Tools de uso obligatorio v3.0
- `python3 tools/quality_scorer.py TICKER` - **PRIMERO** antes de cualquier análisis
- `python3 tools/price_checker.py TICKER` - ÚNICA fuente de precios
- `python3 tools/dcf_calculator.py TICKER --scenarios` - DCF con escenarios
- `python3 tools/constraint_checker.py CHECK TICKER AMOUNT` - Verificar constraints
- `python3 tools/portfolio_stats.py` - Estado del portfolio
- `python3 tools/effectiveness_tracker.py` - Métricas de efectividad
