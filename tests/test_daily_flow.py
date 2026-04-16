"""Tests for the daily monitoring flow and Governor integration."""
import pytest
from unittest.mock import patch, AsyncMock

from orchestrator.base import AgentResult
from orchestrator.governor import Governor


class TestDailyMonitoringFlow:
    @pytest.mark.asyncio
    async def test_daily_returns_monitoring_digest(self):
        mock_data = {
            "agent": "portfolio_monitor",
            "portfolio_summary": {"total_positions": 11, "net_pnl_pct": 3.5},
            "positions": [],
            "summary": "All positions on track.",
        }
        with patch("orchestrator.flows.daily_monitoring.PortfolioMonitorAgent") as m:
            inst = AsyncMock()
            inst.agent_id = "a32"
            inst.run = AsyncMock(
                return_value=AgentResult(
                    agent_id="a32",
                    agent_name="test",
                    success=True,
                    data=mock_data,
                    tokens_used=200,
                    duration_seconds=1.0,
                )
            )
            m.return_value = inst

            gov = Governor()
            result = await gov.run_daily_monitor()

            assert result["flow"] == "daily-monitor"
            assert result["success"] is True
            assert result["data"]["agent"] == "portfolio_monitor"

    @pytest.mark.asyncio
    async def test_daily_handles_agent_failure(self):
        with patch("orchestrator.flows.daily_monitoring.PortfolioMonitorAgent") as m:
            inst = AsyncMock()
            inst.agent_id = "a32"
            inst.run = AsyncMock(
                return_value=AgentResult(
                    agent_id="a32",
                    agent_name="test",
                    success=False,
                    error="API timeout",
                    tokens_used=0,
                    duration_seconds=5.0,
                )
            )
            m.return_value = inst

            gov = Governor()
            result = await gov.run_daily_monitor()

            assert result["flow"] == "daily-monitor"
            assert result["success"] is False
