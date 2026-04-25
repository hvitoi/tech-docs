# %%
import heapq

li = [10, 6, 7, 5, 15, 17, 12]
heapq.heapify(li)

# The heap is then automatically restored
heapq.heappush(li, 4)
li
