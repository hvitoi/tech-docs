from collections import OrderedDict


class LRUCache:
    """
    Ideally a doubly linked backed by a hash map must be used
    - To allow O(1) access to any node
    - To pop those nodes on access and quickly reinsert to the beginning of the list
    - To add new elements as they are inserted
    - To rewrite existing elements (without changing order) as they are added again
    - To remove last elements which exceed capacity
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def put(self, key, val):
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = val
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def get(self, key):
        if key not in self.cache:
            return None
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val
