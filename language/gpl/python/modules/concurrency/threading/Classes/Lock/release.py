# %%
import threading

printer = threading.Lock()

printer.acquire()
printer.release()
