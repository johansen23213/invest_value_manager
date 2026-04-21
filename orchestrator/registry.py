"""Agent registry for ValueHunter v1.0 — specs for all 10 agents."""
from __future__ import annotations

from orchestrator.base import AgentLayer, AgentModel


# Each spec is a plain dict; actual BaseAgent subclasses are created in Sprint 2+.
_AGENT_SPECS: list[dict] = [
    # ── Layer 0 — Governor ──────────────────────────────────────────────
    {
        "agent_id": "a00",
        "name": "Governor",
        "model": AgentModel.OPUS.value,
        "layer": AgentLayer.GOVERNOR.value,
        "description": (
            "Meta-decision orchestrator. Sequences and parallelises agents, "
            "manages state machine, emits audit events, triggers notifications."
        ),
        "skills": ["session-planner", "wave-system", "pipelines"],
        "tools": ["session_opener.py", "command_center.py"],
        "estimated_tokens": 5000,
    },

    # ── Layer 1 — Screening ─────────────────────────────────────────────
    {
        "agent_id": "a11",
        "name": "Quantitative Screener",
        "model": AgentModel.HAIKU.value,
        "layer": AgentLayer.SCREENING.value,
        "description": (
            "Programmatic value screening via yfinance + EDGAR. "
            "Produces scored candidate lists from configurable indices."
        ),
        "skills": ["screening-protocol"],
        "tools": [
            "dynamic_screener.py",
            "batch_scorer.py",
            "quality_universe.py",
            "quality_scorer.py",
        ],
        "estimated_tokens": 3500,
    },
    {
        "agent_id": "a12",
        "name": "Special Situations Screener",
        "model": AgentModel.HAIKU.value,
        "layer": AgentLayer.SCREENING.value,
        "description": (
            "SEC RSS + PR Newswire scanner for merger-arb, liquidations, "
            "spin-offs, net-cash biotechs, odd-lot tenders, and CVRs."
        ),
        "skills": ["screening-protocol"],
        "tools": ["scrapers/sec_edgar_rss.py", "scrapers/pr_newswire.py"],
        "estimated_tokens": 7500,
    },

    # ── Layer 2 — Deep Analysis ─────────────────────────────────────────
    {
        "agent_id": "a21",
        "name": "Financial Analyst",
        "model": AgentModel.SONNET.value,
        "layer": AgentLayer.ANALYSIS.value,
        "description": (
            "DCF 3-scenario, NAV, net cash, ROIC trend, red flags, and MoS. "
            "Core quantitative valuation agent."
        ),
        "skills": [
            "valuation-methods",
            "projection-framework",
            "filing-analysis",
        ],
        "tools": [
            "dcf_calculator.py",
            "quality_scorer.py",
            "narrative_checker.py",
            "forward_return.py",
        ],
        "estimated_tokens": 12000,
    },
    {
        "agent_id": "a22",
        "name": "Special Situation Modeler",
        "model": AgentModel.SONNET.value,
        "layer": AgentLayer.ANALYSIS.value,
        "description": (
            "Merger-arb spread + probability, liquidation value, spin-off "
            "stub valuation, biotech CVR modeling."
        ),
        "skills": ["contrathesis-framework"],
        "tools": [
            "models/merger_arb.py",
            "models/liquidation.py",
            "models/spinoff.py",
            "models/biotech_cash.py",
        ],
        "estimated_tokens": 9000,
    },
    {
        "agent_id": "a23",
        "name": "Business Analyst",
        "model": AgentModel.SONNET.value,
        "layer": AgentLayer.ANALYSIS.value,
        "description": (
            "Moat assessment, management quality, bull/bear scenarios, "
            "catalyst identification, and competitive positioning."
        ),
        "skills": [
            "business-analysis-framework",
            "skin-in-the-game",
            "quality-compounders",
            "sector-deep-dive",
        ],
        "tools": [
            "insider_tracker.py",
            "ownership_analyzer.py",
            "sector_health.py",
        ],
        "estimated_tokens": 10000,
    },
    {
        "agent_id": "a24",
        "name": "Risk Analyst",
        "model": AgentModel.HAIKU.value,
        "layer": AgentLayer.ANALYSIS.value,
        "description": (
            "7-dimension risk scoring, sizing cap recommendation, "
            "FX exposure, max drawdown estimation, thesis-break triggers."
        ),
        "skills": [],
        "tools": [
            "risk_heatmap.py",
            "constraint_checker.py",
            "drift_detector.py",
            "correlation_matrix.py",
        ],
        "estimated_tokens": 4500,
    },
    {
        "agent_id": "a25",
        "name": "Web Researcher",
        "model": AgentModel.HAIKU.value,
        "layer": AgentLayer.ANALYSIS.value,
        "description": (
            "News, earnings calls, 13F filings, Horos/Alpha Vulture "
            "coverage, regulatory and litigation monitoring."
        ),
        "skills": [],
        "tools": [
            "scrapers/horos_scraper.py",
            "scrapers/alpha_vulture_scraper.py",
        ],
        "estimated_tokens": 6000,
    },

    # ── Layer 3 — Portfolio ─────────────────────────────────────────────
    {
        "agent_id": "a31",
        "name": "Decision Maker",
        "model": AgentModel.SONNET.value,
        "layer": AgentLayer.PORTFOLIO.value,
        "description": (
            "Aggregates Layer 2 outputs, applies decision gates "
            "(MoS/ECAGR/risk/consistency/sizing), emits decision JSON."
        ),
        "skills": [
            "investment-rules",
            "pre-execution-check",
            "recommendation-context",
        ],
        "tools": ["consistency_checker.py", "portfolio_optimizer.py"],
        "estimated_tokens": 8000,
    },
    {
        "agent_id": "a32",
        "name": "Portfolio Monitor",
        "model": AgentModel.HAIKU.value,
        "layer": AgentLayer.PORTFOLIO.value,
        "description": (
            "Daily P&L snapshot, thesis drift detection, event timeline "
            "updates, new SEC filings, and review flagging."
        ),
        "skills": [],
        "tools": [
            "portfolio_stats.py",
            "thesis_monitor.py",
            "earnings_intel.py",
            "session_opener.py",
        ],
        "estimated_tokens": 3000,
    },
]


