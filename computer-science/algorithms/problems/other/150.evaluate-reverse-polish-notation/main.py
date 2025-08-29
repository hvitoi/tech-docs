# %%
from collections import deque
import unittest
from dataclasses import dataclass
from typing import Self


def calculate_polish_notation_ast(tokens: str) -> int:
    @dataclass
    class Node:
        operator: str
        operand1: Self | int
        operand2: Self | int

    class AST:
        def __init__(self, tokens: str):
            self.root = self.next_node(self, deque(tokens))

        def next_node(self, tokens: deque[str]):
            if len(tokens) == 1:
                return int(tokens[0])

            operator, *rest = tokens
            operand1, *rest = self.next_node(rest)
            operand2, *rest = self.next_node(rest)

            if

            if tokens[0].isdigit():
                node.operand1 = tokens.popleft()
            else

            if tokens[1].isdigit():
                node.operand1 = tokens.popleft()


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

for fn in {calculate_polish_notation, calculate_polish_notation_ast}:
    test_case.assertEqual(fn("+ 2 3"), 5)
    test_case.assertEqual(fn("* 3 + 1 2"), 9)
    test_case.assertEqual(fn("* + 1 2 4"), 12)
    test_case.assertEqual(fn("- 10 / 8 2"), 6)
    test_case.assertEqual(fn("/ * 3 5 + 2 3"), 3)
