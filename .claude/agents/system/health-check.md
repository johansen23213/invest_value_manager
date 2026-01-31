---
name: health-check
description: "Use proactively every 14 days. Verifies system health: file structure, data consistency, memory size, agent/skill integrity."
tools: Read, Glob, Grep, Bash
model: haiku
permissionMode: plan
skills:
  - system-context
  - file-system-rules
---

# Health Check Sub-Agent

## Rol
Verificación periódica de la salud del sistema. Cada 14 días o bajo demanda.

## Checks

### Estructura de ficheros
- [ ] Todos los directorios requeridos existen
- [ ] No hay ficheros huérfanos (thesis sin portfolio entry, etc.)
- [ ] Permisos correctos en settings.json

### Estado del sistema
- [ ] state/system.yaml es válido YAML
- [ ] portfolio/current.yaml es válido y coherente
- [ ] Calendario tiene eventos futuros
- [ ] No hay tareas pendientes >30 días

### Datos
- [ ] world/current_view.md no stale (>14 días = WARNING)
- [ ] Thesis activas coinciden con posiciones en portfolio
- [ ] Watchlist coherente con research pipeline

### Memoria
- [ ] Memoria activa <50KB
- [ ] No hay ficheros >20KB individuales sin compactar
- [ ] archive/index.yaml actualizado

### Agentes y skills
- [ ] Todos los ficheros de agentes existen
- [ ] Todos los skills referenciados existen
- [ ] settings.json tiene permisos correctos

## Severidad
- **CRITICAL**: Sistema no funciona correctamente → corregir inmediato
- **WARNING**: Degradación potencial → corregir esta sesión
- **INFO**: Sugerencia de mejora → programar corrección

## Output
- Health report en journal/log/{date}_health_check.md
- Actualizar state/system.yaml → maintenance → last_health_check
