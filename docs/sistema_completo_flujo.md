# Sistema Completo — Flujo Integrado Long + Short + Reverse DCF

> Para el humano. Sin jerga innecesaria. Cómo funciona TODO junto.

---

## LA PREGUNTA CENTRAL (todo empieza aquí)

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   "¿DÓNDE SE EQUIVOCA EL MERCADO?"                     │
│                                                         │
│   El mercado pone un precio a cada empresa.             │
│   Ese precio IMPLICA asunciones sobre el futuro.        │
│   Si esas asunciones son incorrectas → oportunidad.     │
│                                                         │
│   Herramienta: REVERSE DCF                              │
│   Input: precio actual + datos de la empresa            │
│   Output: "el mercado asume X% de crecimiento"          │
│                                                         │
└─────────────────────┬───────────────────────────────────┘
                      │
          ┌───────────┼───────────────┐
          ▼           ▼               ▼
    El mercado      El mercado      El mercado
    INFRAVALORA     TIENE RAZÓN     SOBREVALORA
    (asume peor     (no hay gap)    (asume mejor
     de lo real)                     de lo real)
          │               │               │
          ▼               ▼               ▼
     CANDIDATO        IGNORAR        CANDIDATO
       LONG          (no operar)       SHORT
```

---

## CICLO ANUAL — Vista de pájaro

```
AÑO COMPLETO
═══════════════════════════════════════════════════════════════

ENE ──── FEB ──── MAR ──── ABR ──── MAY ──── JUN
 │        │        │        │        │        │
 │   Earnings    Earnings   │   Earnings      │
 │   Season Q4   Season Q4  │   Season Q1     │
 │        │        │        │        │        │
 ├────────┴────────┘        ├────────┴────────┘
 │  ESCANEO TRIMESTRAL      │  ESCANEO TRIMESTRAL
 │  Reverse DCF universo    │  Reverse DCF universo
 │  ¿Dónde están los gaps?  │  ¿Nuevos gaps?
 │                          │
JUL ──── AGO ──── SEP ──── OCT ──── NOV ──── DIC
 │        │        │        │        │        │
 │   Earnings              Earnings           │
 │   Season Q2             Season Q3          │
 │        │                 │        │        │
 ├────────┴────────┐        ├────────┴────────┤
 │  ESCANEO TRIM.  │        │  ESCANEO TRIM.  │
 │  + REVISIÓN     │        │  + REVISIÓN     │
 │  ANUAL MEDIO    │        │  CIERRE AÑO     │
 │                 │        │                 │

CONTINUO TODO EL AÑO:
  ◆ Monitoreo diario (noticias, precios, kill conditions)
  ◆ Rebalanceo mensual (rotation check)
  ◆ Standing orders vigilados (alertas de precio)
  ◆ Pipeline avanzando (análisis de candidatos)
```

---

## CICLO MENSUAL — Lo que pasa cada mes

```
SEMANA 1                SEMANA 2                SEMANA 3                SEMANA 4
────────                ────────                ────────                ────────

┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ ESCANEO      │   │ PIPELINE     │   │ MONITOREO    │   │ REBALANCEO   │
│              │   │              │   │              │   │              │
│ Reverse DCF  │   │ Avanzar      │   │ Posiciones   │   │ Forward      │
│ en universo  │   │ candidatos   │   │ activas:     │   │ return de    │
│ (76+ empr.)  │   │ por pipeline │   │              │   │ todo:        │
│              │   │              │   │ • Noticias   │   │              │
│ ¿Nuevos gaps?│   │ • R1→R2→R3  │   │ • Earnings   │   │ • Bottom 3   │
│ ¿Gaps que    │   │ • R4 comité  │   │ • Kill cond. │   │   longs      │
│  cerraron?   │   │              │   │ • Carry      │   │ • Shorts     │
│              │   │ Si aprobado: │   │   (shorts)   │   │   sin juice  │
│ Priorizar    │   │ → Standing   │   │              │   │              │
│ los mayores  │   │   Order      │   │ Si problema: │   │ ¿Rotar?     │
│              │   │              │   │ → Acción     │   │ ¿Cubrir?    │
└──────┬───────┘   └──────┬───────┘   └──────┬───────┘   └──────┬───────┘
       │                  │                  │                  │
       ▼                  ▼                  ▼                  ▼
  Candidatos         Standing           Decisiones          Portfolio
  priorizados        Orders             de mantener/        optimizado
                     actualizados       salir
