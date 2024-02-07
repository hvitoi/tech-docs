# %%
from unittest import TestCase


def multiply_elements(nums: list) -> int:
    product = 1
    for num in nums:
        product *= num
    return product


def product_except_self(nums: list) -> list:
    return list(
        map(lambda i: multiply_elements(nums[:i] + nums[i + 1 :]), range(len(nums)))
    )


test_case = TestCase()

test_case.assertEqual(product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])
test_case.assertEqual(product_except_self([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])
