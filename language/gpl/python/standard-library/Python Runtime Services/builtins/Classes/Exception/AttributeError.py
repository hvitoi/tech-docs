# %%
# AttributeError -- Exception -- BaseException
#
# Attribute reference or assignment fails.

"abc".nonexistent  # AttributeError: 'str' object has no attribute 'nonexistent'
None.foo  # AttributeError: 'NoneType' object has no attribute 'foo'

# %%
# 3.10+ adds .name and .obj attributes
try:
    "abc".uper()  # typo
except AttributeError as e:
    e.name  # 'uper'
    e.obj  # 'abc'
    # 3.12+ ships a "did you mean" suggestion in the message: "Did you mean: 'upper'?"

# %%
# Avoid by checking with hasattr / getattr default
o = "abc"
hasattr(o, "upper")  # True
getattr(o, "missing", None)  # None, no raise


# %%
# __getattr__ is the hook -- raise AttributeError to signal "not found"
class Lazy:
    def __getattr__(self, name):
        if name == "answer":
            return 42
        raise AttributeError(name)  # MUST raise, returning None breaks hasattr()


# %%
# Common gotcha: AttributeError inside __getattr__ / property / descriptor
# is silently swallowed by hasattr() and turned into False.
class Buggy:
    @property
    def x(self):
        return self._x  # if _x is missing, raises AttributeError


hasattr(Buggy(), "x")  # False  -- masks the real bug
