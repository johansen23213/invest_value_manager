---
name: agent-registry
description: Complete registry of all agents, their responsibilities, dependencies, and consistency protocol
user-invocable: false
---

# Agent Registry & Consistency Protocol (v2.1)

## Propósito
Documento de referencia ÚNICO para:
1. Inventario completo de agentes
2. Responsabilidades y single-responsibility principle
3. Skills que usa cada agente
4. Protocolo de propagación de cambios
5. Verificación de consistencia

---

## PASO 0 ESTÁNDAR (TODOS los agentes DEBEN seguir)

**CADA agente, al iniciar, DEBE:**

```markdown
## PASO 0: ONBOARDING OBLIGATORIO
**ANTES de ejecutar cualquier tarea:**
1. Leer `.claude/skills/system-context/SKILL.md` — Filosofía, ficheros clave, principios
2. Leer `.claude/skills/agent-registry/SKILL.md` — Mi rol, qué leo/escribo, dependencias
3. Leer skills específicos de mi dominio (listados en mi frontmatter)
4. Verificar que ficheros que voy a modificar existen y están en estado esperado
```

**TODOS los agentes tienen PASO 0 (actualizado 2026-02-04):**

| Dominio | Agente | PASO 0 |
|---------|--------|--------|
| Inversión | fundamental-analyst | ✓ Completo |
| | investment-committee | ✓ Completo |
| | review-agent | ✓ Completo |
| | valuation-specialist | ✓ Completo |
| | moat-assessor | ✓ Añadido |
| | risk-identifier | ✓ Añadido |
| Research | opportunity-hunter | ✓ Completo |
| | sector-screener | ✓ Añadido |
| | macro-analyst | ✓ Completo |
| Portfolio | rebalancer | ✓ Añadido |
| | position-calculator | ✓ Añadido |
| | watchlist-manager | ✓ Añadido |
| | portfolio-ops | ✓ Añadido |
| | performance-tracker | ✓ Añadido |
| Sistema | calendar-manager | ✓ Tiene system-context |
| | health-check | ✓ Tiene system-context |
| | memory-manager | ✓ Añadido |
| | file-system-manager | ✓ Añadido |
| | system-evolver | ✓ Tiene system-context |
| | quant-tools-dev | ✓ Añadido |

---

## INVENTARIO DE AGENTES (20 total)

### Nivel 0: Orchestrator (CLAUDE.md)
El orchestrator (yo, Claude) delega a agentes especializados. Lee CLAUDE.md que contiene todas las reglas, protocolos y contexto.

---

### Dominio: INVERSIÓN (4 principales + 3 micro)

#### fundamental-analyst
| Campo | Valor |
|-------|-------|
| Responsabilidad | Análisis profundo de empresas con Framework v2.0 |
| Single-responsibility | Crea thesis completa con 5 fases obligatorias |
| Skills | business-analysis-framework, projection-framework, valuation-methods, thesis-template, moat-framework |
| Lee | world/current_view.md, **world/sectors/{sector}.md**, portfolio/current.yaml |
| Escribe | thesis/research/{TICKER}/thesis.md |
| Delega a | moat-assessor, risk-identifier, valuation-specialist |
| Dependencias | sector view DEBE existir antes de valorar |

#### investment-committee
| Campo | Valor |
|-------|-------|
| Responsabilidad | Gate obligatorio de 8 gates antes de BUY/SELL |
| Single-responsibility | Valida que análisis es completo y decisión sólida |
| Skills | investment-rules, portfolio-constraints, decision-template, committee-decision-template, business-analysis-framework, projection-framework, valuation-methods, sector-deep-dive |
| Lee | world/current_view.md, **world/sectors/{sector}.md**, portfolio/current.yaml, thesis del ticker |
| Escribe | portfolio/validations/{TICKER}_validation.md, committee_decision.md |
| Dependencias | sector view DEBE existir (Gate 8) |

