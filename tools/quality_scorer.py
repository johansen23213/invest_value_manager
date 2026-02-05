#!/usr/bin/env python3
"""
Quality Scorer v3.0 - Calculates Quality Score (0-100) for any stock.

Framework v3.0 Quality Score Components:
- Financial Quality (40 pts): ROIC Spread, FCF Margin, Leverage, FCF Consistency
- Growth Quality (25 pts): Revenue CAGR, EPS CAGR, Gross Margin Trend
- Moat Evidence (25 pts): GM Premium vs Sector, Market Position, ROIC Persistence
- Capital Allocation (10 pts): Shareholder Returns, Insider Ownership

Tiers:
- A (75-100): Quality Compounder, MoS 10-15%
- B (55-74): Quality Value, MoS 20-25%
- C (35-54): Special Situation, MoS 30-40%
- D (<35): DO NOT BUY

Usage:
  python3 tools/quality_scorer.py AAPL
  python3 tools/quality_scorer.py GOOGL META V MA
  python3 tools/quality_scorer.py ALL --detailed
"""

import sys
import argparse
import yfinance as yf
import warnings
warnings.filterwarnings('ignore')

# Gross Margin medians by sector (for Moat Evidence calculation)
SECTOR_GM_MEDIANS = {
    'Technology': 0.55,
    'Communication Services': 0.50,
    'Healthcare': 0.55,
    'Financial Services': 0.30,  # Not really applicable
    'Consumer Cyclical': 0.35,
    'Consumer Defensive': 0.38,
    'Industrials': 0.28,
    'Basic Materials': 0.25,
    'Energy': 0.35,
    'Utilities': 0.40,
    'Real Estate': 0.60,
}

def get_wacc(ticker_obj, rf=0.045):
    """Calculate WACC using CAPM."""
    try:
        info = ticker_obj.info
        beta = info.get('beta', 1.0) or 1.0
        erp = 0.055  # Equity risk premium
        cost_of_equity = rf + beta * erp

        # Simplified: assume cost of debt ~5-6%
        cost_of_debt = 0.055
        tax_rate = 0.25

        # Get debt/equity ratio
        total_debt = info.get('totalDebt', 0) or 0
        market_cap = info.get('marketCap', 1) or 1

        if market_cap > 0:
            d_e_ratio = total_debt / market_cap
            weight_debt = d_e_ratio / (1 + d_e_ratio)
            weight_equity = 1 - weight_debt
        else:
            weight_debt = 0
            weight_equity = 1

        wacc = weight_equity * cost_of_equity + weight_debt * cost_of_debt * (1 - tax_rate)
        return max(wacc, 0.08)  # Floor at 8%
    except:
        return 0.09  # Default

def get_roic(ticker_obj):
    """Calculate ROIC = NOPAT / Invested Capital."""
    try:
        info = ticker_obj.info

        # Try to get from info first
        roic = info.get('returnOnAssets')
        if roic:
            # Rough approximation: ROA * (1 + D/E) ≈ ROIC
            return roic * 1.3  # Approximate adjustment

        # Manual calculation
        financials = ticker_obj.financials
        if financials.empty:
            return None

        ebit = financials.loc['EBIT'].iloc[0] if 'EBIT' in financials.index else None
        if ebit is None:
            return None

        tax_rate = 0.25
        nopat = ebit * (1 - tax_rate)

        balance = ticker_obj.balance_sheet
        if balance.empty:
            return None

        total_assets = balance.loc['Total Assets'].iloc[0] if 'Total Assets' in balance.index else None
        current_liab = balance.loc['Current Liabilities'].iloc[0] if 'Current Liabilities' in balance.index else 0
        cash = balance.loc['Cash And Cash Equivalents'].iloc[0] if 'Cash And Cash Equivalents' in balance.index else 0

        if total_assets:
            invested_capital = total_assets - current_liab - cash
            if invested_capital > 0:
                return nopat / invested_capital
        return None
    except:
        return None

def get_fcf_margin(ticker_obj):
    """Calculate FCF / Revenue."""
    try:
        cf = ticker_obj.cashflow
        financials = ticker_obj.financials

        if cf.empty or financials.empty:
            return None

        fcf = cf.loc['Free Cash Flow'].iloc[0] if 'Free Cash Flow' in cf.index else None
        revenue = financials.loc['Total Revenue'].iloc[0] if 'Total Revenue' in financials.index else None

        if fcf and revenue and revenue > 0:
            return fcf / revenue
        return None
    except:
        return None

