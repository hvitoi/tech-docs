import pytest

# Fixtures defined in conftest.py are auto-discovered by every test
# in this directory (and subdirectories). No import needed.
# You need to inject it in the function signature (see test_conftest.py)


@pytest.fixture
def shared_config():
    return {"env": "test", "debug": True}
