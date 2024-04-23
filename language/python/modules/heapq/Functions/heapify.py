# Mutates and returns None

# %%
import heapq

# MIN HEAP
li = [7, 6, 5, 4, 3, 2, 1]
heapq.heapify(li)
li


# %%
# MAX HEAP
# There is no min heap implementation, however it can be built out of negative values and a min heap
def heapify(nums: list) -> None:
    nums[:] = [el * -1 for el in nums]
    heapq.heapify(nums)


def heappush(nums: list, num: int) -> None:
    heapq.heappush(nums, num * -1)


def heappop(nums: list) -> int:
    return heapq.heappop(nums) * -1


li = [1, 2, 3, 4, 5, 6, 7]
heapify(li)
li

heappush(li, 8)
heappop(li)
