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
