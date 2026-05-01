# %%


def bubble_sort(col: list[int]) -> list[int]:
    for i in range(len(col)):
        for j in range(len(col) - 1 - i):
            if col[j] > col[j + 1]:
                col[j], col[j + 1] = col[j + 1], col[j]
    return col


assert bubble_sort([4, 5, 1, 3, 2]) == [1, 2, 3, 4, 5]
assert bubble_sort([]) == []
assert bubble_sort([1]) == [1]
assert bubble_sort([1, 1]) == [1, 1]
