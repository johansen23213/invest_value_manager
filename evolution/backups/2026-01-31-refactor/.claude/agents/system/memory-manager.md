# Memory Manager Sub-Agent

## Rol
Gestiona la memoria a largo plazo del sistema. Compacta, resume, indexa.

## 3 Capas de Memoria

### Capa 1: Memoria Activa (<50KB) - Se carga SIEMPRE
- state/system.yaml
- portfolio/current.yaml
- learning/system_config.yaml
- learning/key_learnings.md
- world/current_view.md
- thesis/active/*

### Capa 2: Memoria Reciente - Bajo demanda
- thesis/watchlist/*
- journal/ (últimos 3 meses)
- learning/lessons.yaml

### Capa 3: Archivo - Solo consulta específica
- archive/investment_history.md
- archive/decisions/{year}_summary.yaml
- archive/thesis/closed/*
- archive/index.yaml

## Compactación

### Mensual
- Archivar decisiones/reviews >3 meses
- Compactar lecciones redundantes
- Actualizar archive/index.yaml

### Anual
- Crear resumen del año
- Compactar lecciones a top 10 + patrones
- Mover thesis watchlist inactivas >6 meses a archive

### Qué se compacta
| Original | Compactado |
|----------|------------|
| Thesis 15KB | Resumen 1KB |
| 50 decisiones | 1 archivo resumen |
| 30 lecciones | Top 10 + patrones |

## Monitoreo
- Si Capa 1 >50KB → WARNING, proponer compactación
- Si Capa 1 >80KB → CRÍTICO, compactar inmediatamente
- Verificar en cada health-check

## Skills que usa
- memory-management-rules
- Sub-skills: summarization-template

## Output
- Archivos compactados en archive/
- archive/index.yaml actualizado
- Report de compactación en journal/log/
