# %%
from unittest import TestCase


def coin_change(coins: list[int], amount: int) -> int:
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


def coin_change_dp(coins: list[int], amount: int) -> int:
    if amount == 0:
        return 0

    if len(coins) == 0:
        return -1

    higher_bill = coins[-1]

    if amount >= higher_bill:
        next_coins = coin_change_dp(coins, amount - higher_bill)
        return 1 + next_coins if next_coins != -1 else -1

    if amount < higher_bill:
        next_coins = coin_change_dp(coins[:-1], amount)
        return next_coins if next_coins != -1 else -1


def coin_change_backtrack_every_combination(coins: list[int], amount: int) -> int:
    if amount == 0:
        return 0

    options = []

    for coin in coins:
        if amount >= coin:
            next_coins = coin_change_backtrack_every_combination(coins, amount - coin)
            if next_coins == -1:
                return -1
            options.append(1 + next_coins)

    return min(options) if options else -1


test_case = TestCase()

for fn in {coin_change, coin_change_dp, coin_change_backtrack_every_combination}:
    test_case.assertEqual(fn([1, 2, 5], 11), 3)
    test_case.assertEqual(fn([2], 3), -1)
    test_case.assertEqual(fn([1], 0), 0)
