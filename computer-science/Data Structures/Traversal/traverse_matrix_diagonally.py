# %%
from collections import deque
from unittest import TestCase


def traverse_matrix_diag(matrix: list[list]) -> list:
    acc = []

    if not matrix:
        return acc

    len_rows = len(matrix)
    len_cols = len(matrix[0])

    queue = deque([(0, 0)])
    queue_items = {(0, 0)}  # to avoid inserting duplicate items to the queue O(1)

    while queue:
        row, col = queue.popleft()
        acc.append(matrix[row][col])

        pos_right = (row, col + 1)
        pos_down = (row + 1, col)

        for next_pos in [pos_right, pos_down]:
            if (
                (next_pos not in queue_items)
                and (next_pos[0] < len_rows)
                and (next_pos[1] < len_cols)
            ):
                queue.append(next_pos)
                queue_items.add(next_pos)

    return acc


def traverse_matrix_diag_recursive(
    matrix: list[list],
    queue: deque = None,
    acc: list = None,
) -> list:
    """
    The quantity of levels is m + n
    """

    def first_item_from_level(level):
        col = level if level < len_cols else len_cols - 1
        row = 0 if level < len_cols else level - len_cols + 1
        return row, col

    def bfs(level):
        if level > (len_rows + len_cols):
            return []

        acc = []
        row, col = first_item_from_level(level)

        while (0 <= row < len_rows) and (0 <= col < len_cols):
            acc.append(matrix[row][col])
            row = row + 1
            col = col - 1

        return acc + bfs(level + 1)

    len_rows = len(matrix)
    len_cols = len(matrix[0])
    return bfs(0)


test_case = TestCase()

for fn in {traverse_matrix_diag, traverse_matrix_diag_recursive}:
    test_case.assertEqual(
        fn(
            [
                ["a", "b"],
                ["c", "d"],
            ]
        ),
        ["a", "b", "c", "d"],
    )
    test_case.assertEqual(
        fn(
            [
                ["a", "b", "c"],
                ["d", "e", "f"],
                ["g", "h", "i"],
            ]
        ),
        ["a", "b", "d", "c", "e", "g", "f", "h", "i"],
    )
    test_case.assertEqual(
        fn(
            [
                ["a", "b", "c"],
                ["d", "e", "f"],
                ["g", "h", "i"],
                ["j", "k", "l"],
            ]
        ),
        ["a", "b", "d", "c", "e", "g", "f", "h", "j", "i", "k", "l"],
    )
