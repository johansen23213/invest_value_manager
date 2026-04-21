"""Tests for the Special Situation Modeler agent (A2.2)."""
from __future__ import annotations

import json
import pathlib
from dataclasses import asdict
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from agents.a22_special_sit_modeler import SpecialSitModelerAgent, PROMPT_PATH, _MODEL_DISPATCH
from models.merger_arb import MergerArbResult
from orchestrator.base import AgentLayer, AgentModel

VALID_RESPONSE = {
    "ticker": "ACME",
    "agent": "special_sit_modeler",
    "situation_type": "MERGER_ARB",
    "model_output": {
        "spread_pct": 5.88,
        "annualized_spread_pct": 14.2,
        "expected_return_pct": 4.8,
    },
    "thesis": "ACME merger arb offers a compelling spread.",
    "risks": ["FTC review", "financing condition"],
    "recommendation": "ATTRACTIVE",
    "summary": "Attractive merger arb with 14.2% annualized spread.",
}

MERGER_PARAMS = {
    "current_price": 42.5,
    "deal_price": 45.0,
    "expected_close_date": "2026-10-15",
    "close_probability_pct": 90.0,
}


class TestInit:
    def test_agent_id(self):
        agent = SpecialSitModelerAgent()
        assert agent.agent_id == "a22"

    def test_agent_name(self):
        agent = SpecialSitModelerAgent()
        assert agent.name == "Special Situation Modeler"

    def test_agent_model(self):
        agent = SpecialSitModelerAgent()
        assert agent.model == AgentModel.SONNET

    def test_agent_layer(self):
        agent = SpecialSitModelerAgent()
        assert agent.layer == AgentLayer.ANALYSIS


class TestPrompt:
    def test_prompt_file_exists(self):
        assert PROMPT_PATH.exists(), f"Prompt file not found: {PROMPT_PATH}"

    def test_prompt_is_nonempty(self):
        content = PROMPT_PATH.read_text()
        assert len(content) > 100


class TestRun:
    @pytest.mark.asyncio
    async def test_run_merger_arb_with_mocked_model_and_api(self):
        agent = SpecialSitModelerAgent()

        mock_model_fn = MagicMock(return_value=MergerArbResult(
            spread_pct=5.88,
            annualized_spread_pct=14.2,
            expected_return_pct=4.8,
            risk_reward_ratio=1.5,
            days_to_close=183,
            downside_pct=-11.76,
        ))

        with (
            patch.dict(_MODEL_DISPATCH, {"MERGER_ARB": mock_model_fn}),
            patch("agents.a22_special_sit_modeler.AsyncAnthropic") as mock_client_cls,
        ):
            mock_message = AsyncMock()
            mock_message.content = [AsyncMock(text=json.dumps(VALID_RESPONSE))]
            mock_message.usage = AsyncMock(input_tokens=800, output_tokens=400)

            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(return_value=mock_message)
            mock_client_cls.return_value = mock_client

            result = await agent.run(
                {
                    "ticker": "ACME",
                    "situation_type": "MERGER_ARB",
                    "model_params": MERGER_PARAMS,
                },
                run_id="test-run-001",
            )

        assert result.success is True
        assert result.data["agent"] == "special_sit_modeler"
        assert result.data["situation_type"] == "MERGER_ARB"
        assert result.data["recommendation"] == "ATTRACTIVE"
        assert result.tokens_used == 1200
        assert result.run_id == "test-run-001"
        assert result.agent_id == "a22"
        assert result.duration_seconds > 0
        mock_model_fn.assert_called_once_with(**MERGER_PARAMS)

    @pytest.mark.asyncio
    async def test_run_handles_invalid_json(self):
        agent = SpecialSitModelerAgent()

        mock_model_fn = MagicMock(return_value=MergerArbResult(
            spread_pct=5.0, annualized_spread_pct=10.0,
            expected_return_pct=4.0, risk_reward_ratio=1.0,
            days_to_close=180, downside_pct=-10.0,
        ))

        with (
            patch.dict(_MODEL_DISPATCH, {"MERGER_ARB": mock_model_fn}),
            patch("agents.a22_special_sit_modeler.AsyncAnthropic") as mock_client_cls,
        ):
            mock_message = AsyncMock()
            mock_message.content = [AsyncMock(text="not valid json {{{")]
            mock_message.usage = AsyncMock(input_tokens=300, output_tokens=100)

            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(return_value=mock_message)
            mock_client_cls.return_value = mock_client

            result = await agent.run(
                {"ticker": "BAD", "situation_type": "MERGER_ARB", "model_params": MERGER_PARAMS},
                run_id="test-bad",
            )

        assert result.success is False
        assert "Invalid JSON" in result.error

    @pytest.mark.asyncio
    async def test_run_handles_api_error(self):
        agent = SpecialSitModelerAgent()

        mock_model_fn = MagicMock(return_value=MergerArbResult(
            spread_pct=5.0, annualized_spread_pct=10.0,
            expected_return_pct=4.0, risk_reward_ratio=1.0,
            days_to_close=180, downside_pct=-10.0,
        ))

        with (
            patch.dict(_MODEL_DISPATCH, {"MERGER_ARB": mock_model_fn}),
            patch("agents.a22_special_sit_modeler.AsyncAnthropic") as mock_client_cls,
        ):
            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(
                side_effect=RuntimeError("API connection failed")
            )
            mock_client_cls.return_value = mock_client

            result = await agent.run(
                {"ticker": "ERR", "situation_type": "MERGER_ARB", "model_params": MERGER_PARAMS},
                run_id="test-err",
            )

        assert result.success is False
        assert "API connection failed" in result.error

    @pytest.mark.asyncio
    async def test_run_handles_unknown_situation_type(self):
        agent = SpecialSitModelerAgent()

        result = await agent.run(
            {"ticker": "UNK", "situation_type": "UNKNOWN_TYPE", "model_params": {}},
            run_id="test-unk",
        )

        assert result.success is False
        assert "Unknown situation_type" in result.error

    @pytest.mark.asyncio
    async def test_run_handles_model_error(self):
        agent = SpecialSitModelerAgent()

        mock_model_fn = MagicMock(side_effect=TypeError("missing required argument"))

        with patch.dict(_MODEL_DISPATCH, {"MERGER_ARB": mock_model_fn}):
            result = await agent.run(
                {"ticker": "ERR", "situation_type": "MERGER_ARB", "model_params": {}},
                run_id="test-model-err",
            )

        assert result.success is False
        assert "Model execution failed" in result.error
