# Sprint 2 — Deep Analysis Agents Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build 4 AI-powered analysis agents (Financial, Business, Risk, Web Researcher) that call Claude via Anthropic SDK, invoke existing Python tools, and return structured JSON — plus wire them into the Governor's on-demand flow for parallel execution.

**Architecture:** Each agent follows a 3-step pattern: (1) run existing tools via subprocess to gather raw data, (2) send data + agent prompt to Claude API, (3) parse structured JSON response into AgentResult. The on-demand flow fans out all 4 agents in parallel via asyncio.gather().

**Tech Stack:** anthropic SDK (async), asyncio, subprocess, existing 45 tools

**Working directory:** `/Volumes/Storage/Documents/Claude/value_hunter/invest_value_manager/`

**Critical constraint:** Existing tools must be called via subprocess (not imported) to preserve their standalone operation. Agent prompts live in `agents/prompts/`.

---

## File Structure

```
invest_value_manager/
├── agents/
│   ├── __init__.py                          # EXISTS
│   ├── _tool_runner.py                      # NEW — Task 1: subprocess tool invocation
│   ├── a21_financial_analyst.py             # NEW — Task 2
│   ├── a23_business_analyst.py              # NEW — Task 3
│   ├── a24_risk_analyst.py                  # NEW — Task 4
│   ├── a25_web_researcher.py                # NEW — Task 5
│   └── prompts/                             # NEW
│       ├── a21_financial_analyst.md          # NEW — Task 2
│       ├── a23_business_analyst.md           # NEW — Task 3
│       ├── a24_risk_analyst.md               # NEW — Task 4
│       └── a25_web_researcher.md             # NEW — Task 5
├── orchestrator/
│   ├── governor.py                          # MODIFY — Task 6: wire on-demand flow
│   └── flows/
│       └── on_demand_analysis.py            # NEW — Task 6
├── tests/
│   ├── test_tool_runner.py                  # NEW — Task 1
│   ├── test_a21_financial_analyst.py        # NEW — Task 2
│   ├── test_a23_business_analyst.py         # NEW — Task 3
│   ├── test_a24_risk_analyst.py             # NEW — Task 4
│   ├── test_a25_web_researcher.py           # NEW — Task 5
│   └── test_on_demand_flow.py              # NEW — Task 6
```

---

### Task 1: Tool Runner Utility

Shared utility for agents to invoke existing Python tools via subprocess and capture output.

**Files:**
- Create: `agents/_tool_runner.py`
- Create: `tests/test_tool_runner.py`

- [ ] **Step 1: Write failing test**

```python
# tests/test_tool_runner.py
import pytest
from agents._tool_runner import run_tool, ToolResult


class TestRunTool:
    def test_runs_python_script(self):
        result = run_tool("python3", ["-c", "print('hello')"])
        assert result.success is True
        assert "hello" in result.stdout

    def test_captures_stderr(self):
        result = run_tool("python3", ["-c", "import sys; sys.stderr.write('warn')"])
        assert "warn" in result.stderr

    def test_timeout_returns_failure(self):
        result = run_tool("python3", ["-c", "import time; time.sleep(10)"], timeout=1)
        assert result.success is False

    def test_nonexistent_command(self):
        result = run_tool("nonexistent_binary_xyz", [])
        assert result.success is False
        assert result.error is not None
```

- [ ] **Step 2: Run test, verify failure**

Run: `python3 -m pytest tests/test_tool_runner.py -v`
Expected: FAIL — ImportError

- [ ] **Step 3: Implement `agents/_tool_runner.py`**

```python
"""Subprocess wrapper for invoking existing Python tools from agents."""
from __future__ import annotations

import pathlib
import subprocess
from dataclasses import dataclass

ROOT = pathlib.Path(__file__).resolve().parent.parent


@dataclass
class ToolResult:
    tool: str
    success: bool
    stdout: str = ""
    stderr: str = ""
    error: str | None = None
    return_code: int = -1


def run_tool(
    command: str,
    args: list[str],
    timeout: int = 60,
    cwd: pathlib.Path | None = None,
) -> ToolResult:
    try:
        proc = subprocess.run(
            [command] + args,
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=str(cwd or ROOT),
        )
        return ToolResult(
            tool=command,
            success=proc.returncode == 0,
            stdout=proc.stdout,
            stderr=proc.stderr,
            return_code=proc.returncode,
        )
    except subprocess.TimeoutExpired:
        return ToolResult(tool=command, success=False, error=f"Timeout after {timeout}s")
    except FileNotFoundError:
        return ToolResult(tool=command, success=False, error=f"Command not found: {command}")
    except Exception as e:
        return ToolResult(tool=command, success=False, error=str(e))


def run_investment_tool(tool_name: str, args: list[str], timeout: int = 60) -> ToolResult:
    tool_path = ROOT / "tools" / tool_name
    if not tool_path.exists():
        return ToolResult(tool=tool_name, success=False, error=f"Tool not found: {tool_path}")
    return run_tool("python3", [str(tool_path)] + args, timeout=timeout)
```

