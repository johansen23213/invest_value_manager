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

---

## Errores Short-Specific

**#44. Shortear sin catalizador**
Sin catalizador con fecha identificable → NO shortear. "Esta cara" no es thesis. Precio alto + popularity = trampa clasica. Verificar P10 (Catalizador como Ancla Temporal).

**#45. No cubrir cuando catalizador pasa sin efecto**
Si catalizador pasa y nada cambia → CUBRIR. No esperar "a que eventualmente caiga". El carry sigue corriendo. Cada dia sin catalizador vigente es carry quemado.

**#46. Shortear empresa "cara" sin thesis de fragilidad (Tesla trap)**
Precio alto NO es short thesis. Necesita FRAGILIDAD ESTRUCTURAL documentada: dependencia oculta, modelo de negocio insostenible, cambio regulatorio inminente. Si empresa "me viene a la mente" como short → es sesgo → VALIDAR con datos. Aplica misma disciplina que #7 y #29 para longs.

**#47. Apalancamiento excesivo en shorts**
Razonar sobre leverage desde P1 (Sizing por Conviccion) y P11 (Asimetria Consciente). Consultar precedentes en decisions_log.yaml. El leverage amplifica errores mas que aciertos en shorts por la asimetria natural.

---

## Errores Epistemicos

**#48. Tratar opinion de analista como hecho**
Al leer reportes de analistas, articulos, o noticias: SEPARAR datos primarios de interpretaciones. Un analista que dice "growth is accelerating" es OPINION — verificar contra datos reales (filings, earnings). Clasificar fuente (Nivel 1-4 del critical-thinking skill) ANTES de incorporar. Si mi thesis depende de la conclusion de un tercero sin datos primarios propios, la thesis es fragil. Ver critical-thinking skill: Protocolo Anti-Absorcion de Narrativa.

**#50. Net exposure por omision, no por razonamiento**
Cada sesion DEBE incluir razonamiento explicito sobre exposicion neta (Fase 2.5.6). "No shortear" es valido SOLO si lo razone contra el contexto macro+sectorial actual. Si mi portfolio es 100% long y no documente POR QUE, es decision por omision = error. El short side del sistema NO es opcional — es herramienta que DEBO considerar y aceptar/rechazar explicitamente. Ver: session-protocol Fase 2.5, rotation-engine seccion 4, principles.md P4.

**#49. Anclar Fair Value al consensus price target**
Consensus PT = promedio de opiniones con incentivos mixtos (sell-side necesita volumen). El consensus YA esta en el precio. Si mi FV converge al consensus sin razonamiento independiente, NO tengo ventaja informacional. Derivar FV siempre desde datos primarios (FCF, growth, WACC) con tools propios. Consensus sirve como COMPARACION ("mi FV difiere del consensus en X% porque..."), no como ancla.

---

## Errores Operativos

**#51. Confundir sesion con dia — incrementar fecha artificialmente**
Session ≠ Dia. Multiples sesiones pueden ocurrir en UN MISMO dia. SIEMPRE obtener fecha real con `date` o `currentDate` del contexto del sistema. NUNCA asumir fecha desde memoria ni incrementar. Al escribir en memory/system.yaml, usar la fecha REAL del sistema. Error recurrente: session N en Feb 18, memory escribia "Feb 19", siguiente sesion escribia "Feb 20" — todo era Feb 18.
