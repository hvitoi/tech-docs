# A lock object can lock the execution in the current thread
# %%
import threading

printer = threading.Lock()

printer.acquire()
printer.release()
