"""One-shot migration of Horos legacy JSON to unified spanish_fund_position schema.

Legacy format (flat list of positions in knowledge_base/universe/horos_positions.json).
New format (one file per quarter, under knowledge_base/spanish_funds/horos/).
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LEGACY_PATH = ROOT / "knowledge_base" / "universe" / "horos_positions.json"
NEW_DIR = ROOT / "knowledge_base" / "spanish_funds" / "horos"


LEGACY_STATUS_MAP = {
    "EXACT": "verified",
    "FUZZY_MATCH": "ambiguous",
    "UNRESOLVED": "unverified",
}

LEGACY_ACTION_MAP = {
    "NEW": "new",
    "INCREASED": "increased",
    "DECREASED": "reduced",
    "MAINTAINED": "maintained",
    "EXITED": "exited",
}


def _convert_position(row: dict) -> dict:
    ticker = row.get("ticker") or ""
    return {
        "company_name": row["company"],
        "ticker": ticker,
        "ticker_status": LEGACY_STATUS_MAP.get(row.get("ticker_confidence", "UNRESOLVED"), "unverified"),
        "weight_pct": row.get("weight_pct"),
        "action": LEGACY_ACTION_MAP.get((row.get("action") or "MAINTAINED").upper(), "maintained"),
        "upside_pct": row.get("upside_pct"),
        "thesis_text": row.get("thesis_summary"),
    }


def migrate_legacy_json(legacy_positions: list[dict]) -> list[dict]:
    """Group flat positions by quarter and emit one letter JSON per quarter."""
    grouped: dict[str, list[dict]] = defaultdict(list)
    source_urls: dict[str, str] = {}
    for row in legacy_positions:
        q = row["letter_quarter"]
        grouped[q].append(_convert_position(row))
        source_urls[q] = row["source_url"]

    out: list[dict] = []
    for quarter, positions in sorted(grouped.items()):
        out.append({
            "fund_id": "horos",
            "fund_name": "Horos Value Internacional",
            "quarter": quarter,
            "extracted_at": datetime.now(timezone.utc).isoformat(),
            "extraction_model": "regex-v1-legacy-backfill",
            "source_url": source_urls[quarter],
            "fund_return_pct": None,
            "aum_eur": None,
            "positions": positions,
        })
    return out


def main():
    if not LEGACY_PATH.exists():
        print(f"No legacy file at {LEGACY_PATH}; nothing to migrate.")
        return 0
    legacy = json.loads(LEGACY_PATH.read_text())
    migrated = migrate_legacy_json(legacy)
    NEW_DIR.mkdir(parents=True, exist_ok=True)
    for letter in migrated:
        out = NEW_DIR / f"{letter['quarter']}.json"
        out.write_text(json.dumps(letter, indent=2, ensure_ascii=False))
        print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
