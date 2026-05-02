# %%
# We have a dictionary list. E.g ["apple", "banana", ...]
# Given a prefix, we want to return all the words from the above list which matches the prefix.


def occurrences_with_bs_both_sides(arr: list[str], prefix: str) -> int:
    """
    Find the left-most matching element (using binary search)
    Find the right-most matching element (using binary search)
    Slice the array with both indexes
    """

    def find_left_most_match(lo, hi):
        mid_index = lo + (hi - lo) // 2
        mid_value = arr[mid_index]

        if mid_value.startswith(prefix):
            left_index = mid_index - 1
            left_value = arr[left_index] if left_index >= 0 else None
            if left_value and left_value.startswith(prefix):
                return find_left_most_match(lo, mid_index - 1)
            return mid_index

        if prefix < mid_value:
            return find_left_most_match(lo, mid_index - 1)

        if prefix > mid_value:
            return find_left_most_match(mid_index + 1, hi)

    def find_right_most_match(lo, hi):
        mid_index = lo + (hi - lo) // 2
        mid_value = arr[mid_index]

        if mid_value.startswith(prefix):
            right_index = mid_index + 1
            right_value = arr[right_index] if right_index < len(arr) else None
            if right_value and right_value.startswith(prefix):
                return find_right_most_match(mid_index + 1, hi)
            return mid_index

        if prefix < mid_value:
            return find_right_most_match(lo, mid_index - 1)

        if prefix > mid_value:
            return find_right_most_match(mid_index + 1, hi)

    lower_bound = find_left_most_match(0, len(arr) - 1)
    upper_bound = find_right_most_match(0, len(arr) - 1)

    return upper_bound - lower_bound + 1


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.end_of_word = True


def occurrences_with_trie(arr: list[str], prefix: str) -> int:
    def count_downstream_nodes(node: TrieNode):
        counter = 1

        for c in node.children:
            counter += count_downstream_nodes(node.children[c])

        return counter

    trie = Trie()
    for word in arr:
        trie.insert(word)

    node = trie.root
    for c in prefix:
        if c not in node.children:
            return 0
        node = node.children[c]

    return count_downstream_nodes(node)


for fn in [occurrences_with_bs_both_sides, occurrences_with_trie]:
    assert fn(["ab", "cca", "ccb", "cc", "ccd", "cce"], "cc") == 5
