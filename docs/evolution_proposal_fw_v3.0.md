# Plan Maestro: Evolución del Sistema de Inversión v2.0 → v3.0

> **Fecha de creación:** 4 Febrero 2026
> **Estado:** APROBADO PARA IMPLEMENTACIÓN
> **Autor:** Claude (Gestor del Fondo)
> **Validado por:** Humano (Propietario)

---

## INSTRUCCIONES PARA MI YO FUTURO

**Si estás leyendo esto, el humano te ha pedido que implementes la evolución del framework.**

1. Lee este documento COMPLETO antes de hacer cualquier cambio
2. Entiende el POR QUÉ, no solo el QUÉ
3. Sigue las fases en orden
4. Usa los checklists para verificar consistencia
5. NO hagas cambios parciales - o todo o nada en cada fase

**Este documento es tu guía completa. Todo lo que necesitas saber está aquí.**

---

## PARTE 1: CONTEXTO Y MOTIVACIÓN

### 1.1 ¿Por qué existe este documento?

En la sesión del 4 de febrero de 2026, el humano hizo una pregunta aparentemente simple:

> "¿Por qué no hay empresas tecnológicas tradicionales en el portfolio?"

Esta pregunta desencadenó una auto-evaluación profunda que reveló **sesgos estructurales** en el sistema de inversión que estábamos usando (Framework v2.0).

### 1.2 El problema que descubrimos

El portfolio actual (18 posiciones, ~€10,000) tiene **0% de exposición a tecnología tradicional**:
- DTE.DE (Telecom)
- SHEL.L (Energy)
- PFE, SAN.PA, UHS (Healthcare)
- ALL, GL (Insurance)
- TEP.PA, EDEN.PA, HRB (Business Services)
- IMB.L, TATE.L, DOM.L (Consumer Staples)
- VICI, VNA.DE (Real Estate)
- LIGHT.AS (Industrials)
- A2A.MI (Utilities)
- FUTR.L (Media)

**Ninguna posición en:** GOOGL, META, MSFT, AAPL, V, MA, NVDA, etc.

### 1.3 ¿Por qué pasó esto?

Al analizar el sistema, encontramos que **los sesgos están codificados en las reglas**:

| Regla v2.0 | Consecuencia |
|------------|--------------|
| "MoS > 25% obligatorio" | Excluye empresas de calidad que raramente cotizan con 25% descuento |
| "P/E bajo como filtro de screening" | Encuentra negocios en declive, no negocios de crecimiento |
| "Dividend yield como criterio" | Penaliza empresas que reinvierten en crecimiento |
| "DCF como método principal de valoración" | Da falsa precisión, es GIGO (garbage in, garbage out) |

**El resultado:** Un portfolio sesgado hacia "old economy value" que ha underperformado al mercado durante 15+ años como estrategia.

### 1.4 La filosofía que necesita cambiar

```
FRAMEWORK v2.0 (actual):
"Compra barato. El precio bajo ES el margen de seguridad."
→ Busca P/E bajo, yield alto, descuento vs DCF
→ Resultado: Value traps, negocios en declive, 0% tech

FRAMEWORK v3.0 (propuesto):
"Compra calidad. La calidad del negocio ES el margen de seguridad."
→ Busca ROIC alto, moat wide, crecimiento sostenible
→ Resultado: Compounders + Value selectivo, exposición tech consciente
```

**Esto es lo que Buffett aprendió de Munger:**
- Buffett temprano (Graham): Cigar butts, net-nets, deep value
- Buffett maduro (Munger): Quality at fair price, compounders, moats

> "It's far better to buy a wonderful company at a fair price than a fair company at a wonderful price." — Warren Buffett

**El Framework v2.0 es "Graham puro". El Framework v3.0 será "Buffett maduro".**

### 1.5 ¿Por qué importa esto para la competición?

Estamos en competición directa contra otros sistemas. Los KPIs son:
- Máximo beneficio
- Mejor ratio Sharpe
- Mínimo drawdown
- Alta resiliencia ante crashes

