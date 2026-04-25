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

    return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)


counter = 0
fibonacci_memoized(35)
counter  # 36 with memo, 29860703 without
