# %%
from concurrent.futures import ThreadPoolExecutor, as_completed
from random import random
import time

# as_completed() yields futures as they finish (any order).
# Use it when you want to react to results as soon as each one is ready,
# instead of waiting for all of them like .map() does.


def do_something(n):
    time.sleep(random())
    return n


with ThreadPoolExecutor(max_workers=4) as executor:
    futures = {executor.submit(do_something, i): i for i in range(5)}

    for future in as_completed(futures):
        original_input = futures[future]
        print(f"Task {original_input} finished -> {future.result()}")
