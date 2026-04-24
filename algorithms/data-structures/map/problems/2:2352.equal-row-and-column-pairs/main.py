# %%
import unittest
import copy
import collections
import functools


def transposed_grid(grid: list) -> list:
    grid_size = len(grid)
    inverted = copy.deepcopy(grid)
    for i in range(grid_size):
        for j in range(grid_size):
            inverted[i][j] = grid[j][i]
    return inverted


def equal_pairs(grid: list) -> int:
    rows = copy.deepcopy(grid)
    columns = transposed_grid(grid)

    n = 0
    for row in rows:
        for column in columns:
            if row == column:
                n += 1

    return n


def equal_pairs2(grid: list) -> int:
    rows = list(map(tuple, grid))
    columns = list(zip(*grid))

    return functools.reduce(
        lambda acc, el: acc + el - 1,
        collections.Counter(rows + columns).values(),
        0,
    )


test_case = unittest.TestCase()

for fn in {equal_pairs, equal_pairs2}:
    test_case.assertEqual(
        fn(
            [
                [3, 2, 1],
                [1, 7, 6],
                [2, 7, 7],
            ]
        ),
        1,
    )

    test_case.assertEqual(
        fn(
            [
                [3, 1, 2, 2],
                [1, 4, 4, 5],
                [2, 4, 2, 2],
                [2, 4, 2, 2],
            ]
        ),
        3,
    )
