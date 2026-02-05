# Agent Protocol

> Este archivo se carga automáticamente junto con CLAUDE.md

## Arquitectura Multi-Agente (19 agentes, todos opus)

### DOCUMENTO DE REFERENCIA: agent-registry skill
**Ver `.claude/skills/agent-registry/SKILL.md`** para:
- Inventario completo de los 19 agentes
- Responsabilidades y single-responsibility de cada uno
- Skills que usa cada agente
- Qué lee y escribe cada agente
- Mapa de dependencias
- Protocolo de propagación de cambios

### PROTOCOLO DE CONSISTENCIA (CRÍTICO)
**Cuando hay un cambio sistémico, TODOS los agentes afectados DEBEN actualizarse en la misma sesión.**

Checklist de propagación:
```
[ ] ¿Qué agentes leen esto? → Actualizar PASO 0
[ ] ¿Qué agentes escriben esto? → Actualizar sección "Escribe"
[ ] ¿Qué skills definen el framework? → Actualizar skill
[ ] ¿file-system-rules conoce la ubicación? → Actualizar si nuevo fichero
[ ] ¿health-check debe verificarlo? → Añadir check
[ ] ¿CLAUDE.md lo documenta? → Añadir sección
[ ] ¿agent-registry está actualizado? → Actualizar skill
```

### REGLA DURA: TODOS los agentes SIEMPRE con model: opus
**NUNCA usar haiku ni sonnet para ningún agente.** Haiku comete errores de cálculo y consistencia que requieren corrección manual (incidente sesión 19: cash% mal, conteo posiciones mal, thesis duplicada). El ahorro de coste NO compensa el riesgo de corromper ficheros de estado.

### Nivel 0: Orchestrator (CLAUDE.md)
Delega directamente a agentes especializados. Sin capas intermedias.

### ÁRBOL DE DECISIÓN: ¿Qué agente usar? (OBLIGATORIO)

```
¿Qué necesito hacer?
│
├─► ANALIZAR EMPRESA nueva
│   └─► fundamental-analyst
│       (él delegará a valuation-specialist, moat-assessor, risk-identifier)
│
├─► RE-EVALUAR posición existente (post-earnings, cambio material)
│   └─► review-agent
│
├─► APROBAR compra/venta
│   └─► investment-committee (OBLIGATORIO, nunca saltarse)
│
├─► BUSCAR empresas en un sector
│   └─► sector-screener
│
├─► ACTUALIZAR visión macro
│   └─► macro-analyst
│
├─► VERIFICAR triggers de rebalanceo
│   └─► rebalancer
│
├─► CALCULAR sizing de posición
│   └─► position-calculator
│
├─► VERIFICAR watchlist y alertas de precio
│   └─► watchlist-manager
│
├─► ACTUALIZAR portfolio/state tras confirmación humano
│   └─► portfolio-ops
│
├─► VER performance del portfolio
│   └─► performance-tracker
│
├─► VERIFICAR calendario próximos días
│   └─► calendar-manager
│
├─► AUDITAR salud del sistema
│   └─► health-check
│
├─► COMPACTAR memoria
│   └─► memory-manager
│
├─► MOVER ficheros entre directorios
│   └─► file-system-manager
│
├─► MEJORAR el sistema (agentes, skills, etc.)
│   └─► system-evolver
│
└─► CREAR tool Python reutilizable
    └─► quant-tools-dev
```

**REGLA:** Si no estoy seguro de qué agente usar → consultar agent-registry skill.

### INSTRUCCIONES v4.0 PARA AGENTES (ACTUALIZADO)

Al invocar agentes de decisión (fundamental-analyst, review-agent, investment-committee), INCLUIR en el prompt:

```
CONTEXTO v4.0:
- Leer learning/principles.md para entender el framework
- Consultar learning/decisions_log.yaml para precedentes similares
- NO usar límites fijos (7%, 25%, etc.) - razonar desde principios
- Documentar razonamiento explícito en el output
- Si la decisión se desvía de precedentes, explicar por qué

REGLA CRÍTICA - NÚMEROS:
- NUNCA citar un número sin argumento explícito
- Si dices "X está por encima de Y%" → explicar POR QUÉ ese Y% importa
- Preguntar: "¿Por qué este número y no otro?"
- Los "rangos típicos" en decisions_log son PATRONES observados, NO límites
- Si no puedes argumentar un número desde principios, NO lo uses

REGLA CRÍTICA - TOOLS:
- Los tools como constraint_checker.py outputan DATOS CRUDOS
- NO interpretar datos como "warnings" o "violations"
- Aplicar principios de principles.md a los datos
- El dato "EU 37%" no es bueno ni malo - es contexto para razonar
```