- [ ] **Step 4: Run tests, verify pass**

Run: `python3 -m pytest tests/test_tool_runner.py -v`
Expected: 4 PASS

- [ ] **Step 5: Commit**

```bash
git add agents/_tool_runner.py tests/test_tool_runner.py
git commit -m "feat: add tool runner utility for subprocess invocation of existing tools"
```

---

### Task 2: Financial Analyst Agent (A2.1)

**Files:**
- Create: `agents/prompts/a21_financial_analyst.md`
- Create: `agents/a21_financial_analyst.py`
- Create: `tests/test_a21_financial_analyst.py`

- [ ] **Step 1: Create agent prompt**

File `agents/prompts/a21_financial_analyst.md`:
```markdown
# Financial Analyst (A2.1)

You are the Financial Analyst agent in the ValueHunter v1.0 system. Your job is to produce a comprehensive financial analysis of a single company.

## Your Data

You will receive raw output from these quantitative tools:
- **quality_scorer.py**: Quality Score profile (ROIC, margins, growth, FCF)
- **dcf_calculator.py**: DCF valuation with 3 scenarios (bear/base/bull)
- **narrative_checker.py**: Financial trend analysis (margin trajectory, R&D, SBC, receivables)
- **forward_return.py**: Expected CAGR at current market price

## Your Output

Respond with a JSON object (and nothing else) matching this structure:

```json
{
  "ticker": "MORN",
  "agent": "financial_analyst",
  "quality_score": {"raw": 78, "tier": "A", "key_strengths": ["..."], "key_weaknesses": ["..."]},
  "valuation": {
    "dcf_bear": 150.0,
    "dcf_base": 195.0,
    "dcf_bull": 240.0,
    "weighted_fv": 195.0,
    "current_price": 170.0,
    "mos_pct": 12.8,
    "e_cagr_pct": 15.6
  },
  "financial_health": {
    "roic_pct": 25.3,
    "fcf_margin_pct": 18.5,
    "debt_to_equity": 0.4,
    "revenue_growth_3yr_cagr_pct": 8.2,
    "red_flags": []
  },
  "narrative_trends": ["margin expansion", "R&D stable"],
  "investment_grade": "A",
  "summary": "One paragraph financial summary"
}
```

## Rules
- Use ONLY the tool data provided. Do not invent numbers.
- If a tool failed or returned no data, note it in the summary and use available data.
- Red flags: goodwill > 40% of assets, declining ROIC trend, negative FCF, rising SBC > 5% of revenue.
- Investment grade: A (strong buy signal), B (buy with conditions), C (watch), D (avoid).
```

- [ ] **Step 2: Write failing test**

```python
# tests/test_a21_financial_analyst.py
import json
import pytest
from unittest.mock import patch, AsyncMock
from agents.a21_financial_analyst import FinancialAnalystAgent
from orchestrator.base import AgentResult


class TestFinancialAnalystAgent:
    def test_init(self):
        agent = FinancialAnalystAgent()
        assert agent.agent_id == "a21"
        assert agent.name == "Financial Analyst"

    @pytest.mark.asyncio
    async def test_run_with_mocked_tools_and_api(self):
        agent = FinancialAnalystAgent()
        mock_api_response = json.dumps({
            "ticker": "TEST",
            "agent": "financial_analyst",
            "quality_score": {"raw": 75, "tier": "A", "key_strengths": ["High ROIC"], "key_weaknesses": []},
            "valuation": {"dcf_bear": 100, "dcf_base": 130, "dcf_bull": 160, "weighted_fv": 130, "current_price": 110, "mos_pct": 15.4, "e_cagr_pct": 12.0},
            "financial_health": {"roic_pct": 20, "fcf_margin_pct": 15, "debt_to_equity": 0.3, "revenue_growth_3yr_cagr_pct": 7, "red_flags": []},
            "narrative_trends": ["stable margins"],
            "investment_grade": "A",
            "summary": "Strong financial profile."
        })

        with patch("agents.a21_financial_analyst.run_investment_tool") as mock_tool, \
             patch("agents.a21_financial_analyst.AsyncAnthropic") as mock_client_cls:

            from agents._tool_runner import ToolResult
            mock_tool.return_value = ToolResult(tool="test", success=True, stdout="mock tool output")

            mock_message = AsyncMock()
            mock_message.content = [AsyncMock(text=mock_api_response)]
            mock_message.usage = AsyncMock(input_tokens=1000, output_tokens=500)
            mock_client = AsyncMock()
            mock_client.messages.create = AsyncMock(return_value=mock_message)
            mock_client_cls.return_value = mock_client

            result = await agent.run({"ticker": "TEST"}, run_id="test-run")

            assert result.success is True
            assert result.data["ticker"] == "TEST"
            assert result.data["agent"] == "financial_analyst"
            assert "valuation" in result.data

    def test_prompt_file_exists(self):
        import pathlib
        prompt = pathlib.Path(__file__).resolve().parent.parent / "agents" / "prompts" / "a21_financial_analyst.md"
        assert prompt.exists()
```

