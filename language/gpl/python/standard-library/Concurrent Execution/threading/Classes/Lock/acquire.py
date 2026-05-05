# %%
import threading

# Rarely used directly, prefer the context manager idiom

lock = threading.Lock()

lock.acquire()
lock.release()

# %%
# Direct acquire/release is reserved for cases `with` can't express:

if lock.acquire(timeout=2):
    # lock.acquire() returns True if it's able to acquire the lock within 2 seconds
    try:
        ...
    finally:
        lock.release()
else:
    ...  # didn't get it — back off, retry, log, whatever
