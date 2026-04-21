"""Tests for the Decision Maker agent (A3.1)."""
from __future__ import annotations

import json
import pathlib
from unittest.mock import AsyncMock, patch

import pytest

from agents._tool_runner import ToolResult
from agents.a31_decision_maker import DecisionMakerAgent, PROMPT_PATH
from orchestrator.base import AgentLayer, AgentModel

VALID_RESPONSE = {
    "ticker": "MORN",
    "agent": "decision_maker",
    "decision": "BUY",
    "conviction": 7,
    "target_price": 195.0,
    "stop_loss": 140.0,
    "position_size_pct": 5.0,
    "thesis_summary": "Morningstar is a quality compounder with strong moat and attractive valuation.",
    "key_risks": ["Competitive pressure", "Slowing growth"],
    "catalyst_expected": "Q2 earnings",
    "review_trigger": "If ROIC drops below 20%",
    "gates_passed": {
        "conviction": True,
        "return": True,
        "risk": True,
        "consistency": True,
    },
    "reasoning": "Financial analyst grades A with QS 82. Business analyst confirms wide moat. Risk score 4/10. Consistency check shows alignment with past decisions.",
}

SAMPLE_INPUTS = {
    "ticker": "MORN",
    "financial_analyst": {
        "ticker": "MORN",
        "investment_grade": "A",
        "quality_score": {"raw": 82, "tier": "A"},
        "valuation": {"weighted_fv": 195.0, "mos_pct": 18.5, "e_cagr_pct": 14.2},
    },
    "business_analyst": {
        "ticker": "MORN",
        "moat_rating": "WIDE",
        "management_grade": "A",
    },
    "risk_analyst": {
        "ticker": "MORN",
        "risk_score": 4,
        "key_risks": ["Competitive pressure"],
    },
    "web_researcher": {
        "ticker": "MORN",
        "sentiment": "POSITIVE",
        "recent_catalysts": ["Strong Q1 earnings"],
    },
}


class TestInit:
    def test_agent_id(self):
        agent = DecisionMakerAgent()
        assert agent.agent_id == "a31"

    def test_agent_name(self):
        agent = DecisionMakerAgent()
        assert agent.name == "Decision Maker"

    def test_agent_model(self):
        agent = DecisionMakerAgent()
        assert agent.model == AgentModel.SONNET

    def test_agent_layer(self):
        agent = DecisionMakerAgent()
        assert agent.layer == AgentLayer.PORTFOLIO


class TestPrompt:
    def test_prompt_file_exists(self):
        assert PROMPT_PATH.exists(), f"Prompt file not found: {PROMPT_PATH}"

    def test_prompt_is_nonempty(self):
        content = PROMPT_PATH.read_text()
        assert len(content) > 100

    def test_prompt_mentions_gates(self):
        content = PROMPT_PATH.read_text()
        assert "Gate 1" in content
        assert "Gate 2" in content
        assert "Gate 3" in content
        assert "Gate 4" in content


class TestRun:
    @pytest.mark.asyncio
    async def test_run_with_mocked_tools_and_api(self):
        agent = DecisionMakerAgent()

        with (
            patch("agents.a31_decision_maker.run_investment_tool") as mock_tool,
            patch("agents.a31_decision_maker.AsyncAnthropic") as mock_client_cls,
        ):
            mock_tool.return_value = ToolResult(
                tool="test", success=True, stdout="mock consistency check output"
            )

            mock_message = AsyncMock()
            mock_message.content = [AsyncMock(text=json.dumps(VALID_RESPONSE))]
            mock_message.usage = AsyncMock(input_tokens=2000, output_tokens=800)

            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(return_value=mock_message)
            mock_client_cls.return_value = mock_client

            result = await agent.run(SAMPLE_INPUTS, run_id="test-run-001")

        assert result.success is True
        assert result.data["agent"] == "decision_maker"
        assert result.data["decision"] == "BUY"
        assert result.data["conviction"] == 7
        assert result.data["gates_passed"]["conviction"] is True
        assert result.data["gates_passed"]["return"] is True
        assert result.data["gates_passed"]["risk"] is True
        assert result.data["gates_passed"]["consistency"] is True
        assert result.tokens_used == 2800
        assert result.run_id == "test-run-001"
        assert result.agent_id == "a31"
        assert result.duration_seconds > 0

    @pytest.mark.asyncio
    async def test_run_handles_invalid_json(self):
        agent = DecisionMakerAgent()

        with (
            patch("agents.a31_decision_maker.run_investment_tool") as mock_tool,
            patch("agents.a31_decision_maker.AsyncAnthropic") as mock_client_cls,
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

            result = await agent.run(SAMPLE_INPUTS, run_id="test-bad")

        assert result.success is False
        assert "Invalid JSON" in result.error

    @pytest.mark.asyncio
    async def test_run_handles_api_error(self):
        agent = DecisionMakerAgent()

        with (
            patch("agents.a31_decision_maker.run_investment_tool") as mock_tool,
            patch("agents.a31_decision_maker.AsyncAnthropic") as mock_client_cls,
        ):
            mock_tool.return_value = ToolResult(
                tool="test", success=True, stdout="mock data"
            )

            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(
                side_effect=RuntimeError("API connection failed")
            )
            mock_client_cls.return_value = mock_client

            result = await agent.run(SAMPLE_INPUTS, run_id="test-err")

        assert result.success is False
        assert "API connection failed" in result.error

    @pytest.mark.asyncio
    async def test_tool_invocation_count(self):
        """Verify that both tools are invoked (consistency_checker + portfolio_optimizer)."""
        agent = DecisionMakerAgent()

        with (
            patch("agents.a31_decision_maker.run_investment_tool") as mock_tool,
            patch("agents.a31_decision_maker.AsyncAnthropic") as mock_client_cls,
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

            await agent.run(SAMPLE_INPUTS, run_id="test-cnt")

        assert mock_tool.call_count == 2

    @pytest.mark.asyncio
    async def test_agent_inputs_formatted(self):
        """Verify that all agent inputs are included in the Claude message."""
        agent = DecisionMakerAgent()

        with (
            patch("agents.a31_decision_maker.run_investment_tool") as mock_tool,
            patch("agents.a31_decision_maker.AsyncAnthropic") as mock_client_cls,
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

            await agent.run(SAMPLE_INPUTS, run_id="test-fmt")

        call_args = mock_client.messages.create.call_args
        user_content = call_args.kwargs["messages"][0]["content"]
        assert "Financial Analyst (A2.1)" in user_content
        assert "Business Analyst (A2.3)" in user_content
        assert "Risk Analyst (A2.4)" in user_content
        assert "Web Researcher (A2.5)" in user_content
