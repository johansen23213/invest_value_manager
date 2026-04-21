"""Tests for dashboard components: COLOR contract + formatters + share_mode."""
from __future__ import annotations

import pytest

from dashboard.components import (
    COLOR,
    CONVICTION_COLORS,
    PIPELINE_COLORS,
    TIER_COLORS,
    is_hex_color,
    money,
    pct,
    pct_of_portfolio,
)


class TestColorContract:
    def test_color_keys_complete(self):
        expected = {"urgent_red", "positive_green", "warning_amber", "info_blue",
                    "neutral_grey", "tier_a_gold", "muted"}
        assert set(COLOR.keys()) == expected

    def test_all_colors_are_valid_hex(self):
        for name, value in COLOR.items():
            assert is_hex_color(value), f"{name} = {value} is not valid hex"

    def test_pipeline_colors_all_valid(self):
        expected_stages = {"R1_NEW", "R1_COMPLETE", "R2", "R3", "R4_READY", "ACTIVE", "ARCHIVED"}
        assert set(PIPELINE_COLORS.keys()) == expected_stages
        for stage, color in PIPELINE_COLORS.items():
            assert is_hex_color(color), f"{stage} color {color} invalid"

    def test_conviction_colors_three_levels(self):
        assert set(CONVICTION_COLORS.keys()) == {"1_fund", "2_funds", "3+_funds"}
        for level, color in CONVICTION_COLORS.items():
            assert is_hex_color(color)

    def test_tier_colors_abc(self):
        assert set(TIER_COLORS.keys()) == {"A", "B", "C"}
        for tier, color in TIER_COLORS.items():
            assert is_hex_color(color)


class TestIsHexColor:
    def test_valid_6_digit(self):
        assert is_hex_color("#3FA34D")

    def test_valid_3_digit(self):
        assert is_hex_color("#abc")

    def test_missing_hash(self):
        assert not is_hex_color("3FA34D")

    def test_bad_char(self):
        assert not is_hex_color("#3FA34Z")

    def test_wrong_length(self):
        assert not is_hex_color("#3FA34")


class TestMoney:
    def test_share_mode_off_returns_euro(self):
        assert money(10500, share_mode=False) == "€10,500"

    def test_share_mode_on_returns_dash(self):
        assert money(10500, share_mode=True) == "—"

    def test_zero_value_share_mode_off(self):
        assert money(0, share_mode=False) == "€0"

    def test_large_value_formatting(self):
        assert money(1_234_567, share_mode=False) == "€1,234,567"

    def test_negative_value(self):
        assert money(-500, share_mode=False) == "€-500"


class TestPctOfPortfolio:
    def test_basic(self):
        assert pct_of_portfolio(500, 10000) == "5.0%"

    def test_one_decimal(self):
        assert pct_of_portfolio(123, 10000) == "1.2%"

    def test_zero_total_returns_zero(self):
        assert pct_of_portfolio(100, 0) == "0.0%"


class TestPct:
    def test_positive_signed(self):
        assert pct(4.2) == "+4.2%"

    def test_negative_signed(self):
        assert pct(-2.5) == "-2.5%"

    def test_zero_signed_positive(self):
        assert pct(0) == "+0.0%"
