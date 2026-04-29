# %%
from concurrent.futures import ThreadPoolExecutor

# .exception(timeout=None) returns the worker's exception (or None if it succeeded) WITHOUT raising it
# Useful to inspect failures without try/except around .result().


def divide(a, b):
    return a / b


with ThreadPoolExecutor() as executor:
    f_ok = executor.submit(divide, 10, 2)
    f_err = executor.submit(divide, 10, 0)

    print(f_ok.exception())  # None — succeeded
    print(f_err.exception())  # ZeroDivisionError('division by zero')

    # .result() on a failed future re-raises the exception in the calling thread
    try:
        f_err.result()
    except ZeroDivisionError as e:
        print(f"re-raised: {e}")
