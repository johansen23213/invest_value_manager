---
name: news-classification
description: "Framework para clasificar noticias por impacto en thesis de inversión"
user-invocable: false
---

# News Classification Framework

## Propósito
Clasificar noticias de forma consistente para determinar si requieren acción, monitoreo, o pueden ignorarse.

---

## Niveles de Clasificación

### 🔴 CRÍTICO (Acción inmediata)

**Características:**
- Puede invalidar la thesis completamente
- Requiere decisión en <24 horas
- Potencial pérdida >20% si no se actúa

**Ejemplos:**
| Tipo | Ejemplo |
|------|---------|
| **Fraude/Contabilidad** | "SEC investiga irregularidades contables en {COMPANY}" |
| **Liderazgo** | "CEO y CFO dimiten inesperadamente" |
| **Regulatorio** | "FDA rechaza aprobación de fármaco clave" |
| **Financiero** | "Company suspende dividendo" / "Covenant breach" |
| **Legal** | "DOJ presenta cargos criminales contra {COMPANY}" |
| **Guidance** | "Company recorta guidance >20%" |
| **Quiebra** | "Company evalúa Chapter 11" |

**Acción:** ALERTA INMEDIATA → Evaluar SELL → Informar humano

---

### 🟠 MATERIAL (Requiere revisión de thesis)

**Características:**
- Afecta valoración o thesis pero no la invalida
- Requiere actualización de modelo en <7 días
- Potencial impacto 5-20%

**Ejemplos:**
| Tipo | Ejemplo |
|------|---------|
| **Earnings** | "Company reporta miss de EPS >10%" |
| **Guidance** | "Guidance cut 5-20%" |
| **Competencia** | "Competidor anuncia producto disruptivo" |
| **Mercado** | "Company pierde cliente >5% revenue" |
| **Regulación** | "Nueva regulación afectará márgenes" |
| **Insiders** | "CEO vende >25% de sus acciones" |
| **Analyst** | "3+ analysts downgrade a SELL" |
| **Credit** | "Moody's downgrade (pero no a junk)" |

**Acción:** Documentar → Revisar thesis → Actualizar FV si necesario

---

### 🟡 MENOR (Monitorear)

**Características:**
- Relevante pero no cambia thesis
- Puede acumularse con otras señales
- Impacto <5%

**Ejemplos:**
| Tipo | Ejemplo |
|------|---------|
| **Earnings** | "Slight miss de EPS <5%" |
| **Personal** | "Ejecutivo secundario sale" |
| **Legal** | "Demanda menor sin impacto material" |
| **Operativo** | "Problema temporal de supply chain" |
| **Analyst** | "1 analyst baja PT ligeramente" |

**Acción:** Documentar → Monitorear → No acción inmediata

---

### ⚪ RUIDO (Ignorar)

**Características:**
- No tiene impacto en fundamentales
- Opinión vs hecho
- Repetición de información conocida

**Ejemplos:**
| Tipo | Ejemplo |
|------|---------|
| **Opinión** | "Analyst cree que stock está caro" |
| **PT menor** | "PT cambia de $150 a $148" |
| **Repetición** | Misma noticia en diferentes fuentes |
| **Especulación** | "Rumores de M&A sin confirmar" |
| **General** | "Mercado cae, {STOCK} también" |

**Acción:** Ignorar → No documentar

---

## Proceso de Clasificación

```
1. LEER headline y resumen
   ↓
2. ¿Es HECHO o OPINIÓN?
   - Opinión → probablemente RUIDO
   - Hecho → continuar
   ↓
3. ¿Afecta FUNDAMENTALES del negocio?
   - No → RUIDO
   - Sí → continuar
   ↓
4. ¿Cuánto puede afectar el VALOR?
   - >20% → CRÍTICO
   - 5-20% → MATERIAL
   - <5% → MENOR
   ↓
5. ¿Activa alguna KILL CONDITION de la thesis?
   - Sí → CRÍTICO (automático)
   - No → mantener clasificación
```

---

## Contexto Importa

