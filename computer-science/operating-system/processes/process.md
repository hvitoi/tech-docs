# Process

- It's a particular program while it is being executed and managed by the operating system
- The process can be terminated (or "killed") by you, or by the operating system. At that point, it stops running/being executed, and it can no longer do things.
- There can be multiple processes of the same program running at the same time.

## Workers

- Multiple processes can run within the same application at the same time. Those multiple processes are commonly called `workers`
- Example: a http server that listens on a single port (`manager process`), but then transmits the communication to each `worker process`
- Multiple processes normally `do not share any memory`
