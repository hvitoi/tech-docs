# %%
import unittest
import itertools


def decode_string(s: str):
    # if s[0] != "[":
    #     return s

    arr = []
    open_brackets = 0
    current_block = ""

    multiplier = 0

    for i, el in enumerate(s):
        if el == "[":
            open_brackets += 1
            if open_brackets == 1:
                multiplier = int(s[i - 1])
                current_block = ""
                continue

        if el == "]":
            open_brackets -= 1
            if open_brackets == 0:
                done_block = "".join(
                    itertools.repeat(decode_string(current_block), multiplier)
                )
                arr.append(done_block)
                continue

        if open_brackets == 0:
            if not el.isdigit():
                arr.append(el)
        else:
            current_block += el

    return "".join(arr)


test_case = unittest.TestCase()

test_case.assertEqual(decode_string("3[a]2[bc]"), "aaabcbc")
test_case.assertEqual(decode_string("3[a2[c]]b"), "accaccaccb")
test_case.assertEqual(decode_string("2[abc]3[cd]ef"), "abcabccdcdcdef")
