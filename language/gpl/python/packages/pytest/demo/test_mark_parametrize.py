# %%
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


# %%

# Stacked @parametrize creates the cartesian product of parameter sets.
# `ids` gives each case a readable name in the test output.


@pytest.mark.parametrize("x", [1, 2], ids=["one", "two"])
@pytest.mark.parametrize("y", ["a", "b"])
def test_cartesian(x, y):
    # runs 4 times: (1,a) (1,b) (2,a) (2,b)
    assert isinstance(x, int)
    assert isinstance(y, str)


@pytest.mark.parametrize(
    "n,expected",
    [
        pytest.param(2, 4, id="squared-2"),
        pytest.param(3, 9, id="squared-3"),
        pytest.param(0, 1, id="known-bug", marks=pytest.mark.xfail),
    ],
)
def test_square(n, expected):
    assert n * n == expected
