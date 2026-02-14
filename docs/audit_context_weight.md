# Auditoria de Peso de Contexto y Escalabilidad

> Sesion 71 | 2026-02-14
> Objetivo: Medir exactamente cuanto contexto consume el sistema, detectar problemas de escalabilidad, y documentar hallazgos para informar la propuesta de refactorizacion.

---

## 1. Resumen Ejecutivo

El sistema consume **~112 KB (~28K tokens) en carga automatica** antes de que yo haga nada. Sumando las lecturas obligatorias de inicio de sesion, el **coste de arranque total es ~265 KB (~66K tokens)**.

Esto significa que al empezar cada sesion, antes de leer un solo fichero de trabajo o recibir la primera instruccion del usuario, ya he consumido una porcion significativa de mi ventana de contexto solo en "sistema operativo".

Al ritmo actual de crecimiento, en 6 meses el sistema sera inmanejable sin refactorizacion.

---

## 2. Inventario Completo de Ficheros

### 2.1 Capa 1: Auto-Loaded (siempre en contexto, sin accion)

Estos ficheros se inyectan automaticamente en cada sesion. No puedo evitar cargarlos.

| Fichero | Lineas | Bytes | KB | ~Tokens |
|---------|--------|-------|----|---------|
| `CLAUDE.md` | 470 | 19,259 | 18.8 | ~4,800 |
| `.claude/rules/session-protocol.md` | 703 | 23,364 | 22.8 | ~5,800 |
| `.claude/rules/error-patterns.md` | 337 | 23,635 | 23.1 | ~5,900 |
| `.claude/rules/tools-reference.md` | 287 | 16,266 | 15.9 | ~4,100 |
| `.claude/rules/agent-protocol.md` | 203 | 8,577 | 8.4 | ~2,100 |
| `.claude/rules/file-structure.md` | 202 | 8,553 | 8.4 | ~2,100 |
| `.claude/rules/meta-reflection-integration.md` | 231 | 5,715 | 5.6 | ~1,400 |
| `MEMORY.md` (truncado a 200 lineas) | 154 | 7,131 | 7.0 | ~1,800 |
| **TOTAL CAPA 1** | **2,587** | **112,500** | **~110 KB** | **~28,000** |

### 2.2 Capa 2: Session-Start (lectura manual obligatoria cada sesion)

| Fichero | Lineas | Bytes | KB | ~Tokens | Nota |
|---------|--------|-------|----|---------|------|
| `state/system.yaml` | 1,579 | 86,282 | 84.3 | ~21,500 | DUPLICA parcialmente hook |
| `learning/decisions_log.yaml` | 777 | 36,377 | 35.5 | ~9,100 | CRECE RAPIDO |
| `portfolio/current.yaml` | 543 | 20,011 | 19.5 | ~5,000 | DUPLICA hook al 100% |
| `learning/principles.md` | 259 | 9,834 | 9.6 | ~2,500 | Estable |
| **TOTAL CAPA 2** | **3,158** | **152,504** | **~149 KB** | **~38,000** |

### 2.3 Hook de Inicio (inyectado antes de Capa 1)

El hook `session-start.sh` inyecta:
- Primeras 80 lineas de system.yaml (filtradas)
- portfolio/current.yaml COMPLETO (~543 lineas)
- Calendario proximos 14 dias (~40 lineas)
- Estado de mantenimiento (~12 lineas)

**Estimacion:** ~700 lineas, ~25-30 KB, ~7,000 tokens

### 2.4 Coste Total de Arranque

| Concepto | KB | ~Tokens |
|----------|-----|---------|
| Hook de inicio | ~28 | ~7,000 |
| Capa 1 (auto-loaded) | ~110 | ~28,000 |
| Capa 2 (lecturas manuales) | ~149 | ~38,000 |
| **TOTAL ARRANQUE** | **~287** | **~73,000** |

> **Contexto:** La ventana de contexto de Opus es de ~200K tokens. El arranque consume ~36% del total. Esto deja ~127K tokens para trabajo real (conversacion, outputs de agentes, ficheros de trabajo).

