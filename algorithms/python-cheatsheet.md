# Python cheatsheet

## Built-in containers

```python
# list
a = [1, 2, 3]
a.append(4); a.pop(); a.pop(0)        # pop(0) is O(n) — use deque if you need queue semantics
a.insert(i, x); a.remove(x); a.reverse(); a.sort()
sorted(a, key=lambda x: -x, reverse=True)
a[start:stop:step]                     # slicing — supports negative step for reverse
a[::-1]                                # reversed copy
a + b; a * 3                           # concatenation, repetition
sum(a); min(a); max(a); len(a)
any(a); all(a)                         # short-circuit booleans

# dict
d = {}
d[k] = v; d.get(k, default); d.pop(k, default)
k in d
for k, v in d.items(): ...
d.setdefault(k, []).append(x)          # init-and-append idiom
{k: v for k, v in pairs}               # dict comprehension

# set
s = set(); s = {1, 2, 3}
s.add(x); s.remove(x); s.discard(x)    # discard = no-error remove
s & t; s | t; s - t; s ^ t             # intersect, union, diff, sym-diff
frozenset(...)                          # hashable, can be a dict key

# tuple
t = (1, 2, 3); a, b, c = t              # unpacking
t = (x,)                                # single-element tuple needs trailing comma
```

## collections

```python
from collections import Counter, defaultdict, deque, OrderedDict

# Counter — frequency map with arithmetic
c = Counter("aabbc")                    # Counter({'a':2, 'b':2, 'c':1})
c.most_common(2)                        # [('a',2), ('b',2)]
c1 + c2; c1 - c2; c1 & c2               # union/diff/intersect of counts
c.update(iterable)                      # increment counts

# defaultdict — autovivifying values
g = defaultdict(list); g[k].append(v)
freq = defaultdict(int); freq[k] += 1

# deque — O(1) at both ends; the right way to do BFS queues
q = deque(); q.append(x); q.popleft()
q.appendleft(x); q.pop()                # use as stack or queue
q = deque(maxlen=k)                     # auto-evicts older items
```

## heapq — priority queue (min-heap)

```python
import heapq

h = []
heapq.heappush(h, x)
x = heapq.heappop(h)                    # smallest
h[0]                                    # peek
heapq.heapify(a)                        # in-place, O(n)
heapq.nlargest(k, a); heapq.nsmallest(k, a)

# max-heap trick: negate values
heapq.heappush(h, -x); -heapq.heappop(h)

# tuple ordering — Python compares lexicographically, so tag with priority
heapq.heappush(h, (priority, tiebreak, item))
```

## bisect — binary search on sorted list

```python
import bisect

i = bisect.bisect_left(a, x)            # leftmost insertion index → first index ≥ x
i = bisect.bisect_right(a, x)           # rightmost → first index > x
bisect.insort(a, x)                     # insert keeping sorted (O(n) shift)
```

## itertools — iteration combinators

```python
from itertools import (
    combinations, permutations, product, accumulate,
    chain, groupby, islice, count, cycle, repeat
)

list(combinations([1,2,3], 2))          # [(1,2),(1,3),(2,3)]
list(permutations([1,2,3], 2))          # length-2 ordered
list(product([0,1], repeat=3))          # all 3-bit binary tuples
list(accumulate([1,2,3,4]))             # [1,3,6,10] — running sums
list(chain([1,2], [3,4]))               # flatten one level
```

## string

```python
s = "Hello World"
s.lower(); s.upper(); s.title()
s.strip(); s.lstrip(); s.rstrip()       # whitespace by default; pass chars to strip
s.split(); s.split(",")                 # split() with no args splits on any whitespace
",".join(["a","b","c"])
s.startswith("He"); s.endswith("ld")
s.replace("l", "L", 1)                  # 3rd arg = max replacements
s.find("l"); s.index("l")               # find returns -1, index raises
s.count("l")
s.isalpha(); s.isdigit(); s.isalnum(); s.isspace()
ord("a"); chr(97)                        # 97
"abc".encode("utf-8")                    # bytes

# strings are immutable — build with list and ''.join, NOT += in a loop
out = []; out.append(part); ''.join(out)
```

## random

```python
import random

random.seed(42)                         # reproducibility — show this in tests
random.randint(a, b)                    # inclusive on both ends
random.random()                         # float in [0.0, 1.0)
random.uniform(a, b)                    # float in [a, b]
random.choice(seq)
random.choices(seq, weights=w, k=3)     # WITH replacement
random.sample(seq, k)                   # WITHOUT replacement
random.shuffle(a)                       # in-place
random.gauss(mu, sigma)                 # normal distribution
```

