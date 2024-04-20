# %%
from typing import List
from unittest import TestCase


def max_profit(prices: List[int]) -> int:
    highest_gain = 0
    for i, min_price in enumerate(prices):
        for max_price in prices[i:]:
            highest_gain = max(highest_gain, max_price - min_price)
    return highest_gain


def max_profit2(prices: List[int]):
    min_price = prices[0]
    max_profit = 0

    for price in prices[1:]:
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)

    return max_profit


test_case = TestCase()

for fn in {max_profit, max_profit2}:
    test_case.assertEqual(fn([7, 1, 5, 3, 6, 4]), 5)
    test_case.assertEqual(fn([7, 6, 4, 3, 1]), 0)
