# %%
import time

# perf_counter() is preferred over time.time() because it's more precise
# for example to counter the duration of a code block execution
start_time = time.perf_counter()  # Unix epoch
time.sleep(3)  # 3 seconds
process_time = time.perf_counter() - start_time
process_time
