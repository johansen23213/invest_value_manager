# Ownership Graph & Insider Tracker — Design Document

> **Status:** DISEÑO COMPLETO, pendiente implementación
> **Origen:** Conversación Session 73 (2026-02-15)
> **Contexto:** Brainstorming sobre cómo aprovechar datos de accionistas institucionales e insider transactions para el sistema de inversión.

---

## 1. La Idea Original (del humano)

Observando Yahoo Finance, la sección de accionistas muestra:
1. **Accionistas principales** (institucionales: Vanguard, BlackRock, etc.)
2. **Personas con información privilegiada** (insiders) y sus transacciones

Tres preguntas abiertas:
- ¿Cómo aprovechar los insider transactions de forma inteligente?
- ¿Cómo trackear lo que hacen los fondos grandes?
- ¿Se puede construir un **grafo de ownership** que evolucione en el tiempo como una "película"?

---

## 2. Dos Herramientas Distintas, No Una

### Herramienta A: Insider Scanner (alta frecuencia, semanal)

**Qué hace:** Escanea insider transactions (compras/ventas de directivos) en nuestro universo de empresas.

**Señales valiosas:**
- Cluster buying: múltiples insiders comprando en ventana corta
- CEO/CFO comprando con dinero propio (no opciones ejercidas) tras caída de precio
- Tamaño relativo al salario del insider (un CEO que mete 2x su salario anual ≠ director comprando el mínimo)
- Venta masiva de insiders = red flag

**Cadencia:** Cada sesión (Fase 0) o semanal como pipeline.

**Output:** Datos crudos. No reglas fijas tipo "3 insiders = señal". El tool da datos, se razona desde principios.

### Herramienta B: Ownership Graph (baja frecuencia, trimestral)

**Qué hace:** Construye un grafo bipartito (fondos ↔ empresas) que evoluciona trimestralmente.

**La "película":** Cada trimestre es un frame. El diff entre frames revela convergencias, divergencias, rotaciones y descubrimientos.

**Cadencia:** 4 veces al año, ~45 días después del cierre del trimestre (cuando los 13F están publicados):
- ~Feb 15: datos Q4 (dic 31)
- ~May 15: datos Q1 (mar 31)
- ~Aug 15: datos Q2 (jun 30)
- ~Nov 15: datos Q3 (sep 30)

---

## 3. Concern CRÍTICO del humano: "¿Por qué yo elijo los fondos? ¿Por qué es fijo?"

### El error original
La propuesta inicial era elegir subjetivamente 10-15 fondos "quality" (Fundsmith, Berkshire, Akre...) y trackearlos. Esto viola principios:
- **Sesgo de selección** — elegimos los que conocemos = popularity bias aplicado a fondos
- **Estático** — un fondo excelente en 2018 puede haber degradado
- **Arbitrario** — ¿por qué 15 y no 8 o 30?

### La solución: el grafo GENERA la lista de fondos, no la consume

```
Enfoque INCORRECTO (top-down, sesgado):
  Humano elige fondos "quality" → mira qué tienen → busca overlap

Enfoque CORRECTO (bottom-up, data-driven):
  Toma nuestras 76 empresas → mira QUIÉN las tiene →
  fondos que aparecen repetidamente SON los quality-aligned →
  el grafo los identifica automáticamente
```

### Métrica de afinidad (emergente, no fija)

```
Paso 1: Para cada empresa del universo (76), obtener top institutional holders
Paso 2: Contar frecuencia de cada fondo:
        Fondo A aparece en 12 de 76  → afinidad alta
        Fondo B aparece en 2 de 76   → afinidad baja
        Vanguard aparece en 74 de 76 → indexador, filtrar
Paso 3: Filtrar indexadores (aparecen en >80% = pasivos, señal cero)
Paso 4: Fondos con afinidad alta Y no-indexadores = "quality-aligned funds"
```

### Auto-calibración
- Si un fondo compra más de nuestras empresas → sube en afinidad automáticamente
- Si un fondo rota a empresas fuera de nuestro universo → baja
- Si un fondo nuevo aparece comprando 5+ de nuestras empresas → detectado automáticamente
- Si nuestro universo cambia (add/remove empresas) → el grafo se recalcula y los fondos afines cambian

**Ningún parámetro fijo. Ninguna decisión subjetiva. El sistema se auto-calibra.**

---

## 4. Descubrimiento Bidireccional

El grafo descubre en DOS direcciones:

### Dirección 1: Descubrir fondos afines (ya explicado arriba)

