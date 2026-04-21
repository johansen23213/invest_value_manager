"""ValueHunter Dashboard v1 — entry point.

Streamlit multi-page app. Pages auto-detected from dashboard/pages/.
This file:
- Sets the global page config (title, icon, layout).
- Renders the sidebar (settings, glossary, share_mode toggle).
- Shows a landing blurb when the user lands on / (before picking a page).
"""
from __future__ import annotations

import streamlit as st

from dashboard.sidebar import render_sidebar


def main() -> None:
    st.set_page_config(
        page_title="ValueHunter",
        page_icon="🦅",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    render_sidebar()

    st.title("🦅 ValueHunter")
    st.caption("Multi-agent investment analysis system — Dashboard v1")
    st.markdown(
        "Select a page from the sidebar:\n\n"
        "- **🏠 Glance** — morning operator glance (SOs, earnings, actions today)\n"
        "- **📊 Portfolio** — active positions, exposure, allocation\n"
        "- **🎯 Pipeline** — quality universe + adversarial pipeline funnel\n"
        "- **🇪🇸 Spanish Funds** — holdings from 5 Spanish value funds"
    )


if __name__ == "__main__":
    main()
