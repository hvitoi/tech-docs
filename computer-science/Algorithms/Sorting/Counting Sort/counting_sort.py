# %%
from unittest import TestCase


def counting_sort(arr: list[int]) -> list[int]:
    """
    This solution does not optimize the space complexity
    Neither cares about being stable
    """
    counter = [0] * (max(arr) + 1)

    # populate the counter with the occurrences of each num
    for num in arr:
        counter[num] += 1

    # pick only the elements which have occurrences
    sorted = []
    for num, occ in enumerate(counter):
        if occ == 0:
            continue
        sorted.extend([num] * occ)

    return sorted


test_case = TestCase()
test_case.assertEqual(counting_sort([1, 0, 3, 1, 3, 1]), [0, 1, 1, 1, 3, 3])
