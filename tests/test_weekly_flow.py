import pytest
from unittest.mock import patch, AsyncMock
from orchestrator.base import AgentResult
from orchestrator.governor import Governor


def _make_screener_result(agent_id, candidates):
    return AgentResult(
        agent_id=agent_id, agent_name="test", success=True,
        data={"candidates": candidates} if agent_id == "a11" else {"situations": candidates},
        tokens_used=100, duration_seconds=0.5,
    )

def _make_analysis_result():
    return {
        "ticker": "TEST", "all_succeeded": True, "total_tokens": 400,
        "agents": {
            "a21": {"success": True, "data": {"ticker": "TEST", "agent": "financial_analyst"}},
            "a23": {"success": True, "data": {"ticker": "TEST", "agent": "business_analyst"}},
            "a24": {"success": True, "data": {"ticker": "TEST", "agent": "risk_analyst"}},
            "a25": {"success": True, "data": {"ticker": "TEST", "agent": "web_researcher"}},
        }
    }

def _make_decision_result():
    return AgentResult(
        agent_id="a31", agent_name="test", success=True,
        data={"ticker": "TEST", "decision": "BUY", "conviction": 7},
        tokens_used=200, duration_seconds=1.0,
    )


class TestWeeklyFlow:
    @pytest.mark.asyncio
    async def test_weekly_returns_digest(self):
        quant_candidates = [
            {"ticker": "AAA", "score": 90, "signal_reasons": ["cheap"]},
            {"ticker": "BBB", "score": 80, "signal_reasons": ["value"]},
        ]
        with patch("orchestrator.flows.weekly_screening.QuantScreenerAgent") as m_quant, \
             patch("orchestrator.flows.weekly_screening.SpecialSitsScreenerAgent") as m_spec, \
             patch("orchestrator.flows.weekly_screening.run_on_demand_analysis") as m_analysis, \
             patch("orchestrator.flows.weekly_screening.DecisionMakerAgent") as m_dm:

            m_quant.return_value = AsyncMock()
            m_quant.return_value.agent_id = "a11"
            m_quant.return_value.run = AsyncMock(return_value=_make_screener_result("a11", quant_candidates))

            m_spec.return_value = AsyncMock()
            m_spec.return_value.agent_id = "a12"
            m_spec.return_value.run = AsyncMock(return_value=_make_screener_result("a12", []))

            m_analysis.return_value = _make_analysis_result()

            dm_inst = AsyncMock()
            dm_inst.agent_id = "a31"
            dm_inst.run = AsyncMock(return_value=_make_decision_result())
            m_dm.return_value = dm_inst

            gov = Governor()
            result = await gov.run_weekly()

            assert result["flow"] == "weekly"
            assert result["screening"]["total_candidates"] == 2
            assert len(result["decisions"]) >= 1
            assert result["all_succeeded"] is True

    @pytest.mark.asyncio
    async def test_weekly_deduplicates_candidates(self):
        # Same ticker from both screeners — should deduplicate
        quant_cands = [{"ticker": "DUP", "score": 90, "signal_reasons": ["quant"]}]
        special_sits = [{"ticker": "DUP", "type": "MERGER_ARB", "headline": "merger"}]

        with patch("orchestrator.flows.weekly_screening.QuantScreenerAgent") as m_quant, \
             patch("orchestrator.flows.weekly_screening.SpecialSitsScreenerAgent") as m_spec, \
             patch("orchestrator.flows.weekly_screening.run_on_demand_analysis") as m_analysis, \
             patch("orchestrator.flows.weekly_screening.DecisionMakerAgent") as m_dm:

            m_quant.return_value = AsyncMock()
            m_quant.return_value.agent_id = "a11"
            m_quant.return_value.run = AsyncMock(return_value=_make_screener_result("a11", quant_cands))

            m_spec.return_value = AsyncMock()
            m_spec.return_value.agent_id = "a12"
            spec_result = AgentResult(agent_id="a12", agent_name="test", success=True,
                data={"situations": special_sits}, tokens_used=100, duration_seconds=0.5)
            m_spec.return_value.run = AsyncMock(return_value=spec_result)

            m_analysis.return_value = _make_analysis_result()

            dm_inst = AsyncMock()
            dm_inst.agent_id = "a31"
            dm_inst.run = AsyncMock(return_value=_make_decision_result())
            m_dm.return_value = dm_inst

            gov = Governor()
            result = await gov.run_weekly()

            # DUP should appear only once in top tickers
            assert result["screening"]["top_tickers"].count("DUP") == 1
