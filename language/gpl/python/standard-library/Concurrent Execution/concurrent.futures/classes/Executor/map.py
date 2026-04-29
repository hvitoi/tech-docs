# %%
from concurrent.futures import ThreadPoolExecutor
import time

# map() applies a function to each item of an iterable in parallel.
# Results are yielded in the SAME ORDER as the input (unlike as_completed).


def slow_square(n):
    time.sleep(0.5)
    return n * n


with ThreadPoolExecutor(max_workers=4) as executor:
    # automatically Executor.submit() them and lazily Future.result() them as they are iterated over
    results = executor.map(slow_square, [1, 2, 3, 4, 5])

# Iterating consumes results in input order.
# If a worker raises, the exception is re-raised here.
for r in results:
    print(r)
