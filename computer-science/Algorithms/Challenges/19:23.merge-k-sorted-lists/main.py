# %%
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
        lesser: tuple[int, int] = (math.inf, -1)
        for arr_index, pointer in enumerate(pointers):
            arr = lists[arr_index]
            if pointer < len(arr):
                lesser = min(lesser, (arr[pointer], arr_index))
        merged.append(lesser[0])
        pointers[lesser[1]] += 1

    return merged


test_case = TestCase()

for fn in {merge_k_lists_with_pointers}:
    test_case.assertEqual(
        fn([[1, 4, 5], [1, 3, 4], [2, 6]]),
        [1, 1, 2, 3, 4, 4, 5, 6],
    )
    test_case.assertEqual(fn([]), [])
    test_case.assertEqual(fn([[]]), [])