def get_leverage(ticker_obj):
    """Calculate Net Debt / EBITDA."""
    try:
        info = ticker_obj.info
        total_debt = info.get('totalDebt', 0) or 0
        cash = info.get('totalCash', 0) or 0
        net_debt = total_debt - cash

        ebitda = info.get('ebitda', 0) or 0

        if ebitda > 0:
            return net_debt / ebitda
        elif net_debt <= 0:
            return -1  # Net cash position
        return None
    except:
        return None

def get_fcf_consistency(ticker_obj):
    """Count years of positive FCF in last 5 years."""
    try:
        cf = ticker_obj.cashflow
        if cf.empty or 'Free Cash Flow' not in cf.index:
            return None

        fcf_row = cf.loc['Free Cash Flow']
        positive_count = sum(1 for fcf in fcf_row[:5] if fcf and fcf > 0)
        return positive_count
    except:
        return None

def get_revenue_cagr(ticker_obj):
    """Calculate 5-year revenue CAGR."""
    try:
        financials = ticker_obj.financials
        if financials.empty or 'Total Revenue' not in financials.index:
            return None

        revenues = financials.loc['Total Revenue']
        if len(revenues) < 4:
            return None

        rev_now = revenues.iloc[0]
        rev_old = revenues.iloc[-1]  # Oldest available
        years = len(revenues)

        if rev_old and rev_old > 0 and rev_now > 0:
            cagr = (rev_now / rev_old) ** (1 / years) - 1
            return cagr
        return None
    except:
        return None

def get_eps_cagr(ticker_obj):
    """Calculate 5-year EPS CAGR."""
    try:
        financials = ticker_obj.financials
        if financials.empty:
            return None

        eps_key = 'Basic EPS' if 'Basic EPS' in financials.index else 'Diluted EPS'
        if eps_key not in financials.index:
            return None

        eps = financials.loc[eps_key]
        if len(eps) < 4:
            return None

        eps_now = eps.iloc[0]
        eps_old = eps.iloc[-1]
        years = len(eps)

        if eps_old and eps_old > 0 and eps_now > 0:
            cagr = (eps_now / eps_old) ** (1 / years) - 1
            return cagr
        return None
    except:
        return None

def get_gm_trend(ticker_obj):
    """Determine if gross margin is expanding, stable, or declining."""
    try:
        financials = ticker_obj.financials
        if financials.empty:
            return None

        if 'Gross Profit' not in financials.index or 'Total Revenue' not in financials.index:
            return None

        gp = financials.loc['Gross Profit']
        rev = financials.loc['Total Revenue']

        gms = []
        for i in range(min(4, len(gp))):
            if gp.iloc[i] and rev.iloc[i] and rev.iloc[i] > 0:
                gms.append(gp.iloc[i] / rev.iloc[i])

        if len(gms) < 2:
            return None

        # Compare most recent to average of older
        gm_now = gms[0]
        gm_avg = sum(gms[1:]) / len(gms[1:])

        diff = gm_now - gm_avg
        if diff > 0.01:
            return 'Expanding'
        elif diff < -0.01:
            return 'Declining'
        else:
            return 'Stable'
    except:
        return None

def get_gm_premium(ticker_obj):
    """Calculate gross margin premium vs sector median."""
    try:
        info = ticker_obj.info
        gm = info.get('grossMargins')
        sector = info.get('sector', 'Unknown')

        if gm is None:
            return None

        sector_median = SECTOR_GM_MEDIANS.get(sector, 0.35)
        premium = gm - sector_median
        return premium
    except:
        return None

def get_insider_ownership(ticker_obj):
    """Get insider ownership percentage."""
    try:
        info = ticker_obj.info
        insider = info.get('heldPercentInsiders', 0)
        return insider if insider else 0
    except:
        return 0

def get_dividend_years(ticker_obj):
    """Estimate years of consistent dividends/buybacks."""
    try:
        info = ticker_obj.info
        div_yield = info.get('dividendYield', 0)

        # Check if has dividend
        if div_yield and div_yield > 0:
            # Rough estimate based on payout consistency
            # In practice, would need historical data
            return 10  # Assume mature if paying dividend
        return 0
    except:
        return 0

