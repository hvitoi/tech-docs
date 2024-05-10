# Tail recursion

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
