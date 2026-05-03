# %%
# ValueError -- Exception -- BaseException
#
# Argument has the right TYPE but an inappropriate VALUE.
# (Wrong type -> TypeError instead.)

int("abc")  # ValueError: invalid literal for int() with base 10: 'abc'
float("nan-ish")  # ValueError
"abc".index("z")  # ValueError: substring not found
[1, 2].remove(99)  # ValueError: list.remove(x): x not in list

import math

math.sqrt(-1)  # ValueError: math domain error


# %%
# Common pattern: validate inputs and raise ValueError yourself
def percent(x):
    if not 0 <= x <= 100:
        raise ValueError(f"percent out of range: {x}")
    return x


# %%
# UnicodeError is a subclass -- catch ValueError to catch encode/decode errors too
try:
    b"\xff\xfe".decode("utf-8")
except ValueError:  # UnicodeDecodeError is a ValueError
    pass


# %%
# Subclass when callers may want to distinguish
class NegativeAmount(ValueError):
    pass
