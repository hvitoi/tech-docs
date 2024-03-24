# %%
from typing import List
from unittest import TestCase


def trap(bars: List[int]) -> int:
    highest_bar = max(bars)
    trapped_water = 0
    for water_level in range(1, highest_bar + 1):
        bars_above_height = [bar >= water_level for bar in bars]
        left_border = bars_above_height.index(True)
        right_border = len(bars) - 1 - bars_above_height[::-1].index(True)
        trapped_water += bars_above_height[left_border + 1 : right_border].count(False)
    return trapped_water


test_case = TestCase()

test_case.assertEqual(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
test_case.assertEqual(trap([4, 2, 0, 3, 2, 5]), 9)
