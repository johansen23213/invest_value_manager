---
name: memory-management-rules
description: 3-layer memory system rules. Active <50KB, recent on-demand, archive query-only.
user-invocable: false
disable-model-invocation: false
---

# Memory Management Rules Skill

## 3 Capas
| Capa | Tamaño | Carga |
|------|--------|-------|
| Activa | <50KB | SIEMPRE |
| Reciente | <500KB | Bajo demanda |
| Archivo | Ilimitado | Solo consulta |

## Compactación
| Frecuencia | Qué |
|-----------|-----|
| Mensual | Archivar decisiones/reviews >3 meses |
| Anual | Resumen del año, compactar lecciones |

## Umbrales
- Capa 1 >50KB → WARNING
- Capa 1 >80KB → CRÍTICO
- Fichero individual >20KB → Considerar compactar

## Búsqueda eficiente
1. Consultar archive/index.yaml (1KB)
2. Cargar solo fichero específico necesario
3. NO cargar toda la historia
