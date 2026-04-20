"""Merge verified fund positions into state/quality_universe.yaml.

For each verified ticker across fund letters, we append a source entry and
recompute a conviction_signal label. Idempotent on (fund_id, quarter).
"""
from __future__ import annotations

from datetime import date
from pathlib import Path

import yaml

DEFAULT_UNIVERSE_PATH = (
    Path(__file__).resolve().parent.parent.parent / "state" / "quality_universe.yaml"
)

SNIPPET_MAX_CHARS = 500


def _signal_label(n: int) -> str:
    if n == 1:
        return "1_fund"
    if n == 2:
        return "2_funds"
    return "3+_funds"


def merge_letter(letter: dict, universe_path: Path | None = None) -> None:
    path = universe_path or DEFAULT_UNIVERSE_PATH
    data = yaml.safe_load(path.read_text()) if path.exists() else {}
    fund_id = letter["fund_id"]
    quarter = letter["quarter"]

    for pos in letter.get("positions", []):
        if pos.get("ticker_status") != "verified":
            continue
        ticker = pos["ticker"]
        entry = data.get(ticker) or {
            "added_at": date.today().isoformat(),
            "sources": [],
            "conviction_signal": "1_fund",
            "thesis_snippets": {},
        }
        sources = entry.setdefault("sources", [])

        # Idempotency: remove any existing source from (fund_id, quarter) before appending
        sources[:] = [s for s in sources if not (s["fund"] == fund_id and s["quarter"] == quarter)]
        sources.append({
            "fund": fund_id,
            "quarter": quarter,
            "weight": pos.get("weight_pct"),
            "action": pos.get("action"),
        })

        # Recompute conviction over distinct funds
        distinct_funds = len({s["fund"] for s in sources})
        entry["conviction_signal"] = _signal_label(distinct_funds)

        # Thesis snippets: max 2 funds; keep the latest per fund; trim
        thesis = pos.get("thesis_text") or ""
        if thesis:
            snippets = entry.setdefault("thesis_snippets", {})
            snippets[fund_id] = thesis[:SNIPPET_MAX_CHARS]
            # Keep only the most recent 2 funds by insertion order
            if len(snippets) > 2:
                keep = dict(list(snippets.items())[-2:])
                entry["thesis_snippets"] = keep

        data[ticker] = entry

    path.write_text(yaml.safe_dump(data, allow_unicode=True, sort_keys=True))
