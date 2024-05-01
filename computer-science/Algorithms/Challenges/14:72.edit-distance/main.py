# %%
from unittest import TestCase


def min_distance(word: str, target: str) -> int:
    """
    Choices:
    1. do nothing: the best option, always prefer when possible
    2. insert: only if the current char is equal to the next char on target
    3. delete: only if the next char is equal to the current char on target
    4. replace: the fallback option, last option
    """
    operations = 0

    i = 0
    while word != target:
        word_current = word[i] if i < len(word) else None
        word_next = word[i + 1] if i + 1 < len(word) else None
        target_current = target[i] if i < len(target) else None
        target_next = target[i + 1] if i + 1 < len(target) else None

        # do nothing
        if word_current == target_current:
            i += 1
            continue

        # insert
        elif word_current == target_next:
            word = word[:i] + target_current + word[i:]
            i += 2
            operations += 1
            continue

        # delete
        elif word_next == target_current:
            word = word[:i] + word[i + 1 :]
            i += 1
            operations += 1
            continue

        # replace
        else:
            word = word[:i] + target_current + word[i + 1 :]
            operations += 1
            continue

    return operations


test_case = TestCase()
test_case.assertEqual(min_distance("horse", "ros"), 3)
test_case.assertEqual(min_distance("intention", "execution"), 5)