- [ ] **Step 3: Implement `agents/a21_financial_analyst.py`**

```python
"""Agent 2.1 — Financial Analyst. Calls DCF, QS, narrative tools + Claude for synthesis."""
from __future__ import annotations

import json
import pathlib
import time
from typing import Any

from anthropic import AsyncAnthropic

from orchestrator.base import BaseAgent, AgentModel, AgentLayer, AgentResult
from agents._tool_runner import run_investment_tool

PROMPT_PATH = pathlib.Path(__file__).parent / "prompts" / "a21_financial_analyst.md"


class FinancialAnalystAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            agent_id="a21",
            name="Financial Analyst",
            model=AgentModel.SONNET,
            layer=AgentLayer.ANALYSIS,
            description="DCF 3-scenario, NAV, net cash, ROIC trend, accounting red flags, MoS",
            skills=["valuation-methods", "projection-framework", "filing-analysis"],
            tools=["dcf_calculator.py", "quality_scorer.py", "narrative_checker.py", "forward_return.py"],
            estimated_tokens=12000,
        )
        self._system_prompt = PROMPT_PATH.read_text()

    def _gather_tool_data(self, ticker: str) -> str:
        sections = []
        tools_config = [
            ("quality_scorer.py", [ticker, "--detailed"]),
            ("dcf_calculator.py", [ticker, "--scenarios"]),
            ("narrative_checker.py", [ticker]),
            ("forward_return.py", ["--active-only"]),
        ]
        for tool_name, args in tools_config:
            result = run_investment_tool(tool_name, args, timeout=45)
            header = f"=== {tool_name} ==="
            if result.success:
                sections.append(f"{header}\n{result.stdout}")
            else:
                sections.append(f"{header}\n[TOOL FAILED: {result.error or result.stderr}]")
        return "\n\n".join(sections)

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
                messages=[{"role": "user", "content": f"Analyze {ticker}. Here is the raw tool data:\n\n{tool_data}"}],
            )
            response_text = message.content[0].text
            tokens = message.usage.input_tokens + message.usage.output_tokens
            data = json.loads(response_text)
            return AgentResult(
                agent_id=self.agent_id, agent_name=self.name,
                success=True, data=data, tokens_used=tokens,
                duration_seconds=time.time() - start, run_id=run_id,
            )
        except json.JSONDecodeError as e:
            return AgentResult(
                agent_id=self.agent_id, agent_name=self.name,
                success=False, error=f"Invalid JSON from Claude: {e}",
                duration_seconds=time.time() - start, run_id=run_id,
            )
        except Exception as e:
            return AgentResult(
                agent_id=self.agent_id, agent_name=self.name,
                success=False, error=str(e),
                duration_seconds=time.time() - start, run_id=run_id,
            )
```

- [ ] **Step 4: Run tests, verify pass**

Run: `python3 -m pytest tests/test_a21_financial_analyst.py -v`
Expected: 3 PASS

- [ ] **Step 5: Commit**

```bash
git add agents/a21_financial_analyst.py agents/prompts/a21_financial_analyst.md tests/test_a21_financial_analyst.py
git commit -m "feat: add Financial Analyst agent (A2.1) with tool invocation and Claude synthesis"
```

---

### Task 3: Business Analyst Agent (A2.3)

Same pattern as A2.1. Uses tools: insider_tracker.py, ownership_analyzer.py, sector_health.py. Model: sonnet-4-6.

