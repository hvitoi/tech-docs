# %%
# RLock — reentrant lock. The same thread can acquire it multiple times
# without blocking. Each acquire bumps an internal counter; the lock is only
# really released when the counter drops back to zero.
#
# Why it matters: a method that holds the lock can call another method that
# also takes the lock, on the same thread, without self-deadlocking.

import threading


class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.RLock()

    def increment(self):
        with self.lock:
            self.value += 1

    def increment_twice(self):
        with self.lock:  # acquire #1
            self.increment()  # acquire #2 on the SAME thread — RLock just bumps the counter
            self.increment()  # acquire #3 — same


c = Counter()
c.increment_twice()
assert c.value == 2


# %%
# What a plain Lock does in the same situation: self-deadlock. It has no
# concept of ownership, so a re-acquire by the holding thread waits forever
# for itself to release. The timeout=0.5 here just keeps the demo from hanging.

plain = threading.Lock()
plain.acquire()
got_it = plain.acquire(timeout=0.5)
assert got_it is False, "plain Lock won't re-acquire on the same thread"
plain.release()


# %%
# Cost & smell:
#   - RLock does extra bookkeeping per acquire/release (owner thread + count),
#     so it's a touch slower than Lock.
#   - "If you need RLock, you can usually restructure" is a common review nit —
#     take the lock at exactly one layer instead of nesting calls that each
#     re-take it. But when composing public methods that each take the lock
#     (e.g. Account.transfer calling Account.deposit/withdraw), RLock is the
#     simplest correct choice.
