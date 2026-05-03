import os


# monkeypatch sets env vars, attributes, or dict items for the
# duration of one test and reverts them automatically afterwards.


def get_api_key():
    return os.environ.get("API_KEY", "missing")


def test_env_var(monkeypatch):
    monkeypatch.setenv("API_KEY", "secret")
    assert get_api_key() == "secret"


def test_env_var_was_reverted():
    # change from previous test does not leak into this one
    assert get_api_key() == "missing"


class Clock:
    @staticmethod
    def now():
        return "real-time"


def test_patch_attribute(monkeypatch):
    monkeypatch.setattr(Clock, "now", staticmethod(lambda: "frozen"))
    assert Clock.now() == "frozen"
