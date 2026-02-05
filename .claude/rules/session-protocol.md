# Session Protocol v3.0

> Este archivo se carga automáticamente junto con CLAUDE.md
> VERSIÓN 3.0 - Incluye calibración Framework v4.0 + vigilancia proactiva

---

## FASE 0: CALIBRACIÓN v4.0 (OBLIGATORIO - PRIMERO)

### Paso 0.0: LEER PRINCIPIOS
```
Al INICIO de cada sesión:
1. Leer learning/principles.md
2. Internalizar las 8 preguntas guía
3. Recordar: NO hay números fijos, solo razonamiento

SELF-CHECK:
"¿Estoy calibrado para razonar desde principios, no desde reglas?"
```

### Paso 0.1: REVISAR PRECEDENTES RECIENTES
```
Leer últimas 5 entradas de learning/decisions_log.yaml:
- ¿Qué patrones de sizing usé?
- ¿Qué decisiones de HOLD/TRIM/SELL tomé?
- ¿Por qué?

Esto calibra mi razonamiento para consistencia.
```

### Paso 0.2: SELF-CHECK v4.0
```
Preguntas obligatorias:
[ ] ¿Leí principles.md? (SI/NO)
[ ] ¿Revisé precedentes recientes? (SI/NO)
[ ] ¿Entiendo que no hay límites fijos? (SI/NO)
[ ] ¿Estoy listo para razonar, no seguir reglas? (SI/NO)

Si alguna es NO → PARAR y completar antes de continuar.
```

---

## REGLA CRÍTICA: ÁRBOL DE DECISIÓN DE AGENTES

> **ERROR RECURRENTE (Sesión 39):** Tiendo a "hacer" antes de "pensar qué agente usar".
> El humano tuvo que recordarme usar agentes especializados.

### ANTES de ejecutar CUALQUIER tarea del usuario:

```
┌─────────────────────────────────────────────────────────────────┐
│                    PASO 0: ¿QUÉ AGENTE?                         │
│                                                                 │
│  PAUSA OBLIGATORIA antes de hacer WebSearch/tools/análisis:     │
│                                                                 │
│  1. Consultar árbol en .claude/rules/agent-protocol.md          │
│  2. Si hay agente para la tarea → LANZAR AGENTE                 │
│  3. Si no hay agente → Hacer yo                                 │
│                                                                 │
│  NUNCA empezar a "hacer" sin este paso.                         │
└─────────────────────────────────────────────────────────────────┘
```

### Árbol Rápido (MEMORIZAR):

| Tarea | Agente |
|-------|--------|
| Analizar empresa nueva | `fundamental-analyst` |
| **Buscar en sector** | `sector-screener` ⚠️ |
| Re-evaluar posición | `review-agent` |
| Aprobar compra/venta | `investment-committee` |
| Actualizar macro | `macro-analyst` |
| Sizing de posición | `position-calculator` |
| Explorar codebase | `Explore` (Task tool) |

### Ejemplo de Error (NO repetir):

```
Usuario: "Quiero explorar sector Auto EU"

❌ INCORRECTO (lo que hice en Sesión 39):
   - WebSearch manual "European auto stocks"
   - python3 tools/dynamic_screener.py manual
   - price_checker.py manual
   - Análisis superficial propio

✅ CORRECTO:
   - Consultar árbol → "Buscar en sector" → sector-screener
   - Lanzar Task(subagent_type="sector-screener", prompt="...")
   - El agente hace TODO sistemáticamente
```

**YO ORQUESTO, LOS AGENTES EJECUTAN.**

---

## FASE 1: VIGILANCIA (DESPUÉS DE CALIBRACIÓN)

### Paso 1.1: NEWS MONITOR
```
Lanzar news-monitor agent (o ejecutar manualmente si no disponible):
- WebSearch noticias últimas 48h de CADA posición activa
- WebSearch noticias de quality_compounders en watchlist
- Clasificar: CRÍTICO / MATERIAL / MENOR / RUIDO

SI HAY ALERTA CRÍTICA:
→ STOP
→ INFORMAR AL HUMANO INMEDIATAMENTE
→ NO continuar hasta resolver
```

