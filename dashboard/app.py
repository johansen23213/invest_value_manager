"""ValueHunter Dashboard v1 — entry point.

The actual pages live in dashboard/pages/ and are auto-detected by Streamlit.
This file configures the page, sidebar, and shared state (share_mode).

Full setup wired in Task 6. This is a minimal stub.
"""
from __future__ import annotations

import streamlit as st


def main():
    st.set_page_config(
        page_title="ValueHunter",
        page_icon="🦅",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.title("🦅 ValueHunter")
    st.caption("Sub-project 0.5 Dashboard v1 MVP — setup in progress")
    st.info("Pages loading… Sidebar navigation coming in Task 6.")


if __name__ == "__main__":
    main()
