"""
The difference to test_schema_application.py is that this test is strict,
meaning that it will fail if there are any additional properties in the JSON
that are not defined in the schema.
"""

from jsonschema import validate
from json import loads
from pathlib import Path
from referencing import Registry

SCHEMA_PATH = Path(__file__).parent.parent / 'schema'
REQUEST_SCHEMA = SCHEMA_PATH / 'verified_claims_request.json'
RESPONSE_SCHEMA = SCHEMA_PATH / 'verified_claims.json'

schema_store = []
for schema in SCHEMA_PATH.glob('*.json'):
    schema_loaded = loads(schema.read_text())
    to_add = (schema_loaded["$id"], schema_loaded)
    schema_store.append(to_add)

registry = Registry().with_contents(pairs=schema_store)


def add_strict_object_validation(schema, _in_conditional=False):
    """
    Add "unevaluatedProperties": False to object schemas that define "properties".

    Unlike additionalProperties, unevaluatedProperties works correctly with
    allOf/if/then, so evidence-type-specific properties remain scoped to the
    matching branch and wrong-variant properties are still rejected.

    if/then/else subschemas are conditional modifiers for the parent instance,
    so strictness must not be added to them directly. We still recurse into
    objects nested within their "properties" (e.g. then.properties.record is a
    real object schema).
    """
    if not isinstance(schema, dict):
        return

    if (
        not _in_conditional
        and "properties" in schema
        and "additionalProperties" not in schema
        and "unevaluatedProperties" not in schema
    ):
        schema["unevaluatedProperties"] = False

    # Recurse into all subschema locations
    for key in ("properties", "$defs"):
        if key in schema:
            for _, value in schema[key].items():
                add_strict_object_validation(value)
    if "items" in schema:
        add_strict_object_validation(schema["items"])
    # if/then/else are conditional modifiers — don't add additionalProperties
    # to them, but do recurse into nested objects within their properties.
    for key in ("if", "then", "else"):
        if key in schema:
            add_strict_object_validation(schema[key], _in_conditional=True)
    for key in ("oneOf", "anyOf", "allOf", "not"):
        if key in schema:
            items = schema[key] if isinstance(schema[key], list) else [schema[key]]
            for item in items:
                add_strict_object_validation(item)


def test_request_schema(request_example):
    data = loads(request_example.read_text().replace("\n", ""))
    schema = loads(REQUEST_SCHEMA.read_text())
    add_strict_object_validation(schema)
    assert validate(schema=schema, instance=data, registry=registry) is None


def test_response_schema(response_example):
    data = loads(response_example.read_text().replace("\n", ""))
    schema = loads(RESPONSE_SCHEMA.read_text())
    add_strict_object_validation(schema)
    assert validate(schema=schema, instance=data, registry=registry) is None
