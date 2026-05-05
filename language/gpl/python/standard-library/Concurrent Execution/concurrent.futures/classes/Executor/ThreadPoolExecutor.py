# %%
from concurrent.futures import Future, ThreadPoolExecutor, wait
from threading import current_thread
from time import sleep

# A pool of worker threads — good for I/O-bound tasks (HTTP, disk, DB).
# The `with` block creates the pool and shuts it down (waits for tasks) on exit.


def io_task(name):
    print(f"{name} thread started on {current_thread().name}")
    sleep(1)  # simulates I/O wait
    return f"{name} result"


with ThreadPoolExecutor(max_workers=4) as executor:
    # .submit() schedules a callable, returns a Future immediately
    f: Future[str] = executor.submit(io_task, "A")

    # .result() blocks until that future is done
    result = f.result()
    print(result)

    # exiting the `with` waits for all tasks; .result() also re-raises any exception, so calling .result() is not necessary
    # but you can also call wait if you want...
    wait([f])
