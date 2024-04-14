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
  - The resource can be released gracefully by the OS (external scheduler)
  - E.g., memory: if the process is interrupted, the memory stays reserved for this process to when it's resumed
- **Non-preemptive**
  - The resource cannot be released gracefully by the OS (external scheduler)
  - The resource can only be released by the holding process itself
  - E.g., printer: the paper would be stuck in the middle of the impression
