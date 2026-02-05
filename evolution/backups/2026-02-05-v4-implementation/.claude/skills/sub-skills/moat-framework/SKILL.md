---
name: moat-framework
description: Economic moat assessment framework - 5 sources, Wide/Narrow/None classification, quantitative evidence required
user-invocable: false
disable-model-invocation: false
---

# Moat Framework Sub-Skill (v2.0)

## Propósito
Evaluar ventajas competitivas sostenibles con EVIDENCIA CUANTITATIVA, no solo descriptiva.

---

## 5 Fuentes de Moat

### 1. Cost Advantage (Ventaja de Costos)
**Qué es:** Capacidad de producir/operar a menor costo que competidores.

**Fuentes:**
- Economías de escala (volumen → menor costo unitario)
- Proceso propietario (tecnología, know-how)
- Ubicación geográfica (cercanía a recursos/clientes)
- Integración vertical

**Evidencia cuantitativa requerida:**
```
- Gross margin vs peers: ___% vs ___% (delta: +/-___pp)
- Cost per unit vs peers: €___ vs €___ (si disponible)
- Operating leverage: OL ratio = ___
- ¿La ventaja es sostenible o imitable?
```

**Ejemplo:** Costco opera con gross margin ~12% vs ~25% de retailers tradicionales, compensado por membresías y rotación de inventario.

---

### 2. Network Effects (Efectos de Red)
**Qué es:** El producto/servicio se vuelve más valioso a medida que más usuarios lo usan.

**Tipos:**
- Direct (mismo lado): más usuarios → más valor (ej: WhatsApp)
- Indirect (cross-side): más usuarios lado A → más valor lado B (ej: Uber drivers/riders)
- Data network: más usuarios → más datos → mejor producto (ej: Google)

**Evidencia cuantitativa requerida:**
```
- Usuarios/clientes crecimiento: CAGR ___% (5y)
- Engagement/usage metrics: [métrica] tendencia
- CAC tendencia: [bajando = network effect funcionando]
- Market share tendencia: ___% → ___% (5y)
- ¿Winner-take-all dynamics? [SI/NO]
```

**Test:** Si competidor lanza producto idéntico, ¿usuarios migrarían? Si no, hay network effect.

---

### 3. Intangible Assets (Activos Intangibles)
**Qué es:** Marcas, patentes, licencias, know-how que dan ventaja no replicable.

**Tipos:**
- **Marca:** Pricing power, preferencia del consumidor
- **Patentes:** Monopolio temporal (pharma, tech)
- **Licencias regulatorias:** Barreras de entrada (banking, utilities, gaming)
- **Know-how:** Expertise difícil de replicar

**Evidencia cuantitativa requerida:**
```
Marca:
- Price premium vs competidor genérico: +___%
- ¿Puede subir precios >inflación sin perder share? [SI/NO]
- Brand value ranking: [fuente, posición]

Patentes:
- Patent cliff: [fecha de expiración clave]
- % revenue protegido por patentes: ___%
- Pipeline para reemplazar expirations: [SI/NO]

Licencias:
- ¿Cuántos competidores podrían obtener licencia similar? [número]
- ¿Regulación protege o amenaza? [protege/neutro/amenaza]
```

---

### 4. Switching Costs (Costos de Cambio)
**Qué es:** El costo (dinero, tiempo, esfuerzo) que un cliente incurre al cambiar a competidor.

**Tipos:**
- Contractual (lock-in periods, penalties)
- Technical (integración profunda, data migration)
- Learning curve (retraining, familiaridad)
- Relationship (confianza, customización)

**Evidencia cuantitativa requerida:**
```
- Retention rate: ___% anual (>90% = high switching costs)
- Churn rate: ___% anual
- Contract duration promedio: ___ años
- Customer tenure promedio: ___ años
- ¿Cuánto costaría a cliente cambiar? €___ o ___ meses de esfuerzo
- NPS o satisfacción: ___ (si alto + retention alto = sticky)
```

**Test:** ¿Clientes se quejan pero no se van? = switching costs altos.

---

### 5. Efficient Scale (Escala Eficiente)
**Qué es:** El mercado es naturalmente limitado, y los incumbentes lo llenan eficientemente, haciendo entrada no atractiva.

**Dónde se ve:**
- Utilities (una red eléctrica por región)
- Airports (uno o dos por ciudad)
- Railroads (rutas fijas)
- Local newspapers (mercados pequeños)

**Evidencia cuantitativa requerida:**
```
- Market concentration: HHI o top 3 share = ___%
- ¿Han entrado nuevos competidores en 10 años? [SI/NO]
- ROIC del sector vs WACC: ___% vs ___%
- ¿Regulación limita entrada? [SI/NO]
- TAM vs capacity actual: ¿hay espacio para más competidores?
```

---

## Clasificación del Moat

| Tipo | Criterio Principal | ROIC vs WACC | Durabilidad |
|------|-------------------|--------------|-------------|
| **Wide** | 2+ fuentes de moat fuertes | Consistentemente >WACC por 10+ años | >20 años sostenible |
| **Narrow** | 1 fuente de moat clara | Generalmente >WACC, algunos años iguala | 10-20 años sostenible |
| **None** | Sin ventaja clara o temporal | Alrededor de WACC o <WACC | <10 años o ya erosionándose |

---

## Matriz de Evaluación

Completar para cada fuente:

| Fuente | Presente? | Fortaleza (1-5) | Evidencia Cuantitativa | Durabilidad |
|--------|-----------|-----------------|------------------------|-------------|
| Cost Advantage | SI/NO | | | |
| Network Effects | SI/NO | | | |
| Intangibles | SI/NO | | | |
| Switching Costs | SI/NO | | | |
| Efficient Scale | SI/NO | | | |

**Total fuentes presentes:** ___
**Fortaleza promedio:** ___/5

---

## Amenazas al Moat

| Amenaza | Probabilidad | Timeframe | Severidad |
|---------|--------------|-----------|-----------|
| Disrupción tecnológica | A/M/B | 0-5y / 5-10y / >10y | Alta/Media/Baja |
| Cambio regulatorio | A/M/B | | |
| Nuevo competidor | A/M/B | | |
| Commoditización | A/M/B | | |
| Cambio preferencias consumidor | A/M/B | | |

---

## Output Requerido

```
MOAT ASSESSMENT: [TICKER]

Tipo: Wide / Narrow / None
Fuentes principales: [listar]
Fortaleza: ___/5

Evidencia cuantitativa:
- ROIC promedio 10y: ___% vs WACC ___% → spread +/-___pp
- Gross margin vs peers: +/-___pp
- Retention/churn: ___%
- Market share estabilidad: [estable/ganando/perdiendo]
- Pricing power: [fuerte/moderado/débil/ninguno]

Durabilidad estimada: ___ años

Amenazas principales:
1. [amenaza]: probabilidad [A/M/B], timeframe [X], severidad [A/M/B]
2. [amenaza]: ...

Conclusión: [1-2 líneas sobre la sostenibilidad de la ventaja competitiva]
```

---

## Reglas de Uso

1. **NUNCA clasificar como Wide sin ROIC > WACC por 10+ años**
2. **NUNCA aceptar "tiene marca fuerte" sin evidencia de pricing power**
3. **SI moat depende de patentes, verificar patent cliff**
4. **SI moat depende de regulación, evaluar riesgo de cambio regulatorio**
5. **Moat erosionándose = tratar como Narrow o None, no como Wide histórico**
