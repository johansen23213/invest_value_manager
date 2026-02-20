#!/usr/bin/env python3
"""
Quality Scorer v4.0 - Quantitative Profile + Legacy Score

Primary output: Raw quantitative profile with trajectories and sector comparisons.
Secondary output: Legacy QS (0-100) for backward compatibility, marked as deprecated.

The profile shows DATA. The analyst REASONS about quality from the data.

Usage:
  python3 tools/quality_scorer.py AAPL                # Full profile + legacy score
  python3 tools/quality_scorer.py AAPL --raw           # Profile only, no legacy score
  python3 tools/quality_scorer.py AAPL --legacy        # Legacy score only (backward compat)
  python3 tools/quality_scorer.py GOOGL META V MA      # Batch analysis
  python3 tools/quality_scorer.py ALL --detailed        # Extra detail on legacy breakdown
"""

import sys
import argparse
import yfinance as yf
import warnings
warnings.filterwarnings('ignore')

# Gross Margin medians by sector (for relative comparison)
SECTOR_GM_MEDIANS = {
    'Technology': 0.55,
    'Communication Services': 0.50,
    'Healthcare': 0.55,
    'Financial Services': 0.30,
    'Consumer Cyclical': 0.35,
    'Consumer Defensive': 0.38,
    'Industrials': 0.28,
    'Basic Materials': 0.25,
    'Energy': 0.35,
    'Utilities': 0.40,
    'Real Estate': 0.60,
}


# ==============================================================================
# Data Extraction (raw data, no scoring)
# ==============================================================================

def extract_profile(ticker):
    """
    Extract complete quantitative profile for a ticker.
    Returns dict of raw data with trajectories. No scores, no judgments.
    """
    try:
        t = yf.Ticker(ticker)
        info = t.info

        if not info or 'symbol' not in info:
            return None

        profile = {
            'ticker': ticker,
            'name': info.get('shortName', ticker),
            'sector': info.get('sector', 'Unknown'),
            'industry': info.get('industry', 'Unknown'),
            'market_cap': info.get('marketCap', 0),
            'currency': info.get('currency', 'USD'),
            'data_gaps': [],
        }

        # --- RETURNS ON CAPITAL ---
        _extract_returns(t, info, profile)

        # --- WACC ---
        _extract_wacc(t, info, profile)

        # --- MARGINS & FCF ---
        _extract_margins(t, info, profile)

        # --- LEVERAGE ---
        _extract_leverage(t, info, profile)

        # --- GROWTH ---
        _extract_growth(t, info, profile)

        # --- MOAT INDICATORS ---
        _extract_moat(t, info, profile)

        # --- CAPITAL ALLOCATION ---
        _extract_capalloc(t, info, profile)

        return profile

    except Exception as e:
        print(f"Error processing {ticker}: {e}")
        return None


def _extract_returns(t, info, profile):
    """Extract ROIC, ROE, ROA with trajectories."""
    # Current values from yfinance info
    profile['roe'] = info.get('returnOnEquity')
    profile['roa'] = info.get('returnOnAssets')

    # Calculate ROIC properly from financials
    roic_trajectory = []
    try:
        financials = t.financials
        balance = t.balance_sheet

        if not financials.empty and not balance.empty:
            for i in range(min(4, len(financials.columns))):
                try:
                    ebit = financials.loc['EBIT'].iloc[i] if 'EBIT' in financials.index else None
                    if ebit is None:
                        continue

                    # Tax rate: try to calculate from actual taxes
                    tax_rate = 0.25  # fallback
                    if 'Tax Provision' in financials.index and 'Pretax Income' in financials.index:
                        tax_prov = financials.loc['Tax Provision'].iloc[i]
                        pretax = financials.loc['Pretax Income'].iloc[i]
                        if pretax and pretax > 0 and tax_prov is not None:
                            effective_rate = tax_prov / pretax
                            if 0 < effective_rate < 0.50:
                                tax_rate = effective_rate

                    nopat = ebit * (1 - tax_rate)

                    total_assets = balance.loc['Total Assets'].iloc[i] if 'Total Assets' in balance.index else None
                    current_liab = balance.loc['Current Liabilities'].iloc[i] if 'Current Liabilities' in balance.index else 0
                    cash_eq = 0
                    for cash_key in ['Cash And Cash Equivalents', 'Cash Cash Equivalents And Short Term Investments']:
                        if cash_key in balance.index:
                            cash_eq = balance.loc[cash_key].iloc[i] or 0
                            break

                    if total_assets and total_assets > 0:
                        invested_capital = total_assets - (current_liab or 0) - (cash_eq or 0)
                        if invested_capital > 0:
                            roic = nopat / invested_capital
                            year_label = str(financials.columns[i].year) if hasattr(financials.columns[i], 'year') else f"Y-{i}"
                            roic_trajectory.append((year_label, roic))
                except Exception:
                    continue
    except Exception:
        pass

    profile['roic_trajectory'] = roic_trajectory
    profile['roic_current'] = roic_trajectory[0][1] if roic_trajectory else None

    # ROE trajectory
    roe_trajectory = []
    try:
        financials = t.financials
        balance = t.balance_sheet
        if not financials.empty and not balance.empty:
            for i in range(min(4, len(financials.columns))):
                try:
                    net_income = financials.loc['Net Income'].iloc[i] if 'Net Income' in financials.index else None
                    equity = balance.loc['Stockholders Equity'].iloc[i] if 'Stockholders Equity' in balance.index else None
                    if net_income and equity and equity > 0:
                        year_label = str(financials.columns[i].year) if hasattr(financials.columns[i], 'year') else f"Y-{i}"
                        roe_trajectory.append((year_label, net_income / equity))
                except Exception:
                    continue
    except Exception:
        pass
    profile['roe_trajectory'] = roe_trajectory

    if not roic_trajectory:
        profile['data_gaps'].append('ROIC (no financials)')


