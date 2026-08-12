import json
import datetime
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]


def normalize_yaml_dates(value):
    if isinstance(value, (datetime.date, datetime.datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        return {key: normalize_yaml_dates(item) for key, item in value.items()}
    if isinstance(value, list):
        return [normalize_yaml_dates(item) for item in value]
    return value


def test_all_example_records_match_schema():
    schema = json.loads((ROOT / "schemas/responsibility-record.schema.json").read_text())
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    paths = sorted((ROOT / "examples").glob("**/responsibility-record.yaml"))
    assert paths
    for path in paths:
        record = normalize_yaml_dates(yaml.safe_load(path.read_text()))
        errors = list(validator.iter_errors(record))
        assert not errors, f"{path}: {[error.message for error in errors]}"
