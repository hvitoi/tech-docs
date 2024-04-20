# %%

from collections import deque
from unittest import TestCase

# Tip 1: execute BF traversal on the matrix
# Tip 2: if one level returns only Zeros, that means the previous island is done (and a new may start)


def number_of_islands(
    matrix: list[list],
    queue: deque = None,
    islands: int = 0,
    existing_island: bool = False,
) -> int:
    queue = queue if queue is not None else deque([(0, 0)])

    if not matrix or not queue:
        return islands

    rows = len(matrix)
    cols = len(matrix[0])

    next_level_queue = deque()
    next_level_items = set()

    level_has_land = False

    while queue:
        pos = queue.popleft()

        if matrix[pos[0]][pos[1]] == "1":
            level_has_land = True

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

    return number_of_islands(
        matrix,
        next_level_queue,
        islands + 1 if (not existing_island) and level_has_land else islands,
        level_has_land,
    )


test_case = TestCase()
test_case.assertEqual(
    number_of_islands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    ),
    1,
)
test_case.assertEqual(
    number_of_islands(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    ),
    3,
)
