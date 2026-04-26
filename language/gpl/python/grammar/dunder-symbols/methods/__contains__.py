# %%
# __contains__ implements the `in` operator.
# Without it, `in` falls back to iterating with __iter__.
#
# Defining __contains__ explicitly is faster and lets you encode
# custom semantics (e.g. "in stock" rather than just "present").


from collections.abc import Container


class Inventory:
    def __init__(self):
        self.stock = {}

    def restock(self, item, qty):
        self.stock[item] = self.stock.get(item, 0) + qty

    def __contains__(self, item):
        return self.stock.get(item, 0) > 0


warehouse: Container = Inventory()
warehouse.restock("apple", 10)
warehouse.restock("banana", 0)  # listed but out of stock

"apple" in warehouse    # True
"banana" in warehouse   # False  (qty == 0)
"mango" in warehouse    # False  (not listed)
