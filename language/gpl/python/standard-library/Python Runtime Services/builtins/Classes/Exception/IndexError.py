# %%
# IndexError -- LookupError -- Exception -- BaseException
#
# Sequence index out of range. Raised by list/tuple/str/bytes subscript.
# (Dicts raise KeyError, NOT IndexError.)

[1, 2, 3][5]  # IndexError: list index out of range
"abc"[10]  # IndexError: string index out of range
(1, 2)[2]  # IndexError: tuple index out of range

# Slicing does NOT raise -- it clamps silently
[1, 2, 3][5:10]  # []  (no error)

# %%
# Common pattern: guard with len() or use try/except
xs = [1, 2, 3]
i = 5
if 0 <= i < len(xs):
    xs[i]
else:
    None

# %%
# Catching
try:
    [1, 2, 3][5]
except IndexError as e:
    e.args  # ('list index out of range',)

# %%
# LookupError catches BOTH IndexError and KeyError
try:
    {}["k"]
except LookupError:
    pass
