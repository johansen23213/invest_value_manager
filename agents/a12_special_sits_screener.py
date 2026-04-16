"""Special Situations Screener agent (A1.2) — screens SEC EDGAR and PR Newswire for special situations."""
from __future__ import annotations

import json
import pathlib
import time
from typing import Any

from anthropic import AsyncAnthropic

from orchestrator.base import AgentLayer, AgentModel, AgentResult, BaseAgent
from scrapers.sec_edgar_rss import EdgarRSSWatcher
from scrapers.pr_newswire import PRNewswireWatcher

PROMPT_PATH = pathlib.Path(__file__).resolve().parent / "prompts" / "a12_special_sits_screener.md"


class SpecialSitsScreenerAgent(BaseAgent):
    """Screens SEC EDGAR and PR Newswire for actionable special situations."""

    def __init__(self) -> None:
        super().__init__(
            agent_id="a12",
            name="Special Situations Screener",
            model=AgentModel.HAIKU,
            layer=AgentLayer.SCREENING,
            description="SEC EDGAR and PR Newswire screening for special situations",
            skills=["screening-protocol"],
            tools=[],
            estimated_tokens=4000,
        )
        self._system_prompt = PROMPT_PATH.read_text()

    # ------------------------------------------------------------------
    def _gather_data(self) -> str:
        """Query scrapers directly and format results as text for Claude."""
        sections: list[str] = []

        # SEC EDGAR
        try:
            edgar = EdgarRSSWatcher()
            edgar_results = edgar.search(days_back=7)
            header = "=== SEC EDGAR Filings ==="
            if edgar_results:
                body = json.dumps(edgar_results, indent=2)
            else:
                body = "No results found."
            sections.append(f"{header}\n{body}")
        except Exception as e:
            sections.append(f"=== SEC EDGAR Filings ===\n[FAILED: {e}]")

        # PR Newswire
        try:
            pr = PRNewswireWatcher()
            pr_results = pr.search(days_back=7)
            header = "=== PR Newswire ==="
            if pr_results:
                body = json.dumps(pr_results, indent=2)
            else:
                body = "No results found (API stub — not yet active)."
            sections.append(f"{header}\n{body}")
        except Exception as e:
            sections.append(f"=== PR Newswire ===\n[FAILED: {e}]")

        return "\n\n".join(sections)

    # ------------------------------------------------------------------
    async def run(self, inputs: dict[str, Any], run_id: str = "") -> AgentResult:
        start = time.time()

        scraper_data = self._gather_data()

        client = AsyncAnthropic()
        try:
            message = await client.messages.create(
                model=self.model.value,
                max_tokens=4096,
                system=self._system_prompt,
                messages=[{"role": "user", "content": f"Screen for special situations.\n\n{scraper_data}"}],
            )
            response_text = message.content[0].text
            tokens = message.usage.input_tokens + message.usage.output_tokens
            data = json.loads(response_text)
            return AgentResult(
                agent_id=self.agent_id,
                agent_name=self.name,
                success=True,
                data=data,
                tokens_used=tokens,
                duration_seconds=time.time() - start,
                run_id=run_id,
            )
        except json.JSONDecodeError as e:
            return AgentResult(
                agent_id=self.agent_id,
                agent_name=self.name,
                success=False,
                error=f"Invalid JSON from model: {e}",
                duration_seconds=time.time() - start,
                run_id=run_id,
            )
        except Exception as e:
            return AgentResult(
                agent_id=self.agent_id,
                agent_name=self.name,
                success=False,
                error=str(e),
                duration_seconds=time.time() - start,
                run_id=run_id,
            )
