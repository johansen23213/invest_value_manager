"""ValueHunter v1.0 — Streamlit Dashboard (read-only KB viewer)."""
from __future__ import annotations
import json
import pathlib
import yaml
import streamlit as st

ROOT = pathlib.Path(__file__).resolve().parent.parent


def load_yaml(rel_path: str):
    path = ROOT / rel_path
    if path.exists():
        return yaml.safe_load(path.read_text())
    return None


def load_json(rel_path: str):
    path = ROOT / rel_path
    if path.exists():
        return json.loads(path.read_text())
    return None


def page_portfolio():
    st.header("Portfolio")
    data = load_yaml("portfolio/current.yaml")
    if not data:
        st.warning("portfolio/current.yaml not found")
        return
    positions = data.get("positions", [])
    st.metric("Active Positions", len(positions))
    st.metric("Cash", f"${data.get('cash', 0):,.2f}")
    if positions:
        import pandas as pd
        df = pd.DataFrame(positions)
        cols = [c for c in ["ticker", "name", "shares", "invested_usd", "conviction", "fair_value"] if c in df.columns]
        st.dataframe(df[cols], use_container_width=True)


def page_pipeline():
    st.header("Pipeline")
    data = load_yaml("state/quality_universe.yaml")
    if not data:
        st.warning("quality_universe.yaml not found")
        return
    companies = data.get("quality_universe", {}).get("companies", [])
    st.metric("Universe Size", len(companies))
    if companies:
        import pandas as pd
        df = pd.DataFrame(companies)
        cols = [c for c in ["ticker", "name", "tier", "qs_tool", "pipeline_status", "distance_to_entry"] if c in df.columns]
        if cols:
            st.dataframe(df[cols].sort_values("qs_tool", ascending=False) if "qs_tool" in cols else df[cols], use_container_width=True)


def page_decisions():
    st.header("Decisions Log")
    data = load_yaml("learning/decisions_log.yaml")
    if not data:
        st.warning("decisions_log.yaml not found")
        return
    decisions = data.get("sizing_decisions", [])
    st.metric("Total Decisions", len(decisions))
    if decisions:
        import pandas as pd
        df = pd.DataFrame(decisions)
        cols = [c for c in ["date", "ticker", "action", "sizing", "outcome"] if c in df.columns]
        st.dataframe(df[cols], use_container_width=True)


def page_ideas():
    st.header("External Ideas")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Horos Positions")
        horos = load_json("knowledge_base/universe/horos_positions.json")
        if horos:
            st.metric("Positions Tracked", len(horos))
            import pandas as pd
            st.dataframe(pd.DataFrame(horos)[["letter_quarter", "company", "ticker", "upside_pct", "action"]] if horos else pd.DataFrame())
        else:
            st.info("No Horos data yet. Run: python -m scrapers.horos_scraper")
    with col2:
        st.subheader("Alpha Vulture Ideas")
        av = load_json("knowledge_base/universe/alpha_vulture_ideas.json")
        if av:
            st.metric("Ideas Tracked", len(av))
            import pandas as pd
            st.dataframe(pd.DataFrame(av)[["post_date", "title", "ticker", "situation_type"]] if av else pd.DataFrame())
        else:
            st.info("No Alpha Vulture data yet. Run: python -m scrapers.alpha_vulture_scraper")


def page_performance():
    st.header("Performance")
    perf = load_json("knowledge_base/portfolio/performance.json")
    if not perf:
        st.info("Performance data not generated yet.")
        return
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Return", f"{perf.get('total_return_pct', 0):.1f}%")
    col2.metric("Hit Rate", f"{perf.get('hit_rate_pct', 0):.0f}%")
    col3.metric("Sharpe Ratio", f"{perf.get('sharpe_ratio', 0):.2f}")


def main():
    st.set_page_config(page_title="ValueHunter v1.0", page_icon="\U0001f985", layout="wide")
    st.title("ValueHunter v1.0")
    st.caption("Multi-agent investment analysis system")

    page = st.sidebar.selectbox("Page", ["Portfolio", "Pipeline", "Decisions", "External Ideas", "Performance"])

    if page == "Portfolio":
        page_portfolio()
    elif page == "Pipeline":
        page_pipeline()
    elif page == "Decisions":
        page_decisions()
    elif page == "External Ideas":
        page_ideas()
    elif page == "Performance":
        page_performance()


if __name__ == "__main__":
    main()
