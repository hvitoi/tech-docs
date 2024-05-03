# %%
from unittest import TestCase


def coin_change_pick_highest_coins_first(coins: list[int], amount: int) -> int:
    """
    Priority = higher bills! (less coins returned)
    """
    number_of_coins = 0

    while len(coins) > 0:
        higher_bill = coins[-1]

        if amount == 0:
            return number_of_coins

        if amount >= higher_bill:
            number_of_coins += 1
            amount -= higher_bill
            continue

        if amount < higher_bill:
            coins.pop()
            continue

    return -1


def coin_change_backtrack_every_combination(coins: list[int], amount: int) -> int:
    """
    Dynamic programming solution
    It tracks every possible combination at every choice (which bill to pick)
    This is done until the change amount is 0 or if there is no possible combination
    """
    if amount == 0:
        return 0

    options = []

    for coin in coins:
        if amount >= coin:
            next_coins = coin_change_backtrack_every_combination(coins, amount - coin)
            if next_coins == -1:
                return -1  # that means there is no possible combination going this path
            options.append(1 + next_coins)

    return min(options) if options else -1


test_case = TestCase()

for fn in {
    coin_change_pick_highest_coins_first,
    coin_change_backtrack_every_combination,
}:
    test_case.assertEqual(fn([1, 2, 5], 11), 3)
    test_case.assertEqual(fn([2], 3), -1)
    test_case.assertEqual(fn([1], 0), 0)
