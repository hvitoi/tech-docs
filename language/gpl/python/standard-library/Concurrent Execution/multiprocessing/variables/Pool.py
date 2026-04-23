# %%
import time
from multiprocessing import Pool

# A Pool manages a group of worker processes and distributes tasks among them.
# Instead of creating processes manually, you can just map a function across data.
# 🔹 When to use: When you want to run the same function on many inputs (data parallelism).


def square(n):
    time.sleep(1)  # simulate work
    return n * n


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    with Pool(processes=3) as pool:  # 3 workers
        results = pool.map(square, numbers)

    print("Results:", results)
