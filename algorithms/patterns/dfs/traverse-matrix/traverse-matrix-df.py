# %%

# See patterns/bfs/traverse-matrix/ for BFS implementation


def traverse_df(
    matrix: list[list],
    start: tuple[int, int],
):
    """
    Exhaust each direction first before trying the other
    """

    def traverse(pos: tuple[int, int]):
        row, col = pos
        if (
            pos in visited  #
            or not (0 <= row < len_rows)
            or not (0 <= col < len_cols)
        ):
            return

        acc.append(matrix[row][col])
        visited.add(pos)

        traverse((row, col - 1))  # left
        traverse((row - 1, col))  # up
        traverse((row, col + 1))  # right
        traverse((row + 1, col))  # down

        return acc

    len_rows = len(matrix)
    len_cols = len(matrix[0])
    visited = set()
    acc = []
    return traverse(start)


assert traverse_df(
    [
        ["a", "b", "c"],
        ["d", "e", "f"],
        ["g", "h", "i"],
    ],
    (1, 1),
) == ["e", "d", "a", "b", "c", "f", "i", "h", "g"]