```

---

## EL PIPELINE — De "idea" a "dinero invertido"

```
                        ┌─────────────────────┐
                        │  REVERSE DCF SCAN   │
                        │  "El mercado asume   │
                        │   3% crecimiento,    │
                        │   pero la empresa    │
                        │   crece al 12%"      │
                        │   → GAP DETECTADO    │
                        └──────────┬──────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    ▼                              ▼
            GAP = INFRAVALORA              GAP = SOBREVALORA
            (candidato LONG)               (candidato SHORT)
                    │                              │
                    ▼                              ▼
    ┌───────────────────────────┐  ┌───────────────────────────┐
    │ PIPELINE LONG (4 rondas) │  │ PIPELINE SHORT (4 rondas) │
    │                          │  │                            │
    │ R1: Análisis fundamental │  │ S1: Análisis de fragilidad │
    │     + Moat + Riesgos     │  │     + Moat erosion         │
    │     + Valoración         │  │     + Valoración real      │
    │     (3 agentes paralelo) │  │     (3 agentes paralelo)   │
    │          │               │  │          │                 │
    │ R2: Devil's advocate     │  │ S2: Devil's advocate BULL  │
    │     "¿Por qué NO         │  │     "¿Por qué el precio   │
    │      comprar?"           │  │      PODRÍA tener razón?"  │
    │          │               │  │          │                 │
    │ R3: Resolución           │  │ S3: Resolución             │
    │     ¿Quién tiene razón?  │  │     ¿Fragilidad real?      │
    │          │               │  │          │                 │
    │ R4: Comité (10 gates)    │  │ S4: Comité short           │
    │     APROBADO / RECHAZADO │  │     + Gate: ¿catalizador?  │
    │          │               │  │     APROBADO / RECHAZADO   │
    └──────────┼───────────────┘  └──────────┼────────────────┘
               │                              │
               ▼                              ▼
    ┌─────────────────────┐       ┌─────────────────────┐
    │  STANDING ORDER     │       │  STANDING ORDER      │
    │  (alerta de precio) │       │  SHORT               │
    │                     │       │  (alerta de precio)   │
    │  "Si baja a $X,     │       │  "Si sube a $X,       │
    │   avisarme para     │       │   avisarme para       │
    │   validar y comprar"│       │   validar y shortear" │
    └──────────┬──────────┘       └──────────┬────────────┘
               │                              │
               │    PRECIO TOCA TRIGGER       │
               │                              │
               ▼                              ▼
    ┌──────────────────────────────────────────────────────┐
    │              FAST-TRACK VALIDATION                   │
    │         (NO es compra automática)                    │
    │                                                      │
    │  1. ¿Thesis sigue vigente? (¿algo cambió?)          │
    │  2. ¿Noticias recientes que afecten?                │
    │  3. ¿Kill conditions / Hard gates?                  │
    │  4. Reverse DCF a precio actual: ¿gap sigue?        │
    │  5. ¿Restricciones de portfolio?                    │
    │  6. ¿Capital allocation óptima?                     │
    │                                                      │
    │  TODO OK ──→ RECOMIENDO COMPRAR/SHORTEAR            │
    │  ALGO FALLA ──→ RE-EVALUAR (rápido, no pipeline)    │
    │  THESIS MUERTA ──→ CANCELAR standing order          │
    └──────────────────────┬───────────────────────────────┘
                           │
                           ▼
    ┌──────────────────────────────────────────────────────┐
    │              HUMANO CONFIRMA → EJECUTA EN eToro      │
    └──────────────────────────────────────────────────────┘
