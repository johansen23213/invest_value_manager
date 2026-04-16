"""Tests for orchestrator.governor — state machine and flow stubs."""
import pytest

from orchestrator.governor import Governor, GovernorState


@pytest.fixture
def governor():
    return Governor()


def test_governor_initial_state(governor):
    assert governor.state == GovernorState.IDLE


def test_governor_list_agents(governor):
    agents = governor.list_agents()
    assert len(agents) == 10


def test_governor_dry_run(governor, capsys):
    governor.dry_run()
    captured = capsys.readouterr()
    assert "Agent Registry" in captured.out
    assert "10 agents" in captured.out


def test_governor_state_transitions(governor):
    """Verify that _transition changes state correctly."""
    assert governor.state == GovernorState.IDLE

    governor._transition(GovernorState.SCREENING)
    assert governor.state == GovernorState.SCREENING

    governor._transition(GovernorState.CANDIDATE_SELECTION)
    assert governor.state == GovernorState.CANDIDATE_SELECTION

    governor._transition(GovernorState.ANALYSIS_FANOUT)
    assert governor.state == GovernorState.ANALYSIS_FANOUT

    governor._transition(GovernorState.DECISION)
    assert governor.state == GovernorState.DECISION

    governor._transition(GovernorState.NOTIFY)
    assert governor.state == GovernorState.NOTIFY

    governor._transition(GovernorState.IDLE)
    assert governor.state == GovernorState.IDLE


async def test_governor_on_demand_flow(governor):
    result = await governor.run_on_demand("AAPL")
    assert result["flow"] == "on-demand"
    assert result["ticker"] == "AAPL"
    assert result["status"] == "stub"
    assert "run_id" in result
    # Should return to IDLE after flow completes
    assert governor.state == GovernorState.IDLE


async def test_governor_weekly_flow(governor):
    result = await governor.run_weekly()
    assert result["flow"] == "weekly"
    assert result["status"] == "stub"
    assert governor.state == GovernorState.IDLE


async def test_governor_daily_monitor_flow(governor):
    result = await governor.run_daily_monitor()
    assert result["flow"] == "daily-monitor"
    assert result["status"] == "stub"
    assert governor.state == GovernorState.IDLE


async def test_governor_audit_log_written(governor, tmp_path):
    """Verify audit JSONL files are created during flows."""
    from orchestrator.audit import AuditLogger

    governor.audit = AuditLogger(log_dir=tmp_path)
    result = await governor.run_on_demand("MSFT")
    run_id = result["run_id"]

    events = governor.audit.read_run(run_id)
    assert len(events) >= 2  # at least run_start + run_end
    assert events[0].event_type == "run_start"
    assert events[-1].event_type == "run_end"
