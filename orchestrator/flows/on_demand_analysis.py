"""Flow 2 — On-demand analysis of a single ticker.
Fans out 4 analysis agents in parallel, aggregates results.
"""
from __future__ import annotations
import asyncio
from typing import Any
from orchestrator.audit import AuditLogger
from orchestrator.base import AgentResult
from agents.a21_financial_analyst import FinancialAnalystAgent
from agents.a23_business_analyst import BusinessAnalystAgent
from agents.a24_risk_analyst import RiskAnalystAgent
from agents.a25_web_researcher import WebResearcherAgent


async def run_on_demand_analysis(ticker: str, run_id: str, audit: AuditLogger) -> dict[str, Any]:
    agents = [
        FinancialAnalystAgent(),
        BusinessAnalystAgent(),
        RiskAnalystAgent(),
        WebResearcherAgent(),
    ]

    async def run_with_audit(agent) -> AgentResult:
        audit.log_agent_start(run_id, agent.agent_id, {"ticker": ticker})
        result = await agent.run({"ticker": ticker}, run_id=run_id)
        audit.log_agent_end(run_id, agent.agent_id, result.success, tokens=result.tokens_used, duration=result.duration_seconds, error=result.error)
        return result

    results = await asyncio.gather(*[run_with_audit(a) for a in agents])

    aggregate = {
        "ticker": ticker,
        "run_id": run_id,
        "agents": {},
        "all_succeeded": all(r.success for r in results),
        "total_tokens": sum(r.tokens_used for r in results),
        "total_duration": max(r.duration_seconds for r in results) if results else 0,
    }
    for result in results:
        aggregate["agents"][result.agent_id] = result.to_dict()
    return aggregate
