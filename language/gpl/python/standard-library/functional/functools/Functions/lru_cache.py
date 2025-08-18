# %%
from functools import lru_cache


# An LRU cache (Least Recently Used cache) is a caching strategy that
# keeps a limited number of items in memory and automatically discards
# the least recently used items when the cache is full.

# - Automatic caching – function results are stored in memory.
# - Limited size – you can set maxsize (e.g., 128). If the cache exceeds this, the least recently used entries are removed.
# - Speedup – repeated calls with the same arguments are very fast.
# - Thread-safe – safe to use in multithreaded programs.


@lru_cache(maxsize=None)
def fibonacci(n):
    global counter
    counter += 1
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


counter = 0
fibonacci(35)
counter  # 36 with memoization, 29_860_703 without
