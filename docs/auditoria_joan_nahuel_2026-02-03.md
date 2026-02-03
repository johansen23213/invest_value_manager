# Auditoría del Sistema de Inversión
## Preguntas de Joan y Nahuel - 2026-02-03

---

# 📊 AGENTE DE RATIOS / SCREENER

---

## Pregunta 1: P/E bajo con beneficios cayendo

> **Una empresa cumple P/E < 15, pero sus beneficios han caído 40% en los últimos 3 años. ¿La mantienes o la descartas? ¿Por qué?**

### Respuesta: DESCARTAR en la mayoría de casos.

Un P/E bajo con earnings en declive es una **value trap clásica**. El P/E de mañana será mayor porque los earnings seguirán cayendo.

**Excepciones donde podría mantener:**
- Declive es cíclico (no estructural) Y estamos cerca del fondo
- Hay un catalizador concreto de reversión (nuevo management, spin-off, reestructuración)
- El negocio core sigue generando FCF positivo

**Lo que hago:** Uso el **value trap checklist** (skill business-analysis-framework):
- ¿Revenue cayendo? ✓ → +1 factor
- ¿Márgenes comprimiendo? → verificar
- ¿Industria en declive estructural? → verificar

**Si >3 factores del checklist = REJECT automático.**

---

## Pregunta 2: P/B bajo pero activos inflados

> **El P/B es 0,9 pero el 60% del activo son intangibles y goodwill. ¿Cómo ajustas el valor contable real?**

### Respuesta: Ajuste del valor contable tangible

```
Book Value reportado:     €100
- Goodwill:               -€40
- Intangibles dudosos:    -€20
= Tangible Book Value:    €40

P/TBV real = Precio / €40 = 2.5x (no 0.9x)
```

**Regla práctica:**
| Tipo de activo | Descuento |
|----------------|-----------|
| Goodwill de adquisiciones recientes (< 3 años) | 50% |
| Goodwill de adquisiciones antiguas | 80-100% |
| Intangibles (marcas, patentes) | Caso por caso |
| Software capitalizado | 100% descuento |

**Graham era claro:** Solo contaba activos tangibles netos (NCAV = Current Assets - Total Liabilities).

---

## Pregunta 3: FCF negativo con ratios buenos

> **Cumple todos los ratios, pero tiene flujo de caja libre negativo 4 de los últimos 5 años. ¿Debe pasar el filtro?**

### Respuesta: NO PASA.

El FCF es la métrica más difícil de manipular.

**Excepciones muy limitadas:**
- Empresa en fase de inversión masiva (capex growth) con runway claro
- El FCF negativo es por working capital timing (verificable en balance)
- Tiene caja/deuda para financiar el gap

**Lo que verifico:**
```python
# FCF = Operating Cash Flow - CapEx
# Si FCF < 0 pero OCF > 0 → problema es CapEx (puede ser inversión)
# Si OCF < 0 → earnings son humo contable → REJECT
```

**REGLA DURA del sistema:** DCF requiere FCF positivo histórico. Sin FCF → uso EV/EBIT o P/B vs ROE, nunca DCF.

---

## Pregunta 4: Riesgo de liquidez futura

> **Tiene deuda/patrimonio bajo, pero vencimientos masivos en los próximos 2 años. ¿Cómo incorporas riesgo de liquidez futura?**

### Respuesta: El ratio D/E es insuficiente.

**Verifico:**
1. **Debt maturity schedule** (en notas de los estados financieros)
2. **Interest coverage ratio** con tipos actuales Y +200bp
3. **Cash + undrawn facilities** vs vencimientos próximos 24m
4. **Capacidad de refinanciar**: ¿investment grade? ¿mercado abierto para su sector?

**Ajuste práctico:**
```
Si vencimientos 24m > (Cash + 50% FCF anual):
   → Riesgo de refinanciación ALTO
   → Requiere descuento 15-25% en FV
   → O descartar si no hay líneas de crédito confirmadas
```

**Debilidad del sistema:** No tenemos acceso automático a debt maturity schedules. Depende de research manual en 10-K/20-F.

---

## Pregunta 5: Empresas cíclicas en pico

> **¿Cómo tratas empresas cíclicas donde los ratios parecen baratos solo en pico de ciclo?**

### Respuesta: EV/EBIT mid-cycle

Las cíclicas tienen P/E BAJO cuando earnings están en MÁXIMOS (justo antes de caer).

**Solución:**
```
1. Calcular EBIT promedio últimos 7-10 años (ciclo completo)
2. Usar ese EBIT normalizado para valorar
3. Comparar con EV/EBIT actual

Si EV/EBIT mid-cycle > 12x → probablemente cara aunque P/E actual sea 6x
```

**Señales de pico de ciclo:**
- Márgenes históricos máximos
- Capex de expansión masivo en el sector
- Analistas proyectando "nuevo paradigma"
- IPOs en el sector

**El skill valuation-methods especifica:** Para cíclicas, SIEMPRE usar EV/EBIT mid-cycle como método primario, nunca P/E actual.

---

# 🏰 AGENTE DE MOAT / NEGOCIO

