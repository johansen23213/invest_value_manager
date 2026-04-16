"""CLI entry point: python -m orchestrator [command] [args]"""
import asyncio
import sys

from orchestrator.governor import Governor


def main():
    gov = Governor()
    args = sys.argv[1:]

    if not args or args[0] == "--dry-run":
        gov.dry_run()
        return

    command = args[0]

    if command == "on-demand" and len(args) >= 2:
        result = asyncio.run(gov.run_on_demand(args[1]))
        print(f"Result: {result}")
    elif command == "weekly":
        result = asyncio.run(gov.run_weekly())
        print(f"Result: {result}")
    elif command == "daily-monitor":
        result = asyncio.run(gov.run_daily_monitor())
        print(f"Result: {result}")
    else:
        print(f"Unknown command: {command}")
        print("Usage: python -m orchestrator [--dry-run|on-demand TICKER|weekly|daily-monitor]")
        sys.exit(1)


if __name__ == "__main__":
    main()
