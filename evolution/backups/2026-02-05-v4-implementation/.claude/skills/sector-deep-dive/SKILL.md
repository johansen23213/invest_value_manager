---
name: sector-deep-dive
description: Framework for deep sector analysis before investing. TAM, trends, competition, disruption, sentiment.
user-invocable: false
---

# Sector Deep Dive Framework

## Cuándo Usar
- ANTES de primera inversión en un sector nuevo
- Cuando world/sectors/[sector].md no existe o está >30 días stale
- Cuando fundamental-analyst lo requiere para Gate 8

## Output Location
`world/sectors/[sector_name].md`

---

## FRAMEWORK DE ANÁLISIS SECTORIAL

### 1. DEFINICIÓN DEL SECTOR
```
Sector: [nombre]
Sub-sectores: [lista]
Empresas principales: [top 5-10 por market cap]
Empresas en nuestro portfolio/watchlist: [tickers]
```

### 2. TAM Y CRECIMIENTO
```
TAM Global: $[X]B (fuente, año)
TAM Europa: $[X]B
TAM US: $[X]B
CAGR histórico (5y): [X]%
CAGR proyectado (5y): [X]% (fuente)

Drivers de crecimiento:
- [driver 1]
- [driver 2]

Frenos al crecimiento:
- [freno 1]
- [freno 2]
```

### 3. ESTRUCTURA COMPETITIVA
```
Concentración: [fragmentado/oligopolio/monopolio]
Top 5 market share: [X]%
Barreras de entrada: [altas/medias/bajas]
  - [barrera 1]
  - [barrera 2]

Poder de pricing: [alto/medio/bajo]
Poder de proveedores: [alto/medio/bajo]
Poder de clientes: [alto/medio/bajo]
```

### 4. CICLO Y SENSIBILIDAD
```
Tipo: [cíclico/defensivo/growth]
Sensibilidad a tipos de interés: [alta/media/baja]
Sensibilidad a recesión: [alta/media/baja]
Mejor fase del ciclo: [early/mid/late/all]

Beta típico del sector: [X]
```

### 5. DISRUPCIÓN Y RIESGOS
```
Amenazas tecnológicas:
- AI: [impacto esperado]
- Digitalización: [impacto]
- Otras tecnologías: [cuáles]

Amenazas regulatorias:
- [regulación 1]: [probabilidad] [impacto]
- [regulación 2]

Amenazas competitivas:
- Nuevos entrantes: [quiénes]
- Sustitutos: [cuáles]

Riesgo geopolítico: [alto/medio/bajo]
- Exposición China: [X]%
- Exposición supply chain: [descripción]
```

### 6. SENTIMIENTO DE MERCADO
```
Sentimiento actual: [odiado/ignorado/neutral/querido/burbuja]
P/E histórico del sector: [X]x
P/E actual: [X]x
Premium/Discount vs historia: [X]%

Flujos de fondos (últimos 12m): [inflows/outflows]
Cobertura de analistas: [alta/media/baja]
Narrativa dominante: "[la historia que cuenta el mercado]"
```

### 7. TESIS SECTORIAL
```
¿El sector está barato? [SI/NO] - ¿Por qué?
¿La narrativa del mercado es correcta? [SI/NO] - ¿Por qué?
¿Hay catalizadores? [lista]
¿Hay riesgos no apreciados? [lista]

Mi posición sobre el sector:
[ ] SOBREPONDERAR - El mercado está equivocado negativamente
[ ] NEUTRAL - Precio justo, seleccionar empresas específicas
[ ] INFRAPONDERAR - El mercado subestima riesgos
[ ] EVITAR - Problemas estructurales

Horizonte temporal para tesis: [X] meses/años
```

### 8. EMPRESAS RECOMENDADAS
```
Para análisis profundo (cumple criterios):
1. [Ticker] - [razón breve]
2. [Ticker] - [razón breve]

Evitar:
1. [Ticker] - [razón breve]
```

---

## FUENTES OBLIGATORIAS
- Industry reports (Mordor Intelligence, Grand View Research, etc.)
- Trade associations
- Company investor presentations (top 3 players)
- Regulatory filings
- Academic/consultant reports

## ACTUALIZACIÓN
- Frecuencia: Cada 30 días o ante cambio material
- Trigger: Earnings season del sector, regulación nueva, disrupción

---

## TEMPLATE PARA world/sectors/[sector].md

```markdown
# Sector: [Nombre]

> Última actualización: [fecha]
> Analista: Claude
> Status: [SOBREPONDERAR/NEUTRAL/INFRAPONDERAR/EVITAR]

## Resumen Ejecutivo
[2-3 párrafos con la tesis sectorial]

## Métricas Clave
| Métrica | Valor | Tendencia |
|---------|-------|-----------|
| TAM | $XB | ↑/↓/→ |
| CAGR | X% | |
| P/E sector | Xx | vs Yx histórico |

## Estructura Competitiva
[Análisis de 5 fuerzas resumido]

## Disrupción y Riesgos
[Top 3 riesgos con probabilidad e impacto]

## Sentimiento
[Narrativa del mercado y mi contra-tesis si aplica]

## Empresas Objetivo
- [Ticker]: [1 línea]

## Próxima Revisión
[Fecha o trigger]
```