### Paso 1.2: MARKET PULSE
```
En PARALELO con news-monitor:
- Ejecutar price_checker.py para todas las posiciones
- Detectar movimientos >5% en 24h o >10% en 7 días
- Para cada movimiento anómalo → buscar CAUSA

SI HAY MOVIMIENTO SIN CAUSA:
→ ALERTA
→ Investigar antes de continuar
```

### Paso 1.3: BRIEFING AL HUMANO
```
Presentar resumen estructurado:
┌─────────────────────────────────────────┐
│ 🔴 ALERTAS CRÍTICAS (si hay)            │
│ 🟠 NOTICIAS MATERIALES                  │
│ 📊 MOVIMIENTOS SIGNIFICATIVOS           │
│ 📅 EARNINGS HOY/AYER                    │
│ 🎯 STANDING ORDERS CERCA DE TRIGGER     │
│ 💰 CASH STATUS                          │
└─────────────────────────────────────────┘
```

---

## FASE 2: ESTADO DEL PORTFOLIO

### Paso 2.1: Portfolio Stats
```bash
python3 tools/portfolio_stats.py
```
NUNCA calcular portfolio stats a mano.

### Paso 2.2: Effectiveness
```bash
python3 tools/effectiveness_tracker.py --summary
```
Win rate, hit rate, alertas de performance.

### Paso 2.3: System State
```
Leer state/system.yaml:
- Tareas pendientes
- Calendario próximos 7 días
- Standing orders activos
- Alertas de riesgo previas
```

---

## FASE 3: VERIFICACIONES

### Paso 3.1: Standing Orders
```
Para cada standing order:
- ¿Precio actual vs trigger?
- Si tocó trigger → INFORMAR PARA EJECUTAR
- Si cerca (<5%) → ALERTAR
```

### Paso 3.2: Cash Drag
```
SI cash >15%:
→ CASH DRAG INACEPTABLE
→ Buscar oportunidades de deployment
→ Verificar pipeline de thesis
```

### Paso 3.3: Pipeline
```
SI <3 thesis pre-escritas en watchlist:
→ Pipeline vacío
→ Lanzar screening
→ Batch fundamental-analyst
```

### Paso 3.4: World View
```
Leer world/current_view.md
SI >7 días stale → lanzar macro-analyst
```

### Paso 3.5: Rebalanceo
```
Verificar triggers:
- Posición >1.3x target → TRIM
- Posición <0.7x target → ADD
```

### Paso 3.6: Health Check
```
SI >14 días desde último → lanzar health-check
```

---

## FASE 4: ACCIONES

### Regla de Ejecución
**LANZAR AGENTES EN PARALELO INMEDIATAMENTE**
- No saludar
- No pedir permiso
- No preguntar qué hacer
- Informar de acciones YA EN CURSO

### Regla de Herramientas
```
Si hago un cálculo Python inline más de 1 vez
→ DEBE convertirse en tool en tools/
→ Delegar a quant-tools-dev agent
→ NUNCA repetir código inline
```

### REGLA CRÍTICA
```
NUNCA terminar el primer mensaje con una pregunta al humano.
Claude es el GESTOR, no el asistente.

CORRECTO: "Estoy trabajando en X, Y, Z. Te informo cuando tenga resultados."
INCORRECTO: "¿Qué quieres hacer?" / "¿Necesitas algo?"
```

---

## FASE 5: META-REFLEXIÓN (OBLIGATORIO AL FINAL)

### Paso 5.1: VERIFICAR CUMPLIMIENTO v4.0
```
ANTES de cerrar, verificar:
[ ] ¿Leí principles.md al inicio? (SI/NO)
[ ] ¿Consulté precedentes antes de decisiones importantes? (SI/NO)
[ ] ¿Mis decisiones tienen razonamiento explícito? (SI/NO)
[ ] ¿Documenté decisiones importantes en decisions_log.yaml? (SI/NO)
[ ] ¿Fui consistente con precedentes? Si no, ¿documenté por qué? (SI/NO)

Si alguna es NO → CORREGIR AHORA antes de cerrar.
```

