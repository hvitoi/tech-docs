# Async programming

- Python supports both `concurrency` and `parallelism`

## GIL (Global Interpreter Lock)

- It's a mechanism used in `CPython` (the Python interpreter) to ensure that only one thread can be executed at a time
- While the interpreter is being "used" by a thread, it gets locked so that no other thread can use it at the same time

- With that, the GIL `prevents race conditions` when multiple threads access Python objects simultaneously and `simplifies memory management` and `garbage collection`.

- **CPU-bounds tasks**: cannot be run in parallel, because the GIL allows only one thread to execute Python code at a time.
- **I/O-bound tasks**: can be run in parallel, because these tasks go to a separate "queue" while waiting for the response, therefore releasing the lock

- The `multiprocessing` module bypasses the GIL limitations by using separate processes, each with its own interpreter and memory space.

## Modules

### threading

- Uses `threading.Thread`
- Limited by the GIL: not good for CPU-bound tasks, but fine for I/O-bound tasks
- Lightweight compared to processes

### multiprocessing

- Uses `multiprocessing.Process`
- Spawns separate Python processes, each with its own GIL
- Therefore, each process can run its own thread: Offers `true parallelism` across CPU cores

### asyncio
