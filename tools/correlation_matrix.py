#!/usr/bin/env python3
"""
Correlation Matrix Calculator for Portfolio
Calculates pairwise correlations between positions to detect concentration risk.

Usage:
  python3 tools/correlation_matrix.py TICKER1 TICKER2 TICKER3 ...
  python3 tools/correlation_matrix.py --from-portfolio

Output:
  - Correlation matrix heatmap
  - Flagged pairs with correlation > 0.7
  - Portfolio diversification ratio
  - Average correlation
"""

import argparse
import sys
import numpy as np
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import yaml


def load_portfolio_tickers(yaml_path='/home/angel/value_invest2/portfolio/current.yaml'):
    """Extract tickers from portfolio YAML."""
    try:
        with open(yaml_path, 'r') as f:
            portfolio = yaml.safe_load(f)

        # Mapping for tickers that differ between portfolio and yfinance
        TICKER_MAP = {'LIGHT.NV': 'LIGHT.AS'}

        tickers = []
        if 'positions' in portfolio:
            for pos in portfolio['positions']:
                if 'ticker' in pos:
                    t = pos['ticker']
                    tickers.append(TICKER_MAP.get(t, t))

        return tickers
    except Exception as e:
        print(f"Error reading portfolio: {e}")
        return []


def download_returns(tickers, period='1y'):
    """Download daily returns for tickers using yfinance."""
    print(f"\nDownloading {period} of data for {len(tickers)} tickers...")

    # Download adjusted close prices
    data = yf.download(tickers, period=period, progress=False, auto_adjust=True)['Close']

    if isinstance(data, pd.Series):
        # Single ticker case
        data = data.to_frame()
        data.columns = [tickers[0]]

    # Calculate daily returns
    returns = data.pct_change().dropna()

    # Check for missing data
    missing = returns.isnull().sum()
    if missing.any():
        print(f"\nWarning: Missing data detected:")
        for ticker, count in missing[missing > 0].items():
            print(f"  {ticker}: {count} missing values")

    return returns


def calculate_correlation_matrix(returns):
    """Calculate correlation matrix from returns."""
    return returns.corr()


def diversification_ratio(returns, weights=None):
    """
    Calculate portfolio diversification ratio.
    DR = (weighted avg volatility) / (portfolio volatility)
    DR > 1 indicates diversification benefit.
    """
    if weights is None:
        # Equal weights
        weights = np.ones(len(returns.columns)) / len(returns.columns)

    weights = np.array(weights)

    # Individual volatilities
    individual_vols = returns.std()

    # Weighted average volatility
    weighted_avg_vol = np.dot(weights, individual_vols)

    # Portfolio volatility (accounts for correlations)
    cov_matrix = returns.cov()
    portfolio_vol = np.sqrt(np.dot(weights, np.dot(cov_matrix, weights)))

    dr = weighted_avg_vol / portfolio_vol if portfolio_vol > 0 else 0

    return dr, weighted_avg_vol, portfolio_vol


def format_correlation_matrix(corr_matrix):
    """Format correlation matrix for terminal display."""
    # Create a formatted string representation
    n = len(corr_matrix)
    tickers = corr_matrix.columns.tolist()

    # Calculate column widths
    max_ticker_len = max(len(t) for t in tickers)
    col_width = max(6, max_ticker_len)

    # Header
    output = "\n" + " " * col_width + " "
    for ticker in tickers:
        output += f"{ticker:>{col_width}} "
    output += "\n"

    # Separator
    output += "-" * (col_width + 1 + (col_width + 1) * n) + "\n"

    # Data rows
    for i, ticker in enumerate(tickers):
        output += f"{ticker:>{col_width}} "
        for j in range(n):
            val = corr_matrix.iloc[i, j]

            # Color coding via value display
            if i == j:
                cell = "  1.00"  # Diagonal
            elif abs(val) >= 0.7:
                cell = f"[{val:5.2f}]"  # High correlation - flagged
            elif abs(val) >= 0.5:
                cell = f" {val:5.2f} "  # Moderate
            else:
                cell = f" {val:5.2f} "  # Low

            output += f"{cell:>{col_width}} "
        output += "\n"

    return output


def find_high_correlations(corr_matrix, threshold=0.7):
    """Find pairs with correlation above threshold."""
    high_corr_pairs = []

    n = len(corr_matrix)
    for i in range(n):
        for j in range(i + 1, n):  # Only upper triangle
            corr_val = corr_matrix.iloc[i, j]
            if abs(corr_val) >= threshold:
                high_corr_pairs.append({
                    'ticker1': corr_matrix.columns[i],
                    'ticker2': corr_matrix.columns[j],
                    'correlation': corr_val
                })

    return sorted(high_corr_pairs, key=lambda x: abs(x['correlation']), reverse=True)


