# LC#33 https://leetcode.com/problems/search-in-rotated-sorted-array/ (30k likes - Apr-2026)
# %%


def search(nums: list[int], target: int) -> int:
    n = len(nums)
    k = nums[0]
    sorted_nums = nums[k:] + nums[:k]  # unrotate the array (see rotate-array.py)

    def bs(left: int, right: int) -> int:
        if right - left < 0:
            return -1

        mid = left + (right - left) // 2

        if target == sorted_nums[mid]:
            return mid + k

        if target < sorted_nums[mid]:
            return bs(left, mid - 1)

        if target > sorted_nums[mid]:
            return bs(mid + 1, right)

        return -1  # can be omitted (just for type check)

    return bs(0, n - 1)


assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
assert search([1], 0) == -1