```

---

## EL PORTFOLIO EN OPERACIÓN — Día a día

```
┌─────────────────────────────────────────────────────────────────┐
│                    PORTFOLIO COMPLETO                            │
│                                                                 │
│  ┌────────────────────┐  ┌──────────┐  ┌────────────────────┐  │
│  │   LONGS (85-100%)  │  │  CASH    │  │  SHORTS (0-15%)    │  │
│  │                    │  │  (0-20%) │  │                    │  │
│  │  Quality           │  │          │  │  Empresas frágiles │  │
│  │  Compounders       │  │  Reserva │  │  con catalizador   │  │
│  │  QS alto           │  │  para    │  │  y fecha           │  │
│  │  Moat ancho        │  │  oportu- │  │                    │  │
│  │  ROIC >> WACC      │  │  nidades │  │  Coste: ~7%/año    │  │
│  │                    │  │          │  │  Duración: meses   │  │
│  │  Generan valor     │  │          │  │  Generan alpha     │  │
│  │  con el tiempo     │  │          │  │  en crisis         │  │
│  └────────────────────┘  └──────────┘  └────────────────────┘  │
│                                                                 │
│  NET EXPOSURE = Longs - Shorts                                  │
│  Ejemplo: 90% long - 5% short = 85% net exposure al mercado    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

MONITOREO CONTINUO:
═══════════════════

  CADA SESIÓN (2-3 por semana):
  ┌─────────────────────────────────────────────────────────┐
  │ 1. Noticias de TODAS las posiciones (long + short)     │
  │ 2. Precios vs triggers de standing orders              │
  │ 3. Kill conditions: ¿alguna activada?                  │
  │ 4. Carry acumulado de shorts: ¿aceptable?              │
  │ 5. Earnings próximos: ¿framework preparado?            │
  └─────────────────────────────────────────────────────────┘

  CADA MES:
  ┌─────────────────────────────────────────────────────────┐
  │ 1. Forward return de cada posición                     │
  │ 2. Bottom 3 longs → ¿rotar hacia mejor candidato?     │
  │ 3. Shorts sin potencial → ¿cubrir?                    │
  │ 4. Rebalanceo si alguna posición >1.3x o <0.7x target │
  │ 5. Standing orders: ¿thesis todavía frescos?           │
  │ 6. Reverse DCF universo: ¿nuevos gaps?                │
  └─────────────────────────────────────────────────────────┘

  CADA TRIMESTRE:
  ┌─────────────────────────────────────────────────────────┐
  │ 1. Revisión profunda de CADA posición                  │
  │ 2. Sector views actualizados                           │
  │ 3. Macro view actualizado                              │
  │ 4. Effectiveness tracker: ¿estamos generando alpha?    │
  │ 5. Standing orders > 60 días: REVALIDAR o CANCELAR     │
  └─────────────────────────────────────────────────────────┘
```

---

## REBALANCEO Y ROTACIÓN — Cómo mejora el portfolio con el tiempo

```
PRINCIPIO: El portfolio SIEMPRE debe gravitar hacia más calidad.
           Vender lo peor, comprar lo mejor. Continuamente.

