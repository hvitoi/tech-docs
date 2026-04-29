# %%
from concurrent.futures import ThreadPoolExecutor, as_completed
import random
import time

# as_completed() yields futures as they finish (any order).
# Use it when you want to react to results as soon as each one is ready,
# instead of waiting for all of them like .map() does.


def task(n):
    time.sleep(random.uniform(0.1, 1.0))
    return n


with ThreadPoolExecutor(max_workers=4) as executor:
    futures = {executor.submit(task, i): i for i in range(5)}

    for future in as_completed(futures):
        original_input = futures[future]
        print(f"Task {original_input} finished -> {future.result()}")
