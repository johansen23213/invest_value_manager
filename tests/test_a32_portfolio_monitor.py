"""Tests for the Portfolio Monitor agent (A3.2)."""
from __future__ import annotations

import json
from unittest.mock import AsyncMock, patch

import pytest

from agents._tool_runner import ToolResult
from agents.a32_portfolio_monitor import PortfolioMonitorAgent, PROMPT_PATH
from orchestrator.base import AgentLayer, AgentModel

VALID_RESPONSE = {
    "agent": "portfolio_monitor",
    "date": "2026-04-16",
    "positions": [
        {
            "ticker": "MORN",
            "current_price": 175.0,
            "fair_value": 195.0,
            "pnl_pct": 5.2,
            "thesis_status": "ON_TRACK",
            "alerts": ["Near 52-week high"],
        },
        {
            "ticker": "DOM.L",
            "current_price": 620.0,
            "fair_value": 750.0,
            "pnl_pct": -2.1,
            "thesis_status": "DRIFTING",
            "alerts": ["MoS degraded below 15%"],
        },
    ],
    "portfolio_summary": {
        "total_positions": 11,
        "net_pnl_pct": 3.5,
        "positions_on_track": 8,
        "positions_drifting": 2,
        "positions_alert": 1,
    },
    "upcoming_events": [
        {"ticker": "MORN", "event": "Q1 earnings", "date": "2026-05-01", "priority": "high"}
    ],
    "action_items": ["Review MORN pre-earnings framework", "Check DOM.L thesis drift"],
    "summary": "Portfolio performing well with 3.5% net P&L. Two positions drifting from thesis.",
}


class TestInit:
    def test_agent_id(self):
        agent = PortfolioMonitorAgent()
        assert agent.agent_id == "a32"

    def test_agent_name(self):
        agent = PortfolioMonitorAgent()
        assert agent.name == "Portfolio Monitor"

    def test_agent_model(self):
        agent = PortfolioMonitorAgent()
        assert agent.model == AgentModel.HAIKU

    def test_agent_layer(self):
        agent = PortfolioMonitorAgent()
        assert agent.layer == AgentLayer.PORTFOLIO


class TestPrompt:
    def test_prompt_file_exists(self):
        assert PROMPT_PATH.exists(), f"Prompt file not found: {PROMPT_PATH}"

    def test_prompt_is_nonempty(self):
        content = PROMPT_PATH.read_text()
        assert len(content) > 100


class TestRun:
    @pytest.mark.asyncio
    async def test_run_with_mocked_tools_and_api(self):
        agent = PortfolioMonitorAgent()

        with (
            patch("agents.a32_portfolio_monitor.run_investment_tool") as mock_tool,
            patch("agents.a32_portfolio_monitor.AsyncAnthropic") as mock_client_cls,
        ):
            mock_tool.return_value = ToolResult(
                tool="test", success=True, stdout="mock monitoring data output"
            )

            mock_message = AsyncMock()
            mock_message.content = [AsyncMock(text=json.dumps(VALID_RESPONSE))]
            mock_message.usage = AsyncMock(input_tokens=800, output_tokens=400)

            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(return_value=mock_message)
            mock_client_cls.return_value = mock_client

            result = await agent.run({"flow": "daily-monitor"}, run_id="test-run-001")

        assert result.success is True
        assert result.data["agent"] == "portfolio_monitor"
        assert result.data["portfolio_summary"]["total_positions"] == 11
        assert result.data["portfolio_summary"]["net_pnl_pct"] == 3.5
        assert len(result.data["positions"]) == 2
        assert result.tokens_used == 1200
        assert result.run_id == "test-run-001"
        assert result.agent_id == "a32"
        assert result.duration_seconds > 0

    @pytest.mark.asyncio
    async def test_run_handles_invalid_json(self):
        agent = PortfolioMonitorAgent()

        with (
            patch("agents.a32_portfolio_monitor.run_investment_tool") as mock_tool,
            patch("agents.a32_portfolio_monitor.AsyncAnthropic") as mock_client_cls,
        ):
            mock_tool.return_value = ToolResult(
                tool="test", success=True, stdout="mock data"
            )

            mock_message = AsyncMock()
            mock_message.content = [AsyncMock(text="not valid json {{{")]
            mock_message.usage = AsyncMock(input_tokens=500, output_tokens=200)

            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(return_value=mock_message)
            mock_client_cls.return_value = mock_client

            result = await agent.run({"flow": "daily-monitor"}, run_id="test-bad")

        assert result.success is False
        assert "Invalid JSON" in result.error

    @pytest.mark.asyncio
    async def test_run_handles_api_error(self):
        agent = PortfolioMonitorAgent()

        with (
            patch("agents.a32_portfolio_monitor.run_investment_tool") as mock_tool,
            patch("agents.a32_portfolio_monitor.AsyncAnthropic") as mock_client_cls,
        ):
            mock_tool.return_value = ToolResult(
                tool="test", success=True, stdout="mock data"
            )

            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(
                side_effect=RuntimeError("API connection failed")
            )
            mock_client_cls.return_value = mock_client

            result = await agent.run({"flow": "daily-monitor"}, run_id="test-err")

        assert result.success is False
        assert "API connection failed" in result.error

    @pytest.mark.asyncio
    async def test_tool_invocation_count(self):
        """Verify that all 4 tools are invoked."""
        agent = PortfolioMonitorAgent()

        with (
            patch("agents.a32_portfolio_monitor.run_investment_tool") as mock_tool,
            patch("agents.a32_portfolio_monitor.AsyncAnthropic") as mock_client_cls,
        ):
            mock_tool.return_value = ToolResult(
                tool="test", success=True, stdout="data"
            )

            mock_message = AsyncMock()
            mock_message.content = [AsyncMock(text=json.dumps(VALID_RESPONSE))]
            mock_message.usage = AsyncMock(input_tokens=100, output_tokens=100)

            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(return_value=mock_message)
            mock_client_cls.return_value = mock_client

            await agent.run({"flow": "daily-monitor"}, run_id="test-cnt")

        assert mock_tool.call_count == 4