def _extract_wacc(t, info, profile):
    """Calculate WACC with real cost of debt when available."""
    beta = info.get('beta', 1.0) or 1.0
    rf = 0.045
    erp = 0.055
    cost_of_equity = rf + beta * erp

    # Try to get real cost of debt from interest expense / total debt
    total_debt = info.get('totalDebt', 0) or 0
    cost_of_debt = None
    try:
        financials = t.financials
        if not financials.empty and 'Interest Expense' in financials.index:
            interest = abs(financials.loc['Interest Expense'].iloc[0] or 0)
            if total_debt > 0 and interest > 0:
                cost_of_debt = interest / total_debt
                # Sanity check: cost of debt should be 1-15%
                if cost_of_debt > 0.15 or cost_of_debt < 0.01:
                    cost_of_debt = None
    except Exception:
        pass

    if cost_of_debt is None:
        cost_of_debt = 0.055  # fallback
        profile['data_gaps'].append('Cost of debt (using 5.5% default)')

    # Effective tax rate from financials
    tax_rate = 0.25
    tax_source = 'default 25%'
    try:
        financials = t.financials
        if not financials.empty:
            if 'Tax Provision' in financials.index and 'Pretax Income' in financials.index:
                tax_prov = financials.loc['Tax Provision'].iloc[0]
                pretax = financials.loc['Pretax Income'].iloc[0]
                if pretax and pretax > 0 and tax_prov is not None:
                    effective_rate = tax_prov / pretax
                    if 0 < effective_rate < 0.50:
                        tax_rate = effective_rate
                        tax_source = f'effective {tax_rate*100:.1f}%'
    except Exception:
        pass

    market_cap = info.get('marketCap', 1) or 1
    if market_cap > 0 and total_debt > 0:
        d_e_ratio = total_debt / market_cap
        weight_debt = d_e_ratio / (1 + d_e_ratio)
        weight_equity = 1 - weight_debt
    else:
        weight_debt = 0
        weight_equity = 1

    wacc = weight_equity * cost_of_equity + weight_debt * cost_of_debt * (1 - tax_rate)

    profile['wacc'] = wacc
    profile['wacc_components'] = {
        'beta': beta,
        'rf': rf,
        'erp': erp,
        'cost_of_equity': cost_of_equity,
        'cost_of_debt': cost_of_debt,
        'tax_rate': tax_rate,
        'tax_source': tax_source,
        'weight_equity': weight_equity,
        'weight_debt': weight_debt,
    }

    # ROIC-WACC spread
    roic = profile.get('roic_current')
    if roic is not None:
        profile['roic_wacc_spread'] = roic - wacc
    else:
        profile['roic_wacc_spread'] = None