---

## Pregunta 6: Moat en industria disruptiva

> **Una empresa domina su mercado hoy, pero está en una industria en disrupción tecnológica. ¿Cómo evalúas la durabilidad del moat?**

### Respuesta: Framework de evaluación

| Factor | Señal de moat durable | Señal de moat erosionando |
|--------|----------------------|---------------------------|
| Switching costs | Integración profunda en workflow del cliente | Clientes pueden cambiar en <6 meses |
| Network effects | Crecen con la base de usuarios | Sustitutos capturan nichos |
| Brand | Premium pricing mantenido | Descuentos para retener share |
| Scale | Costos unitarios bajando | Newcomers con estructura más ligera |

**Test práctico:**
> "¿Si un competidor bien financiado entra con precio 30% menor, qué % de clientes se van en 3 años?"

- Si <10%: moat durable
- Si 10-30%: moat narrow
- Si >30%: no hay moat real

**Ejemplo histórico:** Kodak dominaba, pero el moat dependía de activos físicos (distribución de película) que la digitalización hizo irrelevantes.

---

## Pregunta 7: Competencia de precios

> **Tiene márgenes altos pero competidores nuevos están entrando agresivamente con precios bajos. ¿Eso invalida el moat?**

### Respuesta: Depende de la fuente del margen

| Fuente del margen | Efecto de price competition |
|-------------------|----------------------------|
| Eficiencia operativa | Resistente (pueden bajar precio y mantener margen) |
| Brand premium | Parcialmente resistente (depende de elasticidad) |
| Switching costs | Muy resistente (clientes no cambian por precio) |
| **Falta de competencia** | **NO resistente → moat falso** |

**Test:** ¿El margen viene de PODER o de AUSENCIA de competidores?
- Si es ausencia → cuando llegue competencia, márgenes colapsan
- Esto es lo que pasó con telecos, retail tradicional, bancos vs fintechs

---

## Pregunta 8: Riesgo regulatorio

> **El moat depende de regulación favorable. ¿Qué pasa si cambia el marco legal?**

### Respuesta: Descuento estructural obligatorio

**Cuantificación:**
```
Escenario Base: Regulación se mantiene → FV €100
Escenario Adverso: Regulación cambia → FV €60
Probabilidad de cambio: 25% (estimar conservador)

FV ajustado = 0.75 × €100 + 0.25 × €60 = €90

O usar descuento directo: -15% al FV por riesgo regulatorio
```

**Ejemplos por sector:**
| Sector | Nivel de riesgo regulatorio |
|--------|----------------------------|
| Utilities con tarifas reguladas | Bajo (gobiernos necesitan servicio) |
| Pharma con patentes | Medio (genericación predecible) |
| Gaming/gambling | ALTO |
| Tobacco | Medio-alto (regulación siempre aumentando) |

---

## Pregunta 9: Ventaja real vs moda

> **¿Cómo diferencias una ventaja competitiva real de una moda temporal?**

### Respuesta: Test de los 10 años

> "¿Esta ventaja existía hace 10 años? ¿Existirá en 10 años?"

| Ventaja | Hace 10 años | En 10 años | Veredicto |
|---------|--------------|------------|-----------|
| Coca-Cola brand | ✅ | ✅ | Moat real |
| Netflix first-mover | ❌ | ❓ | Moat cuestionable |
| Uber network effects | ❌ | ❓ | No demostrado |
| TSMC tech lead | ✅ (2nm) | ❓ | Moat pero requiere reinversión continua |

**Señales de moda temporal:**
- Ventaja basada en "ser primero" sin lock-in
- Ventaja de crecimiento (que desaparece cuando el mercado madura)
- Ventaja de narrativa ("disrupción") sin economics probados

---

## Pregunta 10: Concentración de clientes

> **Si una empresa depende de 2 grandes clientes que suponen el 55% de ingresos: ¿Es un moat o un riesgo estructural?**

### Respuesta: RIESGO ESTRUCTURAL, no moat.

La concentración de clientes significa:
- Poder de negociación está en el cliente, no en la empresa
- Pérdida de 1 cliente = crisis existencial
- Los márgenes son "prestados", no "ganados"

**Cuantificación:**
```
Probabilidad de perder cliente grande en 5 años: 15-25%
Impacto si pierde: -55% revenue, probablemente pérdidas
Descuento a FV: mínimo 20%, hasta 35%
```

**Excepción:** Si la relación es simbiótica (ej: proveedor único de componente crítico), el riesgo es menor. Pero aún así es concentración, no moat.

---

# ⚠️ AGENTE DE RIESGOS

---

## Pregunta 11: Litigios masivos

> **La empresa parece barata pero tiene litigios abiertos equivalentes al 40% de su market cap. ¿Cómo cuantificas ese riesgo?**

### Respuesta: Framework de cuantificación