**Files:**
- Create: `agents/prompts/a23_business_analyst.md`
- Create: `agents/a23_business_analyst.py`
- Create: `tests/test_a23_business_analyst.py`

Output JSON structure:
```json
{
  "ticker": "MORN",
  "agent": "business_analyst",
  "moat": {"type": "wide|narrow|none", "sources": ["brand", "switching costs"], "durability": "high|medium|low"},
  "management": {"skin_in_the_game_pct": 5.2, "capital_allocation": "excellent|good|fair|poor", "key_observations": ["..."]},
  "competitive_position": {"market_share": "...", "competitors": ["..."], "advantages": ["..."]},
  "bull_case": "One paragraph",
  "bear_case": "One paragraph",
  "catalysts": [{"description": "...", "expected_date": "2026-Q3", "impact": "HIGH|MEDIUM|LOW"}],
  "business_quality_grade": "A|B|C|D",
  "summary": "One paragraph"
}
```

Tools invoked: `insider_tracker.py TICKER`, `ownership_analyzer.py --sentiment`, `sector_health.py coverage`

Follow exact same implementation pattern as Task 2 (BaseAgent subclass, prompt file, _gather_tool_data, Claude call, JSON parse).

Tests: init, mocked run, prompt exists.
Commit: `"feat: add Business Analyst agent (A2.3) with moat/management analysis"`

---

### Task 4: Risk Analyst Agent (A2.4)

Model: haiku-4-5. Tools: constraint_checker.py, correlation_matrix.py, drift_detector.py.

**Files:**
- Create: `agents/prompts/a24_risk_analyst.md`
- Create: `agents/a24_risk_analyst.py`
- Create: `tests/test_a24_risk_analyst.py`

Output JSON structure:
```json
{
  "ticker": "MORN",
  "agent": "risk_analyst",
  "risk_score": 4.5,
  "risk_dimensions": {
    "liquidity": {"score": 3, "notes": "..."},
    "concentration": {"score": 5, "notes": "..."},
    "thesis_break": {"score": 4, "notes": "..."},
    "execution": {"score": 3, "notes": "..."},
    "fx_exposure": {"score": 2, "notes": "..."},
    "max_drawdown_pct": {"score": 6, "notes": "..."},
    "correlation": {"score": 4, "notes": "..."}
  },
  "sizing_cap_pct": 8.0,
  "thesis_break_scenarios": ["Revenue decline >15%", "Key customer loss"],
  "overall_assessment": "ACCEPTABLE|ELEVATED|HIGH",
  "summary": "One paragraph"
}
```

Tools invoked: `constraint_checker.py REPORT`, `correlation_matrix.py --from-portfolio`, `drift_detector.py`

Same pattern. Tests: init, mocked run, prompt exists.
Commit: `"feat: add Risk Analyst agent (A2.4) with 7-dimension risk scoring"`

---

### Task 5: Web Researcher Agent (A2.5)

Model: haiku-4-5. Uses Anthropic web_search tool (not subprocess tools).

**Files:**
- Create: `agents/prompts/a25_web_researcher.md`
- Create: `agents/a25_web_researcher.py`
- Create: `tests/test_a25_web_researcher.py`

This agent is DIFFERENT from the others — instead of running subprocess tools, it uses Claude's built-in web_search capability to find recent news, earnings transcripts, and coverage.

Output JSON structure:
```json
{
  "ticker": "MORN",
  "agent": "web_researcher",
  "recent_news": [{"date": "2026-04-10", "headline": "...", "source": "...", "sentiment": "positive|negative|neutral"}],
  "earnings_highlights": "Latest quarter summary if available",
  "value_manager_coverage": {"horos": false, "alpha_vulture": false, "other_13f": ["Berkshire Hathaway"]},
  "regulatory_flags": [],
  "litigation_flags": [],
  "summary": "One paragraph"
}
```

Implementation: Uses `client.messages.create()` with `tools=[{"type": "web_search_20250305", "name": "web_search", "max_uses": 5}]` to enable Claude's built-in web search. Also checks local Horos/AV data files (`knowledge_base/universe/horos_positions.json`, `alpha_vulture_ideas.json`) for existing coverage.

Same test pattern with mocks.
Commit: `"feat: add Web Researcher agent (A2.5) with web search and local KB lookup"`

---

### Task 6: On-Demand Analysis Flow

Wire the 4 agents into the Governor's on-demand flow.

**Files:**
- Create: `orchestrator/flows/__init__.py`
- Create: `orchestrator/flows/on_demand_analysis.py`
- Modify: `orchestrator/governor.py` — replace stub with real flow
- Create: `tests/test_on_demand_flow.py`

