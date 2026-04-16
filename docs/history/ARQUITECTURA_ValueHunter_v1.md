# ValueHunter — Arquitectura Multi-Agente v1.0
*Rediseño desde cero · Estilo Alpha Vulture · Special Situations + Small Caps globales*

---

## Visión General

Sistema de 4 capas con 10 agentes especializados que cubre el ciclo completo:
**Screening → Análisis → Decisión → Gestión de cartera**

```
┌─────────────────────────────────────────────────────────────┐
│                    CAPA 0 — ORCHESTRATOR                    │
│              (Gobernador / Meta-agente central)             │
└──────────────────────────┬──────────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
┌───────────────┐  ┌───────────────┐  ┌───────────────┐
│  CAPA 1       │  │  CAPA 2       │  │  CAPA 3       │
│  SCREENING    │  │  ANÁLISIS     │  │  PORTFOLIO    │
│  (2 agentes)  │  │  (5 agentes)  │  │  (2 agentes)  │
└───────────────┘  └───────────────┘  └───────────────┘
        │                  │                  │
        └──────────────────▼──────────────────┘
                  ┌────────────────┐
                  │  CAPA 4        │
                  │  MEMORIA /     │
                  │  KNOWLEDGE BASE│
                  └────────────────┘
```

---

## CAPA 0 — ORCHESTRATOR (Gobernador)

**Rol:** Cerebro central. Recibe inputs, decide qué agentes activar, en qué orden, con qué contexto. Mantiene el estado global del sistema.

**Responsabilidades:**
- Recibir triggers (nuevo ticker, alerta precio, ciclo semanal, etc.)
- Decidir el flujo: ¿screening rápido o análisis profundo?
- Agregar outputs de agentes hijos en decisión final
- Mantener coherencia entre capas
- Gestionar costes de llamadas API (paralelizar vs. secuenciar)

**Patrón de ejecución:**
- Paralelo en Capa 1 (screening)
- Secuencial + paralelo en Capa 2 (análisis)
- Secuencial en Capa 3 (portfolio, necesita contexto completo)

---

## CAPA 1 — SCREENING (2 Agentes)

### Agente 1.1 — SCREENER CUANTITATIVO
**Input:** Universo de acciones (filtro por market cap, volumen, exchanges)
**Output:** Lista priorizada de candidatos con score 0–100

Criterios de scoring:
- P/E, P/B, EV/EBITDA vs. sector
- Net cash > 0 (especialmente para biotechs / special sits)
- Insider ownership > 10%
- Market cap < 500M USD (small cap zone)
- Volumen mínimo para entrada/salida viable
- Momentum negativo reciente (oportunidad contrarian)

Fuentes de datos: Yahoo Finance API, SEC EDGAR (XBRL), Finviz

### Agente 1.2 — SCREENER SPECIAL SITUATIONS
**Input:** Feeds de noticias corporativas, SEC filings, press releases
**Output:** Lista de eventos especiales detectados con tipo y prioridad

Eventos monitorizados:
- Merger / acquisition announced → merger arbitrage spread
- Strategic review / exploring alternatives → posible liquidación
- Bankruptcy filing → reorganización o liquidación
- Spin-off announced → stub valuation
- Odd-lot tender offer → arbitraje pequeño
- Cash shell / busted biotech → net cash discount
- Share buyback > 10% float

Fuentes: SEC EDGAR RSS, Bloomberg RSS, PR Newswire, Globe Newswire

---

## CAPA 2 — ANÁLISIS EN PROFUNDIDAD (5 Agentes)

*Se activan en paralelo sobre el candidato seleccionado por Capa 1*

### Agente 2.1 — ANALISTA FINANCIERO
**Misión:** Valuar la empresa desde múltiples ángulos

Tareas:
- Construir modelo DCF simplificado (3 escenarios: base, bull, bear)
- Calcular NAV (Net Asset Value) para holding companies / REITs
- Estimar Net Cash neto de deuda y liabilities
- Analizar evolución márgenes y ROIC últimos 5 años
- Detectar red flags contables (accruals, inventario, goodwill)
- Calcular margen de seguridad vs. precio actual

Output: Valoración en 3 rangos + señales de alerta contable

### Agente 2.2 — ANALISTA DE SITUACIÓN ESPECIAL
**Misión:** Si aplica, modelar el evento corporativo específico

