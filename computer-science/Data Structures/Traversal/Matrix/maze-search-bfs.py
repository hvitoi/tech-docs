# %%
from collections import deque
from unittest import TestCase

# With BFS you are guaranteed to find the shortest path, but may take longer to find
# With DFS you are guaranteed to find a path faster, but may not be the shortest
# With DFS you can also apply backtracking, this way you will also guarantee to have the shortest path


def search_maze_bfs_returning_bool(
    maze: list[list], start: tuple[int, int], goal: tuple[int, int]
) -> int:
    """
    Breadth-first solution
    """
    len_rows = len(maze)
    len_cols = len(maze[0])

    queue = deque([(start[0], start[1])])
    visited = set()

    while queue:
        row, col = queue.popleft()

        if (
            (row, col) in visited
            or (not 0 <= row < len_rows)
            or (not 0 <= col < len_cols)
            or maze[row][col] == 1
        ):
            continue

        if (row, col) == goal:
            return True

        visited.add((row, col))

        next_level_positions = [
            (row, col - 1),  # left
            (row - 1, col),  # up
            (row, col + 1),  # right
            (row + 1, col),  # down
        ]
        queue.extend(next_level_positions)

    return False


test_case = TestCase()

test_case.assertEqual(
    search_maze_bfs_returning_bool(
        [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
        ],
        (0, 0),
        (2, 0),
    ),
    True,
)

test_case.assertEqual(
    search_maze_bfs_returning_bool(
        [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
        ],
        (0, 0),
        (2, 0),
    ),
    False,
)

# %%


def search_maze_bfs(
    maze: list[list], start: tuple[int, int], goal: tuple[int, int]
) -> int:
    """
    In order to return the length of the solution, it's necessary to keep
    track of which level we are currently in
    """
    len_rows = len(maze)
    len_cols = len(maze[0])

    queue = deque(
        [
            deque([(start[0], start[1])]),  # level 0
        ]
    )
    visited = set()

    level = 0

    while queue:
        # if there is nothing more in the current level
        if not queue[0]:
            queue.popleft()  # pop the empty level
            level += 1
            continue

        row, col = queue[0].popleft()

        if (
            (row, col) in visited
            or (not 0 <= row < len_rows)
            or (not 0 <= col < len_cols)
            or maze[row][col] == 1
        ):
            continue

        if (row, col) == goal:
            return level

        visited.add((row, col))

        next_level_positions = [
            (row - 1, col),  # up
            (row, col + 1),  # right
            (row + 1, col),  # down
            (row, col - 1),  # left
        ]
        queue.append(deque(next_level_positions))

    return -1


test_case = TestCase()

test_case.assertEqual(
    search_maze_bfs(
        [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
        ],
        (0, 0),
        (2, 0),
    ),
    None,
)

# test_case.assertEqual(
#     search_maze_bfs(
#         [
#             [0, 0, 0, 0],
#             [1, 1, 1, 1],
#             [0, 0, 0, 0],
#         ],
#         (0, 0),
#         (2, 0),
#     ),
#     -1,
# )
