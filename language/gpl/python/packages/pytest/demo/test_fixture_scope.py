import pytest

# Fixture scopes control how often setup/teardown runs.
# Default is "function" (once per test). Wider scopes share the fixture
# across tests for speed, at the cost of test isolation.


@pytest.fixture(scope="module")
def expensive_resource():
    print("\nsetting up once per module")
    yield {"value": 42}
    print("\ntearing down once per module")


def test_first(expensive_resource):
    assert expensive_resource["value"] == 42


def test_second(expensive_resource):
    # same instance as test_first — setup did NOT run again
    expensive_resource["value"] = 99
    assert expensive_resource["value"] == 99
