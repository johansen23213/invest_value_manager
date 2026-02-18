# File Structure & Sector Views

> Este archivo se carga automaticamente junto con CLAUDE.md
> Contiene la estructura de ficheros clave y el protocolo de sector views

---

## Ficheros Clave

| Fichero | Proposito |
|---------|-----------|
| `state/system.yaml` | Core metadata, portfolio quality, last session summary, macro snapshot |
| `state/calendar.yaml` | Future events (earnings, catalysts, macro) |
| `state/standing_orders.yaml` | Active buy/add orders with triggers |
| `state/watchlist.yaml` | Watchlist, price monitors, archived/rejected |
| `state/pipeline_tracker.yaml` | Pipeline frequencies, last_run, maintenance |
| `portfolio/current.yaml` | Portfolio actual (positions + short_positions) - Claude modifica SOLO tras confirmacion humano |
| `portfolio/history.yaml` | Posiciones cerradas (long + short) - para tracking de efectividad |
| `thesis/short/active/` | Short thesis con posicion abierta |
| `thesis/short/research/` | Candidatos short en analisis |
| `thesis/short/_TEMPLATE.md` | Template de thesis short |
| `world/current_view.md` | Vision macro general |
| `world/sectors/{sector}.md` | Vision sectorial (v2.2.1) |
| `state/agent_coordination.yaml` | Coordinacion inter-agente (shared blackboard) |
| `learning/da_accuracy_tracker.yaml` | DA correction tracking — pre/post FV, 6-month review, accuracy stats |

---

## Sector Views (v2.2.1)

### Que son?
Analisis profundos por sector que complementan la vision macro. Ubicados en `world/sectors/`.

### Para que sirven?
1. **Contexto pre-inversion**: ANTES de analizar cualquier empresa, leer su sector view
2. **Pipeline de ideas**: Cada sector tiene "Empresas Objetivo" como watchlist sectorial
3. **Anti-bias**: Evita depender de popularity bias para generar ideas
4. **Consistencia**: Documenta por que un sector esta barato/caro

### Sectores documentados actuales
| Sector | Posiciones |
|--------|------------|
| auto-eu.md | (pipeline only) |
| automotive.md | (pipeline only) |
| business-services.md | EDEN.PA |
| consumer-discretionary.md | LULU |
| consumer-staples.md | DOM.L |
| defense-aerospace.md | (pipeline only) |
| digital-marketplaces.md | MONY.L, AUTO.L |
| energy.md | (pipeline only) |
| environmental-water.md | (pipeline only) |
| financial-data-analytics.md | (pipeline only) |
| healthcare-equipment.md | (pipeline only) |
| hr-payroll-processing.md | ADP (pipeline), PAYC (watchlist) |
| industrial-technology.md | (pipeline only) |
| industrials.md | (pipeline only) |
| insurance.md | GL |
| luxury-goods.md | (pipeline only) |
| media-publishing.md | (pipeline only) |
| payments-fintech.md | (pipeline only) |
| pharma-healthcare.md | NVO |
| real-estate.md | (pipeline only) |
| self-service-vending.md | MEGP.L (pipeline, R4 conditional) |
| semiconductors-equipment.md | (pipeline only) |
| technology.md | ADBE, BYIT.L |
| telecom.md | DTE.DE |
| testing-inspection-certification.md | (pipeline only) |
| utilities.md | (pipeline only) |

### Protocolo de Uso

```
+-----------------+     +-------------------+     +------------------+
| Existe sector   | NO  | Crear con sector- |     | Leer sector view |
| view para esta  |---->| deep-dive skill   |---->| ANTES de         |
| empresa?        |     | o template        |     | fundamental-     |
+--------+--------+     +-------------------+     | analyst          |
         | SI                                      +------------------+
         +--------------------------------------------^
```

### Quien crea/actualiza?
| Agente | Responsabilidad |
|--------|-----------------|
| **sector-screener** | Crea sector view ANTES de screening si no existe |
| **fundamental-analyst** | Verifica que existe y lee ANTES de analizar |
| **macro-analyst** | Puede actualizar si hay cambio macro relevante |
| **health-check** | Verifica que existen sector views para posiciones activas |

### Cada cuanto actualizar?
- **Cada 30 dias** como maximo (staleness check)
- **Ante cambio material**: earnings season del sector, regulacion nueva, disrupcion
- **En cada screening**: anadir empresas encontradas a "Empresas Objetivo"

### Que pasa si NO existe sector view?
1. **fundamental-analyst** DEBE crearlo ANTES de proceder con analisis
2. Usar `world/sectors/_TEMPLATE.md` como base
3. Aplicar sector-deep-dive skill para contenido
4. NO se puede valorar empresa sin contexto sectorial

### Template rapido
Ver `world/sectors/_TEMPLATE.md` para estructura completa. Minimo obligatorio:
- Resumen Ejecutivo (2-3 parrafos)
- Status: SOBREPONDERAR / NEUTRAL / INFRAPONDERAR / EVITAR
- Metricas Clave (TAM, P/E sector, yield)
- Empresas Objetivo (para analisis / evitar)

