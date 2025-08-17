# %%
from collections import deque

# deque is a Doubly Linked List
# Therefore it can be used to implement a Queue

foo = deque()

# enqueue
foo.append("a")
foo.append("b")
foo.append("c")

# dequeue
foo.popleft() # a
foo.popleft() # b
foo.popleft() # c