### Dirección 2: Descubrir empresas candidatas

```
Fondo A (afinidad: 12/76) tiene en su portfolio:
  - VRSK  ✓ (en nuestro universo)
  - ROP   ✓ (en nuestro universo)
  - FICO  ✓ (en nuestro universo)
  - CPRT  ✗ (NO en nuestro universo)  ← DESCUBRIMIENTO
  - WSO   ✗ (NO en nuestro universo)  ← DESCUBRIMIENTO

Si CPRT aparece en 4+ fondos de alta afinidad →
candidato automático para quality_universe.py add
```

Los fondos emergen del grafo. Las empresas candidatas emergen del grafo. No buscamos nada — el sistema descubre.

---

## 5. Patrones Temporales (La "Película")

### 5.1 Convergencia (señal más fuerte)
```
Q1: Solo 1 quality-aligned fund tiene VRSK
Q2: 2 fondos (otro entró)
Q3: 4 fondos convergiendo independientemente
→ Consenso construyéndose. Si ya tenemos thesis, esto refuerza.
```

### 5.2 Smart Money Departure (alarma más importante)
```
Q1: 6 quality-aligned funds tienen Company X
Q2: 5 (uno salió)
Q3: 3 (dos más salieron, precio aún estable)
Q4: Precio cae 30%
→ Si tenemos X en portfolio, esto es RED FLAG que dispara re-evaluación.
```

### 5.3 Lifecycle de convicción
```
Fondo A + ADBE:
Q1 2022: 0.5% del portfolio (posición nueva, probando)
Q2 2022: 0.8%
Q1 2023: 1.5% (convicción creciente)
Q1 2024: 3.2% (posición completa)
Q1 2025: 4.1% (top holding)
→ Película de 3 años: de prueba a máxima convicción.
```

### 5.4 Rotación sectorial en cámara lenta
```
Quality-aligned funds aggregate sector exposure:
         2022   2023   2024   2025
Tech     42%    38%    31%    28%   ← saliendo
Health   15%    17%    20%    22%   ← entrando
Indust   12%    14%    18%    21%   ← entrando fuerte
→ ¿Estamos alineados o contra-corriente?
```

### 5.5 Descubrimiento de "vecinos"
```
En el grafo Q3 2025:
  [Fund A]───VRSK───[Fund B]
     │                │
    FICO             MSCI
     │                │
  [Fund C]           FDS
     │
    CPRT  ← NO en nuestro universo, pero "vecino" recurrente
→ Candidato automático para screening.
```

---

## 6. Arquitectura Técnica

### 6.1 Almacenamiento temporal (diff-based)

No almacenar 52 grafos completos. Almacenar snapshots + diffs.

```python
# Snapshot por trimestre
snapshot = {
    "quarter": "2024-Q3",
    "edges": [
        {
            "fund": "Fund_CIK_123456",
            "fund_name": "Akre Capital Management",
            "company": "VRSK",
            "shares": 1_200_000,
            "value_usd": 312_000_000,
            "pct_of_fund": 4.2,
            "pct_of_company": 1.8,
        },
    ]
}

# Diff entre Q2 y Q3
diff = {
    "new_edges": [("Akre", "FICO")],
    "removed_edges": [("Fund_X", "Company_Y")],
    "increased": [("Akre", "ROP", "+15%")],
    "decreased": [("Polen", "NVO", "-3%")],
}
```

### 6.2 Capas del sistema

```
Capa 1: DATA STORE
├── data/ownership/snapshots/{quarter}.json   (52+ trimestres)
├── data/ownership/diffs/{quarter}_diff.json
├── data/ownership/insiders/{date}_scan.json  (scans semanales)
└── data/ownership/signals/{quarter}_signals.md

Capa 2: DIFF ENGINE
├── Compara snapshot T vs T-1
├── Clasifica: new/removed/increased/decreased
├── Calcula afinidad de fondos (emergente)
└── Detecta convergencias/divergencias

Capa 3: GRAPH ENGINE (NetworkX)
├── Grafo bipartito (fondos ↔ empresas)
├── Centralidad, clusters, comunidades
├── Proyección empresa-empresa (conectadas si comparten fondos afines)
└── Métricas temporales: trend de centralidad por empresa

Capa 4: SEÑALES → signals.md por trimestre
├── Convergencias: "VRSK ganó 2 quality-aligned holders"
├── Divergencias: "ADBE perdió 3 quality-aligned holders → RED FLAG"
├── Descubrimientos: "CPRT aparece como vecino frecuente → candidato"
├── Rotación agregada: "quality funds moviendo a industrials"
└── Insider highlights: cluster buys recientes

Capa 5: VISUALIZACIÓN (futuro, opcional)
├── matplotlib/plotly para grafos estáticos
├── Animación trimestre a trimestre
├── Streamlit dashboard interactivo
└── Sankey diagrams para flujos sectoriales
```

