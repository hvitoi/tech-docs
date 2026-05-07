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


# %%
# Producer-consumer: a queue serializes work between producers and a pool of
# workers. Each task_done() balances one put(); join() blocks until the queue
# is fully drained — the standard way to wait for async processing to finish.
from queue import Queue
from threading import Thread, current_thread

processing_queue = Queue()


def worker():
    while True:
        item = processing_queue.get()
        print(f"{current_thread().name} processed {item}")
        processing_queue.task_done()


# Spawn 3 threads as daemons
# with multiple workers, the queue itself handles the concurrent get() — no extra locking needed.
threads = [Thread(target=worker, daemon=True) for _ in range(3)]
for t in threads:
    t.start()

for item in range(10):
    processing_queue.put(item)

processing_queue.join()  # returns once every put() has had a matching task_done()
