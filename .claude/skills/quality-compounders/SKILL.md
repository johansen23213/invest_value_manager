---
name: quality-compounders
description: "Framework v4.0 - Guia para identificar e invertir en Quality Compounders (Tier A, QS >=75)"
user-invocable: false
disable-model-invocation: false
---

# Quality Compounders Skill v4.0

## Que es un Quality Compounder?

Un negocio excepcional que:
1. Genera ROIC muy superior al coste de capital
2. Puede reinvertir a altas tasas de retorno
3. Tiene ventajas competitivas durables (wide moat)
4. Crece de forma sostenible
5. **Compound value con el tiempo** sin necesidad de re-rating

> "The ideal business is one that earns very high returns on capital and that keeps using lots of capital at those high returns." - Warren Buffett

---

## Criterios para Quality Compounder (QS >=75)

### Financial Quality (>=32/40)
- ROIC > WACC + 15pp (spread >=15pp)
- FCF Margin >15%
- Net Debt/EBITDA <2x (preferible net cash)
- FCF positivo 5/5 anos

### Growth Quality (>=18/25)
- Revenue CAGR >10% (sostenible)
- EPS CAGR >10%
- Gross Margin estable o expandiendo

### Moat Evidence (>=20/25)
- Gross Margin muy superior al sector (>10pp)
- Posicion de mercado dominante (#1-2)
- ROIC >WACC por 10+ anos

### Capital Allocation (>=5/10)
- Track record de dividendos/buybacks
- Idealmente insider ownership >2%

---

## Metodos de Valoracion para Compounders

### Metodo Primario: Owner Earnings Yield

```
Owner Earnings (OE) = FCF - Maintenance Capex
Maintenance Capex ~ Depreciation x 1.1

Owner Earnings Yield = OE / Market Cap
```

**Interpretacion (contexto, no regla):**
- OEY alto = mas valor por euro invertido
- OEY bajo = mercado paga premium por growth futuro
- Comparar OEY + Expected Growth vs coste de capital (WACC)
- Mayor spread entre (OEY + Growth) y WACC = mas atractivo

**Consultar precedentes en `decisions_log.yaml` para ver que niveles de OEY aceptamos historicamente y por que.**

### Metodo Secundario: Reverse DCF

```
Pregunta: Que crecimiento implica el precio actual?

Proceso:
1. Fijar WACC (derivar, no default)
2. Fijar terminal growth (2-3%)
3. Usar DCF tool con varios growth rates
4. Encontrar growth rate que da FV = precio actual

Si Implied Growth > Mi estimacion -> CARO
Si Implied Growth < Mi estimacion -> BARATO
```

### Metodo Terciario: P/E Growth Adjusted (PEG)

```
PEG Ratio = P/E / Growth Rate

Interpretacion contextual:
- PEG bajo sugiere valor relativo al crecimiento
- Pero depende de calidad del crecimiento (organico vs adquisiciones)
- ROIC alto justifica PEG mas alto (reinversion a altas tasas)
```

---

## Sizing y MoS para Compounders

### Framework v4.0: Razonamiento, No Reglas

**NO hay MoS fijo ni sizing fijo para compounders.**

El MoS y sizing se determinan por:
1. Conviccion en la tesis especifica
2. Riesgo de esta empresa en particular
3. Contexto del portfolio (concentracion, correlacion)
4. Precedentes de decisiones similares
5. Contexto macro

### Por que Compounders toleran MoS mas bajo?

Razonamiento (no regla):
1. **Predictibilidad**: FCF mas estable, menos incertidumbre
2. **Moat protege**: Errores de valoracion se corrigen con el tiempo
3. **Compounding**: Incluso a fair value, el crecimiento genera retorno
4. **Escasez**: Raramente cotizan con grandes descuentos

### Precedentes Observados (NO limites)

Consultar `learning/decisions_log.yaml` para ver:
- Que sizing usamos para Tier A (patrones observados: 3-5% inicial)
- Que MoS aceptamos y por que
- Que contexto habia cuando tomamos esas decisiones

**Si el contexto actual es diferente, documentar por que el sizing/MoS seria diferente.**

---

## Cuando Comprar Compounders

### Oportunidades tipicas (no reglas de compra):

**Correccion de Mercado:**
- Correccion general arrastra compounders
- Tipicamente las mejores oportunidades de entry

**Problema Temporal Especifico:**
- Earnings miss por tema one-time
- Investigacion regulatoria sin fundamento
- Guidance conservador malinterpretado
- Ejemplo real: NVO -17% por guidance shock -> compramos con MoS 38%

**Compra Escalonada:**
- Si MoS actual es razonable pero no excepcional
- Comprar posicion inicial, ADD si baja mas
- Documentar razonamiento para cada tramo

---

## Cuando NO Comprar Compounders

1. **Near all-time highs sin catalizador**: El mercado ya reconoce la calidad
2. **Multiplo historicamente alto**: Razonar si el premium es justificado
3. **Cambio estructural en moat**: AI amenaza negocio core, no es temporal
4. **Crecimiento desacelerando**: Runway de reinversion agotado

---

## Kill Conditions para Compounders

Vender si:
1. **Moat impaired estructuralmente** (no temporalmente)
2. **ROIC cae a <WACC por 3+ anos**
3. **Management destruye capital** (M&A sobrepagado, ego)
4. **Quality Score cae a <75** (reclasificar, re-evaluar)

NO vender por:
- Volatilidad de mercado
- Earnings miss aislado
- Analyst downgrade
- Compresion multiplo por sentimiento

---

## Pipeline de Quality Compounders

### Mantener lista actualizada

La lista esta en `state/system.yaml` seccion `watchlist.quality_compounders`.
Actualizar trimestralmente:
1. Recalcular Quality Score
2. Verificar si alguno alcanzo entry razonable
3. Anadir nuevos candidatos via screening sistematico

### Anti-Popularity-Bias

- No depender solo de nombres famosos (GOOGL, META, etc.)
- Usar `dynamic_screener.py` con filtros de calidad para encontrar compounders ocultos
- Mid-caps con cobertura baja pueden ser compounders no descubiertos
- Mercados no-US tienen compounders a valuaciones mas atractivas

---

## Checklist Quality Compounder

Antes de clasificar como Compounder, verificar:

```
[ ] Quality Score >=75 calculado con tool
[ ] ROIC > WACC consistentemente 10+ anos
[ ] FCF positivo y creciente
[ ] Moat identificable y cuantificable
[ ] Crecimiento sostenible (runway largo)
[ ] Management con track record
[ ] No hay disrupcion estructural inminente
```

Si todos OK -> Clasificar como Quality Compounder
Si alguno falla -> Clasificar como Value (Tier B) o Special (Tier C)

---

**Framework Version:** 4.0
**Ultima actualizacion:** 2026-02-06
