"""📊 Portfolio — active positions, exposure, allocation."""
from __future__ import annotations

import re

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


def _parse_fair_value(v) -> float | None:
    """Extract first numeric token from fair_value string. Returns float or None."""
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip()
    m = re.search(r"[-+]?\d*\.?\d+", s.replace(",", ""))
    return float(m.group()) if m else None


# Enrich positions with current value + P&L + derived metrics
enriched = []
for p in positions:
    ticker = p.get("ticker")
    price = prices.get(ticker)
    invested = p.get("invested_usd", 0) or 0
    shares = p.get("shares", 0) or 0
    current_value = (price * shares) if (price and shares) else 0
    pnl_pct_val = ((current_value - invested) / invested * 100) if invested else 0

    # Parse fair value and derive mos_pct + ecagr
    fv_raw = p.get("fair_value")
    fv_numeric = _parse_fair_value(fv_raw)
    if fv_numeric is not None and price and price > 0:
        mos_pct = (fv_numeric - price) / fv_numeric * 100
        ecagr = ((fv_numeric / price) ** (1 / 3) - 1) * 100
    else:
        mos_pct = None
        ecagr = None

    enriched.append({
        "ticker": ticker,
        "name": p.get("name", ""),
        "tier": p.get("tier", ""),
        "sector": p.get("sector", ""),
        "geo": p.get("geo", ""),
        "invested_usd": invested,
        "current_value_usd": current_value,
        "pnl_pct": pnl_pct_val,
        "status": p.get("conviction", ""),
        "mos_pct": mos_pct,
        "ecagr": ecagr,
        "last_review": p.get("last_review", "unknown"),
        "exit_plan": p.get("exit_plan", "No exit plan recorded."),
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
# Sector filter
# ---------------------------------------------------------------------------
sectors = sorted({e["sector"] for e in enriched if e["sector"]})
sector_filter = st.selectbox("Sector filter", ["All"] + sectors)

rows = enriched if sector_filter == "All" else [e for e in enriched if e["sector"] == sector_filter]

# ---------------------------------------------------------------------------
# Primary table — 8 fixed columns (no toggle)
# ---------------------------------------------------------------------------
df = pd.DataFrame(rows)

# Compute weight_pct for each row
if total_value > 0:
    df["weight_pct"] = df["current_value_usd"] / total_value * 100
else:
    df["weight_pct"] = 0.0

primary_cols = ["ticker", "name", "tier", "weight_pct", "pnl_pct", "mos_pct", "ecagr", "status"]

column_config = {
    "ticker": st.column_config.TextColumn("Ticker"),
    "name": st.column_config.TextColumn("Name"),
    "tier": st.column_config.TextColumn("Tier", help="Quality tier — A ≥75 QS, B 55-74, C 35-54."),
    "weight_pct": st.column_config.NumberColumn("Weight %", format="%.1f%%"),
    "pnl_pct": st.column_config.NumberColumn("P&L %", format="%+.1f%%"),
    "mos_pct": st.column_config.NumberColumn(
        "MoS %",
        format="%.1f%%",
        help="Margin of Safety — how far current price is below Fair Value. Higher = more buffer.",
    ),
    "ecagr": st.column_config.NumberColumn(
        "E[CAGR] %",
        format="%.1f%%",
        help="Expected CAGR to Fair Value over ~3 years.",
    ),
    "status": st.column_config.TextColumn(
        "Status",
        help="Portfolio status from Joan's last review — conviction level relative to thesis strength.",
    ),
}

event = st.dataframe(
    df[primary_cols],
    use_container_width=True,
    hide_index=True,
    column_config=column_config,
    selection_mode="single-row",
    on_select="rerun",
    key="portfolio_table",
)

# Show detail panel below if row selected
if event.selection.rows:
    idx = event.selection.rows[0]
    selected_row = rows[idx] if idx < len(rows) else None
    if selected_row:
        with st.container(border=True):
            ticker = selected_row.get("ticker", "?")
            last_review = selected_row.get("last_review", "unknown")
            exit_plan = selected_row.get("exit_plan", "No exit plan recorded.")
            st.markdown(f"### {ticker} detail")
            st.caption(f"Last review: {last_review}")
            st.markdown(f"**Exit plan / thesis excerpt:**\n\n{exit_plan}")

st.caption(
    "ℹ️ P&L % uses local currency prices from yfinance. FX normalization is not applied; "
    "positions in non-USD currencies may include FX drift in the displayed P&L."
)

# ---------------------------------------------------------------------------
# Allocation charts
# ---------------------------------------------------------------------------
st.markdown("### Allocation")
chart_col1, chart_col2 = st.columns(2)
with chart_col1:
    sector_agg = df.groupby("sector")["current_value_usd"].sum().reset_index()
    if len(sector_agg):
        if share_mode:
            sector_agg["pct"] = sector_agg["current_value_usd"] / total_value * 100
            fig = px.pie(sector_agg, names="sector", values="pct", hole=0.4)
        else:
            fig = px.pie(sector_agg, names="sector", values="current_value_usd", hole=0.4)
        fig.update_layout(height=320, margin=dict(t=10, b=10, l=10, r=10))
        st.plotly_chart(fig, use_container_width=True)
with chart_col2:
    if "geo" in df.columns:
        geo_agg = df.groupby("geo")["current_value_usd"].sum().reset_index()
        if len(geo_agg):
            if share_mode:
                geo_agg["pct"] = geo_agg["current_value_usd"] / total_value * 100
                fig = px.bar(geo_agg, x="geo", y="pct", labels={"pct": "% of portfolio"})
            else:
                fig = px.bar(geo_agg, x="geo", y="current_value_usd", labels={"current_value_usd": "USD"})
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