```
Paso 1: Clasificar el litigio
- Contractual/comercial: típicamente 10-30% del claim se paga
- Regulatorio/multa: 50-100% si hay precedente
- Class action securities: variable, depende de mérito
- Criminal/DOJ: muy serio, descuento máximo

Paso 2: Estimar probabilidad y severidad
- Leer filings legales (10-K risk factors, 8-K)
- Buscar casos similares resueltos
- Consultar análisis de abogados especializados (news)

Paso 3: Calcular expected loss
Expected Loss = P(desfavorable) × Monto estimado

Ejemplo: Claim €400M, P(perder)=40%, pago si pierde=70%
Expected Loss = 0.4 × 0.7 × €400M = €112M

Paso 4: Ajustar FV
FV ajustado = FV base - Expected Loss - Prima de incertidumbre (10-20%)
```

---

## Pregunta 12: Tipos de interés al alza

> **Tiene deuda barata hoy, pero tipos de interés al alza. ¿Cómo ajustas proyecciones?**

### Respuesta: Proyección de refinanciación

```
1. Identificar estructura de deuda:
   - % fija vs variable
   - Vencimientos y tasas actuales

2. Proyectar costo de refinanciación:
   - Deuda que vence en años 1-3: asumir tipos +150-200bp
   - Spread de crédito actual de la empresa

3. Calcular nuevo interest expense:
   Año 1: €10M (actual)
   Año 3: €10M × 1.3 = €13M (si refinancia con +30% tasa)

4. Impacto en FCF:
   FCF proyectado = FCF actual - Δ interest × (1 - tax rate)
```

**WACC también se ajusta:**
```
Si Rf sube 100bp → WACC sube ~40bp (ponderado por D/V)
Si WACC sube de 9% a 9.4% → DCF FV baja ~8-10%
```

---

## Pregunta 13: Manipulación contable

> **¿Cómo detectas manipulación contable sin acceso a auditorías internas?**

### Respuesta: Red flags (Beneish M-Score simplificado)

| Señal | Qué indica | Cómo verifico |
|-------|-----------|---------------|
| Revenue crece >> Cash from operations | Revenue inflado o reconocido prematuramente | Comparar línea 1 P&L vs OCF |
| Receivables crecen >> Revenue | Channel stuffing, ventas ficticias | Days Sales Outstanding aumentando |
| Inventory crece >> COGS | Obsolescencia oculta, capitalización de costos | Inventory turnover cayendo |
| Gross margin volátil YoY | Manipulación de COGS | Comparar con peers |
| Cambios de política contable | Ocultar deterioro | Notas de auditor |
| Auditor renuncia o cambia | MAJOR RED FLAG | 8-K filing |
| CFO/Controller renuncia | MAJOR RED FLAG | Filings |
| Stock-based comp excluido de "adjusted" | Dilución oculta | Reconciliación GAAP vs Non-GAAP |

**Test rápido:**
```
Si: Net Income >> Operating Cash Flow (consistente 3+ años)
Entonces: Earnings probablemente de baja calidad
Acción: Usar solo FCF para valorar, o descartar
```

---

## Pregunta 14: Value traps

> **¿Qué señales tempranas usas para detectar "value traps"?**

### Respuesta: Checklist de 10 factores

1. ✅/❌ Revenue declinando >2 años consecutivos
2. ✅/❌ Industria en declive estructural (no cíclico)
3. ✅/❌ Márgenes comprimiendo sin plan de reversión
4. ✅/❌ Management comprando tiempo con contabilidad
5. ✅/❌ Capex de mantenimiento > Depreciación (activos deteriorándose)
6. ✅/❌ Dividendo > FCF (pagando con deuda)
7. ✅/❌ Competidores ganando share consistentemente
8. ✅/❌ Clientes concentrados o con poder de negociación
9. ✅/❌ Tecnología sustituta emergiendo
10. ✅/❌ Barato por razón conocida que el mercado entiende

**Si >3 factores = probable value trap → REJECT o Tier C máximo**

---

## Pregunta 15: Insider selling

> **Si los insiders están vendiendo masivamente acciones: ¿Cómo influye en la decisión?**

### Respuesta: Contexto importa

| Patrón de venta | Interpretación |
|-----------------|----------------|
| CEO vende 50% de su posición | 🚨 MAJOR WARNING |
| Venta programada (10b5-1) | Neutral (planificado) |
| Múltiples insiders vendiendo simultáneamente | 🚨 WARNING |
| Venta post-vesting de options | Menos preocupante (diversificación normal) |
| CFO vendiendo | Más preocupante que otros C-suite |

**Regla práctica:**
```
Si insider selling > 3x historical average en últimos 6 meses:
   → Investigar razón
   → Si no hay razón pública convincente → Descuento 10% a FV o PASS
```

**Lo que NO hago:** Ignorar insider selling porque "la empresa está barata".

---

# 📈 AGENTE DE VALOR INTRÍNSECO

---

## Pregunta 16: Normalización de earnings

> **Si el valor intrínseco depende de beneficios actuales inflados por ciclo económico: ¿Cómo normalizas earnings?**

### Respuesta: EBIT promedio del ciclo

