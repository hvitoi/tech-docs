# %%
from unittest import TestCase


def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    for i in range(len(flowerbed)):
        last_i = i - 1 if (i - 1 >= 0) else None
        next_i = i + 1 if (i + 1 < len(flowerbed)) else None
        if (
            flowerbed[i] == 0
            and (not last_i or flowerbed[last_i] == 0)
            and (not next_i or flowerbed[next_i] == 0)
        ):
            flowerbed[i] = 1
            n -= 1
    return n <= 0


test_case = TestCase()

test_case.assertTrue(can_place_flowers([1, 0, 0, 0, 1], 1))
test_case.assertFalse(can_place_flowers([1, 0, 0, 0, 1], 2))
