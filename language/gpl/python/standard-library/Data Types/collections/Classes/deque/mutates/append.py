# %%
from collections import deque

# Queue behavior

foo = deque()

# enqueue
foo.append("a")
foo.append("b")
foo.append("c")

# dequeue
foo.popleft()
foo.popleft()
foo.popleft()
