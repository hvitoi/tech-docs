# Knapsack Problem (Problema da mochila)

- Given a `bag` with a certain `capacity`, calculate which products (each with a given weight and value) to fit in order to `maximize the value contained in the bag`
- The items in the bag are limited (can only be used once)

## Variations

### Classic

- The objects can be broken down into small pieces (reducing proportionally the weight and the value)
- It's solved by using a `Greedy method` in which we pick the items with higher `profit/weight ratio` first. On the last item, divide it to fit the remaining weight left

### 0-1

- The `0/1` has a constraint that you cannot divide the object
- This now becomes a integer programming problem
