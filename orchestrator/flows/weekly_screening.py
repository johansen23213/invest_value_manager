"""Flow 1 — Weekly screening pipeline.
Dual screener parallel → merge → top-5 → analysis → Decision Maker → digest.
"""
from __future__ import annotations
import asyncio
from typing import Any
from orchestrator.audit import AuditLogger
from orchestrator.base import AgentResult
from orchestrator.flows.on_demand_analysis import run_on_demand_analysis
from agents.a11_quant_screener import QuantScreenerAgent
from agents.a12_special_sits_screener import SpecialSitsScreenerAgent
from agents.a31_decision_maker import DecisionMakerAgent


async def run_weekly_screening(
    run_id: str,
    audit: AuditLogger,
    top_n: int = 5,
) -> dict[str, Any]:
    # Phase 1: Parallel screening
    quant = QuantScreenerAgent()
    special = SpecialSitsScreenerAgent()

    async def run_screener(agent):
        audit.log_agent_start(run_id, agent.agent_id, {"flow": "weekly"})
        result = await agent.run({"flow": "weekly"}, run_id=run_id)
        audit.log_agent_end(run_id, agent.agent_id, result.success, tokens=result.tokens_used, duration=result.duration_seconds, error=result.error)
        return result

    screen_results = await asyncio.gather(
        run_screener(quant),
        run_screener(special),
    )

    # Phase 2: Merge and rank candidates
    candidates = []
    for result in screen_results:
        if result.success and "candidates" in result.data:
            candidates.extend(result.data["candidates"])
        elif result.success and "situations" in result.data:
            for sit in result.data["situations"]:
                candidates.append({
                    "ticker": sit.get("ticker", "UNKNOWN"),
                    "score": 50,  # default score for special sits
                    "signal_reasons": [sit.get("type", "SPECIAL_SIT"), sit.get("headline", "")],
                    "source": "special_sits",
                })

    # Deduplicate by ticker, keep highest score
    by_ticker: dict[str, dict] = {}
    for c in candidates:
        t = c.get("ticker", "")
        if t not in by_ticker or c.get("score", 0) > by_ticker[t].get("score", 0):
            by_ticker[t] = c
    ranked = sorted(by_ticker.values(), key=lambda x: x.get("score", 0), reverse=True)
    top_candidates = ranked[:top_n]

    # Phase 3: Deep analysis for each top candidate
    analyses: dict[str, dict] = {}
    for candidate in top_candidates:
        ticker = candidate.get("ticker", "")
        if not ticker or ticker == "UNKNOWN":
            continue
        analysis = await run_on_demand_analysis(ticker, run_id, audit)
        analyses[ticker] = analysis

    # Phase 4: Decision Maker for each analyzed candidate
    decision_maker = DecisionMakerAgent()
    decisions = []
    for ticker, analysis in analyses.items():
        agent_outputs: dict[str, Any] = {}
        for aid, adata in analysis.get("agents", {}).items():
            if adata.get("success"):
                agent_outputs[aid] = adata.get("data", {})

        dm_inputs = {"ticker": ticker, **agent_outputs}
        audit.log_agent_start(run_id, decision_maker.agent_id, {"ticker": ticker})
        dm_result = await decision_maker.run(dm_inputs, run_id=run_id)
        audit.log_agent_end(run_id, decision_maker.agent_id, dm_result.success, tokens=dm_result.tokens_used, duration=dm_result.duration_seconds, error=dm_result.error)

        if dm_result.success:
            decisions.append(dm_result.data)

    # Phase 5: Aggregate digest
    total_tokens = sum(r.tokens_used for r in screen_results)
    for a in analyses.values():
        total_tokens += a.get("total_tokens", 0)

    return {
        "run_id": run_id,
        "flow": "weekly",
        "screening": {
            "total_candidates": len(candidates),
            "top_n": len(top_candidates),
            "top_tickers": [c.get("ticker") for c in top_candidates],
        },
        "analyses_completed": len(analyses),
        "decisions": decisions,
        "total_tokens": total_tokens,
        "all_succeeded": all(r.success for r in screen_results),
    }
