# Skill: Effectiveness Evaluation Framework v2.0

> Creado: 2026-02-03 | Actualizado: 2026-02-18
> Proposito: Evaluar sistematicamente la efectividad del sistema de inversion

## El Problema

Value investing tiene un problema fundamental: **no sabemos si nuestras predicciones son correctas hasta anos despues**. Esto crea riesgos:
- Confirmation bias (solo recordamos los aciertos)
- Survivorship bias (ignoramos errores que vendimos)
- Overconfidence (asumimos que entendemos el mercado)

## Solucion: Sistema de Evaluacion Multi-Horizonte

### 1. METRICAS DE CORTO PLAZO (< 3 meses)

**No predicen exito a largo plazo, pero detectan errores de timing.**

| Metrica | Que mide | Cuando investigar |
|---------|----------|-------------------|
| Win Rate (30d) | Precision de timing de entrada | Si tendencia descendente vs periodos anteriores |
| Max Drawdown posicion | Perdida no realizada maxima | Si varias posiciones con drawdown simultaneo |
| Volatilidad vs benchmark | Riesgo relativo | Si consistentemente mas volatil sin compensacion |
| Cash drag | Coste de oportunidad | Si pipeline esta vacio Y cash es alto — razonar contexto |

**Accion si metricas preocupan**: Investigar timing de entradas. El problema puede ser de CUANDO, no de QUE.

### 2. METRICAS DE MEDIO PLAZO (3-12 meses)

**Validan la calidad del analisis.**

| Metrica | Que mide | Cuando investigar |
|---------|----------|-------------------|
| Win Rate (12m) | Calidad de seleccion | Si deterioro sostenido vs nuestro baseline historico |
| Thesis On-Track Rate | Precision de thesis | Si mayoria de thesis se invalidan — revisar framework de analisis |
| Avg Return vs FV | Convergencia a valor | Si posiciones no convergen despues de holding period esperado |
| Sharpe Ratio | Retorno ajustado a riesgo | Si negativo sostenido — cuestionar el proceso completo |

**Accion si metricas preocupan**: Revisar framework de analisis (business understanding, projections, moat assessment).

### 3. METRICAS DE LARGO PLAZO (1-5 anos)

**Validan la estrategia completa.**

| Metrica | Que mide | Cuando investigar |
|---------|----------|-------------------|
| FV Hit Rate | Prediccion de fair value | Comparar vs historico propio y calibrar si hay sesgo sistematico |
| Annualized Return vs benchmark | Alpha generation | Si underperform sostenido — cuestionar si el proceso genera alpha |
| Max Drawdown portfolio | Riesgo extremo | Si drawdown severo, revisar correlaciones y concentracion |
| Information Ratio | Alpha por unidad de tracking error | Si negativo, el riesgo activo no genera retorno |

**Accion si metricas preocupan**: Revision estrategica completa. Considerar cambios estructurales al proceso.

**NOTA**: Los thresholds especificos de "alarma" dependen de nuestro propio historial. Comparar SIEMPRE contra nuestra baseline acumulada, no contra numeros fijos. El sistema es joven — las baselines evolucionan con cada trimestre de datos.

## Protocolo de Revision

### SEMANAL (cada lunes)
```bash
python3 tools/effectiveness_tracker.py
```
- Revisar win rate actual vs baseline historica
- Identificar posiciones con drawdown que merezcan revision de thesis
- Verificar pipeline health vs cash

### MENSUAL (primer dia del mes)
- Attribution analysis por sector/geografia
- Comparar vs benchmark (MSCI Europe, S&P 500)
- Revisar Tier A/B/C performance (funciona el tiering?)
- Actualizar portfolio/history.yaml con cierres

### TRIMESTRAL
- Evaluacion retrospectiva de tesis cerradas
- Cuantas tesis llegaron a FV?
- Cuantas tesis fallaron por razon que debimos prever?
- Ajustar framework si patrones de error
- **Recalibrar baselines** con datos acumulados

### ANUAL
- Sharpe ratio vs benchmark
- Attribution analysis completo
- El sistema genera alpha?
- Decision: continuar estrategia o pivotar?

## Registro de Errores (Obligatorio)

Para cada posicion cerrada con perdida o que no alcanzo FV, documentar en `portfolio/history.yaml`:

```yaml
closed_positions:
  - ticker: XXX
    entry_date: 2026-01-26
    exit_date: 2026-03-15
    entry_price: 50.00
    exit_price: 42.00
    pnl_pct: -16%
    thesis_fv: 70.00
    reached_fv: false
    error_type: timing | thesis_wrong | execution | external_shock
    error_description: "Descripcion detallada del error"
    lesson_learned: "Que deberiamos haber hecho diferente"
    system_improvement: "Cambio al sistema para evitar repetir"
```

## Benchmarks de Referencia

### Comparacion obligatoria vs:
1. **MSCI Europe (IEUR)** - benchmark geografico principal
2. **S&P 500 (SPY)** - benchmark global
3. **60/40 Portfolio** - benchmark de riesgo ajustado

### Calibracion temporal (no expectativas fijas):
- **Primeros anos**: El sistema esta en fase de aprendizaje. Underperformance puede ser normal
- **Con mas datos**: Las baselines se vuelven mas fiables. Divergencias son mas significativas
- **Largo plazo**: Un sistema disciplinado deberia generar alpha, pero no esta garantizado

## Alertas como Investigacion, No como Reglas

El sistema debe alertar cuando detecte patrones que merezcan investigacion:

1. **POSICION**: Drawdown significativo → revisar thesis. La magnitud que justifica revision depende del tipo de empresa y conviccion
2. **PORTFOLIO**: Drawdown amplio → revisar exposicion y correlaciones
3. **TESIS**: Progreso nulo tras periodo significativo → re-evaluar timeline y catalizadores
4. **PATRON**: Multiples posiciones correlacionadas en perdida → investigar factor comun (macro, sector, sesgo)

**Las alertas son DATOS que informan investigacion, no REGLAS que dictan accion.**

## Honestidad Epistemologica

### Lo que el sistema PUEDE hacer:
- Identificar empresas infravaloradas con margen de seguridad
- Diversificar para reducir riesgo idiosincratico
- Seguir un proceso disciplinado

### Lo que el sistema NO PUEDE garantizar:
- Que el mercado reconozca el valor (puede tardar anos)
- Que nuestro analisis sea correcto (always uncertain)
- Que no haya cisnes negros (siempre posible)

### Calibracion realista:
- No todas las tesis acertaran. La clave es que los aciertos compensen las perdidas
- El tiempo medio a FV depende del tipo de empresa y catalizadores — no hay "tiempo estandar"
- Algunas posiciones nunca llegaran a FV. Documentar por que y aprender

## Tool de Evaluacion

```bash
# Reporte completo
python3 tools/effectiveness_tracker.py

# Solo metricas resumen
python3 tools/effectiveness_tracker.py --summary

# Comparar vs benchmark
python3 tools/effectiveness_tracker.py --vs-benchmark
```

## Evolucion del Framework

Este framework debe evolucionar basado en datos reales. Cada trimestre:
1. Las baselines reflejan nuestra experiencia real?
2. El tiering A/B/C predice resultados?
3. Hay patrones de error sistematicos?
4. Que metricas son mas predictivas para NUESTRO proceso?

---

**Framework Version:** 2.0
**Ultima actualizacion:** 2026-02-18
