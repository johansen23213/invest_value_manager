"""Financial Analyst agent (A2.1) — quality scoring, DCF valuation, and trend synthesis."""
from __future__ import annotations

import json
import pathlib
import time
from typing import Any

from anthropic import AsyncAnthropic

from agents._tool_runner import run_investment_tool
from orchestrator.base import AgentLayer, AgentModel, AgentResult, BaseAgent

PROMPT_PATH = pathlib.Path(__file__).resolve().parent / "prompts" / "a21_financial_analyst.md"

# Tools this agent invokes and the arguments to pass (ticker is substituted at runtime).
_TOOLS_CONFIG = [
    ("quality_scorer.py", ["__TICKER__", "--detailed"]),
    ("dcf_calculator.py", ["__TICKER__", "--scenarios"]),
    ("narrative_checker.py", ["__TICKER__"]),
    ("forward_return.py", ["--active-only"]),
]


class FinancialAnalystAgent(BaseAgent):
    """Runs four quantitative tools, sends their output to Claude, and returns structured JSON."""

    def __init__(self) -> None:
        super().__init__(
            agent_id="a21",
            name="Financial Analyst",
            model=AgentModel.SONNET,
            layer=AgentLayer.ANALYSIS,
            description="Quality scoring, DCF valuation, financial trend analysis",
            skills=["fundamental-analyst", "valuation-specialist"],
            tools=["quality_scorer.py", "dcf_calculator.py", "narrative_checker.py", "forward_return.py"],
            estimated_tokens=6000,
        )
        self._system_prompt = PROMPT_PATH.read_text()

    # ------------------------------------------------------------------
    def _gather_tool_data(self, ticker: str) -> str:
        """Invoke each tool via subprocess and concatenate their outputs."""
        sections: list[str] = []
        for tool_name, arg_template in _TOOLS_CONFIG:
            args = [ticker if a == "__TICKER__" else a for a in arg_template]
            result = run_investment_tool(tool_name, args, timeout=45)
            header = f"=== {tool_name} ==="
            body = result.stdout if result.success else f"[FAILED: {result.error or result.stderr}]"
            sections.append(f"{header}\n{body}")
        return "\n\n".join(sections)

    # ------------------------------------------------------------------
    async def run(self, inputs: dict[str, Any], run_id: str = "") -> AgentResult:
        ticker = inputs.get("ticker", "")
        start = time.time()

        tool_data = self._gather_tool_data(ticker)

        client = AsyncAnthropic()
        try:
            message = await client.messages.create(
                model=self.model.value,
                max_tokens=4096,
                system=self._system_prompt,
                messages=[{"role": "user", "content": f"Analyze {ticker}.\n\n{tool_data}"}],
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
