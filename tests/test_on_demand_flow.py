import pytest
from unittest.mock import patch, AsyncMock
from orchestrator.base import AgentResult
from orchestrator.governor import Governor


def _make_mock_agent(agent_id):
    inst = AsyncMock()
    inst.agent_id = agent_id
    inst.run = AsyncMock(return_value=AgentResult(
        agent_id=agent_id, agent_name="test", success=True,
        data={"ticker": "TEST", "agent": agent_id}, tokens_used=100, duration_seconds=0.5,
    ))
    return inst


class TestOnDemandFlow:
    @pytest.mark.asyncio
    async def test_returns_aggregate_with_4_agents(self):
        with patch("orchestrator.flows.on_demand_analysis.FinancialAnalystAgent") as m1, \
             patch("orchestrator.flows.on_demand_analysis.BusinessAnalystAgent") as m2, \
             patch("orchestrator.flows.on_demand_analysis.RiskAnalystAgent") as m3, \
             patch("orchestrator.flows.on_demand_analysis.WebResearcherAgent") as m4:
            m1.return_value = _make_mock_agent("a21")
            m2.return_value = _make_mock_agent("a23")
            m3.return_value = _make_mock_agent("a24")
            m4.return_value = _make_mock_agent("a25")

            gov = Governor()
            result = await gov.run_on_demand("TEST")
            assert result["ticker"] == "TEST"
            assert result["all_succeeded"] is True
            assert len(result["agents"]) == 4
            assert "a21" in result["agents"]
            assert "a25" in result["agents"]
            assert result["total_tokens"] == 400

    @pytest.mark.asyncio
    async def test_handles_agent_failure(self):
        with patch("orchestrator.flows.on_demand_analysis.FinancialAnalystAgent") as m1, \
             patch("orchestrator.flows.on_demand_analysis.BusinessAnalystAgent") as m2, \
             patch("orchestrator.flows.on_demand_analysis.RiskAnalystAgent") as m3, \
             patch("orchestrator.flows.on_demand_analysis.WebResearcherAgent") as m4:
            m1.return_value = _make_mock_agent("a21")
            m2.return_value = _make_mock_agent("a23")
            # Make risk agent fail
            fail_agent = AsyncMock()
            fail_agent.agent_id = "a24"
            fail_agent.run = AsyncMock(return_value=AgentResult(
                agent_id="a24", agent_name="test", success=False,
                error="API error", tokens_used=50, duration_seconds=0.1,
            ))
            m3.return_value = fail_agent
            m4.return_value = _make_mock_agent("a25")

            gov = Governor()
            result = await gov.run_on_demand("TEST")
            assert result["all_succeeded"] is False
            assert result["agents"]["a24"]["success"] is False

    @pytest.mark.asyncio
    async def test_governor_state_transitions(self):
        with patch("orchestrator.flows.on_demand_analysis.FinancialAnalystAgent") as m1, \
             patch("orchestrator.flows.on_demand_analysis.BusinessAnalystAgent") as m2, \
             patch("orchestrator.flows.on_demand_analysis.RiskAnalystAgent") as m3, \
             patch("orchestrator.flows.on_demand_analysis.WebResearcherAgent") as m4:
            for m, aid in [(m1,"a21"),(m2,"a23"),(m3,"a24"),(m4,"a25")]:
                m.return_value = _make_mock_agent(aid)
            gov = Governor()
            await gov.run_on_demand("TEST")
            from orchestrator.governor import GovernorState
            assert gov.state == GovernorState.IDLE