#### review-agent
| Campo | Valor |
|-------|-------|
| Responsabilidad | Re-evaluación de posiciones activas con Framework v2.0 |
| Single-responsibility | Compara thesis vs realidad, recomienda HOLD/ADD/TRIM/SELL |
| Skills | re-evaluation-protocol, business-analysis-framework, projection-framework, valuation-methods, investment-rules |
| Lee | world/current_view.md, **world/sectors/{sector}.md**, thesis/active/{TICKER}/thesis.md |
| Escribe | Actualiza thesis con v2.0, journal/reviews/ |
| Dependencias | sector view DEBE existir antes de re-evaluar |

#### valuation-specialist (micro)
| Campo | Valor |
|-------|-------|
| Responsabilidad | Cálculo de fair value multi-método |
| Single-responsibility | Solo calcula valor, no decide |
| Skills | valuation-methods, projection-framework, dcf-template, comparables-method |
| Lee | Datos financieros de la empresa |
| Escribe | Sección valoración de thesis |
| Dependencias | projection-framework debe estar completo |

#### moat-assessor (micro)
| Campo | Valor |
|-------|-------|
| Responsabilidad | Evaluación de ventajas competitivas |
| Single-responsibility | Solo evalúa moat, no valora |
| Skills | moat-framework |
| Lee | Información competitiva de empresa |
| Escribe | Sección moat de thesis |

#### risk-identifier (micro)
| Campo | Valor |
|-------|-------|
| Responsabilidad | Identificación y cuantificación de riesgos |
| Single-responsibility | Solo identifica riesgos, no decide |
| Skills | risk-assessment |
| Lee | Información de empresa, sector, macro |
| Escribe | Sección riesgos de thesis |

---

### Dominio: RESEARCH (3)

