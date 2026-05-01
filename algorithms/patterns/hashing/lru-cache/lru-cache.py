# https://leetcode.com/problems/lru-cache/ - 23k likes (Apr/2026)
from collections import OrderedDict

# Least Recently Used (LRU) cache


class LRUCache:
    """
    Ideally a doubly linked backed by a hash map must be used
    - To allow O(1) access to any node
    - To pop those nodes on access and quickly reinsert to the beginning of the list
    - To add new elements as they are inserted
    - To rewrite existing elements (without changing order) as they are added again
    - To remove last elements which exceed capacity
    """

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache: OrderedDict[int, int] = OrderedDict()

    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = val
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # pop the first (least recently used)

    def get(self, key: int) -> int | None:
        if key not in self.cache:
            return None
        self.cache.move_to_end(key)  # add to last (most recently used)
        return self.cache[key]
