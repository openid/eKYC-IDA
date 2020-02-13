from pathlib import Path

REQUEST_EXAMPLES = list(Path(__file__).parent.glob("../examples/request/*.json"))
RESPONSE_EXAMPLES = list(Path(__file__).parent.glob("../examples/response/*.json"))


def pytest_generate_tests(metafunc):
    if "request_example" in metafunc.fixturenames:
        metafunc.parametrize("request_example", REQUEST_EXAMPLES, ids=list(x.name for x in REQUEST_EXAMPLES))
    if "response_example" in metafunc.fixturenames:
        metafunc.parametrize("response_example", RESPONSE_EXAMPLES, ids=list(x.name for x in RESPONSE_EXAMPLES))
