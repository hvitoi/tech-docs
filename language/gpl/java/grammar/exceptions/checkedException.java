class Main {
  // The "throws" signature tells that this method might throw an exception
  // it's like a warning that this method is dangerous
  public static void main(String[] args) throws Exception {
    // Checked exceptions must either:
    // 1. Be signalized in the method signature (throws signature)
    // 1. Be handled in a try-catch block
    throw new MyException("deu ruim");
  }
}

// Checked exceptions extends "Exception" directly
// These kind of exceptions are verified by the compiler
class MyException extends Exception {
  public MyException(String msg) {
    super(msg);
  }
}
