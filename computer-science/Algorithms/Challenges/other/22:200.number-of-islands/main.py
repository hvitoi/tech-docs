# %%
from unittest import TestCase

# SOLUTION 1
# Step 1: execute BF traversal on the matrix
# Step 2: maintain a list of visited cells to avoid revisiting it
# Step 3: if one level returns only Zeros, that means the previous island is done (and a new may start)

# SOLUTION 2
# Step 1: execute BF traversal on the matrix
# Step 2: maintain a list of visited cells to avoid revisiting it
# Step 3: iterate over all the elements of the matrix (skipping already visited cells)
# Step 3: during the traversal visit all the cells until a Zero is found


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


def number_of_islands_explore_islands(matrix: list[list]) -> int:
    rows = len(matrix)
    cols = len(matrix[0])
    cells_visited: set[tuple[int, int]] = set()
    number_of_islands = 0

    def explore_island_bf(initial_pos: tuple[int, int]):
        cells_to_explore = {initial_pos}
        while cells_to_explore:
            i, j = cells_to_explore.pop()
            cells_visited.add((i, j))

            pos_left = (i, j - 1)
            pos_right = (i, j + 1)
            pos_up = (i - 1, j)
            pos_down = (i + 1, j)

            for next_i, next_j in {pos_left, pos_right, pos_up, pos_down}:
                if (
                    next_i >= 0
                    and next_i < rows
                    and next_j >= 0
                    and next_j < cols
                    and (next_i, next_j) not in cells_visited
                    and (next_i, next_j) not in cells_to_explore
                    and matrix[next_i][next_j] == "1"
                ):
                    cells_to_explore.add((next_i, next_j))

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "1" and (i, j) not in cells_visited:
                number_of_islands += 1
                explore_island_bf((i, j))
    return number_of_islands


test_case = TestCase()

for fn in {number_of_islands_check_barriers, number_of_islands_explore_islands}:
    test_case.assertEqual(
        fn(
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
        fn(
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
        fn(
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
        fn(
            [
                ["0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "1"],
            ]
        ),
        1,
    )
