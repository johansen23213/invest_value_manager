# Protocolo de Carga del Sistema

## Propósito

Definir QUÉ archivos Claude debe leer CUÁNDO, optimizando uso de contexto y velocidad de arranque.

**Meta:** Arranque <60 segundos, contexto activo <50KB.

---

## FASE 1: ARRANQUE (SIEMPRE)

**Ejecutar al inicio de CADA sesión, sin excepción.**

```
ORDEN DE CARGA:

1. state/system.yaml (~3KB)
   ├── Estado general
   ├── Calendario próximos 7 días
   ├── Alertas activas
   ├── Work in progress
   └── Last session summary

2. portfolio/current.yaml (~1KB)
   ├── Posiciones actuales
   ├── Cash disponible
   └── Transactions historial

3. portfolio/target_allocation.yaml (~4KB)
   ├── Estructura target
   ├── Gaps actuales
   ├── Triggers rebalanceo
   └── Estado construcción portfolio

4. learning/system_config.yaml (~5KB)
   ├── Parámetros sistema
   ├── Límites diversificación
   ├── Reglas aprendidas
   └── Configuración rebalanceo

5. world/current_view.md (~4-6KB)
   ├── Visión macro actual
   ├── VERIFICAR: last_update
   ├── Si >7 días → TRIGGER update
   └── Si >14 días → ALERTA CRÍTICA

6. thesis/active/* (~3KB por posición)
   ├── SOLO posiciones con holdings
   ├── Típicamente: 2-5 archivos al inicio
   └── Crece a 16-20 archivos en portfolio completo

TOTAL FASE 1: ~20-40KB (depende de posiciones activas)
TIEMPO: <60 segundos
```

**IMPORTANTE:**
- CLAUDE.md (891 líneas) = leerlo SOLO al primer arranque del día
- Skills .md = leerlos cuando se invocan, NO en arranque
- NO cargar watchlist en arranque (solo si relevante)

---

## FASE 2: CONTEXTO BAJO DEMANDA

**Cargar SOLO cuando necesario para tarea específica.**

### Si ejecuto `/analyze {TICKER}`

```
Cargar:
1. world/current_view.md (si no en Fase 1)
2. thesis/watchlist/{TICKER}/ (si existe análisis previo)
3. thesis/research/{TICKER}/ (si existe)
4. archive/thesis/closed/{TICKER}.yaml (si inversión previa)

NO cargar:
- Otras thesis en watchlist
- Decisiones históricas
- Reviews pasados
```

### Si ejecuto `/decide`

```
Cargar:
1. Thesis relevante (que se va a decidir)
2. portfolio/target_allocation.yaml (gaps, estructura)
3. world/current_view.md (contexto macro)

NO cargar:
- Otras thesis
- Historia completa
```

### Si ejecuto `/review`

```
Cargar:
1. Todas las thesis/active/*
2. journal/decisions/ (últimos 3 meses)
3. journal/reviews/ (últimos 2-3)
4. learning/lessons.yaml (si hay lecciones recientes)

NO cargar:
- Archive completo
- Watchlist
```

### Si ejecuto `/macro`

```
Cargar:
1. world/current_view.md (para actualizar)
2. world/updates/ (últimos 2-3 meses)
3. state/system.yaml (calendario eventos)

NO cargar:
- Thesis
- Portfolio details
- Decisiones históricas
```

### Si ejecuto `/learn`

```
Cargar:
1. learning/lessons.yaml (completo)
2. learning/system_config.yaml
3. archive/investment_history.md (resumen)
4. Posiciones cerradas relevantes

NO cargar:
- Thesis completas
- Journal completo
```

### Si ejecuto `/rebalance`

```
Cargar:
1. portfolio/current.yaml
2. portfolio/target_allocation.yaml
3. learning/system_config.yaml (thresholds)
4. Todas thesis/active/* (para evaluar conviction)

NO cargar:
- Watchlist
- Historia
```

### Si ejecuto `/compact`

```
Cargar:
1. TODO (necesita ver qué hay para compactar)
2. state/system.yaml (maintenance section)

Proceso:
- Lee todos los archivos a compactar
- Crea resúmenes
- Mueve a archive/
```

---

## FASE 3: HISTORIA (SOLO SI NECESARIO)

**Cargar SOLO si usuario pregunta específicamente o necesito contexto histórico.**

### Si usuario pregunta "¿Qué pasó con {TICKER}?"

```
Cargar:
1. archive/index.yaml (buscar ticker)
2. archive/thesis/closed/{TICKER}.yaml (resumen)
3. Si necesita más detalle → buscar en archive/decisions/
```

### Si usuario pide "Historial completo"

```
Cargar:
1. archive/investment_history.md (resumen ejecutivo)
2. Si necesita detalles año específico → archive/decisions/{year}_summary.yaml
```

### NUNCA cargar archive/ en:
- Arranque normal
- Análisis de nuevas empresas
- Decisiones de compra/venta
- Rebalanceos

---

## VERIFICACIONES CRÍTICAS

### Al arranque, SIEMPRE verificar:

