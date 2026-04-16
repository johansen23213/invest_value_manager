"""JSONL audit logger for ValueHunter v1.0 orchestrator runs."""
from __future__ import annotations

import json
import pathlib
import time
from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass
class AuditEvent:
    """A single audit event emitted during an orchestrator run."""

    run_id: str
    event_type: str  # run_start, agent_start, agent_end, run_end
    timestamp: float = field(default_factory=time.time)
    agent_id: str = ""
    data: dict[str, Any] = field(default_factory=dict)

    def to_json(self) -> str:
        return json.dumps(asdict(self), default=str)


class AuditLogger:
    """Append-only JSONL logger that writes one file per run_id."""

    def __init__(self, log_dir: str | pathlib.Path | None = None) -> None:
        if log_dir is None:
            log_dir = pathlib.Path(__file__).resolve().parent / "runs"
        self.log_dir = pathlib.Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)

    # ── low-level ───────────────────────────────────────────────────────

    def _log_path(self, run_id: str) -> pathlib.Path:
        return self.log_dir / f"{run_id}.jsonl"

    def log(self, event: AuditEvent) -> None:
        """Append a single AuditEvent as a JSONL line."""
        path = self._log_path(event.run_id)
        with open(path, "a") as f:
            f.write(event.to_json() + "\n")

    # ── convenience helpers ─────────────────────────────────────────────

    def log_run_start(
        self, run_id: str, flow: str, params: dict[str, Any] | None = None
    ) -> None:
        self.log(
            AuditEvent(
                run_id=run_id,
                event_type="run_start",
                data={"flow": flow, "params": params or {}},
            )
        )

    def log_agent_start(
        self, run_id: str, agent_id: str, inputs: dict[str, Any] | None = None
    ) -> None:
        self.log(
            AuditEvent(
                run_id=run_id,
                event_type="agent_start",
                agent_id=agent_id,
                data={"inputs": inputs or {}},
            )
        )

    def log_agent_end(
        self,
        run_id: str,
        agent_id: str,
        success: bool,
        tokens: int = 0,
        duration: float = 0.0,
        error: str | None = None,
    ) -> None:
        self.log(
            AuditEvent(
                run_id=run_id,
                event_type="agent_end",
                agent_id=agent_id,
                data={
                    "success": success,
                    "tokens": tokens,
                    "duration": duration,
                    "error": error,
                },
            )
        )

    def log_run_end(
        self, run_id: str, success: bool, summary: dict[str, Any] | None = None
    ) -> None:
        self.log(
            AuditEvent(
                run_id=run_id,
                event_type="run_end",
                data={"success": success, "summary": summary or {}},
            )
        )

    # ── read ────────────────────────────────────────────────────────────

    def read_run(self, run_id: str) -> list[AuditEvent]:
        """Read all events for a given run_id. Returns empty list if none."""
        path = self._log_path(run_id)
        if not path.exists():
            return []
        events: list[AuditEvent] = []
        with open(path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                d = json.loads(line)
                events.append(
                    AuditEvent(
                        run_id=d["run_id"],
                        event_type=d["event_type"],
                        timestamp=d["timestamp"],
                        agent_id=d.get("agent_id", ""),
                        data=d.get("data", {}),
                    )
                )
        return events
