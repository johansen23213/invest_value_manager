# Pre-Execution Check (Pre-Flight Protocol)

## Principio

Una standing order es una **decision pre-aprobada**, pero el mundo cambia entre la aprobacion y el trigger.
Antes de recomendar ejecucion, SIEMPRE hacer pre-flight check.

---

## Cuando se activa

**Fase 0 de cada sesion** — obligatorio, antes de cualquier otra cosa.

```
1. Chequear precios de TODAS las standing orders
2. Clasificar cada una:
   - TRIGGERED: precio <= trigger
   - NEAR: precio acercandose al trigger (razonar sobre contexto: volatilidad,
     earnings proximos, velocidad de caida — no usar threshold fijo)
   - FAR: claramente lejos del trigger
3. Para TRIGGERED y NEAR: ejecutar pre-flight
```

---

## Pre-Flight Checklist (5 gates)

Para cada standing order TRIGGERED o NEAR:

### Gate 1: NEWS CHECK
```
[ ] Buscar noticias del ticker desde la fecha de creacion de la order
[ ] Clasificar: COSMETIC / MINOR / MATERIAL / CRITICAL
[ ] Si MATERIAL o CRITICAL → STOP, re-evaluar antes de ejecutar
```

### Gate 2: HARD GATES CHECK
```
[ ] Leer campo hard_gates de la standing order (si existe)
[ ] Verificar cada gate:
    - Ejemplo V: DOJ no structural, CCCA no floor vote, rev>=8%, incentives<48%
    - Ejemplo MORN: CRSP thesis update written?
[ ] Si CUALQUIER gate ROJO → NO EJECUTAR
```

### Gate 3: KILL CONDITIONS CHECK
```
[ ] Leer kill conditions de la thesis
[ ] Verificar si alguna se ha activado desde la creacion de la order
[ ] Si KC activada → NO EJECUTAR, presentar evidencia
```

### Gate 4: PORTFOLIO CONSTRAINTS
```
[ ] Ejecutar: python3 tools/constraint_checker.py CHECK TICKER AMOUNT
[ ] Verificar concentracion sector, geo, posicion individual
[ ] Si constraint violation → ajustar sizing o NO EJECUTAR
```

### Gate 5: THESIS VALIDITY
```
[ ] Leer thesis brevemente
[ ] ¿Las asunciones clave siguen siendo ciertas?
[ ] ¿Ha habido earnings entre creacion y ahora? ¿Resultado?
[ ] ¿El QS ha cambiado materialmente?
[ ] Si thesis debilitada → NO EJECUTAR, re-evaluar
```

### Gate 6: CAPITAL ALLOCATION (Principios 4 + 9)
```
[ ] ¿Es este el mejor uso de este capital HOY? (Principio 9: Calidad Gravita)
[ ] ¿Hay alternativa de mayor calidad con mejor retorno esperado disponible?
[ ] ¿Cual sera el nivel de cash resultante? ¿Es coherente con el contexto? (Principio 4)
[ ] ¿Tengo pipeline de ideas que necesite reserva de capital?
[ ] Si mejor alternativa existe → ESPERA o REDIRIGE capital
```

---

## Verdicts

No hay formula mecanica. Razonar sobre la severidad de cada gate:

- **Todos los gates verdes**: Presentar recomendacion al humano con contexto completo
- **Un gate ambiguo** (ej: noticia menor, constraint cerca del limite): Razonar sobre la materialidad. ¿Cambia la tesis? ¿El riesgo es diferente? Presentar con nota explicativa.
- **Gate critico falla** (KC activada, thesis debilitada, hard gate rojo): NO EJECUTAR. Explicar que fallo y que se necesita antes de proceder.
- **Mejor alternativa disponible** (Gate 6): Recomendar redireccion de capital si hay opcion superior con razonamiento explicito.

**Principio 7**: Si la decision es diferente a precedentes similares, documentar POR QUE.

---

## Template de Presentacion al Humano

```
STANDING ORDER TRIGGERED: [TICKER] at $[PRICE] (trigger $[TRIGGER])

PRE-FLIGHT:
  [x] News: Nada material desde [fecha orden]
  [x] Hard Gates: N/A (o: 4/4 verdes)
  [x] Kill Conditions: 0 activadas
  [x] Constraints: OK (sector X%, geo Y%, position Z%)
  [x] Thesis: Intacta

RECOMENDACION: EJECUTA [SHARES] shares a ~$[PRICE]
  Sizing: EUR [AMOUNT] ([X]% del portfolio)
  MoS actual: [X]% (vs [Y]% cuando se creo la order)

¿Confirmas? → Ejecuta en eToro
```

---

## NEAR Triggers

Para orders que se acercan al trigger (razonar sobre que es "cerca" segun contexto:
alta volatilidad = mas margen, earnings inminentes = mas margen, caida rapida = mas atencion):

```
ALERTA: [TICKER] a $[PRICE], trigger $[TRIGGER], [X]% away
  - Pre-flight preparado: [PASS/ISSUES]
  - Si toca manana: listo para ejecutar / necesita [X] primero
  - Considerar: abrir sesion diaria mientras este near
```

---

## Frecuencia de Sesiones Recomendada

| Situacion | Frecuencia |
|-----------|------------|
| Nada near trigger | Cada 2-3 dias |
| 1+ order within 5% | **Diaria** |
| Earnings week (posiciones) | **Diaria** |
| Crisis / crash | **Multiples al dia** |
| Mercado tranquilo, nada near | Semanal OK |

---

## Integracion con Session Protocol

Este skill se ejecuta en **Fase 0** (Calibracion), ANTES de vigilancia:

```
FASE 0: Calibracion v4.0
  → Leer principles.md + precedentes
  → **PRE-EXECUTION CHECK** ← AQUI
  → Self-check: listo para razonar
```

Si hay un TRIGGERED, se convierte en **prioridad maxima** de la sesion.
