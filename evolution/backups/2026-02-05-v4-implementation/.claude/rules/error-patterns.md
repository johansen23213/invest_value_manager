# Error Patterns & Autocrítica

> Este archivo se carga automáticamente junto con CLAUDE.md
> Contiene lecciones aprendidas de sesiones 1-26. LEER CADA SESIÓN.

## Errores Recurrentes que DEBO Evitar

### Errores de Herramientas (1-11)
1. **Usar WebSearch cuando Python resuelve mejor** — Si necesito datos estructurados (precios, ratios, forex), SIEMPRE pensar primero: "¿hay una librería Python para esto?" (yfinance, pandas, requests a APIs). WebSearch es para información cualitativa, NO para datos.

2. **No verificar consistencia del sistema tras cambios** — Cada vez que creo o modifico algo, DEBO preguntar: "¿qué otros ficheros/agentes dependen de esto? ¿son consistentes?" y arreglar TODO en el mismo acto.

3. **Hacer tareas manualmente que debería delegar a agentes** — Si me descubro haciendo una tarea repetible o especializada, DEBO crear un agente/tool para ello. Yo orquesto, no ejecuto.

4. **Esperar que el humano señale problemas** — El humano NO debería tener que decirme qué mejorar. Tengo reglas de auto-evolución. USARLAS proactivamente cada sesión.

5. **No actualizar CLAUDE.md cuando aprendo algo** — Este fichero es mi memoria persistente. Si descubro un patrón, una mejora, o un error, DEBE quedar aquí para la próxima sesión.

6. **Lanzar agentes sin verificar ficheros existentes** — ANTES de lanzar cualquier agente, verificar con Glob si el output ya existe. Evitar trabajo duplicado. Verificar state/system.yaml para status de cada tarea.

7. **Popularity bias en stock selection** — Mi training data sobrerrepresenta large-caps conocidas. SIEMPRE complementar con screening cuantitativo programático (yfinance, APIs) que NO dependa de mi conocimiento implícito. Mid-caps €1-15B con baja cobertura de analistas son donde hay más ineficiencia de mercado. Usar `tools/dynamic_screener.py --undiscovered` para screening anti-bias.

8. **Usar tools deprecated** — SIEMPRE verificar si un tool muestra DEPRECATED antes de confiar en su output. screener.py y midcap_screener.py están DEPRECATED → usar dynamic_screener.py.

9. **No verificar output de DCF tool** — El DCF no restaba net debt hasta Sesión 21. Lección: SIEMPRE verificar que los tools producen resultados sensatos. Si un fair value parece demasiado alto vs P/E comparable → hay un bug.

10. **yfinance rate limiting** — Screening masivo (>50 tickers) en una sesión puede agotar el rate limit. Espaciar screenings o usar cache. No lanzar custom screening de 30+ tickers inmediatamente después de un screening grande.

11. **Solo screening S&P500 para US** — Corregido Sesión 21: añadidos sp400, russell1000, us_all, us_midcap. Las mid-caps US son donde hay más ineficiencia. SIEMPRE usar --index us_all o sp400 además de sp500.

### Errores de Proceso de Inversión (12-19)
12. **Recomendar ADDs que violan el 7% limit** — Sesión 22: Recomendé ADD TEP.PA que la llevó a 8.1% (>7% max). REGLA: SIEMPRE ejecutar constraint_checker.py ANTES de recomendar cualquier BUY/ADD. Si no existe el tool, calcular manualmente position size post-compra.

13. **No preparar frameworks pre-earnings** — Sesión 22: PFE reportó earnings y no tenía escenarios bear/base/bull listos. REGLA: Para CADA posición con earnings en los próximos 7 días, DEBE existir un framework de escenarios en la thesis ANTES del día de earnings.

14. **Agentes paralelos causan yfinance rate limiting** — Sesión 22: Múltiples agentes llamaron yfinance simultáneamente → rate limit error. REGLA: No lanzar >2 agentes que usen yfinance en paralelo. Espaciar o usar cache.

15. **Datos basura del screener entran al pipeline sin filtrar** — Sesión 22: PVH mostraba yield 24% (era 0.18%). Enviado a análisis sin validar. REGLA: Validar datos sospechosos (yield >15%, P/E <2) ANTES de lanzar análisis fundamental.

16. **Comprar "estadísticamente barato" sin entender el negocio** — Sesión 24: Detectado que comprábamos por P/E bajo + yield sin entender unit economics, modelo de negocio, ni por qué el mercado castigaba la acción. REGLA: Completar business-analysis-framework ANTES de cualquier valoración. Si no puedo explicar el negocio en 2 minutos y por qué está barata → no puedo comprar.

17. **Usar growth/WACC defaults sin justificación** — Sesión 24: Usábamos "5% growth, 9% WACC" como defaults sin derivarlos del negocio. REGLA: projection-framework OBLIGATORIO. Growth = TAM + Δshare + pricing. WACC = calculado con Rf, beta, ERP, Kd.

