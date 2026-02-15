#!/usr/bin/env python3
"""
AI Investment System — Potential Trajectory Simulation 2020-2030

KEY DIFFERENCE from simulation_2020_2030.py:
This models the AI system as IMPROVING over time, not static.
Also adds "Average Investor" (S&P 500 minus behavioral drag) as 4th line.

The question being answered:
"If an AI system improves its capabilities year over year,
what is the realistic trajectory of performance?"

STILL A SIMULATION with transparent assumptions. Not a guarantee.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import yfinance as yf
import os
from pandas import date_range

np.random.seed(42)
output_dir = '/home/angel/value_invest2/docs/simulation_charts'
os.makedirs(output_dir, exist_ok=True)

# ============================================================
# 1. GET S&P 500 DATA
# ============================================================
print("Descargando datos S&P 500...")
sp500 = yf.download('^GSPC', start='2019-12-31', end='2026-02-15', interval='1mo', progress=False)
sp500_close = sp500['Close'].values.flatten()
sp500_monthly = np.diff(sp500_close) / sp500_close[:-1]
n_hist = len(sp500_monthly)
print(f"  {n_hist} meses historicos")


# ============================================================
# 2. SIMULATION ENGINE — TIME-VARYING PARAMETERS
# ============================================================

def get_evolving_params(month_idx, total_months):
    """
    AI system parameters that IMPROVE over time.

    Assumptions (transparent):
    - Cash allocation decreases as the system gets better at finding real MoS
    - Error drag decreases as adversarial processes, contrathesis, primary data improve
    - Alpha increases as the system learns better stock selection
    - Crash protection improves as risk detection matures

    These are modeled as linear improvements — reality would be stepwise.
    The rate of improvement is the KEY assumption.
    """
    # Progress from 0 (start) to 1 (mature)
    t = min(month_idx / total_months, 1.0)
    # Faster learning early (log curve)
    t_log = np.log(1 + t * (np.e - 1))  # maps 0→0, 1→1 but faster early

    # Cash: 55% → 25% (learns to identify real opportunities)
    base_cash = 0.55 - 0.30 * t_log

    # Error drag: -1.5% annual → -0.2% annual
    monthly_drag = -(0.00125 - 0.00105 * t_log)  # -0.00125 to -0.0002

    # Alpha: +1.5% annual → +3.0% annual
    monthly_alpha = 0.00125 + 0.00125 * t_log  # 0.00125 to 0.0025

    # Crash beta: 0.60 → 0.35 (better risk detection)
    crash_beta_severe = 0.60 - 0.25 * t_log
    crash_beta_mild = 0.65 - 0.15 * t_log

    return {
        'base_cash': base_cash,
        'min_cash': max(0.10, base_cash - 0.15),
        'max_cash': min(0.65, base_cash + 0.15),
        'quality_beta': 0.75,  # Doesn't change — inherent to quality stocks
        'crash_beta_severe': crash_beta_severe,
        'crash_beta_mild': crash_beta_mild,
        'monthly_alpha': monthly_alpha,
        'monthly_drag': monthly_drag,
        'idio_vol': 0.008 - 0.003 * t_log,  # Decreasing noise from fewer mistakes
    }


def simulate_evolving(mkt_returns, total_months, rf_schedule=None, start_month=0):
    """Simulate with time-varying (improving) parameters."""
    returns = []
    cash_levels = []
    params_log = []

    for i, mkt_r in enumerate(mkt_returns):
        global_month = start_month + i
        params = get_evolving_params(global_month, total_months)
        params_log.append(params)

        # Trailing return for regime
        if i >= 6:
            trailing = np.mean(mkt_returns[i-5:i+1]) * 12
        elif i >= 1:
            trailing = np.mean(mkt_returns[:i+1]) * 12
        else:
            trailing = mkt_r * 12

        base = params['base_cash']
        if trailing > 0.20:
            cash = base + 0.10
        elif trailing < -0.15:
            cash = base - 0.08
        elif trailing < -0.05:
            cash = base - 0.04
        else:
            cash = base

        cash += np.random.normal(0, 0.02)
        cash = np.clip(cash, params['min_cash'], params['max_cash'])
        cash_levels.append(cash)

        invested = 1 - cash
        beta = params['quality_beta']
        if mkt_r < -0.08:
            beta = params['crash_beta_severe']
        elif mkt_r < -0.04:
            beta = params['crash_beta_mild']

        rf = rf_schedule[i] if rf_schedule and i < len(rf_schedule) else 0.035/12
        alpha = params['monthly_alpha']
        drag = params['monthly_drag']
        idio = np.random.normal(0, params['idio_vol'])

        sys_r = invested * (mkt_r * beta + alpha + drag + idio) + cash * rf
        returns.append(sys_r)

    return np.array(returns), np.array(cash_levels), params_log


def simulate_avg_investor(mkt_returns):
    """
    Average investor: S&P 500 with behavioral drag.

    Modeled based on Dalbar studies:
    - In crashes (market < -5% monthly): panic sells 15% of invested portion
    - In recoveries after crash: slow to re-enter (misses first 3 months)
    - In hot markets (trailing 12m > 25%): adds more at the top (FOMO)
    - Net behavioral drag: ~3.5-4.5% annually

    This is a GENEROUS model — real behavioral drag is often worse.
    """
    returns = []
    invested_pct = 1.0  # starts fully invested
    months_since_panic = 100  # large number = no recent panic

    for i, mkt_r in enumerate(mkt_returns):
        # Panic selling in crashes
        if mkt_r < -0.06:
            # Sells 15-25% of remaining invested portion
            panic_sell_pct = np.random.uniform(0.15, 0.25)
            invested_pct *= (1 - panic_sell_pct)
            months_since_panic = 0
        elif mkt_r < -0.04:
            panic_sell_pct = np.random.uniform(0.05, 0.10)
            invested_pct *= (1 - panic_sell_pct)
            months_since_panic = 0
        else:
            months_since_panic += 1

        # Slow re-entry after panic (takes 4-8 months to get back in)
        if months_since_panic > 3 and invested_pct < 0.95:
            reinvest = min(0.08, 1.0 - invested_pct)  # slowly gets back in
            invested_pct += reinvest

        # FOMO at tops
        if i >= 12:
            trailing_12m = np.prod(1 + mkt_returns[i-11:i+1]) - 1
            if trailing_12m > 0.25 and invested_pct < 1.0:
                # Rushes back in at the top
                invested_pct = min(1.0, invested_pct + 0.15)

        invested_pct = np.clip(invested_pct, 0.3, 1.0)
        cash_pct = 1 - invested_pct

        # Average investor also picks worse stocks (chases hot sectors)
        # Modeled as -0.1% monthly underperformance on invested portion
        stock_pick_drag = -0.001

        rf = 0.02/12 if i < 24 else 0.04/12
        inv_return = invested_pct * (mkt_r + stock_pick_drag) + cash_pct * rf
        returns.append(inv_return)

    return np.array(returns)


# Risk-free schedule
rf_schedule = []
for i in range(200):  # enough for hist + future
    if i < 24:
        rf_schedule.append(0.005 / 12)
    elif i < 30:
        rf_schedule.append(0.015 / 12)
    elif i < 36:
        rf_schedule.append(0.035 / 12)
    elif i < 48:
        rf_schedule.append(0.045 / 12)
    else:
        rf_schedule.append(0.04 / 12)


# Total timeline: 132 months (Jan 2020 — Dec 2030)
total_months_full = 132

# ============================================================
# 3. HISTORICAL SIMULATION (2020 — Feb 2026)
# ============================================================
print("Simulando periodo historico...")

# S&P 500: actual data (already have it)

# Average investor
avg_inv_ret = simulate_avg_investor(sp500_monthly)

# AI Evolving system
ai_ret, ai_cash, ai_params = simulate_evolving(
    sp500_monthly, total_months_full, rf_schedule, start_month=0
)

# ============================================================
# 4. MONTE CARLO FUTURE (Mar 2026 — Dec 2030)
# ============================================================
n_future = 59
n_sims = 1000
print(f"Monte Carlo: {n_sims} sims x {n_future} meses...")

hist_mean = np.mean(sp500_monthly)
hist_std = np.std(sp500_monthly)

sp500_future = np.random.normal(hist_mean, hist_std, (n_sims, n_future))
fat_tail_mask = np.random.random((n_sims, n_future)) < 0.05
sp500_future[fat_tail_mask] *= 2.0

sp500_future_eq = np.cumprod(1 + sp500_future, axis=1)
avg_future_eq = np.zeros((n_sims, n_future))
ai_future_eq = np.zeros((n_sims, n_future))

for s in range(n_sims):
    avg_ret = simulate_avg_investor(sp500_future[s])
    avg_future_eq[s] = np.cumprod(1 + avg_ret)

    future_rf = [0.035/12] * n_future
    a_ret, _, _ = simulate_evolving(
        sp500_future[s], total_months_full, future_rf, start_month=n_hist
    )
    ai_future_eq[s] = np.cumprod(1 + a_ret)


# ============================================================
# 5. BUILD EQUITY CURVES
# ============================================================
sp500_eq = np.concatenate([[100], 100 * np.cumprod(1 + sp500_monthly)])
avg_eq = np.concatenate([[100], 100 * np.cumprod(1 + avg_inv_ret)])
ai_eq = np.concatenate([[100], 100 * np.cumprod(1 + ai_ret)])

hist_dates = date_range('2020-01-01', periods=len(sp500_eq), freq='ME')
future_dates = date_range(hist_dates[-1], periods=n_future+1, freq='ME')[1:]

sp500_fut_scaled = sp500_future_eq * sp500_eq[-1]
avg_fut_scaled = avg_future_eq * avg_eq[-1]
ai_fut_scaled = ai_future_eq * ai_eq[-1]


# ============================================================
# 6. METRICS
# ============================================================
def calc_metrics(returns, label):
    total_ret = np.prod(1 + returns) - 1
    n_years = len(returns) / 12
    cagr = (1 + total_ret) ** (1/n_years) - 1
    vol = np.std(returns) * np.sqrt(12)
    excess = returns - 0.03/12
    sharpe = np.mean(excess) / np.std(returns) * np.sqrt(12) if np.std(returns) > 0 else 0
    downside = returns[returns < 0]
    dv = np.std(downside) * np.sqrt(12) if len(downside) > 0 else 0.001
    sortino = (np.mean(returns) * 12 - 0.03) / dv
    equity = np.cumprod(1 + returns)
    peak = np.maximum.accumulate(equity)
    dd = (equity - peak) / peak
    max_dd = np.min(dd)
    wr = np.mean(returns > 0)
    return {
        'label': label, 'total_return': total_ret, 'cagr': cagr,
        'volatility': vol, 'sharpe': sharpe, 'sortino': sortino,
        'max_drawdown': max_dd, 'win_rate': wr,
        'best_month': np.max(returns), 'worst_month': np.min(returns),
    }

sp500_m = calc_metrics(sp500_monthly, 'S&P 500')
avg_m = calc_metrics(avg_inv_ret, 'Inversor Medio')
ai_m = calc_metrics(ai_ret, 'Sistema IA Evolutivo')


# ============================================================
# 7. CHARTS
# ============================================================
C_SP = '#2563EB'
C_AVG = '#F59E0B'  # Amber
C_AI = '#7C3AED'   # Purple
C_BG = '#FAFAFA'

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 11

# ----- CHART A1: Equity Curves with 4 lines -----
fig, ax = plt.subplots(figsize=(15, 9))
fig.patch.set_facecolor(C_BG)
ax.set_facecolor(C_BG)

# Historical
ax.plot(hist_dates, sp500_eq, color=C_SP, linewidth=2.5, label='S&P 500 (Pasivo)', zorder=5)
ax.plot(hist_dates, avg_eq, color=C_AVG, linewidth=2.5, label='Inversor Medio (con sesgos)', zorder=5)
ax.plot(hist_dates, ai_eq, color=C_AI, linewidth=2.8, label='Sistema IA Evolutivo', zorder=6)

# Future
for data, color in [(sp500_fut_scaled, C_SP), (avg_fut_scaled, C_AVG), (ai_fut_scaled, C_AI)]:
    median = np.median(data, axis=0)
    p10 = np.percentile(data, 10, axis=0)
    p90 = np.percentile(data, 90, axis=0)
    p25 = np.percentile(data, 25, axis=0)
    p75 = np.percentile(data, 75, axis=0)
    ax.plot(future_dates, median, color=color, linewidth=1.8, linestyle='--', zorder=4)
    ax.fill_between(future_dates, p25, p75, alpha=0.12, color=color, zorder=2)
    ax.fill_between(future_dates, p10, p90, alpha=0.05, color=color, zorder=1)

ax.axvline(x=hist_dates[-1], color='gray', linestyle=':', alpha=0.6, zorder=3)

# Annotations
ax.annotate(f'S&P 500: ${sp500_eq[-1]:.0f}', xy=(hist_dates[-1], sp500_eq[-1]),
            xytext=(15, 10), textcoords='offset points', fontsize=10, color=C_SP, fontweight='bold')
ax.annotate(f'IA Evolutivo: ${ai_eq[-1]:.0f}', xy=(hist_dates[-1], ai_eq[-1]),
            xytext=(15, 10), textcoords='offset points', fontsize=10, color=C_AI, fontweight='bold')
ax.annotate(f'Inversor Medio: ${avg_eq[-1]:.0f}', xy=(hist_dates[-1], avg_eq[-1]),
            xytext=(15, -15), textcoords='offset points', fontsize=10, color=C_AVG, fontweight='bold')

ax.set_title('Potencial del Sistema IA Evolutivo 2020-2030\n(Base $100 en Enero 2020 — Parametros Mejorando con el Tiempo)',
             fontsize=15, fontweight='bold', pad=15)
ax.set_ylabel('Valor ($)', fontsize=12)
ax.legend(loc='upper left', fontsize=12, framealpha=0.9)
ax.grid(True, alpha=0.2)
ax.set_xlim(hist_dates[0], future_dates[-1])
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'${x:.0f}'))

plt.tight_layout()
plt.savefig(f'{output_dir}/A1_potential_equity_curves.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart A1: Potential equity curves ✓")


# ----- CHART A2: Parameter Evolution -----
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.patch.set_facecolor(C_BG)
fig.suptitle('Evolucion de Parametros del Sistema IA\n(Como Mejora el Sistema con el Tiempo)',
             fontsize=14, fontweight='bold', y=0.98)

months = np.arange(0, total_months_full)
params_over_time = [get_evolving_params(m, total_months_full) for m in months]

# Year labels for x-axis
year_months = [0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132]
year_labels = ['2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031']

# Cash
ax = axes[0][0]
ax.set_facecolor(C_BG)
cash_vals = [p['base_cash'] for p in params_over_time]
ax.plot(months, cash_vals, color=C_AI, linewidth=2.5)
ax.fill_between(months, [p['min_cash'] for p in params_over_time],
                [p['max_cash'] for p in params_over_time], alpha=0.15, color=C_AI)
ax.set_title('Cash Medio (%)', fontweight='bold')
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x:.0%}'))
ax.set_xticks(year_months[:len(year_months)])
ax.set_xticklabels(year_labels[:len(year_months)], fontsize=8)
ax.grid(True, alpha=0.2)
ax.axvline(x=n_hist, color='gray', linestyle=':', alpha=0.5)

# Alpha vs Drag
ax = axes[0][1]
ax.set_facecolor(C_BG)
alpha_vals = [p['monthly_alpha'] * 1200 for p in params_over_time]  # annualized %
drag_vals = [p['monthly_drag'] * 1200 for p in params_over_time]
net_alpha = [a + d for a, d in zip(alpha_vals, drag_vals)]
ax.plot(months, alpha_vals, color='#16A34A', linewidth=2, label='Alpha (quality selection)')
ax.plot(months, drag_vals, color='#DC2626', linewidth=2, label='Drag (errores)')
ax.plot(months, net_alpha, color=C_AI, linewidth=2.5, label='Alpha NETO', linestyle='--')
ax.axhline(y=0, color='black', linewidth=0.5)
ax.set_title('Alpha vs Drag (% anual)', fontweight='bold')
ax.legend(fontsize=9)
ax.set_xticks(year_months[:len(year_months)])
ax.set_xticklabels(year_labels[:len(year_months)], fontsize=8)
ax.grid(True, alpha=0.2)
ax.axvline(x=n_hist, color='gray', linestyle=':', alpha=0.5)

# Crash beta
ax = axes[1][0]
ax.set_facecolor(C_BG)
severe_vals = [p['crash_beta_severe'] for p in params_over_time]
mild_vals = [p['crash_beta_mild'] for p in params_over_time]
ax.plot(months, severe_vals, color='#DC2626', linewidth=2, label='Beta crash severo (<-8%)')
ax.plot(months, mild_vals, color=C_AVG, linewidth=2, label='Beta crash leve (<-4%)')
ax.axhline(y=1.0, color='gray', linestyle='--', alpha=0.3, label='Mercado (beta=1)')
ax.set_title('Proteccion en Crashes (beta)', fontweight='bold')
ax.legend(fontsize=9)
ax.set_xticks(year_months[:len(year_months)])
ax.set_xticklabels(year_labels[:len(year_months)], fontsize=8)
ax.grid(True, alpha=0.2)
ax.axvline(x=n_hist, color='gray', linestyle=':', alpha=0.5)

# Idiosyncratic vol
ax = axes[1][1]
ax.set_facecolor(C_BG)
idio_vals = [p['idio_vol'] * np.sqrt(12) * 100 for p in params_over_time]  # annualized %
ax.plot(months, idio_vals, color=C_AI, linewidth=2.5)
ax.set_title('Volatilidad Idiosincratica (% anual)', fontweight='bold')
ax.set_xticks(year_months[:len(year_months)])
ax.set_xticklabels(year_labels[:len(year_months)], fontsize=8)
ax.grid(True, alpha=0.2)
ax.axvline(x=n_hist, color='gray', linestyle=':', alpha=0.5)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig(f'{output_dir}/A2_parameter_evolution.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart A2: Parameter evolution ✓")


# ----- CHART A3: Annual Returns Comparison -----
def annual_returns(monthly_rets, start_year=2020):
    annual = {}
    for i, r in enumerate(monthly_rets):
        year = start_year + i // 12
        if year not in annual:
            annual[year] = []
        annual[year].append(r)
    return {y: np.prod(1 + np.array(rs)) - 1 for y, rs in annual.items()}

sp500_ann = annual_returns(sp500_monthly)
avg_ann = annual_returns(avg_inv_ret)
ai_ann = annual_returns(ai_ret)

years = sorted(sp500_ann.keys())
last_year_months = sum(1 for i in range(n_hist) if 2020 + i//12 == years[-1])
if last_year_months < 6:
    years = years[:-1]

fig, ax = plt.subplots(figsize=(14, 7))
fig.patch.set_facecolor(C_BG)
ax.set_facecolor(C_BG)

x = np.arange(len(years))
w = 0.25

bars1 = ax.bar(x - w, [sp500_ann[y] for y in years], w, label='S&P 500', color=C_SP, alpha=0.85, zorder=3)
bars2 = ax.bar(x, [avg_ann[y] for y in years], w, label='Inversor Medio', color=C_AVG, alpha=0.85, zorder=3)
bars3 = ax.bar(x + w, [ai_ann[y] for y in years], w, label='Sistema IA Evolutivo', color=C_AI, alpha=0.85, zorder=3)

for bars in [bars1, bars2, bars3]:
    for bar in bars:
        h = bar.get_height()
        va = 'bottom' if h >= 0 else 'top'
        offset = 0.005 if h >= 0 else -0.005
        ax.text(bar.get_x() + bar.get_width()/2., h + offset, f'{h:.0%}',
                ha='center', va=va, fontsize=8, fontweight='bold')

ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=11)
ax.set_title('Retornos Anuales: S&P 500 vs Inversor Medio vs Sistema IA\n(Parametros del sistema mejorando cada ano)',
             fontsize=14, fontweight='bold', pad=15)
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x:.0%}'))
ax.legend(fontsize=11)
ax.grid(True, alpha=0.2, axis='y')
ax.axhline(y=0, color='black', linewidth=0.5)

plt.tight_layout()
plt.savefig(f'{output_dir}/A3_annual_returns_potential.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart A3: Annual returns ✓")


# ----- CHART A4: Drawdowns -----
def calc_drawdown(returns):
    equity = np.cumprod(1 + returns)
    peak = np.maximum.accumulate(equity)
    return (equity - peak) / peak

sp500_dd = calc_drawdown(sp500_monthly)
avg_dd = calc_drawdown(avg_inv_ret)
ai_dd = calc_drawdown(ai_ret)

dd_dates = hist_dates[1:]

fig, ax = plt.subplots(figsize=(15, 6))
fig.patch.set_facecolor(C_BG)
ax.set_facecolor(C_BG)

ax.fill_between(dd_dates, sp500_dd, 0, alpha=0.25, color=C_SP, label=f'S&P 500 (max: {np.min(sp500_dd):.1%})', zorder=2)
ax.fill_between(dd_dates, avg_dd, 0, alpha=0.25, color=C_AVG, label=f'Inversor Medio (max: {np.min(avg_dd):.1%})', zorder=2)
ax.plot(dd_dates, ai_dd, color=C_AI, linewidth=2, label=f'Sistema IA (max: {np.min(ai_dd):.1%})', zorder=4)

ax.set_title('Drawdowns: La Verdadera Ventaja del Sistema\n(El inversor medio sufre MAS que el mercado)',
             fontsize=14, fontweight='bold', pad=15)
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x:.0%}'))
ax.legend(loc='lower left', fontsize=11, framealpha=0.9)
ax.grid(True, alpha=0.2)

plt.tight_layout()
plt.savefig(f'{output_dir}/A4_drawdowns_potential.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart A4: Drawdowns ✓")


# ----- CHART A5: Cumulative Alpha vs Average Investor -----
# This is the KEY chart — shows the REAL edge is vs average investor, not vs index
alpha_vs_avg = np.cumprod(1 + ai_ret) / np.cumprod(1 + avg_inv_ret) - 1
alpha_vs_sp500 = np.cumprod(1 + ai_ret) / np.cumprod(1 + sp500_monthly) - 1

fig, ax = plt.subplots(figsize=(15, 7))
fig.patch.set_facecolor(C_BG)
ax.set_facecolor(C_BG)

ax.plot(dd_dates, alpha_vs_avg * 100, color=C_AI, linewidth=2.5,
        label=f'vs Inversor Medio: {alpha_vs_avg[-1]:+.1%}', zorder=4)
ax.plot(dd_dates, alpha_vs_sp500 * 100, color=C_SP, linewidth=2.5, linestyle='--',
        label=f'vs S&P 500: {alpha_vs_sp500[-1]:+.1%}', zorder=3)
ax.axhline(y=0, color='black', linewidth=1, zorder=1)

ax.fill_between(dd_dates, alpha_vs_avg * 100, 0,
                where=alpha_vs_avg > 0, alpha=0.15, color=C_AI, zorder=2)
ax.fill_between(dd_dates, alpha_vs_sp500 * 100, 0,
                where=alpha_vs_sp500 > 0, alpha=0.1, color=C_SP, zorder=2)

ax.set_title('Alpha Acumulado del Sistema IA\n(El benchmark correcto es el inversor medio, no el indice teorico)',
             fontsize=14, fontweight='bold', pad=15)
ax.set_ylabel('Alpha Acumulado (%)', fontsize=12)
ax.legend(fontsize=12, framealpha=0.9)
ax.grid(True, alpha=0.2)

plt.tight_layout()
plt.savefig(f'{output_dir}/A5_cumulative_alpha.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart A5: Cumulative alpha ✓")


# ----- CHART A6: Metrics Dashboard -----
fig, axes = plt.subplots(2, 3, figsize=(16, 9))
fig.patch.set_facecolor(C_BG)
fig.suptitle('Dashboard Comparativo: Periodo Historico 2020-2026', fontsize=16, fontweight='bold', y=0.98)

metrics_list = [
    ('CAGR', [sp500_m['cagr'], avg_m['cagr'], ai_m['cagr']], '{:.1%}'),
    ('Volatilidad', [sp500_m['volatility'], avg_m['volatility'], ai_m['volatility']], '{:.1%}'),
    ('Sharpe', [sp500_m['sharpe'], avg_m['sharpe'], ai_m['sharpe']], '{:.2f}'),
    ('Sortino', [sp500_m['sortino'], avg_m['sortino'], ai_m['sortino']], '{:.2f}'),
    ('Max Drawdown', [sp500_m['max_drawdown'], avg_m['max_drawdown'], ai_m['max_drawdown']], '{:.1%}'),
    ('Win Rate', [sp500_m['win_rate'], avg_m['win_rate'], ai_m['win_rate']], '{:.0%}'),
]

labels = ['S&P 500', 'Inversor\nMedio', 'Sistema\nIA']
colors = [C_SP, C_AVG, C_AI]

for idx, (title, values, fmt) in enumerate(metrics_list):
    ax = axes[idx // 3][idx % 3]
    ax.set_facecolor(C_BG)
    bars = ax.bar(range(3), [abs(v) for v in values], color=colors, alpha=0.85, zorder=3)
    for i, (bar, v) in enumerate(zip(bars, values)):
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + abs(bar.get_height())*0.02,
                fmt.format(v), ha='center', va='bottom', fontsize=12, fontweight='bold')
    ax.set_xticks(range(3))
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_title(title, fontsize=12, fontweight='bold', pad=8)
    ax.grid(True, alpha=0.2, axis='y')
    ax.set_ylim(0, max(abs(v) for v in values) * 1.3)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig(f'{output_dir}/A6_metrics_dashboard_potential.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart A6: Metrics dashboard ✓")


# ============================================================
# 8. PRINT FULL RESULTS
# ============================================================
print("\n" + "="*70)
print("RESULTADOS COMPLETOS — SIMULACION DE POTENCIAL")
print("="*70)

print("\n--- PERIODO HISTORICO (2020-Feb 2026) ---")
print(f"{'Metrica':<25} {'S&P 500':>12} {'Inv. Medio':>12} {'Sist. IA':>12}")
print("-" * 65)
for key, label in [
    ('total_return', 'Retorno Total'), ('cagr', 'CAGR'), ('volatility', 'Volatilidad'),
    ('sharpe', 'Sharpe Ratio'), ('sortino', 'Sortino Ratio'), ('max_drawdown', 'Max Drawdown'),
    ('win_rate', 'Win Rate'), ('best_month', 'Mejor Mes'), ('worst_month', 'Peor Mes'),
]:
    s, a, e = sp500_m[key], avg_m[key], ai_m[key]
    if key in ('sharpe', 'sortino'):
        print(f"{label:<25} {s:>12.2f} {a:>12.2f} {e:>12.2f}")
    else:
        print(f"{label:<25} {s:>11.1%} {a:>11.1%} {e:>11.1%}")

# Annual
print("\n--- RETORNOS ANUALES ---")
print(f"{'Ano':<6} {'S&P 500':>10} {'Inv. Medio':>12} {'Sist. IA':>10} {'IA vs Medio':>12}")
print("-" * 52)
for y in years:
    s, a, e = sp500_ann[y], avg_ann[y], ai_ann[y]
    print(f"{y:<6} {s:>9.1%} {a:>11.1%} {e:>9.1%} {e-a:>+11.1%}")

# Future projections
print("\n--- PROYECCIONES 2030 ---")
print(f"{'Percentil':<20} {'S&P 500':>12} {'Inv. Medio':>12} {'Sist. IA':>12}")
print("-" * 60)
for pct, label in [(10, 'P10'), (25, 'P25'), (50, 'Mediana'), (75, 'P75'), (90, 'P90')]:
    s = np.percentile(sp500_fut_scaled[:,-1], pct)
    a = np.percentile(avg_fut_scaled[:,-1], pct)
    e = np.percentile(ai_fut_scaled[:,-1], pct)
    print(f"{label:<20} ${s:>11.0f} ${a:>11.0f} ${e:>11.0f}")

# Full 2020-2030 CAGR
print("\n--- CAGR 2020-2030 COMPLETO ---")
for data, label in [
    (sp500_fut_scaled[:,-1], 'S&P 500'),
    (avg_fut_scaled[:,-1], 'Inversor Medio'),
    (ai_fut_scaled[:,-1], 'Sistema IA'),
]:
    p10, p50, p90 = [np.percentile(data, p) for p in [10, 50, 90]]
    c10 = (p10/100)**(1/11) - 1
    c50 = (p50/100)**(1/11) - 1
    c90 = (p90/100)**(1/11) - 1
    print(f"  {label}: CAGR mediana {c50:.1%} (rango {c10:.1%} a {c90:.1%})")

# Key comparison
print("\n--- VENTAJA CLAVE ---")
ai_vs_avg_total = (ai_eq[-1] / avg_eq[-1] - 1)
ai_vs_sp_total = (ai_eq[-1] / sp500_eq[-1] - 1)
print(f"  Sistema IA vs Inversor Medio (hist): {ai_vs_avg_total:+.1%}")
print(f"  Sistema IA vs S&P 500 (hist): {ai_vs_sp_total:+.1%}")

# Parameter state at key moments
print("\n--- EVOLUCION DE PARAMETROS CLAVE ---")
for month, label in [(0, '2020 (inicio)'), (36, '2023 (3 anos)'), (72, '2026 (6 anos)'), (120, '2030 (10 anos)')]:
    p = get_evolving_params(month, total_months_full)
    net = (p['monthly_alpha'] + p['monthly_drag']) * 1200
    print(f"  {label}: Cash {p['base_cash']:.0%} | Alpha neto {net:+.1f}%/a | Crash beta {p['crash_beta_severe']:.2f}")

print(f"\nCharts en: {output_dir}/")
print("Simulacion completada.")
