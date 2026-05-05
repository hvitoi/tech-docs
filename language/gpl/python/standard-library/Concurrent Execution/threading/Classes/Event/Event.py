# An Event is a one-bit flag that threads can wait on.
# Use it for "wait until something is ready" — e.g. config loaded, shutdown
# requested, connection established. Not for protecting shared state (use a Lock).
# %%
from threading import Event, Thread
from time import sleep

ready = Event()


def worker():
    print("worker: waiting for the signal")
    ready.wait()  # blocks until .set() is called from another thread
    print("worker: go!")


t = Thread(target=worker)
t.start()

sleep(1)  # simulate setup work on the main thread
ready.set()  # releases every thread blocked in .wait()
t.join()

# %%
# .wait(timeout=N) returns True if set within the timeout, False otherwise —
# useful for polling a shutdown flag without busy-waiting.
stop = Event()


def loop():
    while not stop.wait(timeout=0.5):  # sleeps up to 0.5s, wakes early on .set()
        print("tick")
    print("stopped")


t = Thread(target=loop)
t.start()
sleep(2)
stop.set()
t.join()
