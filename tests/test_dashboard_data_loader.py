"""Tests for dashboard/data_loader.py."""
from __future__ import annotations

from pathlib import Path

import pytest

from dashboard.data_loader import (
    load_portfolio,
    load_standing_orders,
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
