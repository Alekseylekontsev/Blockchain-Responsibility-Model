import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

root = Path(__file__).resolve().parents[1]
schema = json.loads((root / "schemas/responsibility-record.schema.json").read_text(encoding="utf-8"))
validator = Draft202012Validator(schema, format_checker=FormatChecker())
for path in sorted((root / "examples").glob("**/responsibility-record.yaml")):
    errors = sorted(validator.iter_errors(yaml.safe_load(path.read_text(encoding="utf-8"))), key=lambda e: list(e.path))
    if errors:
        raise SystemExit("\n".join(f"{path}: {e.message}" for e in errors))
    print(f"valid: {path.relative_to(root)}")
