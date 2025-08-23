import pytest


class Database:
    def __init__(self):
        self.connected = False

    def connect(self):
        self.connected = True

    def close(self):
        self.connected = False


# Fixtures allow you to set up something before and after your tests.
@pytest.fixture
def db():
    db = Database()
    db.connect()
    yield db  # code before yield runs before the test, code after yield runs after test
    db.close()


def test_db_connection(db):
    assert db.connected is True
