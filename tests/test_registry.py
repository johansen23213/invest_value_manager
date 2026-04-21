"""Tests for orchestrator.registry — agent specs and model routing."""
import pytest

from orchestrator.base import AgentLayer, AgentModel
from orchestrator.registry import AgentRegistry

REQUIRED_FIELDS = {"agent_id", "name", "model", "layer", "description",
                   "skills", "tools", "estimated_tokens"}


@pytest.fixture
def registry():
    return AgentRegistry()


def test_registry_has_10_agent_specs(registry):
    assert len(registry.list_agents()) == 10


def test_registry_agents_have_required_fields(registry):
    for spec in registry.list_agents():
        missing = REQUIRED_FIELDS - set(spec.keys())
        assert not missing, f"Agent {spec.get('agent_id', '?')} missing: {missing}"


def test_registry_get_by_id(registry):
    spec = registry.get("a11")
    assert spec is not None
    assert spec["name"] == "Quantitative Screener"


def test_registry_get_by_id_missing(registry):
    assert registry.get("a99") is None


def test_registry_get_by_layer_screening(registry):
    screening = registry.get_by_layer(AgentLayer.SCREENING.value)
    assert len(screening) == 2


def test_registry_get_by_layer_analysis(registry):
    analysis = registry.get_by_layer(AgentLayer.ANALYSIS.value)
    assert len(analysis) == 5


def test_registry_model_routing_haiku_count(registry):
    haiku = [s for s in registry.list_agents()
             if s["model"] == AgentModel.HAIKU.value]
    assert len(haiku) == 5


def test_registry_model_routing_sonnet_count(registry):
    sonnet = [s for s in registry.list_agents()
              if s["model"] == AgentModel.SONNET.value]
    assert len(sonnet) == 4


def test_registry_model_routing_opus_count(registry):
    opus = [s for s in registry.list_agents()
            if s["model"] == AgentModel.OPUS.value]
    assert len(opus) == 1


def test_registry_get_model_for(registry):
    assert registry.get_model_for("a00") == AgentModel.OPUS.value
    assert registry.get_model_for("a11") == AgentModel.HAIKU.value
    assert registry.get_model_for("a21") == AgentModel.SONNET.value
    assert registry.get_model_for("a99") is None


def test_registry_summary(registry):
    summary = registry.summary()
    assert "Agent Registry" in summary
    assert "10 agents" in summary
