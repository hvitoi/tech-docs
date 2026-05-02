# LC#33 https://leetcode.com/problems/search-in-rotated-sorted-array/ (30k likes - Apr-2026)
# %%


def search(nums: list[int], target: int) -> int:
    def bs(lo: int, hi: int) -> int:
        if lo > hi:
            return -1

        mid = lo + (hi - lo) // 2

        if nums[mid] == target:
            return mid

        # left half is sorted
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:  # target is on the left
                return bs(lo, mid - 1)  # search left (sorted half)
            else:
                return bs(mid + 1, hi)  # search right (unsorted half)

        # right half is sorted
        else:
            if nums[mid] < target <= nums[hi]:  # target is on the right
                return bs(mid + 1, hi)  # search right (sorted half)
            else:
                return bs(lo, mid - 1)  # search left (unsorted half)

    return bs(0, len(nums) - 1)


assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert search([4, 5, 6, 7, 0, 1, 2], 5) == 1
assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
assert search([1], 0) == -1
assert search([1], 1) == 0
assert search([40, 50, 60, 10, 20, 30], 10) == 3
assert search([3, 1], 1) == 1
assert search([5, 1, 3], 5) == 0
assert search([1, 2, 3, 4, 5], 3) == 2  # not actually rotated
