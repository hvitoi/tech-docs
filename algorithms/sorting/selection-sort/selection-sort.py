# %%


def selection_sort(col: list[int]) -> list[int]:
    for i in range(len(col)):
        for j in range(i, len(col)):
            if col[i] > col[j]:
                col[i], col[j] = col[j], col[i]
    return col


assert selection_sort([4, 5, 1, 3, 2]) == [1, 2, 3, 4, 5]
assert selection_sort([]) == []
assert selection_sort([1]) == [1]
assert selection_sort([1, 1]) == [1, 1]