def _extract_margins(t, info, profile):
    """Extract margin trajectories and FCF data."""
    # Gross margin trajectory
    gm_trajectory = []
    fcf_trajectory = []
    fcf_margin_trajectory = []
    op_margin_trajectory = []

    try:
        financials = t.financials
        cf = t.cashflow

        if not financials.empty:
            for i in range(min(4, len(financials.columns))):
                try:
                    year_label = str(financials.columns[i].year) if hasattr(financials.columns[i], 'year') else f"Y-{i}"
                    rev = financials.loc['Total Revenue'].iloc[i] if 'Total Revenue' in financials.index else None

                    if 'Gross Profit' in financials.index and rev and rev > 0:
                        gp = financials.loc['Gross Profit'].iloc[i]
                        if gp is not None:
                            gm_trajectory.append((year_label, gp / rev))

                    if 'Operating Income' in financials.index and rev and rev > 0:
                        oi = financials.loc['Operating Income'].iloc[i]
                        if oi is not None:
                            op_margin_trajectory.append((year_label, oi / rev))
                except Exception:
                    continue

        if not cf.empty and 'Free Cash Flow' in cf.index:
            for i in range(min(4, len(cf.columns))):
                try:
                    year_label = str(cf.columns[i].year) if hasattr(cf.columns[i], 'year') else f"Y-{i}"
                    fcf = cf.loc['Free Cash Flow'].iloc[i]
                    if fcf is not None:
                        fcf_trajectory.append((year_label, fcf))

                        # FCF margin
                        if not financials.empty and 'Total Revenue' in financials.index and i < len(financials.columns):
                            rev = financials.loc['Total Revenue'].iloc[i]
                            if rev and rev > 0:
                                fcf_margin_trajectory.append((year_label, fcf / rev))
                except Exception:
                    continue
    except Exception:
        pass

    profile['gm_trajectory'] = gm_trajectory
    profile['gm_current'] = gm_trajectory[0][1] if gm_trajectory else info.get('grossMargins')
    profile['op_margin_trajectory'] = op_margin_trajectory
    profile['fcf_trajectory'] = fcf_trajectory
    profile['fcf_margin_trajectory'] = fcf_margin_trajectory
    profile['fcf_current_margin'] = fcf_margin_trajectory[0][1] if fcf_margin_trajectory else None

    # FCF consistency
    positive_fcf_years = sum(1 for _, fcf in fcf_trajectory if fcf and fcf > 0)
    profile['fcf_positive_years'] = positive_fcf_years
    profile['fcf_total_years'] = len(fcf_trajectory)

    # GM premium vs sector
    sector = info.get('sector', 'Unknown')
    sector_median = SECTOR_GM_MEDIANS.get(sector, 0.35)
    profile['sector_gm_median'] = sector_median
    if profile['gm_current'] is not None:
        profile['gm_premium'] = profile['gm_current'] - sector_median
    else:
        profile['gm_premium'] = None

    # Trend direction
    if len(gm_trajectory) >= 2:
        gm_now = gm_trajectory[0][1]
        gm_avg = sum(v for _, v in gm_trajectory[1:]) / len(gm_trajectory[1:])
        diff = gm_now - gm_avg
        if diff > 0.01:
            profile['gm_trend'] = 'Expanding'
        elif diff < -0.01:
            profile['gm_trend'] = 'Declining'
        else:
            profile['gm_trend'] = 'Stable'
    else:
        profile['gm_trend'] = 'N/A'

    if not gm_trajectory:
        profile['data_gaps'].append('Gross margins')
    if not fcf_trajectory:
        profile['data_gaps'].append('Free Cash Flow')


def _extract_leverage(t, info, profile):
    """Extract leverage metrics."""
    total_debt = info.get('totalDebt', 0) or 0
    total_cash = info.get('totalCash', 0) or 0
    ebitda = info.get('ebitda', 0) or 0
    net_debt = total_debt - total_cash

    profile['total_debt'] = total_debt
    profile['total_cash'] = total_cash
    profile['net_debt'] = net_debt

    if ebitda > 0:
        profile['net_debt_ebitda'] = net_debt / ebitda
    elif net_debt <= 0:
        profile['net_debt_ebitda'] = 0  # Net cash
    else:
        profile['net_debt_ebitda'] = None

    # Interest coverage
    try:
        financials = t.financials
        if not financials.empty and 'EBIT' in financials.index and 'Interest Expense' in financials.index:
            ebit = financials.loc['EBIT'].iloc[0]
            interest = abs(financials.loc['Interest Expense'].iloc[0] or 0)
            if interest > 0 and ebit:
                profile['interest_coverage'] = ebit / interest
            else:
                profile['interest_coverage'] = None
        else:
            profile['interest_coverage'] = None
    except Exception:
        profile['interest_coverage'] = None


