# %%
from typing import Self


class Node:
    def __init__(self, data: object, next: Self):
        self.data = data
        self.next = next
