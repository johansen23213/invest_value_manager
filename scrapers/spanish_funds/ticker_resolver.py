"""Validate LLM-proposed tickers against yfinance.

Each position arrives with ticker_status='unverified'. This module calls
yfinance; if .info.longName is present, we mark verified. Otherwise we
leave unverified. Ambiguous is reserved for future fuzzy-search flow.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Literal

import yfinance as yf

logger = logging.getLogger("valuehunter.spanish_funds.ticker_resolver")

Status = Literal["verified", "unverified", "ambiguous"]


@dataclass(frozen=True)
class TickerResolution:
    ticker: str
    status: Status
    resolved_name: str | None


def resolve_ticker(ticker: str) -> TickerResolution:
    if not ticker:
        return TickerResolution(ticker=ticker, status="unverified", resolved_name=None)
    try:
        info = yf.Ticker(ticker).info
    except Exception as e:
        logger.warning("yfinance error for %s: %s", ticker, e)
        return TickerResolution(ticker=ticker, status="unverified", resolved_name=None)
    name = info.get("longName") if isinstance(info, dict) else None
    if name:
        return TickerResolution(ticker=ticker, status="verified", resolved_name=name)
    return TickerResolution(ticker=ticker, status="unverified", resolved_name=None)


def resolve_positions(positions: list[dict]) -> list[dict]:
    """Mutate-in-place style (returns the list too). Sets ticker_status."""
    for p in positions:
        r = resolve_ticker(p.get("ticker", ""))
        p["ticker_status"] = r.status
    return positions
