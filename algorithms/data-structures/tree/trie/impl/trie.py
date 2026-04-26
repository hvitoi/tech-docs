# %%
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    # there is no need to store the "letter" of the node, because it's already implicit in the child key of the upper node
    children: dict[str, Node] = {}
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

    def search(self, word: str):
        node = self.root

        for letter in word:
            if not node.children[letter]:
                return False
            node = node.children[letter]

        return node.end_of_word


trie = Trie()
trie.insert("apple")
trie.insert("banana")
trie.insert("cucumber")

assert trie.search("apple") is True
assert trie.search("app") is False
