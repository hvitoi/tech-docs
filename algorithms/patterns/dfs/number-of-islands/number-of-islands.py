# https://leetcode.com/problems/number-of-islands/ - 25k likes (Apr/2026)
# %%

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
    cells: set | None = None,
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


def number_of_islands_dfs_recursive(matrix: list[list[str]]) -> int:
    """
    SOLUTION 3 — classical recursive DFS
    - Scan every cell. When an unvisited "1" is found, it is the seed of a new island
      so increment the count and DFS-flood the whole connected component.
    - Recursion gives depth-first behaviour for free: each call dives along one
      neighbour all the way before returning to explore the next direction.
    - Mark cells visited at the start of dfs() (before recursing) so a cell is never
      processed twice.

    Time:  O(rows * cols) — every cell is visited at most once.
    Space: O(rows * cols) worst case for the visited set and the recursion stack
           (a snake-shaped island fills the whole grid → recursion depth = rows*cols,
           which can blow Python's default recursion limit on large inputs).
    """
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    visited: set[tuple[int, int]] = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def explore_island(i: int, j: int) -> None:
        """
        Visit all the points inside of an island
        """
        if (
            i < 0
            or i >= rows
            or j < 0
            or j >= cols
            or matrix[i][j] != "1"
            or (i, j) in visited
        ):
            return
        visited.add((i, j))
        for di, dj in directions:
            explore_island(i + di, j + dj)

    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "1" and (i, j) not in visited:
                count += 1
                explore_island(i, j)
    return count


def number_of_islands_dfs_iterative(matrix: list[list[str]]) -> int:
    """
    SOLUTION 4 — iterative DFS with an explicit stack
    Same shape as BFS but with a list used as a LIFO stack (.append / .pop) instead
    of a FIFO queue. Avoids the recursion depth limit on snake-shaped inputs and is
    the production-safe variant of SOLUTION 3.
    """
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    visited: set[tuple[int, int]] = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def explore_island(start: tuple[int, int]) -> None:
        stack: list[tuple[int, int]] = [start]
        visited.add(start)
        while stack:
            i, j = stack.pop()
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (
                    0 <= ni < rows
                    and 0 <= nj < cols
                    and matrix[ni][nj] == "1"
                    and (ni, nj) not in visited
                ):
                    visited.add((ni, nj))
                    stack.append((ni, nj))

    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "1" and (i, j) not in visited:
                count += 1
                explore_island((i, j))
    return count


for fn in [
    number_of_islands_check_barriers,
    number_of_islands_explore_islands,
    number_of_islands_dfs_recursive,
    number_of_islands_dfs_iterative,
]:
    assert (
        fn(
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        )
        == 1
    )
    assert (
        fn(
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        )
        == 3
    )

    assert (
        fn(
            [
                ["1", "1", "1", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["1", "0", "1", "1", "0"],
                ["0", "0", "1", "0", "1"],
            ]
        )
        == 3
    )

    assert (
        fn(
            [
                ["0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
                ["0", "0", "0", "0", "1"],
            ]
        )
        == 1
    )
