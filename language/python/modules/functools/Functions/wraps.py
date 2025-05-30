# %%
import functools


def memoize(fn):
    cache = {}

    @functools.wraps(fn)
    def lookup_or_miss(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]

    return lookup_or_miss


def memoize2(fn):
    cache = {}

    def lookup_or_miss(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]

    return lookup_or_miss
