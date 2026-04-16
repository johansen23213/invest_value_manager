"""Tests for the Quantitative Screener agent (A1.1)."""
from __future__ import annotations

import json
import pathlib
from unittest.mock import AsyncMock, patch

import pytest

from agents._tool_runner import ToolResult
from agents.a11_quant_screener import QuantScreenerAgent, PROMPT_PATH
from orchestrator.base import AgentLayer, AgentModel

VALID_RESPONSE = {
    "agent": "quant_screener",
    "run_date": "2026-04-16",
    "screener": "QUANT",
    "candidates": [
        {
            "ticker": "MORN",
            "score": 82,
            "signal_reasons": ["P/E below 15", "ROIC > 20%"],
            "key_metrics": {"pe": 14.2, "roic": 25.0},
        }
    ],
    "total_passed": 1,
    "summary": "One strong candidate identified from quality universe.",
}


class TestInit:
    def test_agent_id(self):
        agent = QuantScreenerAgent()
        assert agent.agent_id == "a11"

    def test_agent_name(self):
        agent = QuantScreenerAgent()
        assert agent.name == "Quantitative Screener"

    def test_agent_model(self):
        agent = QuantScreenerAgent()
        assert agent.model == AgentModel.HAIKU

    def test_agent_layer(self):
        agent = QuantScreenerAgent()
        assert agent.layer == AgentLayer.SCREENING


class TestPrompt:
    def test_prompt_file_exists(self):
        assert PROMPT_PATH.exists(), f"Prompt file not found: {PROMPT_PATH}"

    def test_prompt_is_nonempty(self):
        content = PROMPT_PATH.read_text()
        assert len(content) > 100


class TestRun:
    @pytest.mark.asyncio
    async def test_run_with_mocked_tools_and_api(self):
        agent = QuantScreenerAgent()

        with (
            patch("agents.a11_quant_screener.run_investment_tool") as mock_tool,
            patch("agents.a11_quant_screener.AsyncAnthropic") as mock_client_cls,
        ):
            mock_tool.return_value = ToolResult(
                tool="test", success=True, stdout="mock screening data output"
            )

            mock_message = AsyncMock()
            mock_message.content = [AsyncMock(text=json.dumps(VALID_RESPONSE))]
            mock_message.usage = AsyncMock(input_tokens=800, output_tokens=400)

            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(return_value=mock_message)
            mock_client_cls.return_value = mock_client

            result = await agent.run({"ticker": ""}, run_id="test-run-001")

        assert result.success is True
        assert result.data["agent"] == "quant_screener"
        assert result.data["screener"] == "QUANT"
        assert result.data["total_passed"] == 1
        assert result.tokens_used == 1200
        assert result.run_id == "test-run-001"
        assert result.agent_id == "a11"
        assert result.duration_seconds > 0

    @pytest.mark.asyncio
    async def test_run_handles_invalid_json(self):
        agent = QuantScreenerAgent()

        with (
            patch("agents.a11_quant_screener.run_investment_tool") as mock_tool,
            patch("agents.a11_quant_screener.AsyncAnthropic") as mock_client_cls,
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

            result = await agent.run({"ticker": ""}, run_id="test-bad")

        assert result.success is False
        assert "Invalid JSON" in result.error

    @pytest.mark.asyncio
    async def test_run_handles_api_error(self):
        agent = QuantScreenerAgent()

        with (
            patch("agents.a11_quant_screener.run_investment_tool") as mock_tool,
            patch("agents.a11_quant_screener.AsyncAnthropic") as mock_client_cls,
        ):
            mock_tool.return_value = ToolResult(
                tool="test", success=True, stdout="mock data"
            )

            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(
                side_effect=RuntimeError("API connection failed")
            )
            mock_client_cls.return_value = mock_client

            result = await agent.run({"ticker": ""}, run_id="test-err")

        assert result.success is False
        assert "API connection failed" in result.error

    @pytest.mark.asyncio
    async def test_tool_invocation_count(self):
        """Verify that all 2 tools are invoked."""
        agent = QuantScreenerAgent()

        with (
            patch("agents.a11_quant_screener.run_investment_tool") as mock_tool,
            patch("agents.a11_quant_screener.AsyncAnthropic") as mock_client_cls,
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

            await agent.run({"ticker": ""}, run_id="test-cnt")

        assert mock_tool.call_count == 2
