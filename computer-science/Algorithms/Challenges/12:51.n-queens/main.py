# %%
from unittest import TestCase


def can_place_a_queen(board, row, col):
    n = len(board)
    for i in range(n):
        # queen on horizontal
        if board[row][i] == "Q":
            return False

        # queen on vertical
        if board[i][col] == "Q":
            return False

        # queen on diagonal
        # if board[(row + i + 1) % n][(col + i + 1) % n] == "Q":
        #     return False

    return True


def solve_n_queens(n):
    board = [["."] * n for _ in range(n)]

    def solve(row, col, queens_left):
        # all queens placed successfully
        if queens_left == 0:
            return True

        # board ended and not all queens were placed
        if row == n:
            return False

        # end of row
        if col == n:
            solve(row + 1, 0, queens_left)

        # try to place a queen and explore if it's possible
        if can_place_a_queen(board, row, col):
            board[row][col] = "Q"
            if solve(row, col + 1, queens_left - 1):
                return True

        # if not, rollback and try again (without)
        board[row][col] = "."
        return solve(row, col + 1, queens_left)

    solve(0, 0, n)

    return board


test_case = TestCase()

# test_case.assertEqual(
#     solve_n_queens(4),
#     [
#         [
#             [".", "Q", ".", "."],
#             [".", ".", ".", "Q"],
#             ["Q", ".", ".", "."],
#             [".", ".", "Q", "."],
#         ],
#         [
#             [".", ".", "Q", "."],
#             ["Q", ".", ".", "."],
#             [".", ".", ".", "Q"],
#             [".", "Q", ".", "."],
#         ],
#     ],
# )


solve_n_queens(4)