### Sistema de Dependencias y Propagacion (v2.2.2)

**REGLA**: Toda thesis depende de su sector view y del world view. Cambios materiales requieren re-evaluacion.

#### Estructura de Dependencias en Sector Views
Cada sector view tiene seccion "Dependencias Activas":
```markdown
| Tipo | Ticker | Thesis Path | Ultima Eval | Status |
|------|--------|-------------|-------------|--------|
| Portfolio | VICI | thesis/active/VICI | 2026-02-03 | HOLD |
| Watchlist | SRE.L | thesis/research/SRE.L | 2026-02-04 | Entry 75p |
```

#### Protocolo de Cambio Material
Cuando se actualiza sector view o world view con cambio MATERIAL:
1. Clasificar cambio: COSMETICO / MENOR / MATERIAL / CRITICO
2. Si MATERIAL o CRITICO:
   - Marcar todas las dependencias como "NEEDS_REVIEW"
   - Anadir al calendario: "RE-EVAL [tickers] por cambio en [sector/macro]"
   - Documentar en "Historial de Cambios"
3. Lanzar review-agent batch para re-evaluar

| Tipo Cambio | Ejemplo | Accion |
|-------------|---------|--------|
| COSMETICO | Typo, formato | Nada |
| MENOR | Anadir candidato | Actualizar fecha |
| MATERIAL | Status cambia, tipos suben | RE-EVAL dependencias |
| CRITICO | Crisis sector, kill condition | ALERTA + RE-EVAL inmediata |

#### Flujo Post-Analisis (fundamental-analyst)
Despues de analizar una empresa:
1. Si BUY ejecutado -> mover a "Nuestras Posiciones" + anadir a "Dependencias Activas"
2. Si WATCHLIST -> anadir a "Analizadas - En Watchlist" + anadir a "Dependencias Activas"
3. Si AVOID -> anadir a "Evitar" con razon
4. Mover de "Empresas Objetivo" a la seccion correspondiente

#### Ciclo de Vida de Thesis Archivadas
Cuando una thesis se archiva (venta o invalidacion):
1. Mover thesis de `thesis/active/` o `thesis/research/` -> `thesis/archive/`
2. En sector view:
   - Eliminar de "Dependencias Activas"
   - Anadir a "Historial de Analisis" con razon y leccion aprendida
3. En `portfolio/history.yaml`: registrar resultado (P&L, duracion, por que)
4. Mantener maximo 10 entradas en historial, luego purgar a archivo

#### Control de Tamano de Documentos
Cuando sector view supera 300 lineas:
1. Mover "Historial de Analisis" a `world/sectors/archive/{sector}-history.md`
2. Mantener solo ultimos 6 meses en "Analizadas - En Watchlist"
3. Comprimir "Empresas Objetivo" eliminando candidatos ya analizados

---

## Reglas Operativas

### Portfolio
- `portfolio/current.yaml`: Claude puede modificar SOLO tras confirmacion del humano
- NUNCA operar sin thesis documentada
- NUNCA apalancamiento
- Tier D (QS <35) = NO COMPRAR (calidad minima insuficiente)
- Sizing, concentracion y cash se razonan desde principios (`learning/principles.md`) y precedentes (`learning/decisions_log.yaml`)
- Ejecutar `constraint_checker.py` para contexto antes de decisiones de sizing

### Precios
**PRECIOS: SIEMPRE via `python3 tools/price_checker.py TICKER`.**
- NUNCA WebSearch para precios de acciones
- NUNCA hardcodear precios en scripts
- yfinance es la UNICA fuente de precios fiable
- Esta regla aplica a TODOS los agentes sin excepcion

---

## Standing Orders

Mantener en `state/standing_orders.yaml` con stocks que tienen:
- Thesis completa y validada
- Investment committee aprobado
- Precio trigger definido
- Sizing calculado

El humano puede ejecutar en eToro sin esperar sesion cuando el precio toca el trigger.
En la siguiente sesion, confirma y actualizo el sistema.

---

## Coordinacion Inter-Agente

Via `state/agent_coordination.yaml` (shared blackboard pattern).
Ver skill `agent-coordination` para protocolo.

---

## PRINCIPIO ANTI-CASH-DRAG

El cash prolongado sin oportunidades claras tiene coste de oportunidad. Razonar sobre el nivel apropiado dado el contexto.

Causa raiz tipica: proceso secuencial y pipeline vacio.

Solucion:
1. Mantener SIEMPRE 5+ thesis pre-escritas en watchlist con precio target
2. SIEMPRE usar batch mode (3-5 analisis paralelos)
3. Fast-track para stocks con thesis existente
4. Standing orders para que el humano pueda ejecutar entre sesiones
5. Cada sesion: verificar pipeline. Si <3 thesis pre-escritas -> screening inmediato
