# Accepts expressions only

# %%
assert 1 + 1 == 3  # AssertionError: (no description)
assert 1 + 1 == 3, "math is broken"  # AssertionError: math is broken


# %%

# testa a identidade do objeto (se aponta exatamente para o objeto singleton None)
assert [] == None  # Throws! Although both are falsy, they are different objects
assert {} is {}  # Throws! Different objects

# Asserting constant literals is not recommended
assert 5 is 5  # literals (not objects) are equal (this behavior is not guaranteed!)
assert "foo" is "foo"

# %%
assert True  # Truthy
assert [0]  # Truthy

assert []  # Falsy
assert {}  # Falsy
assert ()  # Falsy
assert set()  # Falsy
assert range(0)  # Falsy
assert ""  # Falsy
assert 0  # Falsy
assert None  # Falsy
assert False  # Falsy

# %%
# `assert` is stripped when Python is run with -O (optimized).
# Never use assert for runtime validation of user input or security checks.
# Use it for invariants that must hold if the code is correct.


def withdraw(amount):
    """Wrong, assert is skipped under -O"""
    assert amount > 0  # bypassable!


def withdraw_(amount):
    """Correct"""
    if amount <= 0:
        raise ValueError("amount must be positive")


# %%
# Another gotcha: `assert (x, y)` always passes (non-empty tuple is truthy).
# This is a common bug.
assert (1 == 2, "should fail")  # passes silently!  -- linters catch this
