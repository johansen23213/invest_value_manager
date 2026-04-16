"""Merger arbitrage spread and return calculations."""
from __future__ import annotations
from datetime import date, datetime
from dataclasses import dataclass


@dataclass
class MergerArbResult:
    spread_pct: float
    annualized_spread_pct: float
    expected_return_pct: float
    risk_reward_ratio: float
    days_to_close: int
    downside_pct: float


def calculate_merger_arb(
    current_price: float,
    deal_price: float,
    expected_close_date: str | date,
    break_fee_pct: float = 0.0,
    close_probability_pct: float = 90.0,
) -> MergerArbResult:
    spread_pct = ((deal_price - current_price) / current_price) * 100
    if isinstance(expected_close_date, str):
        expected_close_date = datetime.strptime(expected_close_date, "%Y-%m-%d").date()
    days = (expected_close_date - date.today()).days
    days = max(days, 1)
    annualized = (spread_pct / 100) * (365 / days) * 100
    prob = close_probability_pct / 100
    downside_pct = (
        -((current_price - (current_price * (1 - break_fee_pct / 100))) / current_price) * 100
        if break_fee_pct
        else -spread_pct * 2
    )
    expected_return = prob * spread_pct + (1 - prob) * downside_pct
    risk_reward = abs(spread_pct / downside_pct) if downside_pct != 0 else float("inf")
    return MergerArbResult(
        spread_pct=round(spread_pct, 2),
        annualized_spread_pct=round(annualized, 2),
        expected_return_pct=round(expected_return, 2),
        risk_reward_ratio=round(risk_reward, 2),
        days_to_close=days,
        downside_pct=round(downside_pct, 2),
    )
