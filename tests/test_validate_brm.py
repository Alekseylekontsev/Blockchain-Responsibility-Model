import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]


def test_all_example_records_match_schema():
    schema = json.loads((ROOT / "schemas/responsibility-record.schema.json").read_text())
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    paths = sorted((ROOT / "examples").glob("**/responsibility-record.yaml"))
    assert paths
    for path in paths:
        errors = list(validator.iter_errors(yaml.safe_load(path.read_text())))
        assert not errors, f"{path}: {[error.message for error in errors]}"
