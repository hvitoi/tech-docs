# %%
from unittest import TestCase


def traverse_df(matrix: list[list], start_row: int, start_col: int):
    """
    Exhaust each direction first before trying the other
    """

    def traverse(row, col):
        if (
            (row, col) in visited
            or not (0 <= row < len_rows)
            or not (0 <= col < len_cols)
        ):
            return []

        acc.append(matrix[row][col])
        visited.add((row, col))

        traverse(row, col - 1)  # left
        traverse(row - 1, col)  # up
        traverse(row, col + 1)  # right
        traverse(row + 1, col)  # down

        return acc

    len_rows = len(matrix)
    len_cols = len(matrix[0])
    visited = set()
    acc = []
    return traverse(start_row, start_col)


test_case = TestCase()

test_case.assertEqual(
    traverse_df(
        [
            ["a", "b", "c"],
            ["d", "e", "f"],
            ["g", "h", "i"],
        ],
        1,
        1,
    ),
    ["e", "d", "a", "b", "c", "f", "i", "h", "g"],
)
