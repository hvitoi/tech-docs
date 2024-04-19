# %%
from queue import Queue


foo = Queue()

# enqueue
foo.put("a")
foo.put("b")
foo.put("c")

while not foo.empty():
    # dequeue
    print(foo.get())
