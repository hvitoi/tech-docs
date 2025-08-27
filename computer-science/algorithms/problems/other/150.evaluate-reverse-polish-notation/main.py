# %%


import unittest


def calculate_polish_notation(tokens: str):
    operator, first_operand, second_operand = tokens[:3]

    if operator not in {"+", "-", "*", "/"}:
        raise Exception("Invalid Polish Notation")

    if not first_operand.isdigit():
        raise Exception("Invalid Polish Notation")

    match operator:
        case "+":
            if second_operand.isdigit():
                return int(first_operand) + int(second_operand)
            else:
                return int(first_operand) + calculate_polish_notation(tokens[2:])

        case "-":
            if second_operand.isdigit():
                return int(first_operand) - int(second_operand)
            else:
                return int(first_operand) - calculate_polish_notation(tokens[2:])
        case "*":
            if second_operand.isdigit():
                return int(first_operand) * int(second_operand)
            else:
                return int(first_operand) * calculate_polish_notation(tokens[2:])
        case "/":
            if second_operand.isdigit():
                return int(first_operand) / int(second_operand)
            else:
                return int(first_operand) / calculate_polish_notation(tokens[2:])


test_case = unittest.TestCase()

test_case.assertEqual(calculate_polish_notation(["*", "3", "+", "1", "2"]), 9)