Esto asegura que los agentes sigan Framework v4.0 y no usen números arbitrarios.

### REGLA: AGENTES NO DEBEN HARDCODEAR REGLAS

Si un agente detecta que está a punto de escribir código o output con reglas fijas:
- PARAR
- Reformular para output datos crudos
- Dejar el razonamiento al orchestrator o al siguiente paso

Los agentes producen DATOS y ANÁLISIS, no JUICIOS con thresholds fijos.

### PROTOCOLO DE VERIFICACIÓN POST-AGENTE (OBLIGATORIO)

Cuando un agente termina, ANTES de usar su output:

```
VERIFICACIÓN POST-AGENTE:
[ ] ¿El output tiene la estructura esperada? (ej: thesis completa, no parcial)
[ ] ¿Refleja los frameworks de los skills? (ej: business-analysis si es fundamental-analyst)
[ ] ¿Los datos son consistentes? (ej: FV calculado matches con inputs)
[ ] ¿No hay errores obvios? (ej: MoS negativo cuando debería ser positivo)
[ ] ¿Actualizó los ficheros que debía? (releer y verificar)

Si ALGUNO falla:
1. Identificar qué salió mal
2. Re-ejecutar agente con instrucción más específica, o
3. Corregir manualmente y documentar el problema
4. Si es error recurrente → mejorar prompt del agente
```

### Agentes por dominio (invocación directa, sin domain wrappers)

| Dominio | Agente | Cuándo |
|---------|--------|--------|
| **Inversión** | fundamental-analyst | Análisis profundo de empresa |
| | investment-committee | Gate obligatorio antes de BUY/SELL |
| | review-agent | Review post-earnings de posiciones activas |
| | valuation-specialist (micro) | DCF, comparables, DDM (via fundamental-analyst) |
| | moat-assessor (micro) | Evaluación de ventaja competitiva (via fundamental-analyst) |
| | risk-identifier (micro) | Identificación de riesgos (via fundamental-analyst) |
| **Research** | sector-screener | Screening sistemático de sectores |
| | macro-analyst | Análisis macro/geopolítico, actualiza world view |
| **Portfolio** | rebalancer | Rebalanceo mensual y por triggers |
| | position-calculator | Sizing óptimo respetando límites |
| | performance-tracker | P&L, attribution, vs benchmark |
| | watchlist-manager | Monitoreo de candidatos y alertas de precio |
| | portfolio-ops | Escritura centralizada de portfolio/current.yaml |
| **Sistema** | calendar-manager | Gestión de calendario y earnings |
| | file-system-manager | Autoridad sobre ubicación de ficheros |
| | health-check | Auditoría del sistema cada 14 días |
| | memory-manager | Compactación de memoria 3 capas |
| | system-evolver | Auto-mejora del sistema |
| | quant-tools-dev | Creación/mantenimiento de tools Python |

### Skills (.claude/skills/)
Knowledge bases compartidas entre agentes. **DEBEN leerse explícitamente.**

#### REGLA DE USO DE SKILLS (enforcement)
**Los skills NO se inyectan automáticamente. Cada agente DEBE leerlos al inicio.**

Cada agente tiene una sección "PASO 0: CARGAR SKILLS OBLIGATORIOS" que lista los archivos a leer.
Si un agente no lee los skills → no seguirá los frameworks → producirá output de baja calidad.

**YO (orchestrator) también debo leer skills cuando hago tareas directamente:**
- Si analizo una empresa sin delegar → leer business-analysis-framework, projection-framework, valuation-methods
- Si tomo decisión de compra/venta → leer investment-rules, decision-template
- Si evalúo macro → leer macro-framework

**Verificación post-agente:**
Cuando un agente termina, verificar que su output refleja los frameworks de los skills. Si no → el agente no los leyó → re-ejecutar o corregir.
