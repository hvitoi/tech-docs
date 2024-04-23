# %%
import heapq
from unittest import TestCase


def heapify(nums: list) -> None:
    nums[:] = [el * -1 for el in nums]
    heapq.heapify(nums)


def heappush(nums: list, num: int) -> None:
    heapq.heappush(nums, num * -1)


def heappop(nums: list) -> int:
    return heapq.heappop(nums) * -1


def find_kth_largest_with_max_heap(nums: list[int], k: int) -> int:
    heapify(nums)
    num = None
    for _ in range(k):
        num = heappop(nums)
    return num


test_case = TestCase()
test_case.assertEqual(find_kth_largest_with_max_heap([3, 2, 1, 5, 6, 4], 2), 5)
test_case.assertEqual(find_kth_largest_with_max_heap([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)
