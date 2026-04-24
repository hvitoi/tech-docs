# %%
import unittest
from functools import reduce


def area_between_two_lines(a: tuple, b: tuple) -> int:
    return (b[0] - a[0]) * min(a[1], b[1])


def max_area(heights: list) -> int:
    return max(
        reduce(
            lambda acc, el: max(acc, area_between_two_lines((i, h), el)),
            enumerate(heights),
            0,
        )
        for i, h in enumerate(heights)
    )


def max_area2(heights: list) -> int:
    bars = list(map(lambda el: (el[0] + 1, el[1]), enumerate(heights)))

    current_max = 0
    for i, a in enumerate(bars):
        for b in bars[i:]:
            current_max = max(current_max, area_between_two_lines(a, b))
    return current_max


test_case = unittest.TestCase()

for fn in {max_area, max_area2}:
    test_case.assertEqual(fn([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
    test_case.assertEqual(fn([1, 1]), 1)
