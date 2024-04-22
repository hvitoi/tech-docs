# %%
import unittest


def decode_string_with_stack(s: str) -> str:
    stack: list[str] = []

    for char in s:
        if char == "]":
            nested_block = []
            while True:
                nested_char = stack.pop()
                if nested_char == "[":
                    continue
                if nested_char.isdigit():
                    stack.extend(int(nested_char) * nested_block)
                    break
                nested_block.insert(0, nested_char)
        else:
            stack.append(char)

    return "".join(stack)


test_case = unittest.TestCase()

test_case.assertEqual(decode_string_with_stack("3[a]2[bc]"), "aaabcbc")
test_case.assertEqual(decode_string_with_stack("3[a2[c]]b"), "accaccaccb")
test_case.assertEqual(decode_string_with_stack("2[abc]3[cd]ef"), "abcabccdcdcdef")
