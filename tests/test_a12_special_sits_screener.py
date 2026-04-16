"""Tests for the Special Situations Screener agent (A1.2)."""
from __future__ import annotations

import json
import pathlib
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from agents.a12_special_sits_screener import SpecialSitsScreenerAgent, PROMPT_PATH
from orchestrator.base import AgentLayer, AgentModel

VALID_RESPONSE = {
    "agent": "special_sits_screener",
    "run_date": "2026-04-16",
    "screener": "SPECIAL_SITS",
    "situations": [
        {
            "ticker": "ACME",
            "type": "MERGER_ARB",
            "headline": "ACME Corp to be acquired by BigCo at $45/share",
            "filed_date": "2026-04-10",
            "source": "SEC_EDGAR",
            "initial_attractiveness": "HIGH",
        }
    ],
    "total_found": 1,
    "summary": "One merger arb situation found via SEC EDGAR.",
}


class TestInit:
    def test_agent_id(self):
        agent = SpecialSitsScreenerAgent()
        assert agent.agent_id == "a12"

    def test_agent_name(self):
        agent = SpecialSitsScreenerAgent()
        assert agent.name == "Special Situations Screener"

    def test_agent_model(self):
        agent = SpecialSitsScreenerAgent()
        assert agent.model == AgentModel.HAIKU

    def test_agent_layer(self):
        agent = SpecialSitsScreenerAgent()
        assert agent.layer == AgentLayer.SCREENING


class TestPrompt:
    def test_prompt_file_exists(self):
        assert PROMPT_PATH.exists(), f"Prompt file not found: {PROMPT_PATH}"

    def test_prompt_is_nonempty(self):
        content = PROMPT_PATH.read_text()
        assert len(content) > 100


class TestRun:
    @pytest.mark.asyncio
    async def test_run_with_mocked_scrapers_and_api(self):
        agent = SpecialSitsScreenerAgent()

        mock_edgar_results = [
            {
                "filing_type": "8-K",
                "company": "ACME Corp",
                "cik": "0001234567",
                "filed_date": "2026-04-10",
                "title": "ACME Corp",
                "url": "https://www.sec.gov/Archives/edgar/data/1234567/000",
                "situation_type": "MERGER_ARB",
            }
        ]

        with (
            patch("agents.a12_special_sits_screener.EdgarRSSWatcher") as mock_edgar_cls,
            patch("agents.a12_special_sits_screener.PRNewswireWatcher") as mock_pr_cls,
            patch("agents.a12_special_sits_screener.AsyncAnthropic") as mock_client_cls,
        ):
            mock_edgar = MagicMock()
            mock_edgar.search.return_value = mock_edgar_results
            mock_edgar_cls.return_value = mock_edgar

            mock_pr = MagicMock()
            mock_pr.search.return_value = []
            mock_pr_cls.return_value = mock_pr

            mock_message = AsyncMock()
            mock_message.content = [AsyncMock(text=json.dumps(VALID_RESPONSE))]
            mock_message.usage = AsyncMock(input_tokens=600, output_tokens=300)

            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(return_value=mock_message)
            mock_client_cls.return_value = mock_client

            result = await agent.run({}, run_id="test-run-001")

        assert result.success is True
        assert result.data["agent"] == "special_sits_screener"
        assert result.data["screener"] == "SPECIAL_SITS"
        assert result.data["total_found"] == 1
        assert result.tokens_used == 900
        assert result.run_id == "test-run-001"
        assert result.agent_id == "a12"
        assert result.duration_seconds > 0

    @pytest.mark.asyncio
    async def test_run_handles_invalid_json(self):
        agent = SpecialSitsScreenerAgent()

        with (
            patch("agents.a12_special_sits_screener.EdgarRSSWatcher") as mock_edgar_cls,
            patch("agents.a12_special_sits_screener.PRNewswireWatcher") as mock_pr_cls,
            patch("agents.a12_special_sits_screener.AsyncAnthropic") as mock_client_cls,
        ):
            mock_edgar = MagicMock()
            mock_edgar.search.return_value = []
            mock_edgar_cls.return_value = mock_edgar

            mock_pr = MagicMock()
            mock_pr.search.return_value = []
            mock_pr_cls.return_value = mock_pr

            mock_message = AsyncMock()
            mock_message.content = [AsyncMock(text="not valid json {{{")]
            mock_message.usage = AsyncMock(input_tokens=300, output_tokens=100)

            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(return_value=mock_message)
            mock_client_cls.return_value = mock_client

            result = await agent.run({}, run_id="test-bad")

        assert result.success is False
        assert "Invalid JSON" in result.error

    @pytest.mark.asyncio
    async def test_run_handles_api_error(self):
        agent = SpecialSitsScreenerAgent()

        with (
            patch("agents.a12_special_sits_screener.EdgarRSSWatcher") as mock_edgar_cls,
            patch("agents.a12_special_sits_screener.PRNewswireWatcher") as mock_pr_cls,
            patch("agents.a12_special_sits_screener.AsyncAnthropic") as mock_client_cls,
        ):
            mock_edgar = MagicMock()
            mock_edgar.search.return_value = []
            mock_edgar_cls.return_value = mock_edgar

            mock_pr = MagicMock()
            mock_pr.search.return_value = []
            mock_pr_cls.return_value = mock_pr

            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(
                side_effect=RuntimeError("API connection failed")
            )
            mock_client_cls.return_value = mock_client

            result = await agent.run({}, run_id="test-err")

        assert result.success is False
        assert "API connection failed" in result.error

    @pytest.mark.asyncio
    async def test_scraper_called(self):
        """Verify that both scrapers are instantiated and called."""
        agent = SpecialSitsScreenerAgent()

        with (
            patch("agents.a12_special_sits_screener.EdgarRSSWatcher") as mock_edgar_cls,
            patch("agents.a12_special_sits_screener.PRNewswireWatcher") as mock_pr_cls,
            patch("agents.a12_special_sits_screener.AsyncAnthropic") as mock_client_cls,
        ):
            mock_edgar = MagicMock()
            mock_edgar.search.return_value = []
            mock_edgar_cls.return_value = mock_edgar

            mock_pr = MagicMock()
            mock_pr.search.return_value = []
            mock_pr_cls.return_value = mock_pr

            mock_message = AsyncMock()
            mock_message.content = [AsyncMock(text=json.dumps(VALID_RESPONSE))]
            mock_message.usage = AsyncMock(input_tokens=100, output_tokens=100)

            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(return_value=mock_message)
            mock_client_cls.return_value = mock_client

            await agent.run({}, run_id="test-scrapers")

        mock_edgar_cls.assert_called_once()
        mock_edgar.search.assert_called_once_with(days_back=7)
        mock_pr_cls.assert_called_once()
        mock_pr.search.assert_called_once_with(days_back=7)
