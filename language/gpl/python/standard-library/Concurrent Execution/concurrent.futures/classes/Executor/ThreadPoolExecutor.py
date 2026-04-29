# %%
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread
from time import sleep

# A pool of worker threads — good for I/O-bound tasks (HTTP, disk, DB).
# The `with` block creates the pool and shuts it down (waits for tasks) on exit.


def io_task(name):
    print(f"Task {name} on {current_thread().name}")
    sleep(1)  # simulates I/O wait
    return f"{name} result"


with ThreadPoolExecutor(max_workers=4) as executor:
    # submit() schedules a callable, returns a Future immediately
    futures = [executor.submit(io_task, x) for x in ["A", "B", "C"]]

    # .result() blocks until that future is done
    results = [f.result() for f in futures]

print(results)
