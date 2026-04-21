"""📊 Portfolio — active positions, exposure, allocation."""
from __future__ import annotations

import pandas as pd
import plotly.express as px
import streamlit as st

from dashboard.components import COLOR, TIER_COLORS, money, pct, pct_of_portfolio
from dashboard.data_loader import load_portfolio, load_prices
from dashboard.sidebar import render_sidebar


st.set_page_config(page_title="Portfolio · ValueHunter", page_icon="📊", layout="wide")
render_sidebar()
share_mode = st.session_state.get("share_mode", False)

st.title("📊 Portfolio")

portfolio = load_portfolio()
positions = portfolio.get("positions", [])
cash_usd = portfolio.get("cash_usd", 0.0)

if not positions:
    st.info("No active positions. Portfolio state file is empty or missing.")
    st.stop()

# Fetch live prices for each position
tickers = tuple(p["ticker"] for p in positions if p.get("ticker"))
prices = load_prices(tickers)

# Enrich positions with current value + P&L
enriched = []
for p in positions:
    ticker = p.get("ticker")
    price = prices.get(ticker)
    invested = p.get("invested_usd", 0) or 0
    shares = p.get("shares", 0) or 0
    current_value = (price * shares) if (price and shares) else 0
    pnl_pct = ((current_value - invested) / invested * 100) if invested else 0
    enriched.append({
        "ticker": ticker,
        "name": p.get("name", ""),
        "tier": p.get("tier", ""),
        "sector": p.get("sector", ""),
        "geo": p.get("geo", ""),
        "invested_usd": invested,
        "current_value_usd": current_value,
        "pnl_pct": pnl_pct,
        "fair_value": p.get("fair_value", 0),
        "conviction": p.get("conviction", ""),
    })

total_value = cash_usd + sum(e["current_value_usd"] for e in enriched)
total_invested = sum(e["invested_usd"] for e in enriched)
total_pnl_pct = ((total_value - cash_usd - total_invested) / total_invested * 100) if total_invested else 0

# ---------------------------------------------------------------------------
# Metrics row
# ---------------------------------------------------------------------------
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Portfolio value", money(total_value, share_mode))
c2.metric("P&L", pct(total_pnl_pct))
c3.metric("Cash", pct_of_portfolio(cash_usd, total_value))
c4.metric("Positions", len(enriched))
c5.metric("Net exposure", pct_of_portfolio(total_value - cash_usd, total_value))

st.markdown("---")

# ---------------------------------------------------------------------------
# Filters + column toggle
# ---------------------------------------------------------------------------
filter_col, toggle_col, reset_col = st.columns([2, 1, 1])
with filter_col:
    sectors = sorted({e["sector"] for e in enriched if e["sector"]})
    sector_filter = st.selectbox("Sector filter", ["All"] + sectors)
with toggle_col:
    show_details = st.checkbox("Show details (entry, FV, MoS)", value=False)
with reset_col:
    if st.button("Reset"):
        st.rerun()

rows = enriched if sector_filter == "All" else [e for e in enriched if e["sector"] == sector_filter]

# ---------------------------------------------------------------------------
# Primary table (share_mode aware)
# ---------------------------------------------------------------------------
df = pd.DataFrame(rows)
if share_mode:
    # Hide absolute $ columns
    df["value"] = df["current_value_usd"].apply(lambda v: pct_of_portfolio(v, total_value))
    primary_cols = ["ticker", "name", "tier", "value", "pnl_pct", "conviction"]
else:
    df["invested"] = df["invested_usd"].apply(lambda v: f"${v:,.0f}")
    df["value"] = df["current_value_usd"].apply(lambda v: f"${v:,.0f}")
    primary_cols = ["ticker", "name", "tier", "value", "pnl_pct", "conviction"]

if show_details:
    primary_cols = primary_cols + ["fair_value"]
    df["fair_value"] = df["fair_value"].apply(lambda v: f"${v:,.0f}" if v else "—")

column_config = {
    "tier": st.column_config.TextColumn("Tier", help="Quality tier A/B/C (≥75 / 55-74 / 35-54)."),
    "pnl_pct": st.column_config.NumberColumn("P&L %", format="%+.1f%%"),
    "fair_value": st.column_config.TextColumn("FV", help="Fair Value estimate per share."),
    "conviction": st.column_config.TextColumn("Conviction"),
}
st.dataframe(
    df[primary_cols] if all(c in df.columns for c in primary_cols) else df,
    use_container_width=True,
    hide_index=True,
    column_config=column_config,
)

# ---------------------------------------------------------------------------
# Allocation charts
# ---------------------------------------------------------------------------
st.markdown("### Allocation")
chart_col1, chart_col2 = st.columns(2)
with chart_col1:
    sector_agg = df.groupby("sector")["current_value_usd"].sum().reset_index()
    if len(sector_agg):
        fig = px.pie(sector_agg, names="sector", values="current_value_usd", hole=0.4)
        fig.update_layout(height=320, margin=dict(t=10, b=10, l=10, r=10))
        st.plotly_chart(fig, use_container_width=True)
with chart_col2:
    if "geo" in df.columns:
        geo_agg = df.groupby("geo")["current_value_usd"].sum().reset_index()
        if len(geo_agg):
            fig = px.bar(geo_agg, x="geo", y="current_value_usd",
                         labels={"current_value_usd": "USD" if not share_mode else "—"})
            fig.update_layout(height=320, margin=dict(t=10, b=10, l=10, r=10))
            st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------------------------------
# Shorts placeholder
# ---------------------------------------------------------------------------
st.markdown("### Shorts")
st.caption(
    "No short positions currently active. The system opens shorts when identifying "
    "overvalued or structurally fragile companies with a dated catalyst."
)

# Footer
with st.expander("Data sources"):
    st.caption("portfolio/current.yaml · live prices via yfinance (15 min cache)")
