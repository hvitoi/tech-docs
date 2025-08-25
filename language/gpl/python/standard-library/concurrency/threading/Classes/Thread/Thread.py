# %%
from threading import Thread, current_thread
import time

# Spawn a new OS Thread to run a task
# Given the GIL limitations, only one thread can be executed by CPython at a time


def cpu_task():
    print(f"Running on Thread: {current_thread().name}")
    for _ in range(1_000_000_000):
        pass


start_time = time.perf_counter()

threads = [Thread(target=cpu_task) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Total execution time: {time.perf_counter() - start_time}")