```python
# 1. World view stale?
if days_since_update(world/current_view.md) > 7:
    WARN("World view desactualizado")
    if days > 14:
        ALERT("CRÍTICO: Stale data >14 días")
        EXECUTE mini-update BEFORE any analysis

# 2. Rebalanceo triggers?
portfolio_state = load(portfolio/target_allocation.yaml)
if portfolio_state.triggers_active:
    NOTIFY("⚠️ Triggers de rebalanceo activos")
    LIST triggers

# 3. Eventos próximos?
events_next_7_days = calendar.next_week()
if events_next_7_days:
    NOTIFY("📅 Eventos próximos")
    LIST events

# 4. Alertas precio?
if price_alerts_active:
    CHECK precios actuales
    NOTIFY si trigger

# 5. Memoria excesiva?
if active_memory > 50KB:
    WARN("Memoria activa alta, considerar /compact")
if active_memory > 100KB:
    ALERT("CRÍTICO: Ejecutar /compact obligatorio")
```

---

## OPTIMIZACIÓN DE CONTEXTO

### Reglas de Carga Eficiente

1. **Lazy Loading:**
   - NO cargar "por si acaso"
   - Cargar SOLO cuando necesario
   - Ejemplo: watchlist cargado solo si voy a explorar compras

2. **Incremental Loading:**
   - Cargar resúmenes primero
   - Si necesito detalle → cargar archivo completo
   - Ejemplo: lessons.yaml tiene resumen top 10 + detalle completo

3. **Scope Limiting:**
   - journal/decisions/ → últimos 3 meses, NO todo
   - world/updates/ → últimos 2 meses, NO todo
   - reviews → últimos 2-3, NO todos

4. **Compression:**
   - Archive siempre en formato compacto
   - Thesis cerradas: resumen 5 líneas, NO análisis completo
   - Decisiones antiguas: YAML, NO markdown verboso

---

## EJEMPLO SESIÓN TÍPICA

### Arranque normal (portfolio ya construido)

```
CARGAR:
- state/system.yaml (3KB)
- portfolio/current.yaml (2KB)
- portfolio/target_allocation.yaml (4KB)
- learning/system_config.yaml (6KB)
- world/current_view.md (5KB) → Verificar last_update
- thesis/active/* (18 posiciones × 3KB = 54KB) → Esto será el bulk

TOTAL: ~74KB

VERIFICAR:
- World view: 3 días desde update → OK
- Triggers rebalanceo: Ninguno activo → OK
- Eventos próximos: Shell earnings en 5 días → NOTIFY
- Alertas: Ninguna activada → OK

PRESENTAR:
"Portfolio: €10,000, 18 posiciones, 88% invertido, 12% cash
 Próximos eventos: Shell earnings 5-feb
 No hay acciones pendientes hoy."
```

### Usuario: "Analiza Stellantis"

```
CARGAR ADICIONAL:
- thesis/watchlist/STLAM/ (si existe) (~3KB)
- O buscar en web si nuevo

NO CARGAR:
- Otras watchlist
- Historia

EJECUTAR:
/analyze STLAM
→ Genera thesis completa
→ Ejecuta /decide automáticamente
→ Presenta recomendación
```

### Usuario: "Rebalancea portfolio"

```
YA TENGO CARGADO:
- portfolio/current.yaml
- portfolio/target_allocation.yaml
- thesis/active/* (todas)

EJECUTAR:
/rebalance
→ Calcula desviaciones
→ Identifica triggers
→ Propone trades
→ Presenta plan
```

---

## LÍMITES DE MEMORIA

### Targets

- **Fase 1 (arranque):** <50KB ideal, <75KB aceptable
- **Fase 1+2 (con análisis):** <100KB ideal, <150KB aceptable
- **NUNCA exceder:** 200KB contexto activo

### Si excedo límites

```
SI 50-100KB:
   → OK, monitorear

SI 100-150KB:
   → WARNING: Considerar /compact pronto
   → Revisar si estoy cargando archivos innecesarios

SI 150-200KB:
   → ALERT: Ejecutar /compact recomendado
   → Posiblemente thesis muy largas, compactar

SI >200KB:
   → CRITICAL: Ejecutar /compact OBLIGATORIO
   → Sistema puede empezar a fallar
```

---

## MANTENIMIENTO

### Semanalmente

- Verificar tamaño archivos Fase 1
- Si alguno >10KB → revisar por qué
- thesis/active/* creciendo → normal si portfolio crece

### Mensualmente

- Ejecutar /compact
- Archivar decisiones >3 meses
- Compactar lecciones >30 entradas
- Regenerar resúmenes ejecutivos

### Anualmente

- Full compactación
- Crear resumen año
- Archivar todo >1 año
- Reset counters

---

## DEBUGGING

### Si sesión lenta (>2 minutos arranque)

```
CHECK:
1. ¿Cuántos archivos thesis/active/*?
   → Si >25, portfolio demasiado grande

2. ¿Tamaño world/current_view.md?
   → Si >10KB, compactar

3. ¿Tamaño state/system.yaml?
   → Si >10KB, compactar (mover eventos antiguos)

4. ¿Estoy cargando archive sin querer?
   → Verificar lógica de carga
```

### Si faltan datos

```
CHECK:
1. ¿Estoy en fase correcta?
   → Fase 1 no tiene watchlist, es normal

2. ¿Skill cargó dependencias?
   → Verificar protocolo skill específico

3. ¿Archivo existe?
   → Verificar path, puede ser primera vez
```

---

## CHANGELOG

- **2026-01-27:** V2.0 - Protocolo inicial creado
- **Future:** Ajustar según experiencia real con portfolio 18+ posiciones
