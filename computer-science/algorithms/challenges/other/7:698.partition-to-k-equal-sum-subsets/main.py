# %%
from unittest import TestCase


def can_partition_k_subsets(nums: list[int], k: int):
    target_sum = sum(nums) / k
    buckets = [[] for _ in range(k)]

    for num in nums:
        # check if the number can be fitted in any bucket
        for bucket in buckets:
            # could be improved by storing the bucket sum (instead of calculating it every time)
            if sum(bucket) + num <= target_sum:
                bucket.append(num)
                break

    for bucket in buckets:
        if sum(bucket) != target_sum:
            return False

    return True


def can_partition_k_subsets_recursive(nums: list[int], k: int):
    if k == 0 or sum(nums) % k != 0:
        return False

    if k == 1:
        return True

    target_size = sum(nums) / k
    bucket = []

    leftover_nums = []

    for num in nums:
        if sum(bucket) + num <= target_size:
            bucket.append(num)
        else:
            leftover_nums.append(num)

    if sum(bucket) == target_size:
        return can_partition_k_subsets_recursive(leftover_nums, k - 1)

    return False


test_case = TestCase()

for fn in {can_partition_k_subsets, can_partition_k_subsets_recursive}:
    test_case.assertEqual(fn([4, 3, 2, 3, 5, 2, 1], 4), True)
    test_case.assertEqual(fn([1, 2, 3, 4], 3), False)
