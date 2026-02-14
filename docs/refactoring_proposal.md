# Propuesta de Refactorizacion para Escalabilidad

> Sesion 71 | 2026-02-14
> Basada en: `docs/audit_context_weight.md`
> Objetivo: Reducir coste de arranque de ~73K tokens a ~35K tokens sin perder funcionalidad.
> Principio: El sistema debe funcionar igual o mejor HOY y escalar a 12+ meses de operacion.

---

## 0. Principios de Diseno de la Refactorizacion

1. **Lo que no se necesita cada sesion, no se carga cada sesion.** Mover a on-demand.
2. **Una verdad, un lugar.** Eliminar duplicacion. Referenciar, no copiar.
3. **Los ficheros que crecen deben tener politica de rotacion.**
4. **El arranque debe ser ligero.** El "SO" no puede ser mas grande que el "programa".
5. **Preservar funcionalidad.** Mi yo futuro debe poder hacer exactamente lo mismo, con menos peso.
6. **Cambios incrementales.** No refactorizar todo de golpe. Priorizar por impacto.

---

## 1. CLAUDE.md: Dieta Agresiva

### Estado Actual
- 470 lineas, 19 KB, ~4,800 tokens
- Contiene: rol, framework v4.0, QS, principios (resumen), capital deployment, WAVE, rotation, pipelines, proceso decision, EXIT protocol, arquitectura multi-agente, self-check, validacion consistencia, meta-reflexion, capacidades, permisos, referencias rapidas, diferencia v3/v4

### Problema
CLAUDE.md deberia ser un **indice conciso** que dice QUE hacer y DONDE encontrar como hacerlo. En cambio, es una **enciclopedia** que explica el QUE, el COMO, y el POR QUE, duplicando contenido de rules y skills.

### Propuesta: CLAUDE.md v5.0 (~150-180 lineas, ~6 KB, ~1,500 tokens)

```
Estructura propuesta:
1. Rol (5 lineas) — Una linea de contexto, no un parrafo
2. Framework v4.0 Core (10 lineas) — Solo la filosofia, no la tabla comparativa
3. Quality Score (5 lineas) — Solo la tabla de tiers, referencia a skill
4. Principios (10 lineas) — Solo los 9 nombres con pregunta guia, ref a principles.md
5. Arquitectura (15 lineas) — Solo la lista de agentes por dominio, ref a agent-protocol
6. Tools (5 lineas) — Solo la lista de nombres, ref a tools-reference
7. Permisos (5 lineas)
8. Referencias (tabla ya existente, compactar)
```

### Que se ELIMINA de CLAUDE.md

| Seccion actual | Lineas | Destino |
|----------------|--------|---------|
| "System admin CEO Message" | 25 | ELIMINAR — no aporta contexto tecnico util |
| Framework v4.0 tabla comparativa | 15 | Ya esta en principles.md |
| QS explicacion detallada + regla Tool-First | 20 | Ya esta en investment-rules skill |
| Principios 1-9 resumen detallado | 40 | Ya esta en principles.md |
| Capital Deployment Machine detalle | 20 | Ya esta en capital-deployment skill |
| WAVE System detalle | 15 | Ya esta en wave-system skill |
| Rotation Engine detalle | 12 | Ya esta en rotation-engine skill |
| Pipelines tabla completa | 20 | Ya esta en pipelines skill |
| Proceso de Decision v4.0 (diagrama) | 25 | Ya esta en principles.md |
| EXIT Protocol detalle | 20 | Ya esta en exit-protocol skill |
| Arbol de agentes completo | 30 | Ya esta en agent-protocol.md |
| Self-Check v4.0 | 15 | Mover a session-protocol |
| Validacion de Consistencia | 20 | Mover a session-protocol |
| Meta-Reflexion Colectiva | 15 | Ya esta en meta-reflection-integration rule |
| Diferencia v3/v4 | 15 | ELIMINAR — v3 ya no existe, no necesita comparacion |
| **TOTAL ELIMINABLE** | **~307 lineas** | |

### Ahorro estimado: ~12 KB, ~3,000 tokens

### Riesgo: BAJO
Todo lo eliminado ya existe en otro lugar. CLAUDE.md solo deja de duplicar.

---

## 2. Rules: Consolidar y Podar

### 2.1 error-patterns.md: Archivar errores antiguos

**Estado actual:** 337 lineas, 24 KB — el 2do fichero auto-loaded mas pesado.

