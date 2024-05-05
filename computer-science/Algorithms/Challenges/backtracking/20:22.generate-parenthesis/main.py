# %%
from unittest import TestCase


def generate_parenthesis(n: int) -> list[str]:
    """
    Choice: place "(" or ")"
    Constraints: cannot close ")" a bracket that has not been opened
    Goal: Exhaust all the possibilities


    Time Complexity: ?
    Space Complexity: O(n*2) = O(n), the length of the call stack which is the length of the string
    """

    def _generate_parenthesis(to_open: int, to_close: int) -> list[str]:
        def options_with_opening():
            remaining_options = _generate_parenthesis(to_open - 1, to_close)
            remaining_options = remaining_options if remaining_options else [""]
            return ["(" + option for option in remaining_options]

        def options_with_closing():
            remaining_options = _generate_parenthesis(to_open, to_close - 1)
            remaining_options = remaining_options if remaining_options else [""]
            return [")" + option for option in remaining_options]

        # nothing else to open or close
        if to_open == to_close == 0:
            return []

        # need to open
        if to_close == to_open:
            return options_with_opening()

        # need to close
        if to_open == 0:
            return options_with_closing()

        # can either open or close
        return options_with_opening() + options_with_closing()

    return _generate_parenthesis(n, n)


test_case = TestCase()

test_case.assertEqual(
    generate_parenthesis(0),
    [],
)

test_case.assertEqual(
    generate_parenthesis(1),
    ["()"],
)

test_case.assertEqual(
    generate_parenthesis(3),
    ["((()))", "(()())", "(())()", "()(())", "()()()"],
)
