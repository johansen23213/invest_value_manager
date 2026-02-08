#!/usr/bin/env python3
"""
System Projection Tool - Monte Carlo Simulation
Analyzes the investment system's probability of success over 1, 3, 5, and 10 years.

Framework v4.0: This tool outputs RAW DATA and projections.
The assumptions are explicit and debatable - they are NOT hidden rules.

Usage:
    python3 tools/system_projection.py
    python3 tools/system_projection.py --additions 500   # Monthly capital additions
    python3 tools/system_projection.py --sims 50000      # More simulations
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.patches as mpatches
from datetime import datetime
import sys
import os

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

# Parse arguments
monthly_addition = 0
n_simulations = 10000
for i, arg in enumerate(sys.argv[1:], 1):
    if arg == '--additions' and i < len(sys.argv) - 1:
        monthly_addition = float(sys.argv[i + 1])
    if arg == '--sims' and i < len(sys.argv) - 1:
        n_simulations = int(sys.argv[i + 1])

np.random.seed(42)

# ═══════════════════════════════════════════════════════════════════════════════
# CURRENT SYSTEM STATE (factual, from portfolio/current.yaml)
# ═══════════════════════════════════════════════════════════════════════════════

INITIAL_VALUE = 11186  # EUR total (invested + cash)
N_POSITIONS = 21
CASH_EUR = 790
SYSTEM_AGE_DAYS = 12  # Started ~Jan 26, 2026

# Current tier distribution (from system.yaml quality analysis)
CURRENT_TIERS = {
    'A': {'count': 4, 'tickers': ['ADBE', 'NVO', 'MONY.L', 'LULU']},
    'B': {'count': 5, 'tickers': ['HRB', 'EDEN.PA', 'DOM.L', 'SAN.PA', 'LIGHT.AS']},
    'C': {'count': 12, 'tickers': ['ALL', 'VICI', 'IMB.L', 'GL', 'UHS', 'PFE',
                                     'DTE.DE', 'TEP.PA', 'TATE.L', 'VNA.DE', 'A2A.MI', 'SHEL.L']},
    'D': {'count': 0, 'tickers': []}
}

# ═══════════════════════════════════════════════════════════════════════════════
# MODEL ASSUMPTIONS (explicit, debatable, documented)
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 80)
print("SUPUESTOS DEL MODELO (explícitos - NO son verdades)")
print("=" * 80)

ASSUMPTIONS = """
╔══════════════════════════════════════════════════════════════════════════════╗
║  SUPUESTO                    │ VALOR           │ JUSTIFICACIÓN              ║
╠══════════════════════════════╪═════════════════╪════════════════════════════╣
║ Retorno Tier A (CAGR)       │ 12-16% ± 17%   │ Quality compounders con    ║
║                              │                 │ MoS 30%+, ROIC>15%        ║
║ Retorno Tier B (CAGR)       │ 8-12% ± 20%    │ Quality value, MoS 20-30% ║
║ Retorno Tier C (CAGR)       │ 3-8% ± 25%     │ Special sit., mayor riesgo ║
║                              │                 │ de value trap              ║
║──────────────────────────────┼─────────────────┼────────────────────────────║
║ Alpha sesiones diarias       │ 2-3% (decrece)  │ Info advantage vs buy&hold ║
║                              │                 │ Decay: low-hanging fruit   ║
║ Curva aprendizaje año 1     │ -3% a -5%       │ 42 errores en 12 días      ║
║ Curva aprendizaje año 3+    │ +1%             │ Sistema maduro             ║
║──────────────────────────────┼─────────────────┼────────────────────────────║
║ Costes transacción (eToro)  │ ~1% anual       │ Spreads + frecuencia       ║
║ Cash drag                   │ 7% → 3%         │ Decrece con madurez        ║
║ P(drawdown >20% en 1 año)   │ 12-25%          │ Depende de escenario       ║
║ P(crash >30% en 1 año)      │ 3-8%            │ Tail risk (GFC/COVID)      ║
║──────────────────────────────┼─────────────────┼────────────────────────────║
║ Rotación C→A                │ 5-7 años        │ ~2-3 rotaciones/año        ║
║ Aportaciones mensuales      │ €{:>4,.0f}          │ Configurable               ║
║ Inflación                   │ No modelada     │ Retornos nominales         ║
╚══════════════════════════════╧═════════════════╧════════════════════════════╝

