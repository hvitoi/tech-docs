# shared_config is defined in conftest.py — no import required.


def test_uses_shared_fixture(shared_config):
    # shared_config receives the result of the execution of shared_config()
    assert shared_config["env"] == "test"
