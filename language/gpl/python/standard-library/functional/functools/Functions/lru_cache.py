# %%
from functools import lru_cache

# An LRU cache (Least Recently Used cache) is a caching strategy that
# keeps a limited number of items in memory and automatically discards
# the least recently used items when the cache is full.

# - Automatic caching – function results are stored in memory.
# - Limited size – you can set maxsize (e.g., 128). If the cache exceeds this, the least recently used entries are removed.
# - Speedup – repeated calls with the same arguments are very fast.
# - Thread-safe – safe to use in multithreaded programs.


# 128 is maximum unique argument combinations that are cached (distinct function executions - with same set of parameters)
@lru_cache(maxsize=128)
def fibonacci(n):
    global counter
    counter += 1
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


counter = 0
fibonacci(35)
counter  # 36 with memoization, 29_860_703 without

# %%

# %%
import json
from functools import lru_cache
from http.client import HTTPResponse, HTTPSConnection
from urllib.parse import urlparse


@lru_cache
def get_http_url(url):
    url_parsed = urlparse(url)
    conn = HTTPSConnection(url_parsed.netloc)
    conn.request("GET", url_parsed.path)
    response: HTTPResponse = conn.getresponse()
    return json.loads(response.read())


print(get_http_url("https://httpbin.org/get"))  # lookup
print(get_http_url("https://httpbin.org/get"))  # miss
print(get_http_url("https://httpbin.org/get"))  # miss

get_http_url.cache_clear()  # clear all cache

print(get_http_url("https://httpbin.org/get"))  # lookup
print(get_http_url("https://httpbin.org/get"))  # miss
print(get_http_url("https://httpbin.org/get"))  # miss
