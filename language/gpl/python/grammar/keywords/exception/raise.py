# %%
raise Exception("An error has been found")

# %%
try:
    value = 10 / 0
except Exception as err:
    print("An exception occurred:", err)
    raise  # re-raise the same exception

# %%
# Exception chaining — three flavors when re-raising inside an except block.

# Implicit: original attached as __context__.
#   ValueError: invalid literal ...
#   During handling of the above exception, another exception occurred:
#   RuntimeError: bad input
try:
    int("abc")
except ValueError:
    raise RuntimeError("bad input")

# Explicit cause with `from e`: sets __cause__.
#   ValueError: invalid literal ...
#   The above exception was the direct cause of the following exception:
#   RuntimeError: bad input
try:
    int("abc")
except ValueError as err:
    raise RuntimeError("bad input") from err

# Suppress with `from None`: hides the original. Use when the caught exception
# is an implementation detail the caller shouldn't see.
#   RuntimeError: bad input
try:
    int("abc")
except ValueError:
    raise RuntimeError("bad input") from None