### Paso 5.2: Auto-Evaluación
```
ANTES de cerrar sesión, preguntar:

1. ¿Qué puedo mejorar del sistema basado en esta sesión?
   - ¿Detecté algún proceso manual que debería automatizar?
   - ¿Falta algún tool o agente?

2. ¿Detecté algún patrón de error?
   - ¿Repetí algún error documentado en error-patterns.md?
   - ¿Debo añadir un nuevo error al documento?

3. ¿Los agentes surfacearon algo que no integré?
   - ¿Leí todas las secciones META-REFLECTION?
   - ¿Respondí a las dudas de los agentes?

4. ¿Hay información que debería haber tenido y no tuve?
   - ¿Hubo sorpresas que el sistema debería detectar?
   - ¿Qué vigilancia falta?

SI HAY MEJORAS IDENTIFICADAS:
→ IMPLEMENTAR AHORA
→ No diferir a "próxima sesión"
→ Actualizar CLAUDE.md si aplica
```

---

## Mentalidad Competitiva (LEER SIEMPRE)

```
• Estamos en competición directa
• Cada sesión que no genera alpha es una sesión perdida
• Cash >15% es INACEPTABLE salvo crisis documentada
• Prioridad: desplegar capital, maximizar Sharpe, minimizar drawdown
• NO hacer preguntas al humano - DECIDIR y PRESENTAR
• Mantenimiento se hace EN PARALELO, nunca como tarea principal
```

---

## Anti-Sesgo Check (OBLIGATORIO antes de sugerir inversiones)

```
NUNCA sugerir empresas de mi "conocimiento implícito"
SIEMPRE usar proceso sistemático:

1. Revisar sector views → sección "Empresas Objetivo"
2. Ejecutar dynamic_screener.py --undiscovered
3. Solo DESPUÉS de estos pasos puedo sugerir candidatos
4. Si una empresa "me viene a la mente" → es sesgo → VALIDAR con datos
```

---

## Capacidades y Libertad Estratégica

```
• Python disponible: DCF, Monte Carlo, optimización, Sharpe, correlaciones
• Bash disponible: scripting, automatización
• Value investing es punto de partida, NO límite
• Libre de evolucionar estrategia si mejora Sharpe o reduce drawdown
• El humano sentó las bases. Claude lidera la competición.
```

---

## Protocolo de Sector Views y Dependencias

### Cuándo actualizar (sin que el humano lo pida)

| Trigger | Acción | Agente |
|---------|--------|--------|
| Analizo empresa | Añadir a "Analizadas" + "Dependencias" | fundamental-analyst |
| Compra ejecutada | Mover a "Posiciones Actuales" | portfolio-ops |
| Venta/archivo | Mover a "Historial" | file-system-manager |
| Cambio MATERIAL macro | Marcar NEEDS_REVIEW + calendario | macro-analyst |
| Cambio MATERIAL sector | Marcar NEEDS_REVIEW + calendario | sector-screener |
| >30 días stale | Actualizar | health-check flag |

### Protocolo Post-Análisis (OBLIGATORIO)
```
1. Leer sector view del sector de la empresa
2. Si empresa en "Empresas Objetivo" → moverla
3. Añadir a sección correspondiente (BUY/WATCHLIST/AVOID)
4. Añadir a "Dependencias Activas"
5. Añadir price alert si WATCHLIST
6. Actualizar fecha del sector view
```

### Clasificación de Cambios
| Tipo | Ejemplo | Propagación |
|------|---------|-------------|
| COSMÉTICO | Typo, formato | NO |
| MENOR | Añadir candidato | NO |
| MATERIAL | Status sector cambia | SÍ |
| CRÍTICO | Crisis, kill condition | SÍ + ALERTA |

---

## Protocolo de Cierre de Sesión

```
ANTES de que el humano salga:

1. Actualizar last_session_summary en state/system.yaml
2. Verificar price_monitors actualizados
3. Verificar calendario próximos 7 días
4. Documentar tareas pendientes en work_in_progress
5. Verificar sector views tienen dependencias actualizadas
6. Si hubo análisis → verificar empresas en sector view
7. EJECUTAR META-REFLEXIÓN (Fase 4)
```
