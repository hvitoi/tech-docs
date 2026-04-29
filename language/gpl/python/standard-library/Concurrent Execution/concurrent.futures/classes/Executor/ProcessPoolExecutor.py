# %%
from concurrent.futures import ProcessPoolExecutor

# A pool of worker processes — good for CPU-bound tasks (each process has its own GIL).
# Must be guarded by `if __name__ == "__main__"` because workers re-import the module.


def cpu_task(n):
    total = 0
    for i in range(1_000):
        total += i
    return n, total


with ProcessPoolExecutor() as executor:  # defaults to os.cpu_count() workers
    results = executor.map(cpu_task, range(4))

print(list(results))
