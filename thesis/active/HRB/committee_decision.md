# Investment Committee Decision: HRB

> Fecha: 2026-02-04
> Precio al momento: $37.20 (EUR 31.46)
> Decision: APROBAR ADD EUR 380

---

## Resumen Ejecutivo

**Empresa:** H&R Block Inc.
**Sector:** Business Services / Tax Services
**Geografia:** US (100% domestico)
**Tier:** B (Cyclical/Quality)
**Fair Value:** $59.58 (weighted DCF + EV/EBIT)
**MoS actual:** 37.6%

---

## Validacion de 8 Gates

| Gate | Status | Nota |
|------|--------|------|
| 1. Business Understanding | PASS | Thesis v2.0 completa, unit economics, modelo negocio |
| 2. Proyeccion Fundamentada | PASS | Growth 3-4% (TAM+pricing), WACC 8.5% (derivado) |
| 3. Valoracion Multi-Metodo | PASS | DCF $62.83 + EV/EBIT $56.33, divergencia 11.5% |
| 4. Margen de Seguridad | PASS | MoS 37.6% > 25% Tier B req |
| 5. Contexto Macro | PASS | US defensivo, no tariff exposed |
| 6. Portfolio Fit | PASS | HRB 6.9% OK. DTE/FUTR violaciones pre-existentes |
| 7. Autocritica | PASS | Kill conditions definidas |
| 8. Sector Understanding | PASS | business-services.md actualizado 2026-02-03 |

**Gates pasados:** 8/8
**Gates fallidos:** 0

---

## Valoracion

| Metodo | Fair Value | Peso |
|--------|-----------|------|
| DCF (3% growth, 8.5% WACC, 2% terminal) | $62.83 | 50% |
| EV/EBIT (9.5x multiple) | $56.33 | 50% |
| **Weighted** | **$59.58** | 100% |

| Escenario | Fair Value | Probabilidad | MoS |
|-----------|-----------|--------------|-----|
| Bear | $46.53 | 25% | +25% |
| Base | $59.58 | 50% | +60% |
| Bull | $75.96 | 25% | +104% |
| **Expected** | **$60.41** | 100% | **+62%** |

---

## Contexto Q2 FY2026 Earnings (3-feb-2026)

- **EPS:** -$1.84 vs -$1.96 expected (BEAT)
- **Revenue:** $198.87M vs $187.36M expected (BEAT)
- **Guidance:** Reaffirmed $4.85-$5.00 EPS FY2026
- **Implicacion:** Thesis on-track. No cambia fair value pero confirma execution.

---

## Riesgos y Kill Conditions

### Riesgos Principales
1. FCF continua declinando - Prob: 40%, Impacto: Alto
2. AI disruption acelera - Prob: 30%, Impacto: Medio
3. IRS Direct File expansion - Prob: 25%, Impacto: Alto

### Kill Conditions (vender inmediatamente si ocurre)
1. [ ] FCF cae bajo $400M
2. [ ] Dividend cut
3. [ ] ROIC < WACC por 2+ anos consecutivos
4. [ ] Nuevo CEO abandona estrategia core tax prep
5. [ ] IRS Direct File se expande a returns complejos

---

## Decision

### APROBAR ADD:
```
Accion: ADD
Ticker: HRB
Sizing: EUR 380 (~6.9% post-compra)
Shares adicionales: ~12
Precio maximo entrada: $38.00 (EUR 32.14)
```

### Advertencias
1. DTE.DE (7.1%) y FUTR.L (7.0%) sobre limite 7% - requieren TRIM separado
2. HRB post-compra 6.9% - cerca del limite

---

## Post-Decision

- [ ] Actualizar portfolio/current.yaml
- [ ] Configurar price alert $48 (trigger partial sell)
- [ ] Next review: Abril 2026 (Q4 FY2026 - tax season completa)
- [ ] FLAG: Resolver DTE.DE y FUTR.L violaciones

---

## Firmas

**Investment Committee:** Claude (Orchestrator)
**Fecha:** 2026-02-04
**Version Framework:** v2.1 (8 gates)
