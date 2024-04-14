# Preemption

- It's the act of `temporarily interrupting a task`, with the intention of resuming it at a later time
- This interrupt is done by an `external scheduler` (independent from the task itself)

## External scheduler

- Responsible to define what process will run in a thread at each time
- Interrupts and resumes tasks (context switching)
- Runs in the most privileged `protection ring`

## Context switching

- The changes of the currently running task in a processor (thread)
