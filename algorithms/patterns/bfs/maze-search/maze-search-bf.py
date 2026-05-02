# These implementations use BFS. For DFS/backtracking, see patterns/backtracking/maze-search/
# %%
from collections import deque

# With BFS, you are guaranteed to find the fastest route first, because it's a level by level search


def search_maze_bfs_returning_bool(
    maze: list[list],
    start: tuple[int, int],
    goal: tuple[int, int],
) -> int:
    """
    Returns true when a solution path is found. And it's guaranteed to be the fastest path
    """
    len_rows = len(maze)
    len_cols = len(maze[0])

    queue = deque([start])
    visited = set()

    while queue:
        pos = queue.popleft()
        row, col = pos

        if (
            pos in visited
            or (not 0 <= row < len_rows)
            or (not 0 <= col < len_cols)
            or maze[row][col] == 1
        ):
            continue  # don't go that route

        if pos == goal:
            return True

        visited.add(pos)

        next_level_positions = [
            (row, col - 1),  # left
            (row - 1, col),  # up
            (row, col + 1),  # right
            (row + 1, col),  # down
        ]
        queue.extend(next_level_positions)

    return False


assert (
    search_maze_bfs_returning_bool(
        [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
        ],
        (0, 0),
        (2, 0),
    )
    is True
)

assert (
    search_maze_bfs_returning_bool(
        [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
        ],
        (0, 0),
        (2, 0),
    )
    is False
)


# %%
def search_maze_bfs_returning_length(
    maze: list[list],
    start: tuple[int, int],
    goal: tuple[int, int],
) -> int:
    """
    In order to return the length of the solution, it's necessary to keep
    track of which level we are currently in
    """
    len_rows = len(maze)
    len_cols = len(maze[0])

    queue = deque([(start, 0)])
    visited = set()

    while queue:
        pos, level = queue.popleft()
        row, col = pos

        if (
            pos in visited
            or (not 0 <= row < len_rows)
            or (not 0 <= col < len_cols)
            or maze[row][col] == 1
        ):
            continue  # don't go that route

        if pos == goal:
            return level

        visited.add(pos)

        next_level_positions = [
            ((row - 1, col), level + 1),  # up
            ((row, col + 1), level + 1),  # right
            ((row + 1, col), level + 1),  # down
            ((row, col - 1), level + 1),  # left
        ]
        queue.extend(next_level_positions)

    return -1


assert (
    search_maze_bfs_returning_length(
        [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
        ],
        (0, 0),
        (2, 0),
    )
    == 2
)
assert (
    search_maze_bfs_returning_length(
        [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
        ],
        (0, 0),
        (2, 0),
    )
    == -1
)
