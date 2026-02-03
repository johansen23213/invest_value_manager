# Skill: Effectiveness Evaluation Framework v1.0

> Creado: 2026-02-03
> Propósito: Evaluar sistemáticamente la efectividad del sistema de inversión

## El Problema

Value investing tiene un problema fundamental: **no sabemos si nuestras predicciones son correctas hasta años después**. Esto crea riesgos:
- Confirmation bias (solo recordamos los aciertos)
- Survivorship bias (ignoramos errores que vendimos)
- Overconfidence (asumimos que entendemos el mercado)

## Solución: Sistema de Evaluación Multi-Horizonte

### 1. MÉTRICAS DE CORTO PLAZO (< 3 meses)

**No predicen éxito a largo plazo, pero detectan errores de timing:**

| Métrica | Target | Alarma |
|---------|--------|--------|
| Win Rate (30d) | >40% | <30% |
| Max Drawdown posición | <-15% | >-20% |
| Volatilidad vs benchmark | <1.2x | >1.5x |
| Cash drag | <15% | >20% |

**Acción si alarma**: Revisar timing de entradas, no necesariamente la tesis.

### 2. MÉTRICAS DE MEDIO PLAZO (3-12 meses)

**Validan la calidad del análisis:**

| Métrica | Target | Alarma |
|---------|--------|--------|
| Win Rate (12m) | >50% | <40% |
| Thesis On-Track Rate | >60% | <50% |
| Avg Return vs FV | >50% del MoS | <25% del MoS |
| Sharpe Ratio | >0.5 | <0 |

**Acción si alarma**: Revisar framework de análisis (business understanding, projections).

### 3. MÉTRICAS DE LARGO PLAZO (1-5 años)

**Validan la estrategia completa:**

| Métrica | Target | Alarma |
|---------|--------|--------|
| FV Hit Rate | >60% | <40% |
| Annualized Return | >MSCI Europe +3% | <MSCI Europe |
| Max Drawdown portfolio | <-25% | >-35% |
| Information Ratio | >0.3 | <0 |

**Acción si alarma**: Revisar estrategia completa, considerar cambios estructurales.

## Protocolo de Revisión

### SEMANAL (cada lunes)
```bash
python3 tools/effectiveness_tracker.py
```
- Revisar win rate actual
- Identificar posiciones >-10% (revisar tesis)
- Verificar cash drag

### MENSUAL (primer día del mes)
- Attribution analysis por sector/geografía
- Comparar vs MSCI Europe benchmark
- Revisar Tier A/B/C performance (¿funciona el tiering?)
- Actualizar portfolio/history.yaml con cierres

### TRIMESTRAL
- Evaluación retrospectiva de tesis cerradas
- ¿Cuántas tesis llegaron a FV?
- ¿Cuántas tesis fallaron por razón que debimos prever?
- Ajustar framework si patrones de error

### ANUAL
- Sharpe ratio vs benchmark
- Attribution analysis completo
- ¿El sistema genera alpha?
- Decisión: ¿continuar estrategia o pivotar?

## Registro de Errores (Obligatorio)

Para cada posición cerrada con pérdida o que no alcanzó FV, documentar en `portfolio/history.yaml`:

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
    error_description: "Descripción detallada del error"
    lesson_learned: "Qué deberíamos haber hecho diferente"
    system_improvement: "Cambio al sistema para evitar repetir"
```

## Benchmarks de Referencia

### Comparación obligatoria vs:
1. **MSCI Europe (IEUR)** - benchmark geográfico principal
2. **S&P 500 (SPY)** - benchmark global
3. **60/40 Portfolio** - benchmark de riesgo ajustado

### Performance esperada (value investing histórico):
- **Años 1-3**: Puede underperform significativamente
- **Años 3-5**: Debería empezar a converger
- **Años 5+**: Debería superar benchmark por 2-5% anual

## Alertas Automáticas

El sistema debe alertar cuando:

1. **POSICIÓN**: P&L < -15% (revisar tesis urgente)
2. **PORTFOLIO**: Drawdown < -20% (revisar exposición)
3. **TESIS**: >50% del expected holding period sin progreso hacia FV
4. **PATRÓN**: 3+ posiciones en mismo sector/geografía en pérdida

## Honestidad Epistemológica

### Lo que el sistema PUEDE hacer:
- Identificar empresas infravaloradas con margen de seguridad
- Diversificar para reducir riesgo idiosincrático
- Seguir un proceso disciplinado

### Lo que el sistema NO PUEDE garantizar:
- Que el mercado reconozca el valor (puede tardar años)
- Que nuestro análisis sea correcto (always uncertain)
- Que no haya cisnes negros (siempre posible)

### Probabilidades realistas:
- **Hit rate esperado**: 55-65% (no 100%)
- **Tiempo medio a FV**: 18-36 meses (no semanas)
- **Posiciones que nunca llegan a FV**: 20-30%

## Tool de Evaluación

```bash
# Reporte completo
python3 tools/effectiveness_tracker.py

# Solo métricas resumen
python3 tools/effectiveness_tracker.py --summary

# Comparar vs benchmark
python3 tools/effectiveness_tracker.py --vs-benchmark
```

## Integración con CLAUDE.md

Añadir a checklist de inicio de sesión:
- [ ] Ejecutar effectiveness_tracker.py
- [ ] Revisar posiciones con P&L < -10%
- [ ] Verificar alertas activas

## Evolución del Framework

Este framework debe evolucionar basado en datos reales. Cada trimestre:
1. ¿Las métricas de alarma son apropiadas?
2. ¿El tiering A/B/C predice resultados?
3. ¿Hay patrones de error sistemáticos?
