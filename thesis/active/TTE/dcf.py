#!/usr/bin/env python3
"""TotalEnergies (TTE) Independent DCF Valuation - Conservative
PRICES FROM YFINANCE - NEVER HARDCODE"""

import yfinance as yf

# Live data
stock = yf.Ticker('TTE')
info = stock.info
price_usd = info.get('currentPrice') or info.get('regularMarketPrice') or info.get('previousClose')
eurusd = yf.Ticker('EURUSD=X').info.get('previousClose', 1.04)
price_eur = price_usd / eurusd

shares = 2.297  # Billion
net_debt = 25.0  # $B conservative (Q3 2025 gearing 17.3%)
mcap = price_usd * shares
ev = mcap + net_debt

print("=" * 60)
print("TOTALENERGIES DCF VALUATION (CONSERVATIVE)")
print(f"LIVE PRICE: ${price_usd:.2f} USD = €{price_eur:.2f} EUR")
print(f"EUR/USD: {eurusd:.4f}")
print("=" * 60)
print(f"Market Cap: ${mcap:.1f}B | EV: ${ev:.1f}B")
print(f"Shares: {shares}B")

# DCF: Base FCF $14B, growth 5%/3%/1%, WACC 9%, TG 2%
base_fcf = 14.0
wacc = 0.09
tg = 0.02

fcfs = []
f = base_fcf
for yr in range(1, 11):
    if yr <= 3: f *= 1.05
    elif yr <= 5: f *= 1.03
    else: f *= 1.01
    fcfs.append(f)

tv = fcfs[-1] * (1 + tg) / (wacc - tg)
pv_f = sum(cf / (1 + wacc)**(i+1) for i, cf in enumerate(fcfs))
pv_t = tv / (1 + wacc)**10
eq = pv_f + pv_t - net_debt
fv_eur = (eq / shares) / eurusd
mos = (fv_eur - price_eur) / fv_eur * 100

print(f"\nDCF BASE CASE:")
print(f"  Base FCF: $14B | WACC: 9% | TG: 2%")
for i, cf in enumerate(fcfs):
    print(f"  Yr{i+1}: ${cf:.2f}B")
print(f"  Terminal Value: ${tv:.1f}B")
print(f"  PV FCFs: ${pv_f:.1f}B | PV TV: ${pv_t:.1f}B")
print(f"  Equity: ${eq:.1f}B")
print(f"  FAIR VALUE: EUR {fv_eur:.2f} | MoS: {mos:.1f}%")

# Scenarios
print("\nSCENARIO ANALYSIS:")
scenarios = [
    ("BEAR ($55 Brent)", 11, 0.02, 0.01, 0.00, 0.10, 0.015),
    ("BASE (conservative)", 14, 0.05, 0.03, 0.01, 0.09, 0.02),
    ("MODERATE ($70 Brent)", 16, 0.06, 0.04, 0.02, 0.085, 0.02),
    ("BULL ($80+ Brent)", 18, 0.08, 0.05, 0.02, 0.08, 0.025),
]
for name, bf, g1, g2, g3, w, t in scenarios:
    fs = []
    ff = bf
    for yr in range(1, 11):
        if yr <= 3: ff *= (1+g1)
        elif yr <= 5: ff *= (1+g2)
        else: ff *= (1+g3)
        fs.append(ff)
    tvv = fs[-1]*(1+t)/(w-t)
    pvf = sum(c/(1+w)**(i+1) for i,c in enumerate(fs))
    pvt = tvv/(1+w)**10
    eqq = pvf+pvt-net_debt
    fvv = (eqq/shares)/eurusd
    m = (fvv-price_eur)/fvv*100
    print(f"  {name}: EUR {fvv:.0f} | MoS {m:.0f}% | {'PASS' if m>=25 else 'FAIL'}")

# Sensitivity
print(f"\nSENSITIVITY (EUR fair value) @ price €{price_eur:.2f}:")
print(f"{'WACC':<8} TG=1.5%  TG=2.0%  TG=2.5%")
for w in [0.08, 0.085, 0.09, 0.095, 0.10]:
    row = f"{w*100:.1f}%    "
    for t in [0.015, 0.02, 0.025]:
        fs = []
        ff = 14.0
        for yr in range(1,11):
            if yr<=3: ff*=1.05
            elif yr<=5: ff*=1.03
            else: ff*=1.01
            fs.append(ff)
        tvv = fs[-1]*(1+t)/(w-t)
        pvf = sum(c/(1+w)**(i+1) for i,c in enumerate(fs))
        pvt = tvv/(1+w)**10
        eqq = pvf+pvt-net_debt
        fvv = (eqq/shares)/eurusd
        m = (fvv-price_eur)/fvv*100
        mark = "*" if m>=25 else " "
        row += f"{fvv:>6.0f}{mark}  "
    print(row)
print("* = MoS >= 25%")

# Comparables
print("\nCOMPARABLE VALUATION:")
pe_ttm = info.get('trailingPE', 9.9)
eps = price_eur / pe_ttm if pe_ttm else price_eur / 9.9
fv_pe = eps * 10.9  # peer avg P/E
div = info.get('dividendRate', 3.46)  # USD annual dividend
div_eur = div / eurusd
div_yield_peer = 0.051
fv_div = div_eur / div_yield_peer
fv_eveb = ((38*4.1 - net_debt)/shares)/eurusd
blended = (fv_pe + fv_div + fv_eveb) / 3
mos_comp = (blended - price_eur) / blended * 100
print(f"  P/E method (10.9x peer avg): EUR {fv_pe:.0f}")
print(f"  Yield method (5.1% peer avg): EUR {fv_div:.0f}")
print(f"  EV/EBITDA (4.1x peer avg): EUR {fv_eveb:.0f}")
print(f"  Blended: EUR {blended:.0f} | MoS: {mos_comp:.0f}%")

# Final weighted (DCF 40%, Comps 30%, Bull 15%, Moderate 15%)
# Recalc moderate and bull for weighting
def calc_fv(bf, g1, g2, g3, w, t):
    fs, ff = [], bf
    for yr in range(1,11):
        if yr<=3: ff*=(1+g1)
        elif yr<=5: ff*=(1+g2)
        else: ff*=(1+g3)
        fs.append(ff)
    tvv = fs[-1]*(1+t)/(w-t)
    pvf = sum(c/(1+w)**(i+1) for i,c in enumerate(fs))
    pvt = tvv/(1+w)**10
    return (pvf+pvt-net_debt)/shares/eurusd

fv_moderate = calc_fv(16, 0.06, 0.04, 0.02, 0.085, 0.02)
fv_bull = calc_fv(18, 0.08, 0.05, 0.02, 0.08, 0.025)

wtd = fv_eur*0.4 + blended*0.3 + fv_moderate*0.15 + fv_bull*0.15
mos_final = (wtd - price_eur)/wtd*100
print("\n" + "=" * 60)
print(f"WEIGHTED FAIR VALUE: EUR {wtd:.0f}")
print(f"CURRENT PRICE: EUR {price_eur:.2f}")
print(f"MARGIN OF SAFETY: {mos_final:.0f}%")
print(f"VERDICT: {'BUY CONFIRMED' if mos_final >= 25 else 'NEEDS REVIEW - MoS < 25%'}")
if mos_final >= 25:
    max_pos = 0.07 * 11006  # 7% of ~€11K portfolio
    n_shares = int(max_pos / price_usd)
    print(f"MAX POSITION: EUR {max_pos:.0f} (~{n_shares} shares @ ${price_usd:.2f})")
