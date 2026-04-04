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


def add_additional_properties(schema, _in_conditional=False):
    """
    Add "additionalProperties": False to wherever "properties" is defined in the schema.

    When a schema uses allOf with if/then to conditionally add properties,
    those property names are hoisted into the base "properties" so that
    "additionalProperties" can see them (JSON Schema only considers properties
    defined in the same schema object).

    if/then/else subschemas are not standalone object definitions — they modify
    validation of the parent schema's instance — so additionalProperties: false
    must not be added to them directly. We still recurse into objects nested
    within their "properties" (e.g. then.properties.record is a real object).
    """
    if not isinstance(schema, dict):
        return

    # Hoist property names from allOf if/then branches into base properties,
    # so that additionalProperties: false doesn't reject them.
    if "allOf" in schema and "properties" in schema:
        for branch in schema["allOf"]:
            if "then" in branch and "properties" in branch["then"]:
                for prop_name in branch["then"]["properties"]:
                    if prop_name not in schema["properties"]:
                        schema["properties"][prop_name] = branch["then"]["properties"][prop_name]

    if not _in_conditional and "properties" in schema and "additionalProperties" not in schema:
        schema["additionalProperties"] = False

    # Recurse into all subschema locations
    for key in ("properties", "$defs"):
        if key in schema:
            for _, value in schema[key].items():
                add_additional_properties(value)
    if "items" in schema:
        add_additional_properties(schema["items"])
    # if/then/else are conditional modifiers — don't add additionalProperties
    # to them, but do recurse into nested objects within their properties.
    for key in ("if", "then", "else"):
        if key in schema:
            add_additional_properties(schema[key], _in_conditional=True)
    for key in ("oneOf", "anyOf", "allOf", "not"):
        if key in schema:
            items = schema[key] if isinstance(schema[key], list) else [schema[key]]
            for item in items:
                add_additional_properties(item)


def test_request_schema(request_example):
    data = loads(request_example.read_text().replace("\n", ""))
    schema = loads(REQUEST_SCHEMA.read_text())
    add_additional_properties(schema)
    assert validate(schema=schema, instance=data, registry=registry) is None


def test_response_schema(response_example):
    data = loads(response_example.read_text().replace("\n", ""))
    schema = loads(RESPONSE_SCHEMA.read_text())
    add_additional_properties(schema)
    assert validate(schema=schema, instance=data, registry=registry) is None
