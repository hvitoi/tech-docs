# %%
from functools import reduce
import heapq
from unittest import TestCase


def heappush(heap, item):
    item = (item[0] * -1, item[1], item[2], item[3])
    heapq.heappush(heap, item)


def heappop(heap):
    item = heapq.heappop(heap)
    return (item[0] * -1, item[1], item[2], item[3])


def knapsack(items: dict[str, dict[str, int]], bag_size: int):
    profitable_items = []

    for item in items:
        ratio = items[item]["value"] / items[item]["weight"]
        heappush(
            profitable_items, (ratio, item, items[item]["value"], items[item]["weight"])
        )

    bag = set()
    current_weight = 0

    while current_weight < bag_size:
        available_weight = bag_size - current_weight
        item = heappop(profitable_items)

        quantity_to_pick = min(item[3], available_weight)
        portion_to_pick = quantity_to_pick / item[3]

        bag.add((item[1], portion_to_pick))
        current_weight += quantity_to_pick

    return bag

    # total_value_worth = reduce(
    #     lambda acc, el: acc + el[1] * items[el[0]]["value"], bag, 0
    # )
    # return total_value_worth


test_case = TestCase()

items = {
    "potato": {"value": 10, "weight": 2},
    "corn": {"value": 5, "weight": 3},
    "carrot": {"value": 15, "weight": 5},
    "rice": {"value": 7, "weight": 7},
    "beans": {"value": 6, "weight": 1},
    "broccoli": {"value": 18, "weight": 4},
    "mate": {"value": 3, "weight": 1},
}

test_case.assertEqual(
    knapsack(items, 15),
    {
        ("beans", 1.0),
        ("broccoli", 1.0),
        ("carrot", 1.0),
        ("corn", 0.6666666666666666),
        ("mate", 1.0),
        ("potato", 1.0),
    },
)