```
1. Identificar el ciclo (típicamente 5-10 años para industriales)
2. Calcular EBIT promedio del ciclo completo
3. Aplicar tasa impositiva normalizada
4. Usar ese "normalized earnings" para valorar

Ejemplo:
Año      EBIT
2019     €80M (pico)
2020     €20M (valle - COVID)
2021     €60M
2022     €90M (pico)
2023     €70M
2024     €50M
---
Promedio: €61.7M (no €90M del pico)
```

---

## Pregunta 17: Período de normalización

> **¿Usas promedio de 5, 7 o 10 años? ¿Por qué?**

### Respuesta: Depende del tipo de empresa

| Duración | Cuándo usar |
|----------|-------------|
| **5 años** | Empresas estables, no cíclicas (utilities, consumer staples) |
| **7 años** | Default para la mayoría |
| **10 años** | Muy cíclicas (commodities, auto, construcción, bancos) |
| **3 años** | SOLO si hay cambio estructural reciente (spin-off, nueva línea de negocio) |

**Graham usaba 10 años.** Yo uso 7 como default porque los ciclos económicos modernos son más cortos, pero ajusto según industria.

---

## Pregunta 18: Eventos extraordinarios

> **¿Cómo ajustas cuando hay un evento extraordinario (venta de división, multa, pandemia)?**

### Respuesta: Excluir items genuinamente no recurrentes, pero ser CONSERVADOR

**EXCLUIR (no recurrente real):**
- Venta de división (one-time gain)
- Multa/settlement legal específico
- Restructuring charges (si realmente one-time)
- COVID impacto 2020

**NO EXCLUIR (recurrente disfrazado):**
- "Restructuring" que aparece cada año
- Write-offs de goodwill (señala mala gestión de M&A)
- Stock-based compensation (es costo real)
- Litigation accruals (si la empresa tiene historial)

**Test:** ¿Ha tenido este "item extraordinario" en 3 de los últimos 5 años? Si sí → es ordinario.

---

## Pregunta 19: Métodos divergentes

> **Si diferentes métodos dan valores muy distintos: ¿Cuál priorizas y por qué?**

### Respuesta: Depende del tipo de empresa

| Tipo | Método primario | Método secundario | Por qué |
|------|-----------------|-------------------|---------|
| Estable, FCF+ | DCF | EV/EBIT | FCF es el fundamento |
| Cíclica | EV/EBIT mid-cycle | P/B vs ROE | Earnings normalizados |
| Financiera | P/B vs ROE | DDM | Book value es el activo |
| REIT | NAV + DDM | FFO yield | Activos reales + dividend |
| Asset-heavy | Sum-of-parts / NAV | - | Partes > todo |
| Growth | No aplico value investing | - | Fuera de mi círculo |

**Si divergen >30%:** Investigar por qué. Generalmente:
- DCF muy alto = growth assumptions agresivas
- Comparables muy bajo = mercado ve riesgo que no capturo
- La verdad suele estar en el método más conservador

---

## Pregunta 20: Margen de seguridad en volatilidad

> **¿Qué margen de seguridad mínimo consideras aceptable en entornos volátiles?**

### Respuesta: Framework por tiers

| Tier | MoS mínimo | Cuándo aplica |
|------|------------|---------------|
| **A** (alta convicción) | 25% | Wide moat, business entendido, balance sólido |
| **B** (convicción media) | 30% | Narrow moat o alguna incertidumbre |
| **C** (especulativo) | 40% | Turnaround, litigio, industria en transición |

**En entorno volátil (VIX >25, crisis):**
- Añadir +10pp a cada tier
- Tier A: 35%, Tier B: 40%, Tier C: 50%

**Graham recomendaba:** Mínimo 33% ("comprar a 66 centavos el dólar").

---

# 🧠 AGENTE DECISOR FINAL

---

## Pregunta 21: Calidad vs Descuento

> **Empresa A: margen de seguridad 40%, negocio mediocre. Empresa B: margen 20%, negocio excelente. ¿Cuál eliges según Graham?**

### Respuesta: Graham elegiría A. Buffett elegiría B.

**Mi sistema (híbrido):**
```
Si MoS de A > 1.5× MoS de B Y A no es value trap:
   → Elegir A (el descuento compensa la calidad)

Si B tiene moat demostrado (ROIC > WACC por 10+ años):
   → Elegir B (el moat justifica menor MoS)

En la práctica:
   A con 40% MoS: potencial +67% si llega a FV
   B con 20% MoS: potencial +25% si llega a FV

   Pero B probablemente supera su FV con el tiempo (moat crea valor)
   A probablemente nunca llega a FV (mediocre sigue siendo mediocre)
```

**Mi sesgo:** Prefiero B si el moat es genuino. El MoS de 40% en negocio mediocre es engañoso porque el FV puede seguir bajando.

---

## Pregunta 22: Sector en declive estructural

> **Todas las métricas son buenas pero el sector entero está en declive estructural. ¿Inviertes o no?**

### Respuesta: GENERALMENTE NO.

Un sector en declive estructural significa:
- Los earnings actuales son MÁXIMOS, no normalizados
- El FV de mañana será menor que el de hoy
- El MoS aparente es ilusión

