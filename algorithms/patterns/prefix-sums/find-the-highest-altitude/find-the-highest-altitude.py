# https://leetcode.com/problems/find-the-highest-altitude/ - 3k likes (Apr/2026)
# %%
import itertools


def largest_altitude(gain: list) -> int:
    current_altitude = 0
    max_altitude = 0
    for g in gain:
        current_altitude += g
        max_altitude = max(max_altitude, current_altitude)
    return max_altitude


def largest_altitude2(gain: list) -> int:
    return max(itertools.accumulate(gain, initial=0))


for fn in {largest_altitude, largest_altitude2}:
    assert fn([-5, 1, 5, 0, -7]) == 1
    assert fn([-4, -3, -2, -1, 4, 3, 2]) == 0