def _extract_growth(t, info, profile):
    """Extract growth trajectories."""
    # Revenue trajectory and CAGR
    rev_trajectory = []
    eps_trajectory = []

    try:
        financials = t.financials
        if not financials.empty:
            if 'Total Revenue' in financials.index:
                for i in range(min(4, len(financials.columns))):
                    try:
                        year_label = str(financials.columns[i].year) if hasattr(financials.columns[i], 'year') else f"Y-{i}"
                        rev = financials.loc['Total Revenue'].iloc[i]
                        if rev is not None and rev > 0:
                            rev_trajectory.append((year_label, rev))
                    except Exception:
                        continue

            eps_key = 'Basic EPS' if 'Basic EPS' in financials.index else 'Diluted EPS'
            if eps_key in financials.index:
                for i in range(min(4, len(financials.columns))):
                    try:
                        year_label = str(financials.columns[i].year) if hasattr(financials.columns[i], 'year') else f"Y-{i}"
                        eps = financials.loc[eps_key].iloc[i]
                        if eps is not None:
                            eps_trajectory.append((year_label, eps))
                    except Exception:
                        continue
    except Exception:
        pass

    profile['rev_trajectory'] = rev_trajectory
    profile['eps_trajectory'] = eps_trajectory

    # Calculate CAGRs
    if len(rev_trajectory) >= 2:
        rev_now = rev_trajectory[0][1]
        rev_old = rev_trajectory[-1][1]
        years = len(rev_trajectory) - 1
        if rev_old > 0 and rev_now > 0:
            profile['rev_cagr'] = (rev_now / rev_old) ** (1 / years) - 1
        else:
            profile['rev_cagr'] = None
    else:
        profile['rev_cagr'] = None

    if len(eps_trajectory) >= 2:
        eps_now = eps_trajectory[0][1]
        eps_old = eps_trajectory[-1][1]
        years = len(eps_trajectory) - 1
        if eps_old and eps_old > 0 and eps_now and eps_now > 0:
            profile['eps_cagr'] = (eps_now / eps_old) ** (1 / years) - 1
        else:
            profile['eps_cagr'] = None
    else:
        profile['eps_cagr'] = None

    if not rev_trajectory:
        profile['data_gaps'].append('Revenue')


def _extract_moat(t, info, profile):
    """Extract moat indicators (data only, no scoring)."""
    # Already have: gm_premium, gm_trend, roic_trajectory
    # Market position requires manual input - just note it
    profile['market_position'] = 'Requires manual assessment'


def _extract_capalloc(t, info, profile):
    """Extract capital allocation data."""
    profile['insider_ownership'] = info.get('heldPercentInsiders', 0) or 0
    profile['institutional_ownership'] = info.get('heldPercentInstitutions', 0) or 0

    dy = info.get('dividendYield')
    if dy and isinstance(dy, (int, float)):
        profile['dividend_yield'] = dy if dy < 1 else dy / 100  # normalize
    else:
        profile['dividend_yield'] = 0

    profile['payout_ratio'] = info.get('payoutRatio')

    # Buyback: compare shares outstanding YoY
    profile['shares_outstanding'] = info.get('sharesOutstanding')

    # Check if paying dividend at all
    profile['pays_dividend'] = bool(dy and dy > 0)


# ==============================================================================
# Legacy Score (backward compatibility, deprecated)
# ==============================================================================

