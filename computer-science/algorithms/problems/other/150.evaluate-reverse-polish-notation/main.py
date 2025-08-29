# %%
from collections import deque
import unittest
from dataclasses import dataclass
from typing import Self


def calculate_polish_notation_ast(tokens: str) -> int:
    @dataclass
    class Node:
        operator: str
        left_operand: Self | int
        right_operand: Self | int

    def build_ast(tokens: deque[str]) -> Node:
        token = tokens.popleft()

        if token in {"+", "-", "*", "/"}:
            return Node(
                operator=token,
                left_operand=build_ast(tokens),
                right_operand=build_ast(tokens),
            )

        if token.isdigit():
            return int(token)
        else:
            raise Exception("Invalid Polish Notation")

    def eval_ast(node: Node | int):
        operands = []

        for operand in (node.left_operand, node.right_operand):
            if isinstance(operand, Node):
                operands.append(eval_ast(operand))
            else:
                operands.append(operand)

        match node.operator:
            case "+":
                return operands[0] + operands[1]
            case "-":
                return operands[0] - operands[1]
            case "*":
                return operands[0] * operands[1]
            case "/":
                return operands[0] / operands[1]

    # an additional validation could be performed to check if tokens have been exhausted and there is no elements there left
    ast = build_ast(deque(tokens.split()))
    return eval_ast(ast)


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

        operator, left_operand, right_operand = get_parts(tokens)

        operands = []
        for operand in (left_operand, right_operand):
            if len(operand) == 1:
                operands.append(int(operand[0]))
            else:
                operands.append(calculate(operand))

        match operator:
            case "+":
                return operands[0] + operands[1]
            case "-":
                return operands[0] - operands[1]
            case "*":
                return operands[0] * operands[1]
            case "/":
                return operands[0] / operands[1]

    return calculate(tokens.split())


test_case = unittest.TestCase()

for fn in {calculate_polish_notation, calculate_polish_notation_ast}:
    test_case.assertEqual(fn("+ 2 3"), 5)
    test_case.assertEqual(fn("* 3 + 1 2"), 9)
    test_case.assertEqual(fn("* + 1 2 4"), 12)
    test_case.assertEqual(fn("- 10 / 8 2"), 6)
    test_case.assertEqual(fn("/ * 3 5 + 2 3"), 3)
