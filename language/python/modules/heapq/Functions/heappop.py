# %%
import heapq

li = [10, 6, 7, 5, 15, 17, 12]
heapq.heapify(li)

# The top item of the heap (the minimum value) is popped
# The heap is then automatically restored
heapq.heappop(li)
li
