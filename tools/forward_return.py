#!/usr/bin/env python3
"""
Forward Return Components - Shows MoS%, Growth%, Yield% for portfolio positions.

Outputs RAW DATA as separate columns. NO composite scores, rankings, or recommendations.
The user reasons about these components applying principles.

Components:
  - MoS% = (Fair_Value - Current_Price) / Current_Price * 100
  - Growth% = Expected earnings/FCF growth rate (from thesis or yfinance)
  - Yield% = Current dividend yield (from yfinance)

Usage:
  python3 tools/forward_return.py                     # All positions + pipeline
  python3 tools/forward_return.py --ticker ADBE NVO   # Specific tickers only
  python3 tools/forward_return.py --active-only        # Only active positions
  python3 tools/forward_return.py --pipeline-only      # Only research pipeline
"""

import sys
import os
import re
import argparse
import yaml
import yfinance as yf
import warnings
warnings.filterwarnings('ignore')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORTFOLIO_FILE = os.path.join(BASE_DIR, 'portfolio', 'current.yaml')
SYSTEM_FILE = os.path.join(BASE_DIR, 'state', 'system.yaml')
THESIS_ACTIVE_DIR = os.path.join(BASE_DIR, 'thesis', 'active')
THESIS_RESEARCH_DIR = os.path.join(BASE_DIR, 'thesis', 'research')
DECISIONS_LOG = os.path.join(BASE_DIR, 'learning', 'decisions_log.yaml')


