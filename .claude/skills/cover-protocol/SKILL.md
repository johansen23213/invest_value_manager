# COVER PROTOCOL - Framework v4.0

> **Proceso estructurado para decidir cuando CUBRIR (cerrar) una posicion short.**
> Espejo del exit-protocol para longs.
> **NOTA v4.0:** Framework de razonamiento, no thresholds fijos.

---

## Proposito

Asi como exit-protocol estructura la decision de vender un long,
cover-protocol estructura la decision de cubrir un short.

La mecanica es diferente:
- En longs, el tiempo trabaja a favor (compounding)
- En shorts, el tiempo trabaja en contra (carry cost)
- Esto hace que la inercia natural deba ser CUBRIR, no mantener

---

## Cuando Ejecutar Este Protocolo

1. **Catalizador se acerca o paso** — verificar si thesis se materializo
2. **Carry acumulado supera umbral razonable** — razonar desde P10
3. **Review periodico** de shorts activos (semanal, no mensual como longs)
4. **Noticias positivas sobre la empresa** — la posicion va en contra
5. **Cuando hay mejor uso del capital** — liberar margen para otro short u oportunidad long
6. **Cuando el orchestrator lo solicite**

---

## 6 Gates de Cobertura

### Gate 1: Fragilidad Resuelta?

**Pregunta:** La empresa mejoro fundamentalmente?

- Nuevo management con track record credible
- Modelo de negocio pivoto exitosamente
- La dependencia oculta (Seccion 2 de thesis) dejo de ser dependencia
- Regulacion que esperabamos NO se materializo y el riesgo bajo

**Si la fragilidad ya no existe → CUBRIR.**

### Gate 2: Catalizador Vigente?

**Pregunta:** El catalizador identificado en la thesis sigue siendo viable?

- Si catalizador paso y NO tuvo efecto → CUBRIR (Error #45)
- Si catalizador se pospuso → Recalcular carry acumulado hasta nueva fecha. Sigue siendo rentable?
- Si catalizador se acerca → Evaluar probabilidad de que se materialice

**Sin catalizador vigente → CUBRIR. El carry sigue corriendo sin razon.**

### Gate 3: Beneficio Suficiente?

**Pregunta:** El precio alcanzo o supero el target?

- Si target alcanzado → CUBRIR (parcial o total segun conviccion)
- Si beneficio sustancial pero no en target → Razonar sobre tomar beneficios parciales
- Recordar: "los cerdos son sacrificados" — greed en shorts es mas peligroso que en longs

### Gate 4: Coste de Carry Aceptable?

**Pregunta:** El carry acumulado erosiona el retorno esperado?

- Calcular carry total desde apertura hasta hoy
- Proyectar carry hasta catalizador esperado
- Si carry total > 50% del beneficio esperado → la tesis se esta debilitando por tiempo
- Razonar desde P10 (Catalizador como Ancla Temporal)

### Gate 5: Mejor Uso del Capital?

**Pregunta:** Hay una oportunidad (long o short) con mejor forward return neto?

- Forward return del short actual (incluyendo carry restante)
- Forward return de alternativas disponibles
- Coste de cerrar y reabrir vs mantener
- Un short mediocre que consume margen impide un mejor short o un mejor long

### Gate 6: Friccion de Cobertura?

**Pregunta:** Hay costes ocultos o timing considerations?

- Spread en el momento de cubrir (volatilidad alta = spread alto)
- Impacto fiscal de cerrar con beneficio vs mantener
- Si empresa reporta earnings en dias → esperar o cubrir antes?

---

## Verdicts

| Veredicto | Significado |
|-----------|-------------|
| **HOLD SHORT** | Thesis intacta, catalizador vigente, carry aceptable |
| **COVER PARTIAL** | Tomar beneficios parciales, reducir exposicion |
| **COVER FULL** | Cerrar posicion completamente |

---

## Frecuencia

- **Shorts activos:** Revisar SEMANALMENTE (no mensualmente como longs)
- **Razon:** El carry corre cada dia. La inercia debe ser cuestionar, no mantener.
- **Pipeline tracker:** fragility_watch pipeline con cadencia semanal

---

## Post-Cobertura

1. Registrar en `portfolio/history.yaml` (P&L incluyendo carry total)
2. Mover thesis de `thesis/short/active/` → `thesis/archive/`
3. Actualizar sector view (si aplica)
4. Actualizar quality_universe (remover o mover)
5. Documentar leccion aprendida

---

**Ultima actualizacion:** 2026-02-18
**Framework version:** 4.0
