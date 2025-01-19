# Mutates and returns None

# %%
import heapq

# MIN HEAP
arr = [7, 6, 5, 4, 3, 2, 1]
heapq.heapify(arr)
arr


# %%
import heapq
import unittest
# MAX HEAP
# There is no min heap implementation, however it can be built out of negative values and a min heap

def heapify(nums: list) -> None:
    nums[:] = [-x for x in nums]
    heapq.heapify(nums)
    nums[:] = [-x for x in nums]

def heappush(nums: list, num: int) -> None:
    nums[:] = [-x for x in nums]
    heapq.heappush(nums, -num)
    nums[:] = [-x for x in nums]

def heappop(nums: list) -> int:
    nums[:] = [-x for x in nums]
    popped = heapq.heappop(nums) * -1
    nums[:] = [-x for x in nums]
    return popped

test_case = unittest.TestCase()

arr = [1, 2, 3, 4, 5, 6, 7]

heapify(arr)
test_case.assertEqual(arr, [7, 5, 6, 4, 2, 1, 3])

heappush(arr, 8)
test_case.assertEqual(arr, [8, 7, 6, 5, 2, 1, 3, 4])

popped = heappop(arr)
test_case.assertEqual(popped, 8)
test_case.assertEqual(arr, [7, 5, 6, 4, 2, 1, 3])