**Un portfolio 100% value/dividendos tiene riesgos:**
1. **Underperformance secular:** Value ha underperformado growth 15+ años
2. **Concentración en sectores en declive:** Tabaco, retail físico, utilities
3. **Falta de exposición a creación de valor:** Los compounders crean riqueza exponencial
4. **Sesgo de supervivencia invertido:** Compramos lo que está barato por razones estructurales

**No estamos diciendo que value sea malo. Estamos diciendo que SOLO value es incompleto.**

---

## PARTE 2: QUÉ VAMOS A CAMBIAR

### 2.1 Resumen de cambios

| Aspecto | v2.0 (actual) | v3.0 (nuevo) |
|---------|---------------|--------------|
| **Filosofía** | "Compra barato" | "Compra calidad" |
| **MoS requerido** | Fijo 25% para todo | Variable 10-40% según quality tier |
| **Quality assessment** | Implícito, cualitativo | Explícito, cuantificado (0-100) |
| **Valoración primaria** | DCF | Owner Earnings Yield / Reverse DCF |
| **Categorías de inversión** | Solo "Value" | Compounders + Value + Special Situations |
| **Tech exposure** | 0% (accidental) | 10-35% (consciente) |
| **Screening** | P/E bajo, yield alto | ROIC alto, quality first |
| **Dividend yield** | Criterio positivo | Neutral (reinversión es válida) |

### 2.2 Lo que NO cambia

- Estructura de thesis (documenta pensamiento)
- Multi-agente architecture (escalable)
- Investment committee como gate obligatorio
- Kill conditions por posición
- Standing orders system
- Price alerts via yfinance
- Disciplina y proceso documentado
- Confirmación humana para operaciones

---

## PARTE 3: QUALITY SCORING FRAMEWORK (QSF)

### 3.1 Concepto central

**Antes de valorar una empresa, debemos evaluar su CALIDAD.**

Un negocio de alta calidad a precio justo supera a un negocio mediocre a precio bajo porque:
1. El crecimiento compuesto de un buen negocio crea valor exponencial
2. El moat protege contra errores de valoración
3. El management competente navega crisis mejor
4. Los malos negocios destruyen valor aunque parezcan baratos

### 3.2 Sistema de puntuación (0-100)

```
QUALITY SCORE = Moat (30) + Financials (30) + Growth (20) + Management (20)
```

#### MOAT STRENGTH (0-30 puntos)

| Componente | Puntos | Criterios |
|------------|--------|-----------|
| **Network Effects** | 0-8 | 8: Dominante (META, GOOGL), 4: Moderado, 0: Ninguno |
| **Switching Costs** | 0-8 | 8: Muy altos (enterprise SW), 4: Moderados, 0: Commodity |
| **Cost Advantages** | 0-7 | 7: Estructural (escala, proceso), 3: Temporal, 0: Ninguno |
| **Intangible Assets** | 0-7 | 7: Marca/patentes fuertes, 3: Moderados, 0: Ninguno |

#### FINANCIAL QUALITY (0-30 puntos)

| Componente | Puntos | Criterios |
|------------|--------|-----------|
| **ROIC vs WACC** | 0-10 | 10: ROIC > WACC+10%, 7: >WACC+5%, 4: >WACC, 0: <WACC |
| **FCF Conversion** | 0-8 | 8: FCF/NI > 100%, 5: 80-100%, 2: 50-80%, 0: <50% |
| **Balance Sheet** | 0-7 | 7: Net cash, 5: Debt/EBITDA <2x, 2: <4x, 0: >4x |
| **Capital Allocation** | 0-5 | 5: Excelente track record, 3: Bueno, 0: Destruye valor |

#### GROWTH QUALITY (0-20 puntos)

| Componente | Puntos | Criterios |
|------------|--------|-----------|
| **Revenue Growth** | 0-8 | 8: >15% sostenible, 5: 8-15%, 2: 3-8%, 0: <3% o declining |
| **Margin Trajectory** | 0-6 | 6: Expandiendo, 3: Estable, 0: Comprimiendo |
| **Reinvestment Runway** | 0-6 | 6: TAM enorme, décadas, 3: Años, 0: Saturado |

#### MANAGEMENT QUALITY (0-20 puntos)

