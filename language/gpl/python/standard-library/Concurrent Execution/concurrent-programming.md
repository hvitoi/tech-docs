# Async programming

- Python supports both `concurrency` and `parallelism`
- <https://docs.python.org/3/library/concurrency.html>

## GIL (Global Interpreter Lock)

- It's a mechanism used in `CPython` (the Python interpreter) to ensure that only one thread can be executed at a time
- While the interpreter is being "used" by a thread, it gets locked so that no other thread can use it at the same time

- With that, the GIL `prevents race conditions` and `prevent memory corruption` when multiple threads access Python objects simultaneously. It also `simplifies memory management` and `simplifies garbage collection`.

- **CPU-bounds tasks**: cannot be run in parallel, because the GIL allows only one thread to execute Python code at a time.
- **I/O-bound tasks**: can be run in parallel, because these tasks go to a separate "queue" while waiting for the response, therefore releasing the lock

- The `multiprocessing` module bypasses the GIL limitations by using separate processes, each with its own interpreter and memory space.

## Modules

### threading (python 1.5+ 1999)

- Uses `threading.Thread`
- Limited by the GIL: not good for CPU-bound tasks, but fine for I/O-bound tasks
- Lightweight compared to processes

- On the OS, it starts only one process with N threads

### multiprocessing (python 2.6+ 2008)

- Uses `multiprocessing.Process`
- Spawns separate Python processes, each with its own GIL
- Therefore, each process can run its own thread: Offers `true parallelism` across CPU cores
- The drawback is the overhead: it has its own interpreter and its own memory space

- On the OS, it starts multiple processes with one or more threads

### concurrent.futures (python 3.2+ 2011)

- High-level API over `threading` and `multiprocessing`
- `ThreadPoolExecutor` — pool of threads, good for I/O-bound tasks (**threading**)
- `ProcessPoolExecutor` — pool of processes, good for CPU-bound tasks (**multiprocessing**)
- Preferred over raw `threading`/`multiprocessing` in most real code — simpler interface, manages the pool lifecycle

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# I/O-bound
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(fetch, url) for url in urls]
    results = [f.result() for f in futures]

# CPU-bound
with ProcessPoolExecutor() as executor:
    results = list(executor.map(cpu_heavy_fn, items))
```

### asyncio (python 3.4+ 2014)

- Uses `async-await` syntax
- Introduces `Coroutines`, which are lightweight "threads" managed by the python runtime (similar to java virtual threads)
- It's the preferred way to implement I/O-bound parallelism
- The threading module is now mostly used for compatibility with libraries that are not async-aware

## When to use what

| Scenario | Recommended |
| --- | --- |
| I/O-bound (network, disk) — async codebase | `asyncio` |
| I/O-bound — sync/legacy codebase | `ThreadPoolExecutor` |
| CPU-bound (computation, data processing) | `ProcessPoolExecutor` |
| Mixed CPU + I/O | `ProcessPoolExecutor` + `asyncio` per process |

## GIL removal (Python 3.13+)

- Python 3.13 introduced an experimental **free-threaded mode** (PEP 703) that can be enabled at build time
- Removes the GIL, allowing true multi-threaded parallelism for CPU-bound tasks without `multiprocessing`
- Still experimental — some C extensions and libraries are not yet compatible
- Run with `python3.13t` (the `t` build) or compile CPython with `--disable-gil`
