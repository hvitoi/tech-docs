# Concurrency

- It's a technique performed by the OS to run a bit of each process at a time in order to give a sense of parallelism, although everything is run in sequence
- Tasks overlap in time through `interleaving` (time-slicing), but not necessarily running simultaneously
- Allows multitasking even with a single core processor

- A program can be:
  - Concurrent but not parallel (single-core async web server)
  - Parallel but not concurrent (two cores crunching the same giant math problem)
  - Both (multi-core web server handling multiple requests at once)
