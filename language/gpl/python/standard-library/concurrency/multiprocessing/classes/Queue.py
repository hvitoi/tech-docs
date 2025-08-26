# %%
from multiprocessing import Process, Queue

# A Queue is for message passing between processes.
# It works like a thread-safe FIFO queue. One process can put data, another can get it.
# 🔹 When to use: When processes need to send/receive data (producer-consumer pattern).


def producer(q):
    for i in range(5):
        q.put(i)  # send numbers
    q.put(None)  # sentinel to signal end


def consumer(q):
    while True:
        item = q.get()
        if item is None:  # stop when sentinel is received
            break
        print("Consumed:", item)


if __name__ == "__main__":
    q = Queue()

    processes = [
        Process(target=producer, args=(q,)),
        Process(target=consumer, args=(q,)),
    ]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