- [ ] **Step 1: Create `orchestrator/flows/on_demand_analysis.py`**

```python
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


async def run_on_demand_analysis(
    ticker: str,
    run_id: str,
    audit: AuditLogger,
) -> dict[str, Any]:
    agents = [
        FinancialAnalystAgent(),
        BusinessAnalystAgent(),
        RiskAnalystAgent(),
        WebResearcherAgent(),
    ]

    async def run_with_audit(agent) -> AgentResult:
        audit.log_agent_start(run_id, agent.agent_id, {"ticker": ticker})
        result = await agent.run({"ticker": ticker}, run_id=run_id)
        audit.log_agent_end(
            run_id, agent.agent_id, result.success,
            tokens=result.tokens_used, duration=result.duration_seconds,
            error=result.error,
        )
        return result

    results = await asyncio.gather(*[run_with_audit(a) for a in agents])

    aggregate = {
        "ticker": ticker,
        "run_id": run_id,
        "agents": {},
        "all_succeeded": all(r.success for r in results),
        "total_tokens": sum(r.tokens_used for r in results),
        "total_duration": max(r.duration_seconds for r in results),
    }
    for result in results:
        aggregate["agents"][result.agent_id] = result.to_dict()

    return aggregate
```

- [ ] **Step 2: Update `orchestrator/governor.py` — replace on-demand stub**

Replace the `run_on_demand` method's stub body with:
```python
async def run_on_demand(self, ticker: str) -> dict[str, Any]:
    from orchestrator.flows.on_demand_analysis import run_on_demand_analysis
    run_id = self._new_run_id()
    self.audit.log_run_start(run_id, "on-demand", {"ticker": ticker})
    self._transition(GovernorState.ANALYSIS_FANOUT)
    result = await run_on_demand_analysis(ticker, run_id, self.audit)
    self._transition(GovernorState.DECISION)
    # Sprint 3: A3.1 Decision Maker here
    self._transition(GovernorState.IDLE)
    self.audit.log_run_end(run_id, result["all_succeeded"], result)
    return result
```

- [ ] **Step 3: Write test with fully mocked agents**

```python
# tests/test_on_demand_flow.py
import pytest
from unittest.mock import patch, AsyncMock
from orchestrator.governor import Governor


class TestOnDemandFlow:
    @pytest.mark.asyncio
    async def test_on_demand_returns_aggregate(self):
        from orchestrator.base import AgentResult
        mock_result = AgentResult(
            agent_id="a21", agent_name="test", success=True,
            data={"ticker": "TEST"}, tokens_used=100, duration_seconds=1.0,
        )
        with patch("orchestrator.flows.on_demand_analysis.FinancialAnalystAgent") as m1, \
             patch("orchestrator.flows.on_demand_analysis.BusinessAnalystAgent") as m2, \
             patch("orchestrator.flows.on_demand_analysis.RiskAnalystAgent") as m3, \
             patch("orchestrator.flows.on_demand_analysis.WebResearcherAgent") as m4:
            for m, aid in [(m1, "a21"), (m2, "a23"), (m3, "a24"), (m4, "a25")]:
                inst = AsyncMock()
                inst.agent_id = aid
                inst.run = AsyncMock(return_value=AgentResult(
                    agent_id=aid, agent_name="test", success=True,
                    data={"ticker": "TEST"}, tokens_used=100, duration_seconds=0.5,
                ))
                m.return_value = inst

            gov = Governor()
            result = await gov.run_on_demand("TEST")
            assert result["ticker"] == "TEST"
            assert result["all_succeeded"] is True
            assert len(result["agents"]) == 4
```

- [ ] **Step 4: Run all tests**

Run: `python3 -m pytest tests/ -v`
Expected: All tests PASS (165 existing + ~15 new)

- [ ] **Step 5: Commit**

```bash
git add orchestrator/flows/ orchestrator/governor.py tests/test_on_demand_flow.py
git commit -m "feat: wire on-demand analysis flow with 4-agent parallel fanout"
```

---

## Sprint 2 Verification Checklist

After all tasks complete:
- [ ] `python3 -m pytest tests/ -v` — all green
- [ ] `python3 -m orchestrator --dry-run` — still lists 10 agents
- [ ] All 4 agent classes importable: `python3 -c "from agents.a21_financial_analyst import FinancialAnalystAgent; print('OK')"`
- [ ] On-demand flow with mocked agents produces aggregate JSON
- [ ] No existing v4.6 tools modified
