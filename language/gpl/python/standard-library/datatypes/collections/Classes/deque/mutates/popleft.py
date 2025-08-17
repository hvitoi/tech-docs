# %%
from collections import deque

# Queue behavior

foo = deque()

# Enqueue
foo.append("a")
foo.append("b")
foo.append("c")

# Dequeue
foo.popleft()
foo.popleft()
foo.popleft()
# foo.popleft()  # throws if the queue is empty
