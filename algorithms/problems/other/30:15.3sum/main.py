# %%
from typing import List
from unittest import TestCase


def three_sum(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    result = []
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                incumbent = sorted([nums[i], nums[j], nums[k]])
                if sum(incumbent) == 0 and incumbent not in result:
                    result.append(incumbent)
    return sorted(result)


test_case = TestCase()

for fn in {three_sum}:
    test_case.assertEqual(fn([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
    test_case.assertEqual(fn([0, 1, 1]), [])
    test_case.assertEqual(fn([0, 0, 0]), [[0, 0, 0]])
