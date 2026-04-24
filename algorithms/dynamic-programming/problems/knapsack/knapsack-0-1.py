# %%
import functools
import unittest


def memoize(fn):
    cache = {}

    def lookup_or_miss(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = fn(*args, **kwargs)
        return cache[key]

    return lookup_or_miss


@memoize
def knapsack(items: dict[str, dict[str, int]], bag_capacity: int):
    global counter
    counter += 1

    bag_options = []
    for item_name, item_props in items.items():
        if item_props["weight"] > bag_capacity:
            continue

        leftover_items = {k: items[k] for k in items if k != item_name}
        leftover_capacity = bag_capacity - item_props["weight"]

        bag = set([item_name]).union(knapsack(leftover_items, leftover_capacity))
        bag_options.append(bag)

    most_profitable_bag = [set(), float("-inf")]
    for bag in bag_options:
        worth_value = functools.reduce(
            lambda acc, item: acc + items[item]["value"], bag, 0
        )
        if worth_value > most_profitable_bag[1]:
            most_profitable_bag[:] = [bag, worth_value]

    return most_profitable_bag[0]


test_case = unittest.TestCase()

items = {
    "item1": {"value": 60, "weight": 5},
    "item2": {"value": 50, "weight": 3},
    "item3": {"value": 70, "weight": 4},
    "item4": {"value": 30, "weight": 2},
}

counter = 0
test_case.assertEqual(
    knapsack(items, 5),
    {"item2", "item4"},
)
counter