CADA MES:
                    ┌─────────────────────────────────┐
                    │     FORWARD RETURN ANALYSIS      │
                    │                                  │
                    │  Cada posición tiene:            │
                    │  • MoS% (cuánto puede subir)     │
                    │  • Growth% (cuánto crece/año)    │
                    │  • Yield% (dividendo)            │
                    │  • QS (calidad de la empresa)    │
                    │                                  │
                    │  Forward Return =                │
                    │    MoS + Growth + Yield           │
                    └────────┬────────────────────────┘
                             │
              ┌──────────────┴──────────────┐
              ▼                              ▼
     ┌─────────────────┐          ┌─────────────────┐
     │   BOTTOM 3      │          │    TOP 3        │
     │   (peores)      │          │    (mejores)    │
     │                 │          │                 │
     │  Bajo MoS       │          │  Alto MoS       │
     │  + Bajo QS      │          │  + Alto QS      │
     │  + Bajo Growth   │          │  + Alto Growth   │
     │                 │          │                 │
     │  CANDIDATOS     │          │  CANDIDATOS     │
     │  A VENDER       │          │  A COMPRAR/ADD  │
     └────────┬────────┘          └────────┬────────┘
              │                              │
              │     ¿El bottom 3 tiene       │
              │     MENOS forward return     │
              │     que el top 3 del         │
              │     pipeline?                │
              │              │               │
              │         SÍ ──┤── NO          │
              │              │               │
              ▼              │               │
     ┌────────────────┐      │     ┌─────────────────┐
     │ ROTAR:         │      │     │ MANTENER:       │
     │ Vender bottom, │      │     │ No hay mejor    │
     │ comprar top    │      │     │ alternativa.    │
     │ del pipeline   │      │     │ Esperar.        │
     └────────────────┘      │     └─────────────────┘
                             │
                    ┌────────┴────────────────────────┐
                    │   REVERSE DCF VALIDA:            │
                    │                                  │
                    │   "¿El bottom 3 realmente        │
                    │    no tiene gap? ¿O el mercado   │
                    │    lo infravalora y debería       │
                    │    MANTENER?"                     │
                    │                                  │
                    │   "¿El top del pipeline           │
                    │    realmente tiene gap? ¿O el     │
                    │    mercado tiene razón?"          │
                    │                                  │
                    │   → Evita rotar por rotar         │
                    └──────────────────────────────────┘
```

---

## EL CICLO ANTI-CÍCLICO — La máquina completa en crisis

```
ESTADO NORMAL (mercado estable):
════════════════════════════════

    Portfolio: 90% longs + 5% cash + 5% shorts (si hay fragilidad)
    Reverse DCF: escaneos trimestrales, pocos gaps extremos
    Standing orders: esperando pacientemente

FRAGILIDAD DETECTADA (algo se rompe en un sector):
══════════════════════════════════════════════════

    1. Reverse DCF muestra gap EXTREMO al alza en sector X
       (mercado sobrevalora masivamente)

    2. Pipeline short S1→S4 confirma fragilidad

    3. Abrir short selectivo (5-10% del portfolio)

    4. Simultáneamente: standing orders de longs en otros sectores
       siguen activos, esperando

CRISIS (el sector X colapsa):
═════════════════════════════

    ┌─────────────────────────────────────────┐
    │                                         │
    │   SHORT genera +30-50% en semanas       │
    │              │                           │
    │              ▼                           │
    │   CUBRIR short → CASH                   │
    │              │                           │
    │              ▼                           │
    │   Quality compounders TAMBIÉN caen       │
    │   por contagio (pánico general)          │
    │              │                           │
    │              ▼                           │
    │   Standing orders de LONGS se activan    │
    │   (precios tocan triggers)              │
    │              │                           │
    │              ▼                           │
    │   Fast-track validation → COMPRAR        │
    │   quality compounders EN REBAJAS         │
    │              │                           │
    │              ▼                           │
    │   Mercado se recupera → longs suben      │
    │                                         │
    │   RESULTADO: Convertiste la crisis en    │
    │   MÁQUINA DE COMPRAR BARATO             │
    │                                         │
    └─────────────────────────────────────────┘
```

---

## TIMELINE DE UN CANDIDATO — De descubrimiento a salida

```
MES 0: DESCUBRIMIENTO
    Reverse DCF scan → "Empresa X cotiza como si creciera 3%,
                         pero crece al 12%. Gap = grande"
    → Entra en pipeline

MES 0-1: ANÁLISIS (Pipeline R1→R4)
    R1: Fundamental + Moat + Riesgo + Valoración (paralelo, 1 sesión)
    R2: Devil's advocate (siguiente sesión)
    R3: Resolución de conflictos (si necesario)
    R4: Comité de inversión (10 gates)

    → Si APROBADO: Standing Order creado
    → Si RECHAZADO: Archivo con razón

MES 1-6: ESPERA (Standing Order activo)
    Precio no ha tocado trigger todavía.
    CADA MES: ¿Thesis sigue fresca? ¿Reverse DCF confirma gap?
    Si thesis caduca (>60 días) → Revalidar o Cancelar

