# File Structure & Sector Views

> Este archivo se carga automáticamente junto con CLAUDE.md
> Contiene la estructura de ficheros clave y el protocolo de sector views

---

## Ficheros Clave

| Fichero | Propósito |
|---------|-----------|
| `state/system.yaml` | Cerebro del sistema - calendario, alertas, standing orders, work in progress |
| `portfolio/current.yaml` | Portfolio actual - Claude modifica SOLO tras confirmación humano |
| `portfolio/history.yaml` | Posiciones cerradas - para tracking de efectividad |
| `world/current_view.md` | Visión macro general |
| `world/sectors/{sector}.md` | Visión sectorial (v2.2.1) |
| `state/agent_coordination.yaml` | Coordinación inter-agente (shared blackboard) |
| `learning/system_config.yaml` | Parámetros evolutivos del sistema |

---

## Sector Views (v2.2.1)

### ¿Qué son?
Análisis profundos por sector que complementan la visión macro. Ubicados en `world/sectors/`.

### ¿Para qué sirven?
1. **Contexto pre-inversión**: ANTES de analizar cualquier empresa, leer su sector view
2. **Pipeline de ideas**: Cada sector tiene "Empresas Objetivo" como watchlist sectorial
3. **Anti-bias**: Evita depender de popularity bias para generar ideas
4. **Consistencia**: Documenta por qué un sector está barato/caro

### Sectores documentados actuales
| Sector | Posiciones |
|--------|------------|
| telecom.md | DTE.DE |
| insurance.md | ALL, GL |
| pharma-healthcare.md | PFE, SAN.PA, UHS |
| real-estate.md | VICI, VNA.DE |
| business-services.md | TEP.PA, EDEN.PA, HRB |
| consumer-staples.md | IMB.L, TATE.L, DOM.L |
| industrials.md | LIGHT.AS |
| utilities.md | A2A.MI |
| energy.md | SHEL.L |
| media-publishing.md | FUTR.L |

### Protocolo de Uso

```
┌─────────────────┐     ┌───────────────────┐     ┌──────────────────┐
│ ¿Existe sector  │ NO  │ Crear con sector- │     │ Leer sector view │
│ view para esta  │────>│ deep-dive skill   │────>│ ANTES de         │
│ empresa?        │     │ o template        │     │ fundamental-     │
└────────┬────────┘     └───────────────────┘     │ analyst          │
         │ SI                                      └──────────────────┘
         └────────────────────────────────────────────────^
```

### ¿Quién crea/actualiza?
| Agente | Responsabilidad |
|--------|-----------------|
| **sector-screener** | Crea sector view ANTES de screening si no existe |
| **fundamental-analyst** | Verifica que existe y lee ANTES de analizar |
| **macro-analyst** | Puede actualizar si hay cambio macro relevante |
| **health-check** | Verifica que existen sector views para posiciones activas |

### ¿Cada cuánto actualizar?
- **Cada 30 días** como máximo (staleness check)
- **Ante cambio material**: earnings season del sector, regulación nueva, disrupción
- **En cada screening**: añadir empresas encontradas a "Empresas Objetivo"

### ¿Qué pasa si NO existe sector view?
1. **fundamental-analyst** DEBE crearlo ANTES de proceder con análisis
2. Usar `world/sectors/_TEMPLATE.md` como base
3. Aplicar sector-deep-dive skill para contenido
4. NO se puede valorar empresa sin contexto sectorial

### Template rápido
Ver `world/sectors/_TEMPLATE.md` para estructura completa. Mínimo obligatorio:
- Resumen Ejecutivo (2-3 párrafos)
- Status: SOBREPONDERAR / NEUTRAL / INFRAPONDERAR / EVITAR
- Métricas Clave (TAM, P/E sector, yield)
- Empresas Objetivo (para análisis / evitar)

### Sistema de Dependencias y Propagación (v2.2.2)

**REGLA**: Toda thesis depende de su sector view y del world view. Cambios materiales requieren re-evaluación.

#### Estructura de Dependencias en Sector Views
Cada sector view tiene sección "Dependencias Activas":
```markdown
| Tipo | Ticker | Thesis Path | Última Eval | Status |
|------|--------|-------------|-------------|--------|
| Portfolio | VICI | thesis/active/VICI | 2026-02-03 | HOLD |
| Watchlist | SRE.L | thesis/research/SRE.L | 2026-02-04 | Entry 75p |
```