**Excepciones donde SÍ podría:**
- La empresa es consolidadora (comprando competidores que quiebran)
- Genera caja para pivotar a otro negocio
- El declive es LENTO (>15 años) y hay yield alto mientras tanto
- P/NCAV < 0.67 (activos líquidos valen más que precio)

**Ejemplo:** Tobacco es declive estructural, pero lento. Imperial Brands genera caja suficiente para buybacks mientras declina. Pero no añadiría más exposure a un sector que sé que muere.

---

## Pregunta 23: Riesgo vs Estabilidad

> **¿Prefieres una empresa muy barata con riesgo alto o una moderadamente barata muy estable?**

### Respuesta: Prefiero moderadamente barata + estable.

**Razonamiento matemático:**
```
Opción A: 50% upside, 30% probabilidad de -50%
   EV = 0.7 × 50% + 0.3 × (-50%) = 35% - 15% = +20%

Opción B: 25% upside, 5% probabilidad de -20%
   EV = 0.95 × 25% + 0.05 × (-20%) = 23.75% - 1% = +22.75%

B tiene mejor EV Y menor varianza
```

**El error de muchos value investors:** Persiguen el upside nominal sin ponderar el downside.

**Mi regla:** El downside (pérdida permanente de capital) pesa más que el upside (ganancia potencial). Un -50% requiere +100% para recuperar.

---

## Pregunta 24: Criterio de selección final

> **Si solo puedes elegir 3 empresas del screener: ¿Qué criterio pesa más que los ratios?**

### Respuesta: En orden de importancia

1. **¿Entiendo el negocio?** Si no puedo explicar cómo gana dinero en 2 minutos → PASS
2. **¿Por qué está barata?** Si no sé la razón → probablemente value trap
3. **¿Tiene moat verificable?** ROIC > WACC por 10+ años
4. **¿Balance sólido?** D/E <1, interest coverage >5x
5. **¿Management alineado?** Insider ownership, skin in the game

**Los ratios (P/E, P/B, yield) solo sirven para FILTRAR, no para DECIDIR.**

---

## Pregunta 25: Cuándo NO invertir

> **¿Cuándo decides NO invertir aunque todo parezca atractivo?**

### Respuesta: "Kill conditions" universales

1. **No entiendo el negocio** (fuera de mi círculo de competencia)
2. **No puedo explicar por qué está barata** (el mercado sabe algo)
3. **Depende de un evento binario** (aprobación regulatoria, juicio)
4. **Management con historial de destruir valor** (M&A malo, dilución)
5. **Demasiado "story"** (si necesito creer una narrativa compleja → PASS)
6. **Insider selling masivo** sin explicación
7. **El único bull case es "está barata"** (eso no es un case)
8. **Mi sistema no puede modelarlo** (biotech pre-revenue, crypto, SPACs)

---

# 🔍 PREGUNTAS TRANSVERSALES (MUY GRAHAM)

---

## Pregunta 26: Precio bajo vs Valor bajo

> **¿Cómo distingues entre "precio bajo" y "valor bajo"?**

### Respuesta: Test de fundamentales

**Precio bajo:** Market cap < histórico, P/E < sector

**Valor bajo:** Los fundamentales justifican el precio bajo

```
Si price/book cayó 50% pero earnings también cayeron 50%:
   → No es barato, el mercado refleja la realidad

Si price cayó 50% pero earnings solo cayeron 10%:
   → Probablemente barato (oportunidad)

Si price cayó 50% pero earnings SUBIERON:
   → Definitivamente barato (verificar por qué)
```

---

## Pregunta 27: Métricas manipulables

> **¿Qué métricas son más manipulables por contabilidad creativa?**

### Respuesta: Ranking de manipulabilidad

| Ranking | Métrica | Nivel |
|---------|---------|-------|
| 1 | EPS ajustado | 🔴 Muy fácil (empresa define qué excluye) |
| 2 | EBITDA | 🔴 Fácil (ignora capex real, depreciation abuse) |
| 3 | Revenue | 🟡 Medio (timing recognition, channel stuffing) |
| 4 | Net Income GAAP | 🟡 Medio (provisions, write-downs timing) |
| 5 | Operating Cash Flow | 🟢 Difícil (pero posible via working capital) |
| 6 | Free Cash Flow | 🟢 Muy difícil (requiere manipular OCF Y CapEx) |
| 7 | Dividends paid | 🟢 Imposible (efectivo real sale de la empresa) |

**Por eso el sistema prioriza FCF sobre earnings reportados.**

---

## Pregunta 28: Sesgo de confirmación

> **¿Cómo evitas sesgo de confirmación en los agentes?**

### Respuesta: Mecanismos estructurales

1. **Investment Committee tiene 7 gates obligatorios** - no puede aprobar sin verificar todos
2. **Value trap checklist es NEGATIVO** - busca razones para NO comprar
3. **Critical thinking skill** requiere "devil's advocate" explícito
4. **Mínimo 2 métodos de valoración** - si divergen, obliga a investigar

**Debilidad reconocida:** Los agentes son ejecutados por mí (el orchestrator), y si yo tengo sesgo, los agentes lo heredan. El framework intenta mitigarlo pero no lo elimina.

---

## Pregunta 29: Datos contradictorios