def score_financial(ticker_obj):
    """Calculate Financial Quality score (0-40)."""
    scores = {}

    # ROIC Spread
    roic = get_roic(ticker_obj)
    wacc = get_wacc(ticker_obj)

    if roic is not None:
        spread = (roic - wacc) * 100  # Convert to percentage points
        if spread > 15:
            scores['roic_spread'] = 15
        elif spread > 10:
            scores['roic_spread'] = 12
        elif spread > 5:
            scores['roic_spread'] = 8
        elif spread > 0:
            scores['roic_spread'] = 4
        else:
            scores['roic_spread'] = 0
        scores['roic_spread_value'] = f"{spread:.1f}pp"
    else:
        scores['roic_spread'] = 4  # Default moderate
        scores['roic_spread_value'] = "N/A"

    # FCF Margin
    fcf_margin = get_fcf_margin(ticker_obj)
    if fcf_margin is not None:
        if fcf_margin > 0.20:
            scores['fcf_margin'] = 10
        elif fcf_margin > 0.15:
            scores['fcf_margin'] = 8
        elif fcf_margin > 0.10:
            scores['fcf_margin'] = 5
        elif fcf_margin > 0.05:
            scores['fcf_margin'] = 2
        else:
            scores['fcf_margin'] = 0
        scores['fcf_margin_value'] = f"{fcf_margin*100:.1f}%"
    else:
        scores['fcf_margin'] = 5
        scores['fcf_margin_value'] = "N/A"

    # Leverage
    leverage = get_leverage(ticker_obj)
    if leverage is not None:
        if leverage < 1:
            scores['leverage'] = 10
        elif leverage < 2:
            scores['leverage'] = 8
        elif leverage < 3:
            scores['leverage'] = 5
        elif leverage < 4:
            scores['leverage'] = 2
        else:
            scores['leverage'] = 0
        scores['leverage_value'] = f"{leverage:.1f}x" if leverage >= 0 else "Net Cash"
    else:
        scores['leverage'] = 5
        scores['leverage_value'] = "N/A"

    # FCF Consistency
    fcf_count = get_fcf_consistency(ticker_obj)
    if fcf_count is not None:
        if fcf_count >= 5:
            scores['fcf_consistency'] = 5
        elif fcf_count >= 4:
            scores['fcf_consistency'] = 4
        elif fcf_count >= 3:
            scores['fcf_consistency'] = 2
        else:
            scores['fcf_consistency'] = 0
        scores['fcf_consistency_value'] = f"{fcf_count}/5"
    else:
        scores['fcf_consistency'] = 3
        scores['fcf_consistency_value'] = "N/A"

    total = scores['roic_spread'] + scores['fcf_margin'] + scores['leverage'] + scores['fcf_consistency']
    return total, scores

def score_growth(ticker_obj):
    """Calculate Growth Quality score (0-25)."""
    scores = {}

    # Revenue CAGR
    rev_cagr = get_revenue_cagr(ticker_obj)
    if rev_cagr is not None:
        if rev_cagr > 0.15:
            scores['rev_cagr'] = 10
        elif rev_cagr > 0.10:
            scores['rev_cagr'] = 8
        elif rev_cagr > 0.05:
            scores['rev_cagr'] = 5
        elif rev_cagr > 0:
            scores['rev_cagr'] = 2
        else:
            scores['rev_cagr'] = 0
        scores['rev_cagr_value'] = f"{rev_cagr*100:.1f}%"
    else:
        scores['rev_cagr'] = 5
        scores['rev_cagr_value'] = "N/A"

    # EPS CAGR
    eps_cagr = get_eps_cagr(ticker_obj)
    if eps_cagr is not None:
        if eps_cagr > 0.15:
            scores['eps_cagr'] = 10
        elif eps_cagr > 0.10:
            scores['eps_cagr'] = 8
        elif eps_cagr > 0.05:
            scores['eps_cagr'] = 5
        elif eps_cagr > 0:
            scores['eps_cagr'] = 2
        else:
            scores['eps_cagr'] = 0
        scores['eps_cagr_value'] = f"{eps_cagr*100:.1f}%"
    else:
        scores['eps_cagr'] = 5
        scores['eps_cagr_value'] = "N/A"

    # GM Trend
    gm_trend = get_gm_trend(ticker_obj)
    if gm_trend == 'Expanding':
        scores['gm_trend'] = 5
    elif gm_trend == 'Stable':
        scores['gm_trend'] = 3
    elif gm_trend == 'Declining':
        scores['gm_trend'] = 0
    else:
        scores['gm_trend'] = 3
    scores['gm_trend_value'] = gm_trend or "N/A"

    total = scores['rev_cagr'] + scores['eps_cagr'] + scores['gm_trend']
    return total, scores

