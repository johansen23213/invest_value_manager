"""Liquidation value calculations with asset haircuts."""
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class LiquidationResult:
    gross_asset_value: float
    total_haircuts: float
    net_after_haircuts: float
    net_liquidation_value: float
    per_share_value: float
    upside_pct: float


def calculate_liquidation_value(
    assets: dict[str, float],
    haircuts: dict[str, float],
    liabilities: float,
    shares_outstanding: int,
    current_price: float = 0.0,
) -> LiquidationResult:
    gross = sum(assets.values())
    haircut_total = sum(assets.get(k, 0) * (v / 100) for k, v in haircuts.items())
    net_after = gross - haircut_total
    net_liq = net_after - liabilities
    per_share = net_liq / shares_outstanding if shares_outstanding > 0 else 0
    upside = ((per_share - current_price) / current_price * 100) if current_price > 0 else 0
    return LiquidationResult(
        gross_asset_value=round(gross, 2),
        total_haircuts=round(haircut_total, 2),
        net_after_haircuts=round(net_after, 2),
        net_liquidation_value=round(net_liq, 2),
        per_share_value=round(per_share, 2),
        upside_pct=round(upside, 2),
    )