def calculate_legacy_score(profile):
    """
    Calculate legacy QS (0-100) from profile data.
    Uses the same arbitrary thresholds as v3.0 for consistency with historical scores.
    DEPRECATED: Reason from the profile data above instead.
    """
    scores = {}
    total = 0

    # --- Financial (40 pts) ---

    # ROIC Spread (15 pts max)
    spread = profile.get('roic_wacc_spread')
    if spread is not None:
        spread_pp = spread * 100
        if spread_pp > 15: s = 15
        elif spread_pp > 10: s = 12
        elif spread_pp > 5: s = 8
        elif spread_pp > 0: s = 4
        else: s = 0
        scores['roic_spread'] = s
    else:
        scores['roic_spread'] = 0  # v4.0: unknown = 0, not inflated default
    total += scores['roic_spread']

    # FCF Margin (10 pts max)
    fcf_m = profile.get('fcf_current_margin')
    if fcf_m is not None:
        if fcf_m > 0.20: s = 10
        elif fcf_m > 0.15: s = 8
        elif fcf_m > 0.10: s = 5
        elif fcf_m > 0.05: s = 2
        else: s = 0
        scores['fcf_margin'] = s
    else:
        scores['fcf_margin'] = 0
    total += scores['fcf_margin']

    # Leverage (10 pts max)
    lev = profile.get('net_debt_ebitda')
    if lev is not None:
        if lev <= 0: s = 10  # net cash
        elif lev < 1: s = 10
        elif lev < 2: s = 8
        elif lev < 3: s = 5
        elif lev < 4: s = 2
        else: s = 0
        scores['leverage'] = s
    else:
        scores['leverage'] = 0
    total += scores['leverage']

    # FCF Consistency (5 pts max)
    pos = profile.get('fcf_positive_years', 0)
    tot_yr = profile.get('fcf_total_years', 0)
    if tot_yr > 0:
        if pos >= 4: s = 5
        elif pos >= 3: s = 4
        elif pos >= 2: s = 2
        else: s = 0
        scores['fcf_consistency'] = s
    else:
        scores['fcf_consistency'] = 0
    total += scores['fcf_consistency']

    # --- Growth (25 pts) ---

    # Revenue CAGR (10 pts max)
    rc = profile.get('rev_cagr')
    if rc is not None:
        if rc > 0.15: s = 10
        elif rc > 0.10: s = 8
        elif rc > 0.05: s = 5
        elif rc > 0: s = 2
        else: s = 0
        scores['rev_cagr'] = s
    else:
        scores['rev_cagr'] = 0
    total += scores['rev_cagr']

    # EPS CAGR (10 pts max)
    ec = profile.get('eps_cagr')
    if ec is not None:
        if ec > 0.15: s = 10
        elif ec > 0.10: s = 8
        elif ec > 0.05: s = 5
        elif ec > 0: s = 2
        else: s = 0
        scores['eps_cagr'] = s
    else:
        scores['eps_cagr'] = 0
    total += scores['eps_cagr']

    # GM Trend (5 pts max)
    trend = profile.get('gm_trend', 'N/A')
    if trend == 'Expanding': s = 5
    elif trend == 'Stable': s = 3
    elif trend == 'Declining': s = 0
    else: s = 0
    scores['gm_trend'] = s
    total += scores['gm_trend']

    # --- Moat (25 pts) ---

    # GM Premium (10 pts max)
    gmp = profile.get('gm_premium')
    if gmp is not None:
        if gmp > 0.10: s = 10
        elif gmp > 0.05: s = 7
        elif gmp > -0.05: s = 4
        else: s = 0
        scores['gm_premium'] = s
    else:
        scores['gm_premium'] = 0
    total += scores['gm_premium']

    # Market Position (default 0 - cannot be assessed automatically)
    # NOTE: Changed from default=5 to default=0 per Devil's Advocate Sesion 53.
    # The old default inflated ALL scores by ~5 points. Market position requires
    # manual assessment (monopoly, oligopoly, fragmented) which the tool cannot do.
    scores['market_position'] = 0
    total += 0

    # ROIC Persistence (7 pts max) - from trajectory
    roic_traj = profile.get('roic_trajectory', [])
    if len(roic_traj) >= 2:
        wacc = profile.get('wacc', 0.09)
        above_wacc_count = sum(1 for _, r in roic_traj if r > wacc)
        if above_wacc_count == len(roic_traj): s = 7
        elif above_wacc_count >= len(roic_traj) * 0.5: s = 5
        else: s = 2
        scores['roic_persistence'] = s
    elif profile.get('roic_current') is not None:
        roic = profile['roic_current']
        wacc = profile.get('wacc', 0.09)
        if roic > wacc * 1.5: s = 7
        elif roic > wacc: s = 5
        else: s = 2
        scores['roic_persistence'] = s
    else:
        scores['roic_persistence'] = 0
    total += scores['roic_persistence']

    # --- Capital Allocation (10 pts) ---

    # Shareholder Returns (5 pts max)
    # NOTE: Changed from binary (dividend=5, no dividend=0) per Devil's Advocate Sesion 53.
    # Quality compounders may return capital via buybacks OR dividends. Both valid.
    # Now: pays dividend OR has buyback program (negative shares growth) = 3 base.
    # Extra 2 pts for payout ratio sustainability (payout_ratio < 75% AND pays dividend).
    div_yield = profile.get('dividend_yield', 0) or 0
    payout = profile.get('payout_ratio', 0) or 0
    if div_yield > 0:
        s = 3  # Pays dividend
        if 0 < payout < 0.75:
            s = 5  # Sustainable payout
    elif profile.get('fcf_consistency', 0) >= 3:
        # No dividend but consistent positive FCF suggests buybacks/reinvestment
        s = 2
    else:
        s = 0
    scores['shareholder_returns'] = s
    total += scores['shareholder_returns']

    # Insider Ownership (5 pts max)
    insider = profile.get('insider_ownership', 0)
    if insider > 0.05: s = 5
    elif insider > 0.02: s = 3
    elif insider > 0.005: s = 1
    else: s = 0
    scores['insider_ownership'] = s
    total += scores['insider_ownership']

    # Tier (same thresholds as v3.0 for consistency)
    if total >= 75:
        tier, category = 'A', 'Quality Compounder'
    elif total >= 55:
        tier, category = 'B', 'Quality Value'
    elif total >= 35:
        tier, category = 'C', 'Special Situation'
    else:
        tier, category = 'D', 'Below minimum threshold'

    return {
        'total': total,
        'tier': tier,
        'category': category,
        'scores': scores,
    }


