# List

## Operations

- `Append` (to end) $O(1)$
- `Append` (to beginning) $O(n)$

- `Pop` (from end): $O(1)$
- `Pop` (from beginning): $O(n)$

- `Access` (by index): $O(1)$
- `Search`: $O(n)$

## Implementations

- `Array`
- `Linked List` (less common)

### Python

- Static Array: `array` (array module)
- Dynamic Array: `list` (built-in)

```python
# Static Array
arr = array.array('i', [1, 2, 3, 4])

# Dynamic Array
my_list = ["a", 1, True, ["c", 9]]
```

### C++

- Static Array: `built-in array`, `std::array`
- Dynamic Array: `std::vector`

```c++
// Static Array
char sentence[] = "Hello World";
int numbers[] = {1, 2, 3};

// Dynamic Array
vector<string> colors = {"red", "blue", "green"};
```
