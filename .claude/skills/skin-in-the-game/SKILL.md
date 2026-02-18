# SKIN IN THE GAME - Framework v4.0

> **Framework para evaluar QUIEN opina y cuanto les cuesta estar equivocado.**
> Complementa Filtro 2 del contrathesis-framework.
> **NOTA v4.0:** Framework de razonamiento. No thresholds fijos.

---

## Proposito

No todas las opiniones sobre una empresa valen lo mismo.
Lo que importa no es CUANTOS opinan, sino CUANTO les cuesta equivocarse.

---

## Jerarquia de Credibilidad

### Nivel 1: Mayor Credibilidad

**CEO/CFO comprando con dinero propio (no options)**
- Conocen el negocio mejor que nadie
- Dinero propio = skin in the game real
- Especialmente significativo: compras DESPUES de caidas
- Especialmente significativo: compras por encima de su compensacion anual

**Short seller con track record publicado**
- Ha puesto capital Y reputacion en la linea
- Track record verificable (aciertos y errores)
- Mas credible si tiene historial en el sector

### Nivel 2: Credibilidad Alta

**Institucional anadiendo posicion significativa (>1% del fondo)**
- Smart money con research teams dedicados
- Pero: pueden estar equivocados por largo tiempo
- Mas significativo si es concentrado (position sizing alto)

**Analista contra consenso con argumento publicado**
- Ha tomado riesgo reputacional al disentir
- Mas credible si tiene track record en el sector
- Menos credible si es la primera cobertura del valor

### Nivel 3: Credibilidad Media

**Institucional reduciendo posicion**
- Puede ser rebalanceo, flujos del fondo, o tesis
- Solo significativo si MUCHOS reducen simultaneamente
- Verificar si hay cambio de mandato del fondo

**Director comprando (board member, no executive)**
- Menos informacion que CEO/CFO
- Pero sigue siendo dinero propio
- Puede ser "compra de apoyo" sin conviccion real

### Nivel 4: Menor Credibilidad

**Analista sell-side siguiendo consenso**
- Incentivo a mantener relacion con la empresa
- "Buy" es el default (menos conflictivo)
- Solo significativo si CAMBIA de rating (upgrade/downgrade)

**Insider selling via 10b5-1 / programado**
- Ruido: planeado con meses de anticipacion
- NO es senal de nada (ni bueno ni malo)
- Solo significativo si CANCELAN un plan de venta

**Opinion en redes sociales / foros**
- Zero skin in the game (pueden ser anonimos)
- Volume de opinion ≠ calidad de opinion
- Util solo para detectar narrativas prevalentes (no para validarlas)

---

## Preguntas Guia

1. **Cuanto le cuesta a esta persona estar equivocada?**
   - Si la respuesta es "nada" → credibilidad minima
   - Si la respuesta es "su capital personal" → credibilidad alta

2. **Que incentivo tiene esta persona para opinar asi?**
   - Sell-side: relacion con empresa, comisiones
   - Buy-side: posicion existente (talking their book)
   - Management: compensacion, reputacion, empleo
   - Short seller: posicion short (pero tambien reputacion)

3. **Que sabe esta persona que yo no se?**
   - Insider: informacion operativa no publica
   - Sector specialist: contexto competitivo profundo
   - Generalista: probablemente menos que yo si he hecho el analisis

4. **Que historial tiene esta persona?**
   - Track record verificable > reputacion percibida
   - Errores recientes > aciertos lejanos

---

## Aplicacion Practica

### Para Longs
- Insiders comprando + institucionales anadiendo = CONFIRMACION de thesis
- Insiders vendiendo (no programado) + institucionales saliendo = CUESTIONAMIENTO de thesis
- Si hay conflicto entre datos y opiniones → DATOS ganan

### Para Shorts
- Insiders vendiendo agresivamente (no programado) = CONFIRMACION de fragilidad
- Insiders comprando significativamente = CUESTIONAMIENTO de short thesis
- Short interest alto + squeeze risk = considerar P11 (Asimetria)

### Tool de Soporte
`python3 tools/insider_tracker.py TICKER` — extrae datos de transacciones, institucionales, short interest, consenso.

---

## Anti-Sesgo

- **Authority bias:** No dar mas peso a "nombres famosos" — evaluar por argumento y skin in the game
- **Bandwagon effect:** 100 analistas con "Buy" < 1 insider comprando con dinero propio
- **Confirmation bias:** Buscar ACTIVAMENTE las opiniones contrarias a mi thesis

---

**Ultima actualizacion:** 2026-02-18
**Framework version:** 4.0
