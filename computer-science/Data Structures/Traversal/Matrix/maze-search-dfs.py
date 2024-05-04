# %%

# With BFS you are guaranteed to find the shortest path, but may take longer to find
# With DFS you are guaranteed to find a path faster, but may not be the shortest
# With DFS you can also apply backtracking, this way you will also guarantee to have the shortest path

from unittest import TestCase


def search_maze_dfs_return_bool(
    maze: list[list], start: tuple[int, int], goal: tuple[int, int]
) -> bool:
    def search(row, col):
        if (
            (row, col) in visited
            or (not 0 <= row < len_rows)
            or (not 0 <= col < len_cols)
            or maze[row][col] == 1
        ):
            return False

        visited.add((row, col))

        if (row, col) == goal:
            return True

        next_positions = [
            (row - 1, col),  # up
            (row, col + 1),  # right
            (row + 1, col),  # down
            (row, col - 1),  # left
        ]

        for pos in next_positions:
            if search(*pos):
                return True

        return False

    len_rows = len(maze)
    len_cols = len(maze[0])
    visited = set()
    return search(*start)


test_case = TestCase()

test_case.assertEqual(
    search_maze_dfs_return_bool(
        [
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0],
        ],
        (0, 4),
        (4, 4),
    ),
    True,
)

test_case.assertEqual(
    search_maze_dfs_return_bool(
        [
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
        ],
        (0, 4),
        (4, 4),
    ),
    False,
)


# %%
def search_maze_dfs_return_length(
    maze: list[list], start: tuple[int, int], goal: tuple[int, int]
) -> int:
    def search(row, col):
        if (
            (row, col) in visited
            or (not 0 <= row < len_rows)
            or (not 0 <= col < len_cols)
            or maze[row][col] == 1
        ):
            return -1

        if (row, col) == goal:
            return 0

        visited.add((row, col))

        next_positions = [
            (row - 1, col),  # up
            (row, col + 1),  # right
            (row + 1, col),  # down
            (row, col - 1),  # left
        ]

        for pos in next_positions:
            path_length = search(*pos)
            if path_length != -1:
                return 1 + path_length

        return -1

    len_rows = len(maze)
    len_cols = len(maze[0])
    visited = set()
    return search(*start)


test_case = TestCase()

test_case.assertEqual(
    search_maze_dfs_return_length(
        [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
        ],
        (0, 0),
        (2, 0),
    ),
    8,  # not the shortest solution, but a solution
)

test_case.assertEqual(
    search_maze_dfs_return_length(
        [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
        ],
        (0, 0),
        (2, 0),
    ),
    -1,
)


# %%
def search_maze_dfs_backtracking(
    maze: list[list], start: tuple[int, int], goal: tuple[int, int]
) -> int:
    def search(row, col):
        if (
            (row, col) in visited
            or (not 0 <= row < len_rows)
            or (not 0 <= col < len_cols)
            or maze[row][col] == 1
        ):
            return -1

        if (row, col) == goal:
            return 0

        visited.add((row, col))

        next_positions = [
            (row - 1, col),  # up
            (row, col + 1),  # right
            (row + 1, col),  # down
            (row, col - 1),  # left
        ]

        paths = []
        for pos in next_positions:
            path = search(*pos)
            if path != -1:
                paths.append(path + 1)

        return min(paths) if paths else -1

    len_rows = len(maze)
    len_cols = len(maze[0])
    visited = set()
    return search(*start)


test_case = TestCase()

test_case.assertEqual(
    search_maze_dfs_backtracking(
        [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
        ],
        (0, 0),
        (2, 0),
    ),
    2,
)

test_case.assertEqual(
    search_maze_dfs_backtracking(
        [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
        ],
        (0, 0),
        (2, 0),
    ),
    -1,
)


# %%
def search_maze_dfs_return_path(
    maze: list[list], start: tuple[int, int], goal: tuple[int, int]
) -> list[tuple[int, int]]:
    def search(row, col):
        if (
            (row, col) in visited
            or (not 0 <= row < len_rows)
            or (not 0 <= col < len_cols)
            or maze[row][col] == 1
        ):
            return []

        if (row, col) == goal:
            return [(row, col)]

        visited.add((row, col))

        next_positions = [
            (row - 1, col),  # up
            (row, col + 1),  # right
            (row + 1, col),  # down
            (row, col - 1),  # left
        ]

        for pos in next_positions:
            path = search(*pos)
            if path:
                return [(row, col)] + path

        return []

    len_rows = len(maze)
    len_cols = len(maze[0])
    visited = set()
    return search(*start)


test_case = TestCase()

test_case.assertEqual(
    search_maze_dfs_return_path(
        [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
        ],
        (0, 0),
        (2, 0),
    ),
    [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 2), (2, 1), (2, 0)],
)

test_case.assertEqual(
    search_maze_dfs_return_path(
        [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
        ],
        (0, 0),
        (2, 0),
    ),
    [],
)