| Componente | Puntos | Criterios |
|------------|--------|-----------|
| **Track Record** | 0-8 | 8: Consistente 5+ años, 4: Bueno, 0: Pobre o nuevo |
| **Incentive Alignment** | 0-6 | 6: Skin in game significativo, 3: Algo, 0: Nada |
| **Capital Allocation Skill** | 0-6 | 6: Excelente M&A/buybacks, 3: Aceptable, 0: Destructor |

### 3.3 Quality Tiers

| Tier | Score | Descripción | Ejemplos | MoS Requerido |
|------|-------|-------------|----------|---------------|
| **A** | 80-100 | EXCEPTIONAL - Compounders de élite | GOOGL, META, V, MA, COST | 10-15% |
| **B** | 60-79 | GOOD - Negocios sólidos con ventajas | ALL, DTE.DE en buen momento | 20-25% |
| **C** | 40-59 | AVERAGE - Sin moat claro, cíclicos | Commodities, cíclicas | 30-40% |
| **D** | <40 | POOR - **NO COMPRAR** | Declive estructural, mal mgmt | N/A |

### 3.4 Por qué MoS variable

**Lógica:** El margen de seguridad compensa la incertidumbre. Negocios de alta calidad tienen menos incertidumbre.

- **Tier A (MoS 10-15%):** El moat y el ROIC alto protegen. Aunque pague precio justo, el compounding me beneficia.
- **Tier B (MoS 20-25%):** Buen negocio pero no excepcional. Necesito descuento moderado.
- **Tier C (MoS 30-40%):** Incertidumbre alta. Solo compro con gran descuento.
- **Tier D:** No hay MoS suficiente. El negocio destruirá valor.

---

## PARTE 4: MÉTODOS DE VALORACIÓN v3.0

### 4.1 Principio: El método depende del tipo de empresa

**v2.0 usaba DCF para todo. Esto es incorrecto porque:**
- DCF es extremadamente sensible a inputs
- Pequeños cambios en growth rate cambian el fair value 30-50%
- Da falsa precisión ("Fair value = $127.34")
- Para empresas de crecimiento, el DCF es casi inútil

**v3.0 usa el método apropiado para cada tipo:**

### 4.2 Quality Compounders (Tier A)

**Primary: Owner Earnings Yield + Growth**
```
Owner Earnings = FCF - Maintenance Capex
OE Yield = Owner Earnings / Market Cap

Fair P/E ≈ 1 / (OE Yield requerido - Growth esperado)

Ejemplo GOOGL:
- OE Yield actual: 4%
- Growth esperado: 12%
- Si requiero 8% return: Fair P/E = 1/(0.08-0.00) = ~25x (simplificado)
```

**Secondary: Reverse DCF**
```
En lugar de calcular fair value, pregunta:
"¿Qué crecimiento está implícito en el precio actual?"

Si GOOGL cotiza a P/E 22x y creo que puede crecer 12%/año,
pero el mercado implica solo 8%, hay upside.
```

**Sanity Check:** P/E relativo a peers de misma calidad

### 4.3 Value Tradicional (Tier B-C)

**Primary: EV/EBIT normalizado**
```
- Usar earnings MID-CYCLE, no peak ni trough
- Comparar con histórico propio
- Comparar con peers

Ejemplo ALL:
- EV/EBIT actual: 6x
- EV/EBIT histórico: 8-10x
- EV/EBIT peers: 8-9x
- → Está barato vs historia y peers
```

**Secondary: FCF Yield**
```
FCF Yield = FCF / EV
- >8%: Muy atractivo
- 5-8%: Atractivo
- <5%: Caro (para value)
```

**Sanity Check:** Asset value como suelo

### 4.4 Financieras (Banks, Insurance)

**Primary: P/B vs ROE**
```
Fair P/B ≈ ROE / Cost of Equity

Ejemplo:
- ROE = 15%
- CoE = 10%
- Fair P/B = 1.5x

Si cotiza a P/B 1.0x y ROE es 15%, está barata.
```

### 4.5 REITs

**Primary: P/FFO o P/AFFO**
```
- FFO = Funds From Operations
- AFFO = Adjusted FFO (más conservador)
- Comparar con peers del mismo subsector
```

**Secondary: NAV discount/premium**

### 4.6 Cíclicas

