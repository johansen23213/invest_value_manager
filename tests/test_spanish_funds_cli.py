"""Tests for the manual CLI trigger."""
from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from scrapers.spanish_funds.cli import main


class TestCLI:
    def test_single_fund_happy_path(self, capsys):
        from scrapers.spanish_funds.pipeline import PipelineResult
        result = PipelineResult(fund_id="cobas", processed=True, quarter="2026-Q1",
                                persisted_path=None)
        with patch("scrapers.spanish_funds.cli.process_scraper", return_value=result), \
             patch("scrapers.spanish_funds.cli._anthropic_client", return_value=MagicMock()):
            code = main(["--fund", "cobas"])
        out = capsys.readouterr().out
        assert code == 0
        assert "cobas" in out
        assert "processed=True" in out or "processed: True" in out

    def test_all_funds_flag(self):
        from scrapers.spanish_funds.pipeline import PipelineResult
        results = [
            PipelineResult(fund_id=f, processed=False, skipped_reason="no_letter_found")
            for f in ("cobas", "azvalor", "magallanes", "horos", "valentum")
        ]
        with patch("scrapers.spanish_funds.cli.process_scraper", side_effect=results), \
             patch("scrapers.spanish_funds.cli._anthropic_client", return_value=MagicMock()):
            code = main(["--all"])
        assert code == 0

    def test_unknown_fund_errors(self):
        # argparse exits with SystemExit(2) on invalid choice
        with pytest.raises(SystemExit):
            main(["--fund", "bestinver"])

    def test_dry_run_skips_persist(self, capsys):
        from scrapers.spanish_funds.pipeline import PipelineResult
        result = PipelineResult(fund_id="cobas", processed=True, quarter="2026-Q1",
                                persisted_path=None)
        with patch("scrapers.spanish_funds.cli.process_scraper", return_value=result) as mock_proc, \
             patch("scrapers.spanish_funds.cli._anthropic_client", return_value=MagicMock()):
            code = main(["--fund", "cobas", "--dry-run"])
        assert code == 0
        # In dry-run we still call process_scraper but pass a tmp kb_root
        assert mock_proc.called
