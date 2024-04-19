# %%
from collections import deque


foo = deque()

# enqueue
foo.append("a")
foo.append("b")
foo.append("c")

# dequeue
foo.popleft()
foo.popleft()
foo.popleft()
