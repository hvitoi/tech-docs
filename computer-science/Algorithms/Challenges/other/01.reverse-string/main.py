# %%
from unittest import TestCase


def reverse_string(original_string: str) -> str:
    reversed_string = ""
    for i in reversed(range(len(original_string))):
        reversed_string += original_string[i]
    return reversed_string


test_case = TestCase()

test_case.assertEqual(
    reverse_string("Hi, my name is Henrique"),
    "euqirneH si eman ym ,iH",
)