def main():
    parser = argparse.ArgumentParser(description='Calculate portfolio correlation matrix')
    parser.add_argument('tickers', nargs='*', help='Stock tickers to analyze')
    parser.add_argument('--from-portfolio', action='store_true',
                       help='Read tickers from portfolio/current.yaml')
    parser.add_argument('--period', default='1y',
                       help='Data period (default: 1y). Options: 1mo, 3mo, 6mo, 1y, 2y, 5y')
    parser.add_argument('--threshold', type=float, default=0.7,
                       help='Correlation threshold for flagging (default: 0.7)')

    args = parser.parse_args()

    # Determine tickers
    if args.from_portfolio:
        tickers = load_portfolio_tickers()
        if not tickers:
            print("Error: No tickers found in portfolio")
            sys.exit(1)
        print(f"Loaded {len(tickers)} tickers from portfolio: {', '.join(tickers)}")
    elif args.tickers:
        tickers = args.tickers
    else:
        print("Error: Provide tickers as arguments or use --from-portfolio")
        parser.print_help()
        sys.exit(1)

    # Download data
    try:
        returns = download_returns(tickers, period=args.period)
    except Exception as e:
        print(f"Error downloading data: {e}")
        sys.exit(1)

    if returns.empty:
        print("Error: No data retrieved")
        sys.exit(1)

    print(f"Retrieved {len(returns)} days of returns")

    # Calculate correlation matrix
    corr_matrix = calculate_correlation_matrix(returns)

    # Display results
    print("\n" + "=" * 80)
    print("CORRELATION MATRIX")
    print("=" * 80)
    print(format_correlation_matrix(corr_matrix))

    # Calculate statistics
    print("\n" + "=" * 80)
    print("CORRELATION STATISTICS")
    print("=" * 80)

    # Average correlation (excluding diagonal)
    mask = np.ones(corr_matrix.shape, dtype=bool)
    np.fill_diagonal(mask, False)
    avg_corr = corr_matrix.where(mask).mean().mean()
    print(f"\nAverage correlation (excl. diagonal): {avg_corr:.3f}")

    # Min/Max correlation
    corr_values = corr_matrix.where(mask).values.flatten()
    corr_values = corr_values[~np.isnan(corr_values)]
    print(f"Min correlation: {corr_values.min():.3f}")
    print(f"Max correlation: {corr_values.max():.3f}")

    # Diversification ratio
    dr, weighted_vol, portfolio_vol = diversification_ratio(returns)
    print(f"\nDiversification Ratio: {dr:.3f}")
    print(f"  Weighted Avg Volatility: {weighted_vol*100:.2f}%")
    print(f"  Portfolio Volatility: {portfolio_vol*100:.2f}%")

    if dr > 1:
        benefit = (1 - 1/dr) * 100
        print(f"  Diversification benefit: {benefit:.1f}% risk reduction")

    # High correlation pairs
    print("\n" + "=" * 80)
    print(f"HIGH CORRELATION PAIRS (threshold: {args.threshold})")
    print("=" * 80)

    high_corr = find_high_correlations(corr_matrix, threshold=args.threshold)

    if high_corr:
        print(f"\n⚠️  Found {len(high_corr)} pairs with correlation >= {args.threshold}:\n")
        for pair in high_corr:
            print(f"  {pair['ticker1']} <-> {pair['ticker2']}: {pair['correlation']:6.3f}")
        print("\n⚠️  High correlation may indicate concentration risk.")
        print("   Consider diversifying across uncorrelated positions.")
    else:
        print(f"\n✓ No pairs found with correlation >= {args.threshold}")
        print("  Portfolio appears well-diversified across positions.")

    print("\n" + "=" * 80)

    # Interpretation guide
    print("\nINTERPRETATION:")
    print("  [value] = High correlation (>= 0.7) - potential concentration risk")
    print("  Correlation > 0.7: Strong positive relationship")
    print("  Correlation 0.3-0.7: Moderate relationship")
    print("  Correlation < 0.3: Weak relationship")
    print("  Negative correlation: Moves in opposite directions")
    print("\n  Diversification Ratio > 1.0: Portfolio benefits from diversification")
    print("  Diversification Ratio ~ 1.0: Limited diversification benefit")
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()
