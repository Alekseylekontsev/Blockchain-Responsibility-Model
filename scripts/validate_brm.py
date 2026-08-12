import json
import datetime
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

root = Path(__file__).resolve().parents[1]
schema = json.loads((root / "schemas/responsibility-record.schema.json").read_text(encoding="utf-8"))
validator = Draft202012Validator(schema, format_checker=FormatChecker())


def normalize_yaml_dates(value):
    if isinstance(value, (datetime.date, datetime.datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        return {key: normalize_yaml_dates(item) for key, item in value.items()}
    if isinstance(value, list):
        return [normalize_yaml_dates(item) for item in value]
    return value


for path in sorted((root / "examples").glob("**/responsibility-record.yaml")):
    record = normalize_yaml_dates(yaml.safe_load(path.read_text(encoding="utf-8")))
    errors = sorted(validator.iter_errors(record), key=lambda e: list(e.path))
    if errors:
        raise SystemExit("\n".join(f"{path}: {e.message}" for e in errors))
    print(f"valid: {path.relative_to(root)}")
