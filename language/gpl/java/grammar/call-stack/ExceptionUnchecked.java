class Main {
  public static void main(String[] args) {
    throw new MyException("deu ruim");
  }
}

// unchecked exceptions extends RuntimeException and are not verified by
// the compiler
class MyException extends RuntimeException {
  public MyException(String msg) {
    super(msg);
  }
}