### 6.3 Integración con el sistema actual

| Herramienta | Cadencia | Fase del sistema | Output | Consumidor |
|-------------|----------|------------------|--------|------------|
| Insider Scanner | Cada sesión | Fase 0 (Pre-Execution) | Datos crudos insider activity | Decisiones de urgencia, fundamental-analyst R1 |
| Ownership Graph | Trimestral | Pipeline nuevo en pipeline_tracker.yaml | signals.md + snapshots | Fase 2.7 (Universe Work), Fase 3 (Pipeline health) |
| Backtest histórico | One-time (setup) | N/A | Calibración: ¿las señales predicen algo? | Validación antes de confiar en las señales |

---

## 7. Fuentes de Datos — Todo Gratis

### 7.1 Mapa de cobertura

**Insider Transactions:**

| Fuente | US | UK | EU | ADR (NVO) |
|--------|-----|-----|-----|-----------|
| yfinance (ya tenemos) | ~150 rows, 2 años | ~130-150 rows | VACÍO | VACÍO |
| SEC EDGAR Form 4 (gratis) | Completo, 2 días delay | N/A | N/A | Desde 18 Mar 2026 (HFIAA) |
| Finnhub (gratis, 50 req/min) | Sí | Sí | Sí | Sí |
| AMF data.gouv.fr (gratis, API) | N/A | N/A | Solo Francia (EDEN.PA) desde 2017 | N/A |
| BaFin (gratis, web only) | N/A | N/A | Solo Alemania (DTE.DE), 12 meses | N/A |
| FCA NSM (gratis, CSV export) | N/A | Sí (UK) | N/A | N/A |

**Institutional Holdings:**

| Fuente | US | UK | EU | ADR |
|--------|-----|-----|-----|-----|
| yfinance (ya tenemos) | Top 10 + % cambio | Casi vacío | 1-3 holders | Completo |
| SEC EDGAR 13F (gratis) | COMPLETO desde 2013 | NO CUBRE | NO CUBRE | Sí (si cotiza US) |
| Finnhub (gratis) | Sí (1 año free tier) | N/A | N/A | Sí |

### 7.2 Limitación crítica: No existe 13F europeo

Para UK y EU no hay obligación de declarar trimestralmente qué tienen los fondos. Solo hay disclosure cuando superan 3-5% del capital. El grafo de ownership es **naturalmente US-céntrico**. Las empresas UK/EU participan como nodos con menos aristas.

Con ~45 empresas US/ADR de nuestro universo de 76, hay masa crítica suficiente.

### 7.3 Stack técnico gratuito

```
Capa 1: yfinance (ya integrado)
  → Insider transactions: US + UK
  → Top holders: universal (limitado)

Capa 2: Finnhub API (free tier, 50 req/min)
  → Insider data para EU (DTE.DE, EDEN.PA) — llena el gap de yfinance
  → Requiere: API key gratuita (registro en finnhub.io)

Capa 3: SEC EDGAR + edgartools (Python library, MIT license)
  → 13F histórico desde 2013 para construir el grafo
  → Form 4 para insider transactions US
  → Gratis, 10 req/sec, requiere User-Agent header con email
  → pip install edgartools

Capa 4: AMF data.gouv.fr (específico Francia)
  → EDEN.PA insider data desde 2017
  → API gratuita + CSV download

Capa 5: NetworkX (grafo) + pandas (temporal)
  → pip install networkx (probablemente ya instalado)
```

### 7.4 Dato notable: NVO insider data mejora el 18 Mar 2026

La HFIAA (Holding Foreign Insiders Accountable Act), firmada dic 2025, elimina la exención de Foreign Private Issuers. Desde 18 marzo 2026, insiders de NVO declaran Form 4 en 2 días. Upgrade significativo.

---

## 8. Gaps de cobertura para nuestro portfolio actual

