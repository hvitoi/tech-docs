# %%


def quick_sort(col: list[int]) -> list[int]:
    def partition2(left: int, right: int) -> int:
        """
        Rearrange the arr, moving:
        - the elements smaller than the pivot to the left
        - the elements greater than the pivot to the right

        The pivot is arbitrarily chosen as the first one (left-most)
        """
        p = left
        i = right
        direction = "<-"

        while i != p:
            match direction:
                case "<-":
                    if col[i] < col[p]:
                        col[i], col[p] = col[p], col[i]
                        i, p = p, i
                        direction = "->"
                    else:
                        i -= 1
                case "->":
                    if col[i] > col[p]:
                        col[i], col[p] = col[p], col[i]
                        i, p = p, i
                        direction = "<-"
                    else:
                        i += 1
        return p

    def partition(left: int, right: int) -> int:
        """Lomuto partition"""
        pivot_value = col[right]  # pivot is the rightmost el (convention, could be any)
        pivot_index = left  # initial pivot index, elements to the left of this index (exclusive) should be lower than the pivot value

        for i in range(left, right):  # excludes the last element (the pivot)
            if col[i] <= pivot_value:
                col[pivot_index], col[i] = col[i], col[pivot_index]
                pivot_index += 1

        # Bring pivot to the correct position
        col[pivot_index], col[right] = col[right], col[pivot_index]

        # return the pivot's final resting position
        return pivot_index

    def qs(left: int, right: int) -> None:
        if (right - left) <= 0:
            return

        # after that, the pivot element is guaranteed to be in the right place (the pivot index)
        pivot_index = partition(left, right)

        qs(left, pivot_index - 1)
        qs(pivot_index + 1, right)

    qs(0, len(col) - 1)
    return col


assert quick_sort([4, 5, 1, 3, 2]) == [1, 2, 3, 4, 5]
assert quick_sort([]) == []
assert quick_sort([1]) == [1]
assert quick_sort([1, 1]) == [1, 1]
