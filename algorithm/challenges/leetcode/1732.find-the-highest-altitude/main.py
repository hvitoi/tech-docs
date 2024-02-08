# %%
import unittest
import itertools


def largest_altitude(gain: list) -> int:
    current_altitude = 0
    max_altitude = 0
    for g in gain:
        current_altitude += g
        max_altitude = max(max_altitude, current_altitude)
    return max_altitude


def largest_altitude2(gain: list) -> int:
    return max(
        itertools.accumulate(
            gain,
            lambda acc, el: acc + el,
            initial=0,
        ),
    )


test_case = unittest.TestCase()

for fn in {largest_altitude, largest_altitude2}:
    test_case.assertEqual(fn([-5, 1, 5, 0, -7]), 1)
    test_case.assertEqual(fn([-4, -3, -2, -1, 4, 3, 2]), 0)
