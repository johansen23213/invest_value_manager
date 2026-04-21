"""Tests for notifications — formatters and TelegramNotifier."""
import pytest

from notifications.formatters import format_weekly_digest, format_daily_digest, format_on_demand
from notifications.telegram import TelegramNotifier


class TestFormatWeeklyDigest:
    def test_contains_candidates(self):
        result = {
            "screening": {"total_candidates": 5, "top_tickers": ["AAPL", "MSFT"]},
            "decisions": [{"ticker": "AAPL", "decision": "BUY", "conviction": 8}],
            "total_tokens": 12000,
        }
        msg = format_weekly_digest(result)
        assert "Candidates screened: 5" in msg
        assert "AAPL" in msg
        assert "BUY" in msg
        assert "12,000" in msg

    def test_no_decisions(self):
        result = {"screening": {"total_candidates": 0, "top_tickers": []}, "decisions": [], "total_tokens": 0}
        msg = format_weekly_digest(result)
        assert "No actionable decisions" in msg


class TestFormatDailyDigest:
    def test_contains_positions(self):
        result = {
            "data": {
                "portfolio_summary": {"total_positions": 11, "net_pnl_pct": 3.5, "positions_on_track": 8, "positions_drifting": 2, "positions_alert": 1},
                "action_items": ["Review AAPL thesis"],
                "summary": "Mostly on track.",
            }
        }
        msg = format_daily_digest(result)
        assert "Positions: 11" in msg
        assert "3.5%" in msg
        assert "Review AAPL thesis" in msg

    def test_no_actions(self):
        result = {"data": {"portfolio_summary": {"total_positions": 0, "net_pnl_pct": 0, "positions_on_track": 0, "positions_drifting": 0, "positions_alert": 0}, "action_items": [], "summary": ""}}
        msg = format_daily_digest(result)
        assert "Positions: 0" in msg


class TestFormatOnDemand:
    def test_contains_agents(self):
        result = {
            "ticker": "GOOG",
            "agents": {"a21": {"success": True}, "a23": {"success": True}, "a24": {"success": False}},
            "all_succeeded": False,
            "total_tokens": 5000,
        }
        msg = format_on_demand(result)
        assert "GOOG" in msg
        assert "a21" in msg
        assert "5,000" in msg


class TestTelegramNotifier:
    def test_is_configured_false_without_env(self):
        notifier = TelegramNotifier(bot_token="", chat_id="")
        assert notifier.is_configured is False

    def test_is_configured_true_with_values(self):
        notifier = TelegramNotifier(bot_token="123:ABC", chat_id="456")
        assert notifier.is_configured is True

    async def test_send_returns_false_when_unconfigured(self):
        notifier = TelegramNotifier(bot_token="", chat_id="")
        result = await notifier.send("test")
        assert result is False

    async def test_send_weekly_returns_false_when_unconfigured(self):
        notifier = TelegramNotifier(bot_token="", chat_id="")
        result = await notifier.send_weekly_digest(
            {"screening": {"total_candidates": 0, "top_tickers": []}, "decisions": [], "total_tokens": 0}
        )
        assert result is False

    async def test_send_daily_returns_false_when_unconfigured(self):
        notifier = TelegramNotifier(bot_token="", chat_id="")
        result = await notifier.send_daily_digest(
            {"data": {"portfolio_summary": {}, "action_items": [], "summary": ""}}
        )
        assert result is False

    async def test_send_on_demand_returns_false_when_unconfigured(self):
        notifier = TelegramNotifier(bot_token="", chat_id="")
        result = await notifier.send_on_demand(
            {"ticker": "X", "agents": {}, "all_succeeded": True, "total_tokens": 0}
        )
        assert result is False
