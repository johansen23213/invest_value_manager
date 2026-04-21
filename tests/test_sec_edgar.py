"""Tests for SEC EDGAR RSS watcher and PR Newswire stub."""
import json
import pathlib
import pytest

from scrapers.sec_edgar_rss import EdgarRSSWatcher, SITUATION_KEYWORDS
from scrapers.pr_newswire import PRNewswireWatcher

FIXTURES = pathlib.Path(__file__).parent / "fixtures"


class TestEdgarClassify:
    """Test the _classify method of EdgarRSSWatcher."""

    def setup_method(self):
        self.watcher = EdgarRSSWatcher.__new__(EdgarRSSWatcher)

    def test_merger_keyword(self):
        assert self.watcher._classify("merger agreement", "") == "MERGER_ARB"

    def test_acquisition_keyword(self):
        assert self.watcher._classify("acquisition", "Acme Corp") == "MERGER_ARB"

    def test_definitive_agreement(self):
        assert self.watcher._classify("definitive agreement", "") == "MERGER_ARB"

    def test_liquidation_keyword(self):
        assert self.watcher._classify("plan of dissolution", "") == "LIQUIDATION"

    def test_wind_down(self):
        assert self.watcher._classify("wind down", "") == "LIQUIDATION"

    def test_spinoff_keyword(self):
        assert self.watcher._classify("spin-off", "") == "SPINOFF"

    def test_tender_offer(self):
        assert self.watcher._classify("tender offer", "Big Corp") == "TENDER_OFFER"

    def test_rights_offering(self):
        assert self.watcher._classify("rights offering", "") == "RIGHTS_OFFERING"

    def test_unknown_returns_other(self):
        assert self.watcher._classify("quarterly report", "Boring Inc") == "OTHER"

    def test_title_contributes_to_classification(self):
        # keyword alone is generic, but title contains spin-off
        assert self.watcher._classify("form filed", "spin-off announcement") == "SPINOFF"


class TestEdgarParseResponse:
    """Test _parse_response with fixture data."""

    def setup_method(self):
        self.watcher = EdgarRSSWatcher.__new__(EdgarRSSWatcher)

    def test_parse_fixture(self):
        fixture_path = FIXTURES / "edgar_search_sample.json"
        text = fixture_path.read_text()
        results = self.watcher._parse_response(text, "merger")
        assert len(results) == 2

        # First result
        assert results[0]["filing_type"] == "8-K"
        assert results[0]["company"] == "Acme Corp"
        assert results[0]["cik"] == "0001234567"
        assert results[0]["filed_date"] == "2026-04-10"
        assert "sec.gov" in results[0]["url"]

        # Second result
        assert results[1]["filing_type"] == "SC 14D9"
        assert results[1]["company"] == "Widget Industries Inc"
        assert results[1]["filed_date"] == "2026-04-09"

    def test_parse_classifies_correctly(self):
        fixture_path = FIXTURES / "edgar_search_sample.json"
        text = fixture_path.read_text()
        # "acquisition" keyword should classify as MERGER_ARB
        results = self.watcher._parse_response(text, "acquisition")
        assert all(r["situation_type"] == "MERGER_ARB" for r in results)

    def test_parse_invalid_json(self):
        results = self.watcher._parse_response("not json at all", "merger")
        assert results == []

    def test_parse_empty_hits(self):
        text = json.dumps({"hits": {"hits": []}})
        results = self.watcher._parse_response(text, "merger")
        assert results == []

    def test_parse_missing_display_names(self):
        text = json.dumps(
            {
                "hits": {
                    "hits": [
                        {
                            "_source": {
                                "form_type": "8-K",
                                "entity_id": "123",
                                "file_date": "2026-01-01",
                            }
                        }
                    ]
                }
            }
        )
        results = self.watcher._parse_response(text, "merger")
        assert len(results) == 1
        assert results[0]["company"] == "Unknown"


class TestEdgarSearchResult:
    def test_to_dict(self):
        from scrapers.sec_edgar_rss import EdgarSearchResult

        result = EdgarSearchResult(
            filing_type="8-K",
            company="Test Co",
            cik="000123",
            filed_date="2026-04-01",
            title="Test Filing",
            url="https://sec.gov/test",
            situation_type="MERGER_ARB",
        )
        d = result.to_dict()
        assert d["filing_type"] == "8-K"
        assert d["company"] == "Test Co"
        assert d["situation_type"] == "MERGER_ARB"


class TestPRNewswireWatcher:
    def test_returns_list(self):
        watcher = PRNewswireWatcher()
        result = watcher.search()
        assert isinstance(result, list)
        assert result == []

    def test_accepts_keywords(self):
        watcher = PRNewswireWatcher()
        result = watcher.search(keywords=["merger", "acquisition"], days_back=14)
        assert isinstance(result, list)
        assert result == []