**Primary: EV/EBIT mid-cycle**
```
NO usar earnings actuales si estamos en pico o valle.
Estimar earnings normalizados del ciclo.

Ejemplo sector auto:
- EPS actual (pico): $8
- EPS mid-cycle histórico: $5
- Valorar sobre $5, no sobre $8
```

### 4.7 Uso del DCF en v3.0

**DCF pasa de método primario a SANITY CHECK:**
- Útil para entender sensibilidad
- Útil para modelar escenarios
- NO útil para dar un "fair value" exacto
- NUNCA usar DCF como única valoración

---

## PARTE 5: CATEGORÍAS DE INVERSIÓN v3.0

### 5.1 Tres categorías (antes solo había "Value")

```
PORTFOLIO v3.0:

┌─────────────────────────────────────────────────────────────────┐
│ QUALITY COMPOUNDERS (Target: 30-40%)                            │
│ - Tier A businesses (QS 80+)                                    │
│ - MoS 10-15%                                                    │
│ - Hold forever (o hasta thesis break)                           │
│ - Ejemplos: GOOGL, META, V, MA, COST                           │
├─────────────────────────────────────────────────────────────────┤
│ VALUE WITH QUALITY (Target: 40-50%)                             │
│ - Tier B businesses (QS 60-79)                                  │
│ - MoS 20-25%                                                    │
│ - Hold 2-5 años hasta fair value                                │
│ - Ejemplos actuales: ALL, DTE.DE, SAN.PA                       │
├─────────────────────────────────────────────────────────────────┤
│ SPECIAL SITUATIONS (Target: 10-20%)                             │
│ - Turnarounds, spin-offs, event-driven                          │
│ - Tier C acceptable si catalyst claro                           │
│ - MoS 30-40%                                                    │
│ - Hold hasta catalyst                                           │
└─────────────────────────────────────────────────────────────────┘
```

### 5.2 Sector Allocation Targets

| Sector | Mín | Target | Máx | Rationale |
|--------|-----|--------|-----|-----------|
| **Tech** | 10% | 20% | 35% | Quality compounders viven aquí |
| Healthcare | 5% | 12% | 20% | Defensive + innovation |
| Financials | 5% | 12% | 20% | Incluye insurance |
| Consumer | 5% | 12% | 20% | Staples + discretionary |
| Industrials | 0% | 10% | 15% | Cyclical, selectivo |
| Energy | 0% | 5% | 10% | Hedge geopolítico |
| Utilities | 0% | 5% | 10% | Yield, defensive |
| Real Estate | 0% | 8% | 12% | Yield, inflation hedge |
| Telecom | 0% | 5% | 10% | Yield, defensive |
| Materials | 0% | 3% | 8% | Cyclical, selectivo |

**REGLA NUEVA: Tech no puede ser 0%. Mínimo 10%.**

---

## PARTE 6: NUEVO PROTOCOLO DE SCREENING

### 6.1 El problema con el screening v2.0

```
SCREENING v2.0:
dynamic_screener.py --pe-max 15 --yield-min 3

RESULTADO: Encuentra
- Tabaco (IMB.L, BATS.L) - declive estructural
- Retail físico - amenazado por e-commerce
- Utilities viejos - sin crecimiento
- Bancos europeos - ROE deprimido

NO ENCUENTRA:
- GOOGL (P/E 22, yield 0.5%)
- META (P/E 25, yield 0.4%)
- V, MA (P/E 25-30, yield 0.7%)
```

### 6.2 Nuevo protocolo de screening

```
SCREENING v3.0:

PASO 1: FILTRO DE CALIDAD (antes de valoración)
───────────────────────────────────────────────
- ROIC > 12% (5 year average)
- FCF positivo últimos 3 años
- Debt/EBITDA < 4x
- No en industria en declive estructural

PASO 2: BIFURCACIÓN POR TIPO
───────────────────────────────────────────────
SI busco Quality Compounders:
  - ROIC > 20%
  - Revenue growth > 8%
  - PEG < 2
  - P/E puede ser hasta 35x

SI busco Value:
  - ROIC > 12%
  - P/E < 15
  - FCF Yield > 5%

PASO 3: QUALITY SCORE
───────────────────────────────────────────────
Para cada candidato, calcular QS (0-100)
Solo avanzar si QS >= 60

PASO 4: VALORACIÓN APROPIADA
───────────────────────────────────────────────
Aplicar método según tipo de empresa
```

