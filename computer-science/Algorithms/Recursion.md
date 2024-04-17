# Recursion

> A function that calls itself

- Used to solve problems that itself include a subproblem
  - Specially useful when dealing with data structures that you do not know how deep they are
- A recursion needs a **base case** with indicates when the function should stop calling itself
- E.g., $5! = 5 * 4!$

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

## Tradeoffs

- **Pros**:
  - May (or may not) be easy to reason about. E.g., Depth-first traversal
- **Cons**:
  - May complicate a problem even more
  - Increases the space complexity (the callstack)
  - May lead to stack overflows if a base case is not properly implemented

## Tail recursion

- A technique/trick to avoid an increasing callstack
- With tail recursion, the calling function frees itself from memory (from the callstack) before recursively calling itself
- With tail recursion, there is no `back propagation`, because the function is not returned to be calling function but returned directly
- A requisite for tail recursion is that the recursion is the `very last statement` of the function
  - When that is not the case, the function has to be refactored in order to satisfy this requirement, usually by using an `accumulator`

```python
def factorial_recursive_with_accumulator(n, acc=1):
    if n == 0:
        return acc
    return factorial_recursive_with_accumulator(n - 1, acc * n)
```
