# %%
def outer():
    x = 0

    def inner():
        nonlocal x  # refers to x in outer(). Otherwide it would create a new local variable
        x = x + 1
        print(x)

    inner()
    inner()


outer()
# This tells to python: "Don't create a new local variable x in inner. Use the x from the nearest enclosing scope."

# "nonlocal" only works for enclosing function scopes only (not global scope).
# You can't use it for variables in the global/module scope, use "global" for that.
