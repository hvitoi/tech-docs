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

# start the execution in a separate thread
thread.start()

# synchronize the threads again, so that the main thread is resumed only when the other thread is finished
# Similar to an "await"
thread.join()

print_thread()
