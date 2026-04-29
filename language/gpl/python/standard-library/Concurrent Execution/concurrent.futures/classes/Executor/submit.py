# %%
from concurrent.futures import ThreadPoolExecutor

# submit(fn, *args, **kwargs) schedules a single callable and returns a Future.
# A Future represents an eventual result — query it with .result(), .done(), .exception().


def divide(a, b):
    return a / b


with ThreadPoolExecutor() as executor:
    future_ok = executor.submit(divide, 10, 2)
    future_err = executor.submit(divide, 10, 0)

    print(future_ok.result())  # 5.0 — blocks until done
    print(future_ok.done())  # True

    # Exceptions raised inside the worker are re-raised by .result()
    # Use .exception() to inspect without raising
    print(future_err.exception())  # ZeroDivisionError(...)
