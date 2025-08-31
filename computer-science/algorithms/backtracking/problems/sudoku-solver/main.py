# https://leetcode.com/problems/sudoku-solver/
# %%

import unittest


def solve_sudoku(board: list[list[str]]) -> None:
    """
    1. Choice: place 1-9 in an empty cell
    2. Constraints: placement can't break the board (unique in the row, col and subgrid)
    3. Goal: fill the board
    """
    N = 9

    def is_valid(row, col, choice):
        row, col = int(row), int(col)

        for i in range(9):
            # unique in the column
            if board[i][col] == choice:
                return False

            # unique in the row
            if board[row][i] == choice:
                return False

            # unique in the subgrid
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == choice:
                return False

        return True

    def solve(row, col):
        # end of the board
        if row == N:
            return True

        # end of the row
        if col == N:
            return solve(row + 1, 0)

        # skip if place already filled
        if board[row][col] != ".":
            return solve(row, col + 1)

        # The choice: place 1-9
        for i in range(1, 10):
            choice = str(i)
            # The constraint: can't break the board
            if is_valid(row, col, choice):
                # pick the valid placement
                board[row][col] = choice

                # The goal: fill the board
                # explore if it's possible to solve the rest of the board with that
                if solve(row, col + 1):
                    return True

                # rollback if it's not
                board[row][col] = "."

        # invalid board
        return False

    solve(0, 0)


test_case = unittest.TestCase()

board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

solve_sudoku(board)

test_case.assertEqual(
    board,
    [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"],
    ],
)