# ==============================================================================
# Output Formatting
# ==============================================================================

def fmt_pct(val, show_sign=False):
    """Format a decimal as percentage string."""
    if val is None:
        return 'N/A'
    prefix = '+' if show_sign and val > 0 else ''
    return f"{prefix}{val*100:.1f}%"


def fmt_money(val, currency=''):
    """Format large numbers as B/M."""
    if val is None or val == 0:
        return 'N/A'
    if abs(val) >= 1e9:
        return f"{val/1e9:.1f}B {currency}".strip()
    elif abs(val) >= 1e6:
        return f"{val/1e6:.0f}M {currency}".strip()
    else:
        return f"{val:,.0f} {currency}".strip()


def print_profile(profile, show_legacy=True, show_detail=False):
    """Print the quantitative profile."""
    if profile is None:
        return

    print(f"\n{'='*70}")
    print(f"QUALITY PROFILE: {profile['ticker']} - {profile['name']}")
    print(f"{'='*70}")
    print(f"Sector: {profile['sector']} | Industry: {profile['industry']}")
    print(f"Market Cap: {fmt_money(profile['market_cap'], profile['currency'])}")

    # Data gaps warning
    if profile['data_gaps']:
        print(f"\n[!] Data gaps: {', '.join(profile['data_gaps'])}")

    # --- RETURNS ON CAPITAL ---
    print(f"\n{'─'*70}")
    print("RETURNS ON CAPITAL")
    print(f"{'─'*70}")

    # ROIC trajectory
    roic_traj = profile.get('roic_trajectory', [])
    if roic_traj:
        traj_str = '  '.join(f"{yr}: {fmt_pct(r)}" for yr, r in reversed(roic_traj))
        print(f"  ROIC trajectory:  {traj_str}")
        print(f"  ROIC (latest):    {fmt_pct(profile['roic_current'])}")
    else:
        print(f"  ROIC:             N/A")

    # ROE trajectory
    roe_traj = profile.get('roe_trajectory', [])
    if roe_traj:
        traj_str = '  '.join(f"{yr}: {fmt_pct(r)}" for yr, r in reversed(roe_traj))
        print(f"  ROE trajectory:   {traj_str}")
    elif profile.get('roe') is not None:
        print(f"  ROE:              {fmt_pct(profile['roe'])}")

    # WACC and spread
    wacc = profile.get('wacc')
    spread = profile.get('roic_wacc_spread')
    if wacc is not None:
        wc = profile['wacc_components']
        print(f"  WACC:             {fmt_pct(wacc)} (Ke={fmt_pct(wc['cost_of_equity'])}, "
              f"Kd={fmt_pct(wc['cost_of_debt'])}, beta={wc['beta']:.2f}, "
              f"tax={wc['tax_source']})")
    if spread is not None:
        print(f"  ROIC-WACC spread: {spread*100:+.1f}pp")

    # --- MARGINS ---
    print(f"\n{'─'*70}")
    print("MARGINS & CASH FLOW")
    print(f"{'─'*70}")

    gm_traj = profile.get('gm_trajectory', [])
    if gm_traj:
        traj_str = '  '.join(f"{yr}: {fmt_pct(v)}" for yr, v in reversed(gm_traj))
        print(f"  Gross margin:     {traj_str}  [{profile.get('gm_trend', 'N/A')}]")
        if profile.get('gm_premium') is not None:
            print(f"  vs sector median: {profile['gm_premium']*100:+.1f}pp (sector={fmt_pct(profile['sector_gm_median'])})")
    elif profile.get('gm_current') is not None:
        print(f"  Gross margin:     {fmt_pct(profile['gm_current'])}")

    op_traj = profile.get('op_margin_trajectory', [])
    if op_traj:
        traj_str = '  '.join(f"{yr}: {fmt_pct(v)}" for yr, v in reversed(op_traj))
        print(f"  Operating margin: {traj_str}")

    fcf_traj = profile.get('fcf_trajectory', [])
    if fcf_traj:
        traj_str = '  '.join(f"{yr}: {fmt_money(v)}" for yr, v in reversed(fcf_traj))
        print(f"  FCF:              {traj_str}")
        print(f"  FCF positive:     {profile['fcf_positive_years']}/{profile['fcf_total_years']} years")

    fcf_m_traj = profile.get('fcf_margin_trajectory', [])
    if fcf_m_traj:
        traj_str = '  '.join(f"{yr}: {fmt_pct(v)}" for yr, v in reversed(fcf_m_traj))
        print(f"  FCF margin:       {traj_str}")

    # --- LEVERAGE ---
    print(f"\n{'─'*70}")
    print("LEVERAGE")
    print(f"{'─'*70}")

    lev = profile.get('net_debt_ebitda')
    if lev is not None:
        status = "Net Cash" if lev <= 0 else f"{lev:.1f}x"
        print(f"  Net Debt/EBITDA:  {status}")
    print(f"  Total debt:       {fmt_money(profile.get('total_debt', 0))}")
    print(f"  Cash:             {fmt_money(profile.get('total_cash', 0))}")
    print(f"  Net debt:         {fmt_money(profile.get('net_debt', 0))}")
    ic = profile.get('interest_coverage')
    if ic is not None:
        print(f"  Interest cover:   {ic:.1f}x")

    # --- GROWTH ---
    print(f"\n{'─'*70}")
    print("GROWTH")
    print(f"{'─'*70}")

    rev_traj = profile.get('rev_trajectory', [])
    if rev_traj:
        traj_str = '  '.join(f"{yr}: {fmt_money(v)}" for yr, v in reversed(rev_traj))
        print(f"  Revenue:          {traj_str}")
    rc = profile.get('rev_cagr')
    if rc is not None:
        print(f"  Revenue CAGR:     {fmt_pct(rc, show_sign=True)}")

    eps_traj = profile.get('eps_trajectory', [])
    if eps_traj:
        traj_str = '  '.join(f"{yr}: {v:.2f}" for yr, v in reversed(eps_traj))
        print(f"  EPS:              {traj_str}")
    ec = profile.get('eps_cagr')
    if ec is not None:
        print(f"  EPS CAGR:         {fmt_pct(ec, show_sign=True)}")

    # --- CAPITAL ALLOCATION ---
    print(f"\n{'─'*70}")
    print("CAPITAL ALLOCATION")
    print(f"{'─'*70}")

    insider = profile.get('insider_ownership', 0)
    print(f"  Insider ownership:       {fmt_pct(insider)}")
    print(f"  Institutional ownership: {fmt_pct(profile.get('institutional_ownership', 0))}")
    print(f"  Dividend yield:          {fmt_pct(profile.get('dividend_yield', 0))}")
    pr = profile.get('payout_ratio')
    if pr is not None and isinstance(pr, (int, float)):
        print(f"  Payout ratio:            {fmt_pct(pr)}")

    # --- LEGACY SCORE ---
    if show_legacy:
        legacy = calculate_legacy_score(profile)

        print(f"\n{'='*70}")
        print(f"LEGACY SCORE (deprecating - reason from profile above)")
        print(f"{'='*70}")
        print(f"Score: {legacy['total']}/100 | Tier {legacy['tier']} | {legacy['category']}")

        if show_detail:
            s = legacy['scores']
            print(f"\n  Financial ({s['roic_spread']+s['fcf_margin']+s['leverage']+s['fcf_consistency']}/40):")
            print(f"    ROIC Spread:     {s['roic_spread']:2d}/15")
            print(f"    FCF Margin:      {s['fcf_margin']:2d}/10")
            print(f"    Leverage:        {s['leverage']:2d}/10")
            print(f"    FCF Consistency: {s['fcf_consistency']:2d}/5")
            print(f"  Growth ({s['rev_cagr']+s['eps_cagr']+s['gm_trend']}/25):")
            print(f"    Revenue CAGR:    {s['rev_cagr']:2d}/10")
            print(f"    EPS CAGR:        {s['eps_cagr']:2d}/10")
            print(f"    GM Trend:        {s['gm_trend']:2d}/5")
            print(f"  Moat ({s['gm_premium']+s['market_position']+s['roic_persistence']}/25):")
            print(f"    GM Premium:      {s['gm_premium']:2d}/10")
            print(f"    Market Position: {s['market_position']:2d}/8 (manual)")
            print(f"    ROIC Persistence:{s['roic_persistence']:2d}/7")
            print(f"  Cap Alloc ({s['shareholder_returns']+s['insider_ownership']}/10):")
            print(f"    Shareholder Ret: {s['shareholder_returns']:2d}/5")
            print(f"    Insider Own:     {s['insider_ownership']:2d}/5")

        print(f"\nNote: Legacy score uses arbitrary thresholds. Use the profile above to reason.")
        print(f"      N/A data = 0 pts (not inflated). See learning/principles.md for framework.")

    print()


