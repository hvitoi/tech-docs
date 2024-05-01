# %%
from unittest import TestCase


# Levenshtein distance (edit distance)
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
        word_current = word[i] if i < len(word) else ""
        word_next = word[i + 1] if i + 1 < len(word) else ""
        target_current = target[i] if i < len(target) else ""
        target_next = target[i + 1] if i + 1 < len(target) else ""

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


def min_distance_recursive(word: str, target: str) -> int:
    if word == target:
        return 0

    word_current = word[0] if len(word) > 0 else None
    word_next = word[1] if len(word) > 1 else None

    target_current = target[0] if len(target) > 0 else None
    target_next = target[1] if len(target) > 1 else None

    # do nothing
    if word_current == target_current:
        return min_distance_recursive(word[1:], target[1:])

    # insert
    if word_current == target_next:
        return 1 + min_distance_recursive(word[1:], target[2:])

    # delete
    if word_next == target_current:
        return 1 + min_distance_recursive(word[2:], target[1:])

    # replace
    return 1 + min_distance_recursive(word[1:], target[1:])


test_case = TestCase()

for fn in {min_distance, min_distance_recursive}:
    test_case.assertEqual(fn("horse", "ros"), 3)
    test_case.assertEqual(fn("intention", "execution"), 5)
    test_case.assertEqual(fn("", ""), 0)
    test_case.assertEqual(fn("abc", "abc"), 0)
    test_case.assertEqual(fn("abc", ""), 3)
    test_case.assertEqual(fn("", "abc"), 3)
