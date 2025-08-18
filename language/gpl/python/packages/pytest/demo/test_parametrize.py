import pytest

# Parametrized tests (run same test with multiple inputs)


def multiply(a, b):
    return a * b


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (1, 10, 10),
        (0, 99, 0),
    ],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected
