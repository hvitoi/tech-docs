# %%
from unittest import TestCase


def letter_combinations(digits: str, combinations=None) -> list[str]:
    def multiply_combinations(current_combinations, letters):
        if not current_combinations:
            current_combinations = [""]
        # return [
        #     combination + letter
        #     for combination in current_combinations
        #     for letter in letters
        # ]
        combinations = []
        for current_combination in current_combinations:
            for letter in letters:
                combinations.append(current_combination + letter)
        return combinations

    if combinations is None:
        combinations = []

    if not digits:
        return combinations

    match digits[0]:
        case "2":
            new_combinations = multiply_combinations(combinations, "abc")
            return letter_combinations(digits[1:], new_combinations)
        case "3":
            new_combinations = multiply_combinations(combinations, "def")
            return letter_combinations(digits[1:], new_combinations)
        case "4":
            new_combinations = multiply_combinations(combinations, "ghi")
            return letter_combinations(digits[1:], new_combinations)
        case "5":
            new_combinations = multiply_combinations(combinations, "jkl")
            return letter_combinations(digits[1:], new_combinations)
        case "6":
            new_combinations = multiply_combinations(combinations, "mno")
            return letter_combinations(digits[1:], new_combinations)
        case "7":
            new_combinations = multiply_combinations(combinations, "pqrs")
            return letter_combinations(digits[1:], new_combinations)
        case "8":
            new_combinations = multiply_combinations(combinations, "tuv")
            return letter_combinations(digits[1:], new_combinations)
        case "9":
            new_combinations = multiply_combinations(combinations, "wxyz")
            return letter_combinations(digits[1:], new_combinations)
        case "0":
            new_combinations = multiply_combinations(combinations, " ")
            return letter_combinations(digits[1:], new_combinations)
        case _:
            return letter_combinations(digits[1:], combinations)


test_case = TestCase()

test_case.assertEqual(
    letter_combinations("23"),
    ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
)
test_case.assertEqual(
    letter_combinations(""),
    [],
)
test_case.assertEqual(
    letter_combinations("2"),
    ["a", "b", "c"],
)
