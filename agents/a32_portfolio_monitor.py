"""Portfolio Monitor agent (A3.2) — daily P&L, thesis drift, and event tracking."""
from __future__ import annotations

import json
import pathlib
import time
from typing import Any

from anthropic import AsyncAnthropic

from agents._tool_runner import run_investment_tool
from orchestrator.base import AgentLayer, AgentModel, AgentResult, BaseAgent

PROMPT_PATH = pathlib.Path(__file__).resolve().parent / "prompts" / "a32_portfolio_monitor.md"

# Tools this agent invokes — no ticker substitution needed (portfolio-wide).
_TOOLS_CONFIG = [
    ("portfolio_stats.py", []),
    ("thesis_monitor.py", ["--alerts"]),
    ("earnings_intel.py", ["--days", "7"]),
    ("session_opener.py", ["--quick"]),
]


class PortfolioMonitorAgent(BaseAgent):
    """Runs four monitoring tools, sends their output to Claude, and returns a daily digest."""

    def __init__(self) -> None:
        super().__init__(
            agent_id="a32",
            name="Portfolio Monitor",
            model=AgentModel.HAIKU,
            layer=AgentLayer.PORTFOLIO,
            description="Daily P&L snapshot, thesis drift detection, event timeline, review flagging",
            skills=[],
            tools=["portfolio_stats.py", "thesis_monitor.py", "earnings_intel.py", "session_opener.py"],
            estimated_tokens=3000,
        )
        self._system_prompt = PROMPT_PATH.read_text()

    # ------------------------------------------------------------------
    def _gather_tool_data(self) -> str:
        """Invoke each monitoring tool via subprocess and concatenate their outputs."""
        sections: list[str] = []
        for tool_name, args in _TOOLS_CONFIG:
            result = run_investment_tool(tool_name, args, timeout=45)
            header = f"=== {tool_name} ==="
            body = result.stdout if result.success else f"[FAILED: {result.error or result.stderr}]"
            sections.append(f"{header}\n{body}")
        return "\n\n".join(sections)

    # ------------------------------------------------------------------
    async def run(self, inputs: dict[str, Any], run_id: str = "") -> AgentResult:
        start = time.time()

        tool_data = self._gather_tool_data()

        client = AsyncAnthropic()
        try:
            message = await client.messages.create(
                model=self.model.value,
                max_tokens=4096,
                system=self._system_prompt,
                messages=[{"role": "user", "content": f"Generate daily portfolio monitoring digest.\n\n{tool_data}"}],
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
