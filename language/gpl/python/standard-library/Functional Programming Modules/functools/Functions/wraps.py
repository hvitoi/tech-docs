# %%
import functools

# functools.wraps preserves the original function’s metadata.


def memoize(fn):
    cache = {}

    @functools.wraps(fn)
    def lookup_or_miss(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = fn(*args, **kwargs)
        return cache[key]

    return lookup_or_miss
