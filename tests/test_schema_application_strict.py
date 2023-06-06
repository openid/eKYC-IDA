"""
The difference to test_schema_application.py is that this test is strict,
meaning that it will fail if there are any additional properties in the JSON
that are not defined in the schema.
"""


from jsonschema import validate
from jsonschema import RefResolver
from json import loads
from pathlib import Path

SCHEMA_PATH = Path(__file__).parent.parent / 'schema'
REQUEST_SCHEMA = SCHEMA_PATH / 'verified_claims_request.json'
RESPONSE_SCHEMA = SCHEMA_PATH / 'verified_claims.json'

schema_store = {}
for schema in SCHEMA_PATH.glob('*.json'):
    schema_loaded = loads(schema.read_text())

    schema_store[schema_loaded["$id"]] = schema_loaded

def get_relative_path_resolver(schema):
    return RefResolver.from_schema(schema, store=schema_store)

"""
Add "additionalProperties": False to whereever "properties" is defined in the schema
"""
def add_additional_properties(schema):
    if "properties" in schema:
        schema["additionalProperties"] = False
        for _, value in schema["properties"].items():
            add_additional_properties(value)
    elif "items" in schema:
        add_additional_properties(schema["items"])

def test_request_schema(request_example):
    data = loads(request_example.read_text().replace("\n", ""))
    schema = loads(REQUEST_SCHEMA.read_text())
    add_additional_properties(schema)
    assert validate(schema=schema, instance=data, resolver=get_relative_path_resolver(schema)) is None


def test_response_schema(response_example):
    data = loads(response_example.read_text().replace("\n", ""))
    schema = loads(RESPONSE_SCHEMA.read_text())
    add_additional_properties(schema)
    assert validate(schema=schema, instance=data, resolver=get_relative_path_resolver(schema)) is None