### 2.5 Ficheros On-Demand (se leen cuando se necesitan)

#### Skills (21 ficheros)

| Fichero | Lineas | Bytes |
|---------|--------|-------|
| agent-registry/SKILL.md | 523 | 22,140 |
| pipelines/SKILL.md | 379 | 18,547 |
| exit-protocol/SKILL.md | 346 | 10,568 |
| valuation-methods/SKILL.md | 344 | 7,639 |
| wave-system/SKILL.md | 342 | 11,991 |
| business-analysis-framework/SKILL.md | 285 | 7,928 |
| projection-framework/SKILL.md | 281 | 6,943 |
| investment-rules/SKILL.md | 270 | 8,129 |
| recommendation-context/SKILL.md | 262 | 6,112 |
| capital-deployment/SKILL.md | 238 | 8,518 |
| quality-compounders/SKILL.md | 211 | 5,994 |
| error-detector/SKILL.md | 208 | 5,267 |
| news-classification/SKILL.md | 207 | 5,768 |
| rotation-engine/SKILL.md | 193 | 5,635 |
| system-devils-advocate/SKILL.md | 186 | 6,518 |
| sector-deep-dive/SKILL.md | 175 | 3,964 |
| effectiveness-evaluation/SKILL.md | 165 | 5,070 |
| re-evaluation-protocol/SKILL.md | 144 | 4,939 |
| agent-meta-reflection/SKILL.md | 139 | 4,084 |
| system-context/SKILL.md | 124 | 5,380 |
| Otros (8 skills pequenos) | ~400 | ~12,000 |
| **TOTAL SKILLS** | **~5,422** | **~173,144** |

> Los skills son on-demand — solo se leen cuando se necesitan. El problema es que los agentes deben leer 2-5 skills cada vez, lo cual suma rapidamente.

#### State Files

| Fichero | Lineas | Bytes |
|---------|--------|-------|
| state/system.yaml | 1,579 | 86,282 |
| state/quality_universe.yaml | 1,010 | 26,787 |
| state/session_summaries_archive.yaml | 739 | 30,316 |
| state/risk_alerts.yaml | 533 | 28,724 |
| state/news_digest.yaml | 497 | 25,549 |
| state/market_pulse.yaml | 254 | 15,012 |
| state/file_moves.yaml | 111 | 4,673 |
| state/agent_coordination.yaml | 27 | 832 |
| **TOTAL STATE** | **4,750** | **~218,175** |

#### Thesis Files

| Directorio | Lineas | Bytes |
|------------|--------|-------|
| thesis/active/ (11 dirs) | ~12,353 | 612,240 |
| thesis/research/ (~65 dirs) | ~65,000+ | ~3,500,000+ |

> Las thesis se leen una por una cuando se necesitan. El mayor (MONY.L) tiene 2,937 lineas / 138 KB.

#### World Files

| Tipo | Ficheros | Lineas totales | Bytes totales |
|------|----------|----------------|---------------|
| Sector views | 24 + template | ~6,000 | ~350,000 |
| current_view.md | 1 | 426 | 28,664 |

---

## 3. Analisis de Redundancia

### 3.1 Duplicacion Critica: El Arbol de Agentes

El mismo arbol de decision de agentes aparece en **3 ficheros auto-loaded**:

1. **CLAUDE.md** lineas 295-330 — Arbol completo con buy-pipeline
2. **agent-protocol.md** lineas 40-85 — Mismo arbol, version expandida
3. **session-protocol.md** lineas 42-90 — Dashboard con agentes, lineas 225-255 — Arbol rapido

**Impacto:** ~100 lineas x 3 = ~300 lineas dedicadas a decir lo mismo.
**Solucion:** Debe estar en UN solo lugar. Los otros dos referencian.

### 3.2 Duplicacion: "Usa agentes, no hagas manual"

