"""Tests for the Business Analyst agent (A2.3)."""
from __future__ import annotations

import json
from unittest.mock import AsyncMock, patch

import pytest

from agents._tool_runner import ToolResult
from agents.a23_business_analyst import BusinessAnalystAgent, PROMPT_PATH
from orchestrator.base import AgentLayer, AgentModel

VALID_RESPONSE = {
    "ticker": "TEST",
    "agent": "business_analyst",
    "moat": {
        "type": "Narrow",
        "sources": ["Switching costs", "Brand"],
        "durability": "Moderate",
    },
    "management": {
        "skin_in_the_game_pct": 3.5,
        "capital_allocation": "Good",
        "key_observations": ["CEO bought shares in Q1"],
    },
    "competitive_position": {
        "market_share": "Top 3",
        "competitors": ["COMP1", "COMP2"],
        "advantages": ["Strong brand recognition"],
    },
    "bull_case": "Market share gains from competitor weakness.",
    "bear_case": "Margin compression from new entrants.",
    "catalysts": [
        {
            "description": "New product launch",
            "expected_date": "2026-Q3",
            "impact": "Medium",
        }
    ],
    "business_quality_grade": "B",
    "summary": "Solid business with narrow moat and aligned management.",
}


class TestInit:
    def test_agent_id(self):
        agent = BusinessAnalystAgent()
        assert agent.agent_id == "a23"

    def test_agent_name(self):
        agent = BusinessAnalystAgent()
        assert agent.name == "Business Analyst"

    def test_agent_model(self):
        agent = BusinessAnalystAgent()
        assert agent.model == AgentModel.SONNET

    def test_agent_layer(self):
        agent = BusinessAnalystAgent()
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
        agent = BusinessAnalystAgent()

        with (
            patch("agents.a23_business_analyst.run_investment_tool") as mock_tool,
            patch("agents.a23_business_analyst.AsyncAnthropic") as mock_client_cls,
        ):
            mock_tool.return_value = ToolResult(
                tool="test", success=True, stdout="mock insider/ownership data"
            )

            mock_message = AsyncMock()
            mock_message.content = [AsyncMock(text=json.dumps(VALID_RESPONSE))]
            mock_message.usage = AsyncMock(input_tokens=800, output_tokens=600)

            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(return_value=mock_message)
            mock_client_cls.return_value = mock_client

            result = await agent.run({"ticker": "TEST"}, run_id="test-run-002")

        assert result.success is True
        assert result.data["ticker"] == "TEST"
        assert result.data["agent"] == "business_analyst"
        assert result.data["moat"]["type"] == "Narrow"
        assert result.data["business_quality_grade"] == "B"
        assert result.tokens_used == 1400
        assert result.run_id == "test-run-002"

    @pytest.mark.asyncio
    async def test_run_handles_invalid_json(self):
        agent = BusinessAnalystAgent()

        with (
            patch("agents.a23_business_analyst.run_investment_tool") as mock_tool,
            patch("agents.a23_business_analyst.AsyncAnthropic") as mock_client_cls,
        ):
            mock_tool.return_value = ToolResult(
                tool="test", success=True, stdout="data"
            )

            mock_message = AsyncMock()
            mock_message.content = [AsyncMock(text="broken json")]
            mock_message.usage = AsyncMock(input_tokens=100, output_tokens=50)

            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(return_value=mock_message)
            mock_client_cls.return_value = mock_client

            result = await agent.run({"ticker": "BAD"}, run_id="test-bad")

        assert result.success is False
        assert "Invalid JSON" in result.error

    @pytest.mark.asyncio
    async def test_run_handles_api_error(self):
        agent = BusinessAnalystAgent()

        with (
            patch("agents.a23_business_analyst.run_investment_tool") as mock_tool,
            patch("agents.a23_business_analyst.AsyncAnthropic") as mock_client_cls,
        ):
            mock_tool.return_value = ToolResult(
                tool="test", success=True, stdout="data"
            )

            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(
                side_effect=ConnectionError("Network error")
            )
            mock_client_cls.return_value = mock_client

            result = await agent.run({"ticker": "ERR"}, run_id="test-err")

        assert result.success is False
        assert "Network error" in result.error

    @pytest.mark.asyncio
    async def test_tool_invocation_count(self):
        """Verify that all 3 tools are invoked."""
        agent = BusinessAnalystAgent()

        with (
            patch("agents.a23_business_analyst.run_investment_tool") as mock_tool,
            patch("agents.a23_business_analyst.AsyncAnthropic") as mock_client_cls,
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
