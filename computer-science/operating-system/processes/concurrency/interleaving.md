# Concurrency

- It's a technique performed by the OS to run a bit of each process at a time in order to give a sense of parallelism, although everything is run in sequence
- In technique behind tasks overlapping in time (concurrency) is called `interleaving` (time-slicing), but not necessarily running simultaneously
- Allows multitasking even with a single core processor

- A programa can be: 1. Concurrent but not parallel, 2. Parallel but not concurrent, 3. Both

## Interleaving (time-slicing)

- The `OS scheduler` decides when each process runs on the CPU. The CPU executes a portion (a time slice) of one process, then switches to another, and so on.
- The process, however, is `not forcibly interrupted` in the middle of its CPU burst, unless the slice ends or it voluntarily yields (e.g., waiting for I/O)
