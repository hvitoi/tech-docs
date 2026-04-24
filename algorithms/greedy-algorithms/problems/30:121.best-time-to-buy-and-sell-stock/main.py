# %%
from unittest import TestCase


def max_profit(prices: list[int]) -> int:
    """O(n^2)"""
    highest_profit = 0
    for i, buy_price in enumerate(prices):
        for sell_price in prices[i:]:
            highest_profit = max(highest_profit, sell_price - buy_price)
    return highest_profit


def max_profit2(prices: list[int]):
    """O(n)"""
    buy_price = prices[0]
    highest_profit = 0

    for current_price in prices[1:]:
        highest_profit = max(highest_profit, current_price - buy_price)
        buy_price = min(buy_price, current_price)

    return highest_profit


test_case = TestCase()

for fn in {max_profit, max_profit2}:
    test_case.assertEqual(fn([7, 1, 5, 3, 6, 4]), 5)
    test_case.assertEqual(fn([7, 6, 4, 3, 1]), 0)
