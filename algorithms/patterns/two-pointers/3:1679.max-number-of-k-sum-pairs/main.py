# https://leetcode.com/problems/max-number-of-k-sum-pairs/ - 3k likes (Apr/2026)
# %%


def remove_summing_up_elements(nums: list, k: int):
    """
    Remove the first summing up elements
    """
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums):
            if (i != j) and (num1 + num2) == k:
                nums.pop(i)
                nums.pop(j - 1)
                return nums
    return -1


def max_operations(nums: list, k: int) -> int:
    operations = 0
    while k:
        if remove_summing_up_elements(nums, k) != -1:
            operations += 1
        else:
            return operations
    return operations


assert max_operations([1, 2, 3, 4], 5) == 2
assert max_operations([3, 1, 3, 4, 3], 6) == 1
