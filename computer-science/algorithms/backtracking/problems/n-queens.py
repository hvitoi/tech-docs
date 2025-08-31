# https://leetcode.com/problems/n-queens/
# %%

# WIP
import unittest


def solve_n_queens(n):
    def can_place_a_queen(row, col):
        for i in range(n):
            # queen on horizontal
            if board[row][i] == "Q":
                return False

            # queen on vertical
            if board[i][col] == "Q":
                return False

            # queen on diagonal
            # if board[(row + i) % n][(col + i) % n] == "Q":
            #     return False
        return True

    def solve(row, col, queens_left):
        # all queens placed successfully
        if queens_left == 0:
            return True

        # board ended and not all queens were placed
        if row == n:
            return False

        # end of row
        if col == n:
            return solve(row + 1, 0, queens_left)

        # try to solve with the queen
        if can_place_a_queen(row, col):
            board[row][col] = "Q"
            if solve(row, col + 1, queens_left - 1):
                return True

            # if not possible, rollback
            else:
                board[row][col] = "."

        # try to solve without the queen
        return solve(row, col + 1, queens_left)

    board = [["." for _ in range(n)] for _ in range(n)]
    solve(0, 0, n)
    return board


test_case = unittest.TestCase()

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
