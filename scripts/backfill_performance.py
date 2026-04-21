"""Backfill performance.json from portfolio/history.yaml."""
from __future__ import annotations
import json
import pathlib
import yaml
from datetime import date

ROOT = pathlib.Path(__file__).resolve().parent.parent


def backfill() -> dict:
    history_path = ROOT / "portfolio" / "history.yaml"
    if not history_path.exists():
        return {"error": "portfolio/history.yaml not found"}

    data = yaml.safe_load(history_path.read_text())
    closed = data.get("closed_positions", [])

    if not closed:
        return {"error": "No closed positions found"}

    pnls = [p.get("pnl_percent", 0) for p in closed]
    winners = [p for p in pnls if p > 0]
    losers = [p for p in pnls if p <= 0]

    perf = {
        "as_of_date": date.today().isoformat(),
        "total_return_pct": sum(pnls) / len(pnls) if pnls else 0,
        "hit_rate_pct": (len(winners) / len(pnls) * 100) if pnls else 0,
        "avg_return_pct": sum(pnls) / len(pnls) if pnls else 0,
        "avg_winner_pct": sum(winners) / len(winners) if winners else 0,
        "avg_loser_pct": sum(losers) / len(losers) if losers else 0,
        "total_positions_closed": len(closed),
    }

    output_dir = ROOT / "knowledge_base" / "portfolio"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "performance.json"
    output_path.write_text(json.dumps(perf, indent=2))
    print(f"Performance backfill written to {output_path}")
    return perf


if __name__ == "__main__":
    result = backfill()
    for k, v in result.items():
        print(f"  {k}: {v}")
