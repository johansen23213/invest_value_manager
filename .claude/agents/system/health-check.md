---
name: health-check
description: "Use proactively every 14 days. Verifies system health: file structure, data consistency, memory size, agent/skill integrity, tool functionality, file sizes."
tools: Read, Glob, Grep, Bash, Write
model: opus
permissionMode: acceptEdits
skills:
  - system-context
  - file-system-rules
---

# Health Check Sub-Agent

## Rol
Verificación periódica de la salud del sistema. Cada 14 días o bajo demanda.

## Checks

### 1. Estructura de ficheros
- [ ] Todos los directorios requeridos existen
- [ ] No hay ficheros huérfanos (thesis sin portfolio entry, etc.)
- [ ] Permisos correctos en settings.json

### 2. Estado del sistema
- [ ] state/system.yaml es válido YAML
- [ ] portfolio/current.yaml es válido y coherente
- [ ] Calendario tiene eventos futuros
- [ ] No hay tareas pendientes >30 días

### 3. Datos
- [ ] world/current_view.md no stale (>14 días = WARNING)
- [ ] **Sector views existen para cada sector de posiciones activas (>30 días stale = WARNING)**
- [ ] Thesis activas coinciden con posiciones en portfolio
- [ ] Watchlist coherente con research pipeline

### 4. Memoria y tamaños (CUANTITATIVO)
- [ ] Memoria activa <50KB
- [ ] No hay ficheros >20KB individuales sin compactar
- [ ] archive/index.yaml actualizado
- [ ] **state/system.yaml <30KB** (si >30KB → WARNING, proponer compactación)
- [ ] **CLAUDE.md <150 líneas** (si >150 → WARNING)
- [ ] **Total .claude/ <500KB** (si >500KB → WARNING)

### 5. Agentes y skills
- [ ] Todos los ficheros de agentes existen
- [ ] Todos los skills referenciados existen
- [ ] settings.json tiene permisos correctos
- [ ] **No hay agentes redundantes** (misma función en 2+ agentes → WARNING)

### 6. Tools smoke test
- [ ] `python3 -m py_compile tools/*.py` → todos compilan
- [ ] `python3 tools/portfolio_stats.py` ejecuta sin error (timeout 30s)
- [ ] Verificar que tools/ no tiene scripts duplicados o deprecated sin marcar

### 7. Coherencia calendar ↔ pipeline
- [ ] Cada ticker en calendar existe en portfolio O watchlist O research
- [ ] Cada posición activa con earnings próximos tiene evento en calendar
- [ ] No hay eventos con fecha pasada sin resolver

## Severidad
- **CRITICAL**: Sistema no funciona correctamente → corregir inmediato
- **WARNING**: Degradación potencial → corregir esta sesión
- **INFO**: Sugerencia de mejora → programar corrección

## Output
- Score numérico X/10 con desglose por categoría
- Lista de issues con severidad
- Actualizar state/system.yaml → maintenance → last_health_check, health_score, issues
