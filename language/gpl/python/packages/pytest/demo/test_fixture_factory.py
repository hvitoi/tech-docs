import pytest


class User:
    def __init__(self, name, admin=False):
        self.name = name
        self.admin = admin


# A factory fixture returns a function so each test can build
# customized instances instead of getting a single fixed one.
@pytest.fixture
def make_user():
    created = []

    def _make(name="alice", admin=False):
        user = User(name, admin=admin)
        created.append(user)
        return user

    yield _make
    created.clear()  # teardown can clean up everything the test built


def test_default_user(make_user):
    assert make_user().name == "alice"


def test_admin_user(make_user):
    assert make_user(name="bob", admin=True).admin is True
