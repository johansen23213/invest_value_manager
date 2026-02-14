# Error Patterns — Errores Activos

> Auto-loaded con CLAUDE.md. Solo errores que AUN PUEDEN OCURRIR.
> Archivo completo: `learning/error_patterns_archive.md`

---

## Errores Criticos (mantener numeros originales — error-detector los referencia)

**#3. Hacer manual lo que un agente deberia hacer** (consolida #3, #22, #38, #39, #40)
PASO 0 antes de CUALQUIER tarea: consultar arbol en `agent-protocol.md`. Si hay agente, DELEGAR.
YO ORQUESTO, LOS AGENTES EJECUTAN.

**#7. Popularity bias en stock selection**
SIEMPRE complementar con screening programatico (`dynamic_screener.py --undiscovered`). Si una empresa "me viene a la mente", es sesgo — validar con datos.

**#12. No ejecutar constraint_checker.py antes de BUY/ADD**
SIEMPRE ejecutar `constraint_checker.py CHECK TICKER AMOUNT` antes de recomendar compra.

**#13. No preparar frameworks pre-earnings**
Para CADA posicion con earnings en proximos 7 dias, DEBE existir framework bear/base/bull en la thesis.

**#16. Comprar sin entender el negocio**
Completar `business-analysis-framework` ANTES de cualquier valoracion. Si no puedo explicar el negocio en 2 minutos y por que esta barata, no puedo comprar.

**#18. Depender solo de DCF**
Minimo 2 metodos de valoracion. Seleccionar segun tipo de empresa (ciclica: EV/EBIT, financiera: P/B vs ROE, etc.).

**#29. Sugerir empresas por popularity bias**
ANTES de sugerir: 1) consultar sector views, 2) ejecutar dynamic_screener. SOLO despues puedo sugerir.

**#30. Comprar sin sector view existente** (reincidencia #42)
GATE 0 del Investment Committee: `Glob("world/sectors/*{sector}*")`. Si no existe, STOP.

**#37. Hardcodear reglas en tools/skills**
Tools = DATOS CRUDOS. Skills = FRAMEWORKS. Numeros fijos en codigo me sesgan en el futuro. Usar PRECEDENTES (decisions_log) para consistencia, no hardcoding.

**#41. No completar ciclo post-analisis**
Tras veredicto WATCHLIST/BUY: 1) guardar thesis, 2) actualizar sector view, 3) anadir alerta precio, 4) si BUY: standing order, 5) confirmar al usuario. El analisis NO termina hasta que la alerta esta en el sistema.

**#43. QS de thesis no coincide con quality_scorer.py**
REGLA QS TOOL-FIRST: quality_scorer.py = fuente principal. Thesis muestra AMBOS (QS Tool + QS Ajustado). Ajuste >5 puntos requiere evidencia cuantitativa. Ajustes validos: forward growth deterioration, moat siege, ROIC distortion, insider data incorrect, kill condition approaching.
