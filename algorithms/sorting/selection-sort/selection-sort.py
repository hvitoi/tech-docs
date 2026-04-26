# %%


def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


assert selection_sort([4, 5, 1, 3, 2]) == [1, 2, 3, 4, 5]
assert selection_sort([]) == []
assert selection_sort([1]) == [1]
assert selection_sort([1, 1]) == [1, 1]