class AgentRegistry:
    """Read-only registry of all ValueHunter v1.0 agent specifications."""

    def __init__(self) -> None:
        self._specs: dict[str, dict] = {s["agent_id"]: s for s in _AGENT_SPECS}

    # ── query methods ───────────────────────────────────────────────────

    def list_agents(self) -> list[dict]:
        """Return all agent specs as a list of dicts."""
        return list(self._specs.values())

    def get(self, agent_id: str) -> dict | None:
        """Return a single agent spec by ID, or None."""
        return self._specs.get(agent_id)

    def get_by_layer(self, layer: int) -> list[dict]:
        """Return all agent specs belonging to a given layer value."""
        return [s for s in self._specs.values() if s["layer"] == layer]

    def get_model_for(self, agent_id: str) -> str | None:
        """Return the model string for a given agent ID, or None."""
        spec = self._specs.get(agent_id)
        return spec["model"] if spec else None

    def summary(self) -> str:
        """Human-readable summary table of the registry."""
        lines = [
            "Agent Registry — ValueHunter v1.0",
            "=" * 72,
            f"{'ID':<5} {'Name':<30} {'Model':<20} {'Layer':<4} {'Tokens':>6}",
            "-" * 72,
        ]
        for spec in self._specs.values():
            lines.append(
                f"{spec['agent_id']:<5} "
                f"{spec['name']:<30} "
                f"{spec['model']:<20} "
                f"{spec['layer']:<4} "
                f"{spec['estimated_tokens']:>6}"
            )
        lines.append("-" * 72)
        total_tokens = sum(s["estimated_tokens"] for s in self._specs.values())
        lines.append(f"{'Total':<5} {len(self._specs)} agents{'':<22} {'':<20} {'':<4} {total_tokens:>6}")
        return "\n".join(lines)