Common interview problems that use `random`:

- **Reservoir sampling**: select `k` items from a stream of unknown length uniformly at random.
- **Fisher-Yates shuffle**: in-place uniform shuffle in O(n).
- **Weighted choice without `random.choices`**: prefix sums + `bisect_left(cum, random.random() * total)`.
- **Generating test inputs**: random arrays, strings, graph topologies.

```python
# Fisher-Yates
def shuffle(a):
    for i in range(len(a) - 1, 0, -1):
        j = random.randint(0, i)
        a[i], a[j] = a[j], a[i]

# Reservoir sampling, k=1
def pick(stream):
    chosen = None
    for i, x in enumerate(stream, 1):
        if random.randint(1, i) == 1:
            chosen = x
    return chosen
```

## math

```python
import math

math.inf; -math.inf; math.nan
math.floor(x); math.ceil(x); math.trunc(x)
math.sqrt(x); math.isqrt(n)             # isqrt is integer-only, exact
math.log(x, base); math.log2(x); math.log10(x)
math.gcd(a, b); math.lcm(a, b)
math.factorial(n); math.comb(n, k); math.perm(n, k)
math.dist(p1, p2)                        # Euclidean distance
```

## Numeric tricks

```python
# integer division and modulo
q, r = divmod(a, b)
-7 // 2                                 # -4 (Python floor-divides toward -∞)
-7 % 2                                  # 1  (sign follows divisor)

# bit ops
n & 1                                   # last bit
n >> 1; n << 1                          # halve / double
n & (n - 1)                             # clear lowest set bit (Brian Kernighan)
bin(n); hex(n); int(s, 2); int(s, 16)
n.bit_count()                           # popcount, Python 3.10+
n.bit_length()
```

## Iteration patterns

```python
for i, x in enumerate(a, start=0): ...
for x, y in zip(a, b): ...
for x, y in zip(a, b, strict=True): ... # 3.10+: raise on length mismatch
for i in range(start, stop, step): ...
list(reversed(a)); list(reversed(range(n)))

# 2D grid
for r in range(rows):
    for c in range(cols):
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols: ...
```

## Comprehensions

```python
[x*x for x in a if x > 0]
{x for x in a}
{k: v for k, v in pairs}
(x*x for x in a)                         # generator — lazy

# 2D
grid = [[0] * cols for _ in range(rows)]  # do NOT use [[0]*cols]*rows — that aliases rows
```

## Functions & functools

```python
from functools import lru_cache, cache, reduce

@cache                                   # 3.9+; unbounded memoization
def f(n):
    if n < 2: return n
    return f(n-1) + f(n-2)

reduce(lambda a, b: a + b, [1,2,3], 0)   # rare in interviews; sum() preferred
```

## Testing in 30 seconds

```python
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i

# inline asserts — show this to your interviewer
assert two_sum([2,7,11,15], 9) == [0,1]
assert two_sum([3,2,4], 6) == [1,2]
assert two_sum([3,3], 6) == [0,1]
```

If you have 5 min to spare, write a tiny `unittest`:

```python
import unittest
class T(unittest.TestCase):
    def test_basic(self): self.assertEqual(two_sum([2,7,11,15], 9), [0,1])
    def test_dup(self): self.assertEqual(two_sum([3,3], 6), [0,1])
unittest.main(argv=[''], exit=False)
```

## Class boilerplate

```python
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):                  # huge time-saver when debugging
        return f"Node({self.val})"

# from dataclasses for record-style classes
from dataclasses import dataclass, field
@dataclass
class Point:
    x: int
    y: int
    tags: list[str] = field(default_factory=list)
```

## Things that bite under pressure & Pitfalls

- `int / int` returns `float` in Python 3. Use `//` for floor.
- Mutable default args: `def f(x, acc=[])` — `acc` is shared across calls. Use `None` and assign inside.
- `[[0]*n]*m` shares the inner list — every row is the same object. Use `[[0]*n for _ in range(m)]`.
- Strings and tuples are immutable; lists, dicts, sets are mutable.
- `dict` keys must be hashable — no lists, no dicts, no sets as keys.
- `range(n)` is exclusive on the upper bound.
- `sort` mutates and returns `None`; `sorted` returns a new list.
- Sets and dicts are unordered for equality, but `dict` preserves insertion order for iteration (3.7+).
- `==` checks value; `is` checks identity. For small ints and interned strings `is` may coincide, but never rely on it.
