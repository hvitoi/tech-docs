# %%
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED
import time

# wait() blocks until futures meet a condition, returning (done, not_done) sets.
# return_when:
#   ALL_COMPLETED  (default) — wait for everything
#   FIRST_COMPLETED          — return as soon as any future finishes
#   FIRST_EXCEPTION          — return on first exception (or all done if none)


def do_something(n):
    time.sleep(n)
    return n


with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(do_something, n) for n in (3, 1, 2)]

    done, not_done = wait(futures, return_when=FIRST_COMPLETED)

    print(f"Done: {[f.result() for f in done]}")  # the fastest one (1)
    print(f"Still running: {len(not_done)}")
