"""Risk Analyst agent (A2.4) — 7-dimension risk scoring and portfolio risk assessment."""
from __future__ import annotations

import json
import pathlib
import time
from typing import Any

from anthropic import AsyncAnthropic

from agents._tool_runner import run_investment_tool
from orchestrator.base import AgentLayer, AgentModel, AgentResult, BaseAgent

PROMPT_PATH = pathlib.Path(__file__).resolve().parent / "prompts" / "a24_risk_analyst.md"

_TOOLS_CONFIG = [
    ("constraint_checker.py", ["REPORT"]),
    ("correlation_matrix.py", ["--from-portfolio"]),
    ("drift_detector.py", []),
]


class RiskAnalystAgent(BaseAgent):
    """Scores risk across 7 dimensions and recommends sizing caps."""

    def __init__(self) -> None:
        super().__init__(
            agent_id="a24",
            name="Risk Analyst",
            model=AgentModel.HAIKU,
            layer=AgentLayer.ANALYSIS,
            description="7-dimension risk scoring, correlation analysis, drift detection",
            skills=["risk-identifier"],
            tools=["constraint_checker.py", "correlation_matrix.py", "drift_detector.py"],
            estimated_tokens=3000,
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
                messages=[{"role": "user", "content": f"Analyze risk for {ticker}.\n\n{tool_data}"}],
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
