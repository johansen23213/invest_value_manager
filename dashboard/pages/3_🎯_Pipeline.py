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

# Add fund names for display (shows which funds hold this ticker)
def _fmt_funds(t: str) -> str:
    funds = ticker_to_funds.get(t, [])
    if not funds:
        return ""
    # Capitalize fund_ids for display: "cobas" → "Cobas"
    return " + ".join(sorted(f.capitalize() for f in funds))

df["funds"] = df["ticker"].apply(_fmt_funds)

# Ensure e_cagr column exists
if "e_cagr" not in df.columns:
    df["e_cagr"] = None

def _distance_bucket_icon(d) -> str:
    if d is None:
        return ""
    try:
        d = float(d)
    except (TypeError, ValueError):
        return ""
    if d <= 0:
        return "🟢"  # at entry
    elif d <= 15:
        return "🟡"  # near
    else:
        return "⚪"  # far

df["dist_icon"] = df["distance_to_entry"].apply(_distance_bucket_icon)

CONVICTION_DISPLAY = {"1_fund": "1 fund", "2_funds": "2 funds", "3+_funds": "3+ funds"}
df["conviction_signal"] = df["conviction_signal"].map(lambda x: CONVICTION_DISPLAY.get(x, x))

# ---------------------------------------------------------------------------
# Metrics row
# ---------------------------------------------------------------------------
c1, c2, c3, c4, c5 = st.columns(5)
universe_size = len(df)
c1.metric("Universe size", universe_size)
c2.metric("Tier A", (df["tier"] == "A").sum())
c3.metric("Actionable (entry ≤5%)", (df["distance_to_entry"].abs() <= 5).sum())
r1_complete = (df["pipeline_status"] == "R1_COMPLETE").sum()
r1_pct = r1_complete / universe_size if universe_size else 0
c4.metric("R1_COMPLETE", f"{r1_complete}/{universe_size} ({r1_pct:.0%})")
r4_ready = (df["pipeline_status"] == "R4_READY").sum()
r4_pct = r4_ready / universe_size if universe_size else 0
c5.metric("R4_READY", f"{r4_ready}/{universe_size} ({r4_pct:.0%})")

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
fig.update_layout(height=320, margin=dict(t=20, b=10, l=100, r=10))
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------------------------------
# Filters
# ---------------------------------------------------------------------------
col1, col2, col3, col4 = st.columns([1, 1, 2, 1])
with col1:
    tier_filter = st.selectbox("Tier", ["All", "A", "B", "C"], key="pipeline_tier_filter")
with col2:
    sector_filter = st.selectbox(
        "Sector",
        ["All"] + sorted(df["sector"].dropna().unique().tolist()),
        key="pipeline_sector_filter",
    )
with col3:
    max_dist = st.slider("Max distance to entry (%)", 0, 100, 100, key="pipeline_max_dist")
with col4:
    if st.button("Reset filters"):
        for key in ["pipeline_tier_filter", "pipeline_sector_filter", "pipeline_max_dist"]:
            st.session_state.pop(key, None)
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
primary_cols = ["dist_icon", "ticker", "name", "tier", "pipeline_status",
                "distance_to_entry", "e_cagr", "conviction_signal"]
secondary_cols = ["qs_tool", "sector", "funds"]
cols = primary_cols + (secondary_cols if show_details else [])

column_config = {
    "dist_icon": st.column_config.TextColumn("", help="🟢 at entry · 🟡 near (1-15%) · ⚪ far (>15%)"),
    "tier": st.column_config.TextColumn("Tier", help="A ≥75, B 55-74, C 35-54, D <35 (not bought)."),
    "qs_tool": st.column_config.NumberColumn("QS", help="Quality Score 0-100."),
    "distance_to_entry": st.column_config.NumberColumn(
        "To entry %",
        help="Distance from current price to standing order trigger. Negative = at or below entry.",
        format="%.1f",
    ),
    "e_cagr": st.column_config.NumberColumn(
        "E[CAGR] %",
        format="%.1f",
        help="Expected 3-year CAGR at current market price.",
    ),
    "pipeline_status": st.column_config.TextColumn(
        "Pipeline",
        help="Pipeline stage: R1_NEW → R1_COMPLETE → R2 → R3 → R4_READY → ACTIVE",
    ),
    "conviction_signal": st.column_config.TextColumn(
        "Conviction",
        help="Spanish value fund overlap (1/2/3+ funds). See 'funds' in details for names.",
    ),
    "funds": st.column_config.TextColumn(
        "Funds",
        help="Spanish value funds currently holding this ticker.",
    ),
}

st.dataframe(
    filtered[[c for c in cols if c in filtered.columns]],
    use_container_width=True,
    hide_index=True,
    column_config=column_config,
)

st.caption(f"Showing {len(filtered)} of {len(df)} companies.")