SESGOS CONOCIDOS DEL MODELO:
  • Optimista: Asume que el sistema mejora con el tiempo (puede no hacerlo)
  • Optimista: Asume rotación exitosa C→A (puede ser lenta o fallida)
  • Pesimista: No modela aportaciones de capital (excepto si se configura)
  • Pesimista: Learning curve del año 1 puede ser menos severa
  • Neutral: Volatilidad calibrada a datos históricos de mercado
  • CRITICO: 12 días de track record = CERO evidencia estadística real
""".format(monthly_addition)
print(ASSUMPTIONS)

# ═══════════════════════════════════════════════════════════════════════════════
# MODEL FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def portfolio_mix(year):
    """
    Models the gradual rotation from Tier C to Tier A/B over time.
    Currently: 19% A, 24% B, 57% C
    Target by year 7+: ~55% A, 25% B, 20% C

    This assumes ~2-3 successful rotations per year, which requires:
    - Finding quality companies
    - Selling underperformers or harvesting Tier C at fair value
    - Maintaining discipline
    """
    t = min(year, 10)
    # Logistic growth for Tier A
    tier_a = 0.19 + (0.55 - 0.19) * (1 - np.exp(-0.25 * t))
    tier_b = 0.24 + (0.25 - 0.24) * (1 - np.exp(-0.3 * t))
    tier_c = max(1.0 - tier_a - tier_b, 0.10)
    total = tier_a + tier_b + tier_c
    return tier_a/total, tier_b/total, tier_c/total

def session_alpha(year):
    """
    Daily sessions provide information advantage:
    - Faster reaction to news/earnings
    - Better entry/exit timing
    - Continuous monitoring (vs quarterly check)

    Decays because: early inefficiencies get corrected,
    market learns, low-hanging fruit is picked.
    """
    base_alpha = 0.025  # 2.5% annual alpha from daily attention
    return base_alpha * np.exp(-0.08 * year)

def learning_curve(year):
    """
    System learning effect:
    Year 0-0.5: Heavy mistakes (-4% drag). 42 errors documented in 12 days.
    Year 0.5-1: Still learning (-2%)
    Year 1-2: Breaking even (0%)
    Year 2-3: Slight positive (+0.5%)
    Year 3+: Mature (+1%)

    Note: This assumes the system ACTUALLY learns. If errors repeat,
    the curve stays negative.
    """
    if year < 0.5:
        return -0.04
    elif year < 1:
        return -0.02
    elif year < 2:
        return 0.0
    elif year < 3:
        return 0.005
    else:
        return 0.01

def cash_drag(year):
    """Cash fraction, decreasing as system matures and deploys capital."""
    return max(0.03, 0.07 - 0.004 * year)

# Tier return parameters (annual)
TIER_PARAMS = {
    'A': {'mean': 0.14, 'std': 0.17},  # Quality compounders: high return, lower vol
    'B': {'mean': 0.10, 'std': 0.20},  # Quality value: moderate return/vol
    'C': {'mean': 0.055, 'std': 0.25}, # Special situations: lower return, higher vol
}

TRANSACTION_COST = 0.01  # Annual trading costs

# ═══════════════════════════════════════════════════════════════════════════════
# SCENARIOS
# ═══════════════════════════════════════════════════════════════════════════════

SCENARIOS = {
    'Bull': {
        'description': 'Mercados favorables, rotación exitosa, sistema aprende rápido',
        'market_premium': 0.025,
        'hit_rate_adj': 1.1,    # 10% better hit rate
        'drawdown_annual_prob': 0.08,
        'crash_annual_prob': 0.02,
        'weight': 0.20,
        'color': '#4CAF50',
    },
    'Base': {
        'description': 'Mercados normales, progreso gradual, algunos errores',
        'market_premium': 0.0,
        'hit_rate_adj': 1.0,
        'drawdown_annual_prob': 0.15,
        'crash_annual_prob': 0.04,
        'weight': 0.50,
        'color': '#2196F3',
    },
    'Bear': {
        'description': 'Mercados difíciles, rotación lenta, errores persistentes',
        'market_premium': -0.025,
        'hit_rate_adj': 0.9,    # 10% worse hit rate
        'drawdown_annual_prob': 0.22,
        'crash_annual_prob': 0.07,
        'weight': 0.30,
        'color': '#FF5722',
    }
}

# ═══════════════════════════════════════════════════════════════════════════════
# MONTE CARLO SIMULATION
# ═══════════════════════════════════════════════════════════════════════════════

print(f"\nEjecutando {n_simulations:,} simulaciones Monte Carlo...")
print(f"Aportaciones mensuales: €{monthly_addition:,.0f}")

YEARS = 10
MONTHS = YEARS * 12

results = {}
for scenario_name, scenario in SCENARIOS.items():
    portfolio_values = np.zeros((n_simulations, MONTHS + 1))
    portfolio_values[:, 0] = INITIAL_VALUE
    max_drawdowns = np.zeros(n_simulations)

    for sim in range(n_simulations):
        value = INITIAL_VALUE
        peak = value
        max_dd = 0

        for month in range(MONTHS):
            year = month / 12

            # Portfolio quality mix at this point
            pa, pb, pc = portfolio_mix(year)

            # Weighted expected annual return
            expected_annual = (
                pa * TIER_PARAMS['A']['mean'] * scenario['hit_rate_adj'] +
                pb * TIER_PARAMS['B']['mean'] * scenario['hit_rate_adj'] +
                pc * TIER_PARAMS['C']['mean'] * scenario['hit_rate_adj']
            )

            # Add system effects
            expected_annual += session_alpha(year)
            expected_annual += learning_curve(year)
            expected_annual += scenario['market_premium']

            # Subtract costs
            expected_annual -= TRANSACTION_COST
            expected_annual -= cash_drag(year) * 0.04  # Opportunity cost

            # Monthly parameters
            monthly_return = expected_annual / 12

            # Weighted monthly volatility
            annual_vol = np.sqrt(
                pa**2 * TIER_PARAMS['A']['std']**2 +
                pb**2 * TIER_PARAMS['B']['std']**2 +
                pc**2 * TIER_PARAMS['C']['std']**2 +
                2 * pa * pb * 0.3 * TIER_PARAMS['A']['std'] * TIER_PARAMS['B']['std'] +
                2 * pa * pc * 0.2 * TIER_PARAMS['A']['std'] * TIER_PARAMS['C']['std'] +
                2 * pb * pc * 0.25 * TIER_PARAMS['B']['std'] * TIER_PARAMS['C']['std']
            )
            monthly_vol = annual_vol / np.sqrt(12)

            # Generate return with fat tails (Student-t with 5 df)
            z = np.random.standard_t(5)
            r = monthly_return + monthly_vol * z * 0.7  # Scale t-distribution

            # Drawdown events
            rand = np.random.random()
            if rand < scenario['crash_annual_prob'] / 12:
                # Major crash month (-15% to -30%)
                r -= np.random.uniform(0.15, 0.30)
            elif rand < scenario['drawdown_annual_prob'] / 12:
                # Significant drawdown month (-8% to -18%)
                r -= np.random.uniform(0.08, 0.18)

            # Apply return + additions
            value = value * (1 + r) + monthly_addition
            value = max(value, 100)  # Floor at €100 (no leverage, can't go to 0)

            # Track drawdown
            peak = max(peak, value)
            dd = (peak - value) / peak
            max_dd = max(max_dd, dd)

            portfolio_values[sim, month + 1] = value

        max_drawdowns[sim] = max_dd

    results[scenario_name] = {
        'values': portfolio_values,
        'max_drawdowns': max_drawdowns,
    }

print("Simulación completada.\n")

# ═══════════════════════════════════════════════════════════════════════════════
# CREATE WEIGHTED COMBINED RESULTS
# ═══════════════════════════════════════════════════════════════════════════════

combined_values = np.zeros((n_simulations, MONTHS + 1))
combined_drawdowns = np.zeros(n_simulations)
idx = 0
for s_name, s_params in SCENARIOS.items():
    n = int(n_simulations * s_params['weight'])
    chosen = np.random.choice(n_simulations, size=n, replace=False)
    end_idx = min(idx + n, n_simulations)
    actual_n = end_idx - idx
    combined_values[idx:end_idx] = results[s_name]['values'][chosen[:actual_n]]
    combined_drawdowns[idx:end_idx] = results[s_name]['max_drawdowns'][chosen[:actual_n]]
    idx = end_idx

# Fill remaining slots if any
if idx < n_simulations:
    remaining = n_simulations - idx
    combined_values[idx:] = results['Base']['values'][:remaining]
    combined_drawdowns[idx:] = results['Base']['max_drawdowns'][:remaining]

# Total contributed capital at each month (for ROI calculation with additions)
total_contributed = np.array([INITIAL_VALUE + monthly_addition * m for m in range(MONTHS + 1)])

# ═══════════════════════════════════════════════════════════════════════════════
# ANALYSIS OUTPUT
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 90)
print("PROYECCIÓN DEL SISTEMA DE INVERSIÓN VALUE v4.0")
print(f"Portfolio: €{INITIAL_VALUE:,.0f} | {N_POSITIONS} posiciones | "
      f"Tier A: {CURRENT_TIERS['A']['count']} | "
      f"Simulaciones: {n_simulations:,}")
if monthly_addition > 0:
    print(f"Aportaciones: €{monthly_addition:,.0f}/mes")
print(f"Fecha: {datetime.now().strftime('%Y-%m-%d')}")
print("=" * 90)

# Key timepoints
TIMEPOINTS = [(1, 12), (3, 36), (5, 60), (10, 120)]

# Per-scenario analysis
for year, month in TIMEPOINTS:
    print(f"\n{'─'*90}")
    print(f"  AÑO {year}")
    print(f"{'─'*90}")

    contributed = total_contributed[month]
    pa, pb, pc = portfolio_mix(year)

    print(f"  Mix esperado: Tier A {pa*100:.0f}% | Tier B {pb*100:.0f}% | Tier C {pc*100:.0f}%")
    if monthly_addition > 0:
        print(f"  Capital total aportado: €{contributed:,.0f}")

    for s_name in ['Bull', 'Base', 'Bear']:
        vals = results[s_name]['values'][:, month]
        rets = (vals / contributed - 1) if monthly_addition > 0 else (vals / INITIAL_VALUE - 1)
        cagrs = (vals / INITIAL_VALUE) ** (1/year) - 1

        print(f"\n  {s_name:5s} (peso {SCENARIOS[s_name]['weight']*100:.0f}%):")
        print(f"    Valor mediano:    €{np.median(vals):>10,.0f}  "
              f"(rango 80%: €{np.percentile(vals, 10):,.0f} - €{np.percentile(vals, 90):,.0f})")
        print(f"    CAGR mediano:     {np.median(cagrs)*100:>+7.1f}%")
        print(f"    P(return > 0%):   {(rets > 0).mean()*100:>7.1f}%")
        print(f"    P(CAGR > 8%):     {(cagrs > 0.08).mean()*100:>7.1f}%")
        print(f"    P(pérdida > 20%): {(rets < -0.20).mean()*100:>7.1f}%")

    # Weighted
    vals = combined_values[:, month]
    rets = (vals / contributed - 1) if monthly_addition > 0 else (vals / INITIAL_VALUE - 1)
    cagrs = (vals / INITIAL_VALUE) ** (1/year) - 1

    print(f"\n  {'PONDERADO':}")
    print(f"    Valor mediano:    €{np.median(vals):>10,.0f}")
    print(f"    CAGR mediano:     {np.median(cagrs)*100:>+7.1f}%")
    print(f"    P(return > 0%):   {(rets > 0).mean()*100:>7.1f}%")
    print(f"    P(CAGR > 8%):     {(cagrs > 0.08).mean()*100:>7.1f}%")
    print(f"    P(doblar):        {(vals > INITIAL_VALUE * 2).mean()*100:>7.1f}%")
    print(f"    P(pérdida > 20%): {(rets < -0.20).mean()*100:>7.1f}%")

# ═══════════════════════════════════════════════════════════════════════════════
# SUMMARY TABLE
# ═══════════════════════════════════════════════════════════════════════════════

print(f"\n{'='*90}")
print("TABLA RESUMEN - RESULTADOS PONDERADOS")
print(f"{'='*90}")
print(f"{'':20s} {'1 AÑO':>12s} {'3 AÑOS':>12s} {'5 AÑOS':>12s} {'10 AÑOS':>12s}")
print(f"{'─'*68}")

metrics = {}
for year, month in TIMEPOINTS:
    vals = combined_values[:, month]
    contributed = total_contributed[month]
    rets = (vals / contributed - 1) if monthly_addition > 0 else (vals / INITIAL_VALUE - 1)
    cagrs = (vals / INITIAL_VALUE) ** (1/year) - 1

    metrics[year] = {
        'median_value': np.median(vals),
        'p10_value': np.percentile(vals, 10),
        'p90_value': np.percentile(vals, 90),
        'median_cagr': np.median(cagrs) * 100,
        'p_positive': (rets > 0).mean() * 100,
        'p_benchmark': (cagrs > 0.08).mean() * 100,
        'p_double': (vals > INITIAL_VALUE * 2).mean() * 100,
        'p_triple': (vals > INITIAL_VALUE * 3).mean() * 100,
        'p_loss_20': (rets < -0.20).mean() * 100,
        'p_loss_50': (rets < -0.50).mean() * 100,
        'worst_5': np.percentile(rets, 5) * 100,
        'best_95': np.percentile(rets, 95) * 100,
    }

def row(label, key, fmt=',.0f', prefix='€', suffix=''):
    vals = [metrics[y][key] for y in [1, 3, 5, 10]]
    strs = [f"{prefix}{v:{fmt}}{suffix}" for v in vals]
    print(f"{label:20s} {strs[0]:>12s} {strs[1]:>12s} {strs[2]:>12s} {strs[3]:>12s}")

row("Valor mediano", 'median_value')
row("Peor 10%", 'p10_value')
row("Mejor 10%", 'p90_value')
row("CAGR mediano", 'median_cagr', fmt='+.1f', prefix='', suffix='%')
print(f"{'─'*68}")
row("P(return > 0%)", 'p_positive', fmt='.1f', prefix='', suffix='%')
row("P(CAGR > 8%)", 'p_benchmark', fmt='.1f', prefix='', suffix='%')
row("P(2x capital)", 'p_double', fmt='.1f', prefix='', suffix='%')
row("P(3x capital)", 'p_triple', fmt='.1f', prefix='', suffix='%')
print(f"{'─'*68}")
row("P(pérdida > 20%)", 'p_loss_20', fmt='.1f', prefix='', suffix='%')
row("P(pérdida > 50%)", 'p_loss_50', fmt='.1f', prefix='', suffix='%')
row("Peor 5%", 'worst_5', fmt='+.0f', prefix='', suffix='%')
row("Mejor 5%", 'best_95', fmt='+.0f', prefix='', suffix='%')

# Max drawdown stats
print(f"\n{'─'*68}")
print(f"{'Max Drawdown':20s}")
print(f"  Mediano:          {np.median(combined_drawdowns)*100:>6.1f}%")
print(f"  P(DD > 20%):      {(combined_drawdowns > 0.20).mean()*100:>6.1f}%")
print(f"  P(DD > 30%):      {(combined_drawdowns > 0.30).mean()*100:>6.1f}%")
print(f"  P(DD > 50%):      {(combined_drawdowns > 0.50).mean()*100:>6.1f}%")

# ═══════════════════════════════════════════════════════════════════════════════
# QUALITATIVE RISK ASSESSMENT
# ═══════════════════════════════════════════════════════════════════════════════

print(f"\n{'='*90}")
print("EVALUACIÓN CUALITATIVA DEL SISTEMA")
print(f"{'='*90}")

print("""
FORTALEZAS (factores positivos NO modelados cuantitativamente):
  [+] Framework adaptativo v4.0 (principios > reglas)
  [+] Sesiones diarias = reacción rápida a eventos
  [+] 23 agentes especializados = análisis sistemático
  [+] Anti-bias protocols (screening programático, error tracking)
  [+] Correlación baja entre posiciones (0.109 promedio)
  [+] Diversificación geográfica (US, UK, EU)
  [+] Auto-evolución documentada (v2→v3→v4 en 10 días)
  [+] 42 errores documentados = aprendizaje acelerado