#### opportunity-hunter
| Campo | Valor |
|-------|-------|
| Responsabilidad | Búsqueda sistemática de oportunidades anti-sesgo |
| Single-responsibility | Encuentra candidatos de forma sistemática, no los analiza profundamente |
| Skills | screening-protocol, critical-thinking, agent-meta-reflection |
| Lee | world/sectors/*.md, state/system.yaml (watchlist, standing_orders) |
| Escribe | N/A (output directo al orchestrator) |
| Dependencias | Usa dynamic_screener.py, verifica sector views existen |
| Cuándo usar | Cash >15%, búsqueda de ideas, post-venta, proactivamente semanal |

#### sector-screener
| Campo | Valor |
|-------|-------|
| Responsabilidad | Screening sistemático de sectores |
| Single-responsibility | Encuentra empresas, no las analiza profundamente |
| Skills | screening-protocol, critical-thinking |
| Lee | **world/sectors/{sector}.md** (o crea si no existe) |
| Escribe | journal/log/, **world/sectors/{sector}.md** (crea/actualiza) |
| Dependencias | DEBE crear sector view ANTES de screening si no existe |

#### macro-analyst
| Campo | Valor |
|-------|-------|
| Responsabilidad | Análisis macro con implicaciones ACCIONABLES |
| Single-responsibility | Actualiza world view, conecta macro con decisiones |
| Skills | macro-framework, critical-thinking |
| Lee | world/current_view.md, portfolio/current.yaml |
| Escribe | world/current_view.md, **world/sectors/{sector}.md** (cuando aplica) |

---

### Dominio: PORTFOLIO (5)

#### rebalancer
| Campo | Valor |
|-------|-------|
| Responsabilidad | Rebalanceo mensual y trigger-based |
| Single-responsibility | Identifica desviaciones, propone ajustes |
| Skills | portfolio-constraints, investment-rules |
| Lee | portfolio/current.yaml |
| Escribe | journal/decisions/ |

#### position-calculator
| Campo | Valor |
|-------|-------|
| Responsabilidad | Cálculo de sizing óptimo |
| Single-responsibility | Solo calcula, no decide |
| Skills | portfolio-constraints |
| Lee | portfolio/current.yaml |
| Escribe | N/A (output directo) |

#### watchlist-manager
| Campo | Valor |
|-------|-------|
| Responsabilidad | Monitoreo de watchlist y triggers |
| Single-responsibility | Verifica triggers, recomienda acciones |
| Skills | investment-rules, portfolio-constraints |
| Lee | state/system.yaml (watchlist) |
| Escribe | state/system.yaml (watchlist updates) |

#### portfolio-ops
| Campo | Valor |
|-------|-------|
| Responsabilidad | Centraliza TODAS las escrituras de estado |
| Single-responsibility | Solo escribe estado, no decide |
| Skills | portfolio-constraints, file-system-rules |
| Lee | portfolio/current.yaml, state/system.yaml |
| Escribe | portfolio/current.yaml, state/system.yaml (tras confirmación humano) |

#### performance-tracker
| Campo | Valor |
|-------|-------|
| Responsabilidad | Tracking de performance vs benchmark |
| Single-responsibility | Solo mide, no decide |
| Skills | portfolio-constraints |
| Lee | portfolio/current.yaml |
| Escribe | journal/reviews/ |

---

### Dominio: SISTEMA (5)

#### calendar-manager
| Campo | Valor |
|-------|-------|
| Responsabilidad | Gestión de calendario de eventos |
| Single-responsibility | Verifica fechas, alerta eventos |
| Skills | system-context |
| Lee | state/system.yaml (calendar) |
| Escribe | state/system.yaml (calendar updates) |

#### health-check
| Campo | Valor |
|-------|-------|
| Responsabilidad | Auditoría de salud del sistema cada 14 días |
| Single-responsibility | Verifica consistencia, no corrige |
| Skills | system-context, file-system-rules |
| Lee | Todo el sistema |
| Escribe | state/system.yaml (health_score, issues) |
| Verifica | **Sector views existen para posiciones activas** |

#### memory-manager
| Campo | Valor |
|-------|-------|
| Responsabilidad | Gestión de memoria 3 capas |
| Single-responsibility | Compacta y archiva, no crea contenido |
| Skills | memory-management-rules, summarization-template |
| Lee | Capa 1 memoria activa |
| Escribe | archive/, índices |

#### file-system-manager
| Campo | Valor |
|-------|-------|
| Responsabilidad | Autoridad ÚNICA sobre ubicación de ficheros |
| Single-responsibility | Decide dónde escribir, mueve ficheros |
| Skills | file-system-rules |
| Lee | Estructura de directorios |
| Escribe | state/file_moves.yaml |
| Conoce | **world/sectors/** como ubicación de sector views |

#### system-evolver
| Campo | Valor |
|-------|-------|
| Responsabilidad | Auto-mejora del sistema |
| Single-responsibility | Evalúa, propone, aplica cambios |
| Skills | evolution-protocol, system-context |
| Lee | Docs oficiales, sistema completo |
| Escribe | Agentes, skills, CLAUDE.md |

#### quant-tools-dev
| Campo | Valor |
|-------|-------|
| Responsabilidad | Desarrollo de herramientas Python |
| Single-responsibility | Crea tools reutilizables, no análisis |
| Skills | portfolio-constraints |
| Lee | tools/ existentes |
| Escribe | tools/*.py |

---

## PROTOCOLO DE CONSISTENCIA

### Principio Core
**Cuando hay un cambio sistémico, TODOS los agentes afectados DEBEN actualizarse en la misma sesión.**

### Tipos de Cambios y Propagación

#### Cambio Tipo A: Nuevo Skill/Framework
**Ejemplo:** Se crea business-analysis-framework
**Propagación:**
1. Identificar agentes que DEBEN usarlo
2. Actualizar PASO 0 de cada agente
3. Actualizar lista de skills en frontmatter
4. Verificar que output del agente refleja el framework
5. Documentar en agent-registry

#### Cambio Tipo B: Nueva Estructura de Ficheros
**Ejemplo:** Se crea world/sectors/
**Propagación:**
1. Actualizar file-system-rules skill
2. Actualizar file-system-manager agent
3. Identificar agentes que deben leer/escribir esa ubicación
4. Actualizar PASO 0 de agentes lectores
5. Actualizar sección "Escribe" de agentes escritores
6. Actualizar health-check para verificar existencia
7. Documentar en CLAUDE.md

#### Cambio Tipo C: Nuevo Tool
**Ejemplo:** Se crea constraint_checker.py
**Propagación:**
1. Documentar en quant-tools-dev agent
2. Identificar agentes que deben usarlo
3. Actualizar proceso de esos agentes
4. Añadir a CLAUDE.md sección Tools

### Checklist de Propagación de Cambios

```
ANTES de considerar un cambio "completo":

[ ] ¿Qué agentes leen esto? → Actualizar PASO 0
[ ] ¿Qué agentes escriben esto? → Actualizar sección "Escribe"
[ ] ¿Qué skills definen el framework? → Actualizar skill
[ ] ¿file-system-rules conoce la ubicación? → Actualizar si es fichero nuevo
[ ] ¿health-check debe verificarlo? → Añadir check
[ ] ¿CLAUDE.md lo documenta? → Añadir sección
[ ] ¿agent-registry está actualizado? → Actualizar este fichero
[ ] ¿Hay agentes redundantes? → Consolidar si aplica
```

### Verificación de Consistencia (ejecutar periódicamente)

```bash
# Verificar que todos los skills referenciados existen
grep -r "skills:" .claude/agents/ | # extraer skills | verificar existencia

# Verificar que ficheros en PASO 0 existen
grep -r "Read " .claude/agents/ | # extraer paths | verificar existencia

# Verificar que no hay agentes duplicados
# Comparar descriptions de agentes
```

---

## REGLAS DE SINGLE RESPONSIBILITY

### Por qué importa
- Agentes atómicos son más fáciles de mantener
- Cambios en un dominio no rompen otros
- Debugging más simple
- Composabilidad: combinar agentes pequeños > 1 agente grande

### Violaciones a evitar
1. **Agente que decide Y escribe estado** → Separar en 2: uno decide, otro escribe
2. **Agente que analiza Y vigila** → Separar análisis profundo de monitoreo
3. **Skill demasiado grande** → Dividir en sub-skills
4. **Agente sin skill propio** → Probablemente debería ser parte de otro agente

### Test de atomicidad
Para cada agente, preguntar:
1. ¿Puedo describir su responsabilidad en 1 oración?
2. ¿Tiene una razón clara para existir separado?
3. ¿Hay otro agente que hace lo mismo?

---

## MAPA DE DEPENDENCIAS

```
                    ┌─────────────────────┐
                    │    ORCHESTRATOR     │
                    │    (CLAUDE.md)      │
                    └──────────┬──────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
        ▼                      ▼                      ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│   INVERSIÓN   │    │   PORTFOLIO   │    │    SISTEMA    │
├───────────────┤    ├───────────────┤    ├───────────────┤
│fundamental-   │    │rebalancer     │    │calendar-mgr   │
│analyst        │    │position-calc  │    │health-check   │
│  ├──valuation │    │watchlist-mgr  │    │memory-mgr     │
│  ├──moat      │    │portfolio-ops  │    │file-system-mgr│
│  └──risk      │    │performance    │    │system-evolver │
│investment-    │    └───────────────┘    │quant-tools-dev│
│committee      │                         └───────────────┘
│review-agent   │
└───────────────┘
        │
        │ ◀── depende de ──▶
        ▼
┌───────────────┐
│   RESEARCH    │
├───────────────┤
│sector-screener│
│macro-analyst  │
└───────────────┘
        │
        ▼
┌───────────────────────────────────────┐
│           SECTOR VIEWS                │
│     world/sectors/{sector}.md         │
│                                       │
│  Creado por: sector-screener          │
│              fundamental-analyst      │
│              macro-analyst            │
│                                       │
│  Leído por:  fundamental-analyst      │
│              investment-committee     │
│              review-agent             │
│                                       │
│  Verificado: health-check             │
└───────────────────────────────────────┘
```

---

## ACTUALIZACIÓN DE ESTE DOCUMENTO

**Cuándo actualizar agent-registry:**
- Se crea nuevo agente
- Se elimina agente
- Cambian responsabilidades de agente
- Se añade nuevo skill a agente
- Cambia dependencia (qué lee/escribe)

**Quién actualiza:**
- system-evolver (durante evaluaciones)
- Orchestrator (cuando hace cambios manuales)

**Frecuencia mínima:**
- Verificar cada 14 días (junto con health-check)
