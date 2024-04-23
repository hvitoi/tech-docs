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


def find_kth_largest_max_heap(nums: list[int], k: int) -> int:
    heapify(nums)
    num = None
    for _ in range(k):
        num = heappop(nums)
    return num


def partition(arr: list, *, left: int, right: int) -> int:
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


def find_kth_largest_partitioning(
    arr: list[int], k: int, *, left: int = None, right: int = None
) -> int:
    if left is None:
        left = 0

    if right is None:
        right = len(arr) - 1

    target_index = len(arr) - k
    pivot_index = partition(arr, left=left, right=right)

    if target_index == pivot_index:
        return arr[target_index]

    if target_index < pivot_index:
        return find_kth_largest_partitioning(arr, k, left=left, right=pivot_index - 1)

    if target_index > pivot_index:
        return find_kth_largest_partitioning(arr, k, left=pivot_index + 1, right=right)


test_case = TestCase()

for fn in {find_kth_largest_max_heap, find_kth_largest_partitioning}:
    test_case.assertEqual(fn([3, 2, 1, 5, 6, 4], 2), 5)
    test_case.assertEqual(fn([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)
