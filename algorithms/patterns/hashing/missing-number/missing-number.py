# %%
def missing_number(nums: list[int]) -> int:
    """
    Hashing: O(n) time, O(n) space.
    """
    all_nums = set(nums)
    for n in range(len(nums) + 1):
        if n not in all_nums:
            return n
    raise ValueError("input violates contract: no missing number in [0, n]")


# %%
def missing_number_cyclic_sort(nums: list[int]) -> int:
    """
    Puts each number into the index that they belong
    """
    n = len(nums)
    for i in range(n):
        while nums[i] != i and nums[i] != n:
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
    for i in range(n):
        if nums[i] != i:
            return i
    return n


for fn in [missing_number, missing_number_cyclic_sort]:
    assert fn([3, 0, 1]) == 2
    assert fn([0, 1]) == 2
    assert fn([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
