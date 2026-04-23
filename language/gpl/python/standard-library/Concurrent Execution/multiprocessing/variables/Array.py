# %%
from multiprocessing import Array, Process

# An Array is like Value but for multiple values (a fixed-size array).
# Processes can share a list-like structure directly.
# 🔹 When to use: When multiple processes need to read/update elements of the same list.


def add_one(shared_array):
    for i in range(len(shared_array)):
        shared_array[i] += 1


if __name__ == "__main__":
    arr = Array("i", [1, 2, 3, 4])  # shared int array

    p = Process(target=add_one, args=(arr,))
    p.start()
    p.join()

    print("Array after process:", list(arr))
