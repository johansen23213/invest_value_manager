#!/usr/bin/env python3
"""
System Performance Simulation 2020-2030
Compares: S&P 500 vs Current System (v4.0) vs Enhanced System (+ contrathesis)

DISCLAIMER: This is a SIMULATION with transparent assumptions.
The only real data is the S&P 500 historical returns.
Both system curves are MODELED based on behavioral parameters.
This is NOT a backtest — the systems didn't exist before 2026.
Hindsight bias contaminates the entire historical period.
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

# Monthly returns
sp500_monthly = np.diff(sp500_close) / sp500_close[:-1]
n_hist = len(sp500_monthly)
print(f"  {n_hist} meses de datos S&P 500 ({sp500.index[0].strftime('%Y-%m')} a {sp500.index[-1].strftime('%Y-%m')})")

# ============================================================
# 2. SYSTEM SIMULATION ENGINE
# ============================================================

def simulate_system(mkt_returns, params, rf_schedule=None):
    """
    Simulate system returns based on behavioral parameters.

    This is a FACTOR MODEL, not stock picking.
    It models the system's behavioral characteristics:
    - Cash allocation (high = conservative)
    - Quality beta (lower than market)
    - Alpha from quality selection
    - Drag from process errors
    """
    returns = []
    cash_levels = []

    for i, mkt_r in enumerate(mkt_returns):
        # Trailing 6-month annualized return for regime detection
        if i >= 6:
            trailing = np.mean(mkt_returns[i-5:i+1]) * 12
        elif i >= 1:
            trailing = np.mean(mkt_returns[:i+1]) * 12
        else:
            trailing = mkt_r * 12

        # Cash allocation — driven by market regime
        base = params['base_cash']
        if trailing > 0.20:      # Hot market → more cautious
            cash = base + 0.12
        elif trailing < -0.15:   # Crash → deploy (but slowly)
            cash = base - 0.08
        elif trailing < -0.05:   # Correction
            cash = base - 0.04
        else:
            cash = base

        cash += np.random.normal(0, 0.02)
        cash = np.clip(cash, params['min_cash'], params['max_cash'])
        cash_levels.append(cash)

        invested = 1 - cash
        beta = params['quality_beta']

        # Quality protects in drawdowns
        if mkt_r < -0.08:
            beta = params['crash_beta_severe']
        elif mkt_r < -0.04:
            beta = params['crash_beta_mild']

        # Risk-free rate
        if rf_schedule and i < len(rf_schedule):
            rf = rf_schedule[i]
        else:
            rf = 0.035 / 12  # default 3.5% annual

        alpha = params['monthly_alpha']
        drag = params['monthly_drag']

        # Idiosyncratic noise (concentrated portfolio = more vol)
        idio = np.random.normal(0, params['idio_vol'])

        sys_r = invested * (mkt_r * beta + alpha + drag + idio) + cash * rf
        returns.append(sys_r)

    return np.array(returns), np.array(cash_levels)


# Risk-free rate schedule (approximate, monthly)
rf_schedule = []
for i in range(n_hist):
    if i < 24:      # 2020-2021: ~0.5%
        rf_schedule.append(0.005 / 12)
    elif i < 30:    # H1 2022: rising
        rf_schedule.append(0.015 / 12)
    elif i < 36:    # H2 2022: higher
        rf_schedule.append(0.035 / 12)
    elif i < 48:    # 2023
        rf_schedule.append(0.045 / 12)
    else:           # 2024-2026
        rf_schedule.append(0.04 / 12)


# CURRENT SYSTEM — Framework v4.0
# Assumptions documented in simulation_doc.md
current_params = {
    'base_cash': 0.47,           # A1: High cash (observed: 59% currently)
    'min_cash': 0.25,
    'max_cash': 0.65,
    'quality_beta': 0.73,        # A2: Quality companies, lower beta
    'crash_beta_mild': 0.62,     # A3: Quality holds up in mild crashes
    'crash_beta_severe': 0.50,   # A3: Quality holds up more in severe crashes
    'monthly_alpha': 0.0013,     # A4: ~1.6% annual from quality selection
    'monthly_drag': -0.0012,     # A5: ~-1.4% annual from FV inflation, slow deploy, mistakes
    'idio_vol': 0.008,           # A6: Concentrated portfolio noise
}

# ENHANCED SYSTEM — Framework v4.0 + contrathesis knowledge
enhanced_params = {
    'base_cash': 0.43,           # B1: Slightly less cash (better at identifying real MoS)
    'min_cash': 0.20,
    'max_cash': 0.60,
    'quality_beta': 0.73,        # B2: Same quality factor
    'crash_beta_mild': 0.58,     # B3: Credit signals = slightly earlier risk reduction
    'crash_beta_severe': 0.45,   # B3: Better drawdown protection
    'monthly_alpha': 0.0016,     # B4: ~1.9% annual (fewer consensus traps)
    'monthly_drag': -0.0004,     # B5: ~-0.5% annual (reverse DCF prevents FV inflation)
    'idio_vol': 0.007,           # B6: Slightly less noise (fewer mistakes)
}

print("Simulando sistema actual...")
current_ret, current_cash = simulate_system(sp500_monthly, current_params, rf_schedule)

print("Simulando sistema mejorado...")
enhanced_ret, enhanced_cash = simulate_system(sp500_monthly, enhanced_params, rf_schedule)


# ============================================================
# 3. MONTE CARLO 2026-2030
# ============================================================
n_future = 59   # Mar 2026 to Dec 2030
n_sims = 1000

print(f"Monte Carlo: {n_sims} simulaciones x {n_future} meses...")

# S&P 500 future: use historical monthly distribution
hist_mean = np.mean(sp500_monthly)
hist_std = np.std(sp500_monthly)
# Add slight fat tails
sp500_future = np.random.normal(hist_mean, hist_std, (n_sims, n_future))
# Add occasional fat tail events (5% probability of 2x vol)
fat_tail_mask = np.random.random((n_sims, n_future)) < 0.05
sp500_future[fat_tail_mask] *= 2.0

future_rf = [0.035 / 12] * n_future

sp500_future_eq = np.cumprod(1 + sp500_future, axis=1)
current_future_eq = np.zeros((n_sims, n_future))
enhanced_future_eq = np.zeros((n_sims, n_future))

for s in range(n_sims):
    c_ret, _ = simulate_system(sp500_future[s], current_params, future_rf)
    e_ret, _ = simulate_system(sp500_future[s], enhanced_params, future_rf)
    current_future_eq[s] = np.cumprod(1 + c_ret)
    enhanced_future_eq[s] = np.cumprod(1 + e_ret)


# ============================================================
# 4. BUILD EQUITY CURVES
# ============================================================
sp500_eq = np.concatenate([[100], 100 * np.cumprod(1 + sp500_monthly)])
current_eq = np.concatenate([[100], 100 * np.cumprod(1 + current_ret)])
enhanced_eq = np.concatenate([[100], 100 * np.cumprod(1 + enhanced_ret)])

hist_dates = date_range('2020-01-01', periods=len(sp500_eq), freq='ME')
future_dates = date_range(hist_dates[-1], periods=n_future+1, freq='ME')[1:]

# Scale future equity from last historical value
sp500_fut_scaled = sp500_future_eq * sp500_eq[-1]
current_fut_scaled = current_future_eq * current_eq[-1]
enhanced_fut_scaled = enhanced_future_eq * enhanced_eq[-1]


# ============================================================
# 5. CALCULATE METRICS
# ============================================================

def calc_metrics(returns, label):
    """Calculate key performance metrics."""
    total_ret = np.prod(1 + returns) - 1
    n_years = len(returns) / 12
    cagr = (1 + total_ret) ** (1/n_years) - 1
    vol = np.std(returns) * np.sqrt(12)

    # Sharpe (excess over risk-free ~3%)
    excess = returns - 0.03/12
    sharpe = np.mean(excess) / np.std(returns) * np.sqrt(12) if np.std(returns) > 0 else 0

    # Sortino
    downside = returns[returns < 0]
    downside_vol = np.std(downside) * np.sqrt(12) if len(downside) > 0 else 0.001
    sortino = (np.mean(returns) * 12 - 0.03) / downside_vol

    # Max drawdown
    equity = np.cumprod(1 + returns)
    peak = np.maximum.accumulate(equity)
    drawdown = (equity - peak) / peak
    max_dd = np.min(drawdown)

    # Win rate
    win_rate = np.mean(returns > 0)

    # Best/worst month
    best = np.max(returns)
    worst = np.min(returns)

    return {
        'label': label,
        'total_return': total_ret,
        'cagr': cagr,
        'volatility': vol,
        'sharpe': sharpe,
        'sortino': sortino,
        'max_drawdown': max_dd,
        'win_rate': win_rate,
        'best_month': best,
        'worst_month': worst,
    }

sp500_metrics = calc_metrics(sp500_monthly, 'S&P 500')
current_metrics = calc_metrics(current_ret, 'Sistema Actual')
enhanced_metrics = calc_metrics(enhanced_ret, 'Sistema + Contrathesis')

print("\n=== MÉTRICAS 2020-2026 (Histórico) ===")
for m in [sp500_metrics, current_metrics, enhanced_metrics]:
    print(f"\n{m['label']}:")
    print(f"  Retorno Total: {m['total_return']:.1%}")
    print(f"  CAGR: {m['cagr']:.1%}")
    print(f"  Volatilidad: {m['volatility']:.1%}")
    print(f"  Sharpe: {m['sharpe']:.2f}")
    print(f"  Sortino: {m['sortino']:.2f}")
    print(f"  Max Drawdown: {m['max_drawdown']:.1%}")
    print(f"  Win Rate: {m['win_rate']:.1%}")


# ============================================================
# 6. CHARTS
# ============================================================

# Color scheme
C_SP = '#2563EB'     # Blue
C_CUR = '#DC2626'    # Red
C_ENH = '#16A34A'    # Green
C_BG = '#FAFAFA'

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 11

# ----- CHART 1: Equity Curves -----
fig, ax = plt.subplots(figsize=(15, 8))
fig.patch.set_facecolor(C_BG)
ax.set_facecolor(C_BG)

# Historical
ax.plot(hist_dates, sp500_eq, color=C_SP, linewidth=2.2, label='S&P 500', zorder=5)
ax.plot(hist_dates, current_eq, color=C_CUR, linewidth=2.2, label='Sistema Actual (v4.0)', zorder=5)
ax.plot(hist_dates, enhanced_eq, color=C_ENH, linewidth=2.2, label='Sistema + Contrathesis', zorder=5)

# Future: median + P10/P90 bands
for data, color, label in [
    (sp500_fut_scaled, C_SP, 'S&P 500'),
    (current_fut_scaled, C_CUR, 'Sistema Actual'),
    (enhanced_fut_scaled, C_ENH, 'Sistema + Contrathesis'),
]:
    median = np.median(data, axis=0)
    p10 = np.percentile(data, 10, axis=0)
    p90 = np.percentile(data, 90, axis=0)
    p25 = np.percentile(data, 25, axis=0)
    p75 = np.percentile(data, 75, axis=0)

    ax.plot(future_dates, median, color=color, linewidth=1.5, linestyle='--', zorder=4)
    ax.fill_between(future_dates, p25, p75, alpha=0.15, color=color, zorder=2)
    ax.fill_between(future_dates, p10, p90, alpha=0.06, color=color, zorder=1)

# Divider line
ax.axvline(x=hist_dates[-1], color='gray', linestyle=':', alpha=0.6, zorder=3)
ylim = ax.get_ylim()
ax.text(hist_dates[-2], ylim[1]*0.97, 'Histórico', ha='right', fontsize=10, color='gray', style='italic')
ax.text(future_dates[1], ylim[1]*0.97, 'Proyección (Monte Carlo)', ha='left', fontsize=10, color='gray', style='italic')

ax.set_title('Simulación 2020-2030: Curvas de Equity\n(Base $100, Enero 2020)', fontsize=15, fontweight='bold', pad=15)
ax.set_ylabel('Valor ($)', fontsize=12)
ax.legend(loc='upper left', fontsize=11, framealpha=0.9)
ax.grid(True, alpha=0.2)
ax.set_xlim(hist_dates[0], future_dates[-1])
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'${x:.0f}'))

plt.tight_layout()
plt.savefig(f'{output_dir}/01_equity_curves.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 1: Equity curves ✓")


# ----- CHART 2: Annual Returns -----
def annual_returns_from_monthly(monthly_returns, start_year=2020):
    """Calculate annual returns from monthly returns."""
    annual = {}
    for i, r in enumerate(monthly_returns):
        year = start_year + i // 12
        if year not in annual:
            annual[year] = []
        annual[year].append(r)

    result = {}
    for year, rets in annual.items():
        result[year] = np.prod(1 + np.array(rets)) - 1
    return result

sp500_annual = annual_returns_from_monthly(sp500_monthly)
current_annual = annual_returns_from_monthly(current_ret)
enhanced_annual = annual_returns_from_monthly(enhanced_ret)

years = sorted(sp500_annual.keys())
# Exclude last year if incomplete and <6 months
last_year = years[-1]
# Count months in last year
last_year_months = sum(1 for i in range(len(sp500_monthly)) if 2020 + i//12 == last_year)
if last_year_months < 6:
    years = years[:-1]

fig, ax = plt.subplots(figsize=(14, 7))
fig.patch.set_facecolor(C_BG)
ax.set_facecolor(C_BG)

x = np.arange(len(years))
width = 0.25

bars1 = ax.bar(x - width, [sp500_annual[y] for y in years], width, label='S&P 500', color=C_SP, alpha=0.85, zorder=3)
bars2 = ax.bar(x, [current_annual[y] for y in years], width, label='Sistema Actual', color=C_CUR, alpha=0.85, zorder=3)
bars3 = ax.bar(x + width, [enhanced_annual[y] for y in years], width, label='Sistema + Contrathesis', color=C_ENH, alpha=0.85, zorder=3)

# Add value labels
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        h = bar.get_height()
        va = 'bottom' if h >= 0 else 'top'
        offset = 0.005 if h >= 0 else -0.005
        ax.text(bar.get_x() + bar.get_width()/2., h + offset, f'{h:.0%}',
                ha='center', va=va, fontsize=8, fontweight='bold')

ax.set_xticks(x)
ax.set_xticklabels(years, fontsize=11)
ax.set_title('Retornos Anuales: S&P 500 vs Sistemas\n(2020-2025)', fontsize=15, fontweight='bold', pad=15)
ax.set_ylabel('Retorno Anual', fontsize=12)
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x:.0%}'))
ax.legend(fontsize=11)
ax.grid(True, alpha=0.2, axis='y')
ax.axhline(y=0, color='black', linewidth=0.5)

plt.tight_layout()
plt.savefig(f'{output_dir}/02_annual_returns.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 2: Annual returns ✓")


# ----- CHART 3: Drawdowns -----
def calc_drawdown(returns):
    equity = np.cumprod(1 + returns)
    peak = np.maximum.accumulate(equity)
    return (equity - peak) / peak

sp500_dd = calc_drawdown(sp500_monthly)
current_dd = calc_drawdown(current_ret)
enhanced_dd = calc_drawdown(enhanced_ret)

dd_dates = hist_dates[1:]  # drawdown starts from first return

fig, ax = plt.subplots(figsize=(15, 6))
fig.patch.set_facecolor(C_BG)
ax.set_facecolor(C_BG)

ax.fill_between(dd_dates, sp500_dd, 0, alpha=0.3, color=C_SP, label=f'S&P 500 (max: {np.min(sp500_dd):.1%})', zorder=2)
ax.plot(dd_dates, current_dd, color=C_CUR, linewidth=1.5, label=f'Sistema Actual (max: {np.min(current_dd):.1%})', zorder=3)
ax.plot(dd_dates, enhanced_dd, color=C_ENH, linewidth=1.5, label=f'Sistema + Contrathesis (max: {np.min(enhanced_dd):.1%})', zorder=4)

ax.set_title('Drawdowns desde Máximos\n(2020-2026)', fontsize=15, fontweight='bold', pad=15)
ax.set_ylabel('Drawdown', fontsize=12)
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x:.0%}'))
ax.legend(loc='lower left', fontsize=11, framealpha=0.9)
ax.grid(True, alpha=0.2)
ax.set_xlim(dd_dates[0], dd_dates[-1])

plt.tight_layout()
plt.savefig(f'{output_dir}/03_drawdowns.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 3: Drawdowns ✓")


# ----- CHART 4: Rolling Sharpe (12-month) -----
def rolling_sharpe(returns, window=12, rf_annual=0.03):
    sharpes = []
    for i in range(window, len(returns)):
        r = returns[i-window:i]
        excess = r - rf_annual/12
        if np.std(r) > 0:
            sharpes.append(np.mean(excess) / np.std(r) * np.sqrt(12))
        else:
            sharpes.append(0)
    return np.array(sharpes)

sp500_sharpe = rolling_sharpe(sp500_monthly)
current_sharpe = rolling_sharpe(current_ret)
enhanced_sharpe = rolling_sharpe(enhanced_ret)

sharpe_dates = hist_dates[13:]  # 12-month window starts from month 13

fig, ax = plt.subplots(figsize=(15, 6))
fig.patch.set_facecolor(C_BG)
ax.set_facecolor(C_BG)

ax.plot(sharpe_dates, sp500_sharpe, color=C_SP, linewidth=1.8, label='S&P 500', zorder=3)
ax.plot(sharpe_dates, current_sharpe, color=C_CUR, linewidth=1.8, label='Sistema Actual', zorder=3)
ax.plot(sharpe_dates, enhanced_sharpe, color=C_ENH, linewidth=1.8, label='Sistema + Contrathesis', zorder=3)

ax.axhline(y=0, color='black', linewidth=0.5, zorder=1)
ax.axhline(y=1, color='gray', linewidth=0.5, linestyle='--', alpha=0.5, zorder=1)
ax.axhline(y=-1, color='gray', linewidth=0.5, linestyle='--', alpha=0.5, zorder=1)

ax.set_title('Sharpe Ratio Rolling 12 Meses\n(2021-2026)', fontsize=15, fontweight='bold', pad=15)
ax.set_ylabel('Sharpe Ratio (12m)', fontsize=12)
ax.legend(fontsize=11, framealpha=0.9)
ax.grid(True, alpha=0.2)

plt.tight_layout()
plt.savefig(f'{output_dir}/04_rolling_sharpe.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 4: Rolling Sharpe ✓")


# ----- CHART 5: Cash Allocation Over Time -----
fig, ax = plt.subplots(figsize=(15, 5))
fig.patch.set_facecolor(C_BG)
ax.set_facecolor(C_BG)

cash_dates = hist_dates[1:]
ax.fill_between(cash_dates, current_cash, alpha=0.3, color=C_CUR, label='Cash — Sistema Actual', zorder=2)
ax.plot(cash_dates, enhanced_cash, color=C_ENH, linewidth=2, label='Cash — Sistema + Contrathesis', zorder=3)

ax.set_title('Nivel de Cash a lo Largo del Tiempo\n(2020-2026)', fontsize=15, fontweight='bold', pad=15)
ax.set_ylabel('% en Cash', fontsize=12)
ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x:.0%}'))
ax.legend(fontsize=11, framealpha=0.9)
ax.grid(True, alpha=0.2)
ax.set_ylim(0.1, 0.75)

plt.tight_layout()
plt.savefig(f'{output_dir}/05_cash_allocation.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 5: Cash allocation ✓")


# ----- CHART 6: Metrics Dashboard -----
fig, axes = plt.subplots(2, 3, figsize=(16, 9))
fig.patch.set_facecolor(C_BG)
fig.suptitle('Dashboard de Métricas: Período Histórico 2020-2026', fontsize=16, fontweight='bold', y=0.98)

metrics_list = [
    ('CAGR', [sp500_metrics['cagr'], current_metrics['cagr'], enhanced_metrics['cagr']], '{:.1%}'),
    ('Volatilidad Anual', [sp500_metrics['volatility'], current_metrics['volatility'], enhanced_metrics['volatility']], '{:.1%}'),
    ('Sharpe Ratio', [sp500_metrics['sharpe'], current_metrics['sharpe'], enhanced_metrics['sharpe']], '{:.2f}'),
    ('Sortino Ratio', [sp500_metrics['sortino'], current_metrics['sortino'], enhanced_metrics['sortino']], '{:.2f}'),
    ('Max Drawdown', [sp500_metrics['max_drawdown'], current_metrics['max_drawdown'], enhanced_metrics['max_drawdown']], '{:.1%}'),
    ('Win Rate (mensual)', [sp500_metrics['win_rate'], current_metrics['win_rate'], enhanced_metrics['win_rate']], '{:.0%}'),
]

labels = ['S&P 500', 'Sistema\nActual', 'Sistema +\nContrathesis']
colors = [C_SP, C_CUR, C_ENH]

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
    ax.set_ylim(0, max(abs(v) for v in values) * 1.25)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig(f'{output_dir}/06_metrics_dashboard.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 6: Metrics dashboard ✓")


# ----- CHART 7: Monte Carlo Distribution of Final Values (2030) -----
fig, ax = plt.subplots(figsize=(14, 7))
fig.patch.set_facecolor(C_BG)
ax.set_facecolor(C_BG)

# Final values at end of 2030
sp500_final = sp500_fut_scaled[:, -1]
current_final = current_fut_scaled[:, -1]
enhanced_final = enhanced_fut_scaled[:, -1]

bins = np.linspace(
    min(sp500_final.min(), current_final.min(), enhanced_final.min()) * 0.9,
    max(sp500_final.max(), current_final.max(), enhanced_final.max()) * 0.5,  # trim extreme right tail
    60
)

ax.hist(sp500_final, bins=bins, alpha=0.4, color=C_SP, label=f'S&P 500 (mediana: ${np.median(sp500_final):.0f})', density=True, zorder=2)
ax.hist(current_final, bins=bins, alpha=0.4, color=C_CUR, label=f'Sistema Actual (mediana: ${np.median(current_final):.0f})', density=True, zorder=2)
ax.hist(enhanced_final, bins=bins, alpha=0.4, color=C_ENH, label=f'Sistema + Contrathesis (mediana: ${np.median(enhanced_final):.0f})', density=True, zorder=2)

# Vertical medians
ax.axvline(np.median(sp500_final), color=C_SP, linewidth=2, linestyle='--', zorder=4)
ax.axvline(np.median(current_final), color=C_CUR, linewidth=2, linestyle='--', zorder=4)
ax.axvline(np.median(enhanced_final), color=C_ENH, linewidth=2, linestyle='--', zorder=4)

ax.set_title('Distribución de Valores Finales a Diciembre 2030\n(Monte Carlo, 1000 simulaciones, base $100 en 2020)', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Valor Final ($)', fontsize=12)
ax.set_ylabel('Densidad', fontsize=12)
ax.legend(fontsize=11, framealpha=0.9)
ax.grid(True, alpha=0.2)
ax.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'${x:.0f}'))

plt.tight_layout()
plt.savefig(f'{output_dir}/07_monte_carlo_distribution.png', dpi=150, bbox_inches='tight')
plt.close()
print("Chart 7: Monte Carlo distribution ✓")


# ============================================================
# 7. PRINT FULL METRICS FOR DOCUMENT
# ============================================================
print("\n" + "="*70)
print("MÉTRICAS COMPLETAS PARA DOCUMENTO")
print("="*70)

# Historical period
print("\n--- PERÍODO HISTÓRICO (2020-Feb 2026) ---")
print(f"{'Métrica':<25} {'S&P 500':>12} {'Sist. Actual':>12} {'Sist. Enh.':>12}")
print("-" * 65)
for key, label in [
    ('total_return', 'Retorno Total'),
    ('cagr', 'CAGR'),
    ('volatility', 'Volatilidad'),
    ('sharpe', 'Sharpe Ratio'),
    ('sortino', 'Sortino Ratio'),
    ('max_drawdown', 'Max Drawdown'),
    ('win_rate', 'Win Rate'),
    ('best_month', 'Mejor Mes'),
    ('worst_month', 'Peor Mes'),
]:
    s = sp500_metrics[key]
    c = current_metrics[key]
    e = enhanced_metrics[key]
    if key in ('sharpe', 'sortino'):
        print(f"{label:<25} {s:>12.2f} {c:>12.2f} {e:>12.2f}")
    else:
        print(f"{label:<25} {s:>11.1%} {c:>11.1%} {e:>11.1%}")

# Annual returns
print("\n--- RETORNOS ANUALES ---")
print(f"{'Año':<8} {'S&P 500':>10} {'Sist. Actual':>12} {'Sist. Enh.':>12} {'Diff Actual':>12}")
print("-" * 55)
for y in years:
    s = sp500_annual.get(y, 0)
    c = current_annual.get(y, 0)
    e = enhanced_annual.get(y, 0)
    diff = c - s
    print(f"{y:<8} {s:>9.1%} {c:>11.1%} {e:>11.1%} {diff:>11.1%}")

# Monte Carlo projections
print("\n--- PROYECCIONES 2030 (Monte Carlo, mediana y percentiles) ---")
print(f"{'Métrica':<25} {'S&P 500':>12} {'Sist. Actual':>12} {'Sist. Enh.':>12}")
print("-" * 65)
for pct, label in [(10, 'P10 (pesimista)'), (25, 'P25'), (50, 'Mediana'), (75, 'P75'), (90, 'P90 (optimista)')]:
    s = np.percentile(sp500_final, pct)
    c = np.percentile(current_final, pct)
    e = np.percentile(enhanced_final, pct)
    print(f"{label:<25} ${s:>11.0f} ${c:>11.0f} ${e:>11.0f}")

# Calculate projected CAGR range (2020-2030 full period)
print("\n--- CAGR PROYECTADO 2020-2030 (rango P10-P90) ---")
for data, label in [(sp500_final, 'S&P 500'), (current_final, 'Sistema Actual'), (enhanced_final, 'Sistema + Contrathesis')]:
    p10 = np.percentile(data, 10)
    p50 = np.percentile(data, 50)
    p90 = np.percentile(data, 90)
    cagr_10 = (p10/100)**(1/11) - 1
    cagr_50 = (p50/100)**(1/11) - 1
    cagr_90 = (p90/100)**(1/11) - 1
    print(f"  {label}: CAGR mediana {cagr_50:.1%} (rango {cagr_10:.1%} a {cagr_90:.1%})")

print(f"\nCharts guardados en: {output_dir}/")
print("Simulación completada.")
