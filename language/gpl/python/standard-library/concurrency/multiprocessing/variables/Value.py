# %%
from multiprocessing import Process, Value

# A Value is a shared, single piece of data (int, double, etc.) that multiple processes can safely read and update.
# It uses synchronization under the hood to avoid race conditions.
# 🔹 When to use: When processes need to share and update one variable.
# Without Value, each process would have its own copy. Here, they share and update the same integer.


def increment(shared_value):
    for _ in range(1000):
        shared_value.value += 1


if __name__ == "__main__":
    v = Value("i", 0)  # 'i' = integer, initial value = 0

    processes = [Process(target=increment, args=(v,)) for _ in range(4)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print("Final value:", v.value)
