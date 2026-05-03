import pytest

# Fixtures defined in conftest.py are auto-discovered by every test
# in this directory (and subdirectories). No import needed.


@pytest.fixture
def shared_config():
    return {"env": "test", "debug": True}
