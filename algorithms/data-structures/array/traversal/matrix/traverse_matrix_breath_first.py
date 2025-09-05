# %%
from collections import deque
from unittest import TestCase


def traverse_bf(matrix: list[list], start_row: int, start_col: int):
    """ """
    len_rows = len(matrix)
    len_cols = len(matrix[0])

    acc = []
    queue = deque([(start_row, start_col)])
    visited = set()

    while queue:
        row, col = queue.popleft()

        if (
            (row, col) in visited
            or not (0 <= row < len_rows)
            or not (0 <= col < len_cols)
        ):
            continue

        acc.append(matrix[row][col])
        visited.add((row, col))

        positions = [
            (row, col - 1),  # left
            (row - 1, col),  # up
            (row, col + 1),  # right
            (row + 1, col),  # down
        ]

        queue.extend(positions)
        # could be optimized by not adding elements that are not necessary
        # instead of filtering them in the base case

    return acc


test_case = TestCase()

# From the middle
test_case.assertEqual(
    traverse_bf(
        [
            ["a", "b", "c"],
            ["d", "e", "f"],
            ["g", "h", "i"],
        ],
        1,
        1,
    ),
    ["e", "d", "b", "f", "h", "a", "g", "c", "i"],
)

# From origin
test_case.assertEqual(
    traverse_bf(
        [
            ["a", "b"],
            ["c", "d"],
        ],
        0,
        0,
    ),
    ["a", "b", "c", "d"],
)
test_case.assertEqual(
    traverse_bf(
        [
            ["a", "b", "c"],
            ["d", "e", "f"],
            ["g", "h", "i"],
        ],
        0,
        0,
    ),
    ["a", "b", "d", "c", "e", "g", "f", "h", "i"],
)
test_case.assertEqual(
    traverse_bf(
        [
            ["a", "b", "c"],
            ["d", "e", "f"],
            ["g", "h", "i"],
            ["j", "k", "l"],
        ],
        0,
        0,
    ),
    ["a", "b", "d", "c", "e", "g", "f", "h", "j", "i", "k", "l"],
)
