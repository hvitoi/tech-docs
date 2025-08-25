# %%
import time
from multiprocessing import Process
from threading import current_thread


def cpu_task():
    print(f"Running on Thread: {current_thread().name}")
    for _ in range(1_000_000_000):
        pass


if __name__ == "__main__":
    start_time = time.perf_counter()

    processes = [Process(target=cpu_task) for _ in range(4)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print(f"Total execution time: {time.perf_counter() - start_time}")
