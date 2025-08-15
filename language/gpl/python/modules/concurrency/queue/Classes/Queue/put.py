# %%
from queue import Queue


foo = Queue()

# enqueue
foo.put("a")
foo.put("b")
foo.put("c")

# dequeue
foo.get()
foo.get()
foo.get()