def main():
    parser = argparse.ArgumentParser(description='Quality Scorer v4.0 - Quantitative Profile')
    parser.add_argument('tickers', nargs='+', help='Ticker symbols to analyze')
    parser.add_argument('--detailed', '-d', action='store_true', help='Show legacy score breakdown')
    parser.add_argument('--raw', action='store_true', help='Profile only, no legacy score')
    parser.add_argument('--legacy', action='store_true', help='Legacy score only (backward compat)')

    args = parser.parse_args()

    results = []
    for ticker in args.tickers:
        profile = extract_profile(ticker.upper())
        if profile:
            if args.legacy:
                # Backward compatible: print legacy format only
                legacy = calculate_legacy_score(profile)
                print(f"\n{'='*60}")
                print(f"QUALITY SCORE: {profile['ticker']} - {profile['name']}")
                print(f"{'='*60}")
                print(f"Sector: {profile['sector']}")
                print(f"\nTOTAL SCORE: {legacy['total']}/100 -> TIER {legacy['tier']}")
                print(f"Category: {legacy['category']}")
                print(f"\nNote: Legacy score. Run without --legacy for full profile.")
                print()
            else:
                print_profile(profile, show_legacy=not args.raw, show_detail=args.detailed)
            results.append((profile, calculate_legacy_score(profile)))
        else:
            print(f"\nCould not process {ticker}")

    # Summary table for batch
    if len(results) > 1:
        print(f"\n{'='*70}")
        print("SUMMARY")
        print(f"{'='*70}")
        print(f"{'Ticker':<10} {'Sector':<22} {'ROIC':>6} {'WACC':>6} {'Spread':>7} {'FCF%':>6} {'Lev':>5} {'RevCAGR':>8} {'GM':>6} {'Legacy':>7} {'Tier':>5}")
        print(f"{'-'*95}")

        for profile, legacy in results:
            roic_str = fmt_pct(profile.get('roic_current')) if profile.get('roic_current') is not None else 'N/A'
            wacc_str = fmt_pct(profile.get('wacc')) if profile.get('wacc') is not None else 'N/A'
            spread = profile.get('roic_wacc_spread')
            spread_str = f"{spread*100:+.1f}" if spread is not None else 'N/A'
            fcf_str = fmt_pct(profile.get('fcf_current_margin')) if profile.get('fcf_current_margin') is not None else 'N/A'
            lev = profile.get('net_debt_ebitda')
            lev_str = f"{lev:.1f}x" if lev is not None else 'N/A'
            rc = profile.get('rev_cagr')
            rc_str = fmt_pct(rc, show_sign=True) if rc is not None else 'N/A'
            gm_str = fmt_pct(profile.get('gm_current')) if profile.get('gm_current') is not None else 'N/A'

            print(f"{profile['ticker']:<10} {profile['sector'][:22]:<22} {roic_str:>6} {wacc_str:>6} {spread_str:>7} {fcf_str:>6} {lev_str:>5} {rc_str:>8} {gm_str:>6} {legacy['total']:>5}/100 {legacy['tier']:>5}")


if __name__ == '__main__':
    main()
