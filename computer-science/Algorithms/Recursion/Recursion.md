# Recursion

> A function that calls itself

- Used to solve problems that itself includes the same problem (smaller instances of that same problem)
  - E.g., $5! = 5 * 4!$
- Specially useful when dealing with data structures that you do not know how deep they are
- Useful for `divide and conquer` algorithms
- A recursion needs a **base case** with indicates when the function should stop calling itself
- Any problems can be refactored to use iteration instead of recursion

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
