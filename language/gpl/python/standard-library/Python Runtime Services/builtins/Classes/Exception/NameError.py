# %%
# NameError -- Exception -- BaseException
#
# A local or global name is not found. Almost always a typo or a missing import.

print(undefined_var)  # NameError: name 'undefined_var' is not defined
# 3.10+: "Did you mean: 'undefined'?"

# %%
# 3.10+ adds .name attribute
try:
    foo
except NameError as e:
    e.name  # 'foo'

# %%
# UnboundLocalError -- subclass of NameError.
# Raised when a function references a local name BEFORE assignment, where
# "local" is determined at compile time by whether the name is assigned anywhere
# in the function body.

x = 10


def bad():
    print(x)  # x is local because of the assignment below
    x = 1  # this makes x local for the WHOLE function


bad()  # UnboundLocalError: cannot access local variable 'x'


# Fix with `global` or `nonlocal`
def good():
    global x
    print(x)  # 10
    x = 1
