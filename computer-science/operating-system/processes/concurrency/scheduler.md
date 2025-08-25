# External scheduler

- Responsible to define what process will run in a thread at each time
- Interrupts and resumes tasks (context switching)
- Runs in the most privileged `protection ring`

## Context switching

- It's the act of saving the state (registers, program counter, etc.) of a running process and loading the saved state of another process so it can run.
- Without saving and restoring states, processes wouldn't resume correctly after being paused.
