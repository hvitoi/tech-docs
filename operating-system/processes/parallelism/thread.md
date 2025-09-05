# Thread

- The word "thread" has multiple meanings depending on the context

## Hardware Threads

- Each CPU Core has 2 Threads thanks to `Hyper-Threading` (Intel) or `SMT` (AMD)
- Example: if a CPU has 4 Cores, the OS sees 8 logical CPUs

## OS/Kernel Threads

- An OS thread is a unit of work created by the OS (via system calls like `pthread_create` on Linux).
- Each process can create many OS threads, far more than the number of hardware threads. The `OS scheduler` decides which OS Threads run on which Hardware Threads
- If there are more OS threads than hardware threads, the scheduler will time-slice (interleave)

## Virtual Threads / Coroutine

- It's a lightweight thread managed by a runtime (e.g., JVM, PVM) instead of the OS. Millions os threads are possible.
- They're much lighter and don't map directly to OS Threads. The runtime can schedule many virtual threads onto a much smaller pool of OS threads
- This concept appear with different namings in different programming languages
  - **Java**
    - `new Thread(...)`: OS Thread
    - `Thread.startVirtualThread(...)`: Virtual Thread (Java 19+)
  - **Python**
    - `Thread(...).start()`: OS Thread
    - `async def() + await <coroutine>`: asyncio Coroutine
  - **Go**
    - Goroutine
