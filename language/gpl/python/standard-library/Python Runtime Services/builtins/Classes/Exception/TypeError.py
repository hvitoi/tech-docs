# %%
# TypeError -- Exception -- BaseException
#
# An operation/function got an argument of the wrong TYPE,
# OR was called with the wrong number/keyword of arguments.

len(5)  # TypeError: object of type 'int' has no len()
"a" + 1  # TypeError: can only concatenate str (not "int") to str
[1, 2] + "c"  # TypeError
sorted([1, "a"])  # TypeError: '<' not supported between str and int


# wrong arity / kwargs
def f(x, y): ...


f(1)  # TypeError: missing 1 required positional argument: 'y'
f(1, 2, 3)  # TypeError: takes 2 positional arguments but 3 were given
f(1, z=2)  # TypeError: got an unexpected keyword argument 'z'

# Calling something that isn't callable
None()  # TypeError: 'NoneType' object is not callable

# Hashing an unhashable type (dicts/sets)
{[1, 2]: "x"}  # TypeError: unhashable type: 'list'

# Mixing bytes and str
b"a" + "b"  # TypeError


# %%
# Common pattern: raise TypeError yourself for protocol violations
def double(x):
    if not isinstance(x, (int, float)):
        raise TypeError(f"expected number, got {type(x).__name__}")
    return x * 2


# %%
# NotImplemented (singleton) vs NotImplementedError (exception)
# - Operator dunder methods (__add__, __eq__, ...) should RETURN NotImplemented
#   when they don't handle the other operand; Python then tries the reflected op.
# - Returning NotImplementedError or raising TypeError manually breaks that protocol.
class V:
    def __add__(self, other):
        if not isinstance(other, V):
            return NotImplemented  # NOT raise
        return V()
