"""🎯 Pipeline — quality universe + adversarial pipeline funnel."""
from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from dashboard.components import (
    COLOR,
    CONVICTION_COLORS,
    PIPELINE_COLORS,
    TIER_COLORS,
)
from dashboard.data_loader import (
    compute_multi_fund_signals,
    load_universe,
)
from dashboard.sidebar import render_sidebar


st.set_page_config(page_title="Pipeline · ValueHunter", page_icon="🎯", layout="wide")
render_sidebar()

st.title("🎯 Pipeline & Universe")

df = load_universe()
if len(df) == 0:
    st.info("Quality universe is empty or unavailable.")
    st.stop()

# Enrich with conviction from spanish fund signals
multi_fund = compute_multi_fund_signals()
ticker_to_conviction: dict[str, str] = {}
ticker_to_funds: dict[str, list[str]] = {}
for _, row in multi_fund.iterrows():
    count = row["fund_count"]
    label = "3+_funds" if count >= 3 else "2_funds"
    ticker_to_conviction[row["ticker"]] = label
    ticker_to_funds[row["ticker"]] = [f["fund_id"] for f in row["funds"]]

df["conviction_signal"] = df["ticker"].map(lambda t: ticker_to_conviction.get(t, "1_fund"))

# ---------------------------------------------------------------------------
# Metrics row
# ---------------------------------------------------------------------------
c1, c2, c3, c4, c5 = st.columns(5)
universe_size = len(df)
c1.metric("Universe size", universe_size)
c2.metric("Tier A", (df["tier"] == "A").sum())
c3.metric("Actionable (entry ≤5%)", (df["distance_to_entry"].abs() <= 5).sum())
r1_complete = (df["pipeline_status"] == "R1_COMPLETE").sum()
c4.metric("R1_COMPLETE", f"{r1_complete}/{universe_size}")
r4_ready = (df["pipeline_status"] == "R4_READY").sum()
c5.metric("R4_READY", r4_ready)

st.markdown("---")

# ---------------------------------------------------------------------------
# Funnel
# ---------------------------------------------------------------------------
st.markdown("### Pipeline funnel")
with st.expander("What is the pipeline?", expanded=False):
    st.markdown(
        "Each company enters at **R1_NEW** after screening. Parallel adversarial rounds "
        "(R1 analysis → R2 devil's advocate → R3 resolution → R4 committee) progressively "
        "validate the thesis. **R4_READY** means the committee has approved and the company "
        "is waiting for entry price. **ACTIVE** means it's an open portfolio position."
    )

pipeline_order = ["R1_NEW", "R1_COMPLETE", "R2", "R3", "R4_READY", "ACTIVE"]
counts = [int((df["pipeline_status"] == stage).sum()) for stage in pipeline_order]
fig = go.Figure(go.Funnel(
    y=pipeline_order,
    x=counts,
    marker={"color": [PIPELINE_COLORS.get(s, COLOR["muted"]) for s in pipeline_order]},
    textinfo="value+percent previous",
))
fig.update_layout(height=320, margin=dict(t=20, b=10, l=80, r=10))
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------------------------------
# Filters
# ---------------------------------------------------------------------------
col1, col2, col3, col4 = st.columns([1, 1, 2, 1])
with col1:
    tier_filter = st.selectbox("Tier", ["All", "A", "B", "C"])
with col2:
    sector_filter = st.selectbox("Sector", ["All"] + sorted(df["sector"].dropna().unique().tolist()))
with col3:
    max_dist = st.slider("Max distance to entry (%)", 0, 100, 100)
with col4:
    if st.button("Reset filters"):
        st.rerun()

filtered = df.copy()
if tier_filter != "All":
    filtered = filtered[filtered["tier"] == tier_filter]
if sector_filter != "All":
    filtered = filtered[filtered["sector"] == sector_filter]
filtered = filtered[filtered["distance_to_entry"].abs() <= max_dist]

# ---------------------------------------------------------------------------
# Table
# ---------------------------------------------------------------------------
show_details = st.checkbox("Show details (QS, sector, funds)", value=False)
primary_cols = ["ticker", "name", "tier", "pipeline_status", "distance_to_entry", "conviction_signal"]
secondary_cols = ["qs_tool", "sector"]
cols = primary_cols + (secondary_cols if show_details else [])

column_config = {
    "tier": st.column_config.TextColumn("Tier", help="A ≥75, B 55-74, C 35-54, D <35 (not bought)."),
    "qs_tool": st.column_config.NumberColumn("QS", help="Quality Score 0-100."),
    "distance_to_entry": st.column_config.NumberColumn(
        "To entry %",
        help="Distance from current price to standing order trigger. Negative = at or below entry.",
        format="%.1f",
    ),
    "pipeline_status": st.column_config.TextColumn("Pipeline"),
    "conviction_signal": st.column_config.TextColumn(
        "Conviction",
        help="Spanish value fund overlap: 1/2/3+ funds hold this ticker.",
    ),
}

st.dataframe(
    filtered[[c for c in cols if c in filtered.columns]],
    use_container_width=True,
    hide_index=True,
    column_config=column_config,
)

st.caption(f"Showing {len(filtered)} of {len(df)} companies.")
