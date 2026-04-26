# %%


def merge_sort(arr: list):
    if len(arr) <= 1:
        return arr

    # sort each part. Recurses a maximum of log(n) levels
    mid_index = len(arr) // 2
    sorted_left = merge_sort(arr[:mid_index])
    sorted_right = merge_sort(arr[mid_index:])

    # concatenate the two parts in the correct order
    if sorted_left[-1] <= sorted_right[0]:
        return sorted_left + sorted_right
    else:
        return sorted_right + sorted_left


assert merge_sort([4, 5, 1, 3, 2]) == [1, 2, 3, 4, 5]
assert merge_sort([]) == []
assert merge_sort([1]) == [1]
assert merge_sort([1, 1]) == [1, 1]
