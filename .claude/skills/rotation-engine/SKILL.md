---
name: rotation-engine
description: Framework for continuous portfolio optimization toward quality compounders
user-invocable: false
---

# Rotation Engine - Quality Gravitation Protocol

> Framework v4.0 - Principio 9: "La Calidad Gravita Hacia Arriba"
> Creado: 2026-02-07

---

## Propósito

Protocolo de optimización continua del portfolio. Asegura que el portfolio se mueva
constantemente hacia mayor calidad, reemplazando posiciones mediocres por quality compounders
cuando existen alternativas superiores.

**Esto NO es un algoritmo mecánico. Es un framework de pensamiento.**

---

## Filosofía

Un gestor profesional no espera a que una posición "falle" para rotarla.
Constantemente evalúa: "¿Es cada posición el mejor uso de su capital?"

La respuesta cambia con el tiempo porque:
- Nuevas oportunidades aparecen (fallen angels, selloffs)
- Tesis se debilitan o fortalecen (earnings, macro, competencia)
- El contexto macro evoluciona (tipos, ciclo, geopolítica)
- La convicción cambia con nueva información

---

## Proceso: Cada Sesión

### 1. Ranking por Forward Expected Return

```bash
python3 tools/forward_return.py
```

Esto produce DATOS crudos:
- Forward Expected Return = MoS% + Growth% + Yield%
- Ajustado por conviction y tailwind
- Ranking de mejor a peor

**El ranking es INPUT para razonar, no OUTPUT para ejecutar.**

### 2. Preguntas sobre Bottom 3

Para las 3 posiciones con peor retorno esperado:

```
a) ¿Por qué sigue en el portfolio?
   - ¿Tesis intacta?
   - ¿Catalizador pendiente que justifica esperar?
   - ¿ROIC > WACC? (si no, está destruyendo valor)

b) ¿Hay alternativa mejor?
   - ¿Existe candidato Tier A en pipeline con thesis lista?
   - ¿El Opportunity Score justifica el esfuerzo de rotar?
   - OS = (MoS_candidato / MoS_actual) × (QS_candidato / QS_actual)

c) ¿El timing es favorable?
   - ¿Estoy vendiendo en mínimo sin razón?
   - ¿Hay earnings pronto que podrían cambiar el panorama?
   - ¿La fricción de salida es material?
```

### 3. Pipeline Health

```
La capacidad de rotar depende de tener alternativas listas.
Sin pipeline, no hay rotación — solo cash.

Pipeline sano = >=3 thesis Tier A completas con:
- QS calculado
- Fair value estimado
- Investment committee pre-aprobado o standing order activo

Si pipeline < 3:
→ Activar sector-screener y opportunity-hunter
→ Priorizar sectores con tailwind
→ Usar dynamic_screener.py --undiscovered para anti-bias
```

### 4. Cash como Recurso Estratégico

```
Cash idle + pipeline sano = oportunidad perdida
Cash idle + pipeline vacío = reserva prudente
Cash idle + standing orders cerca = deployment inminente

No hay "nivel correcto" de cash.
Hay razonamiento sobre qué hacer con el cash dado el contexto.
```

---

## Proceso: Semanal

### Conviction Review

```
Para cada posición, actualizar:
- Conviction: high / medium / low
  - high = tesis fortalecida, compraría más si pudiera
  - medium = tesis intacta, HOLD natural
  - low = tesis debilitada, candidata a rotación

- Exit plan: texto corto
  - "Tier A HOLD. ADD below €X si MoS > Y%"
  - "Tier C, rotación pendiente cuando alternativa Tier A disponible"
  - "Esperar earnings [fecha] para decidir"
```

### Tailwind/Headwind Assessment

```
Conectar macro con posiciones:
- Leer world/current_view.md
- Para cada posición: ¿el entorno macro es favorable o desfavorable?
- Posiciones con headwind + baja conviction = prioridad EXIT
- Posiciones con tailwind + alta conviction = prioridad ADD
```

---

## Proceso: Cuando Aparece Oportunidad

```
Cuando sector-screener, opportunity-hunter, o análisis revela
un candidato Tier A con MoS atractivo:

1. ¿Cuál es la peor posición actual? (bottom del ranking)
2. Calcular Opportunity Score: OS = (MoS_nuevo/MoS_peor) × (QS_nuevo/QS_peor)
3. Si OS sugiere rotación → EXIT Protocol para la posición a salir
4. Si EXIT Protocol aprueba → Investment Committee para la nueva posición
5. Si IC aprueba → ejecutar rotación
```

---

## Guardrails (principios, no reglas)

1. **No fire sales.** Rotar no significa vender todo de golpe. Es gradual.
2. **La restricción es el pipeline.** Sin alternativa Tier A lista, no hay rotación.
3. **Timing matters.** No vender en mínimo sin razón. No comprar en máximo.
4. **Document everything.** Cada rotación va a decisions_log.yaml con razonamiento.
5. **Los datos informan, no dictan.** forward_return.py produce ranking. Yo decido.

---

## Integración con EXIT Protocol

El Rotation Engine y el EXIT Protocol son complementarios:

```
Rotation Engine identifica CANDIDATAS a rotación (datos + ranking)
                    ↓
EXIT Protocol evalúa cada candidata con 6 gates (razonamiento)
                    ↓
Investment Committee aprueba la operación (governance)
                    ↓
Portfolio-ops ejecuta y documenta (estado)
```

---

## Anti-Patterns (NO hacer)

1. **"Forward Return < X% = SELL"** → Esto es una regla disfrazada
2. **"Bottom 3 siempre rotan"** → Las bottom 3 se EVALÚAN, no se venden automáticamente
3. **"Tier B = vender"** → Tier B con argumento fuerte puede quedarse
4. **"Cash siempre debe ser < X%"** → Cash depende del contexto
5. **Rotar sin alternativa** → Vender para tener cash no es rotación, es liquidación

---

## Referencia

- `tools/forward_return.py` — Tool de ranking (datos crudos)
- `learning/principles.md` — Principio 9
- `.claude/skills/exit-protocol/SKILL.md` — 6 gates para evaluar exits
- `learning/decisions_log.yaml` — Precedentes de rotaciones anteriores

---

**Última actualización:** 2026-02-07
**Framework version:** 4.0
