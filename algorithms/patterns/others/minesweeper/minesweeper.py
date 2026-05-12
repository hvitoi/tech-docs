# Create a function or class to print a matrix of size x * x.
# Fill it with y mines.
#
# Mark mines as 'x' and mark empty cells as '0'.
# Mines should be randomly distributed
#
# e.g. a possible result of minesweeper_generator(size=4, mines=5) could be:
# [
#   ['0', '0', 'x', 'x'],
#   ['x', '0', '0', '0'],
#   ['0', '0', '0', '0'],
#   ['0', 'x', '0', 'x']
# ]

import random
import unittest


def minesweeper_generator(n: int, mines: int) -> list[list[str]]:

    if mines > n * n:
        raise ValueError("There are more mines than fields")

    if mines <= 0:
        raise ValueError("There should be at least one mine")

    # Initialize empty grid
    grid = [["0"] * n for _ in range(n)]

    # Place mines into the grid
    mines_placed = 0
    while mines_placed != mines:
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)

        if grid[i][j] != "x":
            grid[i][j] = "x"
            mines_placed += 1

    # Populate the number of neighboring mines
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "x":
                continue
            neighbors = [
                (i, j - 1),
                (i, j + 1),
                (i - 1, j),
                (i - 1, j - 1),
                (i - 1, j + 1),
                (i + 1, j),
                (i + 1, j - 1),
                (i + 1, j + 1),
            ]
            counter = 0
            for neighbor in neighbors:
                a, b = neighbor
                if (a < 0 or a >= n) or (b < 0 or b >= n):
                    continue
                if grid[a][b] == "x":
                    counter += 1
            grid[i][j] = str(counter)

    return grid


class TestMineSweeper(unittest.TestCase):
    def test_placing_mines(self):
        mines = 10
        n = 10
        grid = minesweeper_generator(n, mines)
        mines_found = len([el for row in grid for el in row if el == "x"])
        self.assertEqual(mines_found, mines)


if __name__ == "__main__":
    for row in minesweeper_generator(5, 3):
        print(row)
    unittest.main()