Tareas por tipo de evento:
- **Merger arbitrage:** calcular spread, probabilidad de cierre, date esperada, riesgo regulatorio, break fee
- **Liquidación:** estimar cash distribuible, timeline, haircuts en activos ilíquidos
- **Spin-off:** valorar stub, analizar motivaciones del management, historial del sector
- **Biotech cash shell:** ajustar por burn rate, CVRs, reverse merger probabilidad
- **Odd-lot:** calcular rentabilidad neta de comisiones

Output: Modelo de evento + expected value + distribución de probabilidades

### Agente 2.3 — ANALISTA DE NEGOCIO (CUALITATIVO)
**Misión:** Entender el negocio subyacente y su moat

Tareas:
- Describir modelo de negocio en 5 líneas
- Identificar ventajas competitivas (o ausencia de ellas)
- Analizar posición competitiva en el sector
- Evaluar calidad del management (track record, skin in the game, capital allocation)
- Identificar catalizadores futuros (corto y largo plazo)
- Detectar riesgos cualitativos (disruption, regulación, concentración cliente)

Output: Thesis narrative + lista de bull/bear cases + rating management 1-5

### Agente 2.4 — ANALISTA DE RIESGO
**Misión:** Cuantificar y calificar todos los riesgos

Tareas:
- Riesgo de posición sizing (liquidez, bid-ask spread)
- Riesgo de tesis (¿qué tiene que ir mal para perder > 30%?)
- Riesgo de ejecución (para events: timing, contraparte)
- Riesgo macro relevante (tipo de cambio si es posición en USD/GBP/etc.)
- Riesgo regulatorio / legal (litigios pendientes, FDA approvals)
- Maximum drawdown estimado en scenario adverso

Output: Risk score 1-10 + tabla de riesgos priorizados + stop-loss recomendado

### Agente 2.5 — INVESTIGADOR DE CONTEXTO (WEB SEARCH)
**Misión:** Recopilar información reciente no disponible en datos estructurados

Tareas:
- Buscar últimas noticias sobre la empresa y sus competidores
- Revisar últimas conferencias earnings / transcripts
- Detectar comentarios de otros inversores value conocidos (13F filings)
- Buscar análisis de Alpha Vulture, Seeking Alpha, blogs especializados
- Revisar threads de Twitter/X de inversores relevantes
- Buscar litigios, demandas, investigaciones regulatorias recientes

Output: Resumen de contexto reciente + fuentes + alertas detectadas

---

## CAPA 3 — GESTIÓN DE PORTFOLIO (2 Agentes)

### Agente 3.1 — DECISION MAKER
**Misión:** Integrar todos los outputs de Capa 2 y emitir recomendación

Input: Outputs estructurados de los 5 agentes de análisis
Proceso:
1. Calcular Investment Score compuesto (0–100)
2. Comparar con posiciones actuales de cartera (correlación, concentración)
3. Verificar criterios mínimos: margen seguridad > 30%, risk score < 7, tesis clara
4. Emitir una de 5 decisiones: BUY / WATCH / PASS / SELL / ADD

Output estructurado:
```json
{
  "ticker": "XXXX",
  "decision": "BUY",
  "conviction": 7.2,
  "target_price": 14.50,
  "stop_loss": 8.20,
  "position_size_pct": 4.5,
  "thesis_summary": "...",
  "key_risks": ["...", "..."],
  "catalyst_expected": "Q3 2026",
  "review_trigger": "Merger close / earnings miss"
}
```

### Agente 3.2 — PORTFOLIO MONITOR
**Misión:** Vigilancia continua de posiciones abiertas

Tareas periódicas (diario/semanal):
- Monitorizar precio vs. tesis (¿se está cumpliendo?)
- Alertar si precio cae > X% sin razón fundamental
- Trackear progreso de eventos especiales (merger timeline, liquidación updates)
- Calcular rentabilidad real por posición (€, %, anualizado)
- Detectar cambios en fundamentales (nuevos filings, profit warnings)
- Proponer revisión de tesis al Orchestrator si detecta anomalías

Output: Dashboard de cartera + alertas + propuestas de revisión

---

## CAPA 4 — KNOWLEDGE BASE (Memoria Persistente)

Estructura de datos:

