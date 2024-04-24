# %%
import heapq
from unittest import TestCase


def sort_k_sorted_array_with_heap(arr: list[int], k: int):
    """
    Time: O(n*k*log(k)) - could be improved to n*log(k) if the heap is defined once in the beginning
    Space: O(k)
    """
    for i in range(len(arr)):
        left = i
        right = i + k if i + k <= len(arr) - 1 else len(arr) - 1

        heap: list[tuple[int, int]] = [(arr[i], i) for i in range(left, right + 1)]
        heapq.heapify(heap)  # heapq uses the first index by default

        el = heapq.heappop(heap)
        arr[i], arr[el[1]] = arr[el[1]], arr[i]

    return arr


def sort_k_sorted_array_with_pointer(arr: list[int], k: int):
    """
    Time: O(n*k)
    Space: O(1)
    """
    for i in range(len(arr)):
        left = i
        right = i + k if i + k <= len(arr) - 1 else len(arr) - 1

        min_index = left
        for j in range(left + 1, right + 1):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


test_case = TestCase()
for fn in {
    sort_k_sorted_array_with_heap,
    sort_k_sorted_array_with_pointer,
}:
    test_case.assertEqual(
        fn([6, 5, 3, 2, 8, 10, 9, 9], 3),
        [2, 3, 5, 6, 8, 9, 9, 10],
    )
