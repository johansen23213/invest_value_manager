"""Special Situation Modeler agent (A2.2) — runs situation-specific models and generates thesis."""
from __future__ import annotations

import json
import pathlib
import time
from dataclasses import asdict
from typing import Any

from anthropic import AsyncAnthropic

from models.merger_arb import calculate_merger_arb
from models.liquidation import calculate_liquidation_value
from models.spinoff import calculate_stub_value
from models.biotech_cash import calculate_cash_runway
from orchestrator.base import AgentLayer, AgentModel, AgentResult, BaseAgent

PROMPT_PATH = pathlib.Path(__file__).resolve().parent / "prompts" / "a22_special_sit_modeler.md"

_MODEL_DISPATCH = {
    "MERGER_ARB": calculate_merger_arb,
    "LIQUIDATION": calculate_liquidation_value,
    "SPINOFF": calculate_stub_value,
    "NET_CASH": calculate_cash_runway,
}


class SpecialSitModelerAgent(BaseAgent):
    """Runs situation-specific quantitative models and generates investment thesis via Claude."""

    def __init__(self) -> None:
        super().__init__(
            agent_id="a22",
            name="Special Situation Modeler",
            model=AgentModel.SONNET,
            layer=AgentLayer.ANALYSIS,
            description="Special situation modeling: merger arb, liquidation, spinoff, net cash",
            skills=["valuation-methods"],
            tools=[],
            estimated_tokens=5000,
        )
        self._system_prompt = PROMPT_PATH.read_text()

    # ------------------------------------------------------------------
    def _run_model(self, situation_type: str, params: dict[str, Any]) -> dict[str, Any]:
        """Run the appropriate model and return its output as a dict."""
        model_fn = _MODEL_DISPATCH.get(situation_type)
        if model_fn is None:
            raise ValueError(f"Unknown situation_type: {situation_type}")
        result = model_fn(**params)
        return asdict(result)

    # ------------------------------------------------------------------
    async def run(self, inputs: dict[str, Any], run_id: str = "") -> AgentResult:
        ticker = inputs.get("ticker", "")
        situation_type = inputs.get("situation_type", "")
        model_params = inputs.get("model_params", {})
        start = time.time()

        try:
            model_output = self._run_model(situation_type, model_params)
        except Exception as e:
            return AgentResult(
                agent_id=self.agent_id,
                agent_name=self.name,
                success=False,
                error=f"Model execution failed: {e}",
                duration_seconds=time.time() - start,
                run_id=run_id,
            )

        model_text = (
            f"=== {situation_type} Model Output for {ticker} ===\n"
            f"{json.dumps(model_output, indent=2)}"
        )

        client = AsyncAnthropic()
        try:
            message = await client.messages.create(
                model=self.model.value,
                max_tokens=4096,
                system=self._system_prompt,
                messages=[
                    {
                        "role": "user",
                        "content": (
                            f"Analyze the {situation_type} situation for {ticker}.\n\n"
                            f"{model_text}"
                        ),
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
