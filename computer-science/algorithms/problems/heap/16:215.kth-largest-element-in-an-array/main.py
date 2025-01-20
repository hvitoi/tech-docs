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
    """
    Time: O(n*log(n)) - to build a heap out of all the elements
    Space: O(1) - no new array (reuses the same array in-place)
    Space: O(n) - if creating a new heap array (to do not mess up with the original one)
    """
    heapify(nums)
    num = None
    for _ in range(k):
        num = heappop(nums)
    return num


def find_kth_largest_min_heap(nums: list[int], k: int) -> int:
    """
    Time: O(n*log(k)) - to build the heap with the k largest elements
    Space: O(k) - the memory of the heap with the k largest elements
    """
    heap = []
    for num in nums:
        if len(heap) >= k:
            # if num >= heap[-1]:  # if it's not large enough, don't even put it in (do not influence on the time complexity)
            heapq.heappushpop(heap, num)
        else:
            heapq.heappush(heap, num)
    return heap[0]  # peek the next one in the heap


def find_kth_largest_with_partitioning(arr: list[int], k: int) -> int:
    """
    This solution considers that you know in which index the kth largest solution will be
    on a sorted array "len(arr) - k".
    You can then apply partitioning (same from quicksort) to move all elements smaller than it
    to the left and all the numbers greater than it to the right
    """

    def partition(left: int, right: int) -> int:
        pivot = arr[right]
        pivot_index = left
        for i in range(left, right):
            if arr[i] <= pivot:
                arr[pivot_index], arr[i] = arr[i], arr[pivot_index]
                pivot_index += 1
        arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
        return pivot_index

    def kth_largest(left: int, right: int, target_index: int) -> int:
        pivot_index = partition(left, right)

        if pivot_index == target_index:
            return arr[target_index]

        if pivot_index > target_index:
            return kth_largest(left, pivot_index - 1, target_index)

        if pivot_index < target_index:
            return kth_largest(pivot_index + 1, right, target_index)

    target_index = len(arr) - k  # the index of the kth largest number in a sorted array
    return kth_largest(0, len(arr) - 1, target_index)


test_case = TestCase()

for fn in {
    find_kth_largest_max_heap,
    find_kth_largest_min_heap,
    find_kth_largest_with_partitioning,
}:
    test_case.assertEqual(fn([3, 2, 1, 5, 6, 4], 2), 5)
    test_case.assertEqual(fn([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)
