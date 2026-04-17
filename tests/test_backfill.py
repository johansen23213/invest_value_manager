"""Tests for scripts.backfill_performance — performance metrics backfill."""
import json
import pathlib
import pytest
import yaml

from scripts.backfill_performance import backfill, ROOT


class TestBackfill:
    def test_backfill_produces_valid_output(self):
        """backfill() should return dict with required performance fields."""
        result = backfill()
        # If history.yaml has closed positions, validate fields
        if "error" not in result:
            assert "as_of_date" in result
            assert "total_return_pct" in result
            assert "hit_rate_pct" in result
            assert "avg_return_pct" in result
            assert "avg_winner_pct" in result
            assert "avg_loser_pct" in result
            assert "total_positions_closed" in result
            assert isinstance(result["total_positions_closed"], int)

    def test_backfill_schema_compliant(self, load_schema):
        """Output should comply with performance.schema.json."""
        import jsonschema
        result = backfill()
        if "error" in result:
            pytest.skip("No portfolio history available")
        schema = load_schema("performance.schema.json")
        jsonschema.validate(result, schema)

    def test_backfill_writes_file(self, tmp_path):
        """Verify performance.json is written when history exists."""
        output_path = ROOT / "knowledge_base" / "portfolio" / "performance.json"
        result = backfill()
        if "error" in result:
            pytest.skip("No portfolio history available")
        assert output_path.exists()
        data = json.loads(output_path.read_text())
        assert data["as_of_date"] == result["as_of_date"]

    def test_backfill_hit_rate_range(self):
        """Hit rate should be between 0 and 100."""
        result = backfill()
        if "error" in result:
            pytest.skip("No portfolio history available")
        assert 0 <= result["hit_rate_pct"] <= 100

    def test_backfill_closed_count_positive(self):
        """Should have at least 1 closed position if not error."""
        result = backfill()
        if "error" in result:
            pytest.skip("No portfolio history available")
        assert result["total_positions_closed"] > 0
