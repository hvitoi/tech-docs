from config import API_BASE_URL, TIMEOUT


def test_defaults():
    assert API_BASE_URL.startswith("https://")
    assert TIMEOUT > 0