**Problema:** 43 errores documentados. Muchos son historicos (sesiones 19-26) que ya no se cometen. Varios ensenen la misma leccion (errores #3, #22, #38, #39, #40 todos dicen "usa agentes"). La seccion "Diagnostico Honesto" repite errores ya listados.

**Propuesta:**

1. **Mantener en auto-loaded solo los 10-12 errores mas criticos y recientes** (~80 lineas)
2. **Archivar el resto** en `learning/error_patterns_archive.md` (on-demand)
3. **Consolidar errores duplicados:** #3, #22, #38, #39, #40 → 1 entrada: "Delegar a agentes"
4. **Eliminar "Diagnostico Honesto"** — repite puntos 1-8 que ya estan como errores

**Errores a mantener en auto-loaded (los que aun puedo cometer):**
- #7 Popularity bias
- #12 Constraint check antes de ADD
- #13 Frameworks pre-earnings
- #16 Entender negocio antes de comprar
- #30/42 Sector view antes de comprar
- #37 No hardcodear reglas en tools
- #41 Completar ciclo post-analisis
- #43 QS Tool-First
- Consolidado: "Delegar a agentes" (reemplaza #3, #22, #38-40)

**Formato compacto propuesto por error:**
```
### [N]. [Titulo] (Sesion [X])
[1-2 lineas de leccion + regla]
```

**Ahorro estimado:** De 337 a ~100 lineas. ~16 KB → ~6 KB. ~4,000 tokens ahorrados.

### 2.2 session-protocol.md: Separar workflow de dashboard

**Estado actual:** 703 lineas, 23 KB — el fichero auto-loaded MAS pesado.

**Problema:** Contiene 3 cosas distintas mezcladas:
1. Reglas de sesion (que hacer al inicio/final) — necesario cada sesion
2. Dashboard template (formato de presentacion) — solo cuando modo dashboard
3. Workflows detallados de cada FASE — son basicamente skills

**Propuesta:**

1. **Mantener en auto-loaded:** Solo reglas de flujo (~150 lineas)
   - Modo de sesion (dashboard/wave/directo) — 20 lineas
   - FASE 0 calibracion — 30 lineas (compacto)
   - Lista de FASEs con que hacer en cada una — 50 lineas (referencia, no detalle)
   - Cierre de sesion — 20 lineas
   - Mentalidad de gestor — 10 lineas
   - Anti-sesgo check — 10 lineas

2. **Mover a skill `session-dashboard`:** Template del dashboard completo (agentes, protocolos, formato)
3. **Mover a skill `session-phases`:** Detalle de cada FASE (2, 2.5, 2.7, 3, 4, 5) con sub-pasos
4. **Eliminar:** Duplicacion del arbol de agentes (ya en agent-protocol)

**Ahorro estimado:** De 703 a ~150 lineas. ~23 KB → ~5 KB. ~4,500 tokens ahorrados.

### 2.3 agent-protocol.md: Compactar

**Estado actual:** 203 lineas, 8.5 KB

**Problema menor:** Arbol de decision + instrucciones v4.0 para agentes + verificacion post-agente. Razonablemente conciso pero el arbol esta duplicado en CLAUDE.md y session-protocol.

**Propuesta:**
- Se convierte en la UNICA fuente del arbol de agentes
- Eliminar la duplicacion de CLAUDE.md y session-protocol
- Compactar instrucciones v4.0 (son repetitivas)
- De 203 a ~120 lineas

**Ahorro estimado:** ~3 KB, ~800 tokens

### 2.4 meta-reflection-integration.md: Compactar

**Estado actual:** 231 lineas, 5.7 KB

**Problema:** Muy detallado para algo que se resume en: "Lee META-REFLECTION, actua sobre dudas/sugerencias/anomalias, no ignores."

**Propuesta:**
- Compactar a ~50 lineas con checklist y reglas esenciales
- Mover ejemplo practico (NVO) y protocolo detallado a skill

**Ahorro estimado:** ~4 KB, ~1,000 tokens

### 2.5 tools-reference.md: Mantener pero compactar

**Estado actual:** 287 lineas, 16 KB

**Problema moderado:** La documentacion de cada tool es util pero verbose. Los ejemplos de bash commands son necesarios. Las reglas de tools al final son redundantes con CLAUDE.md.

**Propuesta:**
- Eliminar reglas duplicadas al final (~20 lineas)
- Compactar descripciones (cada tool: 1 linea descripcion + ejemplos bash)
- De 287 a ~200 lineas

**Ahorro estimado:** ~4 KB, ~1,000 tokens

### 2.6 file-structure.md: Mantener

**Estado actual:** 202 lineas, 8.5 KB

**Evaluacion:** Contiene la tabla de sector views (util) y protocolos de dependencias. Relativamente conciso. No es prioridad de refactorizacion.

**Propuesta:** Sin cambios significativos. Quizas compactar la seccion de dependencias que es verbose.

---

## 3. State Files: Partir el Monolito

### 3.1 system.yaml: Partir en ficheros especializados

**Estado actual:** 1,579 lineas, 86 KB — se lee completo o casi completo cada sesion

**Propuesta: Partir en ficheros independientes**

| Fichero nuevo | Contenido actual en system.yaml | Lineas | Se lee cada sesion? |
|---------------|--------------------------------|--------|---------------------|
| `state/system.yaml` (reducido) | metadata, framework status, last_session_summary | ~100 | Si (hook) |
| `state/calendar.yaml` | Todas las entradas de calendario | ~500 | Solo proximos 14 dias |
| `state/standing_orders.yaml` | Standing orders activos | ~300 | Si (FASE 3) |
| `state/watchlist.yaml` | Ya existe pero watchlist entries estan en system.yaml | ~290 | Solo watchlist-manager |
| `state/pipeline_tracker.yaml` | Pipeline tracker | ~70 | Si (FASE 0) |
| `state/maintenance.yaml` | Health check, memory, agents count | ~130 | Solo health-check |

**Impacto en lectura de inicio:**
- Antes: Leer system.yaml completo = 1,579 lineas / 86 KB
- Despues: Leer system.yaml (100) + pipeline_tracker (70) + standing_orders (300) = 470 lineas / ~25 KB

**Ahorro por sesion:** ~60 KB, ~15,000 tokens

**Riesgo:** MEDIO — Hay que actualizar todos los agentes y tools que leen/escriben system.yaml. Lista de afectados:
- calendar-manager (lee/escribe calendar)
- watchlist-manager (lee/escribe watchlist)
- risk-sentinel (lee/escribe alerts)
- portfolio-ops (lee/escribe standing_orders, calendar)
- health-check (lee maintenance)
- session-start.sh hook (lee varias secciones)
- Yo mismo (orchestrator) en multiples FASEs

**Mitigacion:** Crear un script de migracion que parta el fichero y verificar que cada agente referencia el fichero correcto.

### 3.2 Eliminar adversarial_review de system.yaml

**Estado actual:** 84 lineas, ~10 KB — proyecto COMPLETADO

**Propuesta:** Mover a `state/session_summaries_archive.yaml` o eliminar. Ya esta documentado en MEMORY.md y decisions_log.

**Ahorro:** 84 lineas, ~10 KB

---

## 4. Learning Files: Politica de Rotacion

### 4.1 decisions_log.yaml: Rotacion obligatoria

**Estado actual:** 777 lineas, 36 KB, 43 entradas
**Proyeccion 1 ano:** ~16,000 lineas, 720 KB — INMANEJABLE

**Propuesta: Sistema de rotacion con ventana deslizante**

1. **decisions_log.yaml** mantiene solo las ultimas 30 entradas (~500 lineas, ~23 KB)
2. **learning/decisions_archive.yaml** recibe las entradas mas antiguas
3. **Rotacion automatica:** Cuando > 40 entradas, mover las 10 mas antiguas al archivo
4. **Patrones extraidos:** Antes de archivar, extraer patron de sizing/razonamiento y mantener en una seccion `patterns:` al inicio del fichero (~50 lineas fijas con patrones agregados)

**Ejemplo de patron extraido:**
```yaml
patterns:
  sizing_by_tier:
    tier_a: "Rango historico 3-5%. Contexto: alta conviccion, MoS tipico 15-30%"
    tier_b: "Rango historico 3-4%. Contexto: conviccion media, MoS tipico 20-35%"
    tier_c: "Rango historico 2-4%. Contexto: special situation, MoS tipico 30-40%"
  recent_decisions:
    last_buy: { ticker: "ACGL", date: "2026-02-14", sizing: "4%", mos: "20%" }
    last_sell: { ticker: "UHS", date: "2026-02-11", reason: "above FV, Medicaid risk" }
```

**Ahorro por sesion:** En 6 meses, leer 500 lineas vs 4,500 = ~170 KB ahorrados.

**Riesgo:** BAJO — Los precedentes antiguos raramente se consultan. Los patrones capturan la esencia.

### 4.2 Error patterns: Misma politica

Ya cubierto en seccion 2.1. Mantener 10-12 activos, archivar el resto.

---

## 5. Hook de Inicio: Optimizar o Eliminar

### Estado Actual
El hook inyecta datos que luego se leen manualmente. Duplicacion pura en portfolio/current.yaml.

### Opcion A: Optimizar el Hook (RECOMENDADA)

Convertir el hook en la UNICA fuente de estado de inicio. No leer manualmente nada que el hook ya inyecte.

**Hook optimizado inyectaria:**
```
1. Session number + last session date (2 lineas)
2. Portfolio resumen (cash + posiciones con ticker, invested, FV, conviction) (~50 lineas)
3. Pipeline tracker (~20 lineas)
4. Standing orders con distancia a trigger (~30 lineas)
5. Calendario proximos 7 dias (~15 lineas)
6. Alertas activas (~10 lineas)
```

**Total hook optimizado:** ~130 lineas, ~5 KB, ~1,300 tokens
**Eliminaria:** Lectura manual de portfolio/current.yaml y system.yaml al inicio

### Opcion B: Eliminar el Hook

No inyectar nada. Leer manualmente solo lo necesario en FASE 0.
- Pro: Sin duplicacion
- Con: Mas lecturas manuales, mas tool calls

**Recomendacion:** Opcion A. Un hook conciso y bien disenado reemplaza multiples lecturas manuales.

---

## 6. MEMORY.md: Mantener Compacto

### Estado Actual
154 lineas, 7 KB. Truncado a 200 lineas por el sistema. Funciona bien.

### Propuesta
- Seguir como esta. El truncamiento a 200 lineas es una buena restriccion natural.
- Mover datos de estado (portfolio snapshot, earnings pipeline, standing orders) FUERA de MEMORY.md
- MEMORY.md deberia contener solo: principios aprendidos, precedentes clave, conocidos issues, y estado a muy alto nivel (2-3 lineas)
- Los datos de estado detallados deben estar en los state files (que el hook inyecta)

**Ahorro potencial:** ~2 KB si se mueven los datos de estado. Pero marginal.

---

## 7. Skills: Sin Cambios Urgentes

Los skills son on-demand y no afectan al arranque. Estan bien dimensionados.

Unica recomendacion: crear un `skills/index.md` que liste todos los skills con descripcion de 1 linea, para que yo (o agentes) podamos encontrar el skill correcto sin tener que recordar o listar todos.

---

## 8. Resumen de Impacto

### Antes vs Despues

| Componente | Antes (tokens) | Despues (tokens) | Ahorro |
|------------|---------------|-------------------|--------|
| CLAUDE.md | ~4,800 | ~1,500 | -3,300 |
| session-protocol.md | ~5,800 | ~1,800 | -4,000 |
| error-patterns.md | ~5,900 | ~1,800 | -4,100 |
| agent-protocol.md | ~2,100 | ~1,500 | -600 |
| meta-reflection.md | ~1,400 | ~600 | -800 |
| tools-reference.md | ~4,100 | ~3,100 | -1,000 |
| file-structure.md | ~2,100 | ~2,100 | 0 |
| MEMORY.md | ~1,800 | ~1,500 | -300 |
| **Subtotal auto-loaded** | **~28,000** | **~13,900** | **-14,100** |
| Hook optimizado | ~7,000 | ~1,300 | -5,700 |
| system.yaml lectura | ~21,500 | ~6,000 | -15,500 |
| decisions_log lectura | ~9,100 | ~6,000 | -3,100 |
| portfolio lectura | ~5,000 | 0 (via hook) | -5,000 |
| principles.md lectura | ~2,500 | ~2,500 | 0 |
| **Subtotal session-start** | **~45,100** | **~15,800** | **-29,300** |
| **TOTAL ARRANQUE** | **~73,000** | **~29,700** | **-43,300 (-59%)** |

### Proyeccion de Escalabilidad

| Periodo | Sin refactorizar | Con refactorizacion |
|---------|-----------------|---------------------|
| Hoy | 73K tokens (36%) | 30K tokens (15%) |
| 6 meses | ~120K tokens (60%) | ~35K tokens (18%) |
| 1 ano | ~200K+ tokens (100%) | ~40K tokens (20%) |

---

## 9. Plan de Implementacion

### Fase 1: Quick Wins (1 sesion, riesgo bajo)

| # | Cambio | Impacto | Riesgo |
|---|--------|---------|--------|
| 1.1 | Podar CLAUDE.md de 470 a ~170 lineas | -3,300 tokens | Bajo |
| 1.2 | Archivar errores antiguos de error-patterns.md | -4,100 tokens | Bajo |
| 1.3 | Eliminar adversarial_review de system.yaml | -10 KB | Nulo |
| 1.4 | Compactar meta-reflection.md | -800 tokens | Bajo |
| **Subtotal Fase 1** | | **~-8,200 tokens** | |

### Fase 2: Refactorizacion Media (1-2 sesiones, riesgo medio)

| # | Cambio | Impacto | Riesgo |
|---|--------|---------|--------|
| 2.1 | Refactorizar session-protocol.md (separar dashboard + phases a skills) | -4,000 tokens | Medio |
| 2.2 | Implementar rotacion en decisions_log.yaml | -3,100 tokens ahora, previene explosion | Bajo |
| 2.3 | Compactar tools-reference.md | -1,000 tokens | Bajo |
| 2.4 | Compactar agent-protocol.md, eliminar duplicacion con CLAUDE.md | -600 tokens | Bajo |
| **Subtotal Fase 2** | | **~-8,700 tokens** | |

### Fase 3: Refactorizacion Profunda (2-3 sesiones, riesgo medio-alto)

| # | Cambio | Impacto | Riesgo |
|---|--------|---------|--------|
| 3.1 | Partir system.yaml en ficheros especializados | -15,500 tokens | Medio-Alto |
| 3.2 | Optimizar hook de inicio (conciso, reemplaza lecturas manuales) | -10,700 tokens | Medio |
| 3.3 | Actualizar todos los agentes que leen/escriben system.yaml | Necesario para 3.1 | Medio |
| 3.4 | Limpiar MEMORY.md (mover estado a state files) | -300 tokens | Bajo |
| **Subtotal Fase 3** | | **~-26,500 tokens** | |

### Resumen de Fases

| Fase | Sesiones | Ahorro acumulado | % de ventana liberada |
|------|----------|------------------|----------------------|
| Fase 1 | 1 | -8,200 tokens | 4% |
| Fase 2 | 1-2 | -16,900 tokens | 8.5% |
| Fase 3 | 2-3 | -43,400 tokens | 22% |

---

## 10. Riesgos y Mitigaciones

### R1: Mi yo futuro no encuentra informacion que se movio
**Mitigacion:** Cada seccion eliminada/movida debe tener un comentario `# Moved to [destino]` en el fichero original. Mantener la tabla de Referencias Rapidas en CLAUDE.md actualizada.

### R2: Agentes fallan al leer ficheros partidos de system.yaml
**Mitigacion:** Crear script de migracion. Verificar cada agente uno por uno. Hacer la particion en una sesion dedicada con testing.

### R3: Se pierde informacion al archivar decisiones/errores
**Mitigacion:** Extraer patrones ANTES de archivar. El archivo sigue accesible on-demand. No se borra nada, solo se mueve.

### R4: CLAUDE.md queda tan compacto que pierdo contexto esencial
**Mitigacion:** Mantener las Referencias Rapidas (la tabla de "Necesito... → Ver..."). Esto actua como indice para encontrar todo lo que se movio. Probar en 2-3 sesiones y ajustar si hace falta.

### R5: El hook optimizado no inyecta algo necesario
**Mitigacion:** Disenar el hook nuevo con un flag de debug que muestre que se inyecto. Probar en sesion controlada.

---

## 11. Metricas de Exito

La refactorizacion es exitosa si:

1. **Coste de arranque < 35K tokens** (vs 73K actual)
2. **Funcionalidad identica:** Dashboard, WAVE, vigilancia, pipelines funcionan igual
3. **Crecimiento controlado:** decisions_log nunca supera 40 entradas activas
4. **Sin perdida de informacion:** Todo lo archivado es accesible on-demand
5. **Tiempo de arranque similar:** No mas de 3-4 lecturas manuales al inicio

---

## 12. Recomendacion Final

**Empezar por Fase 1 inmediatamente.** Son cambios de bajo riesgo con alto impacto que se pueden hacer en esta misma sesion o la siguiente. El ahorro de ~8,200 tokens es significativo y las probabilidades de regresion son minimas.

**Planificar Fase 2 para la sesion siguiente.** Requiere algo mas de cuidado pero sigue siendo bajo riesgo.

**Fase 3 requiere una sesion dedicada.** Partir system.yaml afecta a multiples agentes y necesita testing. Pero es donde esta el mayor ahorro (26,500 tokens) y la clave para la escalabilidad a largo plazo.

El objetivo final: un sistema donde el "SO" consuma ~15% de la ventana de contexto (30K de 200K), dejando el 85% para trabajo productivo. Esto permitiria sesiones WAVE de 8+ horas sin compresion prematura y escalaria a anos de operacion.
