"""Decision Maker agent (A3.1) — synthesizes Layer 2 outputs and applies investment gates."""
from __future__ import annotations

import json
import pathlib
import time
from typing import Any

from anthropic import AsyncAnthropic

from agents._tool_runner import run_investment_tool
from orchestrator.base import AgentLayer, AgentModel, AgentResult, BaseAgent

PROMPT_PATH = pathlib.Path(__file__).resolve().parent / "prompts" / "a31_decision_maker.md"


class DecisionMakerAgent(BaseAgent):
    """Synthesizes Layer 2 agent outputs, applies 4 investment gates, and emits decision JSON."""

    def __init__(self) -> None:
        super().__init__(
            agent_id="a31",
            name="Decision Maker",
            model=AgentModel.SONNET,
            layer=AgentLayer.PORTFOLIO,
            description="Investment decision with conviction gates, sizing, and risk parameters",
            skills=["investment-committee", "investment-rules"],
            tools=["consistency_checker.py", "portfolio_optimizer.py"],
            estimated_tokens=8000,
        )
        self._system_prompt = PROMPT_PATH.read_text()

    # ------------------------------------------------------------------
    def _gather_tool_data(self, ticker: str) -> str:
        """Run consistency checker and portfolio optimizer."""
        sections: list[str] = []

        # Consistency checker
        result = run_investment_tool("consistency_checker.py", [f"BUY {ticker}"], timeout=30)
        header = "=== consistency_checker.py ==="
        body = result.stdout if result.success else f"[FAILED: {result.error or result.stderr}]"
        sections.append(f"{header}\n{body}")

        # Portfolio optimizer
        result = run_investment_tool("portfolio_optimizer.py", ["--deploy"], timeout=30)
        header = "=== portfolio_optimizer.py ==="
        body = result.stdout if result.success else f"[FAILED: {result.error or result.stderr}]"
        sections.append(f"{header}\n{body}")

        return "\n\n".join(sections)

    # ------------------------------------------------------------------
    def _format_agent_inputs(self, inputs: dict[str, Any]) -> str:
        """Format Layer 2 agent outputs into text for Claude."""
        sections: list[str] = []

        agent_keys = [
            ("financial_analyst", "Financial Analyst (A2.1)"),
            ("business_analyst", "Business Analyst (A2.3)"),
            ("risk_analyst", "Risk Analyst (A2.4)"),
            ("web_researcher", "Web Researcher (A2.5)"),
            ("special_sit_modeler", "Special Situation Modeler (A2.2)"),
        ]

        for key, label in agent_keys:
            data = inputs.get(key)
            if data is not None:
                sections.append(f"=== {label} ===\n{json.dumps(data, indent=2)}")

        return "\n\n".join(sections)

    # ------------------------------------------------------------------
    async def run(self, inputs: dict[str, Any], run_id: str = "") -> AgentResult:
        ticker = inputs.get("ticker", "")
        start = time.time()

        agent_data = self._format_agent_inputs(inputs)
        tool_data = self._gather_tool_data(ticker)

        combined = f"{agent_data}\n\n{tool_data}"

        client = AsyncAnthropic()
        try:
            message = await client.messages.create(
                model=self.model.value,
                max_tokens=4096,
                system=self._system_prompt,
                messages=[
                    {
                        "role": "user",
                        "content": f"Make investment decision for {ticker}.\n\n{combined}",
                    }
                ],
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
