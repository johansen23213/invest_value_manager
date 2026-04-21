"""🏠 Glance — morning operator glance."""
from __future__ import annotations

import streamlit as st

from dashboard.components import COLOR, money, pct
from dashboard.data_loader import (
    compute_actions_today,
    load_calendar,
    load_macro,
    load_portfolio,
    load_prices,
    load_standing_orders,
)
from dashboard.sidebar import render_sidebar


st.set_page_config(page_title="Glance · ValueHunter", page_icon="🏠", layout="wide")
render_sidebar()

share_mode = st.session_state.get("share_mode", False)

st.title("🏠 Morning Glance")

# ---------------------------------------------------------------------------
# Header metrics bar
# ---------------------------------------------------------------------------
portfolio = load_portfolio()
positions = portfolio.get("positions", [])
cash_usd = portfolio.get("cash_usd", 0.0)
total_value = cash_usd + sum(p.get("invested_usd", 0) or 0 for p in positions)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Portfolio value", money(total_value, share_mode) if total_value else "—")
col2.metric("Cash", f"{(cash_usd / total_value * 100 if total_value else 0):.0f}%")
col3.metric("Positions", len(positions))
col4.metric("Shorts", 0)  # placeholder

st.markdown("---")

# ---------------------------------------------------------------------------
# Three alert panels
# ---------------------------------------------------------------------------
panel_left, panel_mid, panel_right = st.columns(3)

with panel_left:
    st.markdown("### 🔴 Triggered SOs")
    triggered = [
        so for so in load_standing_orders()
        if str(so.get("current_distance", "0%")).replace("%", "").lstrip("-").replace(".", "").isdigit()
        and float(str(so.get("current_distance", "0%")).replace("%", "")) <= 0
    ]
    if triggered:
        for so in triggered[:5]:
            st.markdown(
                f"- **{so['ticker']}** {so.get('trigger', '')} "
                f"<span style='color:{COLOR['urgent_red']}'>●</span>",
                unsafe_allow_html=True,
            )
    else:
        st.caption("No SOs triggered.")

    near = [
        so for so in load_standing_orders()
        if so.get("category") == "ACTIVE"
        and str(so.get("current_distance", "100%")).replace("%", "").replace(".", "").isdigit()
        and 0 < float(str(so.get("current_distance", "100%")).replace("%", "")) <= 5
    ]
    if near:
        with st.expander(f"+ {len(near)} near trigger"):
            for so in near:
                st.markdown(f"- {so['ticker']} ({so.get('current_distance', '?')})")

with panel_mid:
    st.markdown("### 📅 Earnings (7d)")
    cal = load_calendar(days=7)
    earnings = cal[cal["type"] == "earnings"] if "type" in cal.columns else cal
    if len(earnings) == 0:
        st.caption("No earnings in next 7 days.")
    else:
        for _, row in earnings.iterrows():
            st.markdown(f"- **{row['ticker']}** — {row['date']}")
            st.caption(str(row.get("notes", ""))[:80])

with panel_right:
    st.markdown("### ⚠️ Macro")
    macro = load_macro()
    if not macro:
        st.caption("Macro data unavailable.")
    else:
        vix = macro.get("vix")
        oil = macro.get("oil_wti")
        if vix is not None:
            interp = "constructive" if vix < 20 else "caution" if vix < 30 else "risk-off"
            st.markdown(f"- VIX **{vix:.1f}** — {interp}")
        if oil is not None:
            st.markdown(f"- Oil WTI **${oil:.0f}**")
        sp = macro.get("sp500")
        if sp is not None:
            st.markdown(f"- S&P 500 **{sp:,.0f}**")

st.markdown("---")

# ---------------------------------------------------------------------------
# Top actions
# ---------------------------------------------------------------------------
st.markdown("### 🎯 Top actions today")
actions = compute_actions_today()
if not actions:
    st.info("No priority actions detected.")
else:
    for i, action in enumerate(actions[:10], start=1):
        prio = action.get("priority", "MEDIA")
        prio_color = COLOR["urgent_red"] if prio == "ALTA" else COLOR["warning_amber"]
        st.markdown(
            f"{i}. <span style='color:{prio_color}'>[{prio}]</span> "
            f"**{action['ticker']}** — {action.get('reason', '')}",
            unsafe_allow_html=True,
        )

st.markdown("---")

# ---------------------------------------------------------------------------
# Kill conditions + pending events placeholders
# (full data layer comes from thesis parsing — deferred to v2)
# ---------------------------------------------------------------------------
kc_col, pe_col = st.columns(2)
with kc_col:
    st.markdown("### 🔴 Kill conditions")
    st.caption(
        "Kill condition proximity tracking requires thesis parsing (not yet implemented). "
        "See thesis/active/*/thesis.md for KC details."
    )
with pe_col:
    st.markdown("### ⏳ Pending events")
    st.caption("Manual tracking via notes in thesis files for now.")

st.caption(f"Share mode: {'ON (€ hidden)' if share_mode else 'OFF'}")
