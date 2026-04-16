"""Tests for the Web Researcher agent (A2.5)."""
from __future__ import annotations

import json
import pathlib
from unittest.mock import AsyncMock, patch

import pytest

from agents.a25_web_researcher import WebResearcherAgent, PROMPT_PATH, KB_UNIVERSE
from orchestrator.base import AgentLayer, AgentModel

VALID_RESPONSE = {
    "ticker": "TEST",
    "agent": "web_researcher",
    "recent_news": [
        {
            "date": "2026-04-10",
            "headline": "Company beats Q1 estimates",
            "source": "Reuters",
            "sentiment": "positive",
        }
    ],
    "earnings_highlights": "Q1 revenue +12% YoY, guidance raised.",
    "value_manager_coverage": {
        "horos": "Not covered",
        "alpha_vulture": "Not covered",
        "other_13f": "No data",
    },
    "regulatory_flags": [],
    "litigation_flags": [],
    "summary": "Clean external profile with positive earnings momentum.",
}


class TestInit:
    def test_agent_id(self):
        agent = WebResearcherAgent()
        assert agent.agent_id == "a25"

    def test_agent_name(self):
        agent = WebResearcherAgent()
        assert agent.name == "Web Researcher"

    def test_agent_model(self):
        agent = WebResearcherAgent()
        assert agent.model == AgentModel.HAIKU

    def test_agent_layer(self):
        agent = WebResearcherAgent()
        assert agent.layer == AgentLayer.ANALYSIS


class TestPrompt:
    def test_prompt_file_exists(self):
        assert PROMPT_PATH.exists(), f"Prompt file not found: {PROMPT_PATH}"

    def test_prompt_is_nonempty(self):
        content = PROMPT_PATH.read_text()
        assert len(content) > 100


class TestLocalKB:
    def test_search_for_ticker_in_list(self):
        data = [
            {"ticker": "AAPL", "weight": 5.0},
            {"ticker": "TEST", "weight": 3.0},
        ]
        result = WebResearcherAgent._search_for_ticker(data, "TEST")
        assert result is not None
        assert len(result) == 1
        assert result[0]["ticker"] == "TEST"

    def test_search_for_ticker_in_dict(self):
        data = {"TEST": {"weight": 3.0}, "AAPL": {"weight": 5.0}}
        result = WebResearcherAgent._search_for_ticker(data, "TEST")
        assert result is not None
        assert result["weight"] == 3.0

    def test_search_for_missing_ticker(self):
        data = [{"ticker": "AAPL", "weight": 5.0}]
        result = WebResearcherAgent._search_for_ticker(data, "MISSING")
        assert result is None

    def test_search_case_insensitive(self):
        data = [{"ticker": "TEST", "weight": 3.0}]
        result = WebResearcherAgent._search_for_ticker(data, "test")
        assert result is not None

    def test_load_local_kb_missing_files(self):
        agent = WebResearcherAgent()
        # KB files don't exist in test environment
        kb_data = agent._load_local_kb("TEST")
        assert "NOT FOUND" in kb_data or "not found" in kb_data.lower()


class TestRun:
    @pytest.mark.asyncio
    async def test_run_with_mocked_api(self):
        agent = WebResearcherAgent()

        with patch("agents.a25_web_researcher.AsyncAnthropic") as mock_client_cls:
            # Simulate web search response with multiple content blocks
            # The web search tool response has tool_use blocks and a final text block
            mock_text_block = AsyncMock()
            mock_text_block.text = json.dumps(VALID_RESPONSE)

            mock_search_block = AsyncMock(spec=[])  # No 'text' attribute
            del mock_search_block.text  # Ensure hasattr(b, 'text') is False

            mock_message = AsyncMock()
            mock_message.content = [mock_search_block, mock_text_block]
            mock_message.usage = AsyncMock(input_tokens=1200, output_tokens=800)

            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(return_value=mock_message)
            mock_client_cls.return_value = mock_client

            result = await agent.run({"ticker": "TEST"}, run_id="test-run-004")

        assert result.success is True
        assert result.data["ticker"] == "TEST"
        assert result.data["agent"] == "web_researcher"
        assert len(result.data["recent_news"]) == 1
        assert result.tokens_used == 2000
        assert result.run_id == "test-run-004"

    @pytest.mark.asyncio
    async def test_run_verifies_web_search_tool_config(self):
        """Verify the API is called with web_search tool configuration."""
        agent = WebResearcherAgent()

        with patch("agents.a25_web_researcher.AsyncAnthropic") as mock_client_cls:
            mock_text_block = AsyncMock()
            mock_text_block.text = json.dumps(VALID_RESPONSE)

            mock_message = AsyncMock()
            mock_message.content = [mock_text_block]
            mock_message.usage = AsyncMock(input_tokens=100, output_tokens=100)

            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(return_value=mock_message)
            mock_client_cls.return_value = mock_client

            await agent.run({"ticker": "TEST"}, run_id="test-cfg")

            call_kwargs = mock_client.messages.create.call_args[1]
            assert "tools" in call_kwargs
            tools = call_kwargs["tools"]
            assert len(tools) == 1
            assert tools[0]["type"] == "web_search_20250305"
            assert tools[0]["name"] == "web_search"
            assert tools[0]["max_uses"] == 5

    @pytest.mark.asyncio
    async def test_run_handles_invalid_json(self):
        agent = WebResearcherAgent()

        with patch("agents.a25_web_researcher.AsyncAnthropic") as mock_client_cls:
            mock_text_block = AsyncMock()
            mock_text_block.text = "This is not JSON"

            mock_message = AsyncMock()
            mock_message.content = [mock_text_block]
            mock_message.usage = AsyncMock(input_tokens=100, output_tokens=100)

            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(return_value=mock_message)
            mock_client_cls.return_value = mock_client

            result = await agent.run({"ticker": "BAD"}, run_id="test-bad")

        assert result.success is False
        assert "Invalid JSON" in result.error

    @pytest.mark.asyncio
    async def test_run_handles_api_error(self):
        agent = WebResearcherAgent()

        with patch("agents.a25_web_researcher.AsyncAnthropic") as mock_client_cls:
            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(
                side_effect=RuntimeError("Web search quota exceeded")
            )
            mock_client_cls.return_value = mock_client

            result = await agent.run({"ticker": "ERR"}, run_id="test-err")

        assert result.success is False
        assert "quota exceeded" in result.error

    @pytest.mark.asyncio
    async def test_run_handles_no_text_block(self):
        """Test handling when response has no text content block."""
        agent = WebResearcherAgent()

        with patch("agents.a25_web_researcher.AsyncAnthropic") as mock_client_cls:
            # All blocks are non-text (simulating broken response)
            mock_block = AsyncMock(spec=[])  # No 'text' attribute
            del mock_block.text

            mock_message = AsyncMock()
            mock_message.content = [mock_block]
            mock_message.usage = AsyncMock(input_tokens=100, output_tokens=100)

            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(return_value=mock_message)
            mock_client_cls.return_value = mock_client

            result = await agent.run({"ticker": "NOTEXT"}, run_id="test-notext")

        assert result.success is False
        assert "No text content block" in result.error
