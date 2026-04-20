"""Abstract base class for Spanish fund scrapers.

Subclasses implement `get_latest_letter()` for URL detection.
All downstream processing is shared via the pipeline functions.
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

ALLOWED_FUND_IDS = frozenset({"cobas", "azvalor", "magallanes", "horos", "valentum"})


@dataclass(frozen=True)
class LetterMeta:
    """Metadata about a quarterly letter available for download."""
    url: str
    quarter: str            # e.g. "2026-Q1"
    content_hash: str       # SHA256 of the PDF bytes (pre-download if HEAD ETag, else post-download)


class FundScraper(ABC):
    """Abstract base. Subclasses set fund_id/fund_name and implement get_latest_letter."""

    fund_id: str = ""
    fund_name: str = ""

    def __init__(self) -> None:
        if self.fund_id not in ALLOWED_FUND_IDS:
            raise ValueError(f"fund_id {self.fund_id!r} not in {sorted(ALLOWED_FUND_IDS)}")

    @abstractmethod
    def get_latest_letter(self) -> LetterMeta | None:
        """Return metadata for the most recent letter, or None if no letter found."""
        ...
