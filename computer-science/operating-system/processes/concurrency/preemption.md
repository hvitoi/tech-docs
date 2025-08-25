# Preemption

- It's the act of `temporarily interrupting a task`, with the intention of resuming it at a later time
- This interruption is done by an `external scheduler` (independent from the task itself)
- Without preemption, one process could hog the CPU until it voluntarily yields (cooperative multitasking).
- With preemption, the OS can interrupt a process and switch to another, ensuring that all processes make progress and concurrency is achieved smoothly.