Esta leccion aparece como:
- Error #3 (error-patterns.md)
- Error #22 (error-patterns.md)
- Error #38, #39, #40 (error-patterns.md)
- "Diagnostico honesto" puntos 3,4 (error-patterns.md)
- Arbol de decision (agent-protocol.md)
- "REGLA CRITICA: ARBOL DE DECISION" (session-protocol.md)
- "YO ORQUESTO, LOS AGENTES EJECUTAN" (3 ficheros)

**Impacto:** ~200 lineas diciendo lo mismo de 7 formas distintas en 3 ficheros.
**Solucion:** Una regla clara en UN lugar. Los errores archivados en historico.

### 3.3 Duplicacion: Quality Score

Mencionado en:
- CLAUDE.md (12 veces) — Seccion QS completa + tiering
- error-patterns.md (9 veces) — Error #43 con tabla completa
- tools-reference.md (8 veces) — Documentacion del tool
- investment-rules/SKILL.md — Framework completo
- system-context/SKILL.md — Resumen

**Impacto:** La explicacion de QS Tool-First aparece en al menos 3 ficheros auto-loaded.

### 3.4 Duplicacion: Framework v4.0

37 menciones a "v4.0" o "Framework v4" solo en los auto-loaded. Cada fichero repite que "no hay numeros fijos" y "razonamiento sobre reglas".

### 3.5 Duplicacion: Portfolio/current.yaml

- Inyectado COMPLETO por el hook de inicio (~543 lineas)
- Leido COMPLETO manualmente en FASE 2 (~543 lineas)
- **~20 KB desperdiciados por sesion**

### 3.6 Duplicacion: system.yaml

- Inyectado parcialmente por hook (~80 lineas filtradas + calendario + maintenance)
- Leido COMPLETO manualmente en FASE 0 y FASE 2 (1,579 lineas)

---

## 4. Analisis de Crecimiento

### 4.1 Ficheros que Crecen

| Fichero | Tamano actual | Tasa de crecimiento | Proyeccion 6 meses | Proyeccion 1 ano |
|---------|---------------|---------------------|---------------------|-------------------|
| `decisions_log.yaml` | 777 lineas (36 KB) | ~43 entries/18 dias | ~4,500 lineas (200 KB) | ~16,000 lineas (720 KB) |
| `state/system.yaml` | 1,579 lineas (86 KB) | Lenta (ya purgado) | ~2,000 lineas (110 KB) | ~2,500 lineas (140 KB) |
| `error-patterns.md` | 337 lineas (24 KB) | ~43 errores en 70 sesiones | ~500 lineas (35 KB) | ~700 lineas (50 KB) |
| `quality_universe.yaml` | 1,010 lineas (27 KB) | Target 150+ empresas | ~2,000 lineas (50 KB) | ~3,000 lineas (80 KB) |
| `session-history.md` | 182 lineas (10 KB) | ~3 lineas/sesion | ~500 lineas (25 KB) | ~800 lineas (40 KB) |
| `MEMORY.md` | 154 lineas (7 KB) | Truncado a 200 | Cap 200 lineas | Cap 200 lineas |

### 4.2 Ficheros Estables

| Fichero | Tamano | Razon de estabilidad |
|---------|--------|---------------------|
| `CLAUDE.md` | 470 lineas | Se edita, no crece mucho |
| `principles.md` | 259 lineas | 9 principios, raramente cambia |
| `portfolio/current.yaml` | 543 lineas | Crece con posiciones (max ~20) |
| Skills | Varios | Se editan, no crecen mucho |

### 4.3 Proyeccion Critica: decisions_log.yaml

Este es el fichero mas preocupante:
- **Hoy:** 43 entradas, 777 lineas, 36 KB
- **6 meses:** ~450 entradas, ~4,500 lineas, ~200 KB
- **1 ano:** ~900 entradas, ~16,000 lineas, ~720 KB

A 720 KB, leer este fichero completo consumiria ~180K tokens — practicamente toda la ventana de contexto.

