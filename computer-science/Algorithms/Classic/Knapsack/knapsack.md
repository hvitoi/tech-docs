# Knapsack Problem

- Given a `bag` with a certain `capacity`, calculate which products (each with a given weight and value) to fit in order to `maximize the value contained in the bag`
- The objects can be broken down into small pieces (reducing proportionally the weight and the value)

## Greedy method

- Pick the ones with higher profit to weight ratio first. One the last one, divide it to fit the remaining weight left

## 0/1 variation

- The `0/1` has a constraint that you cannot divide the object
- This now becomes a integer programming problem
