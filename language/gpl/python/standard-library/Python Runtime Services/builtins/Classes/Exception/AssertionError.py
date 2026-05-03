# %%
# AssertionError -- Exception -- BaseException
#
# Raised by failing `assert` statements. Used heavily by test frameworks.

assert 1 + 1 == 2  # ok
assert 1 + 1 == 3, "math is broken"  # AssertionError: math is broken
