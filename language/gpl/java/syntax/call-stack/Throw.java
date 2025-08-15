class Main {
  public static void main(String[] args) {
    // StackOverflowError
    try {
      stackProcess(); // Errors are Throwable
    } catch (Throwable e) {
      System.out.println(e);
    }

    // RuntimeException
    try {
      throw new RuntimeException("Major accident!"); // Exceptions are Throwable
    } catch (Throwable e) { // Throwable, Exception, RuntimeExeception
      System.out.println(e);
    }

  }

  static void stackProcess() {
    stackProcess();
  }
}