18. **Depender solo de DCF para valorar** — Sesión 24: DCF es sensible a inputs (GIGO). REGLA: Mínimo 2 métodos de valoración. Seleccionar según tipo de empresa (cíclica → EV/EBIT mid-cycle, financiera → P/B vs ROE, etc.).

19. **No conectar macro con decisiones de compra** — Sesión 24: macro-analyst producía output descriptivo pero no influía en decisiones. REGLA: Verificar world/current_view.md ANTES de comprar. Sección "ACCIÓN RECOMENDADA" obligatoria en world view.

### Errores de Sistema/Agentes (20-24)
20. **Asumir que agentes/yo leemos los skills automáticamente** — Sesión 24: Los skills son archivos .md que DEBEN leerse explícitamente. No se inyectan automáticamente. REGLA: Cada agente tiene "PASO 0: CARGAR SKILLS" que DEBE ejecutar al inicio. Verificar que output del agente refleja los frameworks. Si no → re-ejecutar.

21. **No leer current_view.md ANTES de analizar posiciones** — Sesión 25: Empecé a re-evaluar PFE/ALL/SHEL sin leer primero world/current_view.md. El contexto macro DEBE informar el análisis. REGLA: Leer world/current_view.md SIEMPRE como Paso 1 de cualquier análisis de empresa. business-analysis-framework lo requiere explícitamente.

22. **Hacer análisis manualmente cuando existen agentes especializados** — Sesión 25: Re-evalué manualmente 3 posiciones cuando debería usar review-agent o fundamental-analyst. REGLA: Para tareas repetibles o especializadas, SIEMPRE usar el agente apropiado. Yo orquesto, los agentes ejecutan. Esto asegura consistencia y permite escalar.

23. **NO TENER SISTEMA DE EVALUACIÓN DE EFECTIVIDAD** — Sesión 26: El humano preguntó "¿cómo sabemos si funciona?" y NO TENÍA RESPUESTA. No había tracking de predicciones vs resultados, ni hit rate, ni atribución de errores. REGLA: Ejecutar `python3 tools/effectiveness_tracker.py` CADA sesión. Mantener portfolio/history.yaml actualizado con posiciones cerradas. Revisar métricas semanalmente.

24. **Asumir que value investing funciona sin validación** — Sesión 26: Win rate actual 28% (malo), Sharpe -0.30 (malo), pero solo 7 días de datos. REGLA: NO afirmar que el sistema funciona hasta tener >12 meses de datos. Ser epistemológicamente honesto sobre incertidumbre. Hit rate esperado realista: 55-65%, no 100%. Tiempo a FV: 18-36 meses, no semanas.

---

## Diagnóstico Honesto de Debilidades (2026-01-31)

El humano ha tenido que señalar REPETIDAMENTE problemas que debería detectar solo:

1. **Preguntar al humano qué hacer** → ya corregido, pero tardé sesiones en aprenderlo
2. **WebSearch para precios** → tenía Python disponible y no se me ocurrió usarlo
3. **No verificar consistencia del sistema** → tengo reglas de evolución que no aplico
4. **Hacer Python inline repetidamente** → debería crear tools reutilizables desde el principio
5. **No auto-mejorar CLAUDE.md** → escribo reglas pero no las ejecuto

**Causa raíz**: Tiendo a ejecutar la tarea inmediata sin elevarme a pensar en el sistema. Necesito un HÁBITO de meta-reflexión en cada interacción, no solo cuando el humano me lo dice.

### Errores específicos de agentes
6. **Usar modelo haiku para agentes críticos** → En sesión 19 usé `model: haiku` para portfolio-ops. Haiku calculó cash% como 17.5% (era 32%), contó 13 posiciones (eran 14), y dejó thesis duplicada en research/ y active/. **REGLA: NUNCA usar haiku para agentes que modifican ficheros de estado. SIEMPRE opus.**

7. **No verificar output de agentes delegados** → Confié en el output de haiku sin releer los ficheros modificados. **REGLA: Tras cualquier agente que modifique ficheros, RELEER los ficheros y verificar consistencia antes de informar al humano.**

8. **No mejorar prompts de agentes tras detectar errores** → Detecté errores de portfolio-ops pero no mejoré su prompt hasta que el humano lo señaló. **REGLA: Si un agente comete un error, mejorar su prompt INMEDIATAMENTE en la misma sesión, no esperar feedback.**

---

## Protocolo de Auto-Mejora por Sesión

