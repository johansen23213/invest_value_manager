"""Flow 3 — Daily portfolio monitoring.
Runs A3.2 Portfolio Monitor against all active positions.
"""
from __future__ import annotations

from typing import Any

from orchestrator.audit import AuditLogger
from agents.a32_portfolio_monitor import PortfolioMonitorAgent


async def run_daily_monitoring(run_id: str, audit: AuditLogger) -> dict[str, Any]:
    monitor = PortfolioMonitorAgent()
    audit.log_agent_start(run_id, monitor.agent_id, {"flow": "daily-monitor"})
    result = await monitor.run({"flow": "daily-monitor"}, run_id=run_id)
    audit.log_agent_end(
        run_id,
        monitor.agent_id,
        result.success,
        tokens=result.tokens_used,
        duration=result.duration_seconds,
        error=result.error,
    )
    return {
        "run_id": run_id,
        "flow": "daily-monitor",
        "success": result.success,
        "data": result.data,
        "tokens_used": result.tokens_used,
        "duration_seconds": result.duration_seconds,
    }