def score_moat(ticker_obj):
    """Calculate Moat Evidence score (0-25)."""
    scores = {}

    # GM Premium vs Sector
    gm_premium = get_gm_premium(ticker_obj)
    if gm_premium is not None:
        if gm_premium > 0.10:
            scores['gm_premium'] = 10
        elif gm_premium > 0.05:
            scores['gm_premium'] = 7
        elif gm_premium > -0.05:
            scores['gm_premium'] = 4
        else:
            scores['gm_premium'] = 0
        scores['gm_premium_value'] = f"{gm_premium*100:+.1f}pp"
    else:
        scores['gm_premium'] = 4
        scores['gm_premium_value'] = "N/A"

    # Market Position (requires manual input, default to mid-tier)
    scores['market_position'] = 5  # Default: assume #3-5
    scores['market_position_value'] = "Manual input needed"

    # ROIC Persistence (simplified - check if ROIC > WACC now)
    roic = get_roic(ticker_obj)
    wacc = get_wacc(ticker_obj)
    if roic is not None:
        if roic > wacc * 1.5:  # Strong
            scores['roic_persistence'] = 7
        elif roic > wacc:
            scores['roic_persistence'] = 5
        else:
            scores['roic_persistence'] = 2
        scores['roic_persistence_value'] = "Estimated from current"
    else:
        scores['roic_persistence'] = 3
        scores['roic_persistence_value'] = "N/A"

    total = scores['gm_premium'] + scores['market_position'] + scores['roic_persistence']
    return total, scores

def score_capalloc(ticker_obj):
    """Calculate Capital Allocation score (0-10)."""
    scores = {}

    # Shareholder Returns
    div_years = get_dividend_years(ticker_obj)
    if div_years >= 10:
        scores['shareholder_returns'] = 5
    elif div_years >= 5:
        scores['shareholder_returns'] = 3
    elif div_years >= 1:
        scores['shareholder_returns'] = 1
    else:
        scores['shareholder_returns'] = 0
    scores['shareholder_returns_value'] = f"{div_years}yr"

    # Insider Ownership
    insider = get_insider_ownership(ticker_obj)
    if insider > 0.05:
        scores['insider_ownership'] = 5
    elif insider > 0.02:
        scores['insider_ownership'] = 3
    elif insider > 0.005:
        scores['insider_ownership'] = 1
    else:
        scores['insider_ownership'] = 0
    scores['insider_ownership_value'] = f"{insider*100:.1f}%"

    total = scores['shareholder_returns'] + scores['insider_ownership']
    return total, scores

def get_tier(score):
    """Determine tier from quality score."""
    # NOTE: Tiers are data. MoS is NOT prescribed - reason from principles.
    if score >= 75:
        return 'A', 'Quality Compounder', 'See precedents'
    elif score >= 55:
        return 'B', 'Quality Value', 'See precedents'
    elif score >= 35:
        return 'C', 'Special Situation', 'See precedents'
    else:
        return 'D', 'DO NOT BUY', 'N/A'

def calculate_quality_score(ticker, detailed=False):
    """Calculate complete Quality Score for a ticker."""
    try:
        t = yf.Ticker(ticker)
        info = t.info

        if not info or 'symbol' not in info:
            return None

        name = info.get('shortName', ticker)
        sector = info.get('sector', 'Unknown')

        # Calculate component scores
        fin_total, fin_detail = score_financial(t)
        growth_total, growth_detail = score_growth(t)
        moat_total, moat_detail = score_moat(t)
        cap_total, cap_detail = score_capalloc(t)

        total_score = fin_total + growth_total + moat_total + cap_total
        tier, category, mos_req = get_tier(total_score)

        result = {
            'ticker': ticker,
            'name': name,
            'sector': sector,
            'total_score': total_score,
            'tier': tier,
            'category': category,
            'mos_required': mos_req,
            'financial': {'total': fin_total, 'max': 40, 'detail': fin_detail},
            'growth': {'total': growth_total, 'max': 25, 'detail': growth_detail},
            'moat': {'total': moat_total, 'max': 25, 'detail': moat_detail},
            'capalloc': {'total': cap_total, 'max': 10, 'detail': cap_detail},
        }

        return result
    except Exception as e:
        print(f"Error processing {ticker}: {e}")
        return None

