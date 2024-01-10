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


def test_request_schema(request_example):
    data = loads(request_example.read_text().replace("\n", ""))
    loaded_schema = loads(REQUEST_SCHEMA.read_text())
    assert validate(schema=loaded_schema, instance=data, registry=registry) is None


def test_response_schema(response_example):
    data = loads(response_example.read_text().replace("\n", ""))
    loaded_schema = loads(RESPONSE_SCHEMA.read_text())

    assert validate(schema=loaded_schema, instance=data, registry=registry) is None
