#!/usr/bin/env python3
"""Validate GAVFS sample documents against Draft 2020-12 JSON Schemas."""
import json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

root = Path(__file__).resolve().parents[1]
for path in sorted((root / "schema").glob("*.schema.json")):
    name = path.name.removesuffix(".schema.json")
    schema = json.loads(path.read_text())
    Draft202012Validator.check_schema(schema)
    example = json.loads((root / "examples" / f"{name}.json").read_text())
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(example)
    print(f"PASS {name}")
print("All GAVFS examples validated.")
