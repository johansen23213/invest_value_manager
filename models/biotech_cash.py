"""Biotech cash runway and value calculations."""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class BiotechCashResult:
    months_until_zero: float
    net_cash_per_share: float
    total_value_per_share: float
    margin_of_safety_pct: float


def calculate_cash_runway(
    net_cash: float,
    monthly_burn_rate: float,
    shares_outstanding: int,
    current_price: float,
    pipeline_value: float = 0.0,
    cvr_value: float = 0.0,
) -> BiotechCashResult:
    months = net_cash / monthly_burn_rate if monthly_burn_rate > 0 else float("inf")
    cash_ps = net_cash / shares_outstanding if shares_outstanding > 0 else 0
    total_ps = (
        cash_ps
        + (pipeline_value / shares_outstanding if shares_outstanding > 0 else 0)
        + cvr_value
    )
    mos = ((total_ps - current_price) / current_price * 100) if current_price > 0 else 0
    return BiotechCashResult(
        months_until_zero=round(months, 1),
        net_cash_per_share=round(cash_ps, 2),
        total_value_per_share=round(total_ps, 2),
        margin_of_safety_pct=round(mos, 2),
    )
