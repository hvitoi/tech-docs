# %%
# 1. Our Choice: place 1-9 in an empty cell
# 2. Our Constraints: placement can't break the board (unique in the row, col and subgrid)
# 3. Our Goal: fill the board

from unittest import TestCase


def solve_sudoku(board: list[list[str]]) -> None:
    n = 9

    def is_valid(row, col, ch):
        row, col = int(row), int(col)

        for i in range(9):
            # unique in the column
            if board[i][col] == ch:
                return False

            # unique in the row
            if board[row][i] == ch:
                return False

            # unique in the subgrid
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == ch:
                return False

        return True

    def solve(row, col):
        # end of the board
        if row == n:
            return True

        # end of the row
        if col == n:
            return solve(row + 1, 0)

        # place already filled
        if board[row][col] != ".":
            return solve(row, col + 1)

        for i in range(1, 10):
            if is_valid(row, col, str(i)):
                # pick a valid placement
                board[row][col] = str(i)

                # explore if it's possible to solve with that
                if solve(row, col + 1):
                    return True

                # rollback if it's not
                board[row][col] = "."

        # invalid board
        return False

    solve(0, 0)


test_case = TestCase()

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