```
/knowledge_base
  /companies
    /{ticker}
      - fundamentals.json       # datos financieros históricos
      - thesis.md               # tesis de inversión documentada
      - analysis_history.json   # historial de análisis con fechas
      - decisions.json          # decisiones tomadas y resultado
  /portfolio
    - current_positions.json    # posiciones activas
    - closed_positions.json     # historial cerrado con P&L
    - performance.json          # métricas globales de cartera
  /learning
    - successful_patterns.md    # qué funcionó y por qué
    - failed_patterns.md        # errores documentados
    - market_regimes.json       # contexto macro en cada decisión
  /universe
    - watchlist.json            # candidatos en seguimiento
    - screener_results.json     # últimos resultados de screening
```

---

## Stack Tecnológico Recomendado

| Componente | Tecnología |
|---|---|
| Agentes | Python + Anthropic SDK (claude-sonnet-4-6) |
| Orquestación | LangGraph o custom orchestrator en Python |
| Datos financieros | yfinance (gratuito) + SEC EDGAR API (gratuito) |
| Noticias / events | RSS feeds SEC + NewsAPI |
| Base de conocimiento | Archivos Markdown + JSON (compatible con Claude Code) |
| Scheduler | APScheduler o cron jobs |
| Dashboard | Streamlit (rápido) o React (si se quiere interfaz rica) |
| Broker integration | Interactive Brokers API (ibkr_web_api) |
| Repositorio | GitHub (evolución del invest_value_manager existente) |

---

## Flujos de Ejecución

### Flujo 1: Screening Semanal (automático)
```
Cron trigger (cada domingo)
  → Orchestrator activa Screener Cuantitativo + Screener Special Situations en paralelo
  → Outputs se consolidan en watchlist priorizada
  → Top 5 candidatos pasan a análisis profundo automático
  → Decision Maker emite recomendaciones preliminares
  → Notificación a Joan con resumen ejecutivo
```

### Flujo 2: Análisis bajo demanda
```
Joan introduce ticker manualmente
  → Orchestrator detecta tipo (ordinary value vs. special situation)
  → Activa los 5 agentes de análisis en paralelo
  → Decision Maker integra y emite decisión
  → Resultado guardado en Knowledge Base
```

### Flujo 3: Monitorización diaria (automático)
```
Cron trigger (cada día hábil, 18:00)
  → Portfolio Monitor revisa todas las posiciones abiertas
  → Detecta alertas de precio, noticias, filings nuevos
  → Si hay alerta crítica: notificación inmediata
  → Si hay cambio de tesis: propone revisión al Orchestrator
```

---

## Métricas de Evaluación del Sistema

- **Hit rate:** % de decisiones BUY que superan benchmark a 12 meses
- **Average return per position:** rentabilidad media de posiciones cerradas
- **Thesis accuracy:** % de catalizadores que se cumplen según timeline estimado
- **Special situations alpha:** diferencia de rendimiento entre bucket events y bucket value puro
- **Screening recall:** % de oportunidades relevantes que el screener captura

---

## Roadmap de Implementación

### Sprint 1 (2 semanas): Fundamentos
- [ ] Diseñar estructura de Knowledge Base y schemas JSON
- [ ] Implementar Screener Cuantitativo básico (yfinance + filtros)
- [ ] Implementar Screener Special Situations (SEC EDGAR RSS)
- [ ] Crear Orchestrator básico (secuencial, sin paralelismo aún)

### Sprint 2 (2 semanas): Agentes de Análisis
- [ ] Agente 2.1 Financiero (DCF simplificado + net cash)
- [ ] Agente 2.3 Negocio (cualitativo con web search)
- [ ] Agente 2.5 Investigador web (Anthropic web search tool)
- [ ] Integrar en Orchestrator

### Sprint 3 (2 semanas): Decisión y Portfolio
- [ ] Agente 2.2 Special Situations (merger arbitrage model)
- [ ] Agente 2.4 Riesgo
- [ ] Agente 3.1 Decision Maker (scoring compuesto)
- [ ] Agente 3.2 Portfolio Monitor (alertas básicas)

### Sprint 4 (1 semana): Dashboard y automatización
- [ ] Dashboard Streamlit con métricas de cartera
- [ ] Scheduler para flujos automáticos
- [ ] Notificaciones (email o Telegram)
- [ ] Testing end-to-end con 3 casos reales históricos

---

*ValueHunter v1.0 — Joan & Angel — Abril 2026*
