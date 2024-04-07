# Time Complexity

- Measures the `speed aspect` of an algorithm
- Describe the performance of an algorithm
- How much the `runtime` grows as the `input size` grows (n vs. t).
- It's estimated by counting the number of elementary steps performed by any algorithm to finish execution
- We use the worst-case time complexity of an algorithm because that is the maximum time taken for any input size

![Runtime Complexity](Big-O%20Complexity%20Chart.png)

<https://www.bigocheatsheet.com/>

## Constant - $O(1)$

$$t = 1$$

- The number of items doesn't influence in the run time

```javascript
statement;
```

## Logarithmic - $O(log\ n)$

$$t = log(n)$$

- Examples:
  - Searching sorted arrays (binary search) - divide and conquer
  - Numbers of times a number can be divided by 2 (divides the working area in half with each iteration). Dividing the working area in half is logarithmic

```javascript
// Numbers of times a number can be divided by 2
// Divides the working area in half on each iteration
while (low <= high) {
  mid = (low + high) / 2;
  if (target < list[mid]) high = mid - 1;
  else if (target > list[mid]) low = mid + 1;
  else break;
}
```

## Linear - $O(n)$

$$t = n$$

- Examples:
  - Iterating through a string (of a collection of data)

```javascript
for (i = 0; i < n; i++) {
  statement;
}
```

- $O(n+m)$: Iterating two different collections with separate for loops

## Log Linear (Quasilinear) - $O(n\ log\ n)$

$$t = n * log(n)$$

- The more items in the collections, the more time costly is the addition of each new item
- Examples:
  - Sorting algorithms: represents the minimum number of comparisons needed to know where to place each element

## Quadratic - $O(n^2)$

$$t = n ^ 2$$

- A loop inside of a loop
- Examples:
  - Steps algorithm
  - Handshake problem

```javascript
for (i = 0; i < n; i++) {
  for (j = 0; j < n; j++) {
    statement;
  }
}
```

- $O(n*m)$: Iterating two nested for loops over different collections

## Exponential - $O(2^n)$

$$t = 2 ^ n$$

- A single new element doubles the runtime
- Examples:
  - Recursive algorithms that solves a problem of size n

## Factorial - $O(n!)$

$$t = n!$$

- You are adding a loop for every element

## Data Structure Operations

- The operation complexity always considers the worst case

|                      | Access   | Search   | Insertion   | Deletion   | Space Complexity   |
| -                    | -        | -        | -           | -          | -                  |
| Array                | $O(1)$   | $O(n)$   | $O(n)$      | $O(n)$     | $O(n)$             |
| Stack                | $O(n)$   | $O(n)$   | $O(1)$      | $O(1)$     | $O(n)$             |
| Queue                | $O(n)$   | $O(n)$   | $O(1)$      | $O(1)$     | $O(n)$             |
| Linked List (Singly) | $O(n)$   | $O(n)$   | $O(1)$      | $O(1)$     | $O(n)$             |
| Linked List (Doubly) | $O(n)$   | $O(n)$   | $O(1)$      | $O(1)$     | $O(n)$             |
| Hash Table           | $N/A$     | $O(n)$  | $O(n)$      | $O(n)$     | $O(n)$             |

## Sorting Algorithms

|                | Space complexity   | Time complexity (best)     | Time complexity (worst) |
| -              | -                  | -                          | -                       |
| Insertion Sort | $O(1)$             | $O(n)$                     | $O(n^2)$                |
| Selection Sort | $O(1)$             | $O(n^2)$                   | $O(n^2)$                |
| Bubble Sort    | $O(1)$             | $O(n)$                     | $O(n^2)$                |
| Mergesort      | $O(n)$             | $O(n\ log\ n)$             | $O(n\ log\ n)$          |
| Quicksort      | $O(log\ n)$        | $O(n\ log\ n)$             | $O(n^2)$                |
| Heapsort       | $O(1)$             | $O(n\ log\ n)$             | $O(n\ log\ n)$          |
