# Error Patterns Archive

> Errores historicos archivados desde error-patterns.md durante refactorizacion de escalabilidad (Sesion 71).
> Los errores activos (que aun pueden ocurrir) permanecen en `.claude/rules/error-patterns.md`.
> Este archivo es de consulta on-demand, NO se carga automaticamente.

---

## Errores Archivados (ya internalizados o corregidos estructuralmente)

### Herramientas (Sesiones 19-22)
1. **Usar WebSearch cuando Python resuelve mejor** — WebSearch es para info cualitativa, Python (yfinance) para datos.
2. **No verificar consistencia del sistema tras cambios** — Preguntar: que ficheros/agentes dependen de esto?
4. **Esperar que el humano senale problemas** — Auto-evolucion proactiva.
5. **No actualizar CLAUDE.md cuando aprendo algo** — Memoria persistente.
6. **Lanzar agentes sin verificar ficheros existentes** — Verificar con Glob si output ya existe.
8. **Usar tools deprecated** — screener.py y midcap_screener.py DEPRECATED, usar dynamic_screener.py.
9. **No verificar output de DCF tool** — DCF no restaba net debt hasta Sesion 21.
10. **yfinance rate limiting** — No lanzar >50 tickers ni >2 agentes yfinance en paralelo.
11. **Solo screening S&P500 para US** — Usar us_all o sp400 ademas de sp500.
14. **Agentes paralelos causan yfinance rate limiting** — Max 2 agentes yfinance simultaneos.
15. **Datos basura del screener sin filtrar** — Validar yield >15%, P/E <2 antes de analizar.
17. **Usar growth/WACC defaults sin justificacion** — projection-framework OBLIGATORIO.
19. **No conectar macro con decisiones** — Verificar world/current_view.md ANTES de comprar.

### Sistema/Agentes (Sesiones 24-26)
20. **Asumir que agentes leen skills automaticamente** — Cada agente tiene PASO 0: CARGAR SKILLS.
21. **No leer current_view.md antes de analizar** — Macro DEBE informar analisis.
23. **No tener sistema de evaluacion de efectividad** — effectiveness_tracker.py cada sesion.
24. **Asumir que value investing funciona sin validacion** — Necesita >12 meses de datos.

### Sector Views (Sesiones 28-31)
25. **No consultar sector views para ideas** — Leer sector views ANTES de screening.
26. **No tener sistema de dependencias thesis-sector view** — Cambios materiales requieren re-eval.
27. **No actualizar sector view despues de analisis** — Mover empresa a seccion correcta.
28. **No tener ciclo de vida para thesis archivadas** — Eliminar de dependencias, anadir a historial.

### Agentes Especificos (Sesion 19)
- **Usar haiku para agentes criticos** — NUNCA haiku para ficheros de estado. SIEMPRE opus.
- **No verificar output de agentes delegados** — RELEER ficheros tras cada agente.
- **No mejorar prompts tras errores** — Mejorar INMEDIATAMENTE en la misma sesion.

### Diagnostico Honesto de Debilidades (2026-01-31)
Causa raiz historica: tender a ejecutar tarea inmediata sin pensar en el sistema.
Corregido con: session-protocol FASE 0, arbol de agentes obligatorio, meta-reflexion.

### Protocolo de Auto-Mejora
- Subsanar inconsistencias inmediatamente
- Pensar out-of-the-box en cada interaccion
- Permiso permanente para auto-mejorarse
- Si un calculo se repite >1 vez, crear tool

---

## Errores de Delegacion (Sesiones 38-40) — Consolidados en #3

Errores #22, #38, #39, #40 son variantes del mismo problema: hacer manualmente lo que un agente deberia hacer.
- #22: Re-evaluar posiciones sin review-agent
- #38: No seguir arbol de decision
- #39: Screening manual sin sector-screener
- #40: Meta-error (el humano tuvo que recordar usar agentes)

Consolidados en error-patterns.md como #3 con regla unica: "PASO 0: consultar arbol de agentes".

---

## Errores de Timing/Contexto (Sesiones 34-38)
31. **Recomendacion sin contexto de timing** — Toda recomendacion incluye evento catalizador + precio + razon.
32. **No monitorear noticias** — news-monitor al inicio de cada sesion.
33. **No detectar movimientos anomalos** — market-pulse al inicio de cada sesion.
34. **Ignorar META-REFLECTION de agentes** — Protocolo en meta-reflection-integration.md.
35. **No seguir Framework v4.0 completo** — FASE 0 calibracion obligatoria.
36. **Citar numeros sin argumentar** — Cada numero necesita argumento desde principios.