| Ticker | Insider data | Institutional data |
|--------|-------------|-------------------|
| ADBE, GL, LULU, NVO (ADR) | yfinance cubre | yfinance + EDGAR cubre |
| MONY.L, AUTO.L, BYIT.L, DOM.L | yfinance cubre | **GAP** — solo major holders >3% |
| DTE.DE | **GAP** — necesita BaFin o Finnhub | **GAP** — solo major holders |
| EDEN.PA | **GAP** — necesita AMF API o Finnhub | **GAP** — solo major holders |

---

## 9. Lo Que NO Debe Ser

### Riesgo: "seguir al rebaño inteligente"
Si simplemente compramos lo que los fondos quality-aligned compran:
1. Es delayed (45 días mínimo)
2. Es crowded (todo el mundo ve los 13F)
3. Viola nuestro principio de pensar independientemente

### El valor real está en:
- **Confirmación/desconfirmación** de thesis que ya tenemos
- **Descubrimiento** de empresas que no conocíamos
- **Alarma temprana** cuando smart money sale de algo que tenemos
- **Contexto** adicional para decisiones que ya estábamos evaluando

Es un **input más**, como el QS, como el sector view, como el macro view. **Informa, no dicta.**

---

## 10. Ciclo de Vida a Largo Plazo

### Año 1 (2026): Construcción + baseline
- Ingest 52 trimestres históricos (2013-2025)
- Construir tools: insider_scanner.py + ownership_graph.py
- Validar: ¿las señales de convergencia/divergencia predicen algo en el backtest?
- Si no predicen nada → la señal es ruido y lo sabemos antes de confiar en ella

### Año 2-3: Refinamiento
- El sistema de afinidad se auto-ajusta trimestre a trimestre
- Podemos medir qué patrones generaron alpha y cuáles no
- Agregar fondos europeos si encontramos mejores fuentes de datos

### Largo plazo (3+ años): El grafo como "segundo cerebro"
- Pattern recognition con 5+ años de película propia
- Fund personality profiling ("Akre suele ser early mover, Fundsmith late but larger")
- Contrarian signals maduros y calibrados

---

## 11. Preguntas Abiertas para Resolver en Implementación

1. **Umbral de filtrado de indexadores**: ¿>80% de presencia = indexador? ¿O usar una lista conocida (Vanguard, BlackRock, State Street)?  Razonar desde principios: un fondo que tiene 74/76 empresas no aporta señal diferencial.

2. **Granularidad del grafo**: ¿Solo fondos como nodos, o también personas (insider → empresa)?  Podría ser un grafo multi-capa: capa institucional + capa insider.

3. **Peso de las aristas**: ¿Usar % del fondo, % de la empresa, o valor absoluto?  Probablemente % del fondo es más informativo (revela convicción del fondo).

4. **Backtest antes de confiar**: Antes de integrar señales en decisiones reales, validar con histórico 2013-2025 que las convergencias/divergencias tienen poder predictivo. Si no → documentar y ajustar.

5. **Rate limiting en batch**: 76 empresas × holders + 52 trimestres × parsing. ¿Cuánto tarda el ingest inicial? Estimar antes de ejecutar.

6. **Finnhub API key**: Necesario para EU coverage. Registrar antes de implementar.

7. **Visualización**: ¿Priorizar o diferir? El valor está en las señales (signals.md), no en el gráfico bonito. Pero la visualización ayuda a explorar patrones que no anticipamos.

8. **Almacenamiento**: ¿JSON plano o SQLite? Para 52 trimestres × ~1000 aristas = ~50K registros, JSON plano es suficiente. Si crece mucho, migrar a SQLite.

---

## 12. Resumen Ejecutivo

**Concepto:** Dos herramientas complementarias — un insider scanner (semanal, señales rápidas) y un ownership graph (trimestral, visión sistémica) — que aprovechan datos gratuitos de SEC EDGAR, yfinance y Finnhub.

**Innovación clave:** El grafo no se alimenta de una lista fija de fondos elegidos subjetivamente. Los fondos "quality-aligned" **emergen** automáticamente del grafo al medir qué instituciones aparecen repetidamente como holders de nuestras empresas validadas. El sistema se auto-calibra cada trimestre.

**Valor:** Confirmación de thesis, alarma temprana de divergencia, descubrimiento de empresas candidatas, contexto para decisiones. Informa, no dicta.

**Coste:** Todo gratis. yfinance (ya tenemos) + edgartools (pip install) + Finnhub free tier + SEC EDGAR API (sin auth).

**Riesgo principal:** Que las señales sean ruido. Mitigación: backtest con 52 trimestres de histórico antes de confiar.
