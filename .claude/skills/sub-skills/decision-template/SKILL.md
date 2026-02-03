---
name: decision-template
description: Investment committee decision document format - expanded checklist with all gates from new framework
user-invocable: false
disable-model-invocation: false
---

# Decision Template Sub-Skill (v2.0)

## Formato Decisión Investment Committee

---

### Veredicto: BUY / WATCHLIST / REJECT

---

### Checklist Completo (todos los gates)

#### Gate 1: Entendimiento del Negocio
- [ ] Business Analysis Framework completado
- [ ] Puedo explicar el negocio en 2 minutos: [SI/NO]
- [ ] Sé por qué está barata: [razón]
- [ ] Tengo contra-tesis documentada: [1 línea]
- [ ] Value trap checklist: [X]/10 factores SI
- [ ] Ventaja informacional identificada: [cuál o "ninguna clara"]

#### Gate 2: Proyección Fundamentada
- [ ] Projection Framework completado
- [ ] Revenue growth derivado de TAM/share/pricing: [X]%
- [ ] WACC calculado (no default): [X]%
- [ ] Terminal growth justificado: [X]%
- [ ] Escenarios Bear/Base/Bull documentados

#### Gate 3: Valoración Multi-Método
- [ ] Método 1: [nombre] → €[FV]
- [ ] Método 2: [nombre] → €[FV]
- [ ] Métodos apropiados para tipo de empresa: [SI/NO]
- [ ] Divergencia entre métodos: [X]% (si >30%, explicación: ___)

#### Gate 4: Margen de Seguridad
- [ ] Tier asignado: [A/B/C]
- [ ] MoS mínimo requerido: [X]%
- [ ] MoS actual vs Expected Value: [X]%
- [ ] MoS actual vs Bear Case: [X]%
- [ ] Quality Score (si Tier A): [X]/10

#### Gate 5: Contexto Macro
- [ ] World view revisado (fecha: ___)
- [ ] Ciclo económico: [early/mid/late]
- [ ] Fit empresa-ciclo: [favorable/neutral/adverso]
- [ ] Megatendencias: [ayudan/neutras/perjudican]

#### Gate 6: Portfolio Fit
- [ ] Precio verificado via price_checker.py: €[X] (fecha: ___)
- [ ] Sizing propuesto: [X]% (€[Y])
- [ ] Position post-compra: [X]% (limit 7%): [OK/VIOLA]
- [ ] Sector post-compra: [sector] = [X]% (limit 25%): [OK/VIOLA]
- [ ] Geografía post-compra: [geo] = [X]% (limit 35%): [OK/VIOLA]
- [ ] Cash post-compra: [X]% (min 5%): [OK/VIOLA]
- [ ] Correlación con posiciones existentes: [alta/media/baja]

#### Gate 7: Autocrítica
- [ ] Asunciones no validadas listadas: [SI/NO]
- [ ] Sesgos posibles reconocidos: [SI/NO]
- [ ] Kill conditions definidas: [SI/NO]
- [ ] Qué me haría cambiar de opinión: [SI/NO]

---

### Resumen de Valoración
| Escenario | Fair Value | Prob | MoS |
|-----------|-----------|------|-----|
| Bear | €___ | 25% | ___% |
| Base | €___ | 50% | ___% |
| Bull | €___ | 25% | ___% |
| **Expected** | **€___** | 100% | **___%** |

Precio actual: €___

---

### Si BUY

**Recomendación clara al humano:**
```
COMPRAR €[X] de [TICKER] ([Y]% del portfolio)

Razón: [1-2 líneas - por qué es oportunidad]
Fair Value: €[base] (MoS [X]%)
Riesgo principal: [1 línea]
Kill condition: [qué me haría vender]

¿Confirmas para ejecutar en eToro?
```

**Post-compra:**
- Mover thesis de research/ a active/
- Actualizar portfolio/current.yaml
- Configurar price alert en €[target base]
- Next review: [fecha o earnings]

---

### Si WATCHLIST

**Condiciones de entrada:**
- Precio objetivo: €[X] (MoS sería [Y]%)
- O condición: [qué debe pasar]

**Configurar:**
- Standing order en state/system.yaml
- Price alert en €[X]
- Thesis queda en thesis/watchlist/[TICKER]/

**Revisitar:** [fecha o trigger]

---

### Si REJECT

**Razón principal:** [1-2 líneas]

**Clasificación:**
- [ ] Value trap (>3 factores)
- [ ] MoS insuficiente
- [ ] No entiendo el negocio suficientemente
- [ ] Contexto macro desfavorable
- [ ] Mejor oportunidad disponible
- [ ] Thesis no compelling
- [ ] Otro: ___

**¿Revisitar en futuro?**
- [ ] No - problema estructural
- [ ] Sí, si precio cae a €[X]
- [ ] Sí, si [condición]
- [ ] Sí, en [fecha] para re-evaluar

**Archivar:** thesis/archive/[TICKER]/

---

### Firma
```
Fecha: [YYYY-MM-DD]
Analyst: fundamental-analyst
Committee: investment-committee
Decisión: [BUY/WATCHLIST/REJECT]
```