def print_result(result, detailed=False):
    """Print quality score result."""
    if result is None:
        return

    print(f"\n{'='*60}")
    print(f"QUALITY SCORE: {result['ticker']} - {result['name']}")
    print(f"{'='*60}")
    print(f"Sector: {result['sector']}")
    print()
    print(f"TOTAL SCORE: {result['total_score']}/100 → TIER {result['tier']}")
    print(f"Category: {result['category']}")
    print(f"MoS Required: {result['mos_required']}")
    print()

    # Component summary
    print(f"Financial Quality:    {result['financial']['total']:2d}/{result['financial']['max']} pts")
    print(f"Growth Quality:       {result['growth']['total']:2d}/{result['growth']['max']} pts")
    print(f"Moat Evidence:        {result['moat']['total']:2d}/{result['moat']['max']} pts")
    print(f"Capital Allocation:   {result['capalloc']['total']:2d}/{result['capalloc']['max']} pts")

    if detailed:
        print(f"\n{'─'*60}")
        print("DETAILED BREAKDOWN:")
        print(f"{'─'*60}")

        print("\nFINANCIAL QUALITY (40 pts):")
        fd = result['financial']['detail']
        print(f"  ROIC Spread:      {fd['roic_spread']:2d} pts  ({fd['roic_spread_value']})")
        print(f"  FCF Margin:       {fd['fcf_margin']:2d} pts  ({fd['fcf_margin_value']})")
        print(f"  Leverage:         {fd['leverage']:2d} pts  ({fd['leverage_value']})")
        print(f"  FCF Consistency:  {fd['fcf_consistency']:2d} pts  ({fd['fcf_consistency_value']})")

        print("\nGROWTH QUALITY (25 pts):")
        gd = result['growth']['detail']
        print(f"  Revenue CAGR:     {gd['rev_cagr']:2d} pts  ({gd['rev_cagr_value']})")
        print(f"  EPS CAGR:         {gd['eps_cagr']:2d} pts  ({gd['eps_cagr_value']})")
        print(f"  GM Trend:         {gd['gm_trend']:2d} pts  ({gd['gm_trend_value']})")

        print("\nMOAT EVIDENCE (25 pts):")
        md = result['moat']['detail']
        print(f"  GM Premium:       {md['gm_premium']:2d} pts  ({md['gm_premium_value']})")
        print(f"  Market Position:  {md['market_position']:2d} pts  ({md['market_position_value']})")
        print(f"  ROIC Persistence: {md['roic_persistence']:2d} pts  ({md['roic_persistence_value']})")

        print("\nCAPITAL ALLOCATION (10 pts):")
        cd = result['capalloc']['detail']
        print(f"  Shareholder Ret:  {cd['shareholder_returns']:2d} pts  ({cd['shareholder_returns_value']})")
        print(f"  Insider Own:      {cd['insider_ownership']:2d} pts  ({cd['insider_ownership_value']})")

    print()

    # Data output - no recommendations with fixed numbers
    if result['tier'] == 'D':
        print("TIER D: Quality below minimum threshold. Do not proceed.")
    else:
        print(f"TIER {result['tier']}: Consult learning/decisions_log.yaml for precedents")
        print("       Apply learning/principles.md to determine appropriate MoS")

def main():
    parser = argparse.ArgumentParser(description='Calculate Quality Score for stocks')
    parser.add_argument('tickers', nargs='+', help='Ticker symbols to analyze')
    parser.add_argument('--detailed', '-d', action='store_true', help='Show detailed breakdown')

    args = parser.parse_args()

    for ticker in args.tickers:
        result = calculate_quality_score(ticker.upper(), args.detailed)
        if result:
            print_result(result, args.detailed)
        else:
            print(f"\nCould not calculate Quality Score for {ticker}")

    # Summary table if multiple tickers
    if len(args.tickers) > 1:
        print(f"\n{'='*60}")
        print("SUMMARY")
        print(f"{'='*60}")
        print(f"{'Ticker':<8} {'Score':>6} {'Tier':>5} {'Category':<20} {'MoS Req':<10}")
        print(f"{'-'*60}")

        for ticker in args.tickers:
            result = calculate_quality_score(ticker.upper())
            if result:
                print(f"{result['ticker']:<8} {result['total_score']:>6} {result['tier']:>5} {result['category']:<20} {result['mos_required']:<10}")

if __name__ == '__main__':
    main()
