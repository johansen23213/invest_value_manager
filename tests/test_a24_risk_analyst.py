"""Tests for the Risk Analyst agent (A2.4)."""
from __future__ import annotations

import json
from unittest.mock import AsyncMock, patch

import pytest

from agents._tool_runner import ToolResult
from agents.a24_risk_analyst import RiskAnalystAgent, PROMPT_PATH
from orchestrator.base import AgentLayer, AgentModel

VALID_RESPONSE = {
    "ticker": "TEST",
    "agent": "risk_analyst",
    "risk_score": 4.5,
    "risk_dimensions": {
        "liquidity": {"score": 3, "notes": "Adequate volume"},
        "concentration": {"score": 5, "notes": "Sector at 25%"},
        "thesis_break": {"score": 4, "notes": "Thesis intact"},
        "execution": {"score": 3, "notes": "Liquid stock"},
        "fx_exposure": {"score": 2, "notes": "No FX mismatch"},
        "max_drawdown_pct": {"score": 6, "notes": "45% drawdown in 2022"},
        "correlation": {"score": 4, "notes": "Moderate correlation"},
    },
    "sizing_cap_pct": 8.0,
    "thesis_break_scenarios": [
        "Revenue growth below 5% for 2Q",
        "Key customer >40% concentration",
    ],
    "overall_assessment": "ELEVATED",
    "summary": "Elevated risk due to sector concentration and historical drawdown.",
}


class TestInit:
    def test_agent_id(self):
        agent = RiskAnalystAgent()
        assert agent.agent_id == "a24"

    def test_agent_name(self):
        agent = RiskAnalystAgent()
        assert agent.name == "Risk Analyst"

    def test_agent_model(self):
        agent = RiskAnalystAgent()
        assert agent.model == AgentModel.HAIKU

    def test_agent_layer(self):
        agent = RiskAnalystAgent()
        assert agent.layer == AgentLayer.ANALYSIS


class TestPrompt:
    def test_prompt_file_exists(self):
        assert PROMPT_PATH.exists(), f"Prompt file not found: {PROMPT_PATH}"

    def test_prompt_is_nonempty(self):
        content = PROMPT_PATH.read_text()
        assert len(content) > 100


class TestRun:
    @pytest.mark.asyncio
    async def test_run_with_mocked_tools_and_api(self):
        agent = RiskAnalystAgent()

        with (
            patch("agents.a24_risk_analyst.run_investment_tool") as mock_tool,
            patch("agents.a24_risk_analyst.AsyncAnthropic") as mock_client_cls,
        ):
            mock_tool.return_value = ToolResult(
                tool="test", success=True, stdout="mock constraint/correlation data"
            )

            mock_message = AsyncMock()
            mock_message.content = [AsyncMock(text=json.dumps(VALID_RESPONSE))]
            mock_message.usage = AsyncMock(input_tokens=600, output_tokens=400)

            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(return_value=mock_message)
            mock_client_cls.return_value = mock_client

            result = await agent.run({"ticker": "TEST"}, run_id="test-run-003")

        assert result.success is True
        assert result.data["ticker"] == "TEST"
        assert result.data["agent"] == "risk_analyst"
        assert result.data["risk_score"] == 4.5
        assert result.data["overall_assessment"] == "ELEVATED"
        assert len(result.data["risk_dimensions"]) == 7
        assert result.tokens_used == 1000
        assert result.run_id == "test-run-003"

    @pytest.mark.asyncio
    async def test_run_handles_invalid_json(self):
        agent = RiskAnalystAgent()

        with (
            patch("agents.a24_risk_analyst.run_investment_tool") as mock_tool,
            patch("agents.a24_risk_analyst.AsyncAnthropic") as mock_client_cls,
        ):
            mock_tool.return_value = ToolResult(
                tool="test", success=True, stdout="data"
            )

            mock_message = AsyncMock()
            mock_message.content = [AsyncMock(text="{{invalid")]
            mock_message.usage = AsyncMock(input_tokens=100, output_tokens=50)

            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(return_value=mock_message)
            mock_client_cls.return_value = mock_client

            result = await agent.run({"ticker": "BAD"}, run_id="test-bad")

        assert result.success is False
        assert "Invalid JSON" in result.error

    @pytest.mark.asyncio
    async def test_run_handles_api_error(self):
        agent = RiskAnalystAgent()

        with (
            patch("agents.a24_risk_analyst.run_investment_tool") as mock_tool,
            patch("agents.a24_risk_analyst.AsyncAnthropic") as mock_client_cls,
        ):
            mock_tool.return_value = ToolResult(
                tool="test", success=True, stdout="data"
            )

            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(
                side_effect=TimeoutError("Request timed out")
            )
            mock_client_cls.return_value = mock_client

            result = await agent.run({"ticker": "ERR"}, run_id="test-err")

        assert result.success is False
        assert "timed out" in result.error

    @pytest.mark.asyncio
    async def test_tool_invocation_count(self):
        """Verify that all 3 tools are invoked."""
        agent = RiskAnalystAgent()

        with (
            patch("agents.a24_risk_analyst.run_investment_tool") as mock_tool,
            patch("agents.a24_risk_analyst.AsyncAnthropic") as mock_client_cls,
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

            await agent.run({"ticker": "CNT"}, run_id="test-cnt")

        assert mock_tool.call_count == 3
