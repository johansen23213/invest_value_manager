"""Web Researcher agent (A2.5) — web search + local knowledge base lookup."""
from __future__ import annotations

import json
import pathlib
import time
from typing import Any

from anthropic import AsyncAnthropic

from orchestrator.base import AgentLayer, AgentModel, AgentResult, BaseAgent

PROMPT_PATH = pathlib.Path(__file__).resolve().parent / "prompts" / "a25_web_researcher.md"
ROOT = pathlib.Path(__file__).resolve().parent.parent
KB_UNIVERSE = ROOT / "knowledge_base" / "universe"


class WebResearcherAgent(BaseAgent):
    """Gathers recent public information via web search and local knowledge base."""

    def __init__(self) -> None:
        super().__init__(
            agent_id="a25",
            name="Web Researcher",
            model=AgentModel.HAIKU,
            layer=AgentLayer.ANALYSIS,
            description="Web search for news, earnings, regulatory, litigation; local KB lookup",
            skills=[],
            tools=["web_search"],
            estimated_tokens=4000,
        )
        self._system_prompt = PROMPT_PATH.read_text()

    # ------------------------------------------------------------------
    def _load_local_kb(self, ticker: str) -> str:
        """Load local knowledge base files and check for ticker coverage."""
        sections: list[str] = []

        for filename in ("horos_positions.json", "alpha_vulture_ideas.json"):
            path = KB_UNIVERSE / filename
            header = f"=== {filename} ==="
            if not path.exists():
                sections.append(f"{header}\n[FILE NOT FOUND: {path}]")
                continue
            try:
                data = json.loads(path.read_text())
                # Search for ticker in the data (could be list or dict)
                coverage = self._search_for_ticker(data, ticker)
                if coverage:
                    sections.append(f"{header}\n{json.dumps(coverage, indent=2)}")
                else:
                    sections.append(f"{header}\n[Ticker {ticker} not found in {filename}]")
            except (json.JSONDecodeError, Exception) as e:
                sections.append(f"{header}\n[ERROR reading {filename}: {e}]")

        return "\n\n".join(sections)

    @staticmethod
    def _search_for_ticker(data: Any, ticker: str) -> Any:
        """Search for a ticker in JSON data (handles lists and dicts)."""
        ticker_upper = ticker.upper()
        if isinstance(data, list):
            matches = [
                item for item in data
                if isinstance(item, dict)
                and (
                    item.get("ticker", "").upper() == ticker_upper
                    or item.get("symbol", "").upper() == ticker_upper
                )
            ]
            return matches if matches else None
        if isinstance(data, dict):
            if ticker_upper in data:
                return data[ticker_upper]
            # Search in nested structures
            for key, value in data.items():
                if key.upper() == ticker_upper:
                    return value
                if isinstance(value, dict) and value.get("ticker", "").upper() == ticker_upper:
                    return value
        return None

    # ------------------------------------------------------------------
    async def run(self, inputs: dict[str, Any], run_id: str = "") -> AgentResult:
        ticker = inputs.get("ticker", "")
        start = time.time()

        # Gather local KB data
        kb_data = self._load_local_kb(ticker)

        client = AsyncAnthropic()
        try:
            message = await client.messages.create(
                model=self.model.value,
                max_tokens=4096,
                system=self._system_prompt,
                tools=[
                    {
                        "type": "web_search_20250305",
                        "name": "web_search",
                        "max_uses": 5,
                    }
                ],
                messages=[
                    {
                        "role": "user",
                        "content": (
                            f"Research {ticker}. Find recent news, earnings, regulatory and "
                            f"litigation information.\n\n"
                            f"=== Local Knowledge Base ===\n{kb_data}"
                        ),
                    }
                ],
            )

            # Web search responses have multiple content blocks.
            # Find the final text block containing the JSON.
            response_text = next(
                b.text for b in message.content if hasattr(b, "text")
            )
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
        except StopIteration:
            return AgentResult(
                agent_id=self.agent_id,
                agent_name=self.name,
                success=False,
                error="No text content block found in web search response",
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
