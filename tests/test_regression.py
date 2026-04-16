"""Regression tests — verify existing v4.6 tools are not broken by v1.0 additions."""
import pathlib
import subprocess
import sys
import pytest
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent


class TestExistingFilesIntact:
    def test_portfolio_current_loads(self):
        path = ROOT / "portfolio" / "current.yaml"
        if not path.exists():
            pytest.skip("portfolio/current.yaml not found")
        data = yaml.safe_load(path.read_text())
        assert "positions" in data
        assert isinstance(data["positions"], list)

    def test_portfolio_history_loads(self):
        path = ROOT / "portfolio" / "history.yaml"
        if not path.exists():
            pytest.skip("portfolio/history.yaml not found")
        data = yaml.safe_load(path.read_text())
        assert "closed_positions" in data

    def test_decisions_log_loads(self):
        path = ROOT / "learning" / "decisions_log.yaml"
        if not path.exists():
            pytest.skip("decisions_log.yaml not found")
        data = yaml.safe_load(path.read_text())
        assert data is not None

    def test_principles_exists(self):
        path = ROOT / "learning" / "principles.md"
        assert path.exists(), "principles.md must not be deleted"

    def test_claude_md_exists_and_has_identity(self):
        path = ROOT / "CLAUDE.md"
        assert path.exists()
        content = path.read_text()
        assert "CIO" in content
        assert "Principios" in content

    def test_tools_directory_intact(self):
        tools_dir = ROOT / "tools"
        assert tools_dir.is_dir()
        py_files = list(tools_dir.glob("*.py"))
        assert len(py_files) >= 30, f"Expected >=30 tools, found {len(py_files)}"

    def test_skills_directory_intact(self):
        skills_dir = ROOT / ".claude" / "skills"
        assert skills_dir.is_dir()

    def test_rules_directory_intact(self):
        rules_dir = ROOT / ".claude" / "rules"
        assert rules_dir.is_dir()
        assert (rules_dir / "agent-protocol.md").exists()
        assert (rules_dir / "error-patterns.md").exists()


class TestExistingToolsRunnable:
    def test_session_opener_file_exists(self):
        assert (ROOT / "tools" / "session_opener.py").exists()

    def test_quality_scorer_file_exists(self):
        assert (ROOT / "tools" / "quality_scorer.py").exists()

    def test_portfolio_stats_file_exists(self):
        assert (ROOT / "tools" / "portfolio_stats.py").exists()
