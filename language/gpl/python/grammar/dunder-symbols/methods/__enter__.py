# %%
# __enter__ + __exit__ make an object a context manager (usable with `with`).
#
# - __enter__(self):
#     runs at block entry; the return value is bound to `as`.
# - __exit__(self, exc_type, exc_value, traceback):
#     runs at block exit (even if an exception was raised);
#     return True to SUPPRESS the exception, anything else (incl. None)
#     to let it propagate.


import time


class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self  # exposed as `t` in `with Timer() as t:`

    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {self.elapsed:.3f}s")
        # implicit return None -> exceptions propagate normally


with Timer() as t:
    sum(range(1_000_000))

# Elapsed: 0.012s

t.elapsed  # 0.012... (still accessible after the block)
