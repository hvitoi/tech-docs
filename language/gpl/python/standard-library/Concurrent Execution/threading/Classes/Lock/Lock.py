# A lock object can lock the execution in the current thread
# %%
import threading

# The idiomatic pattern is to use a lock in the context manager
# With that .acquire() and .release() and called transparently

lock = threading.Lock()


counter = 0


def increment():
    global counter
    for _ in range(100_000):
        with lock:
            counter += 1  # read-modify-write is not atomic without the lock


threads = [threading.Thread(target=increment) for _ in range(8)]

for t in threads:
    t.start()
for t in threads:
    t.join()

assert counter == 800_000
