# System Improvements Proposal — 2026-02-14

> Mejoras priorizadas basadas en la auditoria completa del sistema.
> Cada propuesta incluye: que arreglar, por que, esfuerzo estimado, e impacto.

---

## CRITICAL (Errores que pueden causar decisiones incorrectas)

### C1. Anadir canonical FV headers a 13 thesis activas
**Que:** Anadir `> **Fair Value:** $XXX` como primera linea util de cada thesis en thesis/active/
**Por que:** forward_return.py PRIORITY 0 pattern depende de este header para parsear FV. Sin el, el tool puede coger un FV stale del body o fallar silenciosamente. Esto afecta el Rotation Check diario (FASE 2.5).
**Ficheros:** ALL, AUTO.L, BYIT.L, DOM.L, DTE.DE, EDEN.PA, GL, LULU, NVO (+ corregir formato DKK→USD)
**Esfuerzo:** 15 minutos (batch edit)
**Impacto:** forward_return.py producira datos correctos
**Nota:** ADBE y MONY.L ya lo tienen. Los R4 en research/ (ROP, VLTO, MMC, ACGL, DNLM.L, RACE.MI) tambien lo tienen excepto DSY.PA.

---

## HIGH (Inconsistencias que degradan la fiabilidad del sistema)

### H1. Archivar HRB y SAN.PA de thesis/active/
**Que:** Mover thesis/active/HRB/ → thesis/archive/HRB/ y thesis/active/SAN.PA/ → thesis/archive/SAN.PA/. Eliminar thesis/active/TATE.L/ (ya existe en archive).
**Por que:** Ambas posiciones vendidas el 2026-02-09. Violan el protocolo de lifecycle documentado en file-structure.md. Cualquier agente que escanee thesis/active/ vera 14 directorios en vez de 11, creando confusion.
**Esfuerzo:** 2 minutos (mv commands)
**Impacto:** Consistencia filesystem con portfolio real

### H2. Documentar 4 tools en tools-reference.md
**Que:** Anadir documentacion para consistency_checker.py, drift_detector.py, opportunity_filter.py, system_projection.py
**Por que:** Estos tools existen, son referenciados en session-protocol.md y error-patterns.md, pero no tienen documentacion de uso. Un agente o sesion futura no sabra como usarlos.
**Esfuerzo:** 20 minutos (leer cada tool, documentar usage)
**Impacto:** Descubribilidad y usabilidad de tools

### H3. Renombrar RACE.MI investment_committee.md → committee_decision.md
**Que:** Renombrar el fichero para seguir la convencion de todos los demas R4_APPROVED
**Por que:** 6 de 7 R4_APPROVED usan committee_decision.md. RACE.MI es el unico con investment_committee.md. Cualquier script o agente que busque committee_decision.md no lo encontrara.
**Esfuerzo:** 1 minuto (mv command)
**Impacto:** Consistencia de naming

### H4. Resolver MA y V: standing orders sin R4 pipeline completo
**Que:** Decidir una de dos opciones:
  - **Opcion A:** Cancelar las standing orders de MA y V hasta que completen buy-pipeline R4 (consistent con governance)
  - **Opcion B:** Mantenerlas pero con flag explicito "PRE-PIPELINE — No ejecutar sin R4" (ya tienen WARNING pero es sutil)
**Por que:** Actualmente tienen WARNING en las notas, pero la standing order EXISTE y podria confundir. Son las unicas standing orders sin R4 que no tienen "CANCELLED" status.
**Esfuerzo:** 5 minutos
**Impacto:** Claridad de governance. Evita ejecucion prematura.
**Nota:** MA esta a $538 (71% del trigger $315) y V a $329 (50% del trigger $220) — ambas MUY lejos. Riesgo bajo de ejecucion accidental.

### H5. Completar quality_universe entries para MA y V
**Que:** Actualizar thesis_path de NULL a la ruta real en quality_universe.yaml
**Por que:** El campo thesis_path NULL rompe cualquier tool que intente leer la thesis desde quality_universe
**Esfuerzo:** 2 minutos
**Impacto:** Integridad de datos

### H6. Actualizar file-structure.md: 10 sectores → 26
**Que:** Actualizar la tabla "Sectores documentados actuales" en .claude/rules/file-structure.md
**Por que:** La tabla lista 10 sectores pero hay 26. Documentacion completamente stale.
**Esfuerzo:** 10 minutos
**Impacto:** Documentacion precisa

---

## MEDIUM (Mejoras de calidad y mantenimiento)

### M1. Anadir canonical FV header a DSY.PA (R4_APPROVED)
**Que:** Anadir `> **Fair Value:** EUR 20.00` al thesis de DSY.PA
**Por que:** Unico R4_APPROVED sin canonical header. forward_return.py parsing afectado.
**Esfuerzo:** 1 minuto
**Impacto:** Parsing correcto

### M2. Corregir NVO thesis FV format
**Que:** Cambiar thesis header de "DKK 491" a "> **Fair Value:** $66 (DKK 491)" o sincronizar con portfolio/current.yaml
**Por que:** Portfolio dice "$66 (DKK 491)" pero thesis solo dice "DKK 491". forward_return.py puede fallar en conversion.
**Esfuerzo:** 2 minutos
**Impacto:** Consistencia de datos FV

### M3. Incorporar CPI data a world view
**Que:** Actualizar world/current_view.md con resultado CPI Jan 2026 (2.4% YoY, publicado Feb 13)
**Por que:** El world view dice "CPI Jan 2026 pendiente" pero ya se publico. Stale data.
**Esfuerzo:** 5 minutos (via macro-analyst o manual)
**Impacto:** World view preciso para decisiones

