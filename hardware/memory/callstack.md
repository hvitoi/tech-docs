# Call Stack

- It's a memory space dedicated for `functions`
- **Stack frame** is each block pilled in the stack
  - The `stack pointer` points to the last stack frame in the stack.
  - The `frame pointer` of each stack frame points to the stack before (that called it)
- After the function is completed, it's deallocated and freed
- It's different from Heap, that continues to exist until the program is finished
