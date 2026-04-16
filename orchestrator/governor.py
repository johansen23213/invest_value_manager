"""Governor state machine for ValueHunter v1.0 orchestrator."""
from __future__ import annotations

import uuid
from enum import Enum
from typing import Any

from orchestrator.audit import AuditLogger
from orchestrator.registry import AgentRegistry


class GovernorState(str, Enum):
    IDLE = "IDLE"
    SCREENING = "SCREENING"
    CANDIDATE_SELECTION = "CANDIDATE_SELECTION"
    ANALYSIS_FANOUT = "ANALYSIS_FANOUT"
    DECISION = "DECISION"
    NOTIFY = "NOTIFY"


class Governor:
    """Orchestrator state machine that sequences agent runs.

    Sprint 1: skeleton with stub flows that log events and return
    placeholder results.  Actual Claude API calls come in Sprint 2+.
    """

    def __init__(self) -> None:
        self.registry = AgentRegistry()
        self.audit = AuditLogger()
        self.state = GovernorState.IDLE

    # ── state machine helpers ───────────────────────────────────────────

    def _transition(self, new_state: GovernorState) -> None:
        self.state = new_state

    def _new_run_id(self) -> str:
        return uuid.uuid4().hex[:12]

    # ── public query methods ────────────────────────────────────────────

    def list_agents(self) -> list[dict]:
        return self.registry.list_agents()

    def dry_run(self) -> None:
        """Print registry summary to stdout (no agents executed)."""
        print(self.registry.summary())

    # ── flow stubs ──────────────────────────────────────────────────────

    async def run_on_demand(self, ticker: str) -> dict[str, Any]:
        """On-demand analysis of a single ticker (stub)."""
        run_id = self._new_run_id()
        self.audit.log_run_start(run_id, "on-demand", {"ticker": ticker})

        self._transition(GovernorState.ANALYSIS_FANOUT)
        # Sprint 2+: fan out A2.1-A2.5 in parallel for `ticker`
        self._transition(GovernorState.DECISION)
        # Sprint 2+: run A3.1 Decision Maker
        self._transition(GovernorState.NOTIFY)
        # Sprint 2+: send Telegram digest
        self._transition(GovernorState.IDLE)

        self.audit.log_run_end(run_id, True, {"flow": "on-demand", "ticker": ticker})
        return {"run_id": run_id, "flow": "on-demand", "ticker": ticker, "status": "stub"}

    async def run_weekly(self) -> dict[str, Any]:
        """Weekly screening flow (stub)."""
        run_id = self._new_run_id()
        self.audit.log_run_start(run_id, "weekly", {})

        self._transition(GovernorState.SCREENING)
        # Sprint 2+: run A1.1 + A1.2 in parallel
        self._transition(GovernorState.CANDIDATE_SELECTION)
        # Sprint 2+: consolidate top-5
        self._transition(GovernorState.ANALYSIS_FANOUT)
        # Sprint 2+: for each candidate, fan out A2.*
        self._transition(GovernorState.DECISION)
        # Sprint 2+: run A3.1 per candidate
        self._transition(GovernorState.NOTIFY)
        # Sprint 2+: send Telegram digest
        self._transition(GovernorState.IDLE)

        self.audit.log_run_end(run_id, True, {"flow": "weekly"})
        return {"run_id": run_id, "flow": "weekly", "status": "stub"}

    async def run_daily_monitor(self) -> dict[str, Any]:
        """Daily monitoring flow (stub)."""
        run_id = self._new_run_id()
        self.audit.log_run_start(run_id, "daily-monitor", {})

        self._transition(GovernorState.SCREENING)
        # Sprint 2+: run A3.2 Portfolio Monitor
        self._transition(GovernorState.NOTIFY)
        # Sprint 2+: send Telegram digest if changes
        self._transition(GovernorState.IDLE)

        self.audit.log_run_end(run_id, True, {"flow": "daily-monitor"})
        return {"run_id": run_id, "flow": "daily-monitor", "status": "stub"}