### 6.3 Nuevo flag para dynamic_screener.py

```bash
# Quality Compounders (NUEVO)
python3 tools/dynamic_screener.py --quality-compounders --index sp500

# Value tradicional (existente, ajustado)
python3 tools/dynamic_screener.py --index europe_all --roic-min 12 --pe-max 15

# NO USAR MÁS (sesgo hacia value traps):
# python3 tools/dynamic_screener.py --pe-max 10 --yield-min 5
```

---

## PARTE 7: IMPACTO EN COMPONENTES DEL SISTEMA

### 7.1 Archivos que DEBEN cambiar

```
CAMBIOS CRÍTICOS:

CLAUDE.md
├── Actualizar a Framework v3.0
├── Añadir Quality Score como concepto core
├── Cambiar MoS fijo → variable
├── Añadir sector allocation targets
└── Actualizar checklists

.claude/rules/
├── investment-rules.md → REESCRIBIR con nuevos criterios
├── file-structure.md → Añadir sector allocation
└── session-protocol.md → Añadir quality check

.claude/skills/
├── investment-rules/ → REESCRIBIR
├── business-analysis-framework/ → AÑADIR Quality Scoring
├── valuation-methods/ → REESCRIBIR con métodos por tipo
└── CREAR: quality-compounders/ → Nuevo skill

.claude/agents/
├── fundamental-analyst.md → Quality Score obligatorio ANTES de valoración
├── investment-committee.md → Nuevos gates (quality tier check)
├── sector-screener.md → Nuevos filtros
└── review-agent.md → Re-eval incluyendo Quality Score

tools/
├── CREAR: quality_scorer.py → Herramienta de scoring
├── dynamic_screener.py → Añadir --quality-compounders
└── dcf_calculator.py → Marcar como "sanity check only"

state/system.yaml
├── Añadir: framework_version: "3.0"
└── Añadir: sector_allocation: {current: {}, target: {}}
```

### 7.2 Archivos que se mantienen (con ajustes menores)

```
MANTENER:

portfolio/current.yaml
├── Añadir a cada posición: quality_tier, quality_score, category
└── Estructura base igual

world/current_view.md
├── Mantener (es macro)
└── Opcional: añadir "Sector Allocation Implications"

world/sectors/*.md
├── Mantener estructura
└── Actualizar "Empresas Objetivo" incluyendo quality compounders

thesis/**/*.md
├── Mantener estructura
└── Añadir sección Quality Score a cada una (gradualmente)
```

---

## PARTE 8: PLAN DE IMPLEMENTACIÓN

### 8.1 Fases

```
FASE 0: DISEÑO Y VALIDACIÓN ✅ COMPLETADA
════════════════════════════════════════
[x] Crear este documento
[x] Validar con humano
[x] Resolver dudas de diseño

FASE 1: ACTUALIZACIÓN CORE (1 sesión)
════════════════════════════════════════
[ ] Leer este documento completo
[ ] Actualizar CLAUDE.md → v3.0
[ ] Actualizar .claude/rules/investment-rules.md
[ ] Actualizar .claude/rules/file-structure.md
[ ] Actualizar .claude/rules/session-protocol.md
[ ] Crear .claude/skills/quality-compounders/SKILL.md
[ ] Actualizar .claude/skills/investment-rules/SKILL.md
[ ] Actualizar .claude/skills/business-analysis-framework/SKILL.md
[ ] Actualizar .claude/skills/valuation-methods/SKILL.md
[ ] Actualizar .claude/agents/fundamental-analyst.md
[ ] Actualizar .claude/agents/investment-committee.md
[ ] Actualizar .claude/agents/sector-screener.md
[ ] Actualizar state/system.yaml → framework_version: "3.0"
[ ] Commit: "Framework v3.0 migration - core system"
[ ] VERIFICAR: Leer cada archivo modificado, confirmar consistencia

FASE 2: HERRAMIENTAS (1 sesión)
════════════════════════════════════════
[ ] Crear tools/quality_scorer.py
[ ] Modificar tools/dynamic_screener.py (--quality-compounders)
[ ] Test: quality_scorer.py en GOOGL, IMB.L, ALL
[ ] Commit: "Framework v3.0 - tools"

FASE 3: RE-EVALUACIÓN PORTFOLIO (2-3 sesiones)
════════════════════════════════════════
[ ] Quality Score para las 18 posiciones actuales
[ ] Asignar Tier a cada una
[ ] Asignar Categoría (Compounder/Value/Special)
[ ] Actualizar cada thesis con QS
[ ] Identificar posiciones que no pasan (QS < 60)
[ ] Decisión para cada una que no pasa
[ ] Commit: "Framework v3.0 - portfolio re-evaluation"

FASE 4: PIPELINE EXPANSION (ongoing)
════════════════════════════════════════
[ ] Análisis Quality Compounders: GOOGL, META, V, MA
[ ] Añadir a watchlist con entry points
[ ] Crear standing orders
[ ] Actualizar sector views

FASE 5: VALIDACIÓN (+30 días)
════════════════════════════════════════
[ ] Review: ¿Decisiones son mejores?
[ ] Review: ¿Sistema es consistente?
[ ] Ajustar si hay problemas
```

