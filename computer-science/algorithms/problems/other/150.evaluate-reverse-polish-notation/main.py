# %%
import unittest


def calculate_polish_notation(tokens: str) -> int:
    def get_parts(tokens: list[str]) -> tuple[list[str], list[str]]:
        operator = tokens[0]
        parts = tokens[1:]
        digits_to_consume = 0
        for i, el in enumerate(parts):
            if (el not in {"+", "-", "*", "/"}) and (not el.isdigit()):
                raise Exception("Invalid Polish Notation")

            if el in {"+", "-", "*", "/"}:
                digits_to_consume += 2
                continue

            digits_to_consume -= 1

            if digits_to_consume <= 0:
                return operator, parts[: i + 1], parts[i + 1 :]

    def calculate(tokens: list[str]):
        if len(tokens) < 3:
            raise Exception("Invalid Polish Notation")

        operator, left, right = get_parts(tokens)

        if len(left) == 1:
            left_operand = int(left[0])
        else:
            left_operand = calculate(left)

        if len(right) == 1:
            right_operand = int(right[0])
        else:
            right_operand = calculate(right)

        match operator:
            case "+":
                return left_operand + right_operand
            case "-":
                return left_operand - right_operand
            case "*":
                return left_operand * right_operand
            case "/":
                return left_operand / right_operand

    return calculate(tokens.split())


test_case = unittest.TestCase()

test_case.assertEqual(calculate_polish_notation("+ 2 3"), 5)
test_case.assertEqual(calculate_polish_notation("* 3 + 1 2"), 9)
test_case.assertEqual(calculate_polish_notation("* + 1 2 4"), 12)
test_case.assertEqual(calculate_polish_notation("- 10 / 8 2"), 6)
test_case.assertEqual(calculate_polish_notation("/ * 3 5 + 2 3"), 3)
