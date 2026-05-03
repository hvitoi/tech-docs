import pytest

state = {"counter": 0}


# autouse=True applies the fixture to every test in scope without
# the test having to name it as an argument.
@pytest.fixture(autouse=True)
def reset_state():
    state["counter"] = 0
    yield


def test_first():
    state["counter"] += 1
    assert state["counter"] == 1


def test_second():
    # counter was reset between tests by the autouse fixture
    assert state["counter"] == 0
