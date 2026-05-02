# %%
# We have a dictionary list. E.g ["apple", "banana", ...]
# Given a prefix, we want to return all the words from the above list which matches the prefix.

from __future__ import annotations

from dataclasses import dataclass, field


def occurrences_with_bs_both_sides(arr: list[str], prefix: str) -> int:
    """
    Find the left-most matching element (using binary search)
    Find the right-most matching element (using binary search)
    Slice the array with both indexes

    O(k log n); where:
        - k is the prefix size (for the startswith comparison)
        - n is the length of the arr
    """

    def find_left_most_match(lo: int, hi: int) -> int:
        left_most_index = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if arr[mid].startswith(prefix):
                left_most_index = mid
                hi = mid - 1
            if prefix < arr[mid]:
                hi = mid - 1
            if prefix > arr[mid]:
                lo = mid + 1
        return left_most_index

    def find_right_most_match(lo: int, hi: int) -> int:
        right_most_index = -1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if arr[mid].startswith(prefix):
                right_most_index = mid
                lo = mid + 1
            if prefix < arr[mid]:
                hi = mid - 1
            if prefix > arr[mid]:
                lo = mid + 1
        return right_most_index

    lower_bound = find_left_most_match(0, len(arr) - 1)
    upper_bound = find_right_most_match(0, len(arr) - 1)

    if lower_bound == -1:  # or upper_bound
        return 0

    return upper_bound - lower_bound + 1


@dataclass
class Node:
    children: dict[str, Node] = field(default_factory=dict)
    end_of_word: bool = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        node = self.root

        for letter in word:
            if letter not in node.children:
                node.children[letter] = Node()
            node = node.children[letter]

        node.end_of_word = True


def occurrences_with_trie(arr: list[str], prefix: str) -> int:
    """

    This implementations doesn't count twice duplicates
    """

    def count_downstream_nodes(node: Node) -> int:
        counter = 0

        if node.end_of_word:
            counter += 1

        for c in node.children:
            counter += count_downstream_nodes(node.children[c])

        return counter

    trie = Trie()
    for word in arr:
        trie.insert(word)

    node = trie.root
    for letter in prefix:
        if letter not in node.children:
            return 0
        node = node.children[letter]

    return count_downstream_nodes(node)


for fn in [occurrences_with_bs_both_sides, occurrences_with_trie]:
    assert fn(["ab", "cc", "cca", "ccb", "ccd", "cce"], "cc") == 5
    assert fn(["apple", "cherry"], "banana") == 0
    assert fn(["cab"], "c") == 1
    assert fn(["apple", "banana"], "z") == 0
    assert fn([], "x") == 0
    assert fn(["aa", "ab", "ac"], "a") == 3
    assert fn(["aa", "ab", "ac"], "b") == 0
    assert fn(["aa"], "aa") == 1
    assert fn(["a", "b", "c"], "") == 3
