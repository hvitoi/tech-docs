# %%
from threading import Thread, current_thread
import time

# CPU-bound tasks: can't use multiple CPU cores
# IO-bound tasks: works good


def cpu_task():
    thread = current_thread()
    print(f"Running on Thread: {thread.name}")
    # time.sleep(1)
    for _ in range(1_000_000_000):
        pass


start = time.time()

threads = [Thread(target=cpu_task) for _ in range(4)]
for t in threads:
    t.start()
for t in threads:
    t.join()

end = time.time()

print("Total execution time:", end - start)
