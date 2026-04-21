"""Tests for special situation financial models."""
import pytest

from models.merger_arb import calculate_merger_arb, MergerArbResult
from models.liquidation import calculate_liquidation_value, LiquidationResult
from models.spinoff import calculate_stub_value, SpinoffResult
from models.biotech_cash import calculate_cash_runway, BiotechCashResult


class TestMergerArb:
    def test_basic_spread(self):
        result = calculate_merger_arb(
            current_price=42.50,
            deal_price=45.00,
            expected_close_date="2026-09-15",
            break_fee_pct=3.5,
            close_probability_pct=90.0,
        )
        assert isinstance(result, MergerArbResult)
        # Spread = (45 - 42.50) / 42.50 * 100 = 5.88%
        assert abs(result.spread_pct - 5.88) < 0.01
        assert result.expected_return_pct > 0
        assert result.days_to_close > 0
        assert result.risk_reward_ratio > 0

    def test_annualized_spread_positive(self):
        result = calculate_merger_arb(
            current_price=42.50,
            deal_price=45.00,
            expected_close_date="2026-09-15",
        )
        assert result.annualized_spread_pct > result.spread_pct

    def test_negative_spread(self):
        result = calculate_merger_arb(
            current_price=50.00,
            deal_price=45.00,
            expected_close_date="2026-09-15",
        )
        assert result.spread_pct < 0

    def test_no_break_fee_doubles_downside(self):
        result = calculate_merger_arb(
            current_price=42.50,
            deal_price=45.00,
            expected_close_date="2026-09-15",
            break_fee_pct=0.0,
        )
        # Without break fee, downside = -spread * 2
        assert abs(result.downside_pct - (-result.spread_pct * 2)) < 0.01

    def test_with_break_fee(self):
        result = calculate_merger_arb(
            current_price=42.50,
            deal_price=45.00,
            expected_close_date="2026-09-15",
            break_fee_pct=3.5,
        )
        assert result.downside_pct == -3.5


class TestLiquidation:
    def test_basic_liquidation(self):
        result = calculate_liquidation_value(
            assets={"cash": 100_000_000, "real_estate": 50_000_000},
            haircuts={"real_estate": 30},
            liabilities=80_000_000,
            shares_outstanding=10_000_000,
            current_price=5.0,
        )
        assert isinstance(result, LiquidationResult)
        # gross = 150M, haircuts = 50M * 0.30 = 15M, net_after = 135M
        # net_liq = 135M - 80M = 55M, per_share = 5.50
        assert result.gross_asset_value == 150_000_000.0
        assert result.total_haircuts == 15_000_000.0
        assert result.net_after_haircuts == 135_000_000.0
        assert result.net_liquidation_value == 55_000_000.0
        assert result.per_share_value == 5.5
        assert result.per_share_value > 0
        assert result.upside_pct == 10.0  # (5.50 - 5.00) / 5.00 * 100

    def test_zero_shares(self):
        result = calculate_liquidation_value(
            assets={"cash": 100},
            haircuts={},
            liabilities=50,
            shares_outstanding=0,
        )
        assert result.per_share_value == 0

    def test_no_haircuts(self):
        result = calculate_liquidation_value(
            assets={"cash": 100},
            haircuts={},
            liabilities=50,
            shares_outstanding=10,
        )
        assert result.total_haircuts == 0
        assert result.per_share_value == 5.0


class TestSpinoff:
    def test_basic_stub(self):
        result = calculate_stub_value(
            parent_price=100.0,
            spinoff_value_per_parent_share=40.0,
        )
        assert isinstance(result, SpinoffResult)
        assert result.implied_stub_value == 60.0
        assert result.stub_pct_of_parent == 60.0
        # No standalone estimate, so parent_ex = stub
        assert result.parent_ex_spinoff_value == 60.0

    def test_with_standalone_estimate(self):
        result = calculate_stub_value(
            parent_price=100.0,
            spinoff_value_per_parent_share=40.0,
            parent_standalone_estimate=75.0,
        )
        assert result.implied_stub_value == 60.0
        assert result.parent_ex_spinoff_value == 75.0

    def test_zero_parent_price(self):
        result = calculate_stub_value(
            parent_price=0.0,
            spinoff_value_per_parent_share=40.0,
        )
        assert result.stub_pct_of_parent == 0


class TestBiotechCash:
    def test_basic_runway(self):
        result = calculate_cash_runway(
            net_cash=120_000_000,
            monthly_burn_rate=5_000_000,
            shares_outstanding=10_000_000,
            current_price=8.0,
        )
        assert isinstance(result, BiotechCashResult)
        assert result.months_until_zero == 24.0
        assert result.net_cash_per_share == 12.0
        # total_value_per_share = 12.0 (no pipeline, no CVR)
        assert result.total_value_per_share == 12.0
        # MoS = (12 - 8) / 8 * 100 = 50%
        assert result.margin_of_safety_pct == 50.0

    def test_with_pipeline_and_cvr(self):
        result = calculate_cash_runway(
            net_cash=120_000_000,
            monthly_burn_rate=5_000_000,
            shares_outstanding=10_000_000,
            current_price=8.0,
            pipeline_value=30_000_000,
            cvr_value=2.0,
        )
        # cash_ps=12, pipeline_ps=3, cvr=2 → total=17
        assert result.total_value_per_share == 17.0
        # MoS = (17 - 8) / 8 * 100 = 112.5%
        assert result.margin_of_safety_pct == 112.5

    def test_zero_burn_rate(self):
        result = calculate_cash_runway(
            net_cash=120_000_000,
            monthly_burn_rate=0,
            shares_outstanding=10_000_000,
            current_price=8.0,
        )
        assert result.months_until_zero == float("inf")

    def test_zero_shares(self):
        result = calculate_cash_runway(
            net_cash=120_000_000,
            monthly_burn_rate=5_000_000,
            shares_outstanding=0,
            current_price=8.0,
        )
        assert result.net_cash_per_share == 0
