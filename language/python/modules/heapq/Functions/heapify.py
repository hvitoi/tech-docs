# Mutates and returns None
import heapq

# %%
# MIN HEAP
li = [10, 6, 7, 5, 15, 17, 12]
heapq.heapify(li)
li

# %%
# MAX HEAP (hidden function)
li = [10, 6, 7, 5, 15, 17, 12]
heapq._heapify_max(li)
li
