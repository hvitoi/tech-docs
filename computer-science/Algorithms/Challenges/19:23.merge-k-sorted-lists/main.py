# %%
import heapq
import math
from unittest import TestCase


def merge_k_lists_with_pointers(lists: list[list[int]]) -> list[int]:
    """
    O(k*(a+b+c)) where k is the number of arrays
    """
    total_items = sum([len(arr) for arr in lists])
    pointers = [0 for _ in range(len(lists))]
    merged = []

    while len(merged) != total_items:
        lesser = (math.inf, -1)
        for arr_index, pointer in enumerate(pointers):
            arr = lists[arr_index]
            if pointer < len(arr):
                lesser = min(lesser, (arr[pointer], arr_index))
        merged.append(lesser[0])
        pointers[lesser[1]] += 1

    return merged


def merge_k_lists_with_pointers_and_linked_lists(lists: list[list[int]]) -> list[int]:
    """
    O(k*(a+b+c)) where k is the number of arrays
    """
    total_items = sum([len(arr) for arr in lists])
    merged = []

    while len(merged) != total_items:
        lesser_index = -1
        lesser_value = math.inf
        for arr_index, arr in enumerate(lists):
            if len(arr) > 0 and arr[0] < lesser_value:
                lesser_index, lesser_value = arr_index, arr[0]
        merged.append(lists[lesser_index].pop(0))

    return merged


def merge_k_lists_with_min_heap(lists: list[list[int]]) -> list[int]:
    merged = []

    heap = list(
        filter(
            lambda el: el,
            [(arr.pop(0), i) if len(arr) > 0 else None for i, arr in enumerate(lists)],
        )
    )
    heapq.heapify(heap)

    while heap:
        value, arr_index = heap[0]
        merged.append(value)

        arr = lists[arr_index]
        if arr:
            heapq.heappushpop(heap, (arr.pop(0), arr_index))
        else:
            heapq.heappop(heap)

    return merged


test_case = TestCase()

for fn in {
    merge_k_lists_with_pointers,
    merge_k_lists_with_pointers_and_linked_lists,
    merge_k_lists_with_min_heap,
}:
    test_case.assertEqual(
        fn([[1, 4, 5], [1, 3, 4], [2, 6]]),
        [1, 1, 2, 3, 4, 4, 5, 6],
    )
    test_case.assertEqual(fn([]), [])
    test_case.assertEqual(fn([[]]), [])