### M4. Formalizar price_monitors section
**Que:** Crear seccion explicitada en system.yaml con ticker, trigger, last_check para cada standing order
**Por que:** Actualmente las alertas estan dispersas. Un formato estructurado facilita el checking diario.
**Esfuerzo:** 15 minutos
**Impacto:** Operaciones mas eficientes

### M5. Reframear "25% cash" en CLAUDE.md
**Que:** Cambiar "PRIORIDAD #1 mientras cash > 25%" a algo como "Cuando cash es elevado (patron historico: >25%), capital deployment es prioridad. No es regla fija."
**Por que:** Framework v4.0 dice "no fixed numbers" pero esto lee como regla hardcodeada.
**Esfuerzo:** 2 minutos
**Impacto:** Consistencia con filosofia v4.0

### M6. Nuancear MoS pattern en decisions_log
**Que:** Cambiar "18.4% floor with exceptional WIDE moat" a incluir que MMC 18.4% fue con HALF POSITION + exceptional moat. No es un floor universal.
**Por que:** Descripcion actual oversimplifica el precedente. Un futuro analisis podria citar "18.4% es acceptable" sin las condiciones.
**Esfuerzo:** 2 minutos
**Impacto:** Precedentes mas precisos

### M7. Anadir FGP.L, CMCSA, WPP.L a quality_universe
**Que:** Registrar con pipeline_status PRE_R1 o CONDITIONAL
**Por que:** Standing orders existen pero no estan trackeadas en el universe. Inconsistente con el principio de "organismo vivo".
**Esfuerzo:** 5 minutos
**Impacto:** Tracking completo

### M8. Poner fecha a digital-marketplaces.md
**Que:** Anadir fecha de creacion/actualizacion al sector view
**Por que:** Unico sector view sin fecha. Imposible saber si es stale.
**Esfuerzo:** 1 minuto
**Impacto:** Staleness tracking

### M9. Completar CLAUDE.md quick reference con skills faltantes
**Que:** Anadir las 16 skills que existen en disco pero no estan en la tabla "Referencias Rapidas"
**Por que:** Skills como agent-coordination, portfolio-constraints, re-evaluation-protocol existen pero no son discoverable via quick reference.
**Esfuerzo:** 10 minutos
**Impacto:** Descubribilidad

---

## LOW (Nice-to-have, mejoras incrementales)

### L1. Estandarizar Analysis Date headers en thesis files
**Que:** Anadir "Analysis Date: YYYY-MM-DD" a las primeras lineas de cada thesis
**Por que:** ~50% no lo tienen. Hace audit trail dificil.
**Esfuerzo:** 15 minutos (batch)
**Impacto:** Trazabilidad

### L2. Documentar "Conditional Approval" pattern en decisions_log
**Que:** Anadir seccion patterns.conditional_approvals con RACE.MI, DSY.PA, MMC
**Por que:** Patron emergente no documentado. Podria perderse.
**Esfuerzo:** 5 minutos
**Impacto:** Precedentes completos

### L3. Anadir Pipeline Stage a thesis file headers
**Que:** Incluir "Pipeline: R4_APPROVED" en el header de cada thesis (ademas de en quality_universe)
**Por que:** Actualmente pipeline status SOLO en quality_universe.yaml = single point of failure
**Esfuerzo:** 10 minutos (batch)
**Impacto:** Redundancia de datos

### L4. Anadir valuation_report.md a ROP, VLTO, ACGL
**Que:** Crear fichero separado de valoracion (actualmente inline en thesis)
**Por que:** 3 de 7 R4_APPROVED no tienen este fichero. Los otros 4 si.
**Esfuerzo:** 30 minutos (extraer de thesis)
**Impacto:** Completitud del pipeline

### L5. Automatizar reincidencia tracking
**Que:** Crear un formato machine-readable en error-patterns.md para contar reincidencias
**Por que:** Actualmente manual. Dificil detectar patterns de errores repetidos.
**Esfuerzo:** 15 minutos
**Impacto:** Deteccion temprana de errores recurrentes

---

## EXECUTION PLAN (sugerido)

### Batch 1: Quick wins (30 min, maximo impacto)
- C1: Canonical FV headers (13 thesis activas)
- H1: Archivar HRB, SAN.PA, limpiar TATE.L
- H3: Renombrar RACE.MI committee file
- M1: DSY.PA canonical header
- M2: NVO FV format

### Batch 2: Data integrity (15 min)
- H5: MA y V thesis_path en quality_universe
- M7: FGP.L, CMCSA, WPP.L en quality_universe
- M8: Fecha a digital-marketplaces.md

### Batch 3: Documentation (30 min)
- H2: Documentar 4 tools
- H6: Actualizar file-structure.md sectores
- M9: CLAUDE.md quick reference skills

### Batch 4: Governance refinement (10 min)
- H4: Decidir MA/V standing orders
- M5: Reframear 25% cash
- M6: Nuancear MoS pattern

### Batch 5: Optional cleanup
- L1-L5 a discrecion

---

## METRICAS POST-IMPLEMENTACION

Tras implementar Batch 1-4:

| Metrica | Antes | Despues |
|---------|-------|---------|
| Thesis con canonical header | 2/14 (14%) | 14/14 (100%) |
| Thesis orphanas en active/ | 3 | 0 |
| Tools documentados | 10/14 (71%) | 14/14 (100%) |
| R4 con committee_decision.md | 6/7 (86%) | 7/7 (100%) |
| quality_universe thesis_path NULL | 2 | 0 |
| file-structure.md sectores correct | 10/26 (38%) | 26/26 (100%) |
| Overall consistency score | 7/10 | 9/10 |