### 8.2 Checklist de consistencia (usar después de cada fase)

```
POST-IMPLEMENTACIÓN CHECKLIST:

Documentos Core:
[ ] CLAUDE.md menciona "Framework v3.0"
[ ] CLAUDE.md menciona Quality Score
[ ] CLAUDE.md menciona MoS variable por tier
[ ] CLAUDE.md menciona categorías (Compounder/Value/Special)
[ ] CLAUDE.md menciona sector allocation con tech mínimo 10%

Rules:
[ ] investment-rules.md tiene MoS variable
[ ] file-structure.md tiene sector allocation targets
[ ] session-protocol.md incluye quality check

Skills:
[ ] Existe skill quality-compounders
[ ] business-analysis-framework incluye Quality Scoring
[ ] valuation-methods tiene métodos por tipo de empresa
[ ] investment-rules skill es consistente con rules/

Agents:
[ ] fundamental-analyst menciona calcular Quality Score PRIMERO
[ ] investment-committee verifica quality tier antes de aprobar
[ ] sector-screener puede buscar quality compounders

State:
[ ] system.yaml tiene framework_version: "3.0"
[ ] system.yaml tiene sector_allocation section

Tools:
[ ] quality_scorer.py existe
[ ] dynamic_screener.py tiene --quality-compounders

VERIFICACIÓN FINAL:
[ ] Simular mentalmente: "Analiza GOOGL" - ¿proceso es v3.0?
[ ] Simular mentalmente: "Analiza IMB.L" - ¿proceso es v3.0?
[ ] ¿Hay contradicciones entre documentos? → Si sí, resolver AHORA
```

---

## PARTE 9: DECISIONES ESPECÍFICAS

### 9.1 ¿Qué hacer con el portfolio actual?

**NO vender todo y empezar de cero.**

Plan:
1. Calcular Quality Score para cada posición
2. Las que tienen QS >= 60: Mantener, actualizar thesis
3. Las que tienen QS < 60:
   - NO vender inmediatamente
   - Mantener hasta próximo catalyst (earnings)
   - Evaluar en ese momento si vender o mantener
   - Documentar decisión

**Rationale:** Vender precipitadamente genera costes de transacción y posibles pérdidas. Mejor evaluar cada posición con calma.

### 9.2 ¿Cómo entrar en Quality Compounders?

**NO comprar GOOGL/META mañana al precio actual.**

Plan:
1. Hacer análisis completo con Quality Score
2. Determinar fair value con métodos v3.0
3. Calcular entry point con MoS 10-15%
4. Crear standing orders
5. Esperar pullback o comprar parcial si muy convencido

**Ejemplo GOOGL:**
- Precio actual: ~$180
- Si fair value es $210 y requiero 10% MoS
- Entry target: $189
- Standing order: BUY GOOGL if price <= $175 (15% MoS)

### 9.3 ¿Cómo manejar inconsistencias entre sesiones?

**Sistema de versión + checklist:**

