# %%


def move_zeroes(nums: list) -> None:
    """O(n^2)"""
    zeroes_count = nums.count(0)
    for _ in range(zeroes_count):
        nums.remove(0)
        nums.append(0)


nums = [0, 1, 0, 3, 12]
move_zeroes(nums)
assert nums == [1, 3, 12, 0, 0]

nums = [0]
move_zeroes(nums)
assert nums == [0]

nums = [0, 0, 0, 3, 12]
move_zeroes(nums)
assert nums == [3, 12, 0, 0, 0]
