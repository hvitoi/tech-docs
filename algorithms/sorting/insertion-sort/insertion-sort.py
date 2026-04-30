# %%


def insertion_sort(col: list[int]) -> list[int]:
    for i in range(len(col)):
        for j in range(i, 0, -1):  # go left (except the first item)
            if col[j] < col[j - 1]:
                col[j], col[j - 1] = col[j - 1], col[j]  # bubble sort (inverted)
            else:
                break  # means it's in the right place (no need to go over the other elements)
    return col


assert insertion_sort([4, 5, 1, 3, 2]) == [1, 2, 3, 4, 5]
assert insertion_sort([]) == []
assert insertion_sort([1]) == [1]
assert insertion_sort([1, 1]) == [1, 1]