DEBILIDADES (factores negativos):
  [-] Track record: 12 DÍAS. Cero significancia estadística.
  [-] Portfolio pequeño: €11K. Costes relativos altos.
  [-] 57% Tier C: La mayoría del portfolio es "special situations"
  [-] eToro: Spreads altos, sin opciones, limitado en instrumentos
  [-] Operador único: Si el humano no ejecuta, el sistema se para
  [-] Sin crisis real testeada (solo simulación COVID)
  [-] Over-engineering? 23 agentes para €11K puede ser ineficiente
  [-] Framework en flux: 4 versiones en 12 días = inestabilidad

RIESGOS EXISTENCIALES (pueden destruir el sistema):
  [!] Abandono: El humano deja de operar (probabilidad ALTA en 1-3 años)
  [!] Drawdown psicológico: -30% puede causar panic selling
  [!] Cambio de plataforma: eToro cambia condiciones
  [!] Mercado secular bear: 5+ años de retornos negativos
  [!] Error catastrófico: Concentración inadvertida en sector en crisis

FACTORES DE ÉXITO CRÍTICOS:
  [*] Disciplina: ¿Se mantiene el proceso en drawdowns?
  [*] Rotación: ¿Se logra reemplazar Tier C con Tier A?
  [*] Capital: ¿Se aporta capital adicional para escalar?
  [*] Tiempo: Value investing necesita 3-5 años mínimo
