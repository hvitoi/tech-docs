# %%
import unittest


def remove_stars(s: str) -> str:
    while s.count("*") != 0:
        i = s.find("*")
        s = s[: i - 1 if i > 0 else 0] + s[i + 1 :]
    return s


def remove_stars2(s: str) -> str:
    stars = s.count("*")
    while stars != 0:
        i = s.find("*")
        s = s[: i - 1 if i > 0 else 0] + s[i + 1 :]
        stars -= 1
    return s


test_case = unittest.TestCase()

for fn in {remove_stars, remove_stars2}:
    test_case.assertEqual(
        fn("leet**cod*e"),
        "lecoe",
    )

    test_case.assertEqual(
        fn("erase*****"),
        "",
    )

    test_case.assertEqual(
        fn("*leet**cod*e"),
        "lecoe",
    )

    test_case.assertEqual(
        fn("*leet**cod*e*"),
        "leco",
    )
