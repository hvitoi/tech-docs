# %%
from unittest import TestCase


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

    def search(self, word: str):
        node = self.root

        for c in word:
            if not node.children[c]:
                return False
            node = node.children[c]

        return node.end_of_word


trie = Trie()
trie.insert("apple")
trie.insert("banana")
trie.insert("cucumber")

test_case = TestCase()
test_case.assertEqual(trie.search("apple"), True)
test_case.assertEqual(trie.search("app"), False)
