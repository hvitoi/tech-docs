# %%
import threading
import time

# CPU-bound task using threads


def cpu_task():
    count = 0
    for _ in range(10_000_000):
        count += 1
    return count


start = time.time()
threads = []

for _ in range(4):  # 4 threads
    t = threading.Thread(target=cpu_task)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()
print("Threaded time:", end - start)

# %%
# CPU-bound task using processes

import time
from multiprocessing import Process


def cpu_task():
    count = 0
    for _ in range(10_000_000):
        count += 1
    return count


start = time.time()
processes = []

for _ in range(4):  # 4 processes
    p = Process(target=cpu_task)
    p.start()
    processes.append(p)

for p in processes:
    p.join()

end = time.time()
print("Multiprocessing time:", end - start)
