# %%
from concurrent.futures import ThreadPoolExecutor
from time import sleep

# .add_done_callback(fn) registers a callable invoked with the Future when it finishes
# (success, exception, or cancelled). Runs in the worker thread that completed the task —
# keep callbacks fast and exception-safe; raised exceptions are logged and swallowed.


def work(x):
    sleep(0.2)
    return x * x


def on_done(fut):
    if fut.exception():
        print(f"failed: {fut.exception()}")
    else:
        print(f"done: {fut.result()}")


with ThreadPoolExecutor() as executor:
    f = executor.submit(work, 7)
    f.add_done_callback(on_done)  # fires once f completes — prints "done: 49"
