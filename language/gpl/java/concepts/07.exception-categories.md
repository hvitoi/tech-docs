# Exception categories

- **Throwable**
  - `Exception`
    - _RuntimeException_: unchecked (not verified by compiler)
      - ArithmeticException
      - NullPointerException
    - _DirectlyExtendedException_: checked (must be throwed in the method signature)
  - `Error`
    - _VirtualMachineError_
      - StackOverflowError
