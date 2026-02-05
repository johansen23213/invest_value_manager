---
name: portfolio-constraints
description: "Framework v4.0 - Portfolio context and principles for sizing decisions. NO FIXED LIMITS."
user-invocable: false
disable-model-invocation: false
---

# Portfolio Context Skill - Framework v4.0

## IMPORTANTE: Este Skill NO Contiene Límites Fijos

Framework v4.0 eliminó los límites fijos (7%, 25%, 35%, etc.).
Este skill provee CONTEXTO para razonar, no reglas para seguir.

Para decisiones de sizing, consultar:
- `learning/principles.md` - Los 8 principios de inversión
- `learning/decisions_log.yaml` - Precedentes para consistencia

---

## Contexto de Portfolio

### Herramienta: constraint_checker.py

```bash
python3 tools/constraint_checker.py REPORT    # Ver estado actual
python3 tools/constraint_checker.py CHECK TICKER AMOUNT  # Simular compra
```

Este tool provee DATOS:
- Concentración por posición (% del portfolio)
- Concentración sectorial
- Concentración geográfica
- Cash disponible
- Impacto de pérdida 50% por posición

El tool NO juzga. Tú razonas aplicando principios.

---

## Principios Relevantes (de principles.md)

### Principio 1: Sizing por Convicción y Riesgo
- El tamaño refleja convicción, no un límite fijo
- Pregunta: "Si cae 50%, ¿el impacto es coherente con mi convicción?"

### Principio 2: Diversificación Geográfica
- Riesgo país NO es igual para todos
- Desarrollados estables vs emergentes
- Pregunta: "¿Mi exposición a riesgos similares es prudente?"

### Principio 3: Diversificación Sectorial
- Sectores correlacionados aumentan riesgo conjunto
- Pregunta: "¿Cuál es mi exposición a un shock sectorial?"

### Principio 4: Cash como Posición Activa
- Cash tiene coste de oportunidad
- Pero también permite actuar en oportunidades
- Pregunta: "¿Tengo oportunidades claras para desplegar?"

---

## Patrones Observados (NO límites)

Los siguientes son PATRONES observados en decisiones pasadas,
documentados en `decisions_log.yaml`. NO son límites a seguir ciegamente.

### Sizing Histórico por Tier
| Tier | Patrón Observado | Contexto |
|------|------------------|----------|
| A | 3-5% inicial | Quality Compounders con alta convicción |
| B | 3-5% full | Quality Value, balance riesgo/retorno |
| C | 2-4% | Special Situations, mayor incertidumbre |

### Consideraciones de Concentración
| Dimensión | Patrón | Razonamiento |
|-----------|--------|--------------|
| Posición individual | ~5-7% máx históricamente | Limitar impacto de pérdida en una sola tesis |
| Sector | ~20-25% típico | Evitar shock sectorial devastador |
| Geografía | ~30-35% típico | Considerar riesgo país, divisa |
| Cash | Variable | Depende de oportunidades disponibles |

**RECUERDA:** Estos patrones son para INFORMAR tu razonamiento,
no para seguir ciegamente. Si tu situación difiere, documenta por qué.

---

## Proceso de Decisión de Sizing

```
1. Ejecutar constraint_checker.py CHECK TICKER AMOUNT
2. Leer el output (datos crudos)
3. Aplicar principios 1-4 de principles.md
4. Consultar precedentes similares en decisions_log.yaml
5. Razonar explícitamente:
   - ¿El sizing propuesto es coherente con mi convicción?
   - ¿El impacto de pérdida 50% es aceptable?
   - ¿Aumenta concentración de riesgo de forma imprudente?
6. Documentar el razonamiento
7. Si me desvío de patrones, explicar por qué
```

---

## Anti-Patrones (Qué NO Hacer)

- "Rechazo porque supera 7%" → NO. Razona por qué ese sizing específico.
- "Warning porque cash > 15%" → NO. ¿Hay oportunidades? ¿Contexto macro?
- "EU 37%, warning" → NO. ¿Cuál es el riesgo real de esa exposición?

---

## Referencias

| Necesito... | Ver... |
|-------------|--------|
| Principios de sizing | `learning/principles.md` |
| Precedentes | `learning/decisions_log.yaml` |
| Datos actuales | `python3 tools/constraint_checker.py REPORT` |

---

**Framework Version:** 4.0
**Última actualización:** 2026-02-05
