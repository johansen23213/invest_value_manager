import pathlib
import json
import yaml
import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCHEMAS_DIR = ROOT / "knowledge_base" / "schemas"

@pytest.fixture
def schemas_dir():
    return SCHEMAS_DIR

@pytest.fixture
def load_schema():
    def _load(name: str) -> dict:
        path = SCHEMAS_DIR / name
        return json.loads(path.read_text())
    return _load

@pytest.fixture
def load_yaml():
    def _load(rel_path: str):
        path = ROOT / rel_path
        if not path.exists():
            pytest.skip(f"{rel_path} not found")
        return yaml.safe_load(path.read_text())
    return _load