### Noticia "negativa" puede ser neutral o positiva si:
- **Ya está en el precio**: "NVO cae 18% tras guidance" → si compramos POST-caída, ya lo sabíamos
- **Es esperada**: "Earnings miss en línea con pre-anuncio"
- **Sector-wide**: "Todo el sector cae" → no es específico de la empresa

### Noticia "positiva" puede ser preocupante si:
- **Demasiado buena**: ¿Por qué el mercado no lo anticipó?
- **Insiders vendiendo**: Beat de earnings pero insiders venden
- **Rally sin volumen**: Movimiento de precio sin convicción

---

## Fuentes por Confiabilidad

| Tier | Fuentes | Uso |
|------|---------|-----|
| **1 - Oficial** | SEC filings, company PR, earnings transcripts | Verdad verificada |
| **2 - Primaria** | Reuters, Bloomberg, WSJ, FT | Alta confiabilidad |
| **3 - Secundaria** | Yahoo Finance, CNBC, Seeking Alpha | Verificar con Tier 1-2 |
| **4 - Social** | Twitter, Reddit, foros | Solo para sentimiento, no hechos |

---

## Ejemplos Prácticos

### Ejemplo 1: NVO Guidance Cut
```
Headline: "Novo Nordisk warns 2026 sales may fall 5-13%"
Fuente: Company PR (Tier 1)

Análisis:
- ¿Hecho o opinión? HECHO (guidance oficial)
- ¿Afecta fundamentales? SÍ (revenue projection)
- ¿Cuánto afecta valor? ~15-20% (ya reflejado en caída)
- ¿Kill condition? NO

Clasificación: MATERIAL
Contexto: Si compramos POST-caída, ya está incorporado → MENOR para nosotros
```

### Ejemplo 2: SEC Investigation Rumor
```
Headline: "Sources say SEC may be looking into {COMPANY} accounting"
Fuente: Blog (Tier 4)

Análisis:
- ¿Hecho o opinión? RUMOR (no confirmado)
- ¿Afecta fundamentales? POTENCIALMENTE
- ¿Cuánto afecta valor? INCIERTO

Clasificación: AMARILLO (monitorear)
Acción: Buscar confirmación en Tier 1-2 fuentes
Si se confirma → escalar a CRÍTICO
```

### Ejemplo 3: Analyst Downgrade
```
Headline: "Jefferies downgrades ADBE to Hold"
Fuente: Reuters (Tier 2)

Análisis:
- ¿Hecho o opinión? OPINIÓN de analyst
- ¿Afecta fundamentales? NO (opinión, no hecho)
- ¿Nueva información? Verificar rationale

Clasificación: MENOR (si rationale es conocido) o MATERIAL (si revela info nueva)
```

---

## Checklist Rápido

```
[ ] ¿Es hecho verificable o opinión?
[ ] ¿Fuente confiable (Tier 1-2)?
[ ] ¿Afecta revenue, margins, o moat?
[ ] ¿Activa kill condition?
[ ] ¿Ya está en el precio?
[ ] ¿Es específico de la empresa o sector-wide?
```

---

## Clasificacion para SHORT Positions

Para posiciones SHORT activas, la logica se INVIERTE:

### Noticias POSITIVAS sobre un short = ALERTA
- Earnings beat → posicion va en contra → evaluar COVER
- Nuevo producto exitoso → fragilidad se reduce → evaluar COVER
- Insider buying → smart money contra nuestra thesis → evaluar

### Noticias NEGATIVAS sobre un short = CONFIRMACION
- Earnings miss → thesis se confirma → mantener
- Regulacion adversa → catalizador avanza → mantener
- Insider selling → confirmacion de fragilidad → mantener

### Checklist adicional para shorts
```
[ ] ¿La noticia afecta al CATALIZADOR? (mas cerca, mas lejos, o invalidado?)
[ ] ¿La noticia cambia la FRAGILIDAD? (empresa mejoro o empeoro?)
[ ] ¿La noticia afecta el CARRY? (mas tiempo esperando?)
```