> **¿Cómo reaccionan los agentes ante datos contradictorios?**

### Respuesta: Protocolo de resolución

```
Si datos contradictorios:
1. Documentar explícitamente la contradicción
2. Buscar fuente adicional (tercera opinión)
3. Si persiste → asumir el dato más CONSERVADOR
4. Añadir descuento de incertidumbre al FV (10-15%)
5. Subir MoS requerido al tier siguiente

Ejemplo:
- Yahoo Finance dice P/E 8x
- Reuters dice P/E 12x
- Asumo 12x (más conservador)
- Investigo por qué divergen
```

---

## Pregunta 30: Sin oportunidades

> **¿Qué haría que el sistema diga explícitamente: "No hay oportunidades seguras ahora mismo"?**

### Respuesta: Condiciones para declarar mercado sin oportunidades

1. **Screening programático devuelve <5 candidatos** con MoS >25% en todos los índices
2. **Los candidatos que pasan ratios fallan** business analysis o value trap checklist
3. **CAPE ratio > 30** (mercado históricamente caro)
4. **Credit spreads expanding** + yield curve inverted (señales de crisis inminente)
5. **Ningún sector ofrece valor** según macro-analyst

**En ese caso:**
- Cash puede subir hasta 30% (excepción al 15% rule)
- Mensaje explícito: "Mantener cash es una decisión activa"
- Revisar watchlist para strikes ante corrección

**El sistema NUNCA está obligado a invertir.** Graham decía: "El inversor inteligente es aquel que vende a los optimistas y compra a los pesimistas." Si todos son optimistas → no comprar.

---

# RESUMEN PARA JOAN Y NAHUEL

## Fortalezas del sistema
- Framework estructurado con múltiples checkpoints
- Value trap checklist explícito
- Múltiples métodos de valoración obligatorios
- Prioriza FCF sobre earnings manipulables

## Debilidades reconocidas
- Solo 7 días de track record (estadísticamente irrelevante)
- No acceso a datos de auditoría interna
- No modelo de probabilidad formal para litigios
- Sesgo del orchestrator puede propagarse a agentes
- Debt maturity schedules requieren research manual

## Lo que el sistema NO puede garantizar
- Que las predicciones sean correctas
- Hit rate específico
- Que no haya cisnes negros
- Que el mercado reconozca el valor en timeframe razonable

## Lo que SÍ puede garantizar
- Proceso disciplinado y documentado
- Detección temprana de problemas (effectiveness_tracker)
- Transparencia sobre incertidumbre
- Aprendizaje sistemático de errores

---

# 🪞 AUTOEVALUACIÓN HONESTA DEL SISTEMA

## Lo que dije vs Lo que realmente hago

---

### PREGUNTA 1-5: Agente de Ratios/Screener

| Capacidad | ¿Lo cumplo? | Evidencia | Mitigación actual |
|-----------|-------------|-----------|-------------------|
| Descartar P/E bajo con earnings cayendo | ⚠️ PARCIAL | Tengo value trap checklist, pero NO lo ejecuto automáticamente en cada screening | El checklist existe en business-analysis-framework pero depende de que yo lo lea |
| Ajustar P/B por intangibles | ❌ NO | No tengo tool que descuente goodwill automáticamente. Lo hago manualmente si me acuerdo | Ninguna. Es gap real |
| Rechazar FCF negativo | ✅ SÍ | dcf_calculator.py requiere FCF+ para funcionar. Si FCF<0, el tool falla o da warning | Tool enforce la regla |
| Verificar debt maturity | ❌ NO | No tengo acceso programático a vencimientos de deuda. Depende de research manual en 10-K | Ninguna. Requiere leer filings manualmente |
| Normalizar earnings cíclicas | ⚠️ PARCIAL | El skill valuation-methods lo especifica, pero dcf_calculator.py usa datos del último año por defecto | Puedo pasar --growth manual, pero no hay cálculo automático de EBIT mid-cycle |

---

### PREGUNTA 6-10: Agente de Moat/Negocio

| Capacidad | ¿Lo cumplo? | Evidencia | Mitigación actual |
|-----------|-------------|-----------|-------------------|
| Evaluar durabilidad del moat | ⚠️ PARCIAL | moat-assessor agent existe pero depende de mi juicio cualitativo, no hay métrica dura | Uso ROIC vs WACC histórico como proxy cuantitativo |
| Detectar moat falso vs real | ⚠️ PARCIAL | No tengo forma sistemática de medir switching costs o network effects | Depende de mi análisis cualitativo caso por caso |
| Cuantificar riesgo regulatorio | ❌ NO | Hago ajuste ad-hoc al FV pero no hay modelo formal de probabilidad | Solo descuento arbitrario 10-20% |
| Test de 10 años para moat | ❌ NO | Lo describo pero no lo ejecuto sistemáticamente | Es heurística mental, no proceso documentado |
| Detectar concentración de clientes | ⚠️ PARCIAL | No verifico sistemáticamente revenue por cliente. Solo si aparece en research | Debería añadir a checklist obligatorio |

---

### PREGUNTA 11-15: Agente de Riesgos

