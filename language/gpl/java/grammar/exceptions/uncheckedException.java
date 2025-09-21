class Main {
  public static void main(String[] args) {
    throw new MyException("deu ruim");
  }
}

// Unchecked exceptions extends "RuntimeException"
// These kind of exceptions are NOT verified by the compiler
class MyException extends RuntimeException {
  public MyException(String msg) {
    super(msg);
  }
}
