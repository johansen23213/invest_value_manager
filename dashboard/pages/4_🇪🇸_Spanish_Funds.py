"""🇪🇸 Spanish Funds — holdings from Cobas/AzValor/Magallanes/Horos/Valentum."""
from __future__ import annotations

from datetime import date

import pandas as pd
import streamlit as st

from dashboard.components import COLOR, CONVICTION_COLORS
from dashboard.data_loader import compute_multi_fund_signals, load_spanish_funds
from dashboard.sidebar import render_sidebar


st.set_page_config(page_title="Spanish Funds · ValueHunter", page_icon="🇪🇸", layout="wide")
render_sidebar()

st.title("🇪🇸 Spanish Value Funds")

funds = load_spanish_funds()
if not funds:
    st.info(
        "No Spanish fund data available. Run the weekly ingestion via "
        "`python -m scrapers.spanish_funds.cli --all` to populate."
    )
    st.stop()

# ---------------------------------------------------------------------------
# Top-level unique ticker count
# ---------------------------------------------------------------------------
unique_tickers = set()
for fund_id, letter in funds.items():
    for p in letter.get("positions", []):
        if p.get("ticker_status") == "verified" and p.get("ticker"):
            unique_tickers.add(p["ticker"])

c1, c2 = st.columns(2)
c1.metric("Funds processed", len(funds))
c2.metric("Unique tickers (verified)", len(unique_tickers))

st.markdown("---")

# ---------------------------------------------------------------------------
# Fund cards grid
# ---------------------------------------------------------------------------
st.markdown("### Fund overview")
fund_ids = ["cobas", "azvalor", "magallanes", "horos", "valentum"]
cols = st.columns(len(fund_ids))
for col, fid in zip(cols, fund_ids):
    letter = funds.get(fid)
    with col:
        if letter is None:
            st.markdown(f"**{fid.title()}**")
            st.caption("_No letter yet._")
            continue
        st.markdown(f"**{letter.get('fund_name', fid.title())}**")
        st.caption(f"Last: {letter.get('quarter', '?')}")
        aum = letter.get("aum_eur")
        ret = letter.get("fund_return_pct")
        if aum:
            aum_str = f"€{aum/1e9:.1f}B" if aum >= 1e9 else f"€{aum/1e6:.0f}M"
            st.caption(f"AuM: {aum_str}")
        if ret is not None:
            sign = "+" if ret >= 0 else ""
            st.caption(f"Return: {sign}{ret:.1f}%")
        st.caption(f"Positions: {len(letter.get('positions', []))}")
        src = letter.get("source_url")
        if src:
            st.markdown(f"[view letter ↗]({src})")

st.markdown("---")

# ---------------------------------------------------------------------------
# Multi-fund signals (HERO section — placed before per-fund tabs)
# ---------------------------------------------------------------------------
st.markdown("### 🔔 Multi-fund conviction signals")
st.caption("Tickers held by 2 or more Spanish value funds simultaneously.")

signals = compute_multi_fund_signals()
if len(signals) == 0:
    st.info("No multi-fund overlaps in the latest quarterly letters.")
else:
    for _, row in signals.iterrows():
        ticker = row["ticker"]
        count = row["fund_count"]
        label = "3+_funds" if count >= 3 else "2_funds"
        color = CONVICTION_COLORS[label]
        with st.expander(
            f"**{ticker}** — {row.get('company_name', '')} · **{count} funds**",
            expanded=False,
        ):
            fund_cols = st.columns(min(count, 3))
            for i, f in enumerate(row["funds"][:3]):
                with fund_cols[i]:
                    st.markdown(f"**{f.get('fund_name', f['fund_id'])}**")
                    weight = f.get("weight_pct")
                    action = f.get("action", "")
                    st.caption(
                        f"Weight: {weight:.1f}%" if weight is not None else "Weight: —"
                    )
                    st.caption(f"Action: {action}")
                    thesis = (f.get("thesis_text") or "")[:300]
                    if thesis:
                        st.markdown(f"> {thesis}")

st.markdown("---")

# ---------------------------------------------------------------------------
# Per-fund tabs with holdings table
# ---------------------------------------------------------------------------
st.markdown("### Per-fund holdings")
tabs = st.tabs([funds.get(fid, {}).get("fund_name", fid.title()) if funds.get(fid) else fid.title()
                for fid in fund_ids])
for tab, fid in zip(tabs, fund_ids):
    with tab:
        letter = funds.get(fid)
        if letter is None:
            st.caption("No letter processed yet.")
            continue
        positions = letter.get("positions", [])
        rows = []
        unverified = []
        for p in positions:
            if p.get("ticker_status") != "verified":
                unverified.append(p)
                continue
            rows.append({
                "company": p.get("company_name", ""),
                "ticker": p.get("ticker", ""),
                "weight_pct": p.get("weight_pct", None),
                "fund_view": p.get("action", ""),
                "thesis_snippet": (p.get("thesis_text") or "")[:200],
            })
        if rows:
            df = pd.DataFrame(rows)
            st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.caption("No verified holdings in this letter.")
        if unverified:
            with st.expander(f"⚠️ {len(unverified)} unverified ticker(s) pending resolution"):
                for p in unverified:
                    st.caption(f"- {p.get('company_name', '?')} (proposed: {p.get('ticker', '?')})")

st.markdown("---")
st.caption("Data source: knowledge_base/spanish_funds/*/*.json (latest quarter per fund)")
