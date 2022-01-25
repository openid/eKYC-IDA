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

def test_request_schema(request_example):
    data = loads(request_example.read_text().replace("\n", ""))
    schema = loads(REQUEST_SCHEMA.read_text())
    assert validate(schema=schema, instance=data, resolver=get_relative_path_resolver(schema)) is None


def test_response_schema(response_example):
    data = loads(response_example.read_text().replace("\n", ""))
    schema = loads(RESPONSE_SCHEMA.read_text())

    assert validate(schema=schema, instance=data, resolver=get_relative_path_resolver(schema)) is None
