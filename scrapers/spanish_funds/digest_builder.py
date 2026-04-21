"""Build human-readable Telegram digest from a newly-processed letter."""
from __future__ import annotations

from collections import defaultdict


def _format_aum(aum_eur: float | None) -> str:
    if not aum_eur:
        return "AuM: n/a"
    if aum_eur >= 1_000_000_000:
        return f"AuM: €{aum_eur / 1_000_000_000:.1f}B"
    return f"AuM: €{aum_eur / 1_000_000:.0f}M"


def _format_return(pct: float | None) -> str:
    if pct is None:
        return "Retorno: n/a"
    sign = "+" if pct >= 0 else ""
    return f"Retorno trimestre: {sign}{pct:.1f}%"


def _quarter_heading(q: str) -> str:
    year, qn = q.split("-")
    return f"{qn[0]}{qn[1].upper()} {year}"


def _trim(text: str | None, n: int = 60) -> str:
    if not text:
        return ""
    if len(text) <= n:
        return text
    return text[:n].rstrip() + "..."


def build_digest(letter: dict, multi_fund_tickers: list[str]) -> str:
    """Produce a markdown-friendly Telegram digest for a single new letter."""
    fund_name = letter["fund_name"]
    quarter = letter["quarter"]
    ret = _format_return(letter.get("fund_return_pct"))
    aum = _format_aum(letter.get("aum_eur"))

    by_action: dict[str, list[dict]] = defaultdict(list)
    unverified: list[dict] = []
    for p in letter.get("positions", []):
        if p.get("ticker_status") != "verified":
            unverified.append(p)
            continue
        by_action[p["action"]].append(p)

    parts = [
        f"📬 Nueva carta: {fund_name} {_quarter_heading(quarter)}",
        f"   {ret} | {aum}",
        "",
    ]

    news = by_action.get("new", [])
    if news:
        parts.append(f"🆕 NUEVAS ({len(news)})")
        for p in news:
            w = f"({p['weight_pct']:.1f}%)" if p.get("weight_pct") else ""
            snippet = _trim(p.get("thesis_text"))
            snippet_str = f' — "{snippet}"' if snippet else ""
            parts.append(f"   • {p['ticker']} {p['company_name']} {w}{snippet_str}")
        parts.append("")

    exits = by_action.get("exited", [])
    if exits:
        parts.append(f"❌ SALIDAS ({len(exits)})")
        for p in exits:
            parts.append(f"   • {p['ticker']} {p['company_name']}")
        parts.append("")

    incs = by_action.get("increased", [])
    if incs:
        tickers = ", ".join(p["ticker"] for p in incs)
        parts.append(f"📈 INCREMENTOS ({len(incs)}): {tickers}")

    reds = by_action.get("reduced", [])
    if reds:
        tickers = ", ".join(p["ticker"] for p in reds)
        parts.append(f"📉 REDUCCIONES ({len(reds)}): {tickers}")

    if multi_fund_tickers:
        parts.append("")
        parts.append("🔔 Multi-fund signals: " + ", ".join(multi_fund_tickers))

    if unverified:
        parts.append("")
        parts.append("⚠️ REQUIEREN RESOLUCIÓN MANUAL:")
        for p in unverified:
            proposed = p.get("ticker") or "(no ticker)"
            parts.append(f'   • "{p["company_name"]}" — ticker propuesto {proposed} no validado')

    return "\n".join(parts)
