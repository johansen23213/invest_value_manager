"""Spin-off stub value calculations."""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class SpinoffResult:
    implied_stub_value: float
    stub_pct_of_parent: float
    parent_ex_spinoff_value: float


def calculate_stub_value(
    parent_price: float,
    spinoff_value_per_parent_share: float,
    parent_standalone_estimate: float = 0.0,
) -> SpinoffResult:
    stub = parent_price - spinoff_value_per_parent_share
    stub_pct = (stub / parent_price * 100) if parent_price > 0 else 0
    parent_ex = parent_standalone_estimate if parent_standalone_estimate > 0 else stub
    return SpinoffResult(
        implied_stub_value=round(stub, 2),
        stub_pct_of_parent=round(stub_pct, 2),
        parent_ex_spinoff_value=round(parent_ex, 2),
    )