def load_portfolio():
    """Load portfolio positions from current.yaml."""
    try:
        with open(PORTFOLIO_FILE, 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error loading portfolio: {e}")
        return None


def load_system_qs():
    """Load authoritative QS/Tier from state/system.yaml portfolio_quality_analysis.
    Returns dict of {ticker: (qs, tier)}. This is the AUTHORITATIVE source
    calculated by quality_scorer.py, not the old X/10 format in thesis files."""
    try:
        with open(SYSTEM_FILE, 'r') as f:
            data = yaml.safe_load(f)
        positions = data.get('system', {}).get('portfolio_quality_analysis', {}).get('positions', [])
        result = {}
        for p in positions:
            ticker = p.get('ticker', '')
            score = p.get('score')
            tier = p.get('tier')
            if ticker and score is not None:
                result[ticker] = (score, tier)
        return result
    except Exception:
        return {}


def load_decisions_log():
    """Load decisions log for conviction data."""
    try:
        with open(DECISIONS_LOG, 'r') as f:
            return yaml.safe_load(f)
    except Exception:
        return None


def get_conviction_for_ticker(decisions_log, ticker):
    """Extract conviction level from decisions_log.yaml."""
    if not decisions_log:
        return 'medium'
    decisions = decisions_log.get('decisions', [])
    if not decisions:
        return 'medium'
    for d in reversed(decisions):
        dticker = d.get('ticker', '')
        if isinstance(dticker, str) and dticker.upper() == ticker.upper():
            conv = d.get('conviction', '')
            if not conv:
                details = d.get('details', {})
                if isinstance(details, dict):
                    conv = details.get('conviction', 'medium')
            if isinstance(conv, str):
                conv_lower = conv.lower().strip()
                if 'alta' in conv_lower or 'high' in conv_lower:
                    return 'high'
                elif 'baja' in conv_lower or 'low' in conv_lower:
                    return 'low'
            return 'medium'
    return 'medium'


def get_fx_rates():
    """Get EUR/USD and GBP/EUR and DKK/EUR exchange rates. Reports fallback usage."""
    defaults = {'EURUSD': 1.04, 'GBPEUR': 1.19, 'DKKEUR': 0.134}
    fallbacks_used = []

    try:
        eurusd = yf.Ticker('EURUSD=X').info.get('previousClose')
        if not eurusd:
            eurusd = defaults['EURUSD']
            fallbacks_used.append(f"EUR/USD={eurusd}")
    except Exception:
        eurusd = defaults['EURUSD']
        fallbacks_used.append(f"EUR/USD={eurusd}")
    try:
        gbpeur = yf.Ticker('GBPEUR=X').info.get('previousClose')
        if not gbpeur:
            gbpeur = defaults['GBPEUR']
            fallbacks_used.append(f"GBP/EUR={gbpeur}")
    except Exception:
        gbpeur = defaults['GBPEUR']
        fallbacks_used.append(f"GBP/EUR={gbpeur}")
    try:
        dkkeur = yf.Ticker('DKKEUR=X').info.get('previousClose')
        if not dkkeur:
            dkkeur = defaults['DKKEUR']
            fallbacks_used.append(f"DKK/EUR={dkkeur}")
    except Exception:
        dkkeur = defaults['DKKEUR']
        fallbacks_used.append(f"DKK/EUR={dkkeur}")

    if fallbacks_used:
        print(f"FX WARNING: Using static fallback rates ({', '.join(fallbacks_used)}). MoS% may be inaccurate.")

    return eurusd, gbpeur, dkkeur


def read_thesis_file(thesis_path):
    """Read thesis file content. Returns None if file doesn't exist."""
    full_path = os.path.join(BASE_DIR, thesis_path)
    if not os.path.exists(full_path):
        return None
    try:
        with open(full_path, 'r') as f:
            return f.read()
    except Exception:
        return None


def detect_currency_from_context(thesis_content, match_obj):
    """
    Detect the FV currency by examining:
    1. The matched text itself
    2. The immediate line context (same line as the match)
    3. The broader thesis context (first 3000 chars)

    Returns detected currency string or None.
    """
    # 1. Check within the match itself
    match_text = match_obj.group(0)
    for label, curr in [('EUR', 'EUR'), ('DKK', 'DKK'), ('SEK', 'SEK'),
                        ('$', 'USD'), ('GBp', 'GBp'), ('gbp', 'GBp'), ('GBP', 'GBP')]:
        if label in match_text:
            return curr
    if match_text.rstrip().endswith('p') and not match_text.rstrip().endswith('pp'):
        return 'GBp'

    # 2. Check the same line as the match (get 40 chars before and after)
    start = max(0, match_obj.start() - 40)
    end = min(len(thesis_content), match_obj.end() + 40)
    line_context = thesis_content[start:end]

    # Find what's immediately after the number (e.g., "850 SEK" or "850p")
    # Look for currency right after the matched number
    after_match = thesis_content[match_obj.end():match_obj.end() + 20]
    if re.match(r'\s*SEK\b', after_match):
        return 'SEK'
    if re.match(r'\s*DKK\b', after_match):
        return 'DKK'
    if re.match(r'\s*EUR\b', after_match):
        return 'EUR'
    if re.match(r'\s*GBp\b', after_match, re.IGNORECASE):
        return 'GBp'
    if re.match(r'\s*USD\b', after_match):
        return 'USD'
    if re.match(r'p\b', after_match):
        return 'GBp'

    # Check what's immediately before the number in the line
    before_match = thesis_content[max(0, match_obj.start() - 20):match_obj.start()]
    if 'SEK' in before_match:
        return 'SEK'
    if 'DKK' in before_match:
        return 'DKK'
    if '$' in before_match:
        return 'USD'
    if 'EUR' in before_match:
        return 'EUR'

    # 3. Broader context fallback - check within 200 chars around the match
    nearby_start = max(0, match_obj.start() - 100)
    nearby_end = min(len(thesis_content), match_obj.end() + 100)
    nearby = thesis_content[nearby_start:nearby_end]

    # Order matters: check SEK/DKK before EUR to avoid "850 SEK (74 EUR)" matching EUR
    for label, curr in [('SEK', 'SEK'), ('DKK', 'DKK'), ('GBp', 'GBp'),
                        ('EUR', 'EUR'), ('$', 'USD')]:
        if label in nearby:
            return curr

    return None


def extract_fair_value(thesis_content, ticker, currency='USD'):
    """
    Extract fair value from thesis file using multiple patterns.
    Returns (fair_value_in_native_currency, currency_of_fv) or (None, None).
    """
    if not thesis_content:
        return None, None

    fv = None
    fv_currency = currency

    # Optional markdown bold and currency patterns for reuse
    bold = r'\*{0,2}'
    curr_prefix = r'(?:\$|EUR\s*|GBP\s*|DKK\s*|SEK\s*)?'
    curr_suffix = r'(?:p|GBp)?'

    # Pattern priority (most specific first):
    patterns = [
        # "Weighted FV/Average" in table: | **Weighted ...** | ... | **$394** or **455p**
        (r'\*\*Weighted\s+(?:Avg|Average|FV|Fair Value)\*\*\s*\|[^|]*\|[^|]*\|\s*\*\*\s*' + curr_prefix + r'([0-9,]+(?:\.\d+)?)\s*' + curr_suffix + r'\s*\*\*', 'single'),
        # "Blended Fair Value" in table: | **Blended Fair Value** | ... | **3,701p**
        (r'\*\*Blended Fair Value\*\*\s*\|[^|]*\|[^|]*\|\s*\*\*\s*' + curr_prefix + r'([0-9,]+(?:\.\d+)?)\s*' + curr_suffix + r'\s*\*\*', 'single'),
        # "Weighted Fair Value: XXXp" or "Weighted Fair Value: EUR XX"
        (r'Weighted Fair Value[:\s]+' + curr_prefix + r'([0-9,]+(?:\.\d+)?)\s*' + curr_suffix, 'single'),
        # "Fair Value Consolidado: EUR XX - YY" (range, take midpoint)
        (r'Fair Value Consolidado:\s*(?:EUR|USD|\$|GBP|DKK)\s*([0-9,]+(?:\.\d+)?)\s*-\s*([0-9,]+(?:\.\d+)?)', 'range'),
        # "**Blended Base Fair Value:** $283.74" (with bold markers, UHS-style)
        (bold + r'Blended (?:Base )?Fair Value' + bold + r'[:\s]+' + curr_prefix + r'([0-9,]+(?:\.\d+)?)\s*' + curr_suffix, 'single'),
        # "Fair Value (Weighted)" in table row
        (r'Fair Value \(Weighted\)\s*\|\s*' + curr_prefix + r'([0-9,]+(?:\.\d+)?)', 'single'),
        # "Fair Value Base (Weighted)" in table row
        (r'Fair Value Base \(Weighted\)\s*\|\s*' + curr_prefix + r'([0-9,]+(?:\.\d+)?)', 'single'),
        # "Fair Value (v2.0 Base)" or similar in table
        (r'Fair Value\s*\((?:v\d+\.?\d*\s*)?Base\)\s*\|\s*' + curr_prefix + r'([0-9,]+(?:\.\d+)?)', 'single'),
        # "Fair Value Expected (v3.0): EUR XX"
        (r'Fair Value Expected[^:]*:\s*' + curr_prefix + r'([0-9,]+(?:\.\d+)?)', 'single'),
        # "Fair Value Base" 2-column table: | Fair Value Base | EUR 102 | EUR 122 |
        (r'Fair Value Base\s*\|\s*' + curr_prefix + r'[0-9,]+(?:\.\d+)?\s*\|\s*' + curr_prefix + r'([0-9,]+(?:\.\d+)?)', 'single'),
        # "Fair Value Base" simple: | Fair Value Base | EUR 122 |
        (r'Fair Value Base\s*\|\s*' + curr_prefix + r'([0-9,]+(?:\.\d+)?)', 'single'),
        # "Blended Fair Value (v2.0)" in table: | Blended Fair Value (v2.0) | $283.74 |
        (r'Blended Fair Value\s*\(v\d+\.?\d*\)\s*\|\s*' + curr_prefix + r'([0-9,]+(?:\.\d+)?)', 'single'),
        # "Conservative Fair Value Range: X,XXX - X,XXXp"
        (r'Conservative Fair Value Range:\s*' + curr_prefix + r'([0-9,]+(?:\.\d+)?)\s*-\s*([0-9,]+(?:\.\d+)?)\s*' + curr_suffix, 'range'),
        # "Base Case FV:" or "FV Base:" or "FV Expected:"
        (r'(?:Base Case FV|FV Base|FV Expected)[:\s]+~?\s*' + curr_prefix + r'([0-9,]+(?:\.\d+)?)\s*' + curr_suffix, 'single'),
        # "OEY Fair Value: ~XXXp" (backup)
        (r'OEY Fair Value[:\s]+~?\s*' + curr_prefix + r'([0-9,]+(?:\.\d+)?)\s*' + curr_suffix, 'single'),
        # "Fair Value v2.0: EUR XX-YY" (range in intro)
        (r'Fair Value v\d+\.?\d*:\s*' + curr_prefix + r'([0-9,]+(?:\.\d+)?)\s*-\s*([0-9,]+(?:\.\d+)?)', 'range'),
        # Generic "Fair Value: $XX" (last resort)
        (bold + r'Fair Value' + bold + r'[:\s]+' + curr_prefix + r'([0-9,]+(?:\.\d+)?)\s*' + curr_suffix, 'single'),
    ]

    for pat, pat_type in patterns:
        m = re.search(pat, thesis_content, re.IGNORECASE)
        if m:
            groups = m.groups()
            if pat_type == 'range' and len(groups) >= 2:
                try:
                    v1 = float(groups[0].replace(',', ''))
                    v2 = float(groups[1].replace(',', ''))
                    fv = (v1 + v2) / 2
                except (ValueError, TypeError):
                    continue
            else:
                try:
                    fv = float(groups[0].replace(',', ''))
                except (ValueError, TypeError):
                    continue

            if fv <= 0:
                fv = None
                continue

            # Detect currency using multi-layer context analysis
            detected = detect_currency_from_context(thesis_content, m)
            if detected:
                fv_currency = detected

            break

    return fv, fv_currency


def extract_growth_rate(thesis_content, ticker):
    """
    Extract expected growth rate from thesis.
    Returns growth as a decimal (e.g., 0.08 for 8%).
    """
    if not thesis_content:
        return None

    patterns = [
        (r'Expected Growth[^:]*:\s*(?:~)?(\d+(?:\.\d+)?)\s*%', 'single'),
        (r'Revenue Growth Base:\s*(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)\s*%', 'range'),
        (r'GP Growth[^:]*:\s*(?:~)?(\d+(?:\.\d+)?)\s*%\s*\(base', 'single'),
        (r'=\s*~?(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)\s*%\s*GP growth', 'range'),
        (r'GP CAGR[):\s]+(?:~)?(\d+(?:\.\d+)?)\s*%\s*\(base', 'single'),
        (r'Expected Growth \(GP CAGR\):\s*(\d+(?:\.\d+)?)\s*%', 'single'),
        (r'(?:Expected )?Growth:\s*(\d+(?:\.\d+)?)\s*%', 'single'),
        (r'Revenue Growth:\s*(?:~)?(\d+(?:\.\d+)?)\s*%', 'single'),
        (r'Revenue Growth\s*=.*?(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)\s*%', 'range'),
        (r'growth of\s*(?:~)?(\d+(?:\.\d+)?)\s*%', 'single'),
        (r'~?(\d+(?:\.\d+)?)\s*%\s*CAGR\s*\((?:normalized|base)', 'single'),
    ]

    for pat, pat_type in patterns:
        m = re.search(pat, thesis_content, re.IGNORECASE)
        if m:
            groups = m.groups()
            if pat_type == 'range' and len(groups) >= 2:
                try:
                    g1 = float(groups[0])
                    g2 = float(groups[1])
                    growth = (g1 + g2) / 2 / 100
                    if -0.50 <= growth <= 0.50:
                        return growth
                except (ValueError, TypeError):
                    continue
            else:
                try:
                    growth = float(groups[0]) / 100
                    if -0.50 <= growth <= 0.50:
                        return growth
                except (ValueError, TypeError):
                    continue

    return None


def extract_qs_and_tier(thesis_content):
    """Extract Quality Score and Tier from thesis content."""
    qs = None
    tier = None

    if not thesis_content:
        return qs, tier

    # Pattern 1: "Quality Score: 76/100" or "TOTAL SCORE: 76/100"
    m = re.search(r'(?:Quality Score|TOTAL SCORE|TOTAL)[:\s|]*\*?\*?(\d+)\s*/\s*100', thesis_content, re.IGNORECASE)
    if m:
        qs = int(m.group(1))

    # Pattern 2: "Quality Score: 9/10" (older format, approximate conversion)
    if qs is None:
        m = re.search(r'(?:Quality Score|QUALITY SCORE)[:\s]*\*?\*?(\d+(?:\.\d+)?)\s*/\s*10\b', thesis_content, re.IGNORECASE)
        if m:
            val = float(m.group(1))
            # Map old 1-10 scale to approximate 0-100 range
            # 10/10 ~ 85 (Tier A), 9/10 ~ 80, 8/10 ~ 75, 5/10 ~ 55, etc.
            qs = max(35, min(95, int(val * 8.5 + 10)))

    # Pattern 3: "| **TOTAL** | **81** | **100**" in table
    if qs is None:
        m = re.search(r'\*\*TOTAL\*\*\s*\|\s*\*\*(\d+)\*\*\s*\|\s*\*\*100\*\*', thesis_content)
        if m:
            qs = int(m.group(1))

    # Pattern 4: "TOTAL | **81** | 100" in table
    if qs is None:
        m = re.search(r'TOTAL\s*\|\s*\*?\*?(\d+)\*?\*?\s*\|\s*\*?\*?100\*?\*?', thesis_content)
        if m:
            qs = int(m.group(1))

    # Extract Tier
    m = re.search(r'Tier\s+([A-D])\b', thesis_content, re.IGNORECASE)
    if m:
        tier = m.group(1).upper()

    return qs, tier


def extract_status_from_research(thesis_content):
    """Extract status/notes for research pipeline entries."""
    if not thesis_content:
        return 'Research'

    m = re.search(r'Standing Order[:\s]*(.*?)(?:\n|$)', thesis_content, re.IGNORECASE)
    if m and len(m.group(1).strip()) > 3:
        return m.group(1).strip()[:50]

    m = re.search(r'(?:Verdict|Veredicto)[:\s]*(.*?)(?:\n|$)', thesis_content, re.IGNORECASE)
    if m and len(m.group(1).strip()) > 3:
        return m.group(1).strip()[:50]

    m = re.search(r'\*\*Status\*\*[:\s]*(.*?)(?:\n|$)', thesis_content, re.IGNORECASE)
    if m and len(m.group(1).strip()) > 3:
        return m.group(1).strip()[:50]

    return 'Research'


def convert_fv_to_price_currency(fv, fv_currency, stock_currency, eurusd, gbpeur, dkkeur):
    """Convert fair value to the stock's trading currency for MoS calculation."""
    if fv_currency == stock_currency:
        return fv

    # Convert to EUR first
    fv_eur = fv
    if fv_currency == 'USD':
        fv_eur = fv / eurusd
    elif fv_currency in ('GBp', 'GBX'):
        fv_eur = (fv / 100) * gbpeur
    elif fv_currency == 'GBP':
        fv_eur = fv * gbpeur
    elif fv_currency == 'DKK':
        fv_eur = fv * dkkeur
    elif fv_currency == 'SEK':
        fv_eur = fv * 0.088

    # Convert from EUR to target
    if stock_currency == 'EUR':
        return fv_eur
    elif stock_currency == 'USD':
        return fv_eur * eurusd
    elif stock_currency in ('GBp', 'GBX'):
        return (fv_eur / gbpeur) * 100
    elif stock_currency == 'GBP':
        return fv_eur / gbpeur
    elif stock_currency == 'DKK':
        return fv_eur / dkkeur if dkkeur else fv_eur
    elif stock_currency == 'SEK':
        return fv_eur / 0.088
    return fv_eur


def get_yfinance_data(ticker):
    """Get stock info from yfinance. Single call per ticker."""
    try:
        t = yf.Ticker(ticker)
        info = t.info
        if not info or 'symbol' not in info:
            return None
        return info
    except Exception:
        return None


def get_dividend_yield_pct(info):
    """
    Get reliable dividend yield percentage from yfinance info dict.

    Empirical findings from testing all portfolio currencies (EUR, USD, GBp, DKK):
    - dividendYield: ALREADY in percentage form (e.g., 2.97 = 2.97%, 0.74 = 0.74%)
      Reliable across all currencies. This is the PRIMARY source.
    - trailingAnnualDividendYield: UNRELIABLE for GBp stocks (wrong by 100x because
      dividendRate is in GBP but price is in GBp) and ADRs (cross-currency contamination).
    - dividendRate/price: Only reliable for EUR/USD stocks where both are same unit.
      Wrong for GBp stocks (dividendRate in GBP, price in pence).

    Strategy: Use dividendYield directly. It is already a percentage.
    """
    dy = info.get('dividendYield')

    if dy is None or not isinstance(dy, (int, float)):
        return 0.0

    # yfinance dividendYield is already in percentage form
    # e.g., DTE.DE=2.97, VICI=6.14, IMB.L=4.8, GL=0.74, NVO=3.9
    # Values are typically 0-15 for dividend-paying stocks
    if dy >= 0:
        return dy

    return 0.0


def process_position(ticker, thesis_path, eurusd, gbpeur, dkkeur, decisions_log, system_qs=None, is_research=False):
    """Process a single position/research ticker. Returns dict with all data fields."""
    result = {
        'ticker': ticker,
        'qs': None,
        'tier': None,
        'mos_pct': None,
        'growth_pct': None,
        'yield_pct': None,
        'conviction': None,
        'fv_source': None,
        'growth_source': None,
        'price': None,
        'fv': None,
        'currency': None,
        'is_research': is_research,
        'status': None,
        'error': None,
    }

    thesis_content = read_thesis_file(thesis_path)

    # QS/Tier: Use system.yaml as AUTHORITATIVE source (quality_scorer.py output)
    # Fall back to thesis file only if not in system.yaml
    if system_qs and ticker in system_qs:
        qs, tier = system_qs[ticker]
    else:
        qs, tier = extract_qs_and_tier(thesis_content)
    result['qs'] = qs
    result['tier'] = tier

    TICKER_MAP = {'LIGHT.NV': 'LIGHT.AS'}
    yf_ticker = TICKER_MAP.get(ticker, ticker)

    info = get_yfinance_data(yf_ticker)
    if info is None:
        result['error'] = 'No yfinance data'
        return result

    price = info.get('currentPrice') or info.get('regularMarketPrice') or info.get('previousClose')
    if price is None:
        result['error'] = 'No price data'
        return result

    stock_currency = info.get('currency', 'USD')
    result['price'] = price
    result['currency'] = stock_currency

    # Dividend yield - use dividendYield field directly (already in percentage)
    result['yield_pct'] = get_dividend_yield_pct(info)

    # Extract fair value from thesis
    fv_raw, fv_currency = extract_fair_value(thesis_content, ticker, stock_currency)

    if fv_raw is not None:
        fv_in_stock_currency = convert_fv_to_price_currency(
            fv_raw, fv_currency, stock_currency, eurusd, gbpeur, dkkeur
        )
        mos_pct = ((fv_in_stock_currency - price) / price) * 100
        result['mos_pct'] = mos_pct
        result['fv'] = fv_raw
        result['fv_source'] = f"{fv_raw:.1f} {fv_currency}"
    else:
        result['fv_source'] = 'N/A'

    # Extract growth from thesis first
    growth = extract_growth_rate(thesis_content, ticker)
    if growth is not None:
        result['growth_pct'] = growth * 100
        result['growth_source'] = 'thesis'
    else:
        # Fallback to yfinance analyst estimates
        yf_earnings_growth = info.get('earningsGrowth')
        yf_rev_growth = info.get('revenueGrowth')
        if yf_earnings_growth and isinstance(yf_earnings_growth, (int, float)):
            result['growth_pct'] = yf_earnings_growth * 100
            result['growth_source'] = 'yf_earn'
        elif yf_rev_growth and isinstance(yf_rev_growth, (int, float)):
            result['growth_pct'] = yf_rev_growth * 100
            result['growth_source'] = 'yf_rev'
        else:
            result['growth_pct'] = 0
            result['growth_source'] = 'none'

    # Conviction from portfolio or decisions_log (raw data, no multiplier)
    result['conviction'] = get_conviction_for_ticker(decisions_log, ticker)

    if is_research:
        result['status'] = extract_status_from_research(thesis_content)

    return result


def find_research_tickers():
    """Find all tickers in thesis/research/ directory."""
    results = []
    if not os.path.isdir(THESIS_RESEARCH_DIR):
        return results
    for entry in sorted(os.listdir(THESIS_RESEARCH_DIR)):
        thesis_path = os.path.join('thesis', 'research', entry, 'thesis.md')
        full_path = os.path.join(BASE_DIR, thesis_path)
        if os.path.exists(full_path):
            results.append((entry, thesis_path))
    return results


def print_ranking(active_results, research_results, show_active=True, show_pipeline=True):
    """Print the formatted data tables. No composite scores, no ranking highlights."""
    conv_short = {'high': 'H', 'medium': 'M', 'low': 'L'}

    if show_active and active_results:
        # Sort by MoS% descending (largest upside first), but this is just display order
        ranked = sorted(active_results, key=lambda x: x['mos_pct'] if x['mos_pct'] is not None else -999, reverse=True)

        print()
        print("=" * 100)
        print("FORWARD RETURN COMPONENTS -- ACTIVE POSITIONS")
        print("=" * 100)
        print(f"{'Ticker':<10} {'QS':>3} {'Tier':>4} {'MoS%':>7} {'Grw%':>6} {'Yld%':>6} {'Conv':>4} {'GrSrc':>7}  {'FV':>16}")
        print("-" * 100)

        for r in ranked:
            qs_str = str(r['qs']) if r['qs'] is not None else '?'
            tier_str = r['tier'] if r['tier'] else '?'
            mos_str = f"{r['mos_pct']:+.1f}" if r['mos_pct'] is not None else 'N/A'
            grw_str = f"{r['growth_pct']:.1f}" if r['growth_pct'] is not None else 'N/A'
            yld_str = f"{r['yield_pct']:.1f}" if r['yield_pct'] is not None else '0.0'
            conv_str = conv_short.get(r['conviction'], '?') if r['conviction'] else '?'
            gr_src_str = r['growth_source'] or '-'
            fv_str = r['fv_source'] if r['fv_source'] else 'N/A'

            if r['error']:
                print(f"{r['ticker']:<10} {'':>3} {'':>4} {'ERR':>7} {'':>6} {'':>6} {'':>4} {'':>7}  {r['error']}")
            else:
                print(f"{r['ticker']:<10} {qs_str:>3} {tier_str:>4} {mos_str:>7} {grw_str:>6} {yld_str:>6} {conv_str:>4} {gr_src_str:>7}  {fv_str:>16}")

        print("-" * 100)
        print(f"  {len(active_results)} positions | [Apply learning/principles.md to reason about this data]")

        no_fv = [r for r in ranked if r['mos_pct'] is None and r['error'] is None]
        if no_fv:
            print(f"  FV not found in thesis: {', '.join(r['ticker'] for r in no_fv)}")

    if show_pipeline and research_results:
        valid_research = [r for r in research_results if r['mos_pct'] is not None]
        invalid_research = [r for r in research_results if r['mos_pct'] is None]

        valid_research.sort(key=lambda x: x['mos_pct'], reverse=True)

        print()
        print("=" * 100)
        print("PIPELINE -- RESEARCH THESIS")
        print("=" * 100)
        print(f"{'Ticker':<10} {'QS':>3} {'Tier':>4} {'MoS%':>7} {'Grw%':>6} {'Yld%':>6} {'GrSrc':>7}  {'FV':>16} {'Status'}")
        print("-" * 100)

        for r in valid_research:
            qs_str = str(r['qs']) if r['qs'] is not None else '?'
            tier_str = r['tier'] if r['tier'] else '?'
            mos_str = f"{r['mos_pct']:+.1f}" if r['mos_pct'] is not None else 'N/A'
            grw_str = f"{r['growth_pct']:.1f}" if r['growth_pct'] is not None else 'N/A'
            yld_str = f"{r['yield_pct']:.1f}" if r['yield_pct'] is not None else '0.0'
            gr_src_str = r['growth_source'] or '-'
            fv_str = r['fv_source'] if r['fv_source'] else 'N/A'
            status = (r['status'] or '')[:45]

            print(f"{r['ticker']:<10} {qs_str:>3} {tier_str:>4} {mos_str:>7} {grw_str:>6} {yld_str:>6} {gr_src_str:>7}  {fv_str:>16} {status}")

        if invalid_research:
            print()
            print(f"Skipped (no FV in thesis): {', '.join(r['ticker'] for r in invalid_research)}")

    print()


def main():
    parser = argparse.ArgumentParser(description='Forward Return Ranking for portfolio positions')
    parser.add_argument('--ticker', nargs='+', help='Specific tickers to analyze')
    parser.add_argument('--active-only', action='store_true', help='Only show active positions')
    parser.add_argument('--pipeline-only', action='store_true', help='Only show research pipeline')

    args = parser.parse_args()

    portfolio = load_portfolio()
    if not portfolio:
        print("ERROR: Cannot load portfolio/current.yaml")
        sys.exit(1)

    positions = portfolio.get('positions', [])
    decisions_log = load_decisions_log()
    system_qs = load_system_qs()

    print("Loading FX rates...")
    eurusd, gbpeur, dkkeur = get_fx_rates()
    print(f"FX: EUR/USD={eurusd:.4f} | GBP/EUR={gbpeur:.4f} | DKK/EUR={dkkeur:.4f}")
    if system_qs:
        print(f"QS source: system.yaml ({len(system_qs)} tickers)")

    show_active = not args.pipeline_only
    show_pipeline = not args.active_only

    active_results = []
    if show_active:
        print(f"Processing {len(positions)} active positions...")
        for p in positions:
            ticker = p['ticker']
            if args.ticker and ticker not in args.ticker:
                continue
            thesis_path = p.get('thesis', f'thesis/active/{ticker}/thesis.md')
            result = process_position(ticker, thesis_path, eurusd, gbpeur, dkkeur, decisions_log, system_qs=system_qs, is_research=False)
            active_results.append(result)

    research_results = []
    if show_pipeline:
        research_tickers = find_research_tickers()
        active_tickers = {p['ticker'] for p in positions}
        research_tickers = [(t, path) for t, path in research_tickers if t not in active_tickers]
        if args.ticker:
            research_tickers = [(t, path) for t, path in research_tickers if t in args.ticker]
        if research_tickers:
            print(f"Processing {len(research_tickers)} research pipeline entries...")
            for ticker, thesis_path in research_tickers:
                result = process_position(ticker, thesis_path, eurusd, gbpeur, dkkeur, decisions_log, system_qs=system_qs, is_research=True)
                research_results.append(result)

    print_ranking(active_results, research_results, show_active, show_pipeline)


if __name__ == '__main__':
    main()