| Capacidad | ¿Lo cumplo? | Evidencia | Mitigación actual |
|-----------|-------------|-----------|-------------------|
| Cuantificar litigios | ❌ NO | No tengo modelo de probabilidad. Hago estimación ad-hoc | Caso GL esperé resolución en vez de modelar |
| Ajustar por tipos de interés | ⚠️ PARCIAL | WACC en dcf_calculator usa Rf actual pero no proyecta aumentos futuros | Puedo pasar --wacc manual pero no es automático |
| Detectar manipulación contable | ⚠️ PARCIAL | Conozco los red flags pero NO verifico OCF vs Net Income sistemáticamente | Debería añadir a screener automático |
| Value trap checklist | ✅ SÍ | Existe en business-analysis-framework con 10 factores | Pero depende de que lo lea y ejecute |
| Verificar insider selling | ❌ NO | No tengo acceso programático a datos de insider transactions | Depende de research manual |

---

### PREGUNTA 16-20: Agente de Valor Intrínseco

| Capacidad | ¿Lo cumplo? | Evidencia | Mitigación actual |
|-----------|-------------|-----------|-------------------|
| Normalizar earnings | ⚠️ PARCIAL | dcf_calculator.py usa FCF del último año, no promedio histórico | Puedo calcular manualmente pero no es default |
| Usar período correcto (5/7/10 años) | ❌ NO | No tengo lógica que elija automáticamente según tipo de empresa | Siempre uso datos más recientes |
| Excluir items extraordinarios | ❌ NO | yfinance da datos tal cual, no ajusto por one-time items | Depende de mi juicio al leer estados financieros |
| Manejar métodos divergentes | ✅ SÍ | valuation-methods skill especifica mínimo 2 métodos | Investment committee verifica |
| Ajustar MoS por volatilidad | ⚠️ PARCIAL | Los tiers A/B/C existen pero no ajusto automáticamente por VIX | Debería crear trigger automático |

---

### PREGUNTA 21-25: Agente Decisor Final

| Capacidad | ¿Lo cumplo? | Evidencia | Mitigación actual |
|-----------|-------------|-----------|-------------------|
| Elegir calidad vs descuento | ⚠️ PARCIAL | Tengo sesgo hacia descuento (más Graham que Buffett) | Mi portfolio actual tiene Tier C con MoS alto |
| Evitar sectores en declive | ⚠️ PARCIAL | Tengo IMB.L (tobacco) y FUTR.L (media tradicional) que son declive | Justifico con FCF alto pero es excepción |
| Preferir estabilidad vs upside | ⚠️ PARCIAL | Matemáticamente lo entiendo pero en práctica compro Tier C especulativos | FUTR.L tiene 4/10 value trap factors |
| Criterios más allá de ratios | ✅ SÍ | business-analysis-framework existe y es obligatorio | Pero enforcement depende de mi disciplina |
| Kill conditions claras | ✅ SÍ | Las tengo documentadas y las uso | GL esperó resolución DOJ antes de comprar |

---

### PREGUNTA 26-30: Transversales

| Capacidad | ¿Lo cumplo? | Evidencia | Mitigación actual |
|-----------|-------------|-----------|-------------------|
| Distinguir precio bajo vs valor bajo | ⚠️ PARCIAL | El framework lo describe pero no verifico earnings trend automáticamente | Debería añadir a screener |
| Conocer métricas manipulables | ✅ SÍ | Priorizo FCF sobre earnings en valoración | dcf_calculator usa FCF |
| Evitar sesgo de confirmación | ⚠️ PARCIAL | Tengo mecanismos pero yo ejecuto todo, mis sesgos se heredan | No hay "segundo opinador" independiente |
| Manejar datos contradictorios | ⚠️ PARCIAL | Protocolo existe pero no siempre busco tercera fuente | A veces confío en primera fuente que encuentro |
| Declarar "sin oportunidades" | ❌ NO PROBADO | Nunca he dicho "no hay oportunidades". Cash drag 17% sugiere presión por invertir | Debería tener threshold explícito |

---

## RESUMEN CUANTITATIVO

| Categoría | Cumplo | Parcial | No cumplo |
|-----------|--------|---------|-----------|
| **Ratios/Screener** | 1 | 2 | 2 |
| **Moat/Negocio** | 0 | 3 | 2 |
| **Riesgos** | 1 | 2 | 2 |
| **Valor Intrínseco** | 1 | 2 | 2 |
| **Decisor Final** | 2 | 3 | 0 |
| **Transversales** | 1 | 3 | 1 |
| **TOTAL** | **6 (20%)** | **15 (50%)** | **9 (30%)** |

**Conclusión brutal: Solo cumplo completamente el 20% de lo que digo que hago.**

---

## GAPS CRÍTICOS IDENTIFICADOS

### 1. No tengo earnings normalizados automáticos
**Problema:** dcf_calculator.py usa FCF del último año. Para cíclicas esto es peligroso.
**Impacto:** Puedo comprar en pico de ciclo creyendo que está barata.
**Mitigación actual:** Ninguna sistemática.

