# Memory

## Memory Heap

- Where memory allocation for `global variables` happens (e.g., variables, arrays, hashmaps)

```python
a = 1
```

- **Memory Leak**
  - Whenever the memory is allocated, but forgotten to be deallocated when it is not used anymore
  - It can be solved by `manually deallocating it` or by a `garbage collector`

## Call Stack

- Where we keep track of function calls
  - e.g., in a recursion the call stack is increased until the base case

- **Stack Overflow**
  - When the number of stacks in the call stack is increased indefinitely
  - Usually by bad recursions
