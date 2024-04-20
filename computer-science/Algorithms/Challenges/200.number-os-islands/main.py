# %%
from unittest import TestCase

# SOLUTION 1
# Tip 1: execute BF traversal on the matrix
# Tip 2: maintain a list of visited cells to avoid revisiting it
# Tip 3: if one level returns only Zeros, that means the previous island is done (and a new may start)

# SOLUTION 2
# Tip 1: execute a traversal (BF or DF)
# Tip 2: maintain a list of visited cells to avoid revisiting it
# Tip 3: during the traversal visit all the cells until a Zero is found


def number_of_islands_check_barriers(
    matrix: list[list],
    cells: set = None,
    nums_islands: int = 0,
    existing_island: bool = False,
) -> int:
    cells = cells if cells is not None else set([(0, 0)])

    if not matrix or not cells:
        return nums_islands

    rows = len(matrix)
    cols = len(matrix[0])

    level_has_land = False
    next_level_cells = set()

    while cells:
        pos = cells.pop()

        if matrix[pos[0]][pos[1]] == "1":
            level_has_land = True

        pos_right = (pos[0], pos[1] + 1)
        pos_down = (pos[0] + 1, pos[1])

        for next_pos in [pos_right, pos_down]:
            if (
                (next_pos not in next_level_cells)
                and (next_pos[0] < rows)
                and (next_pos[1] < cols)
            ):
                next_level_cells.add(next_pos)

    return number_of_islands_check_barriers(
        matrix,
        next_level_cells,
        nums_islands + 1 if (not existing_island) and level_has_land else nums_islands,
        level_has_land,
    )


test_case = TestCase()
test_case.assertEqual(
    number_of_islands_check_barriers(
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
    number_of_islands_check_barriers(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    ),
    3,
)

test_case.assertEqual(
    number_of_islands_check_barriers(
        [
            ["1", "1", "1", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["1", "0", "1", "1", "0"],
            ["0", "0", "1", "0", "1"],
        ]
    ),
    3,
)

test_case.assertEqual(
    number_of_islands_check_barriers(
        [
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "1"],
        ]
    ),
    1,
)
