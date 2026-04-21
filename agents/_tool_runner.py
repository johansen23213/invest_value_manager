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
    """Run an arbitrary command with arguments via subprocess.

    Args:
        command: The executable to run (e.g. "python3").
        args: List of arguments to pass to the command.
        timeout: Maximum seconds before killing the process.
        cwd: Working directory for the subprocess. Defaults to project root.

    Returns:
        ToolResult with stdout/stderr and success status.
    """
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
        return ToolResult(
            tool=command,
            success=False,
            error=f"Timeout after {timeout}s",
        )
    except FileNotFoundError:
        return ToolResult(
            tool=command,
            success=False,
            error=f"Command not found: {command}",
        )
    except Exception as e:
        return ToolResult(
            tool=command,
            success=False,
            error=str(e),
        )


def run_investment_tool(
    tool_name: str,
    args: list[str],
    timeout: int = 60,
) -> ToolResult:
    """Run one of the project's Python tools located in the tools/ directory.

    Args:
        tool_name: Filename of the tool (e.g. "quality_scorer.py").
        args: Arguments to pass to the tool script.
        timeout: Maximum seconds before killing the process.

    Returns:
        ToolResult with the tool's output.
    """
    tool_path = ROOT / "tools" / tool_name
    if not tool_path.exists():
        return ToolResult(
            tool=tool_name,
            success=False,
            error=f"Tool not found: {tool_path}",
        )
    return run_tool("python3", [str(tool_path)] + args, timeout=timeout)
