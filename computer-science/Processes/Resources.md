# Resources

- Hardware Resources
  - Printer
  - Processing unit
  - Memory allocation
  - Disk
- Software Resources
  - A function
  - A global variable

## Flow

1. Process requests a resource and wait
1. Process uses the resource once it's available
1. Process frees the resource for usage by other processes

## Types

- **Preemptive**
  - Resources whose accessing process that can be interrupted without problems
  - E.g., memory: if the process is interrupted, the memory stays reserved for this process to when it's resumed
- **Non-preemptive**
  - Resources whose accessing process that cannot be interrupted without problems
  - E.g., printer: the paper would be stuck in the middle of the impression
