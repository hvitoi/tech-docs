# Returns the current thread in which the code is executed
# %%
import threading
import time


def print_thread():
    thread = threading.current_thread()
    print(f"Running in the thread: {thread.name}\n")


def do_something():
    time.sleep(5)
    print_thread()


thread = threading.Thread(target=do_something, args=[])
thread.start()

print_thread()