""")

# ═══════════════════════════════════════════════════════════════════════════════
# GENERATE CHART
# ═══════════════════════════════════════════════════════════════════════════════

print("Generando gráfico...")

fig = plt.figure(figsize=(20, 14))
fig.patch.set_facecolor('#f8f9fa')

# Create grid: 2 rows, top row 2 plots, bottom row 3 plots
gs = fig.add_gridspec(2, 6, hspace=0.35, wspace=0.45,
                       left=0.06, right=0.97, top=0.91, bottom=0.06)

ax1 = fig.add_subplot(gs[0, :3])   # Fan chart
ax2 = fig.add_subplot(gs[0, 3:])   # Probability curves
ax3 = fig.add_subplot(gs[1, :2])   # Distribution year 5
ax4 = fig.add_subplot(gs[1, 2:4])  # Portfolio evolution
ax5 = fig.add_subplot(gs[1, 4:])   # Scenario comparison

months_x = np.arange(MONTHS + 1) / 12

# ─── PLOT 1: Fan Chart (Weighted) ────────────────────────────────────────────

percentiles = [5, 10, 25, 50, 75, 90, 95]
pct_vals = {p: np.percentile(combined_values, p, axis=0) for p in percentiles}

ax1.fill_between(months_x, pct_vals[5]/1000, pct_vals[95]/1000,
                  alpha=0.08, color='#1565C0', label='90% CI')
ax1.fill_between(months_x, pct_vals[10]/1000, pct_vals[90]/1000,
                  alpha=0.12, color='#1565C0', label='80% CI')
ax1.fill_between(months_x, pct_vals[25]/1000, pct_vals[75]/1000,
                  alpha=0.22, color='#1565C0', label='50% CI')
ax1.plot(months_x, pct_vals[50]/1000, color='#0D47A1', linewidth=2.5, label='Mediana')

# Benchmark
benchmark = INITIAL_VALUE * (1.08 ** months_x)
ax1.plot(months_x, benchmark/1000, 'r--', linewidth=1.5, alpha=0.7, label='Benchmark 8% CAGR')

# Capital contributed
if monthly_addition > 0:
    contributed_line = np.array([INITIAL_VALUE + monthly_addition * m for m in range(MONTHS + 1)])
    ax1.plot(months_x, contributed_line/1000, 'gray', linewidth=1, linestyle=':', label='Capital aportado')

ax1.axhline(y=INITIAL_VALUE/1000, color='gray', linestyle='--', alpha=0.3)
ax1.set_title('Evolución del Portfolio (Ponderado por Escenarios)', fontweight='bold', fontsize=12)
ax1.set_xlabel('Años', fontsize=10)
ax1.set_ylabel('Valor (miles €)', fontsize=10)
ax1.legend(loc='upper left', fontsize=8, framealpha=0.9)
ax1.grid(True, alpha=0.2)
ax1.set_xlim(0, 10)

# ─── PLOT 2: Probability Curves ──────────────────────────────────────────────

years_range = np.arange(1, 11)
p_positive_arr = []
p_beat_arr = []
p_double_arr = []
p_loss20_arr = []

for y in years_range:
    m = y * 12
    vals = combined_values[:, m]
    cont = total_contributed[m]
    rets = (vals / cont - 1) if monthly_addition > 0 else (vals / INITIAL_VALUE - 1)
    cagrs = (vals / INITIAL_VALUE) ** (1/y) - 1
    p_positive_arr.append((rets > 0).mean() * 100)
    p_beat_arr.append((cagrs > 0.08).mean() * 100)
    p_double_arr.append((vals > INITIAL_VALUE * 2).mean() * 100)
    p_loss20_arr.append((rets < -0.20).mean() * 100)

ax2.plot(years_range, p_positive_arr, 'g-o', linewidth=2, markersize=7, label='P(return > 0%)')
ax2.plot(years_range, p_beat_arr, 'b-s', linewidth=2, markersize=7, label='P(CAGR > 8%)')
ax2.plot(years_range, p_double_arr, 'm-^', linewidth=2, markersize=7, label='P(doblar capital)')
ax2.plot(years_range, p_loss20_arr, 'r-v', linewidth=2, markersize=7, label='P(pérdida > 20%)')

ax2.set_title('Probabilidades por Horizonte Temporal', fontweight='bold', fontsize=12)
ax2.set_xlabel('Años', fontsize=10)
ax2.set_ylabel('Probabilidad (%)', fontsize=10)
ax2.set_ylim(0, 100)
ax2.set_xticks(years_range)
ax2.legend(loc='center right', fontsize=8, framealpha=0.9)
ax2.grid(True, alpha=0.2)

# Add annotations at year 5
for arr, y_offset, fmt, color in [
    (p_positive_arr, 3, '.0f', 'green'),
    (p_beat_arr, -5, '.0f', 'blue'),
    (p_double_arr, 3, '.0f', 'purple'),
    (p_loss20_arr, -5, '.0f', 'red')
]:
    ax2.annotate(f'{arr[4]:{fmt}}%', xy=(5, arr[4]),
                  xytext=(5.3, arr[4] + y_offset),
                  fontsize=8, color=color, fontweight='bold')

# ─── PLOT 3: Distribution at Year 5 ──────────────────────────────────────────

vals_5y = combined_values[:, 60]
rets_5y = (vals_5y / INITIAL_VALUE - 1) * 100

ax3.hist(rets_5y, bins=80, density=True, alpha=0.7, color='steelblue',
          edgecolor='white', linewidth=0.5)
ax3.axvline(x=0, color='red', linestyle='--', linewidth=1.5, alpha=0.8, label='Break-even')
ax3.axvline(x=np.median(rets_5y), color='#0D47A1', linestyle='-', linewidth=2,
             label=f'Mediana: {np.median(rets_5y):+.0f}%')

benchmark_5y = ((1.08**5) - 1) * 100
ax3.axvline(x=benchmark_5y, color='orange', linestyle='--', linewidth=1.5,
             label=f'Benchmark: +{benchmark_5y:.0f}%')

# Shade loss region
xlim = ax3.get_xlim()
ax3.axvspan(xlim[0], 0, alpha=0.05, color='red')

ax3.set_title('Distribución de Retornos a 5 Años', fontweight='bold', fontsize=12)
ax3.set_xlabel('Retorno Total (%)', fontsize=10)
ax3.set_ylabel('Densidad', fontsize=10)
ax3.legend(fontsize=8, framealpha=0.9)
ax3.grid(True, alpha=0.2)

# ─── PLOT 4: Portfolio Quality Evolution ──────────────────────────────────────

years_comp = np.linspace(0, 10, 100)
tier_a_arr = [portfolio_mix(y)[0] * 100 for y in years_comp]
tier_b_arr = [portfolio_mix(y)[1] * 100 for y in years_comp]
tier_c_arr = [portfolio_mix(y)[2] * 100 for y in years_comp]

ax4.stackplot(years_comp, tier_c_arr, tier_b_arr, tier_a_arr,
               colors=['#FF9800', '#42A5F5', '#66BB6A'],
               alpha=0.85,
               labels=['Tier C (Special Sit.)', 'Tier B (Quality Value)', 'Tier A (Compounders)'])

# Expected CAGR overlay
ax4_twin = ax4.twinx()
expected_cagrs = []
for y in years_comp:
    pa, pb, pc = portfolio_mix(y)
    ec = (pa * TIER_PARAMS['A']['mean'] + pb * TIER_PARAMS['B']['mean'] +
          pc * TIER_PARAMS['C']['mean'] + session_alpha(y) + learning_curve(y) -
          TRANSACTION_COST - cash_drag(y) * 0.04) * 100
    expected_cagrs.append(ec)

ax4_twin.plot(years_comp, expected_cagrs, 'k--', linewidth=2, label='CAGR Esperado')
ax4_twin.set_ylabel('CAGR Esperado (%)', fontsize=9)
ax4_twin.set_ylim(0, 18)
ax4_twin.legend(loc='upper right', fontsize=8)

ax4.set_title('Evolución de Calidad del Portfolio', fontweight='bold', fontsize=12)
ax4.set_xlabel('Años', fontsize=10)
ax4.set_ylabel('Composición (%)', fontsize=10)
ax4.legend(loc='upper left', fontsize=8, framealpha=0.9)
ax4.grid(True, alpha=0.2)
ax4.set_ylim(0, 100)

# ─── PLOT 5: Scenario Comparison (Median paths) ──────────────────────────────

for s_name, s_params in SCENARIOS.items():
    median_path = np.median(results[s_name]['values'], axis=0)
    p10_path = np.percentile(results[s_name]['values'], 10, axis=0)
    p90_path = np.percentile(results[s_name]['values'], 90, axis=0)

    ax5.fill_between(months_x, p10_path/1000, p90_path/1000,
                      alpha=0.1, color=s_params['color'])
    ax5.plot(months_x, median_path/1000, color=s_params['color'],
              linewidth=2, label=f"{s_name} ({s_params['weight']*100:.0f}%)")

ax5.axhline(y=INITIAL_VALUE/1000, color='gray', linestyle='--', alpha=0.3)
ax5.plot(months_x, benchmark/1000, 'k:', linewidth=1, alpha=0.5, label='Benchmark 8%')

ax5.set_title('Comparación por Escenario (Mediana + 80% CI)', fontweight='bold', fontsize=12)
ax5.set_xlabel('Años', fontsize=10)
ax5.set_ylabel('Valor (miles €)', fontsize=10)
ax5.legend(loc='upper left', fontsize=8, framealpha=0.9)
ax5.grid(True, alpha=0.2)
ax5.set_xlim(0, 10)

# ─── Title and Footer ────────────────────────────────────────────────────────

fig.suptitle(
    f'Proyección Sistema de Inversión Value v4.0 | '
    f'€{INITIAL_VALUE:,.0f} | {N_POSITIONS} posiciones | '
    f'{n_simulations:,} simulaciones MC',
    fontsize=15, fontweight='bold', y=0.97
)

fig.text(0.5, 0.01,
         f'Generado: {datetime.now().strftime("%Y-%m-%d")} | '
         f'Supuestos explícitos en el código | '
         f'12 días de track record = CERO evidencia estadística | '
         f'Retornos nominales, sin inflación',
         ha='center', fontsize=8, color='gray', style='italic')

output_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                            'docs', 'system_projection.png')
plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()

print(f"\nGráfico guardado: {output_path}")

# ═══════════════════════════════════════════════════════════════════════════════
# HONEST ASSESSMENT
# ═══════════════════════════════════════════════════════════════════════════════

print(f"\n{'='*90}")
print("EVALUACIÓN HONESTA")
print(f"{'='*90}")

print("""
¿QUÉ DICE ESTE MODELO?

  El modelo sugiere que CON DISCIPLINA Y TIEMPO, el sistema tiene una probabilidad
  razonable (~60-70%) de generar retornos positivos a 5 años y una probabilidad
  moderada (~30-40%) de superar un benchmark de 8% CAGR.

¿QUÉ NO DICE?

  1. No predice el futuro. Es una simulación con supuestos discutibles.
  2. El factor más importante NO está modelado: la DISCIPLINA del operador.
  3. 12 días de datos no permiten calibrar ningún parámetro con confianza.
  4. La rotación Tier C → Tier A puede ser más lenta o más rápida.
  5. Un solo evento (crash, abandono, error) puede invalidar todo.

¿CUÁL ES EL MAYOR RIESGO?

  ABANDONO. La mayoría de sistemas de inversión individuales se abandonan
  antes de 3 años. No por fallo del sistema, sino por pérdida de interés,
  drawdowns psicológicamente insoportables, o cambio de circunstancias.

¿QUÉ AUMENTARÍA LA PROBABILIDAD DE ÉXITO?

  1. TIEMPO: Mantener el sistema >5 años (el compounding necesita tiempo)
  2. CAPITAL: Aportar capital regularmente (reduce impacto de costes fijos)
  3. ROTACIÓN: Acelerar reemplazo de Tier C por Tier A (calidad > cantidad)
  4. DISCIPLINA: Seguir el proceso en drawdowns (lo más difícil)
  5. SIMPLIFICAR: ¿Se necesitan 23 agentes? Reducir complejidad innecesaria.
""")
