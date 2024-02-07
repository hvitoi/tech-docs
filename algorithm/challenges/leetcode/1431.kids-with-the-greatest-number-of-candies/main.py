# %%
from unittest import TestCase


def kids_with_candies(candies_list, extra_candies):
    res = []
    for candies in candies_list:
        if candies + extra_candies >= max(candies_list):
            res.append(True)
        else:
            res.append(False)
    return res


def kids_with_candies2(candies_list, extra_candies):
    return list(
        map(lambda candies: candies + extra_candies >= max(candies_list), candies_list)
    )


def kids_with_candies3(candies_list, extra_candies):
    return [candies + extra_candies >= max(candies_list) for candies in candies_list]


test_case = TestCase()

for fn in [kids_with_candies, kids_with_candies2, kids_with_candies3]:
    test_case.assertEqual(fn([2, 3, 5, 1, 3], 3), [True, True, True, False, True])
    test_case.assertEqual(fn([4, 2, 1, 1, 2], 1), [True, False, False, False, False])
    test_case.assertEqual(fn([12, 1, 12], 10), [True, False, True])
