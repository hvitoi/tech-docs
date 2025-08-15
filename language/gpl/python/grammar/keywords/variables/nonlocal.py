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

# %%
# nonlocal vs. global
x = 0


def change_global():
    global x
    x += 1


def outer():
    y = 0

    def change_enclosing():
        nonlocal y
        y += 1

    change_enclosing()


# %%
# nonlocal most common usage are in closure functions to keep state across multiple calls, without having to use a class


def make_counter():
    count = 0  # enclosed variable

    def increment():
        nonlocal count  # modify enclosing scope variable
        count += 1
        return count

    return increment  # return the inner function


counter = make_counter()

print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