MES X: TRIGGER TOCA
    Precio llega al trigger.
    → Humano me avisa
    → Fast-track validation (6 checks)
    → Si OK: "Compra" → Humano ejecuta en eToro
    → Si no OK: "No compres, esto cambió" → Re-evaluar

MES X+1 en adelante: POSICIÓN ACTIVA
    Monitoreo continuo:
    • Noticias, earnings, kill conditions
    • Forward return vs pipeline
    • Rebalanceo mensual

    Tres destinos posibles:

    ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
    │  MANTENER   │  │    ROTAR    │  │   VENDER    │
    │             │  │             │  │             │
    │  Thesis     │  │  Mejor      │  │  Kill cond. │
    │  intacta.   │  │  candidato  │  │  activada.  │
    │  QS alto.   │  │  en pipeline│  │  Thesis     │
    │  Sigue      │  │  Forward    │  │  rota.      │
    │  compounding│  │  return >>  │  │  Fragilidad │
    │             │  │  esta       │  │  nueva.     │
    │  IDEAL:     │  │  posición   │  │             │
    │  Para       │  │             │  │  EXIT       │
    │  siempre    │  │  VENDE →    │  │  Protocol   │
    │             │  │  COMPRA     │  │  (6 gates)  │
    └─────────────┘  │  mejor      │  └─────────────┘
                     └─────────────┘
```

---

## RESUMEN EN UNA PÁGINA

```
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   1. ESCANEAR: Reverse DCF → ¿dónde se equivoca el mercado? ║
║                                                               ║
║   2. ANALIZAR: Pipeline 4 rondas → ¿es real el gap?          ║
║                                                               ║
║   3. PREPARAR: Standing order → alerta de precio + thesis     ║
║                                                               ║
║   4. VALIDAR: Cuando toca precio → fast-track (NO auto-buy)  ║
║                                                               ║
║   5. EJECUTAR: Humano confirma → compra/shortea en eToro      ║
║                                                               ║
║   6. MONITOREAR: Noticias, earnings, kill conditions, carry   ║
║                                                               ║
║   7. REBALANCEAR: Cada mes → rotar hacia más calidad          ║
║                                                               ║
║   8. REPETIR: El reverse DCF corre continuamente              ║
║               buscando nuevos gaps                             ║
║                                                               ║
║   ─────────────────────────────────────────────────────────   ║
║                                                               ║
║   LONG: Empresa buena + mercado pesimista = COMPRAR           ║
║   SHORT: Empresa frágil + mercado optimista = SHORTEAR        ║
║   NADA: Mercado tiene razón = NO OPERAR                       ║
║                                                               ║
║   El reverse DCF es el DETECTOR.                              ║
║   El pipeline es el VALIDADOR.                                ║
║   Los standing orders son las ALERTAS.                        ║
║   La fast-track validation es el ÚLTIMO CHECK.                ║
║   El rebalanceo es la OPTIMIZACIÓN CONTINUA.                  ║
║   El humano es quien EJECUTA.                                 ║
║   Claude es quien DECIDE.                                     ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## DIFERENCIAS vs SISTEMA ACTUAL

| Aspecto | AHORA | CON REVERSE DCF + SHORTS |
|---------|-------|--------------------------|
| Punto de partida | "¿Es buena empresa?" | "¿Dónde se equivoca el mercado?" |
| Dirección | Siempre LONG | LONG, SHORT, o NO OPERAR como output |
| Standing orders | Auto-ejecutables | Alertas + fast-track validation |
| Rebalanceo | Forward return longs | Forward return longs + shorts + net exposure |
| En crisis | Aguantar + cash | Short genera cash → comprar longs en rebajas |
| Scanning | Quality universe (QS alto) | Quality universe + Fragility universe |
| Frecuencia scan | Ad-hoc | Trimestral sistemático (reverse DCF) |
| Thesis freshness | Sin control | >60 días → revalidar o cancelar |

---

*Documento creado: Session 73, 2026-02-17*
*Para referencia del humano. No es implementación — es diseño conceptual.*
