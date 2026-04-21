"""Cross-fund contextual lookup for the Web Researcher agent.

Given a ticker, return which Spanish value funds currently hold it, each
fund's most recent thesis snippet, weight, and action, considering only
the latest quarter on disk per fund.
"""
from __future__ import annotations

import json
from pathlib import Path

DEFAULT_KB_ROOT = Path(__file__).resolve().parent.parent.parent / "knowledge_base"


def _latest_letter(fund_dir: Path) -> dict | None:
    files = sorted(fund_dir.glob("[0-9]*.json"))
    if not files:
        return None
    return json.loads(files[-1].read_text())


def lookup_spanish_funds(ticker: str, kb_root: Path | None = None) -> dict:
    root = (kb_root or DEFAULT_KB_ROOT) / "spanish_funds"
    if not root.exists():
        return {"ticker": ticker, "fund_count": 0, "holdings": []}

    holdings = []
    for fund_dir in sorted(root.iterdir()):
        if not fund_dir.is_dir():
            continue
        letter = _latest_letter(fund_dir)
        if not letter:
            continue
        for p in letter.get("positions", []):
            if p.get("ticker") == ticker and p.get("ticker_status") == "verified":
                holdings.append({
                    "fund_id": letter["fund_id"],
                    "fund_name": letter["fund_name"],
                    "quarter": letter["quarter"],
                    "weight_pct": p.get("weight_pct"),
                    "action": p.get("action"),
                    "thesis_snippet": (p.get("thesis_text") or "")[:500] or None,
                })
                break

    return {"ticker": ticker, "fund_count": len(holdings), "holdings": holdings}
