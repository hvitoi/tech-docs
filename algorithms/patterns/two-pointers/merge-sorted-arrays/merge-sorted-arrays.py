# https://leetcode.com/problems/merge-sorted-array/ - 19k likes (Apr/2026)
# %%

# It's the same algorithm applied in merge sort


def merge_sorted_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    merged = []
    i = j = 0
    while (i < len(arr1)) or (j < len(arr2)):
        el1 = arr1[i] if i < len(arr1) else float("inf")  # make a sentinel if empty
        el2 = arr2[j] if j < len(arr2) else float("inf")  # make a sentinel if empty

        if el1 <= el2:
            merged.append(el1)
            i += 1
        else:
            merged.append(el2)
            j += 1

    return merged


assert merge_sorted_arrays([0, 3, 4, 31], [4, 6, 30]) == [0, 3, 4, 4, 6, 30, 31]
assert merge_sorted_arrays([], [4, 6, 30]) == [4, 6, 30]
assert merge_sorted_arrays([1, 2, 3], [2, 5, 6]) == [1, 2, 2, 3, 5, 6]


# %%


def merge_sorted_arrays_in_place(
    arr1: list[int],
    m: int,
    arr2: list[int],
    n: int,
) -> None:
    """Modify arr1 in-place. arr1 has length m+n; last n slots are placeholders."""

    i = m - 1
    j = n - 1
    k = m + n - 1

    while j >= 0:
        el1 = arr1[i]
        el2 = arr2[j]

        # i >= 0 is necessary to check if the arr1 has not been exhausted yet
        if i >= 0 and el1 >= el2:
            arr1[k] = el1
            i -= 1
        else:
            arr1[k] = el2
            j -= 1

        k -= 1


nums = [0, 3, 4, 31, 0, 0, 0]
merge_sorted_arrays_in_place(nums, 4, [4, 6, 30], 3)
assert nums == [0, 3, 4, 4, 6, 30, 31]

nums = [9, 10, 0, 0]
merge_sorted_arrays_in_place(nums, 2, [1, 2], 2)
assert nums == [1, 2, 9, 10]