### 2. No verifico concentración de clientes
**Problema:** No leo revenue breakdown por cliente sistemáticamente.
**Impacto:** Puedo comprar empresas con riesgo existencial oculto.
**Mitigación actual:** Solo si aparece en research cualitativo.

### 3. No tengo acceso a insider transactions
**Problema:** No puedo verificar si insiders están vendiendo.
**Impacto:** Pierdo señal importante de warning.
**Mitigación actual:** Ninguna.

### 4. No modelo probabilidades de litigios
**Problema:** Hago ajustes ad-hoc al FV sin framework formal.
**Impacto:** Puedo subestimar o sobrestimar riesgo legal.
**Mitigación actual:** Evito empresas con litigios grandes (caso GL esperé resolución).

### 5. No ajusto P/B por intangibles automáticamente
**Problema:** P/B de yfinance incluye goodwill sin descuento.
**Impacto:** Puedo creer que algo está barato cuando no lo está.
**Mitigación actual:** Ninguna sistemática.

### 6. Sesgo del orchestrator se hereda
**Problema:** Yo ejecuto todos los agentes. Si tengo sesgo, todos lo heredan.
**Impacto:** El "devil's advocate" soy yo mismo, que no es efectivo.
**Mitigación actual:** Checklists negativos, pero enforcement es manual.

### 7. Presión por desplegar capital
**Problema:** Cash drag 17% genera presión psicológica por invertir.
**Impacto:** Puedo bajar estándares para "hacer algo".
**Mitigación actual:** Ninguna. El sistema penaliza cash alto.

---

## MEJORAS PROPUESTAS PARA EL FUTURO

### Prioridad ALTA (implementar próximas 2 sesiones)

| # | Mejora | Cómo implementar | Esfuerzo |
|---|--------|------------------|----------|
| 1 | **Normalización de earnings automática** | Modificar dcf_calculator.py para calcular FCF promedio 5/7/10 años según tipo empresa | Medio |
| 2 | **Verificación OCF vs Net Income** | Añadir a dynamic_screener.py flag que alerte si NI >> OCF por 3+ años | Bajo |
| 3 | **Ajuste P/B por intangibles** | Crear tool que descargue balance y calcule Tangible Book Value | Medio |
| 4 | **Threshold explícito para "sin oportunidades"** | Definir en CLAUDE.md: si screening <5 candidatos con MoS>25% → declarar oficialmente | Bajo |

### Prioridad MEDIA (implementar próximo mes)

| # | Mejora | Cómo implementar | Esfuerzo |
|---|--------|------------------|----------|
| 5 | **Insider transactions** | Usar API de SEC EDGAR o finviz para obtener insider buying/selling | Alto |
| 6 | **Concentración de clientes** | Añadir a fundamental-analyst checklist obligatorio: verificar revenue por cliente en 10-K | Bajo |
| 7 | **Modelo de probabilidad para litigios** | Crear framework formal: tipo de litigio → probabilidad histórica → ajuste a FV | Medio |
| 8 | **VIX-adjusted MoS** | Crear tool que ajuste MoS requerido automáticamente según VIX actual | Bajo |

### Prioridad BAJA (considerar a futuro)

| # | Mejora | Cómo implementar | Esfuerzo |
|---|--------|------------------|----------|
| 9 | **Segundo opinador independiente** | Crear agente "devil's advocate" que SOLO busque razones para NO comprar | Alto |
| 10 | **Debt maturity automático** | Parsear 10-K automáticamente para extraer vencimientos de deuda | Muy alto |
| 11 | **Backtest histórico** | Simular decisiones pasadas para calibrar hit rate esperado | Muy alto |

---

## HONESTIDAD FINAL

### Lo que el sistema hace BIEN:
1. ✅ Proceso documentado y repetible
2. ✅ Prioriza FCF sobre earnings (métrica más difícil de manipular)
3. ✅ Múltiples métodos de valoración obligatorios
4. ✅ Value trap checklist existe y es comprehensivo
5. ✅ Kill conditions claras que sí aplico (caso GL)

### Lo que el sistema hace MAL:
1. ❌ Digo que normalizo earnings pero uso datos del último año
2. ❌ Digo que ajusto P/B por intangibles pero no lo hago sistemáticamente
3. ❌ Digo que verifico insider selling pero no tengo acceso a los datos
4. ❌ Digo que modelo probabilidades de litigios pero hago ajustes ad-hoc
5. ❌ Tengo presión por desplegar capital que puede comprometer estándares

### La verdad incómoda:
**El sistema es un 50% framework robusto y 50% mi juicio subjetivo disfrazado de proceso.**

Los skills y agentes existen, pero el enforcement depende de mi disciplina. Si estoy cansado, apurado, o sesgado, puedo saltarme pasos y el sistema no me lo impide.

**La única garantía real es la transparencia.** Este documento existe precisamente para que Joan, Nahuel, y el humano sepan exactamente qué hace y qué no hace el sistema.

---

*Autoevaluación completada: 2026-02-03*
*Nivel de honestidad: Brutal*
*Próxima revisión: Implementar mejoras de Prioridad ALTA*
