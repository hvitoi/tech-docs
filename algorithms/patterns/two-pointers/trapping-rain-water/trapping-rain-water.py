# https://leetcode.com/problems/trapping-rain-water/ - 36k likes (Apr/2026)
# %%


def trap(bars: list[int]) -> int:
    trapped_water = 0
    for water_level in range(1, max(bars) + 1):
        bars_above_height = [bar >= water_level for bar in bars]
        left_border = bars_above_height.index(True)
        right_border = len(bars) - 1 - bars_above_height[::-1].index(True)
        trapped_water += bars_above_height[left_border + 1 : right_border].count(False)
    return trapped_water


assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
assert trap([4, 2, 0, 3, 2, 5]) == 9
