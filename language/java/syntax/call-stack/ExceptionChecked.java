class Main {
  // "Throws" signature only tells that this method might throw an exception (it'a
  // a warning that this method is dangerous)
  public static void main(String[] args) throws Exception {
    // Checked exceptions must be signaziled in the method signature or must be
    // handled in a try-catch block
    throw new MyException("deu ruim");
  }
}

// checked exceptions extends Exception directly and they are verified by the
// compiler
class MyException extends Exception {
  public MyException(String msg) {
    super(msg);
  }
}