"""Tests for agents/_tool_runner.py — subprocess tool invocation."""
from __future__ import annotations

import pathlib

import pytest

from agents._tool_runner import ToolResult, run_investment_tool, run_tool


class TestRunTool:
    def test_successful_command(self):
        result = run_tool("python3", ["-c", "print('hello')"])
        assert result.success is True
        assert result.stdout.strip() == "hello"
        assert result.return_code == 0
        assert result.error is None

    def test_command_with_stderr(self):
        result = run_tool("python3", ["-c", "import sys; sys.stderr.write('warn\\n'); print('ok')"])
        assert result.success is True
        assert result.stdout.strip() == "ok"
        assert "warn" in result.stderr

    def test_nonzero_exit_code(self):
        result = run_tool("python3", ["-c", "import sys; sys.exit(1)"])
        assert result.success is False
        assert result.return_code == 1

    def test_timeout(self):
        result = run_tool("python3", ["-c", "import time; time.sleep(10)"], timeout=1)
        assert result.success is False
        assert result.error is not None
        assert "Timeout" in result.error

    def test_nonexistent_command(self):
        result = run_tool("__nonexistent_command_abc123__", [])
        assert result.success is False
        assert result.error is not None
        assert "not found" in result.error.lower() or "Command not found" in result.error

    def test_custom_cwd(self, tmp_path: pathlib.Path):
        result = run_tool("python3", ["-c", "import os; print(os.getcwd())"], cwd=tmp_path)
        assert result.success is True
        assert tmp_path.name in result.stdout

    def test_tool_result_dataclass(self):
        r = ToolResult(tool="test", success=True, stdout="out", stderr="err", return_code=0)
        assert r.tool == "test"
        assert r.success is True
        assert r.stdout == "out"
        assert r.stderr == "err"
        assert r.return_code == 0
        assert r.error is None


class TestRunInvestmentTool:
    def test_nonexistent_tool(self):
        result = run_investment_tool("__fake_tool_xyz__.py", [])
        assert result.success is False
        assert result.error is not None
        assert "not found" in result.error.lower() or "Tool not found" in result.error

    def test_existing_tool_runs(self):
        """Verify that a real tool from the tools/ directory can be invoked.

        We use price_checker.py with no args — it should at least start
        (may fail due to missing args, but the subprocess itself should run).
        """
        result = run_investment_tool("price_checker.py", ["--help"])
        # The tool may or may not support --help, but the subprocess should
        # at least execute without FileNotFoundError.
        assert result.error is None or "not found" not in result.error.lower()
        assert result.return_code != -1
