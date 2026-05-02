# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ - 35k likes (Apr/2026)
# %%
def max_profit(prices: list[int]) -> int:
    """
    O(n^2)
    Brute force solution
    """
    highest_profit = 0
    for i, buy_price in enumerate(prices):  # O(n)
        sell_price = max(prices[i:])  # O(n)
        profit = sell_price - buy_price
        highest_profit = max(highest_profit, profit)  # O(1)
    return highest_profit


def max_profit2(prices: list[int]):
    """
    O(n)
    Greedy solution

    It's one pass, it calculates the profit taking into account the buy price of the first element
    Along the way, if a lower buy price is found, it's used as the new buy price for the next elements
    """
    buy_price = prices[0]
    highest_profit = 0

    for sell_price in prices[1:]:  # O(n)
        profit = sell_price - buy_price
        highest_profit = max(highest_profit, profit)  # O(1)
        buy_price = min(buy_price, sell_price)  # O(1)

    return highest_profit


for fn in [max_profit, max_profit2]:
    assert fn([7, 1, 5, 3, 6, 4]) == 5
    assert fn([7, 6, 4, 3, 1]) == 0
