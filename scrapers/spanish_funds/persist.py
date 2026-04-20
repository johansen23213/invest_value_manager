"""Disk persistence for extracted letters and per-fund processing state."""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_KB_ROOT = Path(__file__).resolve().parent.parent.parent / "knowledge_base"


def _fund_dir(fund_id: str, kb_root: Path | None = None) -> Path:
    root = kb_root or DEFAULT_KB_ROOT
    d = root / "spanish_funds" / fund_id
    d.mkdir(parents=True, exist_ok=True)
    return d


def persist_letter(letter: dict, kb_root: Path | None = None) -> Path:
    """Write the extracted letter JSON to spanish_funds/{fund_id}/{quarter}.json."""
    fund_id = letter["fund_id"]
    quarter = letter["quarter"]
    d = _fund_dir(fund_id, kb_root)
    path = d / f"{quarter}.json"
    path.write_text(json.dumps(letter, indent=2, ensure_ascii=False))
    return path


def load_letter(fund_id: str, quarter: str, kb_root: Path | None = None) -> dict | None:
    path = _fund_dir(fund_id, kb_root) / f"{quarter}.json"
    if not path.exists():
        return None
    return json.loads(path.read_text())


def save_raw_pdf(pdf_bytes: bytes, fund_id: str, quarter: str, kb_root: Path | None = None) -> Path:
    raw_dir = _fund_dir(fund_id, kb_root) / "raw"
    raw_dir.mkdir(exist_ok=True)
    path = raw_dir / f"{quarter}.pdf"
    path.write_bytes(pdf_bytes)
    return path


def update_last_processed(
    fund_id: str,
    quarter: str,
    content_hash: str,
    kb_root: Path | None = None,
    extraction_model: str = "",
    url_hash: str = "",
) -> None:
    path = _fund_dir(fund_id, kb_root) / "last_processed.json"
    payload = {
        "quarter": quarter,
        "content_hash": content_hash,
        "url_hash": url_hash,
        "extraction_model": extraction_model,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    path.write_text(json.dumps(payload, indent=2))


def already_processed(fund_id: str, content_hash: str, kb_root: Path | None = None) -> bool:
    path = _fund_dir(fund_id, kb_root) / "last_processed.json"
    if not path.exists():
        return False
    prev = json.loads(path.read_text())
    return prev.get("content_hash") == content_hash or prev.get("url_hash") == content_hash
