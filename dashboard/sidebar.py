"""Sidebar + glossary + share_mode for the dashboard."""
from __future__ import annotations

from typing import Mapping

import streamlit as st

from dashboard.data_loader import load_portfolio  # for freshness hint


GLOSSARY_TERMS: list[tuple[str, str]] = [
    ("QS", "Quality Score — composite quality metric (0-100) combining financial strength, growth, moat, capital allocation."),
    ("MoS", "Margin of Safety — percentage the current price is below Fair Value."),
    ("FV", "Fair Value — intrinsic value estimate per share."),
    ("E[CAGR]", "Expected Compound Annual Growth Rate to Fair Value."),
    ("Tier", "Quality tier (A ≥75 QS, B 55-74, C 35-54). Below 35 = do not buy."),
    ("R1-R4", "Adversarial buy pipeline rounds (parallel analysis → devil's advocate → resolution → committee)."),
    ("KC", "Kill Condition — pre-defined scenario that invalidates a thesis."),
    ("SO", "Standing Order — pre-approved buy/sell trigger with price level."),
    ("Conviction", "Number of Spanish value funds that currently hold a ticker (1/2/3+)."),
]


def resolve_share_mode_from_params(params: Mapping[str, str]) -> bool:
    """Parse share_mode from URL query params. `?share=1` or `?share=true` → True."""
    val = params.get("share", "").lower().strip()
    return val in ("1", "true")


def render_sidebar() -> None:
    """Render the persistent sidebar: settings, glossary, freshness."""
    with st.sidebar:
        st.markdown("### ⚙️ Settings")
        # Initialize share_mode on first load from URL param
        if "share_mode_initialized" not in st.session_state:
            params = st.query_params.to_dict() if hasattr(st, "query_params") else {}
            st.session_state.share_mode = resolve_share_mode_from_params(params)
            st.session_state.share_mode_initialized = True

        st.session_state.share_mode = st.checkbox(
            "Share mode (hide €)",
            value=st.session_state.share_mode,
            help="Anonymizes absolute € values for external sharing. % always visible.",
        )

        if st.button("🔄 Refresh data", use_container_width=True):
            st.cache_data.clear()
            st.rerun()

        st.caption(f"Share mode: {'ON' if st.session_state.share_mode else 'OFF'}")

        st.markdown("---")
        with st.expander("📖 Glossary", expanded=False):
            for term, definition in GLOSSARY_TERMS:
                st.markdown(f"**{term}** — {definition}")

        st.markdown("---")
        st.caption("🦅 ValueHunter Dashboard v1")
        st.caption("Desktop-optimized. Mobile acceptable.")