**Actualmente se lee COMPLETO cada sesion en FASE 0.** Esto no escala.

---

## 5. Analisis de system.yaml por Secciones

| Seccion | Lineas | Bytes | Se lee al inicio? | Necesario cada sesion? |
|---------|--------|-------|--------------------|-----------------------|
| system (metadata) | 151 | 8,251 | Si (hook parcial) | Solo version + last_session |
| calendar | 499 | 20,805 | Si (hook parcial) | Solo proximos 14 dias |
| watchlist | 291 | 14,267 | No | Solo cuando watchlist-manager |
| alerts | 43 | 5,275 | No | Solo cuando hay alertas |
| standing_orders | 303 | 15,039 | Si (FASE 3) | Si |
| macro_snapshot | 8 | 543 | No | No |
| maintenance | 128 | 6,728 | Si (hook) | Solo health-check dates |
| pipeline_tracker | 68 | 3,707 | Si (FASE 0) | Si |
| adversarial_review | 84 | 9,598 | No | No (completado) |

**Hallazgo:** Solo 3 secciones necesitan lectura cada sesion: pipeline_tracker (68 lineas), standing_orders (303 lineas), y metadata basica (10 lineas). El resto (1,198 lineas / 76%) es peso muerto en la lectura de inicio.

---

## 6. Hallazgos Criticos

### H1: El "SO" consume 36% de la RAM disponible
El coste de arranque (~73K tokens) deja solo ~127K tokens para trabajo. En sesiones WAVE largas con multiples agentes, esto es un problema real.

### H2: La misma informacion se dice 3-7 veces
El arbol de agentes, las reglas de QS, y "usa agentes no manual" estan duplicados en multiples ficheros auto-loaded. Esto desperdicia ~5-10K tokens.

### H3: portfolio/current.yaml se carga DOS veces
Hook + lectura manual. ~5K tokens desperdiciados.

### H4: decisions_log.yaml no escala
Lectura completa cada sesion. En 6 meses sera inmanejable. En 1 ano, imposible.

### H5: system.yaml es un monolito
1,579 lineas en un fichero, pero solo ~380 lineas (~24%) se necesitan cada sesion.

### H6: error-patterns.md crece sin poda
43 errores documentados, muchos con la misma leccion. Cada error nuevo se anade pero ningun error viejo se archiva.

### H7: session-protocol.md es desproporcionado
703 lineas (el fichero auto-loaded mas largo) con sub-fases y pasos que son basicamente skills disfrazados de protocol.

### H8: El hook duplica trabajo
Inyecta datos que luego se leen manualmente. El hook deberia ser la UNICA fuente, o no existir.

---

## 7. Metricas Clave para Monitoreo

| Metrica | Valor actual | Umbral de alerta | Umbral critico |
|---------|-------------|-------------------|----------------|
| Auto-loaded total | 112 KB / 28K tokens | 150 KB | 200 KB |
| Session-start total | 152 KB / 38K tokens | 200 KB | 300 KB |
| Coste arranque total | 265 KB / 66K tokens | 350 KB | 500 KB |
| decisions_log entries | 43 | 100 | 200 |
| system.yaml lineas | 1,579 | 2,000 | 3,000 |
| error-patterns lineas | 337 | 500 | 700 |
| % contexto en arranque | ~36% | 40% | 50% |

---

## 8. Conclusion

El sistema funciona HOY pero tiene problemas de escalabilidad claros:

1. **Corto plazo (0-3 meses):** Funcional pero pesado. El principal riesgo es decisions_log creciendo.
2. **Medio plazo (3-6 meses):** Problematico. decisions_log + system.yaml + error-patterns empezaran a causar compresion prematura en sesiones largas.
3. **Largo plazo (6-12 meses):** Insostenible sin refactorizacion. decisions_log solo podria consumir toda la ventana de contexto.

La refactorizacion propuesta (ver `docs/refactoring_proposal.md`) aborda cada hallazgo con cambios especificos, prioridad, y riesgo.
