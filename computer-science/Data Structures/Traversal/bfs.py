# %%
from collections import deque
from unittest import TestCase


def traverse_breadth_first_in_matrix(matrix: list[list]) -> list:
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


def traverse_breadth_first_matrix_recursive(
    matrix: list[list],
    queue: deque = None,
    acc: list = None,
) -> list:
    """Recursively processing of each level of the matrix"""
    acc = acc if acc else []
    queue = queue if queue is not None else deque([(0, 0)])

    if not matrix or not queue:
        return acc

    rows = len(matrix)
    cols = len(matrix[0])

    next_level_queue = deque()
    next_level_items = set()

    while queue:
        pos = queue.popleft()
        acc.append(matrix[pos[0]][pos[1]])

        pos_right = (pos[0], pos[1] + 1)
        pos_down = (pos[0] + 1, pos[1])

        for next_pos in [pos_right, pos_down]:
            if (
                (next_pos not in next_level_items)
                and (next_pos[0] < rows)
                and (next_pos[1] < cols)
            ):
                next_level_queue.append(next_pos)
                next_level_items.add(next_pos)

    return traverse_breadth_first_matrix_recursive(matrix, next_level_queue, acc)


test_case = TestCase()

for fn in {traverse_breadth_first_in_matrix, traverse_breadth_first_matrix_recursive}:
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
