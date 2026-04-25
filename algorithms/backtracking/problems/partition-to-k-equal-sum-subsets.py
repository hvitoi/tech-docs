# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/ - 7k likes (Apr/2026)
# %%
from unittest import TestCase


def can_partition_k_subsets(nums: list[int], k: int):
    target_sum = sum(nums) // k
    buckets = [[] for _ in range(k)]

    def backtrack(i):
        # all numbers placed: did each bucket reach the target?
        if i == len(nums):
            return all(sum(b) == target_sum for b in buckets)

        # try placing the number in every bucket
        num = nums[i]
        for bucket in buckets:
            if sum(bucket) + num <= target_sum:
                bucket.append(num)  # choose
                if backtrack(i + 1):  # explore
                    return True
                bucket.pop()  # undo

        # it want's possible to place it in any bucket
        return False

    return backtrack(0)


test_case = TestCase()

test_case.assertEqual(can_partition_k_subsets([4, 3, 2, 3, 5, 2, 1], 4), True)
test_case.assertEqual(can_partition_k_subsets([1, 2, 3, 4], 3), False)
test_case.assertEqual(can_partition_k_subsets([1, 1, 1, 1, 2, 2, 2, 2], 4), True)
test_case.assertEqual(can_partition_k_subsets([2, 2, 2, 2, 3, 4, 5], 4), False)
