"""Tests for the Financial Analyst agent (A2.1)."""
from __future__ import annotations

import json
import pathlib
from unittest.mock import AsyncMock, patch

import pytest

from agents._tool_runner import ToolResult
from agents.a21_financial_analyst import FinancialAnalystAgent, PROMPT_PATH
from orchestrator.base import AgentLayer, AgentModel

VALID_RESPONSE = {
    "ticker": "TEST",
    "agent": "financial_analyst",
    "quality_score": {
        "raw": 72,
        "tier": "B",
        "key_strengths": ["High ROIC"],
        "key_weaknesses": ["Elevated debt"],
    },
    "valuation": {
        "dcf_bear": 45.0,
        "dcf_base": 62.0,
        "dcf_bull": 85.0,
        "weighted_fv": 63.5,
        "current_price": 55.0,
        "mos_pct": 13.4,
        "e_cagr_pct": 8.2,
    },
    "financial_health": {
        "roic_pct": 18.5,
        "fcf_margin_pct": 12.3,
        "debt_to_equity": 0.8,
        "revenue_growth_3yr_cagr_pct": 6.2,
        "red_flags": [],
    },
    "narrative_trends": ["Margins expanding"],
    "investment_grade": "B",
    "summary": "Solid quality with fair valuation.",
}


class TestInit:
    def test_agent_id(self):
        agent = FinancialAnalystAgent()
        assert agent.agent_id == "a21"

    def test_agent_name(self):
        agent = FinancialAnalystAgent()
        assert agent.name == "Financial Analyst"

    def test_agent_model(self):
        agent = FinancialAnalystAgent()
        assert agent.model == AgentModel.SONNET

    def test_agent_layer(self):
        agent = FinancialAnalystAgent()
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
        agent = FinancialAnalystAgent()

        with (
            patch("agents.a21_financial_analyst.run_investment_tool") as mock_tool,
            patch("agents.a21_financial_analyst.AsyncAnthropic") as mock_client_cls,
        ):
            mock_tool.return_value = ToolResult(
                tool="test", success=True, stdout="mock financial data output"
            )

            mock_message = AsyncMock()
            mock_message.content = [AsyncMock(text=json.dumps(VALID_RESPONSE))]
            mock_message.usage = AsyncMock(input_tokens=1000, output_tokens=500)

            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(return_value=mock_message)
            mock_client_cls.return_value = mock_client

            result = await agent.run({"ticker": "TEST"}, run_id="test-run-001")

        assert result.success is True
        assert result.data["ticker"] == "TEST"
        assert result.data["agent"] == "financial_analyst"
        assert result.data["investment_grade"] == "B"
        assert result.tokens_used == 1500
        assert result.run_id == "test-run-001"
        assert result.agent_id == "a21"
        assert result.duration_seconds > 0

    @pytest.mark.asyncio
    async def test_run_handles_invalid_json(self):
        agent = FinancialAnalystAgent()

        with (
            patch("agents.a21_financial_analyst.run_investment_tool") as mock_tool,
            patch("agents.a21_financial_analyst.AsyncAnthropic") as mock_client_cls,
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

            result = await agent.run({"ticker": "BAD"}, run_id="test-bad")

        assert result.success is False
        assert "Invalid JSON" in result.error

    @pytest.mark.asyncio
    async def test_run_handles_api_error(self):
        agent = FinancialAnalystAgent()

        with (
            patch("agents.a21_financial_analyst.run_investment_tool") as mock_tool,
            patch("agents.a21_financial_analyst.AsyncAnthropic") as mock_client_cls,
        ):
            mock_tool.return_value = ToolResult(
                tool="test", success=True, stdout="mock data"
            )

            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(
                side_effect=RuntimeError("API connection failed")
            )
            mock_client_cls.return_value = mock_client

            result = await agent.run({"ticker": "ERR"}, run_id="test-err")

        assert result.success is False
        assert "API connection failed" in result.error

    @pytest.mark.asyncio
    async def test_tool_invocation_count(self):
        """Verify that all 4 tools are invoked."""
        agent = FinancialAnalystAgent()

        with (
            patch("agents.a21_financial_analyst.run_investment_tool") as mock_tool,
            patch("agents.a21_financial_analyst.AsyncAnthropic") as mock_client_cls,
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

        assert mock_tool.call_count == 4
