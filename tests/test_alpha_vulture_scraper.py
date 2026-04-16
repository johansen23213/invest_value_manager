"""Tests for the Alpha Vulture scraper — RSS parsing, HTML parsing, and schema validation."""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import pytest

from scrapers.alpha_vulture_scraper import (
    _classify_situation,
    _extract_return,
    _extract_ticker,
    build_idea,
    parse_post_html,
    parse_rss_feed,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures"
SCHEMAS = Path(__file__).resolve().parent.parent / "knowledge_base" / "schemas"


@pytest.fixture
def rss_xml() -> str:
    return (FIXTURES / "alpha_vulture_rss.xml").read_text()


@pytest.fixture
def post_html() -> str:
    return (FIXTURES / "alpha_vulture_post.html").read_text()


@pytest.fixture
def alpha_vulture_schema() -> dict:
    return json.loads(
        (SCHEMAS / "alpha_vulture_idea.schema.json").read_text()
    )


# ---------------------------------------------------------------------------
# TestParseRSS
# ---------------------------------------------------------------------------

class TestParseRSS:
    def test_parses_two_items(self, rss_xml: str):
        items = parse_rss_feed(rss_xml)
        assert len(items) == 2

    def test_first_item_title(self, rss_xml: str):
        items = parse_rss_feed(rss_xml)
        assert items[0]["title"] == "Interesting merger arbitrage: ACME Corp acquisition by BigCo"

    def test_first_item_url(self, rss_xml: str):
        items = parse_rss_feed(rss_xml)
        assert items[0]["url"] == "https://alphavulture.com/2026/03/15/acme-corp-merger-arb/"

    def test_first_item_pub_date(self, rss_xml: str):
        items = parse_rss_feed(rss_xml)
        assert items[0]["pub_date"] == "2026-03-15"

    def test_first_item_description(self, rss_xml: str):
        items = parse_rss_feed(rss_xml)
        assert "ACME Corp" in items[0]["description"]

    def test_second_item_url(self, rss_xml: str):
        items = parse_rss_feed(rss_xml)
        assert "bustedbio" in items[1]["url"]


# ---------------------------------------------------------------------------
# TestParsePostHTML
# ---------------------------------------------------------------------------

class TestParsePostHTML:
    def test_extracts_title(self, post_html: str):
        data = parse_post_html(post_html, "https://alphavulture.com/test")
        assert "ACME Corp" in data["title"]

    def test_extracts_ticker(self, post_html: str):
        data = parse_post_html(post_html, "https://alphavulture.com/test")
        assert data["ticker"] == "ACME"

    def test_detects_merger_arb(self, post_html: str):
        data = parse_post_html(post_html, "https://alphavulture.com/test")
        assert data["situation_type"] == "MERGER_ARB"

    def test_extracts_expected_return(self, post_html: str):
        data = parse_post_html(post_html, "https://alphavulture.com/test")
        assert data["expected_return_pct"] == pytest.approx(5.9)

    def test_extracts_pub_date(self, post_html: str):
        data = parse_post_html(post_html, "https://alphavulture.com/test")
        assert data["pub_date"] == "2026-03-15"

    def test_thesis_summary_max_500_chars(self, post_html: str):
        data = parse_post_html(post_html, "https://alphavulture.com/test")
        assert data["thesis_summary"] is not None
        assert len(data["thesis_summary"]) <= 500


# ---------------------------------------------------------------------------
# TestClassifySituation
# ---------------------------------------------------------------------------

class TestClassifySituation:
    def test_merger_arb(self):
        assert _classify_situation("definitive agreement to merge") == "MERGER_ARB"

    def test_liquidation(self):
        assert _classify_situation("plan of dissolution announced") == "LIQUIDATION"

    def test_spinoff(self):
        assert _classify_situation("spin-off expected in Q2") == "SPINOFF"

    def test_net_cash(self):
        assert _classify_situation("trading below cash value") == "NET_CASH"

    def test_other(self):
        assert _classify_situation("nothing special here") == "OTHER"


# ---------------------------------------------------------------------------
# TestExtractTicker
# ---------------------------------------------------------------------------

class TestExtractTicker:
    def test_parenthetical(self):
        assert _extract_ticker("Company (ACME) is great") == "ACME"

    def test_exchange_prefix(self):
        assert _extract_ticker("Listed (NYSE: GOOG) on exchange") == "GOOG"

    def test_ticker_colon(self):
        assert _extract_ticker("ticker: MSFT announced results") == "MSFT"

    def test_no_match(self):
        assert _extract_ticker("no ticker here") is None


# ---------------------------------------------------------------------------
# TestExtractReturn
# ---------------------------------------------------------------------------

class TestExtractReturn:
    def test_expected_return(self):
        assert _extract_return("Expected return: 5.9% absolute") == pytest.approx(5.9)

    def test_spread_of(self):
        assert _extract_return("spread of 3.2% to deal price") == pytest.approx(3.2)

    def test_spread_approximately(self):
        assert _extract_return("spread approximately 5.9%") == pytest.approx(5.9)

    def test_no_match(self):
        assert _extract_return("no return info") is None


# ---------------------------------------------------------------------------
# TestSchemaValidation
# ---------------------------------------------------------------------------

class TestSchemaValidation:
    def test_complete_idea_validates(self, rss_xml: str, post_html: str, alpha_vulture_schema: dict):
        rss_items = parse_rss_feed(rss_xml)
        post_data = parse_post_html(post_html, rss_items[0]["url"])
        idea = build_idea(rss_items[0], post_data)

        # Should not raise
        jsonschema.validate(instance=idea, schema=alpha_vulture_schema)

    def test_idea_has_required_fields(self, rss_xml: str, post_html: str):
        rss_items = parse_rss_feed(rss_xml)
        post_data = parse_post_html(post_html, rss_items[0]["url"])
        idea = build_idea(rss_items[0], post_data)

        assert idea["post_date"] is not None
        assert idea["title"] != ""
        assert idea["situation_type"] in [
            "MERGER_ARB", "LIQUIDATION", "SPINOFF", "NET_CASH",
            "ODD_LOT", "CVR", "TENDER_OFFER", "RIGHTS_OFFERING",
            "STUB", "OTHER",
        ]
        assert idea["source_url"].startswith("https://")

    def test_idea_source_is_alpha_vulture(self, rss_xml: str, post_html: str):
        rss_items = parse_rss_feed(rss_xml)
        post_data = parse_post_html(post_html, rss_items[0]["url"])
        idea = build_idea(rss_items[0], post_data)
        assert idea["source"] == "ALPHA_VULTURE_BLOG"