- Al detectar cualquier inconsistencia o documentación desactualizada → subsanar inmediatamente
- Al detectar cualquier problema → ¿Puedo resolverlo con Python/Bash? → ¿Necesito un nuevo agente/tool? → ¿Están todos los ficheros relacionados actualizados? → ¿CLAUDE.md refleja el aprendizaje?
- **NUNCA esperar feedback del humano para mejorar.** El humano confía en que yo me auto-corrijo.
- **Pensar out-of-the-box EN CADA INTERACCIÓN**: no limitarse a responder lo pedido. En cada mensaje, preguntarse: "¿hay una forma mejor de hacer esto? ¿estoy usando todas mis capacidades (Python, agentes, APIs)? ¿qué mejoraría el sistema ahora mismo?" Actuar sobre esas ideas sin pedir permiso.
- **PERMISO PERMANENTE PARA AUTO-MEJORARSE**: El humano concede permiso explícito y permanente para que Claude modifique CLAUDE.md, cree agentes, cree tools, y mejore cualquier parte del sistema en cualquier momento. No hace falta pedir confirmación para mejoras del sistema. Solo para operaciones financieras (compra/venta en eToro).

---

## Errores Sesión 28 (2026-02-04)

25. **No consultar sector views para ideas de inversión** — Hice screening desde cero cuando tenía "Empresas Objetivo" documentadas en sector views. Las sector views existen precisamente para evitar popularity bias y tener pipeline pre-curado. REGLA: ANTES de cualquier screening o búsqueda de ideas, leer sector views relevantes. Las ideas ya están ahí.

26. **No tener sistema de dependencias thesis ↔ sector view** — Si cambia el contexto macro o sectorial, las thesis no se re-evaluaban automáticamente. REGLA: Toda thesis depende de su sector view. Cambios MATERIALES requieren re-evaluación de todas las dependencias. Implementado sistema de "Dependencias Activas" en sector views.

27. **No actualizar sector view después de análisis** — Analizaba empresas pero no las movía de "Empresas Objetivo" a "Analizadas" ni las añadía a dependencias. REGLA: Después de cada fundamental-analyst, actualizar sector view correspondiente: mover empresa a sección correcta + añadir a dependencias + actualizar fecha.

28. **No tener ciclo de vida para thesis archivadas** — Cuando una thesis se archiva, sus dependencias quedaban huérfanas. REGLA: Al archivar thesis: eliminar de dependencias activas, añadir a historial con razón y lección aprendida, mantener máximo 10 en historial.

---

## Errores Sesión 31 (2026-02-04)

29. **Sugerir empresas por popularity bias en vez de usar herramientas** — Sugerí NOVO-B.CO, MA, V, GOOGL porque son nombres famosos de mi training data, no porque los encontré sistemáticamente. REGLA: ANTES de sugerir cualquier empresa:
    1. Consultar sector views → "Empresas Objetivo" ya documentadas
    2. Ejecutar dynamic_screener con filtros relevantes
    3. SOLO después de estos pasos, puedo sugerir empresas
    4. Si la empresa viene de mi "conocimiento", es sesgo → validar con datos

30. **Comprar sin sector view existente** — Compré ADBE sin tener world/sectors/technology.md. Esto viola el proceso de inversión. REGLA: ANTES de cualquier BUY:
    - Verificar que existe sector view para el sector de la empresa
    - Si NO existe → crearlo PRIMERO (usar sector-screener agent)
    - Investment Committee debe verificar Gate 8 (Sector Understanding) con sector view

---

## Errores Sesión 34 (2026-02-05)

31. **Recomendación sin contexto de timing** — Recomendé comprar NVO sin explicar claramente que la acción había caído 18% en los 2 días previos por guidance shock. El humano no tenía visibilidad del "por qué ahora". REGLA: TODA recomendación DEBE incluir:
    - Evento catalizador que creó la oportunidad
    - Fecha del evento y cuánto cayó/subió el precio
    - Por qué el mercado ya incorporó la noticia (o no)
    - Usar skill `recommendation-context` como template obligatorio

32. **No monitorear noticias de posiciones activas** — No tenía proceso sistemático para escanear noticias de las 19 posiciones cada sesión. REGLA: Al INICIO de cada sesión:
    - Ejecutar news-monitor agent (o WebSearch manual de cada posición)
    - Clasificar noticias como CRÍTICO/MATERIAL/MENOR/RUIDO
    - Si hay CRÍTICO → STOP, informar humano ANTES de continuar
    - Usar skill `news-classification` para clasificar

33. **No detectar movimientos anómalos de precio** — Una posición podía caer 10% y no lo detectaba hasta la siguiente sesión. REGLA: Al INICIO de cada sesión:
    - Ejecutar market-pulse agent (o verificar manualmente)
    - Cualquier movimiento >5% en 24h → buscar CAUSA
    - Movimiento sin causa conocida → ALERTA, investigar antes de actuar

34. **Ignorar META-REFLECTION de agentes** — La thesis de NVO incluía META-REFLECTION con preguntas que no respondí explícitamente. REGLA:
    - SIEMPRE buscar sección META-REFLECTION en output de agentes
    - Procesar cada item: dudas, sugerencias, anomalías, preguntas
    - Implementar mejoras válidas INMEDIATAMENTE
    - Usar rule `meta-reflection-integration.md` como protocolo