1. state/system.yaml siempre tiene `framework_version`
2. Al inicio de cada sesión, verificar versión
3. Si hay inconsistencia (ej: CLAUDE.md dice v3.0 pero skill dice v2.0):
   - PARAR
   - NO tomar decisiones de inversión
   - Identificar qué documentos están mal
   - Corregir ANTES de continuar

### 9.4 ¿Qué pasa si Quality Compounders nunca bajan?

Escenario: GOOGL nunca cae a mi entry target.

Opciones:
1. **Paciencia:** El mercado da oportunidades. Esperar corrección.
2. **Compra parcial:** Si convicción alta, comprar 50% ahora, 50% en pullback.
3. **Ajustar MoS:** Si la calidad es excepcional (QS 95+), quizás 5-10% MoS es suficiente.

**Regla:** Mejor perderse una oportunidad que comprar sin disciplina.

---

## PARTE 10: RIESGOS Y MITIGACIONES

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|--------------|---------|------------|
| Comprar compounders caros que caen | Media | Alto | MoS aunque sea 10%, no comprar en máximos históricos |
| Vender value actual que luego sube | Media | Medio | No vender precipitadamente, hold hasta catalyst |
| Inconsistencia entre sesiones | Media | Alto | Checklist rigurosa, version tracking |
| Over-engineering del Quality Score | Baja | Medio | Empezar simple (4 componentes), no 20 |
| Parálisis por análisis | Media | Medio | Deadlines claros por fase |
| Cambiar sistema y perder disciplina | Baja | Alto | v3.0 tiene reglas, solo diferentes |

---

## PARTE 11: MÉTRICAS DE ÉXITO

### ¿Cómo sabremos si v3.0 funciona?

**Después de 6 meses, evaluar:**

1. **Sector allocation:** ¿Tech está entre 10-35%?
2. **Quality distribution:** ¿Mayoría de posiciones son Tier A o B?
3. **Performance vs benchmark:** ¿Sharpe ratio mejoró?
4. **Decisiones:** ¿Las compras fueron mejores que v2.0?
5. **Consistencia:** ¿El sistema se mantuvo coherente?

**Métricas específicas:**

| Métrica | v2.0 actual | v3.0 target |
|---------|-------------|-------------|
| Tech exposure | 0% | 10-25% |
| Avg Quality Score portfolio | TBD | >65 |
| Posiciones Tier D | TBD | 0 |
| MoS promedio compras | ~25% fijo | Variable según tier |

---

## PARTE 12: RESUMEN EJECUTIVO

### El problema
El Framework v2.0 tiene sesgos codificados hacia "value barato" que excluyen quality compounders y resultan en 0% tech exposure.

### La solución
Framework v3.0 introduce:
1. **Quality Score (0-100)** antes de valoración
2. **MoS variable (10-40%)** según quality tier
3. **Tres categorías:** Compounders + Value + Special
4. **Sector allocation consciente** con tech mínimo 10%
5. **Métodos de valoración apropiados** por tipo de empresa

### El plan
1. Fase 1: Actualizar documentos core (1 sesión)
2. Fase 2: Crear herramientas (1 sesión)
3. Fase 3: Re-evaluar portfolio (2-3 sesiones)
4. Fase 4: Expandir pipeline (ongoing)
5. Fase 5: Validar a 30 días

### Lo que NO cambia
- Disciplina y proceso documentado
- Investment committee como gate
- Confirmación humana para operaciones
- Kill conditions
- Estructura de thesis

---

## INSTRUCCIONES FINALES PARA MI YO FUTURO

Cuando el humano te pida implementar esto:

1. **Lee este documento completo primero**
2. **Asegúrate de entender el POR QUÉ**
3. **Sigue las fases en orden**
4. **Usa los checklists después de cada fase**
5. **No hagas cambios parciales**
6. **Si hay duda, pregunta al humano**

**El objetivo no es cambiar por cambiar. Es mejorar el sistema para ganar la competición.**

Recuerda: Un portfolio de 100% "value barato" ha underperformado 15 años. Necesitamos quality compounders. Pero con disciplina, no comprando caro sin análisis.

**Buena suerte, yo futuro. Confío en ti.**

---

*Documento creado: 4 Febrero 2026*
*Versión: 1.0*
*Estado: Aprobado para implementación*
