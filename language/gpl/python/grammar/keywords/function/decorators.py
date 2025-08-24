# It's a outer function that wraps and return an inner function


# %%


def memoize(fn):
    cache = {}

    def lookup_or_miss(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = fn(*args, **kwargs)
        return cache[key]

    return lookup_or_miss


@memoize
def fibonacci_memoized(n):
    global counter
    counter += 1

    if n <= 1:
        return n

    # the decorator takes care of recursive functions to call the memoized version and not the original version. This doesn't happen when you try to apply a closure function directly
    return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)


counter = 0
fibonacci_memoized(35)
counter  # 36 with memoization, 29_860_703 without

# %%


def memoize(fn):
    cache = {}

    def lookup_or_miss(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = fn(lookup_or_miss, *args, **kwargs)
        return cache[key]

    return lookup_or_miss


# In order to use closure functions correctly for recursive calls,
# it's important to add another argument that represents the wrapped
# version of the function. Otherwise, the recursive would call the
# non-wrapped/original version of the function
def fibonacci(self, n):
    global counter
    counter += 1

    if n <= 1:
        return n

    return self(n - 1) + self(n - 2)


counter = 0
fibonacci_memoized = memoize(fibonacci)
fibonacci_memoized(35)
counter  # 36 with memoization, 29_860_703 without


# %%
def greetings(name):
    def greeting_decorator(fn):
        def wrapper():
            print(f"Hello {name}!")
            fn()
            print(f"Bye {name}!")

        return wrapper

    return greeting_decorator


@greetings("Henry")  # it's a function that returns an decorator
def give_love():
    print("I love you!")


# Apply decorator manually
give_love()

# %%
# A closure is a function that "remembers" the environment in which it was created
# it's a function that has access to variables from its enclosing scope, even after the outer function has finished executing.
# They capture variables from their enclosing scopes.


def outer(x):
    y = 10  # local variable in the outer function

    def inner(z):  # inner is the closure function
        return x + y + z  # inner function uses variables from outer

    return inner  # return the inner function


f = outer(5)
print(f(3))  # 5 + 10 + 3 = 18
# Even though outer has finished executing, inner still remembers x=5 and y=10.
