# %%
from concurrent.futures import ThreadPoolExecutor
from time import sleep

# Future represents the eventual result of an async computation.
# .result(timeout=None) blocks until done, returns the value, or re-raises the worker's exception.
# .done() is a non-blocking poll — True once the future is finished (success, failure, or cancelled).


def slow_double(x):
    sleep(0.5)
    return x * 2


with ThreadPoolExecutor() as executor:
    f = executor.submit(slow_double, 21)

    print(f.done())  # False — still running
    print(f.result())  # 42 — blocks ~0.5s until ready
    print(f.done())  # True

    # .result(timeout=...) raises TimeoutError if not ready in time
    g = executor.submit(slow_double, 5)
    try:
        g.result(timeout=0.1)
    except TimeoutError:
        print("not ready yet")
    print(g.result())  # 10
