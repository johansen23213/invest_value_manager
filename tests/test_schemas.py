import json
import pathlib
import pytest
from jsonschema import Draft7Validator

SCHEMAS_DIR = pathlib.Path(__file__).resolve().parent.parent / "knowledge_base" / "schemas"
SCHEMA_FILES = sorted(SCHEMAS_DIR.glob("*.schema.json"))

@pytest.mark.parametrize("schema_path", SCHEMA_FILES, ids=lambda p: p.name)
def test_schema_is_valid_draft7(schema_path):
    schema = json.loads(schema_path.read_text())
    Draft7Validator.check_schema(schema)

@pytest.mark.parametrize("schema_path", SCHEMA_FILES, ids=lambda p: p.name)
def test_schema_has_required_metadata(schema_path):
    schema = json.loads(schema_path.read_text())
    assert "$schema" in schema
    assert "$id" in schema
    assert "title" in schema
    assert schema["type"] == "object"

def test_all_12_schemas_exist():
    expected = {
        "company.schema.json", "thesis.schema.json", "decision.schema.json",
        "portfolio_position.schema.json", "closed_position.schema.json",
        "performance.schema.json", "watchlist_entry.schema.json",
        "horos_position.schema.json", "alpha_vulture_idea.schema.json",
        "screener_result.schema.json", "special_situation.schema.json",
        "market_regime.schema.json",
    }
    actual = {p.name for p in SCHEMA_FILES}
    assert expected == actual
