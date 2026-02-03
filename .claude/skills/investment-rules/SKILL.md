---
name: investment-rules
description: Core investment rules - buy criteria (margin >25%, moat, thesis), sell criteria with clear triggers, sizing rules, never-do list
user-invocable: false
disable-model-invocation: false
---

# Investment Rules Skill

## Reglas de Compra (GATES OBLIGATORIOS)

### Gate 1: Entendimiento del Negocio
- [ ] Business Analysis Framework completado
- [ ] Puedo explicar el negocio en 2 minutos
- [ ] Sé POR QUÉ está barata y tengo contra-tesis
- [ ] Value trap checklist pasado (<3 factores SI)

### Gate 2: Proyección Fundamentada
- [ ] Projection Framework completado
- [ ] Growth rates derivados de TAM/share/pricing (NO defaults)
- [ ] WACC calculado (NO "usaré 9%")
- [ ] Escenarios Bear/Base/Bull con probabilidades

### Gate 3: Valoración Multi-Método
- [ ] Mínimo 2 métodos de valoración
- [ ] Métodos apropiados para el tipo de empresa
- [ ] Si métodos divergen >30%, explicación documentada

### Gate 4: Margen de Seguridad (TIERED)
| Tier | Tipo | MoS Mínimo | Criterios |
|------|------|-----------|-----------|
| A | Wide Moat Defensivos | **>=15%** | Quality Score >=7/10. Utilities, staples, pharma, insurance. ROE >15%, 10+ yr dividend, FCF predecible |
| B | Cíclicos de Calidad | **>=25%** | Balance sólido, líder de mercado, ROE >12%. Energy, telecom, industrials, financials |
| C | Turnarounds/Especulativo | **>=35%** | Thesis depende de catalizador, FCF incierto, reestructuración, riesgo regulatorio/China |

### Gate 5: Contexto Macro
- [ ] World view actual revisado
- [ ] Fit con ciclo económico evaluado
- [ ] No comprar cíclicas agresivas en late-cycle sin razón documentada

### Gate 6: Portfolio Fit
- [ ] Posición <7%, sector <25%, geografía <35%
- [ ] Cash post-compra >5%
- [ ] Correlación con posiciones existentes evaluada

### Gate 7: Autocrítica
- [ ] Asunciones no validadas listadas
- [ ] Sesgos reconocidos (popularity, confirmation, recency)
- [ ] Kill conditions definidas
- [ ] Qué me haría cambiar de opinión documentado

### Gate 8: Entendimiento del Sector (NUEVO v2.1)
- [ ] Sector view existe en world/sectors/[sector].md
- [ ] TAM, tendencias, competencia entendidos
- [ ] Riesgos de disrupción conocidos
- [ ] Sentimiento de mercado documentado
- [ ] Fit empresa-sector evaluado

## Quality Score (obligatorio para Tier A)
Para calificar Tier A (15% MoS), el stock DEBE puntuar >=7/10:
1. ROE consistente >15% (5+ años)
2. FCF positivo cada año (5+ años)
3. Debt/Equity <1.0 (o Debt/EBITDA <3x para utilities)
4. Dividendo 10+ años sin corte
5. Wide moat (marca, regulación, red, switching costs)
6. Estabilidad revenue (max drawdown <15% en recesiones)
7. Calidad management (insider ownership, capital allocation)
8. Cobertura analistas >10 (líquido, bien entendido)
9. Market cap >€10B (establecida)
10. Sector defensivo (utilities, staples, pharma, insurance)

Score 7-8/10 = Tier A (15% MoS)
Score 5-6/10 = Tier B (25% MoS)
Score <5/10 = Tier C (35% MoS) o REJECT

---

## Reglas de Venta (CLARAS Y ACCIONABLES)

### Venta por Valoración (parcial o total)
| Trigger | Acción | Razón |
|---------|--------|-------|
| Precio = 80% Fair Value Base | Vender 25% | Lock in gains, reducir riesgo |
| Precio = Fair Value Base | Vender 50% (total 75%) | Thesis mostly played out |
| Precio = Fair Value Bull | Vender resto | Full value, rotar a mejor oportunidad |

### Venta por Thesis Invalidada (INMEDIATA)
- Dividend cut (para dividend stocks)
- ROIC < WACC por 2+ años consecutivos
- Management fraud/governance scandal
- Moat structurally impaired (no temporal)
- Deuda fuera de control (coverage <1.5x)
- Kill conditions de la thesis se cumplen

**REGLA:** Vender por thesis invalidada NO IMPORTA el precio. No esperar recuperación.

### Venta por Oportunidad (rotación)
- Encontré mejor oportunidad con MoS >15pp mayor
- Capital limitado, debo concentrar en mejores ideas
- Correlación excesiva con otra posición mejor

### Venta por Rebalanceo
- Posición >10% por apreciación → trim a 7%
- Sector >30% por apreciación → trim a 25%

### NO Vender Por:
- Caída de precio sin cambio en fundamentales
- Miedo general del mercado
- Analyst downgrade sin nueva información
- Earnings miss único si thesis intacta

---

## Reglas de Sizing Dinámico

### Base Sizing: 4% por posición nueva

### Ajustes por Convicción
| Factor | Ajuste |
|--------|--------|
| MoS >40% + Wide moat | +2% (hasta 6%) |
| MoS 35-40% + Narrow moat | +1% (hasta 5%) |
| MoS 25-30% | -1% (3%) |
| MoS 15-25% (Tier A only) | -1.5% (2.5%) |

### Ajustes por Riesgo
| Factor | Ajuste |
|--------|--------|
| Alta correlación con posiciones existentes (>0.7) | -1% |
| Cíclica en late-cycle | -1% |
| Turnaround/especulativo | -1% |
| Emerging market | -0.5% |
| Small cap (<€2B) | -0.5% |

### Sizing Mínimo y Máximo
- Mínimo: 2% (below this, not worth the attention)
- Máximo: 6% (nunca más, incluso con alta convicción)
- Máximo absoluto tras apreciación: 10% (trigger rebalanceo)

---

## Valoración Conservadora (Parámetros)

| Parámetro | Regla |
|-----------|-------|
| Growth rates | Management guidance -20-30% |
| Terminal growth | ≤ GDP (2-3%) |
| WACC mínimo | 8% empresas establecidas |
| WACC típico | 9-11% |
| Pipeline pharma | Haircut 70% |
| Proyecciones >5 años | Alta incertidumbre, usar escenarios |
| Goodwill | Verificar riesgo impairment |

---

## Hechos vs Opiniones
| HECHO (confiar) | OPINIÓN (cuestionar) |
|-----------------|---------------------|
| ROE histórico | "ROE futuro será X%" |
| FCF actual | "FCF crecerá Y%" |
| Deuda actual | "Reduciremos deuda a Z" |
| Dividendo pagado N años | "Pipeline tiene N blockbusters" |
| Market share actual | "Ganaremos share" |
| Margen histórico | "Márgenes expandirán" |

---

## NUNCA (Reglas Inmutables)
- Apalancamiento personal
- Operar sin thesis documentada completa
- Vender por miedo (pánico de mercado)
- Comprar por FOMO (rally de mercado)
- Saltarse rebalanceo scheduled
- Ignorar triggers críticos
- Usar defaults en proyecciones sin justificación
- Comprar sin entender por qué está barata
- Comprar value traps (>3 factores del checklist)
- Ignorar contexto macro para cíclicas
