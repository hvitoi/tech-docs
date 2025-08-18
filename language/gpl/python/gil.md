# GIL (Global Interpreter Lock)

- It's a mechanism used in `CPython`, the standard Python interpreter, to ensure that only one thread executes Python bytecode at a time.
- Python objects are not thread-safe by default.
- The GIL `prevents race conditions` when multiple threads access Python objects simultaneously
- It simplifies memory management and garbage collection.

## Implications

- Multithreading in `CPU-bound` tasks doesn't give real parallelism because the GIL allows only one thread to execute Python code at a time.
- `I/O-bound` tasks (file, network, database) are fine with threads because the GIL is released during I/O operations.
- Multiprocessing bypasses the GIL by using separate processes, each with its own interpreter and memory space.
