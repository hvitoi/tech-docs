# %%
from concurrent.futures import ThreadPoolExecutor
from time import sleep

# .cancel() attempts to cancel a future. Returns True only if it was still PENDING.
# Once a task starts running, it CANNOT be cancelled (threads aren't preemptible).
# .cancelled() / .running() report current state.


def slow_task(name):
    sleep(0.5)
    return name


# max_workers=1 forces queueing so we can observe a pending task
with ThreadPoolExecutor(max_workers=1) as executor:
    running = executor.submit(slow_task, "A")  # starts immediately
    pending = executor.submit(slow_task, "B")  # queued behind A

    sleep(0.05)  # give A a moment to start
    print(running.running())  # True
    print(running.cancel())  # False — too late, already running
    print(pending.cancel())  # True — was still pending
    print(pending.cancelled())  # True
