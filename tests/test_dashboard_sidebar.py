"""Tests for sidebar helpers (share_mode resolution + URL param parsing)."""
from __future__ import annotations

from dashboard.sidebar import resolve_share_mode_from_params


class TestResolveShareMode:
    def test_share_param_1_enables(self):
        assert resolve_share_mode_from_params({"share": "1"}) is True

    def test_share_param_true_enables(self):
        assert resolve_share_mode_from_params({"share": "true"}) is True

    def test_share_param_absent_disables(self):
        assert resolve_share_mode_from_params({}) is False

    def test_share_param_0_disables(self):
        assert resolve_share_mode_from_params({"share": "0"}) is False

    def test_share_param_other_value_disables(self):
        assert resolve_share_mode_from_params({"share": "nope"}) is False
