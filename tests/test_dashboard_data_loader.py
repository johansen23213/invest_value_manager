"""Tests for dashboard/data_loader.py."""
from __future__ import annotations

from datetime import date
from pathlib import Path

import pytest

from dashboard.data_loader import (
    load_portfolio,
    load_standing_orders,
    load_universe,
    load_calendar,
    load_spanish_funds,
    project_root,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "dashboard"


class TestProjectRoot:
    def test_project_root_returns_invest_value_manager_dir(self):
        root = project_root()
        assert root.name == "invest_value_manager"
        assert (root / "pyproject.toml").exists()


class TestLoadPortfolio:
    def test_loads_positions_and_cash(self, monkeypatch):
        monkeypatch.setattr(
            "dashboard.data_loader._portfolio_path",
            lambda: FIXTURES / "portfolio_sample.yaml",
        )
        load_portfolio.clear()  # clear cache
        data = load_portfolio()
        assert data is not None
        assert len(data["positions"]) == 1
        assert data["positions"][0]["ticker"] == "MORN"
        assert data["cash_usd"] == 6860.44

    def test_returns_empty_skeleton_when_missing(self, monkeypatch, tmp_path):
        missing = tmp_path / "nope.yaml"
        monkeypatch.setattr("dashboard.data_loader._portfolio_path", lambda: missing)
        load_portfolio.clear()
        data = load_portfolio()
        assert data == {"positions": [], "cash_usd": 0.0}


class TestLoadStandingOrders:
    def test_loads_all_orders(self, monkeypatch):
        monkeypatch.setattr(
            "dashboard.data_loader._standing_orders_path",
            lambda: FIXTURES / "standing_orders_sample.yaml",
        )
        load_standing_orders.clear()
        orders = load_standing_orders()
        assert len(orders) == 2
        tickers = {o["ticker"] for o in orders}
        assert tickers == {"RACE.MI", "ALFA.L"}

    def test_empty_list_when_missing(self, monkeypatch, tmp_path):
        missing = tmp_path / "nope.yaml"
        monkeypatch.setattr("dashboard.data_loader._standing_orders_path", lambda: missing)
        load_standing_orders.clear()
        orders = load_standing_orders()
        assert orders == []


class TestLoadUniverse:
    def test_returns_dataframe_with_expected_columns(self, monkeypatch):
        monkeypatch.setattr(
            "dashboard.data_loader._universe_path",
            lambda: FIXTURES / "quality_universe_sample.yaml",
        )
        load_universe.clear()
        df = load_universe()
        assert len(df) == 2
        for col in ("ticker", "name", "tier", "qs_tool", "pipeline_status", "distance_to_entry"):
            assert col in df.columns

    def test_empty_df_when_missing(self, monkeypatch, tmp_path):
        missing = tmp_path / "nope.yaml"
        monkeypatch.setattr("dashboard.data_loader._universe_path", lambda: missing)
        load_universe.clear()
        df = load_universe()
        assert len(df) == 0


class TestLoadCalendar:
    def test_filters_to_days_window(self, monkeypatch, tmp_path):
        monkeypatch.setattr(
            "dashboard.data_loader._calendar_path",
            lambda: FIXTURES / "calendar_sample.yaml",
        )
        # Pin "today" so the filter is deterministic
        monkeypatch.setattr("dashboard.data_loader._today", lambda: date(2026, 4, 21))
        load_calendar.clear()
        next_7 = load_calendar(days=7)
        assert len(next_7) == 1  # only MEGP.L within 7 days
        assert next_7.iloc[0]["ticker"] == "MEGP.L"

    def test_wider_window_includes_more(self, monkeypatch):
        monkeypatch.setattr(
            "dashboard.data_loader._calendar_path",
            lambda: FIXTURES / "calendar_sample.yaml",
        )
        monkeypatch.setattr("dashboard.data_loader._today", lambda: date(2026, 4, 21))
        load_calendar.clear()
        next_30 = load_calendar(days=30)
        assert len(next_30) == 2  # MEGP.L + ADBE

    def test_empty_when_missing(self, monkeypatch, tmp_path):
        missing = tmp_path / "nope.yaml"
        monkeypatch.setattr("dashboard.data_loader._calendar_path", lambda: missing)
        load_calendar.clear()
        df = load_calendar(days=30)
        assert len(df) == 0


class TestLoadSpanishFunds:
    def test_loads_latest_per_fund(self, monkeypatch):
        monkeypatch.setattr(
            "dashboard.data_loader._spanish_funds_root",
            lambda: FIXTURES / "spanish_funds_sample",
        )
        load_spanish_funds.clear()
        data = load_spanish_funds()
        assert "cobas" in data
        assert "azvalor" in data
        assert data["cobas"]["fund_name"] == "Cobas Selección"
        assert data["azvalor"]["quarter"] == "2026-Q1"

    def test_returns_empty_dict_when_dir_missing(self, monkeypatch, tmp_path):
        missing = tmp_path / "does_not_exist"
        monkeypatch.setattr("dashboard.data_loader._spanish_funds_root", lambda: missing)
        load_spanish_funds.clear()
        assert load_spanish_funds() == {}