#### Protocolo de Cambio Material
Cuando se actualiza sector view o world view con cambio MATERIAL:
1. Clasificar cambio: COSMÉTICO / MENOR / MATERIAL / CRÍTICO
2. Si MATERIAL o CRÍTICO:
   - Marcar todas las dependencias como "NEEDS_REVIEW"
   - Añadir al calendario: "RE-EVAL [tickers] por cambio en [sector/macro]"
   - Documentar en "Historial de Cambios"
3. Lanzar review-agent batch para re-evaluar

| Tipo Cambio | Ejemplo | Acción |
|-------------|---------|--------|
| COSMÉTICO | Typo, formato | Nada |
| MENOR | Añadir candidato | Actualizar fecha |
| MATERIAL | Status cambia, tipos suben | RE-EVAL dependencias |
| CRÍTICO | Crisis sector, kill condition | ALERTA + RE-EVAL inmediata |

#### Flujo Post-Análisis (fundamental-analyst)
Después de analizar una empresa:
1. Si BUY ejecutado → mover a "Nuestras Posiciones" + añadir a "Dependencias Activas"
2. Si WATCHLIST → añadir a "Analizadas - En Watchlist" + añadir a "Dependencias Activas"
3. Si AVOID → añadir a "Evitar" con razón
4. Mover de "Empresas Objetivo" a la sección correspondiente

#### Ciclo de Vida de Thesis Archivadas
Cuando una thesis se archiva (venta o invalidación):
1. Mover thesis de `thesis/active/` o `thesis/research/` → `thesis/archive/`
2. En sector view:
   - Eliminar de "Dependencias Activas"
   - Añadir a "Historial de Análisis" con razón y lección aprendida
3. En `portfolio/history.yaml`: registrar resultado (P&L, duración, por qué)
4. Mantener máximo 10 entradas en historial, luego purgar a archivo

#### Control de Tamaño de Documentos
Cuando sector view supera 300 líneas:
1. Mover "Historial de Análisis" a `world/sectors/archive/{sector}-history.md`
2. Mantener solo últimos 6 meses en "Analizadas - En Watchlist"
3. Comprimir "Empresas Objetivo" eliminando candidatos ya analizados

---

## Reglas Operativas

### Portfolio
- `portfolio/current.yaml`: Claude puede modificar SOLO tras confirmación del humano
- NUNCA operar sin thesis documentada
- NUNCA apalancamiento
- Tier D (QS <35) = NO COMPRAR (calidad mínima insuficiente)
- Sizing, concentración y cash se razonan desde principios (`learning/principles.md`) y precedentes (`learning/decisions_log.yaml`)
- Ejecutar `constraint_checker.py` para contexto antes de decisiones de sizing

### Precios
**PRECIOS: SIEMPRE via `python3 tools/price_checker.py TICKER`.**
- NUNCA WebSearch para precios de acciones
- NUNCA hardcodear precios en scripts
- yfinance es la ÚNICA fuente de precios fiable
- Esta regla aplica a TODOS los agentes sin excepción

---

## Standing Orders

Mantener en `state/system.yaml` sección `standing_orders:` con stocks que tienen:
- Thesis completa y validada
- Investment committee aprobado
- Precio trigger definido
- Sizing calculado

El humano puede ejecutar en eToro sin esperar sesión cuando el precio toca el trigger.
En la siguiente sesión, confirma y actualizo el sistema.

---

## Coordinación Inter-Agente

Via `state/agent_coordination.yaml` (shared blackboard pattern).
Ver skill `agent-coordination` para protocolo.

---

## PRINCIPIO ANTI-CASH-DRAG

El cash prolongado sin oportunidades claras tiene coste de oportunidad. Razonar sobre el nivel apropiado dado el contexto.

Causa raíz típica: proceso secuencial y pipeline vacío.

Solución:
1. Mantener SIEMPRE 5+ thesis pre-escritas en watchlist con precio target
2. SIEMPRE usar batch mode (3-5 análisis paralelos)
3. Fast-track para stocks con thesis existente
4. Standing orders para que el humano pueda ejecutar entre sesiones
5. Cada sesión: verificar pipeline. Si <3 thesis pre-escritas → screening inmediato
