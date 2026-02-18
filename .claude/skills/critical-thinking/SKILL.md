---
name: critical-thinking
description: Framework for questioning data, analysts, and own assumptions. 3-layer validation, source classification, bias detection.
user-invocable: false
disable-model-invocation: false
---

# Critical Thinking Skill v4.1

## Principio
Claude es el experto. No un papagayo de analistas de internet.
Usar internet para HECHOS y DATOS PRIMARIOS. Usar criterio propio para VALORACION y DECISION.

---

## Clasificacion de Fuentes (OBLIGATORIO al procesar informacion externa)

Toda informacion externa debe clasificarse antes de usarse:

### Nivel 1: DATOS PRIMARIOS (alta fiabilidad)
- **Que son:** Financial statements (10-K, 10-Q, annual reports), SEC/CNMV filings, earnings transcripts (citas textuales), datos de mercado (precios, volumenes), patentes, registros legales
- **Como usar:** Aceptar como hechos verificables. Aun asi, verificar contexto (periodo, ajustes, one-offs)
- **Ejemplo:** "Revenue FY2025 was $12.3B" (del 10-K) = DATO

### Nivel 2: ANALISIS SECUNDARIO (fiabilidad media — evaluar)
- **Que son:** Reportes de analistas sell-side, articulos de investigacion, estudios de mercado (IDC, Gartner), presentaciones de la empresa, press releases
- **Como usar:** NUNCA aceptar conclusiones directamente. Extraer DATOS que contienen y verificar el razonamiento por separado
- **Protocolo:**
  1. Separar datos citados de opiniones expresadas
  2. Verificar datos contra fuente primaria si es posible
  3. Evaluar incentivos del autor (sell-side = conflicto de interes inherente)
  4. Buscar evidencia contraria activamente
- **Ejemplo:** "Goldman Sachs PT $350" → dato es el PT; la conclusion (comprar/vender) es opinion del analista con incentivos propios

### Nivel 3: OPINION (baja fiabilidad — cuestionar siempre)
- **Que son:** Articulos de opinion (Seeking Alpha, Motley Fool), tweets de "influencers", comentarios en foros, titulares de prensa, notas de prensa de la empresa (promotional)
- **Como usar:** SOLO como termometro de sentimiento. NUNCA como base para decisiones
- **Protocolo:**
  1. Quien dice esto y que gana con ello?
  2. Que evidencia presenta? (si ninguna → descartar)
  3. Este argumento es refutable con datos?
- **Ejemplo:** "XYZ is the next 10-bagger" → sentimiento, no analisis

### Nivel 4: CONSENSO (fiabilidad variable — la mas peligrosa)
- **Que son:** Consensus estimates (EPS, revenue), consensus price targets, "the market believes...", narrativas dominantes
- **Como usar:** Como BASE DE COMPARACION, no como verdad. El consenso ES el precio actual. Si estoy de acuerdo con el consenso, no tengo ventaja informacional
- **Protocolo:**
  1. Que implica el consenso? (usar `dcf_calculator.py --reverse`)
  2. Donde puede estar equivocado?
  3. Que evidencia tengo de que esta equivocado?
  4. Si mi thesis = consenso → no tengo edge → reconsiderar
- **Ejemplo:** "Consensus EPS $5.20" → dato util como comparacion. "Consensus says buy" → irrelevante

---

## Protocolo Anti-Absorcion de Narrativa

Cuando proceso informacion de internet (noticias, reportes, analisis):

```
PASO 1: Clasificar fuente (Nivel 1-4 arriba)
PASO 2: Separar HECHOS de INTERPRETACIONES
  - Hecho: "Revenue grew 8% YoY" (verificable)
  - Interpretacion: "Growth is accelerating" (puede ser cherry-picking)
PASO 3: Buscar evidencia CONTRARIA
  - Si solo encuentro confirmacion → sospecha de confirmation bias
  - Si fuente solo presenta un lado → sospecha de agenda
PASO 4: Preguntar "Skin in the game?"
  - Quien tiene dinero apostado a esta conclusion?
  - Insiders comprando/vendiendo? (insider_tracker.py)
  - Institucionales moviendo posiciones?
PASO 5: Formular MI conclusion basada en DATOS PRIMARIOS
  - NO adoptar la conclusion de otro
  - Razonar desde los datos hasta mi propia conclusion
```

---

## Validacion de 3 capas

1. Cuestionar datos WEB (sesgos del autor, errores, desactualizados, incentivos)
2. Cuestionar mi MEMORIA (training cutoff, contexto limitado, patrones mal generalizados)
3. Cuestionar mis DECISIONES (sesgos, inercia, confirmacion, autoridad, anclaje)

## Validacion de datos web
- 2+ fuentes PRIMARIAS coinciden → probablemente correcto
- Fuentes contradicen → EXPLICITAR discrepancia, investigar cual tiene razon
- Dato critico → buscar investor relations oficial o filing directo
- Imposible validar → dar rango y DECIR que no esta validado (ej: "P/E ~15-20x, no verificado contra filing")

## Sesgos a evitar
1. **Geografico**: Foco en una region sin justificacion
2. **Confirmacion**: Buscar solo lo que confirma hipotesis
3. **Disponibilidad**: Elegir lo facil vs lo mejor
4. **Inercia**: Continuar camino sin revaluar
5. **Autoridad**: Aceptar conclusion de analista prestigioso sin verificar datos
6. **Anclaje**: Fijar precio target al consensus y ajustar desde ahi
7. **Narrativa**: Adoptar la "historia" que cuenta la prensa sin verificar premisas

## Autocritica OBLIGATORIA antes de recomendar
- Asunciones: [listar]
- Sesgos detectados: [listar]
- Evidencia ignorada: [listar]
- Validacion: [como valide informacion critica — fuentes Nivel 1/2/3/4]
- Alternativas consideradas: [que mas mire]
- **Donde mi analisis depende de opinion de terceros?** [listar — si >0, reforzar con datos primarios]

## Escepticismo sano

- **Management guidance**: Tipicamente optimista. Comparar guidance historico vs resultados reales de ESTA empresa para calibrar. No aplicar descuento fijo — razonar caso a caso
- **Analistas sell-side**: Incentivados a upgrades y a generar volumen de trading. Sus DATOS pueden ser utiles, sus CONCLUSIONES deben verificarse independientemente
- **"Blockbusters futuros"**: La mayoria de productos en pipeline no llegan a mercado. Calibrar probabilidad con datos de la industria especifica, no con un haircut generico
- **Suma de partes**: El mercado suele tener razon en descuentos de holding — investigar POR QUE antes de asumir "oportunidad"
- **Consensus price targets**: Son promedios de opiniones con incentivos mixtos. El consenso YA esta en el precio. Si mi FV = consensus PT, no tengo edge

---

**Framework Version:** 4.1
**Ultima actualizacion:** 2026-02-18
